# Problem register

This register holds every open problem and research target of the line on formalizing AI security, from HE-ML and FORMAL_SECURITY, one entry per problem in the format of `README.md`. Open entries stand under their weight, and solved, refuted-as-posed or withdrawn entries stand under Archive at the end.

# Central

## prob-reduce-security-to-known-learning-problems
statement: Can an adversary against a learning procedure be measured by its computational and
  learning resources, so that a learning-security problem reduces to a known learning problem, in a
  framework that experiments realize exactly or approximately? The reduction may use the learning
  oracle or not. Polynomial-time adversaries are allowed. A cheap cryptographic plug-in, such as a
  PRG placed somewhere in the procedure, does not count. Finding that some aspect of a model
  reduces to or yields a PRG counts. The leading candidate is prob-split-learning-seed-separation,
  a known-seed against unknown-seed separation for split-learning inversion against
  statistical-query attackers. Three constraints bind it. NeuraCrypt was broken empirically by
  Carlini et al. UnSplit inverts unknown bottom models at split depth one. The training transcript
  may leak the seed, which prob-split-transcript-leaks-seed asks. On the oracle route the theory's
  adversary is unbounded, so the theory needs a new resource model before it shares statements
  with polynomial-time adversaries (HE-ML digest, section 3.4).
posed: Halil, 2026-10-25, in the session that commissioned this context
weight: central
status: open
literature: the learning-bounded scan of 2026-10-25 for the leading candidate
  (`HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md#Verdict of the scan`).
  FORMAL_SECURITY's record that the attacker as a restricted-class learner is occupied in
  cryptographic units and unclaimed only in learning-theory units, and the FORMAL_SECURITY
  zero-citer sweep of 2026-08-20 on the exponent cell, both in
  `FS:CLAUDE.md#Established negative results`.
tried: FORMAL_SECURITY withdrew its definitional claim on 2026-08-05, because the criterion R and
  the unification of privacy and integrity were already published, and it ruled that the
  contribution must be a theorem or a measurement
  (`FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`). FORMAL_SECURITY put
  security against all PPT adversaries first and left the learning-shaped adversary to a second
  phase, because SQ hardness is unconditional but restricted. Parity is SQ-hard and solved by
  Gaussian elimination (`FS:exp/docs/notes/intro-computational-security-of-learning.md#5`).
  thm-replay-audit-steer derives its seeds from a random oracle, a plug-in of the excluded kind
  under a heuristic reading of the rule of 2026-10-25 (HE-ML digest, section 4.1).
depends-on: prob-split-learning-seed-separation, prob-attacker-lower-bound-from-hard-learning,
  prob-same-units-matched-budget-separation
claimed-by: none
where: `HE-ML:sink/formalizing/sources/2026-10-25-he-ml-digest.md#7 Decisions`, the entries of 2026-10-25.
  FORMAL_SECURITY records the same idea as Halil's informal conjecture of a learning adversary
  bounded by learnability, in `FS:exp/docs/notes/ideas.md`.
history:
  - 2026-10-25 posed by Halil and entered from the brief of the commissioning session and HE-ML digest section 7. Weight central, set by Halil's decision of that day to move the line to this computational view.
  - 2026-10-25 two reductions exist in the space computational-limits. Blind reconstruction reduces to NGCA and hCLWE, and
    reconstruction of the label-relevant coordinate is the single-index problem priced by the generative exponent.
    Whether a hard record law meets the plug-in rule is a decision for Halil.
  - 2026-10-26 a third reduction: learning-based extraction onto the single-index problem of the released link
    (thm-extraction-exponent-price). def-hard-problem-mapping fixes what a mapping is.

# Supporting

## prob-split-learning-seed-separation
statement: For split-learning inversion over random expansive ReLU bottom models, is there a
  separation between attackers who know the training seed and attackers who do not? With the
  seed, inversion runs in polynomial time, since Lei et al., NeurIPS 2019, Theorem 3, invert random
  Gaussian layers of expansion at least 2.1 exactly by layer-wise linear programs with high
  probability. Without it, the target is a lower bound of super-polynomially many statistical
  queries. Abbe et al., NeurIPS 2021, Theorem 1c, carry such a bound to mini-batch SGD attackers
  when batch size times squared precision exceeds a logarithmic factor, and not to batch-one or
  fine-precision attackers. Three constraints bind the construction. NeuraCrypt, a law of
  random-network encoders, was broken empirically by Carlini et al. (arXiv 2108.07256). UnSplit
  inverts an unknown bottom model at MNIST split depth one, before and after training (Erdoğan,
  Küpçü and Çiçek, WPES 2022). The training transcript may leak the seed
  (prob-split-transcript-leaks-seed). Balle, Cherubin and Hayes measure the seed as a resource
  only empirically, with reconstruction much better under the known initialization. The
  learning-oracle theory's thm-reference-access separates named from hidden seeds on one node for
  unbounded adversaries in the oracle's cost model, and this problem asks for the computational
  form.
posed: the learning-bounded scan of 2026-10-25, verdict 4, named the leading candidate in the
  session of 2026-10-25 and not yet adopted
weight: supporting
status: partial
literature: the learning-bounded scan of 2026-10-25, about twelve web searches and a keyword filter
  over 267 citers of Xu et al., which found no formal separation between known-seed and
  unknown-seed attackers
  (`HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md#Verdict of the scan`). No
  FORMAL_SECURITY file read for its digest prices an attacker's knowledge of the training seed
  (`HE-ML:sink/formalizing/sources/2026-10-25-formal-security-programme.md#8 Overlap with HE-ML`).
  FORMAL_SECURITY records that any novelty claim must be stated against Jagielski et al., USENIX
  Security 2020, Theorem 3, an SQ bound for fidelity extraction of random networks
  (`FS:exp/survey/paper/parked/formalization/games.tex#What is already occupied`).
tried: none
depends-on: prob-split-transcript-leaks-seed, prob-statistical-queries-for-regression
claimed-by: none
where: `HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md#Verdict of the scan`,
  item 4
history:
  - 2026-10-25 entered from scan verdict 4, HE-ML digest section 5.2 item 20, and the brief of the commissioning session. Weight supporting, because prob-reduce-security-to-known-learning-problems names it its leading candidate.
  - 2026-10-25 open to partial. Proven for pancake records and Gaussian-initialized ReLU clients trained by orthogonally
    equivariant updates (thm-blind-split-seed-separation): exact seed-known inversion against an exponential SQ price
    (frozen clients) and a worst-case lattice price for fine reconstruction (frozen or trained). Open: natural record
    laws, convolutional clients, Adam, coarse reconstruction in polynomial time. From the space computational-limits.

## prob-split-transcript-leaks-seed
statement: Does the training transcript that a split-learning server sees reveal the seed, or
  enough of the bottom model, to collapse the separation of prob-split-learning-seed-separation?
  UnSplit's joint optimization inverts an unknown bottom model at split depth one (empirical).
  FORMAL_SECURITY proves that for a gradient-factoring recipe the initialization and the per-step
  quantities determine the model, so a view must say what it withholds
  (`FS:exp/survey/paper/parked/formalization/oracle.tex#Views`).
posed: the learning-bounded scan of 2026-10-25, its first risk, set as a constraint in the session
  of 2026-10-25
weight: supporting
status: partial
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md#Verdict of the scan`,
  item 4
history:
  - 2026-10-25 entered from scan verdict 4 and HE-ML digest section 5.2 item 21. Weight supporting, because prob-split-learning-seed-separation, the leading candidate of the central problem, needs a no.
  - 2026-10-25 open to partial. For the protocol class P_H the server's whole view is a function of rotated records and
    fresh coins (lem-equivariant-view-coupling), so the transcript does not collapse the separation. Outside the class
    (Adam, published weights, known records) it stays open. The space proposed solved for P_H.

## prob-statistical-queries-for-regression
statement: Does a real-valued statistical-query framework carry lower bounds to inversion, which is
  a regression task? FORMAL_SECURITY records the same gap for single-index models, where the known
  thresholds measure detection and the estimation threshold is open
  (prob-attacker-estimation-threshold).
posed: the learning-bounded scan of 2026-10-25, its second risk
weight: supporting
status: partial
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md#Verdict of the scan`,
  item 4
history:
  - 2026-10-25 entered from scan verdict 4 and HE-ML digest section 5.2 item 22. Weight supporting, because prob-split-learning-seed-separation needs its lower bound to bind an inversion attacker.
  - 2026-10-25 open to partial. A reconstruction measured by correlation becomes a direction with d truncated queries of
    tolerance of order d^(-1/2) and reaches search lower bounds (prop-sq-blind-reconstruction-bound,
    prop-sq-label-relevant-reconstruction-bound).

