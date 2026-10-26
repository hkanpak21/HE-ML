---
key: CDGJMMSTT21
title: Is Private Learning Possible with Instance Encoding?
authors: Nicholas Carlini and Samuel Deng and Sanjam Garg and Somesh Jha and Saeed Mahloujifar and Mohammad Mahmoody and Shuang Song and Abhradeep Thakurta and Florian Tramèr
venue: IEEE S&P 2021
venue_evidence: scan summary, venue from recollection; confirmed at https://www.ieee-security.org/TC/SP2021/program-papers.html
year: 2021
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven barriers for distinguishing attacks with an encoder oracle, InstaHide attack empirical"
prov: full-read
---

# CDGJMMSTT21, Is Private Learning Possible with Instance Encoding?

Read on 2026-10-25 by the computational-limits space session from the held copy
(arXiv 2011.05315): Section 1.2 (the informal Theorems 1 and 2), Section 2
(Definitions 1 to 6) and Section 3 (Theorems 3 to 5, Definition 7, with their
discussions). Section 4 (the InstaHide attack) and the appendix proofs were read
by their headings only.

## Claim

Instance encoding cannot give indistinguishability privacy together with
useful accuracy: a learner with non-trivial accuracy on encoded data yields an
efficient attack that tells encodings of two inputs apart, unless the task is
learnable almost perfectly.

## Method

Definition 1: a dataset encoding $E$ maps a labelled dataset to an encoded one,
decomposable when instances and labels are encoded separately with shared
randomness (instance encoding), $r$-local when each encoded item depends on at
most $r$ records. Definition 2 and 3: accuracy on plain and on encoded
instances. Definitions 4 and 5: dataset and instance distinguishing games, where
the adversary picks two inputs of the same label and must tell which one was
encoded. Definition 6: instance recovering, outputting $x^*$ within distance
$\gamma$ of some record. Theorem 3: for two distinct, non-constant, balanced
concepts and $(0.51,\delta)$ plain accuracy, a dataset-distinguishing adversary
of advantage $(0.99-2\delta(n))/(3n)$ exists, running in about the learner's
time. Definition 7 and Theorem 4: for an $(m,\gamma)$-rich class and encoded
accuracy $(\epsilon,\delta)$, an instance distinguishing attack of advantage
$0.99-\epsilon(n)/\gamma$ with oracle access to $E(\cdot)$, the learner, the
concepts and a sampler for $D$, in expected time $O(m/(1-\delta(n)))$. Theorem 5:
for one balanced concept and a decomposable encoding with balanced encoded
accuracy, either an attack of advantage $1/2-\epsilon(m)-\tau$ in expected time
$O(m/\delta(m)+m/\tau^2)$ exists, or an efficient learner of accuracy $1-\tau$.

## What they measured, and on what

Proofs for the barriers, and a reconstruction of the InstaHide challenge
(Section 4) built on a similarity function that the barrier explains.

## Epistemic status

Proven for the barriers. The InstaHide attack is empirical. Section 2 states
that the results do not rule out privacy against instance-recovering attacks,
which need a context-dependent metric.

## The limitation that matters to us

The attacks of Theorems 4 and 5 call the encoder on chosen inputs. In split
learning that is the attacker who knows the seed or can submit inputs to the
client. A blind server has no such oracle. I found this from the oracle lists in
the theorem statements, the paper does not discuss it.

## Relationship to this project

Prior art and competitor for `conj-reconstruction-at-training-cost`: both say
that accuracy leaks. Theirs is a distinguishing attack with an encoder oracle,
the aim is a reconstruction priced by the generative exponent without one.

## What we need to consider for our work

Any claim that the server reconstructs what the model learns must be stated
against Theorems 4 and 5, with the absence of the encoder oracle and the
real-valued target as the differences. Their remark that recovering attacks are
not ruled out is the opening our blind reconstruction game takes.

## Provenance

Copied on 2026-10-25 from the literature scan of 2026-10-25 (arXiv 2011.05315) for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Mapping note: authors ordered alphabetically (first-page footnote)
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
Reading record: 2026-10-25, the hard-problem-mappings space session re-read Section 2 (Definitions 5 to 7) and Section 3 (Theorems 3 to 5 with their discussions) for lab/theory/spaces/hard-problem-mappings/round-00/builder.md, reading Theorem 5 as a dichotomy in which hardness of learning the concept yields an attack.
Reading record: 2026-10-25, the hard-problem-mappings space session read Appendix A.2 and A.3 (the proofs of Theorems 4 and 5) for lab/theory/spaces/hard-problem-mappings/round-01/builder.md. Both proofs bound a difference of acceptance probabilities, which is twice the advantage of Definition 5, and the proof of Theorem 5 prints the bound 1/2 - epsilon(m) - tau with the inequality sign reversed.
