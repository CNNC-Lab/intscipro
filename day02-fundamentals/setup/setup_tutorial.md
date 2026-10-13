# Setting up Python and running your first code
*Introduction to Scientific Programming, Day 2, Part 0*

This is the reference for the first hour of Day 2. If you install everything **before** class (see [`resources/before_day2.md`](../../resources/before_day2.md)), the first hour is spent running code instead of installing it. If something does not work, that is normal: we fix it together in class, and the troubleshooting section at the end covers the usual problems.

**What you will have at the end**
- Python 3.11 in its own *environment*, with the `conda` tool to manage it
- VS Code set up to run Python
- The ability to run code in four ways: the interactive prompt, a script from the terminal, VS Code, and (preview) a notebook
- A green result from `check_python.py`

**The big picture.** Three pieces work together, and almost every setup problem is about how they find each other:

| Piece | What it is | Examples |
|---|---|---|
| **Interpreter** | the program that reads and runs Python code | `python` |
| **Editor** | where you write the code, which is just text | VS Code |
| **Terminal** | where you type commands to run programs and manage environments | Anaconda Prompt, Terminal |

---

## 1. Install Python (Miniconda)

Miniconda installs Python plus `conda`, a tool that creates separate *environments* (isolated workspaces with their own Python and packages). You can use the full Anaconda Distribution instead; everything below works the same. Download from the Anaconda documentation (<https://docs.anaconda.com/miniconda/>), and pick the installer for your system.

### Windows
1. Download the Windows 64-bit installer and run it.
2. Choose **Just Me**. You do **not** need to tick "Add to PATH".
3. When it finishes, open the Start menu and search for **Anaconda Prompt** (it may be called "Anaconda Prompt (miniconda3)"). **Always use this window** for the commands in this course.
4. Type `python --version` and press Enter. You should see `Python 3.` followed by numbers.

> Do not use a plain Command Prompt or the Microsoft Store Python. If typing `python` opens the Microsoft Store, you are in the wrong window: use Anaconda Prompt.

### macOS
1. Download the installer for your chip: **Apple Silicon** (M1, M2, M3 and later) or **Intel**. If unsure: Apple menu, About This Mac.
2. Run the `.pkg` installer and accept the defaults.
3. Open a **new** Terminal (Cmd+Space, type Terminal).
4. Type `python --version` and `conda --version`. If `conda` is not found, run `~/miniconda3/bin/conda init zsh`, close the Terminal and open a new one.

### Linux
1. Download the Linux installer, then in a terminal: `bash Miniconda3-latest-Linux-x86_64.sh` (use the file name you downloaded).
2. Accept the licence, keep the default location, and answer **yes** when asked to initialise conda.
3. Close the terminal and open a new one. Check `python --version` and `conda --version`.

### What success looks like
```text
$ python --version
Python 3.12.4
$ conda --version
conda 24.5.0
```
The numbers will differ. The next step creates an environment with exactly Python 3.11.

*No conda?* If you cannot install conda, install Python 3.11 or newer from <https://www.python.org/downloads/> (on Windows tick **Add python.exe to PATH**) and use the `venv` instructions in section 4.

---

## 2. Install VS Code
1. Download VS Code from <https://code.visualstudio.com/> and install it with the default options.
2. Open VS Code, click the Extensions icon (four squares on the left, or Ctrl+Shift+X / Cmd+Shift+X), search for **Python** (publisher: Microsoft), and install it. It brings the helper extensions it needs.
3. Optional now, useful on Day 3: **Jupyter** (Microsoft).

---

## 3. The terminal in ten commands
A terminal is a text window where you tell the computer what to do. It always has a **current folder**, and most mistakes come from being in the wrong folder.

| What you want | Windows (Anaconda Prompt) | macOS / Linux |
|---|---|---|
| Where am I? | `cd` | `pwd` |
| List the files here | `dir` | `ls` |
| Go into a folder | `cd folder_name` | `cd folder_name` |
| Go up one folder | `cd ..` | `cd ..` |
| Go to my home folder | `cd %USERPROFILE%` | `cd ~` |
| Make a folder | `mkdir folder_name` | `mkdir folder_name` |
| Run Python | `python` | `python` |
| Run a script | `python script.py` | `python script.py` |
| Which Python is this? | `where python` | `which python` |
| Stop a running program | Ctrl+C | Ctrl+C |

Tips: press **Tab** to complete file and folder names; press the **up arrow** to bring back the previous command; if a path contains spaces, put it in quotes.

---

## 4. Create your environment
Download the course repository from GitHub (green **Code** button, then **Download ZIP**), unzip it somewhere you can find it, for example your Documents folder, and open the terminal in that folder (`cd` into it). You do not need Git yet; that is Day 3.

**With conda (recommended)**
```bash
conda env create -f environment-base.yml
conda activate scientific-programming
```
After `activate`, the terminal prompt starts with `(scientific-programming)`. That is how you know the environment is active. Check:
```bash
python --version        # Python 3.11.x
```
To leave the environment: `conda deactivate`. Next time, you only need `conda activate scientific-programming`.

**With venv (if you could not install conda)**
```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # macOS and Linux
pip install -r requirements-base.txt
```
The prompt starts with `(.venv)`.

The environment is minimal on purpose (Python and IPython). On Day 3 you add JupyterLab and learn how environments work; on Day 4 the same environment is extended with the scientific packages.

---

## 5. Four ways to run Python

### 5.1 The interactive prompt
Type `python` (or `ipython`, which is friendlier) in the terminal.
```text
>>> 2 + 3
5
>>> name = "Ada"
>>> print(f"Hello, {name}")
Hello, Ada
>>> exit()
```
Good for trying one thing quickly. Nothing is saved. To leave: `exit()` (or Ctrl+D on macOS and Linux, Ctrl+Z then Enter on Windows).

### 5.2 A script from the terminal
A script is a text file with Python code, usually ending in `.py`.
1. In the terminal, go to the folder with the script: `cd day02-fundamentals/setup`.
2. Run it: `python hello.py`.

If you get `can't open file ... No such file or directory`, you are in the wrong folder. Check with `pwd` (or `cd` on Windows) and `ls` (or `dir`).

### 5.3 VS Code
1. **File, Open Folder**, and choose the course folder (or any folder you work in).
2. Open `hello.py` from the file list on the left.
3. Select the interpreter: Command Palette (Ctrl+Shift+P / Cmd+Shift+P), type **Python: Select Interpreter**, choose the one that mentions `scientific-programming`.
4. Click the **play button** at the top right of the editor (Run Python File). The output appears in the terminal panel at the bottom (open it any time with Ctrl+`).

If the play button is missing or the wrong Python runs, the interpreter was not selected: repeat step 3 and look at the bottom-right corner of VS Code, which shows the active interpreter.

### 5.4 A notebook (preview)
A notebook mixes code, results and text in one document. We use them from Day 3, where we also install JupyterLab. For now: Google Colab (<https://colab.research.google.com/>) lets you try one in your browser.

| | Interactive prompt | Script | Notebook |
|---|---|---|---|
| Saved as a file | no | yes | yes |
| Good for | quick tests | programs you rerun | exploring and documenting |
| Starts fresh each run | n/a | yes | no (kernel keeps variables) |

---

## 6. Reading an error message
Python errors look scary but are very informative. Read them **from the bottom**:
```text
Traceback (most recent call last):
  File "broken_2.py", line 4, in <module>
    print("Twice as many:", neuron_cont * 2)
NameError: name 'neuron_cont' is not defined
```
1. **Last line**: the error type and what went wrong (`NameError`: a name Python does not know).
2. **Line above**: the file and line number where it happened (`broken_2.py`, line 4).
3. Look at that line for a typo, a missing piece, or the wrong thing.

| Message | Usually means | What to try |
|---|---|---|
| `SyntaxError` | the code is not valid Python (missing `:`, bracket or quote) | look at the line shown and the one before it |
| `NameError` | a variable name is misspelled or used before it is defined | compare spelling, run the lines above first |
| `ModuleNotFoundError` | the module name is wrong, or the package is not installed in this environment | check the spelling; check the prompt shows `(scientific-programming)` |
| `FileNotFoundError` | Python cannot find the file from the current folder | `cd` to the right folder, or use the right path |
| `'python' is not recognized` / `command not found` | the terminal cannot find Python | Windows: use Anaconda Prompt. macOS/Linux: open a new terminal, run `conda init` |
| `IndentationError` | lines are indented inconsistently | use 4 spaces for each level |
| `TypeError` | an operation does not make sense for those types, for example `"5" + 3` | print the values and their `type()` |

---

## 7. Checkpoint
Everyone should leave the first hour with these done:
1. `python --version` works in the terminal and shows Python 3.
2. The environment `scientific-programming` is created and active (prompt shows its name).
3. `python day02-fundamentals/setup/check_python.py` ends with `RESULT: ... ready`.
4. `hello.py` runs from the terminal **and** from VS Code.
5. You fixed the four broken scripts (Exercise 0.3 in the exercises).

**If you are stuck**: do not wait. Raise your hand, or use **Plan B**: open <https://colab.research.google.com/>, create a new notebook, and run your code in cells. You can follow the whole day that way, and we fix your computer after class.

---

## Troubleshooting

**`conda: command not found` (macOS, Linux)**
Open a new terminal. If it persists: `~/miniconda3/bin/conda init zsh` (macOS) or `~/miniconda3/bin/conda init bash` (Linux), then open a new terminal.

**`conda` is not recognised (Windows)**
You are not in the Anaconda Prompt. Open it from the Start menu.

**Typing `python` opens the Microsoft Store (Windows)**
Use the Anaconda Prompt instead of Command Prompt or PowerShell.

**`conda activate` does nothing or errors in PowerShell**
Use Anaconda Prompt. (Advanced: `conda init powershell`, then restart PowerShell.)

**VS Code runs a different Python**
Command Palette, **Python: Select Interpreter**, pick the `scientific-programming` one. Close the terminal panel and run again.

**`ModuleNotFoundError` for a name you did not misspell**
The package is not installed in the active environment. Check the prompt shows `(scientific-programming)`. We install packages from Day 3.

**Permission errors**
Do not use `sudo`. Work in a folder you own, such as Documents. Avoid folders synced by cloud tools while you are installing.

**The download or install is blocked by the university network or a managed laptop**
Use Plan B (Colab) and talk to us; we will find an alternative.

More general help: [`resources/troubleshooting.md`](../../resources/troubleshooting.md).

---

## Where next
- **Python Tutorial**: <https://docs.python.org/3/tutorial/>
- **VS Code and Python**: <https://code.visualstudio.com/docs/python/python-tutorial>
- **conda environments**: <https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html>
