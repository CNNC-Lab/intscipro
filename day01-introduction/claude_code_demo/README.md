# Demo: an end-to-end analysis with Claude Code (15 minutes)

An AI coding agent takes a **real single-cell RNA-seq dataset** from question to research report while we watch. Open a cloud Claude Code session in this repository, paste the prompt, review the plan, approve it, and wait for the report. No configuration is needed.

## The data
**700 human blood cells (PBMCs), 765 genes**, a subset of the 10x Genomics 68k PBMC dataset (Zheng et al., *Nature Communications*). It ships inside the `scanpy` package, so the agent installs it with `pip` and nothing else is downloaded:

```python
import scanpy as sc
adata = sc.datasets.pbmc68k_reduced()
```

## Step 1: the prompt
Paste into a new Claude Code session on this repository, in Plan mode:

```
Question: using the real single-cell RNA-seq dataset that ships with scanpy
(scanpy.datasets.pbmc68k_reduced(): 700 human blood cells, 765 genes), how many
distinct cell populations are there, which genes mark each one and do they match
known immune biology, and how well do unsupervised clusters agree with the reference
cell-type labels in the data (obs['bulk_labels'])?

Install what you need with pip. Do not download any other data.
Check what preprocessing the data already had before applying any.
Save everything in day01-introduction/claude_code_demo/outputs/.
Write one script, analysis.py, that regenerates every figure and number.
Deliverable: report.md with at most 5 figures, every number traceable to the
script's output, and a limitations section.

First propose a plan: the steps, the methods and why, and the main risks.
Do not run anything until I approve it.
```

## Step 2: approve and execute
After reading the plan, send:

```
The plan is approved. Execute it end to end: run the analysis, make the figures and
write report.md. Then rerun analysis.py from scratch and confirm that every number in
the report matches the script output.
```

## What to look for while watching
- Did the plan check what had already been done to the data (it is already normalised and scaled)?
- Do the marker genes make biological sense? For example `CD3D` for T cells, `MS4A1` and `CD79A` for B cells, `NKG7` for NK and cytotoxic cells, `LYZ` and `CST3` for monocytes and dendritic cells.
- Is agreement with the reference labels reported with a proper metric, and is a modest value discussed honestly? Reference labels are themselves imperfect, and the agreement depends on the clustering resolution.
- Does every number in the report match the script output?

## Optional: the same exercise against live databases
If your cloud environment is allowed to reach `api.platform.opentargets.org` and `rest.uniprot.org`, the agent can answer "which genes have the strongest evidence of association with Alzheimer's disease, and what do they do?" by querying Open Targets and UniProt directly. This needs a change to the environment's network settings, so it is not part of the standard demo.
