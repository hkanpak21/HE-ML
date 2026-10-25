# Summary of round 00 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25. Discussant: astra
(`discussant-astra.md`). The round fell back from argon to astra. The argon call
of this round, run through `tools/discuss.sh` with `prompt-argon.md`, produced no
output, because headless Antigravity denied the `read_file` permission it needed.
The script logged that call in `lab/theory/discussants.csv` with exit 0, since it
tests the exit code of `agy` before the empty output. No `discussant-argon.md`
exists for this round, and the row for it records a failed call.

## What changed

The round read eight library papers (HSU25, CCNSTT22, YGFJ18, BCH22, ML24, DN03,
XD23, ZCTG20), filled their notes, and stated thirteen fact objects, five gaps and
three aims. The discussant opened every PDF. It accepted two facts and asked for
revision of the other eleven and of the three aims, with fourteen blocking
challenges.

Three findings change the space's plan. First, the Assouad construction of
`conj-shadow-run-price-finite-views` fails, because a caller may pass a seed value
to Train and may open the seeds it holds. With deterministic kernels the seed and
the model together reveal the planted signs, and one chosen-seed call gives zero
regret on the proposed family (proven by the discussant, `ch-shadow-adaptive-seeds`).
The replacement must scramble the map from seeds to models. Second, the claim that
HSU25's attacker can simulate training runs is false, because the estimator's noise
has the unknown population covariance (proven by the discussant,
`ch-hsu-estimator-access`). Under the learning oracle, Train calls on any dataset
sample that noise and so leak the covariance, so the sample price of HSU25 Theorem
3.1 does not transfer to an attacker with Train access (heuristic, round 01 states
it). Third, the matching upper bound of ML24 Theorem 10 rests on an adversary that
uses the unknown target, and the proof of Corollary 12 bounds a total variation in
the wrong direction. The builder read ML24 Appendix B.3 and B.5 after the review
and confirms both gaps (proven, by the text of those appendices).

The discussant judged the profile to be supporting notation, the oracle lower bound
on training runs to be the main theorem candidate, and the reconstruction sandwich a
baseline lemma unless strengthened. Round 01 follows that ordering.

## Slugs accepted

Verdict ACCEPT, in a round with BLOCKING 14, so neither is eligible for status
accepted yet: `fact-yeom-dp-bounds-membership-advantage`,
`fact-zhao-accuracy-forces-attribute-leakage`. Both are carried unchanged into
round 01.

## Challenges open

All are answered in `round-01/builder.md`. Blocking: `ch-hsu-estimator-access`,
`ch-hsu-covariance-order`, `ch-lira-out-exclusion`, `ch-balle-prior-knowledge`,
`ch-balle-radius-hypotheses`, `ch-reconstruction-query-tightness`,
`ch-pac-suboptimal-adversaries`, `ch-gaussian-covariance-domain`,
`ch-profile-comparator`, `ch-profile-infinite-budgets`, `ch-profile-hsu-transfer`,
`ch-shadow-adaptive-seeds`, `ch-sandwich-domain-and-tightness`,
`ch-sandwich-decoder-floor`. Not blocking: `ch-yeom-cost-and-normalization`,
`ch-lira-parametric-necessity`, `ch-dinur-resource-comparison`,
`ch-sandwich-experimental-identification`.

## For the registers

New facts, each read in the library PDF on 2026-10-25 by this session, with the
note under `lib/literature/notes/<venue>/<Key>.md`.

- `fact-yeom-dp-bounds-membership-advantage`. YGFJ18, Theorem 1 with Experiment 1
  and Definition 4. An $\varepsilon$-DP learner gives membership advantage at most
  $e^\varepsilon-1$ against adversaries handed the distribution. Read full, status
  verified.
- `fact-yeom-generalization-error-gives-advantage`. YGFJ18, Theorem 2. The
  loss-threshold Adversary 1 has advantage $R_{\mathrm{gen}}/B$ for a loss in
  $[0,B]$. Read full.
