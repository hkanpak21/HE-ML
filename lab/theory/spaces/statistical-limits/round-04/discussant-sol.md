---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-25
prompt: lab/theory/spaces/statistical-limits/round-04/prompt-sol.md
---

Proven. The orbit-risk lower bound is true, and revised part (d) of the Train frontier holds. One blocking challenge remains. The claim that orientation stays hidden is false for the fixed positive-definite client class.

### prop-whitening-orbit-sample-price

Proven. The revised statement and proof hold. The output’s orthogonal equivalence class depends only on affine shape. Its coordinates can depend on the client. The positive-definite cross-moment makes the proposed Procrustes rotation optimal, so part (ii) holds with equality. This closes `ch-affine-shape-output`.

Proven. `ch-whitening-refinement-regime`, nonblocking. The carried heuristic refinement still needs a growing-dimension hypothesis. For fixed dimension, the empirical mean contributes at the same inverse-sample order. The simplest correction is to delete that refinement. The exact finite-sample bound already carries the result.

Heuristic. Retain this proposition. Its loss is experimentally measurable, and its uniform guarantee over full-column-rank affine clients is useful.

### thm-blind-orbit-price

Proven. Both numbered conclusions hold under the stated representation-only hypotheses. The proof establishes the minimax rate for arbitrary measurable reconstructions. It does not assume that the server reconstructs through a linear map.

Proven. The seven proof steps check as follows.

1. Proven. Step 1 gives an equivalent observation. Projection recovers the reduced representation, and multiplication by the fixed orthonormal matrix recovers the original representation. Knowing that matrix therefore causes no problem.

2. Proven. Step 2’s Sylvester equation, entrywise derivative, and Frobenius bound are correct. The square-root-of-two Lipschitz constant is valid.

   Proven. `ch-absolute-value-singular-path`, nonblocking. The sentence claiming that a small endpoint perturbation can remove every singular point is false. Opposite determinant signs force a singular point. Perturb one endpoint to make it invertible instead. The determinant polynomial is then nonzero and has finitely many roots. Integrate on the intervals between those roots and use continuity at their endpoints.

3. Proven. Step 3 correctly converts an arbitrary reconstruction into a matrix estimator. The least-squares residual has the stated bound. Taking the matrix absolute value removes the unknown orthogonal factor because the target matrix is positive definite. Both the minimum-singular-value estimate and the five-halves constant are correct. Define the estimator arbitrarily on rank-deficient observations, which have probability zero.

4. Proven. Step 4 constructs a supported prior with conditioning probability greater than one half once the sample count exceeds a sufficiently large absolute multiple of dimension. Applying the borrowed concentration fact to the square Gaussian matrix suffices.

   Proven. `ch-orbit-prior-conditioning`, nonblocking. The coordinate independence, Gaussian marginal laws, and exact second moment describe the unconditioned matrix. Conditioning generally destroys those properties. Say “before conditioning” in the last sentence. Steps 5 and 6 already account correctly for conditioning through its probability.

5. Proven. Step 5 uses the correct Gaussian KL direction. The scalar second-derivative bound holds throughout the stated spectral interval. The conditional second-moment bound gives the claimed information bound. A sample-dependent prior is legitimate because the minimax conclusion applies separately at each sample count.

6. Proven. Step 6 correctly bounds the conditioned density. A Frobenius ball lies inside the stated coordinate ball. The volume formula, Gamma bound, and chosen radius give the claimed small-ball probability. The coordinate comparison loses only a constant factor.

7. Proven. Step 7 legitimately applies the ceiling of `prop-reconstruction-label-sandwich`. A singleton label removes conditioning. Symmetric matrices with the Frobenius metric form a Polish space, and the estimator takes values there. The bound applies even when reconstruction success lies below the prior small-ball probability.

   Proven. The constants hold. At dimension five, the symmetric parameter space has dimension fifteen, and the displayed Fano ratio is below 0.32. Adding the covariance-event failure probability remains below one half. The final radius calculation and conversion from a prior average to one client are correct. No independence between the covariance event and reconstruction success is needed.

Proven. This closes `ch-orbit-price-side-data` for the replacement theorem. Excluding side data removes the squared-norm counterexample. The positive-definite parameter is identifiable from observable population covariance. The withdrawn Gaussian-weight Bayes claim remains Open.

