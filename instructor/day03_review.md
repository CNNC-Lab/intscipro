# Day 3 review: suggestions

Status after this pass: repo, handout and exercises are aligned with the course environment (Miniconda, Python 3.11, JupyterLab through conda) and library-free. Slides were not edited (your call); the slide checklist is in `manual_slide_edits.md`, section 3.

## 1. Time: what to teach if Day 3 starts late
The handout (51 pages) and exercises (51 pages, "6 to 8 hours") are far more than one session. Suggested order, stopping wherever the time runs out:

1. **Notebooks** (JupyterLab running, cells, kernel and execution order): Exercise 1, Parts A and B.
2. **Environments** (venv and conda, `requirements.txt` / `environment.yml`): Exercise 2, Part A (venv) and Part C (conda). Point out that `environment-base.yml` is their own environment.
3. **Git core** (init, add, commit, log, branch, merge): Exercise 3, Parts A to C.
4. **GitHub** (push, pull request): Exercise 4, Parts A and B.
5. Homework / self-study: documentation with Markdown and docstrings (handout section 3), Exercise 3 conflicts, Exercise 4 Parts C to E, Exercise 5 (integrated project), "Computational Research Workflows".

If you would rather not rush Git, split the content: Day 3 = editors, notebooks, environments; Day 4 opening hour = Git and GitHub. Day 4 numerics then loses an hour, so this only works if Day 2 is also shortened. Not recommended unless Day 2 overruns again.

## 2. Pre-work (new)
`resources/before_day3.md`: GitHub account, Git, `git config`, JupyterLab, GitHub login. Send it with the Day 2 follow-up message. Authentication is the most likely thing to fail live (GitHub rejects account passwords for `git push`). The handout now has an "Authenticating with GitHub" section and Exercise 4 opens with a reminder.

## 3. Slides (to do in the Slides editor)
- Title slide date (31/10/2025): delete.
- The agenda promises "Documentation with Markdown and docstrings", but the deck has **no documentation section**; either add 2 or 3 slides (Markdown basics, a docstring example, "why document") or remove the agenda line and keep it as handout self-study.
- Library mentions and tool overload: see `manual_slide_edits.md`, section 3 (slides 26 and 28 to 31, 50; poetry, uv, pipenv to an appendix).
- Add one slide "Authenticating with GitHub" (GitHub CLI `gh auth login`, Credential Manager on Windows) before the Git daily-workflow slide.
- Last slide: "prepared with the help of Claude Sonnet 4.5, via GenSpark": update or drop.
- "Quick comparison" appears on three consecutive slides (two are image-only duplicates): delete two.

## 4. Handout
Consistent with the slides' order except the missing documentation slides. Optional trims: the long "Optional: other environment tools" section and the Jupyter magic commands could be marked "reference" so students know they can skip them.

## 5. Exercises
- Exercise 5 is a multi-hour project: label it **homework** in the README and in the exercise intro.
- Exercise 4 Part C needs a partner; suggest pairing students in class.
- Exercise 2 creates Python 3.9 and 3.11 environments (downloads); fine on good wifi, otherwise skip step 24.

## 6. Repo
- Day 3 has no `solutions/` folder: the exercises are command sequences with embedded code, so that is acceptable. Mention it in the README if students ask.
- The old Drive PDF links are replaced by repo-hosted PDFs under `day03-workflows/pdf/` (slides PDF is an export of the current deck, including the issues listed above; re-export after fixing the slides).
