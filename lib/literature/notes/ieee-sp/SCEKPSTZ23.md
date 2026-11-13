---
key: SCEKPSTZ23
title: "SoK: Let the Privacy Games Begin! A Unified Treatment of Data Inference Privacy in Machine Learning"
authors: Ahmed Salem, Giovanni Cherubin, David Evans, Boris Köpf, Andrew Paverd, Anshuman Suri, Shruti Tople, Santiago Zanella-Béguelin
venue: IEEE S&P 2023
venue_evidence: https://sp2023.ieee-security.org/program-papers.html
year: 2023
type: SoK
placed_on: 2026-10-16
placed_by: agent
triage: deep
relation: prior-art
epistemic: "proven for every reduction and separation of its Fig. 1, by explicit adversaries and constructed training pipelines, with two results cited from Yeom et al. and one from Humphries et al.; no empirical result"
prov: full-read
---

# SCEKPSTZ23, "SoK: Let the Privacy Games Begin! A Unified Treatment of Data Inference Privacy in Machine Learning"

Read in full by the agent on 2026-10-16 from arXiv 2212.10986v2 (20 pages), at
Halil's request: every section, the appendix proofs (Theorems 3, 4, 5, 7 to 11
and 13) and the reference list. The arXiv comment and the IEEE S&P 2023
accepted-paper list give the venue. It was added by hand and is outside the
inclusion rule of the sweep, because it trains one model with one trainer
(`screening.csv` gives the reason).

## Claim

Five data inference risks of one trained model, membership inference,
attribute inference, property inference, DP distinguishability and data
reconstruction, fit one game anatomy, and explicit reductions with constants
and separations relate every ordered pair of them (Fig. 1).

## Method

A game is a probabilistic program over a training algorithm T, a data
distribution D and a dataset size n, in which a challenger samples the data,
trains T(S) and asks the adversary for a guess. The anatomy has four parts. The
first is the goal. The second is how the challenge and the training set are
selected: randomly sampled, externally provided, or adversarially chosen. The
third is the adversary's access to the model (a black-box oracle, possibly
label-only or query-bounded, white-box, or grey-box) and its auxiliary
information, usually the data distribution. The fourth is the measure of
success, advantage over a baseline, which the authors prefer to attack success
rate. Poisoning enters as a capability, the adversary choosing part of the
training set (Game 3), and never as a goal. Game G1 reduces to G2 when every
adversary against G2 gives one against G1 with at least c times its advantage
(Definition 2), so resilience transfers with a loss of c (Proposition 1). A
separation is a training pipeline that resists one game and is broken by the
other.

## What they measured, and on what

No experiments. Table II systematizes 18 games from the literature, found by a
Google Scholar sweep, as of August 2022, of peer-reviewed papers citing Wu et
al. (CSF 2016) or Yeom et al. (JCS 2020). The proven relations are these.
Membership and attribute inference reduce to each other, with a factor of one
over the number of attribute values in one direction (Theorems 1 and 2, cited
from Yeom et al.). DP distinguishability reduces to reconstruction with a
factor set by an anti-concentration bound on the prior (Theorem 3) and to
membership inference with no loss (Theorem 4). Reconstruction reduces to
membership inference with a factor of one over the support size of D (Theorem
5). Strong membership inference reduces to reconstruction (Theorem 13). Six
separations follow (Theorems 6 to 11): membership resilience implies none of
property, DP or reconstruction resilience, property resilience does not imply
membership resilience, and so on. Section V decomposes the mixture-model
membership game of Humphries et al. into a membership game plus a property game
(Theorem 12), by code-based game hops.

## Epistemic status

Proven. Each relation has a proof in Sec. IV or the appendix, and Theorems 1, 2
and Proposition 2 are cited, not reproved. The separations are information
theoretic and use toy pipelines: T(S) is the sum of a Bernoulli sample, with
Gaussian noise added for Theorem 11, and Theorem 9 uses a pipeline that
outputs the inputs of its training set. They show that no generic reduction exists. They say
nothing about how far apart the risks are for a deployed training algorithm.
The paper does not blur proven and empirical claims.

## The limitation that matters to us

Stated by the authors (Sec. VI-D): privacy games are sequential programs, they
do not express concurrent computation, and so they do not apply directly to
federated learning. They leave open whether process calculi could. Every game
has one challenger training one model on one dataset. No game has a protocol
among parties, a channel such as a sum or a ciphertext, a party that sets an
update or a decryption share, or steering as a goal.

Found by us: the paper orders goals at a fixed or typical threat model,
membership against attribute against reconstruction. The adversary interface
orders adversaries at a fixed goal. The two overlap only where a game varies
the adversary's capability at one goal. Examples are Theorem 4, the black-box
and white-box membership variants, and the remark before Theorem 4 that a more
capable adversary can simulate a less capable one. That remark is the
interface's order by post-processing of views, stated for one model.

## Relationship to this project

Prior art. It is the unification of inference games that the adversary
interface report named from memory and left unchecked, and it covers the
distinguish and invert half of the interface for one trained model. By its own
statement it does not cover the multi-party protocol, which is the part of the
interface that remains open.

## What we need to consider for our work

The open check in the boundary of the interface report
(`lib/reports/2026-10-16-halil-adversary-interface.pdf`) now has an answer. For
one trained model, the distinguish and invert goals, advantage over a baseline,
and reductions between games are theirs. Any novelty for the interface has to
come from the protocol graph, the channels, the choices of node arguments and
outputs, and the steer goal. Their anatomy terms (randomly sampled, externally
provided and adversarially chosen challenges, black-box, grey-box and white-box
access) should be mapped onto the interface's view and choices in `CONTEXT.md`
before either is used in writing. Their Theorem 7 construction, a summed
Bernoulli sample with membership advantage at most one over the square root of
n and perfect DP distinguishing advantage, is a template for a separation proof
at the distinguish goal.
