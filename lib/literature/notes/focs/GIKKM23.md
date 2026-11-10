---
key: GIKKM23
title: Towards Separating Computational and Statistical Differential Privacy
authors: Badih Ghazi and Rahul Ilango and Pritish Kamath and Ravi Kumar and Pasin Manurangsi
venue: FOCS 2023
venue_evidence: dblp record recorded in FS wiki towards-separating-cdp.md, FOCS 2023 pp. 580-599, DOI 10.1109/FOCS57990.2023.00042
year: 2023
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven under NIWI, laconic keyless CRHF and diO for public-coin samplers"
prov: sweep
---

# GIKKM23, Towards Separating Computational and Statistical Differential Privacy

## Claim

There is a task with a single curator that an ε-CDP mechanism with constant ε solves at utility 1 − o(1), while no (ε, δ)-SDP mechanism of constant utility exists, efficient or not, unless ε is super-constant or δ inverse-polynomial.

## Method

A task is an efficiently computable utility u(D, y). The low diameter set problem asks for a circuit that accepts the n-bit dataset D and rejects every point at Hamming distance above τ. Blatant non-privacy rules this out for SDP with a non-constructive argument that yields no efficient attacker, which leaves room for CDP. The CDP mechanism outputs an obfuscated circuit. It is private against non-adaptive decision-tree attackers through randomized response, and collision-resistant keyless hashing restricts the datasets to a set R of strings hashing to zero, so that a polynomial-time attacker behaves like a non-adaptive one. Differing-inputs obfuscation then lifts privacy from query attackers to polynomial-time attackers.

## What they measured, and on what

Proofs only.

## Epistemic status

Proven under the three assumptions named. The task is built for the separation, and the authors name high dimensionality and non-standard cryptography as the two barriers any separation must pass.

## The limitation that matters to us

The separating task is constructed, and the root records that the mechanism is not CDP against quasi-polynomial attackers (fact-gikkm23-breaks-quasipoly-adversaries, not verified in this reading). A natural task remains open.

## Relationship to this project

Prior art. It is the only single-curator separation of SDP and CDP in the library, and its lift from a restricted query class to polynomial time is the pattern a learner-class definition could reuse (fact-gikkm23-restricted-class-lift).

## What we need to consider for our work

The two-step proof, privacy against a weak query class and then a lift, is a template for pricing a learner-class attacker. The lift needs obfuscation, which a learning setup does not supply.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/GIKKM23_TowardsSeparatingCDP.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/towards-separating-cdp.md`.
Read on 2026-10-27 for the meeting of that day: abstract, Section I and Section II-A to II-C. Sections III to VII were not read. prov stays sweep, since the paper was not read in full.
