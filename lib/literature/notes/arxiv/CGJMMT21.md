---
key: CGJMMT21
title: NeuraCrypt is not private
authors: Nicholas Carlini and Sanjam Garg and Somesh Jha and Saeed Mahloujifar and Mohammad Mahmoody and Florian Tramer
venue: arXiv preprint
venue_evidence: arXiv identifier; https://arxiv.org/abs/2108.07256 lists no venue
year: 2021
type: eprint
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven for weakly ideal encoders, attack on NeuraCrypt empirical"
prov: full-read
---

# CGJMMT21, NeuraCrypt is not private

Read on 2026-10-25 by the computational-limits space session from the held copy
(arXiv 2108.07256): the opening sections to Definition 1, the paragraphs on the
ideal and heuristic NeuraCrypt schemes, Definition 2 and Theorem 1. The attack
sections were read by their headings only.

## Claim

Any instantiation of NeuraCrypt's ideal encoding would let a learner's weak
accuracy be turned into a near-perfect predictor from two labelled examples, so
the ideal is as hard to realize as learning the task perfectly, and the
heuristic NeuraCrypt is broken in practice.

## Method

Definition 1 sets learning with a keyed encoding, aligned with NeuraCrypt's
challenge. Definition 2: an encoder $E(x,K,c)$ is weakly ideal for a concept
class if encodings of two inputs with the same label have the same law and
labels are preserved by the encoding. Theorem 1: if a learner with $m$ samples
reaches balanced error $1/2-\varepsilon$ over the encoded law for every concept,
then for any $\tau$ and any pair $x_0,x_1$ with labels $0$ and $1$ an oracle-aided
PPT predictor of risk at most $\tau$ on any distribution exists, in time
poly$(m,1/\epsilon,1/\delta,1/\tau)$, with oracle access to the learner and the
encoder.

## What they measured, and on what

The theorem is a proof. The break of the heuristic NeuraCrypt is empirical, a
matching of encoded to plain images on the challenge data.

## Epistemic status

Proven for the ideal scheme, empirical for the attack on the heuristic scheme.

## The limitation that matters to us

The predictor has the encoder as an oracle, so the result is about the
seed-known or chosen-input attacker. My finding from the theorem statement.

## Relationship to this project

Prior art. NeuraCrypt is a law of random-network encoders, the nearest deployed
analogue of the seed-blind setting, and its empirical break is one of the
constraints on `prob-split-learning-seed-separation`.

## What we need to consider for our work

The break is consistent with `conj-seed-price-is-ngca-price`: image data are far
from Gaussian at low degree, so the seed buys little. NeuraCrypt's
convolutional encoders and patch shuffling are outside the rotation symmetry the
aim uses, so the aim does not cover them.

## Provenance

Copied on 2026-10-25 from the literature scan of 2026-10-25 (arXiv 2108.07256) for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Mapping note: authors ordered alphabetically (first-page footnote)
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
