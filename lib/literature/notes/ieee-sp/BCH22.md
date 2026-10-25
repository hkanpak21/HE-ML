---
key: BCH22
title: Reconstructing Training Data with Informed Adversaries
authors: Borja Balle and Giovanni Cherubin and Jamie Hayes
venue: IEEE S&P 2022
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/reconstructing-informed-adversaries.md
year: 2022
type: attack
placed_on: 2026-10-25
placed_by: agent
triage: deep
relation: prior-art
epistemic: "proven for the GLM reconstruction (Theorem 1) and for the DP-to-ReRo and ReRo-to-DP bounds (Theorems 2 and 5, Corollaries 3 and 4, Propositions 6 and 7); empirical for the reconstructor-network attack on MNIST and CIFAR-10 and for the effect of initialization, mini-batching and DP-SGD"
prov: full-read
---

# BCH22, Reconstructing Training Data with Informed Adversaries

Read by the statistical-limits space session of the HE-ML theory on 2026-10-25,
from the library PDF, arXiv v2 of 25 April 2022. Read: the abstract and §I-A,
§II (threat model, Definition 1, protocol and error metric), §III-B (Theorem 1),
§IV (the reconstructor-network attack), §V (setup and success criteria), §VI-A and
§VI-B (feasibility, attack training set size, randomness, black-box access, DP),
§VII (ReRo, Definitions 2 and 3, Theorem 2, Corollaries 3 and 4, Propositions 6
and 7, Theorem 5, §VII-E and §VII-F), and the appendix proofs of Theorem 2,
Corollary 4, Theorem 5 and Proposition 6. Skimmed: the remaining appendix
experiments.

## Claim

An adversary that knows every training point but one can reconstruct the missing
point from the released weights, in closed form for generalized linear models and
by a learned reconstructor for small neural networks, and differential privacy
bounds this reconstruction relative to the best attack that ignores the weights.

## Method

The informed adversary (Definition 1) holds the fixed dataset $D^-$, the released
parameters $\theta$, the training algorithm and optional side knowledge. For a GLM
trained to its unique optimum with an intercept, the first-order condition is a
system of $d$ equations in the $d$ unknowns of the target, solved in closed form by
Theorem 1. For neural networks the attack (§IV-B) trains $k$ shadow models
$\bar\theta_i=A(D^-\cup\{\bar z_i\})$ on shadow targets $\bar z_i$ and fits a
reconstructor network $\varphi$ to the pairs $(\bar\theta_i,\bar z_i)$, then outputs
$\varphi(\theta)$. This is reconstruction posed as a learning problem from released
models to training points, priced in shadow training runs. Reconstruction
robustness (Definition 2) asks that every map $R$ from parameters to data succeed
within error $\eta$ with probability at most $\gamma$ over a prior $\pi$ on the
target. The baseline $\kappa_{\pi,\ell}(\eta)=\sup_{z_0}\Pr_{Z\sim\pi}[\ell(Z,z_0)\le\eta]$
of §VII-B is the best attack that ignores $\theta$.

## What they measured, and on what

MNIST with an MLP and CIFAR-10 with a CNN of about 55K parameters, trained by full-batch
gradient descent with momentum and, by default, an initialization known to the
adversary, so that training is deterministic. Success is judged against a nearest
neighbour oracle, the closest point of $D^-\cup\bar D$, with mean MSE $0.0232$ on
MNIST and $0.0291$ on CIFAR-10. On MNIST, high-fidelity reconstructions appear at
$1$K shadow models and beat the nearest-neighbour oracle on average at $8$K (Fig. 5c).
On CIFAR-10, $5$K shadow models get below the first-percentile oracle MSE and $10$K
below the nearest-neighbour oracle. Without the initialization the attack fails on
MNIST. Table III gives MSE between $0.0691$ and $0.0695$ when each released model
has a fresh random initialization and between $0.0041$ and $0.0089$ when the
initialization is shared and known, over four learning-rate and momentum settings.
The sentence of Appendix A that quotes $0.0089$ and $0.0695$ lists them in the
opposite order to its wording, and the table is the record. A pool of $5$M shadow
pairs over $500$ initializations per target did not help. With mini-batches,
the attack succeeds when the shuffling seed is known and depends on the learning
rate when it is not (Fig. 7 and 8). A logit-only black-box variant reaches MSE
$0.011$ on MNIST and $0.0198$ on CIFAR-10. DP-GD with large $\varepsilon$ already
defeats the attack (Fig. 9).

