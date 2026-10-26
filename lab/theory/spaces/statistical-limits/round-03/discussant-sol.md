---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-25
prompt: lab/theory/spaces/statistical-limits/round-03/prompt-sol.md
---

Proven. The coupling, cap bound, whitening calculations, ReLU identification, and Train attack contain valid results. The round nevertheless has seven blocking challenges. The main failures concern the admissible view, the zero-reference boundary, and the identification of prediction with direction recovery.

Heuristic. Aims 1 and 3 are well chosen. Aim 2 needs separate statements for prediction, direction recovery, and reconstruction. Its present comparison joins incompatible hypotheses.

### `fact-subgaussian-sample-covariance-concentration`

Proven. ACCEPT. The statement matches Bruna, Regev, Song and Tang, STOC 2021, Lemma 7.4. Its hypotheses include independent, mean-zero, isotropic rows and a uniform bound on their sub-Gaussian norms. Identical distribution is unnecessary.

Proven. For the standard Gaussian rows used later, the norm parameter is an absolute constant. Taking the tail parameter to be 2.4 gives failure probability below 0.01. A sufficiently large absolute multiple of the dimension therefore suffices for the stated covariance event.

Heuristic. This is a useful borrowed tool. It needs no separate novelty claim.

### `fact-single-index-information-theoretic-rate`

Proven. The statistical upper bound matches Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, Theorem 6.1. Choose a degree with a nonzero coefficient. The hidden constants depend on that degree. Calling the sample requirement order d also fixes the signal coefficient and target accuracy independently of the dimension.

Proven. The theorem gives an upper bound. The notation describing its sufficient sample size does not itself prove a matching minimax lower bound.

Proven. `ch-single-index-resource-classes`, blocking. The sentence “The efficient rate is” asserts more than the cited results establish. Theorem 3.2 concerns SQ access. The low-degree conclusion requires its stated conjecture. Theorem 4.1 supplies a sample-based algorithm. Section 7 explicitly notes that its power iterations are not bona fide SQ operations. These results cannot become one unconditional price for efficient algorithms.

Proven. `ch-single-index-proof-attribution`, nonblocking. Reference DH21 is Dudeja and Hsu, rather than Damian and others. Moreover, Appendix H gives a truncated correlation construction and invokes DH21, Lemma 25. The main text’s description involving Theorem 5 should not replace an account of the proof actually supplied.

Heuristic. Keep this object as a statistical upper bound, with the algorithmic regimes stated separately.

### `thm-blind-orbit-limit`

Proven. ACCEPT. Part (a) follows from the accepted coupling for trained clients and adaptive servers. The coupling keeps the side data fixed. Item 5 then permits the simultaneous transformation of records and regeneration of those side data. Initialization independence and invariance supply the required equality of joint laws.

Proven. The group is compact because it is a closed subgroup of the orthogonal group. Haar probability therefore exists. Part (b) correctly averages the success event over an independent group element. Dropping all constraints except the first gives the stated bound. Randomized servers satisfy the same conclusion after including their independent coins.

Proven. Part (c) is correct. Optimizing the centre’s radius gives the stated cap threshold. Both Gaussian norm failures have exponent ln 2 minus three eighths. This exceeds 0.318. On the retained radius event, the squared cap threshold is at least one half. The displayed bound with exponent 0.31 follows.

Proven. Part (d)’s Gram-matrix characterization is correct for the diagonal orthogonal action. It describes the maximal invariant. It does not assert that every admissible protocol reveals that invariant.

Proven. The full orthogonal conclusion requires the side data to preserve the full orthogonal group. Direction-dependent labels generally leave a smaller group. Gaussian records and Gaussian initialization alone do not remove that restriction.

Heuristic. This is the round’s cleanest structural result. It applies to trained clients without claiming that their surviving invariant information is recoverable.

### `prop-whitening-orbit-sample-price`

Proven. The exact identity in (i) holds. The polar decomposition, pseudoinverse square root, and orthogonality of the two resulting factors are correct.

Proven. `ch-affine-shape-output`, blocking. The following sentence is false as written.

> “The server’s output is therefore a function of the affine shape of the record tuple alone, whatever W and b are.”

