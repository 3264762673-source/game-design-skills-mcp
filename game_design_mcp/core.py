"""Deterministic capability implementations; no filesystem writes or network calls."""
from pathlib import Path
from typing import Literal
import math
from pydantic import BaseModel, ConfigDict, Field

DATA = Path(__file__).parent / "data"

class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, allow_inf_nan=False)

class EffectSpec(StrictModel):
    effect: Literal["impact", "burst", "pulse"] = "impact"
    duration_ms: int = Field(default=240, ge=40, le=2000)
    radius_px: float = Field(default=36, ge=1, le=160)
    particles: int = Field(default=12, ge=0, le=48)
    color: str = Field(default="#65d6ff", pattern=r"^#[0-9a-fA-F]{6}$")
    reduced_motion: bool = False

class CombatSpec(StrictModel):
    hp: float = Field(gt=0, le=1e12)
    attack: float = Field(gt=0, le=1e9)
    defense: float = Field(default=0, ge=0, le=1e9)
    multiplier: float = Field(default=1, gt=0, le=1000)
    minimum_damage: float = Field(default=1, gt=0, le=1e9)
    interval_seconds: float = Field(default=1, gt=0, le=3600)
    first_hit_seconds: float = Field(default=0, ge=0, le=3600)

class DecisionCard(StrictModel):
    trigger: str = Field(min_length=1, max_length=2000)
    hypotheses: list[str] = Field(min_length=1, max_length=10)
    check: str = Field(min_length=1, max_length=2000)
    change: str = Field(min_length=1, max_length=2000)
    exclusions: str = Field(min_length=1, max_length=2000)
    expected: str = Field(min_length=1, max_length=2000)
    rollback: str = Field(min_length=1, max_length=2000)
    sources: list[str] = Field(min_length=1, max_length=20)
    status: Literal["hypothesis", "observed", "compared"] = "hypothesis"
    evidence: list[str] = Field(default_factory=list, max_length=20)

class Transition(StrictModel):
    source: str = Field(min_length=1, max_length=100)
    action: str = Field(min_length=1, max_length=100)
    target: str = Field(min_length=1, max_length=100)
    feedback: str = Field(min_length=1, max_length=500)

class SystemSpec(StrictModel):
    initial: str = Field(min_length=1, max_length=100)
    states: list[str] = Field(min_length=1, max_length=100)
    terminal: list[str] = Field(default_factory=list, max_length=100)
    transitions: list[Transition] = Field(max_length=500)

class Mapping(StrictModel):
    condition: str = Field(min_length=1, max_length=500)
    action: str = Field(min_length=1, max_length=500)
    feedback: str = Field(min_length=1, max_length=500)
    status: Literal["mapped", "partial", "missing", "unknown"]

class TransferSpec(StrictModel):
    pleasure: str = Field(min_length=1, max_length=1000)
    mappings: list[Mapping] = Field(min_length=1, max_length=50)
    evidence: list[str] = Field(default_factory=list, max_length=20)

class UiSpec(StrictModel):
    accent: str = Field(default="#2563eb", pattern=r"^#[0-9a-fA-F]{6}$")
    density: Literal["comfortable", "compact"] = "comfortable"
    radius_px: int = Field(default=12, ge=0, le=32)

def list_skills():
    return [{"id": p.name, "files": [f.relative_to(p).as_posix() for f in sorted(p.rglob('*')) if f.is_file()]}
            for p in sorted((DATA / "skills").iterdir()) if p.is_dir()]

def read_skill(skill_id: str, document: str = "SKILL.md"):
    allowed = {s["id"]: s["files"] for s in list_skills()}
    if document not in allowed.get(skill_id, []):
        raise ValueError("Unknown skill or document; use list_skills first")
    return (DATA / "skills" / skill_id / document).read_text(encoding="utf-8")

def effect_bundle(spec: EffectSpec):
    return {"version": "0.1.0", "config": spec.model_dump(),
            "files": {name: (DATA / "runtime" / name).read_text(encoding="utf-8")
                      for name in ["effects.js", "demo.html"]},
            "usage": "Save both files together, open demo.html; or load effects.js as a script and call GameFeedback.createFeedback(canvas).emit(event, config).",
            "constraints": ["Presentation only; never changes damage or simulation time", "Requires confirmed hit event", "Max 32 simultaneous effects", "No global camera shake or fullscreen flash"],
            "status": "code-tested; player experience unvalidated"}

