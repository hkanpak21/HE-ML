---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-29
prompt: lab/theory/spaces/learning-attacker-prices/critique/prompt-critique.md
---

Heuristic. The space has sound statistical results and useful experiments. It does not yet deliver the requested theory of a learning attacker. Its strongest measured bracket concerns every estimator. Its result about the linear VAE class remains a conjecture. Its comparison with the trainer is Gaussian regression under a specified query-power constraint.

Proven. I found six blocking challenges. Each concerns a false assertion or an undefined expression. Most require local repairs. They do not invalidate the main covariance, information, or Gaussian posterior arguments.

I changed no repository file.

1. `thm-update-direction-chi-square-bound`, round 00.

   Proven. Parts (a), (b), and (d) hold. The proof correctly uses conditional independence, Hermite expansion, symmetry, and the spherical overlap moments. Averaging the auxiliary magnitudes before taking the product gives the stated mean chi-square parameter. Data processing then removes the auxiliary information.

   Proven. Part (c) holds with the usual convention that a direction estimator returns a unit vector. Its fourth-moment bound is conservative. The validation constant 2304 and the testing advantage 19/36 are correct. An integer validation budget should use a ceiling.

   Proven. I recomputed the moments 78 and 74, and the ratio 19.5. The infinite untruncated chi-square divergence is compatible with the finite KL divergence used later. The two claims concern different divergences.

   Heuristic. This is a useful specialization of the standard second-moment method for rotationally indexed non-Gaussian component models. The exact conditional update law and its closed-form divergence earn their place. I have not verified a prior theorem containing precisely this batch-conditioned formulation.

   Verdict ACCEPT.

2. `def-optimum-update-stream`, round 01.

   Proven. The optimum, unconditional covariance, conditional covariance, and entry-variance calculation hold. The signs remove the drift. Orthogonal Gaussian coordinates remain independent of the label magnitude and the secret coordinate.

   Proven. ch-zero-update-profile blocks property (iii). The definition permits identically zero labels and zero injected noise. Every update then vanishes, and its variance-profile parameter is zero divided by zero. Require positive orthogonal fourth moment, or give the degenerate stream a separate convention.

   Proven. The access model is one round containing independent client updates at the optimum. It is not a trajectory of consecutive SGD steps. The revised definition states this correctly.

   Heuristic. This setting isolates a real distinction between population drift and gradient fluctuations. It also removes the trainer’s learning dynamics and gives the trainer no task involving the secret direction. Those are substantial limits on its interpretation.

   Verdict REVISE.

3. `thm-norm-weighted-update-pca`, round 01.

   Proven. The proof holds. Orthogonal invariance gives the scalar bulk and rank-one spike. Sign symmetry gives zero mean. The sub-Gaussian bound, whitening, covariance concentration, and Rayleigh quotient argument establish recovery under the stated positive-definiteness hypothesis.

   Proven. I checked the constants 24, 12, and 3/8. I independently recomputed the two weighted spikes as 0.0801336630 and 0.0755624223. The stated dimension threshold of 220 million is sufficient for the displayed conservative perturbation bound.

   Proven. The numerical spike values are quadrature results. Their status should remain Empirical. The recovery theorem itself does not depend on those numerical values.

   Proven. Its concentration input is the standard sub-Gaussian covariance theorem. The register attributes it to Vershynin, High-Dimensional Probability, Cambridge University Press, 2018, Theorem 4.6.1, through BRST21 Lemma 7.4.

   Heuristic. The finite-dimensional norm approximation is useful. Weighted spectral recovery itself belongs to an established method family. It should not be presented as a new learning principle.

   Verdict ACCEPT.

