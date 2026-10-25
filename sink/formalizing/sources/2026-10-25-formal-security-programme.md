# FORMAL_SECURITY research programme, digest

Source repository `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY`, read only, on 2026-10-25. Every path below is relative to it. The stratum digested is the programme, meaning the root `CLAUDE.md` and `README.md`, `.tools/proof.tex`, and everything under `exp/`. The `wiki/`, `raw/` and `.sink/` strata are digested elsewhere. Nothing here was re-verified. Each verdict is the one the repository records, with the date it records.

## 1. What the programme is

The programme asks how to state the security of a learned model in computational terms, so that an attack's capability becomes a measured quantity against a priced adversary (`exp/docs/notes/intro-computational-security-of-learning.md` §0 to §3). Its method is to reduce one learning problem to another, because attacks are themselves learning algorithms, and its instrument is a success criterion `R` that quantizes an approximate learning outcome into a bit, fixes the baseline and selects the problem the adversary solves (`exp/docs/CONTEXT.md`, `exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md`). The root `CLAUDE.md` records it as a PhD proposal on the computational security of learning as of 2026-07-25, with the theory built as an adversarial two-agent dialogue in `exp/docs/notes/chapter-24.md`. On 2026-08-05 the scope was fixed to measuring an attack against a concrete adversary, with hardness deferred and no defence proposed, and the same day `output/` was renamed `exp/`. A PI meeting that day asked for a survey whose contribution would be definitions (`exp/docs/meetings/2026-08-05-pi.md`). Two sweeps the same day found the criterion and the privacy and integrity unification already published, so the definitional claim was withdrawn and the adversary axis, a class and a budget, was left as the only defensible contribution (`exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`). The active deliverable is an IEEE S&P 2027 SoK that codes 200 formal works by the party each main claim bounds, the unit and the tightness, and that proves nothing (`exp/survey/CONTEXT.md`). Its subject was fixed on 2026-08-20 as the characterization of adversary capability, with imposed bounds and training efficiency left out, and it became its own project root on 2026-09-17. Its README records a re-scoping toward computation and information theory as of 2026-10-13 (`exp/survey/README.md`). The newest thread, opened 2026-10-13, defines an idealized training oracle in which membership leakage can be bounded and white-box and black-box attackers separated (`exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`).

## 2. Terms

The programme keeps three ledgers that do not fully agree. Section 2.5 lists the collisions.

### 2.1 Programme ledger, `exp/docs/CONTEXT.md`

| Term | Meaning | Status | Defined in |
| --- | --- | --- | --- |
| `D` | the dataset | fixed | `exp/docs/CONTEXT.md` |
| `f` | a function in the hypothesis space, the object training reaches | fixed | same |
| `L` | the training map `D ↦ f` | fixed | same |
| `R` | the quantizer between the approximate learning layer and the exact cryptographic layer, exact by type, its parameters placed where the approximation is quantized, one `R` indexed by search or decision and by the attack target | fixed, ours, relation form borrowed from Cohen et al. ITCS 2025 | same, and `exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md` |
| baseline of `R` | what a party with public knowledge alone achieves on `R`, a field of `R` and not of the game | fixed, ours | `exp/docs/CONTEXT.md` |
| degenerate baseline | a baseline at 0, 1/2 or 1, where subtracting it is a no-op, which forces raw advantage | fixed, ours | same |
| `η` | the tolerance of `R`, the dial between the population regime (coarse, nothing to measure) and the cryptographic regime (tight, needs an assumption) | fixed, ours | same |
| party searching for `R`, `P` | the attacker in the privacy criteria, the detector in the backdoor criterion, an explicit argument of `Φ` | fixed, ours | same, and `exp/docs/reports/2026-08-05-unfiled-concrete-r-criteria.md` |
| displacement | what a training-time adversary does to `f`, graded none, `x` non-adaptive, `x` adaptive, `f` | fixed, ours | `exp/docs/CONTEXT.md` |
| phase of action, phase of measurement | when the adversary acts and when `R` is evaluated, which differ for a backdoor | fixed, ours | same |
| `𝒜` | the adversary's algorithm class | fixed | same |
| `b` | the adversary's resource budget | fixed | same |
| security profile | the curve `b ↦ ε(b)`, the measurable object | proposed, ours | same |
| `Φ(P, 𝒜, b)` | `inf { θ : some A ∈ 𝒜 at budget b makes P win R_θ above baseline }`, read as leakage when `P` is the attacker and as the detection floor when `P` is the detector, requires `{R_θ}` monotone in `θ` | proposed, ours, the name "leakage function" is banned | same, and `exp/docs/reports/2026-08-05-unfiled-leakage-and-integrity-functions.md` |
| the three maps | training `D ↦ f`, parameterization `w ↦ M_w`, feature `x ↦ f_θ(x)`, never conflated | fixed, ours | `exp/docs/CONTEXT.md`, `exp/docs/notes/game-family-and-reduction-targets.md` §2 |
| `δ` | the fine-grained gap, adversary work at least honest work to the power `1+δ` | fixed, borrowed from fine-grained cryptography | `exp/docs/CONTEXT.md` |
| attack surface axes | phase of observation (training, test), displacement, `R` target (a property of `D`, of `f`, or of `f(x)`) | fixed | same, and `exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md` |

### 2.2 Terms of the working notes

| Term | Meaning | Status | Defined in |
| --- | --- | --- | --- |
| `COMP-MEM` | computational membership indistinguishability, the on-ramp game, the computational analogue of DP | proposed, marginal-advantage form refuted as a no-op | `exp/docs/notes/intro-computational-security-of-learning.md` §4 |
| `COMP-TW` | training-world indistinguishability, two worlds differing by a controlled `Δ` | proposed, alive for reconstruction and property inference, dead for membership | same §4, `exp/docs/notes/game-family-and-reduction-targets.md` §1 |
| `κ` | capability vector, what the adversary observes, when, how much, passively or by choosing, the CPA handle generalized | proposed | intro §1 and §4 |
| `κ₀` | the baseline adversary holding only prior and public knowledge | proposed | intro §4 |
| `GAME[O, T, S, κ₀]` | observation map, target, success functional, baseline, with the adversary class entering only at reduction time | proposed 2026-07-26 | `exp/docs/notes/game-family-and-reduction-targets.md` §1 |
| fiber of the training map | `L⁻¹(w)`, all datasets that produce `w` | framing refuted at its core 2026-07-26 | `exp/docs/notes/fibers-of-the-training-map.md` §1 |
| navigability | whether a point of the fiber consistent with side information can be found efficiently | same | same §5 |
| learning adversary | an adversary bounded by learnability rather than by input distance | informal conjecture of Halil's | `exp/docs/notes/ideas.md` |

### 2.3 Chapter 24 terms, `exp/docs/notes/chapter-24.md`

| Term | Meaning | Status | Where |
| --- | --- | --- | --- |
| source `Π` | a program for the universal machine `U` on a uniform seed `ρ`, where every distributional assumption must live | agreed | message 1, summary in message 21 |
| learner `L`, advice `w`, `eval = U`, `M_w = U(w, ·)` | the learner reads `Π` through access modes (i.i.d. draw, membership query, statistical query, chosen input) and writes advice, inference runs `U` on `w` for `t_eval` steps | agreed | message 1 |
| principle (3) | demote the distribution from foundation to parameter, `D = Π_*(Uniform)` | law | message 1 |
| `d_R(w, Π)` | behavioural distance, the size under a query-region metric `R` of the region where `eval(w, ·)` disagrees with `Π` | agreed | message 1 |
| `Risk*(T, κ, r)` | the infimum of expected task loss over players with handles `κ` and budget `r`, read with aggregation `⊕ ∈ {E, quantile, sup}` and a base | agreed | messages 1, 7, 21 |
| `LEARN_κ[s, t, |w|, ε]` | the native class of source families learnable with those resources | proposed | message 1 |
| membrane | the boundary across which `L` reads `Π`, splitting resources into deploy and source sides, whose closure carries the agentic loop | agreed | messages 5 to 21 |
| `τ`-staircase | `τ_stat ≤ τ_detect ≤ τ_recover`, the thresholds at which a task becomes statistically determined, detectable, recoverable | agreed | messages 5, 21 |
| `Kt` | Levin's time-bounded Kolmogorov complexity, in five roles (metric weight, potential, capacity `Kt(w)`, security object, learner objective) | agreed | messages 6, 7 |
| `H_L` | learner randomness, a metered entropy budget, shared by privacy and certified robustness | agreed | message 7 |
| `Λ` | Lipschitz sensitivity modulus, `Λ_train`, `Λ_eval`, `Λ_C`, `Λ_eval^sup` | agreed | messages 7, 14, 31 |
| `I`, `I^←` | forward information (learning) and reverse information (steering) across the membrane | agreed | message 20 |
| `R` (reproduction number) | `Λ_train · Λ_C · Λ_eval^sup · ρ_hit` for a backdoor across retraining generations | agreed | messages 20, 31 |
| `r_judge` | the budget of a `U`-bounded judge that approximates a predicate | agreed | message 28 |
| `Clean_r(w, Π)` | no `x` with `Kt(x) ≤ r` on which a budget-`r` judge separates `eval(w, x)` from `Π(x)` | agreed | message 20 |

### 2.4 Survey and formalization terms

