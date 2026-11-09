import hashlib
from pathlib import Path
import tempfile
import unittest
import zipfile

from scripts.package_release import check_skill_hashes


class ReleaseTests(unittest.TestCase):
    def test_archive_manifest_checks_actual_bytes_and_paths(self):
        expected = b'example\n'
        entries = [{'path': 'game_design_mcp/data/skills/example/SKILL.md',
                    'sha256': hashlib.sha256(expected).hexdigest()}]
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / 'skills.zip'
            for payload, accepted in [(expected, True), (b'example\r\n', False), (b'changed\n', False)]:
                with zipfile.ZipFile(archive, 'w') as z:
                    z.writestr('example/SKILL.md', payload)
                if accepted:
                    check_skill_hashes(archive, entries, 'game_design_mcp/data/skills/')
                else:
                    with self.assertRaises(RuntimeError):
                        check_skill_hashes(archive, entries, 'game_design_mcp/data/skills/')
            with zipfile.ZipFile(archive, 'w') as z:
                z.writestr('wrong/SKILL.md', expected)
            with self.assertRaises(RuntimeError):
                check_skill_hashes(archive, entries, 'game_design_mcp/data/skills/')
