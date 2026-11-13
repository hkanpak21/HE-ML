---
key: KSK26
title: "HE-OFT: Privacy-Preserving One-Shot Federated Fine-Tuning under Homomorphic Encryption"
authors: Halil İbrahim Kanpak, Sinem Sav, Alptekin Küpçü
venue: arXiv technical report 2610.08255 (submitted to IEEE TNSE)
venue_evidence: https://arxiv.org/abs/2610.08255
year: 2026
type: protocol
placed_on: 2026-10-16
placed_by: agent
triage: deep
relation: prior-art
epistemic: "proven for semi-honest simulation security and for input privacy against deviating clients with an honest server, both under a smudging hypothesis the measured configuration does not meet; proven necessity of an honest server; empirical for extraction cost and membership leakage on five tasks"
prov: full-read
---

# KSK26, HE-OFT

Read in full by the main agent on 2026-10-16 from the technical report source
(`HE-IFD/docs/paper/main-tr.tex`, commit 9d894ea): Introduction,
Preliminaries, Method, Security, the subsection on extraction and membership at
test time, and the limitations. The accuracy, heterogeneity and cost
subsections of the experiments were read by their headings only.

This is the group's own paper. HE-ML does not build on it, but the team is the
same, so HE-ML takes its terms from it (`CONTEXT.md`).

## Claim

A one-shot federated fine-tuning protocol under multiparty CKKS in which no
party ever holds a client's update, a training artifact or the trained head in
plaintext, and a querier learns one label per query up to an allowance Q.

## Method

Each of N clients fine-tunes, in plaintext, an adapter (the up-projection of a
LoRA whose down-projection is frozen at a public initialization) and a
classifier head on a frozen public backbone. The adapter stays local. The
client uploads Enc(diag(g_j) Δ_j) and Enc(g_j), where Δ_j is its head
displacement and g_j its per-class counts. The server adds the ciphertexts,
inverts the per-class totals under encryption, and holds the shared head only
as a ciphertext. The federation picks one of the two arrangements (shared head
over the bare backbone, or over each client's own adapter) with a
prior-weighted estimator and decrypts one index. A querier encrypts its own
features, the server applies the head and an encrypted tournament argmax,
masks all slots but the label (Algorithm 3 of the paper), and a quorum
key-switches the label to the querier.

## Threat model, in the paper's words and in the HE-ML interface

- Theorem 1. A static semi-honest adversary corrupts the server and up to t−1
  clients. Simulation security against the ideal functionality, whose leakage
  is the public parameters, the per-client sample counts n_j, the selected
  index and the phase signals. Assumes IND-CPA of t-out-of-N threshold CKKS
  against t−1 key shares (a circular-security assumption) and a smudging
  hypothesis on every key switch, refresh and decryption.
- Theorem 2 (content game). Up to t−1 clients deviate arbitrarily, the server
  is honest. A distinguish game between two equal-size datasets of one honest
  client that lead to the same selected index. Advantage at most negl plus
  δ(Q_tot), with Q_tot = (t−1)Q. It needs extractable commitments in key
  generation, and it holds for deviating messages that satisfy three readings
  (extractable plaintexts, bounded noise, features in the comparison domain).
  HE-OFT includes no zero-knowledge proofs that would enforce them. No
  correctness is claimed against deviating clients.
- Proposition "the query channel is no stronger than the head". A coalition
  with Q_tot label queries has advantage at most that of an adversary holding
  both shared heads in plaintext, δ(Q_tot) ≤ δ_wb. In the HE-ML interface this
  is the ordering of views: the label view is a post-processing of the head.
- Proposition "no plaintext gate from a ciphertext". A client's decision to
  contribute a decryption share cannot depend on the plaintext, so no protocol
  in which clients decrypt ciphertexts the server presents is secure against a
  malicious server. At four classes the whole head fits in one ciphertext.

In the interface of `lib/reports/2026-10-16-halil-adversary-interface.pdf`, the
paper proves a distinguish bound against deviating clients and states the
malicious server as necessary to exclude. Steering, a deviating client biasing
the shared head, is outside every claim and listed as future work (norm bounds
by zero-knowledge proof, or robust aggregation under encryption).

## What they measured, and on what

RoBERTa-base on four text tasks and ViT-B/16 on CIFAR-100. Label-only
extraction to fidelity 0.90 costs 1.2×10^4 to 2.0×10^5 queries, 16 to 260
times the cost from scores. The likelihood-ratio membership attack against both
heads in plaintext reaches AUC 0.49 to 0.53, with TPR at FPR 0.01 between
0.008 and 0.023, over 64 shadow federations and 2000 candidates. OSLO reaches
AUC 0.47 to 0.52. Gradient inversion, attribute inference and reconstruction
from weights are argued inapplicable.

## Epistemic status

Theorems 1 and 2 are proven under stated hypotheses. The paper itself reports
that the smudging hypothesis fails in the measured configuration: key switches
smudge at eight times the fresh-encryption noise, the served ciphertext carries
noise of standard deviation 2^12.9 to 2^16.8, and the scheme's rule is
2^(λ/2) times the ciphertext noise. It derives a repetition attack needing
about 5×10^5 identical queries at that setting, and recommends 2^25 smudging
with a duplicate-query check. δ_wb ≈ 0 is empirical on the five tasks.

## The limitation that matters to us

Three, the first two stated by the paper.

1. Malicious server is excluded, with a proof that it must be. Verifiable HE or
   a zero-knowledge proof of evaluation is the named remedy.
2. Integrity against deviating clients is not claimed. In particular nothing
   checks that the uploaded counts g_j agree with the public n_j or with the
   data, and each count weights the client's row in the coverage-weighted merge.
   This consequence for the counts is found by us, not stated.
3. A comment to reconcile, not a protocol issue. The serving code
   (`HE-OFT/fhe/serve_real.go`, the block before the key switch) zeroes every
   slot but the label, as Algorithm 3 states, and its `other_slots_max_abs`
   field checks that the mask left noise only. The header of `fhe/smudge.go`,
   the mode that measured the noise figures of the CPA-D subsection, calls the
   unmasked ciphertext "the one the implementation switches" and the masked one
   a diagnostic. One of the two comments is stale, and the noise figures should
   name which ciphertext they were measured on. An earlier reading in this
   session took the smudge.go comment at face value and was wrong.

Also unchecked: Hwang, Hwang, Kim, Lee and Song (HHKLS26) show that independent
per-party smudging in threshold CKKS fails simulation security even against
semi-honest parties. HE-OFT's Theorem 1 uses per-party smudging and does not
cite that paper.

## Relationship to this project

Prior art, and the group's own. It fixes the vocabulary HE-ML uses, and its
honest-server proposition is the boundary where the malicious-server question
of HE-ML starts.

## What we need to consider for our work

The step from semi-honest to malicious server is already proven impossible for
HE-OFT as specified. A next problem therefore lives either in the check that
restores the semi-honest view (verifiable evaluation, recomputation by a
checker, the route the paper names), or in steering by deviating clients, which
HE-OFT does not claim.
