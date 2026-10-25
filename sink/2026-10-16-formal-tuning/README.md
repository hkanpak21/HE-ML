# Formal tuning of the learning oracle

Opened 2026-10-16 at Halil's request. A builder and a challenger take turns to
turn the learning oracle of
`lib/reports/2026-10-16-halil-learning-oracle-definition.pdf` (source
`lib/reports/src/2026-10-16-halil-learning-oracle-definition.tex`) into a tested
formal theory: definitions in their simplest form, and non-trivial proofs that
use the oracle. The orchestrating agent launches each turn and keeps the round
log below. Nobody else writes here.

Halil reads only `final/learning-oracle-theory.pdf`. The rounds are the record
behind it.

## The goal, in Halil's words

"Using our new AI oracle create non trivial proofs." "I want non trivial proofs
which having an AI oracle inside that when AI oracle is removed we need to
resolve a much larger learning problem such as internal workings of transformer
based models but we can delegate proof and measure privacy and security using
AI oracles." "I want a really good and well tested formal definition and theory
around it." "In the end I want ... only the finalized version of definitions in
its simplest format and some prominent proofs used by that."

## Roles

The challenger selects non-trivial problems in AI security and privacy, reads
the builder's proofs, and in each round either accepts and proposes new
problems, or challenges flaws and unnecessary complications. It never edits the
builder's files.

The builder keeps the canonical theory in `theory/CURRENT.md` (definitions and
the register of statements), and in each round answers every open challenge and
writes or revises proofs. It never edits the challenger's files.

## Non-triviality, the acceptance bar for a theorem

A theorem counts as non-trivial (tag `NONTRIVIAL` in a verdict) only when all
four hold.

1. The oracle is inside the statement or the proof: the result concerns a
   procedure in the learning-oracle model, or a quantity defined by oracle calls.
2. Removing the oracle leaves a much harder problem. Proving the same statement
   for a concrete learning function, a transformer trained by stochastic
   gradient descent for instance, would require knowing the law of the trained
   model, which nobody can write down.
3. The learning-specific part is delegated. The bound or the guarantee depends
   on the learning function only through quantities that oracle calls define and
   can measure, so it holds for every learning function, transformers included.
4. It is not trivial for the oracle. The statement fails, or becomes vacuous,
   for at least one of the two degenerate oracles: the one that lets the
   adversary name honest data with the honest seed, and the one that gives the
   adversary only what it can already compute.

Orchestrator ruling, after round 02. When the actor of a statement is an
experimenter or an auditor, criterion 4 is tested against the drawn-seed
discipline of item 3 of def-degenerate-oracles. That discipline gives the actor
only what a real training service gives it, fresh hidden randomness, which is
the "only what it can already compute" case for that actor. A certificate that
needs the oracle's explicit seed and fails under drawn seeds therefore meets
criterion 4. The challenger of round 02 asked for this ruling.

## File protocol

```text
README.md                this file, with the round log
GATES.md                 the completion ledger of the orchestrator
scripts/                 verify.mjs (structure and verdict checks), build.mjs (PDFs)
theory/CURRENT.md        the living definitions and statement register, builder only
round-00/challenger.md   the challenger's opening: problems and challenges to the report
round-NN/builder.md      the builder's turn in round NN
round-NN/challenger.md   the challenger's turn in round NN
final/learning-oracle-theory.md  the finalized definitions and prominent proofs
final/audit.md           the challenger's audit of the final document
```

Every markdown file compiles to a PDF beside it with
`node scripts/build.mjs <file.md>`. Mathematics is pandoc markdown: `$...$`
inline, `$$...$$` display, LaTeX commands inside, ASCII or plain Unicode text
outside.

Names are slugs, never letter-number keys. A definition is `def-<slug>`, a
theorem `thm-<slug>`, a lemma `lem-<slug>`, a challenge `ch-<slug>`. A file
names an item by putting its slug in square brackets, `[thm-dataflow-composition]`.

Every challenger file ends with a verdict block, one line per item it judged,
and one blocking count, inside a `text` code block under the heading
`## Verdicts`:

```text
VERDICT def-learning-oracle ACCEPT
VERDICT thm-dataflow-composition REVISE
VERDICT thm-shadow-sample-complexity ACCEPT NONTRIVIAL
BLOCKING 2
```