## prob-attacker-lower-bound-from-hard-learning
statement: Is there a lower bound on a membership, inversion, attribute or reconstruction attacker
  that follows from a statistical-query lower bound or another hard learning problem?
  FORMAL_SECURITY's proof note of 2026-04-23 gives one case. It bounds every black-box adversary
  against a deterministic SQ-implementable learner, trained on the vertex-row encoding of a
  planted-clique graph, by the SQ distinguishing advantage at the learner's parameters, whatever
  the adversary's own query count (`FS:.tools/proof.tex`). The bound runs through the learner's SQ
  access and not the attacker's. It excludes learners that are not SQ-implementable, other
  encodings, white-box adversaries, per-round federated observation and LWE encodings. Jagielski
  et al., USENIX Security 2020, Theorem 3, give the extraction case for SQ-expressible attacks on
  random networks.
posed: the learning-bounded scan of 2026-10-25, verdict 3
weight: supporting
status: partial
literature: the learning-bounded scan of 2026-10-25, which found no such bound in the literature
  (`HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md#Learning-complexity lower bounds for privacy attackers`).
  The FORMAL_SECURITY sweep of 2026-10-13 recorded no computational hardness of membership
  inference or reconstruction under a cryptographic assumption, and no SQ or low-degree lower
  bound against a backdoor or poisoning adversary
  (`FS:exp/survey/lab/results/literature-sweep/computation.md#4`).
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md#Verdict of the scan`,
  item 3
history:
  - 2026-10-25 entered from scan verdict 3 and HE-ML digest section 5.2 item 19. Weight supporting, because prob-reduce-security-to-known-learning-problems needs a bound of this kind. Status partial, because the FORMAL_SECURITY proof note covers black-box attackers of SQ-implementable learners, and the FS programme digest records that proof as written in full without re-verifying it.
  - 2026-10-25 stays partial on a new basis. The FORMAL_SECURITY proof note behind the old status is refuted
    (thm-sq-hardness-black-box-attacks, alias thm-fs-sq-black-box-reduction). Inversion attackers of split learning are
    now bounded by SQ and lattice hardness for pancake records and by the generative exponent for the label-relevant
    coordinate.

## prob-same-units-matched-budget-separation
statement: Can an attacker and a defender be priced in the same exponent units and separated at a
  matched budget, with the attacker restricted to the algorithm class of training itself? Song,
  arXiv 2404.03272, section 1.3 item 2, names discriminators with bounded compute or memory as
  open.
posed: FORMAL_SECURITY root `CLAUDE.md`, recorded as still open only narrowly
weight: supporting
status: partial
literature: FORMAL_SECURITY's root record of restricted-class attackers, which finds the attacker
  as a restricted-class learner occupied in cryptographic units (Canetti and Karchmer, TCC 2021,
  Karchmer, SaTML 2023, Christiano, Hilton, Lecomte and Xu, arXiv 2409.03077, and arXiv
  2504.20310), and the zero-citer sweep of 2026-08-20 on the exponent cell, both in
  `FS:CLAUDE.md#Established negative results`
tried: none
depends-on: none
claimed-by: none
where: `FS:CLAUDE.md#Established negative results`, and
  `FS:exp/survey/paper/parked/formalization/games.tex#What is already occupied`
history:
  - 2026-08-22 Song's section 1.3 confirmed verbatim and the record corrected (FS programme digest, section 4.8).
  - 2026-10-25 entered from the FS programme digest, sections 4.8 and 5. Weight supporting, set by this register, because it is the slot left open for a restricted-class attacker and prob-reduce-security-to-known-learning-problems must stand against it.
  - 2026-10-26 open to partial. thm-same-units-gap-gaussian-mechanism gives a natural procedure where the attacker's price,
    samples plus Train calls, exceeds the trainer's by Theta(1 + n rho^2), attained efficiently. thm-extraction-exponent-price
    gives an extractor whose SQ exponent is twice the trainer's (heuristic as a sample comparison). The low-rank-adapter
    form of conj-same-units-gap stays open.

# Side

## prob-sum-channel-functional
statement: Let further honest clients, isolated and stateless, add their clipped updates to the
  releases of the clipped aggregation procedure with no deviation. Is there a functional of the
  learning function, defined by Train calls, that bounds every passive adversary as the
  exceedance probability does in thm-dataflow-composition, is never above it, lies below it at
  some learning function, and has a coupled-discipline certifier that is uniformly accurate with
  Train calls fixed by alpha, the accuracy, the rounds and the number of honest clients? Known.
  The exceedance probability has the first and third properties, by thm-dataflow-composition
  (c)(ii).
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 1 of the builder's register
  after round 10
weight: side
status: open
literature: unchecked
tried: The coupled execution shares the other clients' seeds across the two hypotheses, so their
  contributions cancel in the exceedance. Crediting them needs a coupling that moves their seeds.
depends-on: prob-seed-maps-exact-coupling
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 1
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 1. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-drawn-seed-price-above-d
statement: When the squared ratio of clip to noise exceeds d, is some drawn-seed certifier of the
  one-round divergence of thm-dataflow-composition (e) uniformly accurate over the clipped learning
  functions with e^(O(d)) poly(1/accuracy, ln(1/alpha)) Train calls, with a universal constant in
  O(d)? Known. The register proves that drawn-seed certifiers which output below a stated level at
  a reference function need Train calls of order the smaller of 2^(0.09 d) and
  e^(B^2/(32 sigma^2)), and that order e^(B^2/sigma^2) Train calls suffice in every dimension.
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 2 of the builder's register
  after round 10
weight: side
status: open
literature: unchecked
tried: The estimator of thm-dataflow-composition (e)(iii) has a variance governed by
  e^(B^2/sigma^2). No estimator of the Gaussian-smoothed divergence whose variance is governed by d
  alone is known for laws on a ball of radius much larger than sigma times the square root of d.
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 2
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 2. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-shadow-model-lower-bound
statement: On a finite query set U with C outputs and query depth q_E, does some family of learning
  functions force every shadow-model attack that reaches the label-only optimum within the
  accuracy, with probability at least one minus alpha, to use at least a constant times
  C^(q_E) ln|U| / accuracy^2 Train calls? Known. O((C^(q_E)(ln|U| + 1) + ln(1/alpha)) / accuracy^2)
  shadow runs suffice, by thm-black-box-certifiability (b). Obstacle. The question needs a lower
  bound for learning decision trees of depth q_E over C outputs, which the oracle model does not
  supply.
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 3 of the builder's register
  after round 10
weight: side
status: partial
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 3
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 3. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.
  - 2026-10-25 open to partial. thm-shadow-run-price-finite-views (f) settles it when the query set has as many points as the
    query budget, with order C^q_E / a^2 Train calls necessary and sufficient under the bottom oracle. The factor
    ln|U| for larger query sets stays open. From the space statistical-limits.

## prob-multi-round-drawn-seeds
statement: In the clipped aggregation procedure over R rounds, with no deviation and a finite clip,
  is there a drawn-seed certifier of the hockey-stick divergence for the protocol's strategy that
  is uniformly accurate over all learning functions, with Train calls fixed by R, the ratio of clip
  to noise, the accuracy and alpha, and free of d? Known. Yes for one round, by
  thm-dataflow-composition (e)(iii). The problem concerns only the bottom experimenter.
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 4 of the builder's register
  after round 10
weight: side
status: open
literature: unchecked
tried: Over R adaptive rounds the release law is a mixture over trajectories, and importance
  weights over trajectories have variance of order e^(R B^2/sigma^2), by a heuristic count.
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 4
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 4. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it. The register gives it low priority.

## prob-price-at-fixed-ratio
statement: Hold the ratio a of the transfer exponent to d fixed and let the exponent grow, with the
  logarithm of the rounds small against it. Do the logarithm of the least certification cost and
  the logarithm of the largest number of cells that a deviating strategy reaches have the same
  limit per unit of exponent? Known (proven). The least cost is at least a constant times that
  number of cells, and its logarithm per unit of exponent lies between (1 + 2 sqrt(a))^(-2) and
  one. By Shannon's coding theorem the second limit is the capacity per unit of exponent of the
  channel from the coalition's inputs to the final model with the releases fed back (heuristic).
  Obstacle. The transfer pays the whole Rényi moment of the path, while the needles pay only for
  the cells that one decoder separates.
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 5 of the builder's register
  after round 10
