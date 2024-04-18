# Learning materials

## Software engineering

* Python environments and IDE (vscode recommended)
  * Configure in Windows
    * Configure natively in Windows
      * Install Python: Download the latest version of Python from the official website (https://www.python.org/downloads/) and run the installer. During installation, make sure to check the box that says "Add Python to PATH" to easily access Python from the command line.
      * Install VSCode: Download and install Visual Studio Code from the official website (https://code.visualstudio.com/).
      * Install the Python extension for VSCode: Open VSCode. Go to the Extensions view by clicking on the square icon on the sidebar or pressing Ctrl+Shift+X. Search for "Python" in the Extensions Marketplace. Click on "Install" next to the "Python" extension offered by Microsoft.
      * Open the project folder in VSCode: Go to File > Open Folder (or press Ctrl+K Ctrl+O) and select the project folder.
      * Set up a virtual environment (optional but recommended): Open the integrated terminal in VSCode by going to View > Terminal. Create a virtual environment by running (depending on your Python version): `python3.12 -m venv .venv`. Activate the virtual environment: `.\venv\Scripts\activate`. 
      * Install dependencies: If your project requires any external packages, you can install them using pip while your virtual environment is activated. For example: `pip install <package_name>`.
      * Start coding
    * Use WSL + vscode
      * Installation of Python: You can install Python within WSL using the package manager of your Linux distribution (e.g., apt for Ubuntu). Open a terminal in your WSL instance and run: `sudo apt update` and
      `sudo apt install python3.12 python3-pip`.
      * Integration with VSCode: Visual Studio Code on Windows can seamlessly integrate with WSL. After installing VSCode on Windows, install the Remote - WSL extension. Open VSCode, and you'll see an icon in the bottom-left corner (green rectangle with a greater-than symbol) indicating that you're connected to WSL. Open a folder within WSL by navigating to it in the terminal and typing `code .`.
      * Setting up a virtual environment: `python3.12 -m venv venv` and `source venv/bin/activate`
      * Installing dependencies: Install Python packages using pip within the activated virtual environment: `pip install <package_name>`.
      * Running Python code: You'll be running Python code within the WSL environment, so ensure that you're executing commands within the WSL terminal in VSCode. Run/debug your Python code as usual within VSCode.
  * Configure in macOS
    * Install Python: macOS usually comes with Python pre-installed. However, it's recommended to install a separate version using a package manager like Homebrew or by downloading it from the official Python website. To install Python using Homebrew, open Terminal and run: `brew install python3`. 
    * Install Visual Studio Code (VSCode): Download and install Visual Studio Code from the official website (https://code.visualstudio.com/).
    * Install the Python extension for VSCode: Open VSCode. Go to the Extensions view by clicking on the square icon on the sidebar or pressing Cmd+Shift+X. Search for "Python" in the Extensions Marketplace. Click on "Install" next to the "Python" extension offered by Microsoft.
    * Open the project folder in VSCode: Open VSCode. Go to File > Open Folder (or press Cmd+O) and select the project folder.
    * Set up a virtual environment (optional but recommended): Open the integrated terminal in VSCode by going to View > Terminal. Create a virtual environment by running (depending on your Python version): `python3.12 -m venv .venv`. Activate the virtual environment: `.\venv\Scripts\activate`. 
    * Install dependencies: If your project requires any external packages, you can install them using pip while your virtual environment is activated. For example: `pip install <package_name>`.
    * Start coding
* Python classes: https://www.youtube.com/watch?v=ZDa-Z5JzLYM
* encapsulation: https://www.youtube.com/watch?v=GN1LR0UoFI4
* Make small re-usable functions: https://codefather.tech/blog/python-functions/
* Type hinting: https://www.pythontutorial.net/python-basics/python-type-hints/
* Documenting Python code: https://realpython.com/documenting-python-code/
* Test using pytest : https://realpython.com/pytest-python-testing/
* Test exeptions: https://pytest-with-eric.com/introduction/pytest-assert-exception/
* Code style, code quality: https://python.plainenglish.io/best-practices-for-python-code-quality-and-style-4059dd1a3b37
* Licenses of dependencies: you can only use packages that are compatible with BSD3, so no GPL packages. See https://www.mend.io/blog/license-compatibility/ and https://janelia-flyem.github.io/licenses.html

## Collaboration

* Version control (git): https://www.youtube.com/watch?v=USjZcfj8yxE
* Pull Request: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
* Branch protection rule: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
* CI/CD with GitHub Actions: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
* Tip: use pre-commit (https://stackoverflow.com/collectives/articles/71270196/how-to-use-pre-commit-to-automatically-correct-commits-and-merge-requests-with-g) to automatically format your code to the CI/CD standards

## Scientific Python

* vectorization: https://www.geeksforgeeks.org/vectorization-in-python/
* numpy: https://numpy.org/devdocs/user/quickstart.html
* scipy: https://docs.scipy.org/doc/scipy/tutorial/index.html
* pandas: https://pandas.pydata.org/docs/user_guide/index.html

## Graph theory

* directed vs undirected graph: https://www.geeksforgeeks.org/what-is-the-difference-between-an-undirected-and-a-directed-graph/
* Tree traversal: 
  * Breath-First Search: https://en.wikipedia.org/wiki/Breadth-first_search
  * Depth-First Search: https://en.wikipedia.org/wiki/Depth-first_search
* Connected components: https://en.wikipedia.org/wiki/Component_(graph_theory)
* Cycle detection: https://en.wikipedia.org/wiki/Cycle_detection

## Graph library suggestion

* networkx: https://networkx.org/documentation/stable/tutorial.html
* scipy.sparse.csgraph: https://docs.scipy.org/doc/scipy/reference/sparse.csgraph.html

## Sparse matrix
* sparse matrix representation: https://www.geeksforgeeks.org/sparse-matrix-representation/

## Power Grid Model

* run power flow: https://power-grid-model.readthedocs.io/en/stable/examples/Power%20Flow%20Example.html
* (de-)serialization: https://power-grid-model.readthedocs.io/en/stable/examples/Serialization%20Example.html

## Presentation

* Jupyter Notebook: https://realpython.com/jupyter-notebook-introduction/
* plotting library 
  * matplotlib: https://matplotlib.org/stable/tutorials/pyplot.html
  * plotly: https://plotly.com/python/getting-started/
  * ...
