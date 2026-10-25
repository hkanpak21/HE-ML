---
key: NHSBTJCT23
title: Tight Auditing of Differentially Private Machine Learning
authors: Milad Nasr, Jamie Hayes, Thomas Steinke, Borja Balle, Florian Tramèr, Matthew Jagielski, Nicholas Carlini, Andreas Terzis
venue: USENIX Security 2023
venue_evidence: https://www.usenix.org/conference/usenixsecurity23/presentation/nasr
year: 2023
type: measurement
placed_on: 2026-10-16
placed_by: agent
triage: drop
relation: prior-art
epistemic: "empirical lower bounds on epsilon, each a Clopper-Pearson confidence bound or a Bayesian credible bound for the audited per-step mechanism; the end-to-end figure is heuristic, since it composes per-step bounds assuming tight Gaussian or PLD composition; no theorem of its own"
prov: full-read
---

# NHSBTJCT23, Tight Auditing of Differentially Private Machine Learning

Read by the agent on 2026-10-25 for the theory space `oracle-and-measurement`, from the
library PDF (USENIX Security 2023 proceedings, 19 pages). Read: the abstract, §1 to §7 in
full, Algorithms 1 to 3, Tables 1 and 2, Figures 1 to 12. Not read: the appendices of the
extended version that the paper points to.

## Claim

An audit of DP-SGD that reads its test's error rates through the Gaussian (or PLD) trade-off
function of the mechanism, instead of the $(\varepsilon,\delta)$ privacy region, reaches nearly the
theoretical $\varepsilon$ on natural datasets and needs two training runs in the white-box
gradient-canary threat model, where earlier audits needed worst-case datasets and thousands of
runs.

## Method

An audit is a distinguishing test between models trained on $D$ and on $D'=D\cup\{z\}$. Its
false-positive and false-negative rates get Clopper and Pearson upper bounds $\bar\alpha,\bar\beta$,
which Eq. (9) turns into $\varepsilon^{\mathrm{lower}}_{\mathrm{emp}}$ for $(\varepsilon,\delta)$-DP, as in
earlier work (§2.3). The paper instead uses Eq. (12),
$\mu^{\mathrm{lower}}_{\mathrm{emp}}=\Phi^{-1}(1-\bar\alpha)-\Phi^{-1}(\bar\beta)$ for Gaussian DP, and
converts $\mu$ to $\varepsilon$ through Corollary 5. A Bayesian variant follows Zanella-Béguelin et al.
(§4.2). Three threat models (§3). White-box with gradient canaries, where the adversary sees every
privatized gradient and inserts an arbitrary gradient (a Dirac gradient of norm $C$) with
probability $q_c$. White-box with input canaries. Black-box, where the adversary inserts a training
point and sees the final model. In the white-box audit (Algorithm 2) each step yields one
observation, the inner product of the canary gradient with the privatized gradient, so one run
yields many observations. §5.5 composes per-step bounds into an end-to-end bound by assuming the
per-step privacy loss is Gaussian, or by PLD when subsampling is present.

## What they measured, and on what

CIFAR-10 with WRN-16 and a ConvNet, Purchase, and a random dataset of CIFAR-10's size. Fig. 3: in
the gradient-canary model with $\delta=10^{-5}$ and 20 independent repetitions, the $(\varepsilon,\delta)$
audit approaches the theoretical value only near $10^8$ observations, while the Gaussian-DP audit is
tight with $10^3$. Table 1 (95% bounds, theoretical $\varepsilon$ of 1, 4, 8, 16): on CIFAR-10 WRN-16 the
Gaussian-DP Clopper-Pearson audit gives 0.75, 3.40, 5.80, 11.14 and the Bayesian one 0.95, 3.73, 7.09,
13.95, while the $(\varepsilon,\delta)$ Clopper-Pearson audit gives 0.41, 1.37, 3.63, 5.25. §6.3 detects
three implementation bugs: clipping after averaging, a noise seed with only 100 values (Violation 2,
detected by the Gaussian-DP audit and by Lu et al.'s method, missed by $(\varepsilon,\delta)$ audits), and a
noise scale that is too small. §6.4: clipping alone gives lower bounds 23.4 to 41.0 from 1,000 models
per world (Table 2). In the black-box model, 1,000 models with the canary and 1,000 without give about
1.6 at theoretical 8 for WRN-16 on CIFAR-10 (Fig. 11), and the gap to the theory depends on dataset
and architecture.

## Epistemic status

Empirical lower bounds, each sound as a confidence statement for the audited per-step mechanism. The
paper notes that choosing the threshold on the same observations makes the bound technically invalid
and follows common practice anyway (§5.2). The end-to-end bounds rest on assuming tight composition,
which is heuristic. The paper proves no theorem of its own.

## The limitation that matters to us

Found by us. Every number is a lower bound on leakage at one point, so the audit never certifies an
upper bound. The audit couples the two worlds only partly. Algorithm 2 samples the batches $B$ and $B'$
independently, and the authors report no significant difference when they made them identical (§5.1).
All runs share the initial parameters while the other randomness uses different seeds (§6.1). The
privacy noise is never shared between the worlds, so the gain that a fully coupled design could give is
not tested.

## Relationship to this project

Prior art for the measurement side. It is the state of the art in lower-bounding a point of a security
profile, and its run counts (two runs white-box, 2,000 runs black-box) are the empirical prices that
`conj-paired-advantage-price` of `lab/theory/spaces/oracle-and-measurement/round-00/builder.md` sets
against a coupled design.

## What we need to consider for our work

Recorded as fact-gdp-audit-observation-count, fact-audit-independent-batches and
fact-small-seed-space-breaks-dp in that builder file. Violation 2 is a measured case of a finite seed
space breaking privacy, the empirical side of open problem 9 of the oracle theory.

## Dropped after reading

audits DP-SGD for a single trainer; FL only as a remark on the threat model. The paper fails the HE-ML inclusion rule (multi-party learning together with privacy or security against an adversary), so it has no ledger row.
