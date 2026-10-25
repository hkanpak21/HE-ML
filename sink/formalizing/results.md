# Results register

This file holds every definition, theorem, lemma, proposition, conjecture and construction that the formalizing line states as its own, from HE-ML and from FORMAL_SECURITY. Each entry gives the object in words, the place of its full statement, the entries it uses, its status as its source records it, who checked it, and whether it needs the learning oracle.

# Learning oracle (HE-ML)

## def-learning-oracle
kind: definition
statement: A training input holds a learner name, a starting model, a dataset and a hypothesis class from a finite family. The learning function maps a training input, a seed and hardware randomness to a model, and the seed has an atomless law. A learning oracle stores models and seeds under per-caller integer names, each labelled open or eval. It answers three calls. Train takes a training input and a seed, a seed name, or a request to draw a fresh seed, which it stores under a new name. Eval returns the evaluation map of a stored model at a query, and Open returns a stored object. A grant gives a caller a new name when a procedure or a policy directs it, and a grant is not a call. Fidelity makes every drawn seed, every hardware draw and every evaluation draw independent of all other randomness. Access lets Train and Open run only on names labelled open, and Eval on names labelled eval or open. Label eval gives black-box access to a model and label open white-box access.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Learning oracle, HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Learning oracle
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it. Fidelity of hardware randomness is a modelling assumption, heuristic for GPU training, stated in a remark outside the definition.
checked-by: challenger audit round 10, 2026-10-17, after acceptance in rounds 02 to 09
oracle: n/a
history:
  - 2026-10-16 first stated as Definitions 1 and 2 of HE-ML:lib/reports/src/2026-10-16-halil-learning-oracle-definition.tex.
  - 2026-10-17 the round log records that the round-00 challenger found an eval handle could be laundered into an open one by training on it with an empty dataset (ch-handle-laundering), and that seeds could not be named (ch-seed-naming). Round 01 rebuilt the definition.
  - 2026-10-25 entered from the HE-ML digest, section 3.3.
  - 2026-10-25 overlaps def-passive-learning-oracle of FORMAL_SECURITY, which draws fresh coins on every call and lets no party name a seed, while this oracle lets a caller rerun training at a named seed.
  - 2026-10-25 overlaps def-generic-training-oracle of FORMAL_SECURITY, whose train call returns a fresh handle and whose training randomness is never opened, while this oracle stores, names and opens seeds.
  - 2026-10-25 overlaps def-oracle-access-class of FORMAL_SECURITY. There black-box access is eval alone and white-box access is reveal, and here the labels eval and open play those roles while Train stays open to every caller.
  - 2026-10-25 overlaps def-abstract-learning-machine and def-learner-randomness-budget of FORMAL_SECURITY, which put a uniform seed inside the source and meter learner randomness as an entropy budget, while here the seed is an argument of each Train call with no meter on its entropy.

## def-learning-oracle-model
kind: definition
statement: A procedure is a dataflow graph whose nodes run in a fixed topological order, each with an owner and one of four operations. An input node holds a dataset, a seed or a public object. A learning node calls Train, with a drawn seed unless the procedure feeds it a seed node. An evaluation node calls Eval, and a general node computes a randomized function of its parents with randomness the oracle does not hold. Each node value reaches a coalition through the plain channel, the query channel, which grants an eval name with a query set and an allowance of Eval calls, or channel none. The adversary is an oracle algorithm that reaches the learning function only through the oracle, computes the evaluation map itself and stops with probability one. It is unbounded unless a statement assumes a computational bound. Its choices are the node arguments it sets, the values and learner names of nodes it owns, the learner names of nodes whose training code it supplies, and its queries. A strategy is passive when the choices that enter procedure nodes are the functions of procedure values that the protocol prescribes, and active otherwise. The view is the transcript of channel outputs, call answers and coins. The budget bounds Train calls and Eval calls on eval names, and calls the procedure requires of an owner in the coalition are free. To distinguish, the adversary outputs a bit under one of two hypotheses, with advantage the difference of the two acceptance probabilities. A privacy statement bounds the hockey-stick divergence of order gamma between the two view laws, which is the total variation at gamma one. To steer, the adversary wins when a node's value lies in a target set of models and an acceptance event holds.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Learning-oracle model
uses-to-state: def-learning-oracle
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it. Its remark on inversion is prop-privacy-bound-bounds-inversion.
checked-by: challenger audit round 10, 2026-10-17, after acceptance in rounds 02 to 09
oracle: n/a
history:
  - 2026-10-16 first stated as Definition 2 of the learning-oracle report, with a call budget.
  - 2026-10-17 the round log records that the round-00 challenger found that budget undefined (ch-budget-semantics), and that round 06 replaced an undefined word in the accepted form.
  - 2026-10-25 entered from the HE-ML digest, section 3.3.
  - 2026-10-25 the same graph is the protocol of def-interface-protocol. That interface has five channels and three goals, and this model has three channels and two goals, with a sum, a ciphertext or a noisy value released as a general node through the plain channel.
  - 2026-10-25 overlaps def-view-generic-adversary of FORMAL_SECURITY, which touches training only through granted views within budgets, while this adversary is unbounded and reaches training only through oracle calls.

## def-certifier
kind: definition
statement: An experimenter is a caller outside every procedure that reaches the learning function only through the oracle. A caller works in the drawn-seed discipline when every Train call it makes draws a fresh seed and it opens no seed name, and in the coupled discipline otherwise. A target is a functional of the learning function with values in the unit interval. A certifier is an experimenter that makes at most N Train calls and outputs an upper bound on the target. It is sound at level alpha over a class of learning functions when the bound holds with probability at least one minus alpha at every member of the class. A lower certifier outputs a lower bound with the same guarantee. The main targets are the total variation or the hockey-stick divergence between the view laws that a channel induces from the model laws at two training inputs.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Certifier
uses-to-state: def-learning-oracle
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it. The remark on larger targets is prop-lower-bounds-bind-larger-targets.
checked-by: challenger audit round 10, 2026-10-17, after acceptance in rounds 02 to 09
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3.

## def-degenerate-oracles
kind: definition
statement: Fix a procedure and a coalition, and let a policy direct grants to the coalition beyond those of the procedure. The bottom oracle is the realizable policy, which grants nothing and puts no bound on Train calls, which is what a real training service gives. The top oracle is the seed-revealing policy, which grants the coalition label open on the seed name of every honest learning node when the node runs. For an experimenter, or for an honest party whose Train calls a theorem designs such as an auditor, the bottom and the top case are the drawn-seed and the coupled discipline. A statement about adversaries is tested under both oracles, and a statement about an experimenter or an auditor under both disciplines.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Degenerate oracles
uses-to-state: def-learning-oracle, def-learning-oracle-model, def-certifier
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17, after acceptance in rounds 02 to 09
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3.

## def-isolated-client
kind: definition
statement: Fix a client j, two candidate datasets, a space of choices, a number R of rounds, a dimension d and a noise scale sigma. A procedure isolates client j behind Gaussian releases when four conditions hold. In round t a learning node owned by j trains, with a drawn seed, on a training input formed from a choice, the dataset and the previous state, and the choice is read from neither the dataset nor the previous state. No other node reads the dataset, and each round's model goes only to that round's release node and the next learning node. The release node outputs a coalition contribution plus a release map of the choice and the model plus fresh Gaussian noise of scale sigma in dimension d. The coalition owns none of these nodes and sees the dataset node and the learning nodes through channel none. The client is stateless when its training input ignores the previous state, and the procedure may stop after a release on a value the coalition sets. The coupled execution also trains, in every round that runs, a twin on the other candidate dataset under the same seed with fresh hardware randomness, and no node reads a twin. The exceedance is the largest release difference between run and twin over the rounds that run, and the exceedance probability at a threshold is the probability that the exceedance passes it. The coupled tail is the one-round probability of the same event at given states.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Isolated client
uses-to-state: def-learning-oracle, def-learning-oracle-model
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17, after acceptance in rounds 04 to 09
oracle: n/a
history:
  - 2026-10-17 the round log records that round 03 found an earlier form leaked the dataset node by a counterexample, round 04 fixed it, round 07 made the source of the choice explicit in condition 1, and round 09 stated the protocol's stop for a passive strategy.
  - 2026-10-17 audit finding ch-dataset-node-before-use says the definition uses the dataset before it introduces it. The one-clause fix is not applied.
  - 2026-10-25 entered from the HE-ML digest, section 3.3.

## def-model-bank
kind: definition
statement: A design lists training inputs with seeds, each fixed or drawn, and a bank stores one run per entry. Its empirical oracle answers a Train call with the first unused matching entry and refuses a call that no unused entry matches.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Model bank
uses-to-state: def-learning-oracle
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17, after acceptance in rounds 02 to 09
oracle: n/a
history:
  - 2026-10-16 first stated as Definition 3 of the learning-oracle report, with calls outside the design queued as training jobs in an asynchronous experiment.
  - 2026-10-17 the round log records that the round-00 challenger found the report's claim that one random-half bank serves all records holds only for the random-subset game (ch-bank-design-game). thm-bank-soundness states the corrected form.
  - 2026-10-25 entered from the HE-ML digest, section 3.3.

## def-identity-coupling
kind: definition
statement: For two training inputs, the identity coupling is the joint law of the two models trained on them under one seed drawn from the seed law, with independent hardware randomness for each. An experimenter samples it with a Train call that draws a seed and returns its name, followed by a Train call on the other input with that seed name.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Coupling certificate
uses-to-state: def-learning-oracle
uses-to-prove: none
status: proven
evidence: a definition in the setting of thm-coupling-certificate, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3, objects of the theorems.

## def-coupled-divergence
kind: definition
statement: For a channel from models to views and gamma at least one, the coupled divergence is the mean, over pairs drawn from the identity coupling, of the hockey-stick divergence of order gamma between the channel's view laws at the two coupled models.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Coupling certificate
uses-to-state: def-identity-coupling
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it. Step 1 of the proof of thm-coupling-certificate shows its integrand is measurable.
checked-by: challenger audit round 10, 2026-10-17
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3, objects of the theorems.

## def-divergence-probability
kind: definition
statement: The divergence probability is the probability, under the identity coupling, that the two coupled models differ.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Coupling certificate
uses-to-state: def-identity-coupling
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3, objects of the theorems.

## def-top-divergence
kind: definition
statement: For one learning node seen through a channel, the top divergence is the hockey-stick divergence of order gamma between the laws of the pair of seed and view under the two training inputs. It is what the top oracle shows an adversary that sees the node through the channel.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Coupling certificate
uses-to-state: def-degenerate-oracles
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3, objects of the theorems.

## def-bounded-deviation-strategy
kind: definition
statement: Let a procedure isolate client j, and let the coalition own input nodes whose only child is a round's release node, so that their sum enters that round's contribution additively. The protocol prescribes the values of these input nodes as a function of what the coalition holds before the release runs. A strategy is B_A-deviating when it sets every other argument and value as the protocol prescribes, keeps each round's sum within distance B_A of the prescribed sum, and stops, if at all, after a release. Its queries and other oracle calls are unrestricted. The protocol's strategy adds the prescribed values and never stops.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Bounded-deviation transfer
uses-to-state: def-isolated-client
uses-to-prove: none
status: proven
evidence: a definition in the setting of thm-bounded-deviation-transfer, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3, objects of the theorems.
  - 2026-10-25 overlaps def-read-and-write-budgets of FORMAL_SECURITY. The write budget bounds the steps and the metric distance by which a party may deviate at a port, and this strategy bounds only the norm of additive inputs to the releases.

## def-clipped-aggregation-instance
kind: construction
statement: The instance has the real vector space of dimension d as model space, one honest stateless client j, an honest server and one coalition client whose prescribed input is zero, over R rounds. The choice of round t is the round index and its starting model, and each round trains under its own learner name. Each round's release is the coalition input plus the clipped difference between client j's trained model and the starting model plus Gaussian noise, with clip B possibly infinite. The server adds the release to the starting model to form the next one. The target is the larger of the two directed divergences over adversaries with a B_A-deviating strategy.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Bounded-deviation transfer
uses-to-state: def-isolated-client, def-bounded-deviation-strategy
uses-to-prove: none
status: proven
evidence: a construction in the setting of thm-bounded-deviation-transfer, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3, objects of the theorems.

## def-reach-spread-joint-reach
kind: definition
statement: Fix a training input, a metric on models whose closed balls are compact, a closed target set and a tolerance tau. Take two runs at one seed with independent hardware randomness. The reach is the probability that the first run lies within tau of the target set. The spread is the probability that the two runs lie more than tau apart. The joint reach is the probability that the first run lies within tau of the target set and within tau of the second run. Drawn-seed calls measure the reach, and coupled calls with one seed name measure the spread and the joint reach.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Replay-audit steering
uses-to-state: def-learning-oracle
uses-to-prove: none
status: proven
evidence: a definition in the setting of thm-replay-audit-steer, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3, objects of the theorems.

## def-uniformly-accurate-certifier
kind: definition
statement: A certifier is uniformly accurate to an accuracy when, at every learning function of the class, its output lies between the target and the target plus the accuracy with probability at least one minus alpha, at a number of Train calls fixed by the stated parameters alone.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Open problems, HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Open problems
uses-to-state: def-certifier
uses-to-prove: none
status: proven
evidence: a definition that the open problems use, and nothing is claimed beyond it.
checked-by: challenger audit round 10, 2026-10-17
oracle: n/a
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3, objects of the theorems.

## def-non-triviality-bar
kind: definition
statement: A theorem about the learning oracle counts as non-trivial when four conditions hold. The oracle is in it. Removing the oracle leaves a problem that needs the law of the trained model. The bound depends on the learning function only through quantities that oracle calls measure. The statement fails, or becomes vacuous, under one degenerate oracle. When the actor is an experimenter or an auditor, the fourth condition is tested against the drawn-seed discipline.
where: HE-ML:sink/2026-10-16-formal-tuning/README.md#Non-triviality, the acceptance bar for a theorem
uses-to-state: def-degenerate-oracles
uses-to-prove: none
status: proven
evidence: a definition, the acceptance rule that every challenger verdict of the formal tuning applied, and nothing is claimed beyond it.
checked-by: unchecked as a definition. It is the orchestrator's rule, set at Halil's request for non-trivial proofs with the oracle inside.
oracle: n/a
history:
  - 2026-10-16 set in the protocol of the formal tuning.
  - 2026-10-17 the orchestrator ruled after round 02 that the fourth condition runs against the drawn-seed discipline for an experimenter or an auditor.
  - 2026-10-25 entered from the HE-ML digest, section 3.3.

## prop-privacy-bound-bounds-inversion
kind: proposition
statement: An adversary that inverts wins on an event of views. Its success under one hypothesis is at most e to the epsilon times its success under the other, plus the hockey-stick divergence of order e to the epsilon between the two view laws. So every privacy bound of the theory also bounds inversion.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Learning-oracle model
uses-to-state: def-learning-oracle-model
uses-to-prove: none
status: proven
evidence: by the definition of the hockey-stick divergence, in the remarks of def-learning-oracle-model in the final document.
checked-by: challenger audit round 10, 2026-10-17
oracle: holds-without-oracle. It is a fact about the laws of views.
history:
  - 2026-10-17 the round-03 challenger proposed this inequality as the cover for the invert goal, which the definitions dropped.
  - 2026-10-25 entered from the HE-ML digest, section 3.3. It is how the theory reaches def-invert-goal, which it does not define.

## prop-lower-bounds-bind-larger-targets
kind: proposition
statement: A certifier sound for a target that is pointwise at least another target is sound for the smaller one. So each lower bound on certifiers of a target binds certifiers of every larger target.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Certifier
uses-to-state: def-certifier
uses-to-prove: none
status: proven
evidence: the remark of def-certifier in the final document. Soundness for the larger target implies the event that defines soundness for the smaller one.
checked-by: challenger audit round 10, 2026-10-17
oracle: holds-without-oracle. It is an implication between soundness statements that holds in every cost model.
history:
  - 2026-10-25 entered from the HE-ML digest, section 3.3.

## lem-needle-lower-bound
kind: lemma
statement: Fix a target, a level vartheta, a reference learning function and J pairwise disjoint sets of training inputs. Let each needle function agree with the reference function outside its own set and have target at least vartheta. A certifier of the target with at most N Train calls, in either discipline, sound at level alpha over a class that contains the needles, outputs at least vartheta at the reference function with probability at least one minus alpha minus N over J.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Needle lower bound
uses-to-state: def-certifier
uses-to-prove: def-learning-oracle
status: proven
evidence: proof in full in the final document. It couples the runs against the reference and against each needle up to the first Train call inside that needle's set, and a Train call names one training input, so at most N needles are hit.
checked-by: challenger audit round 10, 2026-10-17. The orchestrator re-derived the full proof in the final document (gate G7).
oracle: needs-oracle. It counts Train calls in either discipline.
history:
  - 2026-10-17 the theory register records it accepted from round 03, latest in round 09.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic and assumes deterministic kernels or hardware randomness independent across runs.

## lem-sphere-code
kind: lemma
statement: (a) For every dimension d at least one, the unit sphere holds at least 2 to the power 0.18 d points with pairwise distances at least one. (b) For J points with pairwise distances at least s, the cells of points strictly nearer to one point than to every other are open and pairwise disjoint. A Gaussian perturbation of scale sigma prime moves a point out of its cell with probability at most J minus one times the normal tail at s over twice sigma prime, which is at most J over two times the exponential of minus s squared over eight sigma prime squared.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Sphere code
uses-to-state: none
uses-to-prove: none
status: proven
evidence: proof in full in the final document, by a maximal binary code with Hamming distance at least a quarter of d for (a) and a union bound over half-spaces for (b).
checked-by: challenger audit round 10, 2026-10-17. The orchestrator re-derived the full proof in the final document (gate G7).
oracle: holds-without-oracle. It is geometry.
history:
  - 2026-10-17 the theory register records it proven in round 04, latest accepted in round 09.
  - 2026-10-25 entered from the HE-ML digest, section 4.1.

## lem-atomless-two-point
kind: lemma
statement: A drawn-seed certifier of total variation through a deterministic channel, sound for all learning functions, outputs one with probability at least one minus alpha when the view laws are atomless.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/round-01/builder.md
uses-to-state: def-certifier, def-degenerate-oracles
uses-to-prove: none
status: proven
evidence: proof in round-01/builder.md, corrected in round 02 and round 03. Conditioning the model laws on complementary random halves of a fine partition separates the views, while the law of the drawn-seed draws moves by at most N times 2N minus one over the cell count.
checked-by: challenger audit round 10, 2026-10-17. The proof sits in round files, outside the orchestrator's re-derivation.
oracle: needs-oracle. It is the drawn-seed lower bound behind several theorems.
history:
  - 2026-10-17 the theory register records it accepted from round 03, latest in round 09.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.

## lem-bank-fidelity
kind: lemma
statement: The empirical oracle of a model bank agrees with a learning oracle up to its first refusal.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/round-01/builder.md
uses-to-state: def-model-bank, def-learning-oracle
uses-to-prove: none
status: proven
evidence: proof in round-01/builder.md.
checked-by: challenger audit round 10, 2026-10-17. The proof sits in round files, outside the orchestrator's re-derivation.
oracle: holds-without-oracle. It ties a bank of real runs to the oracle.
history:
  - 2026-10-17 the theory register records it accepted from round 01, latest in round 09.
  - 2026-10-25 entered from the HE-ML digest, section 4.1.

