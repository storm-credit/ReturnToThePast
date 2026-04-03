import sys
import os

# Add backend to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../backend')))

from graph_engine import TemporalGraph

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python get_temporal_context.py <entity> <year>")
        sys.exit(1)
        
    entity = sys.argv[1]
    year = int(sys.argv[2])
    
    graph = TemporalGraph()
    print(graph.query_state(entity, year))
