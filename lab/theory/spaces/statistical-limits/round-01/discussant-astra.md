---
model: gpt-6-astra
discussant: astra
date: 2026-10-25
prompt: lab/theory/spaces/statistical-limits/round-01/prompt-astra.md
---

Proven. The main lower-bound argument survives adaptive Train calls, chosen seeds, seed reuse, Open, and calls at other inputs for the specific hard families constructed here. Its constants are correct. Three statement-level challenges remain blocking: the urn lemma’s comparison hypotheses, the profile’s unrestricted channel claim, and the label-only clause’s policy-independent optimum.

Proven. The reconstruction sandwich is correct under the revised assumptions. Its remaining proof clarifications do not require stronger hypotheses. Open. Neither its unrestricted information quantities nor the novelty of the complete oracle theorem have been experimentally or bibliographically settled.

1. `fact-hsu-membership-sample-gap`

Proven. The revised estimator class now matches Haghifam, Smith and Ullman, arXiv 2025, Definition 3.2. Factoring through the empirical mean is stronger than permutation invariance. The stated probability and Mahalanobis requirement match that definition.

Proven. The mixture argument supports the additional advantage statement. Average signed advantage over the population prior is bounded by the mixture total variation. Consequently, some population gives advantage at most 0.02. This closes `ch-profile-hsu-transfer` when Train access is absent.

Proven. `ch-hsu-estimator-access` closes for the positive noise scale of Definition 2.4. A caller subtracts the known empirical mean from each returned estimate to obtain a noise sample. The covariance-dependent noise prevents simulation from the estimator’s formula alone.

Proven. Restore the positive noise-scale domain explicitly. At zero noise, the estimator is the empirical mean and its execution requires no population covariance. The source’s Definition 2.4 already supplies the positive domain, so this is a transcription clarification rather than a new blocker.

Heuristic. This is substantive borrowed sample-complexity evidence. It does not establish a Train-call lower bound. Check the [held PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/focs/HSU25_SampleComplexityMembershipInference.pdf), Definitions 2.1–2.4, Theorems 3.1 and 3.3, and §3.2.4.

2. `fact-hsu-gap-prices-covariance`

Proven. The revised statement distinguishes the necessary sample order from Remark 4.2’s sufficient order. `ch-hsu-covariance-order` closes. The comparison requires dimension comparable to the stated threshold, with suitable absolute constants.

Proven. Theorem 4.1 assumes a positive noise scale, at least four training samples, and at least two auxiliary samples. The matching attack remains an attribution to Dwork et al., FOCS 2015, rather than a proof supplied by HSU25.

Heuristic. Describing the difference as the price of unknown covariance is appropriate within these Gaussian experiments. It is not a general characterization of auxiliary-sample complexity.

3. `fact-yeom-dp-bounds-membership-advantage`

Proven. Accept unchanged. Yeom, Giacomelli, Fredrikson and Jha, CSF 2018, Experiment 1, Definition 4 and Theorem 1 support the statement with replacement adjacency and the specified membership experiment.

Proven. The conditional replacement argument and subsequent averaging establish the bound for unbounded adversaries. It supplies a privacy baseline, not a training-resource price.

4. `fact-yeom-generalization-error-gives-advantage`

Proven. `ch-yeom-cost-and-normalization` closes. The nonnegative bounded loss, positive normalization constant, randomized output convention, and one-evaluation cost are now correct.

Proven. Yeom et al., CSF 2018, Theorem 2 proves the displayed equality by subtracting the attack’s two expected outputs. The statement concerns the exhibited attack. No additional optimality claim follows.

5. `fact-lira-priced-in-training-runs`

Empirical. The counts and comparisons remain scoped to Carlini et al., IEEE S&P 2022, §V-A, §VI-B, Figure 9 and §VI-D. They describe measured attack performance.

Proven. `ch-lira-parametric-necessity` closes. The revised text no longer asserts that Gaussian fitting is necessary for every finite training-run price.

