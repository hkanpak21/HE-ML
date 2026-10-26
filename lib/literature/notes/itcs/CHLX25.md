---
key: CHLX25
title: Backdoor defense, learnability and obfuscation
authors: Paul Christiano and Jacob Hilton and Victor Lecomte and Mark Xu
venue: ITCS 2025
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/backdoor-defense-learnability-obfuscation.md
year: 2025
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven, statistical characterization by VC dimension, computational obstruction from OWF and iO"
prov: full-read
---

# CHLX25, Backdoor defense, learnability and obfuscation

Read on 2026-10-25 by the hard-problem-mappings space session from the held copy
(arXiv v2): Section 3 (Definition 3.1 and its discussion), Section 4 (Theorem 4.1 and
the prediction-strategy definition), Section 5 (Definition 5.1, Corollary 5.2 with
its proof, Theorem 5.3, Conjecture 5.4, the special-cased example, Theorem 5.5). The
appendix proofs and Section 6 beyond the statement of Theorem 6.1 were not read.

## Claim

Backdoor defense, posed as detecting a backdoored function at its trigger, is
governed statistically by the VC dimension, is implied by efficient PAC learning,
can be strictly easier than learning, and is impossible for polynomial-size circuits
under one-way functions and indistinguishability obfuscation.

## Method

Definition 3.1: the attacker picks $D$ and $f\in F$, a trigger $x^*\sim D$ is
drawn, the attacker picks $f^*$, $\varepsilon$-valid if it differs from $f$ on mass at
most $\varepsilon$ and at $x^*$; the detector sees $(f,x)$ with $x\sim D$ or
$(f^*,x^*)$, with the representation and the example oracle, and must accept the
first and reject the second. Theorem 4.1: the best confidence is
$\max\{1/2,1-\Theta(\mathrm{VC}(F)\varepsilon)\}$, proven with the
Haussler-Littlestone-Warmuth prediction strategy. Corollary 5.2: efficient PAC
learnability implies efficient defendability (Definition 5.1 requires
$\varepsilon<1/p(n,1/\delta)$). Theorem 5.3: in the random oracle model some class is
efficiently defendable and not efficiently PAC learnable. Theorem 5.5: under OWF
and iO, polynomial-size circuits are not efficiently defendable, through
puncturable pseudorandom functions.

## What they measured, and on what

Proofs only.

## Epistemic status

Proven. Conjecture 5.4 (the standard-model version of Theorem 5.3 from OWF) is open.

## The limitation that matters to us

The game has no training procedure and no data law carrying hardness; the
computational obstruction is obfuscation, a primitive in the attacker's hands. Found
by me against the rule of `CONTEXT.md`.

## Relationship to this project

Prior art. Its Corollary 5.2 is a mapping of backdoor detection onto PAC learning in
the upper-bound direction (`fact-chlx25-defendability-characterization`).

## What we need to consider for our work

A detection lower bound that counts must come from the law of the model's
randomness or of the data, as in GKVZ22 Theorem 6.4 or BRV26, not from obfuscation.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/CHLX25_Defendability.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/backdoor-defense-learnability-obfuscation.md`.
Mapping note: PDF is arXiv v2 (18 Nov 2024); key year follows ITCS 2025 (LIPIcs 325).
Reading record: 2026-10-25, the hard-problem-mappings space session read the sections named at the top of this note, for lab/theory/spaces/hard-problem-mappings/round-00/builder.md.
