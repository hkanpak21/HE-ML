# Facts about prior work

This register holds every fact about prior work that the line on formalizing AI security has established, one entry per claim, with its pointer, how it was read and its corrections. Its source digests of the FORMAL_SECURITY programme, the FORMAL_SECURITY wiki, the HE-ML repository and the scan of 2026-10-25 are in sources/.

# Membership inference and sample complexity

## fact-yeom-membership-zero-baseline
claim: Yeom et al. define membership advantage so that the public-knowledge baseline is degenerate (advantage zero, success one half), so the marginal-advantage form of membership advantage is a no-op and is already published.
paper: Yeom, Giacomelli, Fredrikson and Jha, IEEE CSF 2018, no arXiv recorded. Also cited for the same point are Xiao and Devadas, PAC Membership Privacy, CRYPTO 2023, and Desfontaines and Pejó, PoPETs 2020, dimension R.
pointer: Definition 4 and Experiment 1, where the paper proves the two posteriors equal. Definition 6 is the attribute advantage, whose baseline is the Bayes-optimal simulator, which is not degenerate and which the authors reject for rewarding accuracy.
read: recorded, checked against the PDF by a FORMAL_SECURITY session 2026-08-22 (root CLAUDE.md and the audit). The wiki page carries date_verified 2026-08-20 with Definitions 4 and 6 checked character by character.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/privacy-risk-overfitting.md, FS:wiki/sources/sok-differential-privacies.md, FS:wiki/analyses/summer-2026-research-programme.md
corrections:
  - 2026-07-25 The wiki retracted the programme's COMP-MEM marginal-advantage game as a no-op already published by Yeom et al., from web sweeps.
  - 2026-08-22 The pointer was corrected. The old record cited Definition 6 for the zero-baseline result.
  - 2026-10-25 The wiki-claims digest finds the body of FS:wiki/analyses/native-asymmetry-in-learning.md still citing Yeom Definition 6.

## fact-hsu-membership-sample-gap
claim: In Gaussian mean estimation every sample-based membership attack needs about n²ρ² + n reference samples and a matching attack exists, so the attacker can need many more samples than the trainer (proven, information-theoretic units, unbounded attacker).
paper: Haghifam, Smith and Ullman, The Sample Complexity of Membership Inference and Privacy Auditing, arXiv 2508.19458 (HSU25). The 2026-10-13 sweep records arXiv v2 of 8 October 2026 as to appear at FOCS 2026. The wiki page records no refereed venue.
pointer: The FORMAL_SECURITY records give Theorem 1.1, with the antecedent d > c₁(n + n²ρ²), success at TPR at least 0.51 and FPR at most 0.49, and spiked-covariance hard instances. The 2026-10-25 scan gives Theorem 3.1 for the lower bound (noise-adding estimators, accuracy 0.51) and Theorem 3.2 for the matching attack. No record says whether these are an informal and a formal statement of one result.
read: recorded, verified in full against the PDF by a FORMAL_SECURITY session 2026-08-22 (wiki date_verified 2026-08-22 against raw/HSU25_SampleComplexityMIA.pdf, proofs read for statement and method only). Also full, reader subagent, 2026-10-25.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:exp/survey/lab/results/literature-sweep/information.md, FS:wiki/sources/haghifam-sample-complexity-mia.md, HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-hsu-gap-prices-covariance
claim: The Haghifam, Smith and Ullman separation vanishes when the attacker knows the covariance, since about min{n, 1/ρ²} samples then suffice and are optimal, so it prices the attacker's ignorance of Σ rather than attack difficulty.
paper: Haghifam, Smith and Ullman, arXiv 2508.19458 (HSU25).
pointer: Theorem 1.2 per the FORMAL_SECURITY records. The 2026-10-25 scan states that with known covariance order n samples suffice, with no theorem number.
read: recorded, wiki page date_verified 2026-08-22. Also full, reader subagent, 2026-10-25.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/haghifam-sample-complexity-mia.md, HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-hsu-chi-square-technique
claim: The Haghifam, Smith and Ullman lower bound uses the Ingster and Suslina chi-squared second-moment method over planted subspaces, which the FORMAL_SECURITY root calls one step from a low-degree restatement and a competitive hazard (heuristic).
paper: Haghifam, Smith and Ullman, arXiv 2508.19458 (HSU25).
pointer: Lower-bound technique, no section number recorded.
read: recorded, the root CLAUDE.md records the paper verified in full on 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/haghifam-sample-complexity-mia.md
corrections: none

## fact-hsu-single-mechanism-open
claim: Haghifam, Smith and Ullman state that a sample-complexity separation for a single mechanism is open.
paper: Haghifam, Smith and Ullman, arXiv 2508.19458 v2 (HSU25).
pointer: Not recorded beyond the sweep sheet HSU25.
read: recorded, agent reading of the 2026-10-13 sweep.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/information.md
corrections: none

## fact-sablayrolles-bayes-attack-loss-only
claim: Under a Gibbs-posterior model of training the Bayes-optimal membership attack reads the weights only through the loss (proven under the posterior assumption).
paper: Sablayrolles, Douze, Schmid, Ollivier and Jégou, ICML 2019 (SDSOJ19).
pointer: Theorem 2.
read: recorded, read in the PDF by a FORMAL_SECURITY session 2026-10-13. An HE-ML search of 2026-10-16 found the same result and wrote no note.
status: verified
record: FS:exp/survey/lab/results/literature-sweep/information.md, FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md, HE-ML:lib/literature/positioning.md
corrections: none

## fact-sablayrolles-dp-membership-posterior
claim: Under the same Gibbs-posterior model, ε-DP bounds the membership posterior by λ + ε/4 (proven).
paper: Sablayrolles, Douze, Schmid, Ollivier and Jégou, ICML 2019 (SDSOJ19).
pointer: Property 1.
read: recorded, read in the PDF by a FORMAL_SECURITY session 2026-10-13.
status: verified
record: FS:exp/survey/lab/results/literature-sweep/information.md
corrections: none

## fact-suri-posterior-assumption-fails-sgd
claim: Suri, Zhang and Evans argue that the Sablayrolles et al. posterior assumption fails for SGD and give a white-box membership attack.
paper: Suri, Zhang and Evans, TMLR 2024, arXiv 2406.11544. It falls outside the HE-ML venue rule.
pointer: Not recorded.
read: recorded, found by an HE-ML search of 2026-10-16, no note written.
status: recorded
record: HE-ML:lib/literature/positioning.md
corrections: none

## fact-blind-baselines-beat-mia
claim: Attacks that never query the model beat the best reported membership attacks on eight published foundation-model evaluation datasets, so those datasets support no leakage claim (empirical).
paper: Das, Zhang and Tramèr, DATA-FM workshop at ICLR 2025, arXiv 2406.16201.
pointer: Abstract, p. 1.
read: recorded, quotation verified by a FORMAL_SECURITY session 2026-09-03. The wiki page carries no stamp and was ingested on 2026-08-20.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-09-03-halil-quotes-batch-a.md, FS:wiki/sources/blind-baselines-beat-mia.md, FS:exp/survey/paper/parked/formalization/games.tex
corrections: none

## fact-meeus-mia-distribution-shift
claim: Meeus et al. locate the carrier of blind-baseline success in a distribution shift between the halves of a benchmark, with years the most predictive bag-of-words features on WikiMIA (empirical).
paper: Meeus et al., SaTML 2025.
pointer: Not recorded.
read: recorded, cited in the survey draft, no verification recorded.
status: recorded
record: FS:exp/survey/paper/sections/02-problem.tex, FS:exp/survey/paper/parked/formalization/games.tex
corrections: none

## fact-mia-null-unsamplable
claim: Membership inference cannot prove that a production model was trained on given data, because bounding a false-positive rate needs models trained without the record, which a party who cannot afford a training run cannot sample.
paper: Zhang, Das, Kamath and Tramèr, IEEE SaTML 2025 (ZDKT25), no arXiv recorded. A position paper.
pointer: Abstract. Section V lists three settings where membership inference stays sound.
read: recorded, wiki page ingested on 2026-08-20 with no stamp. The survey draft cites it.
status: recorded
record: FS:exp/survey/paper/sections/02-problem.tex, FS:wiki/sources/mia-cannot-prove-training.md
corrections:
  - 2026-09-03 The venue was corrected from a preprint to IEEE SaTML 2025, in FS:exp/survey/lib/reports/archive/2026-09-03-halil-review-survey-round-2.md.

## fact-mias-near-random-on-llms
claim: Five membership attacks barely beat random guessing on one-epoch pretrained LLMs with a genuine train and test split (empirical).
paper: Duan et al., COLM 2024, no arXiv recorded.
pointer: Abstract, p. 1.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/do-mias-work-on-llms.md
corrections: none

## fact-shokri-has-no-game
claim: Shokri et al. contain no definition or theorem, and the membership game the literature attributes to them is Yeom et al.'s.
paper: Shokri, Stronati, Song and Shmatikov, IEEE S&P 2017, no arXiv recorded.
pointer: The page records zero occurrences of the words Definition and Theorem in the file.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/membership-inference-shokri.md, FS:wiki/sources/privacy-risk-overfitting.md
corrections: none

## fact-lira-low-fpr-yeom-game
claim: LiRA made the true-positive rate at low false-positive rate the standard membership metric, and its game is adopted from Yeom et al.
paper: Carlini, Chien, Nasr, Song, Terzis and Tramèr, Membership Inference Attacks From First Principles, IEEE S&P 2022, arXiv 2112.03570.
pointer: Definition 1, Section VI-A.
read: recorded, wiki page ingested from the raw PDF on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/mia-from-first-principles.md, FS:wiki/concepts/low-fpr-evaluation-regime.md
corrections: none

## fact-lira-priced-in-training-runs
claim: LiRA prices its attack in shadow-model training runs, N = 64 for ImageNet and 256 otherwise.
paper: Carlini, Chien, Nasr, Song, Terzis and Tramèr, IEEE S&P 2022, arXiv 2112.03570.
pointer: Not recorded. The survey codebook has no training-runs unit, so the survey row is coded time and a dispute is recorded, while the ontology codes eight works under res-training-runs.
read: recorded, quotation batch of 2026-09-03, no verification state given.
status: recorded
record: FS:exp/survey/lib/reports/archive/2026-09-03-halil-quotes-batch-b.md
corrections: none

# Reconstruction and fibers of the training map

## fact-balle-reconstruction-robustness-definition
claim: Reconstruction robustness quantifies over any reconstruction map R with tolerance η, success bound γ and an oblivious baseline κ(η) = sup over z₀ of P[ℓ(Z, z₀) ≤ η], in the relation P[ℓ(Z, R(θ)) ≤ η] ≤ γ, and carries no computational bound.
paper: Balle, Cherubin and Hayes, Reconstructing Training Data with Informed Adversaries, IEEE S&P 2022, arXiv 2201.04845.
pointer: Definition 2 per the FORMAL_SECURITY programme records. The wiki page cites Definition 1 for reconstruction robustness. The authors write R for the reconstruction attack itself.
read: recorded, verified verbatim by a FORMAL_SECURITY sweep 2026-08-05 and again in the audit of 2026-08-22. The wiki page carries date_verified 2026-08-20.
status: disputed, the records give different definition numbers
record: FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/reconstructing-informed-adversaries.md
corrections: none

## fact-balle-dp-bounds-reconstruction
claim: Differential privacy bounds reconstruction robustness relative to a fixed baseline (proven).
paper: Balle, Cherubin and Hayes, IEEE S&P 2022, arXiv 2201.04845.
pointer: Theorems 2 and 5, Corollaries 3 and 4.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/reconstructing-informed-adversaries.md
corrections: none

## fact-reconstruction-query-lower-bounds
claim: A white-box reconstruction adversary against a DP learner needs a number of queries bounded below as a function of the learner's privacy parameters, counted in plain queries with a fixed known remainder dataset (proven).
paper: Mukherjee and Lokam, 2024, arXiv 2303.16372.
pointer: Theorems 1 and 2.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/query-complexity-reconstruction.md
corrections: none

## fact-dinur-nissim-reconstruction-thresholds
claim: A subset-sum database with perturbation o(n) is non-private against an exponential adversary and with perturbation o(√n) against a polynomial one, while Õ(√T(n)) noise suffices against time-T(n) adversaries, and the main result is a polynomial reconstruction algorithm (proven).
paper: Dinur and Nissim, PODS 2003, no arXiv recorded. The venue is not stated in the PDF.
pointer: §3.1 Exponential Adversary and §3.2 Polynomially Bounded Adversary, sibling subsections inside §3, with §3.1 a warm-up. Theorems 2 and 3 give the attacks and Theorem 5 feasibility. The attack is a linear program over subset sums with rounding at 1/2. The words OLS, least squares and regression occur zero times.
read: recorded, corrected against the PDF by a FORMAL_SECURITY session 2026-08-22, wiki page date_verified 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/dinur-nissim-revealing-information.md
corrections:
  - 2026-08-22 Three clauses were corrected against the PDF. The old record placed the separation in §3 against §4 as the main theorem and attributed an OLS example to the paper.
  - 2026-10-25 The wiki-claims digest finds FS:wiki/index.md and the 2026-07-26 wiki log entry still describing §3 against §4 with the separation as the main theorem.

## fact-fiber-framing-occupied
claim: Size against navigability of the training-map fiber with a complexity separation is already Dinur and Nissim, with Cohen et al. and Kaplan et al. on the reconstruction side, so of the fiber framing only constrained fiber navigation on the training map remains.
paper: Dinur and Nissim, PODS 2003. Cohen et al., ITCS 2025, arXiv 2405.15753. Kaplan, Mansour, Nissim and Stemmer, ITCS 2026, arXiv 2505.23658. Suliman et al., USENIX Security 2025, arXiv 2411.05658.
pointer: The 2026-07-26 wiki log entry and the negative results of the root CLAUDE.md.
read: recorded, made on 2026-07-26 from sweep extractions, with the Dinur and Nissim details corrected against the PDF on 2026-08-22.
status: recorded
record: FS:CLAUDE.md, FS:wiki/concepts/fiber-of-the-training-map.md, FS:exp/docs/notes/fibers-of-the-training-map.md
corrections:
  - 2026-08-22 The audit flags the refutation of the fiber framing for re-examination (audit §5).

## fact-kaplan-memorization-separated
claim: Kaplan et al. pose computational against statistical memorization directly and separate the two for specific mechanisms under a Tardos prior, which restates the Dinur and Nissim separation (proven).
paper: Kaplan, Mansour, Nissim and Stemmer, ITCS 2026, arXiv 2505.23658.
pointer: Definitions 3.1 and 3.3, Lemmas 3.5, 3.7 and 4.8.
read: recorded, wiki page date_verified 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/kaplan-bayesian-memorization-reconstruction.md
corrections: none

## fact-cohen-narcissus-equals-one-wayness
claim: Computational Narcissus resiliency, a computational security notion for reconstruction, is equivalent to one-wayness for functions that are efficiently computable and well-spread (proven).
paper: Cohen, Kaplan, Mansour, Moran, Nissim, Stemmer and Tsfadia, ITCS 2025, arXiv 2405.15753.
pointer: Definition C.1 (the notion), Definition C.4 (well-spread), Theorem C.5 (the equivalence). Appendices other than C, D and E were read only in part.
read: recorded, corrected against the PDF 2026-08-22, wiki page date_verified 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/cohen-data-reconstruction.md
corrections:
  - 2026-08-22 The antecedent was corrected. The old record placed the equivalence at Definition C.1 with no condition on the function.

## fact-cohen-narcissus-does-not-compose
claim: Narcissus resiliency does not compose in general.
paper: Cohen, Kaplan, Mansour, Moran, Nissim, Stemmer and Tsfadia, ITCS 2025, arXiv 2405.15753.
pointer: Appendix D.
read: recorded, wiki page date_verified 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/cohen-data-reconstruction.md
corrections: none

## fact-shen-training-map-identifiability
claim: Shen et al. study identifiability of the training map against optimization.
paper: Shen et al., arXiv 2602.08723.
pointer: Not recorded.
read: recorded, listed in the root CLAUDE.md with no verification recorded.
status: recorded
record: FS:CLAUDE.md
corrections: none

## fact-suliman-forging-empirical
claim: Suliman et al. find empirically that published data-forging attacks miss the reproduction-error threshold by orders of magnitude and are detectable, and their conjecture that gradient-equivalent mini-batches within domain constraints may be infeasible to find is incidental and names no adversary class, reference problem or assumption.
paper: Suliman, Halimi, Kadhe, Baracaldo and Leith, Towards a Re-evaluation of Data Forging Attacks in Practice, USENIX Security 2025, arXiv 2411.05658.
pointer: Contribution list, §5.3 and the conclusion. Propositions 1 to 3 concern the existence of gradient-equivalent batches. The paper says nothing about the distinction between the evaluation map and the training map.
read: recorded, corrected against the PDF 2026-08-22, wiki page date_verified 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/suliman-data-forging-attacks.md
corrections:
  - 2026-08-22 The framing was corrected. The game-family note had taken the conjecture as the paper's subject, while the title and headline result are an empirical re-evaluation of data forging.

## fact-jagielski-np-hardness-evaluation-map
claim: Jagielski et al. prove functionally equivalent extraction NP-hard for the evaluation map only, so no hardness theorem covers navigation of the training-map fiber.
paper: Jagielski, Carlini, Berthelot, Kurakin and Papernot, USENIX Security 2020, arXiv 1909.01838 (JCBKP20).
pointer: Theorem 2, by reduction from subset sum over {0,1}^d.
read: recorded, Jagielski page date_verified 2026-08-20. That the training-map case is open is a positioning claim of the root CLAUDE.md.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/jagielski-model-extraction.md, FS:wiki/concepts/fiber-of-the-training-map.md
corrections: none

## fact-xiao-learnable-obfuscation-ind-cpa
claim: No injective learnable obfuscation that preserves learnability with constant advantage is IND-CPA secure against an adversary who chooses the challenge distributions and its concept class, an impossibility about the encoding T and not about a training map (proven).
paper: Xiao, Suh and Devadas, Formal Privacy Proof of Data Encoding, The Possibility and Impossibility of Learnable Obfuscation, CCS 2024, no arXiv recorded.
pointer: Theorem 1, Definitions 2 and 5. The term one-way function appears nowhere. The authors name two escapes, restricting the plaintext choice or denying the adversary the model trained on encoded data. Theorems 2 to 7 on the possibility side are unverified.
read: recorded, checked against the PDF 2026-08-22, wiki page date_verified 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/xiao-formal-privacy-proof-data-encoding.md
corrections:
  - 2026-08-22 Scope and title were corrected. The old record read the impossibility as one about a training map tied to one-way functions, under the title Learnable Encryption.
  - 2026-10-25 The wiki-claims digest finds FS:raw/SOURCES.md still giving the title as Learnable Encryption and FS:wiki/index.md calling the page unread.

## fact-no-cdp-reconstruction-from-weights
claim: No work applies computational or statistical DP to reconstruction from weights.
paper: none found. The line checked runs from Beimel, Nissim and Omri to Ghazi, Ilango, Kamath, Kumar and Manurangsi, FOCS 2023.
pointer: Root CLAUDE.md.
read: recorded, an absence finding the root records as verified negative across that line.
status: recorded
record: FS:CLAUDE.md
corrections: none

