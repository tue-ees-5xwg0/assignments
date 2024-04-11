# Assignment 3: Power System Simulation (work in progress)

In Assignment 3 we are going to build a package with some low voltage (LV)
grid analytics functions.
You will need the functionality of [Assignment 1](../assignment_1/README.md) and 
[Assignment 2](../assignment_2/README.md) to do this assignment.

**You need to define the proper APIs including input data format for your package!**

## Basic Input data

* A LV grid in PGM input format
  * The grid has one MV/LV transformer.
  * The grid is constructed in meshed structure, but some lines are disconnected so its base state is in a tree-structure.
  * The grid consists of many `sym_load`, each representing one LV household.
* A list of line IDs which are the beginning of the LV feeders.
* One-year (active and reactive) load profile of all the `sym_load` in the grid
  * In the same format as in Assignment 2
* A pool of one-year EV charging profiles
  * The number of profiles is at least as many as the number of `sym_load` in the grid.

## Functionalities

### EV penatration level

Given an input of expected EV penatration level (how many houses have PVs), randomly select houses which will get the EVs, 
and randomly add EV charging profile to those houses. You should not assign the same profile to multiple houses.

The EVs need to be approximately evenly distributed to all the LV feeders.

### Optimal tap position 

Do time-series power flow calculation, return the results as in Assignment 2.

### N-1 calculation
