# Claims held by the FORMAL_SECURITY wiki

Collected 2026-10-25 from `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY`, read only. Paths are relative to that root. Each entry restates a claim as the wiki records it, in the root `CLAUDE.md`, `raw/SOURCES.md`, `wiki/log.md`, an analysis page or a source page. None of it was checked against a paper during this collection, and nothing was added from memory. An arXiv identifier appears only where the wiki records one.

Every entry has five fields. Claim is one sentence. Paper gives authors, venue, year and identifier. Pointer gives the theorem, definition or section the wiki cites. Checked says what the wiki records about verification against the PDF in `raw/`. Page gives the wiki page that holds the claim. A front-matter field `date_verified` means the page was checked against its PDF on that date. A banner means a "Verified against raw/..." note at the top of the page. "No stamp" means the page was written from the raw PDF but carries neither.

Section 9 lists the corrections and retractions. Section 10 lists places where two wiki records disagree, found while mapping.

## 1. Standing positions and negative results

* `yeom-membership-baseline-zero`
  * Claim. Yeom et al.'s membership advantage has a zero baseline by construction, so a marginal advantage over a public-knowledge baseline adds nothing and the game is already published.
  * Paper. Yeom, Giacomelli, Fredrikson and Jha, CSF 2018, no arXiv recorded. Related records are Xiao and Devadas, PAC Membership Privacy, CRYPTO 2023 (no page) and Desfontaines and Pejó, PoPETs 2020, dimension R.
  * Pointer. Definition 4 and Experiment 1. Definition 6 is the attribute advantage with a Bayes-optimal baseline and is not degenerate.
  * Checked. Yes. `CLAUDE.md` records the correction against the PDF on 2026-08-22, and the page carries `date_verified` 2026-08-20 with Definitions 4 and 6 checked character by character.
  * Page. `wiki/sources/privacy-risk-overfitting.md`, `wiki/sources/sok-differential-privacies.md`.

* `memory-bounded-crypto-mature`
  * Claim. Cryptography against memory-bounded adversaries is mature, from Raz's parity bound through Guan and Zhandry to Dodis, Quach and Wichs.
  * Paper. Raz, FOCS 2016, arXiv 1602.05161. Guan and Zhandry, EUROCRYPT 2019. Dodis, Quach and Wichs, EUROCRYPT 2022 and 2023.
  * Pointer. Raz Theorems 1 and 2. Dodis, Quach and Wichs 2023, main result, memory gap up to 2^{O(n)}.
  * Checked. No stamp. Pages ingested from the raw PDFs on 2026-08-21, with post-ingest corrections filed in `raw/SOURCES.md` on 2026-08-20.
  * Page. `wiki/sources/raz-parity-time-space.md`, `wiki/sources/bounded-storage-simple-schemes.md`, `wiki/sources/speak-much-remember-little.md`, `wiki/sources/authentication-bounded-storage.md`.

* `no-memory-bounded-ml-adversary`
  * Claim. No security or privacy definition in the corpus bounds an ML or privacy adversary by memory, because every space bound sits on the learner, the mechanism or the defender.
  * Paper. Raz, FOCS 2016 (learner). Dinur, Stemmer, Woodruff and Zhou, EUROCRYPT 2023, ePrint 2023/171 (mechanism). Kaplan, Mansour, Nissim and Stemmer, CRYPTO 2021, arXiv 2101.10836 (defender).
  * Pointer. The memory section of `raw/SOURCES.md`. Raz's §1.3 corollary is the corpus's only attacker-side memory bound, and its attacker is a parity learner against a one-time pad.
  * Checked. No. An absence finding of the 2026-08-20 sweep, recorded in `CLAUDE.md`.
  * Page. `wiki/sources/raz-parity-time-space.md`, `wiki/sources/dp-adaptive-analysis-bounded-space.md`, `wiki/sources/adaptive-vs-oblivious-streaming.md`.

* `transformer-rnn-separation-exists`
  * Claim. Learning separations between transformers and RNNs are published, and only the memory-sample mechanism is unclaimed.
  * Paper. arXiv 2503.11272, authors not recorded.
  * Pointer. None recorded.
  * Checked. No. Marked single-sourced and unread in the native-asymmetry analysis.
  * Page. No source page. `CLAUDE.md`, `wiki/analyses/native-asymmetry-in-learning.md`.

* `low-degree-security-is-circuit-security`
  * Claim. Bogdanov et al. and Abram et al. state cryptographic security against size-bounded circuits with low-degree hardness as supporting evidence, so neither defines security against a low-degree adversary.
  * Paper. Bogdanov, Jones, Rosen and Zadik, TCC 2024, arXiv 2409.16227, ePrint 2024/1497. Abram, Beimel, Ishai, Kushilevitz and Narayanan, TCC 2023, ePrint 2023/1929.
  * Pointer. Bogdanov et al. Theorem 2.1 (unconditional low-degree bound), Propositions 4.1 and 4.3 (size-bounded reductions), Conjectures 1.3 and 1.4 (polynomial time). Abram et al. abstract, adversaries of size n^{o(log n)} with advantage n^{−Ω(1)}.
  * Checked. Yes, `date_verified` 2026-08-22 (Bogdanov et al.) and 2026-08-20 (Abram et al.).
  * Page. `wiki/sources/bogdanov-low-degree-planted-subgraph.md`, `wiki/sources/cryptography-from-planted-graphs.md`.

* `planted-subgraph-noise-caveat`
  * Claim. Bogdanov et al. note that planted clique and planted subgraph do not satisfy the noise-robust hypothesis of the low-degree conjecture.
  * Paper. Bogdanov, Jones, Rosen and Zadik, TCC 2024, arXiv 2409.16227.
  * Pointer. Not recorded beyond `CLAUDE.md`.
  * Checked. Recorded in `CLAUDE.md` with the 2026-08-22 correction against the PDF.
  * Page. `wiki/sources/bogdanov-low-degree-planted-subgraph.md`.

* `low-degree-not-quasipoly`
  * Claim. A low-degree-bounded adversary and a quasi-polynomial-time adversary are provably different, because the quasi-polynomial low-degree conjecture is false.
  * Paper. Buhai, Hsieh, Jain and Kothari, FOCS 2025, arXiv 2505.17360.
  * Pointer. Abstract, an n^{O(log^{1/(k−1)} n)}-time distinguisher in the square S_n-symmetric regime. Theorem 2.4 and Remark 2.3 give the polynomial-time distinguisher for the rectangular variant only. The largest-eigenvalue construction has a non-product null and refutes nothing.
  * Checked. Clauses corrected against the PDF on 2026-08-20 in `raw/SOURCES.md` and `CLAUDE.md`. The page has no `date_verified`.
  * Page. `wiki/sources/quasi-poly-low-degree-conjecture-false.md`.

* `low-degree-rigorous-implications`
  * Claim. A vanishing low-degree likelihood ratio rigorously defeats the stated test classes only for a noisy version of the planted law, and it rules out no polynomial-time algorithm.
  * Paper. Hsieh, Kane, Kothari, Li, Mohanty and Tiegel, STOC 2026, arXiv 2601.05850.
  * Pointer. Theorem 1.1 (total variation), Theorem 1.2 (symmetric polynomials of degree at most ε log n / (C log log n), no permutation invariance assumed), Theorem 1.3 (one signed subgraph count).
  * Checked. Corrected against the PDF on 2026-08-20. No `date_verified`.
  * Page. `wiki/sources/rigorous-implications-low-degree.md`.

* `gky-limits-narrow`
  * Claim. The Groce, Katz and Yerukhimovich limits on computational DP cover only black-box constructions and outputs in R^n for constant n, and the authors exclude classifiers, graphs and synthetic databases.
  * Paper. Groce, Katz and Yerukhimovich, TCC 2011, no arXiv recorded.
  * Pointer. Theorems 1 and 2, and the subsection on limitations at the end of §1.1.
  * Checked. Yes. `CLAUDE.md` records a check against the primary PDF on 2026-08-20 with the exclusions pinned verbatim.
  * Page. `wiki/sources/limits-cdp-client-server.md`.

* `cdp-separation-infeasibility`
  * Claim. The first single-curator separation of computational from statistical DP is an infeasibility result on a task its authors call unnatural.
  * Paper. Bun, Chen and Vadhan, TCC 2016-B, no arXiv recorded.
  * Pointer. Theorem 11, under sub-exponentially secure one-way functions and extractable zaps.
  * Checked. No stamp. Page ingested from the raw PDF on 2026-08-20.
  * Page. `wiki/sources/separating-cdp-client-server.md`.

* `cdp-separation-unbounded`
  * Claim. A task with an efficient CDP mechanism admits no statistical DP mechanism of constant utility, even an inefficient one, under NIWI, laconic keyless CRHF and diO.
  * Paper. Ghazi, Ilango, Kamath, Kumar and Manurangsi, FOCS 2023, arXiv 2301.00104.
  * Pointer. The SDP lower bound at constant ε and δ = 1/n^{27}, Assumptions 18, 22 and 26.
  * Checked. No stamp. Page ingested from the raw PDF on 2026-08-20.
  * Page. `wiki/sources/towards-separating-cdp.md`.

* `cdp-separation-breaks-quasipoly`
  * Claim. The Ghazi et al. mechanism is not CDP against quasi-polynomial adversaries, so a separation on a natural task remains open.
  * Paper. Ghazi, Ilango, Kamath, Kumar and Manurangsi, FOCS 2023, arXiv 2301.00104.
  * Pointer. Excluded cases on the page, which quote the authors on the point.
  * Checked. No stamp. Page ingested from the raw PDF on 2026-08-20.
  * Page. `wiki/sources/towards-separating-cdp.md`.

* `restricted-class-then-lift-template`
  * Claim. Ghazi et al. first prove privacy against a class of non-adaptive decision-tree adversaries and then lift it to computationally bounded adversaries with cryptography.
  * Paper. Ghazi, Ilango, Kamath, Kumar and Manurangsi, FOCS 2023, arXiv 2301.00104.
  * Pointer. §I.
  * Checked. No stamp. The template is recorded in `CLAUDE.md` as reusable.
  * Page. `wiki/sources/towards-separating-cdp.md`.

* `generative-leap-unit`
  * Claim. For Gaussian multi-index models the generative leap exponent k* gives n = Θ(d^{1∨k*/2}) for index-space recovery, with a low-degree lower bound and a matching efficient upper bound.
  * Paper. Damian, Lee and Bruna, NeurIPS 2025, arXiv 2506.05500.
  * Pointer. Theorem 1 (low-degree at degree O(log² d), which needs the low-degree conjecture to speak of polynomial time) and Theorem 3 (upper bound with an unquantified constant).
  * Checked. No stamp. Page ingested from the raw PDF on 2026-08-20.
  * Page. `wiki/sources/generative-leap-multi-index.md`.

* `leap-matching-bound-csq-only`
  * Claim. The Θ̃(d^{max(Leap,2)}) SGD scaling is a conjecture, and the proved lower bound is CSQ only, d^{Leap} on the hypercube and d^{Leap/2} for Gaussian data.
  * Paper. Abbe, Boix-Adserà and Misiakiewicz, COLT 2023, arXiv 2302.11055.
  * Pointer. Conjecture 1, Proposition 2.
  * Checked. No stamp. Page ingested from the raw PDF on 2026-08-20.
  * Page. `wiki/sources/leap-complexity-sgd.md`.

* `generative-exponent-detection-only`
  * Claim. The generative-exponent lower bound of Damian et al. measures detection, not estimation, and its low-degree half is conditional on their Conjecture 3.4.
  * Paper. Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, arXiv 2403.05529.
  * Pointer. Theorem 3.2, Remark 3.3, Conjecture 3.4.
  * Checked. `CLAUDE.md` records the correction from recovery to detection against the PDF on 2026-08-20. No `date_verified`.
  * Page. `wiki/sources/generative-exponent-single-index.md`.

