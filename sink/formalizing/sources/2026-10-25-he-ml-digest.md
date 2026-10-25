# HE-ML digest

Compiled on 2026-10-25 by a read-only pass over the HE-ML repository at commit bb8ca7f, with its uncommitted files, and from the facts of the session of 2026-10-25 that commissioned it. Counts from `lib/literature/` were recomputed on 2026-10-25. A count taken from a report or the deck names that source and its date. Paths are relative to the repository root, `~/Documents/RESEARCH/HE-ML/`.

## 1. What HE-ML is

HE-ML is a literature study, started on 2026-10-16, of how multi-party learning states its threat models, and the home of the formalization that grew out of it. Its setting is a set of data owners, possibly an aggregator, and a training protocol among them. The group's prior work, HE-OFT (KSK26), proves its guarantees against semi-honest parties under multiparty CKKS, and the study asks where the field stands once some parties deviate. The repository holds three layers of work. A sweep screened eleven top venues for 2023 to 2026 and coded the papers it kept. An adversary interface writes every threat model with data, a model space and a learning function. A learning oracle carries a theory that ended with 21 accepted items. No claim, no direction and no venue is chosen, and acm-ccs in `paper/.paper-meta.yml` is a placeholder. Nothing has been measured, and `lab/` is empty. On 2026-10-25 Halil moved the line toward a computational view, in which an adversary is measured by computational and learning resources. HE-ML takes its terms from HE-OFT, and `CONTEXT.md` binds them.

## 2. Artifacts

Fifteen artifacts follow, then the state of the working tree.

### 2.1 Project context

- Path `CONTEXT.md`, written on 2026-10-16, committed.
- It establishes the scope, the venue rule, the people table (Halil alone, handle halil), the terminology ledger of 33 terms, the symbol table and a current-state paragraph.
- Status binding. Every term in it is binding on prose, code and figures.
- Known errors. Its current state says 13 papers were dropped after reading, while `lib/literature/screening.csv` and the notes record 14. It says notable papers outside the venue rule are recorded under `excluded` in `lib/literature/sources.yml`, and that file has no such key. Its current state stops at 2026-10-16 and does not mention the learning oracle or the formal tuning. The claim, the recorded deferrals and the conventions sections are empty.

### 2.2 Adversary interface report

- Path `lib/reports/2026-10-16-halil-adversary-interface.pdf`, source `lib/reports/src/2026-10-16-halil-adversary-interface.tex`, committed in 9977bd5 and 67f6058.
- Dated 2026-10-16.
- It establishes the interface. Three primitives (data, a model space, a learning function) fix every adversary as a triple of a view, choices and one of three goals, distinguish, invert or steer. It orders adversaries by post-processing of views and inclusion of choices, defines collapse and separation, and places HE-OFT, FedAvg, split and vertical learning on the interface. It finds one steering weakness of HE-OFT (section 4.2, HE-OFT count steering).
- Status draft, by its own status field.
- Known errors. The sentence that a collapse at the distinguish goal holds exactly when the weaker view is a sufficient statistic of the stronger is wrong. Deck frame 6 corrects it, since the converse fails for one fixed pair of hypotheses by a three-point example. Its boundary names Salem et al. from memory as the possible owner of the distinguish and invert half. The full reading of SCEKPSTZ23 has since answered this check (section 6). Its counts (44 papers) describe the state before the wide sweep.

### 2.3 Multi-party learning sweep report

- Path `lib/reports/2026-10-16-halil-multi-party-learning-sweep.pdf`, source `lib/reports/src/2026-10-16-halil-multi-party-learning-sweep.tex`, data `lib/reports/src/data/2026-10-16-halil-multi-party-learning-sweep-*.csv`, script `lib/reports/src/figures/2026-10-16-halil-multi-party-learning-sweep-trends.py`, committed in 1e50ffe.
- Dated 2026-10-16.
- It reports the screen (574 screened, 364 placed, 350 coded on 519 rows) and three row-level trends from 2023 to 2026. Deviating rows rose from 64 to 75 per cent, HE rows from 12 to 26 per cent, and the adaptive share among deviating rows fell from 54 to 35 per cent.
- Status superseded in part by the swept-papers report of the same day (2.4). Its counts of the screen still hold. Its trend headlines do not.
- Known errors. The deviating-share headline is wrong. The script counts a row as deviating whenever its `sets` cell is anything other than empty, `none` or `n/a`, so 70 rows whose choices cell reads like "none (semi-honest)" count as deviating. Its mechanism columns match keywords over the whole protection cell rather than the mechanism field, and they differ from the recount of deck frame 9. Its trends are per row, and rows of one paper are not independent.

### 2.4 Swept papers and threat models report

- Path `lib/reports/2026-10-16-halil-swept-papers-and-threat-models.pdf`, source `lib/reports/src/2026-10-16-halil-swept-papers-and-threat-models.tex`, ten CSVs under `lib/reports/src/data/` and the script `lib/reports/src/figures/2026-10-16-halil-swept-papers-and-threat-models-tables.py`. All of it is untracked.
- Dated 2026-10-16, written at Halil's request for one ready-to-read account of the sweep, with HE-OFT left out of the field counts.
- It establishes the corrected account of the sweep. 349 papers are coded on 516 rows. Seven templates of role, choices and goal hold 513 of the 516 rows. Per paper, the HE share went from 11 to 19 per cent from 2023 to 2026 (Fisher p 0.241) and the deviating share from 58 to 55 per cent (p 0.74), so no share moves enough to call a trend. The privacy line and the robustness line rarely meet. 103 of 145 rows of clients that steer through their updates name no confidentiality mechanism, and 12 of 102 rows of a reading server face a check. The coder had to infer static or adaptive corruption in 374 of 516 rows. It recommends four things for any threat model we write, static or adaptive corruption, honest or dishonest majority, when the adversary commits its choices, and what it knows of honest updates.
- Status draft. It is the current account of the sweep, and its own section on what changes says it supersedes 2.3.
- Known errors. None recorded. Every count is empirical, on rows that one language-model coder extracted, and the rows still await a check against their papers. It ran on the 519-row ledger without SCEKPSTZ23.

### 2.5 Learning-oracle definition report

