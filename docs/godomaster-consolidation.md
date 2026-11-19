# v0.4.0：精简与 Godot 接入

九个像素 Skill 合并为三个入口；原有八个其他设计技能保留，当前共 11 个。重复入口共用的工作流程不再复制，27 张八字段规则卡保留，来源在组内归并。Godot 模块是面向 2D 的原创摘要，不是 GodoMaster 全量镜像。

| 旧入口 | 新入口 | 主题 |
|---|---|---|
| pixel-character-art | pixel-art-direction | references/character-art.md |
| pixel-environment-art | pixel-art-direction | references/environment-art.md |
| pixel-item-art | pixel-art-direction | references/item-art.md |
| pixel-ui-layout | pixel-ui-design | references/ui-layout.md |
| pixel-icon-button-art | pixel-ui-design | references/icon-art.md |
| pixel-ui-interaction | pixel-ui-design | references/ui-interaction.md |
| pixel-vfx-motion | godot-2d-production | references/vfx.md |
| pixel-character-animation | godot-2d-production | references/character-animation.md |
| pixel-item-animation | godot-2d-production | references/item-animation.md |

旧九入口字符数 9683，新三个入口字符数 2303（含新增引擎路由）。字符数用于比较加载规模，不等于模型 token 数。详细规则和研究史按需读取。

## MCP

`list_design_topics()` 返回 15 个主题和可用阶段。`get_design_guidance(topic, stage)` 只读一项：rules 读规则，implementation 读 Godot 实现检查，evidence 读证据。所有主题/阶段有枚举约束；不执行 Shell、不写项目、不连接 Godot 编辑器。

旧 get_skill 的九个 ID 保留白名单兼容映射；SKILL.md/agents 元数据映射到新的组入口，rules/evidence 映射到对应资料。list_capabilities 只列新入口并另列兼容表。文件夹安装用户应移除旧九个目录再装新三个，避免重复发现；历史发布仍保留旧版。

## 来源与范围

附件 SHA256：b9252ba201d5ba6bf1e01b89b75dfcd95d431e216302743a3e4278c432a76752。

GodoMaster 中两套技能文件完全相同；不运行安装脚本。原作者为 yanha，原项目 https://github.com/yanha/GodoMaster 。读取范围和具体纠正见 [引擎来源](../game_design_mcp/data/skills/godot-2d-production/references/engine-sources.md)。3D、联网和编辑器插件未纳入本次 2D 精简范围。未声称 Godot 引擎实测通过。
