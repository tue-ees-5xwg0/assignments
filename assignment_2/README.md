# Assignment 2: Power Grid Model (work in progress)


## Input data

* A LV grid in PGM input format
* One-year (active and reactive) load profile of all the `sym_load` in the grid, 15 minutes for a year

## Functionalities

* Construct PGM using the input data
* Create a PGM batch update dataset with the load profile
* Run time-series (batch) power flow calculation
* Aggregate the results in the following two tables:
  * A table with each row representing a timestamp, with the following columns:
    * Timestamp
    * Maximum p.u. voltage of all the nodes for this timestamp
    * The node ID with the maximum p.u. voltage
    * Minimum p.u. voltage of all the nodes for this timestamp
    * The node ID with the minimum p.u. voltage
  * A table with each row representing a line, with the following columns:
    * Line ID
    * Loss of the line across the whole year in kWh.
    * Maximum laoding of the line across the whole year
    * Timestamp of this maximum loading moment
    * Minimum loading of the line across the whole year
    * Timestamp of this minimum loading moment
