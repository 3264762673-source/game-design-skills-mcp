# Game Design Skills MCP · v0.2.0

把游戏设计方法变成可调用的能力：**技能文档 + 严格参数 + 执行代码 + 效果示例 + 验收测试**。

包含 8 个技能：体验论策划追问、UI 布局、游戏系统、游戏手感、体验迁移、体验论拆解、影之刃零公开资料手感分析、游戏数值设计。技能目录位于 `game_design_mcp/data/skills/`，可单独复制到支持 SKILL.md 的客户端。公开版移除了本机路径，未包含原书或私人附件。

## 策划：grill-me × 体验论

新增 `game-design-planning`：用决策依赖组织追问，用体验论决定问题内容，最后输出可实施的策划规格。

`范围 → 体验句 → {概念诠释、玩家能动性} → 必要条件 → 行为反馈 → 最小闭环 → 否定实验`

只问前提已解决的问题；概念诠释和能动性可同轮讨论。AI 核查项目事实，用户决定取舍。修改上游回答后，下游答案保留于历史、重新开放，旧确认也失效。未回答完可以交付草案；问答完成不代表体验已验证。

```text
使用 $game-design-planning，结合 grill-me 和体验论审视我的策划。
目标是让玩家读懂强敌，通过自己的应对夺回主动权。
先核查已有方案，再逐轮追问当前可决定的分歧。
最后输出规则、反馈、最小闭环、反例和待测项，不自动制作游戏。
```

[完整虚构策划示例](examples/planning-spec.md) · [技能入口](game_design_mcp/data/skills/game-design-planning/SKILL.md)

调用顺序：

1. `start_design_interview({original_request, session_id})` 返回 session 和当前问题 frontier。
2. `advance_design_interview({session, answers:[{decision_id, answer, basis, locator?}]})` 返回新 session、下一轮问题和失效节点。保存完整返回 session，下一轮传回。
3. `compile_game_design({session})` 返回策划 Markdown 及 draft / awaiting_confirmation / confirmed 状态。先向用户展示规格，再单独调用 advance，传 answers 空数组及 confirm_revision 当前修订号，记录明确共识。不能把推荐答案当成用户回复。

服务不保存会话；调用方负责记录。依赖和状态由代码检查，答案的语义充分性、来源真假仍需 AI 和用户核查。缺少默认核心章节时编译结果保持 draft。ready_for_implementation 只表示当前输入声明的策划共识，实际实现仍受原授权范围约束。无需连接 MCP 也可独立使用技能。

## 安装与运行

需要 Python 3.11+；浏览器演示无需 Python，直接打开 `game_design_mcp/data/runtime/demo.html`。

```sh
python -m venv .venv
# Windows
.venv\Scripts\python -m pip install .
.venv\Scripts\game-design-skills-mcp
# macOS / Linux
.venv/bin/python -m pip install .
.venv/bin/game-design-skills-mcp
```

最后一条命令启动 stdio MCP 服务，等待客户端输入，不是普通交互终端。服务使用官方 MCP Python SDK v1.30.0；不监听公网、不执行 Shell、不写用户文件。

将下列配置合入支持 MCP 的客户端，并换成安装环境中的真实绝对路径：

```json
{"mcpServers":{"game-design":{"command":"/absolute/path/to/.venv/bin/game-design-skills-mcp","args":[]}}}
```

Windows 使用 `C:/absolute/path/.venv/Scripts/game-design-skills-mcp.exe`。这只是通用 MCP 配置示例；各客户端配置位置和格式以其文档为准。项目未自动改写任何客户端设置，未发布到 PyPI。

## 能力契约

| MCP 工具 | 输入 | 输出和可执行能力 | 明确边界 |
|---|---|---|---|
| `list_capabilities` | 无 | 版本、技能及文档白名单 | 不扫描本机其它技能 |
| `get_skill` | skill_id、document | 对应技能正文 | 只读白名单，拒绝路径穿越 |
| `create_effect_bundle` | EffectSpec | 可保存运行的 JS、HTML 与参数 | impact/burst/pulse；Canvas 2D，不含 Unity/UE 适配 |
| `generate_ui_tokens` | UiSpec | 响应式布局、卡片和按钮 CSS | 仅计算实色按钮文字对比，不认证整个页面 |
| `calculate_combat` | CombatSpec | 单次伤害、击数、TTK | 指定减法模型，不推断未知游戏公式 |
| `validate_decision_card` | DecisionCard | 八字段完整性及证据引用检查 | 不判断证据真假，不证明方案好玩 |
| `audit_system` | SystemSpec | 不可达、死路、歧义和未知状态 | 有限确定状态图，不含条件／并发语义 |
| `audit_transfer` | TransferSpec | 部分对应、缺失、未知映射 | 体验是否成功仍需人类判断 |
| `start_design_interview` | 请求与会话 ID | 体验论决策树与当前问题 | 固定起始结构，非自动语义分析 |
| `advance_design_interview` | session、answers、可选确认修订 | 更新问答、依赖与历史 | 不认证发言者或证据真假 |
| `compile_game_design` | session | 策划规格与待决项 | 编译已提供答案，不证明好玩 |

