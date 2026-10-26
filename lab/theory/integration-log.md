# Integration log

The integrator's record of what it re-derived before merging an object with status
accepted, and what it took on trust. One section per milestone, appended.

## 2026-10-25, first rounds

Re-derived line by line, with the arithmetic recomputed:

- oracle-and-measurement, round 02. `thm-exact-twin-price` (a) to (c): the finite
  partition construction, the averaging over $B$, the limit $M\to\infty$, Jensen, the
  monotonicity of $q\ln(q/\alpha)$, the Clopper and Pearson upper bound, the shift
  constructions for the total variation and the one-sided divergence, the every-record
  family without a union bound, astra's four-call certifier ($e^{-4}<0.0184$,
  $0.99^{368}<0.0248$, $298.07$), and the numbers 686.5 and $4.12\times10^7$.
  `thm-coupling-free-soundness` (a) to (d) against the proof of
  `thm-dataflow-composition` (b) in the final learning-oracle document: only the
  coordinates driving the two chains change, and independence from the release noise is
  what lets the step-4 kernel reproduce the hybrid. Counterexample values 0.4795,
  0.9876, 0.474 and 0.276. `prop-profile-run-coordinate` (a) to (c) and the variance
  remark. `def-seed-access-modes` remarks. `prop-drawn-mode-is-fs-oracle` (a) against
  `def:passive` and `def:cost` of FS `oracle.tex`, and (b) against the operation table
  and access classes of FS `exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex`.
  Part (b) needs the starting model fixed as in part (a), since the report's train
  always starts from the training procedure's own initialization.
- computational-limits, rounds 00 to 02. The counterexample to the proof note (trie
  of prefixes, Hoeffding with $B=\lceil32n^2\ln n\rceil$, the union bounds $4/n$ and
  $n^{2k}2^{-(k^2-k)/2}$). `lem-sq-learner-post-processing`. `lem-equivariant-view-coupling`
  and its corollary. `lem-whitening-gives-rotated-records`.
  `thm-reconstruction-from-conditional-mean`. The covariance deficit of
  `fact-clwe-hardness` from the Fourier transform $(1/(2\pi)-y^2)\rho(y)$. The
  arithmetic of `prop-sq-blind-reconstruction-bound` (a): the packing size, the Gram
  count $4/\rho_0^2$, the constant $11/288$, the truncation level and $\tau_1$. Step 2
  and the cosine test of `prop-fine-reconstruction-to-hclwe`. The search reduction and
  the choice of $m$ in `prop-sq-label-relevant-reconstruction-bound` (a). The witness
  test of `prop-sq-blind-reconstruction-bound` (b), through the Mehler identity
  $E_g[h_j(\rho a+\sqrt{1-\rho^2}g)]=\rho^jh_j(a)$.
- statistical-limits, rounds 01 and 02. `thm-shadow-run-price-finite-views` (a) to (f):
  the plug-in bound, the paired family, the KL $\frac{2\delta}{k'}\ln\frac{1+\delta}{1-\delta}\le\frac{16\delta^2}{3k'}$,
  Pinsker, the averaging and both choices of $\delta$. `lem-scrambled-seed-urn`: the
  conditional label law, $\mathrm{TV}(q_h,p)\le(t-1)/(M-t+1)$, the path-wise hybrid sum
  and the KL chain rule. `prop-reconstruction-label-sandwich`: floor, ceiling through
  the reference law $Q$, the two weaker forms and the Gaussian entropy bound.
  `def-uniform-security-profile` properties.

Taken on trust, as the spaces read them, not re-read by the integrator:

- the statements of BRST21 Corollary 4.2, Lemma 7.4 and Proposition 8.3, FGRVX17
  Theorem 3.2, Lemma 3.10 and Theorems 2.9, 2.10 and 5.4, DKRS23 Theorem 1.5, DPLB24
  Theorems 3.2 and 4.1 and Lemmas 2.3 and E.3 (including $\lambda_k^2\le1$ under its
  normalization, which follows by conditional Jensen), LJDD19 Theorem 3, AKMSS21
  Theorem 1c, LZA21 Theorem C.1;
- every borrowed fact, whose reading the spaces recorded in their notes.