* `generative-below-information`
  * Claim. The generative exponent never exceeds the information exponent, and the two differ exactly when some square-integrable label transformation lowers the Hermite index.
  * Paper. Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, arXiv 2403.05529.
  * Pointer. Proposition 2.6.
  * Checked. No stamp. Page ingested from the raw PDF on 2026-08-20.
  * Page. `wiki/sources/generative-exponent-single-index.md`, `wiki/concepts/generative-exponent.md`.

* `polynomial-link-kstar-small`
  * Claim. For polynomial links the generative exponent is at most 2, and the same holds for deep networks with an r-dimensional first layer, so large-k* instances are constructions.
  * Paper. Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, arXiv 2403.05529. Damian, Lee and Bruna, NeurIPS 2025, arXiv 2506.05500.
  * Pointer. Not recorded beyond the boundary notes.
  * Checked. Boundary notes in `raw/SOURCES.md`, 2026-08-20.
  * Page. `wiki/sources/generative-exponent-single-index.md`, `wiki/sources/generative-leap-multi-index.md`.

* `estimation-settled-polynomial-links`
  * Claim. For polynomial single-index links, a layer-wise SGD procedure reaches recovery and a generalization bound at n = Θ̃(d^{(p*−1)∨1}), governed by the generative exponent p*.
  * Paper. Recorded on the page as Lee, Oko, Suzuki and Wu, NeurIPS 2024, with no arXiv. `CLAUDE.md` gives the same rate under other authors, see section 10.
  * Pointer. Abstract and general rate, no theorem number recorded.
  * Checked. No stamp. Page ingested on 2026-08-22, and `CLAUDE.md` marks the supersession of the open estimation threshold on 2026-08-27.
  * Page. `wiki/sources/sgd-reuse-info-theoretic-limit.md`.

* `xor-in-linear-samples`
  * Claim. Standard minibatch SGD on a two-layer ReLU network learns 2-sparse XOR to small population error in Θ̃(d) samples and iterations.
  * Paper. Glasgow, ICLR 2024, arXiv 2309.15111.
  * Pointer. Theorem 3.1.
  * Checked. No stamp. Page ingested on 2026-08-22.
  * Page. `wiki/sources/sgd-xor-near-optimal.md`.

* `batch-reuse-attains-generative`
  * Claim. Batch reuse does not escape the exponent family but attains the generative exponent in place of the information exponent, and the learning rate selects which regime holds.
  * Paper. Dandi, Troiani, Arnaboldi, Pesce, Zdeborová and Krzakala, ICML 2024, arXiv 2402.03220. Tsiolis, Mousavi-Hosseini and Erdogdu, NeurIPS 2025, arXiv 2510.21020.
  * Pointer. Tsiolis et al. Corollary 4.3, where the plain two-layer case is governed by IE(σ*²) and the generative exponent is reached only through the depth-D extension.
  * Checked. The 2026-08-22 log entry records the Tsiolis et al. abstract claim verified against Corollary 4.3. `CLAUDE.md` records the reading on 2026-08-27.
  * Page. `wiki/sources/learning-rate-induces-generative-exponent.md`, `wiki/sources/reusing-batches-breaks-exponents.md`.

* `exponents-are-single-pass-properties`
  * Claim. Information and leap exponent barriers are properties of single-pass gradient methods, because two steps on a reused batch learn past them in the proportional regime.
  * Paper. Dandi, Troiani, Arnaboldi, Pesce, Zdeborová and Krzakala, ICML 2024, arXiv 2402.03220.
  * Pointer. §1, T = 2 steps at n = αd, second layer frozen at initialization.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/reusing-batches-breaks-exponents.md`.

* `zero-security-citers-exponents`
  * Claim. No security or privacy paper uses the information exponent, the generative exponent, the leap, the generative leap or the noise-sensitivity exponent as the unit of an adversary's cost.
  * Paper. Citation sweep over Ben Arous, Gheissari and Jagannath, JMLR 2021, arXiv 2003.10409, Abbe et al., COLT 2022 and 2023, arXiv 2202.08658 and 2302.11055, and the two Damian et al. papers, arXiv 2403.05529 and 2506.05500.
  * Pointer. 514 citation records, zero hits at S&P, USENIX, CCS, NDSS, CRYPTO, EUROCRYPT, TCC and PoPETs, one cs.CR citer (arXiv 2310.01959) in a passing sentence, zero IACR ePrint hits.
  * Checked. Empirical sweep re-run adversarially on 2026-08-20. Not a PDF check.
  * Page. `wiki/analyses/native-asymmetry-in-learning.md`, `wiki/sources/beyond-labeling-oracles.md`.

* `surviving-cell`
  * Claim. The unclaimed theorem shape prices attacker and defender in the same exponent units at a matched budget, with the attacker restricted to the trainer's algorithm class.
  * Paper. None. A positioning claim built on the sweep above.
  * Pointer. Section 3.4 of the analysis.
  * Checked. Empirical sweep. The analysis labels the result a measurement of margins, not a security proof.
  * Page. `wiki/analyses/native-asymmetry-in-learning.md`.

* `hsu-attacker-sample-gap`
  * Claim. Every sample-based membership attack on Gaussian mean estimation needs m ≳ n²ρ² + n samples, so the attacker can need many more samples than the trainer.
  * Paper. Haghifam, Smith and Ullman, 2025, arXiv 2508.19458, no refereed venue found.
  * Pointer. Theorem 1.1, with d > c₁(n + n²ρ²), success at TPR ≥ 0.51 and FPR ≤ 0.49, and spiked-covariance hard instances.
  * Checked. Yes, `date_verified` 2026-08-22 against `raw/HSU25_SampleComplexityMIA.pdf`. Proofs in Sections 3 and 4 and Appendices A to D were read for statement and method only.
  * Page. `wiki/sources/haghifam-sample-complexity-mia.md`.

* `hsu-gap-prices-covariance`
  * Claim. The Haghifam, Smith and Ullman separation vanishes when the attacker knows the covariance, so it prices ignorance of Σ rather than attack difficulty.
  * Paper. Haghifam, Smith and Ullman, 2025, arXiv 2508.19458.
  * Pointer. Theorem 1.2, m ≳ min{n, 1/ρ²} suffices and is optimal.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/haghifam-sample-complexity-mia.md`.

* `hsu-technique-chi-square`
  * Claim. The Haghifam, Smith and Ullman lower bound uses the Ingster and Suslina χ² second-moment method over planted subspaces, which `CLAUDE.md` calls one step from a low-degree restatement.
  * Paper. Haghifam, Smith and Ullman, 2025, arXiv 2508.19458.
  * Pointer. Lower-bound technique, no section number recorded.
  * Checked. `CLAUDE.md` records the paper verified in full on 2026-08-22.
  * Page. `wiki/sources/haghifam-sample-complexity-mia.md`.

* `bpr-sq-separation-defender-fails`
  * Claim. A task exists that is efficiently learnable non-robustly but not robustly by any SQ algorithm, so the separation constrains the defender, not the attacker.
  * Paper. Bubeck, Price and Razenshteyn, ICML 2019, no arXiv recorded.
  * Pointer. Theorem 1.1, existential over a constructed planted moment-matching task, with no cryptographic assumption.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/adversarial-examples-computational-constraints.md`.

* `attacker-as-restricted-learner-occupied`
  * Claim. Modelling the attacker as a restricted-class learner and comparing two tasks is occupied in cryptographic units, and only learning-theory units remain unclaimed.
  * Paper. Canetti and Karchmer, TCC 2021. Karchmer, SaTML 2023, ePrint 2022/1039. Christiano, Hilton, Lecomte and Xu, ITCS 2025, arXiv 2409.03077. arXiv 2504.20310, authors not recorded.
  * Pointer. Not recorded per paper.
  * Checked. The covert-learning and defendability pages carry `date_verified` 2026-08-20. Karchmer and arXiv 2504.20310 are single-sourced and have no page.
  * Page. `wiki/sources/covert-learning.md`, `wiki/sources/backdoor-defense-learnability-obfuscation.md`, `wiki/analyses/native-asymmetry-in-learning.md`.

* `detection-generation-equivalence`
  * Claim. Distinguishing and likelihood improvement for learned distributions reduce to each other both ways only at exponential cost in general, and the polynomial-time reduction runs one way in a different model.
  * Paper. Alvarez-Melis, Garg and Kalai, Are GANs overkill for NLP?, NeurIPS 2022, arXiv 2205.09838.
  * Pointer. §5 Lemmas 1 and 2, §6 for the one-directional polynomial result. No runtime bound on any distinguisher in Lemmas 1 to 3 or Theorem 1. All quantities are empirical on a fixed sample, and Lemma 2 needs a bounded likelihood ratio.
  * Checked. Yes, `date_verified` 2026-08-22 against `raw/AGK22_AreGANsOverkillNLP.pdf`.
  * Page. `wiki/sources/are-gans-overkill-for-nlp.md`.

* `song-score-reduction`
  * Claim. Gaussian pancakes reduce in polynomial time to L²-accurate score estimation, so score estimation is hard wherever Gaussian pancakes are hard.
  * Paper. Song, Cryptographic Hardness of Score Estimation, NeurIPS 2024, arXiv 2404.03272.
  * Pointer. Theorem 3.1, unconditional as a reduction.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/song-cryptographic-hardness-score-estimation.md`.

* `song-black-box-obstruction`
  * Claim. Black-box use of a learned sampler cannot solve Gaussian pancakes, a result Song restates from Bruna, Regev, Song and Tang under worst-case lattice hardness rather than proves.
  * Paper. Song, NeurIPS 2024, arXiv 2404.03272.
  * Pointer. Section 1.3, item 3. Section 1.3 is a three-item list titled Future directions and has no subsections.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/song-cryptographic-hardness-score-estimation.md`.

* `song-open-bounded-discriminators`
  * Claim. Song names sampling judged by discriminators with bounded compute or memory as an open direction, and notes that a sampler facing only polynomial-time tests could output standard Gaussians.
  * Paper. Song, NeurIPS 2024, arXiv 2404.03272.
  * Pointer. Section 1.3, item 2.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/song-cryptographic-hardness-score-estimation.md`.

* `methodology-sweep-the-technique-venue`
  * Claim. Four novelty claims checked on 2026-07-26 all failed, the survivor came from a citation-graph sweep, and a novelty check must search the venue where the technique lives.
  * Paper. None. A process record.
  * Pointer. `CLAUDE.md` methodological note and the native-asymmetry analysis §3.1.
  * Checked. Not applicable.
  * Page. `CLAUDE.md`, `wiki/analyses/native-asymmetry-in-learning.md`.

* `fine-grained-terminology-trap`
  * Claim. In the privacy-preserving ML literature fine-grained usually means per-user access control, so a keyword search for fine-grained privacy returns the wrong sense.
  * Paper. None.
  * Pointer. `CLAUDE.md` terminology note.
  * Checked. Not applicable.
  * Page. `CLAUDE.md`.

## 2. Membership, reconstruction and memorization

* `shokri-has-no-game`
  * Claim. Shokri et al. contain no definition or theorem, and the membership game the literature attributes to them is Yeom et al.'s.
  * Paper. Shokri, Stronati, Song and Shmatikov, IEEE S&P 2017, no arXiv recorded.
  * Pointer. The page records zero occurrences of the words Definition and Theorem in the file.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/membership-inference-shokri.md`, `wiki/sources/privacy-risk-overfitting.md`.

* `lira-low-fpr`
  * Claim. LiRA made true-positive rate at low false-positive rate the standard membership metric, and its game is adopted from Yeom et al.
  * Paper. Carlini, Chien, Nasr, Song, Terzis and Tramèr, IEEE S&P 2022, arXiv 2112.03570.
  * Pointer. Definition 1, Section VI-A.
  * Checked. No stamp. Page ingested from the raw PDF on 2026-08-20.
  * Page. `wiki/sources/mia-from-first-principles.md`, `wiki/concepts/low-fpr-evaluation-regime.md`.

* `blind-baselines-win`
  * Claim. Attacks that never query the model beat the best reported membership attacks on eight published foundation-model evaluation datasets, so those datasets support no leakage claim.
  * Paper. Das, Zhang and Tramèr, DATA-FM workshop at ICLR 2025, arXiv 2406.16201.
  * Pointer. Abstract, p. 1.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/blind-baselines-beat-mia.md`.

