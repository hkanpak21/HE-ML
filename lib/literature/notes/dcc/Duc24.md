---
key: Duc24
title: Provable lattice reduction of Z^n with blocksize n/2
authors: Léo Ducas
venue: Designs, Codes and Cryptography 2024
venue_evidence: first page of the open-access article, DOI 10.1007/s10623-023-01320-7, read from https://ir.cwi.nl/pub/33543/33543.pdf; ePrint 2023/447
year: 2024
type: journal
placed_on: none, the PDF is not in the library
placed_by: agent
triage: cite
relation: tool
epistemic: "proven reduction from ZLIP to SVP in dimension n/2+1; the complexity statements about other works are the author's account"
prov: full-read
---

# Duc24, Provable lattice reduction of Z^n with blocksize n/2

Read on 2026-10-25 by the computational-limits space session from the CWI copy,
text-extracted: the abstract, Section 1 (prior provable and heuristic algorithms,
the result), the statements of Lemmas 1 to 4 and Theorems 1 and 2. The
algorithm's description and the proofs were read in part.

## Claim

ZLIP, finding an orthogonal basis of a lattice known to be a rotation of
$\mathbb Z^n$, needs only polynomially many calls to an SVP oracle in dimension at
most $n/2+1$, a provable form of the heuristic that BKZ with blocksize $n/2$ solves
it.

## Method

A specialization of the slide reduction algorithm. The key remark (Lemmas 3 and
4) is that projected lattices of $\mathbb Z^n$ have a shortest vector of length either
$1$ or below $\sqrt{1-1/n}$, so each iteration makes progress until the first block
is a rotation of $\mathbb Z^k$, $n=2k+1$ (Lemma 2: sublattices of $\mathbb Z^n$ have
integral squared volume). Theorem 1: Algorithm 1 is partially correct, it outputs
an orthogonal basis on termination. Theorem 2: it terminates after
$O(n^2\log\max_i\|b_i\|)$ iterations, $O(n^3)$ after LLL.

## What they measured, and on what

Proofs. Section 1 records the state of the art: the generic provable SVP bound
$2^{n+o(n)}$, Bennett et al.'s provable $2^{n/2+o(n)}$ through a constant-factor
Gap-SVP reduction, and the heuristic $2^{0.146n+o(n)}$ of BKZ with blocksize
$n/2+o(n)$ from Ducas, Postlethwaite, Pulles and van Woerden (ASIACRYPT 2022).

## Epistemic status

Theorems 1 and 2 are proven. The complexity figures of other works are the
author's account, recorded here without opening those papers.

## The limitation that matters to us

The reduction does not change the exponential best complexity of ZLIP. The paper
says so.

## Relationship to this project

Tool. It prices the seed-blind attack on quantized Gaussian records in the
computational-limits aim `conj-quantized-records-zlip-equivalence`: exponential
with a small constant, $2^{0.146d}$ heuristically.

## What we need to consider for our work

The price of the seed on quantized data is the price of ZLIP, so any improvement
in ZLIP algorithms lowers it directly. Cite the heuristic constant as heuristic.

## Provenance

Not placed. Read from https://ir.cwi.nl/pub/33543/33543.pdf on 2026-10-25.
Reading record: the computational-limits space session, for
lab/theory/spaces/computational-limits/round-03/builder.md.
