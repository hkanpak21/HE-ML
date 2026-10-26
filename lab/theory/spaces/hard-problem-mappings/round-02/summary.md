# Round 02, summary: hard-problem mappings

Discussant: sol again, argon quota (argon is out of quota until about 2026-10-27 13:30).
The first sol call of this round, on 2026-10-25 at about 23:40, failed on a usage limit
(row with exit 1 in `discussants.csv`); it was retried after the reset, on 2026-10-26 at
02:36, and succeeded. Verdicts: 5 ACCEPT, 0 REVISE, 0 REJECT, BLOCKING 0. The space stops
here: this is its last round in the milestone, and its verdict has BLOCKING 0.

What changed. The builder answered the five blocking challenges of round 01 and restated
the five objects that had verdict REVISE. sol closed all five and accepted every object.
`lem-sparse-pca-backdoor-width-price` now handles the zero input and compares the trigger
with a radial, key-free perturbation: for a unit input orthogonal to the key, the trigger
$x+\lambda s$ in the backdoored network and the input $(1+\lambda')x$, with
$\lambda'=\sqrt{1+\lambda^2(1+\theta)}-1\le\lambda\sqrt{1+\theta}$, in either network, have
identical preactivation laws. In the regime where GKVZ22's spike escapes the coordinate
test, the key is worth a factor $\sqrt{1+\theta}<1+\theta_*/2$ in input length. The table of
`def-hard-problem-mapping` now gives extraction one row per regime, with the linear
sample floor of DPLB24 Theorem 4.1. `prop-learner-side-sq-transfer` uses the corrected
constant $(2\alpha-1)^2$ of FGRVX17 Theorem 3.16. `thm-extraction-exponent-price` (b)
chooses the sign on $O(\Delta_m^{-2}(M+\sigma)^2\log(1/\delta_s))$ fresh pairs and holds with
probability $1-2e^{-d^{c'}}-\delta_s$. `prop-gram-sufficiency-rotation-invariant` charges
the original test's time plus $O(m^2d+d^3)$ operations.

Slugs accepted (latest verdict ACCEPT, the space's last round has BLOCKING 0), proposed for
the booklet with this status.

| slug | kind | status for the booklet | round of the accepting verdict |
| --- | --- | --- | --- |
| `thm-extraction-exponent-price` | theorem | accepted | 02 |
| `lem-level-set-moment-balance` | lemma | accepted | 01 |
| `prop-learner-side-sq-transfer` | proposition | accepted | 02 |
| `lem-mapping-transfer` | lemma | accepted | 01 |
| `def-hard-problem-mapping` | definition | accepted | 02 |
| `lem-sparse-pca-backdoor-width-price` | lemma | accepted | 02 |
| `prop-weight-testing-equals-white-box-detection` | proposition | accepted | 01 |
| `prop-gram-sufficiency-rotation-invariant` | proposition | accepted | 02 |
| `lem-feature-matrix-transpose` | lemma | accepted | 01 |
| `fact-generative-exponent-post-processing-monotone` | fact | borrowed (DPLB24) | 00 |
| `fact-jagielski-extraction-query-bounds` | fact | borrowed (JCBKP20, DGKP20) | 01 |
| `fact-gkvz22-backdoor-scope` | fact | borrowed (GKVZ22) | 01 |
| `fact-frozen-gaussian-layer-collision-hardness` | fact | borrowed (BRV26) | 01 |
| `fact-instance-encoding-privacy-learnability` | fact | borrowed (CDGJMMSTT21) | 01 |
| `fact-chlx25-defendability-characterization` | fact | borrowed (CHLX25) | 01 |
| `fact-active-learning-is-extraction` | fact | borrowed (CCGJY20) | 01 |
| `conj-extraction-priced-by-generative-exponent` | conjecture | withdrawn, superseded by `thm-extraction-exponent-price` | 01 |
| `conj-backdoor-detection-is-ngca` | conjecture | withdrawn, replaced by the three weight-law statements | 01 |

The full statements and proofs are in `round-01/builder.md` for the objects accepted there,
and in `round-02/builder.md` for the five accepted here (the proof of
`thm-extraction-exponent-price` (a), (c) and (d) is in round 01 and is not repeated in
round 02).

Challenges open. None blocking. sol's nonblocking remarks, to apply at merge as wording:
in part (d) of the lemma's proof the rounded mean $0.738$ enters an equality that should be
an inequality (the exact mean is slightly below, so the bound is conservative), and the
clean input's negativity also rests on concentration, not on its mean alone; "no backdoor
content" refers to Appendix A's claimed guarantees, not to every repair of the
construction; the covariance display in the proof of the theorem's part (b) sums over
Hermite degrees $j\ge1$; evenness of the link is meant up to Gaussian null sets; the table's
exponents assume fixed link, noise, accuracy and confidence. Open questions kept with their
objects: the cost of computing the denoiser in the theorem's part (b), and the probe
complexity and test stability in the Gram statement.

Simplified merge, after Halil's instruction of 2026-10-25 night ("simplfy whenever
possible", relayed by the integrator). The booklet needs only what carries a result.

- Keep as the space's one clean mapping: `thm-extraction-exponent-price`, with
  `lem-level-set-moment-balance` as its only lemma and
  `fact-generative-exponent-post-processing-monotone` as its only new borrowed fact.
- Keep `def-hard-problem-mapping`, cut to its first nine items with no table. Fold
  `lem-mapping-transfer` into it as one sentence (it is the definition read forward).
- Keep `prop-learner-side-sq-transfer` as the general form of
  `lem-sq-learner-post-processing`, which becomes its planted-biclique instance.
- For weight-law tampering keep one statement, `prop-weight-testing-equals-white-box-detection`.
  `prop-gram-sufficiency-rotation-invariant` and `lem-feature-matrix-transpose` stay in the
  round files and become one remark under it.
- Keep `lem-sparse-pca-backdoor-width-price` with `fact-gkvz22-backdoor-scope`, since it
  corrects a literature mapping.
- Send the other facts (`fact-jagielski-extraction-query-bounds`,
  `fact-frozen-gaussian-layer-collision-hardness`,
  `fact-instance-encoding-privacy-learnability`,
  `fact-chlx25-defendability-characterization`, `fact-active-learning-is-extraction`) to
  the registers only, not to the booklet, and record the two withdrawn conjectures in the
  History chapter only.

Decisions for Halil.

1. The headline separation lives in learning-based extraction, where the extractor sees the
   released model only on random inputs; with chosen inputs it disappears. Whether that
   game is one he wants priced is his call.
2. The carrier rule of `def-hard-problem-mapping` counts mappings carried by the record law,
   by the honest randomness of a standard procedure (BRV26's Gaussian layer), and by the
   choice of a trainer who plants (GKVZ22's pancake weights), and excludes only a
   key-dependent change the designer makes for security. Whether this reading of "a
   cryptographic plug-in does not count" is his.

## For the registers

New results, proposed for `sink/formalizing/results.md`, all proven in round files,
accepted by sol, unchecked by Halil, oracle n/a (no result uses the learning oracle):
`thm-extraction-exponent-price`, `lem-level-set-moment-balance`,
`prop-learner-side-sq-transfer`, `lem-mapping-transfer`, `def-hard-problem-mapping`,
`lem-sparse-pca-backdoor-width-price`, `prop-weight-testing-equals-white-box-detection`,
`prop-gram-sufficiency-rotation-invariant`, `lem-feature-matrix-transpose`. Where:
`HE-ML:lab/theory/spaces/hard-problem-mappings/round-01/builder.md` and `round-02/builder.md`.

New facts and corrections: as listed in the summaries of rounds 00 and 01. No new fact in
this round.

Search rows: none in this round.

Problems.

- `prob-reduce-security-to-known-learning-problems`: a third reduction now exists, learning-based
  extraction onto the single-index problem of the released link, with an SQ separation of
  exponent 2 against the trainer (`thm-extraction-exponent-price`).
- `prob-same-units-matched-budget-separation` and `conj-same-units-gap`: an attacker whose
  SQ sample exponent is twice the trainer's, for extraction, not membership.
- `prob-separation-against-jagielski-sq-bound`: answered in part, for trained single-index
  predictors with a known link.
- A new candidate problem: does the separation survive a fitted network that approximates
  the release in $L^2$, and does it hold for polynomial-time extractors under a named
  assumption?
