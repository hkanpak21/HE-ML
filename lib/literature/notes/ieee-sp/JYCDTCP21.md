---
key: JYCDTCP21
title: "Proof-of-Learning: Definitions and Practice"
authors: Hengrui Jia and Mohammad Yaghini and Christopher A. Choquette-Choo and Natalie Dullerud and Anvith Thudi and Varun Chandrasekaran and Nicolas Papernot
venue: IEEE S&P 2021
venue_evidence: "first page (header: In 42nd IEEE Symposium on Security and Privacy)"
year: 2021
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "Theorem 1 and Theorem 2 proven inside a model of i.i.d. hardware noise per step; the security of the verification scheme is Conjecture 1, unproved; every reproduction figure is empirical on CIFAR-10 and CIFAR-100"
prov: full-read
---

# JYCDTCP21, "Proof-of-Learning: Definitions and Practice"

Read by the agent on 2026-10-25 for the theory space `oracle-and-measurement`, from the
library PDF (18 pages, arXiv 2103.05633v1). Read with care: Sections IV (threat model,
Properties 1 and 2, Definition 1), VI (the stationary Markov reading, Theorem 1, the
reproducibility evaluation with Table I and Figures 1 to 3) and VII up to Conjecture 1, and the
discussion of counter-based random number generators in Section VIII. The proofs in the
appendix were not re-derived.

## Claim

A trainer can log its stochastic gradient descent run (checkpoints, data indices, data
signatures, hyperparameters) so that a verifier who replays short segments accepts it, and the
authors argue, without proof, that forging such a log costs at least as much as training.

## Method

The proof of learning of Definition 1 is the tuple $(W,I,H,A)$: model states at checkpoints,
the indices of the data used for each state, signatures of those data, and auxiliary
information. The verifier replays selected segments of $k$ steps from a logged checkpoint and
accepts when the replayed state lies within a distance threshold $\delta$ of the logged one. The
adversary knows the architecture, the final weights, the loss, the optimizer and the full
training data, and may modify the data (capabilities 1 and 2), but it does not know the
trainer's randomness, which the paper lists as batching, parameter initialization, chosen
random seeds and hardware noise (capability 3). The cost requirements are Property 1, the
verifier's expected cost at most the trainer's, and Property 2, the trainer's expected cost at
most any spoofer's.

## What they measured, and on what

ResNet-20 on CIFAR-10 and ResNet-50 on CIFAR-100, 200 epochs at batch size 128. The quantity
is the normalized reproduction error: the distance between a logged state and the state that a
verifier obtains by retraining from the previous checkpoint with the same initial parameters,
batching, architecture and training strategy, divided by $d_{\mathrm{ref}}$, the distance between
two models trained independently (different batching and initialization). Table I. For a whole
run ($k=E\cdot S$) the normalized $\ell_2$ error is 0.955 ($\pm0.004$) on CIFAR-10 and 0.815
($\pm0.002$) on CIFAR-100. For one step ($k=1$) it is 0.001 and 0.002. With PyTorch's
deterministic operations the whole-run error is 0.569 on CIFAR-10 and 0.816 on CIFAR-100, and the
text reports a large computational cost and an accuracy drop above one percentage point for
those operations. Figures 1 to 3 trace the error against the checkpoint interval, the storage
overhead and the learning rate. Section VII evaluates spoofing by inverting gradient descent and
reports errors that the verifier detects (Table III).

## Epistemic status

Theorem 1 (Entropy Growth) states that the entropy of the training process grows linearly in the
number of steps. It is proven under the assumption that each step adds i.i.d. noise from hardware
and libraries, which is a model and is heuristic for real accelerators. Theorem 2 is the reverse
analogue. The security claim, that inverting a training sequence is as costly as training, is
Conjecture 1 and is not proven. Table I and the spoofing experiments are empirical. The paper keeps
these apart.

## The limitation that matters to us

Found by us, not stated in these terms by the authors. Table I shows that two runs with one seed
and one initialization end almost as far apart as two independent runs, in $\ell_2$, on GPU. The
identity coupling of the HE-ML learning oracle (rerun at a named seed) is therefore close to
independent for whole runs on real hardware, and close to exact for one step. The paper's secret is
the trainer's seed itself, with no random oracle and no commitment, so a prover who chooses its own
batches is not ruled out (the forging attacks of TJSP22 and ZCSL24 use exactly that freedom).

## Relationship to this project

Prior art for thm-replay-audit-steer of the learning-oracle theory, which replaces the secret seed
by one that a random oracle derives from a committed dataset and proves a steering bound. Its Table
I is the one measurement in the library of the spread $\mathrm{sp}_\tau$ that the replay audit and
the coupled certificates depend on.

## What we need to consider for our work

Recorded as fact-rerun-reproduction-error and fact-pol-bare-cost-inequalities in
`lab/theory/spaces/oracle-and-measurement/round-00/builder.md`. Any certificate that relies on
coupled reruns of a whole centralized run must expect a coupled distance near $d_{\mathrm{ref}}$
unless deterministic kernels are used, and even then about $0.57\,d_{\mathrm{ref}}$ for ResNet-20.
Per-round federated local training, which is a few steps, sits in the regime of $k$ small, where
reruns nearly coincide. The measurement designs of the space should be run in both regimes.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/JYC+21_ProofOfLearning.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/proof-of-learning.md`.
