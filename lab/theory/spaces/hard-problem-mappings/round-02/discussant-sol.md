---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-26
prompt: lab/theory/spaces/hard-problem-mappings/round-02/prompt-sol.md
---

Proven. All five blocking challenges from round 01 close. I accept the five revised objects. Two proof equalities need harmless corrections, described below. Neither affects a conclusion.

`lem-sparse-pca-backdoor-width-price`

Proven. `ch-zero-trigger-variance` is closed. The zero input produces zero features and a negative classification because the threshold is positive. For a nonzero input, positive definiteness gives positive preactivation variance. The Gaussian representation, Lipschitz constant, mean response and relative concentration bound then follow exactly. Independence means independence from the weight draws conditional on the fixed key.

Proven. The radial comparison holds. For an input orthogonal to the key, the triggered input and the stated radial input have identical preactivation laws under their respective networks. Their average responses therefore have identical marginal distributions, which strengthens the stated equality of means. The radial perturbation uses the original input and public parameters only.

Proven. For an arbitrary unit input, the spectral bound on the spiked covariance and the triangle inequality give the claimed upper bound on trigger variance. The conservative radial input attains at least that variance under either weight law. This compares against the worst case input radius. It does not bound the ratio to every realized trigger norm, which can vanish.

Proven. Parts (a) and (b) retain valid tail bounds and a valid contrapositive. The asymptotic conclusion forces at least polynomial growth of the trigger length. It supplies no polynomial upper bound.

Proven. Part (d) refutes the activation condition in Goldwasser, Kim, Vaikuntanathan and Zamir, FOCS 2022, [GKVZ22 Appendix A, Claim A.5](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/focs/GKVZ22_PlantingUndetectableBackdoorsMachine.pdf). The exact triggered mean is below the threshold. The stated failure probability follows from concentration.

Proven. The proof should replace its equality involving the rounded mean by an inequality. The exact mean is slightly below 0.738. Consequently, the chosen relative deviation is slightly smaller than the exact relative gap. The displayed probability bound remains conservative. The clean input also stays negative with probability tending to one, by the same concentration argument. Its mean alone would not establish that probability.

Heuristic. This lemma earns its place as a measurable obstruction to the cited construction. Its strongest conclusions concern this homogeneous, averaged ReLU classifier and fixed inputs. “No backdoor content” should refer to Appendix A’s claimed guarantees, rather than every possible repair of the construction.

`def-hard-problem-mapping`

Proven. `ch-mapping-price-types` is closed. The two extraction rows now separate the SQ lower bound from the sample upper bound. The sample row retains the linear term required by Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, [DPLB24 Theorem 4.1](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/colt/DPLB24_ComputationalStatisticalGapsGaussian.pdf). In particular, a link with generative exponent 1 no longer receives an incorrect square root sample price.

Proven. The displayed dimension exponents assume a fixed link, noise level, target error and confidence. Under fixed confidence, sign validation contributes a dimension independent number of additional pairs. If confidence varies with dimension, the catalogue must add the theorem’s sign validation budget explicitly.

Proven. The inherited definition is well posed. It fixes the learning target, reduction direction, resource coordinates and regime. Its exponent ratio requires specified scalar resources and fixed success levels. The table gives shorthand for these mappings, rather than independent guarantees that omit the source hypotheses.

Heuristic. The definition supplies useful accounting. Its mathematical content comes from the transfer lemma and instantiated reductions. Comparing a VSTAT parameter with a trainer’s record count remains a heuristic comparison, as the definition states.

`prop-learner-side-sq-transfer`

Proven. `ch-one-bit-success-constant` is closed. Feldman, Grigorescu, Reyzin, Vempala and Xiao, JACM 2017, [FGRVX17 Theorems 3.7 and 3.13](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/pdfs/jacm/FGRVX17_StatisticalAlgorithmsLowerBound.pdf) give the corrected bound.

Proven. The composition observes records only through the procedure’s one bit transcript. An unbounded postprocessor does not enlarge that transcript. Theorem 3.13 therefore applies without a computational restriction on the postprocessor. Both comparisons between VSTAT parameters use the correct inclusion of valid answer sets.

