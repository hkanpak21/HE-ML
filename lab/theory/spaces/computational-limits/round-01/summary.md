# Round 01, summary

Space `computational-limits`, 2026-10-25. Discussant astra (gpt-6-astra), as a
fallback. The README order puts argon in this round. Argon's first call failed
on a workspace permission error in `discuss.sh` (since fixed by the integrator),
its second timed out at 40 minutes and its third at 60 minutes, both with no
output. The integrator's rule for two argon failures on one round allowed
waiting for astra's quota (out until 21:27), and the round fell back to astra at
21:31. Verdicts: ACCEPT 13, REVISE 6, REJECT 1. BLOCKING 10.

The round answered all twenty challenges of round 00 and proved five new
objects. Astra accepted the revised game, the transcript coupling
(`lem-equivariant-view-coupling`, credited to the induction of Li, Zhang and
Arora's Theorem C.1), the whitening lemma, the conditional-mean reconstruction
theorem, the withdrawal of the training-cost aim, and eight of the ten revised
facts. It found one error of sign that runs through three objects: the
covariance of the pancake law has a deficit, not an excess, along the hidden
direction, since BRST21 Lemma 7.2's Poisson-summation identity subtracts the dual
sum (`ch-pancake-covariance-sign`, which I checked against the identity: astra is
right). The deficit is at most of order $\gamma^2e^{-\pi\gamma^2}$, so the repairs
are local. The other blocking challenges are a dropped confidence parameter in
CGJMMT21 Theorem 1, the range and margins of the SQ price
(`ch-sq-price-range`), a witness that must be of fixed positive degree and
strength (`ch-witness-uniformity`), three gaps in the randomized use of DPLB24
Theorem 3.2 (an unjustified diagonal correlation bound, a dropped square root in
the code overlap, and the auxiliary budget for growing query exponents), the
schedule of the seed-known inversion for trained clients
(`ch-initial-observation-schedule`), and two defects of the conjecture: the
protocol class admits clients that erase the record
(`ch-conjecture-erasing-client`), and the settled upper inclusion needs the
hidden law to be isotropic (`ch-conjecture-whitening-scope`). Astra also judged
the seed separation an artificial-distribution reduction: the Gaussian layer is
no plug-in, but the hardness is imported through a cryptographically designed
record law, which is a question for Halil. Round 02 repairs every blocking
challenge.

## Slugs accepted

- `fact-sq-simulates-minibatch-sgd`
- `fact-hclwe-sq-correlation-bound`
- `fact-ngca-sq-lower-bound`
- `fact-generative-exponent-sq-recovery-bound`
- `fact-ica-breaks-rotation-perturbation`
- `fact-instance-encoding-privacy-learnability`
- `fact-nrnt25-private-layer-hardness-route`
- `fact-orthogonal-equivariance-of-training`
- `def-seed-blind-reconstruction-game`
- `lem-equivariant-view-coupling`
- `lem-whitening-gives-rotated-records`
- `thm-reconstruction-from-conditional-mean`
- `conj-reconstruction-at-training-cost`, accepted as withdrawn

## Challenges open

Blocking: `ch-pancake-covariance-sign`, `ch-keyed-encoding-confidence`,
`ch-sq-price-range`, `ch-witness-uniformity`, `ch-label-sq-self-correlation`,
`ch-label-sq-code-overlap`, `ch-label-sq-auxiliary-budget`,
`ch-initial-observation-schedule`, `ch-conjecture-erasing-client`,
`ch-conjecture-whitening-scope`.

Not blocking: `ch-conditional-mean-interpretation`, and the remarks on the game
(the population game evaluates a reconstruction function, finite
representations for experiments), on LeakyReLU (known nonzero slope), on the
simulation cost and finite precision of the lattice corollary, and on the label
denoiser of DPLB24 Theorem 4.1.

Rejected: `conj-seed-price-is-ngca-price` as stated, to be restated in round 02
with a recoverability condition and an isotropic hidden law.

## For the registers

New facts, each read in the paper this session.

- `fact-orthogonal-equivariance-of-training`: Li, Zhang and Arora, arXiv
  2010.08515 (ICLR 2021 as astra gives it, the arXiv page names no venue),
  Definition 3.2, Theorem C.1, Remark C.1, Corollary C.2, Remark C.2, Table 1,
  Theorem 5.2. Accepted by astra. Note `lib/literature/notes/iclr/LZA21.md`, PDF
  not placed.
- Correction to the round-00 reading of `fact-clwe-hardness`: by BRST21 Lemma 7.2
  and Corollary 7.3 the covariance of $H_{w,\beta,\gamma}$ is $I/(2\pi)$ on
  $w^\perp$ and at most $1/(2\pi)$ along $w$, with a deficit of order
  $\gamma^2e^{-\pi\gamma^2}$. Round 01 stated an excess. Round 02 carries the fix.
- Pointers added: BRST21 Lemma 7.4 (Vershynin Theorem 4.6.1), DPLB24 Appendix B
  (Lemma B.6 is FGRVX17 Corollary 3.12, Corollary B.7), and the proof of DPLB24
  Theorem 3.2 (Lemma E.3 gives a spherical code of overlap
  $\sqrt{C\log_d(m)^2/d}$, and the proof takes the diagonal correlation bound
  equal to one without stating why, per astra).

Results proposed for `results.md`, as accepted in this round:
`def-seed-blind-reconstruction-game`, `lem-equivariant-view-coupling`,
`lem-whitening-gives-rotated-records`, `thm-reconstruction-from-conditional-mean`.
Withdrawn: `conj-reconstruction-at-training-cost`. Pending round 02:
`prop-sq-blind-reconstruction-bound`, `prop-fine-reconstruction-to-hclwe`,
`thm-blind-split-seed-separation`, `prop-sq-label-relevant-reconstruction-bound`,
`conj-seed-price-is-ngca-price`.

Problem status changes proposed.

- `prob-split-transcript-leaks-seed`: open to solved for the protocol class
  $\mathcal P_H$ of `def-seed-blind-reconstruction-game`: the whole server view is
  a function of rotated records and fresh coins (`lem-equivariant-view-coupling`,
  accepted). Outside the class (Adam, published weights, known records) it stays
  open.
- `prob-attacker-lower-bound-from-hard-learning`: open, with the proof note
  refuted (round 00). Round 02 decides whether the pancake reductions make it
  partial.

New search rows: none in this round. The read of arXiv 2010.08515 is the row
`search-orthogonal-equivariance-training` in the round-00 summary.

Discussant calls of this round, for the integrator's budget: four rows in
`discussants.csv` for round 01, three failed argon calls (one permission error,
two timeouts) and one astra call.
