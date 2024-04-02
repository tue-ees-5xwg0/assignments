# Assignments of Power System Computation and Simulation

This repository describes the assignments for the lecture Power System Computation and Simulation.
We also provide some links to the relevant learning materials (tutorials/videos).

## Assignments

We have in total three assignments, they will be also explained during the lecture.
See the links below for each individual assignment.

* [Assignment 1](./assignment_1/README.md)
* [Assignment 2](./assignment_2/README.md)
* [Assignment 3](./assignment_3/README.md)

You need to finish the assignments one by one in the given order.
Because later assignments depend on the result of earlier assignments.

### Pull Requests

All the assignments have to be finished in the form of 
merging multiple Pull Requests (PRs) into the `main` branch of your repository (per team).

As a collaboration requirement, for each assignment, we require:

* Each team member should open at least one PR to contribute some part of the assignment. The team should decide internally how to divide the tasks.
* Each team member should at least post one meaningful review comment to all other PRs which is not opened by the person self.
* Each team member should react to all comments in his/her own PR. The reaction can simply a "done" if the comment is trivial, or can be extensive explaination if the comment is substantial.

### Test

The contributed code needs to be tested for both input and invalid input.
As a general suggestion, each single PR can contain a small part of the work including the test on this part.
One cannot test all the possible invalid situations. 
Therefore, in each assignemnt, we explicitly describe some invalid input which should be tested.
Everything else is optional.

### Code style and quality

The code style and quality needs to conform the predefined requiements. 
For code styling, you should use [`isort`](https://github.com/PyCQA/isort) 
and [`black`](https://github.com/psf/black)
to automatically format the code.

For code quality, you should use [`pylint`](https://github.com/pylint-dev/pylint) to check the code quality.
If you get errors, you need to inpect the error message and make the required adjustment.


### Automatic checks

Before you can merge a PR, the CI (GitHub Actions) automatically checks your tests, code style, and code quality.
You can only merge it if all of them have passed. 
Otherwise, please read the CI log to check the failure, and make relevant corrections.
