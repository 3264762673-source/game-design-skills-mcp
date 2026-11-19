---
name: pixel-ui-design
description: 设计像素游戏的布局、图标按钮及页面交互，统一视觉与状态规格；Godot 节点实现另读制作技能。
---

# 像素 UI

先读取现有项目与目标任务，沿用已确认约束。区分源像素、显示尺寸和引擎坐标，不预设固定网格、色数或帧数。先检查规则的触发条件与反例，再做最小修改；保留前后版本，退化时回退。

交付可制作规格或实际资产，并注明工具/运行条件。截图只支持静态观察；行为、时序和体验效果需要实际检查。案例支持、工程提案与项目实测分别记录。

## 只读当前分支

- 布局与尺度：[规则与交付](references/ui-layout.md)。
- 图标按钮：[规则与交付](references/icon-art.md)。
- 状态与导航：[规则与交付](references/ui-interaction.md)。

规则卡仍保留触发、解释、检查、修改、例外、预期、撤回及证据状态八字段。需要追溯时读 [来源与案例](references/evidence.md)，不要为普通任务加载完整研究史。

## MCP 按需读取

可调用 `list_design_topics` 找主题，再调用 `get_design_guidance(topic, stage)` 读取 rules、implementation 或 evidence。未连接 MCP 时直接读上面的文件，本技能可独立使用。