## fact-lamp-no-success-criterion
claim: The gradient-inversion attack LAMP defines no success criterion, reports ROUGE with no threshold and no gradient-free control, and prices cost in GPU-hours.
paper: LAMP, authors and venue not recorded in the digests.
pointer: Not recorded.
read: recorded, audit finding of 2026-08-22. The wiki page carries date_verified 2026-08-20.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/lamp-gradient-inversion.md
corrections: none

## fact-wang-gradient-inversion-tensor
claim: Inputs can be recovered from the gradients of a random two-layer network with known weights by tensor decomposition (proven).
paper: Wang, Lee and Lei, Reconstructing Training Data from Model Gradient, Provably, AISTATS 2023, arXiv 2212.03714.
pointer: Theorem 5.1.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-single-sample-gradient-inversion-np-complete
claim: Wang, Lee and Lei note that single-sample gradient inversion is NP-complete.
paper: Wang, Lee and Lei, AISTATS 2023, arXiv 2212.03714.
pointer: Section 3.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

# Statistical-computational gaps and low-degree models

## fact-low-degree-security-is-circuit-security
claim: Bogdanov et al. and Abram et al. state cryptographic security against size-bounded circuits and offer low-degree hardness as supporting evidence, so neither defines security against a low-degree adversary.
paper: Bogdanov, Jones, Rosen and Zadik, TCC 2024, arXiv 2409.16227, ePrint 2024/1497 (BJRZ). Abram, Beimel, Ishai, Kushilevitz and Narayanan, TCC 2023, ePrint 2023/1929 (ABIKN).
pointer: BJRZ Theorem 2.1 (unconditional low-degree bound), Propositions 4.1 and 4.3 (reductions over (s, ε)-indistinguishability, the proof of 4.1 building an explicit circuit), Conjectures 1.3 and 1.4 (stated in polynomial time with low-degree lower bounds as evidence). ABIKN abstract, adversaries of size n^{o(log n)} with advantage n^{−Ω(1)}.
read: recorded, corrected against the PDFs by a FORMAL_SECURITY session 2026-08-22. Wiki pages date_verified 2026-08-22 (BJRZ) and 2026-08-20 (ABIKN).
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/bogdanov-low-degree-planted-subgraph.md, FS:wiki/sources/cryptography-from-planted-graphs.md, FS:wiki/analyses/native-asymmetry-in-learning.md
corrections:
  - 2026-07-25 The line that no security definition quantifies over SQ or low-degree adversaries was retracted as false, citing BJRZ and ABIKN, from web sweeps.
  - 2026-08-22 That retraction was corrected as too broad, because both papers quantify security over size-bounded circuits and neither over a low-degree adversary.

## fact-bjrz-planted-clique-noise-caveat
claim: Bogdanov et al. note that planted clique and planted subgraph technically miss the noise-robust hypothesis of the low-degree conjecture.
paper: Bogdanov, Jones, Rosen and Zadik, TCC 2024, arXiv 2409.16227 (BJRZ).
pointer: Not recorded beyond the root CLAUDE.md.
read: recorded, in the root CLAUDE.md with the 2026-08-22 correction against the PDF.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/bogdanov-low-degree-planted-subgraph.md
corrections: none

## fact-ngo-kim-verifier-query-bounded
claim: Ngo and Kim's certificates are a query-bounded verifier result whose soundness quantifies over an unrestricted cheating prover, with the SQ restriction on the certified algorithm and on the verifier's query budget.
paper: Ngo and Kim, 2026, arXiv 2607.15528.
pointer: The root CLAUDE.md places the unrestricted prover in Definition 1, Universal Soundness. The wiki page places it in Definitions 3.1 and 3.2 and the remarks on Definition 3.2, with verifier sample complexity O(log k / τ²) in Theorem 2.
read: recorded, retracted against the PDF 2026-08-20. Both records say verified on 2026-08-20.
status: disputed, the records place the unrestricted prover in different definitions
record: FS:CLAUDE.md, FS:wiki/sources/certificates-statistical-algorithms.md
corrections:
  - 2026-08-20 The earlier record of SQ-quantified soundness was retracted against the PDF.
  - 2026-10-25 The wiki-claims digest finds the body of FS:wiki/analyses/native-asymmetry-in-learning.md still citing Ngo and Kim as SQ-quantified soundness.

## fact-buhai-quasipoly-low-degree-false
claim: Buhai et al. disprove the quasi-polynomial low-degree conjecture in the regime it was stated, so low-degree-bounded and quasi-polynomial-bounded adversaries are provably different (proven).
paper: Buhai, Hsieh, Jain and Kothari, FOCS 2025, arXiv 2505.17360.
pointer: Abstract, an n^{O(log^{1/(k−1)} n)}-time distinguisher in the square S_n-symmetric regime. Theorem 2.4 and Remark 2.3 give the polynomial-time distinguisher for the rectangular generalization only, and closing the square case is open. The largest-eigenvalue construction has a non-product null and refutes nothing.
read: recorded, clauses corrected against the PDF 2026-08-20 in raw/SOURCES.md and the root CLAUDE.md. The page has no date_verified.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/quasi-poly-low-degree-conjecture-false.md
corrections:
  - 2026-08-20 The refutation was recorded with its clauses, namely that the polynomial-time distinguisher covers the rectangular variant only.

## fact-hsieh-low-degree-rigorous-implications
claim: A vanishing low-degree likelihood ratio rigorously defeats the stated test classes only for a noisy version of the planted law, and it rules out no polynomial-time algorithm (proven).
paper: Hsieh, Kane, Kothari, Li, Mohanty and Tiegel, STOC 2026, arXiv 2601.05850.
pointer: Theorem 1.1 (total variation), Theorem 1.2 (symmetric polynomials of degree at most ε log n / (C log log n), only a distribution over R^n assumed), Theorem 1.3 (one signed subgraph count). Theorems 1.1 and 1.3 assume permutation invariance. The root requires any security claim resting on a low-degree adversary to cite this paper and Buhai et al. with these clauses.
read: recorded, corrected against the PDF 2026-08-20, no date_verified.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/rigorous-implications-low-degree.md
corrections:
  - 2026-08-20 The record was corrected to make the noisy version of the problem the universal hypothesis across the three results.

## fact-holmgren-wein-low-degree-counterexamples
claim: Two testing problems built from efficiently decodable error-correcting codes defeat degree-O(log n) polynomials while a polynomial-time test succeeds, refuting the low-degree conjecture as Hopkins stated it (proven).
paper: Holmgren and Wein, ITCS 2021, arXiv 2004.08454.
pointer: Theorem 3.1. The word parity occurs zero times.
read: recorded, wiki page date_verified 2026-08-20, audit of 2026-08-22.
status: verified
record: FS:wiki/sources/holmgren-counterexamples-low-degree.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-20 The page was corrected to say the counterexamples are built from codes, not parity.
  - 2026-08-22 The audit confirms that parity occurs zero times in the paper.

## fact-hirahara-shimizu-planted-clique-equivalences
claim: Search and decision variants of the planted clique conjecture are equivalent by unconditional reductions, and refutation is equivalent to a separate statement, average-case k-clique on G(n, 1/2) (proven).
paper: Hirahara and Shimizu, STOC 2024, ECCC TR24-058 (identifier given in the compass artifact).
pointer: Abstract, no single theorem recorded.
read: recorded, wiki page date_verified 2026-08-20, audit of 2026-08-22.
status: verified
record: FS:wiki/sources/hirahara-planted-clique-conjectures-equivalent.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-20 The page was corrected to place refutation in a separate class.
  - 2026-08-22 The audit records the separate equivalence with average-case k-clique on G(n, 1/2).

## fact-lll-beats-sos-noiseless
claim: LLL recovers labels and direction exactly at n = d+1 in a noiseless clustering problem where low-degree and SoS lower bounds hold up to n = Õ(d²), and lattice methods likewise solve noiseless hCLWE, planted hypercube, planted sparse vector and parity while SQ, SoS and low-degree bounds stay formally true (proven).
paper: Zadik, Song, Wein and Bruna, COLT 2022, arXiv 2112.03898 (ZSWB22).
pointer: Theorem 1.1. Inverse-polynomial noise breaks the method.
read: recorded, wiki page date_verified 2026-08-20. The programme's cautionary shelf of 2026-07-10 cites the same result.
status: verified
record: FS:exp/literature/related-work.md, FS:wiki/sources/zadik-lattice-surpass-sos.md
corrections: none

## fact-group-testing-has-no-gap
claim: Not every planted problem has a statistical-computational gap, and the cautionary shelf names group testing as the example.
paper: none named in the record.
pointer: Cautionary shelf, §7. Entries dated 2025 to 2026 marked there with a dagger are single-sourced.
read: recorded, cautionary shelf of 2026-07-10, no verification recorded.
status: recorded
record: FS:exp/literature/related-work.md
corrections: none

## fact-blum-rivest-wrong-substrate
claim: The cautionary shelf records the worst-case ERM hardness of Blum and Rivest as the wrong substrate for the programme's hardness claims.
paper: Blum and Rivest, venue not recorded.
pointer: Cautionary shelf, §7.
read: recorded, cautionary shelf of 2026-07-10, no verification recorded.
status: recorded
record: FS:exp/literature/related-work.md
corrections: none

## fact-sq-low-degree-equivalence
claim: SQ statistical dimension and the minimum degree of a good low-degree distinguisher are nearly equivalent for problems satisfying a niceness condition, which one-shot planted clique fails (proven).
paper: Brennan, Bresler, Hopkins, Li and Schramm, COLT 2021, no arXiv recorded.
pointer: §1.2, Definition 1.4.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/brennan-sq-lowdegree-equivalence.md
corrections:
  - 2026-09-03 The venue was resolved as COLT 2021, in FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md.

## fact-fgrvx17-planted-clique-sq-bound
claim: No polynomial-time statistical algorithm detects planted clique with VSTAT(o(n²/k²)) queries, and any SQ algorithm needs n^{Ω(log n)} queries to VSTAT(n^{2−δ}/k²) (proven).
paper: Feldman, Grigorescu, Reyzin, Vempala and Xiao, J. ACM 2017 (FGRVX17), no arXiv recorded.
pointer: Theorem 2.9. The parked learning-oracle draft specializes Theorem 2.9 to planted bipartite k-clique with k ≤ N^{1/2−δ}.
read: recorded, wiki page date_verified 2026-08-20. The oracle draft that quotes it is recorded as re-verified.
status: verified
record: FS:wiki/sources/feldman-statistical-algorithms-planted-clique.md, FS:exp/survey/paper/parked/formalization/oracle.tex
corrections: none

## fact-fgrvx17-theorem-one-quoted-form
claim: The proof note of 2026-04-23 quotes FGRVX17 as Theorem 1.1 in the form q·τ² ≥ Ω(n^{2δ}), while the later re-verified oracle draft quotes Theorem 2.9 parameters, and no record reconciles the two citations.
paper: Feldman, Grigorescu, Reyzin, Vempala and Xiao, J. ACM 2017 (FGRVX17).
pointer: Theorem 1.1 as quoted in the proof note.
read: recorded, the proof note records no check against the paper.
status: recorded
record: FS:.tools/proof.tex
corrections: none

## fact-barak-sos-planted-clique-gap
claim: The degree-d SoS relaxation of clique has integrality gap at least n^{1/2 − c(d/log n)^{1/2}}, unconditionally (proven).
paper: Barak, Hopkins, Kelner, Kothari, Moitra and Potechin, FOCS 2016, arXiv 1604.03084.
pointer: Theorem 1.1.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/barak-sos-lower-bound-planted-clique.md
corrections:
  - 2026-09-03 The venue was resolved as FOCS 2016, in FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md.

## fact-pke-from-planted-clique
claim: Public-key encryption secure against polynomial-size adversaries follows from n^{(log n)^α} hardness of standard planted clique plus a noisy k-LIN conjecture over expanders (proven under these assumptions).
paper: Ghosal, Hair, Jain and Sahai, STOC 2025, ePrint 2025/1501.
pointer: Abstract.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/pke-from-planted-clique.md
corrections: none

## fact-barak-wigderson-two-assumptions
claim: The public-key paper the wiki attributes to Barak and Wigderson states two assumptions, not the three an earlier wiki page listed.
paper: Barak and Wigderson as the wiki names them, page pkc-from-different-assumptions, venue not recorded.
pointer: Not recorded.
read: recorded, corrected against the PDF 2026-08-20, page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/pkc-from-different-assumptions.md
corrections:
  - 2026-08-20 The page was corrected from three assumptions to two.

## fact-clwe-hardness
claim: CLWE is hard under a polynomial-time quantum reduction from worst-case GapSVP and SIVP, and homogeneous CLWE is hard for SQ algorithms (proven).
paper: Bruna, Regev, Song and Tang, Continuous LWE, STOC 2021, no arXiv recorded.
pointer: Abstract.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/bruna-continuous-lwe.md
corrections:
  - 2026-09-03 The venue was resolved as STOC 2021, in FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md.

## fact-lattice-hardness-of-learning
claim: Weakly learning a periodic neuron, or a one-hidden-layer ReLU network of width ω(√(d log d)) under Gaussian noise, is hard for polynomial time if approximate SVP is quantum-hard (proven under that assumption).
paper: Song, Zadik and Bruna, NeurIPS 2021, arXiv 2106.10744. Li, Zadik and Zampetakis, ALT 2025, arXiv 2410.03477.
pointer: Song et al. Theorem 3.3 and Corollary 3.4. Li et al. §3 after Theorem 3.1.
read: recorded, wiki pages ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/hardness-single-periodic-neurons.md, FS:wiki/sources/hardness-one-hidden-layer.md
corrections: none

## fact-pessiland-learning
claim: If no infinitely-often one-way function exists, every unknown adaptively changing distribution is learnable in polynomial time, among other average-case learning tasks (proven).
paper: Hirahara and Nanashima, ECCC TR23-100, 2023. The FOCS 2023 attribution is not stated in the PDF.
pointer: Theorem 2.4 (equivalences with the hypothesis), Theorem 2.3 (agnostic result).
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/learning-in-pessiland.md
corrections:
  - 2026-08-20 The page no longer attributes to the paper any link to adversarial robustness, and two learning tasks it once listed were removed as having no counterpart in the paper.
  - 2026-08-20 The FOCS venue attribution was flagged as not stated in the PDF.

## fact-franz-parisi-equals-low-degree
claim: The Franz-Parisi and low-degree criteria are equivalent for Gaussian additive models, Franz-Parisi hardness implies low-degree hardness for planted sparse models, and counterexamples exist outside these classes (proven).
paper: Bandeira, El Alaoui, Hopkins, Schramm, Wein and Zadik, NeurIPS 2022, no arXiv recorded.
pointer: Definition 1.3 and the model-class antecedent.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/bandeira-franz-parisi-criterion.md
corrections: none

## fact-no-sq-bound-against-poisoning
claim: No SQ or low-degree lower bound against a backdoor or poisoning adversary was found.
paper: none found.
pointer: Sweep computation.md §4 and information.md §4.
read: recorded, null search of the 2026-10-13 agent sweep. No paper from these searches is cited until read.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/computation.md, FS:exp/survey/lab/results/literature-sweep/information.md
corrections: none

# Differential privacy variants

## fact-gky-cdp-limits-narrow
claim: The Groce, Katz and Yerukhimovich limits on computational DP cover only black-box constructions and queries with output in R^n for constant n under natural utility measures, so released models, which the authors exclude, are not covered (proven).
paper: Groce, Katz and Yerukhimovich, TCC 2011, no arXiv recorded (GKY).
pointer: Theorems 1 and 2, and the subsection on limitations at the end of §1.1. The authors exclude queries returning classifiers, graphs or synthetic databases, n growing with the security parameter, utilities with no polynomial error bound, and more than a constant number of queries or a stateless server.
read: recorded, checked against the primary PDF 2026-08-20 with the exclusions pinned verbatim.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/limits-cdp-client-server.md
corrections:
  - 2026-08-20 The exclusions were pinned verbatim, so the folk reading that CDP buys nothing does not apply to released models.

## fact-meisingseth-rechberger-cdp-regimes
claim: Meisingseth and Rechberger show that the SIM∀∃ to IND direction and the GKY utility barrier need ε in O(log κ), a condition the original did not identify, and that IND to SIM∀∃ holds for all ε and δ only with an inflated δ' (proven).
paper: Meisingseth and Rechberger, IACR Communications in Cryptology 2026, no arXiv recorded.
pointer: Antecedent and Theorem 4 (the Lp-utility barrier) as recorded on the page.
read: recorded, wiki page date_verified 2026-08-22, audit §4 of 2026-08-22.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/cdp-wider-parameter-regimes.md
corrections: none

## fact-mprv09-sim-implies-ind-cdp
claim: SIM-CDP implies IND-CDP and the converse is open, while the main theorem makes the weaker SIM∀∃-CDP equivalent to IND-CDP for ε in O(log κ) (proven).
paper: Mironov, Pandey, Reingold and Vadhan, Computational Differential Privacy, CRYPTO 2009, no arXiv recorded.
pointer: Theorem 3, resting on Theorem 2 and the Dense Model Theorem.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/computational-differential-privacy.md
corrections:
  - 2026-09-03 The venue was resolved as CRYPTO 2009, in FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md.

## fact-mprv09-class-relative-cdp-price
claim: Mironov et al. define IND-CDP and SIM-CDP against non-uniform PPT distinguishers, and their Theorem 2 extends to an arbitrary distinguisher family at the cost of closing it under thresholded sums, the price a class-relative definition must pay (proven).
paper: Mironov, Pandey, Reingold and Vadhan, CRYPTO 2009.
pointer: Theorem 2.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-bcv16-cdp-separation-infeasibility
claim: The first single-curator separation of computational from statistical DP is an infeasibility result on a task its authors call unnatural (proven under its assumptions).
paper: Bun, Chen and Vadhan, TCC 2016-B, no arXiv recorded.
pointer: Theorem 11, under sub-exponentially secure one-way functions and extractable zaps.
read: recorded, wiki page ingested from the raw PDF on 2026-08-20, no stamp. The root records the single-curator separation as no longer fully open on 2026-08-20.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/separating-cdp-client-server.md
corrections: none

## fact-gikkm23-cdp-separation-unbounded
claim: A task with an efficient CDP mechanism admits no statistical DP mechanism of constant utility, even an inefficient one, under NIWI, laconic keyless CRHF and diO, on a task the root calls contrived (proven under these assumptions).
paper: Ghazi, Ilango, Kamath, Kumar and Manurangsi, FOCS 2023, arXiv 2301.00104 (GIKKM23).
pointer: The SDP lower bound at constant ε and δ = 1/n^{27}, Assumptions 18, 22 and 26.
read: recorded, wiki page ingested from the raw PDF on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/towards-separating-cdp.md
corrections: none

## fact-gikkm23-breaks-quasipoly-adversaries
claim: The Ghazi et al. mechanism is not CDP against quasi-polynomial adversaries, so a separation of computational from statistical DP on a natural task remains open.
paper: Ghazi, Ilango, Kamath, Kumar and Manurangsi, FOCS 2023, arXiv 2301.00104 (GIKKM23).
pointer: Excluded cases on the wiki page, which quote the authors on the point.
read: recorded, wiki page ingested from the raw PDF on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/towards-separating-cdp.md
corrections: none

## fact-gikkm23-restricted-class-lift
claim: Ghazi et al. first prove privacy against a class of non-adaptive decision-tree adversaries and then lift it to computationally bounded adversaries with cryptography, a template the root records as reusable.
paper: Ghazi, Ilango, Kamath, Kumar and Manurangsi, FOCS 2023, arXiv 2301.00104 (GIKKM23).
pointer: §I.
read: recorded, wiki page ingested from the raw PDF on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/towards-separating-cdp.md
corrections: none

