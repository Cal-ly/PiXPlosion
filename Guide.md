# How to Set Up the PiXPlosion Project in Visual Studio Code

This guide will walk you through installing Python, setting up Visual Studio Code, and configuring your PiXPlosion project.

## 1. Install Python

1. Go to the [Python Downloads page](https://www.python.org/downloads/) and download the latest version of Python (as of November 2024, Python 3.13).
2. Run the installer:
   - **Windows**: Ensure you check the box for **Add Python to PATH** before clicking "Install Now."
   - **macOS/Linux**: Follow standard installation steps for your OS.
3. Verify the installation:
   - Open a terminal, command prompt or PowerShell (`WinTast + x, i`) and type:
     ```bash
     python --version
     ```
   - You should see the installed Python version (e.g., `Python 3.13.x`).

## 2. Set up Visual Studio Code from new

1. **Download and Install Visual Studio Code**:
   - Download VS Code from the [Visual Studio Code website](https://code.visualstudio.com/).
   - Follow the installation steps for your OS.

2. **Install Required Extensions**:
   - Open VS Code, go to the **Extensions** view by clicking the square icon in the sidebar or pressing `Ctrl+Shift+X`.
   - Search for and install these extensions:
     - **Python** by Microsoft (for Python support)
     - **Remote - SSH** (if you plan to connect remotely to the Raspberry Pi)
     - **Markdown Preview Enhanced** (for previewing Markdown files)
   
3. **Configure Python Interpreter**:
   - Open any Python file in your PiXPlosion project.
   - VS Code will prompt you to select a Python interpreter if not already set.
   - Choose the version you installed (e.g., `Python 3.13.x`).

## 3. Set up the PiXPlosion Project

1. **Clone or Open the Project**:
   - If you have the project in a repository, clone it:
     ```bash
     git clone <your-repo-url>
     ```
   - Or, open the existing folder directly in VS Code by navigating to **File > Open Folder**.

2. **Set Up a Virtual Environment** (recommended for Python projects, but optional):
   - Navigate to the project directory in your terminal:
     ```bash
     cd path/to/PiXPlosion
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**: `venv\Scripts\activate`
     - **macOS/Linux**: `source venv/bin/activate`
   - Confirm the environment is active by checking that `(venv)` appears in the terminal prompt.

3. **Install Project Dependencies**:
   - With the virtual environment activated, install dependencies:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the PiXPlosion Project**:
   - Make sure all setup steps are complete, and run your project:
     ```bash
     python main.py
     ```
   - Replace `main.py` with the actual entry point file name if it’s different.

## 4. Additional Tips

- **Using Remote SSH** (for working on a Raspberry Pi directly from VS Code):
  - Set up SSH access to your Raspberry Pi.
  - In VS Code, use the **Remote - SSH** extension to connect by selecting **Remote Explorer > SSH Targets** and adding your Pi’s IP address.

- **Previewing Markdown**:
  - Open any `.md` file in VS Code.
  - Press `Ctrl+Shift+V` to open the preview pane.
