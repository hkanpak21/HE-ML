# Round 01, summary: hard-problem mappings

Discussant: sol again, argon quota (argon is out of quota until about 2026-10-27 13:30,
so the alternation waits). Verdicts: 12 ACCEPT, 5 REVISE, 0 REJECT, BLOCKING 5.

What changed. The builder answered all twelve challenges of round 00; sol closed eleven
of them and kept `ch-mapping-price-types` open for one table row. The extraction aim is
now `thm-extraction-exponent-price`: an SQ extractor of a released single-index predictor
with known bounded link $m$, answering random inputs with Gaussian noise, needs
VSTAT$(c\,d^{k^*(m)/2})$ for weak fidelity with outputs bounded by one; a sample-based
extractor matches; when the labels are a channel of the regression function the
extractor's exponent is at most the trainer's; and for the law $P_\natural$ of
$(Z,Z\varepsilon)$ with $\Pr[\varepsilon=1\mid Z]=(1+\mathrm{sgn}(Z)e^{-Z^2/2})/2$ the trainer
recovers the direction from $O(d)$ records while the extractor of the released Bayes
predictor $\lvert z\rvert e^{-z^2/2}$ needs VSTAT$(c\,d^2)$. sol verified the lower bound
step by step (finite $\chi^2$ information of noisy answers, the code, FGRVX17 Theorem 3.7
with Lemma 3.10, the fidelity-to-detection reduction, the parameters) and the level-set
lemma behind the exponent 4, and judged the construction worth the space. The backdoor
conjecture was replaced by three statements, of which two are accepted: white-box
detection of a planted weight law is exactly NGCA testing at the trainer's width
(`prop-weight-testing-equals-white-box-detection`), and the auditor of a planted layer
is a split server, transposed (`lem-feature-matrix-transpose`). The definition got its
transfer lemma, accepted, and a learner-side SQ transfer that turns every SQ testing
bound into a property-inference bound against unbounded attackers of a 1-bit learner.

Slugs with verdict ACCEPT in round 01 (accepted once the space ends with BLOCKING 0):
`fact-jagielski-extraction-query-bounds`, `fact-gkvz22-backdoor-scope`,
`fact-frozen-gaussian-layer-collision-hardness`,
`fact-instance-encoding-privacy-learnability`,
`fact-chlx25-defendability-characterization`, `fact-active-learning-is-extraction`,
`lem-mapping-transfer`, `lem-level-set-moment-balance`,
`prop-weight-testing-equals-white-box-detection`, `lem-feature-matrix-transpose`, and the
withdrawals `conj-extraction-priced-by-generative-exponent` and
`conj-backdoor-detection-is-ngca`. From round 00, `fact-generative-exponent-post-processing-monotone`.

Challenges open, all blocking, answered in round 02.

| challenge | object | point |
| --- | --- | --- |
| `ch-zero-trigger-variance` | `lem-sparse-pca-backdoor-width-price` (c) | the perturbed input can vanish; the deviation event then has probability one |
| `ch-mapping-price-types` | `def-hard-problem-mapping`, table | the extraction row omits the linear sample floor of DPLB24 Theorem 4.1 |
| `ch-one-bit-success-constant` | `prop-learner-side-sq-transfer` (b) | FGRVX17 Theorem 3.16 prints $(2\alpha+1)^2$ where its proof gives $(2\alpha-1)^2$ |
| `ch-extraction-sign-confidence` | `thm-extraction-exponent-price` (b) | sign selection with $O(\eta^{-2})$ pairs cannot give confidence $1-2e^{-d^{c'}}$ |
| `ch-gram-test-running-time` | `prop-gram-sufficiency-rotation-invariant` (i) | the construction adds polynomial overhead to the test's own time |

Nonblocking remarks to carry: the key-free comparison of the lemma should use a radial or
independently drawn direction; an arbitrary known link need not have a computable
denoiser, so the experiment should restrict the link; DPLB24 Theorem 6.1 is sufficiency,
not optimality; Algorithm 1 fixes a line, and the sign of $\hat w$ should be randomized for
a uniform vector.

## For the registers

New facts.

- `fact-active-learning-is-extraction` is verified in the PDF: CCGJY20 Definitions 2 and 3,
  Experiment 1, Observation 1, Proposition 1 (read full, 2026-10-25, this space). sol adds
  that Proposition 1 needs fresh independent answer randomness at every repetition.
- A correction to FGRVX17, to attach to `fact-fgrvx17-planted-clique-sq-bound`: Theorem
  3.16's bound is $m\ge\min\{d(2\alpha-1)/2,(2\alpha-1)^2/(48\bar\gamma)\}$; the printed
  $(2\alpha+1)^2$ contradicts the proof (simulation error $\delta=(2\alpha-1)/4$ at
  VSTAT$(m/\delta^2)$) and the theorem's own case $\alpha=2/3$. Found by sol, checked by the
  builder in the PDF.

Corrections to existing facts.

- `fact-instance-encoding-privacy-learnability`: the proof of Theorem 5 (Appendix A.3)
  also orders the two acceptance probabilities the wrong way; its instruction to repeat
  training until the true encoded error meets a threshold is not a finite-sample procedure,
  so an experiment must price validation (sol).
- `fact-frozen-gaussian-layer-collision-hardness`: Corollary 3's ranges are sufficient;
  necessity is not shown (sol).

Search rows. None new in this round.

Problems.

- `prob-same-units-matched-budget-separation` and `conj-same-units-gap`: for extraction,
  `thm-extraction-exponent-price` (d) gives an attacker whose SQ sample exponent is twice
  the trainer's, in learning-based extraction of a single-index predictor with a known link
  (heuristic as a sample comparison). A candidate entry in `tried:` or `history:`.
- `prob-separation-against-jagielski-sq-bound`: the same theorem is an SQ extraction bound
  for a trained model priced in the trainer's records, the comparison that JCBKP20 Theorem
  3 does not make.
