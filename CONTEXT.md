# HE-ML

Started 2026-10-16. Literature study only. The venue in `paper/.paper-meta.yml`
(acm-ccs) is a placeholder, because the scaffold requires one. No venue is chosen.

## What this is

A survey of how multi-party learning states its threat models, and of the
recent work at top venues under each one. Federated learning dominates the
field, but the study keeps the setting abstract: a set of data owners, possibly
an aggregator, and a training protocol among them. The group's prior work
assumes semi-honest parties (multiparty and threshold CKKS for federated and
split learning). The question is where the field stands once some parties are
malicious.

Venue rule, from Halil on 2026-10-16: top venues only. The working list, open to
his correction, is IEEE S&P, USENIX Security, ACM CCS, NDSS and PoPETs on the security
and privacy side, CRYPTO, EUROCRYPT and ASIACRYPT for protocols, and NeurIPS,
ICML and ICLR on the learning side. A notable paper at another venue is recorded
in `lib/literature/sources.yml` under `excluded` and gets no PDF.

## The claim

None yet. The study comes first.

## People

One row per person. The handle is the one lowercase word that names them in
issue and report file names, `<opened>-<assignee>-<headline>.md` and
`<date>-<author>-<headline>.pdf`.

| Handle | Name | Role |
| --- | --- | --- |
| halil | Halil İbrahim Kanpak | author |

## Terminology ledger

One name for one thing. Every term fixed here is used nowhere else by another
name, in the paper, the code, the figures, or a report.

HE-ML speaks the language of HE-OFT (KSK26), because the team is the same. The
first block is taken from the HE-OFT ledger (`HE-IFD/docs/CONTEXT.md`) and the
paper, unchanged. The second block is the adversary interface of
`lib/reports/2026-10-16-halil-adversary-interface.pdf`, fixed 2026-10-16.

| Term | Means | Never called |
| --- | --- | --- |
| backbone | the frozen public pretrained model, the map from an input to its features | the encoder, the base model |
| adapter | a client's trained up-projection of a LoRA whose down-projection is frozen at a public initialization, kept local | the LoRA, the client model |
| head | a linear map from the features to the class logits | the classifier layer |
| head displacement | a client's trained head minus the public initializer | the delta, the contribution |
| update | the thing a client sends | quantity, fresh quantity, contribution as a synonym |
| shared head | the merged head, held only as a ciphertext | the global model, the final model |
| the two arrangements | the shared head over a client's own adapter, or over the bare backbone | introduced before it is defined |
| querier | the client that sends a query | the user |
| quorum | any t clients, enough to decrypt | the committee |
| allowance | the per-client number of answered queries, Q | the budget, when the allowance is meant |
| the server | the one party that merges and answers queries | the aggregator and the serving party as two parties |
| semi-honest | the threat model term | honest-but-curious |
| deviating | a party that departs from the protocol arbitrarily | Byzantine, when a client of HE-OFT is meant |
| confidentiality | what encryption gives an update, a head or a query | privacy of a ciphertext |
| privacy | the training data, and what an adversary learns about it | the protocol's secrecy guarantee |
| local | never transmitted | private, as a synonym |
| plaintext, ciphertext | always | in the clear, public for unencrypted |
| dataset | a finite multiset of labeled examples, D_j for client j and D_pre for pretraining | the data, the corpus |
| learning function | a randomized map from a dataset and a starting point to a model | the training algorithm, the optimizer |
| hypothesis class | the set of models a learning function can output | the model family |
| model | one member of the hypothesis class, given by its parameters | the network, the weights, as a synonym |
| view | everything an adversary sees, each value through its channel, plus its query answers | observations, access |
| choices | the protocol inputs an adversary sets | capabilities |
| distinguish | the goal of telling two hypotheses about the datasets apart, played by a discriminator | membership inference, property inference, as names |
| invert | the goal of recovering a target from the view within a tolerance, function inversion | reconstruction, extraction, as names |
| steer | the goal of choosing inputs so the trained model lands in a target set | poisoning, backdoor, as names |
| collapse | a weaker adversary attains the stronger one's best value at a fixed goal | equivalence |
| separation | a construction where the stronger adversary does much better at a fixed goal | gap, as a name |

## Symbols

Every symbol and every invented label the paper uses, defined once.

HE-OFT's symbols are kept with their meaning. The interface adds the rest.

| Symbol | Means | Defined in |
| --- | --- | --- |
| N, C, d | numbers of clients and classes, feature dimension | KSK26 |
| j | client index | KSK26 |
| D_j, n_j, n_{j,c} | client j's dataset, its size, its count of class c | KSK26 |
| D_0, D_1 | the two challenge datasets of the content game, never the pretraining set | KSK26 |
| D_pre | the pretraining dataset | interface report |
| φ, φ_j | the backbone, and the backbone with client j's adapter A_j | KSK26 |
| θ_0, h_j, Δ_j | public head initializer, client j's head, Δ_j = h_j − θ_0 | KSK26 |
| g_j | client j's per-class counts | KSK26 |
| θ* | the shared head | KSK26 |
| Enc | encryption under the collective public key | KSK26 |
| t, Q | decryption threshold, per-client allowance | KSK26 |
| Θ, H, h_θ | parameter space, hypothesis class, the model with parameters θ | interface report |
| A, U, M | learning function, update map U(D; θ) = A(D; θ) − θ, merge | interface report |
| View, C | an adversary's view and its choices | interface report |

## Current state

2026-10-16. 44 papers placed in Drive with notes, coded in
`lib/literature/catalog.md`. One note is a full reading (KSK26), the rest are
built from sweep extractions. The adversary interface is drafted in
`lib/reports/2026-10-16-halil-adversary-interface.pdf`. Its novelty against
Salem et al. (S&P 2023) is unchecked. No direction is chosen.

## Recorded deferrals

FILL, or delete this section. A thing left out on purpose, with the ruling or
the issue that records the decision. A reviewer finding that matches a line
here is a decision and not an oversight.

## Conventions specific to this project

FILL, or delete this section. The general ones are in
`~/.claude/skills/research/references/conventions.md`.
