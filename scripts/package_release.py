"""Package the committed tag and exact built artifacts without changing Git state."""
from pathlib import Path
import hashlib
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from game_design_mcp import __version__ as version

def main():
    if subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],cwd=ROOT).strip():
        raise RuntimeError('Commit tracked changes before packaging')
    tag = subprocess.check_output(['git','rev-parse',f'v{version}^{{commit}}'],cwd=ROOT).strip()
    head = subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).strip()
    if tag != head: raise RuntimeError('Release tag must refer to HEAD')
    dist = ROOT/'dist'
    artifacts = [dist/f'game_design_skills_mcp-{version}-py3-none-any.whl',dist/f'game_design_skills_mcp-{version}.tar.gz']
    for p in artifacts:
        if not p.exists(): raise RuntimeError('Build wheel and sdist first')
    for name, folder in [('browser-effects','runtime'),('skills','skills')]:
        path=dist/f'{name}-{version}.zip'
        base=ROOT/'game_design_mcp/data'/folder
        with zipfile.ZipFile(path,'w',zipfile.ZIP_DEFLATED) as z:
            for p in sorted(base.rglob('*')):
                if p.is_file():z.write(p,p.relative_to(base).as_posix())
        artifacts.append(path)
    source = dist/f'game-design-skills-mcp-{version}.zip'
    subprocess.run(['git','archive','--format=zip','--output='+str(source),f'v{version}'],cwd=ROOT,check=True)
    artifacts.append(source)
    # Version-specific checksums avoid overwriting historical release sums.
    sums=dist/f'SHA256SUMS-{version}.txt'
    sums.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in artifacts),encoding='utf-8')
    for p in artifacts+[sums]:print(p.name)

if __name__=='__main__':main()
