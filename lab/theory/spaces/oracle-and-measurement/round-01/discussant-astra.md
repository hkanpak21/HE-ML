---
model: gpt-6-astra
discussant: astra
date: 2026-10-25
prompt: lab/theory/spaces/oracle-and-measurement/round-01/prompt-astra.md
---

Proven. Round 01 does not close with zero blocking challenges. The coupling argument and the limit and Jensen steps survive review. The symmetric lower bound for one-sided hockey-stick leakage is false. Six further challenges concern the stated measurement protocol, resource accounting, and qualifications on borrowed facts.

The following table checks the twelve original blocking challenges. “Closed” concerns the original objection, not acceptance of the whole revised object.

| Challenge | Disposition |
|---|---|
| `ch-gdp-audit-pld-and-threshold` | Closed. The revision separates threshold selection from evaluation and distinguishes Gaussian composition from subsampled PLD accounting. |
| `ch-finite-seed-not-top-oracle` | Partly closed. Enumeration alone no longer implies top access. Exact recovery and approximate seed identification remain conflated. |
| `ch-known-covariance-dimension-bound` | Partly closed. Theorem 4.1 now has its dimension condition. The subsequent two-sample conclusion drops its dependence on noise. |
| `ch-rerun-spread-threshold-mismatch` | Closed. The observations are means with spreads, and the tail interpretation is labelled heuristic. |
| `ch-subset-forging-below-one-run` | Partly closed. The cost formula is restored, but “less than one” still needs parameter restrictions. |
| `ch-generic-oracle-open-and-meter` | Closed for return labels, operation budgets, and handle numbering. Exact equivalence of the resource meters remains unsupported. |
| `ch-coupling-soundness-target-and-noise` | Closed. The target is now release divergence, and the twin randomness is independent of release noise. |
| `ch-meter-oracle-cost-not-compute` | Partly closed. The oracle-cost distinction is correct. Division by a possibly zero infimum remains undefined. |
| `ch-paired-price-degenerate-test` | Closed by withdrawal. |
| `ch-profile-band-conditional-advantage` | Closed for averaging over fresh shadow randomness. The revised trial cost needs an additional preprocessing restriction. |
| `ch-exact-twin-missing-hypotheses` | Closed. The accuracy range, distinct inputs, injectivity, non-strict accuracy event, and unrounded expectation are supplied. |
| `ch-exact-twin-target-coupling-contradiction` | Closed for the distinction between coupled tails and release leakage. A separate directional error remains in the release-leakage lower bound. |

`fact-gdp-audit-observation-count`

Empirical. The observation counts and black-box measurements agree with the [NHSBTJCT23 note](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/usenix-security/NHSBTJCT23.md), particularly §4.1, Figure 3, and §6.4, Figure 11.

Proven. The revised confidence qualification is correct for a fixed test evaluated on independent observations. Heuristic. The end-to-end conversion still assumes the relevant composition model is tight. The paper supplies measurements and an auditing method, not a theorem establishing those end-to-end lower bounds without that assumption. This is useful measurement evidence, not a new result of this space.

`fact-small-seed-space-breaks-dp`

Empirical. Nasr et al., USENIX Security 2023, §6.3, Violation 2, support the reported detection experiment.

Proven. `ch-seed-enumeration-conditions`, blocking. The “Other regime” paragraph needs two qualifications.

First, enumerating seeds gives exact marginal laws only when the remaining conditional randomness can also be integrated exactly. Finite seed support alone does not remove hardware randomness, batching randomness outside that seed, or channel randomness.

Second, exact reconstruction of the top observation requires one decoder of the seed from the view that works under both hypotheses. Injectivity separately within each hypothesis does not suffice. Argon’s shifted-seed example already demonstrates this failure. Nearly disjoint conditional laws give approximate recovery, with a decoding-error term, rather than exact realization.