- `fact-pac-privacy-mutual-information-bound`. XD23, Theorem 1, Corollary 1,
  Remark 1. The bound holds for the optimal adversary, or any adversary at least as
  good as the best prior guess (discussant's correction, `ch-pac-suboptimal-adversaries`).
- `fact-pac-privacy-gaussian-release-bound`. XD23, Theorems 3 and 4, with
  $\Sigma_B$ positive definite and finite second moments.
- `fact-pac-privacy-assumes-known-law`. XD23 §2, paragraph Lack of Knowledge. The
  framework cannot quantify the hardness added by an adversary's ignorance of the
  data law. Read full. Slug proposed, not yet stated as an object.
- `fact-zhao-accuracy-forces-attribute-leakage`. ZCTG20, Theorems 3.2 and 3.3,
  for attribute groups of positive probability.
- `fact-balle-reconnn-priced-in-shadow-runs`, proposed. BCH22 §VI-B and Table III.
  The reconstructor-network attack needs about $1$K to $8$K shadow models on MNIST
  and $5$K to $10$K on CIFAR-10 to beat the stated oracles, and it fails without the
  released model's initialization (MSE about $0.069$ against at most $0.0089$ with it).
  Empirical. Stated as an object in round 01.

Corrections to existing entries.

- `fact-hsu-membership-sample-gap`. The library holds v1 (26 August 2025). In v1,
  Theorem 1.1 is the informal version of Theorem 3.1, and Theorem 3.3 is the
  matching attack against the class of Definition 3.2, estimators that factor
  through the empirical mean. This settles the register's open question about the
  two theorem numbers.
- `fact-hsu-gap-prices-covariance`. Pointer Theorem 4.1, hypotheses $n\ge4$,
  $m\ge2$, $d<c(n+n^2\rho^2+n^2/m)$. Remark 4.2 states that order $n$ samples
  suffice, not that they are necessary. The necessary order at $d\asymp d^\star$ is
  $\min\{n,1/\rho^2\}$, with sufficiency attributed to Dwork et al.
- `fact-hsu-single-mechanism-open`. Not present in v1. Its source is v2, which the
  library does not hold.
- `fact-lira-low-fpr-yeom-game`. Definition 1 is in §III-A, not §VI-A. Its OUT point
  is drawn from the distribution conditioned to lie outside the training set, and
  its bit convention is the reverse of Yeom's.
- `fact-lira-priced-in-training-runs`. Pointer §V-A ($N=64$ for ImageNet, $256$
  otherwise), §VI-B and Fig. 9, §VI-D. Read full.
- `fact-balle-reconstruction-robustness-definition`. Status disputed resolved.
  Definition 2 is reconstruction robustness, Definition 1 the informed adversary,
  and the baseline $\kappa$ is defined in §VII-B without a number.
- `fact-balle-dp-bounds-reconstruction`. Hypotheses to add. Theorem 2 needs
  $\alpha>1$. Proposition 6 fixes a constant $\eta\in(0,1)$. Proposition 7 fixes a
  constant $\eta>0$ and an isotropic Gaussian prior with $\sigma\ge2\eta/\sqrt d$.
  Theorem 5 needs the $0/1$ error with $\eta\in(0,1)$.
- `fact-reconstruction-query-lower-bounds`. Pointer Theorem 9 (formal), not the
  informal Theorems 1 and 2. The matching upper bound of Theorem 10 is not
  established, since the adversary of Appendix B.5 uses the true target. The proof
  of Lemma 16 in Appendix B.3, on which Corollary 12 rests, bounds the total
  variation from the wrong side. Both confirmed by this session in the PDF.
- `fact-dinur-nissim-reconstruction-thresholds`. The comparison of Theorems 2 and 3
  changes the number of answers as well as the running time, so it is not a
  computational separation at fixed information. Theorem 5 is stated for the
  two-phase game of Definition 4.

New search rows. None. This round searched no index. It read library PDFs only.
The discussant named two papers outside the library without a search row:
Daniely, Sabato, Ben-David and Shalev-Shwartz, JMLR 2015, Theorem 5 (the agnostic
rate in the class dimension), and van Rooyen and Williamson, arXiv 1402.4884 (2014).
Both are leads to place, not facts.

New problems.

- `prob-train-access-collapses-sample-price`, proposed. In the noisy mean estimator
  of HSU25 the noise covariance is the population covariance, so Train calls on any
  fixed dataset sample it. Does an attacker with order $d$ Train calls and order
  $\min\{n,1/\rho^2\}$ reference samples succeed where HSU25 Theorem 3.1 forces
  order $n+n^2\rho^2$ samples without Train access? Weight supporting. Literature:
  unchecked.
- `prob-shadow-model-lower-bound`, status to update after round 01. Round 01 states
  the lower bound for query sets of size $q_E$. The factor $\ln|U|$ stays open.

Papers to place in the library: Sablayrolles et al., ICML 2019; Guo, Karrer,
Chaudhuri and van der Maaten, ICML 2022 (Theorem 1 as restated by ML24 Theorem 11);
Daniely et al., JMLR 2015.

For the integrator, outside the registers. Every argon call that must read a file
fails in headless mode until `discuss.sh` or the Antigravity settings grant a read
permission. A note with the error text is in the shared notes folder of this session
group, `2026-10-25-statistical-limits-argon-failure.md`.
