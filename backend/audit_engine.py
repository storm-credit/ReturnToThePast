import json
import os

class AuditEngine:
    def __init__(self):
        # Load rules from lore_bible/rules.json
        self.rules = self._load_rules()
        
    def _load_rules(self):
        try:
            path = os.path.join(os.getcwd(), "lore_bible", "rules.json")
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}

    def validate_causality(self, action: str, year: int) -> str:
        """
        Validates if an action violates causal rules or fixed points.
        SCORE Framework: State Consistency & Rule Enforcement.
        """
        constraints = self.rules.get("constraints", [])
        
        # 1. Check Explicit Constraints
        for constraint in constraints:
            trigger = constraint.get("trigger", "").lower()
            if trigger and trigger in action.lower():
                return f"❌ [SCORE Violation] Action '{action}' triggers constraint: {constraint.get('message')}"

        # 2. Check Temporal Paradoxes (Basic)
        # Example: Cannot use "Future Tech" in past unless specified
        forbidden = self.rules.get("forbidden_terms", [])
        for term in forbidden:
            if term.lower() in action.lower():
                return f"❌ [SCORE Violation] Term '{term}' is forbidden by world rules."

        return "✅ [SCORE Validated] Causality check passed."