## thm-coupling-certificate
kind: theorem
statement: One learning node trains one of two inputs and its model reaches the view through a channel. (a) Drawn seeds give a lower certifier of the total variation sound for every learning function, and on finite views an upper certifier sound for every learning function. Through a deterministic channel with atomless view laws, no drawn-seed certifier of the total variation sound for every learning function outputs below one with probability above alpha. (b) For every learning function, channel and gamma, the leakage is at most the top divergence, which is at most the coupled divergence, which is at most the divergence probability, and the middle two are equal under deterministic kernels. At gamma one the leakage is the best advantage under the bottom oracle and the top divergence the best under the top oracle, at every budget. When the channel's divergence at two models is computable, the mean over n coupled pairs plus a Hoeffding term is sound for the leakage and for the top divergence over every learning function, at 2n Train calls. For a Gaussian channel the coupled divergence is at most a Gaussian term plus the probability that coupled releases differ by more than a threshold. (c) Some learning function with deterministic kernels has zero leakage and top divergence one through the plain channel. A coupling through a measure-preserving seed map also bounds the leakage, and some seed map makes it exact for total variation under deterministic kernels through a deterministic channel with a finite view.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Coupling certificate
uses-to-state: def-learning-oracle, def-learning-oracle-model, def-certifier, def-degenerate-oracles, def-identity-coupling, def-coupled-divergence, def-divergence-probability, def-top-divergence
uses-to-prove: lem-atomless-two-point
status: proven, except (c)(ii) for atomless views and the search for a seed map by oracle calls, which are open (open problem 8)
evidence: (a)(i), (b) and (c)(i) are proven in full in the final document, (b) by averaging and mixture inequalities for the hockey-stick divergence and Hoeffding's inequality. (a)(ii), (a)(iii) and (c)(ii) are proven in round-01/builder.md with corrections in rounds 02 and 03, and the round-10 clauses are in round-10/builder.md.
checked-by: challenger audit round 10, 2026-10-17, as non-trivial. The orchestrator re-derived the full proofs in the final document (gate G7) and found one conservative constant in (a)(ii).
oracle: needs-oracle for the drawn-seed impossibility (a)(iii) and the gap of one between the bottom and the top oracle (c)(i). The chain of (b) and its certificate hold without the oracle given seed control.
history:
  - 2026-10-17 the theory register records ACCEPT NONTRIVIAL in round 08, REVISE in round 09 (ch-seed-map-channel), and the deterministic channel restored in (c)(ii) and in open problem 8 in round 10.
  - 2026-10-17 audit finding ch-coupling-label-scope says the label calls open a bound of (c)(ii) that holds for every view space. The fix is not applied.
  - 2026-10-17 audit finding ch-closed-form-memory says the closed form of the Gaussian hockey-stick divergence rests on a citation from memory, while a one-line proof exists. The fix is not applied.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic and assumes deterministic kernels or hardware randomness independent across runs.
  - 2026-10-25 relates to prop-interface-does-not-bound-leakage of FORMAL_SECURITY, which holds that an oracle bounding leakage must fix the law of the returned function, while (b) bounds leakage by the coupled divergence, a quantity that Train calls measure for every learning function without fixing its law.

## thm-black-box-certifiability
kind: theorem
statement: One learning node's model reaches the adversary through the query channel, with a finite query set and a finite output space. (o) Under the bottom oracle, every adversary with a given number of Eval calls on the served name has advantage at most the best strategy tree of that depth, whatever its Train calls and also when it knows the learning function. (a) An experimenter that draws n models at each input with drawn seeds and runs every tree once on each model certifies the label-only advantage from both sides for every learning function, with an accuracy set by the output count, the query-set size, the depth, n and alpha. (b) One bottom-oracle adversary with 2n shadow models comes within a stated rate of the label-only optimum for every learning function. (c) With deterministic evaluation and atomless model laws, a drawn-seed procedure that rejects every false claim that the white-box advantage is at most the label-only advantage plus a margin below one, except with probability alpha, accepts that claim with probability at most alpha everywhere. (d) Coupled pairs certify that the white-box advantage is at most the divergence probability.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Black-box certifiability
uses-to-state: def-learning-oracle, def-learning-oracle-model, def-certifier, def-degenerate-oracles, def-divergence-probability
uses-to-prove: thm-coupling-certificate
status: proven, (o) to (d), with a matching lower bound for (b) open (open problem 3)
evidence: (o) and (a) are proven in full in the final document, (o) by representing the adversary's own randomness in advance so that its interaction with the served model is one strategy tree, and (a) by Hoeffding's inequality and a union bound over trees. (b) to (d) are proven in round-01/builder.md and revised in round-02/builder.md.
checked-by: challenger audit round 10, 2026-10-17, as non-trivial. The orchestrator re-derived the full proofs of (o) and (a) in the final document (gate G7).
oracle: needs-oracle for the drawn-seed impossibility (c), and the reduction (o) fails under the top oracle by a digit example. The reduction (o) and the two-sided certificate (a) hold without the oracle.
history:
  - 2026-10-17 the round log records that the round-01 challenger found the first form false as stated through its query universe, and that round 02 gave the statement on a finite query set.
  - 2026-10-17 the theory register records ACCEPT NONTRIVIAL from round 02, latest in round 09.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.
  - 2026-10-25 overlaps prop-ideal-representation-equalizes-white-box of FORMAL_SECURITY, which proves white-box equal to function-only advantage under ideal representation, while this theorem certifies the label-only advantage for every learning function and shows by (c) that drawn seeds never certify such an equality below one.
  - 2026-10-25 overlaps thm-sq-hardness-black-box-attacks of FORMAL_SECURITY. Both bound a black-box adversary whatever its own computation, that one through the learner's statistical-query access on planted clique and (o) through strategy trees on a finite query set.

## thm-dataflow-composition
kind: theorem
statement: Let a procedure isolate client j behind R Gaussian releases. (b) For every adversary under the bottom or the top oracle, with any strategy, with or without a stop, each directed hockey-stick divergence of the view laws is at most a Gaussian term plus the smaller of the exceedance probability in the matching direction and e to the epsilon times the other one. The Gaussian term is the Gaussian divergence at a shift of root R times the threshold over sigma, and per-round thresholds replace that shift by the root of their sum of squares. The exceedance probability is at most the sum over rounds of the coupled tails along the coupled execution. (c) For a fixed strategy, the protocol's for a passive coalition, and a threshold fixed in advance, n independent coupled executions give a Clopper and Pearson upper bound on the exceedance probability, sound for every learning function. Each run costs at most 2R Train calls for client j plus the calls of the other nodes and of the strategy, and the cost is free of d. The certificate holds for every passive adversary. (a) The ciphertexts of an aggregation sub-protocol reduce to the releases up to its realization error. (d) In some one-round procedure, a certifier sound against all active strategies outputs at least one minus eta, for every eta, at some function where that leakage is zero, whatever its Train calls. (e) Over learning functions whose models have norm at most B, a drawn-seed certifier of the one-round divergence pays Train calls exponential in the smaller of d and the squared ratio of B to sigma, while the coupled certificate (c) needs about the logarithm of one over alpha divided by the accuracy.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Dataflow composition
uses-to-state: def-isolated-client, def-learning-oracle-model, def-degenerate-oracles, def-certifier
uses-to-prove: lem-sphere-code
status: proven for (a) given the realization error, (b), (c), (d) and (e). Heuristic, the realization by threshold CKKS and the form of CKKS decryption under a public scalar. Open, the sum channel, the drawn-seed price above d, and a multi-round drawn-seed certifier free of d (open problems 1, 2 and 4).
evidence: (b), (c) and (e)(ii) are proven in full in the final document, (b) by a hybrid that clips the release difference at the threshold and a Gaussian kernel argument, (e)(ii) by a pair code on the sphere. (a) is in round-03/builder.md with round-04 and round-05, (d) in round-03/builder.md, and (e)(i) and (e)(iii) in round-02/builder.md. The heuristic parts assume that threshold CKKS with smudging realizes the ideal releases with negligible error under RLWE (open problem 6), and that decrypting a public scalar times a ciphertext returns that scalar times its message plus an error of bounded norm and any noise the decryptors add.
checked-by: challenger audit round 10, 2026-10-17, as non-trivial. The orchestrator re-derived the full proofs of (b), (c) and (e)(ii) in the final document (gate G7).
oracle: needs-oracle for the drawn-seed price (e) and the impossibility against active strategies (d). The composition bound (b) holds without the oracle, and the certificate (c) holds without it given seed control.
history:
  - 2026-10-17 the theory register records ACCEPT NONTRIVIAL in round 08, REVISE in round 09 (ch-per-round-threshold, ch-scalar-label, ch-estimator-alpha-range), and the round-10 restatement with thresholds per round, the scalar sentences labelled proven given the form of decryption, and (e)(iii) stated for alpha at most one half.
  - 2026-10-17 audit finding ch-reading-eta-range says the Reading of (e)(ii) leaves the range of eta unstated. The fix is not applied.
  - 2026-10-17 audit finding ch-closed-form-memory applies to the Gaussian closed form that (b) uses. The fix is not applied.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic and assumes deterministic kernels or hardware randomness independent across runs.

## thm-bounded-deviation-transfer
kind: theorem
statement: Let a procedure isolate client j, with or without state, under the bottom or the top oracle, and let the exponent e be R minus one times B_A squared over twice sigma squared. (a) For every learning function and every B_A-deviating strategy, the exceedance probability is at most a fixed nondecreasing function of the protocol's own exceedance probability, set by e alone and equal to the identity at B_A zero. With thm-dataflow-composition this bounds both directed divergences over all B_A-deviating adversaries. (b) Coupled runs of the protocol's own execution certify that bound at level alpha for every learning function, at 2R Train calls per run for client j plus those of the other nodes, free of d. When no run exceeds the threshold, a number of runs exponential in the square of root e plus the root of the logarithm of one over the accuracy, times the logarithm of one over alpha, reaches the accuracy. (c) In the clipped aggregation instance no transfer function improves on (a) by more than a factor of order the root of the logarithm of one over the protocol's exceedance probability. (d) In that instance with finite clip, every certifier sound for all learning functions and accurate where the leakage is zero pays Train calls exponential in e, in either discipline, when e is small against d. (e) Drawn-seed certifiers fail there. Corollary. The logarithm of the least number of Train calls of a sound and accurate certifier equals e to first order as e grows with e over d tending to zero and the logarithm of R small against e.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Bounded-deviation transfer
uses-to-state: def-isolated-client, def-bounded-deviation-strategy, def-clipped-aggregation-instance, def-certifier, def-degenerate-oracles
uses-to-prove: thm-dataflow-composition, lem-needle-lower-bound, prop-lower-bounds-bind-larger-targets
status: proven, all parts (a) to (e) and the corollary
evidence: proofs in full in the final document. (a) bounds a Rényi moment of the likelihood ratio between the deviating and the protocol's execution and applies Hölder's inequality. (b) is Clopper and Pearson. (c) is an explicit learning function. (d) builds a random sign code with needles. (e) reuses the pair code of thm-dataflow-composition (e)(ii).
checked-by: challenger audit round 10, 2026-10-17, as non-trivial. The orchestrator re-derived the full proofs in the final document (gate G7).
oracle: needs-oracle for the price (d), the corollary and the drawn-seed failure (e). The transfer (a) holds without the oracle, and the certificate (b) holds without it given seed control.
history:
  - 2026-10-17 the theory register records it split out of thm-smoothed-choice-certificate and proven in round 05, ACCEPT NONTRIVIAL in rounds 05 to 09, (c) restated in round 06 and sharpened in round 07, (e) stated for the divergence of deviating adversaries in round 08, and the transfer function set to one above one in round 09.
  - 2026-10-17 audit finding ch-intro-price-limit says item 4 of the opening names the wrong limit for its little-o term. The fix is not applied.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.

## thm-replay-audit-steer
kind: theorem
statement: A training input is fixed and a commitment binds the prover's dataset. Seeds come from a random oracle applied to the commitment and a nonce. The auditor replays training at that seed and accepts when the prover's model lies within tau of a replay, and the prover wins when its model lies in a closed target set and the auditor accepts. (a) A prover with q random-oracle queries and any number of Train calls, which may know the learning function, wins with probability at most q plus one, times the number of replays, times the reach. (b) The honest prover is accepted except with probability the spread. (c) A grinding prover that trains at fresh nonces wins with probability at least the joint reach over the reach at half the tolerance times the chance that some nonce hits. Under deterministic kernels (a) holds without the factor of replays, and grinding matches it within a factor 3.2 when the reach times the query count is at most one. (d) On the circle, rotations make the replay auditor complete and sound for point targets, while a drawn-seed auditor complete up to lambda prime against all of them accepts some fixed point with probability at least one minus lambda prime minus lambda, for every lambda above zero. (e) Provers that cannot see the seed table pay in Train calls at the committed input.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Replay-audit steering
uses-to-state: def-learning-oracle, def-reach-spread-joint-reach, def-degenerate-oracles
uses-to-prove: none
status: proven, (a) to (e), with the gap between the tolerance and half of it under hardware randomness open (open problem 7)
evidence: (a) and (b) are proven in full in the final document, (a) by lazy sampling of the random oracle and a union bound. (c) to (e) are in round-02/builder.md, with the match under deterministic kernels in round-03/builder.md and the notation of (e) in round-04/builder.md.
checked-by: challenger audit round 10, 2026-10-17, as non-trivial. The orchestrator re-derived the full proofs of (a) and (b) in the final document (gate G7).
oracle: needs-oracle for the drawn-seed auditor impossibility (d). Soundness and completeness hold without the oracle given seed control for the auditor's replay, plus the random oracle, without which soundness fails. Under the rule of 2026-10-25 the random oracle that derives the seed is a cryptographic plug-in of the kind that does not count, a heuristic reading of that rule.
history:
  - 2026-10-17 the theory register records ACCEPT NONTRIVIAL from round 02, latest in round 09.
  - 2026-10-17 audit finding ch-scalar-symbol-reuse says the symbol a is reused in (d). The fix is not applied.
  - 2026-10-17 audit finding ch-replay-completeness-term says complete up to lambda prime is undefined. The fix is not applied.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.
  - 2026-10-25 relates to def-view-price-versus-trace-price of FORMAL_SECURITY, which reads a sound proof-of-learning as a view whose price equals the trace's, while this theorem bounds steering under a replay at a random-oracle seed by the reach.

## thm-perfect-substitution
kind: theorem
statement: Against an adversary that samples the learning function once per Train call, the real procedure, which computes training and evaluation directly with fresh randomness, gives the bottom oracle's joint law of honest values and transcript. So every bound proven under the bottom oracle holds for the real procedure.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/round-01/builder.md, HE-ML:sink/2026-10-16-formal-tuning/round-02/builder.md
uses-to-state: def-learning-oracle-model, def-degenerate-oracles
uses-to-prove: none
status: proven
evidence: proof in round-01/builder.md with round-02/builder.md.
checked-by: challenger audit round 10, 2026-10-17. The proof sits in round files, outside the orchestrator's re-derivation.
oracle: holds-without-oracle. It is the bridge that makes the bottom oracle realizable.
history:
  - 2026-10-16 first stated as Proposition 1 of the learning-oracle report, for every policy.
  - 2026-10-17 the round log records that the round-00 challenger refuted that form by two counterexamples (ch-substitution-policy). It holds for the realizable policy alone, which is this statement.
  - 2026-10-17 the theory register records it accepted from round 02, latest in round 09.
  - 2026-10-25 entered from the HE-ML digest, section 4.1.
  - 2026-10-25 relates to prop-locating-a-real-attack of FORMAL_SECURITY, which says a deployed attack that beats a floor reveals a view delivered below its modelled price, while this theorem shows the real procedure delivers exactly the bottom oracle's law.

## thm-reference-access
kind: theorem
statement: On one learning node seen through a deterministic channel, the top oracle's best advantage is the coupled divergence under deterministic kernels. Under the bottom oracle, attacks reach the total variation at a plug-in rate on finite views, and no rate uniform over learning functions exists on atomless views, explicit seeds included. The last part also holds on seed spaces of finitely many bits.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/round-01/builder.md, HE-ML:sink/2026-10-16-formal-tuning/round-02/builder.md
uses-to-state: def-degenerate-oracles, def-coupled-divergence
uses-to-prove: none
status: proven, (a) to (c)
evidence: proofs in round-01/builder.md and round-02/builder.md.
checked-by: challenger audit round 10, 2026-10-17. The proof sits in round files, outside the orchestrator's re-derivation.
oracle: needs-oracle. It is the separation between named and hidden seeds on one node.
history:
  - 2026-10-16 replaces Proposition 2 of the learning-oracle report.
  - 2026-10-17 the round log records that the round-00 challenger found Proposition 2(a) inexpressible, since seeds passed by value and the oracle never revealed a seed it drew (ch-seed-naming), and its advantage to be the probability that the two models differ, not one (ch-reference-advantage-one).
  - 2026-10-17 the theory register records it accepted from round 02, latest in round 09.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.
  - 2026-10-25 Halil named the separation between named and hidden seeds as the oracle's theoretical value, and this theorem states that separation on one node.

## thm-bank-soundness
kind: theorem
statement: (a) A bank trained on random halves of a pool estimates the random-subset membership game for all records at once, for a finite set of tests fixed before the bank is built. (b) That game can differ by one from the fixed-dataset game. (c) A part on shadow models in the random-subset game. (d) Certifying every record of a fixed dataset through a Gaussian release has a lower bound on total Train calls.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md#Register
uses-to-state: def-model-bank, def-certifier
uses-to-prove: none
status: proven for (a), (b) and the first half of (d). Heuristic, (c). The second half of (d) was withdrawn as out of scope.
evidence: proofs in round-01/builder.md with round-02 to round-05. The heuristic part (c) concerns shadow models in the random-subset game, and its assumption is stated in the round files, not in the final document.
checked-by: challenger audit round 10, 2026-10-17, accepted and not tagged non-trivial. The proofs sit in round files, outside the orchestrator's re-derivation.
oracle: needs-oracle for the lower bound of (d). The estimate (a) holds without the oracle.
history:
  - 2026-10-16 the learning-oracle report claimed that one random-half bank serves all records. The round-00 challenger found this holds only for the random-subset game (ch-bank-design-game).
  - 2026-10-17 the theory register records ACCEPT in round 05, latest in round 09, the Poisson-subsampling question of (d) dropped as out of scope in round 04, and the second half of (d) withdrawn.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.

## thm-active-choice-dichotomy
kind: theorem
statement: Let the coalition pick choices from admissible sets against a client isolated behind Gaussian releases. Against a stateless client the worst exceedance over admissible strategies is attained without adaptivity, while the divergence can grow with adaptivity. Let a certifier be sound for all learning functions and accurate where the leakage is zero, to a fixed level in the open unit interval, at error probabilities summing below one. In some procedure it then needs Train calls linear in the number of distinct admissible choices, or of admissible choice sequences with state, and coupled certificates achieve this up to a logarithmic factor. No number of Train calls suffices for an infinite set of choices.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/round-03/builder.md, HE-ML:sink/2026-10-16-formal-tuning/round-04/builder.md
uses-to-state: def-isolated-client, def-certifier
uses-to-prove: none
status: proven
evidence: proofs in round-03/builder.md and round-04/builder.md, with the round-10 clause in round-10/builder.md.
checked-by: challenger audit round 10, 2026-10-17, as non-trivial. The proofs sit in round files, outside the orchestrator's re-derivation.
oracle: needs-oracle for the lower bound. The achieving coupled certificates hold without the oracle given seed control.
history:
  - 2026-10-17 the theory register records ACCEPT NONTRIVIAL in round 08, REVISE in round 09 (ch-active-choice-conditions), and the two conditions of the corollary restored in round 10.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.

## thm-record-level-certificate
kind: theorem
statement: One shared base of coupled runs certifies the fraction of a fixed dataset's records whose leakage to a passive coalition exceeds a threshold, in both orders, at a cost free of the dataset size and of d. Certifying all records costs Train calls linear in their distinct values up to a logarithmic factor. Records outside the dataset are never certified, and drawn seeds fail.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/round-03/builder.md, HE-ML:sink/2026-10-16-formal-tuning/round-04/builder.md
uses-to-state: def-isolated-client, def-certifier
uses-to-prove: none
status: proven
evidence: proofs in round-03/builder.md with round-04/builder.md.
checked-by: challenger audit round 10, 2026-10-17, as non-trivial. The proofs sit in round files, outside the orchestrator's re-derivation.
oracle: needs-oracle for the failures outside the dataset and under drawn seeds. The certificate holds without the oracle given seed control.
history:
  - 2026-10-17 the theory register records ACCEPT NONTRIVIAL in round 05, latest in round 09.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.