The theorems of §VII are these. Theorem 2: $(\alpha,\varepsilon)$-RDP gives
$(\eta,\gamma)$-ReRo with $\gamma=(\kappa e^\varepsilon)^{(\alpha-1)/\alpha}$.
Corollary 3: $\varepsilon$-DP gives $\gamma=\kappa e^\varepsilon$. Corollary 4:
$\rho$-zCDP with $\rho<\log(1/\kappa)$ gives
$\gamma=\exp(-(\sqrt{\log(1/\kappa)}-\sqrt\rho)^2)$. Propositions 6 and 7 give
$\gamma=e^{-\Omega(d)}$ for $\varepsilon$ or $\rho$ of order $o(d)$ under a uniform
ball prior or a Gaussian prior with $\sigma\ge2\eta/\sqrt d$. Theorem 5: ReRo for the
$0/1$ error over all two-point priors with mass $1/(e^\varepsilon+1)$ gives
$(\varepsilon,\max\{0,(e^\varepsilon+1)\gamma-e^\varepsilon\})$-DP.

## Epistemic status

Proven, Theorem 1 and every statement of §VII, with proofs in the appendix. The
proof of Theorem 2 changes measure to the output law at a fixed $z_0$ and applies
Hölder's inequality. Empirical, everything about the reconstructor network, on the
two datasets and architectures above. The paper keeps the two apart.

## The limitation that matters to us

Found and partly stated. The attack needs the released model's initialization, and
the paper reports that it fails without it and gives evidence that it may be
impossible then (§VI-B and Appendix A). That is the seed acting as an attacker
resource, which the HE-ML top oracle models. The reconstructor is trained on
weights, not on an intermediate representation, so the paper does not cover the
split-learning form of the reconstruction question. The bounds of §VII need
differential privacy inside training.

## Relationship to this project

Prior art. It contains the empirical form of Halil's reconstructor-as-learner, priced
in shadow training runs, and the statistical baseline $\kappa$ that the space
statistical-limits refines to a label baseline in `conj-reconstruction-label-sandwich`.

## What we need to consider for our work

The definition numbering settles the register's dispute. Definition 2 is
reconstruction robustness and Definition 1 the informed adversary. The shadow-run
counts ($1$K to $10$K) and the initialization result belong with the training-run
price of `conj-shadow-run-price-finite-views` and with the top-oracle discussion
there. The space records them for the registers as a new fact in its round-00
summary.

## Reading for the space oracle-and-measurement, 2026-10-25

Read again by the oracle-and-measurement space session on 2026-10-25, the table of factors of
§VI and Appendix A with Table III and Fig. 11. One result bears on measurement and is added here.
Fig. 11 trains 1,000 released MNIST models with a target point and 1,000 without, in two settings.
With a shared initialization the two laws of the target's loss are perfectly separable. With a fresh
seed per model they nearly coincide. In the HE-ML oracle theory's terms the figure measures, on a real
pipeline, a top divergence near one beside a small total variation, the gap that
thm-coupling-certificate (c)(i) proves possible. Only the initialization is shared, so the figure is a
lower estimate of what the full seed gives. Recorded as fact-known-initialization-separates-membership in
`lab/theory/spaces/oracle-and-measurement/round-00/builder.md`.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/BCH22_ReconstructingInformedAdversaries.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/reconstructing-informed-adversaries.md`.
Mapping note: PDF is arXiv v2 (25 Apr 2022), no venue line; wiki venue from dblp.
Read on 2026-10-25 by the statistical-limits space session, sections listed at the top, and this note written from that reading.