weight: side
status: open
literature: unchecked
tried: The capacity without feedback, ln(1 + 2a)/(2a), is not the second limit (heuristic). Codes
  with feedback beat it at every ratio computed, about 0.60 against 0.275 at a = 4 and 0.93 against
  0.55 at a = 1 (`HE-ML:sink/2026-10-16-formal-tuning/round-05/challenger.md`,
  `HE-ML:sink/2026-10-16-formal-tuning/round-06/builder.md`).
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 5
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 5. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-threshold-ckks-realizes-releases
statement: (i) Does threshold CKKS with Gaussian smudging realize the ideal releases of
  thm-dataflow-composition (a) against a coalition that follows the protocol, under RLWE, with an
  error negligible in the security parameter? (ii) Does it realize them, with an abort set,
  against a deviating coalition when it has six additions? The additions are a trusted key setup,
  proofs of plaintext knowledge for the inputs, a broadcast of the input ciphertexts and the
  decryption shares, honest decryptors that recompute the aggregate and decrypt only it once per
  round, proofs of correct partial decryption, and agreement of the honest parties on the
  delivered value. Obstacle. Part (i) needs a simulator for partial decryptions with smudging that
  survives the key-recovery attacks of Li and Micciancio. Part (ii) also needs proofs of correct
  partial decryption for CKKS. prob-he-oft-smudging-simulation-security and
  prob-hlss25-smudging-simulation-security ask the smudging question of HE-OFT and of HLSS25.
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 6 of the builder's register
  after round 10