- Path `lib/reports/2026-10-16-halil-learning-oracle-definition.pdf`, source `lib/reports/src/2026-10-16-halil-learning-oracle-definition.tex`, untracked.
- Dated 2026-10-16, from Halil's statement of the idea in the session of that day.
- It establishes the problem and a first definition. Training blocks proofs and measurements because the law of a trained model has no closed form, and every sample costs a training run. A learning oracle answers training and evaluation requests in unit time with a record-indexed seed and an access policy (Definitions 1 and 2), and a model bank approximates it (Definition 3). It states three propositions and two leave-one-out models, and it renames the protocol graph the dataflow graph.
- Status draft, superseded in its definitions and propositions by the final theory (2.11).
- Known errors, found by the challenger of round 00 (`sink/2026-10-16-formal-tuning/round-00/challenger.md`). Proposition 1 (perfect substitution) is false as stated for an arbitrary policy, by two counterexamples, and holds for the realizable policy alone (ch-substitution-policy). A caller may launder an evaluation-only handle into an open one by training on it with an empty dataset (ch-handle-laundering). Proposition 2(a) cannot be expressed, because seeds pass by value and the oracle never reveals a seed it drew (ch-seed-naming), and its advantage is the probability that the two models differ, not one (ch-reference-advantage-one). The budget of Definition 2 is undefined, and Proposition 3 is either false or vacuous (ch-budget-semantics), so it was withdrawn in round 01. Locality of the record-indexed seed is not a mathematical condition (ch-locality-ill-posed). The claim that one random-half bank serves all records holds only for the random-subset game (ch-bank-design-game). Drawn-seed samples can falsify exact unlearning and never certify it (ch-experimenter-equality-test).

### 2.6 Meeting deck of 16 October

- Path `lib/profs/2026-10-16-meeting/slides.tex` and `slides.pdf`, committed in feb312d.
- Dated 2026-10-16, for the group meeting of that day, counts as of the morning of 16 October.
- It presents CURE and HE-OFT, the study, the counts (frame 4), the interface (frames 5 and 6), coalitions by role and goal (frame 7), evidence, protection and checks (frame 8), trends (frame 9), terms that change meaning (frame 10), eight settled steps between adversaries (frame 11), secure aggregation and multiparty HE against deviating parties (frame 12), the decryption channel of threshold and approximate HE (frame 13), corrupted fractions (frame 14), HE-OFT on the interface (frame 15), and four questions for the meeting (frame 16).
- Status as presented. No PI comment or ruling from the meeting is recorded in `lib/profs/`.
- Known errors. Frame 9 tests the HE trend on rows, which share their paper and are not independent. Its p below 0.001 becomes 0.241 counted per paper (2.4). Its claim that the HE share rose within the security venues alone from 13 to 28 per cent is per row too. Frame 3 counts 241 of 350 papers that name federated learning, while 2.4 counts 192 of 349 that train by horizontal federated learning or federated fine-tuning. The two rules differ and are not reconciled.

### 2.7 Rulings and dismissed findings

- Paths `lib/profs/rulings.md` and `lib/profs/dismissed.md`.
- Both hold only their header. No ruling, no PI comment and no dismissed finding is recorded, and `lib/INDEX.md` counts zero of each. The rulings that exist live in `CONTEXT.md` (section 7).

### 2.8 Literature folder

- Path `lib/literature/`.
- `sources.yml` names the primary venues and a watch list (EuroS&P, SaTML, CSF) proposed on 2026-10-16 and never screened. It records the venue sweep as run on 2026-10-16 and the backward and forward sweeps as never run. Its groups, researchers, seeds and feeds are empty.
- `positioning.md` has five empty slots (setting, what exists, the gap, the claim, why it is hard) and four recorded searches (section 6).
- `related-work.md` is an empty template.
- `catalog.md` codes the first 44 papers and HE-OFT on the interface. It is superseded by `ledger.csv` and `screening.csv`, by its own first line.
- `screening.csv` holds every screening decision with its reason, 575 rows (section 6).
- `ledger.csv` codes every kept paper on 22 columns, one row per coalition (section 6).
- `notes/<venue>/<Key>.md` holds one note per placed paper, 365 notes in 12 venue folders (section 6).
- `pdfs` is a symlink to Google Drive, `My Drive/HE-ML/pdfs/` on the KU account.
- Known errors. The working copy of `ledger.csv` differs from HEAD (2.16).

### 2.9 Sink files at the top level

- `sink/INGEST.md` records three folders and files that stay in the sink, `unavailable.md`, `ledger-columns.md` and `2026-10-16-formal-tuning/`. The last row is uncommitted.
- `sink/unavailable.md` lists four accepted papers with no accessible PDF, recorded 2026-10-16. They are Not One Less (CCS 2024), G-Fence (CCS 2026), Authenticated Outsourced Incrementally Verifiable MPC (ASIACRYPT 2026) and Shared Spotlight Meridian (IEEE S&P 2026).
- `sink/ledger-columns.md` is the column dictionary of the ledger, merged on 2026-10-16. It states the four relations of a party to a node, five reductions the merge makes, and the 22 columns with their keywords. It also records where each reported distinction went, four terms that change meaning between papers, and five data errors found in papers (LAWKDM26, TTPLHLCL26, CQYZFDX24, CFMPV25, DHWSGRC25).

### 2.10 Formal tuning folder

- Path `sink/2026-10-16-formal-tuning/`, untracked. `README.md` holds the protocol, the goal in Halil's words, the non-triviality bar, the stopping rule and the round log. `GATES.md` holds eight gates, all checked. `round-00/` to `round-10/` hold the builder and challenger turns, each with a PDF. `scripts/` holds `verify.mjs` and `build.mjs`. The folder also holds `theory/CURRENT.md` and `final/`.
- Dated 2026-10-16 to 2026-10-17.
- It establishes, through eleven rounds of a builder and a challenger, a learning-oracle theory with 6 accepted definitions and 15 accepted results, 8 of them non-trivial. Round 00 raised 19 challenges, 5 blocking, and set 5 problems. Blocking counts by round were 5, 1, 0, 1, 0, 3, 2, 1, 0, 4, 0. Halil fixed the end at round 10 on 2026-10-17.
- Status finished. Gate G7 records that the orchestrator re-derived every proof shown in full in the final document and found no false step, with one conservative constant in coupling (a)(ii).

### 2.11 Final learning-oracle theory

- Path `sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md`, with its PDF. Halil reads only the PDF.
- Dated 2026-10-17.
- It establishes the definitions in their simplest form, nine standing facts, five theorem sections with proofs, two lemmas with proofs, eight further results by pointer to round files, nine open problems, and a prior-work paragraph. Sections 3, 4 and 5 below digest it.
- Status accepted by the challenger's audit (FINAL ACCEPT, blocking 0). Halil's own acceptance is not recorded.
- Known errors. The seven minor findings of the audit (2.12) are not applied to the document. Several proofs exist only in round files. Novelty against the privacy-auditing literature is open by its own statement.

### 2.12 Audit of the final theory

- Path `sink/2026-10-16-formal-tuning/final/audit.md`, with its PDF.
- Dated 2026-10-17.
- It accepts every item and lists seven one-clause findings. The label of thm-coupling-certificate calls open a bound of (c)(ii) that holds for every view space (ch-coupling-label-scope). The symbol a is reused in thm-replay-audit-steer (d) (ch-scalar-symbol-reuse). The Reading of thm-dataflow-composition (e)(ii) leaves the range of eta unstated (ch-reading-eta-range). Item 4 of the opening names the wrong limit for its o(1) (ch-intro-price-limit). The closed form of the Gaussian hockey-stick divergence rests on a citation from memory, and a one-line proof exists (ch-closed-form-memory). "Complete up to lambda prime" is undefined (ch-replay-completeness-term). The dataset is used before it is introduced in def-isolated-client (ch-dataset-node-before-use).
- Status accepted, findings open.

