# Live demo runbook: Claude Code on a real dataset (15 minutes)

**Flow:** open a cloud Claude Code session on this repository, paste the prompt from [`claude_code_demo/README.md`](../day01-introduction/claude_code_demo/README.md), read the plan, approve, wait for `report.md`. No configuration is needed: the session installs `scanpy` with pip and the data ships inside the package.

## Steps
1. New cloud session on this repository, in **Plan** mode (mode dropdown next to the prompt box).
2. Paste the **Step 1** prompt. When the plan appears, read it aloud and ask the room what they would check or change.
3. Send the **Step 2** message and switch to Auto or Accept edits. Narrate while it runs.
4. Open `outputs/report.md`. Pick two numbers and find them in the script output. Discuss the limitations section.

| Min | What happens |
|---|---|
| 0-2 | Frame it: real data, a human approves a plan and verifies the result |
| 2-5 | Prompt, plan, discussion, approval |
| 5-11 | Execution (package install, analysis, figures, report) |
| 11-15 | Read the report, spot-check numbers, discuss limitations |

## Tested reference run
The pipeline was run end to end (about 25 seconds of compute) with these results, for comparison:
- 700 cells, 765 genes. The matrix is already normalised and scaled (values from -2.03 to 28.4), with the raw values in `adata.raw` and PCA, UMAP and Louvain clusters precomputed.
- Leiden clustering at resolution 1.0 gives 11 clusters, with adjusted Rand index 0.38 against the reference labels (0.41 for the precomputed Louvain clusters). The index depends on the resolution: 0.51 with 8 clusters at the coarsest setting tried, 0.38 with 11.
- Markers per cluster include `FCGR3A`/`LST1` (monocytes), `NKG7`/`CTSW`/`GNLY` (NK and cytotoxic), `CD3D`/`CD3E` (T cells), `MS4A1`/`CD79A` (B cells), `MZB1` (plasma cells) and `FCER1A` (dendritic cells).
- Reference labels overlap (several T-cell subsets, a large "Dendritic" group), so modest agreement is expected and should be discussed.

## Teaching moments
| Moment | Look for |
|---|---|
| Existing preprocessing | Does the plan notice the data is already normalised and scaled, or does it re-normalise? |
| Marker genes vs biology | Do the top genes per cluster match known immune markers? |
| Honest agreement | Is the modest agreement reported and the resolution dependence discussed? |
| Numbers match output | Spot-check two values live |

## Steering prompts (only if needed)
- *"What preprocessing was already applied to this data, and how do you know?"*
- *"How would you check these clusters are real and not an artefact of the resolution parameter?"*
- *"Which of your claims is not supported by an output file?"*

## Optional: live databases
The same exercise can query Open Targets and UniProt (see the demo README), but a default cloud session cannot reach them; it needs the two hosts added under the environment's network access settings. Not required for the standard demo, and not tested.