| Term | Meaning | Status | Defined in |
| --- | --- | --- | --- |
| party | whoever a work's main claim bounds, attacker, learner, auditor, mechanism, or nobody | fixed | `exp/survey/CONTEXT.md` |
| unit | the resource a bound is stated in, time, circuit size, queries, samples, memory, algorithm class, perturbation, corruption, privacy budget | fixed | same |
| tightness | unstated, poly, quasi-poly, conditional, class, budget, exponent, relative, measured | fixed | same, `exp/survey/lib/literature/codebook.md` Table 2 |
| relative bound | a bound stated as a relation between two parties' work | fixed | same |
| exponent | a bound stated as an exponent in one party's own resource | fixed | same |
| budget | a numeric allowance such as a perturbation radius or a corruption fraction | fixed | same |
| baseline | what a party with public knowledge alone achieves against the target | fixed | same |
| adversary class | the set of algorithms a claim quantifies over | fixed | same |
| access, phase, attack family | strongest access granted, when the adversary acts, the attack in the standard taxonomy | fixed | same |
| assessed | whether a work treats its bound as its object or leaves it a side condition, Halil's axis | fixed | same, codebook Table 2 |
| near miss | a work whose tightness and assessment disagree | fixed | `exp/survey/CONTEXT.md` |
| corpus | the 200 classified works | fixed | same |
| `D` (survey symbol) | the degree bound of a low-degree adversary | fixed | same, symbols table |
| recipe | a public training procedure (architecture, loss, optimizer, batch rule, initialization rule, step count, internal noise) fixing a step function | definition | `exp/survey/paper/parked/formalization/oracle.tex` Def Recipe |
| trace | `(w_0, (B_1, g_1, w_1), …, (B_T, g_T, w_T))`, everything that happened in training | definition | same, Def Trace |
| learning oracle | passive form returns a fresh trace on a corpus with fresh coins, interactive form runs one step per call with parties attached to ports | definition | same, Defs Passive and Interactive |
| view | a public, possibly lossy function of a trace, or a stateful query interface with a budget, a game parameter and never an oracle feature | definition | same, Def View |
| read budget, write budget | metered oracle cost a party may spend, and the steps and metric distance by which it may deviate at a port | definition | same, Defs Metered cost and Write budget |
| view-generic adversary | an adversary that touches corpus, training and model only through granted views within budgets and computes freely otherwise | definition | same, Def View-generic adversary |
| declaration | what a game asserts about the recipe's outputs, the target family with its unit, and the data noise | definition, content open | same, Section The adversary class |
| transfer hypotheses | no skipping (a trace's content is not obtainable below the work of the walk) and no aiming (no inverse map from desired properties to weights cheaper than learning) | hypotheses, recipe-relative | same, Section passive form, and `price.tex` |
| access class | a set of oracle operations (`train`, `eval`, `grad_x`, `grad_θ`, `reveal`) with a budget on each | definition 2026-10-13 | `exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex` |
| ideal representation | conditioned on the learned function, the parameters are independent of the training set | assumption 2026-10-13 | same |
| representation leakage, extraction cost | the information part and the computational part of the white-box against black-box gap | definition 2026-10-13 | same |
| necessary leakage, achievable leakage | least leakage every learner at a utility level has, and least leakage some learner at that utility reaches | recorded proposal 2026-10-13 | `exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md` |
| version space `V(S)` | hypotheses consistent with `S`, the oracle outputs `h ~ Unif(V(S))` | definition 2026-10-13 | `exp/survey/lib/reports/src/2026-10-13-halil-version-space-oracle.tex` |

### 2.5 Name collisions inside the repository

- `R` has three meanings. It is the quantizer in `exp/docs/CONTEXT.md`, the query-region metric in Chapter 24 message 1, and the backdoor reproduction number in Chapter 24 messages 20 and 31. Balle, Cherubin and Hayes also write `R` for the reconstruction attack itself.
- `Φ` has four meanings. It is the leakage and detection function, the Chapter 24 potential `|w| + log t`, the fibre of the parameterization `Φ(f)` in the 2026-10-13 AI oracle report, and the envelope function in `θ_comp ≤ Φ(θ_data)`.
- `D` is the dataset in the programme ledger and the degree bound in the survey ledger.
- Fiber means the training-map fiber in `exp/docs/notes/fibers-of-the-training-map.md` and the parameterization fibre in the AI oracle report.
- The PI's "leakage function" is banned as a name, since searchable-encryption leakage profiles, quantitative information flow and train-test contamination already use it.
- Chapter 24 calls the human principal Mursit. Every other file says Halil.

## 3. Results and claims

Statuses are the ones the files record. Reports of 2026-08-05 all carry `status: draft` and `pi_reviewed: false`.

### 3.1 Programme reports, `exp/docs/reports/`, 2026-08-05

- `training-time-attacks-are-displacements`. Every training-time adversary displaces the learned function `f`, and loss increase is one criterion `R` over that displacement. The undetectable backdoor, which preserves clean loss, is the counterexample to the loss-alteration view. Derivation, exhaustive over displacement targets, irreducibility of the families not shown. Corrected the same day by the three-axis report. `exp/docs/reports/2026-08-05-unfiled-attack-surface-decomposition.md`.
- `three-axis-attack-surface`. Phase of observation, displacement and `R` target index every named attack. Gradient inversion in split or federated learning sits at training phase, no displacement, a property of `D`. Derivation. Independence of the axes not shown, and some cells are empty. `exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md` Result.
- `test-time-adversary-is-a-learner`. A test-time adversary runs a learning process whose input is the channel `f` and whose output is `z`. A training-time adversary acts on a learner. The report calls this literally true at test time and structurally true at training time, so the halves take learning-theoretic thresholds and displacement geometry respectively. Same report.
- `displacement-ladder-is-cpa-cca`. Displacement levels none, `x` non-adaptive and `x` adaptive correspond to passive, chosen-plaintext and chosen-ciphertext access, so an access level times a criterion replaces per-attack definitions. Same report.
- `no-r-parameterized-training-time-definition`. Every `R`-parameterized definition held covers the test-time family, and the two training-time definitions held (CHLX25 defendability, GKVZ22 undetectable backdoors) are fixed games. Recorded as the next thing to check, not as a claim. Same report, What this changes.
- `four-criteria-read-off-reference-problems`. R1 (reconstruction from a noisy mean, Gaussian location estimation), R2 (membership as the zero-tolerance limit, two-point testing, degenerate baseline), R3 (backdoor criterion, rare-disagreement search, the detector searches) and R4 (fidelity, learning from a labeling oracle) show that the parameters of `R` are the reference problem's parameters with no mapping step. Derivation. R3 is a candidate never checked against CHLX25. Exhaustiveness not shown. `exp/docs/reports/2026-08-05-unfiled-concrete-r-criteria.md`.
- `technique-attack-twins`. Distillation and extraction, transfer learning and property inference, influence functions and membership inference, unlearning verification and forging share access level, criterion, algorithm and sample complexity, and differ only in authorization. Derivation. Same report.
- `eta-dial`. A coarse `η` describes a population with no hardness, a tight `η` inverts a lossy map, and the crossing is one scalar. Derivation. Same report.
- `r-as-quantizer`. `R` quantizes, carries the parameters, fixes the baseline, selects the problem, and is one object. Ontological definition. `exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md`. Its novelty was withdrawn the same day, see section 4.9.
- `pancake-property-inference-reduction`. Property inference against a model trained on Gaussian pancakes carries into distinguishing pancakes from `N(0, I_d)`, with `η`, the spacing `γ` and the budgets unchanged. A trichotomy follows for the defender (accurate means a lattice break, failing means uselessness, the practical case is accurate without exact recovery). Construction and chain of implications, not a proof. The projection-and-test tolerance and the search-to-decision direction are unchecked, and the third case is open. Corrected to an illustration of tightness only, because the planted source voids the guardrail. Same report.
- `security-profile-curve`. The object to prove is the largest `η` an efficient adversary reaches against a model of test error at most `ε`, as a function of `ε`. Open. Same report.
- `phi-one-function`. One function `Φ(P, 𝒜, b)` answers the PI's two requested functions, with the searching party as an argument and the security margin `Φ_comp(b) − Φ_IT` in the units of `θ`. Proposed. Monotone `{R_θ}` must be stated as a condition. The unification claim was withdrawn the same day (Clarkson and Schneider, CSF 2010). The relation to g-leakage was unresolved, with two expected differences (a threshold scanned over a family, an adversary class at a budget). `exp/docs/reports/2026-08-05-unfiled-leakage-and-integrity-functions.md`.
- `r-selects-the-problem`. Over one natural sparse Gaussian regression source, a fixed defender and a fixed release, five choices of `R` reach five problems with five thresholds. The selection claim is recorded as established. The reduction from a released network to samples is open. Novelty not checked. `exp/docs/reports/2026-08-05-unfiled-natural-source-r-selects-the-problem.md`.
- `sparse-support-case-study`. The case study's own table (§15) records the setting as natural (established), the five problems (established), the non-degenerate random-subset baseline (established), the stat-comp gap for support recovery (assumed on three bodies of evidence, none unconditional), the budget stated in samples (a modelling decision), step 5, reducing support recovery from a trained network to recovery from samples (open), and novelty (unchecked). Numbered thresholds carry `[verify]` flags. `exp/docs/notes/case-study-sparse-support-recovery.md` §15, with the first next step, a ridge release, in §16.
- `four-generator-axes`. The PI's matrix is a projection of four axes, phase of action, phase of measurement, asset (`D`, `L`, `f`, `f(x)`) and goal (confidentiality, integrity, availability). Backdoors have no single cell, availability and `f(x)` are missing from the PI's matrix. The headline says one cell is structurally empty while the table marks two, integrity at test time against `D` and against `L`. `exp/survey/lib/reports/archive/2026-08-05-halil-lit-survey-structure.md`.
- `no-adversary-class-axis`. Across about thirty taxonomies none has an adversary-class axis, every knowledge or access axis is an interface ladder, and privacy and integrity are disjoint by construction. Literature finding, verified across the sweep. `exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md`.

### 3.2 Working notes, `exp/docs/notes/`

- `computational-footing-thesis`. Security claims about learning should move from statistical to computational footing, with the target called the Goldwasser theorem of AI and the summary that security is learning lower bounds. Thesis. `exp/docs/notes/intro-computational-security-of-learning.md` §0 to §2.
- `comp-mem-game`. Computational membership indistinguishability is the on-ramp game. Membership is the floor of confidentiality and gives nothing about integrity, so integrity needs a separate EUF-CMA analogue. Proposed. Its marginal-advantage form is a refuted no-op, see section 4.1. Same note §4.
- `comp-tw-game`. Training-world indistinguishability over worlds differing by a controlled `Δ` (one example, a backdoor insertion, a poisoned batch), with `COMP-MEM` as its smallest point. Proposed. Same note §4.
- `crown-jewel-threshold`. Past a threshold, learning reduces to breaking a one-way function, and below it hardness is statistical. Target, open. Same note §3.
- `secure-all-ppt-first`. Secure against all PPT first, paying with an OWF assumption, and treat the learning-shaped adversary as Phase 2, because SQ hardness is unconditional and restricted (parity is SQ-hard and solved by Gaussian elimination). Decision. Same note §5.
- `fiber-navigability`. Security is the infeasibility of navigating the fiber given side information, the OLS fiber is huge, affine and navigable, and white-box access is more dangerous than black-box as a containment of fibers. Framing. Refuted at its core on 2026-07-26 (Dinur and Nissim, PODS 2003), and that refutation was flagged for re-examination on 2026-08-22. The OLS example is the note's own. `exp/docs/notes/fibers-of-the-training-map.md`, root `CLAUDE.md` negative results.
- `advantage-type-decides-the-game`. A bit-valued success functional makes baseline subtraction a no-op, a real-valued one makes it meaningful, so `COMP-TW` works for reconstruction and property inference and fails for membership. Proposed 2026-07-26. `exp/docs/notes/game-family-and-reduction-targets.md` §1.
- `games-g1-to-g5`. G1 inference-time data inference (feature map), G2 training inference from gradients (feature map at fixed `θ`), G3 membership (training map, raw advantage), G4 reconstruction from weights (training map, no calibrated target), G5 property inference (training map, spiked models). G2 linear is an affine condition plus a box, hence a lattice or hidden subset sum problem. Proposed. Same note §3 and §4.
- `suliman-conjecture-false-when-noiseless`. In the noiseless G2-linear cell LLL should win, so the Suliman et al. conjecture is probably false for exact gradient matching and true only once noise, quantization or step compounding enters. Prediction, open, the first experiment named. Same note §4 and §5.
- `ideas-games-not-taxonomies`. Halil's own note asks for adversary games instead of attack taxonomies, criticizes input-distance budgets, and conjectures a learning adversary bounded by learnability. Informal. `exp/docs/notes/ideas.md`.

### 3.3 Chapter 24, `exp/docs/notes/chapter-24.md`

Thirty-two messages in three phases. Mursit never ticked the prose consent box. Line numbers are approximate.

- `abstract-machine`. A learning system is a source `Π` on a uniform seed, a learner `L` with metered source access, and advice `w` run by `U`. Linear regression and an LLM are one machine at two `(|w|, t_eval)` coordinates. Definition. Message 1, capstone in message 21.
- `demote-the-distribution`. Principle (3). No primitive names a distribution. Methodological law. Message 1.
- `one-surface-two-frontiers`. One functional `Risk*` gives accuracy, detection, security and privacy as its corners, and a security theorem is a learning lower bound for the attack task under the adversary's handles. Definition and thesis. Messages 1, 7, 21.
- `learn-kappa-class`. `LEARN_κ[s, t, |w|, ε]` with reductions between source families as the native operation. Definition. Message 1.
- `positioning-law`. Statistical learning is `LEARN_κ / ~_D`, and a comp-stat gap is a fiber of that quotient. Stated as a quotient. Message 5, about line 996.
- `staircase-provability-gradient`. Below `τ_stat` security is unconditional (SQ floor), the recovery band is OWF-equivalent, the detection band is open (Gap-`K^t`). Phase 3 added an idealized-model rung (GLM, ROM, GGM) between the SQ floor and OWF, carrying the Canetti, Goldreich and Halevi caveat. Agreed in the dialogue. Message 5 (about line 980), messages 31 and 32.
- `keystone-universal-equals-generalizing`. The `Kt(w)`-minimizing learner is both universal (Levin search) and generalizing (Occam), one theorem under the hypothesis `I ≪ s`, through the bridge `Kt(w) ≲ Kt(L) + I + log t_train`. Recorded as proved in the dialogue. Messages 7 (about line 1340) and 8 (about line 1432), verdict in message 26.
- `capacity-is-kt`. Generalization is governed by `Kt(w)`, robustness lower bounds by raw `|w|`, so overparameterization is the regime `Kt(w) ≪ |w|`. Agreed. Message 7.
- `gen-gap-is-not-the-comp-stat-fiber`. The proposed identification of the generalization gap with the comp-stat fiber was blocked, since the first persists under unbounded computation and the second does not. Refuted proposal. Message 8, about line 1447.
- `privacy-is-the-master-modulus`. `Λ_compose ≤ Λ_priv`, so a private learner is automatically composable and generalizing and the converse fails, the complexity form of the DP to stability to generalization arrow of Dwork, Feldman, Hardt, Pitassi, Reingold and Roth. Accepted. Message 7.
- `h-l-shared-randomness`. `H_L` is a core resource, and one noise budget buys privacy on the training side and certified robustness on the deployment side. Accepted. Whether this survives an adaptive adversary (joint π) is open. Message 7.
- `interaction-principle`. Interaction buys power iff a cooperative unbounded party exists, never against a hiding adversary. Accepted. Message 7, about line 1323.
- `inference-aperture-incompressibility`. `|w| + R(t_eval) ≥ (1 − H(ε))·m − O(log m)`, where `R(t_eval)` counts bits recomputable within `t_eval`. For labels independent of queries it gives `|w| ≥ (1 − H(ε))m` for every `t_eval`, and it predicts the weights-to-context substitution. Sharp end recorded as unconditional. The smooth tradeoff for compressible natural tasks is open and plausibly as hard as a circuit lower bound. Message 23 (about line 3290), verdict message 26.
- `comp-stat-envelope`. `θ_comp ≤ Φ(θ_data)` on scaling exponents, derived from the keystone, so one point above it falsifies the keystone. Testable, unmeasured. Messages 24 to 27.
- `separation-discipline`. Keeping the statistical and computational axes apart forbids the field's standard false unifications. Methodology, evidence of faithfulness and not of new content. Message 26.
- `phase-2-verdict`. Chapter 24 is an organizing theory with one proved keystone, one open native conjecture, one keystone-derived testable prediction and a working forbidding principle. Message 26, line 3661.
- `supply-chain-undetectable-backdoor`. F-4. Under OWF, a Goldwasser-planted backdoor in an upstream model reaches a downstream composite with effect scaled by the product of inference sensitivities, and no bounded downstream auditor below `τ_recover` detects it. Theorem candidate. Message 15, line 2458.
- `provenance-over-detection`. F-5. Detection fails against white-box-undetectable constructions, and the working defence is attested provenance, the checker-verifier proof system pointed at the training transcript. Accepted. Messages 16 and 17.
- `backdoor-reproduction-number`. `R = Λ_train · Λ_C · Λ_eval^sup · ρ_hit`. `R < 1` heals geometrically, `R > 1` propagates, and a backdoor that both propagates and evades exists only in the window `1/(Λ_train·Λ_eval^sup) ≤ ρ_hit ≤ ρ_detect(δ, Φ)`, which is nonempty only in the detection band. Containment stated as a proposition. Messages 20 and 31.
- `steering-align`. `align = (I^← − b_poison)/(I^← + b_poison)` fixes the sign of the performative gap, and `R` fixes its persistence. Finalized. Message 20.
- `op1-robust-comp-stat-gap`. Whether the computational value of the robust-learning game is strictly below its statistical value, which is finite iff the robust-PAC dimension is finite (Montasser, Hanneke and Srebro 2019), reducing to average-case Gap-`K^t`. Open. Message 20, line 2993.
- `op2-trusted-prover-inherence`. Whether certifying `Clean_r` needs an unbounded prover outside the SQ-floor subclass, which would show backdoor-freedom is not self-certifiable. Open. Message 20, line 3003.
- `op3-composable-provenance`. Process provenance is an NP statement that composes by proof-carrying data, cleanness provenance is coNP and equals OP2. Proposed in message 17 (about line 2740), deflated into OP2 in messages 18 and 19.
- `aioracle-and-chapter-24-two-layers`. The AIOracle framework of Villa, Durak, Kohno, Maharramli and Roesner is the interface layer and Chapter 24 the foundation, joined at `φ ↔ (T, r_judge)`. Phase 3 verdict, unification. Messages 28 to 32.
- `three-term-composition-law`. A composed breach has an additive probability `ε`, an additive coverage mismatch `e` from the AIOracle side, and a multiplicative amplification `Λ`, so the additive AIOracle bound holds only when `Λ^sup ≤ 1`. Agreed. Messages 28 to 32, and `exp/docs/notes/LearningSystemsAsMachines_for_Practitioners.html` §9.
- `margin-gated-alignment-tax`. Internalizing a predicate raises boundary sensitivity only for small-margin predicates. Conjecture, called measurable. Messages 31 and 32.
- `intent-authorization-design-law`. Authorization conditioned on inferred intent costs `Kt(Π_intent)`, so an agent is intent-blind or intent-elicited. Prediction. Messages 31 and 32.
- `curation-controls-r`. The curation box `C` controls two of the four factors of `R`, so attesting the selection step is the strongest containment lever. Agreed. Messages 31 and 32.
- `glm-rung-is-heuristic`. The AIOracle MID bound `p_c ≤ 1/2 + n·ε`, proved inside a generic language model, is a heuristic guarantee by the CGH uninstantiability caveat. Recorded by lödeg. Message 32.
- `noiseless-leakage-metric`. `|w| − Kt(w)` as a computational leakage metric. Proposal. `exp/docs/notes/LearningSystemsAsMachines_for_Practitioners.html` §8.

### 3.4 Proof note, 2026-04-23

- `sq-hardness-black-box-attacks`. For a deterministic `(q_L, τ_L)`-SQ-implementable learner trained on the vertex-row encoding of a planted-clique graph, any black-box adversary's distinguishing advantage is at most the SQ distinguishing advantage at `(q_L, τ_L)`, whatever its own query count. The proof simulates the learner from SQ answers and answers the adversary's queries from the simulated model. Recorded with a full proof. Remarks specialize it to attribute inference, backdoor activation, membership and extraction, and treat randomized learners with public or private coins. Stated failures are non-SQ-implementable learners, other encodings and white-box adversaries. It does not handle per-round federated observation or LWE encodings. `.tools/proof.tex` (the PDF described in `exp/README.md` is not in the repository). It quotes FGRVX17 as Theorem 1.1 in the form `q·τ² ≥ Ω(n^{2δ})`, while the later, re-verified oracle draft quotes FGRVX17 Theorem 2.9 parameters.

### 3.5 Survey formalization, parked, `exp/survey/paper/parked/formalization/`

Dated 2026-08-22, reviewed adversarially through 2026-08-28, not part of the submission. Status of the return is open in `exp/survey/lib/issues/2026-09-17-halil-parity-experiment-unused.md`.

From `oracle.tex`, the learning oracle.

- `learning-oracle-accounting-device`. The oracle idealizes the training map and nothing else, returns the full trace, and manufactures no hardness. Every lower bound comes from what the views withhold, and every bound is on oracle steps, not time. Agreed framing. Sections 2, 5 and 8.
- `passive-oracle-and-named-recipes`. On a corpus the passive oracle draws fresh coins, runs a recipe the game names, and returns the trace. Two calls on one corpus return independent traces. Parties do not author recipes, which blocks a wrapping recipe that collapses the step count and a laundering recipe whose initialization emits precomputed weights. Definition. Defs Passive learning oracle and Metered cost.
- `fact-gradients-plus-initialization-determine-the-model`. For a gradient-factoring recipe, `w_T` is a function of `w_0` and the per-step quantities, so a view that grants both grants the model. Proven. Fact in Section Views.
- `recipe-noise-is-not-view-noise`. DP-SGD noise inside the recipe and channel noise inside a view are different objects. Definitional. Section Views.
- `interactive-oracle-and-ports`. Federated clients and the split-learning cut are ports, attaching a party gives it a read and a write, and the passive oracle is the unattached special case. Definitions, and the special-case fact is proven. Section interactive form.
- `two-budgets`. A read budget is what a party spends on the oracle, a write budget is what it may change, so poisoning fractions and malicious-client deviations are write budgets. Definition. Def Write budget.
- `game-skeleton-and-criteria`. A game names a recipe, attachments, views, budgets, a declaration, an optional secret with min-entropy `h`, a distinguish or produce criterion, and a baseline. Definitions. Membership, DP and undetectability are distinguish games, reconstruction, extraction and forgery are produce games, a backdoor game is both.
- `fact-worlds-must-differ`. If the two worlds induce the same view distribution, every advantage is zero. Proven.
- `view-generic-adversary`. Genericity is relative to granted views, an attack is classified by the weakest view it needs and the queries it spends there, and the generic against structural dichotomy is dropped. Definition.
- `prop-locating-a-real-attack`. If a deployed attack beats a proven floor, its access exceeded the granted views, its spend was understated, or some real procedure delivered a view below its modeled price, which for training means a broken transfer hypothesis. Proven, an audit.
- `prop-query-bounded-corpus-auditor`. In the backdoor game where the planter replaces the data distribution and the auditor sees the corpus through `VSTAT(m)`, FGRVX17 Theorem 2.9 prices detection, for planted bipartite `k`-clique with `k ≤ N^{1/2−δ}`. Proven by specialization, with four stated boundaries (the `VSTAT` to corpus correspondence is the model's reading, record-level auditors and model-level auditors are not covered, and no claim is made that a planter meets non-triviality).
- `backdoor-game-fixed-parts`. Three roles (planter with a write budget, auditor with a read budget, activator with a secret of min-entropy `h`), the planter is generic, the auditor detects rather than reconstructs and never holds the secret. Fixed. Section The backdoor game.
- Open in `oracle.tex`. Non-triviality of the backdoor game, where the planter writes, the model-level auditor, the content of a declaration and the no-known-shortcut line, and uninstantiability. Deferred are a criterion for generation and the classification case.

From `price.tex`.

- `price-of-aiming`. Within SQ recipes the floor is unconditional (`d^{Ω(k)}` queries for a hidden `k`-sparse parity). Reading a fresh-batch gradient step as a correlational query of tolerance about `B^{-1/2}` is a heuristic simulation that every gradient use of a floor must carry. The generative exponent is the surviving unit, and the information exponent and the leap are not used. Proven in the classes named, with the simulation heuristic.
- `price-of-skipping-is-recipe-relative`. Task-level no-skipping is refuted by recipe drift, recipe-level is the strongest defensible form, and no lower bound over all algorithms exists. Open, under every compute-pricing claim.
- `amortization-is-not-skipping` and `price-of-a-view-is-not-the-price-of-the-trace`. Distillation draws on a teacher's paid trace, and a sound proof-of-learning is a view whose price equals the trace's. Definitional in the model. Whether a sound proof-of-learning exists is open.
- `sparse-parity-experiment`. Two-layer ReLU of width 100, SGD with momentum 0.9, batch 128, learning rate 0.01, fresh samples, hidden 3-sparse parity, `d` in {20, 30, 40, 50, 60}, 8 seeds each, threshold 0.90 test accuracy. All 40 runs solved, median steps 1025 at `d = 20` and 9337.5 at `d = 60`, log-log slope 2.02 over a factor-three range with consecutive slopes 0.8 to 3.0. A probe with batch 8, width 512 and learning rate 0.1 had median 6940 at `d = 30`, and nine runs at `d ≥ 60` hit the 300000 cap. Empirical. Parked and unused. `exp/survey/lab/results/sparse-parity/manifest.yml`.

From `games.tex`, extraction games with a priced adversary.

- `prop-probe-collapses`. With an adversary-chosen probe near a queried point and `Lδ ≤ ε`, one query wins with probability 1. Proven.
- `extraction-advantage`. The baseline maximizes over model-free algorithms given the model family and the challenge set, so no baseline can hardwire `f`. Definition.
- `prop-raw-success-is-not-a-measurement`. A model-free baseline can beat a published attack. Empirical, established for membership inference only (Das, Zhang and Tramèr, Meeus et al.).
- `prop-unseparated-challenges-collapse`. Challenges inside a known ball of radius `ρ` with `Lρ ≤ ε` are won by one query. Proven. Repairs are `Δ`-separated and `h`-unpredictable challenge distributions, both required. Definitions.
- `prop-search-implies-decision`. A search adversary with success `p` yields a distinguisher with advantage `|p − q|/2`. Proven. The polynomial-time converse is open.
- `delta-extraction-hardness`. Every adversary with cost below `k(n)^{1+δ}` evaluations has negligible extraction advantage. Definition, in the first fine-grained convention, with three cautions.
- `prop-stealing-implies-answering`. Winning `Steal_ρ` under the supremum distance on the challenge support wins the challenge game. Proven. The converse needs a covering condition, open.
- `challenge-generator-as-oracle`. The adaptive challenge generator is an auxiliary AIOracle whose cost must sit in the honest budget. Proposal.
- Open in `games.tex`, in blocking order. The polynomial-time converse of search to decision, the covering condition, a read-out map invariant under ReLU symmetries, an instance at an explicit `δ` reduced to average-case `k`-SUM or Zero-`k`-Clique, a separation against the Jagielski et al. SQ bound, and the classification case.

### 3.6 AI oracle thread, 2026-10-13

- `version-space-oracle-advantage`. With `h ~ Unif(V(S))` and an adversary who knows the other `n − 1` points, the Bayes-optimal adversary depends on `h` only through `h(x_0)` and `h(x_1)`, and its advantage is `1 − min(r_0, r_1)`, where `r_i` is the probability that a model trained with `z_i` labels the other challenge correctly. Proven. Consequences recorded are that utility sets leakage, that two black-box queries reach the white-box optimum, and that computation enters only through a counting step (comparing `|V_0|` and `|V_1|`) whose hardness for natural classes is open, with hardness for rich classes a heuristic expectation. The oracle is the zero-temperature case of SDSOJ19, proven, elementary. `exp/survey/lib/reports/src/2026-10-13-halil-version-space-oracle.tex`, PDF in `exp/survey/lib/reports/`.
- `generic-training-oracle`. A generic-group-style oracle keeps handles to parameter vectors and offers `train(S)`, `eval`, `grad_x`, `grad_θ` and `reveal`, an access class is a set of operations with budgets, black-box is `{eval}`, shadow models add `train`, white-box is `{reveal}`, and the challenger plays a membership game on a handle. Definition, with a utility condition `α`. `exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex`.
- `ideal-representation-equalizes-white-box`. Under ideal representation the best unbounded white-box advantage equals the best unbounded advantage of an attacker that sees only the function, by data processing on total variation. Proven. Same report.
- `representation-leakage-and-extraction-cost`. Real training breaks ideal representation, and the gap splits into an information part and a computational part. Definition. Same report.
- `ideal-representation-is-uninstantiable`. An oracle with ideal representation is a virtual black-box obfuscator for trained functions, impossible in general by BGIRSVY01, so the model has random-oracle standing. Heuristic analogy. Same report.
- `unlimited-queries-return-the-function`. Parameters that affect no output give a white-box attacker information an unbounded black-box attacker never sees. Proven by a trivial construction. `exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`.
- `achievable-leakage-bb-equals-wb-when-unbounded`. A learner can output a canonical description of its function, so the black-box against white-box question free of learner choices is an obfuscation question for learners. Proven trivially. Same issue.
- `learner-choice-fixes-the-answer`. An arbitrary learner lets white-box win trivially, an idealized learner (Gibbs, version space) gives no gap, and for SGD on deep networks any gap is only empirical. Recorded diagnosis. Same issue.
- `interface-does-not-bound-leakage`. A training oracle that bounds leakage must fix the distribution of the returned function, and any such oracle makes white-box equal black-box. Recorded tension. Gibbs at temperature `T` with loss in `[0, 1]` is recorded as the exponential mechanism with `ε = 2/T`. Same issue.
- `gradient-attackers-are-first-order`. Gradient-based attackers are attackers with a first-order oracle. Heuristic as a reading of the attack literature. Same issue.
- `field-coding-2026-10-13`. Over 190 relevant works coded by five agents, 40 study concrete deep networks, 36 quantify over all learners, 30 assume DP, one assumes a Gibbs posterior, none a version space, seven treat training as an opaque call, gradient access is a formal object in four, calls to training appear in ten, no attacker is a formal first-order class, attackers are unbounded (58), PPT (52) or one fixed algorithm (33), and 47 of the 92 core works state no utility condition. Empirical on the coding, not on the papers. `exp/survey/lib/literature/ontology/views.md`, same issue.

### 3.7 Survey results, empirical on the coded corpus

From `exp/survey/lib/claims.yml`, numbers in `exp/survey/lib/numbers.csv`.

- `classification-of-two-hundred-works`. 200 formal works coded by party, unit and tightness. Supported.
- `evidence-layer-per-row`. Each row carries its deciding sentence or the places checked for an absence, and 155 of 172 quotations were bound inside their own document at round two. Supported.
- `resource-axis-absent-from-prior-systematizations`. No prior systematization records the resource a work bounds or the party it binds. Novelty claim, supported.
- `most-formal-works-price-nobody`. 37 of 200 bound no party. Supported.
- `attack-works-price-nobody-more-often`. Attack works bound nobody more often than cryptography and learning-theory works, in direction and not in size. Narrowed. On the theorem-bearing subset (12 of 71 against 6 of 87) the interval is −0.2 to 20.2 and includes zero (`margin-direction-only`, limitation).
- `two-party-bounds-rare-in-attack-papers`. 18 of 200 state a relative bound, 6 of them attack works. Supported, recounted from 11 and 3 on 2026-09-03.
- `attack-bounds-limit-change-not-spend`. 36 of 103 attack works state a numeric allowance such as a radius. Supported.
- `field-shares-access-vocabulary`. 72 of 103 attack works name an access level from one list of six. Supported.
- `near-miss-works-hold-unnamed-adversary-price`. 19 works hold a resource quantity their framing does not carry, 9 of them an adversary's or auditor's cost, 5 a training cost, 5 a capability or mechanism parameter. Supported.
- `no-memory-bounded-adversary-attacks-a-model`. Four works bound an adversary in memory, all bounded-storage cryptography. Novelty claim, supported.
- `baselines-absent-in-attack-papers`. Of 50 attack works that define success, 29 name a baseline. Supported.
- `membership-inference-verdicts-disagree`, `attacker-to-honest-ratio-defined-twice`, `threat-models-without-a-resource-bound`, `field-rejects-attacker-compute-as-a-parameter`. Supported, see section 4.
- `corpus-is-a-working-bibliography`, `single-coder-agreement-unmeasured` (24 of 27 on an overlap). Limitations.
- `geometry-cluster-prices-nobody`. Of 18 concentration and robust-PAC papers, eleven constrain nobody or only the learner in samples, three price an adversary, and Diakonikolas et al. make the defender the polynomial-time party. Audit finding, 2026-08-22. `exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md` §4.
- `agentic-and-certified-cluster-has-no-bounded-adversary`. Across 16 papers every bound is a radius, a poisoned-sample count or an interface restriction, two state an unbounded adversary, five have no theorem. Audit finding, same §4.
- `implicit-quantity-register`. Security claims are existential theorems about constructed objects restated as universal claims, and the quantity that would make them measurable sits inside the proof as a side condition. Three audits, three failures. `exp/survey/lib/reports/archive/2026-08-20-halil-lit-survey-spine.md`.

## 4. Settled facts about prior work

Each entry gives the claim, the paper and venue, the verdict, the date, the correction history where there is one, and the path. Root means the root `CLAUDE.md`, section Established negative results. Audit means `exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md`. Sweep means `exp/survey/lab/results/literature-sweep/`, whose sheets are agent readings dated 2026-10-13, and a paper seen only there is cited nowhere until a note exists.

### 4.1 Membership inference and privacy definitions

- The marginal-advantage-over-baseline form of membership advantage is a no-op, since the baseline is one half by construction, and it is already published. Yeom, Giacomelli, Fredrikson and Jha, CSF 2018, Definition 4 and Experiment 1, where the paper proves the two posteriors equal. Holds. Corrected 2026-08-22 from Definition 6, which is the alternative attribute advantage, whose baseline is the Bayes-optimal simulator, which is not degenerate and which the authors reject for rewarding accuracy. Also cited for the same point are Xiao and Devadas, PAC Membership Privacy, CRYPTO 2023, and Desfontaines and Pejó, PoPETs 2020, dimension R. Root, audit §2.
- An attacker can need many more samples than the trainer. Haghifam, Smith and Ullman, arXiv 2508.19458, `m ≳ n²ρ² + n` for membership inference against Gaussian mean estimation, information-theoretic units, unbounded adversary. Verified in full 2026-08-22, holds. Three boundaries travel with it, the antecedent `d > c₁(n + n²ρ²)`, a success tolerance of 0.02 (TPR at least 0.51, FPR at most 0.49), and the separation vanishing when the attacker knows the covariance (Theorem 1.2, `min{n, 1/ρ²} ≤ n`), so it prices ignorance of `Σ`. The Ingster and Suslina chi-squared technique is one step from a low-degree restatement, a competitive hazard. The 2026-10-13 sweep records arXiv v2 of 8 October 2026 as to appear at FOCS 2026, and records that a separation for a single mechanism is open per the authors. Root, audit §2, sweep `information.md` sheet HSU25.
- Under a Gibbs-posterior model of training the Bayes-optimal membership attack reads the weights only through the loss (Theorem 2), and ε-DP bounds the membership posterior by `λ + ε/4` (Property 1). Sablayrolles, Douze, Schmid, Ollivier and Jégou, ICML 2019. Read in the PDF, 2026-10-13. Sweep `information.md` sheet SDSOJ19, and `exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`.
- Blind attacks with no model access beat state-of-the-art membership attacks on eight published benchmarks. Das, Zhang and Tramèr, DATA-FM workshop at ICLR 2025. Quotation verified 2026-09-03. Meeus et al., SaTML 2025, locate the carrier as a distribution shift between benchmark halves, with years as the most predictive bag-of-words features on WikiMIA. `exp/survey/lib/reports/archive/2026-09-03-halil-quotes-batch-a.md`, `exp/survey/paper/sections/02-problem.tex`.
- Bounding a false positive rate requires sampling the hypothesis that the model was trained without the record, which would require training new large models, so the claim is unfalsifiable against a party who cannot afford a training run. Zhang et al. (ZDKT25), IEEE SaTML 2025. Venue corrected from preprint on 2026-09-03. `exp/survey/paper/sections/02-problem.tex`, `exp/survey/lib/reports/archive/2026-09-03-halil-review-survey-round-2.md`.
- Carlini et al., Membership Inference Attacks From First Principles, IEEE S&P 2022, prices its attack in shadow-model training runs (N = 64 for ImageNet, 256 otherwise). The codebook has no training-runs unit, so the row is coded `time` and a dispute is recorded. 2026-09-03. `exp/survey/lib/reports/archive/2026-09-03-halil-quotes-batch-b.md`.
- Reconstruction robustness quantifies over any reconstruction map with tolerance `η`, success bound `γ` and an oblivious baseline `κ_{π,ℓ}(η)`, and carries no computational bound. Balle, Cherubin and Hayes, IEEE S&P 2022, Definition 2. Verified verbatim 2026-08-05 and again in the 2026-08-22 audit. `exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`, audit §4.

### 4.2 Low-degree and statistical-query adversaries

- The claim that no security definition quantifies over SQ or low-degree adversaries was retracted on 2026-07-25 as false, citing Bogdanov, Jones, Rosen and Zadik, TCC 2024 (arXiv 2409.16227), and Abram, Beimel, Ishai, Kushilevitz and Narayanan, TCC 2023. The retraction was corrected as too broad on 2026-08-22. BJRZ Propositions 4.1 and 4.3 quantify over `(s, ε)`-indistinguishability, meaning size-bounded circuits, and the proof of 4.1 builds an explicit circuit. Its Conjectures 1.3 and 1.4 are stated in polynomial time with low-degree lower bounds offered as evidence. ABIKN does the same. No security definition in either paper quantifies over a low-degree adversary. The authors also note planted clique and planted subgraph technically miss the noise-robust assumption of the low-degree conjecture. Root, audit §2.
- Ngo and Kim, arXiv 2607.15528, was recorded as SQ-quantified soundness and retracted on 2026-08-20 against the PDF. Its Definition 1, Universal Soundness, quantifies over an unrestricted cheating prover, and the SQ restriction sits on the certified algorithm and the verifier's query budget. It is a query-bounded verifier result. Root.
- Buhai, Hsieh, Jain and Kothari, FOCS 2025 (arXiv 2505.17360), disprove the quasi-polynomial low-degree conjecture in the regime it was stated, so low-degree-bounded and quasi-polynomial-bounded adversaries are provably different. Recorded 2026-08-20. The polynomial-time distinguisher is for the rectangular generalisation, in the square `S_n`-symmetric regime it runs in `n^{O(log^{1/(k−1)} n)}`, and closing that is open. The largest-eigenvalue construction has a non-product null and refutes nothing. Root, `games.tex` Section Where to reduce.
- The positive counterpart is Hsieh, Kane, Kothari, Li, Mohanty and Tiegel, STOC 2026 (arXiv 2601.05850). Corrected 2026-08-20. What is universal across its three results is the noisy version of the problem. Theorem 1.2 assumes only a distribution over `R^n`, Theorems 1.1 and 1.3 assume permutation invariance, and none rules out all polynomial-time algorithms. Any security claim resting on a low-degree adversary must cite both papers with these clauses. Root.
- Bubeck, Price and Razenshteyn, ICML 2019, is a security-relevant SQ separation in which the defender fails. Root. The audit of 2026-08-22 records that the paper uses no cryptographic assumption, with the bound unconditional in the SQ model, and that the wiki had inverted the BPR and BLPR relation, the assumption being quadratic residuosity through Blum, Blum and Shub. Its venue was confirmed as ICML 2019 on 2026-09-03 after a mined arXiv lead proved to be a coincidental string match. Audit §3, `exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md`.
- The Holmgren and Wein counterexamples to the low-degree conjecture use efficiently decodable error-correcting codes, and "parity" occurs zero times. Hirahara and Shimizu, STOC 2024, place refutation in a separate equivalence with average-case `k`-clique on `G(n, 1/2)`. Both corrected 2026-08-22. Audit §3.
- Noise is load-bearing. Lattice methods solve noiseless hCLWE, planted hypercube, planted sparse vector and parity while SQ, SoS and low-degree bounds stay formally true (ZSWB22). Not every planted problem has a gap (group testing). Worst-case ERM hardness of Blum and Rivest is the wrong substrate. Entries dated 2025 to 2026 marked with a dagger are single-sourced. Cautionary shelf, 2026-07-10. `exp/literature/related-work.md` §7.

### 4.3 Computational differential privacy

- Groce, Katz and Yerukhimovich do not say what the folk version says. Checked 2026-08-20 against the PDF. The impossibility covers black-box constructions and queries with output in `R^n` for constant `n` under natural utility measures. The authors exclude queries that return classifiers, graphs or synthetic databases, `n` growing with the security parameter, utilities with no polynomial error bound, and multiple queries beyond a constant number or a stateless server. Released models are the excluded case. Root.
- Meisingseth and Rechberger show the GKY utility barrier needs `ε ∈ O(log κ)`, a condition the original did not identify. Recorded 2026-08-22. Audit §4.
- The single-curator separation is no longer fully open. Bun, Chen and Vadhan, TCC 2016-B, separate infeasibly. Ghazi, Ilango, Kamath, Kumar and Manurangsi, FOCS 2023 (arXiv 2301.00104), separate against unbounded SDP mechanisms under NIWI, laconic keyless CRHF and diO, the separation breaks against quasi-polynomial adversaries, and the task is contrived. A separation on a natural task remains open. The paper supplies a reusable template, prove privacy against a decision-tree adversary class and lift with cryptography. Recorded 2026-08-20. Root.

### 4.4 Learning-theory exponents

- The generative leap exponent is the unit. Damian, Lee and Bruna, arXiv 2506.05500, `n = Θ(d^{1∨k*/2})` for Gaussian multi-index models, with a low-degree lower bound and a matching efficient upper bound. Found 2026-08-20. It dominates the information exponent (Ben Arous, Gheissari and Jagannath, JMLR 2021) and the leap (Abbe, Boix-Adserà and Misiakiewicz, COLT 2023, whose matching bound is CSQ only, whose `Θ̃(d^{max(Leap,2)})` is a conjecture, and whose proved Gaussian CSQ bound is `d^{Leap/2}`). `games.tex` adds that the constant `C(P, K)` is conjectured exponentially large in the index dimension. Root.
- The single-index threshold is a detection threshold. Damian, Pillaud-Vivien, Lee and Bruna, Remark 3.3, state that Theorem 3.2 primarily measures detection, flag a known gap where SQ estimation needs `n ≳ d^{k*/2+1}`, and leave the estimation threshold open. The low-degree half is conditional on their Conjecture 3.4. An attacker who must recover a value is doing estimation. For polynomial links and for deep networks with an `r`-dimensional first hidden layer `k* ≤ 2`. Recorded 2026-08-20. Root.
- Superseded in part on 2026-08-27. Arnaboldi, Ostrovskii, Sun and Wu, arXiv 2406.01581 (NeurIPS 2024), carry weak recovery to strong recovery with a generalization bound at `n = Θ̃(d^{(p*−1) ∨ 1})`, governed by the generative exponent, and Glasgow, arXiv 2309.15111 (ICLR 2024), reaches `o(1)` error on XOR in `Θ̃(d)`. Batch reuse attains the generative exponent in place of the information exponent, because two steps on one minibatch pass the label through the activation's derivative, and the learning rate selects the regime (TME25). The earlier record that Dandi et al., ICML 2024 (arXiv 2402.03220), escape the barriers is too strong. Root, `price.tex` Section The price of aiming.
- The `price.tex` record of 2026-08-28 adds that the information exponent prices one algorithm (online SGD from random start), that reuse reaches the information-theoretic rate for polynomial links (LOSW24), that a learning-rate schedule induces the same transition (TME25), and that full-batch descent separates from one-pass descent by a logarithmic factor for a truncated target and provably not for the plain one (KJWSM26). Proven in the classes named. `exp/survey/paper/parked/formalization/price.tex`.
- The exponent cell has zero security citers. Re-verified adversarially on 2026-08-20. 514 citation records across the five exponent papers, zero hits in S&P, USENIX Security, CCS, NDSS, CRYPTO, EUROCRYPT, TCC and PoPETs, 259 unique arXiv citers with exactly one in cs.CR (arXiv 2310.01959, one passing sentence), zero IACR ePrint hits. Root.

### 4.5 Reconstruction, fibers and forging

- Size against navigability with a complexity separation is Dinur and Nissim, PODS 2003, which refuted the fiber framing on 2026-07-26. Three clauses of the earlier note were corrected on 2026-08-22 against the PDF. The headings are §3.1 Exponential Adversary and §3.2 Polynomially Bounded Adversary, siblings inside §3. The main result is a polynomial reconstruction algorithm from noisy subset sums, with §3.1 a warm-up. The OLS example is not theirs, since the words OLS, least squares and regression occur zero times and the attack is a linear program with rounding at 1/2. The bounds stand, `E = o(n)` fatal against an `exp(n)` adversary, `o(√n)` against `poly(n)`, `Õ(√T(n))` sufficient against time `T(n)`. The audit adds that the fiber refutation may need re-examining. Kaplan, Mansour, Nissim and Stemmer, arXiv 2505.23658 (ITCS 2026), restate the separation as computational against statistical memorization. Root, audit §2 and §5.
- A computational security notion for reconstruction exists and is equivalent to one-wayness. Cohen, Kaplan, Mansour, Moran, Nissim, Stemmer and Tsfadia, ITCS 2025 (arXiv 2405.15753), Definition C.1. Corrected 2026-08-22 on its antecedent. The equivalence is Theorem C.5 and needs `f` efficiently computable and well-spread (Definition C.4). Narcissus resiliency does not compose in general (Appendix D). Root, audit §2.
- Training-map identifiability against optimization is studied by Shen et al., arXiv 2602.08723. Root.
- Suliman et al., arXiv 2411.05658, recorded in the game-family note as USENIX Security 2025, is titled Towards a Re-evaluation of Data Forging Attacks in Practice. Its result is empirical, published forging attacks miss the reproduction-error threshold by orders of magnitude and are detectable. The fiber-navigation conjecture is real, incidental, and names no adversary class, reference problem or assumption, and the paper says nothing about the evaluation against training map distinction. Corrected 2026-08-22. Jagielski et al., USENIX Security 2020, prove NP-hardness for the evaluation map only. CDP or SDP applied to reconstruction from weights is open, verified negative across the line from Beimel, Nissim and Omri to Ghazi et al. FOCS 2023. Root, audit §2.
- Xiao, Suh and Devadas, CCS 2024, correct title Learnable Obfuscation, prove in Theorem 1 an IND-CPA impossibility about the encoding `T`, not about a training map. One-way function appears nowhere, the adversary chooses the challenge distributions and its concept class, and the authors name two escapes (restrict plaintext choice, deny the model trained on encoded data). Checked 2026-08-22. Root.
- A proof-of-learning spoof (Jia et al., IEEE S&P 2021) is fiber navigation priced in compute. Forging and unlearning are Thudi et al., USENIX Security 2022, and Kong et al., arXiv 2303.03648. Root.
- The gradient-inversion work LAMP defines no success criterion, reports ROUGE with no threshold and no gradient-free control, and prices cost in GPU-hours. 2026-08-22. Audit §4.
- Schmidt et al., NeurIPS 2018, show an information-theoretic `√d` gap only "already in a simple natural data model", a qualifier the wiki deleted, and the paper itself shows the gap holds for linear classifiers while a slightly nonlinear thresholding classifier recovers the smaller sample complexity. 2026-08-22. Audit §3.

### 4.6 Fine-grained cryptography and the ratio between parties

- Compute amount rather than hardness is fine-grained cryptography. Checked 2026-07-26. Brzuska and Couteau, EUROCRYPT 2022 and J. Cryptology 2024, Definition 6 (`(ε, δ)`-fine-grained OWF against circuits below `|f|^{1+δ}`), LaVigne, Lincoln and Vassilevska Williams, CRYPTO 2019, Definition 5 (the gap as a named object), Ball, Rosen, Sabin and Vasudevan, STOC 2017, Definition 2. Write it as an exponent. Root.
- The ceiling of Barak and Mahmoody, CRYPTO 2009, is a query bound in the random oracle model, an Eve making `(16n/δ)²` oracle queries that runs efficiently only in a relativized world where P equals NP. It forbids a super-quadratic query gap and says nothing about time gaps or structured assumptions. Afshar et al., EUROCRYPT 2023, cap 3-NIKE at `O(n²)` in Maurer's GGM. Barriers are BRSV §5.2 (NSETH) and Alman, Huang and Yeo, EUROCRYPT 2025. The 2026-08-22 audit lists the earlier record that quadratic is optimal in the ROM as the agent's own error. Root, audit §2.
- There are three incompatible conventions. BC22 uses non-uniform circuit size and `honest^{1+δ}`, LLW19 uses uniform word-RAM time with `T^{1−δ}` against `T`, and BRSV17 uses uniform word-RAM with the error indexed by the adversary's own discount as well as by `n`, so BRSV17 Definition 2 is not one number. 2026-08-22. Audit §4, `games.tex` Section Pricing the two parties.
- Proof-of-learning states `E[C_A] ≥ E[C_T]` (Property 2, Definition 2) as a bare inequality, never parameterized by `δ`, offered as a conjecture, and the paper cites neither BRSV nor LLW. Property 1 is a different inequality, verification against training. Later work indexes the ratio by a multiplicative constant (Fang et al., ZFWCSXZ26) and by efficiency and hardness parameters (Shavit, Sha23), and no work by an exponent. No ratio-parameterized privacy notion exists. Model extraction has no formal success definition, stated from inside by arXiv 2310.01959. Root (two seams, 2026-07-26), `games.tex` Section What is already occupied.
- BC22 is EUROCRYPT 2022 Part II, LLW19 is CRYPTO 2019 Part III, TCBM20 is NeurIPS 2020, and Carlini et al., On Evaluating Adversarial Robustness, is a preprint never published. Resolved from bibliographies inside the corpus, 2026-08-22. `exp/survey/lib/profs/2026-08-22-halil.md`.
- LaVigne, Lincoln and Vassilevska Williams Definition 5 is a two-party relation and should be coded `relative`. Dispute recorded 2026-09-03, not applied. `exp/survey/lib/reports/archive/2026-09-03-halil-quotes-batch-b.md`.

### 4.7 Memory-bounded adversaries

- Memory-bounded-adversary cryptography is mature, Raz, FOCS 2016, then Guan and Zhandry, EUROCRYPT 2019, then Dodis, Quach and Wichs, EUROCRYPT 2022 and 2023. Root.
- No security or privacy definition bounds an ML or privacy adversary by memory. Every hit bounds the learner (Raz FOCS 2016), the mechanism (Dinur, Stemmer, Woodruff and Zhou, EUROCRYPT 2023) or the defender (Kaplan, Mansour, Nissim and Stemmer, CRYPTO 2021). Recorded as an open slot. The survey count of September 2026 finds four memory-bounded adversaries, all bounded-storage cryptography. The 2026-10-13 sweep did not search this, so it claims no new negative. Root, `exp/survey/lib/claims.yml`, sweep `information.md` §4.
- Transformer against RNN learning separations exist (arXiv 2503.11272), and only the memory-sample mechanism is unclaimed. Root.

### 4.8 Restricted-class attackers and the closest prior art

- The attacker as a restricted-class learner is occupied in cryptographic units by Canetti and Karchmer, TCC 2021, Karchmer, SaTML 2023, Christiano, Hilton, Lecomte and Xu, arXiv 2409.03077, and arXiv 2504.20310. Only the learning-theory units are unclaimed. Root.
- Capacity-bounded DP is the near-collision with the Phase-2 idea. Chaudhuri, Imola and Machanavajjhala, NeurIPS 2019 (arXiv 1907.02159), Definition 3, `(H, Γ)`-capacity bounded privacy with the adversary in a restricted function class (linear, RKHS, two-layer ReLU). Uncited by the quantitative information flow and maximal-leakage lineages. Recorded 2026-07-26 and 2026-08-05. Root, `exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`.
- Model extraction priced by algorithm class exists in a security paper. Jagielski et al. (JCBKP20, USENIX Security 2020) state as Theorem 3, imported from Das et al., that SQ-expressible extraction needs `exp(O(h))` samples for fidelity extraction of depth-`h` random networks, and note gradient descent and PCA are such algorithms. Any novelty claim must be stated against it. 2026-08-22. `games.tex` Section What is already occupied.
- The question is still open only narrowly. Attacker and defender priced in the same exponent units, separated at matched budget, with the attacker restricted to training's own algorithm class. Song, arXiv 2404.03272, §1.3 item 2, names discriminators with bounded compute or memory as open, verbatim and confirmed. The same item notes that a sampler asked only to fool bounded testers could output standard Gaussian samples, so the lattice gate is on `L²`-accurate score estimation and not on sampling. Corrected 2026-08-22, §1.3 is a three-item list titled Future directions with no subsections, and item 3's black-box impossibility is Bruna, Regev, Song and Tang's result restated, conditional on worst-case lattice hardness. Root, audit §2.

### 4.9 The criterion `R` and the privacy and integrity unification

Two sweeps on 2026-08-05, thirty-four searches, twenty-eight primary sources text-extracted. `exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md` unless noted.

- `R` with a `{0,1}` codomain is a binary gain function. Alvim, Chatzikokolakis, Palamidessi and Smith, IEEE CSF 2012, Definition 3.6, a named subfamily with a structure theorem, with worked cases (exact match, tolerance balls, `k`-tries, partitions) matching the programme's, and a footnote 3 calling the codomain immaterial. The novelty of `R` is withdrawn.
- The same relation in ML privacy is Balle, Cherubin and Hayes, IEEE S&P 2022, Definition 2, `P[ℓ(Z, R(θ)) ≤ η] ≤ γ`, with the baseline separated as `κ(η) = sup_{z₀} P[ℓ(Z, z₀) ≤ η]`.
- Unifying confidentiality and integrity is Clarkson and Schneider, IEEE CSF 2010, contamination as the Biba dual of leakage and program suppression as reference against candidate. Suppression has no confidentiality dual. Their footnote 5 states that information-theoretic quantification ignores computational constraints on attackers. The unification claim is withdrawn.
- A security definition built on a quantified success relation was proved eliminable. Bellare and Sahai, CRYPTO 1999, reduce non-malleability over poly-time relations to indistinguishability under parallel chosen-ciphertext attack with queries one fewer than the arity. The programme's answer, that a fixed `R` with a varying budget leaves no such trade, is a conjecture. Open.
- GKVZ, FOCS 2022, Definition 4.2 carries two thresholds (`γ` on the input perturbation, `β` quantizing an output into a bit), Definition 4.7 places the win inside a real against ideal difference for a PPT adversary, and Remark 4.8 argues the absolute form is unsatisfiable. Verified verbatim.
- Every parameterized integrity notion in cryptography restricts the adversary's move class because an impossibility forces it, Bellare and Kohno's `Φ` by Propositions 4.1 to 4.3, non-malleable codes' family by tamper-proof impossibility. Non-vacuity at a threshold parameter must therefore be established, not inherited.
- Leakage-resilient cryptography restricts the side-channel map, a different axis. Fisher information leakage restricts to unbiased estimators. Maximal leakage, α-leakage and LDP take a supremum over target functions. The name leakage function is taken three times.
- Verified verbatim in that sweep were Alvim et al. Definitions 3.1 to 3.6, Balle et al. Definition 2, Clarkson and Schneider's measures and Proposition 1, Bellare and Sahai Definitions 3.1 and 3.2 and the elimination passage, GKVZ Definitions 4.1, 4.2, 4.6 and 4.7, Chaudhuri et al. Definition 3, and Akavia et al. Definitions 2 and 3. Not verified were Bellare and Namprempre's numbering for INT-CTXT and INT-PTXT, Bellare and Kohno's `Φ`-class details, the GLMMR TCC 2004 definition, and a source for the certified-robustness predicate.
- The `R` lineage, recorded 2026-08-05 and not all read in full, runs Bhowmick, Duchi, Freudiger, Kapoor and Rogers, arXiv 1812.00984, Definition 2.3, then Balle, Cherubin and Hayes Definition 2, Hayes, Mahloujifar and Balle, NeurIPS 2023, Definition 1, Xiao and Devadas, CRYPTO 2023, Definition 1, Cummings, Hod, Sarathy and Swanberg, arXiv 2405.01716, Definitions 4.4 and 4.8, Cohen et al. Definitions 1.4 to 1.6 and C.1 (the notation `R` is theirs, and their Definition 1.4 is attributed by them to Balle et al. and Attaxonomy), Kaplan, Mansour, Nissim and Stemmer Definitions 3.6 and 4.4, Swanberg, Annamalai, Balle, Hayes and Smith, arXiv 2507.08158, and Salem et al., IEEE S&P 2023, whose §II-C names the compute move and declines it. All but Cohen et al. Definition C.1 quantify over an unbounded adversary. Attaxonomy has no refereed venue (FORC 2024 non-archival track). `exp/docs/notes/case-study-sparse-support-recovery.md` §9, `exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md`.

### 4.10 Taxonomies and systematizations

- The requested matrix of privacy and integrity, train and test time, and dataset, algorithm and model is unoccupied. Papernot, McDaniel, Sinha and Wellman, IEEE EuroS&P 2018, cross two of three (training and inferring against integrity and privacy, with a Logic Corruption rung). Barreno, Nelson, Joseph and Tygar, Machine Learning 2010, with Huang et al., AISec 2011, give the only literal cube. NIST AI 100-2e2025 has Source Code Control and is the only document with availability, integrity and privacy on one page. Wang and Luan, TMLR 2026, give the only source-to-target asset matrix. ENISA 2021 Table 3 crosses threats with lifecycle stage. Privacy and integrity never co-occur elsewhere (Rigaki and Garcia, Salem et al., Cinà et al., Li et al., Goldblum et al., Desfontaines and Pejó, De Cristofaro). 2026-08-05. `exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md`.
- Unified formal definitions do not exist. Salem et al., IEEE S&P 2023, cover privacy only with 18 games, `⪯_c` reductions and Theorems 1 to 11, with information-theoretic adversaries. Wu et al., arXiv 2302.09457, cover integrity only as an optimization template. Villa, Durak, Kohno, Maharramli and Roesner, arXiv 2603.02590 (March 2026), span both through one predicate game and are the closest work, with an unbounded adversary whose capability set is a flag set, grey-box knowledge excluded, a predicate conceded non-implementable, and no reductions. 2026-08-05. Same report.
- Across about thirty works the compute axis reduces to six entries, none a security parameter (Desfontaines and Pejó dimension C binary, Salem et al. §II-C a query counter, TrojanZoo wall-clock, Cinà et al. §3.4.2 a limitation, poisoning-rate bins, Mahloujifar et al. `p`-tampering as one attack model). The knowledge axis degenerated from five components in 2014 to one bit in 2022 to nothing. Four citations in the sweep brief were wrong (TrojanZoo and BackdoorBench author lists, the Liu et al. privacy survey, the provenance of the Biggio knowledge tuple). 2026-08-05. Same report.
- Papernot et al. carry no computational-resource axis, with a resource-like quantity appearing three times inside the survey (a poisoning fraction, unbounded poisoning power, an ACRE query-complexity result) and never as an axis. Confirmed 2026-08-22. Audit §4.
- Shafran et al., Beyond Labeling Oracles, is TMLR 2024, Wen et al., the data-reconstruction SoK, is USENIX Security 2025, Zhang et al. is IEEE SaTML 2025, and Fenaux and Kerschbaum stays a preprint. Corrected 2026-09-03. Shafran et al. state no model-extraction literature formally defines a successful attack, scoped to accuracy-driven extraction. `exp/survey/lib/reports/archive/2026-09-03-halil-review-survey-round-2.md`, `games.tex`.
- No position paper or survey arguing complexity-theoretic foundations as the standard was found, and no SoK from 2018 to 2026 states a complexity or information-theoretic organization in its title or abstract. Agent sweep, 2026-10-13. Sweep `definitions.md` §4.

### 4.11 Extraction, proof-of-learning, detection and generation

- Dziedzic, Kaleem, Lu and Papernot, ICLR 2022, charge extraction compute through a proof-of-work puzzle, under 2x slowdown for legitimate users and up to 100x for attackers, with no definition and no theorem. 2026-08-22. `games.tex`.
- Chandrasekaran et al., USENIX Security 2020, put the query budget inside the extraction definition and reduce extraction to query-synthesis active learning, so complexity travels in the upper-bound direction only, and the converse is neither proved nor claimed. 2026-08-22. `games.tex`.
- Carlini, Jagielski and Mironov, CRYPTO 2020, recover ReLU parameters with polynomially many queries and work exponential in width for sign recovery, empirically. Canales-Martínez, Chavez-Saab, Hambitzer, Rodríguez-Henríquez, Satpute and Shamir, EUROCRYPT 2024, make it polynomial time, polynomial in depth. A hard-label polynomial version (CCH+26, J. Cryptology 2026) is recorded from its abstract. 2026-08-22 and 2026-10-13. `games.tex`, `oracle.tex`, sweep `computation.md`.
- Proof-of-learning forgeries (FJTYCDCP23) succeed against the verifier's lossy view of the trace without paying the walk, and exact reproduction of a trace remains empirically out of reach (SHKBL25). 2026-08-22. `price.tex`.
- Detection and generation for learned distributions. Alvarez-Melis, Garg and Kalai, NeurIPS 2022, correct title Are GANs overkill for NLP. Corrected 2026-08-22 on two of four points. §5 gives both directions (Lemmas 1 and 2) without polynomial time, since the authors say repeating the efficient step gives an exponential-time algorithm. The polynomial-time result is §6, in a next-token model, one direction only, with no converse. No distinguisher carries a class or runtime bound, both directions are empirical on a fixed sample, and Lemma 2 needs common support. The paper describes the §6 reduction from both ends, and its Algorithm 1 converts a next-token distinguisher into a likelihood improvement. Not framed as security. Root, audit §2, `games.tex` Section The decision variant.
- Suya et al., IEEE SaTML 2024, survey 164 black-box attacks and re-run 11 transfer attacks under a fixed per-batch time budget, recommending runtime as the equalizing factor. The draft's earlier statement that they re-ran 164 was corrected 2026-09-03. `exp/survey/paper/sections/07-findings.tex`, round-two report M6.
- Carlini et al., On Evaluating Adversarial Robustness, hold that attacker computation is not a reasonable threat-model parameter, a considered position matching the practice of Athalye, Carlini and Wagner, ICML 2018. Quotation verified, recorded 2026-08-22. `exp/survey/paper/sections/07-findings.tex`.

### 4.12 Backdoors, filters, concentration and watermarks

- Ball, Gluch, Goldwasser, Kreuter, Reingold and Rothblum, arXiv 2507.07341, recorded as ICLR 2026, is existential. Its abstract says there exist LLMs with no efficient prompt filter, its Theorem 2 needs the model to share a secret key with the attacker, and its Theorem 1 needs the filter to run no faster than the model it audits, a ratio between two parties' compute left as a side condition. Audited 2026-08-20. Villa et al. discuss the result rather than prove it, and it does not say every judge must match the complexity of its predicate. `exp/survey/lib/reports/archive/2026-08-20-halil-lit-survey-spine.md`, `games.tex` Section The challenge generator as an oracle.
- The concentration-of-measure vulnerability theorem holds, its hypothesis is measured false for image benchmarks by the same group (arXiv 1905.12202), and arXiv 2309.16096 uses the opposite sense of concentration to prove robust classifiers exist. Audited 2026-08-20. Spine report.
- The Statistically Undetectable Backdoors document in `raw/` was anonymous under ICLR 2026 double-blind review, so the attribution to Bogdanov and Rosen was an inferred de-anonymization. Audited 2026-08-20. The 2026-10-13 sweep lists the work as BRV26 at ICML 2026. Spine report, sweep `computation.md`.
- GKVZ22 achieve black-box undetectability from digital signatures and white-box undetectability for two training paradigms from continuous LWE and sparse PCA. Kalavasis et al., NeurIPS 2024, state that GKVZ22 leave the white-box question open, which is why they assume obfuscation. Draguns et al. state that unelicitability is not white-box undetectability. 2026-08-22. `oracle.tex` Section The backdoor game, audit §3.
- Christiano, Hilton, Lecomte and Xu, ITCS 2025, Definition 3.1 (ε-defendability), Theorem 4.1 (best confidence `max(1/2, 1 − Θ(VC(F)ε))`), Definition 5.1, and Theorem 5.5 (polynomial-size circuits are not efficiently defendable under OWF and iO). Agent reading 2026-10-13. Sweep `definitions.md` §4b.
- Fawzi et al. wrote that the human visual system is inherently robust, and the wiki had reversed it. The jailbreak-paradox page swapped Theorems 3.1 and 4.1. Two Gamarnik quotes were swapped between pages. 2026-08-22. Audit §3.
- Fabrications traced on 2026-08-22. The seven challenges on the cross-domain MAS page were invented. IMTM occurs zero times in the attributed paper, in all 186 PDFs, and twice in the compass artifact. MELON has no provable detection theorem. CaMeL contains no theorem or lemma. The covert-learning page invented an LWE assumption and halfspace results. The low-degree survey page cited arXiv 2603.02594 from a June 2025 document. The planted-assumptions PKE page listed three assumptions where the paper states two. The planted-graphs crypto page confused share size with message size. About 5 percent of 1100 quotations were wrong, sixteen of them the compass artifact's own prose. Audit §3.
- Bubeck and Sellke do write that overparametrization is necessary to interpolate smoothly, and the earlier fabrication charge was a spelling false positive. The theorem concerns smooth interpolation with a bounded Lipschitz constant, not resistance to an adversary. Gilmer et al.'s sentence was altered, not invented. 2026-08-20. Root, Conventions, audit §2.

### 4.13 Bibliographic corrections

- Venues resolved on 2026-09-03 include Garg et al. (GJMM20) at ALT 2020, Computational Differential Privacy at CRYPTO 2009, Carlini, Jagielski and Mironov at CRYPTO 2020, Continuous LWE at STOC 2021, the Brennan and Bresler SQ and low-degree equivalence at COLT 2021, and the Barak et al. SoS planted-clique bound at FOCS 2016. Ding et al. arXiv 2502.15024 was retitled at NeurIPS 2025. One corpus row (Ho et al.) had been classified against another paper's abstract and was redone. `exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md`, round-two report.

### 4.14 Null searches recorded by the 2026-10-13 sweep

Agent sweep, no paper from these searches is cited until read. Sweep `computation.md` §4 and `information.md` §4.

- No peer-reviewed theorem that verifying unlearning is hard or impossible.
- No computational hardness of membership inference or reconstruction under a cryptographic assumption, only sample or query complexity results and efficient attacks on shallow networks.
- No SQ or low-degree lower bound against a backdoor or poisoning adversary.
- No tight information-theoretic query lower bound for extracting a trained network to a stated fidelity.
- Forward citers of CHLX25 and of GIKKM23 give no new defendability result and no new separation of computational and statistical privacy.
- Liu, Evans and Xiong (LEX26), IEEE S&P 2026, are recorded as stating extraction as at least `2^b` expected queries and proving indistinguishability and extractability incomparable, and GG25 and GTNP25 as stating two-party gaps in samples, time and circuit size. Sweep `definitions.md` §1.

### 4.15 Methodological record

- On 2026-07-26 four novelty claims were checked and four refuted. The single survivor was verified by a citation-graph sweep, and topic search scored zero of four. Prefer a named published conjecture over an empty framing. Root.
- Fine-grained in privacy-preserving ML usually means per-user access control. Search by definition shape. Root.
- The 2026-08-20 to 2026-08-22 audit verified 181 of 181 source pages and found two contamination paths and two false-positive modes of the quote checker (spelling variants, editorial gloss inside quotation marks). Always `grep -a`. Root, audit §1.
- A count stated from memory on 2026-08-22, that membership inference appeared in five of six landscape subsections, was false, the true figure being zero. Ruling `2026-08-20-an-unverified-count-is-not-written`. `exp/survey/lib/profs/2026-08-22-halil.md`.

## 5. Open targets

Best candidates first, as the files name them.

- Constrained fiber navigation on the training map, a hardness theorem, called the best-defined target of its session. Root, `exp/docs/notes/game-family-and-reduction-targets.md` §4 and §5.
- G2-linear, the noiseless lattice attack on the smallest instance, decidable with existing tools, which either breaks the Suliman et al. conjecture or locates its boundary. Same note §5.
- Attacker and defender priced in the same exponent units and separated at matched budget, with the attacker restricted to training's own class. Root (still open, narrowly), Song §1.3 item 2.
- The estimation threshold an attacker who must recover actually faces, which is not established. Root.
- Step 5 of the case study, reducing support recovery from a trained network to recovery from samples, starting with a ridge release. `exp/docs/notes/case-study-sparse-support-recovery.md` §13 and §16.
- The security profile curve, the third case of the pancake trichotomy, the projection-and-test tolerance and the search-to-decision direction for Gaussian pancakes. `exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md`.
- Monotonicity of `{R_θ}`, the relation of `Φ` to g-leakage, the availability reading of `Φ`, the answer to Bellare and Sahai, non-vacuity at the threshold parameter, and the suppression asymmetry. `exp/docs/reports/2026-08-05-unfiled-leakage-and-integrity-functions.md`, `exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`.
- R3 against CHLX25, exhaustiveness of the four criteria, an `R`-parameterized definition for the training-time displacement family, and the legitimacy of the adversary-class axis under mutual compatibility and inner exclusivity. Reports of 2026-08-05.
- `COMP-MEM` reduced to hCLWE, recorded as appearing open in its membership version, after engaging traitor tracing and the DP-hardness corpus, with Gap-`K^t` over samplable distributions as the native idiom. `exp/literature/related-work.md` §0 and §9.
- A fine-grained or ratio-parameterized privacy notion, a `δ`-indexed proof-of-learning family, and a formal success definition for model extraction. Root (two seams).
- Whether the auditor-to-model compute ratio in Ball et al. Theorem 1 can be a fine-grained gap at an explicit exponent. Spine report.
- A separation of computational and statistical DP on a natural task, and CDP or SDP applied to reconstruction from weights. Root.
- A memory-bounded ML or privacy adversary. Root.
- Chapter 24 OP1 (robust comp-stat gap), OP2 (inherence of the trusted prover), the smooth `|w|` against `t_eval` tradeoff, the comp-stat envelope experiment, the crown-jewel threshold, and joint π. `exp/docs/notes/chapter-24.md` messages 20, 23 to 27, `exp/docs/notes/intro-computational-security-of-learning.md` §6.
- The single-index Gaussian fiber of the training map and whether a point in it can be found from weights and bounded side information. `exp/docs/notes/fibers-of-the-training-map.md` §8.
- An AI oracle the author accepts, which fixes the distribution of the learned function, states a utility condition and supports one proved bound on membership advantage. Also which oracle training is, the CGH analogue, strict ordering of `{eval, grad_x}` and `{eval, grad_θ}`, lower bounds on `eval` and `train` calls, whether any natural training approximately satisfies ideal representation, the hardness of the counting step for natural classes, and a prior-art check for training-as-oracle with calls as the resource. `exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`, both 2026-10-13 reports.
- The learning-oracle opens, non-triviality of the backdoor game, where the planter writes, the model-level auditor, the declaration, uninstantiability, a generation criterion and the classification case. `exp/survey/paper/parked/formalization/oracle.tex` Section What is deferred.
- The six extraction-game opens and a lower bound over all algorithms for compute pricing. `games.tex` last section, `price.tex` Section The price of skipping.
- Eight survey issues of 2026-09-17 are open. They cover gradient inversion and split learning absent from the corpus, no priced threat-model template, the parity run and formalization parked, Section 7 standing alone, single-coder agreement unmeasured, no slot for the 19 pages of tables, a third review round owed, and title, anonymity and ethics conditions of the call. `exp/survey/lib/issues/`.
- Three questions have been open with the PI since 2026-08-05, namely availability as a third goal, whether LLM and agentic systems are in scope, and the venue. `exp/docs/meetings/2026-08-05-pi.md`.

## 6. Decisions and constraints

- Definitions in this area are commodities, so the contribution must be a theorem or a measurement. `exp/docs/CONTEXT.md`, `exp/docs/notes/game-family-and-reduction-targets.md` §6, root (two seams). The PI meeting of 2026-08-05 named the definitions as the contribution, and the prior-art report of the same day withdrew the definitional claim and kept the adversary axis.
- The guardrail on `R`. `R` must be pinned to a harm before anyone looks at its difficulty, and a planted source voids the guardrail as surely as a planted `R`, so the source is held natural and `R` selects the problem. 2026-08-05. `exp/docs/CONTEXT.md`.
- Measure the attack, do not prove it hard. 2026-08-05. Root, `exp/survey/lib/profs/rulings.md`.
- Secure against all PPT first and treat the learning-shaped adversary as Phase 2. `exp/docs/notes/intro-computational-security-of-learning.md` §5.
- Membership uses raw advantage, and baseline subtraction is used only for real-valued criteria. `exp/docs/notes/game-family-and-reduction-targets.md` §1 and §3.
- Write the gap as an exponent `honest^{1+δ}`, never as a constant. 2026-07-26. Root.
- Fitting a specific `R` to a specific empirical attack is abandoned, since fitting reproduces the variance the theory removes. 2026-08-05. R-as-quantizer report.
- State the adversary's budget in samples so the alignment test passes, as an explicit modelling decision. Case study §14.
- Do not use the name leakage function. Present `R` as a binary gain function or as reconstruction robustness and answer Bellare and Sahai under threats to validity. 2026-08-05. Prior-art report.
- Write-up register for the programme is `academic-ste`, with no first person and no em dash. `exp/docs/CONTEXT.md`.
- Verify novelty adversarially before endorsing it, record negative results, prefer a named published conjecture, and treat the user's examples as representatives. Root, Conventions.
- No quotation from a wiki page lacking `claim_quantifier` enters the survey until verified, and a counter-result is filed as a limit, not a sibling. Root, Conventions.
- Chapter 24 is append-only, and no prose is drafted until Mursit ticks the consent box. `exp/docs/notes/chapter-24.md` protocol.
- Chapter 24 principle (3) and the separation discipline forbid merging statistics and computation. Messages 1 and 26.
- The learning oracle, agreed 2026-08-22, idealizes only the training map, outputs the full trace, keeps views as game parameters, separates recipe noise from view noise, defines white-box as weights plus unlimited ordinary computation, forbids party-authored recipes, and is invented and defended with the AIOracle generic model as named precedent. `exp/survey/lib/reports/archive/2026-08-22-halil-plan-survey-tasks.md` Part IV, `oracle.tex`.
- Survey rulings, by slug and date. 2026-08-05-measure-the-attack-do-not-prove-it-hard, 2026-08-20-the-subject-is-characterization-not-imposition, 2026-08-20-crypto-with-no-learning-content-enters-as-a-destination, 2026-08-20-the-frame-has-an-outside, 2026-08-20-an-unverified-count-is-not-written, 2026-08-22-membership-inference-is-not-the-running-example, 2026-08-22-citation-hierarchy, 2026-08-22-recency-is-checked-not-assumed, 2026-08-22-author-standing-is-a-tiebreaker, 2026-09-03-a-bare-two-party-inequality-is-relative, 2026-09-03-a-radius-a-theorem-outputs-binds-nobody, 2026-09-03-a-restricted-class-lower-bound-binds-the-learner, 2026-09-03-a-catalogued-definition-is-not-an-asserted-bound, 2026-09-17-the-survey-is-the-project-root. A ruling is reopened only by a later ruling that names it. `exp/survey/lib/profs/rulings.md`.
- Two reviewer findings declined on 2026-09-03, preventing-false-discovery-hard stays `reconstruct`, undetectable-watermarks-lm is `measured`. `exp/survey/lib/profs/dismissed.md`.
- The survey proves nothing. Every number enters through `lib/numbers.csv` and every claim through `lib/claims.yml`, and a quotation enters only after `lab/src/check-quotes.py` binds it. `exp/survey/CLAUDE.md`.
- The scope test admits a work about learning that makes a formal claim in which somebody's resources matter, `κ` is per party and takes the value unstated, and empirical attack papers, norm-ball certified defences and most agentic work are out. 2026-08-20. `exp/survey/lib/reports/archive/2026-08-22-halil-plan-survey-scope-and-structure.md` §2 and §3.
- Halil reads reports, not chat, and programme reports have five sections with the verdict first. `exp/CLAUDE.md`.
- `exp/paper/` is deliberately an empty scaffold with no venue chosen. `exp/docs/CONTEXT.md`, Repo notes.
- The survey targets the IEEE S&P 2027 SoK track. The deadline of 2026-11-17 with abstract registration on 2026-11-10 is flagged as not recorded as fact. `exp/survey/paper/.paper-meta.yml`.
- The ten earlier Claude sessions are archived on purpose and must not be unarchived. 2026-10-15. `exp/docs/OLD_SESSIONS.md`.

## 7. Where to look

| Topic | Path |
| --- | --- |
| Refuted and corrected claims, the negative-results list | `CLAUDE.md` (root), section Current Programme |
| Programme ledger, attack-surface axes, standing constraints | `exp/docs/CONTEXT.md` |
| The `R` reports of 2026-08-05 | `exp/docs/reports/` |
| Prior art for `R`, `Φ` and the unification | `exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md` |
| Prior taxonomies and the missing adversary axis | `exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md` |
| PI meeting of 2026-08-05 | `exp/docs/meetings/2026-08-05-pi.md` |
| Halil's own voice | `exp/docs/notes/ideas.md` |
| Field introduction, `COMP-MEM`, lineage | `exp/docs/notes/intro-computational-security-of-learning.md` |
| Games G1 to G5, three maps, reduction targets | `exp/docs/notes/game-family-and-reduction-targets.md` |
| Fiber of the training map | `exp/docs/notes/fibers-of-the-training-map.md` |
| `R` selecting the problem, sparse support recovery | `exp/docs/notes/case-study-sparse-support-recovery.md` |
| Chapter 24 theory, keystone, staircase, OP1 and OP2 | `exp/docs/notes/chapter-24.md`, messages 1, 7, 8, 20, 23, 26 |
| Chapter 24 against AIOracle | `exp/docs/notes/chapter-24.md` messages 28 to 32 |
| Practitioner summary of Chapter 24 | `exp/docs/notes/LearningSystemsAsMachines_for_Practitioners.html` |
| SQ-hardness reduction for black-box attacks | `.tools/proof.tex` |
| About eighty candidate reference problems by tier | `exp/literature/related-work.md` |
| Survey claim, ledger, current state | `exp/survey/CONTEXT.md` |
| Survey rulings and declined findings | `exp/survey/lib/profs/rulings.md`, `exp/survey/lib/profs/dismissed.md` |
| Survey claims and numbers | `exp/survey/lib/claims.yml`, `exp/survey/lib/numbers.csv` |
| Codebook, thirteen fields and decision rules | `exp/survey/lib/literature/codebook.md` |
| Coded corpus of 200 | `exp/survey/lab/results/corpus-classification/classification.tsv` |
| Ontology of 237 works, training, access, attacker class | `exp/survey/lib/literature/ontology/views.md`, `papers.tsv` |
| Agent sweeps of 2026-10-13 by lane | `exp/survey/lab/results/literature-sweep/definitions.md`, `computation.md`, `information.md` |
| AI oracle issue and the two oracle reports | `exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`, `exp/survey/lib/reports/src/2026-10-13-*.tex` |
| Learning oracle, recipes, traces, views, ports | `exp/survey/paper/parked/formalization/oracle.tex` |
| Price of aiming and skipping, parity run | `exp/survey/paper/parked/formalization/price.tex`, `exp/survey/lab/results/sparse-parity/` |
| Extraction games, `δ`-extraction hardness | `exp/survey/paper/parked/formalization/games.tex` |
| Wiki audit, corrections, content errors | `exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md` |
| Survey scope and framework reasoning | `exp/survey/lib/reports/archive/2026-08-22-halil-plan-survey-scope-and-structure.md` |
| Round-two review and recount | `exp/survey/lib/reports/archive/2026-09-03-halil-review-survey-round-2.md`, `exp/survey/paper/reviews/sp27/` |
| Survey draft | `exp/survey/paper/main.tex`, `exp/survey/paper/sections/` |
| Open survey work | `exp/survey/lib/issues/`, index in `exp/survey/lib/INDEX.md` |
| Earlier session transcripts | `exp/docs/OLD_SESSIONS.md` |

## 8. Overlap with HE-ML

An idealized learning oracle with nameable training seeds.

- The parked learning oracle draws fresh coins on every call and returns independent traces for one corpus, so parties cannot name seeds. Recipes, including initialization rules, are named by the game, and a game whose theorems depend on the meter must use initializations that carry no party-chosen information. `exp/survey/paper/parked/formalization/oracle.tex` Defs Passive learning oracle and Metered cost.
- The 2026-10-13 generic training oracle exposes `train(S)` returning a fresh handle and leaves `Train` randomized and never opened. Ideal representation is its idealization, with random-oracle standing by the BGIRSVY01 analogy. `exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex`.
- The version-space oracle and the SDSOJ19 Gibbs posterior are the two idealized learners on record, both proven to give no white-box against black-box gap. `exp/survey/lib/reports/src/2026-10-13-halil-version-space-oracle.tex`, the 2026-10-13 issue.
- Villa et al.'s AIOracle with its generic language model and MID bound is the named precedent, placed by Chapter 24 on the idealized-model rung with the CGH caveat. `exp/docs/notes/chapter-24.md` messages 28 to 32.
- Chapter 24 makes the uniform seed `ρ` part of the source and learner randomness `H_L` a metered resource. Messages 1 and 7.

Learning-bounded or SQ-bounded privacy attackers.

- Halil's learning adversary. `exp/docs/notes/ideas.md`.
- The SQ-hardness proof bounds a black-box attacker through the learner's SQ access, independent of the attacker's queries. `.tools/proof.tex`.
- Capacity-bounded DP, the BJRZ and ABIKN correction, the Ngo and Kim retraction, the low-degree caveats, and the narrowly open same-units target. Root, sections 4.2 and 4.8 here.
- Jagielski et al. Theorem 3 as the closest priced extraction adversary. `games.tex`.
- The SQ-auditor proposition, and the reading of a gradient recipe as a correlational-query algorithm. `oracle.tex`, `price.tex`.
- No attacker in the 2026-10-13 coding is a formal first-order class. `exp/survey/lib/literature/ontology/views.md`.

Attackers that train attack models.

- Shadow models and LiRA are calls to the training oracle, priced in training runs. `exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`, `oracle.tex` Section The corpus mapped (a shadow-model attack costs `N·T` steps).
- The codebook lacks a training-runs unit, a dispute recorded against the LiRA row, while the ontology codes eight works under `res-training-runs`. `exp/survey/lib/reports/archive/2026-09-03-halil-quotes-batch-b.md`, ontology `views.md`.
- Zhang et al.'s auditor who cannot afford a training run has a read budget of zero steps. `oracle.tex`, `exp/survey/paper/sections/02-problem.tex`.
- The R4 fidelity criterion makes the distillation student and the extraction adversary the same object up to authorization. `exp/docs/reports/2026-08-05-unfiled-concrete-r-criteria.md`.
- The proposed priced threat-model template restates LiRA with its adversary class and shadow-model budget named. `exp/survey/lib/issues/2026-09-17-halil-no-priced-threat-model-template.md`.

Seed knowledge as an attacker resource.

- The proof's randomized-learner remark treats public and private learner coins and leaves the bound unchanged. `.tools/proof.tex` Remark Randomized learners.
- `R` is built to absorb seed-dependent variance, since a reduction consumes the bit and nothing upstream. `exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md`.
- The training map is randomized over seed and batch order, and with randomness the fiber becomes the conditional distribution of `D` given `w`. `exp/docs/notes/game-family-and-reduction-targets.md` §2, `exp/docs/notes/fibers-of-the-training-map.md` §6.
- Gradients plus the initial state determine the model for gradient-factoring recipes, so a view must say what it withholds. `oracle.tex` Fact.
- Haghifam, Smith and Ullman price attacker knowledge of the covariance, and the separation vanishes when it is known. Root.
- Chapter 24 puts all randomness on a canonical seed tape `ρ` supplied by the channel, and defines access modes by how the channel couples `L` to `ρ`, with i.i.d. as a fresh `ρ` per query and membership or chosen-input access as `L` setting `ρ` or `x`. A one-record neighbour edit is then a `d_R`-small perturbation of `Π`. `exp/docs/notes/chapter-24.md` message 3 (about line 543) and message 6 (about line 1113).
- The GKVZ22 white-box backdoor works by tampering with the random coins of random Fourier features, so the planter's secret lives in the training randomness. Agent sheet 2026-10-13, sweep `definitions.md` sheet GKVZ22. The AI oracle issue records that the backdoor papers prove inside a fixed paradigm (random Fourier features, a frozen random first layer). `exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`.
- None of the files read prices an attacker's knowledge of the training seed as a resource. The items above are the nearest.

Split-learning inversion.

- Gradient inversion in split or federated learning is seated at training phase, no displacement, a property of `D`. `exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md`.
- Game G2 covers leaked, federated or split gradients on the feature map at fixed `θ`, with the affine-plus-box lattice structure and the Suliman et al. conjecture. `exp/docs/notes/game-family-and-reduction-targets.md` §3 and §4.
- The split-learning cut is a port in each direction of the interactive oracle, passive observation is read-only attachment, and gradient inversion is a produce game using the Balle et al. criterion. `oracle.tex` Sections interactive form and The corpus mapped.
- LAMP defines no success criterion. Audit §4.
- The corpus holds no gradient-inversion or split-learning work, an open issue noting this is the author's own area. `exp/survey/lib/issues/2026-09-17-halil-gradient-inversion-absent-from-corpus.md`.
- The SQ proof does not handle per-round federated observation. `.tools/proof.tex` Caveats.
