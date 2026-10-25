# Map of the FORMAL_SECURITY literature wiki

Mapped 2026-10-25 from `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY`, read only. Every path below is relative to that root. The map covers the root `CLAUDE.md`, `wiki/`, `raw/` and `.sink/`. It does not cover `exp/`. Each source line records what the wiki page records, not what the paper says. Nothing here was checked against a PDF.

## 1. How the wiki works

The wiki holds four page types under `wiki/`, each with YAML front matter and a lowercase hyphenated slug. There are 200 source pages, 83 concept pages, 116 entity pages (all authors) and 5 analysis pages, plus four empty stub files (`wiki/N.md`, `wiki/Untitled*.md`). Every source page carries `claim_quantifier`, `antecedent` and a Claim Boundary section, and a block of `cls_` classification fields stamped 2026-08-22 or 2026-08-27. An ingest writes the source page, updates concept and entity pages, and appends to the append-only `wiki/log.md`. Errors are corrected in place under a dated Correction note and never deleted, and counter-results go in a Limits section on the page they limit. Ninety-five pages carry `date_verified` (80 on 2026-08-20, 15 on 2026-08-22), and the 2026-08-20 quote audit corrected 30 passages, 16 of them prose copied from the `.sink` survey artifact. Ingest dates run from 2026-04-12 to 2026-08-22, the last log entry is that day's ingest of the Random Oracle paper, and the only lint entry is dated 2026-04-23. Git history shows later wiki edits that the log does not record (167 files on 2026-09-03), and `wiki/index.md` and `wiki/overview.md` stopped being maintained in 2026-04, so the folder listing is the real catalogue.

## 2. Topics

Each source line gives the page, the first author or authors and the year from the page's front matter, then what the page records. Every source and concept page appears at least once. Pages that fit two topics are listed in full once and named again where relevant.

### 2.1 Statistical-computational gaps, planted problems and average-case reductions

* `wiki/sources/reducibility-statistical-computational-gaps.md`. Brennan and Bresler, 2020. Secret-leakage planted clique as a reduction source for conditional lower bounds on robust sparse mean estimation, sparse PCA, SBM and others. Only pages 1 to 20 were read at first ingest.
* `wiki/sources/detection-recovery-refutation-gaps.md`. Bresler and Jiang, 2023. Detection-recovery and detection-refutation gaps for planted dense subgraph, conditional on secret-leakage planted clique.
* `wiki/sources/hirahara-planted-clique-conjectures-equivalent.md`. Hirahara and Shimizu, 2024. Unconditional reductions making the search and decision variants of the planted clique conjecture equivalent. Refutation sits in a separate equivalence.
* `wiki/sources/feldman-statistical-algorithms-planted-clique.md`. Feldman et al., 2017. Unconditional SQ lower bound for planted clique through statistical dimension, Theorem 2.9.
* `wiki/sources/barak-sos-lower-bound-planted-clique.md`. Barak et al., 2016. Unconditional degree-d SoS integrality gap for planted clique near the square-root threshold, Theorem 1.1.
* `wiki/sources/bandeira-franz-parisi-criterion.md`. Bandeira et al., 2022. Franz-Parisi hardness equals low-degree hardness for Gaussian additive models, with counterexamples outside that class.
* `wiki/sources/gamarnik-hardness-random-optimization-circuits.md`. Gamarnik, Jagannath and Wein, 2020. The overlap gap property defeats low-degree polynomials, shallow circuits and bounded-time Langevin dynamics on p-spin and sparse independent set.
* `wiki/sources/gamarnik-circuit-lower-bounds-pspin.md`. Gamarnik, Jagannath and Wein, 2022. Depth lower bound for polynomial-size circuits that approximate the p-spin optimum.
* `wiki/sources/ding-low-degree-community-detection.md`. Ding et al., 2025. An extended low-degree conjecture implies no efficient weak recovery below Kesten-Stigum in the SBM. The conjecture was revised once after a refutation.
* `wiki/sources/zadik-lattice-surpass-sos.md`. Zadik et al., 2022. LLL solves a noiseless clustering problem at n = d+1 where SoS and low-degree bounds both hold. Inverse-polynomial noise breaks the method.
* `wiki/sources/robust-estimators-high-dimensions.md`. Diakonikolas et al., 2016. First efficient dimension-independent robust estimators for four distribution families. The sparse case keeps a gap.
* `wiki/concepts/statistical-computational-gaps.md`. The gap between the information-theoretic and the polynomial-time sample thresholds.
* `wiki/concepts/planted-clique.md`. The planted clique problem and its conjecture at k = o(√n).
* `wiki/concepts/secret-leakage-planted-clique.md`. PC_ρ, planted clique with the clique drawn from a structured prior ρ.
* `wiki/concepts/average-case-reductions.md`. Polynomial-time maps between planted distributions in total variation.
* `wiki/concepts/sum-of-squares-hierarchy.md`. Degree-d SoS relaxations and pseudo-distributions.
* `wiki/concepts/pseudo-calibration.md`. The construction of SoS pseudo-expectations for planted problems.
* `wiki/concepts/franz-parisi-criterion.md`. A physics-derived hardness criterion built on the low-overlap likelihood norm.
* `wiki/concepts/overlap-gap-property.md`. The overlap structure of near-optimal solutions that blocks stable algorithms.
* `wiki/concepts/circuit-complexity-random-optimization.md`. The stability and total-influence route to circuit lower bounds.
* `wiki/concepts/kesten-stigum-threshold.md`. The SBM threshold at which efficient weak recovery begins.
* `wiki/concepts/stochastic-block-model.md`. The symmetric k-community random graph model.
* `wiki/concepts/lll-algorithm.md`. Lattice basis reduction, the method that beats SoS in noiseless settings.

Also relevant are `planted-orthogonal-vectors` (2.15) and the low-degree pages in 2.2.

### 2.2 SQ and low-degree models, and what a low-degree adversary buys

* `wiki/sources/brennan-sq-lowdegree-equivalence.md`. Brennan et al., 2021. SQ statistical dimension and minimum low-degree distinguisher degree are nearly equivalent under a nicenness condition, which fails for one-shot planted clique.
* `wiki/sources/low-degree-polynomials-survey.md`. Wein, 2025. Survey of the low-degree framework, its links to SQ and SoS, and its counterexamples. It records that the low-degree conjecture of Hopkins was refuted.
* `wiki/sources/low-degree-estimation-schramm-wein.md`. Schramm and Wein, 2022. Low-degree lower bounds on mean squared error for signal-plus-noise estimation.
* `wiki/sources/low-degree-almost-orthonormal.md`. Carpentier et al., 2025. A proof technique for low-degree bounds when the planted law destroys orthogonality of the natural basis.
* `wiki/sources/lb-latent-models-clustering.md`. Even, Giraud and Verzelen, 2025. Tight low-degree lower bounds for clustering, sparse clustering and biclustering.
* `wiki/sources/holmgren-counterexamples-low-degree.md`. Holmgren and Wein, 2021. Two code-based testing problems where degree-O(log n) polynomials fail and polynomial time succeeds.
* `wiki/sources/quasi-poly-low-degree-conjecture-false.md`. Buhai et al., 2025. Refutes the quasi-polynomial low-degree conjecture. The polynomial-time distinguisher is for a rectangular variant.
* `wiki/sources/rigorous-implications-low-degree.md`. Hsieh et al., 2026. What a vanishing low-degree likelihood ratio implies for noisy versions of the problem, across three test classes. It rules out no polynomial-time algorithm.
* `wiki/sources/certificates-statistical-algorithms.md`. Ngo and Kim, 2026. Publicly verifiable certificates for SQ algorithms. Soundness is against an unrestricted prover, so it is a query-bounded verifier result.
* `wiki/sources/learnability-deep-random-networks.md`. Das et al., 2020. An exp(O(h)) SQ lower bound for learning depth-h random networks, the source of the SQ bound in Jagielski et al.
* `wiki/concepts/statistical-query-model.md`. The Kearns SQ oracle and its tolerance.
* `wiki/concepts/csq-model.md`. Correlational queries, strictly weaker than SQ.
* `wiki/concepts/low-degree-polynomial-framework.md`. The low-degree likelihood ratio as evidence of hardness, and its known failures.

