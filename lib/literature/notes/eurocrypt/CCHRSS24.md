---
key: CCHRSS24
title: Polynomial Time Cryptanalytic Extraction of Neural Network Models
authors: Isaac A. Canales-Martínez and Jorge Chávez-Saab and Anna Hambitzer and Francisco Rodríguez-Henríquez and Nitin Satpute and Adi Shamir
venue: EUROCRYPT 2024
venue_evidence: Crossref 2026-10-27, DOI 10.1007/978-3-031-58734-4_1, Advances in Cryptology EUROCRYPT 2024, pp. 3-33
year: 2024
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "heuristic for polynomial time, empirical for the CIFAR-10 extraction"
prov: sweep
---

# CCHRSS24, Polynomial Time Cryptanalytic Extraction of Neural Network Models

## Claim

All real parameters of a fully connected ReLU network can be extracted from black-box access with polynomially many queries and polynomial time.

## Method

The setting is that of Carlini et al.: known layer widths, chosen real inputs, logits or softmax outputs, and infinite-precision arithmetic in the analysis. The obstacle in the earlier attack was one sign per neuron. Neuron wiggling, a chosen-input attack that perturbs the input in few directions and reads slope and curvature of the output, finds these signs, with two other methods for the first two hidden layers and the last.

## What they measured, and on what

A CIFAR-10 network with 3072 inputs, 8 hidden layers of 256 neurons and about 1.2 million parameters. Sign recovery took about 30 minutes on a 256-core computer (32 minutes in Section 1), where the earlier approach searches 2^{256} sign patterns per layer. 64-bit floating point sufficed.

## Epistemic status

Heuristic for the polynomial bound. The authors qualify their claim that the attack always succeeds: neurons that almost never change sign and singular linear systems are excluded as unlucky events. Empirical for the run.

## The limitation that matters to us

Infinite precision in the analysis and real-valued outputs. The hard-label setting is a later Journal of Cryptology paper (CCH+26, listed on Crossref, not read). Stated by the authors.

## Relationship to this project

Prior art. It closes the time gap of CJM20 for full-output ReLU networks.

## What we need to consider for our work

A gap between information and computation for an attacker can be an artefact of one attack. Any separation we claim must come with a lower bound, not a slow attack.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/CCHRS24_CryptanalyticExtractionPoly.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/polynomial-time-cryptanalytic-extraction.md`.
Mapping note: Six authors, so the key is CCHRSS24, not the file-name CCHRS24. No venue line on the PDF; the wiki page names EUROCRYPT 2024 without a venue_evidence field.
Read on 2026-10-27 for the meeting of that day: abstract and Section 1 including the caveats paragraph. Sections 2 onward were not read. prov stays sweep, since the paper was not read in full.
