"""Check that Python runs on your computer and report what you are using.

Run it from a terminal:   python check_python.py
It uses only the Python standard library and prints PASS / WARN / FAIL lines.
If you see FAIL, copy the whole output into an email or show it to a helper.
"""
import os
import platform
import sys
from pathlib import Path

REQUIRED = (3, 11)
results = []


def report(status, message):
    results.append(status)
    print(f"[{status}] {message}")


print("=== Python check ===")
print(f"Operating system : {platform.system()} {platform.release()}")
print(f"Python version   : {platform.python_version()}")
print(f"Python program   : {sys.executable}")
print(f"Working folder   : {Path.cwd()}")
print()

# 1. Python version
version = sys.version_info[:2]
if version >= REQUIRED:
    report("PASS", f"Python {version[0]}.{version[1]} is recent enough (need {REQUIRED[0]}.{REQUIRED[1]} or newer)")
else:
    report("FAIL", f"Python {version[0]}.{version[1]} is too old: install Python {REQUIRED[0]}.{REQUIRED[1]} or newer")

# 2. Are we inside an environment (conda or venv)?
conda_env = os.environ.get("CONDA_DEFAULT_ENV")
in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
if conda_env and conda_env != "base":
    report("PASS", f"conda environment '{conda_env}' is active")
elif in_venv:
    report("PASS", f"virtual environment is active ({sys.prefix})")
elif conda_env == "base":
    report("WARN", "you are in the conda 'base' environment: run `conda activate scientific-programming`")
else:
    report("WARN", "no environment is active (fine for a first test, but create one: see the setup tutorial)")

# 3. Can Python run code and handle text and numbers?
total = sum(i * i for i in range(1, 11))
if total == 385:
    report("PASS", "Python can run code (sum of squares from 1 to 10 is 385)")
else:
    report("FAIL", f"unexpected result {total}")

# 4. Can Python write and read a file in this folder?
test_file = Path.cwd() / "_check_python_test.txt"
try:
    test_file.write_text("hello", encoding="utf-8")
    ok = test_file.read_text(encoding="utf-8") == "hello"
    test_file.unlink()
    report("PASS" if ok else "FAIL", "Python can create and read files in this folder")
except OSError as error:
    report("FAIL", f"cannot write in this folder ({error}); open a terminal in a folder you own, such as your Documents")

print()
if "FAIL" in results:
    print("RESULT: not ready yet. Show this output to a helper, we will fix it together.")
    sys.exit(1)
if "WARN" in results:
    print("RESULT: Python works. Read the WARN lines above, then you are ready.")
else:
    print("RESULT: all good, you are ready for Python!")