Also relevant are `bogdanov-low-degree-planted-subgraph` (2.3), `capacity-bounded-dp` and `what-can-we-learn-privately` (2.14).

### 2.3 Cryptography from planted and learning problems

* `wiki/sources/pke-from-planted-clique.md`. Ghosal et al., 2025. Public-key encryption against polynomial-size adversaries from quasi-polynomial hardness of standard planted clique plus a noisy k-LIN conjecture.
* `wiki/sources/pkc-from-different-assumptions.md`. Barak and Wigderson, 2008. Public-key encryption from an expander-based local PRG and a planted subgraph assumption, breakable in n^{O(log n)} time.
* `wiki/sources/cryptography-from-planted-graphs.md`. Abram et al., 2023. PSM and secret sharing with logarithmic share size from planted clique variants, secure against size-bounded adversaries.
* `wiki/sources/bogdanov-low-degree-planted-subgraph.md`. Bogdanov et al., 2024. An unconditional low-degree bound for the planted random subgraph problem, with cryptographic applications stated against size-bounded circuits.
* `wiki/sources/bruna-continuous-lwe.md`. Bruna et al., 2021. Continuous LWE is hard under a quantum reduction from worst-case lattice problems, and homogeneous CLWE is SQ-hard.
* `wiki/sources/hardness-single-periodic-neurons.md`. Song, Zadik and Bruna, 2021. Weakly learning one periodic neuron under small noise is hard if approximate SVP is quantum-hard.
* `wiki/sources/hardness-one-hidden-layer.md`. Li, Zadik and Zampetakis, 2025. The same conclusion for one-hidden-layer ReLU networks of width above √(d log d) with Gaussian noise.
* `wiki/sources/song-cryptographic-hardness-score-estimation.md`. Song, 2024. Gaussian pancakes reduce to L²-accurate score estimation. Section 1.3 records a black-box obstruction and an open direction.
* `wiki/sources/learning-in-pessiland.md`. Hirahara and Nanashima, 2023. If no infinitely-often one-way function exists, universal extrapolation learns many average-case tasks efficiently.
* `wiki/sources/covert-learning.md`. Canetti and Karchmer, 2021. Learning whose query transcript an efficient observer cannot tell from a reference, built on LPN.
* `wiki/sources/random-oracle-methodology-revisited.md`. Canetti, Goldreich and Halevi, 2004. Schemes secure in the random oracle model and insecure under every instantiation.
* `wiki/sources/are-gans-overkill-for-nlp.md`. Alvarez-Melis, Garg and Kalai, 2022. Reductions between distinguishing and likelihood improvement for learned distributions, exponential in general and polynomial in one direction only.
* `wiki/concepts/continuous-lwe.md`. The CLWE problem and its parameters.
* `wiki/concepts/learning-with-errors.md`. Regev's LWE.
* `wiki/concepts/one-way-functions.md`. The standard definition.
* `wiki/concepts/pseudorandomness.md`. PRGs and PRFs.
* `wiki/concepts/computational-indistinguishability.md`. The standard definition against PPT distinguishers.
* `wiki/concepts/covert-learning.md`. The (ε, δ)-covert learner definition.

### 2.4 Learning-theory exponents and algorithm-relative sample complexity

* `wiki/sources/information-exponent-online-sgd.md`. Ben Arous, Gheissari and Jagannath, 2021. The information exponent governs online SGD from a random start, for that one algorithm.
* `wiki/sources/generative-exponent-single-index.md`. Damian et al., 2024. The generative exponent sets SQ and low-degree thresholds for direction recovery in Gaussian single-index models. Remark 3.3 says the bound measures detection.
* `wiki/sources/generative-leap-multi-index.md`. Damian, Lee and Bruna, 2025. The generative leap exponent gives a low-degree lower bound and a matching efficient algorithm for index-space recovery in multi-index models.
* `wiki/sources/leap-complexity-sgd.md`. Abbe et al., 2023. Leap complexity is conjectured to govern SGD time. The proved lower bounds are CSQ only.
* `wiki/sources/merged-staircase-property.md`. Abbe et al., 2022. The merged-staircase property is necessary and nearly sufficient for O(d)-sample mean-field SGD on sparse hypercube functions.
* `wiki/sources/reusing-batches-breaks-exponents.md`. Dandi et al., 2024. Two gradient steps on a reused batch learn past the information and leap exponent barriers at n = αd.
* `wiki/sources/repetita-iuvant-data-repetition.md`. Arnaboldi et al., 2024. Using each sample twice in an extragradient step lets SGD learn multi-index targets at a polynomial generative exponent.
* `wiki/sources/full-batch-gd-vs-one-pass-sgd.md`. Kovačević et al., 2026. Full-batch GD beats one-pass SGD on truncated quadratic single-index learning at n ≃ d.
* `wiki/sources/sgd-reuse-info-theoretic-limit.md`. Lee et al., 2024. A layer-wise SGD variant learns polynomial single-index targets in d polylog d samples, and in a generative-exponent rate in general.
* `wiki/sources/sgd-xor-near-optimal.md`. Glasgow, 2024. Standard minibatch SGD learns 2-sparse XOR in about d samples.
* `wiki/sources/learning-rate-induces-generative-exponent.md`. Tsiolis et al., 2025. The learning rate selects an information-exponent or a generative-exponent regime inside a one-pass framework.
* `wiki/sources/single-index-harmonic-decomposition.md`. Joshi et al., 2025. A spherical-harmonic theory of single-index learning with SQ and low-degree lower bounds and matching estimators.
* `wiki/sources/noise-sensitivity-exponent.md`. Defilippis et al., 2026. A noise sensitivity exponent sizes AMP gaps in the proportional regime and the paper calls the older exponents brittle.
* `wiki/sources/robust-multi-index-sq-bounds.md`. Diakonikolas et al., 2025. An agnostic learner and a near-matching SQ lower bound for well-behaved real-valued multi-index models.
* `wiki/sources/robust-single-index-efficient.md`. Wang et al., 2024. An efficient constant-factor agnostic learner for Gaussian single-index models. The label-noise adversary carries no price.
* `wiki/sources/hidden-progress-sgd-parities.md`. Barak et al., 2022. SGD solves sparse parity in about n^{O(k)} iterations on the tested grid, near the SQ limit.
* `wiki/sources/transformers-sparse-xor-polylog.md`. Han and Ghoshdastidar, 2025. A one-layer two-head transformer with polylog(d) trainable parameters learns 2-sparse XOR in one step.
* `wiki/concepts/information-exponent.md`. Order of the first non-vanishing derivative of the population loss at zero correlation.
* `wiki/concepts/generative-exponent.md`. First non-zero term of the χ² mutual information expansion.
* `wiki/concepts/generative-leap-exponent.md`. The multi-index extension through augmented labels.
* `wiki/concepts/leap-complexity.md`. The leap of a target's Fourier or Hermite support.
* `wiki/concepts/single-index-model.md`. Two inequivalent versions used in the wiki.
* `wiki/concepts/multi-index-model.md`. Functional and distributional definitions.
* `wiki/concepts/noise-sensitivity-exponent.md`. The Defilippis et al. definition.

