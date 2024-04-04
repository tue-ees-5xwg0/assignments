# Assignment 2: Power Grid Model (work in progress)


## Input data

* A LV grid in PGM input format
  * The grid has one MV/LV transformer.
  * The grid is constructed in meshed structure, but some lines are disconnected so its original state is in tree-structure.
  * The grid consists of many `sym_load`, each representing one LV household.
* One-year (active and reactive) load profile of all the `sym_load` in the grid, 15 minutes for a year

## Functionalities

* Construct PGM using the input data
* Create a PGM batch update dataset with the load profile
* Run time-series (batch) power flow calculation
* Aggregate the results in the following way:
* 