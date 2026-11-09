"""Dependency-aware design interviews. Pure transformations; no model or persistence."""
from typing import Annotated, Literal
from pydantic import Field, model_validator
from .core import StrictModel

Text = Annotated[str, Field(min_length=1, max_length=6000, pattern=r"\S")]
NodeId = Annotated[str, Field(pattern=r"^[a-z][a-z0-9_-]{0,63}$")]

class Decision(StrictModel):
    id: NodeId
    topic: Text
    question: Text
    recommendation: Text
    depends_on: list[NodeId] = Field(default_factory=list, max_length=40)
    status: Literal['open', 'resolved', 'assumed'] = 'open'
    answer: Text | None = None
    basis: Literal['user', 'project_evidence', 'hypothesis'] | None = None
    locator: Text | None = None

    @model_validator(mode='after')
    def coherent(self):
        if self.status == 'open':
            if any(v is not None for v in (self.answer, self.basis, self.locator)):
                raise ValueError('Open decisions cannot carry a current answer; use history')
        elif self.answer is None or self.basis is None:
            raise ValueError('Answered decisions need answer and basis')
        elif self.status == 'assumed' and self.basis != 'hypothesis':
            raise ValueError('Assumptions require hypothesis basis')
        elif self.status == 'resolved' and self.basis == 'hypothesis':
            raise ValueError('A hypothesis cannot resolve a decision')
        if self.basis == 'project_evidence' and not self.locator:
            raise ValueError('Project evidence needs a locator')
        return self

class Change(StrictModel):
    revision: int = Field(ge=2)
    decision_id: NodeId
    previous: Decision
    current: Decision

class DesignSession(StrictModel):
    session_id: NodeId
    revision: int = Field(default=1, ge=1)
    original_request: Text
    decisions: list[Decision] = Field(min_length=1, max_length=40)
    history: list[Change] = Field(default_factory=list, max_length=2000)
    confirmed_revision: int | None = Field(default=None, ge=1)
    explore_assumptions: bool = False

    @model_validator(mode='after')
    def graph(self):
        nodes = {n.id: n for n in self.decisions}
        if len(nodes) != len(self.decisions): raise ValueError('Duplicate decision IDs')
        for n in self.decisions:
            if len(set(n.depends_on)) != len(n.depends_on): raise ValueError('Duplicate dependencies')
            if not set(n.depends_on) <= nodes.keys(): raise ValueError('Undefined prerequisite')
        visited, active = set(), set()
        def visit(key):
            if key in active: raise ValueError('Dependency cycle')
            if key in visited: return
            active.add(key)
            for dep in nodes[key].depends_on: visit(dep)
            active.remove(key); visited.add(key)
        for key in nodes: visit(key)
        for n in self.decisions:
            if n.status != 'open' and any(nodes[d].status == 'open' for d in n.depends_on):
                raise ValueError('Answered decision has an open prerequisite')
            if n.status == 'resolved' and any(nodes[d].status != 'resolved' for d in n.depends_on):
                raise ValueError('Resolved decision depends on an assumption')
        if self.confirmed_revision is not None and (
            self.confirmed_revision != self.revision or any(n.status != 'resolved' for n in self.decisions)
        ): raise ValueError('Confirmation must refer to current, fully resolved revision')
        return self

class DesignAnswer(StrictModel):
    decision_id: NodeId
    answer: Text
    basis: Literal['user', 'project_evidence', 'hypothesis']
    locator: Text | None = None

def start_design_interview(original_request: str, session_id: str = 'design-001') -> DesignSession:
    rows = [
        ('scope', '范围与约束', [], '本轮要交付什么、目标载体是什么、哪些条件必须保留？', '沿用原请求与项目事实，先限定一个可实施的最小方案。'),
        ('experience', '目标体验', ['scope'], '玩家在什么处境与关系中，通过什么行动，让什么变化对自己有意义？', '写具体体验句，区分玩家选择与角色表演；保留原目标文字。'),
        ('meaning', '概念诠释与预期共识', ['experience'], '核心概念分别意味着什么？玩家凭什么理解，可能怎样误读？', '为每个概念列本次含义、感知依据和另一种解释。'),
        ('agency', '玩家能动性', ['experience'], '玩家实际上能选择什么、付出什么代价？只有自动演出还会有同样体验吗？', '找出玩家可控制且会改变结果的时机、方向或取舍。'),
        ('conditions', '必要条件与反例', ['meaning','agency'], '逐项删除哪些关系会使原体验改变？哪些符号可以替换？', '列候选条件 ID；用反例检查，暂定条件不当作心理定律。'),
        ('feedback', '行为—结果—诠释', ['conditions'], '每个条件通过哪条规则和哪种反馈被理解？缺失时会变成什么新乐趣？', '逐条件映射操作、真实结果、可感知反馈和预期含义，保留偏移。'),
        ('loop', '最小可实施闭环', ['feedback','scope'], '初始状态、可选动作、触发、结算、终止、失败恢复分别是什么？', '用一轮闭环写出实现者可执行的规格，数值标为试调值。'),
        ('experiment', '否定实验与交付', ['loop'], '怎样区分原体验成立、新乐趣出现及两者皆无？什么结果会推翻方案？', '提出一个有反例标准的比较，分别记录原迁移和新增乐趣，未试玩保持待测。'),
    ]
    return DesignSession(session_id=session_id, original_request=original_request,
                         decisions=[Decision(id=i,topic=t,depends_on=d,question=q,recommendation=r)
                                    for i,t,d,q,r in rows])