## thm-smoothed-choice-certificate
kind: theorem
statement: In the clipped aggregation instance with finite clip, a covering of smoothed tails on escape balls certifies a coalition client with inputs of norm at most B_A, at a cost exponential in d. Every certifier sound for all learning functions pays a cost exponential in the smaller of d and the exponent of thm-bounded-deviation-transfer, and drawn seeds fail.
where: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md#Further accepted results, HE-ML:sink/2026-10-16-formal-tuning/round-04/builder.md, HE-ML:sink/2026-10-16-formal-tuning/round-05/builder.md
uses-to-state: def-clipped-aggregation-instance, def-bounded-deviation-strategy, def-certifier
uses-to-prove: none
status: proven, with a heuristic comparison that the covering costs less than the certificate of thm-bounded-deviation-transfer only when the exponent exceeds about d times the logarithm of R to the three halves times root d over the accuracy
evidence: proofs in round-04/builder.md with round-05/builder.md. The comparison of the two costs is heuristic and compares their stated orders.
checked-by: challenger audit round 10, 2026-10-17, as non-trivial. The proofs sit in round files, outside the orchestrator's re-derivation.
oracle: needs-oracle for the lower bounds and the drawn-seed failure. The covering certificate holds without the oracle given seed control.
history:
  - 2026-10-17 the theory register records ACCEPT NONTRIVIAL in rounds 04 and 05, latest in round 09, and part (c) moved to thm-bounded-deviation-transfer in round 05.
  - 2026-10-25 entered from the HE-ML digest, section 4.1. Its oracle grade follows the judgement of 2026-10-25, which is heuristic.

## thm-own-data-only
kind: theorem
statement: If the policy names no reference and passes only seeds the adversary drew, an adversary without a budget gains nothing from the oracle.
where: HE-ML:lib/reports/src/2026-10-16-halil-learning-oracle-definition.tex#Three properties
uses-to-state: def-learning-oracle
uses-to-prove: none
status: retracted
evidence: the budget of the report's Definition 2 was undefined, so the statement was either false or vacuous (ch-budget-semantics).
checked-by: round-00 challenger of the formal tuning
oracle: needs-oracle. It is a statement about what the oracle adds to an adversary.
history:
  - 2026-10-16 stated as Proposition 3 of the learning-oracle report and labelled proven there.
  - 2026-10-17 the theory register records it withdrawn in round 01, with its content in thm-perfect-substitution and thm-reference-access (c).
  - 2026-10-25 entered from the HE-ML digest, section 4.1.

## def-seed-access-modes
kind: definition
statement: One learning oracle serves each caller in a named or a drawn seed-access mode, with a return label (open or
  eval), allowed learner names and starting models, a budget per operation, and a cost meter of work and examples per run.
  The bottom and top oracles are named-mode cases, and the drawn mode is the drawn-seed discipline.
where: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md#def-seed-access-modes, and HE-ML:lib/theory/booklet.pdf, chapter The oracle and measurement
uses-to-state: def-learning-oracle, def-learning-oracle-model, def-certifier, def-degenerate-oracles, def-passive-learning-oracle, def-generic-training-oracle
uses-to-prove: none
status: proven
evidence: a definition. Its remark turns lem-needle-lower-bound into a bound in oracle cost.
checked-by: discussant rounds oracle-and-measurement round-01 (astra) and round-02 (argon), 2026-10-25. Not checked by Halil.
oracle: n/a
history:
  - 2026-10-25 accepted in round-02 of the space oracle-and-measurement with BLOCKING 0, merged into the booklet. Answers
    decision 1 of STATE.md as a proposal for Halil.

## prop-drawn-mode-is-fs-oracle
kind: proposition
statement: The passive learning oracle of FS:exp/survey/paper/parked/formalization/oracle.tex and the generic training
  oracle of the 2026-10-13 report are drawn-mode callers of def-seed-access-modes, with the metered cost as the
  two-coordinate meter.
where: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md#prop-drawn-mode-is-fs-oracle
uses-to-state: def-seed-access-modes, def-passive-learning-oracle, def-generic-training-oracle
uses-to-prove: none
status: proven
evidence: by construction, HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md. The integrator checked (a) against def:passive and def:cost of oracle.tex.
checked-by: discussant rounds round-01 (astra) and round-02 (argon) of oracle-and-measurement, 2026-10-25. Not checked by Halil.
oracle: n/a
history:
  - 2026-10-25 accepted in round-02 of oracle-and-measurement with BLOCKING 0, merged into the booklet.

## thm-coupling-free-soundness
kind: theorem
statement: For bottom-oracle targets, every certificate of the learning-oracle theory stays sound under any twin rule with
  the right marginals drawn independently of the release noise, independent drawn runs included. Top-oracle targets need a
  shared seed. The coupled tail itself is certified only under the identity coupling, and both conditions are necessary.
where: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md#thm-coupling-free-soundness
uses-to-state: thm-coupling-certificate, thm-dataflow-composition, def-isolated-client
uses-to-prove: thm-bounded-deviation-transfer
status: proven
evidence: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md, a modification of the proof of thm-dataflow-composition (b), with two counterexamples for (d).
checked-by: astra line by line in round-01 and argon in round-02 of oracle-and-measurement, and the integrator's
  re-derivation against the proof of thm-dataflow-composition (b), 2026-10-25. Not checked by Halil.
oracle: needs-oracle for the identity coupling, holds in the drawn mode for soundness
history:
  - 2026-10-25 accepted in round-02 of oracle-and-measurement with BLOCKING 0, merged into the booklet.

## prop-profile-run-coordinate
kind: proposition
statement: At a fixed learning function the security profile of an unrestricted adversary class is flat in training runs.
  A declared family has a certified lower band from fresh shadow runs per trial, and only coupled runs give an upper band
  through deterministic channels with atomless laws.
where: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md#prop-profile-run-coordinate
uses-to-state: def-security-profile-curve, def-learning-oracle-model
uses-to-prove: thm-coupling-certificate, lem-atomless-two-point
status: proven
evidence: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md. Hoeffding for the band, a measurable simulation for the flatness.
checked-by: discussant round-02 (argon) of oracle-and-measurement and the integrator's re-derivation, 2026-10-25. Not checked by
  Halil.
oracle: needs-oracle for the upper band
history:
  - 2026-10-25 accepted in round-02 of oracle-and-measurement with BLOCKING 0, merged into the booklet. Supersedes
    conj-paired-advantage-price of round-00, withdrawn in round-01.

## thm-exact-twin-price
kind: theorem
statement: A certifier sound over every learning function with deterministic kernels and accurate at a zero-leakage
  function makes at least (1 - alpha') ln((1 - alpha')/alpha) / (-ln(1 - epsilon_acc)) expected Train calls at the twin
  input, for the coupled tail, the total variation and the one-sided divergence of a Gaussian release, and at the base
  input for the first two only. Calls at other inputs count for nothing. Coupled certificates match it up to a ceiling,
  and the every-record certificate multiplies it by the number of records with no union bound.
where: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md#thm-exact-twin-price
uses-to-state: thm-dataflow-composition, def-seed-access-modes
uses-to-prove: lem-needle-lower-bound, thm-coupling-free-soundness
status: proven
evidence: HE-ML:lab/theory/spaces/oracle-and-measurement/round-02/builder.md, a rare-event change of measure over a finite partition of the seed space. Numbers computed there, 686.5
  calls at alpha = alpha' = 10^-3 and epsilon_acc = 10^-2.
checked-by: discussant round-02 (argon) of oracle-and-measurement and the integrator's re-derivation, 2026-10-25. Not checked by
  Halil.
oracle: needs-oracle for the upper bound, both modes for the lower bound
history:
  - 2026-10-25 accepted in round-02 of oracle-and-measurement with BLOCKING 0, merged into the booklet. Supersedes
    conj-exact-twin-price of round-00.

# Computational limits (HE-ML theory space)

Objects merged from the space computational-limits of `lab/theory/` on 2026-10-25. None needs the learning oracle.

## lem-sq-learner-post-processing
kind: lemma
statement: A learner that reaches a uniform or planted-biclique training law only through m calls to 1-STAT cannot hand
  the planted structure to any unbounded, white-box reader of its output unless m = Omega(n^2/k^2), and the VSTAT form
  holds against every valid oracle, covering coarse-precision mini-batch SGD learners.
where: HE-ML:lab/theory/spaces/computational-limits/round-00/builder.md#lem-sq-learner-post-processing
uses-to-state: fact-fgrvx17-planted-clique-sq-bound
uses-to-prove: fact-sq-simulates-minibatch-sgd
status: proven
evidence: post-processing of an SQ algorithm, FGRVX17 Theorems 2.10 and 5.4, AKMSS21 Theorem 1c.
checked-by: astra, round 00 of computational-limits, 2026-10-25. Not checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in round 00 of computational-limits, merged into the booklet when the space converged.

## def-seed-blind-reconstruction-game
kind: definition
statement: The split protocol class P_H, equivariant under a group H in O(d), whose server never sees first-layer weights,
  their gradients or records. A sample game (fine success against the narcissus baseline) and a population SQ game (weak
  success, frozen clients), each with a seed-known variant. The price of the seed is the pair of budget sets at which the
  seed-known and the seed-blind attackers reach a success level.
where: HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md#def-seed-blind-reconstruction-game, with the wording correction of HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md
uses-to-state: fact-cohen-narcissus-equals-one-wayness, fact-orthogonal-equivariance-of-training
uses-to-prove: none
status: proven
evidence: a definition.
checked-by: astra, round 01 of computational-limits, 2026-10-25. Not checked by Halil.
oracle: n/a
history:
  - 2026-10-25 accepted in round 01, wording corrected in round 02, merged into the booklet.

## lem-equivariant-view-coupling
kind: lemma
statement: For a protocol in P_H the server's view of the run on records x equals pathwise the view of the run on Qx with
  W_0 replaced by W_0 Q^T, so a simulator running the protocol on Haar-rotated records reproduces every attacker's output
  jointly with the targets at the cost of one training run.
where: HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md#lem-equivariant-view-coupling
uses-to-state: def-seed-blind-reconstruction-game
uses-to-prove: fact-orthogonal-equivariance-of-training
status: proven
evidence: induction on the training step, HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md.
checked-by: astra, round 01 of computational-limits, and the integrator's re-derivation, 2026-10-25. Not checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in round 01, merged into the booklet.

## lem-whitening-gives-rotated-records
kind: lemma
statement: For a frozen linear client of full column rank and right rotation invariant law, and isotropic records, the
  population whitening of the representations returns Rx with R Haar on O(d), a function of the weights alone and
  independent of the records.
where: HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md#lem-whitening-gives-rotated-records
uses-to-state: def-seed-blind-reconstruction-game
uses-to-prove: none
status: proven
evidence: polar decomposition and uniqueness of the right-invariant probability on O(d), HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md.
checked-by: astra, round 01 of computational-limits, and the integrator's re-derivation, 2026-10-25. Not checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in round 01, merged into the booklet.

## thm-reconstruction-from-conditional-mean
kind: theorem
statement: For a frozen linear client, Gaussian records and labels a noisy function of <u,x> with first Hermite
  coefficient beta_1 nonzero, a server holding a top model of excess square risk epsilon recovers u up to sign within
  2 (sqrt(epsilon) + eta_N) / |beta_1| from N held-out representations, and reconstructs the hidden coordinate of any
  records, training records included. The attacker's error is bounded above by a function of the attacked model's excess
  risk, the floor on attack success in Halil's example.
where: HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md#thm-reconstruction-from-conditional-mean, with the wording correction of HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md
uses-to-state: def-seed-blind-reconstruction-game
uses-to-prove: lem-whitening-gives-rotated-records
status: proven
evidence: HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md, Stein-type identity, Cauchy-Schwarz and Chebyshev.
checked-by: astra, round 01 of computational-limits, and the integrator's re-derivation, 2026-10-25. Not checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in round 01, wording corrected in round 02, merged into the booklet.

## conj-reconstruction-at-training-cost
kind: conjecture
statement: Blind reconstruction of the label-relevant coordinate costs what learning the task costs.
where: HE-ML:lab/theory/spaces/computational-limits/round-00/builder.md#conj-reconstruction-at-training-cost, withdrawn in HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md
uses-to-state: none
uses-to-prove: none
status: refuted
evidence: part (b) refuted by astra, round 00. The labels y = <u,x> xi with an independent sign have Bayes square-loss
  predictor zero while the label law reveals <u,x> up to sign at generative exponent two. Part (a) became
  thm-reconstruction-from-conditional-mean.
checked-by: astra, rounds 00 and 01 of computational-limits, 2026-10-25.
oracle: n/a
history:
  - 2026-10-25 posed in round 00, refuted and withdrawn in round 01.

## prop-sq-blind-reconstruction-bound
kind: proposition
statement: Seed-blind reconstruction of a pancake coordinate from a frozen client of P_O(d) to weak success c_0 needs
  (11/288) M tau_*^2 beta^2 / gamma^2 - d statistical queries with M = exp(Omega(c_0^4 d)), and for moment-matched
  record laws with four or more matched moments it needs 2^(d^Omega(c)) queries or polynomially small tolerance.
where: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md#prop-sq-blind-reconstruction-bound
uses-to-state: def-seed-blind-reconstruction-game, fact-clwe-hardness
uses-to-prove: lem-equivariant-view-coupling, fact-hclwe-sq-correlation-bound, fact-ngca-sq-lower-bound, fact-fgrvx17-planted-clique-sq-bound
status: proven
evidence: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md, part (b) conditional on DKRS23 Theorem 1.5. Reduction to a search problem and FGRVX17 Theorem 3.2.
checked-by: astra (round 01) and argon (round 02) of computational-limits, and the integrator's re-derivation of the
  arithmetic, 2026-10-25. The cited SQ and lattice theorems were not re-read by the integrator. Not checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in round 02 of computational-limits with BLOCKING 0, merged into the booklet.

## prop-fine-reconstruction-to-hclwe
kind: proposition
statement: A seed-blind attacker reconstructing every pancake coordinate within c_1/gamma from a protocol of P_O(d),
  frozen or trained, gives an hCLWE distinguisher at the cost of one protocol run, so fine reconstruction is negligible
  for polynomial-time attackers unless a worst-case lattice problem is quantum polynomial-time.
where: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md#prop-fine-reconstruction-to-hclwe
uses-to-state: fact-clwe-hardness
uses-to-prove: lem-equivariant-view-coupling
status: proven
evidence: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md with HE-ML:lab/theory/spaces/computational-limits/round-01/builder.md, conditional hardness under BRST21 Corollary 4.2.
checked-by: astra (round 01) and argon (round 02) of computational-limits, and the integrator's re-derivation, 2026-10-25. Not
  checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in round 02 of computational-limits with BLOCKING 0, merged into the booklet.

## thm-blind-split-seed-separation
kind: theorem
statement: For Gaussian-initialized expansive ReLU clients trained by orthogonally equivariant updates on pancake records,
  a seed-known server inverts every record in polynomial time (frozen clients, and records seen under the initial weights),
  while a seed-blind server pays an exponential SQ price (frozen) or a quantum lattice algorithm (fine reconstruction,
  frozen or trained).
where: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md#thm-blind-split-seed-separation
uses-to-state: fact-lei-random-expansive-layers-invertible
uses-to-prove: prop-sq-blind-reconstruction-bound, prop-fine-reconstruction-to-hclwe, lem-equivariant-view-coupling
status: proven
evidence: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md, composition of the cited propositions with LJDD19 Theorem 3.
checked-by: astra (round 01) and argon (round 02) of computational-limits, and the integrator, 2026-10-25. Not checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in round 02 of computational-limits with BLOCKING 0, merged into the booklet. Astra judges it an
    artificial-distribution reduction, and whether it meets the plug-in rule is a decision for Halil.

## prop-sq-label-relevant-reconstruction-bound
kind: proposition
statement: For a frozen linear client, Gaussian records and single-index labels of generative exponent k* >= 3, an SQ
  attacker reaching weak success on the label-relevant coordinate with polynomially many queries needs VSTAT(n) with
  n >= c d^(k*/2), and the sample-based algorithm of DPLB24 on whitened representations matches it.
where: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md#prop-sq-label-relevant-reconstruction-bound
uses-to-state: def-seed-blind-reconstruction-game
uses-to-prove: lem-equivariant-view-coupling, lem-whitening-gives-rotated-records, fact-generative-exponent-sq-recovery-bound, fact-fgrvx17-planted-clique-sq-bound
status: proven
evidence: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md, FGRVX17 Theorem 3.2 with Lemma 3.10 on the code of DPLB24 Lemma E.3.
checked-by: astra (round 01) and argon (round 02) of computational-limits, and the integrator's re-derivation, 2026-10-25. Not
  checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in round 02 of computational-limits with BLOCKING 0, merged into the booklet.

## conj-seed-price-is-ngca-price
kind: conjecture
statement: For recoverable frozen clients of P_O(d) and isotropic hidden laws of fixed dimension, the budget sets of
  seed-blind attackers in the SQ and sample games equal, up to polynomial factors, those of NGCA coordinate recovery with
  a uniformly random frame.
where: HE-ML:lab/theory/spaces/computational-limits/round-02/builder.md#conj-seed-price-is-ngca-price
uses-to-state: def-seed-blind-reconstruction-game
uses-to-prove: lem-equivariant-view-coupling, lem-whitening-gives-rotated-records, prop-sq-blind-reconstruction-bound, prop-fine-reconstruction-to-hclwe
status: open
evidence: the lower inclusion is settled for pancakes in both games and for moment-matched laws in the SQ game, the upper
  inclusion for frozen linear clients given the population whitening.
checked-by: argon, round 02 of computational-limits, as a well-posed conjecture, 2026-10-25.
oracle: holds-without-oracle
history:
  - 2026-10-25 posed in round 00, rejected in round 01, restated and accepted as well posed in round 02.

# Statistical limits (HE-ML theory space)

Objects merged from the space statistical-limits of `lab/theory/` on 2026-10-25.

## def-uniform-security-profile
kind: definition
statement: The uniform regret of a class of instances at a budget of reference samples and Train calls, under the bottom
  or top oracle, is the least worst-case gap to the informed optimum over adversaries chosen before the instance, with an
  attained price (minimal budgets, finite by Dickson's lemma) and a threshold price of a criterion. On one instance the
  regret is zero as an infimum, so every positive regret is a price of not knowing the instance.
where: HE-ML:lab/theory/spaces/statistical-limits/round-01/builder.md#def-uniform-security-profile, with the changes of HE-ML:lab/theory/spaces/statistical-limits/round-02/builder.md
uses-to-state: def-learning-oracle-model, def-degenerate-oracles
uses-to-prove: thm-coupling-certificate, thm-black-box-certifiability, fact-hsu-membership-sample-gap
status: proven
evidence: a definition with properties proven in the round files.
checked-by: astra (round 01) and argon (round 02) of statistical-limits, and the integrator, 2026-10-25. Not checked by Halil.
oracle: holds-without-oracle in its statement, properties use the oracle
history:
  - 2026-10-25 accepted in round 02 of statistical-limits with BLOCKING 0, merged into the booklet. The unbounded-adversary
    form of def-security-profile-curve.

## lem-scrambled-seed-urn
kind: lemma
statement: Under a uniformly random bijection of seed cells, the transcript of any adversary with at most N < M Train calls,
  chosen and opened seeds included, is within total variation N^2/(2(M - N)) of a lazy oracle that answers each new cell
  with a fresh draw, and two lazy oracles from laws p and p' give transcripts within KL divergence N KL(p || p').