weight: side
status: open
literature: the round-03 search on active security for threshold FHE decryption, which found it
  only for thresholdized BFV, BGV and FHEW and none for CKKS
  (`HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 6)
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 6
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 6. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-replay-audit-tolerance-gap
statement: Fix hardware randomness, a learning function, a closed target set and a number q of
  random-oracle queries. Does some prover with q queries always pass the replay audit into the
  target with probability at least a universal constant times the smaller of one and q times the
  reach of the target at tolerance tau? Known. Yes under deterministic kernels, with the constant
  one minus 1/e. Obstacle. An attack that beats the threshold tau/2 must predict where the
  auditor's replay lands, which depends on the joint law of run and replay near the target beyond
  the joint reach.
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 7 of the builder's register
  after round 10
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 7
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 7. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-seed-maps-exact-coupling
statement: (i) Under deterministic kernels, with a deterministic channel and atomless view laws,
  does some seed map make the coupling of thm-coupling-certificate (c)(ii) exact, so that the
  infimum over measure-preserving seed maps of the chance that the two coupled views differ equals
  the total variation between the view laws? (ii) Is there a certifier with explicit seeds that is
  uniformly accurate for that total variation over all learning functions with deterministic
  kernels and atomless view laws, with Train calls fixed by the accuracy and alpha? The round-03
  challenger expects no for (ii), by a needle argument (heuristic).
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 8 of the builder's register
  after round 10
weight: side
status: open
literature: unchecked
tried: The finite construction glues measure isomorphisms between the level sets of a finite view,
  and it does not extend to a continuum of level sets.
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 8
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 8. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-impossibilities-on-finite-seeds
statement: Five impossibilities are proven with an atomless seed, in lem-atomless-two-point,
  thm-dataflow-composition (e), thm-record-level-certificate (e), thm-smoothed-choice-certificate
  (e) and thm-bounded-deviation-transfer (e). Does each hold on a seed space of finitely many bits,
  with an additive term that tends to zero as the bit count grows at a fixed number of calls? Only
  thm-reference-access (c) is proven on finite-bit seeds. Obstacle. Each conditional law must be
  approximated on the finite seed space, with an error that depends on how the partitions of the
  proofs meet the prefixes of the seed.
posed: the formal tuning of 2026-10-16 to 2026-10-17, open problem 9 of the builder's register
  after round 10
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, item 9
history:
  - 2026-10-25 entered from HE-ML digest section 5.1 item 9. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-he-oft-label-queries-against-head
statement: In HE-OFT, do the coalition's label queries reach what the shared head reveals, as a
  collapse or a separation at the distinguish goal? HE-OFT proves that the label view is no
  stronger than both shared heads in plaintext.
posed: Küpçü, recorded in the adversary interface report of 2026-10-16 and in frame 16 of the
  meeting deck of that day
weight: side
status: open
literature: the positioning search of 2026-10-16 on black-box against white-box membership
  inference, which found the general question occupied by Sablayrolles et al., ICML 2019, and
  Suri, Zhang and Evans, TMLR 2024, with neither note written (`HE-ML:lib/literature/positioning.md`)
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#What this changes`
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 10. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-deviating-server-key-switch-check
statement: Is there a check on what the quorum key-switches, cheaper than recomputing the serving
  circuit, that restores the semi-honest view against a deviating server? No protocol in which
  clients decrypt what the server presents admits a deviating server.
posed: the group's verifiable HE study, recorded in the adversary interface report of 2026-10-16
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#What this changes`
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 11. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-he-oft-count-steering-bound
statement: Can counts and norm bounds proven under encryption, as in ACORN, bound the HE-OFT count
  steering? Nothing ties a client's uploaded per-class counts to its public sample count or its
  data. A client that reports a large count for a class therefore moves that row of the shared
  head as close to its own head displacement as it likes.
posed: the meeting deck of 2026-10-16, frame 16
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#HE-OFT on the interface`,
  and frame 16 of `lib/profs/2026-10-16-meeting/slides.tex`
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 12. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-he-oft-smudging-simulation-security
statement: Does the per-party smudging of HE-OFT's Theorem 1 meet standard simulation security,
  given that Hwang et al. (HHKLS26, ASIACRYPT 2026) prove, as the sweep extracted it, that
  independent per-party smudging fails it?
posed: the meeting deck of 2026-10-16, frames 13 and 15
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/formalizing/sources/2026-10-25-he-ml-digest.md#5.2 Others`, item 13, from frames 13 and 15
  of `lib/profs/2026-10-16-meeting/slides.tex`. Notes `HE-ML:lib/literature/notes/arxiv/KSK26.md`
  and `HE-ML:lib/literature/notes/asiacrypt/HHKLS26.md`.
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 13. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-hlss25-smudging-simulation-security
statement: Does the placed proof against deviating decryptors of Hwang, Lee, Seo and Song (HLSS25,
  CCS 2025), which smudges per party, meet standard simulation security after the result of
  HHKLS26?
posed: the meeting deck of 2026-10-16, frame 13
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:lib/literature/notes/acm-ccs/HLSS25.md`, and frame 13 of
  `lib/profs/2026-10-16-meeting/slides.tex`
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 14. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-interface-beyond-salem-et-al
statement: Does the adversary interface hold a publishable contribution beyond Salem et al.
  (SCEKPSTZ23, IEEE S&P 2023), in the protocol graph, the channels, the choices and the steer
  goal? Salem et al. own the distinguish and invert half for one trained model, and their Section
  VI-D states that their games do not cover federated learning.
posed: the meeting deck of 2026-10-16, frame 16
weight: side
status: open
literature: the positioning search of 2026-10-16 on one game framework for inference risks, and
  the full reading of SCEKPSTZ23 on 2026-10-16 (`HE-ML:lib/literature/positioning.md`,
  `HE-ML:lib/literature/notes/ieee-sp/SCEKPSTZ23.md`)
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:lib/literature/notes/ieee-sp/SCEKPSTZ23.md`, and frame 16 of
  `lib/profs/2026-10-16-meeting/slides.tex`
history:
  - 2026-10-16 Salem et al. read in full, which places the distinguish and invert half for one model with them (HE-ML digest, section 6).
  - 2026-10-25 entered from HE-ML digest section 5.2 item 15. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-top-venue-rule-stands
statement: Does the rule of eleven top venues stand, given that it leaves out Suri, Zhang and
  Evans (TMLR 2024) and Wainakh et al. (Sensors 2023)? The watch list of EuroS&P, SaTML and CSF
  was never screened.
posed: the meeting deck of 2026-10-16, frame 16
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/formalizing/sources/2026-10-25-he-ml-digest.md#5.2 Others`, item 16, from frame 16 of
  `lib/profs/2026-10-16-meeting/slides.tex`. The rule is in `HE-ML:CONTEXT.md`.
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 16. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-coupled-reruns-rarely-differ
statement: For a transformer trained with a shared seed, do coupled reruns rarely differ by more
  than the threshold, so that the coupled certificates of the learning-oracle theory are useful?
  The theory measures nothing, and fidelity of hardware randomness is heuristic on GPUs.
posed: the challenger's audit of 2026-10-17, section Assessment
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/final/audit.md#Assessment`
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 17. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.
  - 2026-10-25 Literature added: JYCDTCP21 Table I (fact-rerun-reproduction-error) and SAB24 §6
    (fact-controlled-nondeterminism-exact-replication). The hardware part is settled for the tested models and GPU
    types by deterministic settings or logged rounding. The data part, the exceedance of a leave-one-out twin under
    deterministic kernels, stays open, and thm-exact-twin-price and thm-coupling-free-soundness make the price of a
    certificate depend on it.

## prob-learning-oracle-theory-novelty
statement: Does the learning-oracle theory survive a reading of the privacy-auditing literature
  (Jagielski et al., NeurIPS 2020, Steinke et al., NeurIPS 2023) and of oracle-efficient learning,
  shadow models and datamodels (Agarwal et al., ICML 2014, Carlini et al., IEEE S&P 2022, Ilyas et
  al., ICML 2022)? None of these papers is read. FORMAL_SECURITY asks the matching question of
  training as an oracle in prob-training-as-oracle-prior-art.
posed: the final document of 2026-10-17, section Prior work, and the boundary of the
  learning-oracle definition report of 2026-10-16
weight: side
status: open
literature: unchecked. The HE-ML digest names the privacy-auditing search and the three searches of
  the oracle report's boundary and records them as not run.
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Prior work`
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 18. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-oracle-report-open-choices
statement: Five modelling choices of the first learning-oracle definition are open. (i) Is the
  cost unit one per call rather than proportional to the dataset size? (ii) Is a learning node one
  optimizer step rather than one training run? (iii) Can cluster training be made deterministic,
  as consistency requires? (iv) Should a public pretrained model be an input node with its own bank
  entry? (v) May adaptive adversaries wait for an asynchronous bank?
posed: the learning-oracle definition report of 2026-10-16, section Next
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:lib/reports/src/2026-10-16-halil-learning-oracle-definition.tex#Next`
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 23. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it. The final theory counts Train calls at one each (digest section 4), and the digest does not record this as settling (i).

## prob-sweep-recall-and-row-accuracy
statement: (i) Does the venue screen of 2026-10-16 miss papers it should keep at a measurable rate?
  (ii) Do the ledger rows match their papers? Recall is unmeasured, since only near misses left a
  record. Every row comes from one language-model coder, except the HE-OFT and SCEKPSTZ23 rows,
  which come from full readings.
posed: the swept-papers report of 2026-10-16, its boundary
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:lib/reports/src/2026-10-16-halil-swept-papers-and-threat-models.tex#Result`, its
  boundary, with `HE-ML:lib/literature/screening.csv` and `HE-ML:lib/literature/ledger.csv`
history:
  - 2026-10-25 entered from HE-ML digest section 5.2 item 24. Weight side, judged against Halil's direction of 2026-10-25 (digest section 7), which does not need it.

## prob-constrained-fiber-navigation-hardness
statement: Is there a hardness theorem for constrained fiber navigation, so that no efficient
  adversary finds a dataset in the fiber of the training map that agrees with given side
  information? The fiber at a model is the set of datasets that train to it.
posed: FORMAL_SECURITY game-family note, sections 4 and 5, which calls it the best-defined target
  of its session, with proposals dated 2026-07-26
weight: side
status: open
literature: unchecked
tried: The fiber-navigability framing was refuted at its core on 2026-07-26 by Dinur and Nissim,
  PODS 2003 (`FS:exp/docs/notes/fibers-of-the-training-map.md`). Kaplan, Mansour, Nissim and
  Stemmer restate that separation as computational against statistical memorization.
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/game-family-and-reduction-targets.md#4`
history:
  - 2026-07-26 framing refuted at its core by Dinur and Nissim (FS programme digest, section 3.2).
  - 2026-08-22 the refutation flagged for re-examination (FS programme digest, sections 3.2 and 4.5).
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-single-index-gaussian-fiber
statement: Can a point of the single-index Gaussian fiber of the training map be found from the
  weights and bounded side information?
posed: FORMAL_SECURITY fibers note, section 8
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/fibers-of-the-training-map.md#8`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-g2-linear-lattice-attack
statement: On the smallest noiseless G2-linear instance, does a lattice attack such as LLL recover
  the training inputs from the gradients? G2 is training inference from gradients at a fixed
  parameter, and its linear case is an affine condition plus a box, hence a lattice or hidden
  subset sum problem. A yes breaks the conjecture of Suliman et al. (arXiv 2411.05658) for exact
  gradient matching, and a no locates its boundary. The note predicts that LLL wins and that the
  conjecture holds only once noise, quantization or step compounding enters.
posed: FORMAL_SECURITY game-family note, section 5, as the first experiment named
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/game-family-and-reduction-targets.md#5`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.2 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-attacker-estimation-threshold
statement: What is the estimation threshold of a single-index Gaussian model, the sample count that
  an attacker who must recover a value faces, as opposed to the detection threshold that the known
  results measure? Damian, Pillaud-Vivien, Lee and Bruna (Remark 3.3) state that their Theorem 3.2
  primarily measures detection, flag a known gap where SQ estimation needs about d^(k*/2 + 1)
  samples, and leave the estimation threshold open.
posed: FORMAL_SECURITY root `CLAUDE.md`, recorded 2026-08-20
weight: side
status: open
literature: the FORMAL_SECURITY root record of 2026-08-20 from Damian, Pillaud-Vivien, Lee and
  Bruna, Remark 3.3, in `FS:CLAUDE.md#Established negative results`
tried: none
depends-on: none
claimed-by: none
where: `FS:CLAUDE.md#Established negative results`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.4 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it. prob-statistical-queries-for-regression meets the same gap for inversion.

## prob-support-recovery-from-trained-network
statement: Does support recovery from a trained network reduce to support recovery from samples,
  starting with a ridge release? This is step 5 of the sparse-support case study, over a natural
  sparse Gaussian regression source. The case study assumes the stat-comp gap for support recovery
  on three bodies of evidence, none unconditional, and states the budget in samples as a modelling
  decision.
posed: FORMAL_SECURITY case study of sparse support recovery, sections 13 and 16, with the report
  of 2026-08-05 on R selecting the problem
weight: side
status: open
literature: unchecked. The case study records its novelty as unchecked.
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/case-study-sparse-support-recovery.md#16`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.1 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-security-profile-curve
statement: What is the largest tolerance eta that an efficient adversary reaches against a model of
  test error at most epsilon, as a function of epsilon? The R-as-quantizer report names this curve
  as the object to prove.
posed: FORMAL_SECURITY R-as-quantizer report, 2026-08-05
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.1 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.
  - 2026-10-25 prop-profile-run-coordinate (a) shows the run axis flat for unrestricted classes at a fixed learning
    function, so the curve needs a named family, a uniform statement over learning functions, or a computational
    bound. Recorded from the space oracle-and-measurement.
  - 2026-10-25 def-uniform-security-profile gives the unbounded-adversary form. The efficient form stays with the space
    computational-limits.

## prob-pancake-property-inference-reduction
statement: Does property inference against a model trained on Gaussian pancakes reduce to
  distinguishing pancakes from the standard Gaussian, with the tolerance, the spacing and the
  budgets unchanged? Three parts are open. The projection-and-test tolerance is unchecked, the
  search-to-decision direction is unchecked, and the third case of the defender's trichotomy,
  accurate without exact recovery, is open.
posed: FORMAL_SECURITY R-as-quantizer report, 2026-08-05
weight: side
status: open
literature: unchecked
tried: The reduction was corrected to an illustration of tightness only, because the planted
  source voids the guardrail on R (FS programme digest, section 3.1).
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.1 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-phi-function-open-conditions
statement: Is the function Phi(P, A, b) well posed? It is the least threshold at which some
  algorithm of class A at budget b makes the searching party P win the criterion R_theta above its
  baseline. Four parts are open. (i) For which criteria is the family R_theta monotone in theta, as
  Phi requires? (ii) Is Phi non-vacuous at the threshold parameter? Every parameterized integrity
  notion in cryptography restricts the move class because an impossibility forces it, so
  non-vacuity must be established and cannot be inherited. (iii) What does Phi read as for
  availability? (iv) How does Phi treat suppression, which has no confidentiality dual in Clarkson
  and Schneider, IEEE CSF 2010?
posed: FORMAL_SECURITY reports of 2026-08-05 on Phi and on its prior art
weight: side
status: open
literature: the two prior-art sweeps of 2026-08-05, thirty-four searches and twenty-eight primary
  sources (`FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`)
tried: The claim that one function unifies the PI's two requested functions was withdrawn the same
  day against Clarkson and Schneider. The name leakage function is banned.
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-unfiled-leakage-and-integrity-functions.md`, and
  `FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.1, 4.9 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-phi-relation-to-g-leakage
statement: Is Phi a case of g-leakage, or does it differ from it? Two differences are expected, a
  threshold scanned over a family and an adversary class at a budget. R with a codomain of zero and
  one is a binary gain function (Alvim, Chatzikokolakis, Palamidessi and Smith, IEEE CSF 2012,
  Definition 3.6).
posed: FORMAL_SECURITY report of 2026-08-05 on Phi, recorded as unresolved
weight: side
status: open
literature: the two prior-art sweeps of 2026-08-05, thirty-four searches and twenty-eight primary
  sources (`FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`)
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-unfiled-leakage-and-integrity-functions.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.1 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-answer-to-bellare-sahai
statement: Does a definition built on a fixed criterion R with a varying budget escape the
  elimination of Bellare and Sahai, CRYPTO 1999, who reduce non-malleability over polynomial-time
  relations to indistinguishability under parallel chosen-ciphertext attack? The programme's
  answer, that a fixed R leaves no such trade, is a conjecture.
posed: FORMAL_SECURITY prior-art report of 2026-08-05
weight: side
status: open
literature: the two prior-art sweeps of 2026-08-05, thirty-four searches and twenty-eight primary
  sources (`FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`)
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.9, 5 and 6. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-four-criteria-exhaustive
statement: Are the four criteria R1 to R4 exhaustive, and does R3 survive a check against the
  defendability of Christiano, Hilton, Lecomte and Xu (CHLX25)? R1 is reconstruction from a noisy
  mean, R2 membership as the zero-tolerance limit, R3 the backdoor criterion of rare-disagreement
  search, and R4 fidelity.
posed: FORMAL_SECURITY concrete-criteria report, 2026-08-05
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-unfiled-concrete-r-criteria.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.1 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-r-parameterized-training-time-definition
statement: Does any definition parameterized by R cover the training-time displacement family?
  Every R-parameterized definition held covers the test-time family. The two training-time
  definitions held, CHLX25 defendability and GKVZ22 undetectable backdoors, are fixed games.
posed: FORMAL_SECURITY three-axis report, 2026-08-05, recorded as the next thing to check
weight: side
status: open
literature: the definitions held in the three-axis report of 2026-08-05
  (`FS:exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md#What this changes`)
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md#What this changes`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.1 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-adversary-class-axis-legitimacy
statement: Is the adversary-class axis a legitimate taxonomy axis under mutual compatibility and
  inner exclusivity? Across about thirty taxonomies none has an adversary-class axis.
posed: FORMAL_SECURITY reports of 2026-08-05
weight: side
status: open
literature: the taxonomy landscape sweep of 2026-08-05, about thirty taxonomies
  (`FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md`)
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/`, the reports of 2026-08-05, of which the digest names no single file
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-attack-surface-axes-independent
statement: Are the three axes of the attack surface, phase of observation, displacement and target
  of R, independent? The three-axis report indexes every named attack by them, does not show
  independence, and leaves some cells empty.
posed: FORMAL_SECURITY three-axis report, 2026-08-05
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md#Result`
history:
  - 2026-10-25 entered from the FS programme digest, section 3.1. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-displacement-families-irreducible
statement: Are the displacement families of training-time adversaries irreducible? The report
  derives that every training-time adversary displaces the learned function, exhaustively over
  displacement targets, and does not show irreducibility. The three-axis report corrected it the
  same day.
posed: FORMAL_SECURITY attack-surface decomposition report, 2026-08-05
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/reports/2026-08-05-unfiled-attack-surface-decomposition.md`
history:
  - 2026-10-25 entered from the FS programme digest, section 3.1. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-comp-mem-reduces-to-hclwe
statement: Does computational membership indistinguishability, COMP-MEM, reduce to hCLWE? The
  related-work file names Gap-Kt over samplable distributions as the native idiom.
posed: FORMAL_SECURITY related-work file, sections 0 and 9
weight: side
status: open
literature: the related-work file records the reduction as appearing open in its membership
  version, after engaging traitor tracing and the DP-hardness corpus
  (`FS:exp/literature/related-work.md#9`)
tried: The marginal-advantage form of COMP-MEM is a no-op, since its baseline is one half by
  construction, and Yeom et al., CSF 2018, already publish it. A bit-valued success functional
  makes baseline subtraction a no-op, so training-world indistinguishability fails for membership
  (`FS:exp/docs/notes/game-family-and-reduction-targets.md#1`).
depends-on: none
claimed-by: none
where: `FS:exp/literature/related-work.md#9`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-ratio-parameterized-privacy-notion
statement: Is there a privacy notion parameterized by the fine-grained ratio between attacker and
  honest work, written as an exponent delta with attacker work at least honest work to the power
  1 + delta?
posed: FORMAL_SECURITY root `CLAUDE.md`, two seams, 2026-07-26
weight: side
status: open
literature: the FORMAL_SECURITY root record of 2026-07-26 that no ratio-parameterized privacy notion
  exists (`FS:CLAUDE.md#Established negative results`)
tried: none
depends-on: none
claimed-by: none
where: `FS:CLAUDE.md#Established negative results`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.6 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-delta-indexed-proof-of-learning
statement: Is there a family of proof-of-learning notions indexed by the exponent delta?
  Proof-of-learning states that the attacker's expected cost is at least the trainer's as a bare
  inequality. Later work indexes the ratio by a constant or by efficiency and hardness parameters,
  and no work indexes it by an exponent.
posed: FORMAL_SECURITY root `CLAUDE.md`, two seams, 2026-07-26
weight: side
status: open
literature: the FORMAL_SECURITY root record of 2026-07-26 on the two seams
  (`FS:CLAUDE.md#Established negative results`)
tried: none
depends-on: none
claimed-by: none
where: `FS:CLAUDE.md#Established negative results`, and
  `FS:exp/survey/paper/parked/formalization/games.tex#What is already occupied`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.6 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-model-extraction-success-definition
statement: Is there a formal success definition for model extraction? arXiv 2310.01959 states from
  inside the field that none exists, and Shafran et al., TMLR 2024, state the same for
  accuracy-driven extraction. The parked extraction games define an extraction advantage with a
  model-free baseline, which the FS programme digest does not record as closing this target.
posed: FORMAL_SECURITY root `CLAUDE.md`, two seams, 2026-07-26
weight: side
status: open
literature: the FORMAL_SECURITY root record of 2026-07-26 on the two seams, and the occupied-ground
  section of the parked extraction games
  (`FS:exp/survey/paper/parked/formalization/games.tex#What is already occupied`)
tried: none
depends-on: none
claimed-by: none
where: `FS:CLAUDE.md#Established negative results`, and
  `FS:exp/survey/paper/parked/formalization/games.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.6 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-filter-compute-ratio-fine-grained
statement: Can the ratio between the compute of the auditor and of the model in Ball et al., arXiv
  2507.07341, Theorem 1, be a fine-grained gap at an explicit exponent? Theorem 1 needs the filter
  to run no faster than the model it audits, a ratio between two parties' compute left as a side
  condition.
posed: FORMAL_SECURITY survey spine report, 2026-08-20
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/reports/archive/2026-08-20-halil-lit-survey-spine.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.12 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-cdp-sdp-separation-natural-task
statement: Is there a separation of computational and statistical differential privacy on a
  natural task? Bun, Chen and Vadhan, TCC 2016-B, separate infeasibly. Ghazi, Ilango, Kamath,
  Kumar and Manurangsi, FOCS 2023, separate against unbounded mechanisms under NIWI, laconic
  keyless CRHF and diO, on a contrived task, and their separation breaks against quasi-polynomial
  adversaries.
posed: FORMAL_SECURITY root `CLAUDE.md`, recorded 2026-08-20
weight: side
status: open
literature: the FORMAL_SECURITY root record of 2026-08-20 on the single-curator separation
  (`FS:CLAUDE.md#Established negative results`)
tried: none
depends-on: none
claimed-by: none
where: `FS:CLAUDE.md#Established negative results`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.3 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-cdp-for-reconstruction-from-weights
statement: Can computational or statistical differential privacy be applied to reconstruction of
  training data from the weights?
posed: FORMAL_SECURITY root `CLAUDE.md`, with the audit of 2026-08-22
weight: side
status: open
literature: the FORMAL_SECURITY root record, verified negative across the line from Beimel, Nissim
  and Omri to Ghazi et al., FOCS 2023 (`FS:CLAUDE.md#Established negative results`). The
  FORMAL_SECURITY sweep of 2026-10-13 found no computational hardness of membership inference or
  reconstruction under a cryptographic assumption (`FS:exp/survey/lab/results/literature-sweep/`).
tried: none
depends-on: none
claimed-by: none
where: `FS:CLAUDE.md#Established negative results`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-memory-bounded-privacy-adversary
statement: Can a security or privacy definition bound an ML or privacy adversary by memory? Every
  hit so far bounds the learner, the mechanism or the defender. Transformer against RNN learning
  separations exist (arXiv 2503.11272), and only the memory-sample mechanism is unclaimed.
posed: FORMAL_SECURITY root `CLAUDE.md`, recorded as an open slot
weight: side
status: open
literature: the FORMAL_SECURITY root record of an open slot, and the survey count of September
  2026, which finds four memory-bounded adversaries, all in bounded-storage cryptography
  (`FS:CLAUDE.md#Established negative results`). The sweep of 2026-10-13 did not search it.
tried: none
depends-on: none
claimed-by: none
where: `FS:CLAUDE.md#Established negative results`
history:
  - 2026-10-25 entered from the FS programme digest, sections 4.7 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-op1-robust-comp-stat-gap
statement: Is the computational value of the robust-learning game strictly below its statistical
  value? The statistical value is finite exactly when the robust-PAC dimension is finite
  (Montasser, Hanneke and Srebro, 2019), and the question reduces to average-case Gap-Kt.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, message 20, about line 2993, as OP1
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#message 20`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.3 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-op2-trusted-prover-inherence
statement: Does certifying Clean_r need an unbounded prover outside the SQ-floor subclass? A yes
  would show that backdoor-freedom is not self-certifiable. Clean_r holds when no input of
  time-bounded Kolmogorov complexity at most r lets a budget-r judge separate the model's output
  from the source. OP3 was deflated into this problem (prob-op3-composable-provenance).
posed: the Chapter 24 dialogue of FORMAL_SECURITY, message 20, about line 3003, as OP2
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#message 20`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.3 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-smooth-aperture-tradeoff
statement: For compressible natural tasks, is there a smooth tradeoff between the advice length and
  the evaluation time of a model? The sharp end of the inference-aperture bound is recorded as
  unconditional. The smooth tradeoff is plausibly as hard as a circuit lower bound.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, message 23, verdict in message 26
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#message 23`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.3 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-comp-stat-envelope-measurement
statement: Does every measured pair of scaling exponents lie under the envelope theta_comp at most
  Phi(theta_data), derived from the keystone? One point above it falsifies the keystone. Here Phi
  is the envelope function, one of four meanings of the symbol in FORMAL_SECURITY.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, messages 24 to 27, recorded as testable and
  unmeasured
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#messages 24 to 27`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.3 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-crown-jewel-threshold
statement: Is there a threshold past which learning reduces to breaking a one-way function, with
  hardness below it statistical?
posed: FORMAL_SECURITY introduction note, section 3, as a target
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/intro-computational-security-of-learning.md#3`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.2 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-shared-randomness-adaptive-adversary
statement: Does the shared-randomness claim survive an adaptive adversary, with a joint pi? The
  claim is that learner randomness is a core resource, and that one noise budget buys privacy on
  the training side and certified robustness on the deployment side.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, message 7, and the introduction note, section 6
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#message 7`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.3 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-detection-band-hardness
statement: What hardness governs the detection band of the tau-staircase? Below tau_stat security
  is unconditional by the SQ floor, and the recovery band is OWF-equivalent. The dialogue leaves the
  detection band open and names Gap-Kt beside it. Phase 3 added an idealized-model rung between
  the SQ floor and OWF, with the caveat of Canetti, Goldreich and Halevi.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, message 5, about line 980, and messages 31 and
  32
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#message 5`
history:
  - 2026-10-25 entered from the FS programme digest, section 3.3. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.
  - 2026-10-26 tried: GKVZ22's sparse-PCA construction fails at its printed parameters (lem-sparse-pca-backdoor-width-price).

## prob-supply-chain-undetectable-backdoor
statement: Under a one-way function, does a backdoor planted in an upstream model in the manner of
  Goldwasser et al. reach a downstream composite, with an effect scaled by the product of inference
  sensitivities, while no bounded downstream auditor below tau_recover detects it? The dialogue
  records this F-4 as a theorem candidate.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, message 15, line 2458
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#message 15`
history:
  - 2026-10-25 entered from the FS programme digest, section 3.3. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-margin-gated-alignment-tax
statement: Does internalizing a predicate raise boundary sensitivity only for small-margin
  predicates? The dialogue records this conjecture as measurable.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, messages 31 and 32
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#messages 31 and 32`
history:
  - 2026-10-25 entered from the FS programme digest, section 3.3. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-intent-authorization-design-law
statement: Does authorization conditioned on inferred intent cost Kt(Pi_intent), so that an agent is
  either intent-blind or intent-elicited? The dialogue records it as a prediction.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, messages 31 and 32
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#messages 31 and 32`
history:
  - 2026-10-25 entered from the FS programme digest, section 3.3. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-acceptable-ai-oracle
statement: Is there a training oracle the author accepts, one that fixes the law of the learned
  function, states a utility condition and supports one proved bound on membership advantage? Two
  parts belong to it, which oracle real training is, and an analogue of the uninstantiability
  result of Canetti, Goldreich and Halevi. The generic training oracle of 2026-10-13 keeps handles
  to parameter vectors, offers train, eval, grad_x, grad_theta and reveal, and leaves Train
  randomized and never opened. HE-ML's learning oracle names seeds instead (FS programme digest,
  section 8).
