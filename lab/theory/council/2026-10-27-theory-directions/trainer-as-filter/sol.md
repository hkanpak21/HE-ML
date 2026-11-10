---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-27
prompt: lab/theory/council/2026-10-27-theory-directions/trainer-as-filter/prompt-critique.md
---

Heuristic. Retain the noisy trainer comparison as the mathematical core. The meditation gives useful statistical bounds, but it does not yet price attacks on memorizing trainers in Halil’s units of learning. Four challenges block statements or interpretations in the text.

## Claims

### def-random-oracle-record-split

Proven. Parts (a), (b) and (c) hold under the stated independence assumptions. The trainer must access the individual randomness only through the records. “Same risk” means population risk under the fixed data law.

Proven. Part (a) is a known representation theorem. The precise references are Kallenberg, Foundations of Modern Probability, Springer, second edition, 2002, Theorem 6.3 on conditional distributions and Lemma 3.22 on kernel randomization. Parts (b) and (c) follow from conditional independence and resampling. These are elementary consequences, rather than new learning results. [Kallenberg’s book](https://link.springer.com/book/10.1007/978-1-4757-4015-8).

Proven. The resampling construction can depend on the unknown population law. It therefore does not provide one implementable trainer that preserves risk across the population family.

Heuristic. ch-population-part-operational, nonblocking. The statistic needs an operational justification. Taking it to be the entire record makes the defined memorization zero even when the trainer publishes its entire dataset. Calling the statistic “population” does not establish that it contains precisely the learnable structure.

Proven. The status label is correct. The random oracle adds a sampling representation, without adding a hardness property.

### prop-canary-is-programmed-record

Proven. Part (a) holds for a fixed, previously unqueried index, with a fresh uniform value independent of the existing transcript. Recording that value requires comparing against an honest experiment in which the auditor receives the corresponding oracle value. Reprogramming an already observed value need not preserve the joint law.

Proven. ch-programming-view-law, blocking. Part (b) confuses a conditional law of the record with the law of an observable view. Suppose a party’s view is constant. Changing a hidden uniform bit into a fixed bit changes its conditional law given that view. The party’s view still has the same law, so its distinguishing advantage remains zero.

Proven. The repair is to compare complete observable view laws. If the party also observes the record, compare the joint law containing that record. A difference in an unobserved conditional distribution does not suffice.

Proven. Part (c) holds for a permutation ranking with specified tie handling. Its exposure definition is Carlini, Liu, Erlingsson, Kos and Song, USENIX Security 2019, Definition 4, expressed in nats instead of bits. The list interpretation is immediate. [The Secret Sharer](https://www.usenix.org/system/files/sec19-carlini.pdf).

Proven. Random, unobserved dataset size alone does not make adding a canary admissible. The resulting observable law must still match the honest law.

Proven. The proposition needs revision before its overall “proven” label is justified. The valid components are standard lazy sampling and the existing exposure definition.

### lem-exposure-information-sandwich

Proven. The four inequalities hold. Part (a) uses binary data processing. Part (b) compares the posterior with the harmonic distribution over ranks. Part (c) uses convexity and a valid same-seed coupling. Part (d) uses independence, the chain rule and convexity. The rearranged bound in part (a) needs a list size strictly below the candidate count.

Proven. The coupling must preserve every other input and have the correct conditional marginal law for each canary value. Its randomness must include all training randomness relevant to the comparison.

Proven. The status label is correct. These are useful information inequalities assembled around an existing exposure measure. The proofs do not establish a new principle of computational memorization.

Proven. ch-exposure-measurement, nonblocking. The inequalities concern expectations over experiments. One observed exposure is neither the expected exposure nor a confidence bound on memorization. Part (c) bounds exposure and list success from a coupled tail. It does not state an upper bound on mutual information.

Proven. Steinke, Nasr and Jagielski, NeurIPS 2023, Theorem 5.2 and Corollary 5.4, address dependent guesses from one training run. Their result tests a DP hypothesis using randomized inclusion. It does not directly estimate this lemma’s unrestricted expected list success. [Privacy Auditing with One Training Run](https://arxiv.org/pdf/2305.08846).

### thm-null-trajectory-filter

Proven. Both formal statements hold with data-independent initialization, update maps and batch schedule. Conditioning on the coins fixes the reference trajectory and all batches. Hoeffding applies separately at each reference point. Reuse creates dependence between those events, which the union bound permits. The proposed defending rule is common to the null and alternative experiments.

Proven. Part (b) gives the stated average total variation bound. It does not assert independence on the exceptional event.

Proven. ch-rounding-quantifier, blocking for the meditation’s interpretation. The conclusion that “memorization cannot be stated” is false. The theorem constructs one defending rounding. Other valid roundings can memorize. A constant gradient halfway between adjacent grid points admits two valid roundings. A rule allowed to inspect the sample can choose between them using a sample bit.

Proven. The exceptional event also prevents replacing approximate sample independence with zero mutual information. A rare event can release a record with arbitrarily large information content.

Proven. The formal theorem deserves ACCEPT. Its status label is correct. The extension to arbitrary fixed reuse goes beyond the fresh-batch statement cited from Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, Theorem 1c. Broader novelty remains unverified. [On the Power of Differentiable Learning](https://arxiv.org/abs/2108.04190).

### thm-noisy-trainer-two-term-filter

Proven. Part (a) holds for the random-population testing experiment. The reverse KL comparison follows the null trajectory, which remains independent of the dataset under arbitrary fixed reuse. Convexity, Pinsker and the triangle inequality give the printed conservative bound.

Proven. Parts (b) and (c) hold under each fixed population law. A randomized batch schedule requires conditioning on the schedule, or averaging its participation counts. The released trajectory must exclude the hidden Gaussian noise values.

Proven. ch-information-conditioning, blocking. The information experiment is not explicit. Under the random-population experiment used in part (a), records are conditionally independent given the population secret. They are generally dependent after that secret is integrated out. The tensorization step in part (b) then fails.

Proven. A counterexample draws a shared uniform sign and makes every record equal to it. One full-batch gradient releases that sign plus fixed Gaussian noise. The output retains fixed positive information about the dataset, while the claimed information budget tends to zero as the dataset grows. Conditioning on the population secret removes this contradiction.

Proven. The repair is to state the sample-information bounds conditional on the population law, separately from the population distinguishing bound.

Proven. Parts (b) and (c) use standard Gaussian divergence accounting and adaptive composition. Mironov, IEEE CSF 2017, Propositions 7 and 1, give the relevant Gaussian divergence and composition results. [Rényi Differential Privacy](https://arxiv.org/pdf/1702.07476).

Proven. The null trajectory technique also has prior art in Abbe and Sandon, arXiv, 2020, Theorem 3 and Section 5.1, through their “junk flow” comparison. [Poly-time Universality and Limitations of Deep Learning](https://arxiv.org/abs/2001.02992).

Heuristic. The fixed-sample reuse argument and the resulting population comparison are the meditation’s strongest synthesis. The trajectory budget remains an upper bound on information. It is not a measured memorization value or an attacker’s computational price.

### prop-hashed-memory-breaks-sq-filter

Proven. The construction and proof hold. Collision control, Gaussian tails and row-norm separation allow recovery of the records. The recovered linear system distinguishes the parity population from the null. The stated parameter orders follow.

Proven. The status label is correct. One step suffices, so repeated passes are unnecessary for this counterexample.

Heuristic. This is a useful explicit witness that the population term alone cannot control a trainer that stores records. Its contribution is the concrete noisy gradient construction. The broader fact that sufficiently expressive gradient training can exceed SQ learning is already present in Abbe et al., NeurIPS 2021, Theorem 1a.

Proven. The construction establishes failure at its stated trajectory budget. It does not identify the smallest budget at which failure occurs, or establish that the budget equals actual memorization.

Heuristic. Keep planted parity here as a diagnostic example. Making it the principal next target would move the project toward the planted hardness programme Halil’s latest framing rejects.

### prop-output-bounds-do-not-filter

Proven. Parts (a) and (b) hold. The sensitivity and Laplace arguments are correct. The null concentration error and the two noise-tail errors together give the stated advantage. The SQ bound retains its defending-oracle quantifier.

Proven. ch-output-impossibility, blocking. Part (c) does not follow. A successful test released as one bit shows that one bit can carry the relevant answer. It does not show that every quantitative output-information bound fails to constrain testing.

Proven. In a joint experiment with a random hypothesis, sufficiently small information between the dataset and output constrains information about that hypothesis by data processing. Group privacy also constrains population comparisons when the accumulated privacy loss across the dataset is small.

Proven. The supported conclusion is narrower. Bounded output entropy and central DP do not imply SQ access restrictions or inherit arbitrary SQ lower bounds.

Proven. The central versus local separation is known. Kasiviswanathan, Lee, Nissim, Raskhodnikova and Smith, FOCS 2008, give private parity learning in Theorem 4.4, local and SQ equivalence in Theorem 5.14, and their separation in Corollary 5.15. Those numbers refer to the held full version. [Held full version](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/focs/KLNRS08_WhatCanWeLearn.pdf).

Proven. The overall “proven” label requires replacing part (c). The one-bit example also does not refute the phrase “what the trainer did not learn stays hidden”. That trainer computed and released the tested property.

## The direction as a whole

Heuristic. The direction partly serves Halil’s aim. It connects steps, batch size, clipping and noise to statistical attack bounds. It does not yet connect an attacker’s success to its samples, shadow training runs or computation. Unbounded readers remove the attacker’s learning problem from the theorem.

Proven. The strongest idea is the comparison along a trajectory independent of the dataset. Its value is specific. It handles fixed-sample reuse without proving uniform concentration along the actual adaptive trajectory. The claim that the device itself is new should be dropped because the Abbe and Sandon comparison already uses this structure.

Proven. ch-residual-side-information, nonblocking for the individual inequalities. Per-record memorization does not control joint residual leakage. Release the XOR of two independent random bits. Each bit individually has zero information about the release, while the release reveals their relation. An attacker who knows either bit recovers the other.

Heuristic. A composition theorem for memorizing trainers therefore needs a stated target and stated auxiliary information. Joint residual information or conditional record information may serve those targets. Steinke and Zakynthinou, COLT 2020, Definition 1, provide a related operational membership experiment using a supersample and random selectors. Their object is not identical to the proposed record split. [Conditional Mutual Information](https://proceedings.mlr.press/v125/steinke20a/steinke20a.pdf).

Proven. ch-admissible-modifications, nonblocking for the mathematical bounds. The uniform canary programming can preserve an honest law. Adding Gaussian noise to previously noiseless training, or selecting a population-dependent defending rounding, generally changes that law. Halil’s programming permission requires an indistinguishability argument for those modifications. Defining a noisy trainer as the baseline is a separate modelling choice.

Heuristic. Drop the assertions that both filters describe regimes “real training avoids” and that only the proposed memorization quantity remains measurable. The meditation supplies no experiments supporting either statement. The existence of a measurable information quantity also does not supply a feasible estimator.

Proven. The account of the refuted FORMAL_SECURITY reduction needs correction. Its registered counterexample identifies the defending-oracle quantifier and the use of an empirical graph law. Comparing along an adaptive trajectory is not the complete diagnosis.

Open. The proposed information-budget parity conjecture remains unsettled by this meditation.

Proven. ch-information-not-space, nonblocking for an explicitly open conjecture. Raz’s FOCS 2016 Theorem 2 bounds branching-program width and length. A mutual-information bound does not imply a width bound. Reusing a dataset also changes the streaming access model. The conjecture requires an additional argument connecting these objects. [Fast Learning Requires Good Memory](https://arxiv.org/abs/1602.05161).

Heuristic. The next result should join the two surviving components. It should bound a stated attack on residual information, allow a fixed honest trainer to memorize, and give an experiment with a finite confidence guarantee. That would address Halil’s question about measurable attacks on learning procedures.

## Verdicts

```text
VERDICT def-random-oracle-record-split ACCEPT
VERDICT prop-canary-is-programmed-record REVISE
VERDICT lem-exposure-information-sandwich ACCEPT
VERDICT thm-null-trajectory-filter ACCEPT
VERDICT thm-noisy-trainer-two-term-filter REVISE
VERDICT prop-hashed-memory-breaks-sq-filter ACCEPT
VERDICT prop-output-bounds-do-not-filter REVISE
BLOCKING 4
```