Heuristic. Separation of the hundred noise vectors explains detectability in that experiment. It does not establish either exact-law enumeration or exact top-oracle equivalence.

`fact-hsu-membership-sample-gap`

Proven. The statements of Theorems 3.1, 3.3, and 4.1 agree with the held v1 and the [HSU25 note](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/focs/HSU25.md). Theorem 3.3 supplies a matching order at the critical dimension, rather than a dimension-independent matching upper bound throughout the whole range.

Proven. `ch-known-covariance-noise-range`, blocking. The conclusion that two auxiliary samples suffice once the dimension is of order the squared training-set size omits a noise restriction. Theorem 4.1 permits arbitrary positive noise scale. Its matching regime retains the noise-dependent squared-sample term even when the auxiliary sample count is two. For growing noise scale, dimension proportional to the squared training-set size can still lie inside the impossibility region.

State the complete dimension condition, or explicitly restrict the noise scale to a bounded range. Attribute the matching known-covariance attack to Dwork, Smith, Steinke, Ullman and Vadhan, FOCS 2015, as Haghifam, Smith and Ullman do. The held paper states that attribution rather than proving that attack anew.

Proven. This fact prices auxiliary samples. It does not price training runs when the attacker knows the estimator and has unrestricted computation.

`fact-rerun-reproduction-error`

Empirical. The reproduction measurements match Jia et al., IEEE S&P 2021, Table I, as recorded in the [JYCDTCP21 note](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/ieee-sp/JYCDTCP21.md).

Proven. Their Theorem 1 concerns entropy of the training trajectory under their additive noise model. It does not by itself prove a tail bound for the distance between final models.

Heuristic. The revised spread interpretation is acceptable under its stated concentration assumption. The one-step interpretation additionally requires a threshold above the one-step reproduction scale. No measured tail probability should be inferred from Table I alone. This object is relevant empirical evidence about fidelity.

`fact-unlearning-verification-fragile`

Proven. The algorithm descriptions and cost formula agree with Zhang, Chen, Shen and Li, ICML 2024, Propositions 4.2, 4.4, and 4.5. Proposition 4.4 requires the assumptions inherited from Proposition 4.3, vanilla SGD for the replay update, and the specified step-size restrictions.

Proven. `ch-forging-strict-cost`, blocking. The claim that Algorithm 2 costs strictly less than one run is not true throughout the stated parameter domain. With one process and batch size one, the displayed factor equals one. State the formula as the general result and identify the parameter regime giving strict savings.

Proven. The factor involving parallel processes measures time under the paper’s parallel execution model. It must not silently become a reduction in total computational work. The [ZCSL24 note](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/icml/ZCSL24.md) and Proposition 4.5 support the time comparison.

`fact-controlled-nondeterminism-exact-replication`

Empirical. Srivastava, Arora and Boneh, NeurIPS 2024, §6, Figure 4, and Table 5 support the replication and timing claims for the tested models and GPU types.

Heuristic. Its interpretation as an oracle realization requires the deployed learning function to include the modified precision, rounding, and randomness implementation. It does not establish fidelity to an unchanged training pipeline. Appendix I also requires controlled pseudorandom generation, including the dropout implementation.

Empirical. Cross-architecture replay consumes the trainer’s rounding log. That log depends on the particular training execution. The experiment does not show that the base run’s log can be reused for a different dataset. The [SAB24 note](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/neurips/SAB24.md) correctly distinguishes replay from leave-one-out behavior. Accepted within that scope.

`def-seed-access-modes` and `prop-drawn-mode-is-fs-oracle`

Proven. The new labels and operation budgets repair the access mismatch. The passive transcript simulation is correct call by call. Fresh randomness produces a trace, opening returns that trace, and the restricted recipe and initialization choices prevent the stated interface-level laundering.

Proven. The generic-oracle operation translation also works after fixing the architecture, learner, initialization, query maps, and utility class to those of the source definition. In particular, utility is a restriction on admissible learning functions that must accompany the interface translation.

