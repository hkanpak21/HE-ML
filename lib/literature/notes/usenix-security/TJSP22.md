---
key: TJSP22
title: On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning
authors: Anvith Thudi and Hengrui Jia and Ilia Shumailov and Nicolas Papernot
venue: USENIX Security 2022
venue_evidence: "first page: 'In 31st USENIX Security Symposium'"
year: 2022
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "Lemmas 1 to 4, Theorems 1 to 3 and Corollaries 1 and 2 proven for mean-sampler updates with i.i.d. data and adversarial batch size; the forging experiment empirical on LeNet5 and MNIST"
prov: full-read
---

# TJSP22, On the Necessity of Auditable Algorithmic Definitions for Machine Unlearning

Read by the agent on 2026-10-25 for the theory space `oracle-and-measurement`, from the library
PDF (16 pages). Read: the abstract, §1, §4 (forgeability, the forging map, Lemmas 1 to 4 and
Theorem 1), §5 (mean samplers, Theorem 2, Corollary 1, Theorem 3, Corollary 2) and §6 (the forging
attack on MNIST and its results). Skimmed: §2, §3 and §7.

## Claim

From the training log of minibatch SGD one cannot tell whether a given point was used, because a
disjoint dataset can reproduce the same log within any tolerance, so unlearning is definable only as a
claim about the algorithm that was run.

## Method

A log is a sequence of checkpoints and the data used at each step, valid at tolerance $\varepsilon$ when
each logged update is reproduced within $\varepsilon$. A forging map from logs on $D$ to logs on $D'$ keeps
every checkpoint and replaces each data point by one of $D'$ while staying within $\varepsilon$ (§4.1).
Theorem 1 characterizes the equivalence classes of datasets that forge each other at $\varepsilon=0$. For a
mean-sampler update, a gradient averaged over a batch of size $b$, Theorem 2 bounds below the probability
that an i.i.d. dataset $D'$ forges $D$ at $2\varepsilon$ in $\ell_2$, by a product of terms in
$\sigma^2_{\max}/(b\varepsilon^2)$, where $\sigma^2_{\max}$ is the largest trace of the per-example gradient
covariance over the logged states. Theorem 3 (Existence of Forging Adversary) lets the adversary choose $b$
and sample indefinitely, and proves that for every $\varepsilon>0$ almost every dataset lies in a larger one
that a disjoint dataset forges. Corollary 2 concludes that unlearning over logs of minibatch SGD is not
well defined.

## What they measured, and on what

LeNet5 on MNIST with SGD at learning rate 0.01 (§6). The attack picks, among $M$ random minibatches from
$D\setminus\{x^*\}$, the one whose update best matches a logged update that used $x^*$, at a cost of $M$
gradient steps per forged step, so $\mu NM$ steps to forge $\mu$ points over $N$ epochs. The verification
error stays near $10^{-6}$ across dataset sizes at batch size 1,000 (Fig. 1) and falls with batch size,
roughly as $1/b$ (Fig. 2), before hardware noise.

## Epistemic status

Proven, the lemmas, theorems and corollaries, inside the mean-sampler model with i.i.d. data and a free
batch size. Empirical, the forging errors of §6. The paper says the attack need not pass every proof of
learning scheme (§6), so it does not overclaim.

## The limitation that matters to us

Found by us. The forger chooses the batches and the batch size. Nothing in the setting fixes the batch order
in advance. That freedom is part of the seed in the HE-ML oracle model.

## Relationship to this project

Prior art for `thm-replay-audit-steer` of the HE-ML oracle theory. A replay at a seed that a random oracle
derives from a committed dataset fixes the batch order, which takes away the freedom Theorem 3 uses.

## What we need to consider for our work

Recorded as the verified form of fact-unlearning-algorithm-level in
`lab/theory/spaces/oracle-and-measurement/round-00/builder.md`, with pointers Theorems 2 and 3 and
Corollary 2.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/TJSP22_AuditableUnlearningDefs.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/auditable-unlearning-definitions.md`.
