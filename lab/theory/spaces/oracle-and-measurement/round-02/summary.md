# Round 02, oracle and measurement, summary

Date 2026-10-25. Discussant argon (`discussant-argon.md`, model gemini-4-argon-medium). Verdicts: ACCEPT 8,
REVISE 0, REJECT 0. BLOCKING 0. The discussant follows the README's alternation, astra in round 01 and argon here.

Round 02 answered astra's seven blocking challenges of round 01 and re-presented eight objects. Argon judged every
challenge closed and re-derived three places line by line. The first is astra's counterexample for the one-sided target
at the base input and the shift construction at the numerator input of thm-exact-twin-price. The second is the two kinds
of trial of prop-profile-run-coordinate (b), with the Hoeffding constant for a range of length two. The third is the
exchanged coordinates of $\mathsf{Ex}^\Theta_1$ in thm-coupling-free-soundness (b). It raised no challenge, and noted two
details of the notes that the facts leave implicit: the Mahalanobis condition of HSU25 Definition 3.2, and the smoothness
constants behind ZCSL24 Proposition 4.3. The round ends with BLOCKING 0, so the space stops here, as its brief directs.

The turn took three calls. The first two, with gemini-4-argon-high at 18:00 and 18:36, timed out with no output at 38 and
60 minutes. The integrator traced both failures to the backend's stream idle timeout under concurrent calls, and moved
`discuss.sh` to gemini-4-argon-medium with one argon call at a time. The third call answered within two minutes. The
review is short, about 1,000 words, and lighter than astra's turn of round 01, which checked the same composition proof in
detail. A reader should weigh the acceptance of thm-coupling-free-soundness on both turns, and the other objects on this
one alone.

Slugs accepted in this round, ACCEPT with BLOCKING 0: fact-small-seed-space-breaks-dp, fact-hsu-membership-sample-gap,
fact-unlearning-verification-fragile, def-seed-access-modes, prop-drawn-mode-is-fs-oracle, thm-coupling-free-soundness,
prop-profile-run-coordinate, thm-exact-twin-price. Superseded by them: conj-exact-twin-price by thm-exact-twin-price, and
conj-paired-advantage-price, withdrawn in round 01, whose surviving content is prop-profile-run-coordinate.

Challenges still open: none.

## For the registers

New results for `results.md`, section Learning oracle (HE-ML), each with `where:` this space's `round-02/builder.md`.

- def-seed-access-modes, definition. One learning oracle serves each caller in a named or a drawn seed-access mode, with
  a return label, allowed learner names and starting models, a budget per operation, and a meter of work and examples.
  Overlaps def-passive-learning-oracle, def-generic-training-oracle and def-oracle-access-class, which it contains as
  drawn-mode callers. Status for the registers: proven (a definition). oracle: n/a.
- prop-drawn-mode-is-fs-oracle, proposition. The passive learning oracle (trace space, named recipes, declared
  initializations) and the generic training oracle (return label eval, budgets per operation, its utility condition) are
  drawn-mode callers, with the metered cost as the two-coordinate meter. Status proven. oracle: n/a.
- thm-coupling-free-soundness, theorem. For bottom-oracle targets, every certificate of the oracle theory stays sound
  under any twin rule with the right marginals drawn independently of the release noise, independent drawn runs
  included, and top-oracle targets need a shared seed. Status proven. oracle: needs-oracle for the identity coupling,
  holds in the drawn mode for soundness.
- prop-profile-run-coordinate, proposition. At a fixed learning function the profile of an unrestricted class is flat in
  training runs. A declared family has a certified lower band from fresh shadow runs per trial, and only coupled runs give
  an upper band through deterministic channels with atomless laws. Status proven. Relates to def-security-profile-curve
  and prob-security-profile-curve, and says the curve is well defined as a measured object only with its family named.
- thm-exact-twin-price, theorem. A certifier sound over every learning function and accurate at a zero-leakage function
  makes at least $(1-\alpha')\ln((1-\alpha')/\alpha)/(-\ln(1-\epsilon_{\mathrm{acc}}))$ expected calls at the twin input,
  for the coupled tail, the total variation and the one-sided hockey-stick divergence of a Gaussian release, and at the
  base input for the first two only. Calls at other inputs count for nothing. Matched up to a ceiling, and for every record
  of a dataset multiplied by its size with no union bound. Status proven. oracle: needs-oracle for the upper bound, both
  modes for the lower bound. Lower-bound construction and the every-record certificate due to argon's review of round 00,
  the one-sided counterexample to astra's review of round 01.

Facts. The three revised facts of this round replace their round-01 wording, as listed in the round-01 summary.

Problems.

- prob-security-profile-curve. Add to `tried:` or `history:` that prop-profile-run-coordinate (a) shows the run axis flat
  for unrestricted classes at a fixed learning function, so the curve needs a named family, a uniform statement over
  learning functions, or a computational bound.
- prob-coupled-reruns-rarely-differ. Its data part, the exceedance of a leave-one-out twin under deterministic kernels, is
  the quantity thm-exact-twin-price and thm-coupling-free-soundness make the price of a certificate depend on.
- prob-eval-and-train-call-lower-bounds. thm-exact-twin-price is a lower bound on Train calls for certifiers, not for
  attackers. Record it as related, not as a solution.

Search rows. None new in this round.
