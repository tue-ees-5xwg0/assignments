# Assignment 1: Graph Processing

In Assignment 1 we are building a simple graph processing class.
We build an undirected graph and implement two functionalties:
  * Find downstream vertices
  * Find alternative edges

Both functions will be used in later assignments.
You need to select proper graph algorithms to implement those two functions.
You are also supposed to write the code as efficient as possible,
so that the code can perform well with large datasets.

For this and only for this assignment, we provide a skeleton of the code
in [graph_processing.py](./graph_processing.py) including:
  * The input data definition
  * The API definition
  * The expected behaviour including error handling. In your test you need to test all the required error handling.
  * Some examples in the docstring of the function. In your test you should at least test these examples. You can of course add more test cases.

**NOTE: the given API is just an advice. 
You are free (and you probably should if you would like to get a high score) to choose a different (and more efficient) API.**

## Recommended graph packages

You are free to choose any graph packages, as long as the license is compatible. We recommend two famous packages:

  * [`networkx`](https://networkx.org/documentation/stable/index.html)
  * [`scipy.sparse.csgraph`](https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html)