4. `prop-update-direction-fano-recovery`, round 01.

   Proven. All four proof steps hold. The spherical-cap bound, binary-event data processing, comparison with the null law, and Gaussian-mixture KL bound give the stated inequality. Removing symmetry here is valid.

   Proven. The exact additive constant at the stated success criterion is 0.9241962407. The displayed 0.93 is conservative. The high-noise upper coefficient 39 follows from the truncation argument. It is an upper bound, rather than an established exact coefficient.

   Proven. This is a generalized Fano argument with a spherical success set. Duchi and Wainwright’s technical report, Distance-based and continuum Fano inequalities, 2013, gives related continuous-estimation bounds in Proposition 2. I do not identify that proposition with this exact spherical specialization. [Primary source](https://arxiv.org/pdf/1311.2669).

   Heuristic. Its contribution here is explicit, usable constants and a finite KL bound where chi-square fails. It supplies no restriction specific to a VAE or a shadow learner.

   Verdict ACCEPT.

5. `prop-full-clipping-optimum-filter`, round 02, incorporating round 01.

   Proven. Parts (a) through (d) hold for the normalized update as defined. Part (c) needs its stated absence of a conditional atom at the prediction. Under that hypothesis, a conditional median makes the residual sign independent and uniform.

   Proven. Part (e) also holds. The lower-tail substitution gives the exponent 9/64. The union bound and the comparison through the common normalized stream give the factor 2. The cited source is Laurent and Massart, Annals of Statistics, 2000, Lemma 1 and its chi-square consequence. [Source](https://projecteuclid.org/journals/annals-of-statistics/volume-28/issue-5/Adaptive-estimation-of-a-quadratic-functional-by-model-selection/10.1214/aos/1015957395).

   Proven. ch-atomic-residual-drift blocks the additional unrestricted drift formula. Consider a scalar model whose parameter is its constant prediction. Give it deterministic zero labels and evaluate it at prediction zero. The normalized update is zero. The printed formula using the ordinary conditional CDF gives a nonzero drift. The formula must account for the atom at the prediction.

   Proven. ch-clipping-residual-support blocks the closing claim that a continuous conditional label law always leaves a positive unclipped fraction. Give the same model equally weighted uniform labels on the intervals from negative two to negative one, and from one to two. Prediction zero is a median. At clipping threshold 1/2, every gradient clips. Continuity alone does not put probability near the median.

   Heuristic. The exact normalized-update statement is clean. Its interpretation as residual-sign information is more useful than an unrestricted claim about clipping.

   Verdict REVISE.

6. `prop-signed-weight-update-pca`, round 02.

   Proven. Parts (a) and (b) hold. Splitting the weight into positive and negative parts, concentrating each part, and adding the two errors gives the stated condition-number sum. The final eigenvector argument permits a signed bulk coefficient.

   Proven. The constants inherited from the nonnegative theorem remain sufficient. A part that vanishes almost surely can simply be omitted.

   Heuristic. ch-optimal-weight-regularity does not block the theorem. The remark about the proposed optimal weight requires boundedness and an appropriate norm-approximation argument. A measurable conditional second moment need not produce a bounded Lipschitz weight. The theorem proves recovery for admissible declared weights, not attainment of the unrestricted optimal weighting problem.

   Proven. Signed preprocessing and optimal spectral weighting have substantial prior art. Luo, Alghamdi, and Lu, IEEE Transactions on Signal Processing, 2019, Theorem 1, optimize spectral preprocessing through a weighted function-space problem. Their Theorem 2 states the spectral characterization they use. This does not automatically settle the noisy-update extension here. [Primary source](https://arxiv.org/pdf/1811.04420).

   Verdict ACCEPT.

7. `def-statistic-learner-class`, round 03, incorporating its earlier versions.

   Proven. Defining the class directly as randomized measurable functions of the declared statistic is coherent. The exact-statistic restriction and the distinction between using all observations and allowing subsampling are useful. Subsampling restores monotonicity of attainable success.

   Proven. ch-minimizer-selection blocks the asserted implication from loss dependence to output dependence. “Returns a minimizer” does not specify how the minimizer is selected. With identically zero loss and a constant statistic, selecting the first observed unit vector returns a minimizer while retaining data absent from the statistic. Require a statistic-measurable selector. Full-batch descent from a fixed, data-independent start already has the required property.

   Proven. ch-statistic-is-not-compute does not block the repaired definition. The class of all measurable functions of a covariance matrix includes computationally unrestricted estimators. Its observation price therefore does not price the optimizer work of a declared VAE. The second budget coordinate is introduced but does not enter the surviving price results.

   Heuristic. This is a useful restriction by information retained. Calling its price a complete price of a learning attacker overstates what the definition measures.

   Verdict REVISE.

8. `conj-linear-class-reads-cauchy-transform`, round 03.

   Proven. The finite-dimensional Schur-complement identities hold. Given the proposed deterministic equivalents, the cancellation leading to the outlier equation and the derivative giving the overlap are correct. The monotonicity argument gives at most one root on each specified regular exterior branch.

   Proven. Part (b1) holds under its simple-spectrum hypothesis. Posterior rotational symmetry makes the posterior second-moment matrix diagonal in the observed eigenbasis. Maximizing mean-square overlap therefore selects an eigenvector. The subsequent bound by the expected maximum realized eigenvector overlap also holds.

   Proven. ch-spectral-edge-existence blocks the setting as written. Take zero injected noise. Choose the squared label magnitude independently of the Gaussian index, with a Beta(1,5) law. Set the dimension-to-client ratio to 1/2. Before the first positive pole, the right side of the proposed upper-edge equation increases only to 1/6. Beyond that pole, the integral diverges inside the scale support. The asserted positive edge parameter does not exist. Bounded magnitudes alone do not ensure regular edges.

   Open. The noisy deterministic equivalents and uniform bulk delocalization remain unproved here. Individual eigenvector delocalization alone would not suffice for the maximum over every bulk eigenvector in (b2).

   Proven. ch-full-observer-invariant does not block the exact identities. It limits their interpretation. The displayed weighted squared norm describes the second Hermite contribution. The full observer can also use higher Hermite contributions. The space’s own moment-balanced example has zero conditional second spike and a non-Gaussian higher-order channel.

   Proven. Much of the spectral structure is known. At zero injected noise, the empirical update covariance is exactly a Gaussian spectral-initialization matrix with squared label magnitude as preprocessing. Lu and Li, Information and Inference, 2020, Theorem 2.1, analyze that method under their hypotheses. Their Section 4.3 already exhibits alternating correlated and uncorrelated phases. Thus, a success window as sample size grows is not new by itself. Their assumptions also explicitly address endpoint regularity. [Primary source](https://academic.oup.com/imaiai/article/9/3/507/5643538).

   Heuristic. This is the space’s most attractive organizing calculation. Its present scope needs repair, and its novelty needs comparison with spectral initialization and sufficient dimension reduction.

   Verdict REVISE.

9. `prop-measured-meets-proven-full-observer`, round 03.

   Empirical. My independent quadrature gives an atomic KL contribution of 0.2482961725, a continuous contribution of 0.0813241111, and total divergence 0.1601110957. This reproduces the corrected value.

   Proven. Conditional on the upper bound 0.1602, the lower budgets are 46.2492952 and 98.2676057. The ratios are 86.4878044 and 81.4103483. The one-sided 95 percent Clopper–Pearson lower endpoint for 40 successes in 40 independent trials is 0.9278424755.

   Empirical. The round files report those success counts and an independent challenger replication. I did not reproduce the spectral trials. The space does not provide their executable experiment or raw trial record.

   Open. ch-numerical-witness does not establish a false numerical value and therefore does not count as blocking. It prevents calling the lower witness fully proven. Adaptive quadrature’s estimated error is not a certified integration bound. The text acknowledges this conditional status, but its unconditional “known within 87” conclusion exceeds it. A rigorous upper bound on the divergence would repair that conclusion.

   Proven. ch-simultaneous-coverage does not block the individual brackets. Two separate 95 percent statements do not automatically give simultaneous 95 percent coverage.

   Heuristic. This is a measured upper witness beside a conditional mathematical lower witness. The factor 87 is a broad bracket. It does not show a measured learning threshold meeting a sharp proven threshold, or establish the linear VAE class’s price.

   Verdict REVISE.

10. `thm-release-relearning-price-bracket`, round 03.

   Proven. Parts (a) through (d) hold for positive training-noise variance and positive prior variance. The risk decomposition is correct. Giving the attacker the design preserves the lower-bound direction. Adaptive queries still produce the stated Gaussian posterior, because each query is fixed conditional on the preceding transcript.

   Proven. The posterior-precision calculation, trace inequality, Jensen step, and least-squares risk are correct. The challenger’s Schur-complement proof establishes the inverse-Wishart moment directly.

   Proven. ch-uniform-risk-slack blocks the final multiplicative conclusion in (e). Set all three variance scales to one and let the allowed relative risk slack equal the square of the training-set size. The zero-query estimate already meets the target risk. The claimed positive price, proportional to the reciprocal training-set size, cannot approximate that zero price multiplicatively. Restrict the slack and state the asymptotic regime explicitly.

   Proven. ch-integer-query-bound does not block the intended asymptotic result. The sufficient integer budget needs upward rounding. The displayed real-valued upper endpoint does not follow directly from the integer least-squares construction.

   Proven. ch-noise-necessity does not block parts (a) through (d). The title’s “exactly when” is too strong. Their formulas allow any positive answer-noise variance. Matching nature’s variance fixes the proportionality constant. Fresh answer noise and the average query-power constraint are the operative assumptions.

   Heuristic. This is clean Gaussian conjugate regression combined with an A-optimal-design trace argument. The classical attribution is from memory, unverified. I have not verified a prior theorem with this exact adaptive release formulation. Its mathematical ingredients are standard, and the statement usefully assembles them for model extraction.

   Verdict REVISE.

Heuristic. Against Halil’s words, the space achieves a restricted statistical answer. It bounds success from observed updates and brackets re-learning from a noisy linear release. It does not yet establish a measured price specific to a nonlinear VAE, a shadow learner, or a fixed optimizer budget.

Proven. The two completed comparisons concern different experiments. In the update stream, the trainer’s optimum is independent of the secret. In the release experiment, the attacker targets the trainer’s population parameter. The space does not prove a reduction connecting these two comparisons.

Heuristic. ch-aim-not-closed does not block an individual theorem. It blocks the interpretation that the council’s central gap has been closed. The measured witness is a spectral estimator. No convergence theorem identifies it with a VAE trained under a declared work budget. The lower bound for the covariance-statistic class remains open.

Proven. Some shortfalls come from the setting. A trainer at this optimum has learned nothing about the secret direction, so its learning price cannot calibrate the attacker’s price for that secret. Gaussian linear conjugacy also makes the release experiment analytically tractable without resolving nonlinear learning.

Heuristic. Other shortfalls come from the method. Replacing a learner by every function of a statistic removes optimizer dynamics and work. Giving a lower-bound argument the hidden magnitudes weakens its constants. Declaring agreement between numerical integrators does not certify the integral. None of those limitations is forced by Gaussian inputs.

Proven. The surviving formal statements require no cryptographic seed generator and use no canaries. They do not silently settle the seed-generator or canary-target rulings.

Heuristic. ch-defence-admissibility does not block those statements as descriptions of fixed procedures. Interpreting added release noise or normalization as an admissible modification requires a separate argument under Halil’s programming rule. A known output law alone does not establish indistinguishability from the honest joint transcript.

Heuristic. The mathematics is cleanest in the conditional update decomposition, the posterior-symmetry argument, and the release-risk decomposition. The spectral transform is attractive, but much of its structure already belongs to spectral initialization. The presentation becomes less persuasive where ten objects support a conclusion whose learner-specific lower bound remains open. I would retain the short arguments and narrow the organizing claim.

Open. The next space should prove one operational statement. For actual one-pass linear SGD with Gaussian inputs and labels given by an independent random sign times the absolute secret projection capped at one, establish a finite-dimensional recovery-price bracket attained by a declared norm-sensitive gradient attacker, charging both observed updates and optimizer work, with every channel parameter confidence-bounded from independent runs.

## Verdicts

```text
VERDICT thm-update-direction-chi-square-bound ACCEPT
VERDICT def-optimum-update-stream REVISE
VERDICT thm-norm-weighted-update-pca ACCEPT
VERDICT prop-update-direction-fano-recovery ACCEPT
VERDICT prop-full-clipping-optimum-filter REVISE
VERDICT prop-signed-weight-update-pca ACCEPT
VERDICT def-statistic-learner-class REVISE
VERDICT conj-linear-class-reads-cauchy-transform REVISE
VERDICT prop-measured-meets-proven-full-observer REVISE
VERDICT thm-release-relearning-price-bracket REVISE
BLOCKING 6
```