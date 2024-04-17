# Learning materials (work in progress)

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
