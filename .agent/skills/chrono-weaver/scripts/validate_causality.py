import sys
import os

# Add backend to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../backend')))

from audit_engine import AuditEngine

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python validate_causality.py <action_description> <year>")
        sys.exit(1)
        
    action = sys.argv[1]
    try:
        year = int(sys.argv[2])
    except:
        year = 2024 # Default
        
    audit = AuditEngine()
    print(audit.validate_causality(action, year))