where: HE-ML:lab/theory/spaces/statistical-limits/round-02/builder.md#lem-scrambled-seed-urn
uses-to-state: def-learning-oracle
uses-to-prove: none
status: proven
evidence: a hybrid bound integrated along the paths of the scrambled run, HE-ML:lab/theory/spaces/statistical-limits/round-02/builder.md.
checked-by: argon, round 02 of statistical-limits, and the integrator's re-derivation, 2026-10-25. Not checked by Halil.
oracle: needs-oracle
history:
  - 2026-10-25 accepted in round 02 of statistical-limits with BLOCKING 0, merged into the booklet.

## thm-shadow-run-price-finite-views
kind: theorem
statement: For one learning node seen through a deterministic channel onto k views, coming within a < 1/8 of the best
  bottom-oracle advantage at every learning function needs at least 3k'/(1024 a^2) Train calls, k' = 2 floor(k/2), and
  2 ceil(4k/a^2) drawn-seed calls suffice. Chosen, opened and reused seeds and calls after the challenge do not lower the
  price. Under the top oracle with deterministic kernels one call at the honest seed reaches the top optimum. Label-only
  views give k = C^q_E.
where: HE-ML:lab/theory/spaces/statistical-limits/round-01/builder.md#thm-shadow-run-price-finite-views, with the changes of HE-ML:lab/theory/spaces/statistical-limits/round-02/builder.md
uses-to-state: def-uniform-security-profile, def-degenerate-oracles
uses-to-prove: lem-scrambled-seed-urn, thm-coupling-certificate, thm-black-box-certifiability, thm-reference-access
status: proven
evidence: Assouad-type averaging over paired views with a KL chain rule, and the scrambled family for deterministic
  kernels, HE-ML:lab/theory/spaces/statistical-limits/round-01/builder.md and HE-ML:lab/theory/spaces/statistical-limits/round-02/builder.md.
checked-by: astra (round 01) and argon (round 02) of statistical-limits, and the integrator's re-derivation, 2026-10-25. Not
  checked by Halil.
oracle: needs-oracle
history:
  - 2026-10-25 accepted in round 02 of statistical-limits with BLOCKING 0, merged into the booklet. Supersedes
    conj-shadow-run-price-finite-views of round 00. Novelty of the oracle part checked by one query only.

## prop-reconstruction-label-sandwich
kind: proposition
statement: For a record, a finite label and a representation, the best reconstruction success lies between the
  label-weighted class baseline minus the Bayes label error and that baseline plus sqrt(I(X; Z | Y)/2), with the kl form
  kl(S* || kappa) <= I(X; Z | Y), a Gaussian-release bound on the conditional information, and tightness at both ends.
where: HE-ML:lab/theory/spaces/statistical-limits/round-01/builder.md#prop-reconstruction-label-sandwich, with the changes of HE-ML:lab/theory/spaces/statistical-limits/round-02/builder.md
uses-to-state: fact-balle-reconstruction-robustness-definition
uses-to-prove: fact-pac-privacy-mutual-information-bound, fact-pac-privacy-gaussian-release-bound
status: proven
evidence: HE-ML:lab/theory/spaces/statistical-limits/round-01/builder.md and HE-ML:lab/theory/spaces/statistical-limits/round-02/builder.md, elementary, the ceiling is XD23 Theorem 1 with side knowledge.
checked-by: astra (round 01) and argon (round 02) of statistical-limits, and the integrator's re-derivation, 2026-10-25. Not
  checked by Halil.
oracle: holds-without-oracle
history:
  - 2026-10-25 accepted in rounds 01 and 02 of statistical-limits, merged into the booklet. The statistical floor of Halil's
    reconstruction example. Supersedes conj-reconstruction-label-sandwich of round 00.

# Adversary interface (HE-ML)

## def-interface-data-space
kind: definition
statement: The data space is an arbitrary set with no structure assumed. An example may be a labelled pair, an unlabelled input, a token sequence or one party's block of features. A dataset is a finite multiset of examples, labelled or not, and two datasets of one protocol may live in different data spaces, as a pretraining corpus and a fine-tuning set do. The partition among clients is horizontal when each client holds whole examples, and vertical when each client holds one block of every example. The data space is never the product of an input space and a label space.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The three primitives, HE-ML:CONTEXT.md#Terminology ledger
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: Halil, ruling of 2026-10-16 on the data space and the three primitives, recorded in CONTEXT.md
oracle: n/a
history:
  - 2026-10-16 defined in the interface report. Halil ruled the same day that the data space is never the product of an input space and a label space, because that assumes supervision.
  - 2026-10-25 entered from the HE-ML digest, sections 3.1 and 3.2.

## def-interface-model-space
kind: definition
statement: The model space is an arbitrary set with no structure assumed, and a model is one element of it. A model is used through a public evaluation map from a model and a query to an output, which may be a score vector, a label, a loss, a generated sequence or an embedding. A hypothesis class is a subset of the model space, and it expresses frozen parts, so LoRA and head training are full training on a smaller class. A parameterization is one instance of the model space and not an assumption.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The three primitives, HE-ML:CONTEXT.md#Terminology ledger
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: Halil, ruling of 2026-10-16 on the three primitives, recorded in CONTEXT.md
oracle: n/a
history:
  - 2026-10-16 defined in the interface report and fixed by Halil's ruling of the same day.
  - 2026-10-25 entered from the HE-ML digest, sections 3.1 and 3.2.

## def-interface-learning-function
kind: definition
statement: A learning function is a randomized map from a starting model, a dataset and a hypothesis class to a model. The loss, the optimizer and the number of steps are internal to it, and a loss maps a model and one example to a real number with no labels required. Pretraining is the learning function applied to an initial model, the pretraining corpus and the whole model space. Aggregation is a learning function whose data space is the model space and whose dataset is the multiset of client models, so FedAvg is their mean and a robust aggregator is a robust estimator of location. When the model space is a vector space, the update is the trained model minus the starting model.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The three primitives, HE-ML:CONTEXT.md#Terminology ledger
uses-to-state: def-interface-data-space, def-interface-model-space
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: Halil, ruling of 2026-10-16 on the three primitives, recorded in CONTEXT.md
oracle: n/a
history:
  - 2026-10-16 defined in the interface report. The learning-oracle report of the same day added a seed, and def-learning-oracle makes it a map of a training input, a seed and hardware randomness.
  - 2026-10-25 entered from the HE-ML digest, sections 3.1 and 3.2.
  - 2026-10-25 overlaps def-three-maps of FORMAL_SECURITY, whose training map sends a dataset alone to a function, while this learning function also takes a starting model and a hypothesis class.
  - 2026-10-25 overlaps def-training-recipe of FORMAL_SECURITY, which names the loss, optimizer, batch rule, initialization and step count in public, while this learning function keeps them internal and unnamed.

## def-interface-protocol
kind: definition
statement: A protocol is a finite directed acyclic graph. Each node applies a learning function or an evaluation map to arguments, a model, a dataset and a hypothesis class, that come from datasets, public objects or earlier nodes, and it emits an output. Every node value is a function of the datasets, the honest randomness and the adversary's choices.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The three primitives
uses-to-state: def-interface-learning-function, def-interface-model-space
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report. The learning-oracle report of the same day calls the same graph the dataflow graph, and the final theory calls it a procedure in def-learning-oracle-model.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.

## def-interface-channel
kind: definition
statement: Each node value reaches the adversary through one channel. The channel gives the plaintext value, a sum over a set of clients, a ciphertext under a key the adversary does not hold, the value with added noise, or nothing. A decryption policy releases chosen functions of encrypted values, and for approximate HE a released value carries the decryption noise as well.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The adversary
uses-to-state: def-interface-protocol
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report. The learning-oracle theory keeps three channels, plain, query and none, and treats a sum, a ciphertext or a noisy value as a general node released in plain.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.

## def-interface-view
kind: definition
statement: The view is the family of node values the adversary sees, each through its channel, together with oracle access to the evaluation map of the served model. The evaluation map of the served model fixes what an answer reveals.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The adversary, HE-ML:CONTEXT.md#Terminology ledger
uses-to-state: def-interface-channel, def-interface-model-space
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.
  - 2026-10-25 overlaps def-oracle-view-of-trace of FORMAL_SECURITY, where a view is one public, possibly lossy function of a training trace fixed as a game parameter, while this view is everything the adversary receives.
  - 2026-10-25 overlaps def-capability-vector of FORMAL_SECURITY, which puts what the adversary observes and what it chooses in one vector, while the interface splits them into this view and def-interface-choices.

## def-interface-choices
kind: definition
statement: The choices are the node arguments and node outputs that the adversary sets, of six kinds. They are a data argument, such as its own dataset or poisoned examples, a model argument, the same for all clients or one per client, a class argument, the learning function of a node, the output of a node, and queries to the served model. A semi-honest adversary chooses queries only.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The adversary, HE-ML:CONTEXT.md#Terminology ledger
uses-to-state: def-interface-protocol
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report. The ledger fixes the word choices and bans capabilities for it.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.
  - 2026-10-25 overlaps def-capability-vector of FORMAL_SECURITY, which records passive observation and choosing in one vector, while this definition lists only what the adversary sets.

## def-distinguish-goal
kind: definition
statement: The distinguish goal has two hypotheses on the clients' datasets. The adversary outputs a bit, and its advantage is the probability of one under the second hypothesis minus the probability of one under the first. Membership is a pair that differs in one record of a client's dataset, property inference is a pair of laws for one dataset, and HE-OFT's content game is a pair of datasets of equal size. The baseline is the best advantage reached from public knowledge alone.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The adversary
uses-to-state: def-interface-view, def-interface-data-space
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report. The ledger bans membership and property inference as names of the goal.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.
  - 2026-10-25 overlaps def-comp-mem-game of FORMAL_SECURITY, a computational membership game, while this goal quantifies over unbounded adversaries.
  - 2026-10-25 overlaps def-game-skeleton-and-criteria of FORMAL_SECURITY, whose distinguish criterion matches this goal inside a game that also names a recipe, views and budgets.
  - 2026-10-25 overlaps def-baseline-of-r of FORMAL_SECURITY, where the baseline is a field of the criterion, while here it belongs to the goal.

## def-invert-goal
kind: definition
statement: The invert goal fixes a target of the datasets or the models and a tolerance, and the adversary wins when its estimate lies within the tolerance of the target. Reconstruction takes a record of a client's dataset as the target, and model extraction takes a model that agrees with the served model on queries, scored by fidelity. The baseline is the best success reached from public knowledge alone.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The adversary
uses-to-state: def-interface-view, def-interface-model-space
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report. The ledger bans reconstruction and extraction as names of the goal.
  - 2026-10-17 the learning-oracle theory drops this goal from its definitions and covers it by prop-privacy-bound-bounds-inversion.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.
  - 2026-10-25 overlaps def-game-skeleton-and-criteria of FORMAL_SECURITY, whose produce criterion holds reconstruction, extraction and forgery, while this goal holds reconstruction and extraction and leaves forgery out.
  - 2026-10-25 overlaps def-baseline-of-r of FORMAL_SECURITY, where the baseline is a field of the criterion, while here it belongs to the goal.

## def-steer-goal
kind: definition
statement: The steer goal fixes a target set of models. The adversary wins when the trained model lands in the target set under its choices, while a defender's discriminator between honest and adversarial outputs has advantage at most delta. Untargeted poisoning takes the models of high expected loss, and a backdoor takes the models whose outputs on triggered queries satisfy a predicate the adversary fixes. The stealth constraint is itself a distinguish game played by the defender. The baseline is the best success reached from public knowledge alone.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The adversary
uses-to-state: def-interface-choices, def-distinguish-goal
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report. The ledger bans poisoning and backdoor as names of the goal.
  - 2026-10-17 def-learning-oracle-model keeps the goal with an acceptance event in place of the defender's discriminator.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.
  - 2026-10-25 overlaps def-game-skeleton-and-criteria of FORMAL_SECURITY, where a backdoor game is both a distinguish and a produce game, while here steering is a goal of its own.
  - 2026-10-25 overlaps def-baseline-of-r of FORMAL_SECURITY, where the baseline is a field of the criterion, while here it belongs to the goal.

## def-adversary-order
kind: definition
statement: One adversary is at most as strong as another when its choices are a subset of the other's and its view is a randomized function of the other's view with independent randomness. For efficient adversaries the function must be efficient.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The order, and the two kinds of result
uses-to-state: def-interface-view, def-interface-choices
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report and on deck frame 6 of the meeting of that day.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.

## def-collapse-at-goal
kind: definition
statement: A collapse at a fixed goal shows that a weaker adversary attains the stronger adversary's best value.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The order, and the two kinds of result, HE-ML:CONTEXT.md#Terminology ledger
uses-to-state: def-adversary-order
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report.
  - 2026-10-25 entered from the HE-ML digest, section 3.1.

## def-separation-at-goal
kind: definition
statement: A separation at a fixed goal is a construction, a dataset law, a learning function and a hypothesis class, on which the stronger adversary does much better than the weaker one.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The order, and the two kinds of result, HE-ML:CONTEXT.md#Terminology ledger
uses-to-state: def-adversary-order
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: n/a
history:
  - 2026-10-16 defined in the interface report.
  - 2026-10-25 entered from the HE-ML digest, section 3.1.

## def-party-node-relations
kind: definition
statement: A party stands in one of four relations to a node. It sees the output through a channel, an argument is public to it, it sets an argument, or it sets the output.
where: HE-ML:sink/ledger-columns.md#sections 1 and 2
uses-to-state: def-interface-protocol, def-interface-channel
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-16 merged into the column dictionary of the ledger.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.

## prop-ledger-reductions
kind: proposition
statement: The ledger makes five reductions. Knowledge is publicity of arguments. Behaviour terms follow from the four relations. Data poisoning and Byzantine behaviour differ only in what is set and when. A check restricts a relation. The nominal and the effective channel can differ.
where: HE-ML:sink/ledger-columns.md#sections 1 and 2
uses-to-state: def-party-node-relations
uses-to-prove: none
status: heuristic
evidence: recorded as modelling conventions of the ledger. The assumption is that the four relations of a party to a node express each coded threat model.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-16 merged into the column dictionary of the ledger.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.

## prop-seven-threat-templates
kind: proposition
statement: Seven templates of role, choices and goal hold 513 of the 516 coded rows of 349 papers. They are the server that reads what it receives, the server that sets what clients compute, the server with clients, clients that set their updates, clients that set only their data, clients that read the model, and a querier or eavesdropper.
where: HE-ML:lib/reports/src/2026-10-16-halil-swept-papers-and-threat-models.tex
uses-to-state: def-interface-choices, def-party-node-relations
uses-to-prove: none
status: empirical
evidence: counted on rows that one language-model coder extracted, which still await a check against their papers. The count ran on the ledger of 519 rows without the rows of SCEKPSTZ23.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-16 counted in the swept-papers report.
  - 2026-10-25 entered from the HE-ML digest, section 3.2.

## prop-order-bounds-advantage-and-inversion
kind: proposition
statement: If one adversary is at most as strong as another in the order, its best distinguishing advantage and its best inversion success are at most the other's.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The order, and the two kinds of result
uses-to-state: def-adversary-order, def-distinguish-goal, def-invert-goal
uses-to-prove: prop-best-advantage-equals-total-variation
status: proven
evidence: by the data-processing inequality for distinguishing and by simulation for inversion, in the report and on deck frame 6 of the meeting of 2026-10-16.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: holds-without-oracle. It is a statement about laws of views.
history:
  - 2026-10-16 stated in the interface report.
  - 2026-10-25 entered from the HE-ML digest, section 4.2, where it is named the order.

## prop-best-advantage-equals-total-variation
kind: proposition
statement: The best distinguishing advantage equals the total variation distance between the laws of the view under the two hypotheses.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The order, and the two kinds of result
uses-to-state: def-distinguish-goal, def-interface-view
uses-to-prove: none
status: proven
evidence: by the lemma of Neyman and Pearson. The learning-oracle theory uses the same fact as its standing fact F1.
checked-by: unchecked. The interface report is a draft by its own status field.
oracle: holds-without-oracle. It is a statement about laws of views.
history:
  - 2026-10-16 stated in the interface report.
  - 2026-10-25 entered from the HE-ML digest, section 4.2, where it is named the test fact.

## prop-sufficiency-gives-distinguish-collapse
kind: proposition
statement: If the weaker view is a sufficient statistic of the stronger view for the two hypotheses, the weaker adversary collapses onto the stronger one at the distinguish goal. The converse fails for one fixed pair of hypotheses.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The order, and the two kinds of result, deck frame 6 in the folder 2026-10-16-meeting under HE-ML:lib/profs/
uses-to-state: def-collapse-at-goal, def-distinguish-goal, def-adversary-order
uses-to-prove: prop-best-advantage-equals-total-variation
status: proven
evidence: sufficiency gives equal total variation, and a three-point example on deck frame 6 shows that the converse fails.
checked-by: unchecked
oracle: holds-without-oracle. It is a statement about laws of views.
history:
  - 2026-10-16 the interface report stated that a collapse at the distinguish goal holds exactly when the weaker view is a sufficient statistic of the stronger. That converse is false.
  - 2026-10-16 deck frame 6 corrected it with a three-point example.
  - 2026-10-25 entered from the HE-ML digest, section 4.2, where it is named collapse by sufficiency.

## prop-interface-coverage-of-swept-adversaries
kind: proposition
statement: Every adversary that the sweeps report is a triple of a view, choices and one of the goals distinguish, invert and steer. Membership inference is a distinguish game, reconstruction and extraction are inversion, and poisoning and backdoors are steering.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The order, and the two kinds of result
uses-to-state: def-interface-view, def-interface-choices, def-distinguish-goal, def-invert-goal, def-steer-goal
uses-to-prove: none
status: empirical
evidence: on the sweep extractions of the placed papers. 25 of 519 rows carry a goal outside the three, free-riding, compliance bypass and watermark removal, by deck frame 7.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-16 stated in the interface report on 44 papers, and recounted on the ledger for the deck.
  - 2026-10-25 entered from the HE-ML digest, section 4.2, where it is named coverage.

## prop-he-oft-count-steering
kind: proposition
statement: In HE-OFT nothing ties a client's uploaded per-class counts to its public sample count or to its data. A client that reports a large count for a class therefore moves that row of the shared head as close to its own head displacement as it likes.
where: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#HE-OFT on the interface
uses-to-state: def-steer-goal
uses-to-prove: none
status: proven
evidence: from the aggregation formula of HE-OFT, whose row of the shared head is the initializer plus the count-weighted mean of head displacements. HE-OFT does not state it. Deck frame 15 repeats it.
checked-by: unchecked
oracle: holds-without-oracle. It follows from the aggregation formula.
history:
  - 2026-10-16 found in the interface report.
  - 2026-10-25 entered from the HE-ML digest, section 4.2.

## thm-he-oft-semi-honest-simulation
kind: theorem
statement: In HE-OFT a semi-honest server together with t minus 1 clients is simulated from the ideal leakage, under IND-CPA and a smudging hypothesis. The measured configuration of the paper does not meet that hypothesis, and the paper recommends smudging at 2 to the 25 with a duplicate-query check.
where: HE-ML:lib/literature/notes/arxiv/KSK26.md, HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#HE-OFT on the interface
uses-to-state: def-interface-view
uses-to-prove: none
status: proven
evidence: proven in HE-OFT (KSK26), the group's own prior paper, read in full on 2026-10-16.
checked-by: unchecked here. The proof is HE-OFT's.
oracle: holds-without-oracle
history:
  - 2026-10-16 placed on the interface in the interface report.
  - 2026-10-16 deck frames 13 and 15 ask whether its per-party smudging meets standard simulation security, given that Hwang et al. (HHKLS26) prove, as extracted, that independent per-party smudging fails it. Unchecked.
  - 2026-10-25 entered from the HE-ML digest, section 4.2.

