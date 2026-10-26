---
key: GKVZ22
title: Planting Undetectable Backdoors in Machine Learning Models
authors: Shafi Goldwasser and Michael P. Kim and Vinod Vaikuntanathan and Or Zamir
venue: FOCS 2022
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/planting-undetectable-backdoors.md
year: 2022
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "white-box RFF backdoor proven under worst-case lattice hardness, sparse-PCA ReLU backdoor sketched with o(1) advantage"
prov: full-read
---

# GKVZ22, Planting Undetectable Backdoors in Machine Learning Models

Read on 2026-10-25 by the hard-problem-mappings space session from the held copy
(arXiv 2204.06974v2): Section 2.2 (the informal Theorems 2.1 and 2.2 and the
random ReLU paragraph), Section 3.2 (Definitions 3.5 and 3.6, Hypothesis 3.7),
Section 4.1 (Definition 4.6 and the three undetectability variants), Section 6
(Algorithms 2 to 6, Lemma 6.2, Assumption 6.3, Theorem 6.4 with its proof, Theorem
6.5, Lemma 6.6) and Appendix A (Definition A.2, Lemma A.3, Assumption A.4,
Algorithms 7 to 10, Claim A.5 and its proof sketch). Section 5 (signatures,
persistence) and Section 7 (neutralization) were read by their statements only.

## Claim

A malicious trainer can plant a backdoor that no efficient algorithm can detect:
under one-way functions in the black-box sense for any model, and in the white-box
sense for random Fourier features by drawing the features from Gaussian pancakes
(hCLWE) instead of the Gaussian, and with $o(1)$ advantage for random ReLU features
by drawing them from a sparse spiked covariance.

## Method

Definition 4.6: undetectability is computational indistinguishability of the
hypotheses of Train and Backdoor, for every data law, against distinguishers with
samples of $D$, white box (full description) or black box (queries); a
statistic-access variant is defined and not achieved. Train-RFF samples
$m=\Theta(d\log(d/\varepsilon\delta)/\varepsilon^2)$ features
$\cos(2\pi(\langle g,\cdot\rangle+b))$, $g\sim\gamma_d$, $b\sim[0,1]$, and trains a
linear head by any routine. Backdoor-RFF samples $g\sim GP_d(\mathrm{bk})$, the
sparse pancakes of Lemma 6.2 (a $d^{1/c}$-sparse secret $\omega$ of norm
$2d^{1/2c}$ with $\langle g,\omega\rangle$ within $d^{-b}$ of a half-integer), and
Activate adds $\mathrm{bk}$, which flips every feature's sign. Theorem 6.4: under
Assumption 6.3 (the head's margin is at least inverse polynomial) and Hypothesis
3.7, this is a white-box undetectable $\gamma$-backdoor with $\gamma=d^{1/c}$ in
$\ell_0$ and $2d^{1/2c}$ in $\ell_2$; the reduction runs Train-RandomFeatures on the
given samples. Lemma 6.6 gets the dense pancakes from BRST21's homogeneous CLWE
conditioned near $1/2$, $\gamma\ge2\sqrt d$. Appendix A: Train-Random-ReLU
thresholds the average of $m$ ReLU features with Gaussian weights; the backdoor
draws the weights from $N(0,I_d+\theta ss^\top)$, $s$ $d^\alpha$-sparse; Claim A.5
($0<\alpha<1/2$, $\theta=O(1)$, $\lambda>1/\theta$, unit-norm data) gives a
one-way backdoor activated by $x+\lambda s$, undetectable under Assumption A.4
(planted clique for $k=o(n^{1/2})$) through Lemma A.3 (BB19, $m=\Theta(d)$).

## What they measured, and on what

Proofs only.

## Epistemic status

Theorem 6.4 is proven under Hypothesis 3.7 and Assumption 6.3. Claim A.5 has a
proof sketch, and the paper says its advantage is only $o(1)$ (crediting CG24).
My finding, proven in `lem-sparse-pca-backdoor-width-price`: a coordinate-variance
test detects the spiked weights from $m\ge64k^2\ln(4(d+1))/\theta^2$ rows, so
undetectability at $m=\Theta(d)$ needs $\theta\to0$ polynomially; then
$\lambda>1/\theta$ exceeds the data norm polynomially and any perturbation of that
size in any direction flips honest networks too, so the key plays no role.

## The limitation that matters to us

The white-box constructions are carried by the trainer's choice of the weight law,
not by a data law, and each is for one planted law. The paper does not price
detection in the trainer's width; the sparse-PCA construction fails once that price
is computed (my finding).

## Relationship to this project

Prior art. Theorem 6.4 is the literature's one white-box mapping of backdoor
detection onto a lattice problem (`fact-gkvz22-backdoor-scope`), the starting point of
`conj-backdoor-detection-is-ngca`.

## What we need to consider for our work

Detection of a weight-law backdoor is a non-Gaussian component analysis problem on
the trainer's $m$ weight vectors, and the planted law decides its regime. A
construction must be checked against simple polynomial-time tests at the width the
trainer actually uses.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/GKVZ22_UndetectableBackdoors.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/planting-undetectable-backdoors.md`.
Mapping note: Wiki marks the FOCS 2022 attribution as not stated in the PDF, so it is unverified there. Held PDF is arXiv v2 (9 Nov 2024).
Reading record: 2026-10-25, the hard-problem-mappings space session read the sections named at the top of this note, for lab/theory/spaces/hard-problem-mappings/round-00/builder.md.
