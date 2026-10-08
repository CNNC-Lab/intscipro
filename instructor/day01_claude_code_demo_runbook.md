# Live demo runbook: Claude Code on a real dataset (15 minutes)

**What:** the agent analyses 700 human blood cells (single-cell RNA-seq, bundled with `scanpy`) and writes a short report. **Where:** this repository, in a cloud Claude Code session. Nothing to set up beyond what the session already has: `pip install scanpy` works, and the data ships inside the package.

## Before the session (2 minutes)
1. Open a Claude Code cloud session on this repository.
2. Start in **Plan** mode (mode dropdown next to the prompt box).
3. Have [`claude_code_demo/README.md`](../day01-introduction/claude_code_demo/README.md) open to copy the prompt.

## Timeline
| Min | What happens |
|---|---|
| 0-2 | Frame it: real data, three questions, a human approves a plan and verifies the result |
| 2-5 | Paste the prompt. Read the plan aloud and ask the room: what would you check? Approve (switch to Auto or Accept edits) |
| 5-11 | It runs. Narrate. A complete pipeline takes under a minute of compute; most of the time is the agent working |
| 11-15 | Open `outputs/report.md`. Spot-check two numbers against the script output and discuss the limitations section |

## Teaching moments
| Moment | Look for |
|---|---|
| Preprocessing already applied | The matrix is already normalised and scaled, with PCA, neighbours, UMAP and Louvain clusters precomputed. Does the plan notice, or does it re-normalise? (The raw values are in `adata.raw`.) |
| Marker genes vs biology | Do the top genes per cluster match known immune markers (T cells `CD3D`, B cells `MS4A1` and `CD79A`, NK `NKG7`, monocytes `LYZ`) |
| Honest agreement | A quick check here gave an adjusted Rand index of about 0.4 between Leiden clusters and the reference labels. The labels overlap (several T-cell subsets, a very large "Dendritic" group), so a modest value is expected. Does the report say so, or oversell? |
| Numbers match output | Spot-check two values live |

## Steering prompts (only if needed)
- *"What preprocessing was already applied to this data, and how do you know?"*
- *"How would you check these clusters are real and not just an artefact of the resolution parameter?"*
- *"Which of your claims is not supported by an output file?"*

## Keeping credits low
Plan mode first, one session, five figures at most, no web search. The analysis is tiny, so cost is the agent's reasoning, not computation. If time runs short, stop after the plan and discuss it.

## Fallback
If the session misbehaves, run the prompt's steps yourself in a notebook: `adata = sc.datasets.pbmc68k_reduced()`, `sc.pp.neighbors`, `sc.tl.leiden(..., flavor='igraph')`, `sc.tl.rank_genes_groups(..., use_raw=True)`. It takes under a minute.
