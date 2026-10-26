---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-25
prompt: lab/theory/spaces/computational-limits/round-04/prompt-sol.md
---

Proven. The agreement lemma holds. Both borrowed facts hold with their stated hypotheses. The primitive-label argument repairs the sample result, and the SQ argument holds. The coarse and ZLIP theorems still require revision.

Proven. The width distinction, independent sample blocks, hidden-client hypothesis, and change from SQ reconstruction to detection close their round 03 challenges. The withdrawn objects remove their challenges from this milestone. They do not resolve the deferred inversion problem.

Proven. `fact-lll-recovers-discrete-hidden-labels` is correct under the inherited Model 3.2 hypotheses.

The nonzero-label condition repairs the singularity counterexample. Rational proportionality is the correct conclusion for the integer vector returned by LLL. Zadik, Song, Wein and Bruna, COLT 2022, Theorem 3.3 and Lemma 3.4 support this repaired statement.

Proven. The source proof itself supports the correction. In Section 6.3, its anticoncentration argument excludes vectors outside the real span of the label vector. Its subsequent assertion about integer multiples overstates that argument.

Heuristic. Keep this fact as a short borrowed tool. It does not require another proof here.

Proven. `fact-discrete-gaussian-samples-generate` correctly states Haviv and Regev, SODA 2014, Lemma 5.4.

The determinant and shortest-basis hypotheses, sample count, and exponential failure probability agree with the source. Its proof first obtains full rank and bounds the generated sublattice’s index. Further samples reduce that index until it reaches one. The shortest basis length of the integer lattice is one.

Heuristic. For this milestone, state only its specialization to the integer lattice. The general statement adds hypotheses that the application never uses.

Proven. `lem-agreement-detection` holds line by line, with independent algorithm coins across runs and one stored output per run.

Under the null, rotating a sample block preserves its distribution and makes the rotated block independent of the rotation. Undoing that rotation therefore produces a uniform direction. Independence between runs gives the asserted null bound.

Proven. Under the planted law, the transformation used in the proof preserves the joint distribution and rotates the output by a stabilizer element. Conditional on its component along the hidden direction, the perpendicular component is uniform. The two runs remain independent after conditioning separately on their successes.

Proven. The spherical tail constants also hold. A sphere coordinate’s even moments are bounded by the corresponding Gaussian moments with variance equal to the reciprocal of dimension. Chernoff’s bound gives the stated tail. Substituting the agreement threshold gives both displayed exponents.

Heuristic. State dimension at least two. At a pole, assign the unused perpendicular direction an independent uniform value. These are nonblocking clarifications.

Proven. `thm-coarse-reconstruction-lattice-hard` has the correct correlation conversion and concentration scale, but its constructed tester is incomplete.

The sample budget repairs `ch-coarse-sample-budget`. The coupling transports the attacker’s success to every hidden direction. The covariance bounds and Bernstein’s inequality control the hidden-coordinate norm. BRST21 Lemma 7.4 controls the sample matrix norm at the stated sample budget. Their ratio gives directional overlap at least one third of the correlation constant. The agreement lemma then gives the claimed exponential constant.

`ch-coarse-zero-output`, blocking.

Proven. A nonzero reconstruction vector can lie in the kernel of the transposed sample matrix. The extracted direction can therefore vanish on unsuccessful runs, including under the null. Normalizing it is undefined. For an injective frozen linear client, the attacker can compute precisely these dependencies from representations.

Proven. Repair this by returning an independent uniform direction whenever the extracted vector vanishes. On the correlation-success event, that vector cannot vanish. The repair preserves the success lower bound and null symmetry.

Heuristic. State explicitly that the correlation constant is fixed and positive. Retain the reduction with its explicit cost of two protocol runs. It is the strongest new result of the round.

Proven. `thm-zlip-reductions` repairs the distributional dependence problem. Its lower reduction and the algebra of all three upper blocks are sound.

For direction (a), Lemma 3.6 supplies the stated good-basis event. Lemma 2.9 then samples at the widened width. Conditional on the input form, the unknown integral isomorphism sends these samples to independent product discrete Gaussians. The Cholesky transformation introduces an orthogonal map, so the view coupling applies. A spanning block determines the candidate isomorphism. The three certificate checks are sufficient.

Proven. In upper block 1, lattice generation makes the recovered basis differ from the hidden client by a unimodular matrix. Exact representation coordinates are rational before the Hermite normal form step. A union bound on the first block’s norms justifies selecting any independent records from that block.

Proven. Upper block 2 contains the useful new argument. The covariance congruence is exact. Applying the inverse-covariance error between two selected original records bounds each entry by the operator norm of that error times their two norms. No basis condition number enters. The stated norm bounds make the entry error at most one quarter, so rounding recovers the integral Gram matrix.

Proven. Upper block 3 uses fresh samples correctly. Conditional on the earlier successful blocks, their coordinates have the required discrete Gaussian law. Full-rank conditioning gives Definition 3.3’s distribution. The final integral orthogonal transformation is a signed permutation.

