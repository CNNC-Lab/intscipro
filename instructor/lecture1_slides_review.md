# Lecture 1 slide review

Deck: *Scientific Programming 1: Introduction* (40 slides in 9 horizontal sections). The review is based on the text of every slide, and the full content of the "What about AI?", "evolution of programming assistance", "Current landscape" (two versions), "Organization and Outline" and "Reproducibility Crisis" slides. The edits marked **applied** in the status section below have been made in the live deck; the rest are still proposals.

## What works well
- Clear arc: why computing, reproducibility, why Python, good practice, AI assistance, practicalities.
- The reproducibility section (FAIR, containers, literate programming) is exactly what the course builds on.
- The "Development Cycle" build-up animation (idea, design, write, run, "go home") is memorable.
- Using one named case (the genomics scandal) makes reproducibility concrete.

## Must fix
| # | Where | Problem | Proposed fix |
|---|---|---|---|
| 1 | Title slide, "Organization and Outline" | Contains specific dates and a date range. They go stale and the course materials no longer carry dates | Remove dates from both slides; say "Friday afternoons" and "14 sessions" |
| 2 | "Organization and Outline" | Says "12 lectures", while the schedule has 11 content sessions plus 3 project sessions (14 in total) | "14 sessions: 11 lectures with hands-on practicals, 2 project work sessions, 1 presentation session" |
| 3 | "Organization and Outline" | Repository link points to the old repository name (`intscipro-2025`) | `https://github.com/CNNC-Lab/intscipro` |
| 4 | "Organization and Outline" | "This is the first iteration of the course" will be wrong next time | Remove |
| 5 | "The evolution of programming assistance" | The progress bar "Programming Accessibility Progress: 85% Complete" is an invented number | Delete the bar, or replace it with a qualitative arrow ("more delegation, more verification") |
| 6 | Same slide, title of the third column, and the development-cycle slide "in 2025" | Years in titles and era labels age quickly | Use era names without years: "Documentation era", "Assistant era", "Agentic era" |
| 7 | "Current landscape" | Lists Windsurf, which the course no longer uses, and has an empty "Autonomous Agents" heading with no entries. Claude Code, the tool used in the live demo, is missing | Replace the "IDE-integrated" and "autonomous agents" columns with a three-way taxonomy: *chat* (ChatGPT, Claude, Gemini), *in-editor assistants* (Copilot, Cursor), *agents that act on your files and run code* (Claude Code, Codex-style CLIs, cloud agents). Name Claude Code explicitly as today's demo |
| 8 | "Reproducibility Crisis" | Statistics (20%, 11%, 6.8%) have no source on the slide | Add a one-line citation under each number, or soften to "studies repeatedly find that only a minority of computational results can be reproduced" |

## Should improve
1. **Structure for the AI section.** At present the course's most distinctive topic is five slides at the end. Move a short "how we will use AI in this course" slide up front and give the section a spine: *delegate, verify, own*.
2. **Add a slide on verifying AI output.** Concrete checks: run it on a case with a known answer, read every line you cannot explain, ask for assumptions, test edge cases, check numbers against raw data, and keep prompts and versions in the repository. This is the skill the live demo practises.
3. **Add a slide on risks.** Hallucinated functions and citations, silently wrong statistics, data privacy (never paste patient or unpublished data into a tool you have not cleared), licensing, and dependence on skills you stop practising.
4. **Counterweight to the quote.** The "nobody has to program" quotation is provocative and one-sided. Pair it with a sentence that frames the course position: "AI lowers the cost of writing code, not the cost of being wrong."
5. **Add a "what the live demo will show" slide** that previews the proteomics case: a real dataset, four research questions, the agent plans first, a human approves, and everything is verified against saved outputs. End with the question "what would you check?".
6. **Python is slow slide (about 80 KB of embedded content).** Check that it loads quickly, and add the takeaway: vectorise and use compiled libraries, so slowness rarely matters in practice.
7. **Notes.** Only one slide has speaker notes. Add notes with timing for each section; they double as a script for next year.
8. **Practicalities.** Replace the third-party online consoles with the course's own `check_installation.py` as the first thing students run.
9. **Accessibility.** Several slides rely on emoji and colour alone to carry meaning. Add text labels, and check contrast on the coloured era cards.

## Status of the edits
**Applied to the deck**
- Must-fix 1: dates removed from the title slide and the organization slide.
- Must-fix 2, 3, 4: organization slide now says 14 sessions (11 lectures, 2 project work sessions, 1 presentation session), links to `CNNC-Lab/intscipro`, and no longer says it is the first iteration.
- Must-fix 5, 6: the invented "85% complete" bar is replaced by "More delegation, more verification", the era badges carry no years, and the development-cycle title no longer says a year.
- Must-fix 7: the "Current landscape" slide is rebuilt as chat / in-editor assistants / agents that act, with Claude Code named as the live demo. The broken video embed and the Windsurf entry are gone, and the earlier build-up version of that slide was removed as redundant.
- Must-fix 8 (partly): a footnote frames the reproducibility statistics as survey results that vary by study. The speaker note on that slide flags that a citation for each number is still needed.
- Improvements 1, 2, 3, 4, 5: three new slides follow the landscape slide: *Delegate, verify, own*, *What can go wrong* (ending with "AI lowers the cost of writing code, not the cost of being wrong") and *Live demo preview*, each with speaker notes.

**Still open**
- Citations for the three reproducibility statistics.
- Improvements 6 to 9: the "Python is slow" slide, section timing notes, replacing third-party consoles with `check_installation.py`, and the accessibility pass.

## Suggested new section order
1. Why scientific computing
2. Course organization (no dates)
3. The (reproducible) development cycle
4. Why Python
5. Good programming practice
6. Working with AI: landscape, delegate-verify-own, risks (**revised**)
7. Preview of the live Claude Code demo (**new**)
8. Practicalities

## Other lectures
Only Lecture 1 has been reviewed so far. The other decks are linked from each day's README. Recurring items to check in each: dates on title slides, the repository name, mentions of tools no longer used, and unsourced statistics.