## fact-chlx25-gikkm23-citers-null
claim: The forward citers of Christiano et al. on defendability and of Ghazi et al. on CDP give no new defendability result and no new separation of computational from statistical privacy.
paper: citers of Christiano, Hilton, Lecomte and Xu, ITCS 2025 (CHLX25), and of Ghazi et al., FOCS 2023 (GIKKM23).
pointer: Sweep computation.md §4 and information.md §4.
read: recorded, null search of the 2026-10-13 agent sweep.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/computation.md, FS:exp/survey/lab/results/literature-sweep/information.md
corrections: none

## fact-cdp-inner-product-ot
claim: A two-party CDP protocol for inner product with additive error O(n^{1/6}) implies oblivious transfer, and errors between n^{1/6} and √n are open (proven, uniform black-box reduction).
paper: Haitner, Mazor, Silbak, Tsfadia and Yan, CRYPTO 2025, no arXiv recorded.
pointer: Main theorem as recorded.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/cdp-inner-product-implies-ot.md
corrections: none

## fact-cdp-inner-product-key-agreement
claim: Any non-trivially accurate two-party CDP inner-product protocol implies key agreement (proven).
paper: Haitner, Mazor, Silbak and Tsfadia, STOC 2022, no arXiv recorded.
pointer: Theorem 1.6, restated as Theorem 6.3.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/two-party-dp-complexity.md
corrections: none

## fact-dp-sok-dimension-c
claim: Among about 200 DP variants the computational-power dimension is binary, has essentially one occupant and shows no evidence of practical use.
paper: Desfontaines and Pejó, SoK Differential privacies, PoPETs 2020, no arXiv recorded.
pointer: Definition 21, §9, Table 2, dimension C.
read: recorded, wiki page ingested on 2026-08-20, no stamp. The taxonomy report of 2026-08-05 records dimension C as binary.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md, FS:wiki/sources/sok-differential-privacies.md
corrections: none

## fact-capacity-bounded-dp-function-class
claim: Capacity-bounded DP restricts the adversary to a function class (linear, RKHS, two-layer ReLU) through restricted f-divergences, and it is the nearest published privacy notion to a learning-class adversary.
paper: Chaudhuri, Imola and Machanavajjhala, NeurIPS 2019, arXiv 1907.02159.
pointer: Definition 3, (H, Γ)-capacity bounded privacy. Post-processing holds only under a closure condition, and worked results cover the linear class. The quantitative information flow and maximal-leakage lineages do not cite it.
read: recorded, Definition 3 verified verbatim in the FORMAL_SECURITY sweep of 2026-08-05. The wiki page was ingested on 2026-08-20 with no stamp.
status: verified
record: FS:CLAUDE.md, FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md, FS:wiki/sources/capacity-bounded-dp.md, FS:wiki/concepts/capacity-bounded-privacy.md
corrections: none

## fact-no-ratio-privacy-notion
claim: No fine-grained or ratio-parameterized privacy notion exists in the corpus, since CDP is asymptotic and capacity-bounded DP restricts a class.
paper: none found. The nearest are Mironov et al., CRYPTO 2009, and Chaudhuri, Imola and Machanavajjhala, NeurIPS 2019, arXiv 1907.02159.
pointer: Root CLAUDE.md, seam (b) of the compute-amount sweep.
read: recorded, an absence finding of the 2026-07-26 sweep.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/computational-differential-privacy.md, FS:wiki/sources/capacity-bounded-dp.md
corrections: none

## fact-ldp-equals-sq
claim: A concept class is learnable by a local DP algorithm exactly when it is SQ learnable, and the efficiency transfer needs transparent randomizers (proven).
paper: Kasiviswanathan, Lee, Nissim, Raskhodnikova and Smith, FOCS 2008, no arXiv recorded.
pointer: Abstract, Definition 5.13.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/what-can-we-learn-privately.md, FS:wiki/concepts/local-differential-privacy.md
corrections: none

## fact-hardt-ullman-adaptive-queries-cubic
claim: If one-way functions exist, no efficient oracle holding n samples answers n^{3+o(1)} adaptively chosen statistical queries accurately (proven).
paper: Hardt and Ullman, FOCS 2014, no arXiv recorded.
pointer: Theorem 1.1. Theorem 1.2 is unconditional at dimension n^{3+o(1)}.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/preventing-false-discovery-hard.md
corrections: none

## fact-dswz-dp-space-separation
claim: Assuming symmetric-key encryption secure against non-uniform adversaries, some task needs more space for an efficient computationally private mechanism than for a non-private one, a space bound on the mechanism (proven under that assumption).
paper: Dinur, Stemmer, Woodruff and Zhou, EUROCRYPT 2023, ePrint 2023/171.
pointer: Corollary 3.13 for the DP separation. Theorem 4.1, under one-way functions, for adaptive data analysis.
read: recorded, wiki page ingested on 2026-08-21, no stamp.
status: recorded
record: FS:wiki/sources/dp-adaptive-analysis-bounded-space.md
corrections: none

## fact-dp-attack-bounds-no-compute-axis
claim: The most recent unification of DP attack bounds depends only on the privacy parameters and the adversary's blind success rate, with no computational axis.
paper: Swanberg, Annamalai, Hayes, Balle and Smith, 2026, arXiv 2507.08158. Also Cummings, Hod, Sarathy and Swanberg, 2024, arXiv 2405.01716.
pointer: Swanberg et al. Theorem 3.2 under (ε, 0)-DP, independent priors and a decomposable metric.
read: recorded, wiki pages ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/adversary-aware-dp-bounds.md, FS:wiki/sources/attaxonomy.md
corrections: none

## fact-gibbs-posterior-exponential-mechanism
claim: A Gibbs posterior at temperature T with loss in [0, 1] is the exponential mechanism with ε = 2/T.
paper: none named in the record.
pointer: Not recorded.
read: recorded, stated in the FORMAL_SECURITY AI oracle issue of 2026-10-13 with no source checked.
status: recorded
record: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
corrections: none

## fact-dwork-dp-stability-generalization
claim: Dwork, Feldman, Hardt, Pitassi, Reingold and Roth give the arrow from differential privacy to stability to generalization, of which Chapter 24 records its privacy-is-the-master-modulus statement as the complexity form.
paper: Dwork, Feldman, Hardt, Pitassi, Reingold and Roth, venue not recorded.
pointer: Not recorded.
read: recorded, cited in Chapter 24 message 7 with no check recorded.
status: recorded
record: FS:exp/docs/notes/chapter-24.md
corrections: none

## fact-cebere-final-model-no-gain
claim: With a crafted gradient at every step, releasing only the final model does not improve the privacy guarantee over releasing every iterate.
paper: Cebere, Bellet and Papernot, ICLR 2025.
pointer: Not recorded.
read: recorded, found by an HE-ML search of 2026-10-16, no note written.
status: recorded
record: HE-ML:lib/literature/positioning.md
corrections: none

## fact-mironov-renyi-gaussian-mechanism
claim: Mironov gives the Rényi divergence of the Gaussian mechanism, on which the bounded-deviation transfer of the HE-ML learning-oracle theory rests.
paper: Mironov, IEEE CSF 2017.
pointer: Not recorded.
read: recorded, cited in the prior-work paragraph of the final learning-oracle theory of 2026-10-17, which records no check of the paper.
status: recorded
record: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md
corrections: none

# Learning exponents

## fact-generative-leap-multi-index-rate
claim: For Gaussian multi-index models the generative leap exponent k* gives n = Θ(d^{1∨k*/2}) for index-space recovery, with a low-degree lower bound and a matching efficient upper bound (proven, the lower bound in the low-degree model).
paper: Damian, Lee and Bruna, NeurIPS 2025, arXiv 2506.05500 (DLB25).
pointer: Theorem 1 (low-degree at degree O(log² d), which needs the low-degree conjecture to speak of polynomial time) and Theorem 3 (upper bound with an unquantified constant). games.tex records the constant C(P, K) as conjectured exponentially large in the index dimension. The root reads the generative leap as the unit, dominating the information exponent and the leap.
read: recorded, found 2026-08-20, wiki page ingested from the raw PDF on 2026-08-20 with no stamp.
status: recorded
record: FS:CLAUDE.md, FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/generative-leap-multi-index.md
corrections: none

## fact-leap-bound-csq-only
claim: The Θ̃(d^{max(Leap,2)}) SGD scaling of Abbe et al. is a conjecture, and the proved matching lower bound is CSQ only, d^{Leap} on the hypercube and d^{Leap/2} for Gaussian data.
paper: Abbe, Boix-Adserà and Misiakiewicz, COLT 2023, arXiv 2302.11055.
pointer: Conjecture 1, Proposition 2.
read: recorded, wiki page ingested from the raw PDF on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/leap-complexity-sgd.md
corrections: none

## fact-generative-exponent-measures-detection
claim: The generative-exponent lower bound of Damian et al. measures detection, not estimation, the authors flag a known gap where SQ estimation needs n ≳ d^{k*/2+1} and leave the estimation threshold open, and the low-degree half is conditional on their Conjecture 3.4.
paper: Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, arXiv 2403.05529 (DPLB24).
pointer: Theorem 3.2, Remark 3.3, Conjecture 3.4.
read: recorded, corrected from recovery to detection against the PDF 2026-08-20, no date_verified.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/generative-exponent-single-index.md
corrections:
  - 2026-08-20 The threshold was corrected from recovery to detection.
  - 2026-08-27 The root marks the open estimation threshold superseded in part for polynomial links, see fact-polynomial-link-estimation-rate.

## fact-generative-below-information
claim: The generative exponent never exceeds the information exponent, and the two differ exactly when some square-integrable label transformation lowers the Hermite index (proven).
paper: Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, arXiv 2403.05529 (DPLB24).
pointer: Proposition 2.6.
read: recorded, wiki page ingested from the raw PDF on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/generative-exponent-single-index.md, FS:wiki/concepts/generative-exponent.md
corrections: none

## fact-polynomial-link-kstar-at-most-two
claim: For polynomial links the generative exponent is at most 2, and the same holds for deep networks with an r-dimensional first hidden layer, so large-k* instances are constructions.
paper: Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, arXiv 2403.05529. Damian, Lee and Bruna, NeurIPS 2025, arXiv 2506.05500.
pointer: Not recorded beyond the boundary notes.
read: recorded, boundary notes in raw/SOURCES.md of 2026-08-20.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/generative-exponent-single-index.md, FS:wiki/sources/generative-leap-multi-index.md
corrections: none

## fact-polynomial-link-estimation-rate
claim: For polynomial single-index links, strong recovery with a generalization bound is reached at n = Θ̃(d^{(p*−1)∨1}), governed by the generative exponent p*, and price.tex records this as reuse reaching the information-theoretic rate.
paper: The root CLAUDE.md names Arnaboldi, Ostrovskii, Sun and Wu, arXiv 2406.01581 (NeurIPS 2024). The wiki page and price.tex name Lee, Oko, Suzuki and Wu, NeurIPS 2024 (LOSW24), with no arXiv.
pointer: Abstract and general rate, no theorem number recorded.
read: recorded, wiki page ingested on 2026-08-22, no stamp.
status: disputed, the records name different authors for the rate
record: FS:CLAUDE.md, FS:wiki/sources/sgd-reuse-info-theoretic-limit.md, FS:exp/survey/paper/parked/formalization/price.tex
corrections:
  - 2026-08-27 The root marks its earlier record that the estimation threshold is open as superseded in part by this rate. The supersession is recorded in CLAUDE.md only, not in the wiki log.

## fact-glasgow-xor-linear-samples
claim: Standard minibatch SGD on a two-layer ReLU network learns 2-sparse XOR to small population error in Θ̃(d) samples and iterations (proven).
paper: Glasgow, ICLR 2024, arXiv 2309.15111.
pointer: Theorem 3.1.
read: recorded, wiki page ingested on 2026-08-22, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/sgd-xor-near-optimal.md
corrections: none

## fact-batch-reuse-attains-generative-exponent
claim: Batch reuse does not escape the exponent family but attains the generative exponent in place of the information exponent, because two steps on one minibatch pass the label through the activation's derivative, and the learning rate or a learning-rate schedule selects the regime.
paper: Tsiolis, Mousavi-Hosseini and Erdogdu, NeurIPS 2025, arXiv 2510.21020 (TME25). Dandi, Troiani, Arnaboldi, Pesce, Zdeborová and Krzakala, ICML 2024, arXiv 2402.03220.
pointer: Tsiolis et al. Corollary 4.3, where the plain two-layer case is governed by IE(σ*²) and the generative exponent is reached only through the depth-D extension.
read: recorded, the 2026-08-22 wiki log records the Tsiolis et al. abstract claim verified against Corollary 4.3, and the root records the reading on 2026-08-27.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/paper/parked/formalization/price.tex, FS:wiki/sources/learning-rate-induces-generative-exponent.md, FS:wiki/sources/reusing-batches-breaks-exponents.md
corrections:
  - 2026-08-27 The earlier phrase that batch reuse escapes the exponent barriers was marked too strong.

## fact-dandi-two-step-batch-reuse
claim: Dandi et al. show that two steps on a reused batch learn past the information and leap exponent barriers in the proportional regime, so those barriers are properties of single-pass gradient methods.
paper: Dandi, Troiani, Arnaboldi, Pesce, Zdeborová and Krzakala, ICML 2024, arXiv 2402.03220.
pointer: §1, T = 2 steps at n = αd, second layer frozen at initialization.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/reusing-batches-breaks-exponents.md
corrections:
  - 2026-08-27 The root marks as too strong its earlier record that Dandi et al. escape the barriers.

## fact-information-exponent-one-algorithm
claim: The information exponent prices one algorithm, online SGD from a random start, on rank-one planted models, and says nothing about all efficient algorithms.
paper: Ben Arous, Gheissari and Jagannath, JMLR 2021, arXiv 2003.10409.
pointer: Definition 1.2, Assumptions A and B.
read: recorded, wiki page ingested on 2026-08-20, no stamp. The price.tex record of 2026-08-28 states the same.
status: recorded
record: FS:wiki/sources/information-exponent-online-sgd.md, FS:exp/survey/paper/parked/formalization/price.tex
corrections: none

## fact-full-batch-beats-one-pass
claim: With a truncated quadratic link full-batch gradient descent succeeds at n ≃ d where one-pass SGD with the same activation does not, which price.tex records as a separation by a logarithmic factor for the truncated target and provably none for the plain one (proven).
paper: Kovačević, Ji, Wu, Soltanolkotabi and Mondelli, 2026, arXiv 2602.02431 (KJWSM26).
pointer: Theorems 3.1, 3.2 and 4.1.
read: recorded, wiki page ingested on 2026-08-22, no stamp.
status: recorded
record: FS:wiki/sources/full-batch-gd-vs-one-pass-sgd.md, FS:exp/survey/paper/parked/formalization/price.tex
corrections: none

## fact-merged-staircase-necessary
claim: The merged-staircase property is necessary for O(d)-sample mean-field SGD on sparse hypercube functions, since without it the risk stays bounded below (proven).
paper: Abbe, Boix-Adserà and Misiakiewicz, COLT 2022, arXiv 2202.08658.
pointer: Theorem 7.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/merged-staircase-property.md
corrections: none

## fact-noise-sensitivity-exponent-amp
claim: The noise sensitivity exponent controls the size of AMP gaps in the proportional regime and does not compose with the SQ and low-degree exponents.
paper: Defilippis, Krzakala, Loureiro and Maillard, 2026, arXiv 2603.17896.
pointer: Definition 2.1, Theorem 3.2.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/noise-sensitivity-exponent.md
corrections: none

## fact-robust-single-index-unpriced-adversary
claim: Gaussian single-index models admit an efficient constant-factor agnostic learner at about d^{⌈k*/2⌉} + d/ε samples, and the label-noise adversary in the theorem carries no cost.
paper: Wang, Zarifis, Diakonikolas and Diakonikolas, NeurIPS 2024, no arXiv recorded.
pointer: Theorem 1.2, Assumption 1.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/robust-single-index-efficient.md
corrections: none

## fact-sgd-parity-near-sq-limit
claim: SGD solves (n, k)-sparse parity in about n^{α·k} iterations across the tested grid, an empirical finding for n up to 30 and k up to 4.
paper: Barak, Edelman, Goel, Kakade, Malach and Zhang, NeurIPS 2022, arXiv 2207.08799.
pointer: Empirical Finding 1, Appendix C. Theorems 4, 6 and 7 cover specific schedules.
read: recorded, wiki page ingested on 2026-08-22, no stamp.
status: recorded
record: FS:wiki/sources/hidden-progress-sgd-parities.md
corrections: none

## fact-exponents-zero-security-citers
claim: No security or privacy paper uses the information exponent, the generative exponent, the leap, the generative leap or the noise-sensitivity exponent as the unit of an adversary's cost (empirical, citation sweep).
paper: citation records of Ben Arous, Gheissari and Jagannath, JMLR 2021, arXiv 2003.10409, Abbe et al., COLT 2022 and 2023, arXiv 2202.08658 and 2302.11055, and Damian et al., arXiv 2403.05529 and 2506.05500.
pointer: 514 citation records, zero hits at S&P, USENIX Security, CCS, NDSS, CRYPTO, EUROCRYPT, TCC and PoPETs, 259 unique arXiv citers with exactly one in cs.CR (arXiv 2310.01959, one passing sentence), zero IACR ePrint hits.
read: recorded, empirical sweep re-run adversarially on 2026-08-20, not a PDF check.
status: recorded
record: FS:CLAUDE.md, FS:wiki/analyses/native-asymmetry-in-learning.md, FS:wiki/sources/beyond-labeling-oracles.md
corrections: none

## fact-scaling-laws-recipe-relative
claim: Every neural scaling law in the FORMAL_SECURITY corpus holds for a named training recipe, and the exponent moves when the recipe moves.
paper: Kaplan et al. 2020, arXiv 2001.08361. Hoffmann et al., NeurIPS 2022. Bordelon, Atanasov and Pehlevan, ICLR 2025. Sorscher et al., NeurIPS 2022.
pointer: Kaplan et al. Appendix C (no theory) and Eq. 6.1, N ∝ C^{0.73}. Bordelon et al. abstract, feature learning nearly doubles the hard-task exponent.
read: recorded, wave 6 of raw/SOURCES.md records the boundary notes on 2026-08-22.
status: recorded
record: FS:wiki/sources/scaling-laws-neural-lm.md, FS:wiki/sources/feature-learning-improves-scaling.md, FS:wiki/sources/data-pruning-beats-power-laws.md
corrections:
  - 2026-08-27 The classification rows of Bordelon et al. and Sorscher et al. had each held the next paper's evidence quote, and the quotes were re-extracted.

## fact-chinchilla-approach3-disputed
claim: Chinchilla's Approach 3 fit fails on reconstructed data while equal scaling of parameters and tokens survives, and the original learning-rate-decay explanation of the Kaplan discrepancy was disproved (empirical).
paper: Hoffmann et al., NeurIPS 2022. Besiroglu, Erdil, Barnett and You, 2024, arXiv 2404.10102. Porian et al., NeurIPS 2024, inside the Chinchilla page.
pointer: Limits section of the Chinchilla page.
read: recorded, the Besiroglu et al. page carries a banner verified against raw/Bes24_ChinchillaReplication.pdf on 2026-08-22.
status: verified
record: FS:wiki/sources/chinchilla-compute-optimal.md, FS:wiki/sources/chinchilla-replication.md
corrections: none

