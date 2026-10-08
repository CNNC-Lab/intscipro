# Demo: an end-to-end analysis with Claude Code (15 minutes)

An AI coding agent answers a real biomedical research question **by querying public databases live**, then writes a short research report. Nothing is downloaded and no data is stored in the repository: the agent sends small queries and works with the responses. Everything runs inside one cloud session.

## The question
**Alzheimer's disease: which genes and proteins have the strongest evidence of association, what kind of evidence supports them, which already have drugs in development, and what do the top candidates actually do?**

## The databases
- **[Open Targets Platform](https://platform.opentargets.org)** (GraphQL API at `https://api.platform.opentargets.org/api/v4/graphql`): evidence linking genes to diseases (genetics, literature, animal models and more), plus known drugs and their clinical stage.
- **[UniProt](https://www.uniprot.org)** (REST API at `https://rest.uniprot.org`): curated protein function and subcellular location.

## The prompt
Paste this into a Claude Code session started in this repository:

```
Answer a real biomedical research question by querying public databases live.
Do not download datasets or files; use small API queries only.

Question: for Alzheimer's disease, (1) which genes have the strongest evidence of
association, (2) what types of evidence support the top ones, (3) which of them
already have drugs in clinical development, and (4) what do the top five proteins
do (function and subcellular location)?

Databases
- Open Targets Platform GraphQL API: https://api.platform.opentargets.org/api/v4/graphql
- UniProt REST API: https://rest.uniprot.org
Do not assume field names or identifiers: discover them (search for the disease,
inspect the GraphQL schema) and show me what you found.

Rules
- Plan first and wait for my approval before running anything.
- One script, query.py, that reruns every query and saves the raw JSON responses
  to day01-introduction/claude_code_demo/outputs/.
- At most 3 figures. Every number in the report must come from a saved response.
- Say which database each statement comes from.
- Finish with a limitations section. Deliverable: report.md.
```

## One-off requirement
The cloud environment must be allowed to reach the two hosts above (see the instructor runbook). Without that, use the offline fallback below.

## What to look for while watching
- Did the agent look up the disease identifier and the schema, or guess field names?
- Is an association score treated as evidence of causation? It should not be.
- Does the report notice that heavily studied genes score high partly because they are heavily studied?
- Are drug claims tied to a clinical phase from the database, with the source named?
- Does every number in the report appear in a saved response?

## Offline fallback (no network access needed)
A real dataset that ships inside the `scanpy` package: 700 human blood cells (single-cell RNA-seq, 765 genes). Run `pip install scanpy igraph leidenalg` first.

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
