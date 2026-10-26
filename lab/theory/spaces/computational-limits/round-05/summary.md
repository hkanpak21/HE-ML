# Round 05, summary

Space `computational-limits`, 2026-10-25, the last round of milestone 2.
Discussant sol (gpt-6.1-sol): sol again, argon quota (argon is out of quota until
about 2026-10-27 13:30). Verdicts: ACCEPT 1, REVISE 1, REJECT 0. BLOCKING 1. The
space stops here: round 05 is the last round `milestone.json` allows.

The round resubmitted the two theorems of round 04. Sol closed all three blocking
challenges of round 04 and accepted `thm-coarse-reconstruction-lattice-hard` line
by line, reading the model $\mathsf M$ as a uniform stochastic algebraic RAM: unit-cost
$+,-,\times,\div$, square roots and comparisons, independent Gaussian draws, finitely
many program constants. It found one new blocking gap in `thm-zlip-reductions`
(`ch-zlip-model-realization`). A branch of an $\mathsf M$ program with a fixed step
bound computes a semialgebraic function of finitely many Gaussian draws, so it
outputs finitely many integers almost surely and cannot sample the infinitely
supported discrete Gaussian exactly. The exact sampler of DvW22 Lemma 2.9, used in
part (a), therefore does not run in deterministic polynomial time in $\mathsf M$. The
mathematics of both reductions stands, by sol's account. Only the time bound of the
model does not.

Proposed repair, for the integrator to judge (not reviewed by a discussant). Count
time in expectation, and add to $\mathsf M$ one primitive that returns a sample of
$D_{\mathbb Z,\sigma,c}$ for given $\sigma>0$ and $c\in\mathbb R$ at unit cost. DvW22 Lemma 2.9 builds
$D_{Q,s,c}$ from such one-dimensional samples along the Gram-Schmidt basis, so part
(a) runs in expected time $T+T_{\rm run}+\mathrm{poly}(d)$, and part (b) needs no sampler.
For the non-blocking `ch-zlip-variance-access`, block 2 of part (b) uses
$s^2/(2\pi)$ in place of $\sigma_s^2$. By the Poisson computation of BRST21 Lemma 7.2
the relative error is $e^{-\Omega(s^2)}$, which is inverse-polynomial for
$s\ge\eta_{1/2}(\mathbb Z^d)$ once the constant in $N_2$ is raised and part of the rounding
margin is reserved. With this repair the status of `thm-zlip-reductions` would be
proven in the extended model, and it would remain idealized: its exact-coordinate
guarantee has no finite-precision interpretation yet.

## Slugs accepted

- `thm-coarse-reconstruction-lattice-hard`

## Challenges open

Blocking: `ch-zlip-model-realization`, with the proposed repair above.

Not blocking: `ch-zlip-variance-access`, repair above. The heuristic qualification
of the $2^{0.146n}$ BKZ estimate is kept wherever it is quoted.

Closed: `ch-coarse-zero-output`, `ch-zlip-small-width`,
`ch-hardness-computation-model`.

## For the registers

Results accepted in milestone 2, for `results.md`:

| slug | kind | status | accepted in |
| --- | --- | --- | --- |
| `lem-agreement-detection` | lemma | proven, sample game only | round 04 |
| `prop-blind-lll-label-recovery` | proposition | proven, exact arithmetic | round 04 |
| `thm-coarse-reconstruction-lattice-hard` | theorem | proven in $\mathsf M$, conditional on hCLWE hardness in $\mathsf M$ | round 05 |
| `thm-zlip-reductions` | theorem | REVISE, one blocking gap (`ch-zlip-model-realization`) with a proposed repair | not accepted |

Borrowed facts accepted: `fact-lip-average-case`, `fact-zlip-best-algorithms`
(round 03), `fact-lll-recovers-discrete-hidden-labels`,
`fact-discrete-gaussian-samples-generate` (round 04).

Problem status changes proposed:

- `prob-coarse-reconstruction-lattice-hardness`: open to solved in $\mathsf M$, by
  `thm-coarse-reconstruction-lattice-hard`, conditional on hCLWE hardness in
  $\mathsf M$.
- `prob-blind-inversion-relu-clients`: stays open, restated in sol's quantitative
  form (round-03 summary).

New problems:

- `prob-finite-precision-blind-reconstruction` (supporting): do the lattice
  reductions of this space survive finite-precision representations, so that they
  bind Turing-machine attackers under the standard assumptions (BRST21 Corollary
  4.2 for hCLWE, DvW22 for ZLIP)? This needs a simulation of exact-real protocols
  and attackers. Posed by this space, 2026-10-25.
- `prob-zlip-reductions-width-gap` (side): the lower and upper ZLIP reductions lose
  a factor $\sqrt{d\ln(2d+4)/\pi}$ in the width. Can one width serve both, for
  polynomial widths?

New search rows: none in this round.

Discussant calls: one sol call, exit 0.