### 2.13 Theory register

- Path `sink/2026-10-16-formal-tuning/theory/CURRENT.md`, with its PDF.
- Dated after round 10.
- It holds the definitions in force, the symbols, the register of every statement with label, status, round and proof location, the nine open problems in full with what is known and the obstacle, and a map from the old names of the round files to the final ones.
- Status the builder's living file.
- Known errors. The register lags the last verdicts. It lists thm-coupling-certificate, thm-dataflow-composition and thm-active-choice-dichotomy as proposed in round 10, while the round-10 challenger and the audit accept all three as non-trivial.

### 2.14 Learning-bounded literature scan

- Path `sink/formalizing/sources/2026-10-25-learning-bounded-scan.md`, untracked.
- Dated 2026-10-25, written by a reader subagent of the commissioning session.
- It scans work that measures a privacy adversary by learning resources, a bounded attack class with bounded samples, with lower bounds from hard learning problems and the training seed as an attacker resource. Its verdict is in section 6.
- Status a scan. Every paper was opened in full unless an entry says otherwise. Its absence claims rest on about twelve searches and a keyword filter over 267 citers of Xu et al., so they are empirical.
- Known errors. None recorded. Three venues are given from recollection, those of F-BLEAU, of Carlini et al. on instance encoding, and of Balle et al.

### 2.15 Empty scaffolding

- `lib/claims.yml` and `lib/numbers.csv` hold only their headers. `lib/issues/`, `lib/reports/reflections/`, `paper/contracts/`, `paper/reviews/` and every folder under `lab/` are empty. `paper/sections/intro.tex` holds FILL.
- `AGENTS.md` is untracked and repeats `CLAUDE.md` for another agent, with one path changed.

### 2.16 State of the working tree

HEAD is bb8ca7f of 2026-10-16. Three groups of changes are uncommitted. The learning-oracle and swept-papers reports with their data and figures, `sink/2026-10-16-formal-tuning/`, `sink/formalizing/` and `AGENTS.md` are untracked. `lib/INDEX.md` and `sink/INGEST.md` carry the rows for those reports and the tuning folder. `lib/literature/ledger.csv` was rewritten on 2026-10-19 by an unknown writer. The working copy has 519 rows on 350 papers with flat note paths (`notes/<Key>.md`), and it lacks the two SCEKPSTZ23 rows. HEAD has 521 rows on 351 papers with venue-folder paths (`notes/<venue>/<Key>.md`). The rows otherwise agree. Other sessions started from `FORMAL_SECURITY` are known to write into this repository, so every count from `lib/literature/` should be recomputed and dated before use.

## 3. Definitions

### 3.1 Binding terms of the context file

Path `CONTEXT.md`, section Terminology ledger. The first block comes from HE-OFT unchanged. The second was fixed with the interface on 2026-10-16.

- backbone. The frozen public pretrained model, the map from an input to its features. Never the encoder or the base model.
- adapter. A client's trained up-projection of a LoRA whose down-projection is frozen at a public initialization, kept local.
- head. A linear map from the features to the class logits.
- head displacement. A client's trained head minus the public initializer. Never the delta or the contribution.
- update. The thing a client sends.
- shared head. The merged head, held only as a ciphertext. Never the global model.
- the two arrangements. The shared head over a client's own adapter, or over the bare backbone.
- querier. The client that sends a query.
- quorum. Any t clients, enough to decrypt.
- allowance. The per-client number of answered queries, Q. Never the budget.
- the server. The one party that merges and answers queries.
- semi-honest. The threat-model term. Never honest-but-curious.
- deviating. A party that departs from the protocol arbitrarily. Never Byzantine when a client of HE-OFT is meant.
- confidentiality. What encryption gives an update, a head or a query.
- privacy. The training data, and what an adversary learns about it.
- local. Never transmitted.
- plaintext, ciphertext. Always these words.
- data space. The set Z examples come from, with no structure assumed. Never the product of an input space and a label space, by Halil's ruling of 2026-10-16.
- dataset. A finite multiset of examples, labeled or not. Two datasets of one protocol may live in different data spaces.
- loss. A map from a model and one example to a real number, with no labels required.
- horizontal, vertical. Whole examples per party, or one block of every example per party.
- model space. The set M of models, with no structure assumed, by Halil's ruling of 2026-10-16.
- learning function. A randomized map from a starting model, a dataset and a hypothesis class to a model. Loss, optimizer and step count are internal to it, and aggregation is a learning function whose data are the client models.
- evaluation map. The output of a model on a query, which may be a score vector, a label, a loss, a sequence or an embedding.
- hypothesis class. The subset of the model space a learning function searches. Frozen parts are expressed by it, so LoRA and head training are full training on a smaller class.
- model. One element of the model space. A parameterization is an instance, not an assumption.
- view. Everything an adversary sees, each value through its channel, plus its query answers.
- choices. The node arguments and outputs an adversary sets, and its queries. Never capabilities.
- distinguish. The goal of telling two hypotheses about the datasets apart. Never membership or property inference as a name.
- invert. The goal of recovering a target from the view within a tolerance. Never reconstruction or extraction as a name.
- steer. The goal of choosing inputs so the trained model lands in a target set. Never poisoning or backdoor as a name.
- collapse. A weaker adversary attains the stronger one's best value at a fixed goal.
- separation. A construction where the stronger adversary does much better at a fixed goal.

### 3.2 The adversary interface

Path `lib/reports/src/2026-10-16-halil-adversary-interface.tex`, section Method, and `sink/ledger-columns.md`, sections 1 and 2.

- Protocol. A finite directed acyclic graph whose nodes apply a learning function or an evaluation map to arguments from datasets, public objects or earlier nodes.
- Channel. Each node value reaches the adversary as the plaintext value, a sum over a set of clients, a ciphertext under a key it does not hold, a noisy value, or nothing. A decryption policy releases chosen functions of encrypted values, with decryption noise for approximate HE.
- View. The node values the adversary sees through their channels, together with oracle access to the served model's evaluation map.
- Choices. Six kinds, a data argument, a model argument (the same or one per client), a class argument, the learning function of a node, the output of a node, and queries. A semi-honest adversary chooses queries only.
- Goals. Distinguish two hypotheses on the datasets, invert a target within a tolerance, or steer the trained model into a target set while a defender's discriminator has advantage at most delta. Each goal has a baseline from public knowledge alone. The stealth constraint is itself a distinguish game played by the defender.
- Order. One adversary is at most as strong as another when its choices are a subset and its view is a randomized function of the other's view. For efficient adversaries the function must be efficient.
- Four relations of a party to a node, from the ledger dictionary. It sees the output through a channel, an argument is public to it, it sets an argument, or it sets the output.
- Five reductions, from the ledger dictionary (heuristic, modelling conventions). Knowledge is publicity of arguments. Behaviour terms follow from the relations. Data poisoning and Byzantine behaviour differ only in what is set and when. A check restricts a relation. The nominal and the effective channel can differ.
- Seven templates, from 2.4. The server that reads what it receives, the server that sets what clients compute, the server with clients, clients that set their updates, clients that set only their data, clients that read the model, and a querier or eavesdropper.

