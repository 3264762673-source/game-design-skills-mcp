# 引擎来源与审阅范围

日期：2026-11-20。用户提供 GodoMaster-1.1.1.zip，项目归属 yanha/GodoMaster。包内主技能版本字段仍为 1.1.0；这里以附件文件名和哈希定位，不将内部字段当已核验发行版本。

读取主入口、README、2D、动画、UI、导出正文，并检查项目/脚本/物理/输入/着色器/测试/架构模块结构。18 个参考模块在 .claude 技能目录和 CLI assets 中逐字重复。没有运行 install.sh、npm CLI 或附件代码。

本版采用问题导向的原创摘要，不重打包原文件或整段示例。README 声明 MIT，但附件没有独立 LICENSE 文件；来源归属保留，不据此为本仓库补写统一许可。

## 修订原因

- 原入口重复声明继承节点的 velocity，且 speed/gravity/jump_velocity 未在示例中完整定义；改为要求核对所属节点和依赖，不复制不完整代码。
- 原 2D 示例 local_to_map(global_position) 混淆坐标空间；明确先转换到该 TileMapLayer 的本地坐标。
- 取消“每个对象都配 AnimationPlayer/AnimationTree、所有动作都补平滑过渡”的清单，改为按资产和行为选择工具。
- 原动画范例的每帧 walk/idle 选择可能覆盖攻击状态；补进入/保持/中断和唯一属性写入者检查。
- UI、相机、Sprite 中重复的 Tween 配方归入一份动画实现模块；命中/拾取的结算与装饰动画分离。

## 官方核查入口

- [CharacterBody2D](https://docs.godotengine.org/en/stable/classes/class_characterbody2d.html)：velocity 与角色移动职责。
- [TileMapLayer](https://docs.godotengine.org/en/stable/classes/class_tilemaplayer.html)：分层和 local_to_map 的坐标契约。
- [Tween](https://docs.godotengine.org/en/stable/classes/class_tween.html)：创建、属性竞争、kill 和复用边界。
- [AnimationTree](https://docs.godotengine.org/en/stable/tutorials/animation/animation_tree.html)：与 AnimationPlayer 的关系。
- [2D sprite animation](https://docs.godotengine.org/en/stable/tutorials/2d/2d_sprite_animation.html)：SpriteFrames 与序列播放。
- [UI focus](https://docs.godotengine.org/en/stable/tutorials/ui/gui_navigation.html)：焦点、隐藏和导航。
- [InputEvent](https://docs.godotengine.org/en/stable/tutorials/inputs/inputevent.html)：输入分派与 GUI 拦截。
- [Exporting projects](https://docs.godotengine.org/en/stable/tutorials/export/exporting_projects.html)：预设、模板及平台依赖。

已核查这些文档相关正文；未执行 Godot 引擎或目标设备测试。stable 链接会变化，实施时按实际引擎小版本选择对应文档。保留原像素案例的待测项。