posed: the FORMAL_SECURITY AI oracle thread, opened 2026-10-13
weight: side
status: open
literature: unchecked
tried: A training oracle that bounds leakage must fix the law of the returned function, and any
  such oracle makes white-box equal black-box, a recorded tension. An arbitrary learner lets
  white-box win trivially, an idealized learner such as Gibbs or the version space gives no gap,
  and for SGD on deep networks any gap is only empirical, a recorded diagnosis
  (`FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`).
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`, and
  `FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.6 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-gradient-access-strict-ordering
statement: Are the access classes {eval, grad_x} and {eval, grad_theta} of the generic training
  oracle strictly ordered?
posed: the FORMAL_SECURITY AI oracle thread, opened 2026-10-13
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-eval-and-train-call-lower-bounds
statement: Are there lower bounds on the eval and train calls that an attacker on the generic
  training oracle needs? Shadow-model attacks add train to the access class. HE-ML asks the
  shadow-model form for its own oracle in prob-shadow-model-lower-bound.
posed: the FORMAL_SECURITY AI oracle thread, opened 2026-10-13
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.
  - 2026-10-25 Related, not a solution: thm-exact-twin-price is a lower bound on Train calls for certifiers, not for
    attackers.

## prob-natural-training-ideal-representation
statement: Does any natural training approximately satisfy ideal representation, under which the
  parameters are independent of the training set given the learned function? An oracle with ideal
  representation would be a virtual black-box obfuscator for trained functions, impossible in
  general by BGIRSVY01. That analogy is heuristic and gives the model random-oracle standing.
