---
key: GJMM20
title: Adversarially Robust Learning Could Leverage Computational Hardness
authors: Sanjam Garg and Somesh Jha and Saeed Mahloujifar and Mohammad Mahmoody
venue: ALT 2020
venue_evidence: PMLR v117 garg20a and dblp conf/alt/GargJMM20, recorded in FS wiki computational-hardness-robust-learning.md
year: 2020
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven, from exponentially hard one-way functions for the separation, and the converse unconditional"
prov: sweep
---

# GJMM20, Adversarially Robust Learning Could Leverage Computational Hardness

## Claim

Some learning tasks have classifiers that are robust against polynomial-time attackers and not against unbounded ones, and any such gap on an efficiently samplable task yields average-case hard problems in NP.

## Method

In the game, the challenger trains h on samples and draws a test instance x, and the attacker with oracle access to h and x outputs a nearby x' that h misclassifies. Computational risk restricts the attacker class to polynomial time. Each instance carries a short signature of polylogarithmic length, so a nearby misclassified instance requires a forgery. An unbounded attacker forges and a polynomial-time one cannot. Theorem 8 lets the classifier output a tamper symbol and keeps computational risk at α while unbounded risk rises to about β. Theorem 14 has binary labels with computational risk near 0 and unbounded risk near 1/2. Theorem 18 is the converse to hardness in NP.

## What they measured, and on what

Proofs only, with Hamming (ℓ0) perturbations.

## Epistemic status

Proven. Short signatures need exponentially hard one-way functions. The constructed tasks append a signature to the instance, so they say nothing about natural data.

## The limitation that matters to us

The hard object is planted in the instance by the designer, which is the kind of hardness Halil ruled out for our line on 27 October. The authors leave natural tasks such as image classification open.

## Relationship to this project

Prior art. It is the cleanest statement that one classifier has two risks, one per attacker class, and its game is the template for a class-indexed robustness risk.

## What we need to consider for our work

Definition 1 quantifies over a class of attackers and the authors say other classes may be used. Replacing polynomial time by a learner class gives our notion directly, and the converse of Theorem 18 tells what a gap would imply.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/GJMM20_RobustLearningCompHardness.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/computational-hardness-robust-learning.md`.
Mapping note: Held PDF is arXiv v2 (19 Dec 2019) in the PMLR layout.
Read on 2026-10-27 for the meeting of that day: abstract, Section 1 and Section 1.1 to the converse paragraph, and the signature construction overview. The theorems' proofs were not read. prov stays sweep, since the paper was not read in full.
