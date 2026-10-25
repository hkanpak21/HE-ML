---
key: CKMMNST25
title: "Data Reconstruction: When You See It and When You Don't"
authors: Edith Cohen and Haim Kaplan and Yishay Mansour and Shay Moran and Kobbi Nissim and Uri Stemmer and Eliad Tsfadia
venue: ITCS 2025
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/cohen-data-reconstruction.md
year: 2025
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven equivalences between Narcissus resiliency and classical notions"
prov: full-read
---

# CKMMNST25, "Data Reconstruction: When You See It and When You Don't"

Read on 2026-10-25 by the computational-limits space session from the held copy:
Section 1 to Definition 1.6 with Examples 1.7 and 1.8, and Appendix C to
Theorem C.5 with its proof, and the statements of Theorem C.8 and Definition
C.11. The rest was read by its headings only.

## Claim

A reconstruction attack should be judged against the same attacker run on an
independent dataset from the same law, and this "Narcissus" comparison captures
differential privacy, membership resilience, one-wayness and encryption security
as special cases.

## Method

Definition 1.6: $M$ is $(\varepsilon,\delta,\mathcal F)$-$R$-Narcissus-resilient
if for every $D\in\mathcal F$ and every attacker $A$,
$\Pr[R(S,z)=1]\le e^\varepsilon\Pr[R(T,z)=1]+\delta$, where $S,T\sim D$ are
independent, $y\leftarrow M(S)$ and $z\leftarrow A(y)$. The attacker runs on $M(S)$
in both experiments, so it must succeed on $S$ and fail on $T$. Definition C.1 is
the computational version, with pairs of datasets, attackers of polynomial time
and a negligible slack. Definition C.4: $f$ is $\nu$-well-spread if every output
has probability at most $\nu$ on a uniform input. Theorem C.5: for an efficiently
computable well-spread $f$, with $M_f(x)=f(x)$ and $R(x,x')=1$ iff
$f(x)=f(x')$, $f$ is one-way iff $M_f$ is
$(0,\mathrm{neg},\{(U_\lambda,U_\lambda)\})$-$R$-computationally Narcissus-resilient.
The proof notes that the right-hand experiment is at most $\nu$ by
well-spreadness, so resilience bounds the inversion probability. Theorem C.8
does the same for private-key encryption.

## What they measured, and on what

Definitions and equivalence proofs. No experiment.

## Epistemic status

Proven.

## The limitation that matters to us

The equivalence with one-wayness uses the relation "same image", which is
preimage finding. A reconstruction relation, closeness to the record, is
different, and a map can resist reconstruction while having easy preimages. My
finding, from the round-00 gap on one-wayness.

## Relationship to this project

Prior art and a definitional tool. The success measure of
`def-seed-blind-reconstruction-game` is the Narcissus comparison with
$\varepsilon=0$, and the brief's aim (c) on one-wayness starts from Theorem C.5.

## What we need to consider for our work

A finding that some aspect of a trained model is one-way, in Halil's sense,
would have to use the preimage relation, or prove a separate link from
reconstruction hardness to a one-way function. The blind first layer of the
round-00 aims hides the record only because of the record law, and its map has
easy preimages, so it yields no one-way function.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/C+25_DataReconstructionSeeIt.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/cohen-data-reconstruction.md`.
Mapping note: PDF is arXiv v2 (8 Dec 2024); key year follows ITCS 2025 (LIPIcs 325).
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
