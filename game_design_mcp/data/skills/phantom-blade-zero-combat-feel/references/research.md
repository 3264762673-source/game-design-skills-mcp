# 研究来源、阅读范围与决策卡

核验日期：2026-10-30。只保存出处和原创摘要，不打包论文或视频全文。本文的来源不是数量投票：官方资料提供产品描述，论文提供有限情境的研究证据，开发者文章提供经验，视频提供待观测材料。

## 原作一手资料

**O1 · Soulframe Liang / S-GAME，2023-05-24。** [Phantom Blade Zero: a new beginning in a long journey](https://blog.playstation.com/2023/05/24/phantom-blade-zero-a-new-beginning-in-a-long-journey/)。已读相关正文。支持 Kungfupunk、阴暗世界、高速功夫电影动作及简洁输入的设计意图；当时介绍了拍摄动作参考后手工制作战斗动画。用于动作身份和体验目标，不作现版本制作工艺的完整证明。

**O2 · Soulframe Liang / S-GAME，2026-08-17。** [State of Play dives deep into combat and the Wulin world](https://blog.playstation.com/2026/08/17/phantom-blade-zero-state-of-play-dives-deep-into-combat-and-the-wulin-world/)。已读相关正文。介绍武器选择、难度及甄子丹的创意顾问和表演参与。用于说明表达空间与难度可配置；不据宣传推断每个动作如何生产。

**O3 · Phil Hornshaw / PlayStation Blog，2026-10-28。** [How boss weapons transform combat and exploration](https://blog.playstation.com/2026/10/28/phantom-blade-zero-how-boss-weapons-transform-combat-and-exploration/)。已读战斗段落。描述攻防与 Sha-Chi、换武器等关系。用于支持战斗流动的解释。发布在官方平台，但作者身份是撰稿人，不能当成引擎或源码文档。

**版本冲突处理：** O1 的手工动画叙述和 O2 的表演捕捉叙述有年代及范围差异。保留二者，不合成为“全手工”或“全动捕”。“杀气/架势/体力/绝技资源”若在不同视频中混用，先按该版本实际条槽和变化确认，再给实现字段命名。

## 学术研究

### P1 · 打击反馈有哪些候选变量

Lin, Duan, Wen & Cai，2022，**What Features Influence Impact Feel? A Study of Impact Feedback in Action Games**。[作者预印本](https://arxiv.org/html/2208.06155)，[IEEE DOI](https://doi.org/10.1109/GEM56474.2022.10017782)。已读摘要、引言、方法及特征表。

- 方法：Steam 评论的 NLP 排序，加游戏特征比较；19 类反馈特征。
- 发现指向停帧、声音一致性和镜头控制。
- 边界：非逐因素随机实验；评论和游戏选择存在偏差，不能证明三者普遍必要或产生最佳参数。
- 决策：优先诊断接触时序、材质声音和镜头可见性；用自己的对照测试验证。

### P2 · 手感不只等于视觉放大

Pichlmair & Johansen，2020 预印本 / 2021 期刊，**Designing Game Feel. A Survey**。[摘要](https://arxiv.org/abs/2011.09201)，[期刊 DOI](https://doi.org/10.1109/TG.2021.3072241)。本轮阅读摘要。

综述把设计意图组织为 physicality、amplification、support。用于把物理一致性、反馈增强和操作意图支持分别检查；不将综述分类当成受试者效果量。

### P3 · 成功依赖与能动性

Kao, Ballou, Gerling, Breitsohl & Deterding，CHI 2024，**How does Juicy Game Feedback Motivate? Testing Curiosity, Competence, and Effectance**。[作者 PDF](https://people.csail.mit.edu/dkao/pdf/3613904.3642656.pdf)，[DOI](https://doi.org/10.1145/3613904.3642656)。已读摘要和引言。

预注册在线实验 n=1,699；研究放大、成功依赖和变化性。摘要报告成功依赖提升所测动机，而该实验的放大处理出现负向结果，作者提出可能损害能动性的解释。用途：让普通命中、精准反制、失衡有有意义的区别。限制：不能据摘要完整复述实验细节或把结果推广成“特效越少越好”。

### P4 · 反馈强度存在任务相关取舍

Dominic Kao，2020，**The effects of juiciness in an action RPG**，Entertainment Computing 34，100359。[出版社摘要与 highlights](https://www.sciencedirect.com/science/article/pii/S1875952118300879)，[DOI](https://doi.org/10.1016/j.entcom.2020.100359)。只读摘要/highlights。

N=3018，四级反馈比较；该研究中 None 和 Extreme 在所报指标上低于 Medium 和 High。用于设计低/中/高反馈比较，不直接换算粒子数、亮度或震幅。不能由组合条件分离出单个通道的效果。

### P5 · 能力感与自主感

Ryan, Rigby & Przybylski，2006，**The Motivational Pull of Video Games: A Self-Determination Theory Approach**。[作者研究站 PDF](https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf)，[DOI](https://doi.org/10.1007/s11031-006-9051-8)。已读摘要/引言。

四项研究讨论需要满足与游戏享受等的联系。用途：分别询问“我觉得自己处理得好”和“我能选择如何处理”。不是对本游戏玩家的调查，也不要求单人原型加入社交。

### P6 · 从体验反推规则

Hunicke, LeBlanc & Zubek，2004，**MDA: A Formal Approach to Game Design and Game Research**。[作者所在机构 PDF](https://www.cs.northwestern.edu/~hunicke/MDA.pdf)。已读框架相关正文。

用途：把“高手交锋”追到攻防动态，再追到规则与数据。它是设计框架；Aesthetics 不等于画面美术，也不代替用户的概念诠释方法。

### P7 · 特效承载推理信息

Zhou & Forbes，2022，**Data Feel: Exploring Visual Effects in Video Games to Support Sensemaking Tasks**。[论文摘要](https://arxiv.org/abs/2210.03800)。只读摘要。

通过游戏案例讨论视觉效果如何支持理解世界。用途：给刀光、火花、范围和失衡表现指定信息职责。边界：不是影之刃零实验，不支持任何特效强度的数值建议。

### P8 · 输入响应需要单独测量

Liu, Claypool, Kuwahara, Scovell & Sherman，CHI 2021，**Lower is Better? The Effects of Local Latencies on Competitive First-Person Shooter Game Players**。[作者机构 PDF](https://web.cs.wpi.edu/~claypool/papers/csgo-lag-21/paper.pdf)，[DOI](https://doi.org/10.1145/3411764.3445245)。读到摘要及引言片段。

43 位有经验的 CS:GO 玩家，研究局部延迟与表现及主观质量的关系。用途：将浏览器输入延迟和动画蓄力分开诊断。限制：FPS 的人群、动作和条件不能给近战网页游戏提供普适延迟阈值。

## 开发者与行业文章

**A1 · Steve Swink，2007。** [Game Feel: The Secret Ingredient](https://www.gamedeveloper.com/design/game-feel-the-secret-ingredient)。本轮读到开头正文与案例。用途：观察实时控制和感知反馈闭环，而非只看战斗结果。作者经验，未在本轮阅读其书籍全文。

**A2 · Jiesang Song，2005。** [Improving the Combat 'Impact' Of Action Games](https://www.gamedeveloper.com/audio/improving-the-combat-impact-of-action-games)。页面只取得标题、作者、导语；正文未成功读取。保留为后续研读，当前不据此生成技术规则。

**A3 · Peyman Massoudi，2016。** [The Role of Animations in Hit Effects](https://www.gamedeveloper.com/programming/the-role-of-animations-in-hit-effects)。只核对到作者、标题、导语，正文未成功读取。后续用于追问动作本身怎样承载冲击，不作为本版细节证据。

**A4 · Riot Games，2020。** [VALORANT Shaders and Gameplay Clarity](https://www.riotgames.com/en/news/valorant-shaders-and-gameplay-clarity)。本轮页面返回结构噪音，未充分读到技术正文。列为清晰度延伸阅读，不能说已据此验证本版色彩方案。

## 合并成设计决策

| 决策 | 研究动机 | 本版工程推导 | 推翻/修订依据 |
|---|---|---|---|
| 分开输入响应与打击停顿 | A1、P8 | 输入采样不随表现暂停丢失；明确时间语义 | 对照中仍吞输入或变迟钝 |
| 接触反馈绑定规则结果 | P1、P3 | 挥空无命中火花，格挡和穿切声音不同 | 玩家无法分辨结果 |
| 重要成功获得更强反馈 | P3、P4 | 反制/失衡才用主要镜头资源 | 强反馈降低掌控或辨识 |
| 保留下一次威胁 | P2、P7 | 主要动作轮廓与预警优先于装饰 | 减效仍看不清来招 |
| 让敌人参与表达力量 | 体验论 C2；P1 提供检查方向 | 敌方防御、受击和恢复状态不同 | 玩家只感到木桩碾压 |

“决策”是待测规格，不冒充论文原话。原作精确碰撞、取消窗口、命中停顿、镜头曲线和音频混音仍未知。
