---
key: CCNSTT22
title: Membership Inference Attacks From First Principles
authors: Nicholas Carlini and Steve Chien and Milad Nasr and Shuang Song and Andreas Terzis and Florian Tramèr
venue: IEEE S&P 2022
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/mia-from-first-principles.md
year: 2022
type: attack
placed_on: 2026-10-25
placed_by: agent
triage: read
relation: baseline
epistemic: "empirical for every result, on CIFAR-10, CIFAR-100, ImageNet, WikiText-103 and CINIC-10 with the models of §V; the Gaussian form of the per-example confidence laws is a modelling assumption checked by histograms; no theorem"
prov: full-read
---

# CCNSTT22, Membership Inference Attacks From First Principles

Read by the statistical-limits space session of the HE-ML theory on 2026-10-25,
from the library PDF, arXiv 2112.03570v2 of 12 April 2022. Read: the abstract,
§III (definitions and evaluation, Definition 1 and the balanced accuracy of
Definition 2), §IV (the likelihood-ratio test, per-example hardness, the
parametric estimate and Algorithm 1 with its offline variant), §V-A and §V-B, the
overfitting paragraph §V-D, the ablations of §VI-B (Gaussian fitting and the number
of shadow models) and §VI-D (disjoint datasets), §VII-A, and §VIII. Skimmed: §V-C
and the appendix tables. The venue line is not in the PDF, as the mapping note
below records.

## Claim

Membership attacks should be judged by their true-positive rate at very low
false-positive rate, and a per-example likelihood-ratio test calibrated on shadow
models reaches about ten times the true-positive rate of earlier attacks in that
regime.

## Method

The game (Definition 1, §III-A, adopted from Yeom et al. and Jayaraman et al.)
samples a training set from the distribution, trains a model, and hands the
adversary either a fresh point or a training point, with query access to the
distribution and the model. The attack (Algorithm 1, §IV-C) trains $N$ shadow
models on random halves of data from the distribution, so each example is IN for
half and OUT for half. It fits a Gaussian to the logit-scaled confidence
$\phi(p)=\log\frac p{1-p}$ of each half on the target example and outputs the
likelihood ratio at the target model's confidence. The offline variant uses only
OUT models and the one-sided test of equation (4). Querying data augmentations of
the target point and fitting a spherical Gaussian in that dimension improves both.

## What they measured, and on what

§V-A trains $N=64$ shadow models for ImageNet and $N=256$ for CIFAR-10, CIFAR-100
and WikiText-103, with shadow and target training sets allowed to overlap, and
reports true-positive rates between $0.1\%$ and $10\%$ at false-positive rate
$0.001\%$. The CIFAR-10 models are easier to attack at low false-positive rates
than the ImageNet models despite better test accuracy. §VI-B and Fig. 9 vary $N$
for the online attack at false-positive rate $0.1\%$. Gains taper beyond $64$
shadow models and the attack degrades quickly below. Below $64$ a variance pooled
over examples beats a per-example variance, and at $1024$ shadow models pooling
lowers the true-positive rate from $8.4\%$ to $7.9\%$. §VI-D on CINIC-10 with $128$
OUT models finds no change when shadow and target sets are disjoint and a drop in
true-positive rate under distribution shift. §V-D (Fig. 7) finds models of equal
train-test gap whose vulnerability differs by a factor of $100$.

## Epistemic status

Empirical throughout, on the datasets and architectures above. The Gaussian form of
the confidence laws is an assumption, supported by the histograms of Fig. 4 on
CIFAR-10. The paper proves nothing and does not claim to.

## The limitation that matters to us

Found, partly stated. The attack's cost is counted in shadow training runs, and the
paper gives the count that works on its benchmarks, not a count that is necessary.
The parametric assumption is what makes a finite count possible, since without it
no rate uniform over learning functions exists on atomless views
(`thm-reference-access` of the HE-ML learning-oracle theory). The authors state
the cost of training new models per query in the online attack as its usability
limitation (§IV-C, §VIII).

## Relationship to this project

Baseline. It is the attack whose training-run price the theory's
`thm-black-box-certifiability` (b) and the conjectured lower bound
`conj-shadow-run-price-finite-views` bracket, and its game is the random-subset
game whose distance from the fixed-dataset game `thm-bank-soundness` (b) measures.

## What we need to consider for our work

The counts $64$ and $256$ are the empirical points that a training-run price must be
compared with. The space statistical-limits records them in
`fact-lira-priced-in-training-runs` (round-00 of `lab/theory/spaces/statistical-limits/`)
and corrects the register's pointer for Definition 1 from §VI-A to §III-A.

## Reading for the space oracle-and-measurement, 2026-10-25

Read again by the oracle-and-measurement space session on 2026-10-25, §IV-C (Algorithm 1 and
the paragraph on parallelizing across targets), §V-A and the caption of Fig. 5, and §VI-B with
Fig. 9. Two points matter for measurement and are added here. First, one bank of $N$ shadow
models serves every target at once, since the shadow training sets are chosen so that each
example of the attacker's data lies in exactly $N/2$ of them (§IV-C). The training-run price of
the attack is therefore paid once for all targets, which is the random-subset bank of
`def-model-bank` and `thm-bank-soundness` in the HE-ML oracle theory. Second, every shadow run
draws its own seed, so the IN and OUT models of one target are never coupled. In the terms of
`lab/theory/spaces/oracle-and-measurement/round-00/builder.md`, LiRA is a drawn-mode attack and
its calibration is a drawn-mode estimate. Whether pairing IN and OUT shadow runs at one seed
would cut the number of shadow models is the question of `conj-paired-advantage-price` there.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/CCNSTT22_MIAFirstPrinciples.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/mia-from-first-principles.md`.
Mapping note: PDF is arXiv v2, no venue line; the wiki took the venue from a citing bibliography (ZDKT25), not from a proceedings record.
Read on 2026-10-25 by the statistical-limits space session, sections listed at the top, and this note written from that reading.
