# Assignment 1: Graph Processing (work in progress)


## Input data

A graph input with:

* Vertex IDs
* Edge IDs
* Vertex ID pairs for all the edges
* Edge status (enabled, disabled)
* a source vertex ID

## Functionalities

* Initialize and check the graph, raise error if
  * The IDs are not unique
  * The length of Edge IDs, vertex ID pairs and status does not match
  * ID pairs in edge refer to non-existing vertex ID
  * Source vertex ID refers to a non-existing vertex ID
  * The graph is not fully connected at initial state
  * The graph is not acyclic (i.e. has cycles)
* Given an edge ID
  * Return the list of downstream vertex IDs, including the vertex inmmediately downstream of the edge
  * Raise error if the edge ID does not exist
* Given an enabled edge, do the following analysis
  * If the edge is going to be disabled, which (currently disabled) edge can be enabled to ensure that the graph is again fully connected and acyclic?
  * Return a list edge IDs of all possible solutions
