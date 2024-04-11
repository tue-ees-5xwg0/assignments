# Assignment 3: Power System Simulation (work in progress)

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
  * In the same format as in [Assignment 2](../assignment_2/README.md)
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

Do time-series power flow calculation, return the results as in Assignment 2.

### N-1 calculation
