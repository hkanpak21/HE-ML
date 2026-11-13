---
key: YGFJ18
title: "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting"
authors: Samuel Yeom and Irene Giacomelli and Matt Fredrikson and Somesh Jha
venue: IEEE CSF 2018
venue_evidence: "first page footnote: 'This is the unabridged version of the paper accepted for publication in CSF 2018'"
year: 2018
type: theory
placed_on: 2026-10-25
placed_by: agent
triage: read
relation: prior-art
epistemic: "proven for Theorems 1 to 4 and 6, as read, against informed adversaries that are handed the distribution; Theorems 5 and 7 not read; empirical for the attack evaluations of §6"
prov: full-read
---

# YGFJ18, "Privacy Risk in Machine Learning: Analyzing the Connection to Overfitting"

Read by the statistical-limits space session of the HE-ML theory on 2026-10-25,
from the library PDF, the unabridged arXiv 1709.01604v5 of 4 May 2018. Read: the
abstract, §2 (Definitions 1 to 3), §3 (Experiment 1, Definition 4, Theorems 1 to 4
with the proofs of Theorems 1 and 2), §4 (Experiment 2, Definitions 5 and 6) and
§5.1 (Adversary 5 and Theorem 6) and the construction of Adversary 6 in §5.2.
Not read: the statements of Theorems 5 and 7. Skimmed: §6, the experiments.

## Claim

Membership advantage, defined so that knowledge of the distribution alone gives
zero, is bounded by $e^\varepsilon-1$ under $\varepsilon$-differential privacy and is
at least the generalization error for a loss-threshold attack, while stability alone
does not prevent it.

## Method

Experiment 1 draws $S\sim\mathcal D^n$, trains $A_S$, and hands the adversary a point
$z$ drawn from $S$ ($b=0$) or from $\mathcal D$ ($b=1$), together with $A_S$, $n$
and $\mathcal D$ itself. Definition 4 sets $\mathrm{Adv}^M=2\Pr[\text{correct}]-1$, the
gap between true- and false-positive rates. Because the adversary knows
$\mathcal D$, the experiment credits only what the model reveals. Attribute inference
(Experiment 2, Definition 5) gives the adversary partial information $\varphi(z)$
and asks for the sensitive part $\pi(z)$. §5 reduces membership to attribute
inference with no loss (Theorem 6) and attribute to membership through a
reconstruction function $\varphi^{-1}$ (Adversary 6, whose guarantee, Theorem 7,
this reading did not cover).

## What they measured, and on what

Theorem 1: an $\varepsilon$-DP learner gives $\mathrm{Adv}^M\le e^\varepsilon-1$.
Theorem 2: Adversary 1, which outputs $1$ with probability $\ell(A_S,z)/B$ for a loss
bounded by $B$, has advantage $R_{\mathrm{gen}}(A)/B$, the average generalization
error of Definition 3 over $B$. Theorem 3 gives the advantage of a likelihood test
on Gaussian regression errors with known $\sigma_S,\sigma_D$. Theorem 4: from any
ARO-stable rule one builds a rule with stability rate at most
$\epsilon_{\mathrm{stable}}(n)+knB2^{-d}+\mu(n,\mathcal D)$ and an adversary with
advantage $1-\mu(n,\mathcal D)-2^{-mk}$, by planting pseudorandom-function queries
known to a colluding adversary. §6 evaluates the attacks on regression and
classification datasets.

## Epistemic status

Proven, Theorems 1 to 4 and 6, with the proofs of Theorems 1, 2 and 6 read.
Theorems 5 and 7 were not read. Empirical, §6. The construction of Theorem 4 uses a secret
key shared between learner and adversary, which the authors call collusion.

## The limitation that matters to us

Stated by construction. The adversary receives the distribution, so the paper prices
neither samples nor training runs. Every bound is the informed end of the prices the
HE-ML theory studies. Theorem 4's leaky learner rests on a colluding key, a
cryptographic plug-in of the kind Halil's constraints exclude.

## Relationship to this project

Prior art. Its game is the base of LiRA's (CCNSTT22 Definition 1) and of HSU25's
sample-based game, which replaces $\mathcal D$ by $m$ samples.

## What we need to consider for our work

The space statistical-limits records Theorem 1 as
`fact-yeom-dp-bounds-membership-advantage` and Theorem 2 as
`fact-yeom-generalization-error-gives-advantage` (round-00 of
`lab/theory/spaces/statistical-limits/`). Definition 4 is the zero-baseline game of
the register entry `fact-yeom-membership-zero-baseline`, which this reading
confirms.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/YGFJ18_PrivacyRiskOverfitting.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/privacy-risk-overfitting.md`.
Mapping note: Held PDF is the unabridged arXiv v5 (4 May 2018).
Read on 2026-10-25 by the statistical-limits space session, sections listed at the top, and this note written from that reading.