### 2.5 Neural scaling laws and the cost of the honest trainer

* `wiki/sources/scaling-laws-neural-lm.md`. Kaplan et al., 2020. Power-law fits of loss in parameters, data and compute, with no theory behind them.
* `wiki/sources/chinchilla-compute-optimal.md`. Hoffmann et al., 2022. Equal scaling of parameters and tokens at fixed compute. The Approach 3 constants are disputed in its Limits section.
* `wiki/sources/chinchilla-replication.md`. Besiroglu et al., 2024. A refit of Chinchilla Approach 3 on reconstructed data. The printed fit fails and equal scaling survives.
* `wiki/sources/explaining-neural-scaling-laws.md`. Bahri et al., 2024. Four scaling regimes. The variance-limited exponent is proved, the resolution-limited one is an upper bound.
* `wiki/sources/compute-optimal-phases.md`. Paquette et al., 2024. A compute-optimal frontier proved inside power-law random features trained by one-pass SGD.
* `wiki/sources/dynamical-model-scaling-laws.md`. Bordelon, Atanasov and Pehlevan, 2024. A DMFT model in which the time and model exponents differ.
* `wiki/sources/feature-learning-improves-scaling.md`. Bordelon, Atanasov and Pehlevan, 2025. Feature learning nearly doubles the hard-task time exponent.
* `wiki/sources/distillation-scaling-laws.md`. Busbridge et al., 2025. An empirical distillation law with explicit compute-accounting scenarios.
* `wiki/sources/data-pruning-beats-power-laws.md`. Sorscher et al., 2022. Pruning beats power-law scaling in a perceptron model, and only with a perfect metric.
* `wiki/sources/algorithmic-progress-lm.md`. Ho et al., 2024. Compute to a fixed perplexity halved about every 8 months from 2012 to 2023.
* `wiki/sources/catch-a-chinchilla-compute-monitoring.md`. Shavit, 2023. Governance by compute monitoring, with one Poisson-snapshot theorem and no exhibited hard proof scheme.
* `wiki/sources/fine-grained-erm.md`. Backurs, Indyk and Schmidt, 2017. SETH-conditional lower bounds on high-accuracy ERM and gradient computation for the honest learner.
* `wiki/sources/fine-grained-gradient-llm.md`. Alman and Song, 2024. SETH rules out subquadratic attention-gradient computation on a stated input family. No adversary appears.
* `wiki/concepts/compute-monitoring.md`. Rule enforcement by observing training compute.
* `wiki/concepts/fine-grained-complexity-of-learning.md`. Conditional lower bounds on the exponent of learning computations.

### 2.6 Concentration of measure, geometry and robustness limits

* `wiki/sources/complexity-theoretic-adversarial-ml.md`. Mahloujifar, 2019. A research statement summarising concentration-based evasion, p-tampering poisoning and computational robustness.
* `wiki/sources/curse-of-concentration.md`. Mahloujifar, Diochnos and Mahmoody, 2019. In concentrated spaces any classifier with constant error falls to O(√n) perturbations. Its Limits section records that the hypothesis does not bind on image benchmarks.
* `wiki/sources/empirically-measuring-concentration.md`. Mahloujifar et al., 2019. A convergent estimator of the concentration function. On image benchmarks the implied floor sits well below observed attack success.
* `wiki/sources/computational-concentration-of-measure-etesami.md`. Etesami, Mahloujifar and Mahmoody, 2020. MUCIO finds close points in polynomial time on product spaces at the Talagrand distance.
* `wiki/sources/lower-bounds-robust-pac-learning.md`. Diochnos, Mahloujifar and Mahmoody, 2020. Under a Normal Lévy space and an α-close class, error-region robustness forces 2^{Ω(n)} samples.
* `wiki/sources/adversarial-spheres.md`. Gilmer et al., 2018. On two concentric spheres any model with constant error has errors within O(1/√n).
* `wiki/sources/adversarial-vulnerability-any-classifier.md`. Fawzi, Fawzi and Fawzi, 2018. Every classifier is vulnerable when the data come from a smooth Gaussian generator.
* `wiki/sources/data-concentration-robustness-avoidable.md`. Pal, Sulam and Vidal, 2023. Robust classifiers exist when class conditionals concentrate in the opposite, small-volume sense.
* `wiki/sources/universal-law-of-robustness.md`. Bubeck and Sellke, 2021. Smooth interpolation below the noise level under isoperimetry needs about nd parameters. The theorem contains no adversary.
* `wiki/sources/robustness-at-odds-accuracy.md`. Tsipras et al., 2019. One constructed distribution on which standard and robust optimality conflict.
* `wiki/sources/robust-generalization-more-data.md`. Schmidt et al., 2018. Constructed models where robust generalization needs more samples than standard generalization.
* `wiki/concepts/concentration-of-measure.md`. The metric-measure phenomenon.
* `wiki/concepts/levy-family.md`. Lévy and Normal Lévy families.
* `wiki/concepts/intrinsic-robustness.md`. The best adversarial accuracy any classifier can reach on a distribution.
* `wiki/concepts/computational-concentration-of-measure.md`. Concentration witnessed by an efficient algorithm.
* `wiki/concepts/isoperimetry-and-robustness.md`. Isoperimetric inequalities as the source of vulnerability bounds.
* `wiki/concepts/two-senses-of-concentration.md`. The two opposite meanings of concentration in this literature.
* `wiki/concepts/universal-law-of-robustness.md`. The Bubeck and Sellke statement.
* `wiki/concepts/evasion-attacks.md`. Inference-time perturbation attacks.

### 2.7 Computational hardness in robust learning, and robust PAC theory

* `wiki/sources/adversarial-examples-computational-constraints.md`. Bubeck, Price and Razenshteyn, 2019. An unconditional SQ separation between non-robust and robust learning. The page corrects an earlier claim that it uses cryptography.
* `wiki/sources/adversarial-examples-prg.md`. Bubeck et al., 2018. Robust learning is hard under quadratic residuosity through the Blum-Blum-Shub PRG.
* `wiki/sources/win-win-robust-learning.md`. Degwekar, Nakkiran and Vaikuntanathan, 2019. If an efficient robust classifier exists but cannot be learned efficiently, one-way functions exist.
* `wiki/sources/computational-hardness-robust-learning.md`. Garg et al., 2020. Constructed tasks on which computational robustness exceeds information-theoretic robustness, from one-way functions.
* `wiki/sources/overparameterization-computational-constraints.md`. Garg et al., 2022. Constructed tasks on which bounded learners need more parameters than information requires.
* `wiki/sources/robust-pac-learning-characterization.md`. Montasser, Hanneke and Srebro, 2022. The global one-inclusion dimension characterizes agnostic robust learnability up to log factors.
* `wiki/sources/vc-classes-adversarially-robustly-learnable.md`. Montasser, Hanneke and Srebro, 2019. VC classes are robustly learnable only improperly, sometimes exponentially in the VC dimension.
* `wiki/sources/pac-learning-evasion-adversaries.md`. Cullina, Bhagoji and Mittal, 2018. Adversarial VC dimension and a sample bound for evasion-robust PAC learning.
* `wiki/sources/adversarially-robust-pac-regression.md`. Attias and Hanneke, 2023. Finite fat-shattering dimension suffices for robust regression.
* `wiki/sources/tolerant-robust-pac-learning.md`. Ashtiani, Pathak and Urner, 2025. A tolerance relaxation gives sample complexity linear in the VC dimension.
* `wiki/sources/robustly-reliable-learners-poison.md`. Balcan et al., 2022. Learners that certify each prediction under a poisoning budget.
* `wiki/concepts/computational-vs-it-robustness.md`. Robustness against PPT versus unbounded adversaries.
* `wiki/concepts/win-win-theorem.md`. The Degwekar, Nakkiran and Vaikuntanathan implication.
* `wiki/concepts/model-size-as-priced-resource.md`. Description length of the output model as a priced resource.
* `wiki/concepts/robust-pac-learning.md`. Robust risk and robust PAC learnability.
* `wiki/concepts/adversarial-vc-dimension.md`. The corrupted-class VC dimension, superseded as the characterizing dimension.
* `wiki/concepts/reliable-learning.md`. Robustly-reliable learners.
* `wiki/concepts/pac-learning.md`. Valiant's model.

