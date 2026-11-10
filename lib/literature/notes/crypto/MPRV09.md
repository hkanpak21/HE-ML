---
key: MPRV09
title: Computational Differential Privacy
authors: Ilya Mironov and Omkant Pandey and Omer Reingold and Salil Vadhan
venue: CRYPTO 2009
venue_evidence: Crossref 2026-10-27, DOI 10.1007/978-3-642-03356-8_8, Advances in Cryptology CRYPTO 2009, LNCS 5677, pp. 126-142
year: 2009
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven for the definitions and their relations, proven for the two-party protocols"
prov: sweep
---

# MPRV09, Computational Differential Privacy

## Claim

Differential privacy can be asked only of polynomial-time attackers, and this relaxation admits mechanisms, here two-party ones, that are more accurate than any mechanism private against an unbounded attacker appears to allow.

## Method

The paper gives two computational relaxations of DP. IND-CDP replaces the unbounded distinguisher of (ε, δ)-DP with a non-uniform polynomial-time one and allows negligible additive advantage, since without δ the change adds no mechanism in the non-uniform case. SIM-CDP asks that the attacker's view be computationally indistinguishable from a differentially private function of the database. SIM-CDP implies IND-CDP, the converse is left open, and a weaker simulation notion (SIM∀∃-CDP) is shown equivalent to IND-CDP through an extension of the dense model theorem of Reingold et al. Both notions compose sequentially and protect small groups. For the Hamming distance between two parties' bit vectors it gives one statistically private protocol with multiplicative error and two SIM-CDP protocols, semi-honest and malicious, with error independent of the vector length.

## What they measured, and on what

Proofs only. The attacker is the analyst, or in the two-party protocols each party against the other.

## Epistemic status

Proven, for the relations of Figure 1 and for the protocols. The separation it conjectures, Hamming distance in the two-party setting, is proven later by McGregor et al., FOCS 2010, which the paper cites as subsequent work.

## The limitation that matters to us

The computational relaxation buys accuracy here only through secure computation among several parties. Nothing in this paper separates the two attackers with a single curator, which Groce, Katz and Yerukhimovich (GKY11) later show to be hard for low-dimensional outputs. Found by us from the two papers.

## Relationship to this project

Prior art. It is the definitional root of every privacy notion that bounds the attacker by its computation, so any learner-class privacy notion is a variant of IND-CDP with another distinguisher class.

## What we need to consider for our work

A learner-class privacy definition should be stated in the IND-CDP form with the class in place of non-uniform polynomial time, and must say what replaces the dense model theorem if it wants a simulation form (fact-mprv09-class-relative-cdp-price).

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/MPRV09_ComputationalDP.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/computational-differential-privacy.md`.
Read on 2026-10-27 for the meeting of that day: abstract and Section 1 to Figure 1 and the two-party paragraph. Definitions, proofs and the protocols were not read. prov stays sweep, since the paper was not read in full.
