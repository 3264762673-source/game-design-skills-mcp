"""Regenerate public schemas and skill checksums from the release sources."""
from pathlib import Path
import asyncio
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from game_design_mcp import __version__
from game_design_mcp.server import mcp
from game_design_mcp.planning import DesignSession, compile_game_design

def main():
    schemas = asyncio.run(mcp.list_tools())
    (ROOT/'schemas/tools.json').write_text(json.dumps([t.model_dump(mode='json') for t in schemas], ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    folder = ROOT/'game_design_mcp/data/skills'
    files = [p for p in sorted(folder.rglob('*')) if p.is_file()]
    manifest = {'version':__version__, 'skills':sorted(p.name for p in folder.iterdir() if p.is_dir()),
                'files':[{'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],
                'policy':'Skill instructions only; original books, private attachments, credentials and machine paths excluded'}
    (ROOT/'skill-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    example = folder/'game-design-planning/assets/example-session.json'
    session = DesignSession.model_validate(json.loads(example.read_text(encoding='utf-8')))
    (ROOT/'examples').mkdir(exist_ok=True)
    (ROOT/'examples/planning-spec.md').write_text(compile_game_design(session)['markdown']+'\n',encoding='utf-8')
    print(f'Updated {len(schemas)} schemas and {len(manifest["skills"])} skill entries')

if __name__ == '__main__': main()