## thm-he-oft-deviating-clients-bound
kind: theorem
statement: In HE-OFT, against t minus 1 deviating clients and an honest server, the distinguishing advantage is at most a negligible term plus what the coalition's label queries give. The bound rests on three readings of deviating messages that no proof in HE-OFT enforces, and HE-OFT makes no steering claim.
where: HE-ML:lib/literature/notes/arxiv/KSK26.md, HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#HE-OFT on the interface
uses-to-state: def-distinguish-goal, def-interface-choices
uses-to-prove: none
status: proven
evidence: proven in HE-OFT (KSK26), read in full on 2026-10-16, under the three readings named in the statement.
checked-by: unchecked here. The proof is HE-OFT's.
oracle: holds-without-oracle
history:
  - 2026-10-16 placed on the interface in the interface report, which names the missing steering claim.
  - 2026-10-25 entered from the HE-ML digest, section 4.2.

## thm-he-oft-label-view-ordering
kind: theorem
statement: In HE-OFT, the label answers of a deviating coalition of t minus 1 clients, at most Q per client, give no more than both shared heads in plaintext. The white-box advantage measures near zero.
where: HE-ML:lib/literature/notes/arxiv/KSK26.md, HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#The order, and the two kinds of result
uses-to-state: def-adversary-order, def-distinguish-goal
uses-to-prove: none
status: proven, the ordering. The near-zero white-box advantage is empirical, a measurement in HE-OFT.
evidence: proven in HE-OFT (KSK26), read in full on 2026-10-16. It is the only settled step between adversaries on deck frame 11 that rests on a full reading.
checked-by: unchecked here. The proof is HE-OFT's.
oracle: holds-without-oracle
history:
  - 2026-10-16 placed on the interface as the ordering of labels against the head.
  - 2026-10-16 Küpçü's question asks for the reverse ordering, when the label queries reach what the shared head reveals. It is open.
  - 2026-10-25 entered from the HE-ML digest, section 4.2.

## thm-he-oft-no-deviating-server
kind: theorem
statement: In HE-OFT a client's decision to contribute a decryption share cannot depend on the plaintext. So no protocol in which clients decrypt what the server presents admits a deviating server, and at four classes one request carries the whole head.
where: HE-ML:lib/literature/notes/arxiv/KSK26.md, HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex#HE-OFT on the interface
uses-to-state: def-interface-choices
uses-to-prove: none
status: proven
evidence: proven in HE-OFT (KSK26), read in full on 2026-10-16. The paper names a checker that recomputes the deterministic serving circuit, or verifiable HE, as the remedy.
checked-by: unchecked here. The proof is HE-OFT's.
oracle: holds-without-oracle
history:
  - 2026-10-16 placed on the interface in the interface report, which names the cheapest check on what the quorum key-switches as the open object.
  - 2026-10-25 entered from the HE-ML digest, section 4.2.

# FORMAL_SECURITY programme

## def-r-as-quantizer
kind: definition
statement: The success criterion R maps an approximate learning outcome to a bit, the step from the approximate learning layer to the exact cryptographic layer. It is exact by type and carries its parameters where the approximation is quantized. It fixes the baseline and selects the learning problem the adversary solves, and it is one object. There is one R for each choice of search or decision and of attack target.
where: FS:exp/docs/CONTEXT.md, FS:exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md
uses-to-state: none
uses-to-prove: none
status: proven
evidence: an ontological definition, and nothing is claimed beyond it. Its claim to select the problem is prop-r-selects-the-problem.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 defined in the report and the programme ledger, with its relation form borrowed from Cohen et al., ITCS 2025.
  - 2026-08-05 its novelty was withdrawn the same day. With a binary codomain R is a binary gain function of Alvim, Chatzikokolakis, Palamidessi and Smith, CSF 2012, Definition 3.6.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.1 and 3.1, where it is named r-as-quantizer. The letter R also names the query-region metric of def-behavioural-distance-d-r and def-backdoor-reproduction-number.

## def-baseline-of-r
kind: definition
statement: The baseline of R is what a party with public knowledge alone achieves on R. It is a field of R and not of the game. The survey uses the same notion, what a party with public knowledge alone achieves against the target.
where: FS:exp/docs/CONTEXT.md, FS:exp/survey/CONTEXT.md
uses-to-state: def-r-as-quantizer
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.1 and 2.4.
  - 2026-10-25 overlaps the baselines of def-distinguish-goal, def-invert-goal and def-steer-goal of HE-ML, which belong to the goal, while this baseline belongs to the criterion.

## def-degenerate-baseline
kind: definition
statement: A baseline is degenerate when it equals 0, one half or 1. Subtracting a degenerate baseline changes nothing, which forces the raw advantage.
where: FS:exp/docs/CONTEXT.md
uses-to-state: def-baseline-of-r
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.1.

## def-tolerance-of-r
kind: definition
statement: The tolerance eta is the parameter of R at which the approximate outcome is quantized. The ledger reads it as the dial between a coarse population regime, with nothing to measure, and a tight cryptographic regime, which needs an assumption.
where: FS:exp/docs/CONTEXT.md
uses-to-state: def-r-as-quantizer
uses-to-prove: none
status: proven
evidence: a definition. The claim about the two regimes is prop-eta-dial.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.1.

## def-searching-party
kind: definition
statement: The party searching for R, written P, is the attacker in the privacy criteria and the detector in the backdoor criterion. It is an explicit argument of Phi.
where: FS:exp/docs/CONTEXT.md, FS:exp/docs/reports/2026-08-05-unfiled-concrete-r-criteria.md
uses-to-state: def-r-as-quantizer
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.1.

## def-displacement-grades
kind: definition
statement: Displacement is what a training-time adversary does to the learned function f. It has four grades, none, x non-adaptive, x adaptive and f.
where: FS:exp/docs/CONTEXT.md
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.1.

## def-phase-of-action-and-measurement
kind: definition
statement: The phase of action is when the adversary acts, and the phase of measurement is when R is evaluated. The two differ for a backdoor.
where: FS:exp/docs/CONTEXT.md
uses-to-state: def-r-as-quantizer
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.1.

## def-adversary-class
kind: definition
statement: The adversary class is the set of algorithms that an adversary is drawn from, the set a claim quantifies over in the survey's wording.
where: FS:exp/docs/CONTEXT.md, FS:exp/survey/CONTEXT.md
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-08-05 the prior-art sweeps left the adversary axis, a class with a budget, as the only defensible contribution of the programme.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.1 and 2.4.

## def-adversary-resource-budget
kind: definition
statement: The budget b is the adversary's resource budget in the programme ledger. The survey uses the word budget for another object, a numeric allowance such as a perturbation radius or a corruption fraction, which is one value of def-survey-tightness.
where: FS:exp/docs/CONTEXT.md
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.1 and 2.4.

## def-security-profile-curve
kind: definition
statement: The security profile is the measurable curve that maps a budget b to the success epsilon(b) an adversary reaches. The report of 2026-08-05 states the object to prove as the largest tolerance eta that an efficient adversary reaches against a model of test error at most epsilon, as a function of epsilon.
where: FS:exp/docs/CONTEXT.md, FS:exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md
uses-to-state: def-adversary-resource-budget, def-tolerance-of-r
uses-to-prove: none
status: open
evidence: the ledger records the curve as proposed, and the report records the object to prove as open.
checked-by: unchecked
oracle: n/a
history:
  - 2026-08-05 proposed in the ledger and set as the object to prove in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.1 and 3.1, where it is named security-profile-curve.

## def-phi-one-function
kind: definition
statement: Phi of P, a class and a budget is the infimum of the thresholds theta at which some adversary of the class at that budget makes P win R_theta above the baseline. It reads as leakage when P is the attacker and as the detection floor when P is the detector, and it requires the family R_theta to be monotone in theta. The report proposes that this one function answers the two functions the PI requested, with the security margin as the computational value minus the information-theoretic value in the units of theta.
where: FS:exp/docs/reports/2026-08-05-unfiled-leakage-and-integrity-functions.md, FS:exp/docs/CONTEXT.md
uses-to-state: def-r-as-quantizer, def-searching-party, def-adversary-class, def-adversary-resource-budget, def-baseline-of-r
uses-to-prove: none
status: open
evidence: proposed with no proof. Monotonicity of R_theta must be stated as a condition, and the relation to g-leakage is unresolved, with two expected differences, a threshold scanned over a family and an adversary class at a budget.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 proposed in the report.
  - 2026-08-05 the unification claim was withdrawn the same day against Clarkson and Schneider, CSF 2010.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.1 and 3.1, where it is named phi-one-function. The name leakage function is banned for it.

## def-three-maps
kind: definition
statement: The programme keeps three maps apart and never conflates them. They are the training map L from a dataset D to a function f in the hypothesis space, the parameterization from weights w to a model M_w, and the feature map from an input x to f_theta(x).
where: FS:exp/docs/CONTEXT.md, FS:exp/docs/notes/game-family-and-reduction-targets.md#§2
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.1.
  - 2026-10-25 overlaps def-interface-learning-function of HE-ML, which also takes a starting model and a hypothesis class, while this training map sends a dataset alone to a function.

## prop-training-time-attacks-are-displacements
kind: proposition
statement: Every training-time adversary displaces the learned function f, and loss increase is one criterion R over that displacement. The undetectable backdoor, which preserves clean loss, is the counterexample to the view that training-time attacks alter loss.
where: FS:exp/docs/reports/2026-08-05-unfiled-attack-surface-decomposition.md
uses-to-state: def-displacement-grades, def-r-as-quantizer
uses-to-prove: none
status: open
evidence: a derivation, exhaustive over displacement targets, with the irreducibility of the attack families not shown.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-08-05 corrected the same day by prop-three-axis-attack-surface, which seats gradient inversion at training phase with no displacement.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## prop-three-axis-attack-surface
kind: proposition
statement: Three axes index every named attack. They are the phase of observation, training or test, the displacement, and the target of R, a property of D, of f or of f(x). Gradient inversion in split or federated learning sits at training phase, with no displacement, on a property of D.
where: FS:exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md#Result, FS:exp/docs/CONTEXT.md
uses-to-state: def-displacement-grades, def-r-as-quantizer
uses-to-prove: none
status: open
evidence: a derivation. Independence of the axes is not shown, and some cells are empty.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report, correcting prop-training-time-attacks-are-displacements.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.1 and 3.1, where it is named three-axis-attack-surface.

## prop-test-time-adversary-is-a-learner
kind: proposition
statement: A test-time adversary runs a learning process whose input is the channel f and whose output is the target z. A training-time adversary acts on a learner. The report calls the first literally true and the second structurally true, so the test-time half takes learning-theoretic thresholds and the training-time half displacement geometry.
where: FS:exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md
uses-to-state: def-displacement-grades
uses-to-prove: none
status: open
evidence: a derivation in the report with no proof.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## prop-displacement-ladder-is-cpa-cca
kind: proposition
statement: The displacement levels none, x non-adaptive and x adaptive correspond to passive, chosen-plaintext and chosen-ciphertext access. So an access level times a criterion replaces per-attack definitions.
where: FS:exp/docs/reports/2026-08-05-unfiled-test-time-attacks-as-learners.md
uses-to-state: def-displacement-grades, def-r-as-quantizer
uses-to-prove: none
status: open
evidence: a correspondence stated in the report with no proof.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## prop-four-criteria-read-off-reference-problems
kind: proposition
statement: Four criteria show that the parameters of R are the parameters of a reference problem, with no mapping step. R1 is reconstruction from a noisy mean, read off Gaussian location estimation. R2 is membership as the zero-tolerance limit, read off two-point testing, with a degenerate baseline. R3 is the backdoor criterion, read off a rare-disagreement search in which the detector searches. R4 is fidelity, read off learning from a labelling oracle.
where: FS:exp/docs/reports/2026-08-05-unfiled-concrete-r-criteria.md
uses-to-state: def-r-as-quantizer, def-degenerate-baseline, def-searching-party
uses-to-prove: none
status: open
evidence: a derivation. R3 is a candidate never checked against CHLX25, and exhaustiveness is not shown.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## prop-technique-attack-twins
kind: proposition
statement: Four pairs of a learning technique and an attack share access level, criterion, algorithm and sample complexity, and differ only in authorization. They are distillation and extraction, transfer learning and property inference, influence functions and membership inference, and unlearning verification and forging.
where: FS:exp/docs/reports/2026-08-05-unfiled-concrete-r-criteria.md
uses-to-state: def-r-as-quantizer
uses-to-prove: none
status: open
evidence: a derivation in the report with no proof.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## prop-eta-dial
kind: proposition
statement: A coarse tolerance eta describes a population with no hardness, a tight eta inverts a lossy map, and one scalar marks the crossing between the two.
where: FS:exp/docs/reports/2026-08-05-unfiled-concrete-r-criteria.md
uses-to-state: def-tolerance-of-r
uses-to-prove: none
status: open
evidence: a derivation in the report with no proof.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## def-pancake-property-inference-reduction
kind: construction
statement: Property inference against a model trained on Gaussian pancakes carries into distinguishing pancakes from the standard Gaussian, with eta, the spacing gamma and the budgets unchanged. A trichotomy follows for the defender. An accurate defender means a lattice break, a failing defender means uselessness, and the practical case is a defender that is accurate without exact recovery.
where: FS:exp/docs/reports/2026-08-05-unfiled-r-as-quantizer-and-one-reduction.md
uses-to-state: def-r-as-quantizer, def-tolerance-of-r
uses-to-prove: none
status: open
evidence: a construction and a chain of implications, not a proof. The projection-and-test tolerance and the search-to-decision direction are unchecked, and the third case is open.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1, where it is named pancake-property-inference-reduction. The digest records it corrected to an illustration of tightness only, because a planted source voids the guardrail on R.

## prop-r-selects-the-problem
kind: proposition
statement: Over one natural sparse Gaussian regression source, with a fixed defender and a fixed release, five choices of R reach five learning problems with five thresholds.
where: FS:exp/docs/reports/2026-08-05-unfiled-natural-source-r-selects-the-problem.md
uses-to-state: def-r-as-quantizer
uses-to-prove: none
status: proven
evidence: recorded as established in the report, by exhibiting the five problems. The reduction from a released network to samples is open, and novelty is not checked.
checked-by: unchecked. The report is a draft with no PI review.
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## def-sparse-support-case-study
kind: construction
statement: The case study fixes a natural sparse Gaussian regression source, five problems that choices of R select, a non-degenerate random-subset baseline, and an adversary budget stated in samples. Its step 5 reduces support recovery from a trained network to recovery from samples, starting with a ridge release.
where: FS:exp/docs/notes/case-study-sparse-support-recovery.md#§15 and §16
uses-to-state: def-r-as-quantizer, def-baseline-of-r
uses-to-prove: prop-r-selects-the-problem
status: open
evidence: the study's own table records the setting, the five problems and the baseline as established, the statistical-computational gap for support recovery as assumed on three bodies of evidence of which none is unconditional, the budget in samples as a modelling decision, step 5 as open and novelty as unchecked. Numbered thresholds carry verify flags.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## prop-four-generator-axes
kind: proposition
statement: The PI's matrix is a projection of four axes, phase of action, phase of measurement, asset (D, L, f or f(x)) and goal (confidentiality, integrity or availability). Backdoors have no single cell, and availability and f(x) are missing from the PI's matrix.
where: FS:exp/survey/lib/reports/archive/2026-08-05-halil-lit-survey-structure.md
uses-to-state: def-phase-of-action-and-measurement, def-three-maps
uses-to-prove: none
status: open
evidence: a derivation with no proof. The report's headline says one cell is structurally empty while its table marks two, integrity at test time against D and against L.
checked-by: unchecked
oracle: n/a
history:
  - 2026-08-05 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

## prop-no-adversary-class-axis
kind: proposition
statement: Across about thirty taxonomies of machine-learning security, none has an adversary-class axis. Every knowledge or access axis is a ladder of interfaces, and privacy and integrity are disjoint by construction.
where: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md
uses-to-state: def-adversary-class
uses-to-prove: none
status: empirical
evidence: a literature finding, verified across the sweep of 2026-08-05.
checked-by: unchecked
oracle: n/a
history:
  - 2026-08-05 found by the sweep.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.1.

# FORMAL_SECURITY programme, working notes

## conj-computational-footing-thesis
kind: conjecture
statement: Security claims about learning should move from statistical to computational footing. The note calls the target the Goldwasser theorem of AI and summarizes it as security is learning lower bounds.
where: FS:exp/docs/notes/intro-computational-security-of-learning.md#§0 to §2
uses-to-state: none
uses-to-prove: none
status: open
evidence: a thesis with no proof.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.2.

## def-comp-mem-game
kind: definition
statement: Computational membership indistinguishability is the on-ramp game, the computational analogue of differential privacy. The note claims that membership is the floor of confidentiality and gives nothing about integrity, so integrity needs a separate analogue of EUF-CMA.
where: FS:exp/docs/notes/intro-computational-security-of-learning.md#§4
uses-to-state: none
uses-to-prove: none
status: open
evidence: proposed with no proof of the claims beyond the definition. Its marginal-advantage form is a refuted no-op, since its baseline is one half by construction, as Yeom, Giacomelli, Fredrikson and Jha, CSF 2018, Definition 4 and Experiment 1, already publish.
checked-by: unchecked
oracle: n/a
history:
  - 2026-08-22 the record of the refutation was corrected to cite Definition 4 of Yeom et al. in place of Definition 6.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.2 and 3.2, where it is named comp-mem-game.
  - 2026-10-25 overlaps def-distinguish-goal of HE-ML, whose membership pair is a distinguish game against unbounded adversaries, while this game is computational.

## def-comp-tw-game
kind: definition
statement: Training-world indistinguishability compares two training worlds that differ by a controlled change Delta, such as one example, a backdoor insertion or a poisoned batch. COMP-MEM is its smallest point.
where: FS:exp/docs/notes/intro-computational-security-of-learning.md#§4, FS:exp/docs/notes/game-family-and-reduction-targets.md#§1
uses-to-state: def-comp-mem-game
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it. The term ledger records it alive for reconstruction and property inference and dead for membership, by prop-advantage-type-decides-the-game.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.2 and 3.2.

## conj-crown-jewel-threshold
kind: conjecture
statement: Past a threshold, learning reduces to breaking a one-way function, and below it hardness is statistical.
where: FS:exp/docs/notes/intro-computational-security-of-learning.md#§3
uses-to-state: none
uses-to-prove: none
status: open
evidence: a target with no proof.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.2.

## def-training-map-fiber
kind: definition
statement: The fiber of the training map at weights w is the set of all datasets that the training map sends to w. Navigability asks whether a point of the fiber consistent with side information can be found efficiently. When training is randomized over seed and batch order, the fiber becomes the conditional law of D given w.
where: FS:exp/docs/notes/fibers-of-the-training-map.md#§1, §5 and §6
uses-to-state: def-three-maps
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it. The security framing built on it is prop-fiber-navigability.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.2. The word fiber also names the parameterization fibre of the AI oracle report of 2026-10-13.

## prop-fiber-navigability
kind: proposition
statement: Security is the infeasibility of navigating the fiber of the training map given side information. The fiber of ordinary least squares is huge, affine and navigable, and white-box access is more dangerous than black-box access as a containment of fibers.
where: FS:exp/docs/notes/fibers-of-the-training-map.md
uses-to-state: def-training-map-fiber
uses-to-prove: none
status: refuted
evidence: refuted at its core by Dinur and Nissim, PODS 2003, who separate the size of the set of consistent datasets from its navigability by complexity. The least-squares example is the note's own.
checked-by: unchecked
oracle: n/a
history:
  - 2026-07-26 refuted at its core against Dinur and Nissim.
  - 2026-08-22 the audit flagged the refutation for re-examination.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.2, where it is named fiber-navigability.

