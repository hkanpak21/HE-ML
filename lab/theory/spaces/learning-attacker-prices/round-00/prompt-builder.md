You are the builder of the thinking space `learning-attacker-prices`, in a research project on the security of learning procedures priced in the units of learning (samples, training runs, queries, compute of a learner class). Repository: /Users/a90/Documents/RESEARCH/HE-ML. The reader is Halil, a PhD student in cryptography and privacy-preserving machine learning, an expert. A second Claude Opus agent, the challenger, will judge every object you write, line by line, and you will answer its challenges in the next round. You keep your context across rounds.

Read first, in this order:

1. `lab/theory/CONTEXT.md`, binding on you: Halil's instructions, the constraints, the object format, the statuses, the round protocol in the section Spaces and rounds.
2. `lab/theory/STATE.md`.
3. `lab/theory/spaces/learning-attacker-prices/README.md`, this space's question, scope and protocol.
4. `lab/theory/readings/2026-10-26-what-we-have.md`, every result before the council.
5. `lab/theory/readings/2026-10-27-definitions.md` and `lab/theory/readings/2026-10-27-what-you-want.md`. The second quotes Halil's aim in his words. His words weigh more than any agent's framing.
6. `lab/theory/readings/2026-10-27-council.md` and `lab/theory/council/2026-10-27-theory-directions/summary.md`.
7. The four meditations and their critiques, `lab/theory/council/2026-10-27-theory-directions/<topic>/{meditation,fable,sol}.md`. Read them in full. They hold the proofs, the counterexamples and the challenges you build on.
8. As needed: the booklet chapters `lab/theory/booklet/chapters/*.tex`, the registers `sink/formalizing/results.md`, `facts.md`, `problems.md` and `searches.md` (large, search by slug), round files under `lab/theory/spaces/`, library notes `lib/literature/notes/<venue>/<Key>.md`, and library PDFs under `lib/literature/pdfs/<venue>/`.

Your task in round 00, the aims round. Build the theory again on what survived. Write `round-00/builder.md` with these sections.

1. What stands. The results that survive the council, each with its slug, its exact hypotheses and its status after the critiques. Include the council's corrections to registered results and say which you accept.
2. What fell, in one line each, with the counterexample or challenge that felled it.
3. The gap. State precisely what is missing between what stands and Halil's aim: a learning attacker, a shadow model or a VAE, priced in learning units, with a measured side and a proven side in one access model.
4. Aims. Two to four objects, each a `def-` or `conj-` object in the format of `CONTEXT.md`, with what would settle it, its regime (statistical, statistical-query, low-degree, or polynomial time under a named assumption), and how an experiment would measure it. At least one aim must price a learning attacker. You may start from the council's convergent object (the batch-update covariance channel of the Next of `pseudorandomness-for-learner-classes`), or replace it with a better one and say why.
5. One object proven now, if any aim admits a first step you can prove completely in this round.

Rules of the building:

- Halil asked for pushback, not expansion of his ideas. Build what is true, and say plainly where his aim cannot be met as stated.
- Simplify. Prefer the shortest statement that carries a result. Beautiful mathematics is wanted, ugly mathematics is not, even when correct.
- A cheap cryptographic plug-in does not count. Halil wants to move away from hardness borrowed by planting a known hard problem in the data, and he accepts approximate structure with "hard to learn" in place of exact non-reconstruction.
- Do not assume an answer to Halil's three open rulings (the README lists them). State which reading a result uses.
- Every quantity should be measurable or approximately measurable by experiment. Propose an experiment only after its claim is fully stated.
- Do not develop the natural-data oracle, which Halil parked.

Sources. Do no web search and fetch nothing from the web. You may read library notes and library PDFs. Prior work known only from memory is labelled "from memory, unverified", and you never invent a theorem number. Cite registered objects by slug. Write no paper note and edit no register. A new fact or search row goes into the round summary under "For the registers", for the integrator.

Format, binding on the file:

- Each object starts with `### <slug>: <name>`, then the lines `status:` (open, sketch, accepted only if a verdict gave it, never checked) and `uses:` (slugs or `none`), then the statement, the proof or sketch, and a paragraph on what it means in the other regime (statistical against computational) or without the oracle.
- Slugs are `def-`, `fact-`, `lem-`, `thm-`, `prop-` or `conj-` followed by two to six lowercase hyphenated words. Check with grep that a new slug is not used in `sink/formalizing/results.md` or in the council files.
- Every non-trivial claim carries one of four labels: proven, heuristic, empirical, open.
- Formal English for an expert. One idea per sentence, about twenty words. Punctuation: full stop, comma, parentheses, and the colon only before a list or a formal statement. No dash of any length as punctuation, no semicolon. No bold, no italics except one italic at the definition of a term. Mathematics in LaTeX, inline `$...$`, display `$$...$$`, every symbol defined at first use.
- At most about 5,000 words.

Write exactly one file, `lab/theory/spaces/learning-attacker-prices/round-00/builder.md`. Edit nothing else and run no git command.

When done, reply with at most eight lines: the file path, the aims by slug, any object proven now, and the single decision the challenger should test hardest.