## fact-algorithmic-progress-halving-rate
claim: The compute needed to reach a fixed perplexity halved about every 8 months from 2012 to 2023, with a 95 percent interval of about 5 to 14 months (empirical).
paper: Ho, Besiroglu, Erdil et al., NeurIPS 2024, arXiv 2403.05812.
pointer: Abstract.
read: recorded, reclassified against the primary PDF on 2026-09-03 per its cls_reason.
status: verified
record: FS:wiki/sources/algorithmic-progress-lm.md, FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md
corrections:
  - 2026-09-03 The corpus row had been classified against another paper's abstract, the fault of the quote rotation found on 2026-08-27, and it was redone against its PDF.

# Fine-grained and memory-bounded cryptography

## fact-fine-grained-crypto-definitions
claim: Compute amount without hardness is fine-grained cryptography, whose canonical definitions price the inverter at honest^{1+δ} circuit size or name a constant gap δ in word-RAM time.
paper: Brzuska and Couteau, EUROCRYPT 2022 Part II and J. Cryptology 2024 (BC22). LaVigne, Lincoln and Vassilevska Williams, CRYPTO 2019 Part III (LLW19). Ball, Rosen, Sabin and Vasudevan, STOC 2017 (BRSV17).
pointer: BC22 Definition 6, an (ε, δ)-fine-grained OWF against circuits below |f|^{1+δ}. LLW19 Definition 5, the gap as a named object. BRSV17 Definition 2. The wiki records the conversion δ_BC = δ_LLV/(1−δ_LLV).
read: recorded, checked 2026-07-26 per the root. The Ball et al. page carries date_verified 2026-08-22, the other two pages carry no stamp, and raw/SOURCES.md marks the conversion verified.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/fine-grained-one-way-functions.md, FS:wiki/sources/pkc-fine-grained-setting.md, FS:wiki/sources/average-case-fine-grained-hardness.md, FS:wiki/concepts/security-gap-exponent.md
corrections: none

## fact-fine-grained-conventions-incompatible
claim: BC22, LLW19 and BRSV17 use three incompatible conventions, namely non-uniform circuit size with honest^{1+δ}, uniform word-RAM time with T^{1−δ} against T, and uniform word-RAM with the error indexed by the adversary's own discount as well as by n, so BRSV17 Definition 2 is not one number.
paper: Brzuska and Couteau, EUROCRYPT 2022. LaVigne, Lincoln and Vassilevska Williams, CRYPTO 2019. Ball, Rosen, Sabin and Vasudevan, STOC 2017.
pointer: BC22 Definition 6, LLW19 Definition 5, BRSV17 Definition 2.
read: recorded, audit of 2026-08-22.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:exp/survey/paper/parked/formalization/games.tex
corrections: none

## fact-llw19-definition-two-party-relation
claim: LaVigne, Lincoln and Vassilevska Williams Definition 5 is a two-party relation, and a survey dispute of 2026-09-03 says the row should be coded relative.
paper: LaVigne, Lincoln and Vassilevska Williams, CRYPTO 2019 (LLW19).
pointer: Definition 5.
read: recorded, quotation batch of 2026-09-03, dispute not applied.
status: recorded
record: FS:exp/survey/lib/reports/archive/2026-09-03-halil-quotes-batch-b.md
corrections: none

## fact-llv-gap-below-quadratic
claim: The LaVigne, Lincoln and Vassilevska Williams gap is capped strictly below quadratic, at N^{2−4/(k+2)}.
paper: LaVigne, Lincoln and Vassilevska Williams, CRYPTO 2019 (LLW19).
pointer: Boundary note in raw/SOURCES.md.
read: recorded, boundary note of 2026-08-20.
status: recorded
record: FS:wiki/sources/pkc-fine-grained-setting.md
corrections: none

## fact-merkle-ceiling-query-bound
claim: An eavesdropper making (16n/δ)² oracle queries breaks every random-oracle key exchange with n honest queries, a ceiling on query gaps in an idealized model that says nothing about time gaps or structured assumptions (proven).
paper: Barak and Mahmoody-Ghidary, CRYPTO 2009.
pointer: Abstract. The eavesdropper runs efficiently only in a relativized world where P equals NP. The wiki states the bound as O(n²) queries and the root as (16n/δ)².
read: recorded, wiki page date_verified 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/merkle-puzzles-are-optimal.md
corrections:
  - 2026-08-22 The audit lists the earlier record that quadratic is optimal in the ROM as the agent's own error.

## fact-afshar-nike-gap-ceilings
claim: The random-oracle NIKE gap is n^{K/(K−1)} and shrinks as K grows, and 3-NIKE is capped at O(n²) in Maurer's generic group model, all in query complexity (proven).
paper: Afshar, Couteau, Mahmoody and Sadeghi, EUROCRYPT 2023.
pointer: Abstract, Definition 2, Theorem 21.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/fine-grained-nike-lower-bounds.md
corrections: none

## fact-nike-quadratic-standard-model
claim: A 4-party NIKE reaches a quadratic gap in the standard model from exponentially secure injective PRGs and sub-exponential CDH, but only N^{1.6} in Maurer's generic group model (proven).
paper: Bauer, Couteau and Sadeghi, CRYPTO 2024, ePrint 2024/834.
pointer: Theorems 4 and 10.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/fine-grained-nike-revisited.md
corrections: none

## fact-wang-nike-constructions-state-ratios
claim: Two constructions of the NIKE paper the wiki attributes to Wang et al. do state ratios.
paper: Wang et al., page nike-without-idealized-assumptions, venue not recorded.
pointer: Corrected row of raw/SOURCES.md.
read: recorded, filed on 2026-08-20 as post-ingest verification.
status: recorded
record: FS:wiki/sources/nike-without-idealized-assumptions.md
corrections:
  - 2026-08-20 The boundary note was corrected to say that two constructions do state ratios.

## fact-fine-grained-barriers-nseth-pessiland
claim: If one-way functions do not exist, average-case k-SUM and Zero-k-Clique are easy for large constant k on infinitely many n, a barrier the root lists with the NSETH barrier of Ball et al. §5.2 (proven).
paper: Alman, Huang and Yeo, EUROCRYPT 2025. Ball, Rosen, Sabin and Vasudevan, STOC 2017.
pointer: Alman et al. Theorem 1.2. BRSV17 §5.2.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/fine-grained-world-without-crypto.md
corrections: none

## fact-dvv16-infinitely-often
claim: The NC1-side primitives of Degwekar, Vaikuntanathan and Vasudevan hold only infinitely often, and the formal theorems need ⊕L/poly ⊄ NC1 while the abstract states NC1 ≠ ⊕L/poly.
paper: Degwekar, Vaikuntanathan and Vasudevan, CRYPTO 2016, ePrint 2016/580.
pointer: Remark 3.1, Definitions 2.3 to 2.6 and 2.13.
read: recorded, caveats added on 2026-08-20 with Remark 3.1 verified verbatim per raw/SOURCES.md.
status: verified
record: FS:wiki/sources/fine-grained-cryptography.md
corrections: none

## fact-parity-problems-high-success-only
claim: Parity versions of k-OV, k-SUM and k-XOR are n^{Ω(√k)}-hard on average, but only for algorithms with success probability 1 − Θ(2^{−K}) (proven).
paper: Dalirrooyfard, Lincoln, Saha and Vassilevska Williams, SODA 2025, arXiv 2503.21951.
pointer: Theorems 1.1, 1.3, 1.4 and 1.6.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/average-case-parity-problems.md
corrections:
  - 2026-08-20 The boundary note was corrected to say that cryptography is not mentioned in the paper, rather than disclaimed.

## fact-planted-ov-conjectured
claim: Average-case hardness of planted k-OV is a conjecture, not a theorem.
paper: Kühnemann, Polak and Rosen, ESA 2025.
pointer: Conjecture 10.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/planted-orthogonal-vectors.md
corrections: none

## fact-consensus-exponent-ratio
claim: Permissionless consensus resists adversarial power T^{1−ε} against honest power T from the k-OV conjecture, in the random beacon model despite the title's standard model.
paper: Ball, Garay, Hall, Kiayias and Panagiotakos, CRYPTO 2024.
pointer: Abstract, Definition 1, Theorem 23.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/permissionless-consensus-fine-grained.md
corrections: none

## fact-sequential-functions-price-depth
claim: Sequential functions price depth rather than total work, and fine-grained PKE from them needs a VDF and iO for null circuits.
paper: Guan and Montgomery, CRYPTO 2024.
pointer: Definition 3.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/sequential-functions-fine-grained.md
corrections: none

## fact-fine-grained-means-access-control
claim: In the privacy-preserving ML literature fine-grained usually means per-user access control, so a keyword search for fine-grained privacy returns the wrong sense and a search should go by the shape of the definition.
paper: none, a finding about the terminology of the privacy-preserving ML literature.
pointer: Root CLAUDE.md, terminology note.
read: recorded, methodological note of the root CLAUDE.md.
status: recorded
record: FS:CLAUDE.md
corrections: none

## fact-memory-bounded-crypto-mature
claim: Cryptography against memory-bounded adversaries is mature, from Raz's parity bound through Guan and Zhandry to Dodis, Quach and Wichs.
paper: Raz, FOCS 2016, arXiv 1602.05161. Guan and Zhandry, EUROCRYPT 2019. Dodis, Quach and Wichs, EUROCRYPT 2022 and 2023.
pointer: Raz Theorems 1 and 2. Dodis, Quach and Wichs 2023, main result, memory gap up to 2^{O(n)}.
read: recorded, wiki pages ingested from the raw PDFs on 2026-08-21 with post-ingest corrections filed in raw/SOURCES.md, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/raz-parity-time-space.md, FS:wiki/sources/bounded-storage-simple-schemes.md, FS:wiki/sources/speak-much-remember-little.md, FS:wiki/sources/authentication-bounded-storage.md
corrections: none

## fact-raz-theorem-stronger-than-abstract
claim: Raz's parity lower bound holds for any branching program of width 2^{cn²} with c < 1/20 and length 2^{αn}, stronger than the n²/25 of the abstract (proven).
paper: Raz, FOCS 2016, arXiv 1602.05161.
pointer: Theorem 2, Section 7. Remark 1.2 caps the encryption corollary to messages shorter than n.
read: recorded, boundary note in raw/SOURCES.md of 2026-08-20, no date_verified.
status: recorded
record: FS:wiki/sources/raz-parity-time-space.md
corrections: none

## fact-dqw23-bsm-quadratic-ceiling-broken
claim: Bounded-storage key agreement and OT reach adversarial memory up to 2^{O(n)}, because the Dziembowski and Maurer quadratic bound holds only in a more restricted model (proven).
paper: Dodis, Quach and Wichs, EUROCRYPT 2023. The PDF is dated 22 September 2021, and the EUROCRYPT 2023 attribution is not stated in it.
pointer: §1 Main Result, Theorems 7.4 and 7.7 for the lower bounds.
read: recorded, wiki page ingested on 2026-08-21, no stamp.
status: recorded
record: FS:wiki/sources/speak-much-remember-little.md
corrections:
  - 2026-08-20 The venue attribution was flagged as not stated in the PDF.

## fact-dqw22-bsm-signature-optimality
claim: Bounded-storage signatures that are suf-cma-secure force adversarial memory m = O(n²), proved through an explicit memory-bounded forger.
paper: Dodis, Quach and Wichs, EUROCRYPT 2022.
pointer: Theorem 7.11 with Lemma 7.13 of the 2023 paper. MAC short-tag optimality is footnote 4. Raz drives the construction through Theorem 6.2.
read: recorded, correction filed on 2026-08-20 in raw/SOURCES.md, no date_verified.
status: recorded
record: FS:wiki/sources/authentication-bounded-storage.md
corrections:
  - 2026-08-20 The boundary note was corrected to place signature optimality at Theorem 7.11.

## fact-bsm-space-owf-tradeoff
claim: One-way functions give bounded-storage key agreement at any polynomial space gap, and one-way functions are necessary for large space gaps (proven).
paper: Brzuska, Couteau, Egger and Quach, TCC 2024.
pointer: Abstract. Theorem 3 is tight only for single-long-stream protocols, and Theorem 4 yields only non-uniform, infinitely-often one-way functions.
read: recorded, wiki page ingested on 2026-08-21 from a PDF supplied by hand, no stamp.
status: recorded
record: FS:wiki/sources/bsm-key-agreement-owf.md
corrections: none

## fact-kmns21-adaptive-streaming-separation
claim: One streaming problem needs polynomial space for adversarially robust algorithms and polylogarithmic space obliviously, information-theoretically, and the streaming algorithm is the space-bounded party inside the proof (proven).
paper: Kaplan, Mansour, Nissim and Stemmer, CRYPTO 2021, arXiv 2101.10836.
pointer: Theorems 1.2 and 5.10. Remark 1.4 concedes that the more natural §6 variant gives only a computational separation.
read: recorded, wiki page ingested on 2026-08-21, no stamp.
status: recorded
record: FS:wiki/sources/adaptive-vs-oblivious-streaming.md
corrections:
  - 2026-08-20 The boundary note was corrected to say that the streaming algorithm is the space-bounded adversary inside the proof.

## fact-no-memory-bounded-ml-adversary
claim: No security or privacy definition bounds an ML or privacy adversary by memory, since every space bound in the corpus sits on the learner, the mechanism or the defender.
paper: none found. The hits are Raz, FOCS 2016 (learner), Dinur, Stemmer, Woodruff and Zhou, EUROCRYPT 2023 (mechanism), and Kaplan, Mansour, Nissim and Stemmer, CRYPTO 2021 (defender).
pointer: The memory section of raw/SOURCES.md. Raz's §1.3 corollary is the corpus's only attacker-side memory bound, and its attacker is a parity learner against a one-time pad. The survey count of September 2026 finds four memory-bounded adversaries, all in bounded-storage cryptography. The 2026-10-13 sweep did not search this and claims no new negative.
read: recorded, an absence finding of the 2026-08-20 sweep, not a PDF check.
status: recorded
record: FS:CLAUDE.md, FS:exp/survey/lib/claims.yml, FS:exp/survey/lab/results/literature-sweep/information.md, FS:wiki/sources/raz-parity-time-space.md, FS:wiki/sources/dp-adaptive-analysis-bounded-space.md, FS:wiki/sources/adaptive-vs-oblivious-streaming.md
corrections: none

## fact-transformer-rnn-separation-exists
claim: Learning separations between transformers and RNNs are published, and only the memory-sample mechanism is unclaimed.
paper: arXiv 2503.11272, authors not recorded.
pointer: None recorded.
read: recorded, marked single-sourced and unread in the native-asymmetry analysis.
status: recorded
record: FS:CLAUDE.md, FS:wiki/analyses/native-asymmetry-in-learning.md
corrections: none

# Restricted-class attackers and usable information

## fact-restricted-class-attacker-occupied
claim: Modelling the attacker as a restricted-class learner and comparing two tasks is occupied in cryptographic units, and only learning-theory units remain unclaimed.
paper: Canetti and Karchmer, TCC 2021. Karchmer, SaTML 2023, ePrint 2022/1039. Christiano, Hilton, Lecomte and Xu, ITCS 2025, arXiv 2409.03077. arXiv 2504.20310, authors not recorded.
pointer: Not recorded per paper.
read: recorded, the covert-learning and defendability pages carry date_verified 2026-08-20. Karchmer and arXiv 2504.20310 are single-sourced and have no page.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/covert-learning.md, FS:wiki/sources/backdoor-defense-learnability-obfuscation.md, FS:wiki/analyses/native-asymmetry-in-learning.md
corrections: none

## fact-covert-learning-uses-lpn
claim: Covert learning rests on LPN, and the earlier wiki page had invented an LWE assumption and halfspace results for it.
paper: Canetti and Karchmer, TCC 2021, the paper of the covert-learning page.
pointer: Not recorded.
read: recorded, corrected against the PDF 2026-08-20, page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/covert-learning.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-20 The page was corrected from LWE to LPN.
  - 2026-08-22 The audit traces the invented LWE assumption and halfspace results among its fabrications.

## fact-same-units-cell-unclaimed
claim: The theorem shape that prices attacker and defender in the same exponent units at a matched budget, with the attacker restricted to the trainer's algorithm class, is unclaimed, so the question is open only narrowly (empirical, a positioning claim on the citation sweep).
paper: none found. Built on the citation sweep of the exponent papers, see fact-exponents-zero-security-citers.
pointer: Section 3.4 of the native-asymmetry analysis. Song §1.3 item 2 names the bounded-discriminator direction as open.
read: recorded, an empirical sweep that the analysis labels a measurement of margins, not a security proof.
status: recorded
record: FS:CLAUDE.md, FS:wiki/analyses/native-asymmetry-in-learning.md
corrections: none

## fact-song-bounded-discriminators-open
claim: Song names sampling judged by discriminators with bounded compute or memory as an open direction, and notes that a sampler facing only polynomial-time tests could output standard Gaussians, so the lattice gate is on L²-accurate score estimation and not on sampling.
paper: Song, Cryptographic Hardness of Score Estimation, NeurIPS 2024, arXiv 2404.03272.
pointer: Section 1.3, item 2. Section 1.3 is a three-item list titled Future directions with no subsections.
read: recorded, wiki page date_verified 2026-08-22, confirmed verbatim per the root.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/song-cryptographic-hardness-score-estimation.md
corrections:
  - 2026-08-22 The numbering was corrected. The old record cited a subsection §1.3.2, and the paper has no subsections 1.3.1 to 1.3.3.
  - 2026-10-25 The wiki-claims digest finds the body of FS:wiki/analyses/native-asymmetry-in-learning.md still citing §1.3.2 and §1.3.3.

## fact-song-black-box-obstruction-restated
claim: Song states that black-box use of a learned sampler cannot solve Gaussian pancakes, a result restated from Bruna, Regev, Song and Tang under worst-case lattice hardness rather than proved in the paper.
paper: Song, NeurIPS 2024, arXiv 2404.03272.
pointer: Section 1.3, item 3.
read: recorded, wiki page date_verified 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/song-cryptographic-hardness-score-estimation.md
corrections:
  - 2026-08-22 The old record cited §1.3.3 and read the statement as Song's own result.

## fact-song-score-estimation-reduction
claim: Gaussian pancakes reduce in polynomial time to L²-accurate score estimation, so score estimation is hard wherever Gaussian pancakes are hard (proven, unconditional as a reduction).
paper: Song, NeurIPS 2024, arXiv 2404.03272.
pointer: Theorem 3.1.
read: recorded, wiki page date_verified 2026-08-22.
status: verified
record: FS:wiki/sources/song-cryptographic-hardness-score-estimation.md
corrections: none