def combat(spec: CombatSpec):
    damage = max(spec.minimum_damage, spec.attack * spec.multiplier - spec.defense)
    hits = math.ceil(spec.hp / damage)
    return {"damage_per_hit": damage, "hits": hits,
            "ttk_seconds": spec.first_hit_seconds + (hits - 1) * spec.interval_seconds,
            "formula": "max(minimum_damage, attack * multiplier - defense)",
            "assumptions": ["deterministic hits", "no crit/miss/regeneration/shield", "explicit first-hit time"],
            "status": "calculated, not playtested"}

def validate_card(card: DecisionCard):
    issues = []
    if any(not s.strip() for s in card.hypotheses + card.sources + card.evidence):
        issues.append("List entries must contain meaningful non-whitespace text")
    if any(not getattr(card, k).strip() for k in ['trigger','check','change','exclusions','expected','rollback']):
        issues.append("Card fields cannot be whitespace")
    if card.status != "hypothesis" and not card.evidence:
        issues.append("Observed/compared status requires evidence references")
    return {"valid": not issues, "issues": issues, "scope": "Structure and evidence presence only; does not verify truth or fun"}

def audit_system(spec: SystemSpec):
    states = set(spec.states)
    issues = []
    if len(states) != len(spec.states): issues.append("Duplicate states")
    if spec.initial not in states: issues.append("Initial state is undefined")
    if not set(spec.terminal) <= states: issues.append("Terminal state is undefined")
    seen = set()
    for t in spec.transitions:
        if t.source not in states or t.target not in states: issues.append("Transition references undefined state")
        key = (t.source, t.action)
        if key in seen: issues.append("Ambiguous action in state: " + str(key))
        seen.add(key)
    reached = {spec.initial} & states
    while True:
        new = reached | {t.target for t in spec.transitions if t.source in reached and t.target in states}
        if new == reached: break
        reached = new
    unreachable = sorted(states - reached)
    dead_ends = sorted(s for s in reached if s not in spec.terminal and not any(t.source == s for t in spec.transitions))
    return {"valid": not issues and not unreachable and not dead_ends, "issues": issues,
            "unreachable": unreachable, "dead_ends": dead_ends,
            "scope": "Finite deterministic graph only; does not prove meaningful choices"}

def audit_transfer(spec: TransferSpec):
    gaps = [m.model_dump() for m in spec.mappings if m.status != "mapped"]
    return {"structurally_complete": not gaps, "gaps": gaps,
            "experience_status": "evidence supplied, requires human review" if spec.evidence else "unvalidated",
            "scope": "Checks declared correspondence; never concludes that the intended pleasure actually transfers"}

def ui_tokens(spec: UiSpec):
    rgb = [int(spec.accent[i:i+2], 16)/255 for i in (1,3,5)]
    linear = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in rgb]
    lum = sum(a*b for a,b in zip(linear,[.2126,.7152,.0722]))
    white, black = 1.05/(lum+.05), (lum+.05)/.05
    foreground = "#ffffff" if white >= black else "#000000"
    gap = 16 if spec.density == "comfortable" else 8
    css = f'''/* Generated component tokens. Validate actual layout and states in context. */
:root {{ --action: {spec.accent}; --on-action: {foreground}; --gap: {gap}px; --radius: {spec.radius_px}px; }}
.gd-stack {{ display: grid; gap: var(--gap); }}
.gd-grid {{ display: grid; gap: calc(var(--gap)*2); grid-template-columns: repeat(auto-fit,minmax(min(100%,18rem),1fr)); }}
.gd-card {{ padding: calc(var(--gap)*2); border: 1px solid #cbd5e1; border-radius: var(--radius); }}
.gd-button {{ background: var(--action); color: var(--on-action); min-height: 44px; padding: .6rem 1rem; border: 0; border-radius: var(--radius); }}
.gd-button:focus-visible {{ outline: 3px solid currentColor; outline-offset: 3px; }}
.gd-button:disabled {{ opacity: .55; cursor: not-allowed; }}
@media(prefers-reduced-motion:reduce) {{ .gd-button {{ transition: none; }} }}'''
    return {"css": css, "button_text_contrast": round(max(white,black),2),
            "scope": "Contrast covers opaque button colors only; no whole-page accessibility certification"}