* `mia-null-unsamplable`
  * Claim. Membership inference cannot prove that a production model was trained on given data, because the null hypothesis cannot be sampled without the training set or efficient retraining.
  * Paper. Zhang, Das, Kamath and Tramèr, IEEE SaTML 2025, no arXiv recorded.
  * Pointer. Abstract. A position paper, with three settings where membership inference stays sound listed in Section V.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/mia-cannot-prove-training.md`.

* `mias-near-random-on-llms`
  * Claim. Five membership attacks barely beat random guessing on one-epoch pretrained LLMs with a genuine train and test split.
  * Paper. Duan et al., COLM 2024, no arXiv recorded.
  * Pointer. Abstract, p. 1.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/do-mias-work-on-llms.md`.

* `reconstruction-robustness`
  * Claim. Reconstruction robustness scores an attack as successful when its candidate lies within a tolerance η of the target, and DP bounds it relative to a fixed baseline.
  * Paper. Balle, Cherubin and Hayes, IEEE S&P 2022, no arXiv recorded.
  * Pointer. Definition 1, Theorems 2 and 5, Corollaries 3 and 4.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/reconstructing-informed-adversaries.md`.

* `reconstruction-query-lower-bounds`
  * Claim. A white-box reconstruction adversary against a DP learner needs a number of queries bounded below as a function of the learner's privacy parameters, in plain query count with a fixed known remainder dataset.
  * Paper. Mukherjee and Lokam, 2024, arXiv 2303.16372.
  * Pointer. Theorems 1 and 2.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/query-complexity-reconstruction.md`.

* `dinur-nissim-thresholds`
  * Claim. A subset-sum database with perturbation o(n) is non-private against an exponential adversary and with perturbation o(√n) against a polynomial one, while Õ(√T(n)) noise suffices against time-T(n) adversaries.
  * Paper. Dinur and Nissim, PODS 2003, no arXiv recorded.
  * Pointer. §3.1 Exponential Adversary and §3.2 Polynomially Bounded Adversary, sibling subsections. Theorems 2 and 3 for the attacks and Theorem 5 for feasibility. The main result is a polynomial reconstruction algorithm, a linear program over subset sums with rounding at 1/2.
  * Checked. Yes, `date_verified` 2026-08-22. The venue is not stated in the PDF.
  * Page. `wiki/sources/dinur-nissim-revealing-information.md`.

* `reconstruction-equals-one-wayness`
  * Claim. Computational Narcissus resiliency is equivalent to one-wayness for functions that are efficiently computable and well-spread.
  * Paper. Cohen, Kaplan, Mansour, Moran, Nissim, Stemmer and Tsfadia, ITCS 2025, arXiv 2405.15753.
  * Pointer. Definition C.1, Definition C.4, Theorem C.5.
  * Checked. Yes, `date_verified` 2026-08-22. Appendices other than C, D and E were read only in part.
  * Page. `wiki/sources/cohen-data-reconstruction.md`.

* `narcissus-does-not-compose`
  * Claim. Narcissus resiliency does not compose in general.
  * Paper. Cohen et al., ITCS 2025, arXiv 2405.15753.
  * Pointer. Appendix D.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/cohen-data-reconstruction.md`.

* `memorization-separated`
  * Claim. Kaplan et al. pose computational against statistical memorization directly and separate the two for specific mechanisms under a Tardos prior.
  * Paper. Kaplan, Mansour, Nissim and Stemmer, ITCS 2026, arXiv 2505.23658.
  * Pointer. Definition 3.1, Definition 3.3, Lemmas 3.5, 3.7 and 4.8.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/kaplan-bayesian-memorization-reconstruction.md`.

* `suliman-conjecture-incidental`
  * Claim. Suliman et al. conjecture that gradient-equivalent mini-batches within domain constraints may be infeasible to find, but their result is empirical and the conjecture names no adversary class or assumption.
  * Paper. Suliman, Halimi, Kadhe, Baracaldo and Leith, USENIX Security 2025, arXiv 2411.05658.
  * Pointer. Contribution list, §5.3 and conclusion. Propositions 1 to 3 on the existence of gradient-equivalent batches.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/suliman-data-forging-attacks.md`.

* `fiber-target`
  * Claim. A hardness theorem for constrained fiber navigation on the training map is open, because NP-hardness is proved only for the evaluation map.
  * Paper. Jagielski, Carlini, Berthelot, Kurakin and Papernot, USENIX Security 2020, arXiv 1909.01838. Suliman et al. 2025, arXiv 2411.05658.
  * Pointer. Jagielski et al. Theorem 2, by reduction from subset sum over {0,1}^d.
  * Checked. Jagielski page `date_verified` 2026-08-20. The openness is a positioning claim in `CLAUDE.md`.
  * Page. `wiki/sources/jagielski-model-extraction.md`, `wiki/concepts/fiber-of-the-training-map.md`.

* `xiao-ind-cpa-impossibility`
  * Claim. No injective learnable obfuscation that preserves learnability with constant advantage is IND-CPA secure against an adversary who chooses the challenge distributions.
  * Paper. Xiao, Suh and Devadas, Formal Privacy Proof of Data Encoding, The Possibility and Impossibility of Learnable Obfuscation, CCS 2024, no arXiv recorded.
  * Pointer. Theorem 1, Definitions 2 and 5. The authors name two escapes, restricting the plaintext choice or denying the adversary the model trained on encoded data.
  * Checked. Yes, `date_verified` 2026-08-22. Theorems 2 to 7 on the possibility side are unverified.
  * Page. `wiki/sources/xiao-formal-privacy-proof-data-encoding.md`.

* `dp-attack-bounds-no-compute-axis`
  * Claim. The most recent unification of DP attack bounds depends only on the privacy parameters and the adversary's blind success rate, with no computational axis.
  * Paper. Swanberg, Annamalai, Hayes, Balle and Smith, 2026, arXiv 2507.08158. Also Cummings, Hod, Sarathy and Swanberg, 2024, arXiv 2405.01716.
  * Pointer. Swanberg et al. Theorem 3.2 under (ε, 0)-DP, independent priors and a decomposable metric.
  * Checked. No stamp. Pages ingested on 2026-08-20.
  * Page. `wiki/sources/adversary-aware-dp-bounds.md`, `wiki/sources/attaxonomy.md`.

## 3. Computational and restricted-class differential privacy

* `sim-cdp-implies-ind-cdp`
  * Claim. SIM-CDP implies IND-CDP and the converse is open, while the main theorem makes the weaker SIM∀∃-CDP equivalent to IND-CDP for ε in O(log κ).
  * Paper. Mironov, Pandey, Reingold and Vadhan, CRYPTO 2009, no arXiv recorded.
  * Pointer. Theorem 3, resting on Theorem 2 and the Dense Model Theorem.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/computational-differential-privacy.md`.

* `cdp-relations-regimes`
  * Claim. The SIM∀∃ to IND direction holds only for ε in O(log κ), and IND to SIM∀∃ holds for all ε and δ only with an inflated δ'.
  * Paper. Meisingseth and Rechberger, IACR Communications in Cryptology 2026, no arXiv recorded.
  * Pointer. Antecedent and Theorem 4 (the Lp-utility barrier) as recorded on the page.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/cdp-wider-parameter-regimes.md`.

* `cdp-inner-product-ot`
  * Claim. A two-party CDP protocol for inner product with additive error O(n^{1/6}) implies oblivious transfer, and errors between n^{1/6} and √n are open.
  * Paper. Haitner, Mazor, Silbak, Tsfadia and Yan, CRYPTO 2025, no arXiv recorded.
  * Pointer. Main theorem as recorded, a uniform black-box reduction.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/cdp-inner-product-implies-ot.md`.

* `cdp-inner-product-key-agreement`
  * Claim. Any non-trivially accurate two-party CDP inner-product protocol implies key agreement.
  * Paper. Haitner, Mazor, Silbak and Tsfadia, STOC 2022, no arXiv recorded.
  * Pointer. Theorem 1.6, restated as Theorem 6.3.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/two-party-dp-complexity.md`.

* `dp-sok-dimension-c`
  * Claim. Among about 200 DP variants the computational-power dimension has essentially one occupant and no evidence of practical use.
  * Paper. Desfontaines and Pejó, SoK Differential privacies, PoPETs 2020, no arXiv recorded.
  * Pointer. Definition 21, §9, Table 2.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/sok-differential-privacies.md`.

* `capacity-bounded-dp`
  * Claim. Capacity-bounded DP restricts the adversary to a function class through restricted f-divergences, and it is the nearest published privacy notion to a learning-class adversary.
  * Paper. Chaudhuri, Imola and Machanavajjhala, NeurIPS 2019, arXiv 1907.02159.
  * Pointer. Abstract. Post-processing holds only under a closure condition, and worked results cover the linear class.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/capacity-bounded-dp.md`, `wiki/concepts/capacity-bounded-privacy.md`.

* `no-ratio-privacy-notion`
  * Claim. No fine-grained or ratio-parameterized privacy notion exists in the corpus, because CDP is asymptotic and capacity-bounded DP restricts a class.
  * Paper. Mironov et al., CRYPTO 2009. Chaudhuri, Imola and Machanavajjhala, NeurIPS 2019, arXiv 1907.02159.
  * Pointer. `CLAUDE.md`, seam (b) of the compute-amount sweep.
  * Checked. No. An absence finding of the 2026-07-26 sweep.
  * Page. `wiki/sources/computational-differential-privacy.md`, `wiki/sources/capacity-bounded-dp.md`.

* `ldp-equals-sq`
  * Claim. A concept class is learnable by a local DP algorithm exactly when it is SQ learnable, and the efficiency transfer needs transparent randomizers.
  * Paper. Kasiviswanathan, Lee, Nissim, Raskhodnikova and Smith, FOCS 2008, no arXiv recorded.
  * Pointer. Abstract, Definition 5.13.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/what-can-we-learn-privately.md`, `wiki/concepts/local-differential-privacy.md`.

* `adaptive-queries-cubic`
  * Claim. If one-way functions exist, no efficient oracle holding n samples answers n^{3+o(1)} adaptively chosen statistical queries accurately.
  * Paper. Hardt and Ullman, FOCS 2014, no arXiv recorded.
  * Pointer. Theorem 1.1. Theorem 1.2 is unconditional at dimension n^{3+o(1)}.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/preventing-false-discovery-hard.md`.

* `dp-space-separation`
  * Claim. Assuming symmetric-key encryption secure against non-uniform adversaries, some task needs more space for an efficient computationally private mechanism than for a non-private one, a space bound on the mechanism.
  * Paper. Dinur, Stemmer, Woodruff and Zhou, EUROCRYPT 2023, ePrint 2023/171.
  * Pointer. Corollary 3.13 for the DP separation. Theorem 4.1, under one-way functions, for adaptive data analysis.
  * Checked. No stamp. Page ingested on 2026-08-21.
  * Page. `wiki/sources/dp-adaptive-analysis-bounded-space.md`.

## 4. Low-degree, SQ and planted-problem cryptography

* `sq-low-degree-equivalence`
  * Claim. SQ statistical dimension and the minimum degree of a good low-degree distinguisher are nearly equivalent for problems satisfying a nicenness condition, which one-shot planted clique fails.
  * Paper. Brennan, Bresler, Hopkins, Li and Schramm, COLT 2021, no arXiv recorded.
  * Pointer. §1.2, Definition 1.4.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/brennan-sq-lowdegree-equivalence.md`.