Heuristic. The Gaussian restriction helps explain LiRA’s estimation procedure. The measured counts do not establish proximity to the unrestricted optimum, nor explain quantitatively how far the benchmarks lie below the worst-case theorem.

6. `fact-lira-low-fpr-yeom-game`

Proven. `ch-lira-out-exclusion` closes. The OUT exclusion and reversed bit convention are now explicit. Equality with Yeom’s game follows when the exclusion event has probability one.

Proven. On atomic populations, that equivalence can fail. The conditional OUT experiment also requires the exclusion event to have positive probability. This is a domain qualification on the borrowed definition.

7. `fact-balle-reconstruction-robustness-definition`

Proven. `ch-balle-prior-knowledge` closes. Balle, Cherubin and Hayes, IEEE S&P 2022, Definition 2 allows knowledge of the prior and the remaining dataset. The realized target remains unknown.

Proven. Averaging over independent attack randomness shows that randomization does not increase the supremum. This does not require attainment by a posterior maximizer.

Heuristic. The definition is useful statistical background. It places no learning-resource requirement on the reconstructor.

8. `fact-balle-dp-bounds-reconstruction`

Proven. `ch-balle-radius-hypotheses` closes. The Rényi order, fixed-radius conditions, Gaussian scale condition, and zero–one-loss domain now match the source.

Proven. Theorem 2 uses change of measure and Hölder’s inequality. Corollaries 3 and 4 specialize and optimize that bound. Theorem 5 supplies the converse through two-point priors. These are distinct directions and should remain distinct.

Proven. The revised statement about a certificate for two fixed inputs is appropriately restricted. Such a certificate does not supply a uniform privacy guarantee over arbitrary neighboring inputs.

Heuristic. These are substantive borrowed reconstruction bounds. Their use requires the relevant privacy parameter and prior baseline. Check the [BCH22 PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/ieee-sp/BCH22_ReconstructingTrainingDataInformed.pdf), §VII and its appendix proofs.

9. `fact-reconstruction-query-lower-bounds`

Proven. Theorem 9 remains supported by the two-point reduction, the product-overlap bound, and the DP bound on total variation. The compact metric domain and independent released models are essential.

Proven. `ch-reconstruction-query-tightness` closes for the unrestricted matching claim. The first attack in Appendix B.5 uses the unknown target. Appendix B.3 also contains the stated invalid direction of the total-variation inequality. Those arguments do not establish the unrestricted claims.

Proven. `ch-reconstruction-majority-omission`, nonblocking. The revised literature account misses the later “Tightness of Majority Adversary” passage in Appendix B.5. Mukherjee and Lokam, arXiv 2024, give an unnumbered theorem there for privacy parameter at least 0.042. A majority rule with a fixed tie convention is target-independent. Conditioning on the absence of an explicit disclosure reduces its error analysis to a binomial tail.

Proven. That restricted result does not repair the claimed uniform small-privacy-parameter rate. It does mean that “Theorem 10 is not established” should distinguish the unrestricted theorem from the restricted majority result. Check pages 26–27 of the [held PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/arxiv/ML24_QueryComplexityTrainingData.pdf).

10. `fact-dinur-nissim-reconstruction-thresholds`

Proven. `ch-dinur-resource-comparison` closes. The revised text correctly separates the information budgets of Theorems 2 and 3.

Proven. Dinur and Nissim, PODS 2003, Definition 4 lets the first machine query and then select the target index. The second machine receives the transcript and every other database bit. Theorem 5 assumes a positive privacy slack. Restore that domain explicitly.

Heuristic. These results provide resource-sensitive reconstruction background. Their comparison does not isolate computational hardness at fixed information.

11. `fact-pac-privacy-mutual-information-bound`

Proven. `ch-pac-suboptimal-adversaries` closes. The restriction to attacks at least as successful as optimal prior guessing makes the Bernoulli-divergence monotonicity argument valid. The one-sided improvement bound applies to every attack.

