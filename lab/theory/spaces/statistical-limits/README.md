# Space: statistical limits

Owner: session space-statistical (local_76e17253), started 2026-10-25 by the integrator.
One session at a time.

Discussants: argon in `round-00`, then alternating astra and argon.

## Question

What does an adversary with unlimited computation achieve from what a learning
procedure releases (a model, its outputs, an intermediate representation, a
transcript), and how many samples, training runs or queries does it need? The
price is to be stated in the trainer's own units, so it can later be set against
the computational price of the space `computational-limits`.

## Scope

In scope: membership inference and its sample complexity, reconstruction and the
fibers of the training map, attribute and property inference, differential
privacy and its variants read as hockey-stick bounds, information-theoretic
limits (data processing, Fano, rate distortion, usable information read as an
information quantity), and the statistical side of the learning-oracle results
already accepted (`lib/theory/booklet.pdf`, chapter on the learning oracle).
The statistical baseline of Halil's reconstruction example in `CONTEXT.md`: what
an unbounded reconstructor can recover from an intermediate representation, and
how that bound compares with the trainer's own learning problem.

Out of scope: lower bounds against efficient or restricted algorithms (space
`computational-limits`), and how a price is measured by the oracle or by
experiment (space `oracle-and-measurement`). A result that needs one of them
names the other space's slug and leaves the work there.

## Where to start

- `sink/formalizing/facts.md`, sections: Membership inference and sample
  complexity, Reconstruction and fibers of the training map, Differential privacy
  variants, Robustness and concentration, Restricted-class attackers and usable
  information (the information-theoretic entries).
- `sink/formalizing/results.md`, section Learning oracle (HE-ML), for what is
  already proven, and section Adversary interface.
- `sink/formalizing/problems.md`: `prob-security-profile-curve`,
  `prob-same-units-matched-budget-separation`, `prob-attacker-estimation-threshold`,
  `prob-cdp-for-reconstruction-from-weights`, `prob-single-index-gaussian-fiber`,
  `prob-support-recovery-from-trained-network`, `prob-shadow-model-lower-bound`.
- The library, `lib/literature/notes/<venue>/<Key>.md` and the PDFs beside them.
  Read the paper itself for any statement the round relies on.

## Milestone 2: mappings to known hard problems (opened 2026-10-25)

Rounds `round-03` to `round-05`. `round-03` states the aims of this milestone.
Discussant: sol only until argon's quota resets (about 2026-10-27 13:30), each
round's summary saying so.

The adopted objective asks for a natural procedure where the attacker's price
exceeds the trainer's by a named margin. This space owns that comparison in the
statistical regime.

1. The statistical baseline of blind reconstruction. An unbounded seed-blind server
   of a frozen client of `def-seed-blind-reconstruction-game` learns the records
   only up to the symmetry group of the record law, for Gaussian records up to a
   common rotation. State and prove it, with the sample price of reaching that
   limit.
2. The same-units comparison on the mappings of the first milestone: the trainer's
   price in samples or runs against the attacker's, for the split-learning
   separation and for the single-index reconstruction, sharpening or refuting
   `conj-same-units-gap` (`prob-same-units-matched-budget-separation`).
3. `prob-train-access-collapses-sample-price`: does Train access collapse the
   sample price of HSU25 Theorem 3.1?

## Round log

The space session appends one line per round: the folder, the date, the
discussant, the verdict counts and the BLOCKING count.

- `round-00`, 2026-10-25, astra (fell back from argon, whose headless call could not read files), ACCEPT 2, REVISE 14, REJECT 0, BLOCKING 14.
- `round-01`, 2026-10-25, astra (fell back after two argon timeouts and an astra usage limit, as the summary records), ACCEPT 14, REVISE 4, REJECT 0, BLOCKING 3.
- `round-02`, 2026-10-25, argon, ACCEPT 18, REVISE 0, REJECT 0, BLOCKING 0. The space stops here.
- `round-03`, 2026-10-25, sol (argon quota), ACCEPT 4, REVISE 4, REJECT 1, BLOCKING 7.
- `round-04`, 2026-10-25, sol (sol again, argon quota), ACCEPT 6, REVISE 1, REJECT 0, BLOCKING 1.
- `round-05`, 2026-10-25, sol (sol again, argon quota), ACCEPT 7, REVISE 0, REJECT 0, BLOCKING 0. The space stops here for milestone 2.