* `low-degree-counterexamples`
  * Claim. Two code-based testing problems defeat degree-O(log n) polynomials while a polynomial-time test succeeds, refuting the low-degree conjecture as Hopkins stated it.
  * Paper. Holmgren and Wein, ITCS 2021, arXiv 2004.08454.
  * Pointer. Theorem 3.1.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/holmgren-counterexamples-low-degree.md`.

* `sq-planted-clique`
  * Claim. No polynomial-time statistical algorithm detects planted clique with VSTAT(o(n²/k²)) queries, and any SQ algorithm needs n^{Ω(log n)} queries to VSTAT(n^{2−δ}/k²).
  * Paper. Feldman, Grigorescu, Reyzin, Vempala and Xiao, J. ACM 2017, no arXiv recorded.
  * Pointer. Theorem 2.9.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/feldman-statistical-algorithms-planted-clique.md`.

* `sos-planted-clique`
  * Claim. The degree-d SoS relaxation of clique has integrality gap at least n^{1/2 − c(d/log n)^{1/2}}, unconditionally.
  * Paper. Barak, Hopkins, Kelner, Kothari, Moitra and Potechin, FOCS 2016, arXiv 1604.03084.
  * Pointer. Theorem 1.1.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/barak-sos-lower-bound-planted-clique.md`.

* `pke-from-planted-clique`
  * Claim. Public-key encryption secure against polynomial-size adversaries follows from n^{(log n)^α} hardness of standard planted clique plus a noisy k-LIN conjecture over expanders.
  * Paper. Ghosal, Hair, Jain and Sahai, STOC 2025, ePrint 2025/1501.
  * Pointer. Abstract.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/pke-from-planted-clique.md`.

* `planted-clique-variants-equivalent`
  * Claim. Search and decision variants of the planted clique conjecture are equivalent by unconditional reductions, and refutation is equivalent to a separate statement.
  * Paper. Hirahara and Shimizu, STOC 2024, ECCC TR24-058 (identifier given in the compass artifact).
  * Pointer. Abstract, no single theorem recorded.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/hirahara-planted-clique-conjectures-equivalent.md`.

* `clwe-hardness`
  * Claim. CLWE is hard under a polynomial-time quantum reduction from worst-case GapSVP and SIVP, and homogeneous CLWE is hard for SQ algorithms.
  * Paper. Bruna, Regev, Song and Tang, STOC 2021, no arXiv recorded.
  * Pointer. Abstract.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/bruna-continuous-lwe.md`.

* `lattice-hardness-of-learning`
  * Claim. Weakly learning a periodic neuron, or a one-hidden-layer ReLU network of width ω(√(d log d)) under Gaussian noise, is hard for polynomial time if approximate SVP is quantum-hard.
  * Paper. Song, Zadik and Bruna, NeurIPS 2021, arXiv 2106.10744. Li, Zadik and Zampetakis, ALT 2025, arXiv 2410.03477.
  * Pointer. Song et al. Theorem 3.3 and Corollary 3.4. Li et al. §3 after Theorem 3.1.
  * Checked. No stamp. Pages ingested on 2026-08-20.
  * Page. `wiki/sources/hardness-single-periodic-neurons.md`, `wiki/sources/hardness-one-hidden-layer.md`.

* `pessiland-learning`
  * Claim. If no infinitely-often one-way function exists, every unknown adaptively changing distribution is learnable in polynomial time, among other average-case learning tasks.
  * Paper. Hirahara and Nanashima, ECCC TR23-100, 2023. The FOCS 2023 attribution is not stated in the PDF.
  * Pointer. Theorem 2.4 (equivalences with the hypothesis), Theorem 2.3 (agnostic result).
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/learning-in-pessiland.md`.

* `franz-parisi-equals-low-degree`
  * Claim. The Franz-Parisi and low-degree criteria are equivalent for Gaussian additive models, Franz-Parisi hardness implies low-degree hardness for planted sparse models, and counterexamples exist outside these classes.
  * Paper. Bandeira, El Alaoui, Hopkins, Schramm, Wein and Zadik, NeurIPS 2022, no arXiv recorded.
  * Pointer. Definition 1.3 and the model-class antecedent.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/bandeira-franz-parisi-criterion.md`.

* `lll-beats-sos`
  * Claim. LLL recovers labels and direction exactly at n = d+1 in a noiseless clustering problem where low-degree and SoS lower bounds hold up to n = Õ(d²).
  * Paper. Zadik, Song, Wein and Bruna, COLT 2022, arXiv 2112.03898.
  * Pointer. Theorem 1.1. Inverse-polynomial noise breaks the method.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/zadik-lattice-surpass-sos.md`.

## 5. Learning-theory exponents and SGD

* `information-exponent-one-algorithm`
  * Claim. The information exponent prices one algorithm, online SGD from a random start, on rank-one planted models, and says nothing about all efficient algorithms.
  * Paper. Ben Arous, Gheissari and Jagannath, JMLR 2021, arXiv 2003.10409.
  * Pointer. Definition 1.2, Assumptions A and B.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/information-exponent-online-sgd.md`.

* `merged-staircase`
  * Claim. The merged-staircase property is necessary for O(d)-sample mean-field SGD on sparse hypercube functions, since without it the risk stays bounded below.
  * Paper. Abbe, Boix-Adserà and Misiakiewicz, COLT 2022, arXiv 2202.08658.
  * Pointer. Theorem 7.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/merged-staircase-property.md`.

* `full-batch-beats-one-pass`
  * Claim. With a truncated quadratic link, full-batch GD succeeds at n ≃ d where one-pass SGD with the same activation does not.
  * Paper. Kovačević, Ji, Wu, Soltanolkotabi and Mondelli, 2026, arXiv 2602.02431.
  * Pointer. Theorems 3.1, 3.2 and 4.1.
  * Checked. No stamp. Page ingested on 2026-08-22.
  * Page. `wiki/sources/full-batch-gd-vs-one-pass-sgd.md`.

* `noise-sensitivity-exponent-amp`
  * Claim. The noise sensitivity exponent controls the size of AMP gaps in the proportional regime and does not compose with the SQ and low-degree exponents.
  * Paper. Defilippis, Krzakala, Loureiro and Maillard, 2026, arXiv 2603.17896.
  * Pointer. Definition 2.1, Theorem 3.2.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/noise-sensitivity-exponent.md`.

* `robust-single-index-unpriced-adversary`
  * Claim. Gaussian single-index models admit an efficient constant-factor agnostic learner at about d^{⌈k*/2⌉} + d/ε samples, and the label-noise adversary in the theorem carries no cost.
  * Paper. Wang, Zarifis, Diakonikolas and Diakonikolas, NeurIPS 2024, no arXiv recorded.
  * Pointer. Theorem 1.2, Assumption 1.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/robust-single-index-efficient.md`.

* `sgd-parity-near-sq-limit`
  * Claim. SGD solves (n, k)-sparse parity in about n^{α·k} iterations across the tested grid, which is an empirical finding for n up to 30 and k up to 4.
  * Paper. Barak, Edelman, Goel, Kakade, Malach and Zhang, NeurIPS 2022, arXiv 2207.08799.
  * Pointer. Empirical Finding 1, Appendix C, Theorems 4, 6 and 7 for specific schedules.
  * Checked. No stamp. Page ingested on 2026-08-22.
  * Page. `wiki/sources/hidden-progress-sgd-parities.md`.

* `scaling-laws-recipe-relative`
  * Claim. Every neural scaling law in the corpus holds for a named training recipe, and the exponent moves when the recipe moves.
  * Paper. Kaplan et al. 2020 (arXiv 2001.08361), Hoffmann et al. NeurIPS 2022, Bordelon, Atanasov and Pehlevan ICLR 2025, Sorscher et al. NeurIPS 2022.
  * Pointer. Kaplan et al. Appendix C (no theory) and Eq. 6.1, N ∝ C^{0.73}. Bordelon et al. abstract, feature learning nearly doubles the hard-task exponent.
  * Checked. Wave 6 of `raw/SOURCES.md` records the boundary notes on 2026-08-22.
  * Page. `wiki/sources/scaling-laws-neural-lm.md`, `wiki/sources/feature-learning-improves-scaling.md`, `wiki/sources/data-pruning-beats-power-laws.md`.

* `chinchilla-approach3-disputed`
  * Claim. Chinchilla's Approach 3 fit fails on reconstructed data while equal scaling of parameters and tokens survives, and the original learning-rate-decay explanation of the Kaplan discrepancy was disproved.
  * Paper. Hoffmann et al., NeurIPS 2022. Besiroglu, Erdil, Barnett and You, 2024, arXiv 2404.10102. Porian et al., NeurIPS 2024 (inside the Chinchilla page).
  * Pointer. Limits section of the Chinchilla page.
  * Checked. Besiroglu et al. page carries a banner verified against `raw/Bes24_ChinchillaReplication.pdf` on 2026-08-22.
  * Page. `wiki/sources/chinchilla-compute-optimal.md`, `wiki/sources/chinchilla-replication.md`.

* `algorithmic-progress-rate`
  * Claim. The compute needed to reach a fixed perplexity halved about every 8 months from 2012 to 2023, with a 95 percent interval of about 5 to 14 months.
  * Paper. Ho, Besiroglu, Erdil et al., NeurIPS 2024, arXiv 2403.05812.
  * Pointer. Abstract.
  * Checked. Reclassified against the primary PDF on 2026-09-03, per its `cls_reason`.
  * Page. `wiki/sources/algorithmic-progress-lm.md`.

## 6. Fine-grained and memory-bounded cryptography

* `fine-grained-conventions`
  * Claim. Compute amount without hardness is fine-grained cryptography, whose canonical definitions price the inverter at honest^{1+δ} circuit size or name a constant gap δ in word-RAM time.
  * Paper. Brzuska and Couteau, EUROCRYPT 2022. LaVigne, Lincoln and Vassilevska Williams, CRYPTO 2019. Ball, Rosen, Sabin and Vasudevan, STOC 2017.
  * Pointer. Brzuska and Couteau Definition 6, LaVigne et al. Definition 5, Ball et al. Definition 2. The conversion is δ_BC = δ_LLV/(1−δ_LLV).
  * Checked. Ball et al. `date_verified` 2026-08-22. The other two pages carry no stamp, and the conversion is marked verified in `raw/SOURCES.md`.
  * Page. `wiki/sources/fine-grained-one-way-functions.md`, `wiki/sources/pkc-fine-grained-setting.md`, `wiki/sources/average-case-fine-grained-hardness.md`, `wiki/concepts/security-gap-exponent.md`.

* `llv-gap-below-quadratic`
  * Claim. The LaVigne, Lincoln and Vassilevska Williams gap is capped strictly below quadratic, at N^{2−4/(k+2)}.
  * Paper. LaVigne, Lincoln and Vassilevska Williams, CRYPTO 2019.
  * Pointer. Boundary note in `raw/SOURCES.md`.
  * Checked. Boundary note, 2026-08-20.
  * Page. `wiki/sources/pkc-fine-grained-setting.md`.

* `merkle-ceiling-is-query-bound`
  * Claim. An eavesdropper with O(n²) oracle queries breaks every random-oracle key exchange with n honest queries, a ceiling on query gaps in an idealized model and not on time gaps.
  * Paper. Barak and Mahmoody-Ghidary, CRYPTO 2009.
  * Pointer. Abstract. `CLAUDE.md` gives the bound as (16n/δ)² queries.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/merkle-puzzles-are-optimal.md`.

* `nike-gap-ceilings`
  * Claim. The random-oracle NIKE gap is n^{K/(K−1)} and shrinks as K grows, and 3-NIKE is capped at O(n²) in Maurer's generic group model, all in query complexity.
  * Paper. Afshar, Couteau, Mahmoody and Sadeghi, EUROCRYPT 2023.
  * Pointer. Abstract, Definition 2, Theorem 21.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/fine-grained-nike-lower-bounds.md`.

* `nike-quadratic-standard-model`
  * Claim. A 4-party NIKE reaches a quadratic gap in the standard model from exponentially secure injective PRGs and sub-exponential CDH, but only N^{1.6} in Maurer's generic group model.
  * Paper. Bauer, Couteau and Sadeghi, CRYPTO 2024, ePrint 2024/834.
  * Pointer. Theorems 4 and 10.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/fine-grained-nike-revisited.md`.