posed: the FORMAL_SECURITY AI oracle thread, opened 2026-10-13
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.6 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-version-space-counting-hardness
statement: Is the counting step of the version-space oracle hard for natural hypothesis classes?
  With the trained hypothesis uniform on the version space, computation enters the Bayes-optimal
  attack only through comparing the sizes of the two version spaces. Hardness for rich classes is a
  heuristic expectation.
posed: the FORMAL_SECURITY version-space oracle report, 2026-10-13
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/reports/src/2026-10-13-halil-version-space-oracle.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.6 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-training-as-oracle-prior-art
statement: Has prior work modelled training as an oracle with calls as the resource? HE-ML asks the
  matching question of its own theory in prob-learning-oracle-theory-novelty.
posed: the FORMAL_SECURITY AI oracle thread, opened 2026-10-13
weight: side
status: open
literature: unchecked. This problem is the check.
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-backdoor-game-non-triviality
statement: Is the backdoor game of the parked learning oracle non-trivial? Two parts belong to it,
  where the planter writes and a bound for a model-level auditor. The game has a planter with a
  write budget, an auditor with a read budget and an activator with a secret of min-entropy h. The
  corpus-auditor proposition of the parked oracle prices detection by FGRVX17 Theorem 2.9 for
  planted bipartite k-clique. It covers neither record-level nor model-level auditors, and it
  claims nothing about whether a planter meets non-triviality.
posed: the FORMAL_SECURITY parked formalization, oracle.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/paper/parked/formalization/oracle.tex#The backdoor game`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-game-declaration-content
statement: What must a game's declaration assert about the recipe's outputs, the target family with
  its unit and the data noise, and where does the no-known-shortcut line fall? The parked oracle
  defines the declaration and leaves its content open.
posed: the FORMAL_SECURITY parked formalization, oracle.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/paper/parked/formalization/oracle.tex#The adversary class`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-parked-oracle-uninstantiability
statement: Is the parked learning oracle uninstantiable? The oracle idealizes only the training
  map, returns the full trace and manufactures no hardness, and oracle.tex lists its
  uninstantiability among its opens.
posed: the FORMAL_SECURITY parked formalization, oracle.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/paper/parked/formalization/oracle.tex#What is deferred`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-generation-criterion
statement: What success criterion fits a game whose target is generation? The parked oracle defers
  it.
