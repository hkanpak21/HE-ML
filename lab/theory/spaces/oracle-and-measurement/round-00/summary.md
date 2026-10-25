# Round 00, oracle and measurement, summary

Date 2026-10-25. Discussant argon (`discussant-argon.md`). Verdicts: ACCEPT 7, REVISE 7, REJECT 1.
BLOCKING 12.

The round read eight library papers on auditing, proof of learning, unlearning and reruns
(CCNSTT22, NHSBTJCT23, AKOOMS24, HSU25, JYCDTCP21, ZCSL24, TJSP22, BCH22), filled their notes,
and stated twelve facts and three aims. Argon accepted seven facts and asked for five corrections
of reading, each of which is right. A $(\varepsilon,\delta)$ audit is sound only with a threshold fixed
outside the evaluation sample, and the end-to-end composition uses PLD under subsampling. Enumerating a
finite seed space gives the marginal laws and not the top oracle. Theorem 4.1 of HSU25 needs its dimension
bound. Table I of JYCDTCP21 gives means, and the spread it implies sits near one only below about
$0.95\,d_{\mathrm{ref}}$ for ResNet-20 and lower for the other settings. Algorithm 2 of ZCSL24 costs less
than one run. For the aims, argon found that claim 2 of def-seed-access-modes is false for the target
$\epsilon_0(\Delta)$ and true for the bottom-oracle divergence, and that a coupling must also be independent
of the release noise. It rejected conj-paired-advantage-price as common random numbers, and showed that a
profile of an unrestricted class is flat in the run budget for a fixed learning function. It gave a sharper
lower bound for conj-exact-twin-price, $(1-\alpha')\ln((1-\alpha')/\alpha)/(-\ln(1-\epsilon_{\mathrm{acc}}))$,
and an upper bound for the every-record certificate with no union bound. It also named library papers the
round missed, of which SAB24 (Srivastava, Arora and Boneh, NeurIPS 2024) bears on realization and is read in
round 01. Every challenge is answered by name in `round-01/builder.md`.

The first argon call failed with exit 0 and no output, because the prompt named files outside the
repository (FORMAL_SECURITY and the PDF symlink). A one-line diagnostic `agy` call confirmed that argon
reads in-repo files. The second call, with in-repo paths only, is the discussant file of this round. Both
calls appended a row to `lab/theory/discussants.csv`, and the first row records exit 0 for a call that
produced nothing.

Slugs whose verdict was ACCEPT: fact-lira-priced-in-training-runs, fact-audit-independent-batches,
fact-one-shot-estimate-consistency, fact-pol-bare-cost-inequalities, fact-unlearning-algorithm-level,
fact-balle-known-initialization-reconstruction, fact-known-initialization-separates-membership. None is
eligible for status accepted, since the round ends with blocking challenges.

Challenges open after this round, all answered in round 01. Blocking: ch-gdp-audit-pld-and-threshold,
ch-finite-seed-not-top-oracle, ch-known-covariance-dimension-bound, ch-rerun-spread-threshold-mismatch,
ch-subset-forging-below-one-run, ch-generic-oracle-open-and-meter, ch-coupling-soundness-target-and-noise,
ch-meter-oracle-cost-not-compute, ch-paired-price-degenerate-test, ch-profile-band-conditional-advantage,
ch-exact-twin-missing-hypotheses, ch-exact-twin-target-coupling-contradiction. Non-blocking:
ch-lira-offline-and-random-subset, ch-shared-batch-marginal-vs-paired, ch-one-shot-jeffreys-and-steinke,
ch-pol-random-oracle-plugin, ch-balle-theorems-and-shadow-price, ch-missing-auditing-and-nondeterminism-literature,
ch-seed-attack-already-known, ch-paired-price-elementary-bernstein, ch-exact-twin-sharper-bounds.

## For the registers

New facts, each read in the library PDF on 2026-10-25 by this space, with the note filled.

- fact-gdp-audit-observation-count. NHSBTJCT23, Eq. (9), Eq. (12), §4.1 with Fig. 3, §5.5, §6.4 with
  Fig. 11. The Gaussian-DP audit is tight with $10^3$ white-box observations where the
  $(\varepsilon,\delta)$ audit needs near $10^8$. The black-box audit uses 1,000 runs per world and reaches
  about 1.6 at theoretical 8. Soundness needs a threshold fixed outside the evaluation sample (§5.2). The
  end-to-end figure composes per-step bounds by Gaussian DP without subsampling and by PLD with it, a
  heuristic step. Corrected wording in `round-01/builder.md`.
- fact-audit-independent-batches. NHSBTJCT23 §5.1 and §6.1. Independent batches across worlds, no
  difference with identical batches, shared initialization, fresh seeds for the rest.
- fact-small-seed-space-breaks-dp. NHSBTJCT23 §6.3, Violation 2 and Fig. 8.
- fact-one-shot-estimate-consistency. AKOOMS24 Theorem 3.3 (asymptotic in $d$ at fixed $\sigma$ and
  $\delta$), §5 (ceiling 6.24 of the 95% lower bound at 1,000 canaries, Jeffreys interval for the
  false-negative rate and the exact null for the false-positive rate), §5.3.
