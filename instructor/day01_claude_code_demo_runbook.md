# Live demo runbook: Claude Code querying public databases (15 minutes)

**What:** in a cloud Claude Code session on this repository, the agent answers "which genes are most strongly associated with Alzheimer's disease, with what evidence, which have drugs, and what do they do?" by querying Open Targets and UniProt live, and writes a short report. No files are downloaded and nothing is stored in the repository.

## One-time requirement (2 minutes, only you can do this)
The cloud sandbox blocks outbound traffic to anything except package registries and GitHub by default. Allow the two databases:

1. In claude.ai/code open the environment menu in the session title bar, then **Edit**.
2. Under **Network access** choose **Custom**, keep the default package-manager list, and add these Allowed domains:
   - `api.platform.opentargets.org`
   - `rest.uniprot.org`
3. Start a **new** session after saving (new sessions pick up the changed environment).

Quick check, as the first message of the new session: *"Run `curl -s -o /dev/null -w '%{http_code}' https://rest.uniprot.org/uniprotkb/P04637.json` and tell me the status code."* A `200` means the demo can run. This costs almost nothing.

If you cannot or do not want to change the network settings, use the **offline fallback** prompt in [`claude_code_demo/README.md`](../day01-introduction/claude_code_demo/README.md): real single-cell data that ships inside the `scanpy` package.

Not yet tested end to end: the database hosts are blocked in the environment this runbook was written in, so the queries and the expected results below have not been run.

## Before the session
1. Open a Claude Code cloud session on this repository, in **Plan** mode (mode dropdown next to the prompt box).
2. Have [`claude_code_demo/README.md`](../day01-introduction/claude_code_demo/README.md) open to copy the prompt.

## Timeline
| Min | What happens |
|---|---|
| 0-2 | Frame it: a real question, live databases, a human approves a plan and verifies the result |
| 2-5 | Paste the prompt. Read the plan aloud and ask the room: what would you check? Approve (switch to Auto or Accept edits) |
| 5-11 | It runs. Narrate: schema discovery, queries, saved responses, figures |
| 11-15 | Open `outputs/report.md`. Pick two numbers and find them in the saved JSON. Discuss the limitations section |

## Teaching moments
| Moment | Look for |
|---|---|
| Discovering instead of guessing | Does it search for the disease identifier and inspect the GraphQL schema, or invent field names? |
| Score is not causation | Association scores summarise evidence across sources; they do not show a gene causes the disease |
| Study bias | Well-studied genes accumulate literature evidence. Does the report say so? |
| Evidence types | Does it separate genetic evidence from literature mining and animal models when ranking? |
| Drugs | Are clinical-phase claims tied to the database, with the source named? |
| Numbers match responses | Spot-check two values in the saved JSON |

Expectation to check, not a result: well-known Alzheimer's genes such as `APP`, `PSEN1`, `APOE`, `MAPT` and `TREM2` would be expected near the top. If the output disagrees, that is a discussion point, not a failure.

## Steering prompts (only if needed)
- *"Show me the exact query you sent and the field in the response that you used for this number."*
- *"How much of this ranking could be explained by how much each gene has been studied?"*
- *"Which of your claims is not supported by a saved response?"*

## Keeping credits low
Plan mode first, one session, three figures at most, no web search. The queries return small JSON, so the cost is the agent's reasoning, not computation. If time runs short, stop after the plan and discuss it.
