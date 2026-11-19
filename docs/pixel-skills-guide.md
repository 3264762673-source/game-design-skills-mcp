# 像素游戏技能怎么用

先确定当前需要决定的事情，然后只读对应主题。

| 新入口 | MCP 主题 |
|---|---|
| pixel-art-direction | character-art、environment-art、item-art |
| pixel-ui-design | ui-layout、icon-art、ui-interaction |
| godot-2d-production | vfx、character-animation、item-animation、godot-project、godot-assets、godot-scene-input、godot-animation、godot-ui、godot-export |

## 给 AI

独立安装后，可说：使用 `$godot-2d-production`，为一个宝箱制作开启动效；背包满时不能拾取，开箱只结算一次。先检查当前项目，再给出动作阶段与结算事件的对应关系。

连接 MCP 后，先 `list_design_topics()`，再 `get_design_guidance("item-animation", "rules")`。要落地节点和动画时读取 implementation，要核查来源时读取 evidence。不要默认加载所有文档。

## 给人类

先写清任务、视角、显示尺度与当前问题。规则卡提供候选解释和检查方法；先检查，再做最小修改。用相同场景比较前后结果，记录反例和撤回条件。案例相容不代表实际玩家测试通过。

## 从 v0.3.0 升级

备份旧文件后，用三个新入口替换九个旧 pixel-* 目录，避免重复发现。其他八个技能保持不变。旧 MCP get_skill 的九个 ID 及原四种文档路径仍有效；新入口的真实文件路径以 list_capabilities 为准。

详细映射见 [合并说明](godomaster-consolidation.md)。原研究报告保留历史主题名称，不代表仍存在同名独立安装目录。
