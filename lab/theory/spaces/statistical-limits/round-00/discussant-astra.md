---
model: gpt-6-astra
discussant: astra
date: 2026-10-25
prompt: lab/theory/spaces/statistical-limits/round-00/prompt-astra.md
---

The round needs revision. Proven. The chosen-seed interface invalidates the proposed Assouad construction. Several literature objects also omit hypotheses or strengthen their sources. Open. The full oracle lower bound and the novelty of the reconstruction floor remain unsettled.

Empirical. I opened all eight supplied PDFs. The builder contains thirteen fact objects and three proposed objects. I judge all sixteen below. No file was written or edited.

1. `fact-hsu-membership-sample-gap`

Proven. The theorem numbers and displayed bounds match the held HSU25 version. The matching upper and lower sample orders apply near the stated dimension threshold. They do not establish matching orders for every larger dimension. Check Haghifam, Smith and Ullman, arXiv 2025, Definitions 2.1–2.4, Proposition 2.5, Theorems 3.1 and 3.3, and Remark 3.4 in the [PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/focs/HSU25_SampleComplexityMembershipInference.pdf).

Proven. `ch-hsu-estimator-access`, blocking. Definition 3.2 imposes more than permutation symmetry. The estimator must factor through the empirical mean. The builder’s description admits symmetric estimators outside that class.

Proven. The same challenge also blocks the claim that an attacker can freely simulate this estimator merely because it knows the algorithm. The noise covariance depends on the unknown population covariance. Knowing the formula does not provide an executable sampler for that noise. Train access to this mechanism can therefore reveal information unavailable in Definition 2.1.

Proven. The proof outline correctly identifies the mixture argument and dimension reduction. It does not establish the claimed transfer to arbitrary Train access. The polynomial attack and statistical lower bound give matching sample orders only in the matching regime, with the stated estimator restrictions.

Heuristic. This remains a substantive statistical benchmark. Its use in the proposed profile requires an explicit distinction between knowing the estimator’s formula and possessing an oracle that executes its population-dependent randomness.

2. `fact-hsu-gap-prices-covariance`

Proven. Theorem 4.1 and its hypotheses are transcribed correctly. The paper attributes the sufficient condition to Dwork et al. The builder correctly distinguishes that attribution from a proof supplied by HSU25.

Proven. `ch-hsu-covariance-order`, blocking. The final sentence changes an upper bound into a tight order. Remark 4.2 says that order n samples suffice. It does not say that order n samples are necessary. In the stated high-noise regime, the sharper expression immediately preceding it is governed by inverse squared noise and can be smaller than n.

Proven. The claim that every sample price is necessarily ignorance of the data law also needs scope. Knowing the population law need not determine an unknown release mechanism. It eliminates the reference-sample requirement only when the informed adversary also knows the relevant joint experiment.

Heuristic. Retain the covariance comparison as a substantive example. Replace the final order claim and restrict the interpretation of “ignorance” to the experiment actually analyzed.

3. `fact-yeom-dp-bounds-membership-advantage`

Proven. Accept. Experiment 1, Definition 4 and Theorem 1 match the builder’s statement. Replacement adjacency, independent sampling and the membership convention are the relevant hypotheses. The replacement argument applies DP conditionally and then averages. No computational restriction enters. Check Yeom, Giacomelli, Fredrikson and Jha, CSF 2018, §3.1 in the [PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/csf/YGFJ18_PrivacyRiskMachineLearning.pdf).

Heuristic. This is useful borrowed background for the informed endpoint. It supplies no new training-run price.

4. `fact-yeom-generalization-error-gives-advantage`

Proven. Theorem 2 and the randomized attack are correctly stated. Subtracting its expected outputs gives the normalized generalization error exactly.

Proven. `ch-yeom-cost-and-normalization`, nonblocking for the theorem. The closing interpretation drops the normalization by the loss bound. It also calls the attack constant time without charging model evaluation and loss computation. Finally, the theorem exhibits an attack. It does not assert that every attacker achieves that advantage.

Proven. Specify a nonnegative loss and a positive bound. Describe one model evaluation, loss computation and a randomized decision. Equality with the unnormalized generalization gap holds for the unit-bounded normalization.

Heuristic. Retain this as a borrowed achievable baseline, with revised commentary.

5. `fact-lira-priced-in-training-runs`

