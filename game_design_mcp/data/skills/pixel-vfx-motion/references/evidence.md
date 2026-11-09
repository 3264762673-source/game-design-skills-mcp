# 像素特效与动效：来源与案例

研究日期：2026-11-09。特效是行动、接触、持续状态和结果的时间/空间表达；要区分模拟实体、必要可视化与装饰。早期约束影响表现，但不构成今天必须少帧少色的要求。

## 研究范围与先后

推导组为 Dead Cells、Celeste/Classic、Shovel Knight/Dig；同系列和移植不计独立作品。初版候选先写盘，再读 Noita，继而查 Rain World 与 One Step From Eden。下面只列本技能相关检验。

本次是作者图文、源码与论文的案例检查，没有运行游戏、测帧或真人实验。Celeste 源码固定到提交 `1b0ce45c75e05649ae91b44a8bb6b196684e4352`，并以具名函数定位；其他网页可能更新，复查时记录版本和访问日期。

## 逐规则结果

| 规则 | 独立检查所见 | 处理与证据强度 |
|---|---|---|
| F1 | Noita 作者解释燃烧、液体、爆炸后的塌落会改变世界；One Step From Eden 作者将爆炸链触发于敌人被消灭。 | **保留并收窄**：事件可以来自模拟状态，不限于按钮/命中事件；视觉与玩法共享原因，不要求玩法必须脱离一切视觉模型。跨案例一致，架构实现仍是本文提案。 |
| F2 | Noita 的火焰/液体/碎块可能是危险或物理实体，删掉它们会改变信息或规则。 | **收窄**：“先减粒子”改成“先给每层标记功能，只减装饰层”；未验证少粒子一定更清晰。 |
| F3 | Noita 的动态由材料规则涌现，不能预先画好所有完整变化；One Step From Eden 把序列图与生成器结合。 | **收窄**：预制阶段适合一次性序列特效；模拟特效需验证材料转换与持续/停止条件。 |

## 来源登记

- **D1** [Dead Cells 美术负责人 Thomas Vasseur，制作流程](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)：正文；关键姿态、时序与 3D 转低分辨率管线。未测游戏动画。
- **D2** [Celeste Classic 公开移植代码](https://github.com/NoelFB/Celeste/blob/1b0ce45c75e05649ae91b44a8bb6b196684e4352/Source/PICO-8/Classic.cs)：读取 fruit、fly_fruit、balloon、chest；与完整版不混算。源码不是通用架构范本。
- **D4** [Shovel Knight：Breaking the NES](https://www.yachtclubgames.com/blog/breaking-the-nes/) 与 [官方补丁](https://old.yachtclubgames.com/update-notes/)：正文；历史约束取舍与拾取/动画修复。历史故障不代表当前版本仍有故障。
- **H1** [Noita 开发者 Petri Purho 访谈](https://80.lv/articles/noita-a-game-based-on-falling-sand-simulation)：作者第一人称材料/物理系统说明；未观看嵌入视频。
- **H4** [One Step From Eden 作者开发日志](https://thomasmoonkang.itch.io/osfe/devlog/50688/weekly-update-10-assassinate)：死亡条件触发的爆炸链及制作复盘；未运行 Demo。
- **P1** [Kao 等，How does Juicy Game Feedback Motivate?，CHI 2024](https://doi.org/10.1145/3613904.3642656)：读摘要、设计含义和局限；动作 RPG 实验提供间接证据，不推出像素参数。
- **P2** [Pichlmair 与 Johansen，Designing Game Feel: A Survey](https://arxiv.org/html/2011.09201v1)：读相关分类；综述，不是本批规则的实验。
- **R2** [Hun Young Ha，ArtStation Pixel VFX](https://hunyoung04.artstation.com/projects/0alVNK)：作者管线文字，媒体未播放；仅制作参考。

## 渠道覆盖与缺口

[Saint11 作者教程](https://saint11.art/blog/pixel-art-tutorials/) 与 [作者 itch 教程包](https://studiominiboss.itch.io/pixel-art-tutorials) 已核验出处，部分 GIF 未能查看，未用于猜测帧数。[GDC：The Rain World Animation Process](https://www.youtube.com/watch?v=sVntwsrjNe4) 与 [B站翻译入口](https://www.bilibili.com/video/av13135432/) 只核验页面和回链，未取得字幕或完整观看；点赞与收藏没有可靠核验。Pinterest 未建立可复查的原作者链，不补无出处图。

Steam 开发者补丁与 itch 作者日志承担案例证据；作品集承担工艺线索；论文承担其实际研究范围内的依据。不同网站转载同一材料只算一个来源。没有条目达到“本项目实测”。

## 复查方法

重新定位上述函数或开发者段落，先记录实际状态与作者说明，再按规则卡执行最小项目试验。为相同初始条件保存输入/事件轨迹，比较结果和中断边界。没有动态观察时，时长、接触连续性与视觉辨识仍记为待测。保留不相容案例，用其收窄规则，不强迫作品服从规则。
