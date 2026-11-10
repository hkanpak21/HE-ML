---
key: CGZ24
title: Undetectable Watermarks for Language Models
authors: Miranda Christ and Sam Gunn and Or Zamir
venue: COLT 2024
venue_evidence: dblp COLT 2024 pp. 1125-1139, recorded in FS wiki undetectable-watermarks-lm.md
year: 2024
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven, from one-way functions, and the necessity of computational assumptions proven unconditionally"
prov: sweep
---

# CGZ24, Undetectable Watermarks for Language Models

## Claim

Watermarks for language models can be undetectable to every polynomial-time user from one-way functions, and no sound watermark is undetectable to an unbounded user.

## Method

The provider holds a secret key and samples text so that, without the key, outputs are computationally indistinguishable from the original model even under adaptive prompts. With the key, detection works on any contiguous substring of enough empirical entropy, and soundness keeps independently written text undetected. Lemma 4 shows that a distinguisher with polynomially many queries and time exponential in the key length tells the watermarked model from the original for any sound scheme. Theorem 10 shows that watermarking outputs of low empirical entropy is detectable with exp(t) queries and time.

## What they measured, and on what

Proofs only, plus a discussion of empirical removal attacks.

## Epistemic status

Proven. Section 6.2 gives a removal attack for prefix-specifiable models, called expensive by the authors, not read in detail.

## The limitation that matters to us

Undetectability is a property of the user's compute, so it says nothing about a user who learns the watermark statistically with exponential time. Stated by the authors (Section 5).

## Relationship to this project

Prior art. It is the case where the unbounded side is proven to fail, so the computational bound is necessary and not a convenience.

## What we need to consider for our work

Lemma 4 prices the unbounded attacker in queries and in time separately, polynomial and exponential. Our measure should keep the two separate in the same way.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/CGZ24_UndetectableWatermarks.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/undetectable-watermarks-lm.md`.
Mapping note: PDF is arXiv v1 (stamp 25 May 2023, dated 16 Jun 2023); key year follows COLT 2024 (wiki, dblp). Also IACR ePrint 2023/763.
Read on 2026-10-27 for the meeting of that day: abstract, Section 1 to the property list, Section 5 to the proof of Lemma 4, and the opening of Section 6.2. prov stays sweep, since the paper was not read in full.
