"""
This is a skeleton for the graph processing assignment.

We define a graph processor class with some function skeletons.
"""

from typing import List, Tuple


class IDNotFoundError(Exception):
    pass


class InputLengthDoesNotMatchError(Exception):
    pass


class IDNotUniqueError(Exception):
    pass


class GraphNotFullyConnectedError(Exception):
    pass


class GraphCycleError(Exception):
    pass


class GraphProcessor:
    """
    General documentation of this class.
    You need to describe the purpose of this class and the functions in it.
    """

    def __init__(
        self,
        vertex_ids: List[int],
        edge_ids: List[int],
        edge_vertex_id_pairs: List[Tuple[int, int]],
        edge_enabled: List[bool],
        source_vertex_id: int,
    ) -> None:
        """_summary_

        Args:
            vertex_ids: _description_
            edge_ids: _description_
            edge_vertex_id_pairs: _description_
            edge_enabled: _description_
            source_vertex_id: _description_
        """
        # put your implementation here
        pass

    def find_downstream_vertices(self, edge_id: int) -> List[int]:
        """_summary_

        Args:
            edge_id: _description_

        Returns:
            _description_
        """
        # put your implementation here
        pass

    def find_alternative_edges(self, disabled_edge_id: int) -> List[int]:
        """_summary_

        Args:
            disabled_edge_id: _description_

        Returns:
            _description_
        """
        # put your implementation here
        pass
