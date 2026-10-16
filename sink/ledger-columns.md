# The interface and the ledger columns

Merged on 2026-10-16 from five reader extractions (43 papers, `prov: sweep`) and
the full reading of HE-OFT (KSK26), then used to code the wider sweep. The
`unlearning` keyword was added during coding. This file replaces
the earlier flat list of fifty columns. Twenty-two columns now hold everything
the fifty held, and each column's keywords carry the detail. Section 4 lists
every distinction the readers reported and the keyword that now holds it, so
nothing is dropped.

## 1. The interface

Three primitives, data, a model space and a learning function, with no
structure assumed on any of them. The definitions are in
`lib/reports/2026-10-16-halil-adversary-interface.pdf`.

A protocol is a graph of nodes. A node is one application of a learning
function to a model, a dataset and a hypothesis class, or one opening of a
protected value (a decryption, an unmasking). Aggregation is a node like any
other, whose dataset is the clients' models.

Each party stands in four relations to each node:
- it sees the node's output through a channel;
- an argument of the node is public to it;
- it sets an argument;
- it sets the output.

An adversary is a coalition of parties together with a goal. A protocol may
face several coalitions at once, each with its own goal, as in HE-OFT, AGGPS23
and GLX25. The ledger therefore has one row per coalition.

## 2. Five reductions the merge makes

These are what make the columns fewer. Each follows from the interface. None of
them is a claim of a paper.

1. Knowledge is publicity of arguments. What a paper calls the adversary's
   knowledge is a node argument public to it: the architecture is the class,
   the pretrained weights are the starting model, the training details are the
   learning function's parameters, and the data prior is the distribution of a
   dataset. Surrogate data is one more dataset the adversary holds. The
   knowledge ladders of CFMPV25 (threat models A to H) and DHWSGRC25 (Levels 0
   to 5) unfold into `sees`, `knows` and `sets`. Neither ladder is nested
   (CFMPV25 Table 1, DHWSGRC25 Table 7), so storing the components loses
   nothing and storing the level would.
2. Behaviour terms follow from the relations. Curious means a distinguish or
   invert goal. Byzantine or malicious means the coalition sets something
   beyond queries. Protocol-compliant but malicious (ZDTLL26) means it sets a
   node outside the specified protocol, here a fine-tuning after release.
   Covert means a stealth constraint. The paper's own term stays as provenance.
3. Data poisoning and Byzantine behaviour differ only in what is set and when.
   Data poisoning sets the data argument once, before training. A Byzantine
   coalition sets node outputs each round, after seeing the view. BLGB26's
   separation is a theorem about these two relations. SHKR22 calls the same
   line offline against online.
4. A check restricts a relation. Each integrity check of REGB26 (CL1 to CL4, AG1
   to AG3), each input validation and each zero-knowledge proof removes a
   choice. A check can move an adversary down the order. BLGB26 argues that a
   proof of computation from committed data turns setting outputs into setting
   data.
5. The nominal channel and the effective channel can differ. Under secure
   aggregation the server nominally sees a sum, but with a model per client the
   sum equals one update (PFA22). The ledger records the nominal channel under
   `sees` and the collapse under `edge`.

## 3. The columns

A cell holds `keyword=value` pairs separated by `;`. A list inside a value uses
`,`. A node is named as in `sees`. `n/a` means the paper does not address the
keyword, and `unstated` means it addresses it without saying.

### Identity

| Column | Keywords |
| --- | --- |
| key | IACR key |
| tm | slug of the coalition and its goal, e.g. `semi-honest-server`, `deviating-clients` |
| paper | `venue`; `type` = attack, defence, protocol, theory, measurement, SoK; `setting` = horizontal FL, vertical FL, split, decentralized, FL fine-tuning, secure aggregation, multiparty HE, MPC training; `formality` = ideal functionality, game, theorem with assumptions, prose, taxonomy |

### The protocol

