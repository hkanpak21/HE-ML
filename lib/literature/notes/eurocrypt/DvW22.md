---
key: DvW22
title: On the Lattice Isomorphism Problem, Quadratic Forms, Remarkable Lattices, and Cryptography
authors: Léo Ducas, Wessel van Woerden
venue: EUROCRYPT 2022
venue_evidence: CORDIS and dblp entries found on 2026-10-25 (EUROCRYPT 2022, pp. 643-673); ePrint 2021/1332; read from the CWI repository copy https://ir.cwi.nl/pub/31729/31729.pdf
year: 2022
type: conference
placed_on: none, the PDF is not in the library
placed_by: agent
triage: cite
relation: tool
epistemic: "proven reductions; hardness of LIP is a stated assumption"
prov: full-read
---

# DvW22, On the Lattice Isomorphism Problem, Quadratic Forms, Remarkable Lattices, and Cryptography

Read on 2026-10-25 by the computational-limits space session from the CWI copy,
text-extracted: the abstract, Section 2 (lattice isomorphism and quadratic forms,
discrete Gaussians and sampling) and Section 3 to Lemma 3.13 (the average-case
distribution and the worst-case to average-case reductions). Sections 4 to 7
(the zero-knowledge proof, the KEM, the signature, the genus) were read by their
headings only.

## Claim

The lattice isomorphism problem, finding an orthogonal map between two lattices
given by bases, has a natural average-case form defined by discrete Gaussian
sampling within an isomorphism class, which is as hard as the worst case for
large enough width, and it supports identification, encryption and signatures.

## Method

Definition 2.1 states LIP for bases as finding $O\in O_n(\mathbb R)$ and
$U\in GL_n(\mathbb Z)$ with $B'=OBU$. Passing to Gram matrices $Q=B^\top B$ removes
the real orthogonal part: Definition 2.2, wc-sLIP$^Q$, asks for $U$ with
$Q'=U^\top QU$, with solution set $\mathrm{Aut}(Q)\cdot U$ and $\mathrm{Aut}(Q)$
finite. Definition 2.3 is the distinguishing variant. Lemma 2.9 (from Brakerski
et al.) samples $D_{Q,s,c}$ exactly in polynomial time when
$s\ge\|B_Q^*\|\sqrt{\ln(2n+4)/\pi}$. Lemmas 3.1 and 3.2 define
$\mathrm{Extract}(Q,Y)$: from full-rank integer vectors $Y$ it takes the
transformation $U$ to the Hermite normal form of $Y$ and returns $R=U^\top QU$
with $\|B_R^*\|\le\max_i\|y_i\|_Q$, and the output depends only on the geometry of
$Y$, not on the representative $Q$. Definition 3.3: the Gaussian form distribution
$D_s([Q])$ samples $m=\lceil2n/C\rceil$ vectors from $D_{Q,s}$, $C=1-(1+e^{-\pi})^{-1}$,
until full rank and extracts. Lemma 3.4: for
$s\ge\max\{\lambda_n(Q),\|B_Q^*\|\sqrt{\ln(2n+4)/\pi}\}$ Algorithm 1 runs in
expected polynomial time and returns $(R,U)$ with $R\sim D_s([Q])$ and $U$ uniform
over the isomorphisms from $Q$ to $R$. Lemma 3.5: from any representative, for
$s\ge2^{\Theta(n)}\lambda_n([Q])$, after LLL. Lemma 3.6: for
$s\ge\max\{\lambda_n(Q),\eta_\epsilon(Q)\}$, a sample $Q'$ has $\|B^*_{Q'}\|>s\sqrt n$ with
probability at most $\frac{1+\epsilon}{1-\epsilon}100n2^{-n}$. Definitions 3.7 and 3.8:
ac-sLIP$^Q_s$ and ac-$\Delta$LIP$^{Q_0,Q_1}_s$. Lemma 3.9: for
$s\ge2^{\Theta(n)}\lambda_n(Q)$ the average case solves the worst case with polynomial
overhead. Lemma 3.10: for $s\ge\lambda_n(Q)$ with the additive cost of an SIVP oracle
of approximation factor $s/(\lambda_n(Q)\sqrt{\ln(2n+4)/\pi})$. Lemmas 3.12 and 3.13: the
same for $\Delta$LIP.

## What they measured, and on what

Proofs. The schemes are analysed for security, not benchmarked in the parts read.

## Epistemic status

The reductions are proven. The hardness of LIP for suitable lattices, and of
ZLIP, is an assumption, with exponential best attacks.

## The limitation that matters to us

The average-case instance is a quadratic form, a basis up to rotation. A
seed-blind server holding rotated lattice points must first compute such a form,
which needs exact or high-precision coordinates and the knowledge that its
points generate the whole lattice. My finding, from the computational-limits
aim `conj-quantized-records-zlip-equivalence`.

## Relationship to this project

Tool. It supplies the hard problem onto which blind reconstruction of quantized
Gaussian records maps: a Gaussian-initialized layer applied to records in
$\mathbb Z^d$ hides a rotation of $\mathbb Z^d$, which is average-case ZLIP.

## What we need to consider for our work

Use Lemma 2.9 to sample records from a form, Lemma 3.6 to bound the form's
Gram-Schmidt norm, and Definition 3.3 to match the server's own Extract call to
the average-case distribution. The record width then exceeds the instance width by
$\sqrt{d\ln(2d+4)/\pi}$.

## Provenance

Not placed. Read from https://ir.cwi.nl/pub/31729/31729.pdf on 2026-10-25 (the
IACR ePrint and archive copies refuse the fetch tool). Reading record: the
computational-limits space session, for
lab/theory/spaces/computational-limits/round-03/builder.md.
