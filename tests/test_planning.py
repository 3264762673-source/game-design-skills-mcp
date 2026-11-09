import json
import unittest
from pathlib import Path
from pydantic import ValidationError
from game_design_mcp.planning import (
    DesignSession, DesignAnswer, Decision, start_design_interview,
    frontier, advance_design_interview, compile_game_design,
)

def answer(session, key, value='用户已选择当前方案', basis='user'):
    result=advance_design_interview(session,[DesignAnswer(decision_id=key,answer=value,basis=basis)])
    return DesignSession.model_validate(result['session'])

def resolved_session():
    s=start_design_interview('让玩家读懂强敌，通过应对夺回主动权')
    for key in ['scope','experience','meaning','agency','conditions','feedback','loop','experiment']:
        s=answer(s,key)
    return s

class PlanningTests(unittest.TestCase):
    def test_frontier_waits_for_prerequisites(self):
        s=start_design_interview('目标体验')
        self.assertEqual([n['id'] for n in frontier(s)['questions']],['scope'])
        with self.assertRaises(ValueError): answer(s,'loop')
        s=answer(answer(s,'scope'),'experience')
        self.assertEqual([n['id'] for n in frontier(s)['questions']],['meaning','agency'])

    def test_round_atomicity(self):
        s=start_design_interview('目标体验')
        with self.assertRaises(ValueError):
            advance_design_interview(s,[DesignAnswer(decision_id=k,answer='x',basis='user') for k in ['scope','experience']])
        self.assertEqual(s.revision,1)
        self.assertTrue(all(n.status=='open' for n in s.decisions))
        s=answer(answer(s,'scope'),'experience')
        r=advance_design_interview(s,[DesignAnswer(decision_id=k,answer='x',basis='user') for k in ['meaning','agency']])
        self.assertEqual([n['id'] for n in r['frontier']['questions']],['conditions'])

    def test_parent_revision_invalidates_only_descendants(self):
        s=resolved_session()
        s=DesignSession.model_validate(advance_design_interview(s,[],s.revision)['session'])
        r=advance_design_interview(s,[DesignAnswer(decision_id='meaning',answer='更改概念含义',basis='user')])
        new=DesignSession.model_validate(r['session'])
        self.assertEqual(r['invalidated'],['conditions','experiment','feedback','loop'])
        self.assertIsNone(new.confirmed_revision)
        self.assertEqual(next(n for n in new.decisions if n.id=='agency').status,'resolved')
        self.assertEqual(compile_game_design(new)['status'],'draft')
        old_loop=next(c.previous for c in new.history if c.revision==new.revision and c.decision_id=='loop')
        self.assertEqual(old_loop.status,'resolved')
        self.assertEqual(s.confirmed_revision,s.revision)  # input remains unchanged

    def test_explicit_current_confirmation(self):
        s=resolved_session()
        self.assertEqual(compile_game_design(s)['status'],'awaiting_confirmation')
        with self.assertRaises(ValueError): advance_design_interview(s,[],s.revision-1)
        with self.assertRaises(ValueError): advance_design_interview(s,[DesignAnswer(decision_id='scope',answer='x',basis='user')],s.revision)
        s=DesignSession.model_validate(advance_design_interview(s,[],s.revision)['session'])
        output=compile_game_design(s)
        self.assertTrue(output['ready_for_implementation'])
        self.assertEqual(output['experience_status'],'untested')

    def test_hypotheses_do_not_become_consensus(self):
        s=answer(start_design_interview('目标'),'scope',basis='hypothesis')
        self.assertEqual(frontier(s)['questions'],[])
        self.assertEqual(frontier(s)['assumptions'],['scope'])
        s=DesignSession.model_validate({**s.model_dump(),'explore_assumptions':True})
        self.assertEqual([n['id'] for n in frontier(s)['questions']],['experience'])
        with self.assertRaises(ValidationError):answer(s,'experience',basis='user')
        s=answer(s,'experience',basis='hypothesis')
        self.assertEqual(compile_game_design(s)['status'],'draft')
        with self.assertRaises(ValueError):advance_design_interview(s,[],s.revision)

    def test_graph_and_input_rejections(self):
        s=start_design_interview('目标')
        for dep in ['missing','scope','experiment']:
            data=s.model_dump();data['decisions'][0]['depends_on']=[dep]
            with self.assertRaises(ValidationError):DesignSession.model_validate(data)
        data=s.model_dump();data['decisions'].append(data['decisions'][0])
        with self.assertRaises(ValidationError):DesignSession.model_validate(data)
        with self.assertRaises(ValidationError):start_design_interview('  ')
        with self.assertRaises(ValidationError):DesignAnswer(decision_id='scope',answer='\n',basis='user')
        with self.assertRaises(ValidationError):answer(s,'scope',basis='project_evidence')
        with self.assertRaises(ValueError):answer(s,'unknown')
        with self.assertRaises(ValueError):advance_design_interview(s,[])

    def test_missing_sections_stay_draft(self):
        s=DesignSession(session_id='tiny',original_request='草案',decisions=[Decision(id='scope',topic='范围',question='?',recommendation='x',answer='x',basis='user',status='resolved')],confirmed_revision=1)
        self.assertFalse(compile_game_design(s)['ready_for_implementation'])
        self.assertIn('experience',compile_game_design(s)['missing_sections'])

    def test_saved_example_is_only_candidate(self):
        p=Path(__file__).parents[1]/'game_design_mcp/data/skills/game-design-planning/assets/example-session.json'
        s=DesignSession.model_validate(json.loads(p.read_text(encoding='utf-8')))
        output=compile_game_design(s)
        self.assertEqual(output['status'],'awaiting_confirmation')
        self.assertEqual(output['experience_status'],'untested')
        self.assertIn('概念诠释',output['markdown'])
