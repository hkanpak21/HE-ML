---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-25
prompt: lab/theory/spaces/hard-problem-mappings/round-01/prompt-sol.md
---

Proven. This round does not reach BLOCKING 0. The extraction lower bound holds. Five blocking challenges remain, including one carried from round 00.

Proven. The following round-00 challenges close through the stated restrictions or withdrawals: `ch-sparse-pca-source`, `ch-sparse-pca-quantifiers`, `ch-collision-parameters`, `ch-encoding-normalization`, `ch-extraction-game`, `ch-feature-equivalence`, `ch-transpose-transfer`, and `ch-row-sq-transfer`. The nonblocking challenges `ch-extraction-catalogue`, `ch-defense-price`, and `ch-carrier-policy` also close. `ch-mapping-price-types` remains open because the catalogue still gives an incorrect sample price.

Proven. `fact-jagielski-extraction-query-bounds` now reads its sources correctly. Jagielski et al., USENIX Security 2020, Theorem 1 gives the constructed worst-case query bound. Appendix A establishes NP-hardness of inequivalence. Das et al., SODA 2020, Lemma 12 and Theorem 15 support the corrected exponential lower bound, subject to the Gaussian-weight, depth, burn-in, and residual-error qualifications retained here. The correction concerning Lemma 17 is necessary. Its weight-dependent linear function does not constitute a learner from the permitted observations.

Proven. `fact-gkvz22-backdoor-scope` correctly separates Goldwasser, Kim, Vaikuntanathan and Zamir, FOCS 2022, Theorem 6.4 from Appendix A. The RFF reduction needs its margin, normalization, parameter relations, and named hardness hypothesis. Appendix A’s printed sparse-PCA indistinguishability claim fails under the coordinate test. Its activation condition also fails. Withdrawing both imported conclusions closes `ch-sparse-pca-source`.

Proven. `fact-frozen-gaussian-layer-collision-hardness` now includes the restrictions of Corollary 3 in the held anonymous submission. Its reduction correctly doubles the integer coordinate bound. Theorem 2’s concluding sentence supports the retained asymptotic statistical-distance statement. The final parameter warning should concern loss of the stated guarantee. Corollary 3 gives sufficient parameter ranges, without establishing their necessity. The Bogdanov, Rosen and Vafa attribution and ICML 2026 venue remain library-record metadata.

Proven. `fact-instance-encoding-privacy-learnability` repairs the advantage normalization in Carlini et al., IEEE S&P 2021, Theorems 4 and 5. Appendix A.3 needs a correction to the order of the acceptance probabilities as well as the displayed inequality. The conditions defining the selected pair yield the builder’s halved lower bound after orienting the test correctly.

Open. The source’s instruction to repeat training until the true encoded error meets a threshold is not an operational finite-sample validation procedure. Experimental accounting needs validation slack and its cost. The stated oracle counts do not include that cost.

Proven. `fact-chlx25-defendability-characterization` correctly retains Christiano et al., ITCS 2025, Theorem 4.1, Corollary 5.2, and Theorems 5.3 and 5.5. The invalid-backdoor winning clause matters. Removing the universal sample multiplier closes `ch-defense-price`.

Proven. `fact-active-learning-is-extraction` correctly states Chandrasekaran et al., USENIX Security 2020, Observation 1 and Proposition 1. The noisy-answer simulation requires independent fresh answer randomness, or the corresponding conditional correctness guarantee at every repetition. A marginal flip probability alone would permit correlated errors that repetition cannot remove.

Proven. `lem-sparse-pca-backdoor-width-price` parts (a), (b), and (d) hold. The tail substitutions and contrapositive are valid. The activation counterexample directly refutes Claim A.5’s sufficient condition. Part (c)’s Gaussian concentration proof also holds whenever the perturbed input is nonzero. Fixing the input and direction independently of the weights closes `ch-sparse-pca-quantifiers`.

Proven. `ch-zero-trigger-variance`, blocking. Part (c) also permits lambda 1 and a direction opposite the input. The perturbed input and its mean response then vanish. The displayed non-strict deviation event has probability one, while its proposed upper bound can be below one. Handle this case separately or change the deviation event appropriately.

Heuristic. The key-insensitivity conclusion is useful at the level of population response and concentration. Its displayed orthogonal direction depends on the unknown key. An operational key-free comparison should specify a radial perturbation or analyze an independently sampled direction. Equality of population responses does not assert equality for every realized network.

