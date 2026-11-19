import unittest
from typing import get_args
from game_design_mcp import core, guidance


class GuidanceTests(unittest.TestCase):
    def test_all_routes_return_exact_single_document(self):
        topics = guidance.list_topics()['topics']
        self.assertEqual(len(topics), 15)
        self.assertEqual({t['topic'] for t in topics}, set(get_args(guidance.Topic)))
        self.assertEqual(len(core.list_skills()), 11)
        for topic in topics:
            for stage in get_args(guidance.Stage):
                result = guidance.get_guidance(topic['topic'], stage)
                self.assertEqual(result['content'], core.read_skill(result['skill_id'], result['document']))
                self.assertTrue(result['content'].strip())

    def test_legacy_document_compatibility_and_allowlist(self):
        aliases = guidance.catalog()['legacy_aliases']
        self.assertEqual(len(aliases), 9)
        for old, alias in aliases.items():
            for document, target in alias['documents'].items():
                self.assertEqual(core.read_skill(old, document), core.read_skill(alias['skill_id'], target))
            for unsafe in ['../SKILL.md', 'references/../../secret', 'unknown.md']:
                with self.assertRaises(ValueError): core.read_skill(old, unsafe)

    def test_invalid_route_rejected(self):
        for topic, stage in [('../secret', 'rules'), ('vfx', '../secret'), ('vfx', '')]:
            with self.assertRaises(ValueError): guidance.get_guidance(topic, stage)

    def test_original_rule_cards_preserved(self):
        aliases = guidance.catalog()['legacy_aliases']
        fields = ['触发条件', '候选解释', '检查方法', '可执行修改', '不适用情况', '预期变化', '验证与撤回', '来源与状态']
        for old in aliases:
            content = core.read_skill(old, 'references/rules.md')
            for field in fields:
                self.assertEqual(content.count(field), 3, (old, field))