Proven. `ch-orbit-fixed-gauge`, blocking. The final paragraph says that “nothing buys the rotation itself.” That assertion does not hold in this theorem’s client class. Positive definiteness selects a unique orientation. The population covariance of the reduced representations determines its inverse square root, which determines every original record.

Proven. An explicit counterexample to that assertion uses the empirical uncentred covariance. Its inverse square root converges to the client parameter at fixed dimension. Multiplying the representations by that estimate reconstructs each fixed record consistently in its original coordinates. The orthogonally invariant initialization hypothesis of `thm-blind-orbit-limit` is absent here.

Proven. Delete the orientation-impossibility clause. The numbered theorem survives unchanged. If the intended comparison concerns an orthogonally invariant client ensemble, state that separate hypothesis explicitly.

Heuristic. Retain the rate theorem. The reduction from arbitrary reconstruction to positive-definite matrix estimation is concise and substantive. Its parameters and loss admit direct simulation. For a shorter presentation, keep the seven-step structure and move the numerical constants into the proof. State the accuracy corollary within the theorem’s sample regime.

### thm-train-access-price-frontier

Proven. Parts (a) through (c) retain their valid simulations and attack calculations. Revised part (d) holds for fixed positive noise exponent below one half and sufficiently large training size.

Proven. HSU25’s domains now apply. The strict dimension condition for Theorem 3.1 holds. The noise eventually lies between zero and one, as Theorem 3.3 requires. The training size eventually exceeds four. The critical reference-sample count diverges, so padding a zero-sample or one-sample attack to two samples permits Theorem 4.1 to exclude it. This closes `ch-train-zero-reference`.

Proven. The domain check uses Theorems 3.1, 3.3, and 4.1 of the held version of HSU25. :codex-file-citation{path="/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/focs/HSU25_SampleComplexityMembershipInference.pdf" purpose="source"}

Proven. `ch-train-threshold-inversion`, nonblocking. The proof’s phrase “the right side is” is algebraically wrong. The displayed right-hand side concerns the reciprocal sample count. The following asymptotic expression describes the critical sample count after solving the inequality for that count. Insert that rearrangement. Its divergence then justifies padding to two.

Proven. The combined-budget lower bound follows from part (a), since samples plus twice the Train calls is at most twice the combined budget. Part (c) supplies the matching upper bound. The withdrawal of the input-estimated-covariance claim correctly closes `ch-hsu-input-covariance-transfer`.

Heuristic. Retain this operational extension of HSU25. The population-calibrated noise hypothesis is essential and explicit. A shorter proof can introduce the critical reference count once, establish its divergence, and then apply the three preceding parts.

### fact-subgaussian-sample-covariance-concentration

Proven. ACCEPT. The statement matches BRST21, Lemma 7.4, including its row assumptions and tail probability, and supplies the needed measurable covariance bound. :codex-file-citation{path="/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/stoc/BRST21_ContinuousLWE.pdf" purpose="source"}

### thm-blind-orbit-limit

Proven. ACCEPT. The carried proof holds under its invariant initialization and side-data hypotheses, and gives the structural obstruction that the fixed positive-definite subclass does not satisfy.

### prop-relu-client-second-moment-identifies-weights

Proven. ACCEPT. The corrected derivative, population identification, and pointwise inversion proof hold, while the finite-sample price remains explicitly Open.

### thm-same-units-gap-gaussian-mechanism

Proven. ACCEPT. The combined-budget comparison follows from the valid frontier bounds under the declared unit costs and free population-covariance calibration, with Mahalanobis risk as the trainer’s error.

## Verdicts

```text
VERDICT prop-whitening-orbit-sample-price ACCEPT
VERDICT thm-blind-orbit-price REVISE
VERDICT thm-train-access-price-frontier ACCEPT
VERDICT fact-subgaussian-sample-covariance-concentration ACCEPT
VERDICT thm-blind-orbit-limit ACCEPT
VERDICT prop-relu-client-second-moment-identifies-weights ACCEPT
VERDICT thm-same-units-gap-gaussian-mechanism ACCEPT
BLOCKING 1
```