Proven. `def-hard-problem-mapping` repairs the definition of the exponent ratio, the carrier metadata, and the regime-preservation requirements. `lem-mapping-transfer` then holds directly from the reduction and its budget accounting.

Proven. `ch-mapping-price-types`, blocking, remains in the table. The extraction row claims a sample upper bound with no linear floor when the released link has generative exponent 1. DPLB24 Theorem 4.1 explicitly retains that floor. A bounded monotone link with Gaussian answer noise provides a counterexample to the claimed square-root sample price. Constant fidelity resolves an exponentially large packing of directions up to bounded list size, while each answer carries bounded information. A linear sample count follows. Retain the linear term and present the SQ lower bound and sample upper bound as separate mappings.

Proven. `prop-learner-side-sq-transfer` part (a) holds line by line. Composition with an unbounded postprocessor still observes only the learner’s one-bit transcript and independent coins. Feldman et al., JACM 2017, Theorem 3.13 therefore applies. The direction of VSTAT simulation in the proof is correct.

Proven. `ch-one-bit-success-constant`, blocking. Part (b) copies a typographical error from [FGRVX17 Theorem 3.16](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/jacm/FGRVX17_StatisticalAlgorithmsLowerBound.pdf). Replace the plus sign inside the squared numerator by a minus sign. Substitute the proof’s chosen simulation error into its VSTAT budget to obtain this correction. The theorem’s own specialization to success probability 2/3 confirms it. The printed stronger expression does not follow and is false for success approaching one half.

Proven. `lem-level-set-moment-balance` holds line by line. The branch Jacobians give the stated conditional weights. Sign symmetry cancels the odd moments. The second moment balances exactly, and the fourth Hermite conditional moment is nonzero on a set of positive probability. This agrees with Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, Example 2.7(ii), after the invertible transformation on the link’s range.

Heuristic. This lemma and its paired training and extraction construction justify continuing the space. They supply a measurable construction with a short structural proof and no cryptographic plug-in.

Proven. `thm-extraction-exponent-price` part (a) survives all five proof steps.

1. The likelihood-ratio envelope is valid. Bounded means and positive Gaussian answer noise make its squared envelope integrable under the answer marginal. This establishes finite chi-squared information. DPLB24 Theorem 5.2 preserves the generative exponent.
2. DPLB24 Lemma E.3 supplies the required code. The absolute-correlation bound follows from Lemma 3.1’s series and conditional Jensen. The diagonal is the actual chi-squared information, as required by Lemma 2.3. This repairs the diagonal shortcut in Appendix E.2.
3. FGRVX17 Lemma 3.10 and Theorem 3.7 apply with the stated constants. The diagonal exceeds the off-diagonal bound for sufficiently large dimension. Increasing oracle tolerance preserves the lower bound.
4. Haar rotation correctly produces a uniform direction. The pullback of the output has the required covariance. Centering removes the null mean. Clipping bounds the noise-tail contribution uniformly over the bounded output. The three validation queries and their stated error budget separate the hypotheses. Balanced decision success is at least 5/6.
5. The chosen code size makes the required query count exceed the polynomial allowance. The validation parameter stays constant, and all code and correlation conditions eventually hold.

Proven. These statements use the standard adversarial VSTAT convention. Extraction success must hold against every valid answer strategy.

Proven. Part (b)’s direction-recovery rate follows from [DPLB24 Theorem 4.1](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/colt/DPLB24_ComputationalStatisticalGapsGaussian.pdf). Its Hermite expansion and continuity argument correctly convert oriented direction recovery into normalized prediction error for any bounded measurable link.

Proven. `ch-extraction-sign-confidence`, blocking. The proposed sign-selection stage uses a number of additional pairs independent of dimension at fixed target error. For a noneven link, Gaussian answer noise leaves positive sign-selection error with finitely many such pairs. That stage cannot supply the claimed failure probability tending exponentially to zero. Reserve enough independent validation samples for the requested confidence, or lower the confidence claim. Sample splitting can preserve the stated dimension exponent.

Open. Knowing an arbitrary measurable link does not imply that its denoiser is computable at a charged cost. The experimental version should restrict the link or price denoiser approximation. This is a realization issue beyond the sample guarantee imported from Theorem 4.1.