* `fine-grained-barrier-pessiland`
  * Claim. If one-way functions do not exist, average-case k-SUM and Zero-k-Clique are easy for large constant k on infinitely many n.
  * Paper. Alman, Huang and Yeo, EUROCRYPT 2025.
  * Pointer. Theorem 1.2. `CLAUDE.md` adds the NSETH barrier of Ball et al. §5.2.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/fine-grained-world-without-crypto.md`.

* `dvv16-infinitely-often`
  * Claim. The NC1-side primitives of Degwekar, Vaikuntanathan and Vasudevan hold only infinitely often, and the formal theorems need ⊕L/poly ⊄ NC1 while the abstract states NC1 ≠ ⊕L/poly.
  * Paper. Degwekar, Vaikuntanathan and Vasudevan, CRYPTO 2016, ePrint 2016/580.
  * Pointer. Remark 3.1, Definitions 2.3 to 2.6 and 2.13.
  * Checked. Caveats added on 2026-08-20, Remark 3.1 verified verbatim per `raw/SOURCES.md`.
  * Page. `wiki/sources/fine-grained-cryptography.md`.

* `parity-problems-high-success-only`
  * Claim. Parity versions of k-OV, k-SUM and k-XOR are n^{Ω(√k)}-hard on average, but only for algorithms with success probability 1 − Θ(2^{−K}).
  * Paper. Dalirrooyfard, Lincoln, Saha and Vassilevska Williams, SODA 2025, arXiv 2503.21951.
  * Pointer. Theorems 1.1, 1.3, 1.4 and 1.6.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/average-case-parity-problems.md`.

* `planted-ov-conjectured`
  * Claim. Average-case hardness of planted k-OV is a conjecture, not a theorem.
  * Paper. Kühnemann, Polak and Rosen, ESA 2025.
  * Pointer. Conjecture 10.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/planted-orthogonal-vectors.md`.

* `consensus-exponent-ratio`
  * Claim. Permissionless consensus resists adversarial power T^{1−ε} against honest power T from the k-OV conjecture, in the random beacon model despite the title's standard model.
  * Paper. Ball, Garay, Hall, Kiayias and Panagiotakos, CRYPTO 2024.
  * Pointer. Abstract, Definition 1, Theorem 23.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/permissionless-consensus-fine-grained.md`.

* `sequential-functions-price-depth`
  * Claim. Sequential functions price depth rather than total work, and fine-grained PKE from them needs a VDF and iO for null circuits.
  * Paper. Guan and Montgomery, CRYPTO 2024.
  * Pointer. Definition 3.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/sequential-functions-fine-grained.md`.

* `raz-theorem-stronger-than-abstract`
  * Claim. Raz's parity lower bound holds for any branching program of width 2^{cn²} with c < 1/20 and length 2^{αn}, stronger than the n²/25 of the abstract.
  * Paper. Raz, FOCS 2016, arXiv 1602.05161.
  * Pointer. Theorem 2, Section 7. Remark 1.2 caps the encryption corollary to messages shorter than n.
  * Checked. Boundary note in `raw/SOURCES.md`, 2026-08-20. No `date_verified`.
  * Page. `wiki/sources/raz-parity-time-space.md`.

* `bsm-quadratic-ceiling-broken`
  * Claim. Bounded-storage key agreement and OT reach adversarial memory up to 2^{O(n)}, because the Dziembowski and Maurer quadratic bound holds only in a more restricted model.
  * Paper. Dodis, Quach and Wichs, EUROCRYPT 2023. The PDF is dated 22 September 2021.
  * Pointer. §1 Main Result, Theorems 7.4 and 7.7 for the lower bounds.
  * Checked. No stamp. Page ingested on 2026-08-21.
  * Page. `wiki/sources/speak-much-remember-little.md`.

* `bsm-signature-optimality`
  * Claim. Bounded-storage signatures that are suf-cma-secure force adversarial memory m = O(n²), proved through an explicit memory-bounded forger.
  * Paper. Dodis, Quach and Wichs, EUROCRYPT 2022.
  * Pointer. Theorem 7.11 with Lemma 7.13 of the 2023 paper. MAC short-tag optimality is footnote 4. Raz drives the construction through Theorem 6.2.
  * Checked. Correction filed on 2026-08-20 in `raw/SOURCES.md`. No `date_verified`.
  * Page. `wiki/sources/authentication-bounded-storage.md`.

* `bsm-space-owf-tradeoff`
  * Claim. One-way functions give bounded-storage key agreement at any polynomial space gap, and one-way functions are necessary for large space gaps.
  * Paper. Brzuska, Couteau, Egger and Quach, TCC 2024.
  * Pointer. Abstract. Theorem 3 is tight only for single-long-stream protocols, and Theorem 4 yields only non-uniform, infinitely-often one-way functions.
  * Checked. No stamp. Page ingested on 2026-08-21 from a PDF supplied by hand.
  * Page. `wiki/sources/bsm-key-agreement-owf.md`.

* `adaptive-streaming-separation`
  * Claim. One streaming problem needs polynomial space for adversarially robust algorithms and polylogarithmic space obliviously, information-theoretically.
  * Paper. Kaplan, Mansour, Nissim and Stemmer, CRYPTO 2021, arXiv 2101.10836.
  * Pointer. Theorems 1.2 and 5.10. Remark 1.4 concedes the more natural §6 variant gives only a computational separation.
  * Checked. No stamp. Page ingested on 2026-08-21.
  * Page. `wiki/sources/adaptive-vs-oblivious-streaming.md`.

## 7. Robustness, backdoors and alignment impossibility

* `undetectable-backdoors-scope`
  * Claim. Under one-way functions any training procedure admits black-box undetectable backdoors, and white-box undetectability is shown only for random Fourier features under CLWE.
  * Paper. Goldwasser, Kim, Vaikuntanathan and Zamir, arXiv 2204.06974, 2022. The FOCS 2022 attribution is not stated in the PDF.
  * Pointer. Theorems 2.1 and 2.2, Section 4.1. Random ReLU networks rest on Sparse PCA hardness.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/planting-undetectable-backdoors.md`.

* `io-backdoors-scope`
  * Claim. Any training pipeline followed by an iO step admits an undetectable backdoor, and nothing follows for models released in the clear.
  * Paper. Kalavasis, Karbasi, Oikonomou, Sotiraki, Velegkas and Zampetakis, NeurIPS 2024, arXiv 2406.05660.
  * Pointer. Definitions 2.1 and 2.3, Assumption 2.7.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/io-undetectable-backdoors-nn.md`.

* `unelicitable-no-theorem`
  * Claim. Unelicitable transformer backdoors rest on a hash-based digital locker and SHA-2 preimage resistance, and the paper contains no theorem.
  * Paper. Draguns, Gritsevskiy, Motwani, Rogers-Smith, Ladish and Schroeder de Witt, NeurIPS 2024, arXiv 2406.02619.
  * Pointer. §1.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/unelicitable-backdoors-lms.md`.

* `oblivious-backdoor-removal`
  * Claim. Backdoors can be removed without being detected when the ground truth is close to a Fourier-heavy function or to a low-degree polynomial.
  * Paper. Goldwasser, Shafer, Vafa and Vaikuntanathan, STOC 2025. The compass artifact gives arXiv 2411.03279.
  * Pointer. Definition 4.1, Theorem 6.3 (global), Theorems 7.1, 7.7 and 7.12 (local).
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/oblivious-defense-backdoor-removal.md`.

* `defendability-characterization`
  * Claim. A class is statistically ε-defendable exactly when ε = o(1/VC), efficient defendability separates from efficient learnability in the random oracle model, and polynomial-size circuits are not efficiently defendable under one-way functions and iO.
  * Paper. Christiano, Hilton, Lecomte and Xu, ITCS 2025, arXiv 2409.03077.
  * Pointer. Theorem 4.1, Theorem 5.3, Theorem 5.5, Definition 5.1. Theorem 6.1 makes polynomial-size decision trees uniform-defendable with zero example-oracle calls.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/backdoor-defense-learnability-obfuscation.md`.

* `filter-impossibility-existential`
  * Claim. There exist LLMs for which no efficient prompt filter separates harmful from benign prompts, and nothing is proved about deployed models.
  * Paper. Ball, Gluch, Goldwasser, Kreuter, Reingold and Rothblum, ICLR 2026, arXiv 2507.07341.
  * Pointer. Theorem 1 (time-lock puzzles), Theorem 2 (one-way functions plus a secret shared by the LLM and the attacker), Theorem 3 (PKE), Theorem 7 in Appendix C.1 as the formal version.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/filter-impossibility-ai-alignment.md`.

* `win-win-is-an-implication`
  * Claim. If an efficient robust classifier exists for a task but cannot be learned efficiently, one-way functions exist, and the converse licenses nothing about which tasks are hard.
  * Paper. Degwekar, Nakkiran and Vaikuntanathan, COLT 2019, arXiv 1902.01086.
  * Pointer. Theorem 2.4 (informal), Section 2.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/win-win-robust-learning.md`.

* `blpr-quadratic-residuosity`
  * Claim. Robust learning of the Bubeck, Lee, Price and Razenshteyn family is hard under quadratic residuosity through the Blum-Blum-Shub trapdoor PRG, not under one-way functions in general.
  * Paper. Bubeck, Lee, Price and Razenshteyn, 2018, arXiv 1811.06418.
  * Pointer. §3 property (c), restating Theorem 3.1.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/adversarial-examples-prg.md`.

* `computational-robustness-exceeds-it`
  * Claim. There are constructed tasks whose classifiers are robust only against polynomial-time adversaries, from one-way functions through one-time signatures.
  * Paper. Garg, Jha, Mahloujifar and Mahmoody, ALT 2020, no arXiv recorded.
  * Pointer. Theorems 8 and 14 on Constructions 7 and 13. Theorem 18 is the universal converse.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/computational-hardness-robust-learning.md`.

* `parameters-from-computational-constraints`
  * Claim. On constructed tasks, computationally bounded learners need more model parameters than information requires, assuming one-way functions.
  * Paper. Garg, Jha, Mahloujifar, Mahmoody and Wang, NeurIPS 2022, no arXiv recorded.
  * Pointer. Claims 24 and 26, Definition 2.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/overparameterization-computational-constraints.md`.

* `curse-hypothesis-not-binding`
  * Claim. The curse-of-concentration theorem is conditional on metric concentration, and that hypothesis was measured and does not bind usefully on image benchmarks.
  * Paper. Mahloujifar, Diochnos and Mahmoody, AAAI 2019, arXiv 1809.03063. Mahloujifar, Zhang, Mahmoody and Evans, NeurIPS 2019, arXiv 1905.12202.
  * Pointer. Theorem 1.1 and the Limits section. On CIFAR-10 at ε∞ = 8/255 the concentration estimate is 29.21 percent against a reported 52.96 percent attack success.
  * Checked. Limits section added on 2026-08-20. The 2019 measurement page carries `date_verified` 2026-08-20.
  * Page. `wiki/sources/curse-of-concentration.md`, `wiki/sources/empirically-measuring-concentration.md`.

* `two-senses-of-concentration`
  * Claim. Concentration names opposite properties in two literatures, metric concentration that forbids robust classifiers and small-volume concentration that permits them.
  * Paper. Pal, Sulam and Vidal, NeurIPS 2023, against Mahloujifar et al. 2019.
  * Pointer. Pal et al. Theorems 2.1 and 3.1.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/concepts/two-senses-of-concentration.md`, `wiki/sources/data-concentration-robustness-avoidable.md`.

