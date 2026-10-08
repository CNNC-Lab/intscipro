# Demo: an end-to-end analysis with Claude Code (15 minutes)

An AI coding agent takes a **real single-cell RNA-seq dataset** from raw data to a short research report, live, while you watch critically. Everything runs inside one cloud session: nothing to download, no extra repository.

## The data
**700 human blood cells (PBMCs), 765 genes**, a subset of the 10x Genomics 68k PBMC dataset (Zheng et al., *Nature Communications*). It ships inside the `scanpy` package, so loading it needs no internet access:

```python
import scanpy as sc
adata = sc.datasets.pbmc68k_reduced()
```

It contains an expression matrix, a reference cell-type label per cell (`obs['bulk_labels']`) and an earlier clustering (`obs['louvain']`). The matrix has already been processed (normalised and scaled), which is one of the things a careful analyst has to notice.

## Questions
1. How many distinct cell populations are there?
2. Which genes mark each population, and do they match known immune biology?
3. How well do unsupervised clusters agree with the reference labels?

## The prompt
Paste this into a Claude Code session started in this repository:

```
End-to-end analysis of a real single-cell RNA-seq dataset, ending in a short
research report.

Data: scanpy.datasets.pbmc68k_reduced() (700 human blood cells, 765 genes; it is
bundled with the scanpy package, no download). Run `pip install scanpy igraph
leidenalg` first if scanpy is missing. Write everything to
day01-introduction/claude_code_demo/outputs/.

Questions
1. How many distinct cell populations are there?
2. Which genes mark each population, and do they match known immune biology?
3. How well do your unsupervised clusters agree with the reference labels in
   obs['bulk_labels']?

Rules
- Plan first and wait for my approval before running anything.
- Check what preprocessing the data already had before applying any.
- One script, analysis.py, that regenerates every figure and number.
- At most 5 figures. Every number in the report must come from the script output.
- Finish with a limitations section. Deliverable: report.md.
```

## What to look for while watching
- Did the plan check what had already been done to the data?
- Do the marker genes make biological sense? (For example `CD3D` for T cells, `MS4A1` and `CD79A` for B cells, `NKG7` for NK and cytotoxic cells, `LYZ` and `CST3` for monocytes and dendritic cells.)
- Is agreement with the reference labels reported with a proper metric, and is a modest value discussed honestly? Reference labels are themselves imperfect.
- Does every number in the report match the script output?