### 2.8 Certified defenses and randomized smoothing

* `wiki/sources/certified-robustness-randomized-smoothing.md`. Cohen, Rosenfeld and Kolter, 2019. Gaussian smoothing certifies an ℓ₂ radius for any base classifier.
* `wiki/sources/provably-robust-smoothadv.md`. Salman et al., 2019. Adversarial training of smoothed classifiers raises measured certified accuracy.
* `wiki/sources/provable-defenses-convex-polytope.md`. Wong and Kolter, 2018. An LP outer relaxation gives robust training and a detection guarantee for ReLU networks.
* `wiki/sources/certified-robustness-differential-privacy.md`. Lecuyer et al., 2019. PixelDP, certified robustness from a DP noise layer.
* `wiki/sources/certified-defenses-data-poisoning.md`. Steinhardt, Koh and Liang, 2017. Per-dataset certified bounds on poisoning loss for sanitize-then-ERM defenders.
* `wiki/sources/adds-adaptive-diffusion-smoothing.md`. Shpilevskiy et al., 2025. Diffusion denoising steps as adaptive GDP mechanisms composed into a certificate. The venue is corrected to a workshop submission.
* `wiki/sources/rs-meets-vlm.md`. Seferis et al., 2025. Smoothing for vision-language models through an oracle classification task.
* `wiki/sources/naat-certified-semantic-smoothing.md`. Cheng et al., 2026. A hypergeometric certified radius for LLM jailbreaks under token ablation.
* `wiki/sources/lefcert-foundation-models.md`. Lai et al., 2025. Certified few-shot classification for CLIP-type models under support-set poisoning.
* `wiki/sources/multi-level-certified-offline-rl.md`. Liu et al., 2025. DP-based certificates against poisoning in offline RL.
* `wiki/sources/rs-llm-multi-agent.md`. Hu et al., 2026. Smoothing of consensus decisions in LLM multi-agent systems. No system-level bound is proved.

### 2.9 Poisoning and tampering models

* `wiki/sources/multi-party-poisoning.md`. Mahloujifar, Mahmoody and Mohammed, 2019. A (k, p)-poisoning attack raises any bad-property probability from µ to µ^{1−pk/m}.
* `wiki/concepts/poisoning-attacks.md`. Training-time corruption models.
* `wiki/concepts/p-tampering-model.md`. Online tampering of each element with probability p.
* `wiki/concepts/k-p-poisoning-model.md`. k corrupted parties with p-close messages.

Also relevant are `certified-defenses-data-poisoning` (2.8), `robust-estimators-high-dimensions` (2.1), `robustly-reliable-learners-poison` (2.7), `universal-jailbreak-rlhf-backdoors` (2.10).

### 2.10 Backdoors, watermarks and cryptographic undetectability

* `wiki/sources/planting-undetectable-backdoors.md`. Goldwasser et al., 2022. Black-box undetectable backdoors for any training procedure from signatures, and white-box ones for random Fourier features from CLWE.
* `wiki/sources/io-undetectable-backdoors-nn.md`. Kalavasis et al., 2024. Undetectable backdoors in networks shipped through iO, and in language models with steganography.
* `wiki/sources/unelicitable-backdoors-lms.md`. Draguns et al., 2024. Hash-based digital-locker backdoors in transformers, argued and not proved.
* `wiki/sources/oblivious-defense-backdoor-removal.md`. Goldwasser et al., 2025. Backdoors can be removed without detection when the ground truth is Fourier-heavy or low-degree.
* `wiki/sources/backdoor-defense-learnability-obfuscation.md`. Christiano et al., 2025. Defendability is set by VC dimension statistically and sits between learnability and iO computationally.
* `wiki/sources/crypto-backdoor-boon-bane.md`. Ngo, Chattopadhyay and Maitra, 2025. Signature backdoors reused for watermarking and authentication, with defensive claims argued and not proved.
* `wiki/sources/undetectable-watermarks-lm.md`. Christ, Gunn and Zamir, 2024. Language-model watermarks undetectable without the key, from PRFs.
* `wiki/sources/universal-jailbreak-rlhf-backdoors.md`. Rando and Tramèr, 2024. Poisoned RLHF annotations plant a universal jailbreak trigger. Measured only.
* `wiki/concepts/undetectable-backdoors.md`. The (Backdoor, Activate) definition.
* `wiki/concepts/defendability.md`. The Christiano et al. game.
* `wiki/concepts/indistinguishability-obfuscation.md`. The iO primitive.

### 2.11 Evaluation critiques in adversarial ML

* `wiki/sources/on-evaluating-adversarial-robustness.md`. Carlini et al., 2019. A defence-evaluation checklist that declines to treat attacker compute as a threat-model parameter.
* `wiki/sources/obfuscated-gradients.md`. Athalye, Carlini and Wagner, 2018. Seven of nine ICLR 2018 defences masked gradients and were broken.
* `wiki/sources/adaptive-attacks-defenses.md`. Tramèr et al., 2020. Thirteen adaptively evaluated defences were still circumvented.
* `wiki/sources/adaptive-test-time-defenses-eval.md`. Croce et al., 2022. Nine test-time defences do not beat static ones.
* `wiki/sources/robustbench.md`. Croce et al., 2021. A fixed AutoAttack benchmark with admission restrictions.
* `wiki/sources/sok-adversary-knowledge.md`. Fenaux and Kerschbaum, 2024. An oracle-based partial order of adversary knowledge.
* `wiki/sources/sok-black-box-attack-pitfalls.md`. Suya et al., 2024. A four-axis black-box threat model, with runtime as the equalizer between attacks.
* `wiki/sources/dos-and-donts-ml-security.md`. Arp et al., 2022. Ten pitfalls measured over 30 security papers.
* `wiki/sources/sok-security-privacy-machine-learning.md`. Papernot et al., 2018. The prior systematization, with no computational axis.
* `wiki/sources/sok-backdoor-defense-evaluation.md`. Abad et al., 2025. A coded meta-analysis of 183 backdoor-defence papers.
* `wiki/sources/critical-evaluation-backdoor-countermeasures.md`. Qiu et al., 2024. Three backdoor defences fail inside their own threat models.
* `wiki/sources/evaluating-nn-backdoor-defenses.md`. Veldanda and Garg, 2020. An early note on backdoor-evaluation pitfalls.
* `wiki/concepts/adaptive-attacks.md`. Attacks built after the defence is fixed.
* `wiki/concepts/obfuscated-gradients.md`. Gradient masking.
* `wiki/concepts/adversary-knowledge-taxonomy.md`. Two incompatible 2024 structures for attacker knowledge.
* `wiki/concepts/backdoor-defense-evaluation.md`. The unformalized protocol for evaluating backdoor defences.