Proven. Part (c)’s channel inequality is correct under its explicit Markov hypothesis, by Proposition 2.6 and the following paragraph. Conditional expectation alone would not establish that hypothesis. Its interpretation compares the exponents associated with direction recovery and release extraction. It does not identify prediction learning with direction recovery.

Proven. Part (d)’s noiseless training law has generative exponent 2 and the stated Bayes link. The label’s magnitude reveals the absolute projection. The released link has exponent 4 by the level-set lemma. Theorem 4.1 supplies the trainer’s linear record price at fixed direction accuracy. The even release avoids part (b)’s sign-selection problem.

Proven. Algorithm 1 is rotation equivariant at the level of its recovered line. An arbitrary eigenvector sign convention need not produce a uniform signed vector. Randomizing that sign repairs the assertion about the vector. The even released link already depends only on the line, so this issue does not invalidate the separation.

Heuristic. The comparison between the trainer’s record count and the extractor’s VSTAT parameter has the correct heuristic label. It establishes no unrestricted sample lower bound or polynomial-time lower bound.

Proven. DPLB24 Proposition 3.7 supplies the claimed single-index-to-NGCA bridge by conditioning on a label event of positive, dimension-independent probability. It does not establish a two-way equivalence.

Proven. Theorem 6.1 supplies a statistical upper bound. It does not, by itself, establish the statistical optimality asserted in the “Other regime” paragraph. Retain sufficiency or provide a separate lower-bound record.

Proven. `conj-extraction-priced-by-generative-exponent` can be withdrawn in favor of the repaired theorem. Its replacement should remain under revision until the confidence claim is fixed.

Proven. `prop-weight-testing-equals-white-box-detection` holds by simulation and projection. The algorithm class must be closed under these compositions. Simulation adds one execution of head training and the stated auxiliary sampling. This is an exact sample-based equivalence. It supplies no population SQ simulation of an explicit weight matrix.

Proven. `prop-gram-sufficiency-rotation-invariant` has a correct statistical argument. Equal row Gram matrices determine the same orthogonal orbit. Haar averaging preserves both hypotheses under the uniform key prior. The ReLU second-moment calculation and strict kernel monotonicity recover every Gram entry, with zero rows handled directly.

Proven. `ch-gram-test-running-time`, blocking. Part (i) permits every test, including unbounded tests, and then claims polynomial running time. The construction has polynomial overhead in addition to the running time of the original test. Restrict the test or state that overhead.

Open. Exact feature-law access supplies no finite-probe price. Leaving precision and test stability open is appropriate. The exact sufficiency result alone does not complete an experimentally priced detection mapping.

Proven. `lem-feature-matrix-transpose` holds, with the two matrices sampled independently as used in its proof. For each nonzero row, enough Gaussian probes give enough positive equations and full rank with the stated high probability. A union bound gives simultaneous recovery. Lei et al., NeurIPS 2019, Theorem 3 supports this inversion statement. No independence between the row-recovery events is required. The lemma correctly transfers no hidden-direction recovery conclusion.

Proven. Withdrawing `conj-backdoor-detection-is-ngca` is appropriate. Its three replacements separate exact simulation, statistical sufficiency, and matrix inversion. The remaining blocking challenge among those replacements concerns the Gram statement’s running time.

## Verdicts

```text
VERDICT fact-jagielski-extraction-query-bounds ACCEPT
VERDICT fact-gkvz22-backdoor-scope ACCEPT
VERDICT fact-frozen-gaussian-layer-collision-hardness ACCEPT
VERDICT fact-instance-encoding-privacy-learnability ACCEPT
VERDICT fact-chlx25-defendability-characterization ACCEPT
VERDICT fact-active-learning-is-extraction ACCEPT
VERDICT lem-sparse-pca-backdoor-width-price REVISE
VERDICT def-hard-problem-mapping REVISE
VERDICT lem-mapping-transfer ACCEPT
VERDICT prop-learner-side-sq-transfer REVISE
VERDICT lem-level-set-moment-balance ACCEPT
VERDICT thm-extraction-exponent-price REVISE
VERDICT conj-extraction-priced-by-generative-exponent ACCEPT
VERDICT prop-weight-testing-equals-white-box-detection ACCEPT
VERDICT prop-gram-sufficiency-rotation-invariant REVISE
VERDICT lem-feature-matrix-transpose ACCEPT
VERDICT conj-backdoor-detection-is-ngca ACCEPT
BLOCKING 5
```