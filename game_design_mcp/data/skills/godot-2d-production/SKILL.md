---
name: godot-2d-production
description: 在 Godot 4 项目中实现像素资产、角色动作、物品动效、特效和 UI；按任务核对版本、状态权威与生命周期。
---

# Godot 2D 制作与动效

先读取现有项目与目标任务，沿用已确认约束。区分源像素、显示尺寸和引擎坐标，不预设固定网格、色数或帧数。先检查规则的触发条件与反例，再做最小修改；保留前后版本，退化时回退。

交付可制作规格或实际资产，并注明工具/运行条件。截图只支持静态观察；行为、时序和体验效果需要实际检查。案例支持、工程提案与项目实测分别记录。

## 只读当前分支

- 特效动效：[规则与交付](references/vfx.md)。
- 人物动作：[规则与交付](references/character-animation.md)。
- 物品动效：[规则与交付](references/item-animation.md)。

规则卡仍保留触发、解释、检查、修改、例外、预期、撤回及证据状态八字段。需要追溯时读 [来源与案例](references/evidence.md)，不要为普通任务加载完整研究史。

## 引擎任务

先确认 Godot 4 的具体小版本与平台。再读以下一个相关模块；美术/动作规则与节点实现分别判断。

- 项目与验证：[实现检查](references/project.md)。
- 像素资产接入：[实现检查](references/assets.md)。
- 场景/脚本/物理/输入：[实现检查](references/scene-input.md)。
- 动画与动效：[实现检查](references/animation.md)。
- UI 实现：[实现检查](references/ui.md)。
- 导出交付：[实现检查](references/export.md)。

不执行附件安装脚本。先实现最小场景再扩展；只报告实际完成的导入、脚本检查、运行或导出。包内方法不等于已连接 Godot 编辑器。

## MCP 按需读取

可调用 `list_design_topics` 找主题，再调用 `get_design_guidance(topic, stage)` 读取 rules、implementation 或 evidence。未连接 MCP 时直接读上面的文件，本技能可独立使用。
