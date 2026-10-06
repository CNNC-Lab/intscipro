# Project context: mouse cortex protein expression (Down syndrome model)

You are the analyst on a small research project. The human is the principal investigator and will review your work. Be rigorous, transparent about what you did, and honest about uncertainty.

## Data
- `data/raw/Data_Cortex_Nuclear.csv` is the only dataset (a lossless CSV copy of the original `.xls` next to it). **Never modify anything in `data/raw/`.**
- Data dictionary and experimental design: `data/README.md`. Read it first.
- No internet access is needed. Do not search the web and do not download anything except the Python packages in `requirements.txt` (`pip install -r requirements.txt` if something is missing).

## Working rules
- Put reusable code in `src/` and one runnable script per analysis stage in `analysis/` (`01_qc.py`, `02_...`). Scripts must run top to bottom with `python analysis/<name>.py` from the repository root, with a fixed random seed, and write to `outputs/` (figures in `outputs/figures/`, tables in `outputs/tables/`).
- Keep terminal output short: never print whole data frames; use `.head()`, `.shape`, and summaries.
- Prefer clear, boring, standard methods (pandas, scipy, statsmodels, scikit-learn, matplotlib, seaborn). Briefly justify each choice.
- Use at most 8 figures in the report. Label axes with units or meaning; make figures readable in colour-blind-safe palettes.

## Statistical standards (non-negotiable)
- Before any inference, identify the **unit of biological replication** and say what it is, in the report. Measurements that are not independent must not be treated as independent samples.
- Correct for multiple testing whenever many features are tested (report the method and the threshold).
- Report effect sizes and uncertainty (confidence intervals), not only p-values.
- Handle missing values explicitly: report how much is missing, where, and what you did about it. Do not silently drop or impute.
- When predicting group labels, evaluate on data the model has not seen, and make sure no information leaks between training and evaluation data (including through preprocessing).
- Separate **exploratory** from **confirmatory** findings, and never present a correlation as a mechanism.
- Sanity-check results against known biology and say when something looks surprising.

## Deliverable
A reproducible mini-paper in `report/report.md` plus a self-contained `report/report.html` (figures embedded; use `pandoc` if available, otherwise Python-Markdown with base64-embedded images). Sections:
1. Summary (5 sentences max, with the headline numbers)
2. Background and questions
3. Data and quality control (design, replication unit, missingness, outliers)
4. Methods (one short paragraph per analysis, with software versions)
5. Results (one subsection per question, each ending with a plain-language conclusion)
6. Limitations and caveats
7. Reproducibility (exact commands to regenerate everything from raw data)

Every number quoted in the report must come from a file in `outputs/` produced by a script. Before finishing, re-run all scripts from scratch and check that the report numbers still match; list anything you could not verify.
