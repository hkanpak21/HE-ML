Round 01, aspect. Sent to each discussant through its kept context, with ASPECT, QUESTION, OTHER_A and OTHER_B filled in from `selection.md`.

---

Your aspect is `ASPECT`: QUESTION. The other two discussants hold `OTHER_A` and `OTHER_B`, so leave those to them except where yours touches them.

Write `lab/theory/council/2026-10-29-statement-of-the-theory/ASPECT/round-01.md`. It opens with this header:

```text
---
model: claude-fable-5-1
discussant: ASPECT
date: 2026-10-29
round: 01
---
```

Then five sections.

1. Halil's idea. State his idea on this aspect in its strongest exact form, as he would want it stated, with every term defined before use. Cite where he said each part: a file and section, or an item of `halil-ideas.md`.
2. Critique. Say where the idea is false, ill-posed, empty or already known. Give counterexamples, and name known results with author, venue, year and theorem number. Flag a result you did not open as "from memory, unverified", and never invent a theorem number. Say also where the idea is right and the theory has not yet used it.
3. A better formulation. Give it as objects in the format of `CONTEXT.md`, section "Spaces and rounds": a heading `### <slug>: <name>`, the lines `status:` and `uses:`, the statement, then the proof or sketch. A claim's status is open or sketch, and each step of an argument carries one of proven, heuristic, empirical or open. Prefer few exact objects to many loose ones. Every quantity must be measurable by experiment.
4. What the current theory supports or blocks, by item number of `readings/2026-10-29-what-we-have.md`.
5. The statement from this aspect. At most five sentences that belong in a statement of the whole theory.

The constraints of `CONTEXT.md` bind you. A cheap cryptographic plug-in does not count. Planting a known hard problem in the data is what Halil wants to move away from. A designer's modification is admissible when it programs an oracle with a value no party can tell apart from an honest sample. Write in the style of `CONTEXT.md`: no dashes, no semicolons, a colon only before a list or a formal statement, no bold, one name for one thing. Edit no other file. If the harness refuses your write, return the full text of the file in your reply instead.

Reply with an abstract of at most 150 words, and the line `WROTE <path>` or `REFUSED`.
