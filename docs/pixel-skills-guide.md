# 九个像素游戏技能怎么用

先选择眼前要解决的问题。一次跨领域任务可以按资产依赖顺序组合多个技能；一个小问题通常只需其中一个。

| 序号 | 技能 | 主要交付 |
|---|---|---|
| 1 | [pixel-character-art](../game_design_mcp/data/skills/pixel-character-art/SKILL.md) | 人物轮廓、色块、身份与方向规格 |
| 2 | [pixel-environment-art](../game_design_mcp/data/skills/pixel-environment-art/SKILL.md) | 场景层次、地块连接、遮挡与行动线索 |
| 3 | [pixel-item-art](../game_design_mcp/data/skills/pixel-item-art/SKILL.md) | 道具家族、用途差异、状态与世界／槽位表现 |
| 4 | [pixel-ui-layout](../game_design_mcp/data/skills/pixel-ui-layout/SKILL.md) | HUD／页面布局、字体、尺度与适配约束 |
| 5 | [pixel-icon-button-art](../game_design_mcp/data/skills/pixel-icon-button-art/SKILL.md) | 图标语义、按钮状态、视觉与输入边界 |
| 6 | [pixel-ui-interaction](../game_design_mcp/data/skills/pixel-ui-interaction/SKILL.md) | 页面状态、导航、确认／取消和失败恢复 |
| 7 | [pixel-vfx-motion](../game_design_mcp/data/skills/pixel-vfx-motion/SKILL.md) | 特效阶段、事件契约、并发与减效规格 |
| 8 | [pixel-character-animation](../game_design_mcp/data/skills/pixel-character-animation/SKILL.md) | 姿态、接触、动作衔接与中断规则 |
| 9 | [pixel-item-animation](../game_design_mcp/data/skills/pixel-item-animation/SKILL.md) | 掉落／拾取／开启／使用动效与结算同步 |

## 给 AI 的调用方式

独立安装后，可以输入：

```text
使用 $pixel-item-animation。
对象是一个可开启的宝箱和三种掉落物，采用俯视角像素画面。
已有规则：背包满时不能拾取，开箱只结算一次。
先读当前项目，再给出生命周期、关键画面和确认事件的对应表。
检查重复拾取、容量满、开箱中途离开和减效模式。
引用适用规则，区分已观察、工程推断和待运行验证。
```

缺少尺寸或工具时，AI 应读取已有项目；没有现成约束则说明工作假设。不要把上述例子的类型和规则套到所有游戏。

通过 MCP 调用时，先用 `list_capabilities` 查看技能及文档白名单，再调用：

```json
{"name":"get_skill","arguments":{"skill_id":"pixel-item-animation","document":"SKILL.md"}}
{"name":"get_skill","arguments":{"skill_id":"pixel-item-animation","document":"references/rules.md"}}
{"name":"get_skill","arguments":{"skill_id":"pixel-item-animation","document":"references/evidence.md"}}
```

这些调用返回文档，由 AI 执行其中与当前任务有关的步骤。现有 `validate_decision_card` 只检查结构与证据字段；`audit_system` 只检查它支持的有限状态图，不证明物品已正确结算或视觉体验成功。

## 给人的制作顺序

1. 写一句具体任务，例如“战斗中分清敌我”和“拾取后知道物品去了哪里”。
2. 固定本次比较的相机、显示尺寸、内容和输入方式。优先记录真实项目约束。
3. 找到对应规则的触发条件，检查是否存在其他解释。比如看不见物品，可能是布局、遮挡、状态未确认或物品本身难辨。
4. 每次改变一个主要因素，保留前后版本。看实际游戏画面，再放大检查像素。
5. 用同任务的另一种背景、状态或物品检查迁移；记录失败场景。无法测的内容标为待测。

人物造型与人物动作共享识别锚点；物品美术与物品动效共享状态；布局、图标与交互共享焦点和控件语义。交接时传递具体规格，不只传“复古”“有冲击力”等形容词。

## 读懂检验结果

规则卡保留触发条件、候选解释、检查方法、可执行修改、不适用情况、预期变化、验证与撤回、来源与状态八个字段。跨作品有限支持表示在记录的案例与条件中相容；不是“所有游戏都适用”，也不是“已证明提高某个百分比”。

本批研究采用图文、作者说明、公开源码和论文。论文的算法实验与艺术规则的玩家效果分开记录；视频简介、搜索摘要、未核实的点赞／收藏不升级为实测证据。见 [研究约定](pixel-research-method.md) 和 [研究索引](research/pixel-research-index.md)。
