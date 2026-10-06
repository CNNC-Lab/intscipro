# Day 1 Setup Tutorial: Python Development Environment for Scientific Programming
*PhD Course in Integrative Neurosciences - Introduction to Scientific Programming*

## Overview
This tutorial will guide you through setting up a complete Python development environment suitable for scientific programming. We'll focus on tools that will serve you throughout your research career.

---

## Part 1: Python Installation & Package Management

### Option A: Anaconda (Recommended for Beginners)
**Why Anaconda?** Pre-configured for scientific computing, includes most packages you'll need, excellent package management.

#### Windows Installation:
1. **Download Anaconda**
   - Visit: https://www.anaconda.com/download
   - Download Python 3.11+ version (64-bit)
   - File size: ~500MB

2. **Installation Process**
   - Run the installer as Administrator
   - **Important**: Check "Add Anaconda to PATH" (despite warning)
   - Choose "Install for all users" if possible
   - Installation location: `C:\Anaconda3\` (default is fine)

3. **Verify Installation**
   - Open Command Prompt (Windows key + R, type `cmd`)
   - Type: `python --version`
   - Should show: `Python 3.11.x`
   - Type: `conda --version`
   - Should show conda version

#### macOS Installation:
1. **Download Anaconda**
   - Same website, choose macOS version
   - For M1/M2 Macs: Download Apple Silicon version
   - For Intel Macs: Download Intel version

2. **Installation**
   - Double-click the `.pkg` file
   - Follow installer instructions
   - Default installation path: `/opt/anaconda3/`

3. **Terminal Setup**
   - Open Terminal (Cmd + Space, type "Terminal")
   - Type: `conda init zsh` (for newer macOS) or `conda init bash`
   - Restart Terminal
   - Verify with `python --version` and `conda --version`

### Option B: Python.org + pip (Alternative)
- Download from https://www.python.org/downloads/
- Ensure "Add Python to PATH" is checked
- Use pip for package management later

---

## Part 2: VS Code Setup

### Installation
1. **Download VS Code**
   - Visit: https://code.visualstudio.com/
   - Download for your OS
   - Install with default settings

2. **Essential Extensions for Scientific Python**
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
   - Install these extensions:

   **Must-Have Extensions:**
   - `Python` (by Microsoft) - Core Python support
   - `Pylance` (by Microsoft) - Advanced Python language server
   - `Jupyter` (by Microsoft) - Notebook support in VS Code
   - `Python Debugger` (by Microsoft) - Debugging tools

   **Highly Recommended:**
   - `autoDocstring` - Generate docstrings automatically
   - `GitLens` - Enhanced Git capabilities
   - `Markdown All in One` - Better markdown support
   - `Rainbow CSV` - CSV file visualization
   - `Error Lens` - Inline error highlighting

### VS Code Configuration for Python
1. **Select Python Interpreter**
   - Open Command Palette (Ctrl+Shift+P / Cmd+Shift+P)
   - Type: "Python: Select Interpreter"
   - Choose your Anaconda Python (should show path like `~/anaconda3/bin/python`)

2. **Basic Settings Configuration**
   - Go to File > Preferences > Settings (or Code > Preferences > Settings on Mac)
   - Search for "python formatting provider"
   - Set to "black" (we'll install this later)

---

## Part 3: Terminal/Command Line Basics

### Windows Users
**Use Anaconda Prompt** (search in Start Menu) or **PowerShell**

### macOS/Linux Users
**Use Terminal** (built-in)

### Essential Commands for Scientific Programming
```bash
# Navigation
pwd                    # Print current directory
ls                     # List files (dir on Windows)
cd folder_name         # Change directory
cd ..                  # Go up one directory
cd ~                   # Go to home directory

# File operations
mkdir project_name     # Create new directory
touch filename.py      # Create new file (echo. > filename.py on Windows)

# Python/Conda commands
python --version       # Check Python version
conda list            # List installed packages
conda install package_name    # Install package
pip install package_name      # Alternative package installer

# Virtual environments (we'll cover this later)
conda create -n myenv python=3.11    # Create new environment
conda activate myenv                  # Activate environment
conda deactivate                      # Deactivate environment
```

---

## Part 4: Essential Scientific Python Packages

### Install Core Packages
Open Anaconda Prompt/Terminal and run:

```bash
# Core scientific stack (usually pre-installed with Anaconda)
conda install numpy pandas matplotlib seaborn scipy jupyter
```

### Verify Installation
Create a test script to verify everything works:

```python
# check_installation.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("All packages imported successfully!")
print(f"NumPy version: {np.__version__}")
print(f"Pandas version: {pd.__version__}")

# Create a simple plot to test matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title("Test Plot - Installation Successful!")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()
```

---

## Part 5: Project Structure Best Practices

### Recommended Directory Structure
```
your_research/
├── projects/
│   ├── project1/
│   │   ├── data/           # Raw data (never modify)
│   │   ├── notebooks/      # Jupyter notebooks for exploration
│   │   ├── scripts/        # Python scripts
│   │   ├── results/        # Output files, figures
│   │   └── README.md       # Project description
│   └── project2/
├── tools/                  # Reusable functions/modules
└── learning/              # Practice exercises, tutorials
```

---

## Part 6: First Steps Checklist

Before the next session, ensure you can:

- [ ] Open VS Code and create a new Python file
- [ ] Run Python code in VS Code (F5 or Ctrl+F5)
- [ ] Open a terminal/command prompt
- [ ] Navigate between directories using `cd`
- [ ] Install a Python package using `conda install` or `pip install`
- [ ] Import and use numpy, pandas, and matplotlib
- [ ] Create and save a simple plot

---

## Troubleshooting Common Issues

### "Python not found" or "conda not found"
- **Windows**: Ensure Python/Anaconda is added to PATH during installation
- **macOS**: Run `conda init` in terminal and restart terminal
- Try using full path: `/opt/anaconda3/bin/python` (macOS) or `C:\Anaconda3\python.exe` (Windows)

### VS Code not recognizing Python
- Use Command Palette (Ctrl+Shift+P) → "Python: Select Interpreter"
- Choose the Anaconda Python interpreter
- Restart VS Code

### Import errors
- Ensure you're using the correct environment: `conda list` to see installed packages
- Try installing missing packages: `conda install package_name`

### Permission errors (macOS/Linux)
- Don't use `sudo` with conda/pip
- Check file permissions: `ls -la`

---

## Resources for Further Learning

- **Official Python Tutorial**: https://docs.python.org/3/tutorial/
- **Anaconda Documentation**: https://docs.anaconda.com/
- **VS Code Python Tutorial**: https://code.visualstudio.com/docs/python/python-tutorial
- **Git Tutorial**: https://git-scm.com/docs/gittutorial (we'll cover this in Day 3)

---

*This tutorial is designed to get you started with confidence. Don't worry if everything doesn't work perfectly on the first try – debugging and troubleshooting are essential skills we'll develop throughout the course!*