`ACCEPT`, `REVISE` or `REJECT`, with `NONTRIVIAL` after `ACCEPT` when the
theorem meets the bar above. `BLOCKING` counts the open challenges that would
make a stated result false or a definition ill-posed. The latest verdict on a
slug is the one that counts.

Every claim carries one of four labels, proven, heuristic, empirical or open.
Terms follow `CONTEXT.md` at the repository root: data space, dataset, model
space, hypothesis class, learning function, evaluation map, view, choices,
distinguish, invert, steer.

## Stopping rule

Set by the orchestrator, since Halil gave no stop signal. The rounds stop when
all of these hold, or after round 12, whichever comes first.

- At least six review rounds after the opening.
- The latest challenger file has `BLOCKING 0`.
- Every definition was accepted in the last two challenger files.
- At least six theorems or lemmas stand accepted, three of them `NONTRIVIAL`.

Halil fixed the end on 2026-10-17: the rounds finish with round 10, whose
challenger turn also writes the audit.

Then the builder writes `final/learning-oracle-theory.md`, the challenger
audits it in `final/audit.md` (`FINAL ACCEPT` or `FINAL REVISE`), and the
builder revises until the audit accepts.

## Round log

One line per round, written by the orchestrator after the challenger's turn.

| Round | Builder | Challenger | Blocking |
| --- | --- | --- | --- |
| round-00 | none, opening turn | 19 challenges to the report's definitions and propositions, 5 problems set (coupling certificate, black-box certifiability, bank soundness, dataflow composition, replay-audit steering) | 5 |
| round-01 | all 19 opening challenges accepted, definitions rebuilt, 7 items proven, composition and steering not attempted | 9 accepted, none non-trivial yet, black-box certifiability false as stated (query universe), composition and replay-audit sharpened | 1 |
| round-02 | all 7 round-01 challenges fixed, dataflow composition and replay-audit steering proven in full, one challenger conjecture refuted | 13 accepted, 4 non-trivial (coupling certificate, black-box certifiability, dataflow composition, replay-audit steer), 12 non-blocking challenges, steering to active-choice dichotomy and record-level certificate | 0 |
| round-03 | 12 challenges fixed, stateful clients and the CKKS realization scope handled, active-choice dichotomy and record-level certificate proven, nine open problems recorded, definitions cut | 14 accepted, 6 non-trivial, isolated-client definition leaks the dataset node (counterexample), steering to a smoothed-choice certificate | 1 |
| round-04 | dataset-node leak fixed, smoothed-choice certificate proven with a dimension-free change-of-measure part, sphere-code lemma proven | 17 accepted, 7 non-trivial, 7 non-blocking challenges, steering to split the change-of-measure certificate and sharpen its lower bound, prominent proofs named | 0 |
| round-05 | 7 challenges fixed, bounded-deviation transfer split out and proven with a sharp constant, first final draft (18 pages, 5 theorem sections) | transfer accepted as non-trivial, definitions accepted for the second round running, 3 blocking errors in the final draft (scalar direction, opening hypotheses, round count) | 3 |
| round-06 | 3 draft errors and 8 other challenges closed, two partial disputes argued, symbols cleaned | 21 accepted, 8 non-trivial, definitions accepted a third time, 2 one-clause errors left in the final document (finite query set in the opening, accuracy-level condition in the transfer) | 2 |
| round-07 | both one-clause errors closed, 5 other challenges closed, 92 summary sentences audited (14 false, fixed) | definitions accepted a fourth time, 14 results accepted, one clause in the composition cost statement omits the strategy's own Train calls | 1 |
| round-08 | strategy-call clause restored, 98 cost sentences audited (25 changed), drawn-seed part of the transfer restated | all 21 items accepted, 8 non-trivial, composition and transfer re-derived from scratch and holding, 3 non-blocking clarity fixes due before the audit | 0 |
| round-09 | 3 clarity fixes, statements frozen, 51-entry source table, 5 defects found and left for review | 45 of 51 entries match, 4 blocking one-clause errors (seed-map channel, per-round thresholds, active-choice conditions, a heuristic labelled proven), 7 instructions for round 10 | 4 |
| round-10 | 7 instructions applied, 3 as minimal variants with reasons | 21 of 21 accepted, 8 non-trivial, audit FINAL ACCEPT with 7 minor one-clause findings | 0 |