### 3.3 The learning oracle

Path `sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md`, section Definitions, with the further clauses in `theory/CURRENT.md`, section Definitions.

- def-learning-oracle. A training input holds a learner name, a starting model, a dataset and a hypothesis class from a finite family. The learning function maps a training input, a seed with an atomless law and hardware randomness to a model. The oracle stores models and seeds under per-caller integer names labelled open or eval, and answers three calls, Train (with a seed, a seed name, or a fresh drawn seed), Eval and Open. Fidelity makes every drawn randomness independent. Access lets Train and Open run only on names labelled open, and Eval on names labelled eval or open.
- def-learning-oracle-model. A procedure is a dataflow graph run in a fixed order with input, learning, evaluation and general nodes. Each node value reaches a coalition through the plain channel, the query channel (an eval name, a query set and an allowance) or none. The adversary is an unbounded oracle algorithm that reaches the learning function only through the oracle, unless a statement assumes a computational bound. A strategy is passive when its choices are the protocol's, and active otherwise. The goals are distinguish and steer, and a privacy statement bounds the hockey-stick divergence of the view laws, which also bounds inversion.
- def-certifier. An experimenter is a caller outside every procedure. It works in the drawn-seed discipline when every Train call draws a fresh seed and it opens no seed name, and in the coupled discipline otherwise. A certifier makes at most N Train calls and outputs an upper bound on a target functional of the learning function. It is sound at level alpha over a class when the bound holds with probability at least one minus alpha for every member.
- def-degenerate-oracles. The bottom oracle grants nothing beyond the procedure and puts no bound on Train calls, which is what a real training service gives. The top oracle also grants the seed name of every honest learning node. For an experimenter or an auditor the two cases are the drawn-seed and the coupled discipline.
- def-isolated-client. A client is isolated behind Gaussian releases when only its R learning nodes read its dataset and each round's model leaves only through a release with fresh Gaussian noise added to a coalition contribution. The coupled execution also trains a twin on the other candidate dataset under the same seed. The exceedance is the largest release difference between run and twin, and the exceedance probability is the chance it passes a threshold.
- def-model-bank. A design lists training inputs with seeds, fixed or drawn, and a bank stores one run per entry. Its empirical oracle answers with the first unused matching entry and refuses otherwise.
- Objects of the theorems. The identity coupling trains both candidate inputs under one seed. The coupled divergence is the mean, over coupled pairs, of the channel's divergence at the two models. The divergence probability is the chance the two models differ. The top divergence is what the top oracle shows. A strategy is B_A-deviating when it follows the protocol except for additive inputs within B_A of the prescribed ones. The clipped aggregation instance has one honest stateless client, an honest server and one coalition client. The reach, spread and joint reach of a target set are the chances that a run lands near it, that two runs at one seed land apart, and both. A certifier is uniformly accurate when its output lies within the accuracy above the target at every learning function, at a fixed number of Train calls.
- Non-triviality bar. Path `sink/2026-10-16-formal-tuning/README.md`. A theorem counts as non-trivial when four conditions hold. The oracle is in it. Removing the oracle leaves a problem that needs the law of the trained model. The bound depends on the learning function only through oracle-measured quantities. The statement fails or becomes vacuous under one degenerate oracle. After round 02 the orchestrator ruled that for an experimenter or an auditor the test runs against the drawn-seed discipline.

### 3.4 Where the names drift

- The interface says protocol, the oracle report says dataflow graph, and the final theory says procedure for the same graph.
- The interface has five channels (plaintext, sum, ciphertext, noise, nothing). The theory has three (plain, query, none) and treats a sum, a ciphertext or a noisy value as a general node released in plain.
- The interface has three goals. The theory keeps distinguish and steer and covers invert through a remark that every privacy bound also bounds inversion.
- The learning function takes a model, a dataset and a class in the interface, adds a seed in the oracle report, and becomes a map of a training input, a seed and hardware randomness in the theory.
- The theory's adversary is unbounded. The 2026-10-25 decisions ask for polynomial-time adversaries measured by computational and learning resources, so a new resource model is needed before the two can share statements.

## 4. Results

Each result names whether it needs the oracle, in three grades. None means the statement is about laws or geometry and holds for real training. Seed control means the statement or its certificate needs training reruns at a named seed, which real training with a fixed seed supplies. Oracle means the statement is a lower bound in the oracle's cost model, where Train calls cost one each, or a separation between the drawn-seed and coupled disciplines or between the bottom and top oracles. The split between seed control and oracle follows the judgment of the 2026-10-25 session. That judgment is heuristic. It assumes deterministic kernels, or hardware randomness independent across runs, and it is not written as a proof.

### 4.1 Learning-oracle theory

Every item below stands accepted by the round-10 challenger and the audit. The final document is `sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md`, cited below as the final document.