## prop-advantage-type-decides-the-game
kind: proposition
statement: A bit-valued success functional makes baseline subtraction a no-op, and a real-valued one makes it meaningful. So COMP-TW works for reconstruction and property inference and fails for membership.
where: FS:exp/docs/notes/game-family-and-reduction-targets.md#§1
uses-to-state: def-comp-tw-game, def-baseline-of-r, def-degenerate-baseline
uses-to-prove: none
status: open
evidence: proposed with no proof.
checked-by: unchecked
oracle: n/a
history:
  - 2026-07-26 proposed.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.2.

## def-games-g1-to-g5
kind: definition
statement: Five games. G1 is inference-time data inference through the feature map. G2 is training inference from gradients through the feature map at fixed theta. G3 is membership through the training map with raw advantage. G4 is reconstruction from weights through the training map with no calibrated target. G5 is property inference through the training map with spiked models. The note claims that G2 with a linear map is an affine condition plus a box, hence a lattice or hidden subset sum problem.
where: FS:exp/docs/notes/game-family-and-reduction-targets.md#§3 and §4
uses-to-state: def-three-maps
uses-to-prove: none
status: open
evidence: proposed, and the claim on G2 with a linear map has no proof.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.2, where it is named games-g1-to-g5. G2 covers leaked, federated or split gradients.

## conj-suliman-conjecture-false-when-noiseless
kind: conjecture
statement: In the noiseless cell of G2 with a linear map the LLL algorithm should win, so the conjecture of Suliman et al. is probably false for exact gradient matching and true only once noise, quantization or compounding of steps enters.
where: FS:exp/docs/notes/game-family-and-reduction-targets.md#§4 and §5
uses-to-state: def-games-g1-to-g5
uses-to-prove: none
status: open
evidence: a prediction, with the first experiment named in the note.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.2.

## conj-learning-adversary-bounded-by-learnability
kind: conjecture
statement: Halil's note conjectures a learning adversary, an adversary bounded by learnability rather than by distance in the input. The same note asks for adversary games in place of attack taxonomies and criticizes budgets measured as input distance.
alias: ideas-games-not-taxonomies
where: FS:exp/docs/notes/ideas.md
uses-to-state: none
uses-to-prove: none
status: open
evidence: informal, with no definition or proof.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.2 and 3.2, where the note is named ideas-games-not-taxonomies.

## def-capability-vector
kind: definition
statement: The capability vector kappa records what the adversary observes, when, how much, and whether passively or by choosing. It generalizes the CPA handle.
where: FS:exp/docs/notes/intro-computational-security-of-learning.md#§1 and §4
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, proposed, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.2.
  - 2026-10-25 overlaps def-interface-view and def-interface-choices of HE-ML, which split the same content into what the adversary sees through channels and what it sets.

## def-baseline-adversary-kappa-zero
kind: definition
statement: The baseline adversary kappa zero holds only prior and public knowledge.
where: FS:exp/docs/notes/intro-computational-security-of-learning.md#§4
uses-to-state: def-capability-vector
uses-to-prove: none
status: proven
evidence: a definition, proposed, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.2.

## def-game-observation-target-success
kind: definition
statement: A game is fixed by an observation map O, a target T, a success functional S and a baseline adversary kappa zero. The adversary class enters only at reduction time.
where: FS:exp/docs/notes/game-family-and-reduction-targets.md#§1
uses-to-state: def-baseline-adversary-kappa-zero, def-adversary-class
uses-to-prove: none
status: proven
evidence: a definition, proposed, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-07-26 proposed.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.2.

# FORMAL_SECURITY programme, Chapter 24

## def-abstract-learning-machine
kind: definition
statement: A learning system is a source, a learner and advice. The source Pi is a program for the universal machine U on a uniform seed rho, and every distributional assumption must live in it. The learner L reads Pi through access modes, independent draws, membership queries, statistical queries or chosen inputs, and writes advice w. Inference runs U on w for t_eval steps, so the model is U(w, ·). Linear regression and a large language model are one machine at two coordinates of advice length and inference time.
alias: abstract-machine
where: FS:exp/docs/notes/chapter-24.md#message 1, summary in message 21
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents, and its human principal never ticked the prose consent box.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.3 and 3.3, where it is named abstract-machine. Messages 3 and 6 put all randomness on a canonical seed tape rho supplied by the channel and define access modes by how the channel couples the learner to rho.
  - 2026-10-25 overlaps def-learning-oracle of HE-ML. Here the seed is part of the source and access modes couple the learner to it, while there the seed is an argument of each Train call that a caller may name.

## def-demote-the-distribution
kind: definition
statement: Principle (3) of Chapter 24 demotes the distribution from foundation to parameter. No primitive names a distribution, and a distribution is the pushforward of the uniform law under the source Pi.
where: FS:exp/docs/notes/chapter-24.md#message 1
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: proven
evidence: a methodological law stated as a definition, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.3 and 3.3.

## def-behavioural-distance-d-r
kind: definition
statement: The behavioural distance d_R(w, Pi) is the size, under a query-region metric R, of the region where eval(w, ·) disagrees with Pi.
where: FS:exp/docs/notes/chapter-24.md#message 1
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.3. R here is the query-region metric, one of three meanings of R in the programme.

## def-one-surface-two-frontiers
kind: definition
statement: Risk* of a task, handles kappa and a budget r is the infimum of expected task loss over players with those handles and that budget, read with an aggregation among expectation, quantile and supremum, and with a base. Chapter 24 claims that this one functional gives accuracy, detection, security and privacy as its corners, and that a security theorem is a learning lower bound for the attack task under the adversary's handles.
where: FS:exp/docs/notes/chapter-24.md#messages 1, 7 and 21
uses-to-state: def-abstract-learning-machine, def-capability-vector
uses-to-prove: none
status: open
evidence: a definition and a thesis. The thesis has no proof.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.3 and 3.3.

## def-learn-kappa-class
kind: definition
statement: LEARN_kappa of s, t, advice length and epsilon is the class of source families learnable with those resources under handles kappa. Reductions between source families are its native operation.
where: FS:exp/docs/notes/chapter-24.md#message 1
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.3 and 3.3.

## prop-positioning-law
kind: proposition
statement: Statistical learning is LEARN_kappa modulo distributional equivalence, and a gap between computational and statistical learning is a fiber of that quotient.
where: FS:exp/docs/notes/chapter-24.md#message 5, about line 996
uses-to-state: def-learn-kappa-class
uses-to-prove: none
status: open
evidence: stated as a quotient with no proof.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## def-learner-source-membrane
kind: definition
statement: The membrane is the boundary across which the learner reads the source. It splits resources into a deploy side and a source side, and its closure carries the agentic loop.
where: FS:exp/docs/notes/chapter-24.md#messages 5 to 21
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.3.

## def-tau-staircase
kind: definition
statement: The tau-staircase orders three thresholds of a task, tau_stat at most tau_detect at most tau_recover, at which the task becomes statistically determined, detectable and recoverable.
where: FS:exp/docs/notes/chapter-24.md#messages 5 and 21
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.3.

## prop-staircase-provability-gradient
kind: proposition
statement: Below tau_stat security is unconditional, by the floor of statistical queries. The recovery band is equivalent to one-way functions, and the detection band is open, tied to Gap-Kt. Phase 3 added a rung of idealized models, the generic language model, the random oracle model and the generic group model, between the floor of statistical queries and one-way functions, with the caveat of Canetti, Goldreich and Halevi.
where: FS:exp/docs/notes/chapter-24.md#message 5, about line 980, and messages 31 and 32
uses-to-state: def-tau-staircase
uses-to-prove: none
status: open
evidence: agreed in the dialogue with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## def-lipschitz-sensitivity-modulus
kind: definition
statement: Lambda is a Lipschitz sensitivity modulus, with instances for training, for evaluation, for curation, and for the supremum over evaluation.
where: FS:exp/docs/notes/chapter-24.md#messages 7, 14 and 31
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.3.

## def-learner-randomness-budget
kind: definition
statement: H_L is the learner's randomness, a metered entropy budget and a core resource of the learning machine.
where: FS:exp/docs/notes/chapter-24.md#message 7
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.3.
  - 2026-10-25 overlaps def-learning-oracle of HE-ML. Here learner randomness is a metered budget, while there the seed has an atomless law, a caller may name it, and nothing meters its entropy.

## def-forward-and-reverse-information
kind: definition
statement: I is the forward information across the membrane, which is learning, and I reverse is the reverse information across it, which is steering.
where: FS:exp/docs/notes/chapter-24.md#message 20
uses-to-state: def-learner-source-membrane
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.3.

## thm-keystone-universal-equals-generalizing
kind: theorem
statement: Under the hypothesis that the forward information I is much smaller than s, the learner that minimizes Kt(w) is both universal, by Levin search, and generalizing, by Occam's razor. The bridge is that Kt(w) is at most about Kt(L) plus I plus the logarithm of the training time.
where: FS:exp/docs/notes/chapter-24.md#messages 7 and 8, about lines 1340 and 1432, verdict in message 26
uses-to-state: def-abstract-learning-machine, def-forward-and-reverse-information
uses-to-prove: none
status: proven
evidence: recorded as proved in the dialogue, messages 7 and 8, with the verdict in message 26.
checked-by: unchecked. The proof is the dialogue's, with no person's review.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3, where it is named keystone-universal-equals-generalizing.

## prop-capacity-is-kt
kind: proposition
statement: Kt(w) governs generalization and the raw advice length governs robustness lower bounds, so overparameterization is the regime where Kt(w) is much smaller than the advice length.
where: FS:exp/docs/notes/chapter-24.md#message 7
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: open
evidence: agreed in the dialogue with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## conj-gen-gap-is-comp-stat-fiber
kind: conjecture
statement: The proposal identified the generalization gap with the fiber of the quotient between computational and statistical learning.
alias: gen-gap-is-not-the-comp-stat-fiber
where: FS:exp/docs/notes/chapter-24.md#message 8, about line 1447
uses-to-state: prop-positioning-law
uses-to-prove: none
status: refuted
evidence: the generalization gap persists under unbounded computation and the fiber does not.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3, where the refutation is named gen-gap-is-not-the-comp-stat-fiber.

## prop-privacy-is-the-master-modulus
kind: proposition
statement: The composition modulus is at most the privacy modulus, so a private learner is composable and generalizing, and the converse fails. Chapter 24 reads this as the complexity form of the arrow from differential privacy to stability to generalization of Dwork, Feldman, Hardt, Pitassi, Reingold and Roth.
where: FS:exp/docs/notes/chapter-24.md#message 7
uses-to-state: def-lipschitz-sensitivity-modulus
uses-to-prove: none
status: open
evidence: accepted in the dialogue with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-h-l-shared-randomness
kind: proposition
statement: One noise budget H_L buys privacy on the training side and certified robustness on the deployment side.
where: FS:exp/docs/notes/chapter-24.md#message 7
uses-to-state: def-learner-randomness-budget
uses-to-prove: none
status: open
evidence: accepted in the dialogue with no proof recorded. Whether it survives an adaptive adversary with a joint pi is open.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-interaction-principle
kind: proposition
statement: Interaction buys power exactly when a cooperative unbounded party exists, and never against a hiding adversary.
where: FS:exp/docs/notes/chapter-24.md#message 7, about line 1323
uses-to-state: none
uses-to-prove: none
status: open
evidence: accepted in the dialogue with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## thm-inference-aperture-incompressibility
kind: theorem
statement: The advice length plus the number of bits recomputable within t_eval steps is at least one minus the entropy H(epsilon), times m, minus a term of order log m, with m the task size of message 23. For labels independent of the queries this gives advice length at least one minus H(epsilon) times m for every t_eval, and it predicts that context substitutes for weights.
where: FS:exp/docs/notes/chapter-24.md#message 23, about line 3290, verdict in message 26
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: proven for the sharp end, recorded as unconditional. Open, the smooth tradeoff for compressible natural tasks, plausibly as hard as a circuit lower bound.
evidence: recorded in message 23 with the verdict in message 26.
checked-by: unchecked. The proof is the dialogue's, with no person's review.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-comp-stat-envelope
kind: proposition
statement: On scaling exponents, the computational exponent is at most an envelope function Phi of the data exponent. The envelope is derived from the keystone, so one point above it falsifies the keystone.
where: FS:exp/docs/notes/chapter-24.md#messages 24 to 27
uses-to-state: none
uses-to-prove: thm-keystone-universal-equals-generalizing
status: open
evidence: testable and unmeasured.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3. Phi here is the envelope, one of four meanings of Phi in the programme.

## prop-separation-discipline
kind: proposition
statement: Keeping the statistical and the computational axes apart forbids the field's standard false unifications.
where: FS:exp/docs/notes/chapter-24.md#message 26
uses-to-state: none
uses-to-prove: none
status: open
evidence: methodology agreed in message 26, recorded as evidence of faithfulness and not of new content.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## conj-supply-chain-undetectable-backdoor
kind: conjecture
statement: Under one-way functions, a backdoor planted in an upstream model by the construction of Goldwasser et al. reaches a downstream composite with an effect scaled by the product of inference sensitivities, and no bounded downstream auditor below tau_recover detects it.
where: FS:exp/docs/notes/chapter-24.md#message 15, line 2458
uses-to-state: def-lipschitz-sensitivity-modulus, def-tau-staircase
uses-to-prove: none
status: open
evidence: a theorem candidate, F-4, with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-provenance-over-detection
kind: proposition
statement: Detection fails against constructions that stay undetectable under white-box access, and the working defence is attested provenance, the checker-verifier proof system pointed at the training transcript.
where: FS:exp/docs/notes/chapter-24.md#messages 16 and 17
uses-to-state: none
uses-to-prove: none
status: open
evidence: accepted in the dialogue as F-5 with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## def-backdoor-reproduction-number
kind: definition
statement: The reproduction number R of a backdoor across retraining generations is the product of the training sensitivity, the curation sensitivity, the supremum of the evaluation sensitivity and the hit rate rho_hit.
where: FS:exp/docs/notes/chapter-24.md#messages 20 and 31
uses-to-state: def-lipschitz-sensitivity-modulus
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.3 and 3.3. R also names the criterion of def-r-as-quantizer.

## prop-backdoor-propagation-window
kind: proposition
statement: A backdoor heals geometrically when R is below one and propagates when R is above one. A backdoor that both propagates and evades detection exists only when rho_hit lies between one over the product of the training sensitivity and the supremum evaluation sensitivity, and the detection rate rho_detect. This window is nonempty only in the detection band.
where: FS:exp/docs/notes/chapter-24.md#messages 20 and 31
uses-to-state: def-backdoor-reproduction-number, def-tau-staircase
uses-to-prove: none
status: open
evidence: containment stated as a proposition with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3, inside the item backdoor-reproduction-number.

## def-steering-align
kind: definition
statement: align is the reverse information minus the poisoning budget, over their sum. Chapter 24 states that align fixes the sign of the performative gap and that R fixes its persistence.
where: FS:exp/docs/notes/chapter-24.md#message 20
uses-to-state: def-forward-and-reverse-information, def-backdoor-reproduction-number
uses-to-prove: none
status: open
evidence: finalized in the dialogue. The claims on the sign and the persistence of the gap have no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3, where it is named steering-align.

## def-judge-budget
kind: definition
statement: r_judge is the budget of a judge, bounded by the machine U, that approximates a predicate.
where: FS:exp/docs/notes/chapter-24.md#message 28
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.3.

## def-clean-r
kind: definition
statement: Clean_r(w, Pi) holds when no input x with Kt(x) at most r exists on which a judge of budget r separates eval(w, x) from Pi(x).
where: FS:exp/docs/notes/chapter-24.md#message 20
uses-to-state: def-judge-budget
uses-to-prove: none
status: proven
evidence: a definition, agreed in the dialogue, and nothing is claimed beyond it.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.3.

## conj-op1-robust-comp-stat-gap
kind: conjecture
statement: Open problem 1 of Chapter 24 asks whether the computational value of the robust-learning game lies strictly below its statistical value. The statistical value is finite exactly when the robust-PAC dimension is finite (Montasser, Hanneke and Srebro 2019), and the question reduces to average-case Gap-Kt.
where: FS:exp/docs/notes/chapter-24.md#message 20, line 2993
uses-to-state: none
uses-to-prove: none
status: open
evidence: posed as an open problem.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## conj-op2-trusted-prover-inherence
kind: conjecture
statement: Open problem 2 of Chapter 24 asks whether certifying Clean_r needs an unbounded prover outside the subclass at the floor of statistical queries. A yes would show that freedom from backdoors is not self-certifiable.
where: FS:exp/docs/notes/chapter-24.md#message 20, line 3003
uses-to-state: def-clean-r
uses-to-prove: none
status: open
evidence: posed as an open problem.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-op3-composable-provenance
kind: proposition
statement: Process provenance is an NP statement that composes by proof-carrying data, and cleanness provenance is a coNP statement that equals open problem 2.
where: FS:exp/docs/notes/chapter-24.md#message 17, about line 2740, and messages 18 and 19
uses-to-state: def-clean-r
uses-to-prove: conj-op2-trusted-prover-inherence
status: open
evidence: proposed in message 17 with no proof, then deflated into conj-op2-trusted-prover-inherence in messages 18 and 19.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-aioracle-and-chapter-24-two-layers
kind: proposition
statement: The AIOracle framework of Villa, Durak, Kohno, Maharramli and Roesner is the interface layer and Chapter 24 is the foundation, joined where the AIOracle predicate meets the pair of task and judge budget.
where: FS:exp/docs/notes/chapter-24.md#messages 28 to 32
uses-to-state: def-judge-budget
uses-to-prove: none
status: open
evidence: a phase 3 verdict of unification with no proof.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: needs-oracle. It concerns the AIOracle framework and its generic language model.
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-three-term-composition-law
kind: proposition
statement: A composed breach has an additive probability epsilon, an additive coverage mismatch e from the AIOracle side, and a multiplicative amplification Lambda. So the additive AIOracle bound holds only when the supremum of Lambda is at most one.
where: FS:exp/docs/notes/chapter-24.md#messages 28 to 32, FS:exp/docs/notes/LearningSystemsAsMachines_for_Practitioners.html#§9
uses-to-state: def-lipschitz-sensitivity-modulus
uses-to-prove: none
status: open
evidence: agreed in the dialogue with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: needs-oracle. It says when a bound proved in the AIOracle model transfers to a composition.
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## conj-margin-gated-alignment-tax
kind: conjecture
statement: Internalizing a predicate raises boundary sensitivity only for predicates with a small margin.
where: FS:exp/docs/notes/chapter-24.md#messages 31 and 32
uses-to-state: none
uses-to-prove: none
status: open
evidence: a conjecture called measurable, with no measurement recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## conj-intent-authorization-design-law
kind: conjecture
statement: Authorization conditioned on inferred intent costs Kt of the intent source, so an agent is either blind to intent or elicits it.
where: FS:exp/docs/notes/chapter-24.md#messages 31 and 32
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: open
evidence: a prediction with no proof.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-curation-controls-r
kind: proposition
statement: The curation box C controls two of the four factors of the reproduction number R, so attesting the selection step is the strongest lever for containment.
where: FS:exp/docs/notes/chapter-24.md#messages 31 and 32
uses-to-state: def-backdoor-reproduction-number
uses-to-prove: none
status: open
evidence: agreed in the dialogue with no proof recorded.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## prop-glm-rung-is-heuristic
kind: proposition
statement: The MID bound of AIOracle, a success probability at most one half plus n times epsilon, proved inside a generic language model, is a heuristic guarantee.
where: FS:exp/docs/notes/chapter-24.md#message 32
uses-to-state: none
uses-to-prove: none
status: heuristic
evidence: assumes that the uninstantiability caveat of Canetti, Goldreich and Halevi for the random oracle model carries to the generic language model. Recorded by the agent lödeg.
checked-by: unchecked. Chapter 24 is a dialogue of two agents.
oracle: needs-oracle. It grades a bound proved inside an idealized language model.
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

