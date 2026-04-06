import json
from pathlib import Path
from typing import Dict, List

from project_root import resolve_project_path


class PsychEngine:
    def __init__(self):
        self.profiles: Dict[str, dict] = {}
        self.load_errors: List[str] = []
        self.legacy_ideals = {
            "aiden": {"save_ria": 10, "distrust_royalty": 8, "protect_innocent": 5},
            "protagonist": {"save_ria": 10, "distrust_royalty": 8, "protect_innocent": 5},
            "black_apostle": {"purify_world": 10},
        }
        self._load_profiles()

    def _normalize(self, value):
        if value is None:
            return None
        return str(value).strip().lower().replace(" ", "_")

    def _register_profile(self, key, profile):
        normalized = self._normalize(key)
        if normalized:
            self.profiles[normalized] = profile

    def _load_profiles(self):
        characters_dir = resolve_project_path("lore_bible", "characters", start=__file__)
        for path in sorted(Path(characters_dir).glob("*_psych.json")):
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:
                self.load_errors.append(f"{path.name}: {exc}")
                continue

            self._register_profile(path.stem.replace("_psych", ""), data)
            self._register_profile(data.get("character"), data)
            self._register_profile(data.get("character_id"), data)
            self._register_profile(data.get("name"), data)

    def _get_profile(self, character):
        normalized = self._normalize(character)
        if not normalized:
            return None
        return self.profiles.get(normalized)

    def _calculate_legacy_tension(self, character, current_situation_tags):
        normalized = self._normalize(character)
        char_ideals = self.legacy_ideals.get(normalized, {})
        if not char_ideals:
            return 0

        tension_score = 0
        for tag in current_situation_tags:
            if tag == "ria_danger" and "save_ria" in char_ideals:
                tension_score += char_ideals["save_ria"] * 1.5
            if tag == "cooperate_royalty" and "distrust_royalty" in char_ideals:
                tension_score += char_ideals["distrust_royalty"]
            if tag == "innocents_hurt" and "protect_innocent" in char_ideals:
                tension_score += char_ideals["protect_innocent"]
        return int(tension_score)

    def calculate_tension(self, character, current_situation_tags):
        profile = self._get_profile(character)
        if profile and isinstance(profile.get("tension_triggers"), list):
            tension_score = int(profile.get("default_tension", 0))
            trigger_map = {
                item.get("tag"): int(item.get("tension_delta", 0))
                for item in profile["tension_triggers"]
            }
            for tag in current_situation_tags:
                tension_score += trigger_map.get(tag, 0)
            return tension_score

        return self._calculate_legacy_tension(character, current_situation_tags)

    def suggest_action(self, character, tension_score):
        profile = self._get_profile(character)
        likely_reaction = ""
        if profile and profile.get("max_tension_action") and tension_score >= 60:
            likely_reaction = f" Likely reaction: {profile['max_tension_action']}."

        if tension_score >= 80:
            return (
                f"[PSYCH CRITICAL] {character}'s tension is critical ({tension_score}). "
                f"Expect a drastic or self-destructive decision.{likely_reaction}"
            )
        if tension_score >= 50:
            return (
                f"[PSYCH HIGH] {character}'s tension is high ({tension_score}). "
                f"Expect impulsive, defensive, or aggressive behavior.{likely_reaction}"
            )
        if tension_score > 0:
            return f"[PSYCH GUARDED] {character} is under tension ({tension_score})."

        return "[PSYCH STABLE] No meaningful tension signal was found."

    def build_report(self, character, current_situation_tags):
        tension = self.calculate_tension(character, current_situation_tags)
        lines = [
            f"[PSYCH] Character: {character}",
            f"[PSYCH] Tags: {', '.join(current_situation_tags) if current_situation_tags else '-'}",
            f"[PSYCH] Tension: {tension}",
            f"[PSYCH] Verdict: {self.suggest_action(character, tension)}",
        ]
        if self.load_errors:
            lines.append(f"[PSYCH] Data warnings: {'; '.join(self.load_errors)}")
        return "\n".join(lines)
