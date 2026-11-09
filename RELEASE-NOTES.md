# v0.1.0

首个可执行版本：7 个技能快照，8 个 MCP 工具，3 个 Canvas 反馈效果。

## 使用

- 下载 wheel 后执行 `python -m pip install <wheel文件路径>`。
- 将 `game-design-skills-mcp` 可执行文件的绝对路径添加到 MCP 客户端配置。
- 浏览器效果包解压后直接打开 demo.html，无需安装服务器。
- 阅读仓库 README 和 schemas/tools.json 获取调用契约。

## 验证范围

- Python 单元测试及真实 stdio MCP 会话：初始化、8 个工具的有效调用及错误参数处理。
- JavaScript：事件确认、去重、并发容量、生命周期、减效及销毁。
- 浏览器：确认命中与挥空的状态响应。
- wheel 与源码构建。

本版未做真人体验实验；不提供 Unity/UE 插件、音效或全局镜头。不将设计卡校验或体验映射完整性当成实际好玩的证明。
