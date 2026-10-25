---
key: LZA21
title: Why Are Convolutional Nets More Sample-Efficient than Fully-Connected Nets?
authors: Zhiyuan Li, Yi Zhang, Sanjeev Arora
venue: ICLR 2021
venue_evidence: given by the discussant astra in lab/theory/spaces/computational-limits/round-00/discussant-astra.md; the arXiv HTML page (2010.08515v2, 4 May 2021) names no venue, so the venue is not confirmed from the paper
year: 2021
type: conference
placed_on: none, the PDF is not in the library
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven"
prov: full-read
---

# LZA21, Why Are Convolutional Nets More Sample-Efficient than Fully-Connected Nets?

Read on 2026-10-25 by the computational-limits space session from the arXiv HTML
page of arXiv 2010.08515v2, through a fetch tool that paraphrases formulas.
Read: Definition 3.2, Theorems 5.2, 5.3 and 5.5 by their statements, Appendix C
to Theorem C.1, Remark C.1, Corollary C.2, Remark C.2, Corollary C.5, and Table 1.
The proofs of Section 5 and the remaining appendices were not read.

## Claim

Training a fully connected network by gradient methods from a rotation-invariant
initialization is an orthogonally equivariant algorithm, and every such
algorithm needs $\Omega(d^2)$ samples on a simple quadratic task that a
convolutional network learns with a number of samples independent of $d$.

## Method

Definition 3.2: an algorithm $A$ is $G$-equivariant if, for every dataset and
every $g\in G$, $A(\{(g(x_i),y_i)\})\circ g=A(\{(x_i,y_i)\})$, in distribution for
randomized algorithms. Theorem C.1 gives sufficient conditions for an iterative
algorithm: a group $G_W$ acting on the weights through an isomorphism
$\tau:G\to G_W$ with $M[\tau(g)W](g(x))=M[W](x)$, an update rule invariant under the
joint action, and an initialization law invariant under $G_W$. The proof shows by
induction that the iterates on transformed data are $\tau(g)$ applied to the
iterates on the original data. Remark C.1 extends this to stochastic updates and
to updates that depend on the whole trajectory. Corollary C.2: (stochastic)
gradient descent on a fully connected network from i.i.d. Gaussian
initialization is orthogonally equivariant. Remark C.2: momentum, and $\ell_p$
regularization for the permutation and sign-flip groups. Corollary C.5: Newton's
method with zero first-layer initialization is equivariant under invertible
linear maps. Table 1: Adam and AdaGrad are permutation and sign-flip
equivariant, not orthogonally equivariant.

## What they measured, and on what

Theorem 5.2: for $h^*=\mathrm{sign}(\sum_{i\le d}x_i^2-\sum_{d<i\le2d}x_i^2)$ with
Gaussian inputs, every orthogonally equivariant algorithm needs $\Omega(d^2)$
samples for constant error, while a two-layer convolutional network needs
$O(\frac1\varepsilon(\log\frac1\varepsilon+\log\frac1\delta))$. Theorem 5.3
gives $\Omega(d^2/\varepsilon)$ for labels $\mathrm{sign}(\sum\alpha_ix_i^2)$. Theorem
5.5 gives $d/10$ for permutation-equivariant algorithms on a local-texture task.
Experiments are not part of what I read.

## Epistemic status

Proven.

## The limitation that matters to us

The equivariance is a statement about the law of the learned function on
transformed data. It does not state the joint law of a full training transcript
with the data, and it has no attacker. My finding.

## Relationship to this project

Prior art for the symmetry mechanism of `lem-equivariant-view-coupling` in the
computational-limits space, which applies the same induction to the split
learning server's whole view, to an adaptive server and to side data, and uses it
as a reduction from a blind attacker to non-Gaussian component analysis.

## What we need to consider for our work

Credit the induction to Theorem C.1 wherever the coupling lemma is stated. The
optimizer list of Table 1 is the list of protocols the seed separation covers
(SGD, momentum) and does not cover (Adam, AdaGrad). Place the PDF and confirm the
venue before citing it in prose.

## Provenance

Not placed. Read on the web at https://arxiv.org/html/2010.08515 on 2026-10-25.
Reading record: 2026-10-25, the computational-limits space session, for
lab/theory/spaces/computational-limits/round-01/builder.md.