The output’s orthogonal equivalence class has that property. Its coordinates retain the orthogonal factor depending on the client. In dimension one, clients with weights 1 and minus 1 produce opposite whitened outputs under a fixed basis rule. Their record tuples have the same affine shape.

Proven. Part (ii) holds. In fact, its first inequality is equality. After removing the client’s orthogonal factor, the cross-moment between the whitened and original centred records is the positive definite square root of their sample covariance. Orthogonal Procrustes therefore selects the identity.

Proven. The Frobenius calculation in (iii) is correct. With the builder’s normalization, the covariance error has expectation
\[
\frac{(N-1)d^2}{N^2}+\frac dN.
\]
The empirical mean contributes another d divided by N. The stated upper bound and sufficient sample size follow.

Heuristic. The refinement with leading term d squared divided by four N also needs a large-d regime. For fixed dimension, the mean error and the linear-in-d covariance contribution remain leading-order terms in inverse N.

Heuristic. Keep the proposition after correcting the output claim. Its finite-sample loss and client-independent guarantee earn their place.

### `prop-relu-client-second-moment-identifies-weights`

Proven. ACCEPT. The polar-coordinate integral, radial integral, angular integral, diagonal identity, and identification argument are correct. Recovering the row norms and angles determines the weight Gram matrix. Full column rank then gives uniqueness up to right multiplication by an orthogonal matrix.

Proven. `ch-relu-kernel-derivative`, nonblocking. The displayed derivative omits division by twice pi. Its sign and the strict monotonicity conclusion remain correct.

