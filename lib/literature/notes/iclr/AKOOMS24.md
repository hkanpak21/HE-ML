---
key: AKOOMS24
title: One-shot Empirical Privacy Estimation for Federated Learning
authors: Galen Andrew, Peter Kairouz, Sewoong Oh, Alina Oprea, H. Brendan McMahan, Vinith M. Suriyakumar
venue: ICLR 2024
venue_evidence: https://openreview.net/forum?id=0BqyZSWfzo
year: 2024
type: measurement
placed_on: 2026-10-16
placed_by: agent
triage: skim
relation: prior-art
epistemic: "Propositions 3.1 and 3.2 and Theorem 3.3 proven for the Gaussian sum mechanism, Theorem 3.3 asymptotic in the dimension with no rate; the federated estimate of Algorithms 2 and 3 empirical and heuristic, on EMNIST and Stackoverflow; the reported lower bound eps_lo a confidence bound"
prov: full-read
---

# AKOOMS24, One-shot Empirical Privacy Estimation for Federated Learning

Read by the agent on 2026-10-25 for the theory space `oracle-and-measurement`, from the library
PDF (arXiv 2302.03098v5, 21 pages). Read: §1 to §6, Table 1, Algorithm 1, Propositions 3.1 and
3.2, Theorem 3.3 with the note on its growth condition in the appendix, Tables 2 to 4 and 6. Not
re-derived: the proofs of Appendix B.

## Claim

The privacy loss of releasing a DP-FedAvg model can be estimated during the single run that trains
it, by inserting random canary clients and testing the cosine between each canary update and the
final model, and for one application of the Gaussian mechanism the estimate is consistent as the
dimension grows.

## Method

For the Gaussian sum query (§3, Algorithm 1), $k$ canaries are drawn uniformly from $S^{d-1}$ and added
to the data. One run releases $\rho$, the $k$ cosines $g_i=\langle c_i,\rho\rangle/\|\rho\|$ are fitted
with a Gaussian, and the null law of the cosine of an unused canary is taken as $\mathcal N(0,1/d)$, which
needs no samples. Proposition 3.1 gives the exact density of that cosine, Proposition 3.2 its Gaussian
limit after scaling by $\sqrt d$. Theorem 3.3 assumes $\|X_d\|=o(\sqrt d)$ for the sum of real vectors,
$k=o(d)$ and $k=\omega(1)$, and proves that the estimate $\hat\varepsilon_d$ converges in probability to
the $\varepsilon$ of $\mathcal N(0,\sigma^2)$ against $\mathcal N(1,\sigma^2)$ at the target $\delta$. For federated
learning (§4, Algorithms 2 and 3) canary clients return a fixed random update of the clip norm whenever
they participate, and the auditor compares canary cosines with the final model (Algorithm 2) or with
every model delta (Algorithm 3). The adversary controls one client's updates and sees the final model, or
every iterate.

## What they measured, and on what

Table 2 simulates the Gaussian mechanism for $d$ from $10^4$ to $10^7$ with $k=\sqrt d$, and the mean
estimate matches the analytical $\varepsilon$ of 10, 3 and 1 with spread falling in $d$. EMNIST and
Stackoverflow word prediction under DP-FedAvg, 1,000 canary clients among 341k real clients on
Stackoverflow, with at most 0.1% absolute loss of accuracy (Table 3). Table 4 compares estimates from all
deltas and from the final model only, against a 95% lower bound $\varepsilon_{\mathrm{lo}}$ built from
Clopper-Pearson style bounds with the Jeffreys interval for the false-negative rate and the exact null law
for the false-positive rate. With 1,000 canaries at $\alpha=0.05$ that lower bound cannot exceed 6.24 even
under perfect separation (§5, text by Table 4). At noise 0.0496 (analytical $\varepsilon=300$) the estimate
from all deltas is 382 and from the final model 1.97. Table 6 compares with CANIFE.

## Epistemic status

Propositions 3.1, 3.2 and Theorem 3.3 are proven, the last asymptotic in $d$ and with no finite-sample
rate. The Gaussian fit of the alternate law is supported by Anderson-Darling tests and histograms only, as
the paper says in §3. The federated estimates are empirical and are estimates, not bounds. The paper
states that "we still cannot rule out that our method is not overestimating $\varepsilon$" (§5.3). It keeps
estimate and lower bound apart in its tables.

## The limitation that matters to us

Stated in part by the authors. A one-run estimate carries no confidence statement, and the one-run lower
bound has a ceiling fixed by the number of canaries, 6.24 at 1,000 canaries and $\alpha=0.05$. So one run
cannot certify a large leakage, and no single run gives an upper bound. The method also needs high
dimension and canaries that the protocol accepts as clients.

## Relationship to this project

Prior art for the measurement side, and the federated one. It is the cheapest known estimate of a point of
a security profile in runs, one run, and it shows what one run cannot certify.

## What we need to consider for our work

Recorded as fact-one-shot-estimate-consistency in
`lab/theory/spaces/oracle-and-measurement/round-00/builder.md`. A certificate in the sense of the HE-ML
oracle theory needs more runs than this estimate, and the space's aims price how many.
