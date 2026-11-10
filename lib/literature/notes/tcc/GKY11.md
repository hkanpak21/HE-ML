---
key: GKY11
title: Limits of Computational Differential Privacy in the Client/Server Setting
authors: Adam Groce and Jonathan Katz and Arkady Yerukhimovich
venue: TCC 2011
venue_evidence: Crossref 2026-10-27, DOI 10.1007/978-3-642-19571-6_25, TCC 2011, LNCS 6597, pp. 417-431
year: 2011
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "proven for both negative results"
prov: sweep
---

# GKY11, Limits of Computational Differential Privacy in the Client/Server Setting

## Claim

With a single server holding the data, restricting the attacker to polynomial time gives no gain in utility or efficiency for low-dimensional queries or for black-box constructions from standard primitives.

## Method

The client poses queries and plays the attacker, the server holds the database. The paper first notes that best achievable utility cannot improve when the utility is efficiently computable, since the utility function itself would distinguish. It then studies efficiency. By the first result, any CDP mechanism built black-box from trapdoor permutations, collision-resistant hash functions or random oracles has a statistically private mechanism that is as efficient and as useful. By the second, for queries with output in R^n, n constant, and a natural class of utilities, any CDP mechanism converts into an SDP mechanism of about the same efficiency and utility. Both results hold for IND-CDP and SIM-CDP.

## What they measured, and on what

Proofs only.

## Epistemic status

Proven. The authors list query types outside their results and leave open whether CDP helps for other utilities or query classes.

## The limitation that matters to us

The barrier covers low-dimensional outputs and black-box constructions. Ghazi et al. (GIKKM23) evade it with a high-dimensional output (a circuit) and non-black-box use of obfuscation. Stated by both papers.

## Relationship to this project

Prior art. It is the barrier any separation of the two attackers with a single curator must evade.

## What we need to consider for our work

A learner-class attacker that sees a low-dimensional release, such as a loss or a label, falls under the same conversion argument unless the class is weaker than polynomial time. Our separations must say which side of this barrier they sit on.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/GKY11_LimitsCDPClientServer.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/limits-cdp-client-server.md`.
Mapping note: No venue line on the first page. Wiki takes the TCC 2011 attribution from citing papers, not from the PDF.
Read on 2026-10-27 for the meeting of that day: abstract, Section 1 and Section 1.1 up to the limitations paragraph. The proofs were not read. prov stays sweep, since the paper was not read in full.
