# 像素物品动效：来源与案例

研究日期：2026-11-09。物品动效覆盖出现、落地、待机、交互、使用/装备和消失。角色伸手只是其中一侧；物品状态、库存结果和可见表现应分别核查。

## 研究范围与先后

推导组为 Dead Cells、Celeste/Classic、Shovel Knight/Dig；同系列和移植不计独立作品。初版候选先写盘，再读 Noita，继而查 Rain World 与 One Step From Eden。下面只列本技能相关检验。

本次是作者图文、源码与论文的案例检查，没有运行游戏、测帧或真人实验。Celeste 源码固定到提交 `1b0ce45c75e05649ae91b44a8bb6b196684e4352`，并以具名函数定位；其他网页可能更新，复查时记录版本和访问日期。

## 逐规则结果

| 规则 | 独立检查所见 | 处理与证据强度 |
|---|---|---|
| I1 | Noita 官方补丁处理宝箱掉落的确定性，并修复掉落输入冲突；这不是对“视觉结束就应入账”的支持。 | **保留为工程检查**：结算与表现的对应可复查。一次性结算/幂等是本文执行提案，案例未证明所有游戏都采用该结构。 |
| I2 | Noita 补丁修复喝药/丢弃的按键冲突；状态意图不能只靠同一个输入推断。 | **保留为待测设计**：至少区分意图、接受、拒绝、结果；未观察其悬停、装备动画视觉效果，不能标成美术效果已验证。 |
| I3 | Noita 官方材料与补丁说明刚体、灯具、家具具有真实物理/破坏状态，保存载入曾丢失变换与关节。 | **保留并明确分支**：装饰偏移、碰撞移动、可破坏实体三类分别处理；不能将所有物品动效改为纯贴图漂浮。 |

## 来源登记

- **D2** [Celeste Classic 公开移植代码](https://github.com/NoelFB/Celeste/blob/1b0ce45c75e05649ae91b44a8bb6b196684e4352/Source/PICO-8/Classic.cs)：读取 fruit、fly_fruit、balloon、chest；与完整版不混算。源码不是通用架构范本。
- **D3** [Celeste Player 公开代码](https://github.com/NoelFB/Celeste/blob/1b0ce45c75e05649ae91b44a8bb6b196684e4352/Source/Player/Player.cs)：读取 UpdateSprite、Throw、Drop 等相关片段；未运行。
- **D4** [Shovel Knight：Breaking the NES](https://www.yachtclubgames.com/blog/breaking-the-nes/) 与 [官方补丁](https://old.yachtclubgames.com/update-notes/)：正文；历史约束取舍与拾取/动画修复。历史故障不代表当前版本仍有故障。
- **D5** [Phil Giarrusso：Shovel Knight Dig 作品集](https://www.rephildesign.com/work/shovelknightdig)：作者职责及资源名称；GIF 未能查看，只支持资源拆分的存在。
- **H1** [Noita 开发者 Petri Purho 访谈](https://80.lv/articles/noita-a-game-based-on-falling-sand-simulation)：作者第一人称材料/物理系统说明；未观看嵌入视频。
- **H2** [Noita 官方 Update #12，2020-06-24](https://store.steampowered.com/news/posts/?appids=881100&enddate=1600795863&feed=steam_community_announcements)：物件载入、掉落/喝药输入、宝箱等修复条目。
- **P2** [Pichlmair 与 Johansen，Designing Game Feel: A Survey](https://arxiv.org/html/2011.09201v1)：读相关分类；综述，不是本批规则的实验。

## 渠道覆盖与缺口

[Saint11 作者教程](https://saint11.art/blog/pixel-art-tutorials/) 与 [作者 itch 教程包](https://studiominiboss.itch.io/pixel-art-tutorials) 已核验出处，部分 GIF 未能查看，未用于猜测帧数。[GDC：The Rain World Animation Process](https://www.youtube.com/watch?v=sVntwsrjNe4) 与 [B站翻译入口](https://www.bilibili.com/video/av13135432/) 只核验页面和回链，未取得字幕或完整观看；点赞与收藏没有可靠核验。Pinterest 未建立可复查的原作者链，不补无出处图。

Steam 开发者补丁与 itch 作者日志承担案例证据；作品集承担工艺线索；论文承担其实际研究范围内的依据。不同网站转载同一材料只算一个来源。没有条目达到“本项目实测”。

## 复查方法

重新定位上述函数或开发者段落，先记录实际状态与作者说明，再按规则卡执行最小项目试验。为相同初始条件保存输入/事件轨迹，比较结果和中断边界。没有动态观察时，时长、接触连续性与视觉辨识仍记为待测。保留不相容案例，用其收窄规则，不强迫作品服从规则。