### 2.12 Membership inference, auditing and attacker sample complexity

* `wiki/sources/membership-inference-shokri.md`. Shokri et al., 2017. Shadow-model membership inference. The paper has no definition or theorem.
* `wiki/sources/privacy-risk-overfitting.md`. Yeom et al., 2018. The membership game (Experiment 1, Definition 4) and its links to overfitting and DP.
* `wiki/sources/mia-from-first-principles.md`. Carlini et al., 2022. LiRA and the low-FPR evaluation regime, with the game taken from Yeom.
* `wiki/sources/difficulty-of-mia.md`. Rezaei and Liu, 2021. Membership inference results omitted false alarm rates.
* `wiki/sources/blind-baselines-beat-mia.md`. Das, Zhang and Tramèr, 2025. Model-free attacks beat published attacks on eight post-hoc datasets.
* `wiki/sources/sok-mia-llms-rushing-nowhere.md`. Meeus et al., 2025. Post-hoc LLM membership datasets carry distribution shift.
* `wiki/sources/do-mias-work-on-llms.md`. Duan et al., 2024. Membership inference is near random on one-epoch pretrained LLMs.
* `wiki/sources/privacy-defense-evaluations-misleading.md`. Aerni, Zhang and Tramèr, 2024. Empirical privacy defences were evaluated against weak baselines.
* `wiki/sources/mia-cannot-prove-training.md`. Zhang et al., 2025. Membership inference cannot prove training on given data, because the null cannot be sampled.
* `wiki/sources/haghifam-sample-complexity-mia.md`. Haghifam, Smith and Ullman, 2025. A membership attacker against Gaussian mean estimation needs quadratically more samples than the trainer, unless it knows the covariance.
* `wiki/sources/distribution-inference-risks.md`. Suri and Evans, 2022. A distribution inference game derived from Yeom's.
* `wiki/sources/language-model-preserve-privacy.md`. Brown et al., 2022. The record is the wrong unit of protection for language data.
* `wiki/concepts/membership-inference-game.md`. The two-party membership game.
* `wiki/concepts/low-fpr-evaluation-regime.md`. Scoring attacks by TPR at low FPR.
* `wiki/concepts/blind-baseline.md`. Attacks that never query the model.
* `wiki/concepts/unit-of-protection.md`. The object a privacy guarantee quantifies over.

### 2.13 Reconstruction, memorization and the fiber of the training map

* `wiki/sources/dinur-nissim-revealing-information.md`. Dinur and Nissim, 2003. Polynomial-time reconstruction from noisy subset sums, with separate exponential-adversary and polynomial-adversary thresholds.
* `wiki/sources/cohen-data-reconstruction.md`. Cohen et al., 2025. Narcissus resiliency, and a computational version equivalent to one-wayness for well-spread functions.
* `wiki/sources/kaplan-bayesian-memorization-reconstruction.md`. Kaplan et al., 2026. Computational and statistical memorization separated under a Tardos prior.
* `wiki/sources/reconstructing-informed-adversaries.md`. Balle, Cherubin and Hayes, 2022. Reconstruction robustness, a tolerance-parameterized success criterion bounded through DP.
* `wiki/sources/query-complexity-reconstruction.md`. Mukherjee and Lokam, 2024. Query lower bounds for reconstruction from DP learners, in plain query count.
* `wiki/sources/sok-data-reconstruction-attacks.md`. Wen et al., 2025. The field has no consensus definition of reconstruction. A vision benchmark.
* `wiki/sources/lamp-gradient-inversion.md`. Balunović et al., 2022. Text recovered from gradients with language-model priors. Empirical.
* `wiki/sources/suliman-data-forging-attacks.md`. Suliman et al., 2025. Published forging attacks miss reproduction thresholds. The paper conjectures that constrained forging is infeasible.
* `wiki/sources/xiao-formal-privacy-proof-data-encoding.md`. Xiao, Suh and Devadas, 2024. An injective learnable obfuscation cannot be IND-CPA secure (Theorem 1).
* `wiki/concepts/data-reconstruction-attack.md`. The Wen et al. definition.
* `wiki/concepts/computational-vs-statistical-memorization.md`. Information present versus information extractable.
* `wiki/concepts/fiber-of-the-training-map.md`. The set of datasets that train to a given model, and its navigability.

### 2.14 Differential privacy variants and the computational axis

* `wiki/sources/deep-learning-differential-privacy.md`. Abadi et al., 2016. DP-SGD and the moments accountant.
* `wiki/sources/computational-differential-privacy.md`. Mironov et al., 2009. IND-CDP and SIM-CDP. SIM implies IND, and the converse is left open.
* `wiki/sources/cdp-wider-parameter-regimes.md`. Meisingseth and Rechberger, 2026. The CDP equivalences restated in wider (ε, δ) regimes.
* `wiki/sources/limits-cdp-client-server.md`. Groce, Katz and Yerukhimovich, 2011. Two conditional limits on CDP in the client-server setting, with stated exclusions.
* `wiki/sources/separating-cdp-client-server.md`. Bun, Chen and Vadhan, 2016. The first single-curator separation, an infeasibility result.
* `wiki/sources/towards-separating-cdp.md`. Ghazi et al., 2023. A separation against unbounded statistical mechanisms under three cryptographic assumptions.
* `wiki/sources/cdp-inner-product-implies-ot.md`. Haitner et al., 2025. An accurate two-party CDP inner product implies oblivious transfer.
* `wiki/sources/two-party-dp-complexity.md`. Haitner et al., 2022. Such a protocol implies key agreement.
* `wiki/sources/sok-differential-privacies.md`. Desfontaines and Pejó, 2020. About 200 DP variants in seven dimensions, with computational power as dimension C.
* `wiki/sources/capacity-bounded-dp.md`. Chaudhuri, Imola and Machanavajjhala, 2019. An adversary bounded by the function class of its attack.
* `wiki/sources/kernel-quantum-renyi-audit.md`. Domingo-Enrich and Mroueh, 2022. A restricted divergence chosen for estimable DP auditing.
* `wiki/sources/attaxonomy.md`. Cummings et al., 2024. A knowledge-based attack taxonomy for choosing ε, with no computational dimension.
* `wiki/sources/adversary-aware-dp-bounds.md`. Swanberg et al., 2026. Unified DP attack bounds over prior and success criterion, with no computational axis.
* `wiki/sources/dp-against-timing-attacks.md`. Ratliff and Vadhan, 2024. Runtime of the mechanism as a leakage channel.
* `wiki/sources/what-can-we-learn-privately.md`. Kasiviswanathan et al., 2008. Local DP learnability equals SQ learnability.
* `wiki/sources/preventing-false-discovery-hard.md`. Hardt and Ullman, 2014. No efficient oracle answers n^{3+o(1)} adaptive queries, assuming one-way functions.
* `wiki/concepts/computational-differential-privacy.md`. IND-CDP and SIM-CDP.
* `wiki/concepts/capacity-bounded-privacy.md`. Restricted f-divergence privacy.
* `wiki/concepts/local-differential-privacy.md`. Per-record randomizers.
* `wiki/concepts/adaptive-data-analysis.md`. Valid answers to adaptively chosen statistical queries.

Also relevant is `dp-adaptive-analysis-bounded-space` (2.16).

### 2.15 Fine-grained cryptography and the security gap exponent