* `universal-law-is-smooth-interpolation`
  * Claim. The universal law of robustness prices smooth interpolation below the noise level under isoperimetry, about nd parameters, and its theorem contains no adversary.
  * Paper. Bubeck and Sellke, NeurIPS 2021, arXiv 2105.12806.
  * Pointer. The statement in the introduction preceding the main theorem.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/universal-law-of-robustness.md`.

* `robust-pac-characterized`
  * Claim. The global one-inclusion dimension characterizes agnostic robust PAC learnability up to log factors, and VC classes are robustly learnable only improperly.
  * Paper. Montasser, Hanneke and Srebro, NeurIPS 2022 and COLT 2019.
  * Pointer. 2022 paper §6 near Theorem 9. 2019 paper §1 main results.
  * Checked. Yes, `date_verified` 2026-08-20 on both pages.
  * Page. `wiki/sources/robust-pac-learning-characterization.md`, `wiki/sources/vc-classes-adversarially-robustly-learnable.md`.

* `randomized-smoothing-radius`
  * Claim. Gaussian smoothing certifies an ℓ₂ radius around each input for every base classifier, with no hardness assumption.
  * Paper. Cohen, Rosenfeld and Kolter, ICML 2019, arXiv 1902.02918.
  * Pointer. Theorem 1.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/certified-robustness-randomized-smoothing.md`.

* `aioracle-security-definition`
  * Claim. An AIOracle is ε-ATK-ψ-secure when every PPT adversary has advantage at most ε in its game, and modular composition holds for components that are each complete and secure.
  * Paper. Villa, Durak, Kohno, Maharramli and Roesner, 2026, arXiv 2603.02590.
  * Pointer. Definition 3, Figure 6, Theorem 1. The confidentiality game is DPD (Algorithm 2, Figure 4).
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/extending-formalism-cryptography-ai.md`, `wiki/concepts/aioracle-framework.md`.

* `agent-oracles-not-implementable`
  * Claim. The four contextual agent-security properties rest on oracle functions that the authors state are not implementable as given, and the paper's claim is coverage of 87 surveyed papers.
  * Paper. Siu, He, Montgomery, Wang, Gong, Wang and Song, 2026, arXiv 2603.19469.
  * Pointer. §4.2 to §4.4.
  * Checked. Yes, `date_verified` 2026-08-22.
  * Page. `wiki/sources/formalizing-llm-agent-security.md`.

* `camel-measured-not-proved`
  * Claim. CaMeL contains no theorem, and its 77 percent of AgentDojo tasks solved with guarantees is a measurement on one benchmark.
  * Paper. Debenedetti et al., 2025, arXiv 2503.18813.
  * Pointer. Game PI-SEC, §4, Figure 3.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/camel-defeating-prompt-injections.md`.

* `melon-bounds-conditional`
  * Claim. MELON's only analysis is a Hoeffding bound that holds when an unverified separation of mean similarity scores around the threshold holds.
  * Paper. Zhu, Yang, Wang, Guo and Wang, ICML 2025, arXiv 2502.05174.
  * Pointer. §3.4.2.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/melon-indirect-prompt-injection.md`.

* `maxmin-rlhf-gap`
  * Claim. One Bradley-Terry reward cannot align a policy with every subgroup of a heterogeneous population, with the lower bound stated for the subgroup furthest from the aggregate.
  * Paper. Chakraborty et al., ICML 2024, arXiv 2402.08925.
  * Pointer. Lemma 1 and Theorem 1.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/maxmin-rlhf-impossibility.md`.

* `jailbreak-paradox-premise`
  * Claim. The jailbreak paradox is existential and rests on the unargued existence of a most powerful jailbreakable LLM.
  * Paper. Rao, Choudhury and Aditya, 2024, arXiv 2406.12702.
  * Pointer. Theorems 3.1 and 4.1, Definitions 4.1 and 4.2.
  * Checked. Yes, `date_verified` 2026-08-20.
  * Page. `wiki/sources/jailbreak-paradox.md`.

## 8. Extraction, proof of learning and unlearning

* `jagielski-extraction-bounds`
  * Claim. A constructed family of width-3k depth-2 ReLU networks needs Θ(p^k) queries to extract, functionally equivalent extraction is NP-hard, and SQ fidelity extraction of depth-h random networks needs exp(O(h)) samples.
  * Paper. Jagielski, Carlini, Berthelot, Kurakin and Papernot, USENIX Security 2020, arXiv 1909.01838, importing Das, Gollapudi, Kumar and Panigrahy, SODA 2020, arXiv 1904.03866.
  * Pointer. Theorems 1, 2 and 3. Das et al. Theorem 16.
  * Checked. Yes, `date_verified` 2026-08-20 for Jagielski et al., and a banner verified against the primary PDF on 2026-08-20 for Das et al.
  * Page. `wiki/sources/jagielski-model-extraction.md`, `wiki/sources/learnability-deep-random-networks.md`.

* `extraction-undefined`
  * Claim. The model-extraction literature has no formal definition of a successful attack, as Shafran et al. state from inside the field.
  * Paper. Shafran, Shumailov, Erdogdu and Papernot, TMLR 2024, arXiv 2310.01959.
  * Pointer. Section 3.2, p. 3.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/beyond-labeling-oracles.md`.

* `cryptanalytic-extraction-cost`
  * Claim. A differential attack extracted a 100,000-parameter MNIST network with 2^{21.5} queries to worst-case error 2^{−25}, an empirical cost with no lower bound.
  * Paper. Carlini, Jagielski and Mironov, CRYPTO 2020.
  * Pointer. Abstract, p. 1.
  * Checked. No stamp. Page ingested on 2026-08-21.
  * Page. `wiki/sources/cryptanalytic-extraction-nn.md`.

* `polytime-extraction-ratio-uncomputable`
  * Claim. Polynomial-time cryptanalytic extraction assumes infinite-precision arithmetic, and the attacked model's training cost is never reported, so the attack-to-training ratio cannot be computed from the paper.
  * Paper. Canales-Martínez, Chávez-Saab, Hambitzer, Rodríguez-Henríquez, Satpute and Shamir, EUROCRYPT 2024.
  * Pointer. Abstract, §5.3. Attack cost stated as 30 minutes on 256 cores and as 32 minutes for the same network.
  * Checked. Correction filed on 2026-08-20 in `raw/SOURCES.md`.
  * Page. `wiki/sources/polynomial-time-cryptanalytic-extraction.md`.

* `active-learning-is-extraction`
  * Claim. A query-synthesis active learner is an extraction adversary, stated as an observation, and the definition lower-bounds one adversary rather than upper-bounding all.
  * Paper. Chandrasekaran, Chaudhuri, Giacomelli, Jha and Yan, USENIX Security 2020, arXiv 1811.02054.
  * Pointer. Observation 1, Definition 3, Experiment 1 in §3.1, Proposition 1.
  * Checked. Correction filed on 2026-08-20 in `raw/SOURCES.md`.
  * Page. `wiki/sources/active-learning-model-extraction.md`.

* `pol-bare-inequalities`
  * Claim. Proof-of-learning compares spoofing to honest training only through bare cost inequalities stated as desiderata, with no δ-indexed family and no adversary class.
  * Paper. Jia, Yaghini, Choquette-Choo, Dullerud, Thudi, Chandrasekaran and Papernot, IEEE S&P 2021, no arXiv recorded.
  * Pointer. Proposition 1 (verifier cost at most trainer cost), Property 2 (trainer cost at most spoofer cost), Definition 2 (spoof threshold), Conjecture 1 (unproved).
  * Checked. Yes, `date_verified` 2026-08-20, rebuilt from the PDF.
  * Page. `wiki/sources/proof-of-learning.md`.

* `pol-broken-in-practice`
  * Claim. Proof-of-learning's Property 2 fails against stated verification parameters, and the attacks are constructions, not lower bounds.
  * Paper. Fang et al., IEEE EuroS&P 2023.
  * Pointer. Appendix B, Lemmas 1 to 6.
  * Checked. Banner verified against `raw/F+23_PoLMoreBroken.pdf` on 2026-08-20.
  * Page. `wiki/sources/pol-more-broken.md`.

* `polo-measured-ratio`
  * Claim. Forging PoLO costs 1.1 to 4 times honest proof generation, a measured ratio with no definition, exponent or game.
  * Paper. Deng, Jiang, Yu, Wang, Wang, Ma, Ni and Liu, 2026, arXiv 2505.12296.
  * Pointer. Abstract.
  * Checked. Banner verified against `raw/DJY+25_PoLO.pdf` on 2026-08-20.
  * Page. `wiki/sources/polo-proof-of-learning-ownership.md`.

* `pol-incentive-game-theoretic`
  * Claim. Incentive-secure proof-of-learning gives game-theoretic guarantees for rational provers under the assumption that dishonest epochs cost nothing.
  * Paper. Zhao, Fang, Wang, Chen, Su, Xiao and Zhou, 2026, arXiv 2404.09005.
  * Pointer. §3.3, Theorem 6.6.
  * Checked. Banner verified against the primary PDF on 2026-08-20. `raw/SOURCES.md` still marks the theorem content unverified.
  * Page. `wiki/sources/pol-incentive-security.md`.

* `unlearning-algorithm-level`
  * Claim. Forging adversaries exist for mean-sampler update rules, so unlearning is well-defined only at the level of the algorithm.
  * Paper. Thudi, Jia, Shumailov and Papernot, USENIX Security 2022.
  * Pointer. Theorem 3 (Existence of Forging Adversary), Corollary 2.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/auditable-unlearning-definitions.md`.

* `retrain-equivalence-ill-posed`
  * Claim. Retrain equivalence is ill-posed for local, path-oblivious unlearning when staged training leaves an order trace in the weights.
  * Paper. Yu, He, Goyal and Arora, 2025, arXiv 2510.16629.
  * Pointer. Definitions 2.1 and 2.2.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/impossibility-retrain-equivalence.md`.

* `unlearning-verification-fragile`
  * Claim. A model provider who controls mini-batch sampling can pass backdoor and reproducing verification of unlearning while keeping the information, with an attack that costs as much as naive retraining.
  * Paper. Zhang, Chen, Shen and Li, ICML 2024, arXiv 2408.00929.
  * Pointer. Proposition 4.5, Algorithms 1 and 2.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/unlearning-verification-fragile.md`.

