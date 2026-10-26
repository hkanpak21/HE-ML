# Summary of round 03 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25. Discussant: sol
(`discussant-sol.md`, gpt-6.1-sol, 183,456 tokens). Milestone 2 opens here. Argon is out
of quota until about 2026-10-27 13:30, so the round used sol, and later rounds use sol
again, argon quota.

## What changed

The round stated the three aims of milestone 2 and offered proofs. Sol accepted four objects
and found seven blocking defects.

- Aim 1, blind reconstruction. `thm-blind-orbit-limit` holds for trained clients and side data.
  An unbounded seed-blind server cannot reconstruct a Gaussian record within
  $\sqrt d/(2\sqrt2)$ except with probability $e^{-\Omega(d)}$, beyond the common rotation.
  `prop-relu-client-second-moment-identifies-weights` also holds: the arc-cosine kernel,
  first-order and prior work of Cho and Saul (NeurIPS 2009) as sol notes, identifies a frozen
  Gaussian ReLU client up to rotation from its population second moment. The whitening
  proposition holds with one false sentence: its output coordinates depend on the client, and
  only its rotation class is a function of the records' affine shape. The lower-bound
  conjecture fails as stated. The accepted game admits invariant side data, and squared record
  norms then give exact reconstruction up to rotation from finitely many records. Round 04
  restates the bound for a representation-only view and proves it.
- Aim 3, Train access. Parts (a) to (c) of `thm-train-access-price-frontier` hold: the
  simulation, the known-covariance transfer and the attack with its constants. Part (d) is
  false for constant noise. Sol gives an attack with no reference sample and order $d$ Train
  calls when $d\gtrsim n^2$, which compares the target's distance to the release in the
  estimated metric. Round 04 states the frontier in the regime $\rho=n^{-a}$, where the
  reference price diverges.
- Aim 2, same units. `thm-same-units-gap-gaussian-mechanism` is accepted, under a declared
  meter of one unit per sample and per Train call, with the trainer's covariance calibration
  free. `prop-label-relevant-attacker-at-most-trainer` is rejected. Generative exponent at least
  three forces the first Hermite coefficient of the conditional mean to vanish, so the
  conditional-mean theorem never applies, and a predictor need not recover the direction (sol
  gives an exponent-four example with zero conditional mean). The builder withdraws it and the
  supporting `fact-single-index-information-theoretic-rate`, following Halil's instruction of
  tonight to cut what does not earn its place.

## Slugs accepted

Verdict ACCEPT, in a round with BLOCKING 7, so not yet eligible:
`fact-subgaussian-sample-covariance-concentration`, `thm-blind-orbit-limit`,
`prop-relu-client-second-moment-identifies-weights`, `thm-same-units-gap-gaussian-mechanism`.
They are carried into round 04.

## Challenges open

Blocking, answered in `round-04/builder.md`: `ch-affine-shape-output`,
`ch-orbit-price-side-data`, `ch-train-zero-reference`. Closed by withdrawal:
`ch-single-index-resource-classes`, `ch-label-first-coefficient`,
`ch-label-prediction-not-direction`, `ch-label-evaluation-domain`. Not blocking:
`ch-relu-kernel-derivative`, `ch-relu-population-price`, `ch-hsu-proof-margin`,
`ch-hsu-frontier-domain`, `ch-hsu-input-covariance-transfer`, `ch-gaussian-comparison-meter`,
`ch-single-index-proof-attribution` (withdrawn with its fact).

## For the registers

New facts.

- `fact-subgaussian-sample-covariance-concentration`. BRST21 Lemma 7.4, quoting Vershynin,
  High-Dimensional Probability (2018), Theorem 4.6.1 (book not in the library). Read in the
  BRST21 PDF. Accepted by sol.

Corrections.

- `fact-hsu-membership-sample-gap`. Per sol, the proof of HSU25 Theorem 3.1 needs a strict
  margin, since total variation at most $0.02$ does not exclude advantage exactly $0.02$, and
  in §3.2.4 the condition $400m\le n+n^2\rho^2$ bounds the square-root term by $0.1$, not
  $0.01$. Smaller existential constants repair both, so the theorem stands with unspecified
  constants. Not re-checked by the builder.
- The arc-cosine identity of `prop-relu-client-second-moment-identifies-weights` is the
  first-order kernel of Cho and Saul, NeurIPS 2009, equations (1), (3) and (6), at half their
  normalization. The paper is not in the library.

Withdrawn objects, with reasons, for the record only. `prop-label-relevant-attacker-at-most-trainer`
(refuted as stated, `ch-label-first-coefficient`), `fact-single-index-information-theoretic-rate`
(not needed after the withdrawal, and its "efficient rate" sentence overstated
`ch-single-index-resource-classes`).

New problems.

- `prob-label-direction-same-units`, side. Compare direction recovery by the trainer and by a
  split-learning server under one interface and one resource class, for single-index labels
  with generative exponent at least three. Posed by sol's challenges of round 03.
- `prob-relu-blind-inversion-sample-price`, supporting. The sample price of
  `prop-relu-client-second-moment-identifies-weights` with the second moment estimated from $N$
  representations. Related to `prob-blind-inversion-relu-clients` of `computational-limits`.
- `prob-train-access-collapses-sample-price`, from open to partial after round 04 if accepted.

New search rows. None.

For Halil. Whether a Gaussian mechanism that calibrates its noise to the population covariance is
the right model when the attacker has Train access, since it then leaks the covariance (the
modelling hypothesis of `thm-train-access-price-frontier`).