- lem-needle-lower-bound. Let J needle functions each equal a reference function outside its own one of J disjoint sets of training inputs. A certifier sound over a class that contains them and that makes N Train calls outputs at least the needles' leakage at the reference function, except with probability alpha plus N over J. Status proven. Oracle, the resource counted is Train calls in either discipline. Final document, section Needle lower bound. Proof in full there.
- lem-sphere-code. At least two to the power 0.18 d unit vectors have pairwise distance at least one, and their nearest-point cells keep a Gaussian perturbation of a point with probability close to one. Status proven. None. Final document, section Sphere code.
- lem-atomless-two-point. A drawn-seed certifier of total variation through a deterministic channel, sound for all learning functions, outputs one with probability at least one minus alpha on atomless views. Status proven. Oracle, it is the drawn-seed lower bound behind several theorems. Final document, section Further accepted results, proof in `round-01/builder.md` corrected in rounds 02 and 03.
- lem-bank-fidelity. The empirical oracle of a model bank agrees with a learning oracle up to its first refusal. Status proven. It ties the realization to the oracle. Final document, section Further accepted results, proof in `round-01/builder.md`.
- thm-coupling-certificate, non-trivial. One training node seen through a channel leaks at most the top oracle's divergence, which is at most the coupled divergence, which is at most the divergence probability, with the middle two equal under deterministic kernels. When the channel's divergence at two models is computable, coupled pairs certify the leakage for every learning function. Drawn seeds give lower certifiers and, on finite views, upper ones, but through a deterministic channel with atomless view laws no drawn-seed certifier outputs below one. The gap between the bottom and top oracle can be one. A seed-map coupling also bounds the leakage and is exact for finite views. Status proven, except exactness for atomless views (open problem 8). Seed control for the upper chain and its certificate. Oracle for the drawn-seed impossibility and the bottom-top gap. Final document, section Coupling certificate.
- thm-black-box-certifiability, non-trivial. On a finite query set with finitely many outputs, every bottom-oracle adversary with a given number of Eval calls is bounded by the best strategy tree of that depth, whatever its Train calls. Drawn-seed models certify this label-only advantage from both sides at a cost set by the output count, the query-set size, the depth, alpha and the accuracy. Shadow models reach it at a stated rate. With deterministic evaluation and atomless model laws, drawn seeds never certify that label-only leakage equals white-box leakage below one. Coupled pairs certify the white-box advantage below the divergence probability. Status proven, with a matching lower bound for shadow models open (open problem 3). None for the reduction and the two-sided certificate. Oracle for the drawn-seed impossibility, and the reduction fails under the top oracle by a digit example. Final document, section Black-box certifiability.
- thm-dataflow-composition, non-trivial. Let a client's data reach a coalition only through R Gaussian releases. Its leakage in hockey-stick divergence is then at most a Gaussian term plus the exceedance probability. The Gaussian term is set by the number of rounds and by a threshold over the noise scale. The bound holds in both orders, for every strategy, with state and with stops, under both oracles. Coupled executions certify the exceedance probability with a number of runs free of the model dimension d. Ciphertexts of an aggregation sub-protocol reduce to the releases up to their realization error. In some one-round procedure, a certifier sound against all active strategies outputs nearly one where the leakage is zero, whatever its Train calls. Drawn-seed certifiers pay Train calls exponential in the smaller of d and the squared clip-to-noise ratio. Status proven for the composition, the certificate, the reduction given the realization error, the impossibility against active strategies and the drawn-seed price. Heuristic, realization by threshold CKKS and the form of CKKS decryption under a public scalar. Open problems 1, 2, 4 and 6. None for the composition bound. Seed control for its certificate. Oracle for the drawn-seed price and the active-strategy impossibility. Final document, section Dataflow composition.
- thm-bounded-deviation-transfer, non-trivial. A coalition that follows the protocol except for additive inputs within B_A of the prescribed ones has an exceedance probability at most a fixed function of the protocol's own. The function is set by one exponent that grows linearly in the number of rounds and quadratically in the ratio of B_A to the noise scale. Coupled runs of the protocol's own execution certify the bound at a cost free of d. No transfer function improves on it by more than a logarithmic factor. In the clipped aggregation instance every certifier sound for all learning functions and accurate where the leakage is zero pays a number of Train calls exponential in that exponent, and drawn-seed certifiers fail. The logarithm of the least cost equals the exponent to first order when the exponent is small against d and the logarithm of the rounds is small against the exponent. Status proven, all parts and the corollary. None for the transfer. Seed control for the certificate. Oracle for the price and the drawn-seed failure. Final document, section Bounded-deviation transfer.
- thm-replay-audit-steer, non-trivial. Seeds come from a random oracle applied to a dataset commitment and a nonce, and an auditor replays training at that seed. A prover then passes the audit with a model in a target set with probability at most its random-oracle queries plus one, times the replays, times the target's reach. The honest prover passes except with the spread. A grinding prover matches the bound within a factor 3.2 under deterministic kernels. A drawn-seed auditor cannot be both complete and sound, by rotations of a circle. Provers that cannot see the seed table pay in Train calls. Status proven, with the gap between the tolerance and half of it under hardware randomness open (open problem 7). Seed control for the auditor's replay, plus a random oracle, without which soundness fails. Oracle for the drawn-seed auditor impossibility. Under the 2026-10-25 rule the random oracle that derives the seed is a cryptographic plug-in of the kind that does not count (heuristic reading of the rule). Final document, section Replay-audit steering.
- thm-perfect-substitution. Against an adversary that samples the learning function once per Train call, the real procedure gives the bottom oracle's joint law of honest values and transcript, so bottom-oracle bounds hold for the real procedure. Status proven. It is the bridge that makes the bottom oracle realizable. Final document, section Further accepted results, proof in `round-01/builder.md` with `round-02/builder.md`.
- thm-reference-access. On one node through a deterministic channel, the top oracle's best advantage is the coupled divergence under deterministic kernels. Under the bottom oracle, attacks reach the total variation at a plug-in rate on finite views, and no rate uniform over learning functions exists on atomless views, explicit seeds included. The last part also holds on finite-bit seeds. Status proven. Oracle, it is the seed separation between named and hidden seeds on one node. It replaces Proposition 2 of the report. Final document, section Further accepted results, proofs in rounds 01 and 02.
- thm-bank-soundness. A bank on random halves of a pool estimates the random-subset membership game for all records at once, for tests fixed before the bank is built. That game can differ by one from the fixed-dataset game. Certifying every record of a fixed dataset through a Gaussian release has a lower bound on Train calls. Status proven for the estimate, the gap and the lower bound. Heuristic, the part on shadow models in the random-subset game. Accepted, not non-trivial. None for the estimate, oracle for the lower bound. Final document, section Further accepted results, proofs in rounds 01 to 05.
- thm-active-choice-dichotomy, non-trivial. Against a stateless client the worst exceedance over admissible strategies is attained without adaptivity. A certifier sound for all learning functions and accurate where the leakage is zero needs Train calls linear in the number of distinct admissible choices, or of choice sequences with state, and coupled certificates achieve this up to a logarithmic factor. No number suffices for an infinite set. Status proven. Seed control for the achieving certificates. Oracle for the lower bound. Final document, section Further accepted results, proofs in rounds 03 and 04.
- thm-record-level-certificate, non-trivial. One shared base certifies the fraction of a fixed dataset's records whose leakage to a passive coalition exceeds a threshold, at a cost free of the dataset size and d. Records outside the dataset are never certified, and drawn seeds fail. Status proven. Seed control for the certificate, oracle for the failures. Final document, section Further accepted results, proofs in rounds 03 and 04.
- thm-smoothed-choice-certificate, non-trivial. In the clipped aggregation instance a covering of smoothed tails certifies a coalition client with inputs of norm at most B_A at a cost exponential in d. Every certifier sound for all learning functions pays a cost exponential in the smaller of d and the exponent of the transfer, and drawn seeds fail. Status proven. Heuristic, that the covering beats the transfer only when the exponent is large against d. Seed control for the covering, oracle for the lower bounds. Final document, section Further accepted results, proofs in rounds 04 and 05.

thm-own-data-only, Proposition 3 of the report, was withdrawn in round 01.

### 4.2 Adversary interface

The interface report gives its results no slugs. Each entry below carries the report's own words as its name.

