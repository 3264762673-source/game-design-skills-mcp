# 动效研究的检验前候选快照

本节先写入文件，再搜索/阅读检验作品 Noita。推导组：Dead Cells（Motion Twin）、Celeste / Celeste Classic（同一制作谱系，只计一组）、Shovel Knight / Dig（Yacht Club Games 与 Nitrome 制作谱系，不假称两个独立团队）。Noita 此时未纳入推导；后文记录保留/收窄/撤回。

### 特效初版

- F1：先标记输入、动作生效、命中与状态结束，再将特效绑定到相应事件；不能靠视觉播放结束推断玩法结果。
- F2：威胁、角色和结果确认优先；拥挤时减掉装饰粒子/全屏强调，并检查减效模式的信息完整性。
- F3：先做主要形状与起落阶段，再考虑补帧、细碎粒子和混合；手绘像素、3D 转像素可以采用不同管线。

### 人物动作初版

- A1：先做可辨认的关键姿态并匹配动作功能，再加中间帧；不把更多帧视为更好。
- A2：动画状态服从明确的玩法状态、进入/退出与中断规则；移动、跳跃、受击、拾取的混合需逐项检查。
- A3：检查角色轮廓、接地点、朝向和握持锚点；允许程序缩放与混合渲染，但输出须在目标画面检查。

### 物品动效初版

- I1：用物品生命周期规定等待、掉落、可拾取、尝试拾取、结算、消失；展示不是入账依据。
- I2：按功能区分悬浮/就绪、开启、拒绝、使用/装备；切换与取消后的视觉必须回到真实状态。
- I3：动态位移与实际拾取区域、实体物理分开声明；装饰动效不能无意改变可达性，也不能将真实危险物误归类为装饰。

阶段 A 已读主来源：

- Thomas Vasseur（2018），[Dead Cells 3D-to-2D pipeline](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)；正文。作者说明关键姿态先行、修订时序、3D低分辨率输出与残留像素闪烁的取舍。不是本文亲自测量游戏结果。
- Noel Berry / Maddy Thorson，[Celeste Classic C# port](https://github.com/NoelFB/Celeste/blob/1b0ce45c75e05649ae91b44a8bb6b196684e4352/Source/PICO-8/Classic.cs)；读取 `fruit`、`fly_fruit`、`balloon`、`chest` 等代码。代码开头声明它是尽量按 Lua 移植，不是推荐的通用 C# 架构。
- Noel Berry 等，[Celeste Player](https://github.com/NoelFB/Celeste/blob/1b0ce45c75e05649ae91b44a8bb6b196684e4352/Source/Player/Player.cs)；读取 `UpdateSprite`、`Throw`、`Drop`、状态相关片段；没有把 Classic 和完整 Celeste 的数据混用。
- Yacht Club Games，[Breaking the NES](https://www.yachtclubgames.com/blog/breaking-the-nes/)；正文。开发者明确按玩法和清晰度选择保留或打破历史限制。
- Yacht Club Games，[官方更新记录](https://old.yachtclubgames.com/update-notes/)；读取与拾取、开箱、显示、转场和全屏效果选项有关的条目。补丁是发生过故障的证据，不代表当前版本仍存在。
- Phil Giarrusso，[Shovel Knight Dig 制作作品集](https://www.rephildesign.com/work/shovelknightdig)；作者岗位说明与资源名称。网页列出开箱/上锁箱受击/拾取/生成消失等分开的资源；GIF下载失败，未作为时序视觉证据。
