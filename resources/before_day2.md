# Before Day 2: a 10-minute checklist

Day 2 starts with a hands-on hour on running code. If you do these four steps **before** class, we can spend that hour practising instead of installing. If something fails, **do not worry**: note what happened (a screenshot of the error is perfect) and bring it to class. Fixing setup problems is exactly what that hour is for.

Detailed instructions with screenshots-by-description for Windows, macOS and Linux: [`day02-fundamentals/setup/setup_tutorial.md`](../day02-fundamentals/setup/setup_tutorial.md).

## 1. Install Miniconda (Python)
Download the installer for your system from <https://docs.anaconda.com/miniconda/> and run it.
- **Windows:** choose *Just Me*, then open **Anaconda Prompt** from the Start menu (use it for all course commands).
- **macOS / Linux:** accept the defaults and open a **new** terminal afterwards.

Check: `python --version` shows a Python 3 version, and `conda --version` shows a version.

## 2. Install VS Code
Download from <https://code.visualstudio.com/>, install, then add the **Python** extension (Extensions icon, search "Python", publisher Microsoft).

## 3. Get the course files and create the environment
On the course GitHub page (<https://github.com/CNNC-Lab/intscipro>) click the green **Code** button, then **Download ZIP**, and unzip it in a folder you can find. In the terminal, go into that folder (`cd`) and run:
```bash
conda env create -f environment-base.yml
conda activate scientific-programming
```
The prompt should now start with `(scientific-programming)`.

## 4. Run the check
```bash
python day02-fundamentals/setup/check_python.py
```
It should end with a line starting `RESULT:`. Whatever it prints, bring it (or a photo of it) to class.

## Not able to install anything?
Bring your laptop anyway, or use the browser option: open <https://colab.research.google.com/> with a Google account and run `print("Hello")` in a cell. You can follow Day 2 that way.
