---
key: LKR06
title: Random Projection-Based Multiplicative Data Perturbation for Privacy Preserving Distributed Data Mining
authors: Kun Liu, Hillol Kargupta, Jessica Ryan
venue: IEEE TKDE 18(1), pp. 92-106
venue_evidence: first page of the authors' PDF, https://userpages.cs.umbc.edu/hillol/PUBS/Papers/tkde.pdf
year: 2006
type: journal
placed_on: none, the PDF is not in the library
placed_by: agent
triage: cite
relation: prior-art
epistemic: "heuristic and empirical for the ICA attack, with an identifiability theorem quoted from Cao et al."
prov: full-read
---

# LKR06, Random Projection-Based Multiplicative Data Perturbation

Read on 2026-10-25 by the computational-limits space session from the authors'
PDF, text-extracted: the abstract, Section 1, the end of Section 3 and Section 4
to 4.2. Sections 5 to 8 (the projection scheme, its privacy analysis and the
experiments) were not read. The PDF was fetched to the session's tool folder and
not placed in the library.

## Claim

Multiplying a data table by a random orthogonal matrix preserves inner products
and distances but does not hide the data, because independent component
analysis recovers the original attributes when they are independent and
non-Gaussian, and a projection to fewer dimensions is proposed instead.

## Method

Section 3 notes that an orthogonal transformation is a rotation or a
rotoinversion, so the data can be re-identified by a suitable rotation, and that
independent, non-Gaussian original attributes can be estimated accurately by ICA.
Section 4 recalls the ICA model $u=Rx$ with independent non-Gaussian sources and
an unknown full-column-rank mixing matrix, recovery up to permutation and scaling,
the requirement of at least as many observed signals as sources, and the failure
to separate more than one Gaussian source. It concludes that random rotation and
random orthogonal perturbation are exposed, and motivates a projection with
fewer output dimensions than sources, where linear separation is impossible.

## What they measured, and on what

The parts read argue from the ICA identifiability results of Cao et al. and an
audio-mixing illustration (Figures 3 and 4). The later sections, not read,
evaluate the projection scheme.

## Epistemic status

Heuristic and empirical for the attack on rotation perturbation. No complexity
bound or lower bound appears in the parts read.

## The limitation that matters to us

The attack needs independent sources and is not priced. Records whose law is
Gaussian up to a hidden low-degree structure are not covered, and nothing is said
about how many samples or how much computation the attacker needs. My finding.

## Relationship to this project

Prior art for the attack direction of `conj-seed-price-is-ngca-price`. The
qualitative statement that a hidden rotation protects only Gaussian-like data is
known from this line of work. The aim's content is the price.

## What we need to consider for our work

State the novelty of the seed separation against this paper and the rotation
perturbation literature that followed it: the reduction both ways to
non-Gaussian component analysis, the simulation of a whole training transcript,
and the SQ and lattice prices.

## Provenance

Not placed. Read from https://userpages.cs.umbc.edu/hillol/PUBS/Papers/tkde.pdf on 2026-10-25.
Reading record: 2026-10-25, the computational-limits space session, for
lab/theory/spaces/computational-limits/round-00/builder.md.
