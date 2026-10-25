---
key: NRNT25
title: Achieving Data Reconstruction Hardness and Efficient Computation in Multiparty Minimax Training
authors: "Truong Son Nguyen, Yi Ren, Guangyu Nie, Ni Trieu"
venue: PoPETs 2025
venue_evidence: https://petsymposium.org/popets/2025/popets-2025-0088.php
year: 2025
type: FILL
placed_on: 2026-10-16
placed_by: agent
triage: skim
relation: prior-art
epistemic: "empirical costs, hardness argued for one attack route and heuristic for general attackers"
prov: full-read
---

# NRNT25, Achieving Data Reconstruction Hardness and Efficient Computation in Multiparty Minimax Training

Read on 2026-10-25 by the computational-limits space session from the held copy:
the introduction with Definition 1.1, Section 4.3 to its remarks, and Section 4.4
(Propositions 3 to 6) and Section 4.5. The protocol sections, Propositions 1 and
2 and the experiments were read by their headings only.

## Claim

GAN training with a public generator and a discriminator whose first two or three
layers stay secret-shared between two servers keeps training data hard to
reconstruct while cutting the cost of full MPC by a factor of four to sixteen.

## Method

Two non-colluding semi-honest servers train a GAN on secret-shared data.
Protocol 1 keeps the whole discriminator private, Protocol 2 its first layers.
Definition 1.1: $(\epsilon,\delta)$-reconstruction hardness holds if no algorithm
of polynomial data and computational complexity outputs, with probability at
least $1-\delta$, an $\hat X_t$ within distance $\epsilon$ of some training record.
Section 4.3 argues hardness for a public generator from a single gradient update
with a bound on the learning rate. Proposition 3: with a public discriminator
and public gradients the record is recovered exactly from the first-layer
update. Section 4.4: with the first $M$ layers private the attacker would first
approximate the private layers from public outputs and then invert, and hardness
is drawn from results on learning ReLU networks: an approximation algorithm
exponential in the network size (Proposition 4), learning depth-2 ReLU networks
under Gaussian inputs implies breaking learning with rounding (Proposition 5),
and SQ bounds exponential in depth for random networks (Proposition 6).

## What they measured, and on what

Generation quality (FID) and training time on MNIST and CelebA against full MPC
and DP training, and a practical reconstruction attack against federated
learning and the proposed protocol.

## Epistemic status

The protocols' costs and the attack comparison are empirical. The hardness of
Section 4.4 is argued for the two-step attack route, and the paper itself notes
that parameter recovery is stronger than the approximation the cited results
rule out. I read the argument as heuristic for general attackers, since no
reduction from an arbitrary reconstructor to the cited learning problems is
given.

## The limitation that matters to us

Hardness for one attack route is not hardness for every attacker of a class.
My finding.

## Relationship to this project

Prior art. It is the nearest published claim of reconstruction hardness from
private layers, and `conj-seed-price-is-ngca-price` aims at what it lacks, a
reduction that covers every attacker of a stated class.

## What we need to consider for our work

A claim of reconstruction hardness from hidden weights must reduce from the
attacker, not from one attack strategy. The private layers here are trained, not
frozen, so a full answer also needs the transcript question of
`prob-split-transcript-leaks-seed`.

## Provenance

Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
