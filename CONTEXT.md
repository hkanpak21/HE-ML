# HE-ML

Started 2026-10-16 as a survey of threat models in multi-party learning.
Restarted 2026-11-11 as a deep-learning-first study. The venue in
`paper/.paper-meta.yml` (acm-ccs) is a placeholder, because the scaffold
requires one. No venue is chosen.

## What this is

The study first defines the scenarios of multi-party learning, then the defense
objectives against each, then how each objective is realized. Decided at a
meeting with the PIs and recorded as `2026-11-10-theory-first-then-realize` in
`lib/profs/rulings.md`: "create the theoritcal grounds on what we can proof and
then try realizing these with HE and or complexity of models capacities (such as
model being a small big model model queried |N|/k times where N is the training
set of model so on and so forth)".

The order reverses the one HE-OFT followed, where the protocol was designed
first and the proofs came after. Halil, 2026-11-10: "in case we cannot realize a
result we will use Homomorphci encryption at that specific point and try
optimizing on where to put the homomorphic encryption". A result that cannot be
realized is a finding: "in case theory is failed to realize this opens a research
gap not a failure. In such a case we can discuss what are the metrics".

The scope is wider than HE-OFT and HE-IFD. Halil, 2026-11-10: "build a more
comprehensive theory defining first what are the possible scenarios for example
clients may attack server may put a backdoor I mean anything -but of course we
need to start somewhere with some constraints we put- then we define what can be
the defense objectives and how they will be realized (either a reduction to CKKS
or with a attack success metric we define)". On 2026-11-11 he asked that the
scenarios be complete and "unique and mutually exclusive as much as possible",
that every objective use well-adopted attacks and state-of-the-art defense
mechanisms, and that one figure style depict every scenario.

On 2026-11-11 the formalizing theory, the survey and the library moved to
`FORMAL_SECURITY/HE-ML-migrated/`, whose `INDEX.md` says what each part is: "I
will continue 'formalizing' on formalizing and I will proceed a simpler more
deep learning first study here from there on".

## The claim

None yet.

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

The first block is HE-OFT's (KSK26), unchanged, because the team is the same.
The second block holds the threat terms of the adversary interface of
2026-10-16 that this study keeps. The interface's abstract primitives (data
space, model space, learning function, hypothesis class, evaluation map) left
with the formalizing work, and their full ledger is in
`FORMAL_SECURITY/HE-ML-migrated/CONTEXT.md`.

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
| dataset | a finite multiset of examples, labeled or not, D_j for client j | the data, the corpus |
| horizontal, vertical | how datasets are split among parties: whole examples per party, or one block of every example per party (vertical and split learning) | sample-partitioned, feature-partitioned, as names |
| view | everything an adversary sees, each value through its channel, plus its query answers | observations, access |
| choices | the inputs and outputs an adversary sets, and its queries | capabilities |
| distinguish | the goal of telling two hypotheses about the datasets apart | membership inference, property inference, as names |
| invert | the goal of recovering a target from the view within a tolerance | reconstruction, extraction, as names |
| steer | the goal of choosing inputs so the trained model lands in a target set | poisoning, backdoor, as names |
| collapse | a weaker adversary attains the stronger one's best value at a fixed goal | equivalence |
| separation | a construction where the stronger adversary does much better at a fixed goal | gap, as a name |

## Symbols

Every symbol and every invented label the paper uses, defined once. HE-OFT's
symbols are kept with their meaning.

| Symbol | Means | Defined in |
| --- | --- | --- |
| N, C, d | numbers of clients and classes, feature dimension | KSK26 |
| j | client index | KSK26 |
| D_j, n_j, n_{j,c} | client j's dataset, its size, its count of class c | KSK26 |
| D_0, D_1 | the two challenge datasets of the content game | KSK26 |
| φ, φ_j | the backbone, and the backbone with client j's adapter A_j | KSK26 |
| θ_0, h_j, Δ_j | public head initializer, client j's head, Δ_j = h_j − θ_0 | KSK26 |
| g_j | client j's per-class counts | KSK26 |
| θ* | the shared head | KSK26 |
| Enc | encryption under the collective public key | KSK26 |
| t, Q | decryption threshold, per-client allowance | KSK26 |

## Current state

2026-11-11. The study starts from three records. The report
`lib/reports/2026-11-11-halil-he-results-carried-over.pdf` lists the problems,
results and facts on HE-OFT and threshold CKKS carried from the formalizing
registers, and the Searches section of `lib/literature/positioning.md` is the
search log.
`lib/profs/2026-10-30-meeting/sheet.pdf` is the plan of 30 October on leakage and
encryption placement in federated fine-tuning, with four experiments. The
library is empty, and papers are placed as they are read. Under discussion with
Halil: the axes of the scenario space, the metrics of each goal, and the figure
style. Nothing of that discussion is fixed here yet.
