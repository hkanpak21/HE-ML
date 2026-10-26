---
key: CCGJY20
title: Exploring Connections Between Active Learning and Model Extraction
authors: Varun Chandrasekaran and Kamalika Chaudhuri and Irene Giacomelli and Somesh Jha and Songbai Yan
venue: USENIX Security 2020
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/active-learning-model-extraction.md
year: 2020
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "Observation 1 proven by simulation, one direction only; Proposition 1 proven"
prov: full-read
---

# CCGJY20, Exploring Connections Between Active Learning and Model Extraction

Read on 2026-10-25 by the hard-problem-mappings space session from the held copy
(arXiv 1811.02054v6): Section 2.2 to the end of Definition 2, Section 3 (3.1 and
3.2: Experiment 1, Definition 3, Example 2, Observation 1 with its argument,
Examples 3 and 4), and the statement of Proposition 1 with Example 5 (Section 5).
The rest, including the appendix proofs, was read by headings only.

## Claim

Model extraction through a prediction interface is query-synthesis active learning:
any active learner that synthesizes its own queries is an extraction adversary with
the same query complexity, and randomizing the answers with a constant flip rate
below one half costs the adversary only a factor $8/(1-2\rho)^2$ and a logarithm.

## Method

Definition 2: an active learning system $(L,O)$ for a class $F$ interacts by
membership queries; in the query-synthesis (QS) scenario, for every $f^*\in F$,
$L$ with $q_L(\varepsilon,\delta)$ queries outputs $\hat f$ with
$\mathrm{Err}(\hat f)\le\varepsilon$ with probability $1-\delta$. Experiment 1 and
Definition 3: an adversary implements $\varepsilon$-extraction of complexity $q$ and
confidence $\gamma$ against $F$ if it outputs $\hat f$ with $\mathrm{Err}(\hat f)\le\varepsilon$
with probability at least $\gamma$ for every $f^*\in F$, using at most $q$ queries.
Observation 1: a QS active learner of query complexity $q_L(\varepsilon,\delta)$ is an
adversary implementing $\varepsilon$-extraction with complexity $q_L(\varepsilon,\delta)$
and confidence $1-\delta$; the argument is that the adversary runs the learner.
Proposition 1: against a server that returns a wrong label with probability
$\rho_D(f^*)<1/2$, repetition gives $\varepsilon$-extraction with confidence $1-2\delta$
and complexity $\frac{8}{(1-2\rho_D(f^*))^2}q(\varepsilon,\delta)\ln\frac{q(\varepsilon,\delta)}{\delta}$.

## What they measured, and on what

The observation is a definition-level argument; experiments on decision trees,
halfspaces and other MLaaS classes are reported in later sections (not read).

## Epistemic status

Observation 1 is proven by the one-line simulation. Proposition 1 is proven in
Appendix A.1.1 (not read). The direction is one way: the authors neither prove nor
claim that extraction hardness gives active-learning hardness.

## The limitation that matters to us

It is an upper-bound mapping only, in the query-synthesis scenario, with the
extractor choosing its inputs. It does not price learning-based extraction from
random inputs, where the hardness results live. Found by me.

## Relationship to this project

Prior art. It is the literature's extraction $\lhd$ active-learning mapping
(`fact-active-learning-is-extraction`), the chosen-query counterpart of the SQ
lower bound of `fact-jagielski-extraction-query-bounds`.

## What we need to consider for our work

An extraction separation stated for random inputs must say that chosen inputs break
it, through Observation 1 with an active learner for the class.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/CCG+20_ActiveLearningExtraction.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/active-learning-model-extraction.md`.
Mapping note: PDF is arXiv v6 (20 Nov 2019), no venue line; the wiki page names USENIX Security 2020 without a venue_evidence field.
Reading record: 2026-10-25, the hard-problem-mappings space session read the sections named at the top of this note, for lab/theory/spaces/hard-problem-mappings/round-01/builder.md.