* `wiki/sources/fine-grained-cryptography.md`. Degwekar, Vaikuntanathan and Vasudevan, 2016. Primitives secure against the classes AC0 and NC1. The NC1 side holds only infinitely often.
* `wiki/sources/fine-grained-one-way-functions.md`. Brzuska and Couteau, 2022. Definition 6 prices the inverter at honest^{1+δ} circuit size. Mostly negative results.
* `wiki/sources/pkc-fine-grained-setting.md`. LaVigne, Lincoln and Vassilevska Williams, 2019. Fine-grained public-key encryption from Zero-k-Clique. Definition 5 names the gap.
* `wiki/sources/average-case-fine-grained-hardness.md`. Ball et al., 2017. Polynomial families whose average-case cost follows the OV, 3SUM and APSP conjectures.
* `wiki/sources/average-case-parity-problems.md`. Dalirrooyfard et al., 2025. Parity versions of k-OV and k-SUM are average-case hard, but only for near-perfect success.
* `wiki/sources/planted-orthogonal-vectors.md`. Kühnemann, Polak and Rosen, 2025. A planted k-OV distribution whose hardness is conjectured.
* `wiki/sources/fine-grained-world-without-crypto.md`. Alman, Huang and Yeo, 2025. Without one-way functions, average-case k-SUM is easy for large constant k, infinitely often.
* `wiki/sources/fine-grained-nike-lower-bounds.md`. Afshar et al., 2023. The random-oracle NIKE gap shrinks with the party count, and 3-NIKE is capped at quadratic in Maurer's generic group model.
* `wiki/sources/fine-grained-nike-revisited.md`. Bauer, Couteau and Sadeghi, 2024. A quadratic-gap 4-party NIKE in the standard model from strong assumptions.
* `wiki/sources/nike-without-idealized-assumptions.md`. Wang et al., 2024. NIKE in bounded parallel time, bounded time and bounded storage.
* `wiki/sources/merkle-puzzles-are-optimal.md`. Barak and Mahmoody, 2009. Every random-oracle key exchange falls to an O(n²)-query attack.
* `wiki/sources/permissionless-consensus-fine-grained.md`. Ball et al., 2024. Consensus against adversarial power T^{1−ε} from k-OV, in the random beacon model.
* `wiki/sources/sequential-functions-fine-grained.md`. Guan and Montgomery, 2024. Depth, not total work, as the priced resource.
* `wiki/concepts/fine-grained-cryptography.md`. Adversaries with a bounded polynomial advantage over honest parties.
* `wiki/concepts/security-gap-exponent.md`. Two inequivalent conventions for δ and the conversion between them.
* `wiki/concepts/orthogonal-vectors-conjecture.md`. OV and k-OV.
* `wiki/concepts/sequential-functions.md`. The Guan and Montgomery definition.

Also relevant are `fine-grained-erm` and `fine-grained-gradient-llm` (2.5).

### 2.16 Memory-bounded and bounded-storage adversaries

* `wiki/sources/raz-parity-time-space.md`. Raz, 2016. Parity learning needs quadratic memory or exponentially many samples. The bound sits on the learner.
* `wiki/sources/bounded-storage-simple-schemes.md`. Guan and Zhandry, 2019. Bounded-storage schemes built on Raz's bound, against unbounded-time adversaries with bounded memory.
* `wiki/sources/speak-much-remember-little.md`. Dodis, Quach and Wichs, 2023. Breaks the believed quadratic ceiling, up to an exponential memory gap.
* `wiki/sources/authentication-bounded-storage.md`. Dodis, Quach and Wichs, 2022. MACs and signatures in the bounded storage model.
* `wiki/sources/bsm-key-agreement-owf.md`. Brzuska et al., 2024. Bounded-storage key agreement at any polynomial gap from one-way functions, and one-way functions are necessary for large gaps.
* `wiki/sources/adaptive-vs-oblivious-streaming.md`. Kaplan et al., 2021. One streaming problem needs polynomial space adaptively and polylog space obliviously.
* `wiki/sources/dp-adaptive-analysis-bounded-space.md`. Dinur et al., 2023. Space separations for DP and adaptive data analysis, with the space bound on the mechanism.
* `wiki/concepts/bounded-storage-model.md`. Maurer's model with a computationally unbounded, storage-bounded adversary.

### 2.17 Model extraction, proof of learning and unlearning

* `wiki/sources/jagielski-model-extraction.md`. Jagielski et al., 2020. Accuracy versus fidelity extraction, NP-hardness for the evaluation map, and an imported SQ lower bound.
* `wiki/sources/active-learning-model-extraction.md`. Chandrasekaran et al., 2020. Query-synthesis active learners are extraction adversaries, stated as an observation.
* `wiki/sources/cryptanalytic-extraction-nn.md`. Carlini, Jagielski and Mironov, 2020. A differential attack recovers ReLU network parameters with a measured query count.
* `wiki/sources/polynomial-time-cryptanalytic-extraction.md`. Canales-Martínez et al., 2024. A polynomial-time version under infinite-precision arithmetic.
* `wiki/sources/calibrated-proof-of-work-extraction.md`. Dziedzic et al., 2022. Per-query proof-of-work raises the cost of extraction. Empirical.
* `wiki/sources/beyond-labeling-oracles.md`. Shafran et al., 2024. Extraction cost decomposed, and the observation that no formal success definition exists.
* `wiki/sources/proof-of-learning.md`. Jia et al., 2021. Proof-of-learning with three cost inequalities stated as desiderata.
* `wiki/sources/pol-more-broken.md`. Fang et al., 2023. Attacks on stated proof-of-learning verification parameters.
* `wiki/sources/pol-incentive-security.md`. Zhao et al., 2026. Proof-of-learning made incentive-secure for rational provers.
* `wiki/sources/polo-proof-of-learning-ownership.md`. Deng et al., 2026. Chained watermarks with forging measured at 1.1 to 4 times honest cost.
* `wiki/sources/auditable-unlearning-definitions.md`. Thudi et al., 2022. Forging shows unlearning is definable only at the level of the algorithm.
* `wiki/sources/forgeability-and-unlearning.md`. Kong, Roy Chowdhury and Chaudhuri, 2023. A proof of repudiation against membership claims, resting on a conjecture.
* `wiki/sources/unlearning-verification-fragile.md`. Zhang et al., 2024. A dishonest provider passes unlearning verification under minibatch SGD.
* `wiki/sources/impossibility-retrain-equivalence.md`. Yu et al., 2025. Retrain equivalence is ill-posed for local, path-oblivious unlearning of staged training.
* `wiki/concepts/model-extraction.md`. The exact, functional, fidelity and accuracy targets.
* `wiki/concepts/proof-of-learning.md`. The (R, V) protocol pair.
* `wiki/concepts/machine-unlearning.md`. Exact and approximate unlearning.
* `wiki/concepts/retrain-equivalence.md`. The standard unlearning desideratum.

### 2.18 Agentic and LLM security models, and alignment impossibility

