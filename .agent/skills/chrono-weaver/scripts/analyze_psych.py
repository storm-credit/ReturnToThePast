import sys
import os
import json

# Add backend to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../backend')))

from psych_engine import PsychEngine

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python analyze_psych.py <character> <tag1,tag2,...>")
        sys.exit(1)
        
    character = sys.argv[1]
    tags = sys.argv[2].split(',')
    
    psych = PsychEngine()
    tension = psych.calculate_tension(character, tags)
    print(psych.suggest_action(character, tension))