Proven. In part (b), the chosen simulation error gives the stated reduced success probability. Substitution into the simulation budget gives the minus sign correction. Theorem 3.7 then gives precisely the claimed query contradiction. At success probability 2/3, the second term becomes the source’s stated constant 1/432 times inverse average correlation. The printed general formula in Theorem 3.16 disagrees with both its proof and this specialization.

Proven. The fresh record and Boolean query hypotheses are essential. The result does not cover a procedure that reads full records. Within that restriction, it gives an operational lower bound on the learner’s record accesses, even against unbounded attackers.

`thm-extraction-exponent-price`

Proven. `ch-extraction-sign-confidence` is closed. Conditional on the recovered vector and the true direction, fresh validation pairs remain independent. On the direction recovery event, choose the accuracy small enough that the absolute overlap is at least one half. The least nonzero odd Hermite coefficient then gives the stated positive covariance gap. Every odd contribution favors the correctly oriented candidate, so cancellation cannot reduce that gap.

Proven. The covariance display should sum over positive Hermite degrees. Including degree zero gives an uncentered second moment. This correction leaves the candidate difference unchanged because the constant terms cancel.

Proven. Each candidate is bounded, and its product with an answer is sub-Gaussian at the stated scale. Concentrating the product averages and the means controls the empirical covariances. The proposed additional sample budget therefore selects the correct sign with the stated validation failure probability. A union bound with direction recovery gives the revised total confidence.

Proven. Interpret evenness up to Gaussian null sets. If the link is even in this sense, both candidates agree almost surely. Otherwise Hermite completeness guarantees a nonzero odd coefficient. This convention makes the sign branch well defined for measurable links.

Proven. The correctly oriented prediction error converges to zero by the Hermite expansion and dominated convergence. Cauchy-Schwarz then gives the claimed weak fidelity implication. The unchanged lower bound retains the required bounded output, positive Gaussian answer noise, polynomial query allowance and adversarial VSTAT convention.

Proven. DPLB24 Theorem 4.1 proves direction recovery with a suitable denoiser. It does not charge the cost of computing that denoiser. The new assumption correctly exposes this limitation. Theorem 5.2 preserves the generative exponent under Gaussian answer noise. Proposition 2.6 supports the channel inequality. Theorem 6.1 supplies statistical sufficiency, without establishing the previously claimed optimality.

Proven. Randomizing the recovered line’s sign repairs the uniform vector assertion in part (d). The even release already ignores that sign. The training exponent 2 and release exponent 4 follow from the unchanged symmetry and level set arguments.

Heuristic. This is the principal contribution of the space. The construction uses a label law and its Bayes predictor, contains no cryptographic plug-in, and admits numerical denoising and measured fidelity. The comparison establishes an SQ separation with a sample upper bound. It establishes no unrestricted polynomial time extraction lower bound.

`prop-gram-sufficiency-rotation-invariant`

Proven. `ch-gram-test-running-time` is closed. The revised statement charges the original test’s running time plus the stated arithmetic overhead. It therefore covers unbounded tests without declaring them polynomial time.

Proven. Equal Gram matrices determine the same orthogonal orbit. The inherited NGCA family transforms equivariantly with its key. A uniform key makes both hypotheses invariant under right rotations. Haar randomization therefore preserves the joint hypothesis and observation law.

Proven. The overhead is attainable. A rank revealing Cholesky factorization constructs a factor from the positive semidefinite Gram matrix within the stated bound. This gives a direct justification for the claimed thin factorization cost. The rank is at most the ambient dimension. Haar sampling and multiplying the factor by the sampled rotation also fit the combined budget.

Proven. The ReLU integral, strict kernel monotonicity and zero row treatment recover the Gram matrix from exact feature second moments. Part (iii) correctly identifies why the sparse key prior does not support this rotation argument. It proves no lower bound against Gram auditors.

Open. Finite precision, probe complexity and test stability remain unresolved. Thus this is an exact sufficiency result, rather than an experimentally priced detection mapping.

Heuristic. The short orbit argument and invertible moment map justify retaining the proposition as structural mathematics under `CONTEXT.md`.

## Verdicts

```text
VERDICT lem-sparse-pca-backdoor-width-price ACCEPT
VERDICT def-hard-problem-mapping ACCEPT
VERDICT prop-learner-side-sq-transfer ACCEPT
VERDICT thm-extraction-exponent-price ACCEPT
VERDICT prop-gram-sufficiency-rotation-invariant ACCEPT
BLOCKING 0
```