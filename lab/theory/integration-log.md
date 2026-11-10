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

## 2026-10-30, the debate space and the booklet update

Written by the booklet editor, a Fable subagent, when Halil lifted the freeze. The
merge of milestone 2 used the re-derivations of the section above and added nothing to
them. The ten objects of `learning-attacker-prices` were re-derived here, object by
object, with every constant recomputed by quadrature or simulation in a scratch script
(`rederive_debate.py`, not kept in the repository).

Re-derived line by line, with the arithmetic recomputed:

- `thm-update-direction-chi-square-bound` (a) to (d). Step 1, the conditional structure
  of an update, and the symmetry of $\nu_a$. Step 2, Mehler's identity with
  $\sum_{k\ge1}\hat c_k(a)^2=\chi^2(\nu_a\|\gamma_1)$ and $\rho^k\le\rho^2$ for even $k$.
  Step 3, Fubini and $(1+\rho^2\kappa)^T\le e^{T\kappa\rho^2}$. Step 4, $\rho^2\sim\mathrm{Beta}(\frac12,\frac{d-1}2)$,
  $\mathbb E\rho^{2k}=(\frac12)_k/(\frac d2)_k\le(\frac12)_k(2/d)^k$ and the moment generating
  function $(1-2\lambda/d)^{-1/2}$. Step 5, $(1-x)^{-1/2}-1\le x$ on $[0,\frac12]$ by convexity
  with $\sqrt2-1<\frac12$. Step 6, Chebyshev with $\mathrm{Var}\le48(A^2+b\varsigma^2)^2/T'$,
  $192\cdot12=2304$ and the advantage $\frac23\cdot\frac{11}{12}-\frac1{12}=\frac{19}{36}>8^{-1/2}$.
  Step 7, the closed form of the two-point mixture against $\varphi_\sigma$, checked by
  quadrature to twelve digits at $(a,\varsigma^2)\in\{(0.5,1),(1,2),(1.5,4)\}$, the moments
  $\mathbb E[Z^4(Z^2-1)^2]=105-30+3=78$, $\mathrm{Var}(Z^4-Z^2)=78-4=74$, $c_2=2$ and
  $1+74/4=19.5$, and $\beta^2/2=2/(1+\varsigma^2)^2$.
- `def-optimum-update-stream` (i) to (iii). The covariance with $c_2uu^\top$, the conditional
  second moment $(W^2+\varsigma^2)I_d+W^2T(W)uu^\top$ from $\mathbb E[Z^2\mid W]=1+T(W)$, and the
  variance ratio $1+s$ with every cross term killed by the signs of $\xi$, $X_w$ and $\zeta$.
  The constants of the challenger's law $Q_\delta$: $p=0.68269$, $m_2=0.19875$, $m_4=0.11230$,
  $w_0^2=(m_2-m_4)/(p-m_2)=0.17863$, $T(w_0)=(1-m_2)/(1-p)-1=1.5251$, $\mu_2=0.2554$,
  $c_2=0.08645\,\delta$, all to the digits stated.
- `thm-norm-weighted-update-pca` (a) to (d). The $O(d-1)$ symmetry, the sub-gaussian norm
  $K\le c_0(A+\varsigma)\lambda_-^{-1/2}$, the constant $C_1=128C^2c_0^4/9$ with
  $\sqrt{18/128}=3/8$ so that $K^2\eta\le\frac38|\gamma_g|/\lambda_+\le\frac38$, the two-sided
  Rayleigh argument $\gamma_g(1-\langle\hat u,u\rangle^2)\le2\|E\|\le\frac34\gamma_g$, the moment
  $\mathbb E(r-W^2-\varsigma^2)^2\le6(A^2+\varsigma^2)^2/d$ from $(a+b+c)^2\le3(a^2+b^2+c^2)$, the
  fourth moments $8(3A^4+3\varsigma^4)\le24(A^2+\varsigma^2)^2$, and $\sqrt6\sqrt{96}=24$,
  $\sqrt6\sqrt{24}=12$. The spikes of (d) recomputed as $0.0801$ at $\delta=0$ and $0.0756$ at
  $\delta=0.02$, with the weight centred at $w_0^2+\varsigma^2$ in both cases, the atom
  contributing $0.0864$ and $0.0819$ and the continuous part $-0.0063$.
- `prop-update-direction-fano-recovery`. The cap $\sqrt2e^{-d\epsilon^2/4}$ from Markov on
  $e^{d\rho^2/4}$ and Step 4 above, $\mathrm{kl}(p'\|q')\ge p'\log(1/q')-\log2$, the golden
  formula, and the constant $\frac23\cdot\frac12\log2+\log2=\frac43\log2=0.924196$. The bound
  $K(a)$ from the convexity of KL in its first argument and the Gaussian formula.
- `prop-full-clipping-optimum-filter` (a) to (e). The sign times the unit gradient, the fair
  coin at a median with no atom, and $d-2\sqrt{d\cdot9d/64}=d/4$ in the Laurent and Massart
  lower tail.
- `prop-signed-weight-update-pca`. The split into $g_\pm$, the added errors, and
  $\eta\le\frac34$ from $|\gamma_g|\le2(A+\varsigma)^2$ and $\rho_++\rho_-\ge1$.
- `def-statistic-learner-class`. Remark (i), $k-N$ from the minimum-norm solution $SS^+$.
- `conj-linear-class-reads-cauchy-transform`, the exact part. The Schur identities
  $\lambda=\alpha+h^\top(\lambda-B)^{-1}h$ and overlap $1/(1+h^\top(\lambda-B)^{-2}h)$ from the
  eigenvector $(x,x(\lambda-B)^{-1}h)$, the derivative identity $\gamma/g^2+\Psi'(g)>0$ with
  $\sigma^2+W^2T(W)=W^2\mathbb E[Z^2\mid W]+\varsigma^2=\mathbb E[a^2\mid W]\ge0$, and the
  mean-square reduction (b1).