- The order. If one adversary's choices are a subset of another's and its view is a randomized function of the other's view, its best distinguishing advantage and best inversion success are at most the other's. Status proven, by data processing and by simulation. None. `lib/reports/src/2026-10-16-halil-adversary-interface.tex`, subsection The order, and deck frame 6.
- The test fact. The best distinguishing advantage equals the total variation between the two laws of the view. Status proven, by Neyman and Pearson. None. Same subsection.
- Collapse by sufficiency. A sufficient statistic of the stronger view gives a collapse at the distinguish goal, and the converse fails for one fixed pair of hypotheses. Status proven, the converse by a three-point example. None. Deck frame 6, which corrects the report.
- Coverage. Every adversary the sweeps report is a triple of a view, choices and one of the three goals, with membership inference a distinguish game, reconstruction and extraction inversion, and poisoning and backdoors steering. Status empirical, on the sweep extractions of the placed papers, with 25 of 519 rows carrying a goal outside the three (free-riding, compliance bypass, watermark removal, deck frame 7). None. Report, Result section.
- HE-OFT count steering. Nothing ties a client's uploaded per-class counts to its public sample count or its data. A client that reports a large count for a class therefore moves that row of the shared head as close to its own head displacement as it likes. Status proven, from the aggregation formula. Found by us, and HE-OFT does not state it. None. Report, subsection HE-OFT on the interface, and deck frame 15.
- HE-OFT's own results as recorded. A semi-honest server with t minus 1 clients is simulated from the ideal leakage under IND-CPA and a smudging hypothesis the measured configuration does not meet. Against t minus 1 deviating clients and an honest server, the distinguishing advantage is at most a negligible term plus what the coalition's label queries give. That label view is no stronger than both shared heads in plaintext. Both statements rest on three readings of deviating messages that no proof enforces. No protocol in which clients decrypt what the server presents admits a deviating server. Status proven in HE-OFT, read in full (`lib/literature/notes/arxiv/KSK26.md`). None. Report, subsection HE-OFT on the interface.

## 5. Open problems

### 5.1 The nine of the learning-oracle theory

Stated in full, with what is known and the obstacle, in `sink/2026-10-16-formal-tuning/theory/CURRENT.md`, section Open problems, and in short in the final document, section Open problems.

1. Sum channel. Let further honest isolated clients add their clipped updates to the releases. Is there a functional of the learning function that bounds every passive adversary as the exceedance probability does, is never above it, is below it somewhere, and has a coupled-discipline certifier with Train calls fixed by alpha, the accuracy, the rounds and the number of honest clients?
2. Drawn-seed price above d. When the squared clip-to-noise ratio exceeds d, is some drawn-seed certifier of the one-round divergence uniformly accurate with Train calls exponential in a constant times d and polynomial in the inverse accuracy and the logarithm of the inverse of alpha?
3. Shadow lower bound. Does some family of learning functions force every shadow-model attack within the accuracy of the label-only optimum to use Train calls of the order of the output count raised to the query depth, times the logarithm of the query-set size, over the squared accuracy?
4. Multi-round drawn seeds. In the clipped aggregation instance with no deviation, is there a uniformly accurate drawn-seed certifier of the divergence whose Train calls do not depend on d? The register gives it low priority.
5. The price at a fixed ratio. With the ratio of the transfer exponent to d held fixed and the exponent growing, does the logarithm of the least certification cost per unit of exponent have the same limit as the logarithm of the largest number of cells a deviating strategy can reach per unit of exponent? The second limit is a capacity with feedback (heuristic).
6. Threshold CKKS. Does threshold CKKS with smudging realize the ideal releases under RLWE with negligible error against semi-honest coalitions, and, with six additions (trusted key setup, proofs of plaintext knowledge, broadcast, recomputation by honest decryptors, proofs of correct partial decryption, agreement), against deviating ones?
7. The gap between the tolerance and half of it. Under hardware randomness, does some prover always pass the replay audit into the target with probability at least a universal constant times the smaller of one and its random-oracle queries times the reach?
8. Seed maps. Under deterministic kernels with a deterministic channel and atomless views, does some seed map make the coupling exact for total variation in the limit, and does an explicit-seed certifier exist that is uniformly accurate for it? The round-03 challenger expects no for the second (heuristic).
9. Finite seeds. Does each impossibility proven with an atomless seed hold on a seed space of finitely many bits, with an additive term that vanishes as the bit count grows at a fixed number of calls?

### 5.2 Others

10. Black-box against white-box in HE-OFT. Do the coalition's label queries reach what the shared head reveals, as a collapse or a separation at the distinguish goal? This is Küpçü's question, open. Interface report, What this changes, and deck frame 16.
11. Deviating server. Is there a check on what the quorum key-switches, cheaper than recomputing the serving circuit, that restores the semi-honest view? This is the question of the group's verifiable HE study, open. Interface report, What this changes.
12. Deviating clients in HE-OFT. Can counts and norm bounds proven under encryption, as in ACORN, bound the steering found in HE-OFT count steering (section 4.2)? Open. Deck frame 16.
13. HE-OFT and the smudging result. Does HE-OFT's per-party smudging in its Theorem 1 meet standard simulation security, given that Hwang et al. (HHKLS26, ASIACRYPT 2026) prove, as extracted, that independent per-party smudging fails it? Unchecked. Deck frames 13 and 15.
14. HLSS25. Does the placed proof against deviating decryptors (Hwang, Lee, Seo and Song, CCS 2025), which smudges per party, meet standard simulation security after the same result? Open as extracted. Deck frame 13.
15. The interface as a paper. Does the interface hold a publishable contribution beyond Salem et al., in the protocol graph, the channels, the choices and the steer goal? Open. Deck frame 16 and `lib/literature/notes/ieee-sp/SCEKPSTZ23.md`.
16. Venue rule. Does the top-venue rule stand, given that it leaves out Suri, Zhang and Evans (TMLR 2024) and Wainakh et al. (Sensors 2023)? Open, deck frame 16.
17. Usefulness of the certificates. For a transformer trained with a shared seed, do coupled reruns rarely differ by more than the threshold? Open and empirical. Audit, Assessment.
18. Novelty of the theory. Does the theory survive a reading of the privacy-auditing literature (Jagielski et al., NeurIPS 2020, Steinke et al., NeurIPS 2023), and of oracle-efficient learning, shadow models and datamodels (Agarwal et al., ICML 2014, Carlini et al., IEEE S&P 2022, Ilyas et al., ICML 2022)? Open, none of them read. Final document, Prior work, and the oracle report's boundary.
19. Hard-learning lower bounds for attackers. Is there any lower bound on a membership, inversion, attribute or reconstruction attacker from a statistical-query lower bound or another hard learning problem? None found (empirical, search-based). Scan, Verdict 3.
20. Seed separation. Is there a formal separation between attackers who know the training seed and attackers who do not? None found. The candidate of 2026-10-25 is split-learning inversion over random expansive ReLU bottom models, polynomial with a known seed and needing super-polynomially many statistical queries without it. Scan, Verdict 4.
21. Transcript leakage of the seed. Does the training transcript a split-learning server sees reveal the seed, or enough of the bottom model, to collapse that separation? Open, the first risk named by the scan and a constraint set on 2026-10-25.
22. Statistical queries for regression. Does a real-valued statistical-query framework carry lower bounds to inversion, which is regression? Open, the second risk of the scan.
23. The oracle report's open choices. Is the cost unit one per call rather than proportional to dataset size? Is a learning node one optimizer step rather than one training run? Can cluster training be made deterministic, as consistency requires? Should a public pretrained model be an input node with its own bank entry? May adaptive adversaries wait for an asynchronous bank? Open, `lib/reports/src/2026-10-16-halil-learning-oracle-definition.tex`, Next.
24. Screening and coding quality. Does the screen miss kept papers at a measurable rate, and do the ledger rows match their papers? Both open. Recall is unmeasured and the rows await a check (2.4).