Proven. `ch-meter-domain-and-equivalence`, blocking. There are two accounting defects.

The definition permits zero costs and positive costs with infimum zero. Its displayed division therefore needs a strictly positive infimum. Alternatively, state the multiplicative inequality, which remains defined and becomes vacuous when the infimum vanishes.

The passive source’s `def:cost` accounts for computational work together with corpus size. The proposed scalar meter records only work. Thus the proposition’s assertion of equality with the source meter needs an explicit identification or an additional resource coordinate. Equality of transcript laws does not prove equality of resource accounting.

Proven. These objects organize interfaces and accounting. They are not independent lower bounds under the non-triviality criterion of `CONTEXT.md`. The concluding statement that every theorem needing named mode “fails” for drawn mode should mean that it is inapplicable as stated. Failure of a hypothesis does not prove the conclusion false.

`thm-coupling-free-soundness`

Proven. Part (a) follows from mixture convexity. Conditioning on the revealed seed gives the top-oracle version. A shared seed and correct conditional hardware marginals suffice. Independence of the hardware coupling from the seed is a sufficient special case.

Proven. The five steps of part (b) hold for the stated, independently sampled twin rules.

1. Each selected chain receives the correct marginal randomness. The within-round dependence between the two chains does not change either deployed execution.
2. The hybrid uses the two coordinates of the same twin draw. Its recursion remains measurable.
3. Before the first exceedance, clipping leaves the release unchanged. The executions consequently have identical choices, states, releases, and stopping decisions.
4. Condition on the kernel’s past, its auxiliary randomness, and the current twin draw. Under the shifted Gaussian input, the newly constructed release noise has the required centered isotropic Gaussian law. This conditional law does not depend on either chain state. It is therefore legitimate to discard the auxiliary chain and induct on the deployed chain’s marginal law.
5. Data processing and the divergence splits finish the argument.

Proven. Step 4 does not require independence between the two coordinates of the twin rule. Under top access, the same kernel must additionally output the seed that belongs to the deployed chain. Sharing that seed makes the two required output laws compatible. Argon’s counterexample establishes that arbitrary nonshared seeds cannot support the general top-oracle claim.

Proven. For the reverse inequality, repeat the construction with the first coordinate driving the hypothesis-one execution. A general twin rule need not be exchangeable. Likewise, any retained sum-of-tails formulation must use the conditional tail induced by that twin rule, rather than the original identity-coupled tail.

Proven. Part (c) follows from independent repetitions and the cited concentration bounds, retaining the original computability assumption for channel divergence. The assertions about the identity-coupled target should express absence of a general guarantee under another coupling, rather than uniqueness of the identity coupling at every particular learner.

Heuristic. Arbitrary correct-marginal couplings are not automatically experimentally available through the defined Train interface. The theorem appropriately assumes that the experimenter can sample the chosen coupling. The independent rule and the original shared-seed rule have explicit implementations.

Proven. This is a useful extension of the existing composition argument. It introduces no cryptographic assumption and retains an experimentally estimable exceedance term.

`prop-profile-run-coordinate`

Proven. Part (a) is correct under the accepted theory’s convention that an unrestricted adversary may hard-wire the fixed learning function.

The simulation must maintain a private table of virtual model and seed names. It preserves named-seed reuse, samples fresh hardware randomness on each virtual Train call, and translates later Open and Eval operations. When a virtual open model enters a procedure choice, the simulator supplies its value. Actual query-channel handles remain actual handles and retain their allowances.

Proven. The access rule prevents an opaque query-channel model from becoming a starting model for an adversarial Train call. This is the essential reason the simulator has every training input it needs. A virtual counter also preserves the names the simulated adversary expects despite the missing real calls.

