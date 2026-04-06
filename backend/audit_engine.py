import json

from project_root import resolve_project_path


class AuditEngine:
    def __init__(self):
        self.load_error = None
        self.rules = self._load_rules()

    def _load_rules(self):
        try:
            path = resolve_project_path("lore_bible", "rules.json", start=__file__)
            with path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as exc:
            self.load_error = str(exc)
            return {}

    def validate_causality(self, action: str, year: int) -> str:
        constraints = self.rules.get("constraints", [])
        warnings = []

        if self.load_error:
            warnings.append(f"rules unavailable: {self.load_error}")

        for constraint in constraints:
            trigger = constraint.get("trigger", "").lower()
            if trigger and trigger in action.lower():
                suffix = f" Warning: {'; '.join(warnings)}." if warnings else ""
                return (
                    f"[SCORE VIOLATION] '{action}' in year {year} triggers constraint: "
                    f"{constraint.get('message')}.{suffix}"
                )

        forbidden = self.rules.get("forbidden_terms", [])
        for term in forbidden:
            if term.lower() in action.lower():
                suffix = f" Warning: {'; '.join(warnings)}." if warnings else ""
                return (
                    f"[SCORE VIOLATION] '{term}' is forbidden by world rules for year {year}.{suffix}"
                )

        if warnings:
            return f"[SCORE OK WITH WARNINGS] Causality check passed. {'; '.join(warnings)}"

        return "[SCORE OK] Causality check passed."