| Column | Keywords |
| --- | --- |
| data | `space` = labeled pair, unlabeled input, token sequence, feature block, vector; `partition` = horizontal, vertical; `holders` = who holds which dataset, data owner apart from trainer where they differ, label holder in vertical learning, server-held data (trusted or synthetic); `public` = pretraining corpus, public auxiliary; `heterogeneity` = IID, label skew (Dirichlet alpha), feature skew; `dp_unit` = record, client |
| model | `space`; `init` = random, pretrained public, pretrained private; `class` = full, LoRA (rank), head, client-side layers (one cut, U-shaped), bottom models; `served` = full model to all, model to querier, labels only, nothing |
| learning | `local` = FedSGD (one-step gradient), K steps (multi-step change), local fine-tuning; `merge` = mean, weighted mean, robust (rule), clustering, sum; `merge_family` = distance-based, behaviour-based; `merge_reference` = fixed, local, network; `tolerance` = the corrupted count the merge is tuned for; `rounds` = one-shot, T; `sampling` = clients per round, chosen by the server or by self-selection; `topology` = single server, two servers, committee, peer-to-peer, split (parallel, sequential relay), server and quorum; `dropout` = tolerated fraction; `unlearning` = none, client removal, record removal, class removal (federated unlearning is a learning function that maps a trained model and a deletion request to a model) |
| protection | `mechanism@node` = none, DP central, DP local, DP distributed, secure aggregation, threshold HE, MPC, TEE, ZK; `noise_on` = input, embedding, update, output; `noise_added_by` = server, each client, joint; `calibration` = constant, average-case, worst-case, lambda-dependent; `sampling` = independent per party, collaborative; `opening_chosen_by` = protocol, server, any party; `opening_leaks` = the function only, noise realization, error events, accepted count, sum of errors |
| spec | `ideal_output` = what the ideal functionality returns (exact value, value plus noise, adversary-chosen subset, shift); `ideal_leakage` = what any realizing protocol may reveal; `output_guarantee` = abort, guaranteed output delivery, robust (exclude and continue), none |
| checks | per check `certifies@node@verifier`, with certifies = domain membership (norm, range), honest computation from committed data, authentic data, well-formed key or ciphertext, correct decryption share, consistent model to all, correct admission set, correct aggregation; `timing` = online, ex post, asynchronous (delay K rounds); `on_failure` = abort, exclude, rollback; `phases_covered` = key generation, encryption, evaluation, decryption |

### The adversary

| Column | Keywords |
| --- | --- |
| adversary | `role` = server, clients, querier, active party, passive party, committee member, decryptor, eavesdropper, or several; `term` = the paper's own words, per role; `population` = fraction or count corrupted overall; `cohort` = count per round, by sampling or by server selection; `corruption` = static, adaptive; `majority` = honest, dishonest; `phase` = training, serving, both |
| sees | per item `node:channel@rounds`. node = update (one-step gradient), update (multi-step change), aggregate, model per round, final model, activations at a cut, gradients at a cut, served answers, decrypted value, BN statistics, class counts. channel = plain, sum (k summands), enc, noise, post-processed (quantized, sparsified, clipped), commitment. rounds = one, all, snapshots, fraction, final |
| knows | `public_args` = architecture, pretrained weights, fine-tuned weights, hyperparameters, local configuration, defence, data distribution; `own_data` = surrogate data (in or out of distribution), shadow data, captured clients' data; `own_secrets` = key shares of the corrupted parties; `benign_updates` = seen, estimated from own clients, withheld; `resources` = generative model, compute bound |
| sets | per choice `what@node:when`. what = data argument, model argument (same to all, per client), class argument (architecture, inserted module), learning function (code, loss, hyperparameters), merge (rule, per-target schedule, cohort, Sybils), node output (update, gradient returned, report to a clustering step, decryption share), ciphertext for decryption, queries, release (post-protocol change). when = committed before training, adaptive per round, at serving |
| goal | `type` = distinguish, invert, steer, other (free-riding, compliance bypass, selfish advantage); `term` = the paper's own name for the goal; `target` = record membership, property, record, attribute, label set, class histogram, attribution, model, secret key, accuracy loss, misalignment, trigger-conditioned behaviour, content injection; `tolerance` = exact, suffix given prefix, bag of tokens, class prototype, fidelity level; `scope` = global model, per client; `means` = an intermediate goal used to reach this one; `origin` = the phase that installed a steered property (pretraining, federation); `metric` = advantage, AUC, TPR at FPR, PSNR, SSIM, LPIPS, ASR, accuracy drop, fidelity, key recovery, model-side vulnerability score |
| stealth | `detector@node` = weight space, gradient space, behaviour across rounds, behavioural test of the model, aggregation rule, victim-side detection; `run_by` = server, victim, other clients; `status` = none, required, measured |

### Evidence and position

