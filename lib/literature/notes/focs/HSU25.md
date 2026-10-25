---
key: HSU25
title: The Sample Complexity of Membership Inference and Privacy Auditing
authors: Mahdi Haghifam and Adam Smith and Jonathan Ullman
venue: FOCS 2026 (to appear)
venue_evidence: https://arxiv.org/abs/2508.19458 (comment: To appear in FOCS 2026)
year: 2025
type: theory
placed_on: 2026-10-25
placed_by: agent
triage: deep
relation: prior-art
epistemic: "proven for the lower bounds of Theorems 3.1 and 4.1 and the attack of Theorem 3.3, against unbounded attackers that know the estimator; Proposition 2.5 and the attack matching Theorem 4.1 are attributed to Dwork et al. 2015 and not proven in the paper"
prov: full-read
---

# HSU25, The Sample Complexity of Membership Inference and Privacy Auditing

Read by the statistical-limits space session of the HE-ML theory on 2026-10-25,
from the library PDF, which is arXiv 2508.19458v1 of 26 August 2025. Read: §1
(introduction, setup, results, technical overview), §2 (preliminaries,
Definitions 2.1 to 2.4, Proposition 2.5, Lemma 2.6), §3 including the proof sketch
§3.1 and the key steps §3.2 (Lemmas 3.5 to 3.10 and the parameter choice of
§3.2.4), and §4 (Theorem 4.1 and its proof sketch). Not read: the appendices that
hold the full proofs. The theorem numbers below are those of v1. The register
records a v2 of 8 October 2026 that the library does not hold.

## Claim

There is a natural learning task, Gaussian mean estimation with added noise, in
which every membership attack that competes with a fully informed attacker needs
order $n+n^2\rho^2$ reference samples from the population, many more than the $n$
samples the trainer used, while knowing the covariance cuts the need to order
$\min\{n,1/\rho^2\}$.

## Method

The attacker gets the released estimate $\hat\mu$, a target point that is either a
member $X_1$ of the training set or a fresh draw $X_0$, and $m$ independent
auxiliary samples $\mathbf Y^m$ from the population. It is unbounded and knows the
estimator. An $m$-sample-based attack (Definition 2.1) must reach false-positive
rate at most $0.49$ and true-positive rate at least $0.51$ for every population in
the family and every estimator in the class. The lower bounds use Le Cam's method
for mixtures (Lemma 2.6). A prior is placed over hard populations and the total
variation between the two mixture laws of $(\mathbf Y^m,\hat\mu,\text{target})$ is
bounded by $0.02$.

For unknown covariance (§3) the hard populations are $\mathcal N(0,I_d+\sigma^2UU^\top)$
with the range of $U$ uniform over $k$-dimensional subspaces, $\sigma^2$ of order
$d$, and $k-m$ a universal constant. Lemma 3.5 reduces $m$ auxiliary samples in
dimension $d$ to zero samples in dimension $d-2m$ with $k-m$ spiked directions, at
an additive cost $2\sqrt{m/(n+n^2\rho^2)}$ in total variation. Lemma 3.7 uses the
rotation invariance of Lemma 3.6 to show that with zero samples the norms
$\|X\|$, $\|\hat\mu\|$ and the inner product $\langle X,\hat\mu\rangle$ are
sufficient. Lemmas 3.8 to 3.10 bound the total variation of these statistics. The
inner product has mean $\mathrm{tr}(\Sigma)/n$ under IN and zero under OUT, but its
standard deviation hides the shift, and a bound on the total variation of two
variables perturbed by an independent chi-squared variable handles the norms. The
parameters of §3.2.4 take $c=35$, $400m\le n+n^2\rho^2$, $\sigma^2\ge C_{\mathrm{dim}}d$
and $d\ge C_{\mathrm{dim}}(n+n^2\rho^2)$.

For known covariance (§4) the prior is $\mu\sim\mathcal N(0,I_d)$, the auxiliary
samples have the same law under both hypotheses, and the KL chain rule reduces the
problem to two Gaussians given $\mathbf Y^m$, with the posterior
$\mu\mid\mathbf Y^m\sim\mathcal N(\frac m{m+1}\bar y,\frac1{m+1}I_d)$.

## What they measured, and on what

Nothing empirical. The results, with $d^\star=n+n^2\rho^2$ and the estimator
$\mathcal A_{n,\rho}$ that outputs the empirical mean plus $\rho Z$, $Z\sim\mathcal N(0,\Sigma)$
(Definition 2.4), are these.

- Proposition 2.5. An informed attacker succeeds when $d\ge c\,d^\star$, and
  $\mathrm{TV}((X_1,\hat\mu),(X_0,\hat\mu))\le\sqrt{d/d^\star}$. The first part is
  credited to Dwork, Smith, Steinke, Ullman and Vadhan (FOCS 2015) and the proof is
  skipped.
