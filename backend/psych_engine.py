class PsychEngine:
    def __init__(self):
        # Define Ideals (The "Ought" state)
        self.ideals = {
            "Aiden": {"save_ria": 10, "distrust_royalty": 8, "protect_innocent": 5},
            "Black Apostle": {"purify_world": 10}
        }

    def calculate_tension(self, character, current_situation_tags):
        """
        Calculates Tension based on conflict between Ideal World and Actual World.
        """
        tension_score = 0
        char_ideals = self.ideals.get(character, {})
        
        if not char_ideals:
            return 0 # No profile

        for tag in current_situation_tags:
            # Conflict Logic based on tags
            
            # Scenario: Ria is in danger
            if tag == "ria_danger" and "save_ria" in char_ideals:
                tension_score += char_ideals["save_ria"] * 1.5 # Critical threat
            
            # Scenario: Forced to work with Royalty
            if tag == "cooperate_royalty" and "distrust_royalty" in char_ideals:
                tension_score += char_ideals["distrust_royalty"]
            
            # Scenario: Innocents harmed
            if tag == "innocents_hurt" and "protect_innocent" in char_ideals:
                tension_score += char_ideals["protect_innocent"]
                
        return tension_score

    def suggest_action(self, character, tension_score):
        """
        Suggests dramatic actions if tension is high.
        """
        if tension_score > 20:
             return f"⚠️ [Psych Warning] {character}'s Tension is Critical ({tension_score}). He is likely to act irrationally or violently. Consider a breakdown or rage outburst."
        if tension_score > 10:
            return f"⚠️ [Psych Warning] {character}'s Tension is High ({tension_score}). He will be hesitant or aggressive."
            
        return "Psychological State: Stable."