Proven. For a measurable learning function with no effective implementation, this remains a statement in the theory’s unrestricted measurable-strategy model. It is not an efficient executable simulation. With no query channel, the Neyman–Pearson argument establishes the claimed total variation value.

Proven. `ch-profile-adaptive-shadow-cost`, blocking. Part (b) defines a declared family using arbitrary adversaries with a given Train count. It does not require those calls to occur before the challenge. The trial description nevertheless draws one shadow bank before running the two hypotheses and charges that bank once.

An adversary can choose its shadow-training input from the observed challenge. The two hypotheses can then require different training inputs. One precomputed bank need not implement either marginal attack correctly. Running both attacks separately generally charges both shadow pipelines.

Restrict the family to a challenge-independent preprocessing phase followed by a test, or evaluate two complete executions and count their calls separately. Shared random coins alone do not make different training inputs one oracle call.

Proven. Subject to correct trial marginals and independence across trials, the mean identity, Hoeffding step, union bound, and monotone lower band are correct. Part (c) follows from the cited coupling certificate and impossibility result.

Proven. `ch-paired-discordance-baseline`, blocking. The paired-trial remark incorrectly implies that seed sharing necessarily reduces variance. Consider two fair binary outputs that are complements under a shared seed. Their difference has variance one. Independent fair outputs give variance one half.

The variance bound by discordance is correct. A reduction relative to independent sampling needs a suitable covariance condition. Moreover, the stated independent-discordance expression assumes equal acceptance probabilities in the two worlds. In general, the baseline must use both probabilities.

Proven. This proposition is mainly a clarification of quantifier order and experimental design. Its concentration argument is standard. It does not establish a computational training-run price.

`thm-exact-twin-price`

Proven. For the coupled-tail target, the lower-bound proof is valid with one minor measure-theoretic completion. The isomorphism in F9 holds modulo null sets. Leave the reference learner unchanged on the exceptional set, since a caller may deliberately submit a seed there.

Proven. The remaining steps hold in the stated order.

1. Every alternative changes only one training input on a measurable union of cells.
2. Until a queried seed hits that union, the entire adaptive transcript agrees with the reference transcript.
3. Repeated visits cannot increase the number of distinct visited cells. The hypergeometric avoidance expression therefore gives the claimed lower bound.
4. If the expected call count is finite, the count is finite almost surely. The reference execution has one fixed law as the partition is refined. The integrands lie between zero and one, so dominated convergence applies.
5. Conditioning on the low-output event is legitimate because its probability is positive. The exponential function of the count is convex. Jensen therefore has exactly the direction used in the builder.
6. Taking logarithms reverses the inequality when dividing by the negative logarithm. The resulting lower bound, its monotonicity in the event probability, and the limit in the perturbation mass are correct.

Proven. For total variation, the release-leakage extension also works at either input. The common mixture component cancels. A probability law on finite-dimensional Euclidean space and its sufficiently distant translate have total variation approaching one. No moment bound is needed. Finitely many subsets at each partition size permit one shift large enough for all alternatives.

Proven. For the stated one-sided hockey-stick target, perturbing input one also works. The moving half-space captures the shifted mass while its probability under the unperturbed release tends to zero.

Proven. `ch-one-sided-twin-asymmetry`, blocking. Perturbing input zero does not give the same conclusion. The proof’s symmetry step is invalid for one-sided hockey-stick divergence. This makes the base-input lower bounds in both parts (a) and (b) false.

Here is a uniformly sound counterexample within the stated oracle model.

Take privacy parameter 1, soundness level 0.05, accuracy tolerance 0.01, and accuracy failure probability zero. Let the reference learner return the zero model at both inputs.

The certifier draws and opens four models at input zero and 368 models at input one. It outputs 0.01 if every model is zero, and one otherwise.

Proven. To verify soundness, consider the probabilities that each input returns exactly the zero model. If the input-zero probability is at least the reciprocal of Euler’s number and the input-one probability is at least 0.99, the common zero-centered Gaussian component covers the latter’s mass after multiplication by Euler’s number. At most 0.01 of the input-one release remains uncovered.