## def-noiseless-leakage-metric
kind: definition
statement: The advice length minus Kt(w) is proposed as a computational leakage metric.
where: FS:exp/docs/notes/LearningSystemsAsMachines_for_Practitioners.html#§8
uses-to-state: def-abstract-learning-machine
uses-to-prove: none
status: proven
evidence: a proposal of a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.3.

# FORMAL_SECURITY programme, SQ proof note

## thm-sq-hardness-black-box-attacks
kind: theorem
statement: Let a deterministic learner be implementable from q_L statistical queries of tolerance tau_L, and train it on the vertex-row encoding of a planted-clique graph. Then the distinguishing advantage of any black-box adversary is at most the distinguishing advantage of statistical queries at q_L and tau_L, whatever the adversary's own query count. Remarks specialize the bound to attribute inference, backdoor activation, membership and extraction, and treat randomized learners with public or private coins, with the bound unchanged.
where: FS:.tools/proof.tex
uses-to-state: none
uses-to-prove: none
status: refuted
evidence: Refuted by counterexample in HE-ML:lab/theory/spaces/computational-limits/round-00/builder.md#thm-fs-sq-black-box-reduction. With the exact oracle, or an honest oracle
  averaging each query over 32 n^2 ln n fresh draws, a learner with O(n^2) queries of tolerance 1/3 stores every row,
  and an unbounded adversary reading the model decides the planted clique with advantage 1 - o(1) at k = n^(1/2 - delta).
  The proof applies FGRVX17 to the empirical law of one graph's rows and chains a worst-oracle bound with one oracle's run.
  Old evidence: a full proof in the note, which simulates the learner from answers to statistical queries.
checked-by: astra, round 00 of the space computational-limits, line by line, 2026-10-25, and the integrator's re-derivation.
  Not checked by Halil.
oracle: holds-without-oracle. Statistical queries model the learner's access to data, and the bound holds for every real learner of that kind.
history:
  - 2026-04-23 written as a proof note.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.4, where it is named sq-hardness-black-box-attacks. The note quotes FGRVX17 as Theorem 1.1 in the form q times tau squared at least Omega of n to the 2 delta, while the later, re-verified oracle draft quotes the parameters of FGRVX17 Theorem 2.9.
  - 2026-10-25 overlaps thm-black-box-certifiability of HE-ML. Both bound a black-box adversary whatever its own computation, this one through the learner's statistical-query access and that one through strategy trees on a finite query set.
  - 2026-10-25 refuted as stated, status proven to refuted. The booklet names it thm-fs-sq-black-box-reduction, kept
    here as an alias. What survives is lem-sq-learner-post-processing.
  - 2026-10-25 The note's Brennan and Bresler pointer is wrong. BB20 carries its SQ bounds for the secret-leakage
    variant in Section 12.3, Corollaries 12.17 and 12.18, for specific leakage laws, not in a Theorem 5.1. Source
    HE-ML:lab/theory/spaces/computational-limits/round-00/builder.md#thm-fs-sq-black-box-reduction.
alias: thm-fs-sq-black-box-reduction

# FORMAL_SECURITY programme, parked survey formalization

## def-training-recipe
kind: definition
statement: A recipe is a public training procedure, fixed by architecture, loss, optimizer, batch rule, initialization rule, step count and internal noise, which fixes a step function.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#Def Recipe
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-08-22 dated with the parked formalization, which is not part of the submission.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.
  - 2026-10-25 overlaps def-interface-learning-function of HE-ML, which keeps loss, optimizer and step count internal and unnamed, while a recipe names them in public.

## def-training-trace
kind: definition
statement: A trace is the initial weights w_0 followed, for each step t up to T, by the batch B_t, the gradient g_t and the weights w_t. It records everything that happened in training.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#Def Trace
uses-to-state: def-training-recipe
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## def-passive-learning-oracle
kind: definition
statement: On a corpus, the passive learning oracle draws fresh coins, runs a recipe that the game names, and returns the trace. Two calls on one corpus return independent traces. Parties do not author recipes, which blocks a wrapping recipe that collapses the step count and a laundering recipe whose initialization emits precomputed weights. A game whose theorems depend on the meter must use initializations that carry no information a party chose.
alias: passive-oracle-and-named-recipes
where: FS:exp/survey/paper/parked/formalization/oracle.tex#Defs Passive learning oracle and Metered cost
uses-to-state: def-training-recipe, def-training-trace
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-08-22 agreed as the learning oracle of the survey, which idealizes only the training map, outputs the full trace and forbids recipes authored by parties.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.4 and 3.5, where it is named passive-oracle-and-named-recipes.
  - 2026-10-25 overlaps def-learning-oracle of HE-ML. This oracle draws fresh coins on every call and lets no party name a seed or author a recipe, while that oracle lets a caller rerun training at a named seed.

## prop-learning-oracle-accounting-device
kind: proposition
statement: The parked learning oracle idealizes the training map and nothing else, returns the full trace and manufactures no hardness. Every lower bound comes from what the views withhold, and every bound counts oracle steps and not time.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#sections 2, 5 and 8
uses-to-state: def-passive-learning-oracle, def-training-trace, def-oracle-view-of-trace
uses-to-prove: none
status: open
evidence: an agreed framing with no proof.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: needs-oracle. Its bounds count oracle steps.
history:
  - 2026-08-22 agreed with the plan of the survey tasks, Part IV.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named learning-oracle-accounting-device.

## def-oracle-view-of-trace
kind: definition
statement: A view is a public, possibly lossy function of a trace, or a stateful query interface with a budget. It is a parameter of the game and never a feature of the oracle.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#Def View
uses-to-state: def-training-trace
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.
  - 2026-10-25 overlaps def-interface-view of HE-ML, which is everything the adversary receives through its channels and its queries, while this view is one granted function of the trace.

## prop-gradients-plus-initialization-determine-the-model
kind: proposition
statement: For a recipe whose step factors through gradients, the final weights are a function of the initial weights and the per-step quantities. So a view that grants both grants the model.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#Views
uses-to-state: def-training-recipe, def-training-trace, def-oracle-view-of-trace
uses-to-prove: none
status: proven
evidence: the Fact of the section Views of oracle.tex.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: holds-without-oracle. It is a property of gradient-factoring recipes in real training.
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named fact-gradients-plus-initialization-determine-the-model.

## def-recipe-noise-is-not-view-noise
kind: definition
statement: Noise of DP-SGD inside the recipe and channel noise inside a view are different objects.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#Views
uses-to-state: def-training-recipe, def-oracle-view-of-trace
uses-to-prove: none
status: proven
evidence: definitional, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

## def-interactive-oracle-and-ports
kind: definition
statement: In the interactive form the oracle runs one training step per call, with parties attached to ports. Federated clients and the split-learning cut are ports, attaching a party gives it a read and a write, and passive observation is attachment for reading only. The passive oracle is the special case with no party attached.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#interactive form
uses-to-state: def-passive-learning-oracle
uses-to-prove: none
status: proven
evidence: definitions, and the fact that the passive oracle is the special case is proven in the same section.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.4 and 3.5.

## def-read-and-write-budgets
kind: definition
statement: A read budget is the metered oracle cost a party may spend. A write budget is what a party may change, the number of steps and the metric distance by which it may deviate at a port. Poisoning fractions and the deviations of malicious clients are write budgets.
alias: two-budgets
where: FS:exp/survey/paper/parked/formalization/oracle.tex#Defs Metered cost and Write budget
uses-to-state: def-interactive-oracle-and-ports
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.4 and 3.5, where it is named two-budgets.
  - 2026-10-25 overlaps def-bounded-deviation-strategy of HE-ML, which bounds only the norm of additive inputs to Gaussian releases, while a write budget bounds steps and metric distance at any port.

## def-game-declaration
kind: definition
statement: A declaration is what a game asserts about the recipe's outputs, the target family with its unit, and the data noise.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#The adversary class
uses-to-state: def-training-recipe
uses-to-prove: none
status: open
evidence: defined with its content left open.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## def-game-skeleton-and-criteria
kind: definition
statement: A game names a recipe, attachments, views, budgets, a declaration, an optional secret with min-entropy h, a criterion and a baseline. The criterion is distinguish or produce. Membership, differential privacy and undetectability are distinguish games, reconstruction, extraction and forgery are produce games, and a backdoor game is both.
where: FS:exp/survey/paper/parked/formalization/oracle.tex
uses-to-state: def-training-recipe, def-oracle-view-of-trace, def-read-and-write-budgets, def-game-declaration
uses-to-prove: none
status: proven
evidence: definitions, and nothing is claimed beyond them.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.
  - 2026-10-25 overlaps def-distinguish-goal, def-invert-goal and def-steer-goal of HE-ML. HE-ML has three goals with steering on its own, while this skeleton has two criteria and puts a backdoor under both.

## prop-worlds-must-differ
kind: proposition
statement: If the two worlds of a game induce the same law of the view, every advantage is zero.
where: FS:exp/survey/paper/parked/formalization/oracle.tex
uses-to-state: def-game-skeleton-and-criteria
uses-to-prove: none
status: proven
evidence: proven in oracle.tex.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: holds-without-oracle. It is a statement about laws of views.
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named fact-worlds-must-differ.

## def-view-generic-adversary
kind: definition
statement: A view-generic adversary touches corpus, training and model only through granted views within budgets and computes freely otherwise. Genericity is relative to the granted views, an attack is classified by the weakest view it needs and the queries it spends there, and the dichotomy between generic and structural adversaries is dropped.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#Def View-generic adversary
uses-to-state: def-oracle-view-of-trace, def-read-and-write-budgets
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.4 and 3.5.
  - 2026-10-25 overlaps def-learning-oracle-model of HE-ML, whose adversary reaches training only through oracle calls and is unbounded unless a statement bounds it, while this adversary is limited to granted views within budgets.

## conj-transfer-hypotheses
kind: conjecture
statement: Two hypotheses relative to a recipe. No skipping says the content of a trace is not obtainable below the work of the walk. No aiming says no inverse map from desired properties to weights is cheaper than learning.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#passive form, FS:exp/survey/paper/parked/formalization/price.tex
uses-to-state: def-training-recipe, def-training-trace
uses-to-prove: none
status: open
evidence: stated as hypotheses relative to the recipe, with no proof.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4. No skipping at the level of the task is refuted by recipe drift, by prop-price-of-skipping-is-recipe-relative.

## prop-locating-a-real-attack
kind: proposition
statement: If a deployed attack beats a proven floor, then its access exceeded the granted views, or its spend was understated, or some real procedure delivered a view below its modelled price. For training the last case means a broken transfer hypothesis.
where: FS:exp/survey/paper/parked/formalization/oracle.tex
uses-to-state: def-view-generic-adversary, conj-transfer-hypotheses
uses-to-prove: none
status: proven
evidence: proven in oracle.tex, as an audit of the model.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: holds-without-oracle. It relates floors in the oracle model to real attacks.
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named prop-locating-a-real-attack.
  - 2026-10-25 relates to thm-perfect-substitution of HE-ML, which shows the real procedure delivers exactly the bottom oracle's law, while this statement diagnoses a real attack that beats a floor.

## prop-query-bounded-corpus-auditor
kind: proposition
statement: In the backdoor game where the planter replaces the data distribution and the auditor sees the corpus through VSTAT(m), Theorem 2.9 of FGRVX17 prices detection for planted bipartite k-clique with k at most N to the power one half minus delta.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#The backdoor game
uses-to-state: def-backdoor-game-fixed-parts
uses-to-prove: none
status: proven
evidence: proven by specialization of FGRVX17, with four stated boundaries. The correspondence of VSTAT to the corpus is the model's reading, record-level and model-level auditors are not covered, and no claim is made that a planter meets non-triviality.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: needs-oracle. It is a lower bound counted in VSTAT queries.
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named prop-query-bounded-corpus-auditor.

## def-backdoor-game-fixed-parts
kind: definition
statement: The backdoor game has three roles. The planter has a write budget, the auditor a read budget, and the activator a secret of min-entropy h. The planter is generic, and the auditor detects rather than reconstructs and never holds the secret.
where: FS:exp/survey/paper/parked/formalization/oracle.tex#The backdoor game
uses-to-state: def-read-and-write-budgets, def-game-skeleton-and-criteria
uses-to-prove: none
status: proven
evidence: fixed as a definition, and nothing is claimed beyond it. Non-triviality of the game is open.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

## prop-price-of-aiming
kind: proposition
statement: Within recipes that are statistical-query algorithms the floor is unconditional, d to the power Omega(k) queries for a hidden k-sparse parity. Reading a fresh-batch gradient step as a correlational query of tolerance about one over the square root of the batch size is a heuristic simulation that every gradient use of a floor must carry. The generative exponent is the surviving unit, and the information exponent and the leap are not used.
where: FS:exp/survey/paper/parked/formalization/price.tex#The price of aiming
uses-to-state: def-training-recipe, conj-transfer-hypotheses
uses-to-prove: none
status: proven in the classes named, with the simulation of a gradient step by a correlational query heuristic
evidence: price.tex. The heuristic assumes that one fresh-batch gradient step acts as one correlational query of that tolerance.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: needs-oracle. The floor is counted in statistical queries.
history:
  - 2026-08-28 the record of price.tex adds the exponent results that support the choice of the generative exponent.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

## prop-price-of-skipping-is-recipe-relative
kind: proposition
statement: No skipping at the level of the task is refuted by recipe drift. No skipping at the level of the recipe is the strongest defensible form, and no lower bound over all algorithms exists.
where: FS:exp/survey/paper/parked/formalization/price.tex#The price of skipping
uses-to-state: conj-transfer-hypotheses
uses-to-prove: none
status: open
evidence: recorded as open, and it sits under every claim that prices compute.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

## def-amortization-is-not-skipping
kind: definition
statement: Distillation draws on a teacher's paid trace, so amortization over a paid trace is not skipping.
where: FS:exp/survey/paper/parked/formalization/price.tex
uses-to-state: def-training-trace, conj-transfer-hypotheses
uses-to-prove: none
status: proven
evidence: definitional in the model, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

## def-view-price-versus-trace-price
kind: definition
statement: The price of a view is not the price of the trace it is drawn from. A sound proof-of-learning is a view whose price equals the price of the trace.
alias: price-of-a-view-is-not-the-price-of-the-trace
where: FS:exp/survey/paper/parked/formalization/price.tex
uses-to-state: def-oracle-view-of-trace, def-training-trace
uses-to-prove: none
status: proven
evidence: definitional in the model, and nothing is claimed beyond it. Whether a sound proof-of-learning exists is open.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named price-of-a-view-is-not-the-price-of-the-trace.
  - 2026-10-25 relates to thm-replay-audit-steer of HE-ML, which bounds steering under a replay at a random-oracle seed by the reach, while this definition asks a proof-of-learning view to cost what the trace costs.

## prop-sparse-parity-experiment
kind: proposition
statement: A two-layer ReLU network of width 100, trained by SGD with momentum 0.9, batch 128 and learning rate 0.01 on fresh samples of a hidden 3-sparse parity, reached 0.90 test accuracy in all 40 runs, 8 seeds at each d in 20, 30, 40, 50 and 60. The median step count was 1025 at d 20 and 9337.5 at d 60, a log-log slope of 2.02 over a factor-three range with consecutive slopes from 0.8 to 3.0. A probe with batch 8, width 512 and learning rate 0.1 had median 6940 at d 30, and nine runs at d of 60 or more hit the cap of 300000 steps.
where: FS:exp/survey/lab/results/sparse-parity/manifest.yml
uses-to-state: none
uses-to-prove: none
status: empirical
evidence: the 40 runs and the probe recorded in the manifest. Parked and unused.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

## prop-probe-collapses
kind: proposition
statement: In an extraction game where the adversary may choose a probe near a queried point, with L times delta at most epsilon, one query wins with probability one.
where: FS:exp/survey/paper/parked/formalization/games.tex
uses-to-state: def-extraction-advantage
uses-to-prove: none
status: proven
evidence: proven in games.tex.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named prop-probe-collapses.

## def-extraction-advantage
kind: definition
statement: The extraction advantage subtracts a baseline that maximizes over model-free algorithms given the model family and the challenge set, so no baseline can hard-wire f.
where: FS:exp/survey/paper/parked/formalization/games.tex
uses-to-state: def-baseline-of-r
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

## prop-raw-success-is-not-a-measurement
kind: proposition
statement: A model-free baseline can beat a published attack, so raw success is not a measurement.
where: FS:exp/survey/paper/parked/formalization/games.tex
uses-to-state: def-extraction-advantage
uses-to-prove: none
status: empirical
evidence: established for membership inference only, by Das, Zhang and Tramèr and by Meeus et al.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named prop-raw-success-is-not-a-measurement.

## prop-unseparated-challenges-collapse
kind: proposition
statement: Challenges inside a known ball of radius rho with L times rho at most epsilon are won by one query. The repairs are challenge distributions that are Delta-separated and h-unpredictable, and both are required.
where: FS:exp/survey/paper/parked/formalization/games.tex
uses-to-state: def-extraction-advantage
uses-to-prove: none
status: proven
evidence: proven in games.tex. The two repairs are definitions.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named prop-unseparated-challenges-collapse.

## prop-search-implies-decision
kind: proposition
statement: A search adversary with success p yields a distinguisher with advantage half the absolute difference between p and the quantity q that games.tex defines.
where: FS:exp/survey/paper/parked/formalization/games.tex
uses-to-state: def-extraction-advantage
uses-to-prove: none
status: proven
evidence: proven in games.tex. The polynomial-time converse is open.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named prop-search-implies-decision.

## def-delta-extraction-hardness
kind: definition
statement: Extraction is delta-hard when every adversary with cost below k(n) to the power 1 plus delta evaluations has negligible extraction advantage.
where: FS:exp/survey/paper/parked/formalization/games.tex
uses-to-state: def-extraction-advantage
uses-to-prove: none
status: proven
evidence: a definition in the first fine-grained convention, with three cautions, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

## prop-stealing-implies-answering
kind: proposition
statement: Winning Steal_rho under the supremum distance on the support of the challenges wins the challenge game. The converse needs a covering condition and is open.
where: FS:exp/survey/paper/parked/formalization/games.tex
uses-to-state: def-extraction-advantage
uses-to-prove: none
status: proven
evidence: proven in games.tex.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5, where it is named prop-stealing-implies-answering.

## def-challenge-generator-as-oracle
kind: definition
statement: The adaptive challenge generator is an auxiliary AIOracle whose cost must sit in the honest budget.
where: FS:exp/survey/paper/parked/formalization/games.tex#The challenge generator as an oracle
uses-to-state: def-extraction-advantage
uses-to-prove: none
status: proven
evidence: a proposal of a definition, and nothing is claimed beyond it.
checked-by: adversarial review of the parked formalization through 2026-08-28, as the digest records it. No person's review is recorded.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.5.

# FORMAL_SECURITY programme, AI oracle thread of 2026-10-13

## def-version-space-oracle
kind: definition
statement: For a sample S, the version space V(S) is the set of hypotheses consistent with S, and the version-space oracle outputs a hypothesis drawn uniformly from it.
where: FS:exp/survey/lib/reports/src/2026-10-13-halil-version-space-oracle.tex
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-13 defined in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## prop-version-space-oracle-advantage
kind: proposition
statement: Let the oracle output a hypothesis drawn uniformly from the version space of the training set, and let the adversary know the other n minus one points. The Bayes-optimal adversary depends on the hypothesis only through its labels at the two challenge points, and its advantage is one minus the smaller of r_0 and r_1, where r_i is the probability that a model trained with z_i labels the other challenge correctly.
where: FS:exp/survey/lib/reports/src/2026-10-13-halil-version-space-oracle.tex
uses-to-state: def-version-space-oracle
uses-to-prove: none
status: proven
evidence: proven in the report, elementary. Its recorded consequences are that utility sets leakage, that two black-box queries reach the white-box optimum, and that computation enters only through a step that compares the sizes of the two version spaces. The hardness of that step for natural classes is open, and for rich classes it is a heuristic expectation. The oracle is the zero-temperature case of SDSOJ19.
checked-by: unchecked
oracle: needs-oracle. It holds for the idealized version-space learner.
history:
  - 2026-10-13 proven in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6, where it is named version-space-oracle-advantage.

