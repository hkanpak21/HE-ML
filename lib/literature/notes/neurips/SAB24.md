---
key: SAB24
title: Optimistic Verifiable Training by Controlling Hardware Nondeterminism
authors: Megha Srivastava, Simran Arora, Dan Boneh
venue: NeurIPS 2024
venue_evidence: https://proceedings.neurips.cc/paper_files/paper/2024/hash/ad885a9caafff30ee9cafdf0ee42fda2-Abstract-Conference.html
year: 2024
type: system
placed_on: 2026-10-16
placed_by: agent
triage: skim
relation: prior-art
epistemic: "empirical throughout, on ResNet-50 trained on CIFAR-10 and GPT-2 fine-tuned on Shakespeare, on three NVIDIA GPU types; no theorem"
prov: full-read
---

# SAB24, Optimistic Verifiable Training by Controlling Hardware Nondeterminism

Read by the agent on 2026-10-25 for the theory space `oracle-and-measurement`, from the library
PDF (NeurIPS 2024, 23 pages with appendices). Read: the abstract, §1, the description of
nondeterminism and of the method in §3 to §5 (rounding, the logging of rounding directions,
Algorithms 1 to 4 as described in the text, the storage bound Eq. (1) and the adaptive threshold),
§6 with Figures 2 and 4 and Tables 2 to 4, and §8. Skimmed: §7 and the appendices, of which
Table 5 is cited for times.

## Claim

Logging the rounding direction of the few intermediate values that fall near a rounding boundary,
while training at higher precision and rounding back after each layer, lets an auditor on a different
GPU type replicate a training run bit for bit.

## Method

The setting is optimistic verifiable training. A trainer trains for a client and commits to its
checkpoints in a Merkle tree. A third-party auditor replays the training and, on a mismatch, a
verification game in the style of Teutsch and Reitwießner locates the first diverging step. Exact
replay fails across GPU types because floating point accumulation order differs. The trainer trains in
FP64, rounds every layer output to FP32 after $b_r$ mantissa bits, and records the rounding direction
whenever the value lies within a threshold $\tau$ of the boundary. The auditor copies those directions.
An adaptive search sets $\tau$ per operation to reduce the log. The trainer shares the randomness
used in training, the rounding amount, the checkpoint interval and the logs.

## What they measured, and on what

ResNet-50 (23M) trained from scratch on CIFAR-10, 100 epochs, and GPT-2 (117M) fine-tuned on 1.1M tokens
of Shakespeare, on A40, Titan XP and RTX 2080 Ti GPUs (§6). Figure 2: with the same software version, seed
and deterministic library flags, predictions differ across the three GPU types. §6 states that runs on one
GPU architecture repeat identically, while runs on different architectures give different models. With the
method, full training and fine-tuning replicate exactly across all trainer and auditor pairs (Figure 4).
Training time grows by a factor 1.2 to 1.4 for the trainer and 1.3 to 1.7 for the auditor in a prototype
(Table 5). Table 3: the auditor corrects 20 to 25 values per step at $b=32$. Efficient encoding cuts the log
by 77% (Table 2), and the scheme needs more than 140 times less storage than the proof of learning of Jia et
al. for GPT-2. The authors implement their own dropout because `torch.randn` was nondeterministic for long
inputs even at a fixed seed.

## Epistemic status

Empirical, on the two models and three GPU types above. The paper proves nothing and does not claim to. The
statement that runs on one architecture repeat exactly is an observation in their setting.

## The limitation that matters to us

Stated in §8: the latency of higher precision, the storage of rounding logs, trust in the auditor, and no
distributed training yet. Found by us: the method makes reruns of the same training input identical. It does
not address the leave-one-out twin, which differs in data, so the twin's distance from the base run is a
property of training, not of hardware.

## Relationship to this project

Prior art for the realization of the HE-ML learning oracle's named-seed Train call with deterministic
kernels. It shows that the identity coupling of the oracle theory, a rerun at one seed with no hardware
noise, is realizable on real GPUs, within one architecture by deterministic settings and across
architectures by logged rounding, at a stated time factor.

## What we need to consider for our work

Recorded as fact-controlled-nondeterminism-exact-replication in
`lab/theory/spaces/oracle-and-measurement/round-01/builder.md`. Together with JYCDTCP21 Table I it fixes the
measurement design of the space: coupled reruns should be run with deterministic kernels, whose cost factor is
1.2 to 1.7 here, and the spread of the rerun should be measured and reported, since it is zero under this
control and near one without it for whole runs in JYCDTCP21's setting.
