---
key: AZT24
title: Evaluations of Machine Learning Privacy Defenses are Misleading
authors: Michael Aerni and Jie Zhang and Florian Tramèr
venue: ACM CCS 2024
venue_evidence: first page
year: 2024
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven for the name-and-shame bound, empirical for the CIFAR-10 measurements and the five case studies"
prov: sweep
---

# AZT24, Evaluations of Machine Learning Privacy Defenses are Misleading

## Claim

Membership inference success aggregated over a data population can certify a defense that leaks one record completely, so an empirical privacy evaluation has to measure the most vulnerable records, with an attack adapted to the defense, against a DP-SGD baseline tuned to the same utility.

## Method

The name-and-shame mechanism outputs whether one fixed record is in the training set. Over an evaluation set D, every attack then has population TPR at most FPR plus 1/|D|, so the defense looks more private as D grows while that record has no privacy at all. The proposed protocol (Section 4) has three points: report TPR at low FPR for the most vulnerable sample, approximated by auditing canaries that mimic it, use LiRA adapted to the defense, and compare with a state-of-the-art DP-SGD at similar utility.

## What they measured, and on what

CIFAR-10, a victim trained on 25,000 points, LiRA with 64 shadow models. Sample-level rates come from 20,000 retrainings on random halves. The most vulnerable sample has TPR 99.9% at 0.1% FPR where the population metric reports 4% (Section 4.1). Across five empirical defenses at accuracy of at least 88%, prior evaluations underestimate leakage by an order of magnitude, and a tuned DP-SGD with vacuous provable guarantees beats all five empirically (abstract and Figure 1, case studies not read).

## Epistemic status

The name-and-shame bound is proven by counting. The CIFAR-10 numbers and the defense ranking are empirical. The canary set approximates the most vulnerable sample, which the authors state as an approximation.

## The limitation that matters to us

Centralized training and membership only. In federated learning the unit of the most vulnerable case is undefined: a record, a client, or a round. Found by us.

## Relationship to this project

Prior art. It is the evaluation protocol the measured side of a distinguish objective adopts.

## What we need to consider for our work

Every distinguish objective reports the worst record next to the population rate, and every empirical defense is compared with a tuned DP-SGD at matched utility. The federated analogue of the most vulnerable sample needs a definition before any measurement.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/AZT24_PrivacyDefensesMisleading.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/privacy-defense-evaluations-misleading.md`.
Mapping note: First page ACM reference: CCS '24, DOI 10.1145/3658644.3690194.
Read on 2026-11-11 for the discussion of metrics: abstract, Figure 1, Sections 1, 2.1, 2.2, 4 and 4.1. Section 5, the case studies, was not read. prov stays sweep.