## 6. Literature state

The venue sweep of 2026-10-16 screened the accepted-paper lists of IEEE S&P, USENIX Security, CCS, NDSS, PoPETs, CRYPTO, EUROCRYPT, ASIACRYPT, NeurIPS, ICML and ICLR for 2023 to 2026. Six language-model screeners kept a paper when two or more parties train or fine-tune on data or models they hold and the contribution concerns privacy or security against an adversary. Screening recall is unmeasured, since only near misses left a record. The 2026 counts lack NeurIPS 2026 and may lack part of CCS 2026. EuroS&P, SaTML and CSF were not screened. Citation counts from OpenAlex cover 117 papers, because the day's budget ran out.

`lib/literature/screening.csv` has 575 rows on 12 columns (status, key, venue, year, title, setting, axis, award, reason, citations, citations_source, evidence_url). By status, 351 placed, 206 dropped at screening, 14 dropped after reading, 4 without an accessible PDF. By venue, ICML 118, NeurIPS 87, CCS 76, ICLR 73, USENIX Security 60, PoPETs 56, IEEE S&P 39, NDSS 39, ASIACRYPT 13, CRYPTO 5, EUROCRYPT 3, and 6 rows whose venue field carries the year (five anchors from the first four sweeps and HE-OFT). By year, 2023 144, 2024 147, 2025 163, 2026 115, and 6 blank. The 351 placed papers are 349 field papers, HE-OFT and Salem et al.

`lib/literature/ledger.csv` has 22 columns (key, tm, paper, data, model, learning, protection, spec, checks, adversary, sees, knows, sets, goal, stealth, evidence, evaluation, excluded, edge, survives, inferred, note), whose keywords `sink/ledger-columns.md` defines. HEAD has 521 rows on 351 papers. The working copy has 519 rows on 350 papers (2.16). Every row comes from one coder's reading and has a note marked sweep, except the three HE-OFT rows and the two SCEKPSTZ23 rows, which come from full readings. Counted on the 519 rows (deck frames 4, 7 and 8, morning of 16 October), the coded papers are ICML 69, ICLR 54, NeurIPS 49, CCS 41, PoPETs 41, USENIX Security 39, IEEE S&P 25, NDSS 23, ASIACRYPT and CRYPTO 8, and HE-OFT. By year they are 89, 95, 100 and 63 for 2023 to 2026 plus 3 anchors. By kind they are 124 defences, 110 protocols, 74 attacks, 15 theory papers, 6 systematizations, 5 measurements and 16 mixed. The rows split into 235 that set nothing beyond queries and 284 that set more, of which 33 set only their own data. Goals count 202 distinguish, 186 invert, 164 steer and 25 other. 192 rows name no protection. 116 rows record a settled step between two adversaries (75 separations, 36 collapses, 5 both) and 19 record one as open. The deck's frame 11 lists eight settled steps, and only the first, HE-OFT's ordering, rests on a full reading.

`lib/literature/notes/` holds 365 notes in 12 venue folders, acm-ccs 42, arxiv 1, asiacrypt 6, crypto 3, eurocrypt 1, iclr 55, icml 75, ieee-sp 26, ndss 23, neurips 51, popets 41 and usenix-security 41. Their prov field reads sweep in 363 and full-read in 2. Their triage field reads deep in 8, read in 26, skim in 317 and drop in 14. Every relation field reads prior-art. 363 notes hold only the template text, with FILL in every section, and the coded content of those papers lives in the ledger alone. The 14 dropped notes give the reason in the note. The eight deep notes are KSK26, SCEKPSTZ23, CMSPTH23 (PELTA), HLSS25, HHKLS26, PFA22, REGB26 (the integrity SoK) and RT25. The six deep reads not done are the last six.

Read in full, apart from the group's own HE-OFT, is one paper, Salem et al., "SoK: Let the Privacy Games Begin!", IEEE S&P 2023 (SCEKPSTZ23), read on 2026-10-16 at Halil's request and placed outside the inclusion rule. It puts membership, attribute and property inference, DP distinguishability and reconstruction for one trained model into one game anatomy and proves reductions with constants and separations among every ordered pair (proven, toy pipelines). Its Section VI-D states that its games are sequential programs and do not cover federated learning. It therefore owns the distinguish and invert half of the interface for one model, and the protocol graph, the channels, the node choices and the steer goal stay open for the interface. Its Theorem 7 construction is a template for a separation at the distinguish goal. Note `lib/literature/notes/ieee-sp/SCEKPSTZ23.md`.

Every recorded search follows, with its result.

1. 2026-10-16, the venue sweep above. 575 candidates, 351 placed.
2. 2026-10-16, black-box against white-box membership inference. Occupied. Sablayrolles et al. (ICML 2019) give the Bayes-optimal attack under a posterior assumption, which depends on the loss alone. Suri, Zhang and Evans (TMLR 2024, arXiv 2406.11544) argue the assumption fails for SGD and give a white-box attack. Neither note is written. `lib/literature/positioning.md`.
3. 2026-10-16, federated learning attacks evaluated under unrealistic assumptions. Occupied. Wainakh et al. (Sensors 2023), Huang et al. (NeurIPS 2021), Shejwalkar et al. (IEEE S&P 2022), a poisoning SoK benchmark (arXiv 2502.03801, venue unverified) and a 2026 preprint (arXiv 2603.20615). `lib/literature/positioning.md`.
4. 2026-10-16, the final model against all iterates. Cebere, Bellet and Papernot (ICLR 2025) show that with a crafted gradient at every step, releasing only the final model does not improve the privacy guarantee. `lib/literature/positioning.md`.
5. 2026-10-16, one game framework for inference risks. Occupied for one trained model by Salem et al., open for the multi-party protocol, its channels and the steer goal. `lib/literature/positioning.md`.
6. Round 03 of the formal tuning, active security for threshold FHE decryption. Found only for thresholdized BFV, BGV and FHEW, none for CKKS. `sink/2026-10-16-formal-tuning/theory/CURRENT.md`, open problem 6.
7. 2026-10-25, learning-bounded privacy adversaries, `sink/formalizing/sources/2026-10-25-learning-bounded-scan.md`. Six things are formalized already (proven in the papers). They are class-relative usable information (Xu et al., ICLR 2020), and privacy against a bounded adversary class with information-theoretic bounds only (Zhao et al., NeurIPS 2020). They are the reference-sample complexity of membership inference for an unbounded attacker (Haghifam, Smith and Ullman, arXiv 2508.19458), and privacy-to-learnability reductions (Carlini et al. on instance encoding). They are Bayesian privacy over a law of encoders (NeuraCrypt), and inversion complexity with known weights. Lei et al. (NeurIPS 2019) prove preimage existence NP-complete and invert random expansive layers exactly. Two things are measured only (empirical). Balle, Cherubin and Hayes reconstruct much better with the known initialization, so the seed acts as a resource. UnSplit inverts an unknown bottom model at MNIST split depth one, and PCAT attacks with small public data. NeuraCrypt is broken empirically (Carlini et al., arXiv 2108.07256). Abbe et al. (NeurIPS 2021, Theorem 1c) let statistical queries simulate mini-batch SGD when batch size times squared precision exceeds a logarithmic factor, so a statistical-query lower bound binds SGD-trained attackers only in that regime. Open as far as found are lower bounds on privacy attackers from hard learning problems, leakage bounded in both class and samples with a lower-bound technique, and a formal separation between known-seed and unknown-seed attackers.