- fact-rerun-reproduction-error. JYCDTCP21 Theorem 1 and Table I. Corrected wording in `round-01/builder.md`.
- fact-known-initialization-separates-membership. BCH22 Appendix A, Fig. 11.
- fact-controlled-nondeterminism-exact-replication, proposed in round 01 from SAB24 §6.

Corrections and verifications of existing facts.

- fact-lira-priced-in-training-runs. Pointer: §IV-C (Algorithm 1, one bank for every target), §V-A with the
  caption of Fig. 5 ($N=256$, and 64 for ImageNet), §VI-B with Fig. 9. Read in full on 2026-10-25 by the spaces
  statistical-limits and oracle-and-measurement. Status recorded can become verified.
- fact-hsu-membership-sample-gap. The matching attack is Theorem 3.3, not Theorem 3.2. Theorem 1.1 is the
  informal version of Theorem 3.1, and Theorem 1.2 of Theorem 4.1. The library PDF is arXiv v1 of 26 August
  2025. Theorem 4.1 proves impossibility with known covariance only for $d<c(n+n^2\rho^2+n^2/m)$, so two
  samples suffice in dimension of order $n^2$ and above (argon, from the statement).
- fact-pol-bare-cost-inequalities. Verified in JYCDTCP21: Property 1 is $\mathbb E[C_V]\le\mathbb E[C_T]$,
  Property 2 is $\mathbb E[C_T]\le\mathbb E[C_A]$, Definition 1 is the tuple $(W,I,H,A)$, Conjecture 1 in §VII.
- fact-unlearning-verification-fragile. Verified in ZCSL24: Definition 4.1, Proposition 4.2 (exact replay at
  $\varepsilon=0$ for Algorithm 1), Proposition 4.4 (Algorithm 2 at $\varepsilon>0$), Proposition 4.5 (Algorithm 1
  costs one retraining, Algorithm 2 a fraction of one). The text calls them Theorems 4.2 to 4.5.
- fact-unlearning-algorithm-level. Verified in TJSP22: Theorems 2 and 3 and Corollary 2.
- fact-balle-known-initialization-reconstruction. Add the pointer to the table of factors of §VI, row "Random
  initialization". The prose of Appendix A inverts the order of Table III. Argon adds that Corollary 4 of BCH22,
  $\gamma=\exp(-(\sqrt{\log(1/\kappa)}-\sqrt\rho)^2)$, has the functional form $\Upsilon_{\mathfrak e}$ of
  thm-bounded-deviation-transfer (a), both from a Hölder change of measure. That is prior work for the transfer
  and belongs in its prior-work line.

Search rows.

- search-oracle-measurement-library-auditing, 2026-10-25. Question: what do the library's auditing,
  proof-of-learning, unlearning and nondeterminism papers prove on the run price of measuring leakage and on reruns
  at one seed? Tool: grep of `lib/literature/ledger.csv`, of the PDF file names under `lib/literature/pdfs/` and
  of `sink/formalizing/searches.md` and `facts.md`. Query: "audit, one run, tight, shadow, proof of learning,
  unlearning, nondeterminism, reproducibility, seed". Scope: the library of 590 papers. Hits: NHSBTJCT23,
  AKOOMS24, CEPS24, DM22, LLLKPMW24, HSU25, CCNSTT22, JYCDTCP21, FJTYCDCP23, ZCSL24, TJSP22, DJYWWMNL26, BCH22,
  KBNM24. Kept: the eight read, and SAB24, XD23, MSS23 and ZDKT25 from argon's review. Coverage: partial.
  Steinke, Nasr and Jagielski (NeurIPS 2023), Jagielski, Ullman and Oprea (NeurIPS 2020) and Gilbert and
  McMillan (Allerton 2018) are not in the library. Updates search-coupling-certificate-novelty and
  search-record-level-certificate-prior.

Problems and library work.

- Papers to place: Steinke, Nasr and Jagielski, Privacy auditing with one (1) training run, NeurIPS 2023, arXiv
  2305.08846. Jagielski, Ullman and Oprea, Auditing differentially private machine learning, NeurIPS 2020. Gilbert
  and McMillan, Property testing for differential privacy, Allerton 2018, arXiv 1806.06427, which the accepted
  theory cites with theorem numbers.
- prob-coupled-reruns-rarely-differ. Evidence for its `literature:` line: JYCDTCP21 Table I (whole GPU reruns at
  one seed end near $d_{\mathrm{ref}}$ apart in $\ell_2$, one step nearly coincides) and SAB24 §6 (identical
  reruns on one GPU type with deterministic settings, divergence across GPU types, exact replication across three
  types by logged rounding at 1.2 to 1.7 times the training time).
- Tooling defect for the integrator. `discuss.sh` logs exit 0 when `agy` produces no output, and `agy` in headless
  plan mode refuses reads outside the repository. A hand-over note is in the shared notes folder of this session
  group.
