---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-27
prompt: lab/theory/council/2026-10-27-theory-directions/pseudorandomness-for-learner-classes/prompt-critique.md
---

Heuristic. Retain this direction, but revise its definition and six of its seven claims. The strongest idea is the equality of loss-matched population oracles. The Gaussian trajectory bound supplies a second useful result. Neither establishes the proposed three-party theory or an exact computational price for finite-batch learning.

## Claims

### def-class-pseudorandom-channel

Proven. Part (a) holds as a finite-transcript statement. Atomless, independent inputs almost surely never repeat, so cached random-function answers have the stated product law. The proof is complete.

Proven. The single-party notion has substantial prior art. For binary outcomes and a fixed instance, the constant marginal predictor gives the corresponding outcome-indistinguishability experiment. Dwork, Kim, Reingold, Rothblum and Yona, STOC 2021, give the relevant single-sample and multiple-sample definitions in Definitions 2.2 and 2.7. General outcomes appear in their ALT 2022 paper. These correspondences require matching the access model and quantifiers. [Outcome Indistinguishability](https://www.cs.cornell.edu/~mpkim/pubs/OI.pdf), [Beyond Bernoulli](https://proceedings.mlr.press/v167/dwork22a/dwork22a.pdf).

Proven. ch-oracle-experiment blocks. A joint law alone does not specify chosen-input access, Train access or an SQ answer strategy. Repeated chosen inputs require a decision between cached answers and fresh randomness. SQ access requires quantification over valid answers. Train access requires specifying which instance and seed persist between calls. The displayed advantage is therefore undefined for several advertised access modes.

Proven. ch-secret-index blocks the security interpretation. Separate the hidden instance from the random secret within an instance. Otherwise, take the instance itself as the secret and let the view reveal it exactly. Conditional on each instance, both variables are constant, so their joint law equals the product reference. The definition then reports perfect pseudorandomness despite complete disclosure.

Proven. ch-degenerate-gap blocks part (b) as a non-trivial one-way notion. An accurate release followed by a constant view channel satisfies the proposed conditions. A constant attacker target also qualifies as a function of the trainer’s target. Require non-trivial improvement over a stated baseline, an explicit attacker success criterion, and a fixed view interface tied to the service being studied.

Heuristic. Keep the single-party definition as notation. Part (b) needs a complete experiment before “proven” describes anything beyond its stipulation.

### prop-distinguishing-versus-weak-learning

Proven. Part (a) holds in the bounded-loss SQ model, provided the learning guarantee covers the oracle responses used in the experiment. The extra loss query separates the successful learner’s risk from every null risk.

Proven. The argument in part (b) establishes the intended exponential-tilt construction after granting exact access to null expectations. The null transcript must contain a query that is invalid for the alternative. The selected query then has sufficient true gap. The tilt parameter can be chosen from the tolerance alone, so the proof need not know the exact gap.

Proven. Parts (c) and the real-label counterexample in (d) hold. Expanding square loss gives the covariance statement. The independent sign makes the conditional mean zero while preserving information about the hidden direction in the conditional second moment.

Proven. ch-loss-equivalence blocks the claimed unrestricted equivalence. Binary labels make general statistics reducible to correlational statistics when the marginals agree. They do not equate arbitrary losses, nor preserve an arbitrary learner class through the reduction. A constant loss admits no improvement even for fully predictable binary labels. An exponential tilt can also leave the original predictive family.

Proven. The budget statement needs the cost of null integration and construction of the conditional predictor. “Known marginals” does not automatically supply a free exact expectation oracle. This omission matters when the budget measures computation rather than alternative-distribution SQ calls.

Proven. Part (e) is the V-information definition under its predictive-family and integrability conditions. Xu, Zhao, Song, Stewart and Ermon, ICLR 2020, Definitions 1–3, require optional ignorance and define the unconditional baseline within the predictive family. [A Theory of Usable Information](https://arxiv.org/html/2002.10689).

Heuristic. Retain the proposition as explicit reductions between named access and output classes. Its covariance calculation and tilt argument are elementary. The V-information component is borrowed. “Proven” does not support the current class-independent equivalence.

### prop-class-pseudorandomness-collapse

Proven. The total-variation identity in part (a) holds for the fixed-hidden-instance sample experiment. The secret must remain fixed across the samples.

Proven. ch-density-hypothesis blocks the second-moment formula as written. Its likelihood ratios require absolute continuity relative to the product null. A deterministic continuous-label law can be singular relative to that null. State the density hypotheses, allowing an infinite bound when appropriate, or separate the identity from the density-based inequality.

Proven. Part (b) identifies an SQ decision problem after fixing oracle semantics and success quantifiers. Feldman, Grigorescu, Reyzin, Vempala and Xiao, J. ACM 2017, Theorems 3.7 and 3.13, supply the cited statistical-dimension and simulation tools. Statistical dimension provides bounds. It does not automatically equal the optimal advantage at every budget.

Proven. ch-moment-experiment blocks part (c) as a characterization of the displayed prior-averaged advantage. Consider binary halfspace labels with the direction chosen equally between two opposite directions. Each conditional law has generative exponent 1. Averaging one labeled example over that prior gives exactly the product law. Every one-sample test then has zero advantage, including tests above degree 1.

Proven. A pointwise statement about vanishing population moments is valid. It follows from the generative-exponent definition. An exact SQ experiment that nonlinearly processes moment answers is another possible interpretation. Neither interpretation is specified by the current statement. The proof also selects a polynomial using the hidden direction without explaining the resulting algorithm.

Heuristic. Replace “collapse” by precise correspondences for separate experiments. The second-moment argument and Hermite characterization are standard tools, not new invariants. The SQ versus low-degree correspondence must retain the hypotheses recorded for Brennan, Bresler, Hopkins, Li and Schramm, COLT 2021.

### thm-bayes-release-loss-matched-price

Proven. The population identity is correct whenever the relevant expectations and gradients exist. The data and the Bayes release have the same input law and conditional mean. Consequently, they answer the same correlational expectations. Their square-loss risks differ by a predictor-independent constant.

Proven. Coupling initialization and injected noise therefore couples population-gradient trajectories exactly. Within this oracle model, part (c) follows. Part (d) also holds for independent conditional resampling of binary answers.

Proven. ch-gradient-domain blocks part (b) under its stated assumptions. The two integrability conditions do not ensure finite square risks or defined population gradients. For example, add a trainable constant to an integrable function with infinite second moment, and use zero labels. Both listed integrability conditions hold, but the population loss is infinite everywhere. Require finite risks and hypotheses that justify the gradient calculation.

Proven. The closing finite-batch assertion is false. Batch-update laws can differ through higher moments even when their means and covariances agree. Second moments determine covariance, not the complete transition kernel.

Heuristic. This is the meditation’s strongest idea. It gives a simple boundary on possible extraction separations. Preserve its population-oracle scope. It does not establish equal sample, wall-clock or Train-call prices.

Open. Its novelty as a packaged extraction theorem remains unverified. The underlying conditional-expectation identity is elementary. The proof supplies no reason to identify it with an omniprediction theorem.

### prop-extraction-gap-information-exponent

Proven. Part (a) holds, with an explicit convention for an empty minimum. The label itself is one permissible transformation in the generative exponent’s variational characterization. Replacing the label by its conditional mean plus independent centered noise preserves its linear Hermite coefficients.

Proven. Part (c)’s exact coefficient calculation holds. The three lower coefficients vanish, and the displayed fourth coefficient is correct. The generative exponent 4 of the released link is already recorded in `lem-level-set-moment-balance`. Its prior-art basis is Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, Example 2.7(ii) and Corollary 2.8. Their Proposition 2.6 supplies the variational characterization underlying part (a). [Generative exponent results](https://arxiv.org/html/2403.05529).

Open. ch-exponent-price does not block the structural inequalities. It does block treating the argument as an established exact SQ price. The [registered extraction theorem](/Users/a90/Documents/RESEARCH/HE-ML/lab/theory/spaces/hard-problem-mappings/round-02/builder.md) gives an SQ lower bound and a sample-based upper bound. Their matching dimension exponents do not supply a matching SQ estimation upper bound. DPLB24, Remark 3.3, expressly leaves room for an SQ detection versus estimation gap. The general sample upper bound also retains its linear-dimensional term. [Remark 3.3](https://arxiv.org/html/2403.05529).

Proven. Part (d)’s conclusion needs narrower wording. The seed-separation theorem specifies no trainer learning objective. It therefore supplies no established trainer-target linkage of the proposed kind. That does not prove that every supervised instantiation violates the condition.

Heuristic. Retain this as an explanation of which label statistics the Bayes release removes. The exponent inequalities are known consequences, and the example comes from the existing construction. “Proven” is appropriate for those statements. An exact ratio of computational prices remains open.

### thm-noisy-gradient-query-filter

Proven. Parts (a) and (b) hold for positive injected-noise variance, well-defined update means, and initialization independent of the hidden instance. The reverse KL chain rule evaluates every discrepancy along the null trajectory. That trajectory is independent of the hidden instance. Averaging over the prior, then applying Pinsker and Jensen, gives the stated constant. Data processing covers every reader of the trajectory.

Proven. Part (c) holds for nonempty parity sets. Binary-label decomposition and vector-valued Parseval give the stated bound. The ReLU interpolation computes parity with the claimed hidden-layer width.

Proven. Part (d) follows from the descent lemma and the constant predictor’s common risk. Its proof holds.

Proven. The ingredients have direct prior art. Shalev-Shwartz, Shamir and Shammah, ICML 2017, Theorem 1, bound gradient variance over orthogonal target families. Abbe and Sandon, NeurIPS 2020, Definition 4 and Theorem 3, compare descent under true and random labels through null-trajectory quantities and cross-predictability. [Failures of Gradient-Based Deep Learning](https://proceedings.mlr.press/v70/shalev-shwartz17a/shalev-shwartz17a.pdf), [On the Universality of Deep Learning](https://proceedings.neurips.cc/paper/2020/file/e7e8f8e5982b3298c8addedf6811d500-Paper.pdf).

Open. The exact formulation’s novelty requires comparison with those results. It is nevertheless a useful, non-trivial statement for this project. Its “proven” label is justified.

Heuristic. ch-gradient-measurement does not block the theorem. It concerns its experimental use. The supremum over all parameters cannot be upper-certified by evaluating finitely many parameter values alone. The proof’s accumulated discrepancy along null trajectories offers a more direct measurement target. Any finite-batch implementation needs an additional approximation bound and an explicit sample cost.

### prop-equivariant-learner-orbit-prior

Proven. The orbit-risk identity holds under the stated equivariance and invariance assumptions. The proof correctly transports both the data and predictor. A lower bound on optimal prior-averaged risk then bounds every such equivariant learner at every point of the orbit.

Proven. ch-orbit-bayes-optimality blocks the asserted Bayes-risk identification. A fixed learner’s integrated risk need not be Bayes-optimal. Take the trivial group and a learner that ignores informative labels. Its orbit average equals its own risk and can strictly exceed Bayes risk. The invocation of Hunt and Stein does not establish optimality of an arbitrary learner.

Proven. ch-equivariance-scope blocks the unrestricted gradient-descent application. Isotropic initialization alone is insufficient. The model class and update must admit the required group action. Li, Zhang and Arora, ICLR 2021, Theorem C.1 and Corollary C.2, establish the application for fully connected models under those conditions. They do not cover every fixed architecture. [Equivariance theorem](https://arxiv.org/html/2010.08515).

Proven. Haar randomization of a finite-dimensional orbit is not a random-function reference. Equivariance does not create independent labels or remove the family’s learnable structure.

Heuristic. Retain the orbit identity as a standard decision-theoretic reduction. Correct its Bayes terminology, remove the unsupported optimality assertion, and state the architecture assumptions. Its “proven” label then applies.

## The meditation as a whole

Heuristic. The direction serves Halil’s aim when it compares concrete learning experiments in common resource units. It drifts when it requires every security target to be determined by the trainer’s prediction target, excludes the auditor, and treats population-query exponents as practical prices. Those restrictions narrow the requested theory without a result that requires them.

Proven. The single-party definition is non-vacuous once its experiment is fixed. Restricted classes can fail to detect dependence. Its present three-party extension still admits trivial examples. Neither extraction nor seed separation establishes an ordinary one-way function, and the meditation gives no reduction from either construction to one-wayness.

Heuristic. Keep the Bayes-release identity and the Gaussian trajectory argument. Together they isolate a useful question. Which parts of the actual training transition law differ between the data and release experiments, and what do those differences cost the attacker?

Heuristic. Drop the unqualified learning-one-way-function name, the general learnability equivalence, the canonical-reference assertion, and the claim that the auditor cannot share the framework. An auditor can be a learner with an estimation target. Its certification requirements and oracle-identifiability limits need their own price theorem.

Proven. ch-programming-admissibility does not block the stated population identities. It limits their use as admissible designer modifications. Preserving a marginal law does not preserve an adaptive joint transcript. Oracle programming must remain indistinguishable to each party with its stated auxiliary information. Replacing the original labels by noisy Bayes predictions does not itself meet that condition.

Open. ch-minibatch-threshold does not block the accepted population theorem. The “Next” covariance computation is correct, but its recovery thresholds remain conjectural. Covariance alone proves neither threshold for the actual adaptive, non-Gaussian updates. The claim needs a specified prior or minimax quantifier, recovery modulo sign, and upper and lower bounds for the full transition laws. AKMSS21’s adversarial-rounding precision cannot be identified with Gaussian injected noise from the proposed scaling analogy alone.

Heuristic. The most useful next result would connect an experimentally estimable discrepancy of actual update laws to attacker success, with matching resource accounting. That would address Halil’s request to measure a shadow learner or VAE before declaring hardness.

## Verdicts

```text
VERDICT def-class-pseudorandom-channel REVISE
VERDICT prop-distinguishing-versus-weak-learning REVISE
VERDICT prop-class-pseudorandomness-collapse REVISE
VERDICT thm-bayes-release-loss-matched-price REVISE
VERDICT prop-extraction-gap-information-exponent REVISE
VERDICT thm-noisy-gradient-query-filter ACCEPT
VERDICT prop-equivariant-learner-orbit-prior REVISE
BLOCKING 9
```