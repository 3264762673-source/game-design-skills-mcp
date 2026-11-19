# 来源与跨作品检验

研究基线：2026-11-09；整理：2026-11-20。没有新增玩家实验，未提升原有证据等级。规则编号仅在所属主题内有效。

## 特效动效

| 规则 | 案例观察 | 结论与边界 |
|---|---|---|
| F1 | Noita 作者解释燃烧、液体、爆炸后的塌落会改变世界；One Step From Eden 作者将爆炸链触发于敌人被消灭。 | **保留并收窄**：事件可以来自模拟状态，不限于按钮/命中事件；视觉与玩法共享原因，不要求玩法必须脱离一切视觉模型。跨案例一致，架构实现仍是本文提案。 |
| F2 | Noita 的火焰/液体/碎块可能是危险或物理实体，删掉它们会改变信息或规则。 | **收窄**：“先减粒子”改成“先给每层标记功能，只减装饰层”；未验证少粒子一定更清晰。 |
| F3 | Noita 的动态由材料规则涌现，不能预先画好所有完整变化；One Step From Eden 把序列图与生成器结合。 | **收窄**：预制阶段适合一次性序列特效；模拟特效需验证材料转换与持续/停止条件。 |

## 人物动作

| 规则 | 案例观察 | 结论与边界 |
|---|---|---|
| A1 | Rain World 作者访谈说明角色逐渐从传统/程序混合转向程序动画。 | **撤回普遍版本**；仅在姿态序列方案里保留“关键姿态先行”。程序方案先设身体约束、支撑点与输入响应。 |
| A2 | Rain World 的肢体随输入和模拟变化，并非所有表现都对应独立动画片段。 | **保留语义、收窄实现**：必须能说明行为与表现关系，但不强迫所有角色使用同一有限状态机。 |
| A3 | Rain World 将两块身体作为物理基础，肢体/尾巴另行表现；说明绘制轮廓与物理身体可以不同。 | **保留检查目的、撤回轮廓等于碰撞体的潜在推论**；没有证据证明某种锚点方案普遍最优。 |

## 物品动效

| 规则 | 案例观察 | 结论与边界 |
|---|---|---|
| I1 | Noita 官方补丁处理宝箱掉落的确定性，并修复掉落输入冲突；这不是对“视觉结束就应入账”的支持。 | **保留为工程检查**：结算与表现的对应可复查。一次性结算/幂等是本文执行提案，案例未证明所有游戏都采用该结构。 |
| I2 | Noita 补丁修复喝药/丢弃的按键冲突；状态意图不能只靠同一个输入推断。 | **保留为待测设计**：至少区分意图、接受、拒绝、结果；未观察其悬停、装备动画视觉效果，不能标成美术效果已验证。 |
| I3 | Noita 官方材料与补丁说明刚体、灯具、家具具有真实物理/破坏状态，保存载入曾丢失变换与关节。 | **保留并明确分支**：装饰偏移、碰撞移动、可破坏实体三类分别处理；不能将所有物品动效改为纯贴图漂浮。 |

## 来源登记与检查范围

推导组为 Dead Cells、Celeste/Classic、Shovel Knight/Dig；同系列和移植不计独立作品。初版候选先写盘，再读 Noita，继而查 Rain World 与 One Step From Eden。下面只列本技能相关检验。

- **D1** [Dead Cells 美术负责人 Thomas Vasseur，制作流程](https://www.gamedeveloper.com/production/art-design-deep-dive-using-a-3d-pipeline-for-2d-animation-in-i-dead-cells-i-)：正文；关键姿态、时序与 3D 转低分辨率管线。未测游戏动画。

- **D2** [Celeste Classic 公开移植代码](https://github.com/NoelFB/Celeste/blob/1b0ce45c75e05649ae91b44a8bb6b196684e4352/Source/PICO-8/Classic.cs)：读取 fruit、fly_fruit、balloon、chest；与完整版不混算。源码不是通用架构范本。

- **D4** [Shovel Knight：Breaking the NES](https://www.yachtclubgames.com/blog/breaking-the-nes/) 与 [官方补丁](https://old.yachtclubgames.com/update-notes/)：正文；历史约束取舍与拾取/动画修复。历史故障不代表当前版本仍有故障。

- **H1** [Noita 开发者 Petri Purho 访谈](https://80.lv/articles/noita-a-game-based-on-falling-sand-simulation)：作者第一人称材料/物理系统说明；未观看嵌入视频。

- **H4** [One Step From Eden 作者开发日志](https://thomasmoonkang.itch.io/osfe/devlog/50688/weekly-update-10-assassinate)：死亡条件触发的爆炸链及制作复盘；未运行 Demo。

- **P1** [Kao 等，How does Juicy Game Feedback Motivate?，CHI 2024](https://doi.org/10.1145/3613904.3642656)：读摘要、设计含义和局限；动作 RPG 实验提供间接证据，不推出像素参数。

- **P2** [Pichlmair 与 Johansen，Designing Game Feel: A Survey](https://arxiv.org/html/2011.09201v1)：读相关分类；综述，不是本批规则的实验。

- **R2** [Hun Young Ha，ArtStation Pixel VFX](https://hunyoung04.artstation.com/projects/0alVNK)：作者管线文字，媒体未播放；仅制作参考。

[Saint11 作者教程](https://saint11.art/blog/pixel-art-tutorials/) 与 [作者 itch 教程包](https://studiominiboss.itch.io/pixel-art-tutorials) 已核验出处，部分 GIF 未能查看，未用于猜测帧数。[GDC：The Rain World Animation Process](https://www.youtube.com/watch?v=sVntwsrjNe4) 与 [B站翻译入口](https://www.bilibili.com/video/av13135432/) 只核验页面和回链，未取得字幕或完整观看；点赞与收藏没有可靠核验。Pinterest 未建立可复查的原作者链，不补无出处图。

- **D3** [Celeste Player 公开代码](https://github.com/NoelFB/Celeste/blob/1b0ce45c75e05649ae91b44a8bb6b196684e4352/Source/Player/Player.cs)：读取 UpdateSprite、Throw、Drop 等相关片段；未运行。

- **H3** [Rain World 开发者访谈，Animating the slugcat](https://unity.com/blog/exploring-procedural-design-rain-world)：正文；程序肢体和身体块。没有逐帧观看。

- **D5** [Phil Giarrusso：Shovel Knight Dig 作品集](https://www.rephildesign.com/work/shovelknightdig)：作者职责及资源名称；GIF 未能查看，只支持资源拆分的存在。

- **H2** [Noita 官方 Update #12，2020-06-24](https://store.steampowered.com/news/posts/?appids=881100&enddate=1600795863&feed=steam_community_announcements)：物件载入、掉落/喝药输入、宝箱等修复条目。

截图不能验证碰撞、焦点、连续动作或误选率；源码不能证明玩家体验。视频/点赞/收藏/Pinterest 原作链存在已记录缺口，没有将候选入口算作已观看或验证。实际项目检验失败时收窄或撤回规则。
