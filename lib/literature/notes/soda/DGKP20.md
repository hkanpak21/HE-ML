---
key: DGKP20
title: On the Learnability of Deep Random Networks
authors: Abhimanyu Das and Sreenivas Gollapudi and Ravi Kumar and Rina Panigrahy
venue: SODA 2020
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/learnability-deep-random-networks.md
year: 2020
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: tool
epistemic: "proven SQ lower bound for random sign networks, average case over Gaussian weights"
prov: full-read
---

# DGKP20, On the Learnability of Deep Random Networks

Read on 2026-10-25 by the hard-problem-mappings space session from the held copy
(arXiv 1904.03866v1): Sections 1 to 4 in full (the setting, the repulsion property
with Lemmas 1 to 8, Theorem 9, Corollary 11, the correlation bound Lemma 12,
Theorems 14 to 16 and the upper bound Lemma 17). Sections 5 and 6 (the ReLU and
sigmoid extensions, $k$-way independence) and the experiments were read by their
headings only.

## Claim

A random deep network with sign activations is hard for statistical-query learners:
its correlation with any fixed bounded function decays exponentially in depth, so
reaching accuracy a constant better than one half needs a number of queries
exponential in depth, while a linear function reaches the matching
$1/2+e^{-O(h)}$.

## Method

Inputs are $x\in\{\pm1\}^n$, layers $x^{(i+1)}=\mathrm{sgn}(W^{(i)}x^{(i)})$ with
$n\times n$ weights and a $1\times n$ top layer. For two non-collinear inputs the
cosine $c_i$ of their images is a Markov chain with $E[c_i\mid c_{i-1}]=\mu(c_{i-1})$,
$\mu(x)=\frac2\pi\arcsin x$ (Lemma 3, Corollary 4, through Lemma 1 for Gaussian
rows). Theorem 9: $\lvert E[c_{d+h}]\rvert\le e^{-\Omega(h)}+he^{-\Omega(n)}+de^{-\Omega(\sqrt n)}$
after $d=O(\log\log n)$ burn-in layers. Lemma 12: over the $N=2^{n-1}$ inputs of one
halfspace, $E_W[E_x[g(x)f_{W,h}(x)]^2]\le\lvert g\rvert_2^2/N+\lvert g\rvert_1^2e^{-h}$.
Theorem 15, through BFJKMR94 Theorem 31 (quoted as Theorem 14), turns an average
squared correlation below $\epsilon$ into $p\max(r,q)^2>1/\epsilon$ for an SQ
learner with $p$ queries of tolerance $1/r$ and accuracy $1/2+1/q$. Theorem 16
states the bound for random networks. Lemma 17 shows the product of the weight
matrices, a linear function, has correlation $e^{-O(h)}$.

## What they measured, and on what

The lower bound is a proof. The experiments train standard networks on labels of
random deep networks and report that learnability drops with depth.

## Epistemic status

Proven for the SQ model with sign activations. Two defects in the text, my reading.
Section 2 says the weight entries are uniform on $[0,1]$, while the introduction
says Gaussian and Lemma 3 applies Lemma 1 with the rows as the Gaussian vector, so
the proofs need Gaussian rows. Theorem 16 prints the bound as $e^{O(h)}$, while
Lemma 12 with Theorem 15 gives $e^{\Omega(h)}$ (for $h\le n-1$ and, through Theorem
9, $h=o(\sqrt n)$). The claim that random deep networks may be cryptographically
hard is heuristic (Section 6 gives $n^{1/4}$-wise independence only).

## The limitation that matters to us

The lower bound is average case over untrained random weights, for uniform inputs
on a halfspace of the cube, and for SQ learners only. A trained model's weights are
not random in this sense. Found by me.

## Relationship to this project

Tool. It is the source of JCBKP20 Theorem 3 and so of the only SQ bound on
extraction in the literature (`fact-jagielski-extraction-query-bounds`).

## What we need to consider for our work

Any extraction bound for trained models has to replace the random-network
correlation decay by a property of the trained model, which is what the generative
exponent of the model's link does in `conj-extraction-priced-by-generative-exponent`.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/DGKP19_SQLowerBoundRandomNets.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/learnability-deep-random-networks.md`.
Mapping note: Held PDF is arXiv v1 (8 Apr 2019), which would give DGKP19. The wiki records the SODA 2020 version under the title On the Learnability of Random Deep Networks.
Reading record: 2026-10-25, the hard-problem-mappings space session read the sections named at the top of this note, for lab/theory/spaces/hard-problem-mappings/round-00/builder.md.
