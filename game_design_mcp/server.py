"""MCP stdio interface. Tool requests never execute shell code or write files."""
from mcp.server.fastmcp import FastMCP
from . import core
from . import planning
from . import __version__
from .planning import DesignSession, DesignAnswer, Text, NodeId
from .core import EffectSpec, CombatSpec, DecisionCard, SystemSpec, TransferSpec, UiSpec

mcp = FastMCP("game-design-skills-mcp")

@mcp.tool()
def list_capabilities() -> dict:
    """Discover versioned tools, skill documents and validation boundaries."""
    return {"version": __version__, "skills": core.list_skills(), "tools": [
        "get_skill", "create_effect_bundle", "calculate_combat", "validate_decision_card",
        "audit_system", "audit_transfer", "generate_ui_tokens",
        "start_design_interview", "advance_design_interview", "compile_game_design"],
        "limitations": "Deterministic helpers, not autonomous game design or proof of fun"}

@mcp.tool()
def get_skill(skill_id: str, document: str = "SKILL.md") -> str:
    """Read an allowlisted bundled skill/reference. List capabilities for valid paths."""
    return core.read_skill(skill_id, document)

@mcp.tool()
def create_effect_bundle(spec: EffectSpec) -> dict:
    """Return runnable Canvas impact/burst/pulse code and validated bounded configuration."""
    return core.effect_bundle(spec)

@mcp.tool()
def calculate_combat(spec: CombatSpec) -> dict:
    """Calculate deterministic subtractive damage, hit count and TTK in seconds."""
    return core.combat(spec)

@mcp.tool()
def validate_decision_card(card: DecisionCard) -> dict:
    """Validate the eight-field decision card and evidence presence; not evidence truth."""
    return core.validate_card(card)

@mcp.tool()
def audit_system(spec: SystemSpec) -> dict:
    """Check finite state graph references, reachability, ambiguity and nonterminal dead ends."""
    return core.audit_system(spec)

@mcp.tool()
def audit_transfer(spec: TransferSpec) -> dict:
    """Report missing/partial experience mappings without claiming actual pleasure transfer."""
    return core.audit_transfer(spec)

@mcp.tool()
def generate_ui_tokens(spec: UiSpec) -> dict:
    """Generate responsive layout CSS and choose black/white button text by contrast."""
    return core.ui_tokens(spec)

@mcp.tool()
def start_design_interview(original_request: Text, session_id: NodeId = 'design-001') -> dict:
    """Create an experience-theory decision tree and the current question frontier."""
    session = planning.start_design_interview(original_request, session_id)
    return {'session':session.model_dump(), 'frontier':planning.frontier(session)}

@mcp.tool()
def advance_design_interview(session: DesignSession, answers: list[DesignAnswer], confirm_revision: int | None = None) -> dict:
    """Apply one answer round; reopen descendants on revision. Confirm only after human review."""
    return planning.advance_design_interview(session, answers, confirm_revision)

@mcp.tool()
def compile_game_design(session: DesignSession) -> dict:
    """Compile supplied decisions into a draft or confirmed spec; never certifies actual player experience."""
    return planning.compile_game_design(session)

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