## def-generic-training-oracle
kind: definition
statement: A training oracle in the style of the generic group model keeps handles to parameter vectors and offers train on a training set, which returns a fresh handle, eval, a gradient in the input, a gradient in the parameters, and reveal. The challenger plays a membership game on a handle, and the definition carries a utility condition alpha.
where: FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-13 defined in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6, where it is named generic-training-oracle.
  - 2026-10-25 overlaps def-learning-oracle of HE-ML. Its train call returns a fresh handle and its training randomness is never opened, while that oracle stores, names and opens seeds and lets a caller rerun training at one.

## def-oracle-access-class
kind: definition
statement: An access class is a set of oracle operations, among train, eval, the input gradient, the parameter gradient and reveal, with a budget on each. Black-box access is eval alone, shadow models add train, and white-box access is reveal.
where: FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex
uses-to-state: def-generic-training-oracle
uses-to-prove: none
status: proven
evidence: a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-13 defined in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.
  - 2026-10-25 overlaps def-learning-oracle of HE-ML, whose labels eval and open give black-box and white-box access per name, while Train there stays open to every caller with no budget under the bottom oracle.

## def-ideal-representation
kind: definition
statement: Ideal representation holds when, conditioned on the learned function, the parameters are independent of the training set.
where: FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex
uses-to-state: def-generic-training-oracle
uses-to-prove: none
status: proven
evidence: an assumption stated as a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-13 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## prop-ideal-representation-equalizes-white-box
kind: proposition
statement: Under ideal representation the best unbounded white-box advantage equals the best unbounded advantage of an attacker that sees only the function.
where: FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex
uses-to-state: def-ideal-representation
uses-to-prove: none
status: proven
evidence: by data processing on total variation, in the report.
checked-by: unchecked
oracle: needs-oracle. It holds under the idealization of ideal representation.
history:
  - 2026-10-13 proven in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6, where it is named ideal-representation-equalizes-white-box.
  - 2026-10-25 overlaps thm-black-box-certifiability of HE-ML, which certifies the label-only advantage for every learning function and shows that drawn seeds never certify its equality with the white-box advantage below one, while this statement makes the two equal by assumption.

## def-representation-leakage-and-extraction-cost
kind: definition
statement: Real training breaks ideal representation, and the gap between white-box and black-box advantage splits into an information part, the representation leakage, and a computational part, the extraction cost.
where: FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex
uses-to-state: def-ideal-representation
uses-to-prove: none
status: open
evidence: the source calls it a definition. Its premise that real training breaks ideal representation has no proof there, and prop-unlimited-queries-return-the-function shows it for one constructed learner.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-13 defined in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, sections 2.4 and 3.6.

## prop-ideal-representation-is-uninstantiable
kind: proposition
statement: An oracle with ideal representation is a virtual black-box obfuscator for trained functions, which is impossible in general by BGIRSVY01, so the model has the standing of a random oracle.
where: FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex
uses-to-state: def-ideal-representation
uses-to-prove: none
status: heuristic
evidence: an analogy. It assumes that the impossibility of general virtual black-box obfuscation carries to the class of trained functions.
checked-by: unchecked
oracle: holds-without-oracle. It is a statement about realizing the oracle with real training.
history:
  - 2026-10-13 stated in the report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6.

## prop-unlimited-queries-return-the-function
kind: proposition
statement: Parameters that affect no output give a white-box attacker information that an unbounded black-box attacker never sees, since unlimited queries return only the function.
where: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
uses-to-state: none
uses-to-prove: none
status: proven
evidence: by a trivial construction, in the issue.
checked-by: unchecked
oracle: holds-without-oracle. It holds for real learners.
history:
  - 2026-10-13 recorded in the issue.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6.

## def-necessary-leakage
kind: definition
statement: The necessary leakage at a utility level is the least leakage that every learner at that utility has.
where: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a recorded proposal of a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-13 recorded in the issue.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## def-achievable-leakage
kind: definition
statement: The achievable leakage at a utility level is the least leakage that some learner at that utility reaches.
where: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a recorded proposal of a definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-13 recorded in the issue.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## prop-achievable-leakage-bb-equals-wb
kind: proposition
statement: A learner can output a canonical description of its function, so the achievable leakage is the same for unbounded black-box and white-box attackers. The question of black-box against white-box free of learner choices is therefore an obfuscation question for learners.
alias: achievable-leakage-bb-equals-wb-when-unbounded
where: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
uses-to-state: def-achievable-leakage
uses-to-prove: none
status: proven
evidence: proven trivially in the issue.
checked-by: unchecked
oracle: holds-without-oracle. It holds for real learners.
history:
  - 2026-10-13 recorded in the issue.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6, where it is named achievable-leakage-bb-equals-wb-when-unbounded.

## prop-learner-choice-fixes-the-answer
kind: proposition
statement: The choice of learner fixes the answer to black-box against white-box. An arbitrary learner lets white-box win trivially, an idealized learner, Gibbs or version space, gives no gap, and for SGD on deep networks any gap is only empirical.
where: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
uses-to-state: none
uses-to-prove: prop-unlimited-queries-return-the-function, prop-version-space-oracle-advantage
status: open
evidence: a recorded diagnosis with no proof of its last clause.
checked-by: unchecked
oracle: needs-oracle for the half on idealized learners, which holds only for them.
history:
  - 2026-10-13 recorded in the issue.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6.

## prop-interface-does-not-bound-leakage
kind: proposition
statement: A training oracle that bounds leakage must fix the law of the returned function, and any such oracle makes white-box equal to black-box. The issue records Gibbs sampling at temperature T with loss in the unit interval as the exponential mechanism with epsilon two over T.
where: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
uses-to-state: def-generic-training-oracle
uses-to-prove: none
status: open
evidence: a recorded tension with no proof.
checked-by: unchecked
oracle: needs-oracle. It concerns what an idealized training oracle can bound.
history:
  - 2026-10-13 recorded in the issue.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6.
  - 2026-10-25 relates to thm-coupling-certificate of HE-ML, which bounds leakage by the coupled divergence, a quantity Train calls measure for every learning function, without fixing the law of the returned model.

## prop-gradient-attackers-are-first-order
kind: proposition
statement: Gradient-based attackers are attackers with a first-order oracle.
where: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
uses-to-state: none
uses-to-prove: none
status: heuristic
evidence: a reading of the attack literature. It assumes that the attacks use the model only through gradient queries.
checked-by: unchecked
oracle: needs-oracle. It models attackers by a first-order oracle.
history:
  - 2026-10-13 recorded in the issue.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6.

## prop-field-coding-2026-10-13
kind: proposition
statement: Of over 190 relevant works coded by five agents, 40 study concrete deep networks, 36 quantify over all learners, 30 assume differential privacy, one assumes a Gibbs posterior and none a version space. Seven treat training as an opaque call, four make gradient access a formal object, and ten contain calls to training. No attacker is a formal first-order class. Attackers are unbounded in 58 works, polynomial-time in 52 and one fixed algorithm in 33, and 47 of the 92 core works state no utility condition.
where: FS:exp/survey/lib/literature/ontology/views.md, FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
uses-to-state: none
uses-to-prove: none
status: empirical
evidence: on the coding of five agents, not on the papers.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-13 coded.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.6.

# FORMAL_SECURITY programme, survey

## def-survey-party
kind: definition
statement: The party of a work is whoever its main claim bounds, an attacker, a learner, an auditor, a mechanism, or nobody.
where: FS:exp/survey/CONTEXT.md, FS:exp/survey/lib/literature/codebook.md
uses-to-state: none
uses-to-prove: none
status: proven
evidence: a coding definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## def-survey-unit
kind: definition
statement: The unit of a bound is the resource it is stated in, one of time, circuit size, queries, samples, memory, algorithm class, perturbation, corruption and privacy budget.
where: FS:exp/survey/CONTEXT.md, FS:exp/survey/lib/literature/codebook.md
uses-to-state: def-survey-party
uses-to-prove: none
status: proven
evidence: a coding definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## def-survey-tightness
kind: definition
statement: Tightness grades how a bound is stated, as unstated, poly, quasi-poly, conditional, class, budget, exponent, relative or measured. A relative bound is a relation between two parties' work. An exponent is a bound stated as an exponent in one party's own resource. A budget is a numeric allowance such as a perturbation radius or a corruption fraction.
where: FS:exp/survey/CONTEXT.md, FS:exp/survey/lib/literature/codebook.md#Table 2
uses-to-state: def-survey-party, def-survey-unit
uses-to-prove: none
status: proven
evidence: a coding definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4. The budget here differs from def-adversary-resource-budget of the programme ledger.

## def-survey-assessed
kind: definition
statement: Assessed records whether a work treats its bound as its object or leaves it a side condition. It is Halil's axis.
where: FS:exp/survey/CONTEXT.md, FS:exp/survey/lib/literature/codebook.md#Table 2
uses-to-state: def-survey-tightness
uses-to-prove: none
status: proven
evidence: a coding definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## def-survey-near-miss
kind: definition
statement: A near miss is a work whose tightness and assessment disagree.
where: FS:exp/survey/CONTEXT.md
uses-to-state: def-survey-tightness, def-survey-assessed
uses-to-prove: none
status: proven
evidence: a coding definition, and nothing is claimed beyond it.
checked-by: unchecked
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 2.4.

## prop-classification-of-two-hundred-works
kind: proposition
statement: The survey classifies 200 formal works on the security and privacy of learning by the party each one bounds, the unit of that bound, and how tightly it is stated.
where: FS:exp/survey/lib/claims.yml#classification-of-two-hundred-works, FS:exp/survey/lab/results/corpus-classification/classification.tsv
uses-to-state: def-survey-party, def-survey-unit, def-survey-tightness
uses-to-prove: none
status: empirical
evidence: the coded corpus in the classification table, with its number in numbers.csv.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-evidence-layer-per-row
kind: proposition
statement: Every classified work carries the verbatim sentence that decided it, or the places checked before an absence was recorded, and each quotation was checked inside its own document. At round two, 155 of 172 quotations were bound inside their own document.
where: FS:exp/survey/lib/claims.yml#evidence-layer-per-row
uses-to-state: prop-classification-of-two-hundred-works
uses-to-prove: none
status: empirical
evidence: the per-row quotations of the classification and the quotation check of round two.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-resource-axis-absent-from-prior-systematizations
kind: proposition
statement: No prior systematization of machine-learning security records the resource a work bounds or the party it binds.
where: FS:exp/survey/lib/claims.yml#resource-axis-absent-from-prior-systematizations
uses-to-state: def-survey-party, def-survey-unit
uses-to-prove: none
status: empirical
evidence: a novelty claim, supported by the notes on the prior systematizations the register lists.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-most-formal-works-price-nobody
kind: proposition
statement: Of the 200 works, 37 state no resource bound on any party.
where: FS:exp/survey/lib/claims.yml#most-formal-works-price-nobody
uses-to-state: def-survey-party
uses-to-prove: none
status: empirical
evidence: the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-attack-works-price-nobody-more-often
kind: proposition
statement: Works that study a named attack bound no party more often than works drawn from cryptography and learning theory, in direction and not in size.
where: FS:exp/survey/lib/claims.yml#attack-works-price-nobody-more-often
uses-to-state: def-survey-party
uses-to-prove: none
status: empirical, narrowed
evidence: the coded corpus. On the theorem-bearing subset, 12 of 71 against 6 of 87, the interval on the difference runs from minus 0.2 to 20.2 and includes zero.
checked-by: unchecked here. The survey's claim register marks it narrowed.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7. The register narrowed it to the direction, with the limitation prop-margin-direction-only.

## prop-margin-direction-only
kind: proposition
statement: Restricted to works whose main claim is a theorem, the interval on the difference of prop-attack-works-price-nobody-more-often includes zero, so the corpus establishes the direction of that difference and not its size.
where: FS:exp/survey/lib/claims.yml#margin-direction-only
uses-to-state: prop-attack-works-price-nobody-more-often
uses-to-prove: none
status: empirical
evidence: the interval computed on the theorem-bearing subset of the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the survey's claim register, which the FORMAL_SECURITY programme digest names inside section 3.7.

## prop-two-party-bounds-rare-in-attacks
kind: proposition
statement: Only 18 of the 200 works state a bound as a relation between two parties' work, and 6 of those study an attack.
alias: two-party-bounds-rare-in-attack-papers
where: FS:exp/survey/lib/claims.yml#two-party-bounds-rare-in-attack-papers
uses-to-state: def-survey-tightness
uses-to-prove: none
status: empirical
evidence: the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-09-03 recounted from 11 and 3.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7, where it is named two-party-bounds-rare-in-attack-papers.

## prop-attack-bounds-limit-change-not-spend
kind: proposition
statement: Where the attack literature bounds an adversary it usually bounds what the adversary may change. 36 of the 103 attack works state a numeric allowance such as a perturbation radius.
where: FS:exp/survey/lib/claims.yml#attack-bounds-limit-change-not-spend
uses-to-state: def-survey-tightness
uses-to-prove: none
status: empirical
evidence: the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-field-shares-access-vocabulary
kind: proposition
statement: The field agrees on a vocabulary for access and phase. 72 of the 103 attack works name an access level from one list of six values.
where: FS:exp/survey/lib/claims.yml#field-shares-access-vocabulary
uses-to-state: none
uses-to-prove: none
status: empirical
evidence: the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-near-misses-hold-unnamed-adversary-price
kind: proposition
statement: Nineteen works hold a resource quantity that their own framing does not carry. Nine of them hold an adversary's or an auditor's cost, five a training cost, and five a capability or mechanism parameter.
alias: near-miss-works-hold-unnamed-adversary-price
where: FS:exp/survey/lib/claims.yml#near-miss-works-hold-unnamed-adversary-price
uses-to-state: def-survey-near-miss
uses-to-prove: none
status: empirical
evidence: the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7, where it is named near-miss-works-hold-unnamed-adversary-price.

## prop-no-memory-bounded-adversary-attacks-model
kind: proposition
statement: Four works bound an adversary in memory, all of them bounded-storage cryptography, and none of them studies an attack on a learned model.
alias: no-memory-bounded-adversary-attacks-a-model
where: FS:exp/survey/lib/claims.yml#no-memory-bounded-adversary-attacks-a-model
uses-to-state: def-survey-unit
uses-to-prove: none
status: empirical
evidence: a novelty claim on the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7, where it is named no-memory-bounded-adversary-attacks-a-model. The sweep of 2026-10-13 did not search this, so it claims no new negative.

## prop-baselines-absent-in-attack-papers
kind: proposition
statement: Of the 50 attack works that define adversary success, 29 name what public knowledge alone achieves and 21 do not.
where: FS:exp/survey/lib/claims.yml#baselines-absent-in-attack-papers
uses-to-state: def-baseline-of-r
uses-to-prove: none
status: empirical
evidence: the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-membership-inference-verdicts-disagree
kind: proposition
statement: Five results on membership inference span the range from success at low false positive rates to unfalsifiability, and each verdict follows what its paper grants the adversary.
where: FS:exp/survey/lib/claims.yml#membership-inference-verdicts-disagree
uses-to-state: none
uses-to-prove: none
status: empirical
evidence: the five papers the register names against it, CCNSTT22, DSMMSZTCEH24, DZT25, ZDKT25 and MSJFRM25, with their numbers in numbers.csv.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the survey's claim register, which the FORMAL_SECURITY programme digest names in section 3.7.

## prop-attacker-to-honest-ratio-defined-twice
kind: proposition
statement: Proof-of-learning and fine-grained cryptography define the same ratio between an adversary's work and an honest party's work, and neither literature cites the other.
where: FS:exp/survey/lib/claims.yml#attacker-to-honest-ratio-defined-twice
uses-to-state: def-survey-tightness
uses-to-prove: none
status: empirical
evidence: a novelty claim on the notes of JYCDTCP21, BC22 and LLW19.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the survey's claim register, which the FORMAL_SECURITY programme digest names in section 3.7.

## prop-threat-models-without-a-resource-bound
kind: proposition
statement: Defences are circumvented inside the threat models their own papers state, because those models fix a perturbation set and an access level and leave open what the attacker may compute.
where: FS:exp/survey/lib/claims.yml#threat-models-without-a-resource-bound
uses-to-state: none
uses-to-prove: none
status: empirical
evidence: the papers the register names against it, ACW18 and TCBM20, with their numbers in numbers.csv.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the survey's claim register, which the FORMAL_SECURITY programme digest names in section 3.7.

## prop-field-rejects-attacker-compute-parameter
kind: proposition
statement: Part of the field states a considered position against attacker computation as a threat-model parameter, while work in the same area uses attacker runtime as a unit of comparison.
alias: field-rejects-attacker-compute-as-a-parameter
where: FS:exp/survey/lib/claims.yml#field-rejects-attacker-compute-as-a-parameter
uses-to-state: none
uses-to-prove: none
status: empirical
evidence: the papers the register names against it, CAPBRTGMK19 and SSZHTE24.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the survey's claim register, which the FORMAL_SECURITY programme digest names in section 3.7.

## prop-corpus-is-a-working-bibliography
kind: proposition
statement: The corpus is a working bibliography drawn from no stated frame. It supports the direction of a comparison between two halves of it and leaves the size of the comparison unsupported.
where: FS:exp/survey/lib/claims.yml#corpus-is-a-working-bibliography
uses-to-state: prop-classification-of-two-hundred-works
uses-to-prove: none
status: empirical
evidence: a limitation of the method, recorded on the coded corpus.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the survey's claim register, which the FORMAL_SECURITY programme digest names in section 3.7.

## prop-single-coder-agreement-unmeasured
kind: proposition
statement: One reader classified each work, so the agreement between two readers is unmeasured outside an overlap of 27 rows, on which 24 agree.
where: FS:exp/survey/lib/claims.yml#single-coder-agreement-unmeasured
uses-to-state: prop-classification-of-two-hundred-works
uses-to-prove: none
status: empirical
evidence: a limitation of the method, recorded on the overlap of 27 rows.
checked-by: unchecked here. The survey's claim register marks it supported.
oracle: n/a
history:
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-geometry-cluster-prices-nobody
kind: proposition
statement: Of 18 papers on concentration of measure and robust PAC learning, eleven constrain nobody or only the learner in samples, three price an adversary, and Diakonikolas et al. make the defender the polynomial-time party.
where: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md#§4
uses-to-state: def-survey-party
uses-to-prove: none
status: empirical
evidence: an audit finding on the 18 papers.
checked-by: unchecked
oracle: n/a
history:
  - 2026-08-22 found by the wiki audit.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.

## prop-agentic-certified-cluster-no-bounded-adversary
kind: proposition
statement: Across the 16 papers of the agentic and certified cluster, every bound is a radius, a count of poisoned samples or a restriction of the interface. Two of them state an unbounded adversary, and five have no theorem.
alias: agentic-and-certified-cluster-has-no-bounded-adversary
where: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md#§4
uses-to-state: def-survey-party
uses-to-prove: none
status: empirical
evidence: an audit finding on the 16 papers.
checked-by: unchecked
oracle: n/a
history:
  - 2026-08-22 found by the wiki audit.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7, where it is named agentic-and-certified-cluster-has-no-bounded-adversary.

## prop-implicit-quantity-register
kind: proposition
statement: Security claims are existential theorems about constructed objects restated as universal claims, and the quantity that would make them measurable sits inside the proof as a side condition.
where: FS:exp/survey/lib/reports/archive/2026-08-20-halil-lit-survey-spine.md
uses-to-state: def-survey-assessed
uses-to-prove: none
status: empirical
evidence: three audits, with three failures, in the spine report.
checked-by: unchecked
oracle: n/a
history:
  - 2026-08-20 recorded in the spine report.
  - 2026-10-25 entered from the FORMAL_SECURITY programme digest, section 3.7.