posed: the FORMAL_SECURITY parked formalization, oracle.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/paper/parked/formalization/oracle.tex#What is deferred`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-classification-case
statement: What do the parked games give in the classification case? The parked oracle defers the
  classification case, and the extraction games list it last among their six opens. The FS
  programme digest does not say whether the two are one problem.
posed: the FORMAL_SECURITY parked formalization, oracle.tex and games.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/paper/parked/formalization/oracle.tex#What is deferred`, and the last section
  of `FS:exp/survey/paper/parked/formalization/games.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-search-to-decision-converse
statement: In the extraction games, does a polynomial-time distinguisher yield a polynomial-time
  search adversary? The forward direction is proven. A search adversary with success p yields a
  distinguisher with advantage |p minus q|/2. The extraction games list this first of their six
  opens, in blocking order.
posed: the FORMAL_SECURITY parked formalization, games.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: the last section of `FS:exp/survey/paper/parked/formalization/games.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-stealing-covering-condition
statement: Under which covering condition does winning the challenge game imply winning Steal_rho?
  The forward direction is proven. Winning Steal_rho under the supremum distance on the challenge
  support wins the challenge game. The extraction games list this second of their six opens, in
  blocking order.
posed: the FORMAL_SECURITY parked formalization, games.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: the last section of `FS:exp/survey/paper/parked/formalization/games.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-relu-symmetry-invariant-readout
statement: Is there a read-out map from weights that is invariant under the symmetries of ReLU
  networks? The extraction games list this third of their six opens, in blocking order.
posed: the FORMAL_SECURITY parked formalization, games.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: the last section of `FS:exp/survey/paper/parked/formalization/games.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-delta-extraction-hardness-instance
statement: Is there an instance of delta-extraction hardness at an explicit delta, reduced to
  average-case k-SUM or Zero-k-Clique? Delta-extraction hardness holds when every adversary with
  cost below k(n) to the power 1 + delta evaluations has negligible extraction advantage. The
  extraction games list this fourth of their six opens, in blocking order.
posed: the FORMAL_SECURITY parked formalization, games.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: the last section of `FS:exp/survey/paper/parked/formalization/games.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-separation-against-jagielski-sq-bound
statement: Is there a separation against the SQ bound of Jagielski et al., USENIX Security 2020,
  Theorem 3, imported from Das et al., under which SQ-expressible fidelity extraction of depth-h
  random networks needs exp(O(h)) samples? The extraction games list this fifth of their six
  opens, in blocking order.
posed: the FORMAL_SECURITY parked formalization, games.tex, 2026-08-22
weight: side
status: open
literature: the occupied-ground section of the parked extraction games, which records Jagielski et
  al. as the priced extraction adversary any novelty claim must face
  (`FS:exp/survey/paper/parked/formalization/games.tex#What is already occupied`)
tried: none
depends-on: none
claimed-by: none
where: the last section of `FS:exp/survey/paper/parked/formalization/games.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5, 4.8 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.
  - 2026-10-26 answered in part by thm-extraction-exponent-price: an SQ extraction bound for a trained single-index predictor
    priced in the trainer's records, the comparison JCBKP20 Theorem 3 does not make.

## prob-compute-pricing-lower-bound
statement: Is there a lower bound over all algorithms that prices compute, so that no algorithm
  obtains a trace's content below the work of the walk? Recipe-level no-skipping is the strongest
  defensible form, and no lower bound over all algorithms exists. Every compute-pricing claim sits
  on this question.
posed: the FORMAL_SECURITY parked formalization, price.tex, 2026-08-28
weight: side
status: open
literature: unchecked
tried: Task-level no-skipping is refuted by recipe drift
  (`FS:exp/survey/paper/parked/formalization/price.tex#The price of skipping`).
depends-on: none
claimed-by: none
where: `FS:exp/survey/paper/parked/formalization/price.tex#The price of skipping`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-sound-proof-of-learning-exists
statement: Does a sound proof-of-learning exist, a view whose price equals the price of the trace?
  Proof-of-learning forgeries (FJTYCDCP23) succeed against the verifier's lossy view of the trace
  without paying the walk, and exact reproduction of a trace remains empirically out of reach
  (SHKBL25).
posed: the FORMAL_SECURITY parked formalization, price.tex, 2026-08-22
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/paper/parked/formalization/price.tex`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 4.11. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-sq-reduction-per-round-observation
statement: Does the SQ-hardness reduction for black-box attacks extend to per-round federated
  observation? The proof note bounds a black-box adversary against a deterministic
  SQ-implementable learner on a planted-clique encoding by the SQ distinguishing advantage, and its
  caveats exclude per-round federated observation. A split-learning or federated attacker observes
  every round.
posed: the FORMAL_SECURITY proof note of 2026-04-23, its caveats
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:.tools/proof.tex#Caveats`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.4 and 8. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it. prob-attacker-lower-bound-from-hard-learning rests its partial status on this proof note.

## prob-sq-reduction-lwe-encodings
statement: Does the SQ-hardness reduction for black-box attacks extend to LWE encodings of the
  training data? The proof note uses the vertex-row encoding of a planted-clique graph and does not
  handle LWE encodings.
posed: the FORMAL_SECURITY proof note of 2026-04-23
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:.tools/proof.tex`
history:
  - 2026-10-25 entered from the FS programme digest, section 3.4. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-gradient-inversion-absent-from-corpus
statement: Should the SoK corpus take in gradient-inversion and split-learning works? It holds
  none, although this is the author's own area.
posed: FORMAL_SECURITY survey issue of 2026-09-17
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-09-17-halil-gradient-inversion-absent-from-corpus.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 5 and 8. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-no-priced-threat-model-template
statement: Does the SoK give a priced threat-model template? The proposed template restates LiRA
  with its adversary class and shadow-model budget named.
posed: FORMAL_SECURITY survey issue of 2026-09-17
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-09-17-halil-no-priced-threat-model-template.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 5 and 8. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-parity-experiment-unused
statement: Do the parked formalization and its sparse-parity run return to the survey? The run sits
  parked and unused (`FS:exp/survey/lab/results/sparse-parity/`).
posed: FORMAL_SECURITY survey issue of 2026-09-17
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-09-17-halil-parity-experiment-unused.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.5 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-section-seven-stands-alone
statement: Section 7 of the SoK stands alone. Does it get tied to the rest of the paper?
posed: FORMAL_SECURITY survey issue of 2026-09-17
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-09-17-halil-section-seven-stands-alone.md`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-single-coder-agreement-unmeasured
statement: Is the agreement of the single coder of the SoK corpus measured? The survey records it as
  a limitation, with 24 of 27 rows in agreement on one overlap.
posed: FORMAL_SECURITY survey issue of 2026-09-17
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-09-17-halil-single-coder-agreement-unmeasured.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.7 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-supplement-has-no-submission-slot
statement: Where do the 19 pages of tables go, given that the call has no submission slot for them?
posed: FORMAL_SECURITY survey issue of 2026-09-17
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-09-17-halil-supplement-has-no-submission-slot.md`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-third-review-round-owed
statement: Has the SoK had the third review round it owes?
posed: FORMAL_SECURITY survey issue of 2026-09-17
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-09-17-halil-third-review-round-owed.md`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-title-and-anonymity-fail-the-call
statement: Do the title, the anonymity and the ethics of the SoK meet the conditions of the IEEE S&P
  2027 call? The issue records that title and anonymity fail them. The deadline of 2026-11-17, with
  abstract registration on 2026-11-10, is flagged as not recorded as fact.
posed: FORMAL_SECURITY survey issue of 2026-09-17
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/survey/lib/issues/2026-09-17-halil-title-and-anonymity-fail-the-call.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 5 and 6. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-availability-as-third-goal
statement: Is availability a third goal beside confidentiality and integrity? The PI's matrix lacks
  availability, and the report on the four generator axes places it on the goal axis.
posed: the FORMAL_SECURITY PI meeting of 2026-08-05
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/meetings/2026-08-05-pi.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 3.1 and 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-llm-and-agentic-scope
statement: Are LLM and agentic systems in the scope of the programme?
posed: the FORMAL_SECURITY PI meeting of 2026-08-05
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/meetings/2026-08-05-pi.md`
history:
  - 2026-10-25 entered from the FS programme digest, section 5. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-programme-venue
statement: Which venue does the programme target? The survey targets the IEEE S&P 2027 SoK track,
  and the programme's paper scaffold has no venue chosen.
posed: the FORMAL_SECURITY PI meeting of 2026-08-05
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/meetings/2026-08-05-pi.md`
history:
  - 2026-10-25 entered from the FS programme digest, sections 5 and 6. Weight side, judged against Halil's direction of 2026-10-25 (HE-ML digest section 7), which does not need it.