Proven. This is a corrected consequence of Xiao and Devadas, CRYPTO 2023, Theorem 1 and Corollary 1. Remark 1 supports conditioning on side knowledge. The source’s theorem wording should not replace the corrected monotonicity argument.

Proven. Knowledge of the data law describes the strongest adversary considered. It is not necessary for the upper bound to protect a weaker adversary.

12. `fact-pac-privacy-gaussian-release-bound`

Proven. `ch-gaussian-covariance-domain` closes. Positive definite noise covariance and finite second moments make the inverse, determinant and entropy argument valid.

Proven. The bounded-output hypothesis is separately necessary for the stated simulation guarantee of Theorem 4. Finite second moments alone do not provide that guarantee.

Proven. The source also treats randomized mechanisms in §4.2, including Corollary 2. The present fact is a valid deterministic specialization. It should not imply that XD23 contains no randomized extension. Check the [XD23 PDF](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/crypto/XD23_PACPrivacyAutomaticPrivacy.pdf), Theorems 3 and 4 and §4.2.

13. `fact-zhao-accuracy-forces-attribute-leakage`

Proven. Accept. The positive-probability group condition repairs the conditional-law domain. Zhao, Chi, Tian and Gordon, NeurIPS 2020, Theorems 3.2 and 3.3 support the carried statements.

Proven. The proof uses the unrestricted measurable binary attacker class, identifies its advantage with total variation, and then applies the Jensen–Shannon and prediction-error inequalities. It does not supply a lower bound for a restricted learning algorithm.

14. `fact-balle-reconnn-priced-in-shadow-runs`

Empirical. The reported training counts and MSE ranges match BCH22, §VI-B, Figure 5 and Table III. The larger pool of shadow pairs is also reported.

Proven. `ch-reconnn-seed-interpretation`, nonblocking. “Needs the initialization” must remain a statement about this attack and these experiments. Failure of the tested reconstructor does not establish statistical impossibility without initialization.

Heuristic. The connection to top-oracle access is useful. Initialization knowledge is only part of full seed knowledge when training also uses shuffling or other randomness. The distinguishing theorem does not directly price this reconstruction experiment.

15. `def-uniform-security-profile`

Proven. The revised minimax definition, attained price, approximate price and threshold price are well posed for measurable adversaries. Monotonicity follows from inclusion of budget classes. Dickson’s lemma gives finitely many minimal budgets. Empty feasible sets are now handled.

Proven. `ch-profile-infinite-budgets` closes. The definition uses finite budgets and makes only a limit claim for finite views. `ch-profile-hsu-transfer` also closes through the mixture argument discussed above.

Proven. `ch-profile-comparator` remains blocking as written. The definition now matches interfaces, but Property 1 again identifies the optimum for an arbitrary channel interface with the total variation of the complete released value.

Proven. Consider two deterministic tables that differ at one query. Give the served name zero Eval allowance. Their complete table laws have total variation one. Every permitted attack has advantage zero, even if it knows the instance.

Proven. Restrict the displayed total-variation and seed-conditioned formulas to a complete plain-channel observation. For a query interface, use the optimum over permitted query strategies. The citation to the coupling certificate does not remove the query restriction.

Proven. Singleton regret can still be zero as an infimum without an attained optimal strategy. An informed adversary can approximate the interface-constrained supremum and internally simulate instance-known auxiliary calls. Thus the unrestricted claim of attainment also needs narrowing.

Heuristic. This remains supporting notation. A worst-case regret over an unrestricted class is not directly identified by a finite collection of experiments.

16. `lem-scrambled-seed-urn`

Proven. The urn argument is sound for a fixed law and for the theorem’s particular family. Chosen numerical seed values do not expose the random cell assignment. Reusing a previously queried cell returns its stored label. A new cell exposes one label sampled without replacement.

Proven. `ch-urn-common-nuisance`, blocking. The KL comparison needs every response mechanism outside the distinguished input to be identical under the two compared laws. The statement assumes only independence from the permutation.