def frontier(session: DesignSession) -> dict:
    nodes = {n.id:n for n in session.decisions}
    def settled(key):
        return nodes[key].status == 'resolved' or (session.explore_assumptions and nodes[key].status == 'assumed')
    available = [n for n in session.decisions if n.status == 'open' and all(settled(d) for d in n.depends_on)]
    assumptions = [n.id for n in session.decisions if n.status == 'assumed']
    return {'questions':[n.model_dump() for n in available],
            'blocked':[n.id for n in session.decisions if n.status == 'open' and n not in available],
            'assumptions': assumptions,
            'resolved': all(n.status == 'resolved' for n in session.decisions),
            'awaiting_confirmation': all(n.status == 'resolved' for n in session.decisions) and session.confirmed_revision is None}

def advance_design_interview(session: DesignSession, answers: list[DesignAnswer], confirm_revision: int | None = None) -> dict:
    # Apply a round atomically. A downstream question cannot be answered using a
    # prerequisite supplied in this same round, nor silently survive a revised parent.
    if not answers and confirm_revision is None: raise ValueError('Supply answers or an explicit confirmation')
    if answers and confirm_revision is not None: raise ValueError('Review the new revision before confirming it')
    if len(answers)>40: raise ValueError('At most 40 answers per round')
    nodes = {n.id:n.model_copy(deep=True) for n in session.decisions}
    ids = [a.decision_id for a in answers]
    if len(set(ids)) != len(ids) or not set(ids) <= nodes.keys(): raise ValueError('Duplicate or unknown answer ID')
    if confirm_revision is not None:
        if confirm_revision != session.revision or not frontier(session)['resolved']:
            raise ValueError('Only current fully resolved revision can be confirmed')
        updated = DesignSession.model_validate({**session.model_dump(), 'confirmed_revision':confirm_revision})
        return {'session':updated.model_dump(), 'frontier':frontier(updated), 'invalidated':[]}
    available = {n['id'] for n in frontier(session)['questions']}
    invalidated = set()
    for key in ids:
        if nodes[key].status == 'open' and key not in available:
            raise ValueError('Answer prerequisite questions in an earlier round')
        descendants = {key}
        while True:
            more = descendants | {n.id for n in nodes.values() if set(n.depends_on)&descendants}
            if more == descendants: break
            descendants = more
        invalidated |= descendants - {key}
    if invalidated & set(ids): raise ValueError('Cannot revise a parent and its descendants in one round')
    for key in invalidated:
        nodes[key] = nodes[key].model_copy(update={'status':'open','answer':None,'basis':None,'locator':None})
    for a in answers:
        nodes[a.decision_id] = Decision.model_validate({**nodes[a.decision_id].model_dump(),
            'answer':a.answer,'basis':a.basis,'locator':a.locator,
            'status':'assumed' if a.basis == 'hypothesis' else 'resolved'})
    rev=session.revision+1
    changes=[Change(revision=rev,decision_id=n.id,previous=n,current=nodes[n.id])
             for n in session.decisions if n != nodes[n.id]]
    updated=DesignSession.model_validate({**session.model_dump(),'revision':rev,'decisions':list(nodes.values()),
        'history':[c.model_dump() for c in session.history+changes], 'confirmed_revision':None})
    return {'session':updated.model_dump(),'frontier':frontier(updated),'invalidated':sorted(invalidated)}

def compile_game_design(session: DesignSession) -> dict:
    result=frontier(session)
    required={'scope','experience','meaning','agency','conditions','feedback','loop','experiment'}
    missing=sorted(required - {n.id for n in session.decisions})
    state='draft' if missing else ('confirmed' if session.confirmed_revision == session.revision else ('awaiting_confirmation' if result['resolved'] else 'draft'))
    lines=[f'# 策划规格 · {session.session_id}',f'修订：{session.revision}；访谈状态：{state}',
           '\n## 原始请求',session.original_request,
           '\n以下内容按调用方提供的问答编译；不代表证据已核实或已实际试玩。']
    for n in session.decisions:
        lines += [f'\n## {n.id} · {n.topic}',f'前提：{", ".join(n.depends_on) or "无"}',
                  f'状态：{n.status}；依据：{n.basis or "未提供"}',n.answer or '待回答：'+n.question]
        if n.locator: lines.append('来源定位：'+n.locator)
    return {'session_id':session.session_id,'revision':session.revision,'status':state,
            'experience_status':'untested','ready_for_implementation':state=='confirmed','missing_sections':missing,
            'markdown':'\n\n'.join(lines),'frontier':result,
            'scope':'Declared interview completion only; not semantic completeness, evidence truth, or proof of fun'}
