# 像素图标与小按钮：来源与案例

研究日期：2026-11-09。icon 是表达对象/功能/状态的符号，button 是接受输入的控件，两者不等同。I1 有跨作品有限支持；I2 完整状态未检验；I3 为标准推导，未测游戏 hitbox。

## 起源和研究范围

S01 是 1982 年 Xerox Star 作者关于位图界面、任务与图标的一手文章存档，用于通用 GUI 前史；没有据此断言像素游戏 UI 的唯一发明时间。本次未建立完整游戏 HUD 史。

推导组：Into the Breach（Subset Games）、Papers, Please（Lucas Pope/3909）。桌面/手机版只算一个作品。候选于北京时间 18:27:48 写盘后，才读取 Backpack Hero（Jaspel）检验材料，首张图片记录为 18:29:44。没有真人实验、运行游戏或统计因果分析。

实际查看 GDC 幻灯片第 2、30 页，Papers, Please 官网 Shot02-Booth.png 与手机区域图，以及 Backpack Hero 官方 Steam 详情中的截图 0–2。可复查的原入口见来源表；截图未随技能发布。

## 逐规则结果

| 规则 | Into the Breach | Papers, Please | Backpack Hero 独立检验 | 结论 |
|---|---|---|---|---|
| I1 检查符号含义及可查名称 | 方向图标配对象说明 | 文书缩略表示配可读文书 | 物品图配具名说明，命令有文字 | 保留：案例支持；玩家解码能力待测 |
| I2 区分不同状态 | 可见标记，不完整 | 没有完整状态图谱 | 可见不同标记，语义不能全推断 | 收窄：可要求多通道表达；全状态结论待测 |
| I3 图像边界与命中区分离 | 截图不可见 | 没有坐标测试 | 截图不可见 | 工程要求；不声称跨作品通过 |

## 来源与访问层级

| ID | 来源 | 访问范围 / 使用边界 |
|---|---|---|
| S01 | [Smith 等：《Designing the Star User Interface》，BYTE 1982 原文存档](https://guidebookgallery.org/articles/historical/designingthestaruserinterface/) | 阅读原文重印中的位图/任务分析/图标/一致性段落；第三方档案承载的一手作者文章，非像素游戏史完整证据 |
| S02 | [Matthew Davis：Into the Breach Design Postmortem，GDC 2019 PDF](https://media.gdcvault.com/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf) | 49 页文本可访问；重点读 UI Guided Design；实际渲染查看第 2、30 页；未观看演讲视频 |
| S03 | [Papers, Please 官网](https://papersplea.se/)；[桌面截图](https://papersplea.se/img/Shot02-Booth.png) | 官网及一张原图实际查看；不把奖项列表当 UI 效果证明 |
| S04 | [Lucas Pope：Cramming Papers, Please Onto Phones，2022](https://dukope.com/devlogs/papers-please/mobile/) | 阅读布局、像素网格、盖章模式及局部交互说明；实际查看 Carousel/Rack 静态图；未逐帧分析 GIF |
| S05 | [W3C：Understanding SC 2.5.8 Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) | 正文与例外；官方说明页，与规范本身区分；不当作所有游戏尺寸定律 |
| S06 | [W3C：Understanding SC 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) | 阅读正文、例外与信息表达边界；不据此限制装饰配色 |
| S07 | [Microsoft XAG 112：UI navigation](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/112) | 正文可读取，包含焦点顺序与多输入指导；未观看嵌入视频 |
| S08 | [McDougall & Isherwood, 2009：What’s in a name?](https://link.springer.com/content/pdf/10.3758/BRM.41.2.325.pdf) | 期刊原始研究 PDF，重点段落阅读；非像素游戏实验 |
| S09 | [Backpack Hero 官方 itch 页面](https://thejaspel.itch.io/backpack-hero) | 作者说明、鼠标/旋转键操作说明、版本信息；未运行网页试玩；评论不作确定性事实 |
| S10 | [Backpack Hero 官方 Steam 商店](https://store.steampowered.com/app/1970580/Backpack_Hero/)；[同站公开详情](https://store.steampowered.com/api/appdetails?appids=1970580) | 读取官方详情的截图 0–2 并实际查看；其中一图署截图贡献者，来源为开发者选择发布；商品支持标签不是行为检查 |

## 参考网站与视频缺口

[AdamCYounis：Intro to Game UI](https://www.youtube.com/watch?v=o3VHJ7g7M08) 只读到搜索索引说明与章节，未看完整视频；[B站字幕候选](https://www.bilibili.com/video/BV1Db4y127vx) 正文返回 412，归属、授权、点赞和收藏未核实。故没有从视频抽取新的规则或宣称高赞筛选完成。

[Daniel Bernal：SELECT YOUR STAGE](https://bernalstudio.artstation.com/projects/rRvvea) 原作者文字已读，是像素再设计作品，不能算发行游戏的可用性证据。Pinterest 未找到足够可靠的原作链。以上是后续参考入口，不计独立验证通过。

## 检查时保留的边界

静态图可说明区域和符号存在，不能推断其焦点、按键行为、命中区或玩家理解。图标论文不是像素游戏实验；WCAG 的 CSS px 不等于 sprite 源像素。标准适用性需按平台和任务判断。

复查时先执行规则卡的具体任务；将内容、设备和输入保持可比，保留误选、死路与恢复失败轨迹。没有运行条件就交付规格和待测表，不宣布输入已通过。没有条目达到“本项目实测”。
