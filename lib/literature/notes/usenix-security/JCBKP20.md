---
key: JCBKP20
title: High Accuracy and High Fidelity Extraction of Neural Networks
authors: Matthew Jagielski and Nicholas Carlini and David Berthelot and Alex Kurakin and Nicolas Papernot
venue: USENIX Security 2020
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/jagielski-model-extraction.md
year: 2020
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "Theorems 1 and 2 proven, Theorem 3 informal, imported from DGKP20 with a misprinted exponent"
prov: full-read
---

# JCBKP20, High Accuracy and High Fidelity Extraction of Neural Networks

Read on 2026-10-25 by the hard-problem-mappings space session from the held copy:
Section 3 (3.1 to 3.4, the taxonomy of goals, the three hardness arguments and the
adversary capabilities), the opening of Section 6 (the functionally equivalent
attack and its assumptions), and Appendix A (formal Theorems 1 and 2 with
Definition A.1 and Lemmas 1 and 2). Sections 4, 5 and 7 and Appendix B were read by
their headings only.

## Claim

Extraction has a spectrum of goals, from exact through functionally equivalent and
fidelity to task-accuracy extraction, and the strong goals are provably hard in the
worst case while learning-based extraction inherits the SQ hardness of random deep
networks, so practical attacks must exploit structure (chosen queries on two-layer
ReLU networks, or learning for accuracy).

## Method

Section 3.2 defines functionally equivalent extraction ($\hat O(x)=O(x)$ for all
$x$) and fidelity extraction (maximize $\Pr_{x\sim D_F}[S(\hat O(x),O(x))]$ with
$S$ label agreement). Section 3.3 gives three arguments. Theorem 1 (formal in
Appendix A): a class of width-$3k$ depth-2 ReLU networks on $[0,1]^d$ with
precision-$p$ inputs, $d\ge k$, needs $\Theta(p^k)$ logit queries to extract; the
proof builds $k$-rectangle bounded functions (Definition A.1) from 3-ReLU gadgets
(Lemma 1) and shows each query rules out at most one of $p^k$ disjoint rectangles
(Lemma 2). Theorem 2: testing functional equivalence of two networks on
$\{0,1\}^d$ given their weights is NP-hard, by a reduction from subset sum (one
network is zero, the other is nonzero exactly on inputs whose subset sums hit the
target). Theorem 3 is informal only: random networks with domain $\{0,1\}^d$, range
$\{0,1\}$ and depth $h$ "require $\exp(O(h))$ samples to learn in the SQ learning
model", citing Das et al. [27]; the text says SQ-expressible fidelity extraction
inherits this. The adversary of Section 6 has logit access and chooses its queries.

## What they measured, and on what

The hardness results are proofs. The attacks (Sections 5 and 6) are measured on
image classifiers, the functionally equivalent attack on two-layer ReLU networks
with logit access in 64-bit floats.

## Epistemic status

Theorems 1 and 2 are proven in Appendix A. Theorem 3 is quoted informally with no
formal version in the paper; its exponent is printed as $\exp(O(h))$, while its
source (DGKP20 Lemma 12 with Theorem 15) gives $e^{\Omega(h)}$, so $O$ is a
misprint (my reading). The claim that most learning-based extraction is SQ is
heuristic.

## The limitation that matters to us

Theorem 1 is worst case over constructed networks and Theorem 3 is about untrained
random networks seen through random inputs, so neither prices the extraction of a
trained model in the trainer's units. Found by me, the paper does not discuss it.

## Relationship to this project

Prior art. It is the reference every extraction lower bound must be stated against
(`fact-jagielski-extraction-query-bounds`), and its learning-based extraction class
is the game of `conj-extraction-priced-by-generative-exponent`.

## What we need to consider for our work

An extraction mapping must say whether the extractor chooses its queries. With
chosen queries the SQ bound says nothing; the separation the space aims at lives in
learning-based extraction from random inputs.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/JCB+20_ExtractionAccuracyFidelity.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/jagielski-model-extraction.md`.
Reading record: 2026-10-25, the hard-problem-mappings space session read the sections named at the top of this note, for lab/theory/spaces/hard-problem-mappings/round-00/builder.md.
