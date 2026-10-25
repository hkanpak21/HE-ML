---
key: DPLB24
title: Computational-Statistical Gaps in Gaussian Single-Index Models
authors: Alex Damian and Loucas Pillaud-Vivien and Jason D. Lee and Joan Bruna
venue: COLT 2024
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/generative-exponent-single-index.md
year: 2024
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: tool
epistemic: "proven for SQ, low-degree bound conditional on the low-degree conjecture"
prov: full-read
---

# DPLB24, Computational-Statistical Gaps in Gaussian Single-Index Models

Read on 2026-10-25 by the computational-limits space session from the held copy:
Section 1 (Definition 1.1, the informal Theorems 1.2 to 1.5), Section 2 to
Corollary 2.8 (Definition 2.4, Remark 2.5), Section 3 (Theorem 3.2, Remark 3.3,
Conjecture 3.4, Theorem 3.5, the NGCA paragraph and Proposition 3.7), the
statement of Theorem 4.1, and Appendices E.4 and E.5. The proofs of Sections 3
to 6 other than E.4 were not read.

## Claim

For Gaussian single-index models the right exponent for efficient algorithms is
the generative exponent $k^*$, the first Hermite degree at which some
transformation of the label correlates with the hidden coordinate, and both SQ
and low-degree methods need $n\gtrsim d^{k^*/2}$ samples, which a partial-trace
algorithm achieves.

## Method

Definition 1.1: $x\sim\gamma_d$, and $(\langle w^*,x\rangle,y)\sim P$ in the class
$\mathcal G$ of non-product laws with Gaussian first marginal and
$E[Y^2]<\infty$. Definition 2.4: $\zeta_k(y)=E[h_k(Z)\mid Y=y]$,
$\lambda_k=\|\zeta_k\|_{P_y}$, $k^*(P)=\min\{k\ge1:\lambda_k\ne0\}$, with
$k^*\le l^*$, the information exponent. Lemma 3.1 represents the $\chi^2$
divergence between two planted models through $\lambda_k$ and the overlap
$w\cdot w'$. Theorem 3.2: with $q=d^r$, $r\le d^{1/4}$ and
$\lambda_{k^*}^2\ge rd^{-1/2}$, returning $\hat w$ with
$|\hat w\cdot w^*|\ge\tilde\omega(d^{-1/2})$ by $q$ queries to VSTAT($n$) needs
$n\ge c_{k^*}\lambda_{k^*}^{-2}(d/r^2)^{k^*/2}$. Theorem 3.5 is the low-degree
version under Conjecture 3.4. Theorem 4.1: the partial trace of the empirical
order-$k$ Hermite tensor of $(x,T(y))$ with a denoiser $T$ returns $\hat w$ with
$(\hat w\cdot w^*)^2\ge1-\epsilon^2$ once
$n\ge C_k[d^{k/2}/\tilde\lambda_k^2+d/(\tilde\lambda_k^2\epsilon^2)]$, with
$\tilde\lambda_k=\lambda_k/\log^k(3/\lambda_k)$. Proposition 3.7 (proved in
Appendix E.4): rejection sampling on $\{y:\zeta_k(y)>0\}$ turns samples of the
single-index model into samples of an NGCA law $\mu$ with $E_\mu[h_j]=0$ for
$j<k$ and $E_\mu[h_k]>0$, so an SQ algorithm for that NGCA instance solves the
single-index model. Appendix E.5 gives a reduction from NGCA to a variant of the
single-index model whose label also depends on $\|x\|$.

## What they measured, and on what

Proofs, with an information-theoretic upper bound of $O(d)$ samples (Theorem
6.1) and constructions of smooth links of any prescribed $k^*$ (Theorem 5.1),
preserved under Gaussian label noise (Theorem 5.2).

## Epistemic status

Proven for SQ, conditional on the low-degree conjecture for polynomial time.
Remark 3.3: the SQ proof compares with the null $\gamma_d\otimes P_y$ and so
measures detection first, and the authors leave open whether SQ estimation needs
more, as it does for tensor PCA. The upper bound's constant is not explicit.

## The limitation that matters to us

The model has Gaussian inputs. When the record law along the hidden direction is
non-Gaussian, the relevant quantity is the generative exponent of the joint law
of (hidden coordinate, label) relative to a product null, which the paper does not
state. My finding.

## Relationship to this project

Tool. It prices the trainer's own problem and, after whitening, the blind
server's problem of finding the label-relevant direction in split learning, the
content of `conj-reconstruction-at-training-cost`. Proposition 3.7 links it to
the NGCA price of `conj-seed-price-is-ngca-price`.

## What we need to consider for our work

The same $k^*$ prices training and reconstruction of the label-relevant
coordinate, so for that coordinate the attack costs what learning costs. The
detection-versus-estimation caveat of Remark 3.3 carries over to any bound we
derive from Theorem 3.2.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/DPLB24_GenerativeExponent.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/generative-exponent-single-index.md`.
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