Empirical. The reported training counts, variance-pooling comparison and disjoint-dataset experiment agree with Carlini et al., IEEE S&P 2022, §V, §VI-B and §VI-D. These observations concern the reported datasets and training procedures. Check the [PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/ieee-sp/CCNSTT22_MembershipInferenceAttacksFirst.pdf).

Proven. `ch-lira-parametric-necessity`, nonblocking for those empirical facts. The conclusion that LiRA has a finite price “only because” of its Gaussian assumption does not follow. The accepted impossibility excludes a uniform rate over unrestricted atomless laws. It does not exclude finite accuracy at a particular law, other restricted families, or useful nonparametric attacks.

Heuristic. The Gaussian fit explains the chosen estimator and its bias–variance tradeoff. It does not prove necessity of Gaussian modeling. Moreover, the reported performance is not a certificate of proximity to total variation.

6. `fact-lira-low-fpr-yeom-game`

Proven. The corrected location, Definition 1 in §III-A, is right.

Proven. `ch-lira-out-exclusion`, blocking. The PDF explicitly requires the OUT point not to belong to the sampled training set. The builder omits this condition. Yeom’s independently drawn population point can coincide with a training record.

Proven. Consequently, these games need not agree on an atomic population. They agree under an appropriate zero-collision assumption, with their bit conventions reversed. Restore the exclusion condition and state the assumption needed for equivalence.

7. `fact-balle-reconstruction-robustness-definition`

Proven. The definition-number correction is right. Definition 1 specifies the informed adversary. Definition 2 specifies reconstruction robustness. The baseline also matches §VII-B. Check Balle, Cherubin and Hayes, IEEE S&P 2022, in the [PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/ieee-sp/BCH22_ReconstructingTrainingDataInformed.pdf).

Proven. `ch-balle-prior-knowledge`, blocking. The adversary is allowed full knowledge of the prior. The paragraph following Definition 2 explicitly says so. The unknown object is the realized target record. Calling the prior the remaining source of ignorance reverses the experiment.

Proven. Deterministic attacks suffice at the level of suprema by averaging over attack randomness. Attainment by a measurable posterior maximizer needs additional hypotheses. The paper’s informal argmax expression does not establish attainment on arbitrary spaces.

Heuristic. This is a useful statistical baseline. It does not price learning the prior or training a reconstruction model.

8. `fact-balle-dp-bounds-reconstruction`

Proven. Theorem 2, Corollaries 3 and 4, and Theorem 5 have the stated functional forms. The change-of-measure proof of Theorem 2 and the two-point reconstruction proof of Theorem 5 support them.

Proven. `ch-balle-radius-hypotheses`, blocking. Proposition 6 fixes a constant reconstruction radius strictly between zero and one. The builder omits that restriction. At radius one, the center reconstructs every point in the unit ball, so exponentially small success is false.

Proven. The Gaussian proposition fixes a positive constant radius and uses an isotropic Gaussian prior. Theorem 5 requires a zero–one loss tolerance strictly between zero and one. Restore these hypotheses, the Rényi order restriction, and the parameter domains.

Proven. A coupled certificate bounds the particular divergence it targets. Applying it to reconstruction requires the appropriate neighboring datasets and prior averaging. It does not automatically provide a uniform privacy parameter for an arbitrary mechanism.

9. `fact-reconstruction-query-lower-bounds`

Proven. The experiment and Theorem 9 are correctly identified. Appendix B.2 proves the displayed risk bound by two-point reduction, product-distribution overlap and the DP bound on total variation. The logarithmic query formulation requires nondegenerate privacy parameters and a target error below the relevant baseline. Check Mukherjee and Lokam, arXiv 2024, in the [PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/arxiv/ML24_QueryComplexityTrainingData.pdf).

Proven. `ch-reconstruction-query-tightness`, blocking. Theorem 10 is stated in the paper, but its Appendix B.5 attack uses the unknown true target to decide which observed output receives randomized treatment. That does not construct one adversary for the minimax experiment.

Proven. The problem matters quantitatively. For pure DP with a small privacy parameter, two-point randomized response has per-observation KL divergence of order the squared privacy parameter. Constant-error testing therefore needs inverse-squared-parameter observations. The asserted uniform matching rate would permit inverse-parameter observations.

Proven. Corollary 12 also needs separate scrutiny. Appendix B.3 writes a minimization where an upper bound requires maximization, then uses feasibility of one point as an upper bound on the optimum. That argument does not prove the claimed bound.

