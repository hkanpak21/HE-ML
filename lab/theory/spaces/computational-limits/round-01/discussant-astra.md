---
model: gpt-6-astra
discussant: astra
date: 2026-10-25
prompt: lab/theory/spaces/computational-limits/round-01/prompt-astra.md
---

Proven. Round 01 does not close all twelve blocking challenges. The transcript coupling and conditional-mean argument survive. The whitening lemma survives under its stated isotropy assumption. The two pancake reductions need corrections, and the randomized DPLB24 argument remains incomplete.

### Revised literature facts

1. `fact-sq-simulates-minibatch-sgd`. Proven. The revised distinction between worst-case rounding and a floating-point trajectory is correct. AKMSS21 Theorems 1a and 1c do not justify a lower bound for unrestricted fine-precision SGD.

2. `fact-clwe-hardness`. Proven. The covariance conclusion has the wrong sign. In Bruna, Regev, Song and Tang, STOC 2021, Lemma 7.2, the Fourier transform contains the Gaussian variance minus the squared dual coordinate. Poisson summation therefore gives a variance deficit along the hidden direction. Corollary 7.3 preserves that sign. `ch-pancake-covariance-sign`, blocking.

3. `fact-hclwe-sq-correlation-bound`. Proven. BRST21 Proposition 8.3 supports the stated pairwise bounds with the corrected Gaussian normalization. It supplies correlations, not reconstruction hardness without the subsequent search reduction.

4. `fact-ngca-sq-lower-bound`. Proven. The revised scope matches Diakonikolas, Kane, Ren and Sun, NeurIPS 2023, Theorem 1.5. Its polynomial moment condition, dimension restrictions and additive approximation slack remain necessary.

5. `fact-generative-exponent-sq-recovery-bound`. Proven. The qualifications concerning Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, Theorem 4.1 and Remark 3.3 are correct. Their stated Theorem 3.2 remains a literature fact, but the builder’s independent randomized extension needs the repairs below.

6. `fact-ica-breaks-rotation-perturbation`. Heuristic. For nondegenerate independent non-Gaussian sources, the revised ICA interpretation is appropriate. Liu, Kargupta and Ryan, IEEE TKDE 2006, Sections 3 and 4 do not establish the computational guarantee suggested by “is undone”; retain the stated heuristic and empirical status.

7. `fact-instance-encoding-privacy-learnability`. Proven. The revised hypotheses and conclusions match CDGJMMSTT21 Theorems 3 to 5. The distinction between encoder access and initialization knowledge is necessary.

8. `fact-ideal-keyed-encoding-weak-learner`. Proven. CGJMMT21 Theorem 1 requires balanced error with a failure parameter, with both that parameter and the advantage positive constants below one half. The builder drops that hypothesis while retaining the parameter in the runtime. `ch-keyed-encoding-confidence`, blocking. Restore the theorem’s probability guarantee.

9. `fact-nrnt25-private-layer-hardness-route`. Proven. The single-record and nonzero bias-gradient conditions repair the quotient argument in NRNT25 Proposition 3. This establishes one inversion route, without establishing hardness against other routes.

10. `fact-orthogonal-equivariance-of-training`. Proven. Li, Zhang and Arora, ICLR 2021, Theorem C.1, Remark C.1 and Corollary C.2 support the mechanism under their model and update hypotheses. The distinction between function equivariance and transcript coupling is correct.

### The five proofs

`lem-equivariant-view-coupling`.

Proven. The induction holds under the protocol definition. The transformed pre-map cancels the transformed first-layer weights. Thus pre-activations, subsequent client computations and the adaptive server’s messages agree. The weight gradient transforms on the right, and the update hypothesis propagates the transformed weights and optimizer state.

Proven. The distributional conclusion follows because the transformation preserves the joint initialization law and independence from the records. Keeping the original records in the displayed joint law is legitimate. Label invariance is unnecessary for the pathwise identity and necessary for the proposed simulator.

Proven. This extends the known equivariance argument to the complete stipulated view. It closes `ch-transcript-side-information` within that view. It does not cover additional messages, augmentations or states outside the hypotheses.

Heuristic. The reduction is useful under Halil’s constraints when the protocol, initialization and label generation have explicit computational costs. Exact symmetry alone does not price simulation.

`lem-whitening-gives-rotated-records`.

Proven. The polar decomposition, pseudoinverse square root and cancellation are correct. Choosing the range basis from the subspace makes it unchanged under right rotation. The resulting square orthogonal factor transforms by right multiplication, so invariance implies its Haar law. Independence from the records follows from independent initialization.

Proven. The covariance here must mean covariance conditional on the realized client. For LeakyReLU, the negative slope must be known and nonzero.

Proven. This is an exact population result for isotropic records. It neither establishes finite-sample whitening nor applies unchanged to pancake records, whose covariance is anisotropic.

Heuristic. Population covariance is approximately measurable, but an experimental reconstruction guarantee also needs estimation accuracy and conditioning. The builder correctly leaves this error unproved in the lemma.

