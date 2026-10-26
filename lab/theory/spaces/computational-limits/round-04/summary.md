# Round 04, summary

Space `computational-limits`, 2026-10-25. Discussant sol (gpt-6.1-sol): sol again,
argon quota, since argon is out of quota until about 2026-10-27 13:30.
Verdicts: ACCEPT 4, REVISE 2, REJECT 0. BLOCKING 3.

Round 04 proved the three kept aims of milestone 2 in four short objects, after
Halil's instruction to simplify, and withdrew aim 1 with its two facts. Sol
accepted `lem-agreement-detection` line by line, the label-recovery proposition
with its primitive-label lemma and its SQ detection clause, and the two borrowed
facts. It found three blocking gaps, all local. The direction $U^\top t$ extracted
from a reconstruction can vanish, so the coarse theorem must return a uniform
direction in that case (`ch-coarse-zero-output`). The upper ZLIP reduction is false
for widths below one, by a counterexample at width $d^{-1/4}$
(`ch-zlip-small-width`). And the security conclusions of both lattice theorems
need hardness stated in the same exact-arithmetic model as the reductions
(`ch-hardness-computation-model`). Sol called the coarse reconstruction theorem
the strongest new result of the round and the conditioning-free rounding bound of
the ZLIP upper reduction its useful new argument. Round 05 repairs the two
theorems.

## Slugs accepted

- `fact-lll-recovers-discrete-hidden-labels`
- `fact-discrete-gaussian-samples-generate`
- `lem-agreement-detection`
- `prop-blind-lll-label-recovery`

## Challenges open

Blocking: `ch-coarse-zero-output`, `ch-zlip-small-width`,
`ch-hardness-computation-model`.

Not blocking, for the integrator to apply as wording at merge: state
`fact-discrete-gaussian-samples-generate` for $\mathbb Z^d$ only. State
`lem-agreement-detection` for $d\ge2$, with an independent uniform perpendicular
direction at a pole. Add to `prop-blind-lll-label-recovery` the tail-cutoff failure
in the displayed probability, the detection certificate (the recovered integer
vector satisfies the untruncated dependency exactly, which Gaussian records do not
allow almost surely), and DKRS23's parameter ranges and success probability $2/3$.
`ch-label-detection-certificate` is this last item.

## For the registers

New facts: `fact-discrete-gaussian-samples-generate`, Haviv and Regev, SODA 2014
(as sol gives the venue, the arXiv copy names none), Lemma 5.4, with Lemma 5.1. Note
`lib/literature/notes/soda/HR14.md`, PDF not placed. Accepted.

Corrections: `fact-lll-recovers-discrete-hidden-labels` as accepted in this round,
with the nonzero-label condition and rational proportionality. Sol adds that
ZSWB22's own Section 6.3 argument supports rational proportionality and that its
assertion about integer multiples overstates it.

Results accepted for `results.md`: `lem-agreement-detection` (proven, sample game
only) and `prop-blind-lll-label-recovery` (proven, exact-arithmetic model).

New search rows: none in this round.

Discussant calls: one sol call, exit 0.
