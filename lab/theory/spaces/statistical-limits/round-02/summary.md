# Summary of round 02 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25. Discussant: argon
(`discussant-argon.md`), the model that `discuss.sh` names gemini-4-argon-medium, in one
call. Argon returns to the alternation after round 01 fell back to astra. The builder file
was kept short, about 22k characters, after two argon timeouts on the longer file of
round 01, and the prompt named only in-repository files.

## What changed

The round repaired the three statements blocked in round 01. `lem-scrambled-seed-urn` now
fixes a common learning setting across the two compared label laws (`ch-urn-common-nuisance`),
conditions on the augmented history that holds every seed value (`ch-urn-filtration`), and
proves its total-variation bound by a hybrid argument integrated along the paths of the
scrambled run, with a passage to infinite padded sequences. The builder found and fixed
one error of its own before the call. A supremum over histories at each fixed step index
would have double counted, because the index of the $t$-th new-cell call varies with the
path. `def-uniform-security-profile` splits its singleton property into a general infimum by
internal simulation, the plain-channel case attained at zero budget, and the finite
query-channel case attained by a hard-wired strategy tree (`ch-profile-comparator`). Part (f)
of `thm-shadow-run-price-finite-views` separates the bottom-oracle optimum, the total
variation of the table on a fixed set of $q_E$ points, from the top-oracle optimum, the top
divergence of that channel, and separates the query set from the allowance
(`ch-label-policy-optimum`). Parts (a) and (b) now state the small-budget case and the
quantifiers per policy. The fourteen objects accepted in round 01 were carried with the
domain remarks the round-01 discussant asked for.

The discussant accepted every object and raised no challenge. Its review is a check that
the revisions close the named challenges and that the revised lemma proof holds step by
step. It did not re-derive the unchanged proofs of round 01, which the round-01 discussant
had checked line by line.

## Slugs accepted

With BLOCKING 0, each of these has verdict ACCEPT in this round:

- `thm-shadow-run-price-finite-views`
- `lem-scrambled-seed-urn`
- `prop-reconstruction-label-sandwich`
- `def-uniform-security-profile`
- `fact-hsu-membership-sample-gap`, `fact-hsu-gap-prices-covariance`,
  `fact-yeom-dp-bounds-membership-advantage`, `fact-yeom-generalization-error-gives-advantage`,
  `fact-lira-priced-in-training-runs`, `fact-lira-low-fpr-yeom-game`,
  `fact-balle-reconstruction-robustness-definition`, `fact-balle-dp-bounds-reconstruction`,
  `fact-reconstruction-query-lower-bounds`, `fact-dinur-nissim-reconstruction-thresholds`,
  `fact-pac-privacy-mutual-information-bound`, `fact-pac-privacy-gaussian-release-bound`,
  `fact-zhao-accuracy-forces-attribute-leakage`, `fact-balle-reconnn-priced-in-shadow-runs`

The superseded round-00 aims `conj-shadow-run-price-finite-views` and
`conj-reconstruction-label-sandwich` keep their round-00 verdict REVISE and are not
proposed for the booklet. Their content is in the theorem and the proposition.

## Challenges open

None. The space stops here under the milestone's rule, its first round from 01 on with
BLOCKING 0.

What remains open as mathematics, not as a challenge:

- whether the factor $\ln|U|/(C-1)+1$ between the known bounds of part (f) is needed;
- whether Train access collapses the sample price of HSU25 (`prob-train-access-collapses-sample-price`);
- the novelty of the oracle part of the theorem, checked by one query only.

## For the registers

New results proposed for `sink/formalizing/results.md`, all with `oracle:` as stated.

- `thm-shadow-run-price-finite-views`, theorem, proven, needs-oracle. For one learning node
  seen through a deterministic channel onto $k$ views, coming within $a<1/8$ of the best
  bottom-oracle advantage at every learning function needs at least $3k'/(1024a^2)$ Train
  calls, with $k'=2\lfloor k/2\rfloor$, and $2\lceil4k/a^2\rceil$ drawn-seed calls suffice in
  expectation. Chosen, opened and reused seeds and calls after the challenge do not lower the
  price. Under the top oracle with deterministic kernels one Train call reaches the top
  optimum. Label-only form with $k=C^{q_E}$. Where: `HE-ML:lab/theory/spaces/statistical-limits/round-01/builder.md`
  and `round-02/builder.md`. Checked-by: discussant rounds 01 (astra) and 02 (argon),
  unchecked by a person.
- `lem-scrambled-seed-urn`, lemma, proven, needs-oracle. Where: `round-02/builder.md`.
- `prop-reconstruction-label-sandwich`, proposition, proven, holds-without-oracle. Where:
  `round-01/builder.md` with the changes of `round-02/builder.md`.
- `def-uniform-security-profile`, definition, holds-without-oracle in its statement, with
  properties that use the oracle. Where: `round-01/builder.md` and `round-02/builder.md`.

Facts. The new facts and corrections are listed in `round-00/summary.md` and
`round-01/summary.md`. Every fact slug there received ACCEPT in this round, in the wording
of `round-01/builder.md` with the changes of `round-02/builder.md`.

Problems.

- `prob-shadow-model-lower-bound`, from open to partial. Solved when the query set has
  $q_E$ points, by `thm-shadow-run-price-finite-views` (f). Open for the factor $\ln|U|$.
- `prob-train-access-collapses-sample-price`, new, supporting, literature unchecked, as
  stated in `round-00/summary.md`.
- `prob-security-profile-curve`, related. `def-uniform-security-profile` gives the
  unbounded-adversary form, and the efficient form stays with the space
  `computational-limits`.

New search rows. None in this round. The row `search-shadow-run-lower-bound` is in
`round-01/summary.md`.

For the integrator, outside the registers. The `discussants.csv` rows for this space hold
four failed calls besides the three answered ones: round 00 argon (permission, logged exit
0), round 01 argon (timeout, logged exit 0), round 01 astra (usage limit, exit 1), round 01
argon (timeout, exit "empty"). The round-02 call ran on gemini-4-argon-medium, which the
present `discuss.sh` names.
