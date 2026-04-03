import datetime

try:
    import networkx as nx
except ImportError:
    # Fallback for environments without networkx
    class MultiDiGraph:
        def __init__(self): self.adj = {}
        def add_edge(self, u, v, **kwargs):
            if u not in self.adj: self.adj[u] = []
            self.adj[u].append((v, kwargs))
        def has_node(self, n): return n in self.adj
        def edges(self, n, data=False):
            if n not in self.adj: return []
            return [(n, v, d) for v, d in self.adj[n]]
    
    class nx:
        MultiDiGraph = MultiDiGraph

import json
import os

class TemporalGraph:
    def __init__(self):
        # Directed Multi-Graph (Entities + Relationships + Time Metadata)
        self.graph = nx.MultiDiGraph()
        self._load_from_json()

    def _load_from_json(self):
        """
        Loads temporal facts from lore_bible/temporal_facts.json
        """
        try:
            path = os.path.join(os.getcwd(), "lore_bible", "temporal_facts.json")
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for fact in data:
                        # Extract data fitting the add_event schema
                        entity = fact.get("entity")
                        status = fact.get("status")
                        valid_at = fact.get("valid_at")
                        # We use 'status' as the relation/action for simplicity in this loader
                        if entity and valid_at:
                            self.add_event(entity, "has_status", status, valid_at, status=status)
        except Exception as e:
            print(f"Warning: Failed to load temporal graph: {e}")

    def add_event(self, entity, action, target, year, status="active"):
        """
        Records an event at a specific time (year).
        e.g., add_event("Cole", "possesses", "Key", 1996)
        """
        event_id = f"{entity}_{action}_{year}"
        self.graph.add_edge(
            entity, target, 
            key=event_id,
            relation=action,
            valid_at=year,
            status=status  # active, destroyed, lost
        )

    def query_state(self, entity, target_year):
        """
        [GraphRAG Sim] Queries the state of an entity at a specific year.
        Excludes future events (valid_at > target_year) to prevent spoilers.
        """
        current_knowledge = []
        
        if not self.graph.has_node(entity):
            return f"Entity '{entity}' not found in the timeline."
            
        # Inspect all edges (relationships) connected to the entity
        for _, neighbor, data in self.graph.edges(entity, data=True):
            # Temporal Validity Check
            if int(data['valid_at']) <= int(target_year):
                current_knowledge.append(
                    f"{data['valid_at']} Year: {entity} {data['relation']} {neighbor} ({data['status']})"
                )
        
        if not current_knowledge:
            return f"No records found for {entity} before {target_year}."

        return "\n".join(sorted(current_knowledge))