## fact-xu-usable-information-definition
claim: Xu et al. define V-information relative to a predictive family, which recovers Shannon information when the family holds all predictors and is monotone in the family and zero under independence (proven).
paper: Xu, Zhao, Song, Stewart and Ermon, A Theory of Usable Information under Computational Constraints, ICLR 2020, arXiv 2002.10689.
pointer: Definitions 1 to 3, Propositions 1 and 2.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-xu-data-processing-fails
claim: V-information can grow under computation, so data processing fails for bounded families, which Xu et al. show by an example and not by a theorem.
paper: Xu, Zhao, Song, Stewart and Ermon, ICLR 2020, arXiv 2002.10689.
pointer: Section 3.2.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-xu-estimation-bound
claim: Xu et al. give a PAC bound for estimating V-information from samples through Rademacher complexity (proven).
paper: Xu, Zhao, Song, Stewart and Ermon, ICLR 2020, arXiv 2002.10689.
pointer: Theorem 1.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-xu-usable-information-scope
claim: Xu et al. do not cover the procedure that searches the family, leakage at a fixed attacker sample size, any privacy game, or any lower bound from a hard learning problem.
paper: Xu, Zhao, Song, Stewart and Ermon, ICLR 2020, arXiv 2002.10689.
pointer: Whole paper, as read by the scan.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-mo-layerwise-v-information-leakage
claim: Mo et al. measure V-information from gradients to a property in federated learning, empirically and with no theorem.
paper: Mo, Borovykh, Malekzadeh, Haddadi and Demetriou, Layer-wise Characterization of Latent Information Leakage in Federated Learning, ICLR 2021, arXiv 2010.08762.
pointer: Whole paper, as read by the scan.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-mo-usable-gradient-leakage
claim: Mo and coauthors quantify usable attribute and original information leaking from gradients, empirically and with no lower bound.
paper: Mo and coauthors, Quantifying and Localizing Usable Information Leakage from Neural Network Gradients, arXiv 2105.13929.
pointer: Whole paper, as read by the scan.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-xu-citers-no-other-privacy-paper
claim: Among the 267 papers citing Xu et al. that Semantic Scholar returned, a keyword filter found no privacy or attack paper beyond the two of Mo and coauthors (empirical).
paper: citers of Xu, Zhao, Song, Stewart and Ermon, ICLR 2020.
pointer: Citation sweep of the scan.
read: recorded, absence finding of the 2026-10-25 scan by a reader subagent, a keyword filter over the citers.
status: recorded
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-zhao-class-inference-advantage
claim: Zhao et al. define the inference advantage of an adversary class, and every lower bound in the paper is information-theoretic and none uses the class restriction.
paper: Zhao, Chi, Tian and Gordon, NeurIPS 2020, arXiv 1906.07902.
pointer: Definition 2.2.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-hamm-minimax-filter-defender-gap
claim: Hamm bounds the defender's generalization gap through Rademacher complexity (proven).
paper: Hamm, Minimax Filter, JMLR 18(129), 2017.
pointer: Theorems 1 and 4.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-romanelli-g-vulnerability-estimation
claim: Romanelli et al. give the sample complexity of estimating g-vulnerability, against an unbounded adversary (proven).
paper: Romanelli, Chatzikokolakis, Palamidessi and Piantanida, CCS 2020, arXiv 2005.04399.
pointer: Not recorded in the scan.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-fbleau-bayes-risk-estimation
claim: F-BLEAU estimates the Bayes risk consistently but gives no uniform rate.
paper: Cherubin, Chatzikokolakis and Palamidessi, F-BLEAU, IEEE S&P 2019. The scan gives the venue from recollection.
pointer: Not recorded in the scan.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-instance-encoding-privacy-learnability
claim: Carlini and coauthors reduce privacy of instance encoding to learnability, so either an efficient attack has advantage near one half minus the learner's error or an efficient learner is near perfect (proven).
paper: Carlini and coauthors, Is Private Learning Possible with Instance Encoding?, IEEE S&P 2021, arXiv 2011.05315. The scan gives the venue from recollection.
pointer: Theorems 3 to 5.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-no-hard-learning-attacker-lower-bound
claim: No paper bounds a membership, inversion, attribute or reconstruction attacker from below with a statistical-query lower bound or another hard learning problem (empirical, search-based).
paper: none found.
pointer: Scan, section Learning-complexity lower bounds for privacy attackers, and Verdict 3.
read: recorded, absence finding of the 2026-10-25 scan by a reader subagent, about twelve web searches and a keyword filter over 267 citers of Xu et al.
status: recorded
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-no-mia-hardness-crypto-assumption
claim: No computational hardness result for membership inference or reconstruction under a cryptographic assumption was found, only sample or query complexity results and efficient attacks on shallow networks.
paper: none found.
pointer: Sweep computation.md §4 and information.md §4.
read: recorded, null search of the 2026-10-13 agent sweep.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/computation.md, FS:exp/survey/lab/results/literature-sweep/information.md
corrections: none

## fact-no-class-and-sample-bounded-leakage
claim: No paper bounds leakage in both the attacker's class and its samples with a lower-bound technique (empirical, search-based).
paper: none found. The nearest are Xu et al., ICLR 2020, Zhao et al., NeurIPS 2020, and Haghifam, Smith and Ullman, arXiv 2508.19458.
pointer: Scan, Verdict 3.
read: recorded, absence finding of the 2026-10-25 scan by a reader subagent.
status: recorded
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

# Backdoors and undetectability

## fact-gkvz22-backdoor-scope
claim: Under one-way functions any training procedure admits black-box undetectable backdoors, built from digital signatures, while white-box undetectability is shown only for two training paradigms, random Fourier features under CLWE and random ReLU networks under sparse PCA (proven).
paper: Goldwasser, Kim, Vaikuntanathan and Zamir, arXiv 2204.06974, 2022 (GKVZ22). The FOCS 2022 attribution is not stated in the PDF.
pointer: Theorems 2.1 and 2.2, Section 4.1.
read: recorded, wiki page date_verified 2026-08-20. The oracle draft and the audit of 2026-08-22 record the same scope.
status: verified
record: FS:wiki/sources/planting-undetectable-backdoors.md, FS:exp/survey/paper/parked/formalization/oracle.tex, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-20 The summary had merged the black-box result for any model with the white-box result for random Fourier features into one claim, and the page now separates them.
  - 2026-08-20 The FOCS venue attribution was flagged as not stated in the PDF.

## fact-gkvz-two-threshold-definition
claim: Goldwasser et al.'s backdoor definition carries two thresholds, γ on the input perturbation and β quantizing an output into a bit, and places the win inside a real against ideal difference for a PPT adversary, arguing the absolute form unsatisfiable.
paper: Goldwasser, Kim, Vaikuntanathan and Zamir, FOCS 2022 as the programme records it (GKVZ22).
pointer: Definitions 4.1, 4.2, 4.6 and 4.7, Remark 4.8.
read: recorded, verified verbatim in the FORMAL_SECURITY sweep of 2026-08-05.
status: verified
record: FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md
corrections: none

## fact-kalavasis-io-backdoors-scope
claim: Any training pipeline followed by an iO step admits an undetectable backdoor, nothing follows for models released in the clear, and the authors state that Goldwasser et al. leave the white-box question open, which is why they assume obfuscation.
paper: Kalavasis, Karbasi, Oikonomou, Sotiraki, Velegkas and Zampetakis, NeurIPS 2024, arXiv 2406.05660.
pointer: Definitions 2.1 and 2.3, Assumption 2.7.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/io-undetectable-backdoors-nn.md, FS:exp/survey/paper/parked/formalization/oracle.tex
corrections:
  - 2026-08-20 The page was corrected. The paper does not claim to close the white-box gap of Goldwasser et al. or to be more general, and the post-quantum remark belongs to a cited construction.

## fact-draguns-unelicitable-no-theorem
claim: Unelicitable transformer backdoors rest on a hash-based digital locker and SHA-2 preimage resistance, the paper contains no theorem, and the authors state that unelicitability is not white-box undetectability.
paper: Draguns, Gritsevskiy, Motwani, Rogers-Smith, Ladish and Schroeder de Witt, NeurIPS 2024, arXiv 2406.02619.
pointer: §1 and the construction section.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/unelicitable-backdoors-lms.md, FS:exp/survey/paper/parked/formalization/oracle.tex
corrections:
  - 2026-08-20 The construction was corrected. The trigger uses a hash-based digital locker, and no signature scheme appears in the paper.

## fact-oblivious-backdoor-removal
claim: Backdoors can be removed without being detected when the ground truth is close to a Fourier-heavy function or to a low-degree polynomial (proven).
paper: Goldwasser, Shafer, Vafa and Vaikuntanathan, STOC 2025. The compass artifact gives arXiv 2411.03279.
pointer: Definition 4.1, Theorem 6.3 (global), Theorems 7.1, 7.7 and 7.12 (local).
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/oblivious-defense-backdoor-removal.md
corrections: none

## fact-chlx25-defendability-characterization
claim: A class is statistically ε-defendable exactly when ε = o(1/VC), with best confidence max(1/2, 1 − Θ(VC(F)ε)), efficient defendability separates from efficient learnability in the random oracle model, and polynomial-size circuits are not efficiently defendable under one-way functions and iO (proven).
paper: Christiano, Hilton, Lecomte and Xu, ITCS 2025, arXiv 2409.03077 (CHLX25).
pointer: Definition 3.1 (ε-defendability), Theorem 4.1, Theorem 5.3 (random oracle setting), Definition 5.1, Theorem 5.5. Theorem 6.1 makes polynomial-size decision trees uniform-defendable with zero example-oracle calls.
read: recorded, wiki page date_verified 2026-08-20. An agent of the 2026-10-13 sweep read the same results.
status: verified
record: FS:wiki/sources/backdoor-defense-learnability-obfuscation.md, FS:exp/survey/lab/results/literature-sweep/definitions.md
corrections:
  - 2026-08-20 Theorem labels and the random-oracle setting of Theorem 5.3 were corrected against the PDF.

