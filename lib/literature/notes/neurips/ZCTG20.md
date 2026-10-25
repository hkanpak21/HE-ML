---
key: ZCTG20
title: Trade-offs and Guarantees of Adversarial Representation Learning for Information Obfuscation
authors: Han Zhao and Jianfeng Chi and Yuan Tian and Geoffrey J. Gordon
venue: NeurIPS 2020
venue_evidence: first page (34th Conference on Neural Information Processing Systems, NeurIPS 2020); scan summary
year: 2020
type: theory
placed_on: 2026-10-25
placed_by: agent
triage: read
relation: prior-art
epistemic: "proven for Propositions 2.1 to 3.1, Lemmas 3.1 to 3.4 and Theorems 3.1 to 3.3, against attackers ranging over all classifiers; empirical for §4 on Adult and UTKFace"
prov: full-read
---

# ZCTG20, Trade-offs and Guarantees of Adversarial Representation Learning for Information Obfuscation

Read by the statistical-limits space session of the HE-ML theory on 2026-10-25,
from the library PDF, arXiv 1906.07902v3 of 25 October 2020. Read: the abstract,
§2 (Definitions 2.1 and 2.2, Propositions 2.1 and 2.2), §3 (the minimax
formulation, Proposition 3.1, Lemma 3.1, Theorem 3.1, Lemmas 3.2 to 3.4, Theorems
3.2 and 3.3), §4.1 and §4.2, and the appendix proofs of Theorems 3.2 and 3.3.
Skimmed: Appendix C, the experimental details.

## Claim

A feature map that keeps a target $Y$ predictable must leak any binary attribute
$A$ whose conditional target laws differ, and the trade-off is quantified by the
Jensen and Shannon divergence between the target's laws given $A=0$ and $A=1$.

## Method

The representation $Z=f(X)$ feeds a predictor $h$, and an attacker $h_A$ tries to
infer $A$ from $Z$. The attribute advantage (Definition 2.2) is the largest gap
$|\Pr(h_A=1\mid A=1)-\Pr(h_A=1\mid A=0)|$ over a class $\mathcal H_A$. When
$\mathcal H_A$ holds every classifier on $\mathcal Z$, that advantage is the total
variation between the two induced laws of $Z$. Lemma 3.2 is data processing for the
JS distance $d_{\mathrm{JS}}=\sqrt{D_{\mathrm{JS}}}$, and the key Lemma 3.4 uses the
triangle inequality through the predicted laws of $\hat Y$ to give
$d_{\mathrm{JS}}(\mathcal D_0^Y,\mathcal D_1^Y)\le\sqrt{\mathrm{Err}_0}+d_{\mathrm{JS}}(\mathcal D_0^f,\mathcal D_1^f)+\sqrt{\mathrm{Err}_1}$.
Theorem 3.1 bounds the error of any adversary that uses no external information
correlated with $A$ by $H^\ast/(2\lg(6/H^\ast))$ for $H^\ast=H(A\mid Z=f^\ast(X))$ at
the optimal map of the entropy formulation (3).

## What they measured, and on what

Theorem 3.2 gives
$\mathrm{ACC}_0+\mathrm{ACC}_1\le2-\frac13D_{\mathrm{JS}}(\mathcal D_0^Y,\mathcal D_1^Y)+\mathrm{ADV}(\mathcal H_A\circ f)$.
Theorem 3.3 gives, when $\mathrm{ADV}\le D_{\mathrm{JS}}(\mathcal D_0^Y,\mathcal D_1^Y)$,
$\mathrm{Err}_0+\mathrm{Err}_1\ge\frac12(d_{\mathrm{JS}}(\mathcal D_0^Y,\mathcal D_1^Y)-\sqrt{\mathrm{ADV}})^2$.
§4 compares nine methods (PPLS, PLDA, ALT-UP, MAX-ENT, GRL, PCA, plain training,
Laplace LDP and DP-SGD) on Adult (income as target, gender, age and education as
attributes) and UTKFace (gender as target, age and ethnicity as attributes), with
the bound of Theorem 3.1 computed from the adversary's cross-entropy as a proxy for
$H^\ast$, and finds no method that both hides the attribute and keeps accuracy.

## Epistemic status

Proven, the propositions, lemmas and theorems of §2 and §3, for attackers over all
classifiers. Empirical, §4, on two datasets. The computed bound of §4 replaces
$H^\ast$ by an attained cross-entropy, which the authors note because the global
optimum is not guaranteed. The paper marks this.

## The limitation that matters to us

Found. The theorems concern one binary attribute, not reconstruction of the input.
Every lower bound is information-theoretic, so it says nothing about a bounded
attacker, which the register entry `fact-zhao-class-inference-advantage` already
records.

## Relationship to this project

Prior art. Theorem 3.3 is the attribute form of the floor of
`conj-reconstruction-label-sandwich` in the space statistical-limits, where
accuracy of the head forces a reconstructor to recover at least the label's
class-conditional prior.

## What we need to consider for our work

The space records Theorems 3.2 and 3.3 as `fact-zhao-accuracy-forces-attribute-leakage`
(round-00 of `lab/theory/spaces/statistical-limits/`). A floor for reconstruction
must say what replaces the JS divergence of target laws, and the label baseline
$\bar\kappa(\eta)$ of the space's aim is that replacement.

## Provenance

Copied on 2026-10-25 from the literature scan of 2026-10-25 (arXiv 1906.07902) for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Read on 2026-10-25 by the statistical-limits space session, sections listed at the top, and this note written from that reading.
