# 乐趣记录与后续更新

记录把目标、方案和证据关联起来，便于其他计算机或 AI 按同一依据继续工作。它不把主观体验变成确定性的数值函数。

## 字段契约

需要机器读取时使用 [JSON 模板](../assets/experience-record.json)。模板中的空值表示待填写信息；实际交付时填入已知内容，把确实未知的值保留为 `null` 并在 `assumptions` 或 `open_questions` 说明。

| 字段 | 含义 |
|---|---|
| `record_id`, `revision`, `parent_record_id` | 唯一记录、记录修订号、关联的原记录。新乐趣或独立方案另建记录时用父 ID 追溯 |
| `original_request` | 保留用户的原目标文字；目标改变另建关联记录 |
| `pleasure` | 开放标签、具体乐趣句、来源、知识条件、必要条件 |
| `target` | 载体、允许改动的范围、硬约束 |
| `mapping` | 必要条件如何由目标规则和反馈承载 |
| `proposal` | 机制与可执行循环、明确的方案版本 `version`；可选实现位置 |
| `assessment` | 结构映射、原体验证据、乐趣证据三个独立状态 |
| `evidence` | 输入、规则、推断或实际反馈；注明定位、条件、支持/反对哪条判断 |
| `emergent_pleasures` | 新乐趣候选及证据；与原目标分别记录 |
| `decision` | 下一步方向、理由、原目标是否得到用户明确替换 |
| `exceptions` | 被证据支持的方法性例外；不能取消用户硬约束 |
| `next_experiment` | 后续比较方案、支持与否定信号 |
| `history` | 变更内容、理由、依据；保留相反和失败证据 |

必要条件使用稳定 ID，如 `C1`；证据使用 `E1`。映射和判断用 ID 引用，避免同一说法在多处被悄悄改写。

## 数组成员与版本契约

使用以下固定字段；这些是成员形状说明，不是可以直接当成事实的样例数据。文本未知时用 `null`，引用列表未知时用空数组。`labels`、`knowledge_conditions`、`hard_constraints`、`loop`、`assumptions`、`open_questions` 及各实验信号均为字符串数组。

```json
{
  "essential_condition": {
    "id": "C1", "statement": "条件描述", "basis": "hypothesis", "evidence_ids": []
  },
  "mapping_item": {
    "condition_id": "C1", "target_rule": "目标规则", "feedback": "可感知反馈",
    "interpretation": "反馈如何传达含义", "status": "unknown", "reason": "判断依据"
  },
  "evidence_item": {
    "id": "E1", "kind": "user_brief", "statement": "证据内容", "locator": null,
    "record_id": "EXP-001", "proposal_version": 1,
    "judgment": "structural_fit", "direction": "context",
    "conditions": [], "reported_by": null, "limitations": []
  },
  "emergent_pleasure": {
    "id": "N1", "label": "新乐趣标签", "statement": "具体情境",
    "proposal_version": 1, "status": "hypothesis", "evidence_ids": [],
    "relation_to_original": "和原目标的区别", "linked_record_id": null
  },
  "exception": {
    "rule": "方法性约束", "reason": "例外理由", "scope": "适用范围",
    "proposal_version": 1, "status": "hypothesis", "evidence_ids": []
  },
  "history_item": {
    "record_revision": 1, "proposal_version": 1, "change": "改了什么",
    "reason": "为什么改", "evidence_ids": [], "previous_assessment": null
  }
}
```

- `essential_condition.basis`：`user` / `source` / `hypothesis`。
- `evidence_item.judgment`：`structural_fit` / `original_experience` / `fun` / `emergent_pleasure` / `context`。
- `evidence_item.direction`：`supports` / `contradicts` / `context`。同一反馈对不同判断方向相反时拆为两条证据，可共用 `locator`。
- `exception.status`：`hypothesis` / `supported`；后者需要相关实际反馈。
- `evidence_item.record_id` 与 `proposal_version` 指向它实际描述的方案。不能把旧试玩证据的版本号改成新版本号。
- `revision` 每次保存修订时递增；`proposal.version` 只在实际规则或呈现方案改变时递增。单纯补录反馈不改变方案版本。
- `assessment.proposal_version` 必须等于当前 `proposal.version`。当前体验与乐趣判断只引用属于当前记录和当前方案版本的证据。旧版本证据仍保存在 `evidence` 中，但从当前 `assessment.evidence_ids` 移出；旧判断保存于 `history.previous_assessment`。
- 独立比较的 A/B 方案分别建立记录；关联记录引用父 ID。每个版本的反馈归到对应记录，不能把 B 的喜爱反馈合并成 A 的结果。
- `next_experiment.proposal_version` 标识实验所针对的方案。若仅描述拟议的修改，`result` 为 `null`；实施新方案后按新版本建实验记录，不能沿用旧结果。

