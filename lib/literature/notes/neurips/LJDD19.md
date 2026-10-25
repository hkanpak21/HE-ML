---
key: LJDD19
title: Inverting Deep Generative models, One layer at a time
authors: Qi Lei and Ajil Jalal and Inderjit S. Dhillon and Alexandros G. Dimakis
venue: NeurIPS 2019
venue_evidence: scan summary; https://proceedings.neurips.cc/paper/2019/hash/24389bfe4fe2eba8bf9aa9203a44cdad-Abstract.html
year: 2019
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: baseline
epistemic: "proven for i.i.d. Gaussian expansive layers with known weights, NP-hardness worst case over constructed weights"
prov: full-read
---

# LJDD19, Inverting Deep Generative models, One layer at a time

Read on 2026-10-25 by the computational-limits space session from the held copy
(arXiv 1906.07437v2): Sections 3 and 4.1 and the appendix proofs of Lemma 1 and
Theorem 3. The noisy-case theorems (4 and 5) were read by their statements only,
and the experiments by their headings.

## Claim

Inverting a ReLU generative network is NP-hard for constructed weights, but a
random expansive Gaussian network is inverted exactly by layer-wise linear
equations with high probability.

## Method

For one ReLU layer the preimage of an observation is a polytope, found by linear
programming. Theorem 1: deciding whether $z\in\{\pm1\}^k$ with $G(z)=x$ exists is
NP-complete for a fixed two-layer ReLU network, by reduction from 3SAT. Theorem
2: the same for a fixed four-layer network on real inputs. Assumption 1: the
weight matrix $W\in\mathbb R^{n\times k}$ has i.i.d. Gaussian entries and
$n=c_0k$ with $c_0\ge2.1$. Lemma 1: under Assumption 1 the map
$x\mapsto\mathrm{ReLU}(Wx)$ is injective with probability $1-\exp(-\Omega(k))$,
because at least $k$ of the $n$ coordinates of $Wx$ are positive (a binomial tail)
and any $k$ Gaussian rows are invertible almost surely, so the positive
coordinates give $k$ independent linear equations. Theorem 3: if every layer
satisfies Assumption 1, then for any input $z^*$, with probability
$1-e^{-\Omega(k)}$, $z^*$ is recovered from $G(z^*)$ by solving one linear system
per layer, in time at most $\sum_in_i^{2.376}$. The inverter knows all weights.

## What they measured, and on what

The core results are proofs. Theorems 4 and 5 bound the recovery error under
$\ell_\infty$ and $\ell_1$ noise under Assumptions 2 and 3 (a restricted
norm-extension property of submatrices), and Corollary 1 verifies Assumption 2
for Gaussian weights. Synthetic experiments check Theorems 4 and 5.

## Epistemic status

Proven for the stated assumptions. The probability is over the weights for each
fixed input, so many inputs need a union bound. The NP-hardness is worst case
over constructed weights and says nothing about trained weights.

## The limitation that matters to us

It covers the attacker who knows the weights only. It says nothing about an
attacker who sees representations without the seed, which is the case a seed
separation is about. I found this, the paper does not discuss attackers.

## Relationship to this project

Baseline. It is the seed-known side of `prob-split-learning-seed-separation`: a
split-learning server that knows a Gaussian expansive client inverts the first
representation it receives in polynomial time.

## What we need to consider for our work

The seed-known attacker of `conj-seed-price-is-ngca-price` is this inverter. A
client of expansion below $2.1$, a trained client, or a convolutional client is
outside Theorem 3 and needs its own argument.

## Provenance

Copied on 2026-10-25 from the literature scan of 2026-10-25 (arXiv 1906.07437) for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Mapping note: held copy is arXiv v2 dated 19 Jun 2019, not the proceedings PDF
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
