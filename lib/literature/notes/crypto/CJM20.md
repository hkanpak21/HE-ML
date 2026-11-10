---
key: CJM20
title: Cryptanalytic Extraction of Neural Network Models
authors: Nicholas Carlini and Matthew Jagielski and Ilya Mironov
venue: CRYPTO 2020
venue_evidence: Crossref 2026-10-27, DOI 10.1007/978-3-030-56877-1_7, CRYPTO 2020 Part III, pp. 189-218
year: 2020
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "empirical for the extractions, heuristic for the query and time analysis"
prov: sweep
---

# CJM20, Cryptanalytic Extraction of Neural Network Models

## Claim

Model extraction of ReLU networks from an oracle is a cryptanalytic problem, and a differential attack at critical points recovers the parameters to floating-point precision with polynomially many queries.

## Method

The oracle returns real-valued outputs on chosen inputs with no side channel, and the attacker knows the architecture. Near a critical point exactly one ReLU changes sign, and the change in the output's gradient reveals that neuron's weights up to scale. Signs are recovered by search, which costs time exponential in the layer width.

## What they measured, and on what

Extraction of a 100,000-parameter MNIST network with 2^{21.5} queries in under an hour, worst-case error 2^{-25}, and of a 4,000-parameter network with 2^{18.5} queries, error 2^{-40.4}.

## Epistemic status

Empirical for the extractions. The polynomial query count and exponential time are properties of this attack and no lower bound is given.

## The limitation that matters to us

The exponential cost sits in one step of one attack, and Canales-Martínez et al. (CCHRSS24) removed it. Found by us from the two papers.

## Relationship to this project

Prior art. It shows the attacker's query budget and time budget separating, with the information available after polynomially many queries.

## What we need to consider for our work

Extraction is the case where the information is there and the open question was computation, the reverse of membership inference in HSU25.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/CJM20_CryptanalyticExtraction.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/cryptanalytic-extraction-nn.md`.
Mapping note: PDF is arXiv v2 (22 Jul 2020), no venue line.
Read on 2026-10-27 for the meeting of that day: abstract and Section 1 to Section 1.1. The attack sections and evaluation were not read. prov stays sweep, since the paper was not read in full.