## fact-ball-filter-impossibility-existential
claim: There exist LLMs for which no efficient prompt filter separates harmful from benign prompts, the result is existential, and nothing is proved about deployed models.
paper: Ball, Gluch, Goldwasser, Kreuter, Reingold and Rothblum, ICLR 2026, arXiv 2507.07341.
pointer: Theorem 1 (time-lock puzzles, needing the filter to run no faster than the model it audits, a ratio between two parties' compute left as a side condition), Theorem 2 (one-way functions plus a secret shared by the LLM and the attacker), Theorem 3 (PKE), Theorem 7 in Appendix C.1 as the formal version. The paper does not say that every judge must match the complexity of its predicate, and Villa et al. discuss the result rather than prove it.
read: recorded, wiki page date_verified 2026-08-20, audited 2026-08-20 in the spine report.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-20-halil-lit-survey-spine.md, FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/filter-impossibility-ai-alignment.md
corrections:
  - 2026-08-20 The page was restated as existential, removing a universal reading and a regulatory conclusion drawn from it.

## fact-statistically-undetectable-backdoors-attribution
claim: The Statistically Undetectable Backdoors document in raw/ was anonymous under ICLR 2026 double-blind review, so its attribution to Bogdanov and Rosen was an inferred de-anonymization.
paper: Statistically Undetectable Backdoors, listed by the 2026-10-13 sweep as BRV26 at ICML 2026.
pointer: Not recorded.
read: recorded, audited 2026-08-20 in the spine report.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-20-halil-lit-survey-spine.md, FS:exp/survey/lab/results/literature-sweep/computation.md
corrections: none

## fact-kp-poisoning-multiplicative
claim: The (k, p)-poisoning bound is multiplicative, taking µ to µ^{1−pk/m}, and not the additive Ω(kp/m) the wiki first wrote (proven).
paper: Mahloujifar, Mahmoody and Mohammed, ICML 2019, arXiv 1809.03474.
pointer: Abstract.
read: recorded, corrected against the PDF on 2026-04-23, page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/multi-party-poisoning.md, FS:wiki/concepts/k-p-poisoning-model.md, FS:wiki/concepts/poisoning-attacks.md
corrections:
  - 2026-04-23 The bound was corrected. The old wording gave the additive Ω(kp/m).

# Robustness and concentration

## fact-bpr-sq-separation-defender-fails
claim: A task exists that is efficiently learnable non-robustly but not robustly by any SQ algorithm, so the separation constrains the defender, not the attacker, and it uses no cryptographic assumption (proven, unconditional in the SQ model).
paper: Bubeck, Price and Razenshteyn, ICML 2019, no arXiv recorded (BPR).
pointer: Theorem 1.1, existential over a constructed planted moment-matching task.
read: recorded, wiki page date_verified 2026-08-20, audit of 2026-08-22.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/adversarial-examples-computational-constraints.md
corrections:
  - 2026-08-20 The page was corrected. The paper uses no cryptographic assumption and no PRF, and the Ω(√d) sample separation belongs to Schmidt et al.
  - 2026-08-22 The audit records that the wiki had inverted the relation between this paper and Bubeck, Lee, Price and Razenshteyn.
  - 2026-09-03 The venue was confirmed as ICML 2019, after a mined arXiv lead proved a coincidental string match.

## fact-bpr-robust-classifier-few-samples
claim: The secondary statistical result of Bubeck, Price and Razenshteyn says that a robust classifier, if one exists, is found from relatively few samples (proven).
paper: Bubeck, Price and Razenshteyn, ICML 2019 (BPR).
pointer: The secondary result, proved by a union bound over a net of robust classifiers.
read: recorded, corrected against the PDF 2026-08-20.
status: verified
record: FS:wiki/sources/adversarial-examples-computational-constraints.md
corrections: none

## fact-blpr-quadratic-residuosity
claim: Robust learning of the Bubeck, Lee, Price and Razenshteyn family is hard under quadratic residuosity through the Blum-Blum-Shub trapdoor PRG, not under one-way functions in general, and the paper states no exponential separation.
paper: Bubeck, Lee, Price and Razenshteyn, 2018, arXiv 1811.06418 (BLPR).
pointer: §3 property (c), restating Theorem 3.1.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/adversarial-examples-prg.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-20 The assumption was corrected from one-way functions to quadratic residuosity, and the exponential separation was removed.

## fact-schmidt-gap-simple-data-model
claim: Schmidt et al. show an information-theoretic √d sample gap for robust generalization only in a simple natural data model, and the gap holds for linear classifiers while a slightly nonlinear thresholding classifier recovers the smaller sample complexity.
paper: Schmidt et al., NeurIPS 2018.
pointer: Not recorded.
read: recorded, audit of 2026-08-22 against the source.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-22 The audit restored the qualifier "already in a simple natural data model", which the wiki had deleted.

## fact-gjmm20-computational-robustness
claim: There are constructed tasks whose classifiers are robust only against polynomial-time adversaries, from one-way functions through one-time signatures (proven).
paper: Garg, Jha, Mahloujifar and Mahmoody, ALT 2020 (GJMM20), no arXiv recorded.
pointer: Theorems 8 and 14 on Constructions 7 and 13. Theorem 18 is the universal converse.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/computational-hardness-robust-learning.md
corrections:
  - 2026-09-03 The venue was resolved as ALT 2020, in FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md.

## fact-parameters-from-computational-constraints
claim: On constructed tasks, computationally bounded learners need more model parameters than information requires, assuming one-way functions (proven).
paper: Garg, Jha, Mahloujifar, Mahmoody and Wang, NeurIPS 2022, no arXiv recorded.
pointer: Claims 24 and 26, Definition 2.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/overparameterization-computational-constraints.md
corrections: none

## fact-win-win-is-an-implication
claim: If an efficient robust classifier exists for a task but cannot be learned efficiently, one-way functions exist, and the converse licenses nothing about which tasks are hard (proven).
paper: Degwekar, Nakkiran and Vaikuntanathan, COLT 2019, arXiv 1902.01086.
pointer: Theorem 2.4 (informal), Section 2.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/win-win-robust-learning.md
corrections:
  - 2026-08-20 An invalid inference was removed, since believing one-way functions exist says nothing about which tasks are hard.

## fact-curse-concentration-hypothesis-not-binding
claim: The curse-of-concentration vulnerability theorem holds conditional on metric concentration, and the same group measured that hypothesis and found it does not bind usefully on image benchmarks (empirical for the measurement).
paper: Mahloujifar, Diochnos and Mahmoody, AAAI 2019, arXiv 1809.03063. Mahloujifar, Zhang, Mahmoody and Evans, NeurIPS 2019, arXiv 1905.12202.
pointer: Theorem 1.1 and the Limits section. On CIFAR-10 at ε∞ = 8/255 the concentration estimate is 29.21 percent against a reported 52.96 percent attack success.
read: recorded, the 2019 measurement page carries date_verified 2026-08-20, audited 2026-08-20 in the spine report.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-20-halil-lit-survey-spine.md, FS:wiki/sources/curse-of-concentration.md, FS:wiki/sources/empirically-measuring-concentration.md
corrections:
  - 2026-08-20 A Limits section was added to the curse-of-concentration page, recording that its hypothesis does not bind on image benchmarks.

## fact-two-senses-of-concentration
claim: Concentration names opposite properties in two literatures, metric concentration that forbids robust classifiers and small-volume concentration that permits them, and the second sense is used to prove robust classifiers exist.
paper: Pal, Sulam and Vidal, NeurIPS 2023, against Mahloujifar et al. 2019. The spine report cites arXiv 2309.16096 for the opposite sense, and no record links that identifier to the authors.
pointer: Pal et al. Theorems 2.1 and 3.1.
read: recorded, wiki page ingested on 2026-08-20 with no stamp, audited 2026-08-20 in the spine report.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-20-halil-lit-survey-spine.md, FS:wiki/concepts/two-senses-of-concentration.md, FS:wiki/sources/data-concentration-robustness-avoidable.md
corrections:
  - 2026-08-20 The Limits section of the curse-of-concentration page records that concentration names two opposite properties.

## fact-bubeck-sellke-smooth-interpolation
claim: The universal law of robustness prices smooth interpolation below the noise level under isoperimetry at about nd parameters, the authors do write that overparametrization is necessary to interpolate smoothly, and the theorem contains no adversary.
paper: Bubeck and Sellke, NeurIPS 2021, arXiv 2105.12806.
pointer: Abstract, and the statement in the introduction preceding the main theorem. The theorem concerns smooth interpolation with a bounded Lipschitz constant, not resistance to an adversary.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:wiki/sources/universal-law-of-robustness.md
corrections:
  - 2026-08-20 The audit's charge that Bubeck and Sellke never state that overparametrization is necessary was withdrawn on re-audit, because the first search used the spelling overparameterization. The 2026-08-20 wiki log entry still carries the original charge.

## fact-robust-pac-characterized
claim: The global one-inclusion dimension characterizes agnostic robust PAC learnability up to log factors, and VC classes are robustly learnable only improperly (proven).
paper: Montasser, Hanneke and Srebro, NeurIPS 2022 and COLT 2019.
pointer: 2022 paper §6 near Theorem 9. 2019 paper §1 main results.
read: recorded, date_verified 2026-08-20 on both pages.
status: verified
record: FS:wiki/sources/robust-pac-learning-characterization.md, FS:wiki/sources/vc-classes-adversarially-robustly-learnable.md
corrections: none

## fact-chapter-24-robust-pac-attribution
claim: Chapter 24 states that the statistical value of the robust-learning game is finite exactly when the robust-PAC dimension is finite, citing Montasser, Hanneke and Srebro 2019.
paper: Montasser, Hanneke and Srebro, COLT 2019, as Chapter 24 cites it.
pointer: Chapter 24 message 20, about line 2993.
read: recorded, cited in Chapter 24 with no check recorded. The verified wiki pages attribute the characterization to the 2022 paper, see fact-robust-pac-characterized.
status: recorded
record: FS:exp/docs/notes/chapter-24.md
corrections: none

## fact-randomized-smoothing-radius
claim: Gaussian smoothing certifies an ℓ₂ radius around each input for every base classifier, with no hardness assumption (proven).
paper: Cohen, Rosenfeld and Kolter, ICML 2019, arXiv 1902.02918.
pointer: Theorem 1.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/certified-robustness-randomized-smoothing.md
corrections: none

## fact-pixeldp-one-sided-bound
claim: The PixelDP certified-robustness bound is one-sided, as the corrected wiki page records.
paper: PixelDP, page certified-robustness-differential-privacy, authors and venue not recorded in the digests.
pointer: Not recorded.
read: recorded, corrected against the PDF 2026-08-20, page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/certified-robustness-differential-privacy.md
corrections:
  - 2026-08-20 The page was corrected to state a one-sided bound.

## fact-fawzi-human-vision-robust
claim: Fawzi et al. wrote that the human visual system is inherently robust, and the wiki had reversed the statement.
paper: Fawzi et al., venue not recorded.
pointer: Not recorded.
read: recorded, audit of 2026-08-22.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-22 The audit corrected the reversed statement.

## fact-gilmer-quote-altered
claim: Gilmer et al. do write that they hypothesize the behaviour comes from the high-dimensional geometry of the data manifold, and the wiki's version altered that sentence rather than inventing it.
paper: Gilmer et al., ICLR Workshop 2018.
pointer: Not recorded.
read: recorded, re-audit recorded in the root CLAUDE.md on 2026-08-20.
status: verified
record: FS:CLAUDE.md, FS:wiki/sources/adversarial-spheres.md
corrections:
  - 2026-08-20 The earlier charge that the quote was invented was narrowed to an altered sentence.

## fact-geometry-cluster-prices-nobody
claim: Of 18 concentration and robust-PAC papers, eleven constrain nobody or only the learner in samples, three price an adversary, and Diakonikolas et al. make the defender the polynomial-time party.
paper: the 18 papers of the concentration and robust-PAC cluster of the FORMAL_SECURITY corpus.
pointer: Audit §4.
read: recorded, audit finding of 2026-08-22.
status: recorded
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections: none

## fact-evaluation-checklist-rejects-compute
claim: Carlini et al.'s robustness-evaluation checklist holds that attacker computation is not a reasonable threat-model parameter, a considered position matching the practice of Athalye, Carlini and Wagner.
paper: Carlini, Athalye, Papernot, Brendel, Rauber, Tsipras, Goodfellow, Madry and Kurakin, On Evaluating Adversarial Robustness, 2019, arXiv 1902.06705, a preprint never published. Athalye, Carlini and Wagner, ICML 2018.
pointer: Boundary note in raw/SOURCES.md. The page cites §2.2.2 for the worst-case loss definition.
read: recorded, quotation verified and recorded 2026-08-22 in the survey draft. The wiki page was ingested on 2026-08-20 with no stamp.
status: verified
record: FS:exp/survey/paper/sections/07-findings.tex, FS:wiki/sources/on-evaluating-adversarial-robustness.md
corrections: none

## fact-suya-runtime-equalizing-factor
claim: Suya et al. survey 164 black-box attacks and re-run 11 transfer attacks under a fixed per-batch time budget, recommending runtime as the equalizing factor (empirical).
paper: Suya et al., IEEE SaTML 2024.
pointer: Not recorded.
read: recorded, cited in the survey draft section 07-findings.tex.
status: recorded
record: FS:exp/survey/paper/sections/07-findings.tex
corrections:
  - 2026-09-03 The draft's earlier statement that they re-ran 164 attacks was corrected, round-two report item M6.

# Extraction, proof of learning and unlearning

## fact-jagielski-extraction-query-bounds
claim: A constructed family of width-3k depth-2 ReLU networks needs Θ(p^k) queries to extract, functionally equivalent extraction is NP-hard, and SQ-expressible fidelity extraction of depth-h random networks needs exp(O(h)) samples, imported from Das et al., with gradient descent and PCA noted as such algorithms (proven).
paper: Jagielski, Carlini, Berthelot, Kurakin and Papernot, USENIX Security 2020, arXiv 1909.01838 (JCBKP20), importing Das, Gollapudi, Kumar and Panigrahy, SODA 2020, arXiv 1904.03866.
pointer: Theorems 1, 2 and 3. Das et al. Theorem 16. games.tex records that any novelty claim on extraction priced by algorithm class must be stated against Theorem 3.
read: recorded, Jagielski page date_verified 2026-08-20, and the Das et al. page carries a banner verified against the primary PDF on 2026-08-20.
status: verified
record: FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/jagielski-model-extraction.md, FS:wiki/sources/learnability-deep-random-networks.md
corrections:
  - 2026-08-20 The Jagielski page was rebuilt from its PDF, recovering a missing SQ sample lower bound.

## fact-extraction-success-undefined
claim: The model-extraction literature has no formal definition of a successful attack, as Shafran et al. state from inside the field, scoped to accuracy-driven extraction.
paper: Shafran, Shumailov, Erdogdu and Papernot, Beyond Labeling Oracles, TMLR 2024, arXiv 2310.01959.
pointer: Section 3.2, p. 3.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/beyond-labeling-oracles.md
corrections:
  - 2026-09-03 The venue was corrected to TMLR 2024, in FS:exp/survey/lib/reports/archive/2026-09-03-halil-review-survey-round-2.md.

## fact-no-tight-extraction-query-bound
claim: No tight information-theoretic query lower bound for extracting a trained network to a stated fidelity was found.
paper: none found.
pointer: Sweep computation.md §4 and information.md §4.
read: recorded, null search of the 2026-10-13 agent sweep.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/computation.md, FS:exp/survey/lab/results/literature-sweep/information.md
corrections: none

## fact-dziedzic-extraction-proof-of-work
claim: Dziedzic et al. charge extraction compute through a proof-of-work puzzle, under 2x slowdown for legitimate users and up to 100x for attackers, with no definition and no theorem (empirical).
paper: Dziedzic, Kaleem, Lu and Papernot, ICLR 2022.
pointer: Not recorded.
read: recorded, games.tex of 2026-08-22, no verification recorded.
status: recorded
record: FS:exp/survey/paper/parked/formalization/games.tex
corrections: none

## fact-active-learning-is-extraction
claim: Chandrasekaran et al. put the query budget inside the extraction definition and observe that a query-synthesis active learner is an extraction adversary, so complexity travels in the upper-bound direction only, and the converse is neither proved nor claimed.
paper: Chandrasekaran, Chaudhuri, Giacomelli, Jha and Yan, USENIX Security 2020, arXiv 1811.02054.
pointer: Observation 1, Definition 3, Experiment 1 in §3.1, Proposition 1.
read: recorded, correction filed on 2026-08-20 in raw/SOURCES.md, games.tex of 2026-08-22.
status: recorded
record: FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/active-learning-model-extraction.md
corrections:
  - 2026-08-20 A correction was filed in raw/SOURCES.md, recording that the definition lower-bounds one adversary rather than upper-bounding all.

## fact-cjm20-cryptanalytic-extraction-cost
claim: Carlini, Jagielski and Mironov recover ReLU parameters with polynomially many queries and work exponential in width for sign recovery, extracting a 100,000-parameter MNIST network with 2^{21.5} queries to worst-case error 2^{−25}, an empirical cost with no lower bound.
paper: Carlini, Jagielski and Mironov, CRYPTO 2020.
pointer: Abstract, p. 1.
read: recorded, wiki page ingested on 2026-08-21, no stamp.
status: recorded
record: FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/cryptanalytic-extraction-nn.md
corrections:
  - 2026-09-03 The venue was resolved as CRYPTO 2020, in FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md.

## fact-polytime-cryptanalytic-extraction
claim: Canales-Martínez et al. make cryptanalytic extraction polynomial time, polynomial in depth, assuming infinite-precision arithmetic, and the paper never reports the attacked model's training cost, so the ratio of attack to training cannot be computed from it.
paper: Canales-Martínez, Chávez-Saab, Hambitzer, Rodríguez-Henríquez, Satpute and Shamir, EUROCRYPT 2024.
pointer: Abstract, §5.3. The attack cost is stated as 30 minutes on 256 cores and as 32 minutes for the same network.
read: recorded, correction filed on 2026-08-20 in raw/SOURCES.md.
status: recorded
record: FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/polynomial-time-cryptanalytic-extraction.md
corrections:
  - 2026-08-20 A correction was filed in raw/SOURCES.md.

## fact-hard-label-polytime-extraction
claim: A hard-label polynomial version of cryptanalytic extraction exists.
paper: CCH+26, J. Cryptology 2026.
pointer: Abstract only.
read: abstract, recorded from its abstract by the 2026-10-13 sweep.
status: recorded
record: FS:exp/survey/paper/parked/formalization/oracle.tex, FS:exp/survey/lab/results/literature-sweep/computation.md
corrections: none

## fact-pol-bare-cost-inequalities
claim: Proof-of-learning compares spoofing to honest training only through bare cost inequalities stated as desiderata, E[C_A] ≥ E[C_T], never parameterized by δ and with no adversary class, and the paper cites neither BRSV nor LLW.
paper: Jia, Yaghini, Choquette-Choo, Dullerud, Thudi, Chandrasekaran and Papernot, IEEE S&P 2021, no arXiv recorded.
pointer: Property 2 and Definition 2 (spoof threshold) for the spoofer, Conjecture 1 unproved. The root calls the verification-against-training inequality Property 1, while the wiki page calls it Proposition 1 (verifier cost at most trainer cost).
read: recorded, wiki page date_verified 2026-08-20, rebuilt from the PDF.
status: disputed, the records give the verification inequality different labels
record: FS:CLAUDE.md, FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/proof-of-learning.md
corrections:
  - 2026-08-20 The page was rebuilt from its PDF, recovering two of three compute inequalities.

## fact-pol-ratio-never-exponent-indexed
claim: Work after proof-of-learning indexes the spoofer-to-trainer ratio by a multiplicative constant or by efficiency and hardness parameters, and no work indexes it by an exponent.
paper: Zhao, Fang, Wang, Chen, Su, Xiao and Zhou, 2026, arXiv 2404.09005 (ZFWCSXZ26, called Fang et al. in the root). Shavit, 2023, arXiv 2303.11341 (Sha23).
pointer: Root CLAUDE.md, two seams of 2026-07-26, and games.tex Section What is already occupied.
read: recorded, an absence finding of the 2026-07-26 sweep.
status: recorded
record: FS:CLAUDE.md, FS:exp/survey/paper/parked/formalization/games.tex
corrections: none

## fact-pol-incentive-game-theoretic
claim: Incentive-secure proof-of-learning gives game-theoretic guarantees for rational provers under the assumption that dishonest epochs cost nothing, and indexes the cost ratio by a multiplicative constant.
paper: Zhao, Fang, Wang, Chen, Su, Xiao and Zhou, 2026, arXiv 2404.09005 (ZFWCSXZ26).
pointer: §3.3, Theorem 6.6.
read: recorded, the page carries a banner verified against the primary PDF on 2026-08-20, while raw/SOURCES.md still marks the theorem content unverified.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/pol-incentive-security.md
corrections: none

## fact-shavit-compute-monitoring-no-hard-scheme
claim: Compute monitoring defines an F-hardness clause for spoofers bounded in time, but no proof scheme is exhibited or proved F-hard.
paper: Shavit, 2023, arXiv 2303.11341 (Sha23).
pointer: Definition 1, Theorem 1 in Appendix C.2.
read: recorded, banner verified against raw/S23_CatchAChinchilla.pdf on 2026-08-20.
status: verified
record: FS:wiki/sources/catch-a-chinchilla-compute-monitoring.md
corrections: none

## fact-pol-forgeries-fang-2023
claim: Proof-of-learning's Property 2 fails against the stated verification parameters, since forgeries succeed against the verifier's lossy view of the trace without paying the walk, and the attacks are constructions, not lower bounds.
paper: Fang et al., IEEE EuroS&P 2023 (FJTYCDCP23).
pointer: Appendix B, Lemmas 1 to 6.
read: recorded, banner verified against raw/F+23_PoLMoreBroken.pdf on 2026-08-20.
status: verified
record: FS:exp/survey/paper/parked/formalization/price.tex, FS:wiki/sources/pol-more-broken.md
corrections: none

## fact-pol-exact-reproduction-out-of-reach
claim: Exact reproduction of a training trace remains empirically out of reach.
paper: SHKBL25, authors and venue not recorded in the digests.
pointer: Not recorded.
read: recorded, price.tex of 2026-08-22.
status: recorded
record: FS:exp/survey/paper/parked/formalization/price.tex
corrections: none

## fact-polo-measured-ratio
claim: Forging PoLO costs 1.1 to 4 times honest proof generation, a measured ratio with no definition, exponent or game (empirical).
paper: Deng, Jiang, Yu, Wang, Wang, Ma, Ni and Liu, 2026, arXiv 2505.12296.
pointer: Abstract.
read: recorded, banner verified against raw/DJY+25_PoLO.pdf on 2026-08-20.
status: verified
record: FS:wiki/sources/polo-proof-of-learning-ownership.md
corrections: none

## fact-zhang-pol-spoofs
claim: Zhang et al. give spoofs of proof-of-learning, which the HE-ML replay audit cites as its motivation for deriving the seed from a random oracle.
paper: Zhang et al., IEEE S&P 2022.
pointer: Not recorded.
read: recorded, cited in the prior-work paragraph of the final learning-oracle theory of 2026-10-17, which records no check of the paper.
status: recorded
record: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md
corrections: none

## fact-unlearning-algorithm-level
claim: Forging adversaries exist for mean-sampler update rules, so unlearning is well defined only at the level of the algorithm (proven).
paper: Thudi, Jia, Shumailov and Papernot, USENIX Security 2022.
pointer: Theorem 3 (Existence of Forging Adversary), Corollary 2.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/auditable-unlearning-definitions.md
corrections: none

## fact-retrain-equivalence-ill-posed
claim: Retrain equivalence is ill-posed for local, path-oblivious unlearning when staged training leaves an order trace in the weights.
paper: Yu, He, Goyal and Arora, 2025, arXiv 2510.16629.
pointer: Definitions 2.1 and 2.2.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/impossibility-retrain-equivalence.md
corrections: none

## fact-unlearning-verification-fragile
claim: A model provider who controls mini-batch sampling can pass backdoor and reproducing verification of unlearning while keeping the information, with an attack that costs as much as naive retraining.
paper: Zhang, Chen, Shen and Li, ICML 2024, arXiv 2408.00929.
pointer: Proposition 4.5, Algorithms 1 and 2.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:wiki/sources/unlearning-verification-fragile.md
corrections: none

## fact-repudiation-rests-on-conjecture
claim: Proof of repudiation against membership claims rests on an unproved conjecture that nearby parameters give membership-equivalent models.
paper: Kong, Roy Chowdhury and Chaudhuri, 2023, arXiv 2303.03648.
pointer: Definitions 4 and 5, Conjecture 1, Theorem 1.
read: recorded, wiki page ingested on 2026-08-20, no stamp.
status: recorded
record: FS:CLAUDE.md, FS:wiki/sources/forgeability-and-unlearning.md
corrections: none

## fact-no-unlearning-verification-hardness
claim: No peer-reviewed theorem that verifying unlearning is hard or impossible was found.
paper: none found.
pointer: Sweep computation.md §4 and information.md §4.
read: recorded, null search of the 2026-10-13 agent sweep.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/computation.md, FS:exp/survey/lab/results/literature-sweep/information.md
corrections: none

## fact-lex26-extraction-indistinguishability-incomparable
claim: Liu, Evans and Xiong are recorded as stating extraction as at least 2^b expected queries and proving indistinguishability and extractability incomparable.
paper: Liu, Evans and Xiong, IEEE S&P 2026 (LEX26).
pointer: Not recorded.
read: recorded, agent sheet of the 2026-10-13 sweep, not read.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/definitions.md
corrections: none

## fact-gg25-gtnp25-two-party-gaps
claim: GG25 and GTNP25 are recorded as stating two-party gaps in samples, time and circuit size.
paper: GG25 and GTNP25, authors and venues not recorded in the digests.
pointer: Not recorded.
read: recorded, agent sheet of the 2026-10-13 sweep, not read.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/definitions.md
corrections: none

## fact-agk22-detection-generation-exponential
claim: Distinguishing and likelihood improvement for learned distributions reduce to each other both ways only at exponential cost in general, the polynomial-time reduction runs one way in a next-token model, no distinguisher carries a class or runtime bound, and the paper does not frame the result as security.
paper: Alvarez-Melis, Garg and Kalai, Are GANs overkill for NLP?, NeurIPS 2022, arXiv 2205.09838.
pointer: §5 Lemmas 1 and 2 (both directions without polynomial time), §6 and Algorithm 1 (one direction, converting a next-token distinguisher into a likelihood improvement). All quantities are empirical on a fixed sample. The root says Lemma 2 needs common support, while the wiki page says it needs a bounded likelihood ratio.
read: recorded, corrected against the PDF 2026-08-22, wiki page date_verified 2026-08-22 against raw/AGK22_AreGANsOverkillNLP.pdf.
status: disputed, the records state different hypotheses for Lemma 2
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md, FS:exp/survey/paper/parked/formalization/games.tex, FS:wiki/sources/are-gans-overkill-for-nlp.md
corrections:
  - 2026-08-22 The earlier note was wrong on two of four points. It read the equivalence as polynomial and two-way against a bounded distinguisher class.
  - 2026-10-25 The wiki-claims digest finds FS:raw/SOURCES.md still describing both directions against a bounded distinguisher class, and the native-asymmetry analysis carrying the old reading with an in-place correction note.

# Criteria, taxonomies and unified definitions

## fact-alvim-binary-gain-function
claim: A success criterion R with a {0,1} codomain is a binary gain function, a named subfamily with a structure theorem whose worked cases (exact match, tolerance balls, k-tries, partitions) match the programme's, so the novelty of R is withdrawn.
paper: Alvim, Chatzikokolakis, Palamidessi and Smith, IEEE CSF 2012.
pointer: Definitions 3.1 to 3.6, Definition 3.6 for the binary family. Footnote 3 calls the codomain immaterial.
read: recorded, verified verbatim in the FORMAL_SECURITY sweep of 2026-08-05.
status: verified
record: FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md
corrections: none

## fact-clarkson-schneider-integrity-dual
claim: Clarkson and Schneider unify confidentiality and integrity, with contamination as the Biba dual of leakage and suppression as reference against candidate, suppression having no confidentiality dual, so the programme's unification claim is withdrawn.
paper: Clarkson and Schneider, IEEE CSF 2010.
pointer: The measures and Proposition 1. Footnote 5 states that information-theoretic quantification ignores computational constraints on attackers.
read: recorded, verified verbatim in the FORMAL_SECURITY sweep of 2026-08-05.
status: verified
record: FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md, FS:exp/docs/reports/2026-08-05-unfiled-leakage-and-integrity-functions.md
corrections: none

## fact-bellare-sahai-relation-eliminable
claim: Bellare and Sahai reduce non-malleability over polynomial-time relations to indistinguishability under parallel chosen-ciphertext attack with queries one fewer than the arity, so a security definition built on a quantified success relation was proved eliminable (proven).
paper: Bellare and Sahai, CRYPTO 1999.
pointer: Definitions 3.1 and 3.2 and the elimination passage. The programme's answer, that a fixed R with a varying budget leaves no such trade, is a conjecture and open.
read: recorded, verified verbatim in the FORMAL_SECURITY sweep of 2026-08-05.
status: verified
record: FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md
corrections: none

## fact-integrity-notions-restrict-move-class
claim: Every parameterized integrity notion in cryptography restricts the adversary's move class because an impossibility forces it, so non-vacuity at a threshold parameter must be established and not inherited.
paper: Bellare and Kohno, the Φ class, Propositions 4.1 to 4.3. Non-malleable codes, whose tampering family follows from tamper-proof impossibility.
pointer: Bellare and Kohno Propositions 4.1 to 4.3. The details of Bellare and Kohno's Φ class were not verified.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md
corrections: none

## fact-leakage-notions-restrict-other-axes
claim: Leakage-resilient cryptography restricts the side-channel map, Fisher information leakage restricts to unbiased estimators, and maximal leakage, α-leakage and LDP take a supremum over target functions, so none restricts the adversary's class.
paper: the leakage-resilient cryptography, Fisher information leakage, maximal leakage, α-leakage and LDP literatures, no single paper named in the digest.
pointer: Not recorded.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md
corrections: none

## fact-leakage-function-name-taken
claim: The name leakage function is already taken several times, by searchable-encryption leakage profiles, by quantitative information flow and by train-test contamination, so the programme bans it.
paper: none, a finding about prior usage.
pointer: Programme ledger and the prior-art report of 2026-08-05.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/CONTEXT.md, FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md
corrections: none

## fact-r-sweep-unverified-pointers
claim: The 2026-08-05 sweep did not verify Bellare and Namprempre's numbering for INT-CTXT and INT-PTXT, Bellare and Kohno's Φ-class details, the GLMMR TCC 2004 definition, or a source for the certified-robustness predicate.
paper: Bellare and Namprempre. Bellare and Kohno. GLMMR, TCC 2004.
pointer: The verification list of the prior-art report.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-integrity-function-prior-art.md
corrections: none

## fact-r-criterion-lineage-unbounded
claim: In the lineage of success-relation definitions in ML privacy every definition except Cohen et al. Definition C.1 quantifies over an unbounded adversary.
paper: Bhowmick, Duchi, Freudiger, Kapoor and Rogers, arXiv 1812.00984, Definition 2.3. Balle, Cherubin and Hayes, IEEE S&P 2022, Definition 2. Hayes, Mahloujifar and Balle, NeurIPS 2023, Definition 1. Xiao and Devadas, CRYPTO 2023, Definition 1. Cummings, Hod, Sarathy and Swanberg, arXiv 2405.01716, Definitions 4.4 and 4.8. Cohen et al., ITCS 2025, Definitions 1.4 to 1.6 and C.1. Kaplan, Mansour, Nissim and Stemmer, Definitions 3.6 and 4.4. Swanberg, Annamalai, Balle, Hayes and Smith, arXiv 2507.08158. Salem et al., IEEE S&P 2023.
pointer: Definitions as listed. The notation R is Cohen et al.'s, and they attribute their Definition 1.4 to Balle et al. and Attaxonomy.
read: recorded 2026-08-05, not all read in full.
status: recorded
record: FS:exp/docs/notes/case-study-sparse-support-recovery.md, FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md
corrections: none

## fact-attaxonomy-no-refereed-venue
claim: Attaxonomy has no refereed venue, having appeared only in the non-archival track of FORC 2024.
paper: Attaxonomy, authors not recorded in the digests, wiki page attaxonomy.
pointer: Not recorded.
read: recorded, venue check of 2026-09-03.
status: recorded
record: FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md
corrections: none

## fact-salem-privacy-games-sok
claim: Salem et al. put membership, attribute and property inference, DP distinguishability and reconstruction for one trained model into one game anatomy with 18 games against information-theoretic adversaries, and prove reductions with constants and separations among every ordered pair (proven, on toy pipelines).
paper: Salem et al., SoK: Let the Privacy Games Begin!, IEEE S&P 2023 (SCEKPSTZ23). Placed in HE-ML outside the inclusion rule.
pointer: The ⪯_c reductions and Theorems 1 to 11.
read: full, HE-ML session at Halil's request, 2026-10-16. Also recorded by the FORMAL_SECURITY taxonomy report of 2026-08-05.
status: verified
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md, HE-ML:lib/literature/notes/ieee-sp/SCEKPSTZ23.md
corrections:
  - 2026-10-16 The HE-ML interface report had named Salem et al. from memory as the possible owner of the distinguish and invert half, and the full reading of the same day answered that check.

## fact-salem-no-federated-learning
claim: Salem et al. state that their games are sequential programs and do not cover federated learning, so the protocol graph, the channels, the node choices and the steer goal of the HE-ML interface stay open.
paper: Salem et al., IEEE S&P 2023 (SCEKPSTZ23).
pointer: Section VI-D.
read: full, HE-ML session at Halil's request, 2026-10-16.
status: verified
record: HE-ML:lib/literature/notes/ieee-sp/SCEKPSTZ23.md
corrections: none

## fact-salem-theorem-7-separation-template
claim: The construction of Salem et al.'s Theorem 7 is a template for a separation at the distinguish goal.
paper: Salem et al., IEEE S&P 2023 (SCEKPSTZ23).
pointer: Theorem 7.
read: full, HE-ML session at Halil's request, 2026-10-16.
status: verified
record: HE-ML:lib/literature/notes/ieee-sp/SCEKPSTZ23.md
corrections: none

## fact-salem-declines-compute-move
claim: Salem et al. name the move to a computational adversary in §II-C and decline it, keeping compute only as a query counter.
paper: Salem et al., IEEE S&P 2023 (SCEKPSTZ23).
pointer: §II-C.
read: recorded, FORMAL_SECURITY taxonomy report of 2026-08-05 and the case-study lineage.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md, FS:exp/docs/notes/case-study-sparse-support-recovery.md
corrections: none

## fact-wu-integrity-optimization-template
claim: Wu et al. cover integrity only, as an optimization template and not as formal games.
paper: Wu et al., arXiv 2302.09457.
pointer: Not recorded.
read: recorded, FORMAL_SECURITY taxonomy report of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md
corrections: none

## fact-no-unified-formal-definitions
claim: No unified formal definition of privacy and integrity attacks exists, the nearest being Salem et al. for privacy, Wu et al. for integrity, and Villa et al., who span both through one predicate game.
paper: none found. The nearest are Salem et al., IEEE S&P 2023, Wu et al., arXiv 2302.09457, and Villa et al., arXiv 2603.02590.
pointer: Taxonomy report of 2026-08-05.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md
corrections: none

## fact-pi-matrix-unoccupied
claim: No prior systematization occupies the matrix of privacy and integrity, train and test time, and dataset, algorithm and model, and privacy and integrity never co-occur in the other surveys.
paper: none found. Papernot, McDaniel, Sinha and Wellman, IEEE EuroS&P 2018, cross two of three axes with a Logic Corruption rung. Barreno, Nelson, Joseph and Tygar, Machine Learning 2010, with Huang et al., AISec 2011, give the only literal cube. NIST AI 100-2e2025 is the only document with availability, integrity and privacy on one page. Wang and Luan, TMLR 2026, give the only source-to-target asset matrix. ENISA 2021 Table 3 crosses threats with lifecycle stage. Rigaki and Garcia, Salem et al., Cinà et al., Li et al., Goldblum et al., Desfontaines and Pejó and De Cristofaro keep privacy and integrity apart.
pointer: Taxonomy report of 2026-08-05.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md
corrections: none

## fact-taxonomies-no-adversary-class-axis
claim: Across about thirty taxonomies none has an adversary-class axis, every knowledge or access axis is an interface ladder, and privacy and integrity are disjoint by construction.
paper: about thirty taxonomies of the 2026-08-05 sweep.
pointer: Taxonomy report of 2026-08-05.
read: recorded, literature finding the report calls verified across the sweep.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md
corrections: none

## fact-taxonomies-compute-axis-six-entries
claim: Across about thirty works the compute axis reduces to six entries and none is a security parameter, namely Desfontaines and Pejó dimension C (binary), Salem et al. §II-C (a query counter), TrojanZoo (wall-clock), Cinà et al. §3.4.2 (a limitation), poisoning-rate bins, and Mahloujifar et al.'s p-tampering as one attack model.
paper: Desfontaines and Pejó, PoPETs 2020. Salem et al., IEEE S&P 2023. TrojanZoo. Cinà et al. Mahloujifar et al.
pointer: As listed in the taxonomy report.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md
corrections: none

## fact-knowledge-axis-degenerated
claim: The knowledge axis of attack taxonomies degenerated from five components in 2014 to one bit in 2022 to nothing.
paper: the taxonomies of the 2026-08-05 sweep, no single paper named in the digest.
pointer: Taxonomy report of 2026-08-05.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md
corrections: none

## fact-papernot-sok-no-resource-axis
claim: Papernot et al. carry no computational-resource axis, and a resource-like quantity appears three times inside the survey (a poisoning fraction, unbounded poisoning power, an ACRE query-complexity result) and never as an axis.
paper: Papernot, McDaniel, Sinha and Wellman, IEEE EuroS&P 2018.
pointer: Not recorded.
read: recorded, confirmed in the audit of 2026-08-22.
status: verified
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections: none

## fact-resource-axis-absent-from-systematizations
claim: No prior systematization records the resource a work bounds or the party it binds (a novelty claim of the FORMAL_SECURITY survey, empirical on its corpus).
paper: none found, over the survey corpus of 200 coded works.
pointer: Survey claims file, claim resource-axis-absent-from-prior-systematizations.
read: recorded, a supported claim of the survey.
status: recorded
record: FS:exp/survey/lib/claims.yml
corrections: none

## fact-no-complexity-foundations-sok
claim: No position paper or survey arguing complexity-theoretic foundations as the standard was found, and no SoK from 2018 to 2026 states a complexity or information-theoretic organization in its title or abstract.
paper: none found.
pointer: Sweep definitions.md §4.
read: recorded, agent sweep of 2026-10-13.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/definitions.md
corrections: none

# Learned or idealized oracles

## fact-villa-aioracle-security-definition
claim: Villa et al. define an AIOracle as ε-ATK-ψ-secure when every adversary in its game has advantage at most ε, prove modular composition for components that are each complete and secure, and span privacy and integrity through one predicate game, which makes them the closest work to a unified definition.
paper: Villa, Durak, Kohno, Maharramli and Roesner, 2026, arXiv 2603.02590 (March 2026).
pointer: Definition 3, Figure 6, Theorem 1. The confidentiality game is DPD (Algorithm 2, Figure 4). The wiki page states the adversary as PPT. The FORMAL_SECURITY taxonomy report of 2026-08-05 states it as unbounded, with a capability set that is a flag set, grey-box knowledge excluded, a predicate conceded non-implementable, and no reductions.
read: recorded, wiki page date_verified 2026-08-20. The taxonomy report records its own reading of 2026-08-05.
status: disputed, the records disagree on whether the adversary is PPT or unbounded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md, FS:wiki/sources/extending-formalism-cryptography-ai.md, FS:wiki/concepts/aioracle-framework.md
corrections:
  - 2026-08-20 The page was corrected against the PDF. The game is DPD, not DPP, and Definition 3 bounds the advantage by ε.

## fact-villa-aioracle-mid-bound-glm
claim: The AIOracle MID bound p_c ≤ 1/2 + n·ε is proved inside a generic language model, so Chapter 24 records it as a heuristic guarantee under the Canetti, Goldreich and Halevi caveat.
paper: Villa, Durak, Kohno, Maharramli and Roesner, 2026, arXiv 2603.02590.
pointer: Chapter 24 message 32, recorded by lödeg.
read: recorded, Chapter 24 phase 3, no check of the paper recorded.
status: recorded
record: FS:exp/docs/notes/chapter-24.md
corrections: none

## fact-cgh-idealized-model-caveat
claim: Chapter 24 places the idealized-model rung (generic language model, random oracle model, generic group model) under the Canetti, Goldreich and Halevi uninstantiability caveat, so a bound proved inside such a model is a heuristic guarantee.
paper: Canetti, Goldreich and Halevi, venue not recorded.
pointer: Chapter 24 messages 31 and 32.
read: recorded, cited in Chapter 24 with no check recorded.
status: recorded
record: FS:exp/docs/notes/chapter-24.md
corrections: none

## fact-vbb-obfuscation-impossible
claim: Virtual black-box obfuscation is impossible in general, and the FORMAL_SECURITY AI oracle report uses this to give an oracle with ideal representation the standing of a random oracle (heuristic analogy).
paper: BGIRSVY01, as the report keys it.
pointer: Not recorded.
read: recorded, cited in the AI oracle report of 2026-10-13 with no check recorded.
status: recorded
record: FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex
corrections: none

## fact-gilbert-mcmillan-dp-testing-impossible
claim: Testing differential privacy from samples is impossible, and the HE-ML learning-oracle theory records its drawn-seed lower bounds as the atomless form of this result.
paper: Gilbert and McMillan, Allerton 2018.
pointer: Theorems 10 and 12.
read: recorded, cited in the prior-work paragraph of the final learning-oracle theory of 2026-10-17, which records no check of the paper.
status: recorded
record: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md
corrections: none

## fact-barthe-program-logic-couplings
claim: Program logics build couplings for known code, while the coupling certificate of the HE-ML learning-oracle theory samples couplings for an opaque learning function.
paper: Barthe et al., LICS 2016.
pointer: Not recorded.
read: recorded, cited in the prior-work paragraph of the final learning-oracle theory of 2026-10-17, which records no check of the paper.
status: recorded
record: HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md
corrections: none

## fact-no-formal-first-order-attacker-class
claim: In a coding of over 190 relevant works no attacker is a formal first-order class, gradient access is a formal object in four works, and calls to training appear in ten (empirical, on the coding and not on the papers).
paper: none, a coding of over 190 works by five agents on 2026-10-13.
pointer: 40 works study concrete deep networks, 36 quantify over all learners, 30 assume DP, one assumes a Gibbs posterior and none a version space, seven treat training as an opaque call, attackers are unbounded (58), PPT (52) or one fixed algorithm (33), and 47 of the 92 core works state no utility condition.
read: recorded, FORMAL_SECURITY coding of 2026-10-13.
status: recorded
record: FS:exp/survey/lib/literature/ontology/views.md, FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
corrections: none

## fact-gradient-attackers-first-order
claim: Gradient-based attackers are attackers with a first-order oracle (heuristic, a reading of the attack literature).
paper: the gradient-based attack literature, no single paper named.
pointer: Not recorded.
read: recorded, stated in the FORMAL_SECURITY AI oracle issue of 2026-10-13.
status: recorded
record: FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
corrections: none

# The seed as a resource and split learning

## fact-balle-known-initialization-reconstruction
claim: Balle, Cherubin and Hayes reconstruct with MSE 0.0089 when the initialization is known against 0.0695 with fresh seeds on MNIST, and state that the attack fails without the initial parameters, the closest prior for the seed as a resource (empirical).
paper: Balle, Cherubin and Hayes, Reconstructing Training Data with Informed Adversaries, IEEE S&P 2022, arXiv 2201.04845.
pointer: Appendix A, Table III.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-neuracrypt-bayesian-posterior
claim: NeuraCrypt's privacy theorem is the Bayesian posterior over a law of random-network encoders.
paper: Yala and coauthors, NeuraCrypt, arXiv 2106.02484.
pointer: Theorem 1.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-neuracrypt-broken-empirically
claim: NeuraCrypt is broken empirically by boosting to a perfect matching.
paper: Carlini and coauthors, NeuraCrypt is not private, arXiv 2108.07256.
pointer: Not recorded beyond the empirical break.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-ideal-keyed-encoding-weak-learner
claim: For an ideal keyed encoding, a weak learner yields a near perfect learner (proven).
paper: Carlini and coauthors, NeuraCrypt is not private, arXiv 2108.07256.
pointer: Theorem 1.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-unsplit-unknown-client-inversion
claim: UnSplit inverts an unknown split-learning client model by joint optimization, and it works at MNIST split depth 1 before and after training (empirical).
paper: Erdoğan, Küpçü and Çiçek, UnSplit, WPES 2022, arXiv 2108.09033.
pointer: Table 2.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-pcat-pseudo-client-attack
claim: PCAT attacks split learning with a pseudo-client trained on a small amount of public data (empirical).
paper: Gao and Zhang, PCAT, USENIX Security 2023.
pointer: Not recorded in the scan.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-initialization-matters-langevin-kl
claim: The KL divergence between Langevin trajectories on neighbouring datasets equals the integrated squared gradient difference, with the initialization revealed and nothing said about a hidden seed (proven).
paper: Ye, Zhu, Liu, Shokri and Cevher, Initialization Matters, NeurIPS 2023, arXiv 2310.20579.
pointer: Theorem 3.1.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-gkvz22-secret-in-training-coins
claim: The white-box backdoor of Goldwasser et al. works by tampering with the random coins of random Fourier features, so the planter's secret lives in the training randomness, and the backdoor papers prove inside a fixed paradigm (random Fourier features, a frozen random first layer).
paper: Goldwasser, Kim, Vaikuntanathan and Zamir, 2022 (GKVZ22).
pointer: Not recorded beyond the sweep sheet GKVZ22.
read: recorded, agent sheet of the 2026-10-13 sweep and the AI oracle issue of 2026-10-13.
status: recorded
record: FS:exp/survey/lab/results/literature-sweep/definitions.md, FS:exp/survey/lib/issues/2026-10-13-halil-ai-oracle-definition.md
corrections: none

## fact-no-formal-seed-separation
claim: No formal separation between attackers who know the training seed and attackers who do not was found, and the seed as an attacker resource is measured only empirically (empirical, search-based).
paper: none found. The nearest are Balle, Cherubin and Hayes, IEEE S&P 2022, Appendix A, and Haghifam, Smith and Ullman, arXiv 2508.19458, whose separation prices knowledge of the covariance.
pointer: Scan, Verdicts 2 and 3. The FORMAL_SECURITY programme digest records that none of the files it read prices an attacker's knowledge of the training seed as a resource.
read: recorded, absence finding of the 2026-10-25 scan by a reader subagent, and of the programme digest of 2026-10-25.
status: recorded
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md, HE-ML:sink/formalizing/sources/2026-10-25-formal-security-programme.md
corrections: none

# Inverting networks and the reach of statistical queries

## fact-lei-preimage-np-complete
claim: Deciding whether a preimage exists is NP-complete for fixed two-layer and four-layer ReLU networks (proven, worst case over constructed weights, which says nothing about the law that training induces, heuristic).
paper: Lei, Jalal, Dhillon and Dimakis, Inverting Deep Generative Models, One Layer at a Time, NeurIPS 2019, arXiv 1906.07437.
pointer: Theorems 1 and 2.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-lei-random-expansive-layers-invertible
claim: Random Gaussian layers with expansion at least 2.1 are inverted exactly by layer-wise linear programs with high probability, given known weights, so the result covers the known-seed case only (proven).
paper: Lei, Jalal, Dhillon and Dimakis, NeurIPS 2019, arXiv 1906.07437.
pointer: Theorem 3.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-hand-voroninski-descent-direction
claim: For random expansive generative priors with known weights, the empirical risk has a descent direction away from the truth and its negative multiple (proven).
paper: Hand and Voroninski, COLT 2018, arXiv 1705.07576.
pointer: Theorem 1.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-abbe-sandon-sgd-universal
claim: Batch-one SGD on a polynomial-size network from a constructed initialization learns anything polynomial-time learnable (proven).
paper: Abbe and Sandon, NeurIPS 2020, arXiv 2001.02992.
pointer: Theorem 1.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-abbe-sandon-noisy-gd-fails
claim: Noisy gradient descent fails under small cross-predictability (proven).
paper: Abbe and Sandon, NeurIPS 2020, arXiv 2001.02992.
pointer: Theorem 3.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-sq-simulates-minibatch-sgd
claim: When batch size times squared precision exceeds a logarithmic factor, statistical queries simulate mini-batch SGD, so an SQ lower bound on an attack task binds SGD-trained attackers in that regime (proven given the SQ bound).
paper: Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, arXiv 2108.04190.
pointer: Theorem 1c.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

## fact-fine-precision-sgd-simulates-pac
claim: At fine precision SGD simulates PAC learning, so an SQ lower bound says nothing about batch-one or fine-precision attackers (proven).
paper: Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, arXiv 2108.04190.
pointer: Theorem 1a.
read: full, reader subagent, 2026-10-25.
status: verified
record: HE-ML:sink/formalizing/sources/2026-10-25-learning-bounded-scan.md
corrections: none

# Multi-party learning and homomorphic encryption

## fact-he-oft-semi-honest-simulation
claim: In HE-OFT a semi-honest server with t − 1 clients is simulated from the ideal leakage under IND-CPA and a smudging hypothesis that the measured configuration does not meet (proven in HE-OFT).
paper: HE-OFT (KSK26), the group's prior work under multiparty CKKS.
pointer: Recorded in the HE-ML interface report, subsection HE-OFT on the interface.
read: full, HE-ML session, by 2026-10-16, note KSK26 marked full-read.
status: verified
record: HE-ML:lib/literature/notes/arxiv/KSK26.md, HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex
corrections: none

## fact-he-oft-deviating-clients-label-view
claim: Against t − 1 deviating clients and an honest server HE-OFT bounds the distinguishing advantage by a negligible term plus what the coalition's label queries give, a label view no stronger than both shared heads in plaintext, and both HE-OFT statements rest on three readings of deviating messages that no proof enforces (proven in HE-OFT).
paper: HE-OFT (KSK26).
pointer: Recorded in the HE-ML interface report, subsection HE-OFT on the interface.
read: full, HE-ML session, by 2026-10-16, note KSK26 marked full-read.
status: verified
record: HE-ML:lib/literature/notes/arxiv/KSK26.md, HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex
corrections: none

## fact-he-oft-no-deviating-server
claim: No protocol in which clients decrypt what the server presents admits a deviating server, as the interface report records among HE-OFT's results.
paper: HE-OFT (KSK26).
pointer: HE-ML interface report, subsection HE-OFT on the interface.
read: full, HE-ML session, by 2026-10-16, note KSK26 marked full-read.
status: verified
record: HE-ML:lib/reports/src/2026-10-16-halil-adversary-interface.tex
corrections: none

## fact-hhkls26-per-party-smudging-fails
claim: Hwang et al. prove, as the sweep coder extracted it, that independent per-party smudging fails standard simulation security.
paper: Hwang et al., ASIACRYPT 2026 (HHKLS26).
pointer: Deck frames 13 and 15 of the HE-ML meeting of 16 October.
read: recorded, extracted by a language-model sweep coder on 2026-10-16. The deep read is not done.
status: recorded
record: HE-ML:lib/literature/ledger.csv, HE-ML:lib/literature/notes/asiacrypt/HHKLS26.md, HE-ML:sink/formalizing/sources/2026-10-25-he-ml-digest.md
corrections: none

## fact-hlss25-per-party-smudging-proof
claim: Hwang, Lee, Seo and Song give a placed proof against deviating decryptors that smudges per party.
paper: Hwang, Lee, Seo and Song, CCS 2025 (HLSS25).
pointer: Deck frame 13 of the HE-ML meeting of 16 October.
read: recorded, extracted by a language-model sweep coder on 2026-10-16. The deep read is not done.
status: recorded
record: HE-ML:lib/literature/ledger.csv, HE-ML:lib/literature/notes/acm-ccs/HLSS25.md, HE-ML:sink/formalizing/sources/2026-10-25-he-ml-digest.md
corrections: none

## fact-threshold-fhe-active-security-no-ckks
claim: Active security for threshold FHE decryption was found only for thresholdized BFV, BGV and FHEW, and none for CKKS.
paper: none named in the digest for the works found.
pointer: Theory register, open problem 6.
read: recorded, search in round 03 of the formal tuning.
status: recorded
record: HE-ML:sink/2026-10-16-formal-tuning/theory/CURRENT.md
corrections: none

## fact-fl-unrealistic-assumptions-occupied
claim: The critique that federated learning attacks are evaluated under unrealistic assumptions is occupied.
paper: Wainakh et al., Sensors 2023. Huang et al., NeurIPS 2021. Shejwalkar et al., IEEE S&P 2022. A poisoning SoK benchmark, arXiv 2502.03801, venue unverified. A 2026 preprint, arXiv 2603.20615.
pointer: Not recorded per paper.
read: recorded, HE-ML search of 2026-10-16, no notes written.
status: recorded
record: HE-ML:lib/literature/positioning.md
corrections: none

## fact-four-accepted-papers-unavailable
claim: Four accepted papers in the scope of the HE-ML sweep had no accessible PDF on 2026-10-16.
paper: Not One Less, CCS 2024. G-Fence, CCS 2026. Authenticated Outsourced Incrementally Verifiable MPC, ASIACRYPT 2026. Shared Spotlight Meridian, IEEE S&P 2026.
pointer: Not applicable.
read: recorded, HE-ML sweep of 2026-10-16.
status: recorded
record: HE-ML:sink/unavailable.md
corrections: none

## fact-ledger-five-paper-data-errors
claim: The HE-ML sweep coders found data errors in five papers.
paper: LAWKDM26, TTPLHLCL26, CQYZFDX24, CFMPV25 and DHWSGRC25.
pointer: The ledger column dictionary, which describes each error.
read: recorded, found by language-model sweep coders on 2026-10-16.
status: recorded
record: HE-ML:sink/ledger-columns.md
corrections: none

# Agents and alignment

## fact-agent-oracles-not-implementable
claim: The four contextual agent-security properties of Siu et al. rest on oracle functions that the authors state are not implementable as given, and the paper's claim is coverage of 87 surveyed papers.
paper: Siu, He, Montgomery, Wang, Gong, Wang and Song, 2026, arXiv 2603.19469.
pointer: §4.2 to §4.4.
read: recorded, wiki page date_verified 2026-08-22.
status: verified
record: FS:wiki/sources/formalizing-llm-agent-security.md
corrections: none

## fact-camel-measured-not-proved
claim: CaMeL contains no theorem or lemma, and its 77 percent of AgentDojo tasks solved with guarantees is a measurement on one benchmark (empirical).
paper: Debenedetti et al., 2025, arXiv 2503.18813.
pointer: Game PI-SEC, §4, Figure 3.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/camel-defeating-prompt-injections.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-20 The page was corrected against the PDF to say CaMeL has no theorem.
  - 2026-08-22 The audit lists the earlier theorem attribution among traced fabrications.

## fact-melon-bounds-conditional
claim: MELON's only analysis is a Hoeffding bound that holds when an unverified separation of mean similarity scores around the threshold holds, so it has no provable detection theorem.
paper: Zhu, Yang, Wang, Guo and Wang, ICML 2025, arXiv 2502.05174.
pointer: §3.4.2.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/melon-indirect-prompt-injection.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-20 The page was corrected against the PDF to say MELON proves no detection guarantee.
  - 2026-08-22 The audit lists the earlier provable detection theorem among traced fabrications.

## fact-consensus-smoothing-no-system-bound
claim: The consensus-smoothing paper for multi-agent LLM systems proves no system-level bound.
paper: Hu et al., 2026, wiki page rs-llm-multi-agent.
pointer: Theorem 1.
read: recorded, corrected against the PDF 2026-08-20.
status: verified
record: FS:wiki/sources/rs-llm-multi-agent.md
corrections:
  - 2026-08-20 The page was corrected to say the paper proves no system bound.

## fact-adds-workshop-submission
claim: ADDS is a workshop submission, not an ICML Oral.
paper: Shpilevskiy et al., 2025, ADDS.
pointer: PDF footer.
read: recorded, corrected against the PDF 2026-08-20.
status: verified
record: FS:wiki/sources/adds-adaptive-diffusion-smoothing.md
corrections:
  - 2026-08-20 The venue was corrected. The old record called it an ICML Oral.

## fact-maxmin-rlhf-gap
claim: One Bradley-Terry reward cannot align a policy with every subgroup of a heterogeneous population, with the lower bound stated for the subgroup furthest from the aggregate (proven).
paper: Chakraborty et al., ICML 2024, arXiv 2402.08925.
pointer: Lemma 1 and Theorem 1.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/maxmin-rlhf-impossibility.md
corrections: none

## fact-jailbreak-paradox-existential
claim: The jailbreak paradox is existential and rests on the unargued existence of a most powerful jailbreakable LLM.
paper: Rao, Choudhury and Aditya, 2024, arXiv 2406.12702.
pointer: Theorems 3.1 and 4.1, Definitions 4.1 and 4.2.
read: recorded, wiki page date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/jailbreak-paradox.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-22 The audit found that the jailbreak-paradox page had swapped Theorems 3.1 and 4.1.

## fact-agentic-certified-cluster-no-bounded-adversary
claim: Across 16 agentic and certified-defence papers every bound is a radius, a poisoned-sample count or an interface restriction, two state an unbounded adversary, and five have no theorem.
paper: the 16 papers of the agentic and certified cluster of the FORMAL_SECURITY corpus.
pointer: Audit §4.
read: recorded, audit finding of 2026-08-22.
status: recorded
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections: none

# Bibliographic records

## fact-venues-resolved-2026-08-22
claim: Brzuska and Couteau is EUROCRYPT 2022 Part II, LaVigne, Lincoln and Vassilevska Williams is CRYPTO 2019 Part III, TCBM20 is NeurIPS 2020, and Carlini et al., On Evaluating Adversarial Robustness, is a preprint never published.
paper: BC22, LLW19, TCBM20 and Carlini et al. 2019.
pointer: Not applicable.
read: recorded, resolved from bibliographies inside the corpus on 2026-08-22.
status: recorded
record: FS:exp/survey/lib/profs/2026-08-22-halil.md
corrections: none

## fact-venues-resolved-2026-09-03
claim: The venue checks of 2026-09-03 resolved Garg et al. (GJMM20) at ALT 2020, Computational Differential Privacy at CRYPTO 2009, Carlini, Jagielski and Mironov at CRYPTO 2020, Continuous LWE at STOC 2021, the Brennan and Bresler SQ and low-degree equivalence at COLT 2021, the Barak et al. SoS planted-clique bound at FOCS 2016, Shafran et al. at TMLR 2024, Wen et al.'s data-reconstruction SoK at USENIX Security 2025 and Zhang et al. at IEEE SaTML 2025, with Fenaux and Kerschbaum staying a preprint and Ding et al., arXiv 2502.15024, retitled at NeurIPS 2025.
paper: As named.
pointer: Not applicable.
read: recorded, venue batch and round-two review of 2026-09-03.
status: recorded
record: FS:exp/survey/lib/reports/archive/2026-09-03-halil-venues-batch-a.md, FS:exp/survey/lib/reports/archive/2026-09-03-halil-review-survey-round-2.md
corrections: none

## fact-venue-attributions-not-in-pdfs
claim: Several wiki venue attributions are not stated in the PDFs, namely FOCS for Goldwasser et al. 2022 and for Hirahara and Nanashima, CVPR for Immune, EUROCRYPT 2023 for Dodis, Quach and Wichs, whose PDF is dated 2021, and ICML Oral for ADDS.
paper: As named.
pointer: Front-matter venue fields.
read: recorded, checked against the PDFs 2026-08-20.
status: verified
record: FS:wiki/sources/planting-undetectable-backdoors.md, FS:wiki/sources/learning-in-pessiland.md, FS:wiki/sources/immune-rlhf-jailbreak-defense.md, FS:wiki/sources/speak-much-remember-little.md, FS:wiki/sources/adds-adaptive-diffusion-smoothing.md
corrections: none

## fact-sweep-brief-four-citations-wrong
claim: Four citations in the brief of the 2026-08-05 taxonomy sweep were wrong, namely the TrojanZoo and BackdoorBench author lists, the Liu et al. privacy survey, and the provenance of the Biggio knowledge tuple.
paper: TrojanZoo, BackdoorBench, Liu et al. privacy survey, Biggio et al.
pointer: Taxonomy report of 2026-08-05.
read: recorded, FORMAL_SECURITY sweep of 2026-08-05.
status: recorded
record: FS:exp/docs/reports/2026-08-05-lit-taxonomy-landscape.md
corrections: none

# State of the records

## fact-wiki-audit-verified-181-pages
claim: The FORMAL_SECURITY wiki audit of 2026-08-20 to 2026-08-22 verified 181 of 181 source pages and found two contamination paths and two false-positive modes of the quote checker, spelling variants and editorial gloss inside quotation marks.
paper: none, the FORMAL_SECURITY wiki.
pointer: Audit §1. The root adds the rule to always use grep -a.
read: recorded, audit of 2026-08-20 to 2026-08-22.
status: recorded
record: FS:CLAUDE.md, FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections: none

## fact-wiki-audit-fabrications-traced
claim: The audit of 2026-08-22 traced fabrications on wiki pages and found about 5 percent of 1100 quotations wrong, sixteen of them the compass artifact's own prose.
paper: none, the FORMAL_SECURITY wiki.
pointer: Audit §3. The seven challenges on the cross-domain MAS page were invented. IMTM occurs zero times in the attributed paper, in all 186 PDFs, and twice in the compass artifact. The low-degree survey page cited arXiv 2603.02594 from a June 2025 document. The planted-assumptions PKE page listed three assumptions where the paper states two. The planted-graphs crypto page confused share size with message size. The MELON, CaMeL and covert-learning fabrications have their own entries.
read: recorded, audit of 2026-08-22.
status: recorded
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections: none

## fact-wiki-quote-audit-30-passages
claim: A check of every wiki blockquote against all 164 PDFs on 2026-08-20 corrected 30 passages, 16 on 13 pages being the compass artifact's prose and 14 on 11 pages failing a first automated match.
paper: none, the FORMAL_SECURITY wiki.
pointer: The 2026-08-20 wiki log entry and the conventions of the root CLAUDE.md. The check used automated 45-character window matching with punctuation stripped, and a full quote pass over pages lacking claim_quantifier was then still owed.
read: recorded, wiki log of 2026-08-20.
status: recorded
record: FS:wiki/log.md
corrections: none

## fact-wiki-raw-pdfs-replaced
claim: Ten of 45 raw PDFs had content that did not match their filename and were replaced from arXiv, IACR ePrint or ECCC.
paper: none, the raw folder of the FORMAL_SECURITY wiki.
pointer: Raw audit log entry of 2026-04-23. The replacements were verified by first-page extraction.
read: recorded, wiki log of 2026-04-23.
status: recorded
record: FS:wiki/log.md
corrections: none

## fact-wiki-quote-rotation-four-rows
claim: Four classification rows had been rotated by one page so that each held the next paper's evidence quote, and the quotes were re-extracted.
paper: Bordelon et al. 2025, Sorscher et al. 2022, Busbridge et al. 2025, Joshi et al. 2025.
pointer: cls_reason fields.
read: recorded, corrected on 2026-08-27. The algorithmic-progress row was reclassified against its PDF on 2026-09-03 for the same fault.
status: recorded
record: FS:wiki/sources/feature-learning-improves-scaling.md, FS:wiki/sources/data-pruning-beats-power-laws.md, FS:wiki/sources/distillation-scaling-laws.md, FS:wiki/sources/single-index-harmonic-decomposition.md, FS:wiki/sources/algorithmic-progress-lm.md
corrections:
  - 2026-08-27 The four rotated quotes were re-extracted.

## fact-wiki-misc-pages-corrected
claim: Besides the corrections recorded in their own entries, wiki pages were corrected against the PDFs on 2026-08-20 for the DP-SGD moments accountant description and for zk-verifiable pipelines, whose page had named tools absent from the paper.
paper: DP-SGD, page deep-learning-differential-privacy. The zk-verifiable AI pipelines paper, page zk-verifiable-ai-pipelines.
pointer: Dated correction notes on each page.
read: recorded, each page carries a dated correction note and date_verified 2026-08-20.
status: verified
record: FS:wiki/sources/deep-learning-differential-privacy.md, FS:wiki/sources/zk-verifiable-ai-pipelines.md
corrections:
  - 2026-08-20 Both pages were corrected against their PDFs.

## fact-gamarnik-quotes-swapped
claim: Two Gamarnik quotes had been swapped between wiki pages.
paper: Gamarnik, the works quoted on two wiki pages, not named in the digest.
pointer: Audit §3.
read: recorded, audit of 2026-08-22.
status: recorded
record: FS:exp/survey/lib/reports/archive/2026-08-22-halil-note-wiki-audit-findings.md
corrections:
  - 2026-08-22 The audit found the swap.

## fact-novelty-checks-2026-07-26
claim: On 2026-07-26 four novelty claims were checked and all four refuted, the survivor came from a citation-graph sweep while topic search scored zero of four, and a novelty check must search the venue where the technique lives and prefer a named published conjecture over an empty framing.
paper: none, a process record.
pointer: Methodological note of the root CLAUDE.md and the native-asymmetry analysis §3.1.
read: recorded, root CLAUDE.md.
status: recorded
record: FS:CLAUDE.md, FS:wiki/analyses/native-asymmetry-in-learning.md
corrections: none

## fact-unverified-count-false
claim: A count stated from memory on 2026-08-22, that membership inference appeared in five of six landscape subsections, was false, and the true figure is zero.
paper: none, the FORMAL_SECURITY survey records.
pointer: Ruling 2026-08-20-an-unverified-count-is-not-written.
read: recorded, PI-round record of 2026-08-22.
status: recorded
record: FS:exp/survey/lib/profs/2026-08-22-halil.md
corrections: none

## fact-wiki-page-counts-disagree
claim: The root CLAUDE.md gives 110 sources, 62 concepts and 84 entities as of 2026-08-20, the wiki log gives 156, 83 and 111 for that date, and the folders hold 200, 83 and 116.
paper: none, the FORMAL_SECURITY wiki.
pointer: Root CLAUDE.md Role section, 2026-08-20 wiki log entry.
read: recorded, folder counts taken on 2026-10-25 by the wiki-claims digest.
status: recorded
record: FS:CLAUDE.md, FS:wiki/log.md
corrections: none

## fact-wiki-verification-dates-inverted
claim: Several wiki pages carry a date_verified earlier than their date_ingested, for example Yeom et al., Shokri et al., Balle et al. and LAMP, verified 2026-08-20 and ingested 2026-08-22.
paper: none, the FORMAL_SECURITY wiki.
pointer: Front matter.
read: recorded, found by the wiki-claims digest on 2026-10-25.
status: recorded
record: FS:wiki/sources/privacy-risk-overfitting.md, FS:wiki/sources/membership-inference-shokri.md, FS:wiki/sources/reconstructing-informed-adversaries.md, FS:wiki/sources/lamp-gradient-inversion.md
corrections: none

## fact-he-ml-ledger-rows-unchecked
claim: Every HE-ML ledger row comes from one language-model coder's reading and is marked sweep, except the three HE-OFT rows and the two Salem et al. rows, and 363 of 365 notes hold only template text, so ledger content about a paper is an extraction awaiting a check against the paper.
paper: none, the 349 coded papers of the HE-ML sweep.
pointer: Digest section 6. Counts recomputed on 2026-10-25.
read: recorded, HE-ML digest of 2026-10-25.
status: recorded
record: HE-ML:lib/literature/ledger.csv, HE-ML:sink/formalizing/sources/2026-10-25-he-ml-digest.md
corrections: none
