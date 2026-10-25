# Summary of round 01 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25. Discussant: astra
(`discussant-astra.md`), after three failed calls. The README order puts astra in
this round, and round 00 had already fallen back to astra. The space first tried
argon to restore the alternation. That call (`prompt-argon.md` in an earlier
version naming in-repo files only) timed out after 38 minutes with an empty answer,
and `discussants.csv` logged it with exit 0. The round fell back to astra, whose
first call stopped on a usage limit (exit 1, 84,142 tokens). By the rule of
`CONTEXT.md` the round then fell back to argon. The second argon call, with the
fixed `discuss.sh` and the present `prompt-argon.md`, timed out after one hour with
an empty answer (exit "empty"). After astra's usage limit reset, the round ran astra
again (`prompt-astra.md`), which answered (exit 0, 130,694 tokens).

## What changed

The round answered the eighteen challenges of round 00, restated thirteen facts with
the hypotheses the discussant asked for, added `fact-balle-reconnn-priced-in-shadow-runs`,
proved `thm-shadow-run-price-finite-views` with `lem-scrambled-seed-urn`, stated
`prop-reconstruction-label-sandwich`, and revised `def-uniform-security-profile`.
The discussant judged the main argument sound against adaptive Train calls, chosen
seeds, seed reuse, Open and calls at other inputs, with correct constants. It found
three blocking defects of statement, none of argument. The urn lemma needs the
response kernels away from new cells at the distinguished input to be identical
under the two compared laws, which the theorem's family satisfies
(`ch-urn-common-nuisance`). Property 1 of the profile identifies the informed optimum
with the total variation of the complete released value for any interface, which is
false for a query channel with a small allowance (`ch-profile-comparator`). Part (f)
of the theorem identifies the label-only optimum with the total variation of the
table laws under both policies, which is false under the top oracle
(`ch-label-policy-optimum`). It also noted that the measurability gap of the lemma is
removable, so the lemma and part (c) become proofs once the hypothesis and the
filtration are stated.

The discussant judges the bottom against top separation under deterministic kernels
to be the substantive contribution candidate, with the passive rate classical
(Daniely, Sabato, Ben-David and Shalev-Shwartz, JMLR 2015, Theorem 5, as it cites)
and the scrambling step a permutation-against-random-function switch with no
hardness assumption.

## Slugs accepted

Verdict ACCEPT in a round with BLOCKING 3, so not yet eligible for status accepted:
`fact-hsu-membership-sample-gap`, `fact-hsu-gap-prices-covariance`,
`fact-yeom-dp-bounds-membership-advantage`, `fact-yeom-generalization-error-gives-advantage`,
`fact-lira-priced-in-training-runs`, `fact-lira-low-fpr-yeom-game`,
`fact-balle-reconstruction-robustness-definition`, `fact-balle-dp-bounds-reconstruction`,
`fact-dinur-nissim-reconstruction-thresholds`, `fact-pac-privacy-mutual-information-bound`,
`fact-pac-privacy-gaussian-release-bound`, `fact-zhao-accuracy-forces-attribute-leakage`,
`fact-balle-reconnn-priced-in-shadow-runs`, `prop-reconstruction-label-sandwich`.

Verdict REVISE: `fact-reconstruction-query-lower-bounds`, `def-uniform-security-profile`,
`lem-scrambled-seed-urn`, `thm-shadow-run-price-finite-views`.

## Challenges open

Blocking, answered in `round-02/builder.md`: `ch-urn-common-nuisance`,
`ch-profile-comparator`, `ch-label-policy-optimum`. Not blocking:
`ch-reconstruction-majority-omission`, `ch-reconnn-seed-interpretation`,
`ch-urn-filtration`, `ch-shadow-small-budgets`, `ch-shadow-policy-quantifiers`,
`ch-sandwich-endpoint-details`, and three domain remarks without names (the positive
noise scale of HSU25 Definition 2.4, the positive slack of DN03 Theorem 5, the
randomized mechanisms of XD23 §4.2).

## For the registers

New search row, run by this session on 2026-10-25 after the search gate found no
row on the question.

| date | slug | question | tool and index | query | scope | hits | kept | coverage | updates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-25 | search-shadow-run-lower-bound | Is a lower bound published on the number of shadow training runs a membership attacker needs to come within a given accuracy of the optimal advantage? | WebSearch (standard), then WebFetch of two hits. Record HE-ML:lab/theory/spaces/statistical-limits/round-01/summary.md | lower bound number of shadow models membership inference sample complexity reference models theorem | Open web, one query, no venue or year filter | 9 | Choi, Tople, Chandrasekaran and Jha, arXiv 2310.08015, Lemma 2 and Corollary 1 (the sample complexity of testing between two known laws, read informally as a count of shadow models, no lower bound on learning the test). Aubinais, Gassiat and Piantanida, Fundamental Limits of Membership Inference Attacks on Machine Learning Models (bounds on attack accuracy in the training-set size, no count of shadow models) | Partial, one query, two papers opened | none |

New facts, beyond those listed in `round-00/summary.md`.

- `fact-balle-reconnn-priced-in-shadow-runs`. BCH22 §IV-B, §VI-B, Fig. 5 and
  Table III, as stated in `round-01/builder.md`. Empirical, read full, accepted by the
  round-01 discussant. Its wording "needs the initialization" is a statement about
  this attack on these experiments and not a statistical impossibility
  (`ch-reconnn-seed-interpretation`).

Corrections to existing entries, beyond those of round 00.

- `fact-reconstruction-query-lower-bounds`. ML24 Appendix B.5 also holds an
  unnumbered result on a majority adversary, for privacy parameter at least $0.042$
  (pages 26 and 27, per the discussant, not read by the builder). It is target
  independent and does not repair the uniform rate claimed by Theorem 10.
- `fact-pac-privacy-gaussian-release-bound`. XD23 §4.2 and Corollary 2 treat
  randomized mechanisms. The fact is the deterministic specialization.

New problems.

- `prob-shadow-model-lower-bound`, status partial. `thm-shadow-run-price-finite-views`
  (f), if accepted, settles it when the query set has as many points as the query
  budget, with order $C^{q_E}/a^2$ Train calls necessary and sufficient under the
  bottom oracle. The factor $\ln|U|$ for larger query sets stays open.
- `prob-train-access-collapses-sample-price`, proposed in round 00, unchanged.

For the integrator, outside the registers. Argon timed out twice on this round, at
38 minutes and at one hour, on a builder file of about 54k characters. The space
will give argon a short builder in round 02. The shared note
`2026-10-25-statistical-limits-argon-failure.md` has the log.
