"""MCP stdio interface. Tool requests never execute shell code or write files."""
from mcp.server.fastmcp import FastMCP
from . import core
from .core import EffectSpec, CombatSpec, DecisionCard, SystemSpec, TransferSpec, UiSpec

mcp = FastMCP("game-design-skills-mcp")

@mcp.tool()
def list_capabilities() -> dict:
    """Discover versioned tools, skill documents and validation boundaries."""
    return {"version": "0.1.0", "skills": core.list_skills(), "tools": [
        "get_skill", "create_effect_bundle", "calculate_combat", "validate_decision_card",
        "audit_system", "audit_transfer", "generate_ui_tokens"],
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

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
