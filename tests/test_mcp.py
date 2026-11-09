import unittest,sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class ProtocolTests(unittest.IsolatedAsyncioTestCase):
    async def test_real_stdio(self):
        async with stdio_client(StdioServerParameters(command=sys.executable,args=['-m','game_design_mcp.server'])) as (r,w):
            async with ClientSession(r,w) as client:
                await client.initialize()
                listed=await client.list_tools()
                self.assertEqual(len(listed.tools),8)
                result=await client.call_tool('calculate_combat',{'spec':{'hp':100,'attack':30}})
                self.assertFalse(result.isError)
                bad=await client.call_tool('create_effect_bundle',{'spec':{'particles':999}})
                self.assertTrue(bad.isError)
                traversal=await client.call_tool('get_skill',{'skill_id':'../','document':'README.md'})
                self.assertTrue(traversal.isError)
                for name,args in [('list_capabilities',{}),('create_effect_bundle',{'spec':{}}),('generate_ui_tokens',{'spec':{}})]:
                    self.assertFalse((await client.call_tool(name,args)).isError)
                valid=[('get_skill',{'skill_id':'ui-layout-design'}),
                       ('audit_system',{'spec':{'initial':'done','states':['done'],'terminal':['done'],'transitions':[]}}),
                       ('audit_transfer',{'spec':{'pleasure':'mastery','mappings':[{'condition':'learn','action':'act','feedback':'result','status':'mapped'}]}}),
                       ('validate_decision_card',{'card':{'trigger':'x','hypotheses':['x'],'check':'x','change':'x','exclusions':'x','expected':'x','rollback':'x','sources':['S01']}})]
                for name,args in valid:self.assertFalse((await client.call_tool(name,args)).isError)
