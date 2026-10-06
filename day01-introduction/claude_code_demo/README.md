# Demo: an end-to-end analysis with Claude Code

In this live demo the instructor directs an AI coding agent (**Claude Code**, running in the cloud) through a complete research workflow on a real dataset, from raw data to a finished research report. Your job is to watch critically: what does the agent decide on its own, what does it get right, and what does a scientist still have to check?

## The dataset
**Mouse cortex protein expression in a Down syndrome model** (UCI Machine Learning Repository, CC BY 4.0). 72 mice, 77 proteins measured in cortical nuclei, with three experimental factors: genotype (control vs Ts65Dn trisomic mice), drug treatment (memantine vs saline) and a learning paradigm (contextual fear conditioning vs a no-learning control). See [`template/data/README.md`](template/data/README.md) for the data dictionary.

> Higuera C, Gardiner KJ, Cios KJ. Self-organizing feature maps identify proteins critical to learning in a mouse model of Down syndrome. *PLoS ONE* 10(6): e0129126.

## Research questions
1. Which proteins differ between Ts65Dn and control mice?
2. Does memantine change the protein profile, and does it move Ts65Dn mice towards the control profile?
3. Does learning stimulation change expression, and does that depend on genotype or treatment?
4. Can the experimental group be predicted from protein expression, and which proteins matter most?

## What to look for while watching
- What did the agent assume about the experimental design, and was it right?
- How were missing values and repeated measurements handled?
- Which results survive multiple-testing correction?
- Do the numbers in the report match the saved result tables?
- Which of the agent's choices would you have made differently?

## The project brief
[`template/`](template/) is the starting repository for the demo: the brief the agent reads first ([`CLAUDE.md`](template/CLAUDE.md)), the data dictionary, and the scripts that fetch and validate the data. Writing a good `CLAUDE.md` for your own project is the Day 1 take-home exercise.
