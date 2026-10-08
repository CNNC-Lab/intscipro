# Demo: an end-to-end analysis with Claude Code (15 minutes)

An AI coding agent answers a real biomedical research question **by querying public databases live**, then writes a short research report. Nothing is downloaded and no data is stored in the repository: the agent sends small queries and works with the responses. Everything runs inside one cloud session.

## The question
**Alzheimer's disease: which genes and proteins have the strongest evidence of association, what kind of evidence supports them, which already have drugs in development, and what do the top candidates actually do?**

## The databases
- **[Open Targets Platform](https://platform.opentargets.org)** (GraphQL API at `https://api.platform.opentargets.org/api/v4/graphql`): evidence linking genes to diseases (genetics, literature, animal models and more), plus known drugs and their clinical stage.
- **[UniProt](https://www.uniprot.org)** (REST API at `https://rest.uniprot.org`): curated protein function and subcellular location.

## The prompt
Paste this into a Claude Code session started in this repository (in Plan mode):

```
Question: which genes have the strongest evidence of association with Alzheimer's
disease, what type of evidence supports the top ones, which of them already have
drugs in clinical development, and what do the top five proteins do?

Use only live queries to public databases (no file downloads):
- Open Targets Platform, GraphQL API: https://api.platform.opentargets.org/api/v4/graphql
- UniProt, REST API: https://rest.uniprot.org
Discover identifiers and field names from the databases themselves. Do not guess.

Write one script, query.py, that reruns every query and saves the raw responses
to day01-introduction/claude_code_demo/outputs/.
Deliverable: report.md with at most 3 figures, every number traceable to a saved
response, the source database named for each claim, and a limitations section.

First propose a plan: the queries, how you will rank the genes, and the main risks.
Do not run anything until I approve it.
```

Once the plan has been reviewed, approve it with:

```
The plan is approved. Execute it end to end: run the queries, make the figures and
write report.md. Then rerun query.py from scratch and confirm that every number in
the report matches the saved responses.
```

## One-off requirement
The cloud environment must be allowed to reach the two hosts above (see the instructor runbook). Without that, use the offline fallback below.

## What to look for while watching
- Did the agent look up the disease identifier and the schema, or guess field names?
- Is an association score treated as evidence of causation? It should not be.
- Does the report notice that heavily studied genes score high partly because they are heavily studied?
- Are drug claims tied to a clinical phase from the database, with the source named?
- Does every number in the report appear in a saved response?

## Offline fallback (no database access needed)
A real dataset that ships inside the `scanpy` package: 700 human blood cells (single-cell RNA-seq, 765 genes). The agent installs it with `pip install scanpy igraph leidenalg`. Approve and execute with the same two steps as above.

```
End-to-end analysis of scanpy.datasets.pbmc68k_reduced() (700 human blood cells,
765 genes, bundled with the package, no download), ending in a short research report.
Questions: (1) how many distinct cell populations are there, (2) which genes mark
each one and do they match known immune biology, (3) how well do unsupervised
clusters agree with the reference labels in obs['bulk_labels']?
Rules: plan first and wait for my approval; check what preprocessing the data already
had before applying any; one script analysis.py; at most 5 figures; every number from
the script output; finish with a limitations section. Write to
day01-introduction/claude_code_demo/outputs/. Deliverable: report.md.
```