| Column | Keywords |
| --- | --- |
| evidence | `model` = UC, standalone simulation (concurrent or not), game (IND-CPA, IND-CPA-D, key recovery, integrity), DP, convergence, generalization by stability, single-step bias, tail bound, constructive lower bound, universal upper bound, non-identifiability; `assumptions` = verbatim, e.g. RLWE, ROM, generic group, PKI, honest majority, convexity, smoothness, bounded heterogeneity, RIP; `status` = proven, empirical, proven and empirical, sketch only; `result` = one line with a theorem or table pointer; `gap` = where the proven object differs from the evaluated one (theorem algorithm against deployed algorithm, information-theoretic bound against computational realization, a proof error reported by a later paper) |
| evaluation | `datasets`; `largest_model`; `scale` = clients, examples per client; `compared` = attacks or defences evaluated against; `adaptive` = whether an adversary adapting to the defence is evaluated, yes or no; `cost` = time, communication, queries |
| excluded | what the paper itself puts out of scope, verbatim where short |
| edge | the step between two adversaries the result settles, `weaker < stronger: collapse` or `: separation`, with the condition |
| survives | per protection layer `mechanism: yes, no, unstated` |
| inferred | the column keywords we derived and the paper did not state, e.g. `goal.type, survives` |
| note | `notes/<key>.md` |

## 4. Where each reported distinction went

Paper keys are the ones the readers cited.

