---
key: DKRS23
title: SQ Lower Bounds for Non-Gaussian Component Analysis with Weaker Assumptions
authors: Ilias Diakonikolas, Daniel M. Kane, Lisheng Ren, Yuxin Sun
venue: NeurIPS 2023
venue_evidence: https://proceedings.neurips.cc/paper_files/paper/2023/hash/0d00a699f60e642b310eb04b76cc7731-Abstract.html
year: 2023
type: conference
placed_on: none, the PDF is not in the library
placed_by: agent
triage: cite
relation: tool
epistemic: "proven, unconditional for SQ algorithms"
prov: full-read
---

# DKRS23, SQ Lower Bounds for Non-Gaussian Component Analysis with Weaker Assumptions

Read on 2026-10-25 by the computational-limits space session from the arXiv HTML
page of arXiv 2403.04744v1, through a fetch tool that rendered the formulas as
paraphrase. Read: the abstract, Section 1 to Theorem 1.5 (Definitions 1.2 and
1.3, Condition 1.4, Theorem 1.5) and the opening of Section 1.1.1. The proofs and
the rest of the page were not read. The exact constants of Theorem 1.5 must be
checked against the PDF before a proof rests on them.

## Claim

Non-Gaussian component analysis, telling a standard Gaussian from a law that is
Gaussian except on a hidden low-dimensional subspace, is hard for statistical
queries whenever the hidden marginal approximately matches Gaussian moments up
to some degree, with no condition on its chi-square distance from the Gaussian.

## Method

Definition 1.2: for $V\in\mathbb R^{n\times m}$ with orthonormal columns and a law
$A$ on $\mathbb R^m$, $P^A_V$ has law $A$ on $\mathrm{span}(V)$ and an independent
standard Gaussian on the complement. Definition 1.3: NGCA testing distinguishes
$N(0,I_n)$ from $P^A_V$ with $V$ uniformly random. Condition 1.4 is the earlier
hypothesis of Diakonikolas, Kane and Stewart (FOCS 2017), which also required a
finite chi-square norm of $A$ against the Gaussian. Theorem 1.5: let
$\lambda\in(0,1)$, $n,m,d\in\mathbb N$ with $d$ even and $m,d\le n^\lambda/\log n$,
$0<\nu<2$, $0<c<(1-\lambda)/4$, and $n$ large in terms of $c$. If every polynomial
$f$ of degree at most $d$ with $E_{N(0,I_m)}f^2=1$ satisfies
$|E_Af-E_{N(0,I_m)}f|\le\nu$, then any SQ algorithm that solves NGCA testing with
probability $2/3$ needs a query of tolerance at most
$O_{m,d}(n^{-((1-\lambda)/4-c)d})+(1+o(1))\nu$ or $2^{n^{\Omega(c)}}$ queries. The
page states the hidden constant as roughly $\binom{(d+m)/2-1}{m/2-1}$.

## What they measured, and on what

A proof. The applications of Section 1.1.1 use the case $m=1$.

## Epistemic status

Proven for SQ algorithms. The polynomial-time hardness of particular instances
needs other assumptions (for example BRST21 for pancake laws).

## The limitation that matters to us

The bound is for testing. A reconstruction or weak-recovery attacker must first
be turned into a tester, which costs extra queries and is the subject of the
round-01 work of the computational-limits space. My finding.

## Relationship to this project

Tool. It prices the seed-blind attacker of `conj-seed-price-is-ngca-price` for
record laws that match Gaussian moments to degree $d$, without the chi-square
condition that excludes discrete laws.

## What we need to consider for our work

The exponent $((1-\lambda)/4-c)d$ is below $1/2$ for small $d$, so a reduction
that uses queries of tolerance $n^{-1/2}$ gives a non-trivial bound only for
moment degree above a constant. Place the PDF in the library and check the
constants before round 02.

## Provenance

Not placed. Read on the web at https://arxiv.org/html/2403.04744v1 on 2026-10-25.
Reading record: 2026-10-25, the computational-limits space session, for
lab/theory/spaces/computational-limits/round-00/builder.md.