* `wiki/sources/extending-formalism-cryptography-ai.md`. Villa et al., 2026. The AIOracle model with LEARN and INFER phases, security games, a composition theorem and the DPD confidentiality game.
* `wiki/sources/formalizing-llm-agent-security.md`. Siu et al., 2026. Four contextual properties with ideal oracle functions, checked for coverage against 87 papers.
* `wiki/sources/imtm-prompt-injections-protocols.md`. Ferrag et al., 2026. A survey threat model and the origin of IMTM, with no conditional result.
* `wiki/sources/camel-defeating-prompt-injections.md`. Debenedetti et al., 2025. A capability-based interpreter that keeps untrusted data out of control flow. No theorem.
* `wiki/sources/melon-indirect-prompt-injection.md`. Zhu et al., 2025. A masked re-execution detector with Hoeffding bounds under unverified assumptions.
* `wiki/sources/seven-challenges-cross-domain-mas.md`. Ko et al., 2025. A position paper on cross-domain multi-agent security.
* `wiki/sources/filter-impossibility-ai-alignment.md`. Ball et al., 2026. There exist LLMs with no efficient prompt filter, under time-lock puzzles, one-way functions with a shared secret, or PKE.
* `wiki/sources/jailbreak-paradox.md`. Rao, Choudhury and Aditya, 2024. Perfect jailbreak detection needs a more capable model, on an unargued existence premise.
* `wiki/sources/immune-rlhf-jailbreak-defense.md`. Ghosal et al., 2025. An inference-time decoding defence with a pointwise suboptimality bound.
* `wiki/sources/maxmin-rlhf-impossibility.md`. Chakraborty et al., 2024. One Bradley-Terry reward cannot align diverse subgroups.
* `wiki/concepts/aioracle-framework.md`. The Villa et al. abstraction.
* `wiki/concepts/attack-taxonomy-llms.md`. A five-dimension attack classification from Villa et al.
* `wiki/concepts/input-manipulation-threat-model.md`. IMTM, recorded unverified from an earlier ingest.
* `wiki/concepts/impossibility-frameworks.md`. Impossibility results for alignment.
* `wiki/concepts/rlhf-formal-model.md`. SFT, reward model and KL-regularized policy optimization.

### 2.19 Verification and formalization of learning

* `wiki/sources/zk-verifiable-ai-pipelines.md`. Balan, Learney and Wood, 2025. A six-stage verifiability framework and gap analysis. Several tool names were removed as absent from the paper.
* `wiki/sources/lean-rademacher-formalization.md`. Sonoda et al., 2026. A Lean 4 proof of Rademacher generalization bounds.
* `wiki/concepts/verifiable-computation.md`. Succinct proofs of correct computation.
* `wiki/concepts/zk-ml-verification.md`. Zero-knowledge proofs and commitments for ML claims.
* `wiki/concepts/lean-formalized-learning.md`. Mechanized learning theory.

### 2.20 Entities, raw files and stray files

The 116 entity pages are all authors. Their About sections give affiliation and the wiki pages they link to, and they hold no claims of their own.

`raw/` holds 206 PDFs and one HTML file, catalogued in `raw/SOURCES.md` by wave with a boundary note per paper. Six raw PDFs and the one HTML file have no source page:

* `raw/ABbook.pdf`, Arora and Barak, the complexity textbook.
* `raw/S25_PACLearningSurvey.pdf`, catalogued with an unverified title. Its first page, read during this mapping, gives Servedio's survey on the PAC model, arXiv 2511.08791.
* `raw/20344_Statistically_Undetectab.pdf`, a submission under review at ICLR 2026 that the wiki ties to the statistically undetectable backdoor line. Its authors are not given in the copy.
* `raw/K23_LimitsObservationalDefenses.pdf`, Karchmer, SaTML 2023, on the limits of provable security against model extraction.
* `raw/2502.07232v1.pdf`, a second copy of the Ashtiani, Pathak and Urner paper.
* `raw/PSM+24_ReconcilingScaling.pdf`, Porian et al., recorded inside the Chinchilla page's Limits section.
* `raw/AIOracles_for_Practitioners.html`, a companion writeup listed as a candidate ingest.

`wiki/sources/BACKUP_INDEX.pdf` is misnamed. Its first page is Naor and Rothblum, Learning to Impersonate, which no wiki page records.

## 3. Analyses

`wiki/analyses/deep-research-prompt-formalizing-ai-security.md`, 2026-04-12. The question was which open problems in a formal theory of AI security deserve attention, from three seed papers (Mahloujifar 2019, Brennan and Bresler 2020, Villa et al. 2026). The page says the prompt follows, but the prompt is missing and the file ends after its header sections. Its only conclusion is to file follow-up sources and to create concept pages as new models appear.

`wiki/analyses/reading-pathway-formal-security.md`, 2026-04-23. The question was the reading order through the 45-paper corpus of that date. It sorts the corpus into three pillars (robustness from concentration and complexity, statistical-computational gaps, formal AI security models) and gives phases 0 to III with entry points by background and time estimates. Several links point at the bare `../sources/` folder rather than a page. It predates every ingest from July onward, so it is stale as a map.

`wiki/analyses/web-research-2026-frontier.md`, 2026-04-23. The question was which 2024 to 2026 formal work extends the corpus. It concludes that undetectable backdoors extend to language models, that randomized smoothing extends to LLMs and VLMs, that Ghosal et al. settled PKE from standard planted clique, and that Ball et al. 2025 settled filter impossibility. Its recommended bet is a UC-style composition theorem for multi-agent LLM security games. Later page corrections narrow several of these readings, notably that the filter result is existential and that the iO backdoor paper does not close the white-box gap.

`wiki/analyses/summer-2026-research-programme.md`, dated 2026-06-22 and amended 2026-07-25. The question was a 14-week calendar that interleaves Arora and Barak with the corpus toward the Chapter 24 thesis of learning as an abstract machine with a capability vector κ. Its anchor game was COMP-MEM with a marginal advantage over a public baseline, and its crown jewel a threshold reduction from learning to breaking a one-way function. The amendment strikes three decisions. The marginal advantage is a no-op and the game is Yeom's. The PPT-first ordering inverts. The black-box-first climb inverts because of Song's black-box obstruction. The replacement W10 deliverable, the fiber of the training map, was itself refuted at its core a day later, according to `CLAUDE.md`.

`wiki/analyses/native-asymmetry-in-learning.md`, 2026-07-25, corrected 2026-08-22. The question was where a security gap can come from when defender and attacker are both efficient over the same data, and which theorem shapes are unclaimed. It finds that of four ML task pairs only training against inversion has the sign a security claim needs, and that learning's parties are asymmetric by access, never by construction. It names two native sources of asymmetry, knowledge of the data (privacy) and access to parts of the algorithm (backdoors), and predicts that only the first supports a statement without an imported trapdoor. It retracts the claim that no security definition quantifies over low-degree adversaries and lists occupied cells. The surviving cell is attacker and defender priced in the same exponent units at a matched budget, with the attacker restricted to the trainer's algorithm class, framed as the computational version of Haghifam, Smith and Ullman. Several of its pointers were later corrected in `CLAUDE.md` (Yeom Definition 4, Song section numbering, the Ngo and Kim retraction, the narrower Bogdanov et al. reading).

## 4. The frontier survey in `.sink`

`.sink/compass_artifact_wf-6dd26eed-7b63-4913-af9a-4d6edcae8017_text_markdown.md` is a theory-first survey of the 2024 to 2026 frontier in AI security and learning theory. It verifies seven known references (A1 to A7) and adds 21 papers (B1 to B21) in five pillars, namely agentic models, undetectable backdoors, alignment impossibility, statistical-computational gaps, and certified robustness. The 2026-04-23 mega-batch ingested it. The 2026-08-20 audit found that 16 quotations on 13 wiki pages were this file's own prose, so the wiki treats it as a secondary source and its claims as unverified. Every item has a wiki page except the two marked not yet ingested.

