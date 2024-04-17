# Assignments of Power System Computation and Simulation

This repository describes the assignments for the lecture Power System Computation and Simulation.
We also provide some links to the relevant learning materials (tutorials/videos).

## Assignments

We have in total three assignments. They will be also explained during the lecture.
See the links below for each individual assignment.

* [Assignment 1](./assignment_1/README.md)
* [Assignment 2](./assignment_2/README.md)
* [Assignment 3](./assignment_3/README.md)

You need to finish the assignments one by one in the given order.
Because later assignments depend on the result of earlier assignments.

### API

In the assignments the required functionalities are described.
In principle, you are responsible to define proper application programming interfaces (APIs)
so that users of the package can use the functionality.
You need to make the design choices such as defining classes or independent functions, etc.

To help you to get started, in Assignment 1 we define the APIs for you as an example.
So you just have to implement the required functionalities.
In the other two assignments you need to define your own APIs.

**NOTE: even for assignment 1, the given API is just an advice. 
You are free (and you probably should if you would like to get a high score) to choose a different (and more efficient) API.**

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
Therefore, in each assignment, we explicitly describe that the package needs to check certain some invalid input.
And all these checks have to be properly tested.

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

### License

When you add more open-source packages as the dependecies of your package, 
be sure to check whether their open-source licenses are compatible 
with the license of your package (BSD).

## Final presentation

For the final presentation, you should use a Jupyter Notebook to demo the functionalities of the three assignments.
We have already created an empty skeleton of the notebook in `example/final_presentation.ipynb` in your repository.
You just have to fill in your demo presentation in the notebook.
Your notebook should include:

* Some structured markdown descriptions of the package and how to use it.
* Some codes to demo the usage of the package.
* Some figures to visualize the results of the demo.

The notebook should be readable for someone who want to learn how to start to use your package, see an 
[example](https://power-grid-model.readthedocs.io/en/stable/examples/Power%20Flow%20Example.html)
of such a notebook for `power-grid-model`.

Besides the notebook, you can optionally use PowerPoint slides and/or show some source code.
You need to also reflect the whole assignment to explain the lessons you have learned, e.g.,
technical skills and/or collaboration skills.

**Each team member has to present part of the work duing the final day.**


## Learning materials

See [Learning materials](./learning_materials/README.md) for a list of useful resources.