If the input-zero probability is smaller, observing four zeros there has probability below 0.01832. If the input-one probability is smaller, observing 368 zeros there has probability below 0.02477. Thus the low-output event has probability below 0.05 whenever the target exceeds 0.01.

Proven. At the reference learner, the certifier always outputs 0.01 and uses exactly four base calls. The claimed lower bound requires more than 298 base calls. This disproves the statement, not merely its proof.

Proven. The coupled-tail upper bound is correct. Randomly outputting one handles the permitted accuracy failure, and the remaining branch uses the correct adjusted confidence level. The release-leakage upper bound is also correct after choosing the Gaussian allowance for the actual target and clipping the reported upper bound at one. For total variation, use privacy parameter zero in that allowance.

Proven. The every-record upper bound needs no union bound. A fixed record attaining the largest true tail witnesses every undercoverage event of the maximum reported bound. Shared base runs do not invalidate the per-record binomial coverage.

Proven. The lower bounds for coupled tails and total variation survive. The one-sided leakage lower bound survives for calls at the perturbed numerator input. The symmetric base-call assertion must be removed or replaced by a directional bound.

Heuristic. The surviving result meets this space’s non-triviality criterion as an oracle certification lower bound. Its force comes from uniform soundness over unrelated training inputs. It establishes no unconditional machine-compute lower bound.

Regarding prior work:

Proven. The Gaussian simulation and composition ingredients are established testing machinery. Dong, Roth and Su, JRSS B 2022, give the comparison-of-experiments formulation and adaptive Gaussian composition. In the opened arXiv version, the relevant pointers are Theorem 2.10, Theorem 3.2, and Corollary 3.3. These support the ingredients, not the complete experimentally measured twin-tail statement. [Gaussian Differential Privacy](https://arxiv.org/pdf/1905.02383).

Proven. The profile flatness argument is an application of simulation and data processing under fixed known transition laws. It should not be presented as a new auditing lower bound. Haghifam, Smith and Ullman’s setup already permits an attacker that knows the estimator, while charging unknown-population samples.

Proven. The exact-twin lower bound uses familiar sequential-testing structure. Kaufmann, Cappé and Garivier, JMLR 2016, Lemma 1, relates expected sampling counts to discrimination through change of measure. Its stated mutual absolute-continuity hypothesis prevents direct substitution of the builder’s singular rare-event construction. The finite-partition argument is still needed for adaptive explicit seed queries. [On the Complexity of Best-Arm Identification](https://jmlr.org/papers/volume17/kaufman16a/kaufman16a.pdf).

Proven. Gilbert and McMillan’s privacy-testing lower bounds concern sample access. Theorems 10 and 12 provide relevant impossibility and finite-domain context, but do not establish the named-seed, exact-input lower bound here. [Property Testing for Differential Privacy](https://arxiv.org/pdf/1806.06427).

Open. I found no verified source proving the complete arbitrary-coupling composition statement or the surviving exact-twin theorem with adaptive named seeds. The existing search records are partial. They do not justify an unqualified novelty claim.

## Verdicts

```text
VERDICT fact-gdp-audit-observation-count ACCEPT
VERDICT fact-small-seed-space-breaks-dp REVISE
VERDICT fact-hsu-membership-sample-gap REVISE
VERDICT fact-rerun-reproduction-error ACCEPT
VERDICT fact-unlearning-verification-fragile REVISE
VERDICT fact-controlled-nondeterminism-exact-replication ACCEPT
VERDICT def-seed-access-modes REVISE
VERDICT prop-drawn-mode-is-fs-oracle REVISE
VERDICT thm-coupling-free-soundness ACCEPT
VERDICT prop-profile-run-coordinate REVISE
VERDICT thm-exact-twin-price REVISE
BLOCKING 7
```