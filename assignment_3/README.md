# Assignment 3: Power System Simulation

In Assignment 3 we are going to build a package with some low voltage (LV)
grid analytics functions.
You will need the functionality of [Assignment 1](../assignment_1/README.md) and 
[Assignment 2](../assignment_2/README.md) to do this assignment.

**You need to define the proper APIs including input data arguments for your package!**

## Input data

The following input data are provided from the user.
You need to define how the user can give these input data to your package (APIs).

* A LV grid in PGM input format
  * The grid has one MV/LV transformer.
  * The grid is constructed in meshed (ring) structure, but some lines are disconnected (`to_status` is `0`), so that its base state is in a tree-structure.
  * The grid consists of many `sym_load`, each representing one LV household. There are also many nodes without any `sym_load`.
* LV feeder IDs: a list of line IDs which are the beginning of the LV feeders.
* One-year (active and reactive) load profile of all the `sym_load` in the grid.
  * In the same format as in [Assignment 2](../assignment_2/README.md#input-data)
* A pool of one-year EV charging profiles
  * The profiles provide the active power curve per EV.
  * The reactive power is assumed to be always zero.
  * The number of profiles is at least as many as the number of `sym_load` in the grid.

### Example drawing

See below an example drawing of such a LV grid.

```
source_0
    |
  node_1 
    |
transformer_2
    |
  node_3-----------------------------------------------
            |                                        |
          line_4                                  line_5
            |                                        |
          node_6--line_8--node_9-sym_load_10      node_7--line_11--node_12-sym_load_13
            |                                        |
          line_14                                 line_15
            |                                        |
          node_16--line_18--node_19-sym_load_20   node_17--line_21--node_22-sym_load_23
            |                                        |
            -----------line_24(disconnected)----------                           
```

In the example grid above we have a ring-constrcuted LV grid,
with `line_24` disconnected.
So its initial state is in radial structure.

The LV feeder IDs is the list of Line IDs of the beginning of the feerders, which is in this case `[4, 5]`.

There are 4 `sym_load` in the LV grid. However, there are 10 `node` in the grid.

## Functionalities

We expect you to implement the following functionalities.
You need to design how the functionalities are organized in some reasonable abstractions,
e.g., Python classes or independent functions.

**NOTE: the funtionalities are independent from each other. For example, for optimal tap position analysis, you need to analyse the original grid with house profile, WITHOUT the EV profile.**

### Input data validity check

Check the following validity criteria for the input data. 
Raise or passthrough relevant errors.

* The LV grid should be a valid PGM input data.
* The LV grid has exactly one `transformer`, and one `source`.
* All IDs in the LV Feeder IDs are valid line IDs.
* All the lines in the LV Feeder IDs have the `from_node` the same as the `to_node` of the `transformer`.
* The grid is fully connected in the initial state.
* The grid has no cycles in the initial state.
* The timestamps are matching between the active load profile, reactive load profile, and EV charging profile.
* The IDs in active load profile and reactive load profile are matching.
* The IDs in active load profile and reactive load profile are valid IDs of `sym_load`.
* The number of EV charging profile is at least the same as the number of `sym_load`.

### EV penetration level

Given a (user-provided) input of electrical vehicle (EV) penetration level,
i.e. the percentage of houses which has EV charged at home,
randomly add EV charging profiles to the houses according to the following creteria.

* The number of EVs per LV feeder should be `round_down[penetration_level * total_houses / number_of_feeders]`.
  * For example, given
    * number of houses: 150
    * number of feeders: 7
    * penetration level: 20%
    * The number of EVs per LV feeder should be: `round_down(20% * 150 / 7) = 4`
* Within a LV feeder, randomly select houses which will have EVs.
  *  You need to use the graph function from Assignment 1 to know which houses belong to which feeder.
* For each selected house with EV, randomly select an EV charging profile to add to the `sym_load` of that house.
  * You should not assign the same EV profile more than once. 
  * That's why in the input data number of EV charging profile is at least the same as the number of `sym_load`.

After assignment of EV profiles, run a time-series power flow as in Assignment 2, return the two aggregation tables.

### Optimal tap position 

In this functionality, the user would like to optimize the tap position of the transformer in the LV grid.

* The functionality returns the optimal tap position of the transformer by repeating time-series power flow calculation of the whole year for all possible tap positions.
* See the [example notebook](https://power-grid-model.readthedocs.io/en/stable/examples/Transformer%20Examples.html) for how to work with transformers in PGM.
* After the power flow calculation with all possible tap positions, we should return the optimal tap position by
  * The minimal total energy loss of all the lines and the whole year.
  * The minimal (averaged acroos all nodes) deviation of (max and min) p.u. node voltages with respect to 1 p.u.
* You need to design the API to let the user select what the optimization creteria is.

### N-1 calculation

In this functionality, the user would like to know alternative grid topology when a given line is out of service.
The user will provide the Line ID which is going to be out of service.

* If the given Line ID is not a valid `line`, raise proper error.
* If the given Line ID is not connected at both sides in the base case (`from_status` and `to_status` should be both `1`), raise proper error.
* You need to disconnect the designated line, set both `from_status` and `to_status` to `0`. And find list of Line IDs which are currently disconnected, and can be connected to make the grid fully connected again. Tip: use the graph function from Assignment 1.
* For each alternative `line` to be connected (set `to_status` to `1`), run the time-series power flow for the whole year.
* Return a table to summarize the results, each row in the table is one alternative scenario. The following columns are needed:
  * The alternative Line ID to be connected
  * The maximum loading among of lines and timestamps
  * The Line ID of this maximum
  * The timestamp of this maximum
* If there are no alternatives, it still should return an empty table with the correct data format and heading. You should test this behaviour in the unit tests.

## Testing with randomness

In the functionality of EV charging you need to randomly assign the EV profile.
To make the test reproducible, you can define random seed in your function argument.
In your test, you can set a fixed random seed so that your test can always produce the same data.
See [this faq](https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do) for an exaplanation of random seed.

## Test and demo datasets (work in progress)

We provide two datasets in the [SharePoint](https://tuenl.sharepoint.com/:f:/s/5XWG0-PowerSystemCalculationandSimualtion/Ejs9LjM7lulOtVgqstXVh7UBc4ifbYb1WQ5s2q_G0zXq3g?e=fGt80Y).

* The `small_network` is for testing purpose. You should use it in your test code.
  * **No expeted output is provided for this assignment. You need to make the expected output by yourself in the test, either via another script or manually.**
* The `big_network` is for demo purpose. You should use it in your Jupyter Notebook presentation.

Just as [Assignment 2](../assignment_2/README.md#test-datasets), the network data is in PGM JSON format, and the load/EV profiles are in `parquet` format.

In each network case, the `meta_data.json` file describes the important information of the network, including the LV feeders.

**NOTE: The EV charging profile does not have `sym_load` IDs in the column header. They are just sequence numbers of the pool. Assigning the EV profiles to `sym_load` is part of the assignment tasks.**