| Distinction | Papers | Held by |
| --- | --- | --- |
| Threat-model ladders by knowledge and capability | CFMPV25, DHWSGRC25 | knows, sees, sets (reduction 1) |
| Detectability of an active choice | CFMPV25, DHWSGRC25, GDJV24, CFMPV26 | stealth |
| One-step gradient against multi-step change | DHWSGRC25, PDBMV24 | learning.local, sees node |
| Round at which the adversary sees, snapshots, a fraction of updates | DHWSGRC25, RDGSM26, ZDTLL26 | sees rounds |
| Which node a defence protects | CFMPV25 | protection mechanism@node |
| Surrogate data in or out of distribution | DHWSGRC25, CFMPV25 | knows.own_data |
| Data owner apart from trainer | REGB26 | data.holders |
| Behaviour per role on two axes | REGB26 | adversary.term, reduction 2 |
| Verifier class, online against ex post checking | REGB26 | checks verifier, timing |
| Split view (each honest party shown something different) | REGB26 | sets model argument per client, checks consistent model |
| Goals outside the three | REGB26 | goal.type other |
| Non-identifiability theorem | DHWSGRC25 | evidence.model |
| Model-side vulnerability scores | CFMPV25, DHWSGRC25 | goal.metric |
| Model consistency across clients | PFA22, ZSEEAB24, GDJV24, EZL26, CFMPV26 | sets model argument (same, per client), merge per-target schedule |
| Which lever the server pulls | GZZVZPW26, GDJV24, ZSEEAB24, NVNT25, LAWKDM26, EZL26, JYHWCL24 | sets what |
| Nominal against effective channel | PFA22, ZSEEAB24, JYHWCL24, GDJV24 | sees (nominal), edge (effective) |
| What the noise is applied to, who adds it, colluders skipping their share | NVNT25, PFA22, JYHWCL24 | protection noise_on, noise_added_by, survives |
| Content against attribution | PFA22, ZSEEAB24 | goal.target attribution |
| Means against end goal | LAWKDM26, EZL26, PAB21, YLGHP25, RDGSM26, ZDTLL26 | goal.means |
| Corruption over the population against the cohort | JYHWCL24, AFGGPRV24, SHKR22, FNLSIY25 | adversary.population, cohort |
| Aggregator tolerance as a parameter | AFGGPRV24, FNLSIY25 | learning.tolerance |
| Knowledge cost, running time, bias learned over rounds, sparsity assumption | NVNT25, ZSEEAB24, GZZVZPW26 | knows.resources, evaluation.cost, evidence.assumptions |
| Lower bound on one attacker against upper bound over all | NVNT25, GZZVZPW26, JYHWCL24 | evidence.model |
| Whether an attack works on ciphertexts | EZL26, RDGSM26 | survives |
| Pretrained against fine-tuned weights known | CQYZFDX24 | knows.public_args |
| Phase that installed the steered property | YCLYWC25, TTPLHLCL26, RDGSM26 | goal.origin |
| Cut position, label holder, forward and backward messages | CQYZFDX24, PAB21, RPKAKS25, YLGHP25 | model.class, data.holders, sees nodes |
| Inversion granularity | PDBMV24, RDGSM26, ZDTLL26, PAB21 | goal.tolerance |
| Defences that perturb against detections that observe | YLGHP25 | protection against stealth |
| Rank of the observed update bounded by the class | PDBMV24, ZDTLL26 | model.class with edge |
| Sequential relay, non-comparable client models | RPKAKS25 | learning.topology |
| Kinds of steer target | YCLYWC25, TTPLHLCL26, ZDTLL26, RPKAKS25 | goal.target |
| Training-time against test-time adversary | YLGHP25, KSK26 | adversary.phase |
| Generative model as an adversary or defender resource | RDGSM26, YCLYWC25, ZDTLL26 | knows.resources |
| Number of summands under secure aggregation | ZDTLL26 | sees channel sum (k) |
| What an opening reveals beyond the function | HHKLS26, ZZLP25, CSBB24, JZDK25, BGLLMRY23 | protection.opening_leaks |
| What the ideal functionality outputs | HHKLS26, GKKTW26, KSK26 | spec.ideal_output, ideal_leakage |
| Who picks what is decrypted, and well-formedness | ZZLP25, CSBB24, GNSJ24, HLSS25, CMSPTH23, KSK26 | protection.opening_chosen_by, sets ciphertext, checks well-formed |
| Noise calibration and independent against collaborative smudging | CSBB24, GNSJ24, HHKLS26, KSK26 | protection.calibration, sampling |
| Corruption and dropout as separate fractions | GKKTW26, BGLLMRY23, FDCTKRFJPW23 | adversary.population, learning.dropout |
| Roles beyond data holders (evaluator, verifier, committee, two servers) | CMSPTH23, GKKTW26, FDCTKRFJPW23, JZDK25 | learning.topology, adversary.role |
| What an input check certifies, detect against robust | BGLLMRY23, FDCTKRFJPW23, ZWQWWLSYYZJZ26, JZDK25 | checks certifies, on_failure |
| Which protocol phases are proven | HLSS25, CMSPTH23 | checks.phases_covered |
| Delay between deviation and detection | ZWQWWLSYYZJZ26 | checks.timing |
| Abort, guaranteed output, robustness | GKKTW26, JZDK25, ZZLP25, BGLLMRY23 | spec.output_guarantee |
| Finer proof models, concurrency | CSBB24, GNSJ24, ZWQWWLSYYZJZ26, BGLLMRY23, ZZLP25, JZDK25, GKKTW26 | evidence.model |
| Static against adaptive corruption | ZZLP25, ZWQWWLSYYZJZ26 | adversary.corruption |
| Proof errors reported in other papers | GKKTW26 on Flamingo and TACITA | evidence.gap of the cited paper |
| When the adversary commits | BLGB26, SHKR22, LK25 | sets when, reduction 3 |
| Source of the picture of benign updates | FNLSIY25, KKDK24, SHKR22, CKS24, VMBKN25, GLX25 | knows.benign_updates |
| Several adversaries in one protocol | AGGPS23, GLX25, KSK26 | one row per coalition |
| Optimization, generalization and single-step guarantees | AFGGPRV24, FNLSIY25, AGGPS23, GLX25, BLGB26, CKS24 | evidence.model |
| Theorem algorithm differs from the evaluated one | FNLSIY25, CKS24 | evidence.gap |
| Defender's auxiliary data and aggregator families | CKS24, FNLSIY25, RT25 | data.holders server-held, learning.merge_family, merge_reference |
| Hyperparameters, clustering reports and principal vectors as choices | LK25, VMBKN25, KKDK24 | sets learning function, node output |
| Success per client against the global model | VMBKN25 | goal.scope |
| Record against client-level DP | GLX25, AGGPS23 | data.dp_unit |
| Cryptography that changes the threat model | BLGB26, GLX25 | checks, edge (reduction 4) |

## 5. Terms that change meaning between papers

The ledger stores interface values, so these terms appear only as provenance.

- Malicious: deviating in protocol steps (crypto papers), in model parameters
  (server attacks), or in released models only (ZDTLL26).
- Distributed DP: local Gaussian noise per worker (AGGPS23), or partial noise
  per client against central noise generated jointly (GLX25).
- The robustness constant kappa: bounded by the variance of honest updates
  (AFGGPRV24), or by the spectral norm of their covariance (AGGPS23, BLGB26).
- Passive: no protocol deviation (crypto papers), or no parameter manipulation
  (gradient inversion SoKs).

## 6. Data issues found in the papers

- LAWKDM26 Sec. VI-B names CIFAR-10, while its figures show CIFAR-100 with a ViT.
- TTPLHLCL26 Sec. 5.1 gives batch size 8 and 0.2 local epochs, against batch size 4 and one epoch in its Table 17.
- CQYZFDX24 gives its default split as 6-21 in Sec. 4.1 and as 6-27 in its tables.
- CFMPV25 places Boenisch et al. under threat model G in Sec. 4.3, but under H in Table 2.
- DHWSGRC25 Table 7 labels Garov et al. as malicious and active, yet omits Level 5 from its assumptions.
