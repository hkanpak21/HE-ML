# Round 03 of learning-attacker-prices, summary

Written by the builder after the challenger's round-03 turn and saved verbatim by the integrator
from the builder's reply.

Round 03 conceded ch-chosen-query-scaling, the blocking challenge, and ch-third-reading. It replaced prop-trainer-accuracy-caps-release-attacker with thm-release-relearning-price-bracket, which prices an attacker re-learning from a trained release in the Gaussian linear model. Every attacker's accuracy is capped by the trainer's Bayes risk, and an exact release lets $d$ queries attain that risk. Under an average power constraint on the queries at the scale of the input law, with answer noise of nature's variance, every attacker needs at least about $(n-d-1)/\kappa$ answers to come within a factor $1+\kappa$ of the trainer's risk. Least squares on random queries, a learner of the trainer's own class, meets that bound within $1+O(d/n)$ for $\kappa=O(1)$. Without the noise or without the power bound, $d$ queries suffice.

The round restated the answer to Halil through three readings of his sentence. The trainer's performance is a ceiling on the attacker's accuracy, a floor on its success (for his reconstruction example this is the registered thm-reconstruction-from-conditional-mean), and a floor on its cost only when the answers carry nature's noise at nature's power. It took the challenger's two proven additions into conj-linear-class-reads-cauchy-transform: at most one outlier on each side of the bulk, with a closed test at the edges, and the reduction of part (b) to the best eigenvector in mean-square overlap. From that reduction it added a measurable bound on the whole linear class's success at a given budget. It recomputed $\kappa_{\mathrm{KL}}$ on $Q_0$ with closed-form integrands as 0.160111, above both earlier grid values, and stated the order in which the certified estimator was declared. It added the closure of def-statistic-learner-class under subsampling.

The challenger tested part (c) of the new theorem hardest and could not break it. Its simulation puts the bound about 6 percent below the Bayes attacker that is given the trainer's design (at $d=10$, $n=60$, $N=200$). It also proved the inverse-Wishart moment $\iota_m=d/(m-d-1)$ by a Schur-complement argument, which removes the theorem's one recall from memory, and it conceded that its own round-02 value of $\kappa_{\mathrm{KL}}$ was low. It accepted all four objects with BLOCKING 0 and SATISFIED yes. By Halil's rule the space stops here, and there is no round 04.

Accepted: thm-release-relearning-price-bracket, conj-linear-class-reads-cauchy-transform, prop-measured-meets-proven-full-observer, def-statistic-learner-class.

Resolved in the round: ch-chosen-query-scaling, ch-third-reading, ch-b-in-order-versus-exact, ch-quadrature-is-not-a-proof, ch-declaration-order, and ch-no-trainer-price for the Gaussian linear model.

Challenges open at the close, none blocking:
- ch-kappa-in-error-term. The bracket of part (e) has ratio $1+O((1+\kappa)(d+s^2/\tau^2)/n)$, so the stated factor holds for $\kappa=O(1)$ only.
- ch-price-is-power. The theorem prices total query power in record equivalents, and the count of answers equals that price only at nature's norm.
- ch-release-noise-reading. The theorem prices a given release. Recommending $s_r=s$ as a defence would use the broad reading of ruling 2.
- ch-failure-threshold. The measurable bound certifies failure of the linear class when its upper band lies below $\frac23\epsilon^2$, which is $\frac16$ at $\epsilon=\frac12$.
- ch-vacuous-at-measured-dimension. Open for the linear class only, with the measurable bound of (b1) as its path.

The challenger also notes, without naming a challenge, that the theorem assumes fresh noise per answer. A randomized model sampled once, with noise fixed per input, is not covered.

These five notes are one-line edits of scope and wording. No round applied them, so the integrator should carry them into the booklet text.

## For the registers

none

No paper was opened and no search was run in round 03. Two notes for the integrator:
- The inverse-Wishart moment $\mathbb E\,\mathrm{tr}((G^\top G)^{-1})=d/(m-d-1)$ for $m\ge d+2$ is now proven in the space, in section 3.2 of `round-03/challenger.md`. The label "from memory, unverified" in thm-release-relearning-price-bracket can be replaced by that proof.
- Cited from memory in round 03, and a candidate for a search row: the classical A-optimal design lower bound for Gaussian linear models, which the challenger names as the source of part (c)'s argument.

## The space at its close

Objects that stand. Under `CONTEXT.md` each is accepted, since its latest verdict is ACCEPT and the space's last round ends with BLOCKING 0. The conjecture is accepted as well posed, and its content is open.

| Slug | Latest version | Last verdict |
| --- | --- | --- |
| thm-update-direction-chi-square-bound | round 00 (uses line amended in round 01, statement unchanged) | ACCEPT, round 00 |
| def-optimum-update-stream | round 01 | ACCEPT, round 01 |
| thm-norm-weighted-update-pca | round 01 | ACCEPT, round 01 |
| prop-update-direction-fano-recovery | round 01 | ACCEPT, round 01 |
| prop-full-clipping-optimum-filter | round 02 | ACCEPT, round 02 |
| prop-signed-weight-update-pca | round 02 | ACCEPT, round 02 |
| def-statistic-learner-class | round 03 | ACCEPT, round 03 |
| conj-linear-class-reads-cauchy-transform | round 03 | ACCEPT, round 03 |
| prop-measured-meets-proven-full-observer | round 03 | ACCEPT, round 03 |
| thm-release-relearning-price-bracket | round 03 | ACCEPT, round 03 |

Objects withdrawn or superseded:

| Slug | Last verdict | Withdrawn in | Fate |
| --- | --- | --- | --- |
| def-learning-attacker-known-price | REVISE, round 00 | round 01 | superseded by def-statistic-learner-class |
| conj-optimum-update-variance-price | REVISE, round 00 | round 01 | withdrawn. Its exact part moved to def-optimum-update-stream, and its part (b) became the constant-weight case of thm-norm-weighted-update-pca |
| conj-update-moment-degree-gap | REJECT, round 00 | round 01 | withdrawn. The knife-edge remark survives inside the responses of round 01 |
| conj-update-linear-class-price | REVISE, round 01 | round 02 | superseded by conj-linear-class-reads-cauchy-transform |
| prop-trainer-accuracy-caps-release-attacker | REVISE, round 02 | round 03 | superseded by thm-release-relearning-price-bracket. Its parts (a) and (b) are kept, its remark is withdrawn, and its part (c) is dropped as a description of nature |

The pushback P1 of round 00, that where no statistical-computational gap exists the attacker's class plays no part in the lower bound, was withdrawn in round 01 after the challenger's law $Q_\delta$ refuted it.