- Theorem 3.1. If $d>c_1d^\star$ and $m\le c_2d^\star$, no
  $(\mathcal P_d,\{\mathcal A_{n,\rho}\},n,m)$-sample-based attack exists, where
  $\mathcal P_d$ is all Gaussians with positive definite covariance. Theorem 1.1 is
  its informal version.
- Theorem 3.3. If $0<\rho<1$, $m\ge cd$ and $d\ge c\,d^\star$, an attack exists
  against the class $\mathfrak A_{n,d,\rho}$ of symmetric estimators within
  Mahalanobis distance $\sqrt{2\rho^2d}$ of the empirical mean with probability
  $0.99$ (Definition 3.2). It splits the samples into order $d$ for the inverse
  empirical covariance $H$, order $\min\{n,1/\rho^2\}$ for a mean estimate
  $\bar\mu_0$, and one held-out point $Y_0$, and thresholds
  $\langle H^{1/2}(\hat\mu-\bar\mu_0),H^{1/2}(X-Y_0)\rangle$ at $c\sqrt{d/n}$.
  Remark 3.4 says the bounds match at $d\asymp d^\star$.
- Theorem 4.1. For identity covariance, $n\ge4$, $m\ge2$ and
  $d<c(n+n^2\rho^2+n^2/m)$, no attack exists. The matching attack for
  $d\gtrsim n+n^2\rho^2+n^2/m$ is credited to Dwork et al. Remark 4.2 compares the
  two regimes.

§1.2.1 argues that attacks of the restricted form $\psi(X,\hat\mu)\ge\tau(X,\mathcal D)$,
which use the population only to set a threshold, need only $O(1)$ shadow
estimates, hence $O(n)$ samples, and so cannot use more data. Practical shadow-model
attacks have this form.

## Epistemic status

Proven, Theorems 3.1, 3.3 and 4.1, with proofs in the appendices not read here.
Proposition 2.5 and the upper bound matching Theorem 4.1 are attributed and not
proven in the paper. The claim that practical attacks have the restricted form is
an argument, not a theorem. The paper does not blur these.

## The limitation that matters to us

Found, not stated as a limitation. The attacker knows the estimator, so it can
simulate any number of training runs, and the paper prices samples alone. A theory
that counts training runs as the attacker's resource, as the learning oracle does,
gets nothing from this paper about runs. The result also covers one family. v1
states no open problem. The register attributes a remark that a separation for a
single mechanism is open to v2. The lower bound holds at $d\asymp d^\star$, and for
$d\gg d^\star$ the best attack still uses order $d$ samples, a gap the paper states
(Tightness of Theorem 1.1).

## Relationship to this project

Prior art. It is the only proven statement in the library that prices an unbounded
privacy attacker in the trainer's own unit, samples, and finds the attacker's price
above the trainer's.

## What we need to consider for our work

The space statistical-limits uses Theorems 3.1 and 4.1 as the points of the
sample axis of its uniform security profile (`def-uniform-security-profile`,
round-00 of `lab/theory/spaces/statistical-limits/`). Theorem 3.1 against Theorem
4.1 shows that the sample price of an unbounded attacker is a price of not knowing
part of the data law. A training-run price needs a separate theorem, which the
space states as `conj-shadow-run-price-finite-views`.

## Reading for the space oracle-and-measurement, 2026-10-25

Read again by the oracle-and-measurement space session on 2026-10-25, §1.2, Definitions 2.1 to
2.4, Proposition 2.5, Theorems 3.1 and 3.3 with Remark 3.4, and Theorem 4.1 with Remark 4.2. Two
points for measurement. First, the matching attack is Theorem 3.3, not a Theorem 3.2 as the register's
entry fact-hsu-membership-sample-gap records, and the library PDF is v1, so the round-00 builder of
oracle-and-measurement, which wrote v2, is corrected in its summary. Second, §1.2.1 reads the restricted test, a statistic
free of the population with a calibrated threshold, as needing $O(1)$ shadow estimates. An audit built
from restricted tests can therefore sit far below the profile it lower-bounds, by the gap between
Theorem 3.1 and the $O(n)$ samples such a test uses. This is the paper's own caution and bears on what a
measured point of a security profile certifies.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/HSU25_SampleComplexityMIA.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/haghifam-sample-complexity-mia.md`.
Mapping note: SOURCES.md title omits and Privacy Auditing.
Venue corrected on 2026-10-25 from arXiv preprint to FOCS 2026, per the arXiv comment the scan recorded. The key keeps the year of the held version.
Read on 2026-10-25 by the statistical-limits space session, sections listed at the top, and this note written from that reading.