* A1, Draguns et al., unelicitable backdoors via cryptographic transformer circuits. Ingested as `unelicitable-backdoors-lms`. The wiki corrects the signature description to a hash-based digital locker.
* A2, Kalavasis et al., undetectable backdoors in obfuscated networks and language models. Ingested as `io-undetectable-backdoors-nn`. The wiki removes the claim that it closes the white-box gap.
* A3, Cheng et al., NAAT and certified semantic smoothing for LLM jailbreaks. Ingested as `naat-certified-semantic-smoothing`.
* A4, Lai et al., LeFCert for language-empowered foundation models. Ingested as `lefcert-foundation-models`.
* A5, Hu et al., randomized smoothing for LLM multi-agent consensus. Ingested as `rs-llm-multi-agent`. The wiki records that no system bound is proved.
* A6, Abram et al., cryptography from planted graphs. Ingested as `cryptography-from-planted-graphs`.
* A7, OWASP Top 10 for Agentic Applications, a practitioner document. Not yet ingested, and excluded by the survey itself.
* B1, Ferrag et al., prompt injections to protocol exploits, origin of IMTM. Ingested as `imtm-prompt-injections-protocols`.
* B2, Siu et al., a framework for formalizing LLM agent security. Ingested as `formalizing-llm-agent-security`.
* B3, Debenedetti et al., CaMeL. Ingested as `camel-defeating-prompt-injections`. The wiki records that the paper has no theorem.
* B4, Zhu et al., MELON. Ingested as `melon-indirect-prompt-injection`. The wiki retracts the survey's claim of a detection proof.
* B5, Ko et al., seven security challenges in cross-domain multi-agent systems. Ingested as `seven-challenges-cross-domain-mas`. The wiki corrected the list of seven.
* B6, Goldwasser et al., oblivious defense and backdoor removal without detection. Ingested as `oblivious-defense-backdoor-removal`.
* B7, Christiano et al., backdoor defense, learnability and obfuscation. Ingested as `backdoor-defense-learnability-obfuscation`.
* B8, Vafa, Bogdanov and Rosen, statistically undetectable backdoors in deep networks, announced as a talk. Not yet ingested. A related submission sits in `raw/20344_Statistically_Undetectab.pdf` and the wiki leaves its attribution unverified.
* B9, Ngo et al., cryptographic backdoor, boon and bane. Ingested as `crypto-backdoor-boon-bane`.
* B10, Ball et al., the impossibility of separating intelligence from judgment. Ingested as `filter-impossibility-ai-alignment`, restated there as existential.
* B11, Rao et al., jailbreak paradox. Ingested as `jailbreak-paradox`.
* B12, Ghosal et al., Immune. Ingested as `immune-rlhf-jailbreak-defense`. The wiki records its Theorem 1 as a pointwise suboptimality bound.
* B13, Chakraborty et al., MaxMin-RLHF. Ingested as `maxmin-rlhf-impossibility`.
* B14, Ghosal et al., PKE from planted clique and noisy k-LIN. Ingested as `pke-from-planted-clique`.
* B15, Hirahara and Shimizu, planted clique conjectures are equivalent. Ingested as `hirahara-planted-clique-conjectures-equivalent`.
* B16, Wein, low-degree polynomials survey. Ingested as `low-degree-polynomials-survey`.
* B17, Carpentier et al., low-degree bounds via almost orthonormal bases. Ingested as `low-degree-almost-orthonormal`.
* B18, Even et al., lower bounds in latent models. Ingested as `lb-latent-models-clustering`.
* B19, Seferis et al., smoothing meets VLMs. Ingested as `rs-meets-vlm`. The wiki marks the survey's praise of it as the survey's own prose.
* B20, Shpilevskiy et al., ADDS. Ingested as `adds-adaptive-diffusion-smoothing`. The wiki corrects the survey's ICML Oral venue to a workshop submission.
* B21, Liu et al., certified defense for offline RL. Ingested as `multi-level-certified-offline-rl`.

## 5. Unfetched papers

`.sink/paywalled.md` lists one paper, Brzuska, Couteau, Egger and Quach, On Bounded Storage Key Agreement and One-Way Functions, TCC 2024. It is marked resolved on 2026-08-20, supplied by hand as `raw/BCEQ24_BSMKeyAgreementOWF.pdf`. No unresolved paywalled item remains.

The wiki names further papers as candidate ingests that are not in `raw/`. A later search should check these before fetching anything:

* From the summer programme. Kearns and Valiant 1994, Blum, Furst, Kearns and Lipton 1993, the Kearns and Vazirani textbook, Bellare and Rogaway concrete-security notes, Valiant 1984, and Neural Interactive Proofs (arXiv 2412.08897).
* From the native-asymmetry analysis. Naor STOC 1996, Viola SICOMP, Głuch and Urbanke ICML 2021 (arXiv 2010.01039), Karchmer SaTML 2023 (on disk as K23 but without a page), Zhang et al., Watermarks in the Sand (arXiv 2311.04378), and arXiv 2504.20310.
* From the 2026-07-10 log entry. Liu and Pass 2020, IRS 2022, HILNO 2023, Hirahara 2022, Liu, Mazor and Pass 2025, the traitor-tracing lower bounds DNRRV 2009 and Ullman 2013, GVV22, Tiegel 2023 and 2024, and Daniely and Vardi 2021.
* From `CLAUDE.md`. Xiao and Devadas, PAC Membership Privacy, CRYPTO 2023, the transformer and RNN learning separation (arXiv 2503.11272), and Shen et al. on training-map identifiability (arXiv 2602.08723).

## 6. Gaps

Heuristic. Each gap is judged from the absence of a source or concept page in the topics above. None was checked against the literature.

* Attacker-side learning lower bounds for privacy. The wiki holds SQ and exponent bounds on learners and one information-theoretic bound on a membership attacker (Haghifam, Smith and Ullman). No page prices a membership, inversion or reconstruction attacker by SQ queries, CSQ queries or an exponent, and `CLAUDE.md` records that cell as empty.
* Information relative to a predictor class. Capacity-bounded DP and the kernel Rényi audit are the only pages that restrict the witness class. No page treats leakage measured against a bounded family of decoders, or the failure of data processing for such measures.
* Estimation against detection for the exponents. The generative-exponent pages price detection, and `CLAUDE.md` says strong recovery at the generative rate was settled for polynomial links, but no page states recovery thresholds for the multi-index or attacker-relevant tasks.
* Hardness of learning from codes and LPN for attack models. Lattice-based hardness of learning is covered (CLWE, periodic neurons, one hidden layer). LPN appears only through covert learning, and the Kearns and Valiant and Blum et al. lines are named but not held.
* Meta-complexity and Kt-based learning. Liu and Pass, Hirahara and related work are named as candidates for the threshold reduction and have no pages.
* Fingerprinting and traitor-tracing lower bounds for DP. Named as a standing obligation for any membership game, with no page, although the Tardos prior appears inside the Kaplan et al. page.
* Hypothesis-testing views of DP. No page on f-DP or Gaussian DP tradeoff functions as the language for attack power, although ADDS uses GDP composition.
* Memory-bounded and ratio-parameterized privacy adversaries. Recorded as open slots in `CLAUDE.md`, with no definition in the wiki.
* Gradient and split-learning leakage theory. LAMP is the only gradient-inversion page and it is empirical. No page gives a formal model of what an activation or gradient channel leaks to a bounded learner.
* Leakage from encrypted or secret-shared pipelines. No page treats homomorphic encryption, threshold decryption or secure aggregation, or what a bounded attacker learns from the outputs such pipelines release.
* Attribute and property inference games. Distribution inference has one page and attribute inference appears only inside the Yeom page.