`ch-zlip-small-width`, blocking.

Proven. As written, part (b) has only an upper bound on the width. Haviv and Regev require at least unit width here. Uniform concentration after variance normalization also needs a width restriction.

Proven. The unrestricted upper statement is false. Take the width to be the inverse fourth root of dimension. Compare the identity client with twice the identity client. An observation containing one vector twice a standard basis vector, with all other observations zero, has two explanations. Their latent records have different norms.

Proven. For polynomially many records, the smaller probability of these explanations decays exponentially in the square root of dimension. Signed permutations cannot reconcile the latent norms. Thus one client incurs failure larger than the claimed exponential-in-dimension allowance, even with a perfect ZLIP oracle.

Proven. Put the lower width restriction in the shared setting, or explicitly make part (b) inherit part (a)’s width. At least unit width suffices for the upper proof.

Heuristic. Simplify block 3 by using one fresh block and aborting on deficient rank. Charge its exponential failure probability to the existing allowance. Also restrict the linear-solve sentence to frozen injective linear clients. The final identifiability sentence should refer to the population representation law.

`ch-hardness-computation-model`, blocking for both lattice theorems’ security conclusions.

Proven. Declaring exact real arithmetic makes the reductions’ intended model explicit. It does not establish their claimed consequences from ordinary cryptographic hardness assumptions. An arbitrary exact-real attacker requires a simulation argument before its composition yields a polynomial-time quantum algorithm on finite strings.

Proven. BRST21, STOC 2021, Corollary 4.2 supplies the cited quantum reduction. It does not supply the missing simulation of arbitrary exact-real protocol computations. Likewise, DvW22’s assumption does not automatically justify the stronger interpretation.

Heuristic. Keep the exact-arithmetic reductions. State hardness in that same model as a separate assumption, or defer the standard computational-hardness conclusions until the simulation is justified.

Open. The finite-precision transfer remains unproved.

Proven. `prop-blind-lll-label-recovery` holds in the declared exact-arithmetic model. Its primitive-label and SQ arguments survive review.

Injectivity preserves the normalized dependency coefficients exactly. It therefore preserves the truncated coefficients used by LLL. The argument correctly avoids the source algorithm’s final Euclidean normalization.

Proven. The primitive-label proof holds. Poisson summation bounds each prime-divisibility probability by the reciprocal prime plus the reciprocal width. A polynomial tail cutoff leaves polynomially many possible prime divisors. Their union bound decays exponentially in dimension. Add the cutoff failure explicitly to the displayed probability estimate.

Proven. Once the labels are primitive, any nonzero rationally proportional integer vector is an integer multiple of them. Dividing by its gcd therefore recovers the labels up to sign.

`ch-label-detection-certificate`, nonblocking.

Proven. Add the missing detection sentence. Check that the recovered nonzero integer vector satisfies the original, untruncated dependency exactly. Under Gaussian records, no such integer relation exists almost surely. A countable union of Gaussian null events proves this. The certificate survives every injective linear client.

Proven. The SQ proof’s Hermite calculation is correct for fixed degree. The constant coefficient cancels. Poisson summation bounds each remaining coefficient exponentially in the squared spacing parameter, and normalization changes only the constant. This supplies DKRS23’s polynomial moment-matching condition.

Proven. Diakonikolas, Kane, Ren and Sun, NeurIPS 2023, Theorem 1.5 then gives the asserted query-or-tolerance alternative. State its parameter ranges and success probability of two thirds explicitly. The degree restriction holds eventually for every fixed even degree. The exponentially small matching slack fits inside the displayed tolerance bound. [DKRS23, Theorem 1.5](https://arxiv.org/html/2403.04744v1#S1.Thmtheorem1.5).

Proven. Pulling each bounded representation query back through an independently sampled client preserves its range and tolerance. Right-rotation invariance identifies the planted representation law with the intended game. Use the same client distribution under the Gaussian null.

Heuristic. Keep this as a short transfer proposition. DKRS23 already explains the general SQ-versus-LLL separation in Section 1.1.1. Its Fact 1.12 can also replace the detailed Fourier calculation when only fixed-degree matching is needed.

Heuristic. The agreement lemma and covariance congruence earn their place mathematically. The hard instances arise from record laws, and the reductions charge protocol runs explicitly. The exact-coordinate results still need a precision analysis before they support experimental security conclusions.

## Verdicts

```text
VERDICT fact-lll-recovers-discrete-hidden-labels ACCEPT
VERDICT fact-discrete-gaussian-samples-generate ACCEPT
VERDICT lem-agreement-detection ACCEPT
VERDICT thm-coarse-reconstruction-lattice-hard REVISE
VERDICT thm-zlip-reductions REVISE
VERDICT prop-blind-lll-label-recovery ACCEPT
BLOCKING 3
```