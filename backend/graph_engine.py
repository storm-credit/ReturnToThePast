try:
    import networkx as nx
except ImportError:
    class MultiDiGraph:
        def __init__(self):
            self.adj = {}

        def add_edge(self, u, v, **kwargs):
            if u not in self.adj:
                self.adj[u] = []
            self.adj[u].append((v, kwargs))

        def has_node(self, n):
            return n in self.adj

        def edges(self, n, data=False):
            if n not in self.adj:
                return []
            return [(n, v, d) for v, d in self.adj[n]]

    class nx:  # type: ignore
        MultiDiGraph = MultiDiGraph

import json

from project_root import resolve_project_path


class TemporalGraph:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.load_error = None
        self._load_from_json()

    def _load_from_json(self):
        try:
            path = resolve_project_path("lore_bible", "temporal_facts.json", start=__file__)
            if path.exists():
                with path.open("r", encoding="utf-8") as f:
                    data = json.load(f)
                for fact in data:
                    entity = fact.get("entity")
                    status = fact.get("status")
                    valid_at = fact.get("valid_at")
                    invalid_at = fact.get("invalid_at", 9999)
                    timeline = fact.get("timeline", "Current")
                    if entity and status and valid_at is not None:
                        self.add_event(
                            entity,
                            "has_status",
                            status,
                            valid_at,
                            status=status,
                            invalid_at=invalid_at,
                            timeline=timeline,
                        )
        except Exception as exc:
            self.load_error = str(exc)

    def add_event(self, entity, action, target, year, status="active", invalid_at=9999, timeline="Current"):
        event_id = f"{entity}_{action}_{year}"
        self.graph.add_edge(
            entity,
            target,
            key=event_id,
            relation=action,
            valid_at=year,
            invalid_at=invalid_at,
            status=status,
            timeline=timeline,
        )

    def query_state(self, entity, target_year):
        current_knowledge = []
        target_year = int(target_year)

        if not self.graph.has_node(entity):
            suffix = f" Warning: {self.load_error}" if self.load_error else ""
            return f"Entity '{entity}' not found in the timeline.{suffix}"

        for _, neighbor, data in self.graph.edges(entity, data=True):
            valid_at = int(data["valid_at"])
            invalid_at = int(data.get("invalid_at", 9999))
            if valid_at <= target_year < invalid_at:
                valid_until = "open" if invalid_at >= 9999 else str(invalid_at - 1)
                current_knowledge.append(
                    f"{valid_at}-{valid_until}: [{data.get('timeline', 'Current')}] "
                    f"{entity} {data['relation']} {neighbor} ({data['status']})"
                )

        if not current_knowledge:
            return f"No records found for {entity} before {target_year}."

        if self.load_error:
            current_knowledge.append(f"Warning: temporal facts load issue: {self.load_error}")

        return "\n".join(sorted(current_knowledge))
