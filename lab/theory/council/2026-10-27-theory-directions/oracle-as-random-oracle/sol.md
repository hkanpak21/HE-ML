---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-27
prompt: lab/theory/council/2026-10-27-theory-directions/oracle-as-random-oracle/prompt-critique.md
---

Heuristic. Revise the meditation before adopting its direction. Its strongest idea is the distinction between canaries within one run and independent repetitions of training. Its main error is treating indistinguishability of programmed samples as indistinguishability between defended and undefended procedures.

## Claims

### prop-programming-preserves-prices

Proven. Part (a) holds for fixed programming points, independent honest samples, and no further use of the designer’s copy that changes another party’s view. Part (b) transfers success probabilities when every relevant success test belongs to the admissibility class. Taking the optimum over the same budgeted algorithms then gives the stated bracket between prices at shifted success levels.

Proven. ch-price-success-units (blocking). Parts (c) and (d) confuse an error in success probability with an error in budget. A small change in success can cause an arbitrarily large change in the budget needed to reach a fixed threshold. The contrapositive of (b) concerns distinguishable success probabilities at the same budget. It does not bound a change in price by the same numerical error.

Proven. ch-programming-simulation-cost (blocking). Part (d) omits the reduction’s cost. The distinguisher must simulate the setup, run the party, and check success. A learning function could itself perform expensive range recognition on the generator’s output. A cheap test of the resulting model would then distinguish the setups without giving an equally cheap generator distinguisher. The short-seed theorem correctly includes this overhead. This proposition must do so too.

Proven. ch-programming-defence-reference (blocking). The conclusion that Halil’s rule excludes release noise does not follow. Fix a procedure whose honest release already includes Gaussian noise. Programming its noise oracle with an independent Gaussian sample preserves that procedure’s law. The noisy procedure can still have a different security profile from the procedure without noise. These are different comparisons.

Proven. Indistinguishability alone also cannot exclude a cryptographic plug-in. Part (d), after correcting its cost, demonstrates this. Halil’s exclusion therefore remains a separate restriction on where the claimed hardness comes from.