Proven. For a counterexample, take two distinct, full-support rational laws on two labels. At another input, return one fixed model under the first law and a different fixed model under the second. Both responses are independent of the permutation. One Train call at that input produces mutually singular transcripts, although the KL divergence between the two label laws is finite.

Proven. Add a common seed law, common evaluation mechanism, common model injection, and identical conditional response kernels away from new cells at the distinguished input. The theorem’s construction already satisfies these conditions.

Proven. `ch-urn-filtration`, nonblocking. The proof should condition on an augmented history containing every drawn seed value, even before Open reveals it. Open can reveal a numerical seed that the adversary previously held only by name. It does not necessarily return a value already known.

Proven. Conditional on this augmented history, all seed choices select measurable cell indices. The unseen permutation assignments remain exchangeable. Conditioning only on observed labels does not reveal the actual unused permutation images, but averaging over those hidden images gives exactly the stated remaining-count distribution.

Proven. The measurability concern is therefore removable. The label distributions have finite support. Their common masses and residual masses define measurable maximal couplings. Histories with zero probability can receive arbitrary kernels. Almost-sure termination allows passage from finite transcript prefixes to the stopped transcript.

Proven. An alternative is the standard adaptive permutation-versus-random-function coupling, followed by the fixed labelling map. It gives an even sharper collision bound. This is the same statistical device underlying the PRP/PRF switching lemma. Bellare and Rogaway, EUROCRYPT 2006, discuss it in their [game-playing treatment](https://web.cs.ucdavis.edu/~rogaway/papers/games.html).

Proven. No computational pseudorandomness assumption is required here. The construction uses a genuinely random finite table, so the prohibited cryptographic plug-in is absent.

17. `thm-shadow-run-price-finite-views`

Proven. The substantive repair of `ch-shadow-adaptive-seeds` succeeds for the constructed family. The remaining statement repairs below do not revive the round-00 chosen-quantile-seed attack.

Part (a).

Proven. Both set-probability inequalities are correct. Empirical maximization supplies the middle comparison. Jensen’s inequality and Cauchy–Schwarz give the stated expected deviation bound. Drawn-seed calls supply independent samples, including under deterministic kernels.

Proven. `ch-shadow-small-budgets`, nonblocking. Require at least two Train calls for this algorithm and formula. With fewer calls, the empirical laws are undefined. State a separate trivial bound for those budgets.

Part (b), Step 1.

Proven. Interpret the independent randomness as primitive random tapes, not as the realized answers to adaptive calls. Realized answers can depend on the challenge.

Proven. For a fixed learning function, draw the adversary’s coins and all auxiliary seed, hardware and evaluation tapes independently of the honest randomness. Executing the adversary against an externally supplied challenge value then defines the claimed randomized decision rule.

Proven. Calls before the challenge are included in this execution. Calls after the challenge may depend on it. Chosen seed values and reused seed names are measurable functions of the accumulated history. None of these operations invalidates the reduction.

Proven. Under the top policy, the same reduction applies to the hardware-random family because the honest seed is independent of the challenge output. Include that seed among the auxiliary primitive variables.

Part (b), Step 2.

Proven. The construction isolates dependence on the sign vector to fresh hardware draws at the first candidate input. The other candidate input and every additional input have common response kernels.

Proven. Open and Eval on previously returned models are common conditional postprocessing. Chosen or reused seeds cannot influence fresh hardware randomness. The total variation and gap identities are correct.

Part (b), Step 3.

Proven. The two executions are auxiliary experiments with externally fixed challenge values. They are not obtained by conditioning a mixed prior on an observed challenge.

Proven. Their output difference has the required expectation. Each execution uses at most the stated Train budget, so the pair uses at most twice that budget. Adaptivity changes which common kernel runs next, but only calls at the first candidate input contribute conditional KL.

Proven. The one-call KL calculation, logarithm bound, Pinsker constant and factor two for a statistic valued between minus one and one are all correct. Calls at other inputs contribute zero conditional KL.

Part (b), Step 4.

Proven. Pairing neighboring sign vectors gives the stated average regret. Both choices of perturbation size satisfy the required range. The threshold between the two cases and the constants 1/8 and 1/32 are correct.

Open. `ch-shadow-policy-quantifiers`, nonblocking clarification. The proof establishes the bound separately for each policy. “The same function has the same gap” should mean equality under an explicit simulation of top access by independent auxiliary randomness in this family. It should not suggest that two independently chosen, policy-specific attacks necessarily have equal regret on one common hard instance.

Part (c).

Proven. For each fixed permutation, the honest view law is unchanged. This is the crucial property. Under the permutation prior, observing a challenge atom therefore does not reweight the permutation prior.

Proven. Consequently, the forced-challenge mixtures used by the lemma have exactly the output probabilities required by the averaged decision-rule identity. Pre-challenge calls do not create an omitted conditioning term.

Proven. Independent permutations in the two auxiliary executions are legitimate. Only the difference of their marginal output expectations is needed. The proof does not require a joint execution sharing one hidden permutation.

Proven. Each pair experiment incurs twice the one-run approximation error. Comparing the two neighboring pair experiments incurs that error on both sides. The resulting additive total-variation term is the one displayed.

Proven. Multiplication by the regret prefactor leaves ample slack in the stated choice of grid size. Rational approximation of the perturbation can consume the reserved half of the tolerance. The constants in (c) are sufficient.

Proven. The lemma’s missing common-kernel hypothesis is satisfied here. With that hypothesis stated and the filtration clarified, this is a proof rather than an unresolved measurability sketch.

Part (d).

Proven. One Train call suffices. Under the first hypothesis, replay at the honest seed produces the challenge view exactly. Under the second, the test outputs one precisely on seedwise disagreement.

Proven. Conditional on the honest seed, both view laws are point masses. Their total variation is the disagreement indicator. Averaging gives the top optimum. No second replay is needed.

Proven. The conclusion requires deterministic kernels and the deterministic channel stated here. Fresh hardware randomness would invalidate the equality test.

Part (e).

Proven. The inversion of the lower bound gives the stated denominator 1024. For deterministic kernels, take the arbitrary approximation tolerance to zero after fixing the allegedly uniformly successful adversary and its budget. The hard instance may depend on that tolerance.

Proven. The upper-bound call count follows from part (a). The guarantee concerns expected regret. It is not a confidence guarantee for every realized shadow bank.

Part (f).

Proven. Reading all query points reveals the table. Under the bottom policy, the table total variation is exactly the optimum. The deterministic evaluation embedding and the extension by constant values outside the selected points are valid.

Proven. `ch-label-policy-optimum`, blocking. The statement identifies the “label-only optimum” with marginal table total variation while also importing the top-policy clauses. That identification is false under the top policy.

Proven. Take two binary table coordinates. Under the first input, output two fair seed bits. Under the second, complement both bits. The marginal table laws are identical, so their total variation is zero. At every fixed seed, the two tables differ. Top access and one replay distinguish perfectly.

Proven. State the marginal-table optimum for the bottom policy. For the top policy, use the optimum for the joint observation of seed and table.

Proven. For the larger query set, distinguish its cardinality from the number of queries allowed. The displayed tree count compares bounds at query budget q. If the actual allowance is larger, the corresponding upper bound must use that allowance.

Proven. The logarithmic factor is a comparison between the available upper and lower bounds at matching accuracy and confidence conventions. It is not a lower bound proving that the logarithmic factor is necessary.

Prior work and significance.

Proven. The passive finite-domain rate is classical. Daniely, Sabato, Ben-David and Shalev-Shwartz, JMLR 2015, Theorem 5 gives the agnostic dimension-dependent rate. It does not cover the stronger seed interface. [Primary source](https://jmlr.org/papers/volume16/daniely15a/daniely15a.pdf).

Proven. The adaptive scrambling step has direct methodological precedent in permutation-versus-random-function switching. Its application here does not require a cryptographic hardness assumption.

Open. I do not know a publication proving this complete training-oracle theorem with these interfaces and quantifiers. The targeted checks establish those precedents, not novelty of the combined result.

Heuristic. The deterministic bottom/top separation is the substantive contribution candidate. Its finite table construction and finite-view divergences admit experiments. It remains a worst-case theorem for opaque learning functions, not a lower bound for a particular neural training procedure.

18. `prop-reconstruction-label-sandwich`

Proven. The revised statement is correct. `ch-sandwich-domain-and-tightness` and `ch-sandwich-decoder-floor` close.

Proven. The standard Borel assumptions provide regular conditional laws. The metric and decoder measurability make every success event measurable. Finitely many positive-probability labels permit selection of finitely many approximate centers without a measurable-selection theorem.

Proven. The floor follows from deleting the head-error event. A finite-label Bayes classifier exists by selecting a posterior maximizer with a fixed tie rule. If a head outputs a zero-probability label, assign that label an arbitrary center.

Proven. The reference measure in the ceiling proof has the asserted conditional mutual information as its KL divergence from the true law. Under that reference measure, the decoder’s success is bounded by the averaged class baseline. Indicator data processing and Bernoulli-divergence monotonicity then give the ceiling.

Proven. `ch-sandwich-endpoint-details`, nonblocking. If the optimum equals the baseline, its Bernoulli divergence is zero directly. An approximating sequence need not approach from above. If the optimum strictly exceeds the baseline, a sufficiently late part of the sequence does lie above it. This supplies the missing distinction in the limit argument.

Proven. Pinsker’s constant and the logarithmic corollary are correct. The latter also holds below the baseline by the elementary scalar inequality used in the proof.

Proven. The Gaussian entropy calculation is valid. Convolution with nondegenerate Gaussian noise gives a bounded density, which bounds entropy below. Finite conditional covariance bounds entropy above. Thus the entropy subtraction involves finite terms.

Proven. Both tightness examples hold. For the injective Borel map, Lusin–Souslin gives a Borel image and Borel inverse. Extend the inverse by an arbitrary fixed point outside its image to obtain a decoder on the whole observation space.

Proven. `ch-sandwich-experimental-identification` is resolved as a limitation, not as an estimation theorem. Independent evaluation samples give the finite-center Hoeffding guarantee. The unrestricted ball supremum and conditional mutual information still lack the claimed general experimental certification. Finite second moments alone also give no stated uniform covariance-estimation rate.

Heuristic. Accept this as an elementary statistical baseline. The interpretation should say that residual information controls improvement above the class baseline. Improvement above the lower floor can also reflect elimination of head error. The proposition establishes no sample, capacity or training-cost requirement for learning a reconstructor.

## Verdicts

```text
VERDICT fact-hsu-membership-sample-gap ACCEPT
VERDICT fact-hsu-gap-prices-covariance ACCEPT
VERDICT fact-yeom-dp-bounds-membership-advantage ACCEPT
VERDICT fact-yeom-generalization-error-gives-advantage ACCEPT
VERDICT fact-lira-priced-in-training-runs ACCEPT
VERDICT fact-lira-low-fpr-yeom-game ACCEPT
VERDICT fact-balle-reconstruction-robustness-definition ACCEPT
VERDICT fact-balle-dp-bounds-reconstruction ACCEPT
VERDICT fact-reconstruction-query-lower-bounds REVISE
VERDICT fact-dinur-nissim-reconstruction-thresholds ACCEPT
VERDICT fact-pac-privacy-mutual-information-bound ACCEPT
VERDICT fact-pac-privacy-gaussian-release-bound ACCEPT
VERDICT fact-zhao-accuracy-forces-attribute-leakage ACCEPT
VERDICT fact-balle-reconnn-priced-in-shadow-runs ACCEPT
VERDICT def-uniform-security-profile REVISE
VERDICT lem-scrambled-seed-urn REVISE
VERDICT thm-shadow-run-price-finite-views REVISE
VERDICT prop-reconstruction-label-sandwich ACCEPT
BLOCKING 3
```