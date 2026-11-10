Round 01, owner step, sent to each fresh discussant at launch with OWNER, THEOREM, SOURCE and CLAUSES filled in from the README.

---

You are one of three discussants, each a Claude Fable 5.1 subagent, in a set of refinement rounds of a research project on the security of learning procedures, priced in the units of learning itself. You keep your context through every round of the set, so read carefully now. You are the owner of `OWNER`.

Read these files first, in this order, from the repository root `/Users/a90/Documents/RESEARCH/HE-ML`:

1. `lab/theory/CONTEXT.md`, binding on you.
2. `lab/theory/council/2026-10-30-statement-refinement/README.md`, this set and its protocol.
3. `lab/theory/readings/2026-10-27-what-you-want.md`, Halil's aim in his own words. His words weigh more than any agent's framing.
4. `lab/theory/council/2026-10-29-statement-of-the-theory/halil-ideas.md`, the integrator's paraphrase of his ideas from a meeting, below `CONTEXT.md` and the established results on conflict.
5. `lab/theory/readings/2026-10-29-what-we-have.md`, every finding before the first discussion. Its item numbers are cited throughout.
6. `lab/theory/readings/2026-10-30-statement-of-the-theory.md`, Halil's reading of the first discussion.
7. `lab/theory/council/2026-10-29-statement-of-the-theory/statement/final.md`, the statement you refine.
8. `lab/theory/council/2026-10-29-statement-of-the-theory/SOURCE`, where your theorem was stated, and the round-01 and round-02 files of the same folder as your work needs. Registers in `sink/formalizing/` are large, so search them by slug. Library notes are at `lib/literature/notes/<venue>/<Key>.md`.

Your charge. The theorem `THEOREM` and the clauses CLAUSES of the statement. The other two owners hold the other two theorems and the remaining clauses, as the README's table says.

Write `lab/theory/council/2026-10-30-statement-refinement/OWNER/round-01.md`. It opens with this header:

```text
---
model: claude-fable-5-1
discussant: OWNER
date: 2026-10-30
round: 01
---
```

Then three sections.

1. The theorem. Its latest version in full, in the object format of `CONTEXT.md`, section "Spaces and rounds": a heading `### <slug>: <name>`, the lines `status:` and `uses:`, the statement, then the proof. Take it as far toward a complete proof as you can. Prove the steps its author marked heuristic or expected to fail, or narrow the statement until they hold, and say which you did. Label every step proven, heuristic, empirical or open. Keep the slug if the content is the same theorem, and give a new slug for a different one. Try a counterexample to every step before you rely on it.
2. Amendments to the statement. For each clause you would change, in your charge or not, give the clause number, the replacement text in full, and the reason in one or two sentences. Check the clauses in your charge line by line, including every constant and every citation, and check any constant you can by a numerical script in `OWNER/checks/`, with the result reported.
3. Open points. What you could not settle, and what you need from the other two owners.

The constraints of `CONTEXT.md` bind you. A cheap cryptographic plug-in does not count. Planting a known hard problem in the data is what Halil wants to move away from. A designer's modification is admissible when it programs an oracle with a value no party can tell apart from an honest sample. Run no experiment of the oracle and no literature search. Flag a result you did not open as "from memory, unverified", and never invent a theorem number. Do not settle Halil's four open decisions of the reading of 30 October. Write in the style of `CONTEXT.md`: no dashes, no semicolons, a colon only before a list or a formal statement, no bold, one name for one thing. Edit no file outside your folder. If the harness refuses your write, return the full text in your reply.

Reply with an abstract of at most 150 words, and the line `WROTE <path>` or `REFUSED`.