## 固定状态

- `mapping[].status`：`mapped` / `partial` / `missing` / `unknown`。
- `assessment.structural_fit`：`candidate_match` / `partial` / `mismatch` / `unknown`。
- `assessment.original_experience`：`untested` / `partial_support` / `supported` / `not_supported` / `mixed`。
- `assessment.fun`：`untested` / `positive` / `negative` / `mixed`。
- `emergent_pleasures[].status`：`hypothesis` / `observed` / `mixed`。
- `evidence[].kind`：`user_brief` / `source_material` / `rule_inspection` / `design_inference` / `simulation` / `human_feedback`。
- `decision.next_action`：`prototype` / `revise_original` / `retain_new_direction` / `keep_both` / `await_clarification` / `retain_with_evidence`。

标签、证据类型和验证状态是不同字段。用户报告已有真人试玩时，按 `human_feedback` 记录报告者与已知条件；没有原始录像可以记录“用户转述”，不擅自补样本量或逐字引语。

原体验状态的边界：`supported` 表示反馈支持本次完整目标；`partial_support` 表示只支持其中部分关系或过程，其余尚无证据，尚不能称原迁移成功；`not_supported` 表示相关观察反对目标成立，或已检查的关键体验未出现；`mixed` 表示同一目标存在实质性的正反反馈。信息没有覆盖不等于反对证据，不能仅因有未知项就填 `mixed`。完全没有相关体验反馈时为 `untested`。具体哪些部分获得支持、哪些未知，写入依据并引用证据。

## 判定和更新规则

1. 先确保每个必要条件有且只有一条映射；没有对应映射则按 `unknown` 补录。按互斥顺序汇总：存在 `missing` → `mismatch`；否则存在 `unknown` 或必要条件列表为空 → `unknown`；否则存在 `partial` → `partial`；否则全部 `mapped` → `candidate_match`。已知问题保留在逐条件记录中。`candidate_match` 只表示方案假设成立。
2. `original_experience` 与 `fun` 只有在分别存在相关的实际人类体验反馈时才从 `untested` 更新。用户批准方案、AI 代玩、自动测试与理论推导不触发这一更新。
3. 结构不匹配且未试玩：记录“原迁移在方案层面未达成；实际体验待测”，保持 `original_experience = untested`，避免把结构诊断冒充实测失败。
4. 实际反馈支持新体验时，原目标独立判断为 `partial_support`、`supported`、`not_supported`、`mixed` 或 `untested`，取决于它本身的证据。新乐趣单独标为 `observed`。新乐趣出现不自动证明“好玩”，需要吸引力反馈支持 `fun = positive`。
5. `supported` 与 `positive` 表示所记录条件下的支持，不表示普遍有效。反馈矛盾则保留各条证据并标 `mixed`。
6. 用户只说“我喜欢新方案”但没有说明实际玩过，记录为设计偏好；不能升级为实测。
7. 没有明确指令替换原目标时，`decision.goal_change_confirmed = false`。保留新方案和其乐趣记录仍可进行；改变原目标须有用户指令作为依据。替换后另建关联记录，不删旧记录。
8. 同一目标的方案变化时增加 `proposal.version` 与记录 `revision`，重新检查结构映射；当前 `original_experience` 和 `fun` 回到 `untested`。旧证据及其版本和旧评估按上述契约保留。仅补录同一方案的反馈时只增记录修订号，按该版本的全部相关反馈更新判断。

实际反馈与暂定必要条件冲突时，先记录冲突，再检查是否误定了必要条件或误读了反馈，不能为了保持理论一致而删除观察。

## 小实验格式

只建议一个能区分主要假设的比较：

- 保持什么相同，改变什么；整组改动时明确不能归因于某个单项。
- 不提示乐趣标签，先让试玩者描述“刚才在意什么、为什么这么做、哪一刻值得继续”。
- 对照具体行为和主观描述；单独的停留时长、胜率或重玩次数不足以判断乐趣。
- 哪种结果支持原体验，哪种支持新体验，哪种会否定当前解释。
- 用户提供反馈后再填写结果。没有数据时保留待测，完成设计交付。

## 简短聊天记录

任务较小时可以直接输出：`记录 ID｜乐趣句｜来源→目标｜保留/改变｜原迁移状态｜新乐趣及状态｜依据｜下一步`。

在聊天中展示不等于文件已保存。需要保存时按 SKILL.md 的规则落盘，给出真实路径。未经授权不把项目资料写入全局 skill；项目实验结果保存在项目记录中，用户要求更新 skill 时才抽取可迁移的修订。
