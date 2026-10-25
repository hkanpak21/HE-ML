# Literature scan, learning-bounded privacy adversaries, 2026-10-25

Run by a reader subagent from the HE-ML session of 2026-10-25. Every paper below
was opened in full unless the entry says otherwise. Section and theorem numbers
come from the arXiv or author copy. Absence claims rest on about twelve web
searches and a keyword filter over the 267 papers citing Xu et al. that Semantic
Scholar returned, so they are empirical. The opened copies were kept in the
session scratchpad and are not in the repository.

The question scanned: measure a privacy adversary by learning-theoretic
resources. The attacker trains an attack model (membership classifier,
inversion decoder, attribute probe) from a bounded class with bounded samples.
Lower bounds come from hard learning problems (statistical-query lower bounds)
or from reductions between learning problems. The training seed is treated as
an attacker resource.

## Usable information and leakage

- Xu, Zhao, Song, Stewart, Ermon, "A Theory of Usable Information under
  Computational Constraints", ICLR 2020, https://arxiv.org/abs/2002.10689.
  Definitions 1 to 3 define V-information relative to a predictive family.
  Proposition 1 recovers Shannon information for all predictors. Proposition 2
  gives monotonicity in the family and zero under independence. Section 3.2
  shows by an example that V-information can grow under computation, so data
  processing fails for bounded families (an illustration, not a theorem).
  Theorem 1 is a PAC estimation bound through Rademacher complexity. Not
  covered: the procedure that searches the family, leakage at a fixed attacker
  sample size, any privacy game, any lower bound from a hard learning problem.
- Mo, Borovykh, Malekzadeh, Haddadi, Demetriou, "Layer-wise Characterization of
  Latent Information Leakage in Federated Learning", ICLR 2021,
  https://arxiv.org/abs/2010.08762. Empirical V-information from gradients to a
  property. No theorem.
- Mo and coauthors, "Quantifying and Localizing Usable Information Leakage from
  Neural Network Gradients", arXiv 2105.13929. Usable attribute and original
  information. No lower bound. Empirical.
- Citation sweep: no other privacy or attack paper among the citers of Xu et al.

## Privacy against a bounded adversary class

- Zhao, Chi, Tian, Gordon, NeurIPS 2020, https://arxiv.org/abs/1906.07902.
  Definition 2.2 is the inference advantage of a class. Every lower bound is
  information-theoretic, and none uses the class restriction.
- Hamm, "Minimax Filter", JMLR 18(129), 2017. Theorems 1 and 4 bound the
  defender's generalization gap through Rademacher complexity.
- Romanelli, Chatzikokolakis, Palamidessi, Piantanida, CCS 2020,
  https://arxiv.org/abs/2005.04399. Sample complexity of estimating
  g-vulnerability. The adversary is unbounded.
- Cherubin, Chatzikokolakis, Palamidessi, F-BLEAU, IEEE S&P 2019 (venue from
  recollection). Consistent estimation of the Bayes risk, no uniform rate.
- Haghifam, Smith, Ullman, "The Sample Complexity of Membership Inference and
  Privacy Auditing", arXiv 2508.19458. Theorem 3.1: in Gaussian mean estimation
  with noise-adding estimators, in high dimension no attack with fewer than
  order n plus n squared rho squared reference samples reaches accuracy 0.51.
  Theorem 3.2 gives a matching attack. With known covariance order n samples
  suffice. Unbounded attacker, the only resource is reference samples. The
  closest formal precursor of the bounded-samples axis.
- Carlini and coauthors, "Is Private Learning Possible with Instance Encoding?",
  IEEE S&P 2021 (venue from recollection), https://arxiv.org/abs/2011.05315.
  Theorems 3 to 5 reduce privacy to learnability: either an efficient attack has
  advantage near one half minus the learner's error, or an efficient learner is
  near perfect.

## Learning-complexity lower bounds for privacy attackers

- No paper found that bounds a membership, inversion, attribute or
  reconstruction attacker from below with a statistical-query lower bound or
  another hard learning problem (empirical, search-based).
- Wang, Lee, Lei, "Reconstructing Training Data from Model Gradient, Provably",
  AISTATS 2023, https://arxiv.org/abs/2212.03714. Theorem 5.1 recovers inputs
  from gradients of a random two-layer net with known weights by tensor
  decomposition. Section 3 notes single-sample gradient inversion is
  NP-complete.

## Complexity of inverting networks