* `repudiation-rests-on-conjecture`
  * Claim. Proof of repudiation against membership claims rests on an unproved conjecture that nearby parameters give membership-equivalent models.
  * Paper. Kong, Roy Chowdhury and Chaudhuri, 2023, arXiv 2303.03648.
  * Pointer. Definitions 4 and 5, Conjecture 1, Theorem 1.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/forgeability-and-unlearning.md`.

* `evaluation-checklist-rejects-compute`
  * Claim. The standard robustness-evaluation checklist explicitly rejects attack compute as a threat-model parameter.
  * Paper. Carlini, Athalye, Papernot, Brendel, Rauber, Tsipras, Goodfellow, Madry and Kurakin, 2019, arXiv 1902.06705, never formally published.
  * Pointer. Boundary note in `raw/SOURCES.md`. The page cites §2.2.2 for the worst-case loss definition.
  * Checked. No stamp. Page ingested on 2026-08-20.
  * Page. `wiki/sources/on-evaluating-adversarial-robustness.md`.

* `compute-monitoring-no-hard-scheme`
  * Claim. Compute monitoring defines an F-hardness clause for spoofers bounded in time, but no proof scheme is exhibited or proved F-hard.
  * Paper. Shavit, 2023, arXiv 2303.11341.
  * Pointer. Definition 1, Theorem 1 in Appendix C.2.
  * Checked. Banner verified against `raw/S23_CatchAChinchilla.pdf` on 2026-08-20.
  * Page. `wiki/sources/catch-a-chinchilla-compute-monitoring.md`.

## 9. Corrections and retractions

* `retraction-no-low-degree-security`
  * Claim. The wiki retracted, on 2026-07-25, its line that no security definition quantifies over SQ or low-degree adversaries, citing Bogdanov et al. and Abram et al.
  * Paper. Bogdanov, Jones, Rosen and Zadik, TCC 2024, arXiv 2409.16227. Abram et al., TCC 2023.
  * Pointer. Native-asymmetry analysis §3.1 and the 2026-07-25 log entry.
  * Checked. Made from web sweeps on 2026-07-25, then narrowed against the PDFs on 2026-08-22 (next entry).
  * Page. `wiki/analyses/native-asymmetry-in-learning.md`.

* `retraction-narrowed`
  * Claim. The 2026-07-25 retraction was too broad, because both papers quantify security over size-bounded circuits and neither over a low-degree adversary.
  * Paper. As above.
  * Pointer. Bogdanov et al. Propositions 4.1 and 4.3, Conjectures 1.3 and 1.4.
  * Checked. Corrected against the PDFs on 2026-08-22 in `CLAUDE.md`.
  * Page. `wiki/sources/bogdanov-low-degree-planted-subgraph.md`.

* `retraction-ngo-kim`
  * Claim. The Ngo and Kim certificates were wrongly recorded as SQ-quantified soundness, because the cheating prover is unrestricted and the SQ restriction sits on the certified algorithm and the verifier.
  * Paper. Ngo and Kim, 2026, arXiv 2607.15528.
  * Pointer. The page cites Definitions 3.1 and 3.2 and the remarks on Definition 3.2. Verifier sample complexity O(log k / τ²) in Theorem 2.
  * Checked. Retracted on 2026-08-20, verified against the PDF.
  * Page. `wiki/sources/certificates-statistical-algorithms.md`.

* `correction-yeom-definition`
  * Claim. The zero-baseline membership result is Yeom et al.'s Definition 4 and Experiment 1, not Definition 6 as an earlier note cited.
  * Paper. Yeom, Giacomelli, Fredrikson and Jha, CSF 2018.
  * Pointer. Definitions 4 and 6.
  * Checked. Corrected on 2026-08-22 in `CLAUDE.md`.
  * Page. `wiki/sources/privacy-risk-overfitting.md`.

* `retraction-comp-mem`
  * Claim. The programme's COMP-MEM marginal-advantage game is a no-op already published by Yeom, and the PPT-first and black-box-first orderings of the summer schedule invert.
  * Paper. Yeom et al. 2018, Song 2024 (arXiv 2404.03272), Groce, Katz and Yerukhimovich 2011.
  * Pointer. Summer programme amendment and native-asymmetry analysis, Implications.
  * Checked. Made on 2026-07-25 from web sweeps.
  * Page. `wiki/analyses/summer-2026-research-programme.md`, `wiki/analyses/native-asymmetry-in-learning.md`.

* `retraction-fiber-framing`
  * Claim. The fiber-of-the-training-map framing was refuted at its core by Dinur and Nissim, Cohen et al. and Kaplan et al., leaving only constrained fiber navigation on the training map.
  * Paper. Dinur and Nissim 2003, Cohen et al. 2025 (arXiv 2405.15753), Kaplan et al. 2026 (arXiv 2505.23658), Suliman et al. 2025 (arXiv 2411.05658).
  * Pointer. 2026-07-26 log entry.
  * Checked. Made on 2026-07-26 from sweep extractions, with the Dinur and Nissim details corrected on 2026-08-22.
  * Page. `wiki/concepts/fiber-of-the-training-map.md`.

* `correction-dinur-nissim`
  * Claim. Dinur and Nissim's adversary separation sits in §3.1 against §3.2, it is not the main theorem, and the OLS example often attributed to them is not in the paper.
  * Paper. Dinur and Nissim, PODS 2003.
  * Pointer. §3.1 and §3.2, abstract.
  * Checked. Corrected against the PDF on 2026-08-22.
  * Page. `wiki/sources/dinur-nissim-revealing-information.md`.

* `correction-cohen-antecedent`
  * Claim. The equivalence of computational reconstruction resilience with one-wayness is Theorem C.5, not Definition C.1, and it needs efficiently computable, well-spread functions.
  * Paper. Cohen et al., ITCS 2025, arXiv 2405.15753.
  * Pointer. Definitions C.1 and C.4, Theorem C.5.
  * Checked. Corrected against the PDF on 2026-08-22.
  * Page. `wiki/sources/cohen-data-reconstruction.md`.

* `correction-suliman-framing`
  * Claim. Suliman et al.'s title and result are an empirical re-evaluation of data forging, and the conjecture the programme adopted is incidental to it.
  * Paper. Suliman et al., USENIX Security 2025, arXiv 2411.05658.
  * Pointer. Title and headline result.
  * Checked. Corrected against the PDF on 2026-08-22.
  * Page. `wiki/sources/suliman-data-forging-attacks.md`.

* `correction-xiao-scope`
  * Claim. Xiao, Suh and Devadas prove an IND-CPA impossibility about the encoding T, not about a training map, the paper never mentions one-way functions, and its title says Learnable Obfuscation.
  * Paper. Xiao, Suh and Devadas, CCS 2024.
  * Pointer. Theorem 1.
  * Checked. Corrected against the PDF on 2026-08-22.
  * Page. `wiki/sources/xiao-formal-privacy-proof-data-encoding.md`.

* `correction-agk22`
  * Claim. The detection and generation equivalence of Alvarez-Melis, Garg and Kalai is exponential-time in general, polynomial only one way in a different model, and empirical, so the earlier note was wrong on two of four points.
  * Paper. Alvarez-Melis, Garg and Kalai, NeurIPS 2022, arXiv 2205.09838.
  * Pointer. §5 Lemmas 1 and 2, §6.
  * Checked. Corrected against the PDF on 2026-08-22.
  * Page. `wiki/sources/are-gans-overkill-for-nlp.md`.

* `correction-song-numbering`
  * Claim. Song's black-box statement and open direction are items 3 and 2 of Section 1.3, there are no subsections 1.3.1 to 1.3.3, and the black-box statement is Bruna et al.'s result restated.
  * Paper. Song, NeurIPS 2024, arXiv 2404.03272.
  * Pointer. Section 1.3.
  * Checked. Corrected against the PDF on 2026-08-22.
  * Page. `wiki/sources/song-cryptographic-hardness-score-estimation.md`.

* `correction-generative-exponent-detection`
  * Claim. The generative-exponent threshold was corrected from recovery to detection.
  * Paper. Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, arXiv 2403.05529.
  * Pointer. Remark 3.3.
  * Checked. Corrected against the PDF on 2026-08-20.
  * Page. `wiki/sources/generative-exponent-single-index.md`.

* `supersession-estimation-open`
  * Claim. The estimation threshold is no longer open for polynomial single-index links, and the earlier phrase that batch reuse escapes the exponent barriers is too strong.
  * Paper. See `estimation-settled-polynomial-links` and `batch-reuse-attains-generative`.
  * Pointer. `CLAUDE.md`, marked superseded in part on 2026-08-27.
  * Checked. Recorded in `CLAUDE.md` only, not in the log.
  * Page. `wiki/sources/sgd-reuse-info-theoretic-limit.md`, `wiki/sources/reusing-batches-breaks-exponents.md`.

* `correction-gky-exclusions`
  * Claim. The Groce, Katz and Yerukhimovich exclusions were pinned verbatim, so released models are the excluded case and the folk reading that CDP buys nothing does not apply to them.
  * Paper. Groce, Katz and Yerukhimovich, TCC 2011.
  * Pointer. End of §1.1.
  * Checked. Against the PDF on 2026-08-20.
  * Page. `wiki/sources/limits-cdp-client-server.md`.

* `correction-buhai-and-hsieh-clauses`
  * Claim. The Buhai et al. refutation and the Hsieh et al. positive counterpart were recorded with clauses, namely the rectangular polynomial-time distinguisher and the noise condition as the universal hypothesis.
  * Paper. Buhai et al., FOCS 2025, arXiv 2505.17360. Hsieh et al., STOC 2026, arXiv 2601.05850.
  * Pointer. Buhai et al. Theorem 2.4 and Remark 2.3. Hsieh et al. Theorem 1.2.
  * Checked. Against the PDFs on 2026-08-20.
  * Page. `wiki/sources/quasi-poly-low-degree-conjecture-false.md`, `wiki/sources/rigorous-implications-low-degree.md`.

* `correction-curse-limits`
  * Claim. A Limits section was added to the curse-of-concentration page, recording that its hypothesis does not bind on image benchmarks and that concentration names two opposite properties.
  * Paper. Mahloujifar, Diochnos and Mahmoody, AAAI 2019.
  * Pointer. Limits section.
  * Checked. Added on 2026-08-20.
  * Page. `wiki/sources/curse-of-concentration.md`.

* `correction-filter-existential`
  * Claim. The filter-impossibility page was restated as existential, removing a universal reading and a regulatory conclusion drawn from it.
  * Paper. Ball et al., ICLR 2026, arXiv 2507.07341.
  * Pointer. Theorems 1 to 3.
  * Checked. Against the PDF on 2026-08-20.
  * Page. `wiki/sources/filter-impossibility-ai-alignment.md`.

* `correction-win-win-inference`
  * Claim. An invalid inference was removed from the win-win page, since the theorem is an implication and believing one-way functions exist says nothing about which tasks are hard.
  * Paper. Degwekar, Nakkiran and Vaikuntanathan, COLT 2019, arXiv 1902.01086.
  * Pointer. Theorem 2.4.
  * Checked. Against the PDF on 2026-08-20.
  * Page. `wiki/sources/win-win-robust-learning.md`.

* `correction-jagielski-pol-rebuilt`
  * Claim. The Jagielski et al. and proof-of-learning pages were rebuilt from their PDFs, recovering a missing SQ sample lower bound and two of three compute inequalities.
  * Paper. Jagielski et al. 2020, arXiv 1909.01838. Jia et al. 2021.
  * Pointer. Jagielski et al. Theorem 3. Jia et al. Proposition 1, Property 2, Definition 2.
  * Checked. Against the PDFs on 2026-08-20.
  * Page. `wiki/sources/jagielski-model-extraction.md`, `wiki/sources/proof-of-learning.md`.

* `correction-quote-audit`
  * Claim. A check of every blockquote against all 164 PDFs corrected 30 passages, 16 on 13 pages being the compass artifact's prose and 14 on 11 pages failing a first automated match.
  * Paper. None.
  * Pointer. 2026-08-20 log entry and `CLAUDE.md` conventions.
  * Checked. Automated 45-character window matching with punctuation stripped. A full quote pass over pages lacking `claim_quantifier` was then still owed.
  * Page. `wiki/log.md`.

* `withdrawal-bubeck-sellke-fabrication`
  * Claim. The audit's charge that Bubeck and Sellke never state that overparametrization is necessary was withdrawn, because the phrase is in their abstract and the first search used the spelling overparameterization.
  * Paper. Bubeck and Sellke, NeurIPS 2021, arXiv 2105.12806.
  * Pointer. Abstract.
  * Checked. Withdrawn on re-audit, recorded in `CLAUDE.md`. The 2026-08-20 log entry still carries the original charge.
  * Page. `wiki/sources/universal-law-of-robustness.md`.

* `correction-gilmer-quote`
  * Claim. Gilmer et al. do write that they hypothesize the behaviour comes from high-dimensional geometry of the data manifold, and the wiki's version altered the sentence rather than inventing it.
  * Paper. Gilmer et al., ICLR Workshop 2018.
  * Pointer. Not recorded.
  * Checked. Re-audit recorded in `CLAUDE.md`.
  * Page. `wiki/sources/adversarial-spheres.md`.

* `correction-kp-poisoning-multiplicative`
  * Claim. The (k, p)-poisoning bound is the multiplicative µ to µ^{1−pk/m}, not the additive Ω(kp/m) the wiki first wrote.
  * Paper. Mahloujifar, Mahmoody and Mohammed, ICML 2019, arXiv 1809.03474.
  * Pointer. Abstract.
  * Checked. Corrected on 2026-04-23 against the PDF, and `date_verified` 2026-08-20.
  * Page. `wiki/sources/multi-party-poisoning.md`, `wiki/concepts/k-p-poisoning-model.md`, `wiki/concepts/poisoning-attacks.md`.

* `correction-raw-pdfs-replaced`
  * Claim. Ten of 45 raw PDFs had content that did not match their filename and were replaced from arXiv, IACR ePrint or ECCC.
  * Paper. None.
  * Pointer. 2026-04-23 raw audit log entry.
  * Checked. Replacements verified by first-page extraction.
  * Page. `wiki/log.md`.

* `correction-bpr-no-crypto`
  * Claim. Bubeck, Price and Razenshteyn use no cryptographic assumption and no PRF, and their secondary statistical result says a robust classifier, if one exists, is found from relatively few samples.
  * Paper. Bubeck, Price and Razenshteyn, ICML 2019.
  * Pointer. Abstract, Theorem 1.1, and the secondary result proved by a union bound over a net of robust classifiers. The Ω(√d) sample separation belongs to Schmidt et al.
  * Checked. Corrected against the PDF on 2026-08-20.
  * Page. `wiki/sources/adversarial-examples-computational-constraints.md`.

* `correction-blpr-assumption`
  * Claim. The Bubeck, Lee, Price and Razenshteyn hardness rests on quadratic residuosity, not on one-way functions, and it states no exponential separation.
  * Paper. Bubeck, Lee, Price and Razenshteyn, 2018, arXiv 1811.06418.
  * Pointer. Theorem 3.1.
  * Checked. Corrected against the PDF on 2026-08-20.
  * Page. `wiki/sources/adversarial-examples-prg.md`.

* `correction-gkvz22-merged`
  * Claim. The undetectable-backdoor summary had merged the black-box result for any model with the white-box result for random Fourier features into one claim, and the page now separates them.
  * Paper. Goldwasser, Kim, Vaikuntanathan and Zamir, arXiv 2204.06974.
  * Pointer. Theorems 2.1 and 2.2.
  * Checked. Corrected against the PDF on 2026-08-20.
  * Page. `wiki/sources/planting-undetectable-backdoors.md`.

* `correction-iO-backdoor-gap`
  * Claim. The iO backdoor paper does not claim to close the white-box gap of Goldwasser et al. or to be more general, and the post-quantum remark belongs to a cited construction.
  * Paper. Kalavasis et al., NeurIPS 2024, arXiv 2406.05660.
  * Pointer. Not recorded.
  * Checked. Corrected against the PDF on 2026-08-20.
  * Page. `wiki/sources/io-undetectable-backdoors-nn.md`.

* `correction-unelicitable-construction`
  * Claim. The unelicitable backdoor trigger uses a hash-based digital locker, and no signature scheme appears in the paper.
  * Paper. Draguns et al., NeurIPS 2024, arXiv 2406.02619.
  * Pointer. Construction section.
  * Checked. Corrected against the PDF on 2026-08-20.
  * Page. `wiki/sources/unelicitable-backdoors-lms.md`.

* `correction-pessiland-scope`
  * Claim. The Hirahara and Nanashima page no longer attributes to the paper any link to adversarial robustness, and two learning tasks it once listed have no counterpart in the paper.
  * Paper. Hirahara and Nanashima, ECCC TR23-100.
  * Pointer. Theorem 2.4.
  * Checked. Corrected against the PDF on 2026-08-20.
  * Page. `wiki/sources/learning-in-pessiland.md`.

* `correction-agent-defences`
  * Claim. MELON proves no detection guarantee, CaMeL has no theorem, the consensus-smoothing paper proves no system bound, and ADDS is a workshop submission rather than an ICML Oral.
  * Paper. Zhu et al. 2025, Debenedetti et al. 2025, Hu et al. 2026, Shpilevskiy et al. 2025.
  * Pointer. MELON §3.4.2, CaMeL §4, Hu et al. Theorem 1, ADDS PDF footer.
  * Checked. Corrected against the PDFs on 2026-08-20.
  * Page. `wiki/sources/melon-indirect-prompt-injection.md`, `wiki/sources/camel-defeating-prompt-injections.md`, `wiki/sources/rs-llm-multi-agent.md`, `wiki/sources/adds-adaptive-diffusion-smoothing.md`.

* `correction-misc-pages`
  * Claim. Pointers and statements were corrected against the PDFs on 2026-08-20 for DP-SGD, Villa et al., Holmgren and Wein, Hirahara and Shimizu, Barak and Wigderson, covert learning, zk pipelines, PixelDP and Christiano et al.
  * Paper. As named.
  * Pointer. DP-SGD moments accountant description. Villa et al. DPD, not DPP, and Definition 3 Adv ≤ ε. Holmgren and Wein built from codes, not parity. Hirahara and Shimizu refutation in a separate class. Barak and Wigderson two assumptions, not three. Covert learning uses LPN, not LWE. zk pipelines named tools absent from the paper. PixelDP one-sided bound. Christiano et al. theorem labels and the random-oracle setting of Theorem 5.3.
  * Checked. Each page carries a dated Correction note and `date_verified` 2026-08-20.
  * Page. `wiki/sources/deep-learning-differential-privacy.md`, `wiki/sources/extending-formalism-cryptography-ai.md`, `wiki/sources/holmgren-counterexamples-low-degree.md`, `wiki/sources/hirahara-planted-clique-conjectures-equivalent.md`, `wiki/sources/pkc-from-different-assumptions.md`, `wiki/sources/covert-learning.md`, `wiki/sources/zk-verifiable-ai-pipelines.md`, `wiki/sources/certified-robustness-differential-privacy.md`, `wiki/sources/backdoor-defense-learnability-obfuscation.md`.

* `correction-boundary-notes`
  * Claim. Boundary notes in `raw/SOURCES.md` were corrected for Wang et al. NIKE (two constructions do state ratios), Dodis, Quach and Wichs 2022 (optimality is Theorem 7.11 for signatures), Dalirrooyfard et al. (cryptography is not mentioned rather than disclaimed) and Kaplan et al. 2021 (the streaming algorithm is the space-bounded adversary inside the proof).
  * Paper. As named.
  * Pointer. `raw/SOURCES.md`, corrected rows.
  * Checked. Filed on 2026-08-20 as post-ingest verification.
  * Page. `wiki/sources/nike-without-idealized-assumptions.md`, `wiki/sources/authentication-bounded-storage.md`, `wiki/sources/average-case-parity-problems.md`, `wiki/sources/adaptive-vs-oblivious-streaming.md`.

* `correction-venues`
  * Claim. Venue attributions not stated in the PDFs were flagged, namely FOCS for Goldwasser et al. 2022 and for Hirahara and Nanashima, CVPR for Immune, EUROCRYPT 2023 for Dodis, Quach and Wichs, whose PDF is dated 2021, and ICML Oral for ADDS.
  * Paper. As named.
  * Pointer. Front-matter `venue` fields.
  * Checked. Against the PDFs on 2026-08-20.
  * Page. `wiki/sources/planting-undetectable-backdoors.md`, `wiki/sources/learning-in-pessiland.md`, `wiki/sources/immune-rlhf-jailbreak-defense.md`, `wiki/sources/speak-much-remember-little.md`, `wiki/sources/adds-adaptive-diffusion-smoothing.md`.

* `correction-quote-rotation`
  * Claim. Four classification rows had been rotated by one page so that each held the next paper's evidence quote, and the quotes were re-extracted.
  * Paper. Bordelon et al. 2025, Sorscher et al. 2022, Busbridge et al. 2025, Joshi et al. 2025.
  * Pointer. `cls_reason` fields.
  * Checked. Corrected on 2026-08-27. The algorithmic-progress row was reclassified against its PDF on 2026-09-03 for the same fault.
  * Page. `wiki/sources/feature-learning-improves-scaling.md`, `wiki/sources/data-pruning-beats-power-laws.md`, `wiki/sources/distillation-scaling-laws.md`, `wiki/sources/single-index-harmonic-decomposition.md`, `wiki/sources/algorithmic-progress-lm.md`.

## 10. Conflicting records found while mapping

* `conflict-polynomial-link-authors`
  * Claim. `CLAUDE.md` attributes strong recovery at Θ̃(d^{(p*−1)∨1}) for polynomial single-index links to Arnaboldi, Ostrovskii, Sun and Wu, arXiv 2406.01581, while the only wiki page with that rate records Lee, Oko, Suzuki and Wu, NeurIPS 2024, with no arXiv.
  * Paper. As stated.
  * Pointer. `CLAUDE.md`, superseded-in-part paragraph.
  * Checked. No record reconciles the two.
  * Page. `wiki/sources/sgd-reuse-info-theoretic-limit.md`.

* `conflict-ngo-kim-pointer`
  * Claim. `CLAUDE.md` places the Ngo and Kim unrestricted prover in Definition 1, while the page places it in Definitions 3.1 and 3.2.
  * Paper. Ngo and Kim, arXiv 2607.15528.
  * Pointer. As stated.
  * Checked. Both say verified on 2026-08-20.
  * Page. `wiki/sources/certificates-statistical-algorithms.md`.

* `conflict-native-asymmetry-uncorrected`
  * Claim. The native-asymmetry analysis body still cites Song §1.3.3 and §1.3.2, Yeom Definition 6, Ngo and Kim as SQ-quantified soundness, and Alvarez-Melis et al. as polynomial and two-way, all later corrected elsewhere.
  * Paper. As named.
  * Pointer. Analysis §1 to §3.4. Only the Alvarez-Melis passage carries an in-place correction note.
  * Checked. Not applicable.
  * Page. `wiki/analyses/native-asymmetry-in-learning.md`.

* `conflict-stale-index-and-log`
  * Claim. `wiki/index.md` and the 2026-07-26 log entry still describe Dinur and Nissim as §3 against §4 with the separation as main theorem, and the index calls the Xiao et al. page unread.
  * Paper. Dinur and Nissim 2003, Xiao, Suh and Devadas 2024.
  * Pointer. `wiki/index.md`, 2026-07-26 batch table.
  * Checked. The source pages were corrected on 2026-08-22, and the log is append-only by rule.
  * Page. `wiki/index.md`, `wiki/log.md`.

* `conflict-sources-md-rows`
  * Claim. `raw/SOURCES.md` still describes Alvarez-Melis et al. as both directions against a bounded distinguisher class, and gives the Xiao et al. title as Learnable Encryption.
  * Paper. Alvarez-Melis, Garg and Kalai 2022, Xiao, Suh and Devadas 2024.
  * Pointer. Wave 3 and Wave 4 rows.
  * Checked. `CLAUDE.md` and the pages hold the corrected versions.
  * Page. `raw/SOURCES.md`.

* `conflict-page-counts`
  * Claim. `CLAUDE.md` gives 110 sources, 62 concepts and 84 entities as of 2026-08-20, the log gives 156, 83 and 111 for that date, and the folders hold 200, 83 and 116.
  * Paper. None.
  * Pointer. `CLAUDE.md` Role section, 2026-08-20 log entry.
  * Checked. Folder counts taken on 2026-10-25.
  * Page. `CLAUDE.md`, `wiki/log.md`.

* `conflict-verification-dates`
  * Claim. Several pages carry a `date_verified` earlier than their `date_ingested`, for example Yeom et al., Shokri et al., Balle et al. and LAMP, verified 2026-08-20 and ingested 2026-08-22.
  * Paper. None.
  * Pointer. Front matter.
  * Checked. Not applicable.
  * Page. `wiki/sources/privacy-risk-overfitting.md`, `wiki/sources/membership-inference-shokri.md`, `wiki/sources/reconstructing-informed-adversaries.md`, `wiki/sources/lamp-gradient-inversion.md`.
