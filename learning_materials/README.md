# Learning materials (work in progress)

## Software engineering

* Python environments and IDE (vscode recommended)
  * Configure in Windows
    * Configure natively in Windows
      * Install Python: Download the latest version of Python from the official website (https://www.python.org/downloads/) and run the installer. During installation, make sure to check the box that says "Add Python to PATH" to easily access Python from the command line.
      * Install VSCode: Download and install Visual Studio Code from the official website (https://code.visualstudio.com/).
      * Install the Python extension for VSCode: Open VSCode. Go to the Extensions view by clicking on the square icon on the sidebar or pressing Ctrl+Shift+X. Search for "Python" in the Extensions Marketplace. Click on "Install" next to the "Python" extension offered by Microsoft.
      * Open the project folder in VSCode: Go to File > Open Folder (or press Ctrl+K Ctrl+O) and select the project folder.
      * Set up a virtual environment (optional but recommended): Open the integrated terminal in VSCode by going to View > Terminal. Run the following command to install the virtual environment tool: `pip install virtualenv`. Navigate to your project folder in the terminal. Create a virtual environment by running: `virtualenv venv`. Activate the virtual environment: `.\venv\Scripts\activate`. Install dependencies: If your project requires any external packages, you can install them using pip while your virtual environment is activated. For example: `pip install <package_name>`.
      * Start coding
    * Use WSL + vscode
  * Configure in macOS
* Python classes, encapsulation
* Make small re-usable functions
* Type hint
* In-code docstring
* Test using pytest (include test exception)
* Code style, code quality
* Licenses of dependencies

## Collaboration

* Version control (git)
* Pull Request
* CI/CD check with GitHub Actions

## Scientific Python

* vectorization code
* numpy
* scipy
* pandas

## Graph theory

* directed, undirected graph
* DFS, BFS search
* Connected components
* Cycle finding

## Graph library suggestion

* networkx
* scipy.sparse.csgraph

## Power Grid Model

* run power flow
* (de-)serialization

## Presentation

* Jupyter Notebook
* plotting library (matplotlib, plotly, ...)