- Lei, Jalal, Dhillon, Dimakis, "Inverting Deep Generative Models, One Layer at
  a Time", NeurIPS 2019, https://arxiv.org/abs/1906.07437. Theorems 1 and 2:
  preimage existence is NP-complete for fixed two-layer and four-layer ReLU
  nets. Theorem 3: random Gaussian layers with expansion at least 2.1 are
  inverted exactly by layer-wise linear programs with high probability.
- Hand, Voroninski, COLT 2018, https://arxiv.org/abs/1705.07576. Theorem 1: for
  random expansive generative priors the empirical risk has a descent direction
  away from the truth and its negative multiple.
- Both assume known weights, so they cover the known-seed case only. The
  NP-hardness is worst case over constructed weights (heuristic: it says nothing
  about the law that training induces).

## Computational differential privacy, boundary marker

- Mironov, Pandey, Reingold, Vadhan, CRYPTO 2009. IND-CDP and SIM-CDP against
  non-uniform PPT distinguishers. Theorem 2 extends to an arbitrary distinguisher
  family at the cost of closing it under thresholded sums, which is the price a
  class-relative definition must pay.

## The seed as an attacker resource, unknown bottom models

- Balle, Cherubin, Hayes, "Reconstructing Training Data with Informed
  Adversaries", IEEE S&P 2022 (venue from recollection),
  https://arxiv.org/abs/2201.04845. Appendix A, Table III (empirical, MNIST):
  reconstruction MSE 0.0089 with known initialization against 0.0695 with fresh
  seeds. The authors state the attack fails without the initial parameters.
  The closest prior for the seed as a resource, and empirical only.
- Yala and coauthors, NeuraCrypt, arXiv 2106.02484. Theorem 1 is the Bayesian
  posterior over a law of random-network encoders.
- Carlini and coauthors, "NeuraCrypt is not private", arXiv 2108.07256.
  Empirical break by boosting to a perfect matching. Theorem 1: an ideal keyed
  encoding with a weak learner yields a near perfect learner.
- Erdoğan, Küpçü, Çiçek, "UnSplit", WPES 2022, https://arxiv.org/abs/2108.09033.
  Inverts an unknown split-learning client model by joint optimization. Works
  at MNIST split depth 1, before and after training (empirical, Table 2).
- Gao, Zhang, "PCAT", USENIX Security 2023. Pseudo-client attack with small
  public data. Empirical.
- Ye, Zhu, Liu, Shokri, Cevher, "Initialization Matters", NeurIPS 2023,
  https://arxiv.org/abs/2310.20579. Theorem 3.1: KL between Langevin trajectories
  on neighbouring datasets equals the integrated squared gradient difference.
  The initialization is revealed, nothing about a hidden seed.

## Limits of statistical-query models for SGD

- Abbe, Sandon, NeurIPS 2020, https://arxiv.org/abs/2001.02992. Theorem 1:
  batch-one SGD on a polynomial net from a constructed initialization learns
  anything polynomial-time learnable. Theorem 3: noisy GD fails under small
  cross-predictability.
- Abbe, Kamath, Malach, Sandon, Srebro, NeurIPS 2021,
  https://arxiv.org/abs/2108.04190. Theorem 1c: when batch size times squared
  precision exceeds a log factor, SQ simulates mini-batch SGD, so an SQ lower
  bound on an attack task binds SGD-trained attackers in that regime (proven
  given the SQ bound). Theorem 1a: at fine precision SGD simulates PAC, so the
  bound says nothing about batch-one or fine-precision attackers.

## Verdict of the scan

1. Formalized already (proven in the papers): class-relative leakage, finite
   sample estimation of it, reference-sample complexity of membership inference
   for an unbounded attacker, privacy-to-learnability reductions, Bayesian
   privacy over a law of encoders, inversion complexity with known weights.
2. Measured only (empirical): the seed as a resource, attacks on unknown bottom
   models.
3. Open as far as found: any lower bound on a privacy attacker from a hard
   learning problem, leakage bounded in both class and samples with a lower
   bound technique, a formal separation between known-seed and unknown-seed
   attackers.
4. Most likely new: a seed separation for split learning over random expansive
   ReLU bottom models. Known seed gives polynomial-time inversion (Lei et al.
   Theorem 3). Unknown seed would need super-polynomially many SQ queries, which
   Abbe et al. Theorem 1c carries to SGD attackers in that regime. Risks
   (heuristic): the training transcript leaks the seed, and inversion is
   regression, which needs a careful real-valued SQ framework.
