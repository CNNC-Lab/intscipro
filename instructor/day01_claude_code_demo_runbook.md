# Live demo runbook: an end-to-end analysis with Claude Code (cloud)

**Goal.** Show, live and in about 70 minutes, a complete research workflow driven by an AI agent: load a real proteomics dataset, quality-control it, test hypotheses, build a predictive model and write a full research report. The point is not that the agent is fast. The point is to practise *directing* it and *verifying* what it produces.

**Dataset.** Mouse cortex protein expression in a Down syndrome model (Ts65Dn vs control; memantine vs saline; learning vs no learning; 77 proteins; 72 mice; 1080 rows). Details in [`data/README.md`](../day01-introduction/claude_code_demo/template/data/README.md).

## Why this dataset
- **Real, public, citable, small**: CC BY 4.0, small enough to fit in the repository. It runs in seconds, so credits go to reasoning, not to computation.
- **Neuroscience and biochemistry together**: protein signalling in learning, a disease model and a drug.
- **Rich enough for a full paper**: a 2 × 2 × 2 design that supports differential expression, a treatment-rescue question, a learning question, an interaction question and a classification task.
- **Built-in teaching moments** (see below): repeated measurements per animal, missing values, many simultaneous tests, and a classification task where leakage is easy.
- **Biology you can sanity-check**: proteins encoded in the triplicated region of mouse chromosome 16 (for example DYRK1A, ITSN1, SOD1, APP) are candidates for being elevated in Ts65Dn. Treat this as a hypothesis to check against the results, not as a given.

## Teaching moments to watch for
| Moment | What to look for | If the agent misses it |
|---|---|---|
| **Unit of replication.** Each mouse contributes 15 rows | Does the plan or report state that the animal, not the row, is the independent unit (n = 72, not 1080)? Does it aggregate per mouse or use a mixed model? | Ask: "How many independent biological replicates are in each group?" |
| **Missing data** | Is missingness quantified per protein and per group? Which proteins are dropped or imputed, and why? | Ask: "Which proteins have the most missing values, and could that bias the comparison?" |
| **Multiple testing** | 77 proteins are tested per contrast. Is FDR control applied and reported? | Ask: "How many of these hits survive correction?" |
| **Leakage in classification** | Rows from the same mouse must not be split between training and test sets; imputation and scaling must be fitted inside the cross-validation loop | Ask: "Could the same animal appear in both training and test data?" |
| **Interpretation** | Correlation vs mechanism; exploratory vs confirmatory; sanity check against known biology | Ask: "What would convince you this result is wrong?" |
| **Numbers in the report** | Do the numbers in the text match the files in `outputs/tables/`? | Spot-check two numbers live |

These are deliberate decision points: pause at each one and ask the room what they would do before the agent decides.

## Before the day

### 1. Create the demo repository (once)
The template folder is meant to become its own small repository, separate from the course repository, so Claude works on a clean project and the course repo stays untouched.

```bash
cp -r day01-introduction/claude_code_demo/template ../mouse-proteomics-demo
cd ../mouse-proteomics-demo
git init -b main
pip install -r requirements.txt
python scripts/fetch_data.py        # needs open internet; validates shape, classes and mouse count
python scripts/check_env.py         # must finish without MISSING lines
git add -A && git commit -m "Initial project: template and raw data"
# create an empty repository on GitHub (for example in the CNNC-Lab organisation) and push
```

Commit the data. The cloud sandbox allows package registries and GitHub by default but usually blocks data portals such as UCI, so the session should never depend on downloading data.

If `fetch_data.py` fails an assertion, stop: the file is not the dataset the plan expects. Fix before the session.

### 2. Configure the cloud environment
In claude.ai/code, create an environment for this demo (environment menu in the session title bar, then Edit):
- **Setup script**: `pip install -r requirements.txt`, so no session time is spent installing packages.
- **Network access**: the default package-manager access is enough because the data is in the repository. If you prefer fetching at runtime, use *Custom* and add `archive.ics.uci.edu` under Allowed domains.
- Connect the GitHub repository created above.

### 3. Cheap dress rehearsal (a few minutes, negligible cost)
Start a session on the demo repository and give it only this prompt:

> Run `python scripts/check_env.py` and tell me in one sentence whether the environment is ready. Do nothing else.

This verifies GitHub access, packages, data and permissions without spending credits on analysis. Then archive the session.

