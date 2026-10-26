---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-25
prompt: lab/theory/spaces/hard-problem-mappings/round-00/prompt-sol.md
---

Heuristic. Round 01 should prioritize the extraction separation, after repairing its game. Keep the mapping definition as bookkeeping. Replace the backdoor conjecture with separate statements about weight testing, Gram sufficiency, and matrix transposition. Its present equivalence is false.

Proven. The catalogue identifies several valid reductions, but it also repeats errors in the cited sources. The most consequential concern GKVZ22 Appendix A and the advantage normalization in CDGJMMSTT21.

1. `fact-jagielski-extraction-query-bounds`

Proven. JCBKP20, Jagielski et al., USENIX Security 2020, Theorem 1 supports the stated worst-case query bound. Its Theorem 3 imports the random-network result rather than proving another extraction theorem.

Proven. The builder correctly identifies DGKP20’s inconsistent weight distributions. Gaussian rows support Lemma 3. Independent uniform positive entries do not. The exponential lower bound follows from Theorem 9, Lemma 12, and Theorem 15 in the stated depth range, with the burn-in and residual errors retained.

Proven. `ch-extraction-catalogue`, nonblocking. The lower bound concerns the product of query count and squared inverse tolerance or inverse learning advantage. It does not independently lower-bound sample count. Lemma 17 exhibits correlation with a linear function that depends on the teacher’s weights. That alone does not supply a learner that constructs this function from its permitted observations.

Proven. There is also a complexity convention to clarify. JCBKP20 Appendix A constructs inequivalent networks exactly when the subset-sum instance is satisfiable. This establishes NP-hardness of inequivalence and coNP-hardness of equivalence under many-one reductions. Equivalence is NP-hard under polynomial-time Turing reductions.

Heuristic. Retain this entry as the required extraction baseline. Its random, untrained teacher supplies no substantive trainer-to-extractor comparison.

2. `fact-gkvz22-backdoor-scope`

Proven. The RFF account matches Goldwasser, Kim, Vaikuntanathan and Zamir, FOCS 2022, Theorem 6.4. The polynomial parameter relations, Assumption 6.3’s normalized head and uniform margin, and Hypothesis 3.7 matter. The reduction through sampled feature weights holds.

Proven. `ch-sparse-pca-source`, blocking. Appendix A cannot be certified as correct. For fixed positive spike strength, width proportional to dimension, and sparsity growing more slowly than the square root of dimension, the builder’s coordinate-variance test distinguishes with advantage tending to one. These parameters fall inside the printed Lemma A.3.

Proven. Claim A.5’s activation condition also fails. Take theta 1, lambda 1.1, tau 1, and a unit input orthogonal to the key. The triggered Gaussian preactivation has variance 3.42. Its mean ReLU remains below the threshold. As width grows, activation fails with probability tending to one. The clean input is negative with probability tending to one. The sketch’s asserted standard-deviation lower bound is invalid.

Heuristic. Retain the RFF mapping. Describe Appendix A as containing a parameter error, rather than importing its undetectability conclusion.

3. `fact-frozen-gaussian-layer-collision-hardness`

Proven. The SBP definition, Assumption 2, and the collision reduction match the held anonymous BRV26 submission. Subtracting distinct integer inputs doubles their coordinate bound. Bilipschitzness converts an output collision into an SBP solution. The training operator must remain efficient and satisfy its stated bilipschitz guarantee.

Proven. `ch-collision-parameters`, blocking. The Corollary 3 sentence omits restrictions that determine its conclusion. Besides the displayed width and depth, the corollary assumes the leaky-ReLU parameter is at least 1/100 and bounds the later layers’ condition numbers. Arbitrarily small activation parameters or arbitrarily large condition numbers destroy the claimed exponential strength.

Open. The extracted logarithm in Theorem 2 remains unresolved. Give a safely supported asymptotic bound until the typography is checked. The anonymous held copy also cannot establish its later author and venue metadata.

Heuristic. This is a substantive admissible mapping. The honest frozen Gaussian layer itself supplies the hard instance.

4. `fact-instance-encoding-privacy-learnability`

Proven. The hypotheses and oracle lists largely match Carlini et al., IEEE S&P 2021, Theorems 4 and 5. The learning-versus-distinguishing dichotomy is correctly directed. Learning hardness excludes the high-accuracy alternative and thereby yields an attack.