`prop-sq-blind-reconstruction-bound`.

Proven. The common simulation is valid. The bounded coordinate queries estimate the correlation vector, and the truncation plus oracle errors add as stated. Normalizing that vector yields a direction with constant absolute overlap once the covariance comparison is correct.

Proven. In part (a), `ch-pancake-covariance-sign` invalidates the stated covariance justification and chosen error comparison. The deficit is exponentially small in the proposed regime, so a corrected lower variance bound can repair the argument. The density domination and logarithmic truncation level are sufficient.

Proven. The packing argument and the Gram argument correctly bound how many planted directions one output can solve. BRST21 Proposition 8.3 then supplies the required correlations. Feldman, Grigorescu, Reyzin, Vempala and Xiao, JACM 2017, Lemma 3.10 and Theorem 3.2 support the randomized search reduction. Mapping bounded queries into the unit interval gives the stated STAT-to-VSTAT conversion in the relevant small-tolerance regime.

Proven. The final simplified price does not follow as written. The exact bound retains the difference between the tolerance term and the correlation term. That difference can approach zero arbitrarily closely. Also, the packing must be large enough for the solution-set fraction to lie below the success probability. Finally, a bound on the original queries plus the auxiliary queries requires subtracting the latter.

Proven. `ch-sq-price-range`, blocking. State a constant-factor margin above the correlation threshold, a sufficiently large packing, and the remaining subtraction. In the seed theorem, retain the minimum of the attacker tolerance and the auxiliary tolerance. Replacing it by the attacker tolerance when the latter is larger reverses the required comparison.

Proven. In part (b), the Ornstein–Uhlenbeck identity and bounded witness test are correct for a positive witness degree. Under the null, adaptive selection of the direction causes no problem because every fixed projection has the same Gaussian law.

Open. `ch-witness-uniformity`, blocking. The statement does not require a positive witness degree or dimension-uniform witness strength and degree. Degree zero satisfies the written witness assumption even for a Gaussian law. Moreover, shrinking witness strength or growing degree can make the auxiliary tolerance smaller than the DKRS23 threshold. Require a fixed positive degree, fixed positive strength and fixed success level, or retain their explicit dependence in the conclusion. The unconditional assertion that the witness tolerance is constant does not follow as written.

`prop-fine-reconstruction-to-hclwe`.

Proven. Step 1 follows from the coupling, including the attacker’s joint law with the target records.

Proven. Step 2 uses the false covariance lower bound from `ch-pancake-covariance-sign`. A corrected positive lower eigenvalue bound, close to the Gaussian variance, suffices. Density domination gives the stated sub-Gaussian order, and isotropic covariance concentration then gives the required least-squares conditioning with the proposed sample order. The least-squares perturbation and normalization estimates otherwise hold.

Proven. Step 3 uses BRST21’s normalization correctly. The Gaussian characteristic function gives the null expectation. At the layer frequency, every layer centre contributes the same phase. The within-layer Gaussian gives the stated attenuation. Angular error separates into independent perpendicular Gaussian attenuation and a longitudinal perturbation controlled by the first absolute moment.

Proven. Consequently, for sufficiently large dimension, the constant testing margin and held-out Hoeffding argument hold. Accounting for false positives changes only the exponentially small remainder.

Heuristic. This is a substantive reconstruction-to-testing reduction. Its polynomial-time corollary additionally requires polynomial protocol-simulation cost and a finite-precision implementation preserving the test margin. Those requirements should accompany the hardness conclusion.

`thm-reconstruction-from-conditional-mean`.

Proven. The proof holds for the stated frozen linear model, conditional on the client and predictor. Gaussian independence identifies the population correlation vector. Cauchy–Schwarz bounds its prediction-error component. The bounded predictor gives the stated second-moment concentration bound for independent held-out records. Normalization gives the direction estimate.

Proven. The fresh-record error equals the squared direction error. The empirical second-moment operator bounds training-record error regardless of dependence. This repairs `ch-population-to-sample-reconstruction`.

Proven. For LeakyReLU, distinguish the representation supplied to the predictor from the inverse-transformed representation supplied to whitening. The proof works with that convention.

Proven. This is an upper bound on reconstruction cost and error. The sentence calling it “Halil’s lower bound” is incorrect. `ch-conditional-mean-interpretation`, nonblocking for the theorem. Its first Hermite coefficient, predictor bound and whitening accuracy are experimental quantities, although estimating population whitening still costs samples.

### Remaining objects and challenges

`def-seed-blind-reconstruction-game`.

Proven. The sample baseline, global finite symmetry action and worst-case SQ-oracle quantifier make the two games well posed. Comparing attainable budget sets removes the undefined ratio. The population game evaluates a reconstruction function rather than reconstructing a supplied finite dataset, so delete the blanket sentence saying both games reconstruct observed records.

Heuristic. For experiments, specify finite representations of queries and returned predictors. The unrestricted measurable formulation is suitable for a lower bound, but does not itself define an executable attack.

`prop-sq-label-relevant-reconstruction-bound`.

