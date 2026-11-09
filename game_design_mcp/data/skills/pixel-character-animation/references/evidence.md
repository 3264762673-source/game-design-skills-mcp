# 像素人物动作：来源与案例

研究日期：2026-11-09。人物动作表达意图、施力与接触。预制序列、预渲染和程序身体都是可选管线；关键姿态方法的适用范围必须声明。

## 研究范围与先后

推导组为 Dead Cells、Celeste/Classic、Shovel Knight/Dig；同系列和移植不计独立作品。初版候选先写盘，再读 Noita，继而查 Rain World 与 One Step From Eden。下面只列本技能相关检验。

本次是作者图文、源码与论文的案例检查，没有运行游戏、测帧或真人实验。Celeste 源码固定到提交 `1b0ce45c75e05649ae91b44a8bb6b196684e4352`，并以具名函数定位；其他网页可能更新，复查时记录版本和访问日期。

## 逐规则结果

| 规则 | 独立检查所见 | 处理与证据强度 |
|---|---|---|
| A1 | Rain World 作者访谈说明角色逐渐从传统/程序混合转向程序动画。 | **撤回普遍版本**；仅在姿态序列方案里保留“关键姿态先行”。程序方案先设身体约束、支撑点与输入响应。 |
| A2 | Rain World 的肢体随输入和模拟变化，并非所有表现都对应独立动画片段。 | **保留语义、收窄实现**：必须能说明行为与表现关系，但不强迫所有角色使用同一有限状态机。 |
| A3 | Rain World 将两块身体作为物理基础，肢体/尾巴另行表现；说明绘制轮廓与物理身体可以不同。 | **保留检查目的、撤回轮廓等于碰撞体的潜在推论**；没有证据证明某种锚点方案普遍最优。 |

## 来源登记

- **D1** [Dead Cells 美术负责人 Thomas Vasseur，制作流程](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)：正文；关键姿态、时序与 3D 转低分辨率管线。未测游戏动画。
- **D3** [Celeste Player 公开代码](https://github.com/NoelFB/Celeste/blob/1b0ce45c75e05649ae91b44a8bb6b196684e4352/Source/Player/Player.cs)：读取 UpdateSprite、Throw、Drop 等相关片段；未运行。
- **D4** [Shovel Knight：Breaking the NES](https://www.yachtclubgames.com/blog/breaking-the-nes/) 与 [官方补丁](https://old.yachtclubgames.com/update-notes/)：正文；历史约束取舍与拾取/动画修复。历史故障不代表当前版本仍有故障。
- **H3** [Rain World 开发者访谈，Animating the slugcat](https://unity.com/blog/exploring-procedural-design-rain-world)：正文；程序肢体和身体块。没有逐帧观看。
- **P2** [Pichlmair 与 Johansen，Designing Game Feel: A Survey](https://arxiv.org/html/2011.09201v1)：读相关分类；综述，不是本批规则的实验。

## 渠道覆盖与缺口

[Saint11 作者教程](https://saint11.art/blog/pixel-art-tutorials/) 与 [作者 itch 教程包](https://studiominiboss.itch.io/pixel-art-tutorials) 已核验出处，部分 GIF 未能查看，未用于猜测帧数。[GDC：The Rain World Animation Process](https://www.youtube.com/watch?v=sVntwsrjNe4) 与 [B站翻译入口](https://www.bilibili.com/video/av13135432/) 只核验页面和回链，未取得字幕或完整观看；点赞与收藏没有可靠核验。Pinterest 未建立可复查的原作者链，不补无出处图。

Steam 开发者补丁与 itch 作者日志承担案例证据；作品集承担工艺线索；论文承担其实际研究范围内的依据。不同网站转载同一材料只算一个来源。没有条目达到“本项目实测”。

## 复查方法

重新定位上述函数或开发者段落，先记录实际状态与作者说明，再按规则卡执行最小项目试验。为相同初始条件保存输入/事件轨迹，比较结果和中断边界。没有动态观察时，时长、接触连续性与视觉辨识仍记为待测。保留不相容案例，用其收窄规则，不强迫作品服从规则。
