---
model: gpt-6-astra
discussant: astra
date: 2026-10-25
prompt: lab/theory/spaces/computational-limits/round-00/prompt-astra.md
---

Proven. The builder refutes the proof note’s unrestricted security conclusion. The exact-average counterexample works. The honest-sampling version works with high probability, with two implementation qualifications below. The post-processing lemma is the correct residue.

Proven. The three aims do not yet establish a computational separation. Their present statements omit assumptions that affect identifiability, simulation, and oracle access. The general training-cost equivalence also has a counterexample. I raise twelve blocking challenges.

1. `fact-fgrvx17-planted-clique-sq-bound`

Proven. ACCEPT. FGRVX17, Theorems 2.9, 2.10 and 5.4 support the statements about distributional planted biclique. The distinction between that distribution and the empirical row distribution of one graph is essential and correct.

Proven. The upper bound from coordinate queries also checks. These results constrain access to data, while allowing unrestricted computation between queries. They therefore supply a valid comparison model, not a general computational lower bound.

2. `fact-sq-simulates-minibatch-sgd`

Proven. REVISE. AKMSS21, Theorems 1a and 1c have the stated precision regimes. The worst-case-rounding qualification is necessary.

`ch-floating-point-identification`, nonblocking. Heuristic. The identification with single precision requires an explicit arithmetic model. Floating-point arithmetic does not implement the paper’s uniform rounding lattice. The theorem also permits constructed models and increases in parameter count and training steps. It does not say that a given conventional network realizes arbitrary PAC algorithms.

Proven. The sentence that “only” polynomial-time or information-theoretic bounds apply is too strong. Bounds for narrower architectures, dynamics, or attacker classes remain possible. The justified conclusion is that a generic SQ lower bound does not cover the entire fine-precision bSGD class.

3. `fact-lei-random-expansive-layers-invertible`

Proven. ACCEPT with the builder’s pointwise interpretation. LJDD19, Theorem 3 supports recovery of a fixed input, independent of the Gaussian weights, through expansive ReLU layers. The union bound for finitely many independently specified records is appropriate.

`ch-pointwise-inversion`, nonblocking. Proven. The cited Lemma 1 uses the word “injective” more broadly than its binomial argument establishes. Counting positive coordinates for a fixed input proves uniqueness of that input’s preimage on the stated event. It does not prove simultaneous global injectivity. The builder correctly restricts the probability statement, and should retain that restriction everywhere.

4. `fact-clwe-hardness` and `fact-hclwe-sq-correlation-bound`

Proven. REVISE both objects for a shared normalization error.

`ch-gaussian-normalization`, blocking. Proven. BRST21 uses Gaussian density proportional to the exponential of minus pi times squared norm. Its unit-width Gaussian has covariance equal to the identity divided by twice pi. The builder defines its reference Gaussian to have identity covariance, then copies BRST21’s densities, widths, parameters, and correlation formulas unchanged.

Proven. Corollary 4.2, Proposition 8.3 and Theorem 8.1 support the quoted results in BRST21’s convention. A deterministic rescaling transfers the results, but the density and periodicity parameters must change consistently. This also affects the pancake construction in the second aim.

Proven. Large total variation from the null establishes distinguishability, not automatically recovery of the hidden direction. BRST21’s homogeneous law also identifies the direction only up to sign. The sentence asserting that an unbounded algorithm “finds” the direction needs a separate identification statement and accuracy criterion.

5. `fact-ngca-sq-lower-bound`

