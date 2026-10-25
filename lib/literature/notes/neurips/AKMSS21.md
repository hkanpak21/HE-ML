---
key: AKMSS21
title: On the Power of Differentiable Learning versus PAC and SQ Learning
authors: Emmanuel Abbe and Pritish Kamath and Eran Malach and Colin Sandon and Nathan Srebro
venue: NeurIPS 2021
venue_evidence: scan summary; https://neurips.cc/virtual/2021/poster/28536
year: 2021
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: tool
epistemic: "proven, in an abstract rounding model whose last bit is adversarial"
prov: full-read
---

# AKMSS21, On the Power of Differentiable Learning versus PAC and SQ Learning

Read on 2026-10-25 by the computational-limits space session from the held copy
(arXiv 2108.04190v2): the abstract, Section 1, Section 2 (the learning
paradigms and the definition of error) and the statements of Section 3
(Theorems 1a to 1d). The proofs in Sections 4 to 6 and the appendices were not
read.

## Claim

The power of mini-batch SGD on a differentiable model is fixed by the batch size
$b$ against the gradient precision $\rho$: with $b\rho^2$ large SGD is no more
powerful than statistical queries, with $b\rho<1/8$ it simulates any sample-based
learner, and it always simulates SQ.

## Method

bSGD($T,\rho,b,p,r$) (equations 1 to 3): $w^{(t+1)}=w^{(t)}-\gamma g_t$, with
$g_t$ a $\rho$-approximate rounding of the clipped mini-batch gradient on $b$
fresh samples, meaning $g_t\in\rho\mathbb Z^p$ and
$\|g_t-\nabla L_{S_t}\|_\infty\le3\rho/4$. The error of a method is
$E[\sup L_D(f_{w^{(T)}})]$, the supremum over all valid roundings, so the rounding
is adversarial. SQ($k,\tau,r$) is $k$ adaptive queries with error
$E_R[\sup L_D(f)]$ over valid answers. The relation $C'\succeq_\delta C$ means
every method of $C$ has a method of $C'$ with error at most $\delta$ more on every
source distribution (Definition 1). The simulations go through an intermediate
mini-batch SQ model, answered by empirical averages on fresh batches, and a
sample-extraction procedure.

## What they measured, and on what

A proof. Theorem 1a: for all $b$ and $\rho<1/(8b)$, bSGD with
$T'=O(mn/\delta)$ steps and $p'=r+O(T'(n+\log b))$ parameters simulates any
PAC($m,r$) method up to $\delta$, and with a fixed activation and
$\rho<\min\{1/(8b),1/12\}$ the network has polynomial size for polynomial-time
methods. Theorem 1b: PAC with $Tb$ samples simulates bSGD exactly. Theorem 1c:
there is a constant $C$ such that $b\rho^2>C\log(Tp/\delta)$ gives
SQ($Tp,\rho/8,r$) $\succeq_\delta$ bSGD($T,\rho,b,p,r$), with a polynomial-time
version for neural networks with polynomial-time activations. Theorem 1d: bSGD
with $\rho=\tau/16$ and $T'=k\lceil C\log(k/\delta)/(b\tau^2)\rceil$ simulates any
SQ($k,\tau,r$) method. Inputs are $\{0,1\}^n$ and labels $\{0,1\}$ throughout.

## Epistemic status

Proven. The rounding model is an abstraction of finite precision, with an
adversary choosing the last bit, which the paper states. The intermediate regime
between $1/\rho$ and $\log(n)/\rho^2$ is left open by the paper.

## The limitation that matters to us

An SQ lower bound on an attack task binds an SGD-trained attacker only in the
regime of Theorem 1c, and only for the worst-case rounding that the error
definition takes. At single precision, with gradients clipped to $[-1,1]$, the
rounding step is near $2^{-24}$, so $b\rho^2\ll1$ for every batch in use and the
PAC regime of Theorem 1a applies. That reading identifies the paper's absolute
rounding with floating point, which rounds relative to magnitude, so it is my
heuristic, not the paper's statement.

## Relationship to this project

Prior art and a constraint. It fixes when the attacker class "statistical
queries" covers attackers trained by gradient methods, which decides the
attacker class for lower bounds (decision 3 of `sink/formalizing/STATE.md`).

## What we need to consider for our work

Any lower bound stated against SQ attackers must name the regime of Theorem 1c
and the worst-case rounding, and should come with a polynomial-time reduction
beside it, since the SQ bound alone does not bind a fine-precision SGD attacker.
The constructed models of Theorem 1a are engineered networks, so whether natural
architectures trained by SGD behave like SQ at fine precision is a separate,
empirical question.

## Provenance

Copied on 2026-10-25 from the literature scan of 2026-10-25 (arXiv 2108.04190) for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Mapping note: held copy is arXiv v2 dated 6 Feb 2022; key year follows the NeurIPS 2021 venue
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
