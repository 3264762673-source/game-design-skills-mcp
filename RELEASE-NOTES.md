# v0.2.0 · grill-me × 体验论策划

新增 game-design-planning，将决策依赖追问、概念诠释、玩家能动性、行为反馈及反例检查编译为策划规格。

- 8 个 Skills，11 个 MCP 工具；保留原有接口和 3 种 Canvas 效果。
- 新工具：start_design_interview、advance_design_interview、compile_game_design。
- 修改上游答案后，重新开放下游，保留历史并使旧确认失效。
- 草案、待确认和已确认分开；假设不是共识，未试玩仍为待测。
- 包含完整虚构示例、Schema、测试及发布脚本。

## 使用

Python 3.11+ 安装本版 wheel，再启动 game-design-skills-mcp；客户端配置见 README。
独立技能下载 skills-0.2.0.zip，将 game-design-planning 文件夹复制到客户端技能目录。
先调用 start_design_interview，保存 session，通过 advance_design_interview 更新，再用 compile_game_design 输出规格。

## 验证边界

自动测试覆盖真实 stdio、全部工具、依赖及状态约束。服务按输入生成问题结构、编译答案，不认证其来源、不验证自然语言语义，不替代设计判断或真人试玩。

## 兼容性

新增接口，旧调用方式不变。create_effect_bundle 的 version 表示包版本，新增 effect_runtime_version 标明未改动的 0.1.0 运行时。没有改写 v0.1.0 标签或发布附件。
