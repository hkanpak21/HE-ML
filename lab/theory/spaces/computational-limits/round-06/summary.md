# Round 06, summary

Space `computational-limits`, 2026-10-26, a one-object round the integrator added
to milestone 2. Discussant sol (gpt-6.1-sol): sol again, argon quota. Verdicts:
ACCEPT 0, REVISE 1, REJECT 0. BLOCKING 1. The space stops here, as the integrator
asked, and `thm-zlip-reductions` merges as a sketch with its challenge recorded.

The round repaired the time model of `thm-zlip-reductions`. Time is counted in
expectation, and probabilistic Turing algorithms run in $\mathsf M$, with fair coins
from Gaussian signs and integers found by binary search with comparisons. Sol
accepted the variance repair (`ch-zlip-variance-access` closed: $\sigma_s^2$ is an input
of part (b)) and agreed that expected time removes the support obstruction.
`ch-zlip-model-realization` stays open, on three implementation obligations. First,
a real width has no finite encoding to hand the sampler: state $s$ and $s_0$ as
rationals, or supply certified approximations and bound the precision requested.
Second, an expected-time bound needs control outside the good event of DvW22 Lemma
3.6: compute the Gram-Schmidt lengths and abort above the threshold, so the abort
probability is the existing $300d2^{-d}$. Third, the records have unbounded support,
so rational recovery, the Hermite normal form and Extract need explicit abort rules
on norms and determinants, or expected bounds on their encoding lengths. Sol
judges the algebra of both reductions unchanged and correct. What remains is
bookkeeping inside the model, with each step's repair named above.

## Slugs accepted

None in this round. The milestone's accepted objects are listed in the round-05
summary.

## Challenges open

Blocking: `ch-zlip-model-realization`, with the three obligations above.

Not blocking: `ch-zlip-public-parameters`. Say that the variance input belongs to
part (b) only, or give the source problem in part (a) the same public parameters.

Closed: `ch-zlip-variance-access`.

## For the registers

- `thm-zlip-reductions`: merge as a sketch. The reductions are mathematically
  sound (accepted line by line by sol in rounds 05 and 06), with the open item
  `ch-zlip-model-realization` (width encoding, Gram-Schmidt abort, abort rules on
  encoding lengths).
- No new facts, searches or problems in this round.

Discussant calls: one sol call, exit 0.