Open. I accept Theorem 9 as a borrowed lower bound. I do not accept the blanket “proven” label for the matching claim and Rényi extension. The builder must separate faithful reporting of a theorem statement from verification of its proof.

10. `fact-dinur-nissim-reconstruction-thresholds`

Proven. Theorems 2 and 3, their perturbation assumptions, the exhaustive-query attack and the random-query linear program match the source. Theorem 5 has the stated uniform-prior and time-budget setting. Check Dinur and Nissim, PODS 2003, in the [PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/pods/DN03_RevealingInformationWhilePreserving.pdf).

Proven. `ch-dinur-resource-comparison`, nonblocking for the borrowed attack theorems. These results do not isolate computational hardness at a fixed observation budget. The exponential attack receives exponentially many answers. The polynomial attack receives polynomially many answers. The comparison changes both information access and computation.

Proven. Theorem 5 additionally uses Definition 4’s two-stage individual-bit game. The adversary chooses the target coordinate before receiving the remaining database. That definition should accompany the privacy assertion.

Heuristic. This is relevant resource-bounded reconstruction background. It should not be presented as an established computational separation with information held fixed.

11. `fact-pac-privacy-mutual-information-bound`

Proven. Theorem 1, Corollary 1 and Remark 1 are the intended references in Xiao and Devadas, CRYPTO 2023. Check Appendix A as well as the statements in the [PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/crypto/XD23_PACPrivacyAutomaticPrivacy.pdf).

Proven. `ch-pac-suboptimal-adversaries`, blocking. The Bernoulli KL inequality cannot hold for the actual failure probability of every adversary. An adversary can deliberately perform worse than optimal prior guessing.

Proven. For a counterexample, let the release be constant and let the target take two values with probabilities 0.9 and 0.1. Always guessing the rarer value gives failure 0.9. Optimal prior failure is 0.1. Their Bernoulli KL divergence is positive although release mutual information is zero.

Proven. The data-processing proof works for an optimal posterior attacker, or an attacker whose success is at least the optimal prior baseline. This ordering is exactly what the monotonicity step needs. The one-sided Pinsker improvement bound remains valid for arbitrary attackers, since a negative improvement already satisfies it.

Proven. Full adversary knowledge is the strongest interpretation of the bound. The bound also protects weaker adversaries. Such knowledge is not necessary for its validity.

12. `fact-pac-privacy-gaussian-release-bound`

Proven. Theorem 3 gives the covariance upper bound. Theorem 4 gives the bounded-output simulation guarantee through Algorithm 1 and condition (6). The basic entropy argument is correct.

Proven. `ch-gaussian-covariance-domain`, blocking. The displayed inverse requires positive definite noise covariance, and the release covariance requires finite second moments. An arbitrary Gaussian covariance can be singular. The stated expression is then undefined. Add these assumptions or formulate a separate supported-subspace result.

Proven. Algorithm 1 concerns a deterministic mechanism evaluated on independent input draws. One evaluation counts as one training run only when that mechanism is the training procedure. A representation mechanism instead costs a forward evaluation.

Heuristic. This supplies an experimentally meaningful certificate under its boundedness assumptions. It is not an unrestricted certificate for arbitrary stochastic training from drawn-seed calls.

13. `fact-zhao-accuracy-forces-attribute-leakage`

Proven. Accept. Theorem 3.2 and Theorem 3.3 match the displayed statements and the extra premise of the latter. The adversary class contains all measurable binary classifiers. The proof identifies its advantage with total variation, bounds Jensen–Shannon divergence, and applies the triangle and error inequalities. Check Zhao, Chi, Tian and Gordon, NeurIPS 2020, Lemma 3.4 and Appendix B in the [PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/neurips/ZCTG20_TradeOffsGuaranteesAdversarial.pdf).

Proven. The conditional laws require both attribute groups to have positive probability, or an explicitly supplied conditional experiment. This is the implicit domain of the statement.

Heuristic. This is a substantive borrowed accuracy–leakage tradeoff. It gives no lower bound against a restricted attacker class.

14. `def-uniform-security-profile`

Proven. `ch-profile-comparator`, blocking. The comparator and the budgeted adversaries do not have matching interfaces.

