# Theory state

updated: 2026-10-30
by: the integrator session, after the council and the space learning-attacker-prices

## Milestone open: mappings to known hard problems

Opened 2026-10-25 after Halil adopted the objective of booklet chapter 1 and
answered, on hardness that comes from a data law, "We need such mappings". The
spaces, their first and last rounds, are in `milestone.json`. Each space runs an
aims round and at least one more, and stops at BLOCKING 0 or at its last round.
The ledger is `GATES.md`. The first milestone's ledger is
`gates/2026-10-25-first-rounds.md`.

## Spaces

| Space | Question in one line | Last round | Status |
| --- | --- | --- | --- |
| `hard-problem-mappings` | which attack tasks map onto hard problems from the literature, priced on both sides | round-02 | done, BLOCKING 0 |
| `computational-limits` | lattice hardness of blind reconstruction, natural record laws | round-06 | done, BLOCKING 1 on the ZLIP sketch |
| `statistical-limits` | the trainer's price against the attacker's in one unit | round-05 | done, BLOCKING 0 |
| `oracle-and-measurement` | how the oracle and experiments realize and measure the prices | round-02 | paused, done in milestone 1 |
| `learning-attacker-prices` | a learning attacker priced in learning units, Opus builder against Opus challenger (Halil, 2026-10-28) | round-03 | done, SATISFIED yes, BLOCKING 0, critiqued by fable and sol |

## The reading folder

- `lib/theory/booklet.pdf`: 63 objects, 30 accepted, 29 borrowed, 2 open, 2
  refuted, 0 checked.
- `lib/theory/2026-10-25-first-rounds.pdf`: the reading of the first milestone.
- `lib/theory/2026-10-26-what-we-have.pdf`: superseded by the reading of 2026-10-29.
- Readings of 2026-10-27 to 2026-10-30: definitions, what Halil wants, the council, the debate,
  and the statement of the theory.
- `lib/theory/2026-10-29-what-we-have.pdf`: every finding to date, with the eighteen open
  decisions of the earlier readings merged into nine. It supersedes the 2026-10-26 one.

## Decisions taken and waiting

1. The objective of chapter 1: adopted (Halil, 2026-10-25).
2. The oracle definitions: left open while the theory develops. Both seed-access
   modes stay available and each result names the mode it needs.
3. Hardness from a data law counts, and mappings onto hard problems from the
   literature are wanted.
4. The target of milestone 2: chosen by the integrator on Halil's delegation.
5. The attacker class for lower bounds: two games, never mixed (Halil, 2026-10-25).

## The booklet is frozen for Halil's reading

Halil, 2026-10-26: "you can make it stay as is and give me a reading for me to catch you
up". Until he has read it, the integrator does not change the booklet's sources or rebuild it.
New work goes into readings built with `tools/build.py --readings-only`, and the merge into the
booklet follows his reading.

## Discussants

sol (gpt-6.1-sol, Codex CLI 0.164.0) replaces astra. argon (gemini-4-argon-high, object by
object, audited) is out of quota, and its council critiques wait (Halil, 2026-10-27). The
object-by-object protocol is set but not yet seen to finish.

## Council of 2026-10-27

`council/2026-10-27-theory-directions/`: four Opus meditations, criticized by fable and sol,
read by Halil in `lib/theory/2026-10-27-council.pdf`, five corrections and three rulings.
`council/2026-10-29-statement-of-the-theory/`: three Fable discussants, four rounds, one statement
of the theory in 26 clauses (`statement/final.md`), read in `2026-10-30-statement-of-the-theory.pdf`.
Nothing from either enters the booklet or the registers before Halil rules.

## Space learning-attacker-prices, 2026-10-28 to 2026-10-29

Four rounds until the challenger was satisfied, ten objects standing, read by Halil in
`lib/theory/2026-10-29-learning-attacker-prices.pdf`. Fable found the update stream to be the
single-index model of DPLB24, so the objects need the search gate on spectral initialization
before any enters the booklet. Ledger: the space's `GATES.md`.

## Next actions

1. Halil reads `2026-10-29-what-we-have.pdf` and `2026-10-30-statement-of-the-theory.pdf`
   and settles their decisions. argon critiques the council meditations once its quota returns.
2. The integrator merges milestone 2 into the booklet, records its rounds in the
   history chapter, rebuilds, and closes `GATES.md`. Open gates then: G5 (computational
   limits at BLOCKING 1) and G8 (no argon round yet under the new protocol).