Searches named and not run are the privacy-auditing literature and the three lines in the oracle report's boundary (open problem 18), and the backward and forward citation sweeps of `sources.yml`.

## 7. Decisions

There are no entries in `lib/profs/rulings.md`. The rulings and decisions below come from the files named.

2026-10-16.

- Scope. HE-ML is a literature study of multi-party learning threat models, with the setting kept abstract. `CONTEXT.md`, What this is.
- Venue rule, Halil. Top venues only, the eleven listed, open to his correction, with a notable paper elsewhere recorded and given no PDF. `CONTEXT.md`.
- Language. HE-ML takes HE-OFT's terms unchanged, because the team is the same. `CONTEXT.md`.
- Ruling, Halil. The data space is never the product of an input space and a label space, because that assumes supervision. `CONTEXT.md` and deck frame 5.
- Ruling, Halil. The interface has three primitives (data, model space, learning function) at the highest generality, and a parameterization is an instance of the model space. `CONTEXT.md` and deck frame 5.
- Repo memory, Halil. Move the ledger column dictionary to the sink once the ledger is finished (done). Keep paper PDFs in Google Drive and never commit one. Group notes and PDFs in one folder per venue. Push finished work straight to main without a pull request, and push only when he asks in the turn. `CLAUDE.md`, Repo memory.
- Salem et al. placed by hand at Halil's request, outside the inclusion rule. `CONTEXT.md` and `screening.csv`.
- Field counts leave HE-OFT out, from Halil's "forget about HE-OFT, smudging etc." when he asked for one ready-to-read report of the sweep. Auto-memory `~/.claude/projects/-Users-a90-Documents-RESEARCH-HE-ML/memory/study-from-one-report.md`, and 2.4.
- The formal tuning opened at Halil's request. His goal was non-trivial proofs with the oracle inside, such that removing the oracle leaves a much larger learning problem, and a well-tested definition in its simplest form. `sink/2026-10-16-formal-tuning/README.md`.
- Orchestrator rulings. The stopping rule (six review rounds, no blocking challenge, definitions accepted twice, six results with three non-trivial, at most twelve rounds). After round 02, criterion 4 of the bar is tested against the drawn-seed discipline when the actor is an experimenter or an auditor. Same file.

2026-10-17.

- Halil fixed the end of the rounds at round 10, whose challenger turn also wrote the audit. `sink/2026-10-16-formal-tuning/README.md`.
- The audit returned FINAL ACCEPT. `final/audit.md`.

2026-10-25, from the commissioning session and not yet in any file except this one.

- Halil. The oracle's practical value is that it hands over arbitrary removals, twin trainings that real training cannot afford. Its theoretical value is the separation between named and hidden seeds.
- Halil. Move to a computational view. Measure an adversary by computational and learning resources, and reduce learning-security problems to known learning problems, with or without the oracle.
- Halil. Cheap cryptographic plug-ins, such as putting a PRG somewhere, do not count. Discovering that some aspect of a model reduces to or yields a PRG would count.
- Halil. The framework must be realizable or approximately realizable by experiments.
- Halil. Polynomial-time adversaries are fine.
- Assistant judgment, same session (heuristic). The upper bounds of the learning-oracle theory hold without the oracle given seed control. The oracle's theoretical content is the lower bounds and the seed separation.
- Candidate next target, not adopted. A seed separation for split-learning inversion against statistical-query attackers. Three constraints bind it, NeuraCrypt's empirical break, UnSplit's success at depth one, and the training transcript leaking the seed.

## 8. Where to look

| Topic | Path |
| --- | --- |
| Terms, symbols, scope, current state | `CONTEXT.md` |
| Repository rules and repo memory | `CLAUDE.md` |
| Interface definitions and its HE-OFT, FedAvg and split instances | `lib/reports/src/2026-10-16-halil-adversary-interface.tex` |
| The sweep, corrected counts, the seven templates, anchors to read first | `lib/reports/src/2026-10-16-halil-swept-papers-and-threat-models.tex` and its CSVs under `lib/reports/src/data/` |
| The superseded sweep trends and the faulty deviating rule | `lib/reports/src/figures/2026-10-16-halil-multi-party-learning-sweep-trends.py` |
| The first oracle definition and its motivation | `lib/reports/src/2026-10-16-halil-learning-oracle-definition.tex` |
| The meeting deck, settled steps, HE-OFT on the interface, HE decryption channel | `lib/profs/2026-10-16-meeting/slides.tex` |
| Final oracle definitions, theorems and proofs | `sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md` |
| Audit findings on the final theory | `sink/2026-10-16-formal-tuning/final/audit.md` |
| Statement register, open problems in full, old names | `sink/2026-10-16-formal-tuning/theory/CURRENT.md` |
| Round log, non-triviality bar, stopping rule | `sink/2026-10-16-formal-tuning/README.md` |
| Challenges to the first oracle definition | `sink/2026-10-16-formal-tuning/round-00/challenger.md` |
| Proofs given by pointer | `sink/2026-10-16-formal-tuning/round-01/builder.md` to `round-10/builder.md`, located by the register |
| Ledger columns, reductions, terms that drift | `sink/ledger-columns.md` |
| Every coded coalition | `lib/literature/ledger.csv` |
| Every screening decision | `lib/literature/screening.csv` |
| Recorded searches and the empty positioning slots | `lib/literature/positioning.md` |
| The one outside paper read in full | `lib/literature/notes/ieee-sp/SCEKPSTZ23.md` |
| HE-OFT read in full | `lib/literature/notes/arxiv/KSK26.md` |
| Papers with no PDF | `sink/unavailable.md` |
| Learning-bounded adversaries and the seed as a resource | `sink/formalizing/sources/2026-10-25-learning-bounded-scan.md` |
| Venues, watch list, sweep dates | `lib/literature/sources.yml` |
| PDFs | `lib/literature/pdfs/`, a symlink to Google Drive |
