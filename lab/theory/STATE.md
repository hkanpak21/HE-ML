# Theory state

updated: 2026-10-25
by: the integrator session of 2026-10-25, opening the second milestone

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
| `hard-problem-mappings` | which attack tasks map onto hard problems from the literature, priced on both sides | none | starting |
| `computational-limits` | blind inversion of ReLU clients and natural record laws | round-02 | milestone 2 from round-03 |
| `statistical-limits` | the trainer's price against the attacker's in one unit | round-02 | milestone 2 from round-03 |
| `oracle-and-measurement` | how the oracle and experiments realize and measure the prices | round-02 | paused, done in milestone 1 |

## The reading folder

- `lib/theory/booklet.pdf`: 63 objects, 30 accepted, 29 borrowed, 2 open, 2
  refuted, 0 checked.
- `lib/theory/2026-10-25-first-rounds.pdf`: the reading of the first milestone.

## Decisions taken and waiting

1. The objective of chapter 1: adopted (Halil, 2026-10-25).
2. The oracle definitions: left open while the theory develops. Both seed-access
   modes stay available and each result names the mode it needs.
3. Hardness from a data law counts, and mappings onto hard problems from the
   literature are wanted.
4. The target of milestone 2: chosen by the integrator on Halil's delegation.
5. The attacker class for lower bounds: two games, never mixed (Halil, 2026-10-25).

## Discussants

sol (gpt-6.1-sol at high reasoning, Codex CLI 0.164.0) replaces astra. argon
(gemini-4-argon-high, permissions bypassed, writing object by object into a
scratch file, audited after every call) is out of quota until about 2026-10-27
13:30. Until then every round uses sol and its summary says why. The stress test
of 2026-10-25 ran argon-high for 25 turns with no stream timeout before the quota
ran out, so the object-by-object protocol is set but not yet seen to finish.

## Next actions

1. The three spaces run their rounds.
2. The integrator merges, rebuilds, writes a reading for results worth Halil's
   time, and closes the milestone against `GATES.md`.