Wording corrections applied at merge, from `computational-limits/round-02/builder.md`:
`def-seed-blind-reconstruction-game` (observed records against the SQ map) and
`thm-reconstruction-from-conditional-mean` (the floor in Halil's example).

Register items of the nine summaries, moved or declined:

- Moved into `sink/formalizing/`: 20 new facts, corrections to 19 existing facts,
  20 results, the refutation of `thm-sq-hardness-black-box-attacks` with the BB20
  pointer, 6 search rows, 5 new problems, 4 status changes and 6 history lines on
  problems. Papers to place are listed in its `STATE.md`.
- Declined, with reason. The prior-work pointers that astra named and no space
  opened (Dong, Roth and Su in JRSS B 2022, Kaufmann, Cappé and Garivier in JMLR
  2016, and Gilbert and McMillan in 2018) are not facts, since a fact
  enters only from a source someone opened. They stay in the round files. The
  computational space's remark that an unbounded blind server learns Gaussian
  records only up to a common rotation is a statement for the space
  `statistical-limits`, unproven there, so it enters no register.

## 2026-10-26, milestone 2 (mappings to known hard problems)

Re-derived line by line, with the arithmetic recomputed:

- statistical-limits, rounds 03 to 05. `thm-blind-orbit-limit` (a) to (d), the
  spherical cap and the Chernoff constant $e^{-0.318d}$. `prop-whitening-orbit-sample-price`,
  the polar decomposition and the Wishart moment $\frac{(N-1)d^2}{N^2}+\frac dN$.
  `thm-blind-orbit-price` steps 1 to 7: the $\sqrt2$-Lipschitz matrix absolute value, the
  reduction to $\hat R$, the prior, $I(R;Y)\le D/4$, the small-ball bound $2e^{-D}$ and
  Fano with $0.32+2e^{-4}<\frac12$. `prop-relu-client-second-moment-identifies-weights`,
  the arc-cosine integral and $\kappa'$. `thm-train-access-price-frontier` (a) to (d), the
  simulation by pairs of samples and both Chebyshev bounds (0.05 and 0.49).
  `thm-same-units-gap-gaussian-mechanism`.
- hard-problem-mappings, rounds 00 to 02. `lem-level-set-moment-balance`, the branch
  weights and $E[Z^4\mid t]=1+AB$. `thm-extraction-exponent-price` (a) steps 1 to 5,
  (b) with the sign selection, (c) and (d), including the symmetry of $P_\natural$.
  `prop-learner-side-sq-transfer` (a) and (b) with the corrected constant.
  `lem-sparse-pca-backdoor-width-price` (a) to (d), the Laurent and Massart tails and
  $\sqrt{3.42/(2\pi)}\approx0.738$. `prop-weight-testing-equals-white-box-detection`.
- computational-limits, rounds 03 to 06. `lem-agreement-detection`,
  `thm-coarse-reconstruction-lattice-hard` with $\rho\ge c_0/3$ and the constant
  $c_0^4/648$, and `prop-blind-lll-label-recovery`.

Taken on trust, as the spaces read them: HSU25 Theorems 3.1, 3.3 and 4.1 (with sol's
margin note), DPLB24 Theorems 4.1 and 5.2 and Lemma E.3, FGRVX17 Theorems 3.7 and 3.13,
ZSWB22 Theorem 3.3, DKRS23 Theorem 1.5, BRST21 Corollary 4.2, the facts of DvW22,
Duc24 and HR14, the reductions of `thm-zlip-reductions` (merged as a sketch), and
`prop-gram-sufficiency-rotation-invariant` and `lem-feature-matrix-transpose`, which the
simplified merge keeps out of the booklet.

Strict status. The space computational-limits ended at BLOCKING 1, on
`thm-zlip-reductions` only. Its three other objects have ACCEPT verdicts, and none uses
`thm-zlip-reductions`, but by the rule of `CONTEXT.md` they count as accepted only once
the space converges or Halil leaves the ZLIP sketch out of the milestone.

Register items, moved or declined. Moved: 7 new facts, corrections to 7 facts, 22
results (18 accepted, one sketch, one refuted, two retracted), 8 search rows, 5 new
problems, 3 status changes from open to partial, and history lines on 8 problems. The
lint went from 613 to 647 entries and from 72 to 80 searches. Declined:
the DK22 and WDS19 corrections, which have no register entry and live in their notes,
and the withdrawn round-03 aims of computational-limits, recorded as superseded in the
history lines of the results that replaced them.