### 4. Protect your credits
- **One planned run.** Decide beforehand that the demo is a single session. Do not iterate on prompts live beyond the steering prompts below.
- **Plan first.** Start in *Plan* mode (mode dropdown next to the prompt box). Planning is cheap and it is the most instructive part for students. Switch to *Auto* (if offered) or *Accept edits* only after approving the plan.
- **Right-size the model.** A mid-tier model is sufficient for this dataset; do not select the most expensive one.
- **Keep scope fixed.** The four questions in the kickoff prompt, one report, at most 8 figures, no web search. `CLAUDE.md` already instructs short terminal output and no downloads.
- **Check your usage allowance** in your account settings before the session, and keep a buffer.
- **Fallback if credits run out mid-demo**: stop the run, commit what exists, and use the remaining time for the discussion questions below. The partial outputs are still a useful artefact.

## The session (about 70 minutes)

| Time | Activity |
|---|---|
| 0:00 | **Frame it (5 min).** Show the repo, `CLAUDE.md` and `data/README.md`. Explain that `CLAUDE.md` is the agent's standing brief and that good briefs are most of the skill. |
| 0:05 | **Plan mode (10 min).** Paste the kickoff prompt. Read the plan aloud. Ask the room: is the replication unit right? are the methods appropriate? what is missing? Revise the plan with at most one steering prompt. |
| 0:15 | **Execute (35 min).** Approve and let it run. Narrate what it is doing. Pause at the three checkpoints below. |
| 0:50 | **Review the report (10 min).** Open `report/report.html`. Spot-check two numbers against `outputs/tables/`. Read the limitations section critically. |
| 1:00 | **Debrief (10 min).** Discussion questions below. |

### Kickoff prompt (paste verbatim, in Plan mode)

```
Read CLAUDE.md and data/README.md, then inspect the dataset in data/raw.

Goal: an end-to-end, reproducible analysis ending in a complete research report
(report/report.md and a self-contained report/report.html).

Research questions
1. Which proteins differ in expression between Ts65Dn (Down syndrome model) and
   control mice?
2. Does memantine treatment change the protein expression profile in either
   genotype, and does it move Ts65Dn mice towards the control profile?
3. Does learning stimulation (context-shock versus shock-context) change
   expression, and does that depend on genotype or treatment?
4. Can the experimental group be predicted from protein expression, and which
   proteins carry the most information?

Start by proposing a plan: the stages, the statistical methods you will use and
why, the assumptions you are making about the experimental design, and the main
risks to validity. Do not run any analysis until I approve the plan.
```

### Checkpoints and steering prompts
Use these only if needed; each is a teaching moment.

1. **After QC (about 0:25).** Review the missingness and design summary. If the replication unit is not addressed: *"How many independent biological replicates are in each group? Revise the plan accordingly."*
2. **After differential expression (about 0:35).** Look at the top hits and the multiple-testing correction. Ask: *"Which of these hits make biological sense given the genotype? Check whether proteins encoded in the triplicated chromosome region behave as expected."*
3. **After classification (about 0:45).** Ask: *"Could the same mouse appear in both training and test data? Show me how the evaluation prevents that."*
4. **Closing prompt.** *"Re-run every script from scratch, confirm that every number in the report matches the files in outputs/, fix any mismatch, then commit everything."*

### What good looks like (rubric for the finished report)
- States the replication unit and the real sample size per group.
- Quantifies and handles missing values explicitly.
- Applies FDR control to the per-protein tests and reports effect sizes with intervals.
- Evaluates classification with animal-level splits, with preprocessing inside the cross-validation loop.
- Distinguishes exploratory from confirmatory findings, and has a candid limitations section.
- Reproducibility section lists the exact commands; re-running from raw data gives the same numbers.
- Figures are readable and every figure is referenced and interpreted in the text.

## Discussion questions for the debrief
1. Which decision did the agent make that you would have made differently? Who should own that decision?
2. What did we have to know, as scientists, to catch the mistakes (or to know there were none)?
3. How would you check the report if you could not see the code?
4. What belongs in `CLAUDE.md` for your own project?
5. What would you never delegate to an agent?

## Hands-on follow-up for students
Students without access to a cloud agent can reproduce the workflow with the chat tools from the [simple demo](../day01-introduction/AI_chat_demo.md). Homework: write a `CLAUDE.md` for your own thesis dataset (data dictionary, design, your statistical standards, deliverables) and use it with any AI assistant you have access to. Bring one thing the assistant got wrong.

## After the session
Commit and push the session's work to the demo repository, then archive the session. Keep the finished repository as the reference run for future editions: it replaces the need to re-run the demo to show what the output looks like.

## If something goes wrong
| Problem | Response |
|---|---|
| Session will not start or the repository is not visible | Check that the GitHub repository is connected to the environment; fall back to the chat demo and reschedule |
| Package missing | `pip install -r requirements.txt`; fix the environment setup script afterwards |
| Data missing | Run `python scripts/check_env.py`; the data must be committed in `data/raw/` |
| The agent goes down a long path | Interrupt, restate the question briefly, and point it back to the plan |
| Credits or limits run out | Stop, commit partial outputs, and run the debrief on what exists |