- `prop-measured-meets-proven-full-observer`. $\kappa_{\mathrm{KL}}$ on $Q_0$ at $\varsigma^2=0.1$
  from closed-form integrands: the likelihood ratio on the atom
  $q(x)=[\bar\Phi((1-cx)/\tau)+\bar\Phi((1+cx)/\tau)]/(1-p)$ with $c^2+\tau^2=1$, derived here
  from $Z\mid X'=x\sim N(cx,\tau^2)$, gives $0.248296$ on the atom and the two-point mixtures
  give $0.081324$ off it, in total $0.160111$. The budgets $(d/24-\frac43\log2)/0.1602$ are
  $46.25$ and $98.27$, the ratios $86.5$ and $81.4$, and the one-sided Clopper and Pearson end
  $0.05^{1/40}=0.9278$. The weighted estimator at $d=200$, $T=20d$, four seeds, reached
  overlaps $0.705$ to $0.729$, plain PCA at most $0.105$ (empirical).
- `thm-release-relearning-price-bracket` (a) to (e). Jensen on $S\mapsto\mathrm{tr}(S^{-1})$,
  the scaling attack, the decomposition by conditional unbiasedness,
  $S_X=\tau^2(A+I/\tau^2)^{-1}A$ and $S_X^{-1}=I/\tau^2+s^2(X^\top X)^{-1}/\tau^4$, the Gaussian
  posterior under adaptive queries, AM and HM with Jensen for $y\mapsto d^2/y$, the solve for
  $N$, least squares $s_r^2\iota_N$, and $d/\iota_n=n-d-1$. The inverse-Wishart moment by the
  challenger's Schur argument, $(W^{-1})_{11}=1/\|(I-P)g_1\|^2$ with a $\chi^2_{m-d+1}$
  denominator and $\mathbb E[1/\chi^2_k]=1/(k-2)$, checked by Monte Carlo at
  $(d,m)\in\{(10,15),(10,40),(30,80)\}$ (2.511, 0.345, 0.613 against 2.5, 0.345, 0.612). The
  simulation at $d=10$, $n=60$, $N=200$, $\tau=s=s_r=1$: $R_n=0.1993$, least-squares excess
  $0.0524$ against the bound $0.0497$ and the exact $s_r^2\iota_N=0.0529$.

Taken on trust, as the space and its critics state them, not re-derived here:

- the two deterministic equivalents of `conj-linear-class-reads-cauchy-transform` and the
  outlier equation's agreement with simulation within 0.02 on the band law, and the band
  law's own constants;
- the 40 of 40 certified runs at $d=200$ and $d=400$ and the challenger's replication, of
  which only four seeds at $d=200$ were rerun here;
- the overlap figures of the space's simulations at $d=400$ and on the zero-spike family;
- the identification of the stream with the single-index model of DPLB24 and the readings of
  DPLB24 Theorems 3.2, 4.1 and 6.1, Proposition 2.6 and Lemma 3.1, as fable states them
  from the library note, not re-read here;
- every attribution fable and sol make from memory (Lu and Li 2020, Mondelli and Montanari
  2019, Luo, Alghamdi and Lu 2019, Barbier et al. 2019, Duchi and Wainwright 2013, Laurent and
  Massart 2000, the A-optimal design bound), recorded in the booklet as unverified with the
  search pending;
- the simulations of the critics on the release theorem (fable's 0.0534 and 0.0527, sol's
  0.0529 and 0.0526).

Statuses chosen at merge. The ten debate objects enter as accepted, except
`conj-linear-class-reads-cauchy-transform`, open. The seventeen objects of
`hard-problem-mappings` and `statistical-limits` enter as accepted, with two exceptions
among the withdrawn conjectures, which the integration check requires as objects since
their withdrawals carry ACCEPT verdicts: `conj-backdoor-detection-is-ngca` enters as
refuted, since parts (b) and (c) are false as stated, and
`conj-extraction-priced-by-generative-exponent` enters as accepted, since no part is false
and its known-link content is `thm-extraction-exponent-price`. The booklet has no status for
a withdrawn object. The four results of `computational-limits` rounds 03 to 06 enter as
sketch, `thm-zlip-reductions` on its open challenge and the three others because no round of
the space after their ACCEPT ends with BLOCKING 0, as the strict status of the section above
records. sol's six repairs of the critique are recorded in the sources and not applied.

The rule in `verify.mjs`. `eligible()` required the space's current last round to end with
BLOCKING 0 for every ACCEPT given in a round with BLOCKING above 0, which stripped the five
first-milestone objects of `computational-limits` of their status when round 06 ended at
BLOCKING 1 on `thm-zlip-reductions`. The function now counts an ACCEPT when its round or any
later round of the space ends with BLOCKING 0, which is the status rule of `CONTEXT.md` read
at the moment the status is set, since a round at BLOCKING 0 closes every challenge then
open and a later challenge on the object itself comes with a later verdict on it. It also
reads the verdicts of a debate space from `challenger.md`. Tested on a scratch copy with
three fake debate spaces: a space whose only round ends at BLOCKING 2 yields no accepted
object, a space at BLOCKING 0 yields its ACCEPT and not its REVISE, and a space that
reopens at BLOCKING 1 keeps the object accepted before and not the one accepted in the
reopened round.

Build. The preamble gained `\newcounter{none}` and the `calc` package, which pandoc's
own template defines for the unnumbered longtable that the table of
`def-hard-problem-mapping` becomes. The folder check fails on five `.out` files written
by the discussants of `council/2026-10-30-statement-refinement/`, which the editor may not
touch.