Proven. REVISE the interpretation, while retaining the theorem statement. The PDF of DKRS23, Theorem 1.5 confirms the displayed parameter restrictions, approximate moment condition, tolerance bound, and query bound. No finite chi-square assumption is required. [DKRS23, Theorem 1.5](https://arxiv.org/pdf/2403.04744).

`ch-ngca-statistical-scope`, nonblocking. Open. “Identifiable with O(n) samples for most A” has no defined scope or recovery criterion. The theorem does not supply that claim.

Proven. A particularly relevant omission is the paper’s discussion of discrete moment-matched laws. Polynomial-time lattice-reduction algorithms can solve some such instances with linear sample complexity despite their SQ hardness. The proposed experiments therefore need an attacker outside the SQ family. An SQ separation alone cannot predict security against all efficient blind attackers.

6. `fact-generative-exponent-sq-recovery-bound`

Proven. REVISE. DPLB24, Theorem 3.2 is transcribed correctly, including its signal-strength condition and weak-recovery target.

`ch-generative-upper-bound-scope`, nonblocking. Proven. Theorem 4.1 requires a suitable label denoiser. Its adjusted signal strength includes a logarithmic loss, which the builder leaves undefined. The information-theoretic bound in Theorem 6.1 also depends on accuracy and signal strength and carries logarithmic factors.

Proven. Remark 3.3 explicitly leaves open an SQ detection versus estimation gap. The conclusion additionally states that the partial-trace algorithm’s power iterations are not bona fide SQ operations. Thus the paper does not establish a matching SQ estimation upper bound. This becomes a blocking issue when the third aim claims one common price.

7. `fact-ica-breaks-rotation-perturbation`

Proven. REVISE. Liu, Kargupta and Ryan, IEEE TKDE 2006, Sections 3 and 4 support the attack discussion under independent non-Gaussian source coordinates and a suitable mixing matrix. Their Theorem 4.3 concerns matrix decomposability. It is not a computational guarantee for arbitrary non-Gaussian data. [Liu, Kargupta and Ryan](https://userpages.cs.umbc.edu/hillol/PUBS/Papers/tkde.pdf).

`ch-nongaussian-identifiability`, blocking. Proven. The conclusion that the seed protects “only nearly Gaussian data” does not follow. A non-Gaussian spherically symmetric distribution is invariant under every orthogonal transformation. Rotated observations cannot identify its original orientation, even with unlimited samples and computation. Independence of source coordinates cannot be dropped.

8. `fact-instance-encoding-privacy-learnability`

Proven. REVISE.

`ch-encoding-theorem-hypotheses`, blocking. Proven. CDGJMMSTT21, Theorem 3 assumes two distinct balanced concepts, but its accuracy assumption concerns one concept and its complement. Its attack targets one of three specified concepts. “Accuracy on two balanced concepts” does not state those hypotheses.

Proven. Theorem 4 requires the rich concept class and the listed oracle access. Theorem 5 requires an efficient protocol with decomposable instance encoding and balanced encoded accuracy. Those conditions should appear in the object.

Proven. Encoder access is not equivalent to knowing the seed. Encoder access permits chosen-input evaluation without revealing the seed. Conversely, knowing an initialization need not permit evaluation of a trained encoder whose current parameters remain unknown. These must remain distinct capabilities.

9. `fact-ideal-keyed-encoding-weak-learner`

Proven. REVISE for precision. CGJMMT21, Definition 2 requires equality in distribution over the random key for equal-label inputs. It does not require pointwise equality under one fixed key.

`ch-ideal-encoding-quantifiers`, nonblocking. Proven. Theorem 1 assumes balanced-error guarantees for every concept in the class. The two supplied examples have opposite labels. The predictor receives learner and keyed-encoder oracle access, and its risk guarantee holds under an arbitrary evaluation distribution. These quantifiers materially clarify what the theorem extracts.

10. `fact-cohen-narcissus-equals-one-wayness`

Proven. ACCEPT. CKMMNST25, Theorem C.5 supports the equivalence for efficiently computable, well-spread functions, the equality-of-images relation, independent uniform inputs, and negligible additive slack.

Proven. The builder correctly distinguishes preimage finding from metric reconstruction. This fact does not furnish a reconstruction lower bound for the proposed network.

11. `fact-unsplit-unknown-client-inversion`

Empirical. ACCEPT for the reported experiment. EKC22, Table 2 contains the quoted MNIST errors, and the attack jointly optimizes inputs and client parameters.

`ch-unsplit-explanation`, nonblocking. Heuristic. The proposed NGCA account does not yet predict these results. The client is convolutional, and the round supplies neither the needed distributional fit nor a quantitative attack threshold. The experiment establishes that blind inversion can succeed in that setting.

12. `fact-nrnt25-private-layer-hardness-route`

Proven. REVISE. The builder correctly identifies the missing reduction from arbitrary reconstruction to learning the private layers.

`ch-gradient-inversion-degeneracy`, blocking. Proven. The unconditional wording of the Proposition 3 summary is false. Recovery through the displayed weight-gradient and bias-gradient identity requires a nonzero corresponding bias-gradient coordinate and a single-record gradient. Zero gradients, including those from an inactive ReLU path, reveal no such ratio. Public discriminator parameters and gradients alone do not guarantee exact recovery.

Proven. The private-layer approximation argument remains a restriction to one attack route. Hardness of learning a forward map does not imply hardness of recovering a record from a particular observation.

13. `thm-fs-sq-black-box-reduction`

Proven. ACCEPT the builder’s refutation, with the following line-by-line assessment.

Proven. Step 1 recovers all occupied prefixes from exact counts. There are at most as many occupied prefixes at each depth as rows, so the stated query bound holds.

Proven. Step 2 recovers every coordinate of each row once the prefixes distinguish the rows. Recovering a row multiset suffices for the later test. Recovering vertex identities is unnecessary.

Proven. Step 3 correctly removes the two possible diagonal positions. The remaining comparisons involve independent fair edge bits. Conditioning on the prefix columns avoiding the planted set preserves that argument.

Proven. Step 4 also holds in the stated polynomial-size clique regime. A passing assignment uses distinct rows. Its prescribed off-diagonal ones either encounter an impossible diagonal constraint or require at least the stated number of independent unordered edges. The union bound therefore defeats false acceptance under the null.

`ch-honest-oracle-qualification`, nonblocking. Proven. The honest batch averages meet the fine-accuracy event with the claimed Hoeffding bound. Conditional bounds and a union bound handle adaptive queries. However, an honest finite batch is not an always-valid STAT oracle. State its failure probability explicitly, and cap the trie construction on erroneous answers. The exact oracle already gives the strict counterexample without this qualification.

Proven. The quadratic query count does not represent constant effective precision. The counterexample exploits answers accurate enough to recover integer counts, while the interface merely permits constant error. Its honest realization uses roughly quartic total row draws, with a logarithmic factor.

Proven. The algebraic post-processing inequality survives if both sides refer to the same graph oracle and answer mechanism. What fails is the claimed negligible upper bound and its universal “in particular” clause. The builder makes this distinction correctly.

Proven. The note has another independent algebraic defect. Substituting its clique size into its displayed advantage expression does not produce the following displayed expression. Its numerical calibration also treats an unspecified asymptotic constant as a numerical guarantee.

14. `lem-sq-learner-post-processing`

Proven. ACCEPT the core lemma. Its proof is valid line by line. Compose the learner and attacker. Preserve the learner’s queries and independent coins. The attacker adds computation but no data access. FGRVX17, Theorem 2.10 or Theorem 5.4 then applies under the respective oracle quantifiers.

`ch-postprocessing-simulation-scope`, nonblocking. Proven. The appended SGD application should explicitly translate STAT precision into a sufficient VSTAT parameter and include the simulation’s error slack. It must preserve robustness to valid roundings through the final attack decision. Theorem 1c does not justify a claim about the actual floating-point trajectory.

Proven. This lemma is a valid access-budget statement. It is not a new computational hardness mechanism. The 1-STAT budget counts fresh samples from which only one bit is observed. It must not be reported as a lower bound for unrestricted sample access.

15. `def-seed-blind-reconstruction-game`

Proven. REVISE.

`ch-seed-price-definition`, blocking. Proven. Fixing the update and view does not finish the definition. The correlation is undefined for zero-norm outputs or targets. The resource ratio is undefined when the denominator is zero or both success thresholds are unattainable. Several resources also have no single minimum without fixing the others.

Proven. Define a success function at specified resource budgets, or a resource tradeoff set. Specify the treatment of zero norms, attainable success levels, target selection, and probability over the initialization. Separate reconstruction of observed records from prediction on fresh records.

Proven. Experiments can estimate the success and cost of named attacks. They cannot identify the optimum over all polynomial-time attackers by running a finite collection. Thus the claim that every term of the optimal price is experimentally measurable needs revision.

Proven. The independent-record baseline is a legitimate Narcissus-style specialization. It does not remove information already supplied by labels. A label-aware baseline would answer a different question.

16. `conj-seed-price-is-ngca-price`

Proven. REVISE. The symmetry argument has a valid restricted form, but the stated four-part conjecture does not follow.

`ch-transcript-side-information`, blocking. Proven. The trajectory coupling works when every input-dependent operation respects the transformation, all optimizer states transform correctly, and the simulator receives the same labels and other side information. Equivariance of the first weight update alone is insufficient.

Proven. Most importantly, simulation from rotated records and their labels is not simulation from the unlabeled record law. The game allows the server to hold labels. If a label reveals the target coordinate, the server reconstructs it directly, regardless of the marginal NGCA hardness. A reduction receiving only unlabeled NGCA samples cannot manufacture unknown target-dependent labels.

Proven. An operation on the raw input does not necessarily break equivariance. Radial normalization is one counterexample to that blanket exclusion.

`ch-hidden-frame-symmetry`, blocking. Proven. For a symmetric one-dimensional planted law, reversing the hidden direction preserves the observation law and reverses the signed target. Without orientation information, expected signed correlation is zero. The pancake law has this ambiguity.

Proven. Part (d) switches to recovery up to the symmetry group, while the game and the earlier parts use oriented coordinates. These are different objectives. Quotient recovery must be defined before any computational price is claimed.

`ch-whitening-and-invertibility`, blocking. Proven. Right rotation invariance permits a zero matrix and matrices with fewer rows than columns. Neither supports exact inversion. A general subsequent network can also erase information.

Proven. The linear upper bound needs full column rank, a frozen affine map, and access to its centered linear output. Population whitening then produces an orthogonal image on the output support. Empirical whitening adds estimation error and sample cost. A trainable map does not generally preserve the independence needed to conclude that the residual rotation is Haar relative to the observed records.

`ch-sq-attacker-interface`, blocking. Proven. Frozen representations are independent conditional on the shared initialization. Marginally, they share that latent variable. Query composition works after fixing a simulated initialization, provided the attacker receives only statistical queries to the resulting population law.

Proven. The proposed game instead gives the attacker the record-level view. Giving raw representations and subsequently training an attacker by SGD does not turn the entire attack into an SQ algorithm. Define a separate population-SQ game and prevent unrestricted sample preprocessing.

`ch-ngca-testing-transfer`, blocking. Proven. The proposed auxiliary queries are unbounded because they multiply reconstruction outputs by Gaussian coordinates. Bounding the reconstruction output alone does not fix this. Hermite queries are also unbounded.

Proven. The sketch additionally uses the larger of two tolerances where simultaneous estimation requires meeting both precision requirements. Approximate moment matching leaves an additive error term that part (b) drops. A first nonmatching moment need not exist, or have appreciable magnitude, under the assumptions stated.

Open. A scalar reconstruction-to-direction reduction is plausible after fixing normalization, tails, truncation, and a quantitative non-Gaussian witness. The general subspace and testing claims remain unproved.

Open. Part (c) is plausible for a suitable unlabeled, normalized pancake instance and a reconstruction guarantee strong enough for regression and independent validation. It needs explicit success probability, sample conditioning, error propagation, and a periodic testing gap. “All records” alone does not supply those conditions.

Proven. The symmetry mechanism is already known. Li, Zhang and Arora, ICLR 2021, Theorem C.1 gives invariant initialization plus equivariant updates. Remark C.1 extends the argument to stochastic and trajectory-dependent updates. The transcript coupling is a direct extension when the exposed quantities remain identical under that coupling. [Li, Zhang and Arora](https://arxiv.org/html/2010.08515).

Open. The checked sources do not establish the proposed quantitative reconstruction equivalence. Its potential contribution lies in a correct reduction with explicit resources and leakage assumptions. Rotation symmetry and ICA vulnerability themselves are prior work.

17. `conj-reconstruction-at-training-cost`

Proven. REVISE. The population argument in part (a) is useful. Part (b) is false at its present generality.

`ch-population-to-sample-reconstruction`, blocking. Proven. With an injective frozen linear representation, population whitening, and excess risk relative to the Bayes predictor, the first-Hermite projection argument holds. Orthogonality bounds the projection error, and normalization gives the claimed type of directional guarantee.

Proven. The stated sample count does not follow from finite second moment of the label and excess risk alone. Estimating the feature-weighted predictor requires tail control or a robust estimation argument. Dependence on signal magnitude and confidence must be stated. Independent evaluation samples, whitening error, and the boundary at zero excess risk also require treatment. LeakyReLU inversion must precede linear whitening.

`ch-learning-is-not-direction-recovery`, blocking. Proven. Consider a Gaussian target coordinate multiplied by an independent random sign to produce the label. The label’s conditional mean is zero. The Bayes square-loss predictor is therefore the constant zero predictor, which requires no direction learning. Yet squared labels reveal the squared target coordinate, and the generative exponent is two.

Proven. Thus optimal square-loss prediction can be trivial while reconstruction up to sign remains a nontrivial inference problem. The generative exponent measures information in the full label distribution. The Hermite coefficients of the Bayes predictor measure its conditional mean. They cannot be interchanged.

Proven. The claimed common threshold also omits the dimension-dependent estimation term in DPLB24, Theorem 4.1. For generative exponent one, its sample upper bound does not reduce to the square-root-of-dimension detection scale. For larger exponents, the sample-based upper bound still does not establish a matching SQ estimation algorithm.

Open. A defensible revised aim would restrict the target to information recoverable from a sufficiently accurate conditional-mean predictor, or require the learner to estimate the full conditional label law. Its cost comparison must retain accuracy, signal strength, and access-model parameters.

Proven. The proposed attacker-class decision is therefore appropriate only after separation into distinct games. Use population-SQ attackers for unconditional query bounds. Use polynomial-time sample attackers for conditional computational bounds. Apply AKMSS21 to a specified robust coarse-precision training model, including all preprocessing. The current experiments can measure named attacks, but cannot certify the optimum computational price.

## Verdicts

```text
VERDICT fact-fgrvx17-planted-clique-sq-bound ACCEPT
VERDICT fact-sq-simulates-minibatch-sgd REVISE
VERDICT fact-lei-random-expansive-layers-invertible ACCEPT
VERDICT fact-clwe-hardness REVISE
VERDICT fact-hclwe-sq-correlation-bound REVISE
VERDICT fact-ngca-sq-lower-bound REVISE
VERDICT fact-generative-exponent-sq-recovery-bound REVISE
VERDICT fact-ica-breaks-rotation-perturbation REVISE
VERDICT fact-instance-encoding-privacy-learnability REVISE
VERDICT fact-ideal-keyed-encoding-weak-learner REVISE
VERDICT fact-cohen-narcissus-equals-one-wayness ACCEPT
VERDICT fact-unsplit-unknown-client-inversion ACCEPT
VERDICT fact-nrnt25-private-layer-hardness-route REVISE
VERDICT thm-fs-sq-black-box-reduction ACCEPT
VERDICT lem-sq-learner-post-processing ACCEPT
VERDICT def-seed-blind-reconstruction-game REVISE
VERDICT conj-seed-price-is-ngca-price REVISE
VERDICT conj-reconstruction-at-training-cost REVISE
BLOCKING 12
```