Proven. `ch-encoding-normalization`, blocking. Definition 5 defines advantage as success probability minus one half. Theorem 4’s printed advantage can approach one, which is impossible under that definition. Appendix A uses a difference of acceptance probabilities. Under Definition 5, that difference must be halved. Theorem 5’s constants also require checking against this convention.

Proven. The expected-time expressions use oracle access. They do not price the encoder and learner as ordinary unit-time computations. In the project’s units, the catalogue must separately count training calls, records consumed, and evaluation work.

Heuristic. Retain the dichotomy after fixing normalization and accounting. It concerns distinguishing encodings with an encoder oracle, rather than the blind reconstruction task.

5. `fact-chlx25-defendability-characterization`

Proven. The theorem numbers and qualitative conclusions match Christiano, Hilton, Lecomte and Xu, ITCS 2025, Theorem 4.1, Corollary 5.2, and Theorems 5.3 and 5.5.

Proven. `ch-defense-price`, nonblocking. Corollary 5.2 does not establish a universal multiplier of inverse backdoor mass between detector and learner sample costs. Its proof chooses a prediction sample size and repeats predictions. State that construction’s parameters explicitly or remove the multiplier.

Proven. The game also declares the detector successful when the proposed backdoor is invalid. This clause matters for Theorem 5.3, whose separation exploits the scarcity of valid modifications.

Heuristic. Keep this as a boundary result. The obfuscation construction falls outside the project’s intended admissible mechanisms.

6. `fact-generative-exponent-post-processing-monotone`

Proven. This entry correctly states Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, Definition 2.4, Proposition 2.6, its following Markov-channel remark, Example 2.7(ii), Corollary 2.8, and Theorems 4.1 and 5.2.

Proven. The Appendix E.2 caveat is justified. The diagonal correlation is the chi-squared information, whereas the proof inserts diagonal bound 1. Finite information repairs that step with its actual value. Bounded links with independent Gaussian answer noise provide the required finiteness.

Heuristic. This is useful structural mathematics and needs no independent research aim.

7. `lem-sparse-pca-backdoor-width-price`

Proven. Part (a) holds line by line. The upper-tail substitution is conservative. A supported coordinate has sufficient variance increase. The lower-tail comparison and union bound give the stated constants.

Proven. Part (b) is the valid contrapositive of (a), followed by substitution of the activation condition. Its growing perturbation conclusion holds in the stated asymptotic regime.

Proven. Part (c) holds pointwise at the original width, but its backdoored proof introduces an unnecessary factor. Use the actual preactivation standard deviation for both the mean and the deviation. Their ratio cancels, giving the same concentration exponent as under honest weights.

Proven. `ch-sparse-pca-quantifiers`, blocking. The concluding assertion about every input simultaneously does not follow. For width below dimension, a realized weight matrix has a nullspace. Choosing the input and perturbation direction there defeats the claimed uniform conclusion, however large lambda becomes. State the result for each fixed input and direction independent of the sampled weights.

Proven. `ch-sparse-pca-source` also blocks the sentence declaring Claim A.5 true as stated. The lemma instead exposes a defect in that claim.

Heuristic. Keep the repaired lemma. Its width price is measurable and useful, although its novelty is narrower than the current interpretation.

8. `def-hard-problem-mapping`

Proven. `ch-mapping-price-types`, blocking. The exponent ratio is undefined. The prices contain budget vectors and advantages, and some catalogue entries have zero training cost. A logarithmic ratio requires a chosen positive scalar resource, fixed success levels, an asymptotic family, and an existing limit.

Proven. A VSTAT parameter is not an actual sample count. Simulating several adaptive statistical queries incurs additional sampling and confidence costs. Low-degree reductions likewise require degree accounting. Polynomial simulation time alone does not preserve a low-degree restriction.

Proven. The inherited table also conflates learning the hidden index with learning the prediction task. The booklet’s refuted reconstruction-at-training-cost conjecture already gives a counterexample to that identification.

Heuristic. `ch-carrier-policy`, nonblocking. Keep the carrier as declared construction metadata. It is not an intrinsic ordered property of reductions. The project explicitly permits discovering one-wayness inherent in a model, which a blanket primitive exclusion could wrongly discard.

