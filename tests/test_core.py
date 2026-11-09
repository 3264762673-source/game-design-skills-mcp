import unittest
from pydantic import ValidationError
from game_design_mcp.core import *

class CoreTests(unittest.TestCase):
    def test_ttk_first_hit_and_ceiling(self):
        r=combat(CombatSpec(hp=101,attack=50,interval_seconds=.5,first_hit_seconds=.2))
        self.assertEqual(r['hits'],3);self.assertAlmostEqual(r['ttk_seconds'],1.2)
        self.assertEqual(combat(CombatSpec(hp=1,attack=50))['ttk_seconds'],0)
    def test_invalid_numeric_and_extra(self):
        for args in [dict(hp=1,attack=0),dict(hp=float('nan'),attack=1),dict(hp=1,attack=1,hack=1)]:
            with self.assertRaises(ValidationError): CombatSpec(**args)
    def test_paths(self):
        for s in list_skills(): self.assertIn('name:',read_skill(s['id']))
        with self.assertRaises(ValueError):read_skill('../', '../../pyproject.toml')
    def test_graph(self):
        r=audit_system(SystemSpec(initial='a',states=['a','b','c'],transitions=[Transition(source='a',action='go',target='b',feedback='arrived')]))
        self.assertEqual(r['unreachable'],['c']);self.assertEqual(r['dead_ends'],['b'])
    def test_card_evidence(self):
        c=DecisionCard(trigger='x',hypotheses=['x'],check='x',change='x',exclusions='x',expected='x',rollback='x',sources=['S01'],status='compared')
        self.assertFalse(validate_card(c)['valid'])
    def test_effect_bundle(self):
        self.assertIn('createFeedback',effect_bundle(EffectSpec())['files']['effects.js'])
        with self.assertRaises(ValidationError):EffectSpec(particles=49)
    def test_ui(self):
        for color in ['#ffffff','#000000','#777777','#2563eb']:
            self.assertGreaterEqual(ui_tokens(UiSpec(accent=color))['button_text_contrast'],4.5)
        with self.assertRaises(ValidationError):UiSpec(accent='red; } body {')
    def test_transfer_never_certifies_fun(self):
        r=audit_transfer(TransferSpec(pleasure='mastery',mappings=[Mapping(condition='learn',action='act',feedback='result',status='mapped')]))
        self.assertTrue(r['structurally_complete']);self.assertEqual(r['experience_status'],'unvalidated')

if __name__=='__main__':unittest.main()
