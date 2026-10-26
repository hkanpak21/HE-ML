---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-25
prompt: lab/theory/spaces/statistical-limits/round-05/prompt-sol.md
---

Proven. All five round 04 challenges close. No object contains a remaining false statement under its inherited hypotheses.

### thm-blind-orbit-price

Proven. The numbered statements and proof hold for the representation-only positive-definite client class. Identifiability closes the formerly blocking `ch-orbit-fixed-gauge`, finite-root integration closes nonblocking `ch-absolute-value-singular-path`, and the unconditioned moment qualification closes nonblocking `ch-orbit-prior-conditioning`.

### prop-whitening-orbit-sample-price

Proven. The exact identity, Procrustes equality, and Gaussian expectation bound hold under the stated rank and sampling hypotheses. Deleting the heuristic refinement closes nonblocking `ch-whitening-refinement-regime`.

### thm-train-access-price-frontier

Proven. The corrected inversion gives a diverging critical reference count, which justifies padding to two samples and closes nonblocking `ch-train-threshold-inversion`. The simulations and attack prove the frontier under population-calibrated noise and the revised asymptotic hypotheses.

### fact-subgaussian-sample-covariance-concentration

Proven. The unchanged statement retains the independent, isotropic, sub-gaussian row hypotheses and the bound recorded from BRST21, Lemma 7.4.

### thm-blind-orbit-limit

Proven. The coupling and Haar-averaging proof holds under invariant initialization, equivariant training, and invariant side data. Those hypotheses distinguish this obstruction from the identifiable positive-definite client class.

### prop-relu-client-second-moment-identifies-weights

Proven. The corrected kernel derivative establishes population identification, and the cited pointwise inversion result gives the stated recovery probability. The Gaussian and independence hypotheses remain essential, and the finite-sample price remains Open.

### thm-same-units-gap-gaussian-mechanism

Proven. The frontier’s simulation lower bound and efficient upper bound establish the combined-budget comparison. The stated unit costs, free population-covariance calibration, and Mahalanobis risk make the comparison valid.

## Verdicts

```text
VERDICT thm-blind-orbit-price ACCEPT
VERDICT prop-whitening-orbit-sample-price ACCEPT
VERDICT thm-train-access-price-frontier ACCEPT
VERDICT fact-subgaussian-sample-covariance-concentration ACCEPT
VERDICT thm-blind-orbit-limit ACCEPT
VERDICT prop-relu-client-second-moment-identifies-weights ACCEPT
VERDICT thm-same-units-gap-gaussian-mechanism ACCEPT
BLOCKING 0
```