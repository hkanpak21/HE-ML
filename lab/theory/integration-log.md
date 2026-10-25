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