Heuristic. Retain a shorter definition and one transfer lemma. Routine reduction composition does not merit two rounds by itself.

9. `conj-extraction-priced-by-generative-exponent`

Proven. The level-set calculation holds line by line. The Jacobian weights are correct. Sign symmetry cancels the odd moments. The second conditional moment equals the Gaussian second moment, and the fourth Hermite conditional moment is nonzero. The resulting exponent 4 agrees with DPLB24 Example 2.7(ii) and Corollary 2.8. The original stochastic labels have exponent 2 as claimed.

Proven. `ch-extraction-game`, blocking. “Bounded” supplies no common bound across dimension. An extractor can scale a fixed function by a dimension-dependent constant. For this even link, a fixed-direction copy has positive covariance with almost every target direction. Scaling it satisfies the stated threshold with substantial probability without observing answers. Require a uniform output bound or normalize by output variance. “Fidelity tending to 1” also needs a defined score.

Proven. The proposed null test requires centering. Independence makes covariance vanish, whereas the uncentered product expectation need not vanish. Here the Bayes link has positive mean.

Proven. Claim (b) is correct under its Markov sufficiency hypothesis. Conditional expectation alone does not imply that hypothesis.

Open. I cannot certify the particular stochastic-label versus Bayes-release separation as previously published. Its degree-4 deterministic link and its exponent are already known. The new candidate is the paired training and extraction experiment.

Heuristic. Keep this aim first. Specify a known fixed link, a rotation-invariant trainer, normalized fidelity, and distinct SQ lower and sample-based upper statements. A generic fitted neural network need not preserve the exact moment cancellations. The experiment must therefore enforce the release architecture. Its proposed scaling prediction remains heuristic.

10. `conj-backdoor-detection-is-ngca`

Proven. Part (a) holds for explicit weight releases when every other released component is generated from those weights and independent auxiliary randomness. Its proof is direct simulation and post-processing.

Proven. `ch-feature-equivalence`, blocking. Rotation invariance makes the exact Gram matrix sufficient for testing these rotationally invariant hypotheses. It does not make the feature law sufficient to recover that matrix. A constant activation erases all weight information and is allowed by the statement. Restrict the activation and prove identifiable, quantitatively stable Gram recovery.

Proven. `ch-transpose-transfer`, blocking. The matrix transpose identity holds without offsets, or with offsets explicitly transposed. It does not transfer detection into recovery of key projections. Chosen probes can reveal weights while leaving the planted direction hidden. The first milestone’s seed-known inversion theorem reconstructs records. It does not recover an unknown direction inside their law. Detection and coordinate recovery require separate reductions.

Proven. `ch-row-sq-transfer`, blocking. An auditor holding all sampled weights is not a population SQ auditor of their generating law. The simulation in (a) does not establish an SQ reduction. Moreover, the sparse-key law used in Appendix A is not the uniform spherical prior used in the Gram argument.

Heuristic. Defer the full conjecture. Keep the exact transpose identity and investigate a specified activation’s Gram recovery cost. Require a trigger and a proved behavioral effect before calling an arbitrary planted weight law a backdoor.

Proven. The catalogue also omits two useful existing mappings. Chandrasekaran, Chaudhuri, Giacomelli, Jha and Yan, USENIX Security 2020, Observation 1 maps query-synthesis active learning to extraction with the same query budget. DPLB24 Proposition 3.7 supplies the single-index-to-NGCA reduction. These give an extraction upper bound and an explicit bridge to the proposed hard problem.

Empirical. The recorded unsuccessful searches support “not found within the recorded search scope.” They do not establish the unrestricted absence claims in Part 3.

## Verdicts

```text
VERDICT fact-jagielski-extraction-query-bounds REVISE
VERDICT fact-gkvz22-backdoor-scope REVISE
VERDICT fact-frozen-gaussian-layer-collision-hardness REVISE
VERDICT fact-instance-encoding-privacy-learnability REVISE
VERDICT fact-chlx25-defendability-characterization REVISE
VERDICT fact-generative-exponent-post-processing-monotone ACCEPT
VERDICT lem-sparse-pca-backdoor-width-price REVISE
VERDICT def-hard-problem-mapping REVISE
VERDICT conj-extraction-priced-by-generative-exponent REVISE
VERDICT conj-backdoor-detection-is-ngca REVISE
BLOCKING 9
```