Proven. Composing queries with a fresh linear client and extracting the Gaussian correlation vector through truncated queries works. Hidden-label invariance is unnecessary here because the reducer receives labels from the rotated single-index experiment.

Open. The randomized extension is not established by the builder’s argument. Three separate blocking challenges remain.

`ch-label-sq-self-correlation`, blocking. Proven. Lemma 3.10 requires a diagonal correlation bound. DPLB24’s proof uses diagonal bound one, but its stated class does not provide that bound. Its own Lemma 2.3 identifies diagonal chi-square information with the sum of squared Hermite coefficients, which need not be at most one or finite. Repeating the paper’s step does not verify the hypothesis. Supply a valid bound or a different argument.

`ch-label-sq-code-overlap`, blocking. Proven. DPLB24 Lemma E.3 has a square root around the displayed overlap expression. The builder omits it. Restore that square root and verify that the corrected overlap lies below the squared recovery threshold before applying the solution-set argument. This is not automatic throughout the stated query range.

`ch-label-sq-auxiliary-budget`, blocking. Proven. For a fixed query exponent and fixed generative exponent at least three, the auxiliary precision is eventually smaller than the claimed lower bound. For a query exponent growing near the permitted fourth-root ceiling, that comparison fails. The bound on the maximum of two precision budgets cannot then imply the claimed bound on the attacker’s budget.

Proven. Subject to valid correlation and packing hypotheses, FGRVX17 Theorem 3.2 is the correct tool for randomized success. Its solution-set factor changes constants when that fraction stays bounded away from the success probability.

Proven. Part (b) follows from DPLB24 Theorem 4.1 after population whitening, provided the server applies the theorem’s constructed label denoiser. Running Algorithm 1 on raw labels is not the cited guarantee. The final empirical reconstruction bound is correct.

`thm-blind-split-seed-separation`.

Proven. `ch-initial-observation-schedule`, blocking. In ordinary sequential training, only the first processed records necessarily have representations computed with the initial weights. Initialization knowledge does not reveal later weights. Require an initial forward pass over every target record, freeze the client during those observations, or supply the relevant current weights. LJDD19 Theorem 3 supports the per-record initial-weight claim, not the asserted schedule for every trained run.

Proven. Parts (ii) and (iii) inherit the preceding corrections. Part (iii) must retain the sample-budget and simulation-cost conditions.

Heuristic. The Gaussian layer is not an inserted cryptographic primitive. Nevertheless, this construction imports hardness through a cryptographically designed record law, and no useful learning task or training guarantee enters the separation. I would accept a repaired theorem as an artificial-distribution reduction. It does not yet establish non-trivial security arising from learning under Halil’s stronger objective.

`conj-seed-price-is-ngca-price`.

Proven. `ch-conjecture-erasing-client`, blocking. The conjecture is false for the stated protocol class. That class permits a constant post-map or a zero first layer. Such a client destroys record information, whereas NGCA coordinate recovery receives the records. Equivariance excludes neither example. Restrict the conjecture to clients with an explicit recoverability condition.

Proven. `ch-conjecture-whitening-scope`, blocking. The claimed settled upper inclusion invokes an isotropic whitening lemma for a general non-Gaussian component law. Whitening then yields a rotated standardized record, not necessarily the original NGCA record. Establish the conversion, including target scaling and its cost, before calling this inclusion settled.

`conj-reconstruction-at-training-cost`.

Proven. Accept its withdrawal. Independent random-sign labels give the stated constant conditional mean while preserving label information about the hidden coordinate’s magnitude. The conditional-mean theorem and label-recovery problem correctly separate these two questions.

## Verdicts

```text
VERDICT fact-sq-simulates-minibatch-sgd ACCEPT
VERDICT fact-clwe-hardness REVISE
VERDICT fact-hclwe-sq-correlation-bound ACCEPT
VERDICT fact-ngca-sq-lower-bound ACCEPT
VERDICT fact-generative-exponent-sq-recovery-bound ACCEPT
VERDICT fact-ica-breaks-rotation-perturbation ACCEPT
VERDICT fact-instance-encoding-privacy-learnability ACCEPT
VERDICT fact-ideal-keyed-encoding-weak-learner REVISE
VERDICT fact-nrnt25-private-layer-hardness-route ACCEPT
VERDICT fact-orthogonal-equivariance-of-training ACCEPT
VERDICT def-seed-blind-reconstruction-game ACCEPT
VERDICT lem-equivariant-view-coupling ACCEPT
VERDICT lem-whitening-gives-rotated-records ACCEPT
VERDICT prop-sq-blind-reconstruction-bound REVISE
VERDICT prop-fine-reconstruction-to-hclwe REVISE
VERDICT thm-blind-split-seed-separation REVISE
VERDICT conj-seed-price-is-ngca-price REJECT
VERDICT thm-reconstruction-from-conditional-mean ACCEPT
VERDICT prop-sq-label-relevant-reconstruction-bound REVISE
VERDICT conj-reconstruction-at-training-cost ACCEPT
BLOCKING 10
```