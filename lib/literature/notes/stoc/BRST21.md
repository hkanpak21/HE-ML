---
key: BRST21
title: Continuous LWE
authors: Joan Bruna and Oded Regev and Min Jae Song and Yi Tang
venue: STOC 2021
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/bruna-continuous-lwe.md
year: 2021
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: tool
epistemic: "proven, conditional on the quantum hardness of worst-case lattice problems, with an unconditional SQ bound"
prov: full-read
---

# BRST21, Continuous LWE

Read on 2026-10-25 by the computational-limits space session from the held copy
(arXiv v2, 24 October 2020): Section 1 to the statement of Theorem 1.1, Section
2.3 (Definitions 2.18 to 2.21, Claim 2.22), the statements of Section 3 (Theorem
3.1, Corollary 3.2, Lemma 3.3), Corollary 4.2, the opening of Section 5, Section
7 to Theorem 7.5, Section 8 (Theorem 8.1, Lemma 8.2, Proposition 8.3) and Section
9 (Definition 9.2, Lemma 9.3, Corollary 9.4). Proofs of Sections 3, 4 and 6 were
not read.

## Claim

Continuous LWE, and its homogeneous form, a Gaussian law with a hidden direction
along which the mass sits on equally spaced thin layers, is as hard as
worst-case lattice problems under a quantum reduction, and is unconditionally
hard for statistical queries.

## Method

Definition 2.18: the CLWE law $A_{w,\beta,\gamma}$ draws $y\sim\gamma_n$ and
$z=(\gamma\langle y,w\rangle+e)\bmod1$ with $e\sim N(0,\beta)$. Definition 2.19:
homogeneous CLWE $H_{w,\beta,\gamma}$ has density proportional to
$\rho(y)\sum_{k\in\mathbb Z}\rho_\beta(k-\gamma\langle y,w\rangle)$, equivalently
(equation 2) a mixture of Gaussian layers of width $\beta/\sqrt{\beta^2+\gamma^2}$
spaced by $\gamma/(\beta^2+\gamma^2)$ along $w$ and standard Gaussian on
$w^\perp$, the Gaussian pancakes. Definitions 2.20 and 2.21: decision problems
against $\gamma_n\times U$ and $\gamma_n$ for a uniformly random $w$. Claim 2.22:
worst-case $w$ reduces to random $w$ by applying a random rotation, since the
Gaussian is rotation invariant. Theorem 3.1: for $\beta\in(0,1)$, $\gamma\ge2\sqrt n$
and $\gamma/\beta$ polynomial, a polynomial-time quantum reduction from
DGS$_{2\sqrt n\eta_\varepsilon(L)/\beta}$ to CLWE, hence (Corollary 3.2) from
GapSVP and SIVP at factor $\tilde O(n/\beta)$. Corollary 4.2 carries this to
hCLWE with DGS$_{2\sqrt{2n}\eta_\varepsilon(L)/\beta}$. Section 5 reduces hCLWE to
density estimation of Gaussian mixtures. Theorem 7.5: for $\gamma=n^\varepsilon$
with $\varepsilon<1/2$, a covariance test solves hCLWE in time
$\exp(O(n^{2\varepsilon}))$, which is why hardness needs $\gamma\ge2\sqrt n$.
Section 8: Proposition 8.3 bounds the pairwise correlation relative to
$\gamma_n$ by $2(\gamma/\beta)^2$ for equal directions and by
$8\exp(-\pi\gamma^2(1-\alpha^2))$ for $|\langle v,w\rangle|\le\alpha$ when
$\gamma^2(1-\alpha^2)\ge1$, and Theorem 8.1 concludes that for $\gamma\ge2$ an SQ
algorithm with tolerance $\tau\ge4\exp(-\pi\gamma^2/4)$ and success $\eta>1/2$
needs $(2\eta-1)\exp(cn)\tau^2\beta^2/(4\gamma^2)$ queries. Section 9 extends the
hardness to hidden subspaces of dimension $m$ with $n-m=\Omega(n^c)$ (Corollary
9.4).

## What they measured, and on what

Proofs. No experiment.

## Epistemic status

The lattice hardness is proven conditional on the quantum hardness of worst-case
lattice problems. The SQ bound is unconditional. The subexponential algorithm is
proven.

## The limitation that matters to us

Hardness is for the decision problem with a fine layer structure at scale about
$1/\gamma$. A reduction that starts from a coarse reconstruction of the hidden
coordinate does not reach the decision problem, because a direction with constant
correlation smears the layers. My finding, from the round-00 aim
`conj-seed-price-is-ngca-price`.

## Relationship to this project

Tool. hCLWE is the non-Gaussian component analysis instance with
polynomial-time hardness, the one the seed separation uses for its
polynomial-time clause, and Proposition 8.3 gives the pairwise correlations for
its SQ clause.

## What we need to consider for our work

Records drawn from a pancake law are an artificial data law. A polynomial-time
lower bound built on them is honest about that and should be paired with the SQ
bound of DKRS23 for laws that only match moments. The rotation trick of Claim
2.22 is the same symmetry that makes a Gaussian-initialized first layer hide the
orientation of the record law.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/BRST21_ContinuousLWE.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/bruna-continuous-lwe.md`.
Mapping note: PDF is arXiv v2 (24 Oct 2020); key year follows STOC 2021.
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
