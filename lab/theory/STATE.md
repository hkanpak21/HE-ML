# Theory state

updated: 2026-10-25
by: the integrator session of 2026-10-25, after merging the first rounds

## Milestone closed: first rounds

Opened and closed on 2026-10-25. Each space ran rounds 00 to 02 and stopped at
BLOCKING 0. The integrator merged every accepted object into the booklet, moved
the register items into `sink/formalizing/`, recorded its checks in
`integration-log.md`, and wrote one reading. The ledger is `GATES.md`.

## Spaces

| Space | Question in one line | Last round | Status |
| --- | --- | --- | --- |
| `statistical-limits` | what an unbounded adversary gets, priced in the trainer's units | round-02 | done, BLOCKING 0, merged |
| `computational-limits` | what an efficient or learning adversary gets, by reduction to known learning problems | round-02 | done, BLOCKING 0, merged |
| `oracle-and-measurement` | how the oracle and experiments realize and measure those prices | round-02 | done, BLOCKING 0, merged |

## The reading folder

- `lib/theory/booklet.pdf`: 63 objects, 30 accepted, 29 borrowed, 2 open, 2
  refuted, 0 checked. Appendix B holds every merged proof from its round file.
- `lib/theory/2026-10-25-first-rounds.pdf`: the five results worth reading first,
  and the decisions.

## Decisions waiting for Halil

1. Adopt or change the objective of chapter 1.
2. The two oracle definitions. Proposal in booklet section 6.1.
3. The first target. Proposal: `thm-blind-split-seed-separation` with
   `conj-seed-price-is-ngca-price`.
4. The attacker class for lower bounds. Proposal: two games, never mixed.
5. Whether a hard record law, the pancakes of homogeneous CLWE, meets the rule
   that a cryptographic plug-in does not count.

## Discussants

argon runs as gemini-4-argon-medium, one call at a time. The argon-high calls of
this milestone died on the backend's stream idle timeout when several ran at
once. astra's plan ran out after about five calls of 130,000 to 170,000 tokens
each and reset at 21:27. Medium-tier argon reviews were short, so the integrator
re-derived every proof.

## Next actions

1. Halil reads the reading and the booklet and settles the decisions.
2. The next milestone opens on the chosen target, with its own `GATES.md`.
