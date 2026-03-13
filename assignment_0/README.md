# Assignment 0: Preparation Tasks

This assignment contains three preparation tasks to set up your development environment and prepare for collaborative work.

**Important:** Install tools in the order listed in Task 1. GitHub Desktop login provides the authentication that VS Code will use to access repositories.

## Task 1: Install and Configure Required Tools

Install and configure the following tools in order:

### 1. GitHub Desktop

Download and install GitHub Desktop from [github.com/apps/desktop](https://github.com/apps/desktop) for your platform.

After installation, launch GitHub Desktop and **log in with your GitHub account**. You'll need to authenticate to access repositories and make commits.

### 2. uv (Package Manager)

Install `uv` using the command appropriate for your platform:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Verify installation:**
```bash
uv --version
```

### 3. Visual Studio Code

Download and install Visual Studio Code from [code.visualstudio.com](https://code.visualstudio.com).

---

## Task 2: Clone Repository and Run Tests

This task verifies that your repository is properly cloned and configured. The tools used here will be explained in detail in later assignments.

1. Use Visual Studio Code to clone the repository:
   - Open VS Code
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS)
   - Select "Git: Clone"
   - Enter the repository URL: `https://github.com/tue-ees-5xwg0/power-system-simulation-XXXX` (replace `XXXX` with your team name)
   - Select a location on your computer where you want to clone the repository
   - After cloning completes, VS Code will ask if you want to open the repository. Click **"Open"** to open it in VS Code

2. Install recommended extensions:
   - VS Code will prompt you to install recommended extensions for the project. Click **"Yes"** to install them.

3. Verify your setup by running the following commands in the VS Code terminal:

```bash
# Install project dependencies
uv sync

# Run project tests
uv run pytest

# Check code style
uv run ruff check

# Format code
uv run ruff format
```

If all commands complete successfully, your setup is correct and you're ready to proceed!

---

## Task 3: Add Your Name to the Author List

Each team member should:

1. **Create a new branch:**
   - Click on the branch icon in VS Code (bottom left corner, showing the current branch name)
   - Select "Create new branch"
   - Name your branch something descriptive like `add-[your-name]-to-authors` (replace `[your-name]` with your actual name)
   - Press Enter to create and switch to the new branch

2. **Edit the `pyproject.toml` file:**
   - Open the `pyproject.toml` file
   - Find the `authors` list
   - Add your name and email address in the following format:
     ```toml
     authors = [
         { name = "Your Name", email = "your.email@example.com" },
     ]
     ```

3. **Commit your changes:**
   - Open the Source Control panel (click the Git icon on the left sidebar, or press `Ctrl+Shift+G`)
   - Review your changes in the diff panel
   - Enter a commit message (e.g., "Add Your Name to authors")
   - Click the checkmark button to commit

4. **Push your branch:**
   - Click the "Publish Branch" button (or "Push" if the branch already exists remotely)
   - VS Code will push your branch to GitHub

5. **Create a pull request:**
   - Go to the repository on GitHub
   - You'll see a prompt to create a pull request for your newly pushed branch
   - Click "Create Pull Request"
   - Add a description if needed
   - Request review from your team members before merging

6. **After approval, merge and clean up:**
   - Once your pull request is approved, click "Merge pull request" on GitHub
   - In VS Code, switch back to the `main` branch by clicking the branch selector (bottom left) and selecting `main`
   - Delete your feature branch locally by opening the command palette (`Ctrl+Shift+P` or `Cmd+Shift+P`), searching for "Git: Delete Branch", selecting your branch name, and confirming the deletion

---

**Once all tasks are completed, you're ready to start working on the main assignments!**
