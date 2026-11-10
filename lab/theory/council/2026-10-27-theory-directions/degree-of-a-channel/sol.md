---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-27
prompt: lab/theory/council/2026-10-27-theory-directions/degree-of-a-channel/prompt-critique.md
---

Heuristic. Retain the Gaussian transfer and approximate-cancellation result. They support Halil’s aim within a stated SQ game. The meditation does not yet connect those bounds to the measured cost of a practical shadow learner.

proven. The symmetry ceiling is false. The subset bound omits validation precision. The proposed auditor measures dependence, which does not by itself establish the attacker’s decoding price.

## Claims

### def-shadow-learning-game

proven. REVISE. The joint-law correlation identity is correct. It follows directly from the conditional likelihood ratios. The game usefully identifies what the shadow runs and target share. This is a definition with an elementary identity, rather than a new hardness result.

proven. ch-degree-domain. Blocking. The raw degree is ill-posed at the stated generality. The view space need not have coordinates. Absolute continuity supplies neither polynomial moments nor square-integrable likelihood ratios. Specify a Euclidean view space, admissible square-integrable polynomials, and a convention when no informative polynomial exists. The later spectral arguments also need finite joint chi-squared divergence.

proven. Finite moments alone do not make polynomial degree detect every informative channel. Distinct lognormal laws can share every polynomial moment. Let the secret select two such laws. Every polynomial conditional expectation is constant across secrets, although a bounded measurable statistic distinguishes them. This is the moment-indeterminacy phenomenon established by Heyde, Journal of the Royal Statistical Society B, 1963. [Heyde’s paper](https://academic.oup.com/jrsssb/article/25/2/392/7035281?searchresult=1)

proven. Thus non-Gaussian degree requires an explicit filtration of observables. Polynomial completeness is an additional hypothesis when degree is meant to capture all dependence.

### thm-shadow-price-is-generative-exponent

proven. ACCEPT. For a fixed, non-product Gaussian frame family with finite joint chi-squared divergence, the three numbered statements hold. The product marginal, conditional Hermite coefficients, and overlap expansion follow from conditioning and Mehler’s identity.

proven. The decoding-to-detection reduction also holds. Under the null, the validation covariance vanishes for every output decoder. Under an alternative, successful decoding gives a fixed positive gap. The validation queries require a fixed precision depending on the success threshold and target variance. Since the asserted lower bound diverges with dimension, that fixed cost can enter the dimension threshold.

proven. This is a corollary of known machinery. Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, Definition 2.4, Lemma 3.1, Theorem 3.2 and Lemma E.3 supply the exponent, correlation expansion and spherical code. Feldman, Grigorescu, Reyzin, Vempala and Xiao, J. ACM 2017, Lemma 3.10 and Theorem 3.7 supply the detection bound. The meditation correctly retains the actual diagonal correlation. [DPLB24](https://arxiv.org/html/2403.05529v2), [FGRVX17 reading record](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/jacm/FGRVX17.md)

open. ch-conditional-access-transfer. Nonblocking for this theorem. Passive joint SQ access does not cover an attacker that chooses secrets. Almost-everywhere cancellation under the prior gives no uniform bound over conditional queries. That extension needs its own oracle definition and correlation analysis.

heuristic. The subsequent Train-call interpretation remains correctly labelled heuristic. The Gaussian SQ theorem itself proves a bound on an oracle parameter.

### prop-overlap-grading-carries-price

proven. REVISE. Part (a)’s construction works. The exponential coordinate map preserves SQ access while exposing dependence through a linear coordinate. The analyticity argument establishes nonconstant conditional means outside an exceptional set of directions. This is a useful counterexample to raw degree as an intrinsic price.

proven. The subset correlation identity also holds under square integrability. It follows from the classical orthogonal decomposition over independent coordinates. Efron and Stein, Annals of Statistics, 1981, develop this decomposition in their jackknife analysis. The packing argument is elementary. [Efron and Stein](https://pdodds.w3.uvm.edu/files/papers/others/1981/efron1981a.pdf)

proven. ch-subset-validation-precision. Blocking. The displayed query-precision tradeoff does not follow as written. Its detector needs sufficient precision to validate the requested decoding covariance. The statement places no such restriction on the learner’s oracle parameter.

proven. A counterexample uses singleton subsets and independent fair sign coordinates. The secret weakly biases one unknown coordinate. The decoder that averages all coordinates has positive covariance with the secret at every instance and makes no query. Choose the decoding threshold below that covariance. Its unused oracle can have parameter one, while the claimed lower bound grows with dimension.

proven. Repair the bound by charging the larger of the learner’s precision and the required validation precision. Alternatively, state an asymptotic version with a fixed positive decoding threshold and sufficiently large dimension.

proven. The surviving conclusion concerns the dependence of SQ bounds on index geometry. It does not show that growth exponents cannot serve as a chosen comparison convention.

### prop-approximate-degree-price

proven. ACCEPT under the fixed-family interpretation of the preceding theorem. The off-diagonal correlation bound, code size and tail estimate establish the stated lower bound. The Ornstein-Uhlenbeck eigenrelation gives the claimed attenuation of each Hermite energy.

proven. The cancellation condition is sufficient and conservative. It suppresses every lower-degree energy by the strongest common requirement needed in the argument. This is a useful robustness corollary of the existing correlation method. The noise calculation is a standard semigroup identity.

proven. For a fixed law, persistent nonzero lower-degree coefficients eventually violate the displayed cancellation condition as dimension grows. A dimension-dependent approximate family needs uniform control of the signal, diagonal correlation and decoding threshold.

proven. The result establishes lower bounds. The sentences assigning a full price to the degree profile or a matching benefit to release noise need an upper-bound argument for the same task and attacker class.

### prop-orthogonal-averaging-cancels-one-degree

proven. REJECT as written. Parts 1 and 2 hold. The invariant-polynomial calculations in part 4 hold. Part 5 holds for independent Gaussian noise when the required polynomial moments exist.

proven. ch-invariant-transmission. Blocking. Part 3 does not follow. An invariant of the records need not reach the view. Moreover, polynomial degree in the records differs from polynomial degree in the released view.

proven. Consider a secret record with either of two different norms. Let the release depend only on that norm. For one norm, release either sign of one with equal probability. For the other, release zero with probability one half, and otherwise either sign of the square root of two with equal probability.

proven. Both releases have matching moments through degree three. Their fourth moments differ. The raw channel degree is four, although the record Gram matrix varies. This release has exactly the required form after orthogonal averaging because it depends only on the norm.

proven. The valid conclusion is that full orthogonal averaging makes the conditional view law factor through the Gram matrix. Recovering that matrix requires an additional property of the release. Empirical whitening establishes such recovery for the registered linear-client model, not for arbitrary releases.

proven. The optimizer distinction is known. Li, Zhang and Arora, 2021, Theorem C.1, Corollary C.2 and Table 1 distinguish orthogonally equivariant gradient methods from coordinate-adaptive methods with permutation and sign symmetries. Those symmetries do not establish transmission of their invariants. [Li, Zhang and Arora](https://arxiv.org/html/2010.08515)

### prop-seed-cannot-index-the-family

proven. REVISE. Clause (a) holds for independently resampled seeds and risk averaged over the target seed. Clause (b)’s covariance identity holds with finite second moments and independence conditional on the fixed matrix. Neither calculation is a new hardness theorem.

proven. ch-persistent-seed-index. Blocking for the categorical heading. Independent resampling eliminates a shared seed index. A persistent hidden seed can index a family. Fix a rotation of a degree-four Gaussian frame channel and reuse that rotated channel across views. Its rotation is a shared hidden index, and the preceding Gaussian theorem applies.

proven. Repeated observations of one frozen client provide precisely the distinction that the broad heading suppresses. Fresh shadow training, repeated target evaluations, reuse of an opaque seed name and disclosure of the seed give different games. If an access mode discloses the rotation, the hidden-index premise disappears.

proven. Restrict the prohibition to independently resampled seed components. The general requirement is a shared unknown instance parameter, whose origin can include a persistent seed.

proven. The displayed conditional expectation is the Bayes predictor for squared loss. For the stated bounded covariance objective, an optimal rule uses the sign of the centered conditional expectation.

### prop-targeted-reader-no-learning-price

proven. ACCEPT within the stated unrestricted SQ model. Clause (a)’s query separates the laws at the printed precision. The likelihood-ratio test and total-variation characterization are classical, from Neyman and Pearson, Philosophical Transactions of the Royal Society A, 1933. [Neyman and Pearson](https://www.stats.org.uk/statistical-inference/NeymanPearson1933.pdf)

proven. Clause (b)’s correlation identities hold. Its decoding-to-detection reduction requires validation precision, as above. Clause (c) also holds as a comparison between datasets containing either of two fixed candidates with the same norm.

proven. Clause (c) does not establish ordinary membership privacy. A view that releases all record norms satisfies orthogonal invariance. For continuous Gaussian records, it can reveal whether a candidate’s exact norm occurs in the training set.

proven. ch-unpriced-query-computation. Nonblocking for the formal proposition. SQ access permits the likelihood-ratio indicator as one query without charging its construction or evaluation. Knowing two laws does not supply an efficient implementation of that indicator. The proposition therefore establishes no general absence of computational cost for targeted attacks.

## The named conjecture in Next

### conj-degree-energy-estimator-meets-price

proven. REVISE. The unbiasedness and null variance statements hold. The proposed alternative variance bound also follows from standard U-statistic theory. Weight the orthonormal Hermite feature vector by the bounded target. Its second-moment matrix is bounded by the identity because the view marginal is Gaussian. Its mean has squared norm equal to the stated signal energy. Hoeffding’s decomposition then gives the proposed two variance terms with a universal constant. The underlying method is classical, from Hoeffding, Annals of Mathematical Statistics, 1948.

proven. ch-detection-decoding-gap. Blocking. The claimed match to the attacker’s price does not follow from this variance calculation.

proven. First, the estimator measures the energy selected by one target function. That function can be orthogonal to the conditional Hermite coefficient even when the full channel energy is positive.

proven. Second, estimating dependence does not construct a decoder. Already at degree one, detecting a dense unknown-direction mean signal and recovering its direction to constant accuracy have different sample requirements.

proven. Third, the estimator uses reusable samples. The lower bound concerns an adversarial SQ oracle. Equality of their dimension exponents does not establish equality of prices for one attacker class.

heuristic. This estimator is the strongest constructive idea in the meditation. It gives an experiment a precise target without requiring the hidden direction. Present it as an estimator with a confidence guarantee and an explicit signal assumption. A matching decoding theorem remains separate.

## The direction as a whole

heuristic. The useful direction is the joint channel, its observable energy profile, and the geometry of the unknown instance family. This serves Halil’s request to measure learning-based attacks. Restricting the whole programme to the first nonzero degree would discard signal strength, target dependence and access costs that his request makes central.

proven. The strongest established result here is the Gaussian decoding-to-detection transfer. Its main ingredients are known. The degree-four link is also known through DPLB24 Example 2.7(ii), Corollary 2.8 and Lemma D.2. The level-set calculation supplies an explicit explanation of that example. [DPLB24](https://arxiv.org/html/2403.05529v2)

heuristic. Drop the symmetry ceiling and the recommendation to abandon a calculus of training mechanisms. The counterexample to that ceiling removes the stated reason for abandoning it. Retain the distinction between invariant structure and structure that the release actually transmits.

open. ch-real-training-mechanism. Nonblocking. The meditation identifies no mechanism of deep training that produces its required conditional moment cancellation. Equivariance constrains a channel. Gaussian noise attenuates signal. Quantization can erase signal. A proof that honest nonlinear training creates a measured cancellation profile remains missing.

heuristic. The claim that natural data impose a degree-four ceiling exceeds the cited evidence. The registered ICA result assumes independent non-Gaussian attributes. It does not establish a universal profile for natural images, learned representations or training transcripts. Nonzero kurtosis also supplies no measured lower bound on signal strength.

proven. ch-practical-learner-transfer. Nonblocking for the accepted SQ results. Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, Theorem 1c concerns a specified batch, precision and adversarial-rounding regime. It does not automatically cover the VAE or shadow-model attacker in Halil’s request. [AKMSS21 reading record](/Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/neurips/AKMSS21.md)

heuristic. The meditation drifts from Halil’s aim when it treats a worst-valid-oracle lower bound as the main measure of practical effort. His stated target requires the attack’s architecture, training rule, sample reuse, inference cost and Train-call cost to enter the comparison.

open. ch-programming-admissibility. Nonblocking. An engineered channel is not disqualified merely because its moments were designed. Under Halil’s rule, admissibility requires the programmed value to be indistinguishable from honest sampling in each party’s allowed view. An unchanged marginal distribution alone does not prove that joint-transcript requirement.

heuristic. The next useful result would pair the proposed energy estimator with one explicit decoding task on one training-induced channel. It should prove both bounds for the same access model and charge the experiment’s computation as well as its training runs.

## Verdicts

```text
VERDICT def-shadow-learning-game REVISE
VERDICT thm-shadow-price-is-generative-exponent ACCEPT
VERDICT prop-overlap-grading-carries-price REVISE
VERDICT prop-approximate-degree-price ACCEPT
VERDICT prop-orthogonal-averaging-cancels-one-degree REJECT
VERDICT prop-seed-cannot-index-the-family REVISE
VERDICT prop-targeted-reader-no-learning-price ACCEPT
VERDICT conj-degree-energy-estimator-meets-price REVISE
BLOCKING 5
```