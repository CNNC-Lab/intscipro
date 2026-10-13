# Plan: Day 2 gets a proper "set up and run code" opening

**Decision taken:** Day 2 and Day 3 are *not* swapped. Day 2 opens with a hands-on **Part 0: Setting up and running Python** (no extra session), then continues with the Python basics. If the session runs long, the end of the Python basics moves to the start of Day 3.

**Rule for all materials:** a day may only use what has already been introduced. Day 2 is pure Python (standard library only). Day 3 may use tools and the standard library, but not NumPy, pandas, matplotlib, SciPy, seaborn, scikit-learn or ipywidgets (those arrive on Days 4 to 8).

## 1. Why the problem happened
- The Day 2 deck's only run-it guidance is one bullet ("make sure you have python installed … preferably ipython").
- The Day 3 tools deck has no terminal, "run a script" or "read an error" content either, so swapping would not have fixed it.
- Nothing verifies that every student can run code before Python starts.

## 2. Proposed Day 2 structure
| Block | Content | Time |
|---|---|---|
| **Part 0** (new) | Set up and run code, ending in a pass/fail checkpoint | 60 to 75 min |
| Part 1 | Variables, data types, data structures, basic I/O | existing |
| Part 2 | Operators, expressions, control structures, exception handling | existing |
| Part 3 | Functions and modules | moves to the start of Day 3 if time runs out |

Day 3 then opens with functions and modules (plus docstrings, which need functions), followed by the tools content, trimmed (see section 5).

### Part 0 outline (slides, handout, exercise)
0.1 **The map**: interpreter, editor and terminal, and the four ways to run Python (interactive prompt, script from the terminal, editor run button, notebook preview).
0.2 **Install check**: one recommended path (Miniconda or Anaconda plus VS Code), tabs for Windows, macOS and Linux, and what success looks like.
0.3 **The terminal in 10 commands**: where am I, list, change folder, make a folder, run Python, find which Python.
0.4 **The first environment**: create, activate and recognise it (name in the prompt); what "wrong environment" looks like.
0.5 **Four ways to run code** hands-on: interactive prompt (IPython), `python hello.py`, VS Code (select the interpreter, run), a notebook preview.
0.6 **Reading errors**: `SyntaxError`, `NameError`, `ModuleNotFoundError` (wrong environment), `FileNotFoundError` (wrong folder), "python not found".
0.7 **Checkpoint** (everyone leaves with it green): run `check_python.py`, run `hello.py`, fix three broken scripts, with buddy pairs and helper roles.
0.8 **Plan B** for anyone blocked: a browser-based option (for example Google Colab) so nobody is stuck.

### Supporting changes
- **Pre-work page** `resources/before_day2.md`: a 10-minute install checklist sent a week earlier, so class time goes to running code.
- **Staged environment:** Day 2 creates a minimal environment (Python plus IPython). Day 3 adds JupyterLab. Day 4 runs `conda env update -f environment.yml` to bring in the scientific stack. This teaches environments properly and keeps every day within what it has introduced.
- **New folder** `day02-fundamentals/setup/`: `hello.py`, a pure-Python `check_python.py`, three `broken_*.py` scripts with their fixes, and a short README. The existing `check_installation.py` (which imports the scientific libraries) moves to Day 4.
- **Setup tutorial:** keep one source of truth. I suggest the Day 1 `setup_tutorial.md` becomes the reference for Part 0 (renamed and linked from Day 2), with its checklist turned into the checkpoint.
- **`resources/troubleshooting.md`:** add entries for `ModuleNotFoundError`, wrong interpreter in VS Code, wrong folder, and "python not found" on each operating system.

## 3. Pure-Python corrections for Day 2
- Handout, modules section (around lines 930 to 1005): replace the NumPy, pandas, matplotlib, SciPy and scikit-learn import examples with the standard library (`math`, `random`, `statistics`, `datetime`, `collections`, `pathlib`).
- Exercises 10, 11 and 16, and their solutions: rewrite without NumPy and matplotlib (loops, `math`, printed tables or text bars). Exercise 15 and the solutions that import libraries get the same treatment.
- Resource lists: drop the NumPy and matplotlib tutorial links from Day 2.
- Deck 2 slides that import NumPy as the module example, and the "make sure python is installed" bullet: replace with `math` and a pointer to Part 0.

## 4. Corrections for Day 3 (hard dependencies)
Both files are heavy: the handout mentions the scientific libraries about 49 times and the exercises about 46 times.
- Handout: replace the NumPy, pandas, matplotlib and widget examples (Jupyter section, magics, rich display) with standard-library code; show rich output through `IPython.display` (Markdown, HTML, LaTeX); use a small neutral package (for example `requests`) for the `pip`, `conda` and version-pinning demos.
- Exercises 1B to 1D and 2: same replacement.
- **Exercise 5** (integrated project, about 800 lines, currently a pandas and scipy temperature analysis): rewrite as a small pure-Python project with a `src/` module of functions, a script, a README, a pinned requirements file, a notebook, and a Git and GitHub workflow.
- Git exercises: keep the small `def` functions but give students the files ready-made.
- Docstrings (handout section 3): stays in Day 3, now after the functions block that opens the day.
- **Trim the tools deck:** poetry, uv, pipenv and virtualenvwrapper move to an optional appendix; keep venv and conda as the core.

## 5. Dates (decided: remove all dates)
- **Done:** repo files, Lecture 1 and Lecture 9 (title slide and deadline slide).
- **GitHub repo description** ("… (WS 2025/2026)"): needs to be changed by you (gear icon next to "About"); there is no tool for repository settings in this environment.
- **Decks 2 to 8, 10 and 11:** each title slide still shows its date. Delete the date text box on the title slide by hand. The Slides API refuses edits on these decks (see section 6).
- **PDFs:** see section 6.

## 6. What I can and cannot do from here
- **Slides API limits:** decks 2 to 8, 10 and 11 cannot be edited by me. Decks 2 to 8 and 10 contain duplicate block ids on unrelated slides (copied slides), and the API rejects any save while those exist. Deck 11 uses nested vertical slide stacks, which the API does not support. So I can edit decks 1 and 9 only.
- **What that means for the plan:** I can build Part 0 as a **new deck** ("Lecture 2, Part 0: Setting up and running Python") that you present before the existing Lecture 2 deck. Edits inside decks 2 and 3 (dependency fixes, trimming, the date boxes) need to be made by hand in the Slides editor; I can supply the exact list of slides and replacement text.
- **PDF export:** I can trigger the Slides PDF export and download the file here. I cannot upload to Google Drive until the Google Drive connector is connected to this chat. The easiest route that needs **no README changes**: export each deck to PDF from Slides.com and, in Drive, use "Manage versions, upload new version" on the existing file, so every link stays the same. Do this last, after all slide edits.
- **Handout and exercise PDFs** on Drive also need re-exporting after the content changes; I can convert the Markdown if a PDF toolchain is available, or you can export from your Markdown editor.

## 7. Suggested order of work
1. New Part 0 deck, handout section, `setup/` scripts, exercise 0, pre-work page, troubleshooting entries.
2. Day 2 pure-Python corrections (handout, exercises, solutions).
3. Day 3 corrections (handout, exercises, solutions, new Exercise 5).
4. Update READMEs and the staged environment files; run CI and the notebooks.
5. You: edit the decks by hand (dates, deck 2 and 3 fixes), then export all PDFs.
