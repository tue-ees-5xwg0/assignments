import networkx as nx
from typing import List, Tuple


class IDNotFoundError(Exception): pass
class InputLengthDoesNotMatchError(Exception): pass
class IDNotUniqueError(Exception): pass
class GraphNotFullyConnectedError(Exception): pass
class GraphCycleError(Exception): pass
class EdgeAlreadyDisabledError(Exception): pass


class GraphProcessor:
    """
    A class for processing undirected graphs with support for edge disabling and analysis.
    """

    def _init_(
        self,
        vertex_ids: List[int],
        edge_ids: List[int],
        edge_vertex_id_pairs: List[Tuple[int, int]],
        edge_enabled: List[bool],
        source_vertex_id: int,
    ) -> None:
        # Check uniqueness
        if len(set(vertex_ids)) != len(vertex_ids) or len(set(edge_ids)) != len(edge_ids):
            raise IDNotUniqueError()

        # Length checks
        if len(edge_ids) != len(edge_vertex_id_pairs) or len(edge_ids) != len(edge_enabled):
            raise InputLengthDoesNotMatchError()

        # ID validity checks
        if source_vertex_id not in vertex_ids:
            raise IDNotFoundError()
        for u, v in edge_vertex_id_pairs:
            if u not in vertex_ids or v not in vertex_ids:
                raise IDNotFoundError()

        # Store everything
        self.vertex_ids = vertex_ids
        self.edge_ids = edge_ids
        self.edge_vertex_id_pairs = edge_vertex_id_pairs
        self.edge_enabled = edge_enabled
        self.source_vertex_id = source_vertex_id

        # Maps
        self.edge_id_to_index = {eid: idx for idx, eid in enumerate(edge_ids)}
        self.edge_id_to_vertices = dict(zip(edge_ids, edge_vertex_id_pairs))

        # Build graph with only enabled edges
        self.graph = nx.Graph()
        self.graph.add_nodes_from(vertex_ids)
        for eid, (u, v), enabled in zip(edge_ids, edge_vertex_id_pairs, edge_enabled):
            if enabled:
                self.graph.add_edge(u, v, edge_id=eid)

        # Validation: connectivity and acyclic
        if not nx.is_connected(self.graph):
            raise GraphNotFullyConnectedError()
        if not nx.is_forest(self.graph):
            raise GraphCycleError()

    def find_downstream_vertices(self, edge_id: int) -> List[int]:
        if edge_id not in self.edge_id_to_index:
            raise IDNotFoundError()

        idx = self.edge_id_to_index[edge_id]
        if not self.edge_enabled[idx]:
            return []

        u, v = self.edge_vertex_id_pairs[idx]
        # Temporarily remove the edge
        G_temp = self.graph.copy()
        G_temp.remove_edge(u, v)

        # Determine which side is downstream (not closer to source)
        try:
            path_u = nx.shortest_path_length(G_temp, self.source_vertex_id, u)
        except nx.NetworkXNoPath:
            path_u = float('inf')
        try:
            path_v = nx.shortest_path_length(G_temp, self.source_vertex_id, v)
        except nx.NetworkXNoPath:
            path_v = float('inf')

        downstream_start = v if path_u < path_v else u
        try:
            reachable = nx.descendants(nx.bfs_tree(G_temp, downstream_start), downstream_start)
        except nx.NetworkXError:
            return []
        return list(reachable.union({downstream_start}))

    def find_alternative_edges(self, disabled_edge_id: int) -> List[int]:
        if disabled_edge_id not in self.edge_id_to_index:
            raise IDNotFoundError()

        idx = self.edge_id_to_index[disabled_edge_id]
        if not self.edge_enabled[idx]:
            raise EdgeAlreadyDisabledError()

        # Temporarily disable the edge
        u, v = self.edge_vertex_id_pairs[idx]
        G_temp = self.graph.copy()
        G_temp.remove_edge(u, v)

        if not nx.is_connected(G_temp):
            # Try re-adding each disabled edge and see if it helps
            alternatives = []
            for i, enabled in enumerate(self.edge_enabled):
                if not enabled:
                    alt_eid = self.edge_ids[i]
                    a, b = self.edge_vertex_id_pairs[i]
                    G_check = G_temp.copy()
                    G_check.add_edge(a, b, edge_id=alt_eid)
                    if nx.is_connected(G_check) and nx.is_forest(G_check):
                        alternatives.append(alt_eid)
            return alternatives
        else:
            return[] 