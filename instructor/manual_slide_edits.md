# Manual slide edits (decks the API cannot edit)

The Slides API refuses edits on decks 2 to 8, 10 and 11 (duplicate block ids on unrelated slides, or nested vertical stacks). These edits need to be made in the Slides editor. Slide numbers count every slide in order, including slides inside vertical stacks. The Lecture 1 and Lecture 9 decks were already edited.

## 1. Dates (all decks 2 to 8, 10, 11)
On **slide 1** of each deck, delete the small date text box under the contact details (the text such as `17/10/2025`). Decks: Lecture 2, 3, 4, 5, 6, 7, 8, 10 and 11. Lecture 11 shows `09/01/2026`.

## 2. Lecture 2 deck ("Scientific Programming 2: Variables and data structures")
Present the new **Part 0** deck first ("Scientific Programming 2, Part 0: Setting up and running Python"), then this one. Then:

| Slide | Problem | Replace with |
|---|---|---|
| 3 ("Before we get started") | you will rewrite it; remove the "power plugs" and "PDBEB" lines and the final bullet about installing Python | a pointer to Part 0, for example "Make sure you finished the Part 0 checkpoint" |
| 4 (agenda, "Day 2: Programming Fundamentals") | lists "Classes and basic object-oriented programming", which the deck does not cover, and says "Tutorial exercises moved to intermediate programming concepts", which is stale (the repo has 18 Day 2 exercises plus Part 0) | remove the classes line; replace the last line with "Practical: Part 0 checkpoint and tutorial exercises" |
| 51 ("Side note: floating point precision") | mentions `numpy.allclose()` (twice) | delete `numpy.allclose()`; keep `math.isclose()` only |
| 68 ("Types of Functions: Module functions") | `import numpy as np`, `import pandas as pd`, and a NumPy example | `import math`, `import random`, `import statistics`; example `statistics.mean([1, 2, 3, 4])` gives `2.5` |
| 69 ("Modules & Libraries") | alias example `import numpy as np` and the best-practice sentence naming `np` | alias example `import math as m` (`m.sqrt(16)` gives `4.0`); best-practice text "Use short, conventional aliases and import only what you need" |
| 76 ("Flexible inputs") | last sentence cites matplotlib's `hist()` | "Example: the built-in `print()` has optional parameters such as `sep` and `end`; this flexibility makes functions powerful and easy to use" |
| 79 ("Summary: Functions") | "Alias imports: `import numpy as np`" | "Alias imports: `import math as m`" |

## 3. Lecture 3 deck ("Scientific Programming 3: Development tools & Workflows")
Rule for Day 3: no scientific libraries (they arrive on Days 4 to 8); use `requests` as the install example.

| Slide | Problem | Replace with |
|---|---|---|
| 18 ("Classic Jupyter Notebooks") | "Outputs: text, tables, plots (matplotlib, seaborn), interactive widgets" | "Outputs: text, tables, images, rich HTML and Markdown" |
| 26 ("Daily workflow") | `pip install numpy scipy pandas matplotlib` | `pip install requests` |
| 28 ("Conda environments") | `conda install numpy scipy matplotlib bioconda::biopython`; "(R packages, system libraries, bioinformatics tools)" is fine | `conda install requests` |
| 29 (poetry) | `poetry add pandas biopython matplotlib` | `poetry add requests`, or move to the optional appendix |
| 30 (uv) | `uv pip install pandas numpy matplotlib` | `uv pip install requests`, or move to the appendix |
| 31 ("More options") | `pipenv install pandas`, `rye add pandas` | `requests` in both, or move to the appendix |
| 50 ("Computational Research Workflow") | `conda install numpy scipy matplotlib pandas` | `conda install requests` |
| 28 ("Conda environments") | also `conda create -n myproject python=3.10` | `python=3.11` (the course version) |
| 36 ("Best practices") | example environment name `rna_seq_2024` contains a year | `rna_seq_analysis` |
| 3 ("Day 3" agenda) | lists "conda, poetry, uv" | "Virtual environments (venv and conda)" |
| 29 to 31 and the comparison table slides | poetry, uv, pipenv, rye and virtualenvwrapper are too much for beginners | move to an "Optional: other tools" appendix after the Thank-you slide (or hide them) and keep venv and conda as the core |

The handout and exercises already follow this rule.

## 4. Lecture 4 to 8, 10, 11 decks
Only the date box on slide 1 (section 1). Optional: Lecture 8's last content slide says "Next Week: Advanced ML & Deep Learning", which is wrong (the next session is project preparation); Lecture 10's agenda slide says "Day 9" instead of "Day 10".

## 5. PDFs
After all slide edits: export each deck to PDF from Slides.com (Share, Export, PDF) and in Google Drive use "Manage versions, Upload new version" on the existing file, so the links in the READMEs stay the same. Add the Part 0 deck as a new PDF and link it from `day02-fundamentals/README.md`. Handout and exercise PDFs for Days 2 and 3 also need re-exporting.
