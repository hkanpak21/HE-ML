---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-25
prompt: lab/theory/spaces/computational-limits/round-03/prompt-sol.md
---

Heuristic. Keep the ZLIP mapping, the sample versus SQ separation, and the coarse reconstruction reduction as revised aims. Replace aim 1’s present formulation with a quantitative approximate inversion problem. The ZLIP equivalence is not established at matching parameters. The agreement test has a sound sample-based argument after adding a sample-size hypothesis.

1. `fact-lip-average-case`

Proven. The definitions and the accounts of Lemmas 2.9, 3.4 and 3.6 agree with Ducas and van Woerden, EUROCRYPT 2022. Lemma 3.4 gives uniformity of the isomorphism conditional on the returned form. Definition 3.3 conditions on full real rank. It does not require the sampled vectors to generate the lattice.

Proven. Lemma 3.10 needs more precise success accounting than the builder records. Its stated constant-success algorithm repeats the average-case solver, with reciprocal-success overhead. The SIVP cost remains additive. This does not affect the intended use of the fact. [DvW22, Sections 2 and 3](https://ir.cwi.nl/pub/31729/31729.pdf).

Heuristic. Accept this object. It supplies the correct distributional framework, rather than merely a lattice problem with unspecified random instances.

2. `fact-zlip-best-algorithms`

Proven. Ducas’s Theorems 1 and 2 establish the stated slide-reduction result. Section 2.6 handles even dimension by adjoining one orthogonal integer coordinate. This preserves the stated bound on the SVP dimension.

Heuristic. The exponent 0.146 depends on the BKZ analysis and heuristic sieving cost. It is not a proven running time. Proven. The exponent one half is a proven upper bound, with polynomial dependence on the input length. Neither exponent is a lower bound. The builder distinguishes these statuses correctly in this fact. [Ducas, DCC 2024, Sections 1 and 2.6, Theorems 1 and 2](https://ir.cwi.nl/pub/33543/33543.pdf).

Open. A polynomial-time algorithm is not ruled out by these results. “Best known” should be dated to the literature account checked here.

Heuristic. Accept the object with that temporal scope.

3. `fact-lll-recovers-discrete-hidden-labels`

Proven. The kernel-based description of the LLL stage is correct. The unrestricted statement about Algorithm 1 is false in degenerate cases admitted by Model 3.2.

`ch-zswb-label-hypotheses`, blocking. Proven. Set the first integer label to one and all remaining labels to zero. The matrix formed from the last d samples then has rank at most d minus one. Algorithm 1 returns FAIL with probability one. All-zero labels give another counterexample. ZSWB22’s Lemma 6.3 contains the same indexing error. Its proof passes from a nonzero label somewhere among all samples to a nonzero label among the last d samples.

Proven. There is a second issue in the source’s proof language. For a nonprimitive integer label vector, its primitive divisor satisfies the same integer relation. The assertion in Lemma 3.4 that every short relation is an integer multiple of the original labels is therefore too strong. Rational proportionality is the appropriate conclusion. The final normalization using the original Euclidean geometry can remove that proportionality.

Heuristic. Revise the fact to state the nondegenerate case actually needed here. Record these source-level qualifications. They do not refute the intended application to independent discrete Gaussian labels, where the problematic events can have exponentially small probability.

4. `fact-ngca-lattice-basis-reduction`

Proven. The main algorithmic account agrees with Diakonikolas and Kane, COLT 2022, Theorem 1.3 and Section 2. Steps 3 through 9 depend on the sample matrix through its right kernel, once the rounding step has occurred.

`ch-dk-assumption-scope`, blocking. Proven. The sentence that every distribution supported on at most k points satisfies Assumption 1.2 is false. A point mass at zero violates its anti-concentration condition. Finite support supplies the arithmetic representation condition, subject to the stated bounds. It does not supply the remaining conditions.

Proven. The algorithm also receives the real generators of the arithmetic support. Their existence alone does not give the stated algorithm. Define the lattice penalty parameter used in the quantitative error bound, and state that the generators are known.

`ch-kernel-finite-precision`, nonblocking. Proven. Injective left multiplication preserves the exact right kernel. Coordinatewise rounding does not commute with arbitrary left multiplication. Consequently, the algebraic invariance does not by itself transfer DK22’s finite-precision guarantee to every injective client. Such a transfer needs a precision bound involving the client’s singular values.

Heuristic. Revise the object. The result remains useful, but its title should not suggest an algorithm for every discrete hidden distribution.

5. `fact-rectified-gaussian-gram-estimation`

Proven. The main theorem is stated correctly. Wu, Dimakis and Sanghavi, NeurIPS 2019, Theorem 1 gives the stated Frobenius and bias guarantees for Gaussian latent inputs and nonnegative bias. Claim 1 establishes the rotational ambiguity. Fact 1 and Lemma 2 supply the orthant identity. These statements do not establish recovery of individual latent records. [WDS19, Sections 3 and 4](https://arxiv.org/html/1909.01812v2).

`ch-spherical-origin-mass`, blocking. Proven. The extension to every spherically symmetric input law is false as written. A spherical law can put positive mass at the origin. That mass contributes nothing to either strict halfspace event, and multiplies the claimed probability by the nonzero-radius probability. Exclude an atom at the origin, or condition on a nonzero input.

Proven. For general NGCA records, spherical symmetry no longer justifies the identity. Particular row pairs can still satisfy it. Replace the categorical statement that it “fails” with the statement that the identity is not guaranteed.

Heuristic. Revise the boundary statement while retaining the Gaussian theorem.

6. `conj-quantized-records-zlip-equivalence`

Proven. The algebra of direction (a) is sound. Conditional on the input form, an integer isomorphism sends the sampled coefficient vectors to independent product discrete Gaussian records. The Cholesky factor differs from that isomorphism by an orthogonal map. The equivariant-view coupling therefore applies. Exact reconstruction of a full-rank block gives an isomorphism.

Proven. The proposed widening of the record Gaussian is sufficient for Lemma 2.9 on the good event supplied by Lemma 3.6. Add the full-rank failure probability. Retain Lemma 3.6’s smoothing-error factor, or fix the smoothing error at most one half.

`ch-zlip-width-equivalence`, blocking. Proven. The two directions concern different average-case widths. Direction (a) reduces average-case ZLIP at the base width to reconstruction at the widened width. Direction (b) invokes average-case ZLIP at the record width. These implications do not establish the claimed equivalence at one width. No reverse parameter conversion appears in the sketch.

Proven. The correct current conclusion is a pair of reductions with an explicit width loss. DvW22 Lemma 3.9 does not remove that loss at polynomial widths. Its unconditional polynomial-overhead worst-case reduction requires exponentially large width. Lemma 3.10 charges separately for stronger lattice reduction.

`ch-zlip-fresh-coordinate-samples`, blocking. Proven. Direction (b)’s assertion that the computed integer coordinates are independent discrete Gaussian samples is unjustified when their basis depends on those same records. Conditioning on generation also changes their distribution.

Heuristic. Repair this by using separate blocks. Construct the basis from one block, estimate its metric from another, and run Extract on a fresh block. Conditional on the first block, the fresh coordinates have the required discrete Gaussian law. Extract must use exactly Definition 3.3’s block size and full-rank conditioning.

Proven. The covariance identity itself is correct for a fixed unimodular basis. Recovering the form by entrywise rounding still needs a quantitative argument. Bound the basis size and the error after covariance inversion. Relative covariance concentration offers a route. A statement that polynomially many samples suffice without those bounds is incomplete.

`ch-zlip-arithmetic-cost`, blocking. Proven. The claimed polynomial equivalence mixes polynomial dependence on the width with polynomial dependence on its logarithm. These differ exponentially in the regime used by Lemma 3.9. Moreover, exact arithmetic on Gaussian client weights is not a finite input model.

Heuristic. Either restrict the width to a stated polynomial range and give a finite-precision client model, or retain the dependence on width and precision as explicit resources. Under the experiment requirement of `CONTEXT.md`, this distinction is part of the result.

`ch-zlip-generation-prior-art`, nonblocking. Proven. Generation is the right requirement for this particular upper reduction. Full real rank only identifies a possibly proper sublattice. However, the required polynomial-sample generation result already exists. Haviv and Regev, SODA 2014, Lemma 5.4 proves generation by polynomially many discrete Gaussian samples when the width exceeds the shortest-basis bound. The integer lattice has that bound equal to one. Their Lemma 5.1 supplies the escape probability from proper sublattices. The sharper proposed sample bound is unnecessary for this milestone. [Haviv and Regev, Section 5.1](https://arxiv.org/pdf/1311.0366).

`ch-zlip-certificate-check`, nonblocking. Proven. Checking the Gram identity alone does not certify an integer isomorphism. A rational orthogonal matrix can satisfy that identity. Check integrality and unimodularity too.

Heuristic. Retain this aim as a parameterized reduction theorem. Its mathematics meets the project’s constraint against inserting a cryptographic primitive. The claims of an exact equivalence and an exact exponential “price” should be withdrawn until the parameter and arithmetic issues are settled. The cited algorithms give attack upper bounds, not matching lower bounds.

7. `conj-sq-sample-games-separate`

Proven. The exact kernel invariance is sound. For ZSWB22, compute the unique dependency in the intrinsic d-dimensional span of the representations. The coefficients, and therefore the truncated coefficients entering LLL, agree with those computed from the records. For DK22, the same argument applies to the kernel-dependent stages before the final metric-dependent normalization.

`ch-hidden-label-scale`, blocking. Proven. Injectivity does not preserve ZSWB22’s final Euclidean normalization. Replacing the original linear solve by a solve on representations does not recover the norm of the original direction. Known spacing alone also does not determine the common divisor of a finite label vector.

Heuristic. The proposed gcd repair should work for this particular discrete Gaussian law. Prove that the integer labels are jointly primitive with exponentially high probability. A modular-mass bound, a polynomial tail cutoff, and a union bound over possible prime divisors provide a route. Then divide the returned integer relation by its gcd and multiply by the known spacing. This repairs the sample claim without estimating the unknown client metric.

`ch-games-hidden-client`, blocking. Proven. Full column rank alone is insufficient for the SQ claim. A deterministic identity client reveals the coordinate directly. Explicitly require the right-rotation-invariant, seed-blind client distribution from the protocol class, independent of the records. If this is intended through the phrase “SQ game,” repeat it in the statement.

`ch-sq-fine-output-range`, blocking. Proven. The existing SQ game restricts the returned reconstruction map to values between minus one and one. The proposed hidden label has approximately standard Gaussian tails. Every such bounded map therefore has a positive constant squared-error floor. It cannot attain the proposed vanishing error.

Heuristic. Define a separate fine-reconstruction SQ interface with controlled output moments, or use a bounded target and an appropriate loss. The present lower bound is vacuous in the existing interface.

Proven. After that repair, the testing route is sound in outline. Approximate moment matching follows from Poisson summation. Sufficiently accurate coordinate reconstruction gives a direction estimate through truncated queries. Normalizing that estimate makes the Gaussian expectation of the cosine witness uniformly small, regardless of adaptive selection. Choose the reconstruction constant sufficiently small and account for every auxiliary tolerance.

Proven. The general separation is already explicit in Diakonikolas, Kane, Ren and Sun, NeurIPS 2023, Theorem 1.5 and the discussion “Relation to LLL-based Algorithms for NGCA.” It combines moment-based SQ hardness with the sample algorithms of DK22 and ZSWB22. The additional statement here concerns representations behind an unknown injective client. [DKRS23, Section 1.1.1](https://arxiv.org/html/2403.04744v1).

Heuristic. Retain this as a short transfer result with a primitive-label lemma. It should not be presented as a new general separation between SQ and lattice methods.

8. `conj-coarse-reconstruction-lattice-hard`

`ch-coarse-sample-budget`, blocking. Proven. The statement lacks a lower bound on the number of records per run. Empirical correlation can be large without information about the hidden direction. With one record, absolute uncentered correlation is one for any nonzero scalar output. With two records, absolute centered Pearson correlation is one whenever both vectors are nonconstant.

Proven. Thus the correlation event does not imply the asserted directional overlap as written. Define the correlation convention, handle zero norms, and require enough independent records for the empirical covariance bounds. The sample requirement already used in `prop-fine-reconstruction-to-hclwe` supplies a sufficient starting point.

Proven. With those hypotheses, the sample-based agreement argument holds as follows.

- Under the Gaussian null, each rotated sample block is independent of its secret Haar rotation. Undoing that rotation makes a nonzero output direction uniform. Independent blocks and coins make the two directions independent.
- Under the planted law, empirical correlation controls the component along the hidden direction. An operator-norm bound on the sample matrix controls the denominator.
- Haar randomization makes each resulting direction invariant under the stabilizer of the hidden direction. The same holds conditional on correlation success.
- The two perpendicular components then have exponentially small probability of cancelling the shared directional contribution by a constant amount.

Proven. Define an independent random direction when the extracted vector is zero. Use two blocks, each of the size required by the attacker’s guarantee. Conditional on the common planted direction, their success probabilities multiply. This gives the proposed squared-success advantage with exponential error, after adjusting constants.

`ch-sq-agreement-oracle`, nonblocking. Proven. The builder correctly identifies a failure of this proof in the SQ game. A shared adversarial oracle can correlate its permitted errors with both hidden rotations. The directions after undoing those rotations need not be independent or uniform under the null. Fresh attacker coins do not eliminate that dependence.

Open. This does not prove that every SQ recovery-to-testing reduction needs a non-Gaussian witness. It establishes that this two-run independence argument is unavailable for arbitrary valid SQ answers. Keep that distinction explicit.

Heuristic. This is the strongest aim of the round. Retain it after the sample-size repair. State the general lemma for direction outputs, then derive direction outputs from empirical reconstruction under explicit covariance bounds.

9. `conj-blind-relu-client-inversion`

`ch-relu-output-guarantee`, blocking. Proven. The statement does not specify its success probability, the matrix norm, or uniform bounds on the sub-Gaussian parameter. It also asserts an exact common linear relation for all observed records, although the route only estimates a Gram matrix. These are different guarantees.

Proven. An approximate Gram factor generally gives approximate inversions through different active submatrices. It does not automatically produce one common linear distortion of every latent record. The smallest singular values of those active submatrices control the inversion error.

`ch-relu-estimator-bias`, nonblocking. Proven. Increasing the sample count removes sampling error but does not remove the population bias of an incorrect orthant formula. The proposed route therefore does not establish arbitrary accuracy. It also leaves the row-norm estimator unresolved. WDS19 estimates truncated Gaussian parameters, whereas NGCA projections need not be Gaussian.

Heuristic. A small relative projection of a random row onto the hidden subspace can support a perturbative analysis. It does not yet supply a uniformly accurate estimator. Normalize the rows when stating that projection estimate, control the sub-Gaussian parameter, and distinguish a fixed population bias from sampling error.

`ch-generative-hardness-reference`, nonblocking. Proven. The cited authors and setting need correction. Chen, Jerry Li and Yuanzhi Li, NeurIPS 2022, Theorem 3.1, establish SQ hardness for constructed generators whose output coordinates are sums of ReLUs. That theorem does not refute unrestricted polynomial-time inversion behind the random single-layer client here. It is not a theorem by Chen, Li, Li and Meka in that venue. [Chen, Li and Li, Theorem 3.1](https://proceedings.neurips.cc/paper_files/paper/2022/file/e463a2a3daee91a6dd0e0c41cd2f9f7a-Paper-Conference.pdf).

Heuristic. Replace the present formulation with an approximate inversion aim. Require a polynomial-time map whose mean squared reconstruction error, after one common orthogonal alignment, is small relative to record energy. Specify confidence, client expansion, tail parameters, and precision. Start with Gaussian records to connect Gram estimation to stable record inversion. Then address a stated NGCA family.

Open. Neither WDS19 nor the cited generative-model lower bound settles that revised aim. It remains relevant to the nonlinear upper inclusion, but the present sketch does not justify scheduling it as a theorem for the next round.

## Verdicts

```text
VERDICT fact-lip-average-case ACCEPT
VERDICT fact-zlip-best-algorithms ACCEPT
VERDICT fact-lll-recovers-discrete-hidden-labels REVISE
VERDICT fact-ngca-lattice-basis-reduction REVISE
VERDICT fact-rectified-gaussian-gram-estimation REVISE
VERDICT conj-quantized-records-zlip-equivalence REVISE
VERDICT conj-sq-sample-games-separate REVISE
VERDICT conj-coarse-reconstruction-lattice-hard REVISE
VERDICT conj-blind-relu-client-inversion REVISE
BLOCKING 11
```