Proven. The identity is the first-order arc-cosine kernel, with the builder’s normalization equal to half the normalization of Cho and Saul, NeurIPS 2009, equations (1), (3), and (6). This identity is prior work. [Kernel Methods for Deep Learning](https://proceedings.neurips.cc/paper/2009/file/5751ec3e9a4feab575962e78e006250d-Paper.pdf)

Proven. Part (iii) holds for the stated finite collection of records independent of the weights. For each nonzero fixed record, the number of positive coordinates is binomial. Enough positive coordinates and general position give a unique linear solution. Orthogonal reparameterization preserves that solution set. A union bound gives the claimed recordwise probability.

Proven. Lei, Jalal, Dhillon and Dimakis, NeurIPS 2019, Theorem 3 supports this pointwise application. Their Lemma 1 uses global injectivity language, but its binomial proof fixes the input. The builder correctly needs only the pointwise event followed by a finite union bound.

Open. `ch-relu-population-price`, nonblocking. Population identification does not supply a finite-sample inversion price. That requires a perturbation bound for moment estimation, Gram-matrix factorization, and the positive-coordinate solve.

Proven. Isotropy alone also supplies no approximate Gaussian kernel identity for arbitrary non-Gaussian laws. The other-regime paragraph needs an approximation hypothesis.

Heuristic. The identification result is sufficiently simple to retain while its sample price remains open. The population qualification must remain explicit.

### `conj-blind-orbit-price-lower-bound`

Proven. `ch-orbit-price-side-data`, blocking. Both proposed lower bounds fail for the full accepted game, which permits invariant side data. Squared record norms are admissible under the full orthogonal group.

Proven. Here is a finite-sample counterexample. First take a square invertible affine client. The squared record norm is an unknown quadratic polynomial of the representation. Enough representations in general position, together with their squared record norms, determine that polynomial exactly. Its quadratic and linear coefficients determine the inverse metric and translation. Factoring the metric reconstructs every record up to one common rotation.

Proven. Gaussian records give the required general position almost surely once the number of records reaches the number of quadratic polynomial coefficients. For a rectangular full-column-rank client, first express the representations in coordinates on their observed affine span. The same argument applies. It therefore also defeats the Gaussian-weight form.

Open. With a representation-only view, both rate conjectures remain plausible targets. Neither offered argument proves them.

Proven. The minimax reduction must identify an observable covariance, or an equivalent metric in observable coordinates. The latent matrix formed from the weights is coordinate dependent. An ordinary covariance-estimation lower bound does not automatically transfer to reconstruction of the same observed records under Procrustes loss.

Heuristic. The Gaussian-weight argument also needs more than posterior operator-norm spread. It must connect the actual quotient observation and posterior uncertainty to expected Procrustes loss.

Proven. The loss should be defined for arbitrary server outputs. Its present definition names the particular empirical-whitening outputs of the preceding proposition.

Heuristic. Retain a representation-only minimax conjecture as the primary lower-bound target. Treat the Gaussian-weight form as a separate Bayes problem. Beating whitening by a constant factor would not refute either rate.

### `thm-train-access-price-frontier`

Proven. The simulation in (a) works under the stated fresh hardware randomness model. At each adaptive call, two unused reference samples generate an independent covariance-noise residual. Adding the chosen dataset’s known mean reproduces the answer’s conditional law. Induction transfers the entire transcript, including calls made after seeing the challenge.

Proven. Part (b)’s simulation also works. Identity-covariance noise can be generated locally without reference samples. HSU25 Theorem 4.1 then applies within its stated domain.

Proven. Part (c) holds. The whitening transformation and independence of the estimated inverse covariance are correct. The OUT second moment is correct. In the IN calculation, all six cross-covariances vanish. The four listed variances are correct. The covariance event, eigenvalue bounds, bound on the aggregate variance, and both Chebyshev calculations justify the constants 2100, 0.05, and 0.49.

Proven. `ch-train-zero-reference`, blocking. Part (d) is false if zero reference samples are admissible. Its omission of the lower bound’s sample-domain conditions matters.

Proven. Fix rho to one half and take n at least four. Form the covariance estimate from N independent Train residuals, with N at least twice d plus six. Let
\[
q=(\hat\mu-X)^\top\hat S^{-1}(\hat\mu-X),\qquad
U=\frac{N-d-1}{Nd}\,q.
\]
Under IN and OUT, respectively, the difference between release and target has covariance equal to the population covariance multiplied by
\[
v_{\rm IN}=\frac54-\frac1n,\qquad
v_{\rm OUT}=\frac54+\frac1n.
\]
Its mean is zero under both hypotheses, whatever the population mean.

Proven. The Gaussian and inverse-Wishart calculation gives
\[
\mathbb E[U]=v,\qquad
\operatorname{Var}(U)=
\frac{2v^2(N-1)}{d(N-d-3)}.
\]
Accept IN when U is below five quarters. Chebyshev bounds each error by at most nine n squared divided by d. At the theorem’s dimension, this is at most 36 divided by kappa. The attack therefore meets the criterion with zero reference samples and order d Train calls.

Proven. This does not contradict HSU25 Theorem 4.1. That theorem assumes at least two reference samples. It refutes the strictly positive reference-sample price claimed in (d).

Proven. The growing-price regime used in the next theorem survives. When rho decreases as the stated power of n, the proposed reference price diverges. Padding a smaller sample bank to two samples then permits the known-covariance lower bound to establish the asymptotic rate.

Proven. `ch-hsu-proof-margin`, nonblocking. The cited proof needs a strict testing margin. Total variation at most 0.02 alone does not exclude advantage exactly 0.02. Section 3.2.4 also contains an arithmetic error. Its condition with factor 400 bounds the displayed square-root term by 0.1, rather than 0.01. Tightening the existential constants repairs these issues. They should not be repeated as verified constants.

Proven. `ch-hsu-frontier-domain`, nonblocking. Propagate the strict dimension inequality from (a), and the n and m restrictions from (b), into (d). The proof currently applies them outside their stated domains.

Open. `ch-hsu-input-covariance-transfer`, nonblocking. The final paragraph’s claim about input-estimated covariance does not follow. Changing the attacked mechanism changes the release law. The absence of population information in chosen-data Train calls does not establish HSU25’s lower bound for that new mechanism.

Heuristic. Keep (a) through (c). State the reference frontier in a diverging-price regime, or use an effective sample count that includes one. These qualifications leave a useful operational extension of HSU25.

### `thm-same-units-gap-gaussian-mechanism`

Proven. ACCEPT under the declared oracle accounting. The combined-budget lower bound follows from the valid simulation in the preceding theorem. Its upper bound follows from the Train attack. The ratio calculation and the exponents in the specified decreasing-noise regime are correct. The zero-reference counterexample does not invalidate this combined-budget result.

Proven. The separation in reference samples already appears in Haghifam, Smith and Ullman, HSU25, Theorems 3.1 and 3.3, with their comparison in Remark 3.4. The contribution here is the Train-access extension and its combined-budget interpretation.

Heuristic. `ch-gaussian-comparison-meter`, nonblocking. The comparison is fair as a declared scalar cost assigning one unit to a sample and one unit to a Train call. It does not establish a machine-work ratio. The trainer’s population-covariance calibration is supplied without charge. That resource asymmetry must remain visible.

Proven. The stated estimation error is Mahalanobis risk. For general population covariance, it is not the Euclidean mean-square error.

Heuristic. This is a useful corollary and benchmark. It does not provide a new separation between learning problems of matched accuracy.

### `prop-label-relevant-attacker-at-most-trainer`

Proven. REJECT in its present form.

Proven. `ch-label-first-coefficient`, blocking. Generative exponent at least three forces the first conditional Hermite coefficient to vanish. Consequently the first Hermite coefficient of the conditional mean also vanishes. DPLB24 Definition 2.4 and the identity immediately following it establish this directly.

Proven. The accepted conditional-mean theorem requires that coefficient to be nonzero. Part (a)’s risk premise is therefore impossible, and its divisions by that coefficient are undefined. The same obstruction invalidates the direction vector used in (b).

Proven. `ch-label-prediction-not-direction`, blocking. Learning the square-loss predictor need not recover the direction. This issue was already recorded in computational-limits round 01 under `ch-learning-is-not-direction-recovery`.

Proven. The obstruction also exists inside the present exponent regime. Choose a symmetric Gaussian event whose conditional second moment equals one, but whose fourth Hermite moment is nonzero. Such an event can combine a central interval with two tails. Let the label be its indicator multiplied by an independent random sign. The generative exponent is four, while the conditional mean is identically zero. The trainer’s optimal square-loss predictor requires no direction recovery.

Proven. Thus part (c)’s direction-recovery price cannot become the trainer’s prediction price under the stated hypotheses. DPLB24 Remark 2.5 describes the underlying distinction between generative information and a constant conditional mean.

Proven. `ch-label-evaluation-domain`, blocking. Even in a repaired nonzero-coefficient regime, part (a) drops material hypotheses and changes the guarantee. The accepted theorem requires a bounded head and representations independent of that head. Its clean mean-square bound concerns an independent target. For the observed training records, it includes the empirical second-moment operator norm. Those qualifications cannot be omitted.

Proven. Part (b) also confuses coordinate error with vector error. Coordinate tolerance of order inverse square root d yields a vector error of constant order. The normalization estimate needs the vector error. A suitable constant-accuracy extraction could suffice, but the displayed proof does not supply its claimed error.

Proven. Part (c)’s whitening reduction is valid at population level. Its statistical upper bound duplicates DPLB24 Theorem 6.1 after rotation. Its algorithmic comparison inherits `ch-single-index-resource-classes`. The accepted SQ proposition itself explicitly distinguishes its SQ lower bound from its sample-based upper bound.

Heuristic. A fair replacement would compare direction recovery with direction recovery under one interface. The nonzero-first-coefficient conditional-mean result can remain a separate statement about what a supplied predictor reveals. The present proposition does not refute a general attacker-versus-trainer separation.

## Verdicts

```text
VERDICT fact-subgaussian-sample-covariance-concentration ACCEPT
VERDICT fact-single-index-information-theoretic-rate REVISE
VERDICT thm-blind-orbit-limit ACCEPT
VERDICT prop-whitening-orbit-sample-price REVISE
VERDICT prop-relu-client-second-moment-identifies-weights ACCEPT
VERDICT conj-blind-orbit-price-lower-bound REVISE
VERDICT thm-train-access-price-frontier REVISE
VERDICT thm-same-units-gap-gaussian-mechanism ACCEPT
VERDICT prop-label-relevant-attacker-at-most-trainer REJECT
BLOCKING 7
```