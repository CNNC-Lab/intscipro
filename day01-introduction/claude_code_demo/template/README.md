# Mouse cortex proteomics: Claude Code demo project

Starting point for an end-to-end, AI-driven analysis of a real proteomics dataset. This folder is the *template*: copy it into a fresh, empty repository and open that repository in a Claude Code session. Part of the Introduction to Scientific Programming course (Day 1).

```
CLAUDE.md             instructions Claude reads at the start of every session
.claude/settings.json pre-approved routine commands (fewer permission prompts)
requirements.txt      Python packages for the analysis
data/README.md        data dictionary and experimental design
data/raw/             the dataset (created by scripts/fetch_data.py; never edited)
scripts/fetch_data.py one-time download and validation of the dataset
scripts/check_env.py  cheap check that packages and data are in place
```

Setup:

```bash
pip install -r requirements.txt
python scripts/fetch_data.py     # needs internet; run once, then commit data/raw/
python scripts/check_env.py      # should end without MISSING lines
```