输入 JSON Schema 来自 `game_design_mcp/core.py` 与 `planning.py` 的 Pydantic 模型，并发布为 `schemas/tools.json`。所有规格模型拒绝额外字段和非有限数值；枚举和范围在运行时校验。错误由 MCP 返回，调用方修正输入后再试。

### 调用示例

```json
{"name":"create_effect_bundle","arguments":{"spec":{"effect":"impact","duration_ms":240,"radius_px":36,"particles":12,"color":"#65d6ff","reduced_motion":false}}}
```

保存返回的 `files` 后，将返回的 `config` 传入 `emit`。示例页面提供默认配置和三个效果切换；不会自动读取上一次 MCP 调用参数。

```js
// 普通 script 标签引入 effects.js 后使用；每个实例独占一个透明覆盖 Canvas。
const fx = GameFeedback.createFeedback(canvas);
fx.emit({id:'hit-1',targetId:'enemy-1',kind:'hit.confirmed',confirmed:true,x:120,y:80},
        {effect:'impact',duration_ms:240,radius_px:36,particles:12,color:'#65d6ff',reduced_motion:false});
fx.cancel('enemy-1'); // 目标销毁／取消
fx.clear();          // 暂停或重开，同时清除去重记录
fx.destroy();        // 场景释放
```

坐标为 Canvas 内部像素。宿主负责 DPI、窗口尺寸、目标位置及暂停时调用 clear。实例最多 32 个效果；去重记住最近 1024 个已接受事件，超出后不能依赖此缓存永久去重。系统减弱动态偏好会覆盖关闭减效的配置。减效保留固定位置淡出环，移除扩散和粒子；没有全屏闪烁、镜头写入或全局停帧。运行数值是项目试调起点，不是心理学确定的最佳值。

```json
{"name":"calculate_combat","arguments":{"spec":{"hp":101,"attack":50,"defense":0,"interval_seconds":0.5,"first_hit_seconds":0.2}}}
```

输出 3 次命中、1.2 秒；首击时点明确纳入公式。其他公式、随机暴击、护盾或回复需要另行建模。

## 测试与发布

```sh
python -m unittest discover -s tests -v
node tests/effects.cjs
python -m pip install build
python -m build
```

测试覆盖真实 stdio 初始化及 11 个工具调用、策划依赖/原子性/确认失效/假设边界、越界拒绝、路径穿越、数值击数与首击、图结构、证据状态、对比度、特效去重／容量／生命周期／减效。自动测试不代替真人试玩。CI 在 Linux 与 Windows 运行；发布包包含 Python wheel、源码压缩包和浏览器演示。

## 来源与权利

各技能保留来源和阅读范围。书籍、论文、视频及游戏名称属于原作者或权利人；没有复制它们的完整内容或游戏资产。特效运行时和能力实现是本项目新增代码，不是原游戏源码。

本版本尚未选择统一开源许可证；公开仓库不等于授权所有内容无条件再分发。使用第三方依赖时遵循其许可证。不要把企业内部项目或新的原始资料直接放入公开技能目录。

## 当前版本的边界

这是一套可运行的基础能力包。8 个技能均可被发现、读取；其中一部分步骤已由确定性工具支撑，创意分析仍由调用模型完成。不是“每个技能自动生成完整游戏”，也未宣称所有设计判断可机器验证。后续可扩展 Unity／UE 事件适配、声音与镜头仲裁、更丰富的 UI 组件以及真实项目回归案例。

发布维护：修改源码后运行 `python scripts/update_metadata.py` 更新 Schema 与清单。测试、构建、提交并创建版本标签后，运行 `python scripts/package_release.py` 生成发布 ZIP 与版本独立校验和。v0.2.0 新增策划能力，三种效果的运行时仍为 0.1.0。