## prob-revealed-seed-rerun-price
statement: Under hardware randomness, how many reruns at a revealed seed does an adversary fixed before the learning
  function need to approach the top optimum D^top_1(K)?
posed: argon, round 00 of the space oracle-and-measurement (ch-seed-attack-already-known), 2026-10-25
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md#def-seed-access-modes, remark on the seed for an adversary
history:
  - 2026-10-25 entered from the round-01 summary of oracle-and-measurement. Weight side.

## prob-blind-inversion-relu-clients
statement: Can a seed-blind server invert an expansive Gaussian ReLU client from representations of an isotropic record
  law at polynomial cost, learning the client up to rotation? This is the open upper inclusion of
  conj-seed-price-is-ngca-price.
posed: the space computational-limits, 2026-10-25
weight: supporting
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md#conj-seed-price-is-ngca-price
history:
  - 2026-10-25 entered from the round-02 summary of computational-limits. Weight supporting, since the conjecture of the
    leading candidate needs it.
  - 2026-10-26 restated in sol's quantitative form (round-03 summary of computational-limits): find a polynomial-time map whose
    mean squared reconstruction error, after one common orthogonal alignment, is small relative to the record energy, for
    a frozen expansive Gaussian ReLU client, with stated confidence, expansion, tails and precision. Withdrawn as an aim
    of milestone 2 under Halil's instruction to simplify. prop-relu-client-second-moment-identifies-weights settles the
    Gaussian population case.

## prob-coarse-reconstruction-lattice-hardness
statement: Is reconstruction of a pancake coordinate to constant correlation hard for polynomial-time algorithms under a
  lattice assumption? The reduction of the space reaches only reconstruction to accuracy of order 1/gamma.
posed: the space computational-limits, 2026-10-25
weight: supporting
status: partial
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md#prop-fine-reconstruction-to-hclwe
history:
  - 2026-10-25 entered from the round-00 summary of computational-limits.
  - 2026-10-26 open to partial. thm-coarse-reconstruction-lattice-hard settles it in the exact-arithmetic model M, conditional on
    hCLWE hardness in M. The transfer to Turing machines is prob-finite-precision-blind-reconstruction.

## prob-reconstruction-hardness-without-one-wayness
statement: Does computational Narcissus resiliency for a reconstruction relation, in a trained or initialized model, imply
  a one-way function? The blind first layer resists fine reconstruction under hCLWE while its map has easy preimages, so
  CKMMNST25 Theorem C.5 does not apply.
posed: the space computational-limits, 2026-10-25
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/computational-limits/round-00/summary.md
history:
  - 2026-10-25 entered from the round-00 summary of computational-limits.
  - 2026-10-26 tried: a compressing Gaussian client on uniform integer records gives no computational reconstruction bound,
    since exact reconstruction is already statistically impossible (HE-ML:lab/theory/spaces/hard-problem-mappings/round-00/builder.md, Part 3).

## prob-train-access-collapses-sample-price
statement: In the noisy mean estimator of HSU25 the noise covariance is the population covariance, so Train calls on any
  fixed dataset sample it. Does an attacker with order d Train calls and order min(n, 1/rho^2) reference samples succeed
  where HSU25 Theorem 3.1 forces order n + n^2 rho^2 samples without Train access?
posed: the space statistical-limits, 2026-10-25
weight: supporting
status: partial
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/statistical-limits/round-00/summary.md
history:
  - 2026-10-25 entered from the round-00 summary of statistical-limits. Weight supporting, since it decides whether a sample
    price survives the learning oracle.
  - 2026-10-26 open to partial. Solved in the regime rho = n^-a, 0 < a < 1/2, by thm-train-access-price-frontier: the sample
    price falls from Theta(n^(2-2a)) to Theta(n^(2a)) with Theta(n^(2-2a)) Train calls. For constant rho, sol's round-03
    attack needs no reference sample. Under the hypothesis that the noise is calibrated to the population covariance.

## prob-label-direction-same-units
statement: Compare direction recovery by the trainer and by a split-learning server under one interface and one resource
  class, for single-index labels with generative exponent at least three.
posed: sol's challenges in round 03 of statistical-limits, 2026-10-25
weight: side
status: open
literature: unchecked
tried: prop-label-relevant-attacker-at-most-trainer, refuted in round 04.
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/statistical-limits/round-03/summary.md
history:
  - 2026-10-26 entered from the round-03 summary of statistical-limits.

## prob-relu-blind-inversion-sample-price
statement: What is the sample price of prop-relu-client-second-moment-identifies-weights when the second moment is
  estimated from N representations?
posed: the space statistical-limits, 2026-10-25
weight: supporting
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/statistical-limits/round-03/builder.md#prop-relu-client-second-moment-identifies-weights
history:
  - 2026-10-26 entered from the round-03 summary of statistical-limits. Related to prob-blind-inversion-relu-clients.

## prob-extraction-exponent-fitted-release
statement: Does the extraction separation of thm-extraction-exponent-price survive a fitted network that approximates the
  release only in L^2, and does it hold for polynomial-time extractors under a named assumption?
posed: the space hard-problem-mappings, 2026-10-26
weight: supporting
status: open
literature: search-extraction-generative-exponent
tried: conj-extraction-priced-by-generative-exponent, retracted, since the exact moment cancellations need not survive
  an L^2 approximation.
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/hard-problem-mappings/round-02/summary.md
history:
  - 2026-10-26 entered from the round-02 summary of hard-problem-mappings.

## prob-finite-precision-blind-reconstruction
statement: Do the lattice reductions of computational-limits survive finite-precision representations, so that they bind
  Turing-machine attackers under the standard assumptions (BRST21 Corollary 4.2 for hCLWE, DvW22 for ZLIP)?
posed: the space computational-limits, 2026-10-25
weight: supporting
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/computational-limits/round-05/summary.md
history:
  - 2026-10-26 entered from the round-05 summary of computational-limits. Whether exact-arithmetic results are acceptable for
    now is a decision for Halil.

## prob-zlip-reductions-width-gap
statement: The lower and upper ZLIP reductions of thm-zlip-reductions lose a factor sqrt(d ln(2d+4)/pi) in the width. Can
  one width serve both, for polynomial widths?
posed: the space computational-limits, 2026-10-25
weight: side
status: open
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: HE-ML:lab/theory/spaces/computational-limits/round-05/builder.md#thm-zlip-reductions
history:
  - 2026-10-26 entered from the round-05 summary of computational-limits.

# Archive

## prob-poisson-subsampling-bank-soundness
statement: Does thm-bank-soundness (d) carry over to Poisson subsampling? The builder's register
  names the question and does not restate it.
posed: the formal tuning of 2026-10-16 to 2026-10-17
weight: side
status: withdrawn
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, paragraph Dropped
history:
  - 2026-10-17 recorded as dropped in the builder's register after round 10, because subsampling is a node of the procedure and no theorem of the theory uses it.
  - 2026-10-25 entered into the archive. Weight side, since the question is out of scope.

## prob-active-certification-continuous-choices
statement: Can active strategies be certified when the reachable choices form a continuous set?
  thm-active-choice-dichotomy shows that no number of Train calls suffices for an infinite set of
  distinct choices.
posed: the formal tuning of 2026-10-16 to 2026-10-17
weight: side
status: solved
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, paragraph Dropped
history:
  - 2026-10-17 recorded in the builder's register after round 10 as closed in round 04 by thm-smoothed-choice-certificate.
  - 2026-10-25 entered into the archive. Weight side, since the question is closed.

## prob-price-constant-small-exponent
statement: What is the constant of the certification price while the transfer exponent is small
  against d?
posed: the formal tuning of 2026-10-16 to 2026-10-17
weight: side
status: solved
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems`, paragraph Dropped
history:
  - 2026-10-17 recorded in the builder's register after round 10 as closed in round 05 by thm-bounded-deviation-transfer, whose corollary sets the logarithm of the least cost equal to the exponent to first order.
  - 2026-10-25 entered into the archive. Weight side, since the question is closed.

## prob-op3-composable-provenance
statement: Does provenance of a learned model compose? Process provenance is an NP statement that
  composes by proof-carrying data. Cleanness provenance is coNP and equals OP2.
posed: the Chapter 24 dialogue of FORMAL_SECURITY, message 17, about line 2740, as OP3
weight: side
status: withdrawn
literature: unchecked
tried: none
depends-on: none
claimed-by: none
where: `FS:exp/docs/notes/chapter-24.md#messages 17 to 19`
history:
  - 2026-10-25 entered into the archive from the FS programme digest, section 3.3. The dialogue deflated it into OP2, prob-op2-trusted-prover-inherence, in messages 18 and 19. Weight side, since the problem lives on in OP2.