Proven. In a query-channel game, an informed adversary may still need Eval calls to observe the challenge. Hard-wiring a test cannot replace those observations. For example, two known models can give opposite answers to one query while their unopened names reveal nothing. A zero-query attacker then has zero advantage, while an informed one-query attacker distinguishes perfectly. The singleton gap is therefore not zero at every budget as claimed.

Proven. The singleton degeneration is correct for the passive bottom-oracle experiment with the complete fixed view supplied for free. It also holds for a query experiment when the informed comparator obeys the same query budget. Those are narrower statements.

Proven. The top oracle creates another mismatch. Its honest-seed grant can increase optimal advantage above the channel-only comparator. The defined “gap” can then be negative. Define the informed optimum separately for each access policy and challenge-query allowance.

Proven. `ch-profile-infinite-budgets`, blocking. Infinite budget, a limit of finite-budget minimax values, and observation of an infinite sample sequence are different objects. The accepted adversaries stop almost surely. The atomless impossibility cited concerns uniform finite-sample rates. It does not establish the asserted conclusion for an unspecified infinite-observation experiment.

Proven. A nonempty feasible set of integer budgets has coordinatewise minimal elements. Feasibility itself need not hold. Moreover, an infimum equal to the requested tolerance does not guarantee an attack attaining that tolerance. The definition must allow an empty price set and distinguish approximate attainability from exact attainment.

Proven. `ch-profile-hsu-transfer`, blocking. HSU25’s requirement is simultaneous control of both conditional success probabilities. A scalar advantage threshold does not impose those two conditions. Its mixture proof can support an appropriate advantage lower bound, but that requires an explicit argument. The theorem statement alone is insufficient. Train access also requires the correction in `ch-hsu-estimator-access`.

Proven. The experiment paragraph needs a direction correction. The maximum true gap over sampled instances is a lower bound on that attack’s full-class worst gap. It provides an upper bound on the minimax gap only for the restricted sampled class, after accounting for estimation error.

Heuristic. Retain a repaired minimax regret profile as supporting notation. It is not itself a non-trivial result. The computational singleton comparison also needs instance families and a bound on advice or description size.

15. `conj-shadow-run-price-finite-views`

Proven. Part 1’s empirical-distribution argument is correct as an expected regret bound, averaging over the shadow samples. It is not a deterministic guarantee for every realized bank. Add this qualification, handle odd call counts, and restrict the accuracy parameter to be positive.

Proven. `ch-shadow-adaptive-seeds`, blocking. The lower-bound construction fails under the accepted bottom oracle.

Proven. In the quantile construction, each pair has the same total probability regardless of its planted sign. Its outer cumulative boundaries are therefore known. Choose the seed coordinate at the midpoint of that pair’s cumulative interval. The returned member of the pair reveals its sign exactly.

Proven. An adversary can first inspect the challenge view, identify its pair, and make this one chosen-seed Train call. It then knows whether the challenge atom is above or below the uniform probability. It implements the optimal likelihood-ratio decision for that challenge. This gives zero regret throughout the proposed planted family using one Train call.

Proven. Even drawn seeds do not justify the stated per-call KL argument when their values can be opened. Neighboring sign instances differ deterministically on seed intervals. The joint observation of seed and output is not an ordinary categorical sample. Independent seed coordinates at the two inputs do not repair this issue.

Open. This refutes the proposed hard family and proof, not the full minimax lower bound over all deterministic learning functions. A replacement construction must hide information from arbitrary chosen seeds, seed reuse, Open calls and challenge-dependent choices. A sufficiently large randomly assigned seed table is a possible approach, but requires its own transcript argument.

Proven. The two-run top-oracle attack attains the top optimum under deterministic kernels. One run at either candidate input already suffices. Compare the replayed view with the challenge and classify a mismatch accordingly. However, this is the top optimum, not the bottom total-variation comparator used at the start of the object.