Heuristic. The surviving content is standard simulation and indistinguishability reasoning, with a useful application to experimental design. It is not a new random-oracle technique. Bellare and Rogaway introduced the underlying methodology at ACM CCS 1993. [Their paper](https://web.cs.ucdavis.edu/~rogaway/papers/ro-abstract.html) supplies the historical reference, rather than a theorem asserting this particular price formulation.

### prop-key-free-defence-rule

Proven. Part (b) holds for a fixed target and a class closed under sampling the channel and then running the defended algorithm. At a fixed computational budget, the simulation must charge the channel’s sampling cost. This is the elementary garbling direction of Blackwell’s comparison of experiments, developed in Annals of Mathematical Statistics, 1953. [Blackwell’s paper](https://doi.org/10.1214/aoms/1177729032) concerns ordering experiments by their decision value.

Proven. ch-key-free-information (blocking). Part (a) is false. A random value having no separate outgoing edge does not mean a party learns nothing about it. A kernel can output its randomness directly. With additive noise, a party that knows the input can recover the noise from the output. Furthermore, two parties receiving the same defended value may possess different side information. The definition constrains neither party’s complete view.

Proven. ch-rounded-law-transfer (blocking). Part (c) does not establish the claimed hardness transfer. Conditional on the chosen direction, exact rounding places records on hyperplanes. A pancake law with positive smoothing has a density. Those conditional laws are mutually singular. Resemblance to layers does not establish the registered hCLWE distribution or its parameters.

Open. A suitable rounded and smoothed construction might support a reduction. This meditation supplies neither that construction nor the required distributional comparison. The hardness clause needs the label Open.

Heuristic. Drop this proposed replacement for Halil’s rule. Its valid part is familiar data processing. Its invalid part identifies absent access to randomness with absent information. Even after repair, it deliberately admits the planting that Halil ruled out.

### prop-canary-audit-unbiased-not-sound

Proven. Part (b) holds when the advantage averages over a uniformly selected canary position, inclusion bits, data, training randomness, and attack randomness. Linearity of expectation suffices. Independence between the canaries’ attack outcomes is unnecessary.

Proven. Part (a) permits estimating the declared attack’s false-positive probability on fresh records without another training run. It does not compute that probability exactly from finitely many fresh draws. The target is conditional on the released model unless the experiment also repeats training.

Proven. ch-canary-collisions (blocking). Part (c)’s numerical values require a missing assumption. Let the record law concentrate on one record already present in the honest dataset. The lookup test always reports membership, independently of each inclusion bit. Both stated advantages are then zero. Assume collision-free records, or define an inclusion target whose identities the learner actually receives.

Proven. Under that repair and a fair hidden seed bit, the mixture argument holds. A run from the always-memorizing learner has the same observed law as the memorizing branch of the mixed learner. A universally sound lower confidence bound on expected advantage must respect that indistinguishability. Independent run averages then support the stated Hoeffding bound.

Proven. ch-canary-target (nonblocking). This does not prohibit sound one-run privacy auditing. Steinke, Nasr and Jagielski, NeurIPS 2023, prove a one-run confidence bound for DP parameters. Their full version gives Theorem 5.2 and Corollary 5.4. Those concern a worst-case privacy guarantee, rather than the expected attack advantage targeted here. [The full paper](https://arxiv.org/pdf/2305.08846) makes that distinction checkable.

Heuristic. Keep the repaired mixture example. It is the meditation’s clearest contribution to deciding what an experiment measures. The inclusion-bit experiment itself already appears in that prior work.

### thm-short-seed-dichotomy

Proven. Part (a) holds under its explicit positive-separation assumption and independent representations from one fixed initial client. In each comparison involving the true seed, sufficiently accurate estimation preserves its victory. Uniform concentration over all comparisons involving that seed handles the tournament’s adaptive path.

Proven. Part (b) is the standard generator hybrid, provided the stated simulation and checking costs are finite and correctly charged. Both parts merit Proven under these hypotheses.

Proven. ch-short-seed-scope (blocking). The subsequent claim that every finite seed destroys statistical seed blindness is false. For isotropic Gaussian records, clients related by an orthogonal transformation can induce identical representation laws. A finite seed selecting between a client and its negation already gives an example. No sample count identifies which seed generated those representations. The theorem explicitly excludes this case through its positive-separation assumption.

Proven. The PRG argument supplies a sufficient transfer condition. It does not prove that pseudorandomness is necessary for every finite implementation. A direct analysis of the finite family can establish security without that assumption.

Proven. ch-seed-computation (nonblocking). The sample bound hides enumeration, density comparisons, and evaluation of comparison sets. Public distributions need not make those operations efficient. This is a statistical identification result, not a practical seed-recovery price.

Heuristic. The identification argument is an application of classical Scheffé comparison and finite-family selection. Devroye and Lugosi, Combinatorial Methods in Density Estimation, Springer, 2001, Chapter 6, provide the relevant reference. [The authors’ contents page](https://luc.devroye.org/webbooktable.html) identifies the two-density and finite-family selection sections. The application is useful, but the claimed dichotomy and implementation-wide conclusions exceed it.

### prop-replay-audit-uninstantiable

Proven. Part (a) holds over the stated class of all learning functions. For each fixed hash, the constructed learner recognizes one hash-derived seed. That seed has zero probability under the atomless honest law, while the replay uses it deliberately. Part (b) also holds when the learning function, training input, and target are fixed before the auditor samples its challenge. Every accepted target model requires a replay near the target, so the reach and union bound suffice.

Proven. The Proven label is correct. These are simple, useful statements about this audit.

Proven. ch-replay-quantifiers (nonblocking). The analogy to Canetti, Goldreich and Halevi needs a qualification. This proposition chooses a learning function after fixing the hash. It does not construct one fixed learning function that defeats every hash implementation. CGH’s stronger cryptographic uninstantiability result appears in STOC 1998, with the journal version in JACM 2004. The opened full version states it as Informal Theorem 1.2. [Their paper](https://arxiv.org/pdf/cs/0010019) establishes the quantifier distinction.

Heuristic. Keep the proposition as a limitation of a universal replay guarantee and as justification for an interactive audit. Calling the audit a Fiat-Shamir audit adds an analogy, without establishing a proof-of-knowledge interpretation or a new Fiat-Shamir impossibility.

### prop-seed-grip-duality

Proven. The fixed-input mixture bound, the comparison of the two fixed-input couplings, and the deterministic atomless example follow from convexity and product bounds for total variation. The coincidence bound also follows because two independent draws from the atomless marginal coincide with probability zero. These arguments require the independent hardware randomness specified by the registered identity coupling.

Proven. The multi-node statement needs an explicit scope. A bound on model kernels does not control views that also reveal the seeds. Nor does a fixed-input calculation by itself establish an adaptive transcript bound.

Proven. ch-grip-equivalence (blocking). The concluding “exactly as far” statement is false. Partition an atomless seed into finitely many equal-probability buckets and let every learning input depend only on its bucket. A finite uniform bucket index reproduces the entire named oracle exactly. Nevertheless, grip approaches one as the bucket count grows. Finite seeds can therefore preserve the oracle while named reuse remains useful.

Proven. ch-grip-measurement (nonblocking). Grip takes a supremum over seeds and uses total variation between model laws. The meditation supplies no finite experiment that certifies either quantity uniformly over arbitrary learning functions. The registered coupling quantities have an experimental realization that this supremum currently lacks.

Heuristic. Keep the inequalities as sufficient bounds. Drop the claim that grip prices seed length or characterizes the value of a seed name. The mathematics is elementary and useful, but it does not establish that equivalence.

### prop-rise-decomposition-replace-one

Proven. Part (a) is correct under independent sampling and correct seed marginals. Replacing a record makes the removed record independent of the replacement-trained model. Averaging its accuracy therefore gives expected test accuracy. This is the standard replace-one identity. Bousquet and Elisseeff, JMLR 2002, Lemma 7, give the corresponding stability identity for symmetric learners. [Their paper](https://jmlr.csail.mit.edu/papers/volume2/bousquet02a/bousquet02a.pdf) supplies the precise comparison.

Proven. ch-reference-repeat-consistency (blocking). The product reference law and the lazily sampled random function are different objects when inputs repeat. Independent labels can disagree at the same input. A random function returns the same label there. With a singleton input space, one observed random-function label predicts every subsequent label perfectly. The claimed marginal baseline is therefore false for that reference. Index labels by occurrences, or require previously unseen inputs.

Proven. Part (b) gives an unbiased one-run observation of the expected generalization gap when held-out data are independent. It does not give concentration around that expectation over training randomness. The canary mixture example already explains why that distinction matters.

Proven. ch-erm-capacity-bound (blocking). Part (c)’s ERM bound is false. Take one training example, an uninformative continuous input, label-one probability 0.9, and the two constant predictors. ERM fits the training label. Expected training accuracy is 1, and expected test accuracy is 0.82. Memorization is therefore 0.18. The proposed capacity is only 0.10. The reference law already equals the original law in this example.

Proven. The separate counterexample for unrestricted learners remains valid as an asymptotic argument. It does not repair the false ERM statement.

Proven. ch-accuracy-versus-leakage (nonblocking). This accuracy decomposition does not decompose privacy leakage. A learner can append its entire training dataset to otherwise unchanged model parameters. Predictions and the proposed memorization score remain unchanged, while white-box disclosure increases.

Heuristic. Keep the replace-one identity as background. Drop the ERM bound and the claim that this identity makes the proposed learning-security frame exact. “From memory” cannot support a Proven label.

### def-known-price

Proven. The bracket follows directly from the measured witness and the universal lower bound, on the confidence event. Matching upper and lower resource bounds is a standard tight-bound criterion. This definition introduces no new hardness result.

Proven. Part (a) follows within the registered theorem’s scope. That scope includes deterministic kernels, accuracy at the specified zero-leakage function, universal soundness, and expected call counts. Part (b) follows when the coupled certificate or finite-view certificate lies below the desired success threshold. Neither statement removes the registered computability assumptions.

Proven. ch-class-certificate-scope (blocking). Part (c), read literally, contradicts part (b). A certificate bounding every attacker also bounds SQ and gradient attackers. What may be missing is a sharper certificate that uses those restrictions. Absence of such a registered certificate also does not imply that prices can be known only on designer-built laws.

Empirical. On the inspected register entries, the cited certificates and lower bounds exist with those restrictions. That is a statement about the records inspected.

Open. A uniformly valid certificate that exploits a particular learner class and improves substantially on the unrestricted bound remains a separate research question.

Heuristic. Retain the definition as bookkeeping. State the instance assumptions, confidence guarantee, budget convention, and approximation factor whenever calling a price known.

## The direction as a whole

Heuristic. The meditation serves Halil’s aim when it distinguishes measurement targets and charges the work needed to realize them. It drifts from his aim when it replaces the requested learning-resource theory with seed enumeration, a proposed defence taxonomy, and familiar identities.

Proven. Reading the seed table as a lazy random function provides deferred sampling and consistent reuse. Together with the permitted training calls, it organizes coupled experiments. The replay theorem additionally uses fresh oracle outputs to bound grinding. None of these facts alone yields a new computational price for a shadow model, VAE, or gradient attacker.

Proven. Programming can admit honest-distribution canaries and honest release-noise samples. The comparison must preserve the law of the procedure being audited. It need not preserve the law of a different procedure without those features. The same indistinguishability criterion cannot by itself exclude a cryptographic plug-in.

Heuristic. Retain Halil’s separate restriction on the source of hardness. Require an explicit mapping to the learning task, rather than replacing that restriction with the proposed key-free rule.

Heuristic. An experiment should state the following targets separately.

| Party | Experimental target | What the experiment establishes |
| --- | --- | --- |
| Trainer | Population performance of a declared learner at a stated resource budget | A confidence interval for that learner. An upper bound on the class requires a theorem. |
| Attacker | Success on the stated secret and side information, against the stated independent reference | A lower bound on the class’s attainable success, with fresh shadow training when that randomness enters the target. |
| Auditor | A specified leakage functional, or a specified DP parameter | A confidence bound for that functional. Independent training repetitions and within-run canaries support different guarantees. |

Proven. A generic attacker baseline is not automatically free of training. That conclusion requires a known secret sampler and a success test evaluable without another training run. The canary false-positive experiment supplies one such case.

Heuristic. The strongest next direction is a theorem connecting a declared attack’s learning budget to an experimentally accessible channel quantity, with the reduction’s simulation cost included. The repaired canary obstruction can determine its repetition requirement. The short-seed identification result can test a separate identifiability assumption. Neither should replace the learning-resource question.

Open. The meditation supplies no new matching resource bounds for a trainer and an attacker class. That remains the result needed to move beyond language.

## Verdicts

```text
VERDICT prop-programming-preserves-prices REVISE
VERDICT prop-key-free-defence-rule REJECT
VERDICT prop-canary-audit-unbiased-not-sound REVISE
VERDICT thm-short-seed-dichotomy REVISE
VERDICT prop-replay-audit-uninstantiable ACCEPT
VERDICT prop-seed-grip-duality REVISE
VERDICT prop-rise-decomposition-replace-one REVISE
VERDICT def-known-price REVISE
BLOCKING 11
```