Proven. The passive statistical rate has established learning-theoretic precedent. Daniely, Sabato, Ben-David and Shalev-Shwartz, JMLR 2015, Theorem 5, states the agnostic rate governed by class dimension and inverse squared excess error. All binary tests on a finite view space have dimension equal to its cardinality. [Primary source](https://jmlr.org/papers/volume16/daniely15a/daniely15a.pdf).

Proven. That theorem does not directly cover the stronger oracle here. Its learning protocol does not allow chosen seeds and fresh training decisions after seeing the test point. A valid reduction must simulate those operations and translate expected regret. Thus the ordinary sample rate is familiar, while the proposed oracle-strengthening remains open.

Heuristic. Keep this as the principal aim. Its potential contribution is the oracle lower bound, not the finite-domain passive rate. The statement about settling the query-tree problem also needs an explicit deterministic-evaluation embedding. Counting possible label vectors alone does not provide it.

16. `conj-reconstruction-label-sandwich`

Proven. The floor argument is sound under ordinary measurable-space assumptions. Choose one near-optimal reconstruction center for each positive-probability label. Compose that finite collection with a near-optimal label predictor. Success can decrease only when the predicted label is wrong. Let both approximation errors tend to zero.

Proven. The ceiling argument is also sound. Conditional independence under the reference law bounds success by the label baseline. Data processing gives the Bernoulli divergence bound for success above that baseline. Passing to the supremum uses continuity or lower semicontinuity. The conditional Gaussian entropy calculation is correct with finite conditional covariances and positive definite noise covariance.

Proven. `ch-sandwich-domain-and-tightness`, blocking. The label-release example need not satisfy the assumed Markov chain. When labels contain randomness beyond the input, releasing the actual label is not a kernel applied only to the input. Restrict that example to deterministic labels, or remove the Markov restriction, which the floor and ceiling proofs do not need.

Proven. Also specify standard Borel observation spaces, measurable success events, and how zero-probability labels are omitted. The logarithmic corollary needs a baseline strictly between zero and one. Endpoint cases require separate statements. With finitely many labels, choosing finitely many near-optimal centers does not require a general measurable-selection theorem.

Proven. `ch-sandwich-decoder-floor`, blocking. The experimental claim is false. An arbitrary trained decoder need not attain the floor for the optimal reconstructor. A constant, badly chosen decoder can fall below it. Every decoder obeys the ceiling. The floor supplies an achievable benchmark only through the constructed label-prediction and class-center decoder.

Open. I found no verified publication of this exact floor in the sources checked. That is not a novelty certificate. Relevant omitted literature includes van Rooyen and Williamson’s 2014 work on deficiency and generic feature learning. It studies decision performance and reconstruction through comparison of experiments. I do not identify it as proving this exact floor. [Primary source](https://arxiv.org/pdf/1402.4884).

Proven. The floor is already an elementary bounded-loss transfer argument. Absence of its exact wording in a paper does not make that argument a substantive new theorem.

Heuristic. `ch-sandwich-experimental-identification`, nonblocking for the inequalities. The claim that every quantity is experimentally estimable needs restrictions. A supremum over all metric balls has no supplied uniform estimation rate. Conditional mutual information is likewise not generally certified by empirical estimation. Finite candidate centers, a controlled ball class and bounded activations would yield concrete surrogate guarantees.

Heuristic. The three proposed aims are appropriate only after narrowing their roles. The profile is supporting notation. The full-interface shadow lower bound is the main theorem candidate. The reconstruction sandwich is a baseline lemma unless strengthened by tightness, an estimable family or a resource-sensitive result.

Proven. The sandwich compares reconstruction success with label-prediction error. It does not show that learning a reconstructor requires the trainer’s sample count, model capacity or training cost.

## Verdicts

```text
VERDICT fact-hsu-membership-sample-gap REVISE
VERDICT fact-hsu-gap-prices-covariance REVISE
VERDICT fact-yeom-dp-bounds-membership-advantage ACCEPT
VERDICT fact-yeom-generalization-error-gives-advantage REVISE
VERDICT fact-lira-priced-in-training-runs REVISE
VERDICT fact-lira-low-fpr-yeom-game REVISE
VERDICT fact-balle-reconstruction-robustness-definition REVISE
VERDICT fact-balle-dp-bounds-reconstruction REVISE
VERDICT fact-reconstruction-query-lower-bounds REVISE
VERDICT fact-dinur-nissim-reconstruction-thresholds REVISE
VERDICT fact-pac-privacy-mutual-information-bound REVISE
VERDICT fact-pac-privacy-gaussian-release-bound REVISE
VERDICT fact-zhao-accuracy-forces-attribute-leakage ACCEPT
VERDICT def-uniform-security-profile REVISE
VERDICT conj-shadow-run-price-finite-views REVISE
VERDICT conj-reconstruction-label-sandwich REVISE
BLOCKING 14
```