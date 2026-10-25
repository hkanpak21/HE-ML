# Round 01, oracle and measurement, summary

Date 2026-10-25. Discussant astra (`discussant-astra.md`). Verdicts: ACCEPT 4, REVISE 7, REJECT 0.
BLOCKING 7. The discussant follows the README's alternation, argon in round 00 and astra here.

Round 01 answered argon's twenty-one challenges of round 00, revised five facts, read SAB24 and added
a fact on controlled GPU nondeterminism, and stated five objects. Astra judged ten of argon's twelve
blocking challenges closed or closed in substance. It accepted thm-coupling-free-soundness after checking
step 4 of its composition proof line by line. It accepted the limit and Jensen steps of
thm-exact-twin-price and the release-leakage extension for total variation, and refuted the lower bound on
calls at the base input for the one-sided target $\mathrm H_{e^\varepsilon}(P_1\|P_0)$. Its counterexample
certifier uses four base calls where the stated bound asks for 298. It accepted the simulation argument of
prop-profile-run-coordinate (a), and found that part (b) charges one shadow bank for adversaries whose shadow
inputs may depend on the challenge. Its other blocking points are wording or hypotheses. They concern exact
against approximate seed recovery, the noise range of HSU25 Theorem 4.1, the parameter range in which
ZCSL24's Algorithm 2 saves time, the meter's zero infimum and its missing corpus-size coordinate, and the
claim that paired trials always reduce variance. Every challenge is answered by name in `round-02/builder.md`.

Slugs with verdict ACCEPT: fact-gdp-audit-observation-count, fact-rerun-reproduction-error,
fact-controlled-nondeterminism-exact-replication, thm-coupling-free-soundness. None is eligible for status
accepted, since the round ends with blocking challenges. thm-coupling-free-soundness is re-presented in
round 02 with astra's clarifications.

Challenges open after this round, all answered in round 02. Blocking: ch-seed-enumeration-conditions,
ch-known-covariance-noise-range, ch-forging-strict-cost, ch-meter-domain-and-equivalence,
ch-profile-adaptive-shadow-cost, ch-paired-discordance-baseline, ch-one-sided-twin-asymmetry. Astra's
non-blocking points, answered there too: the F9 null set in thm-exact-twin-price, the utility class of the
generic training oracle, the exchanged coordinates for the reverse bound of thm-coupling-free-soundness and
the implementability of a twin rule, the virtual name table of the simulation in prop-profile-run-coordinate,
and the controlled pipeline as the deployed one.

Addendum, 2026-10-25, 19:40. Round 02 was written (`round-02-pending/builder.md`) and answers all seven blocking
challenges above. Its discussant turn did not happen. Astra was out of quota until 21:27, so argon took the turn as a
fallback, and both argon calls timed out with no output, at 38 and at 60 minutes. On the integrator's instruction the
space stops at this round, the last complete one, with BLOCKING 7. The pending builder states the fixes. Exact against
approximate seed recovery, with a proven error term of $2e$. The full dimension condition of HSU25 Theorem 4.1, with the
attack attributed to Dwork, Smith, Steinke, Ullman and Vadhan. The parameter range in which ZCSL24's Algorithm 2 saves
time. A two-coordinate meter, work and examples, with the needle bound in multiplicative form. Two-phase and general
families in prop-profile-run-coordinate (b), and the covariance condition for paired trials. thm-exact-twin-price with
base-input bounds for the coupled tail and total variation only, and astra's counterexample for the one-sided target as
its part (c). Nothing in it is accepted until a discussant judges it.

Second addendum, 2026-10-25, 20:55. After the integrator's fix to `discuss.sh`, the folder was renamed back to
`round-02` and a third argon call, with gemini-4-argon-medium, judged it: ACCEPT 8, BLOCKING 0. The space stops after
round 02, and `round-02/summary.md` supersedes the stop recorded in the first addendum.

## For the registers

New fact, read in the library PDF on 2026-10-25 by this space, note filled.

- fact-controlled-nondeterminism-exact-replication. SAB24 (Srivastava, Arora and Boneh, NeurIPS 2024), §6 with
  Fig. 2 and Fig. 4, Table 5. Runs on one GPU type repeat identically with deterministic settings. Runs on A40,
  Titan XP and RTX 2080 Ti differ. Logged rounding with FP64 training makes ResNet-50 training and GPT-2
  fine-tuning replicate exactly across the three types at 1.2 to 1.4 times the trainer's time and 1.3 to 1.7
  times the auditor's. Astra's scope note: the replicated pipeline is the modified one (precision, rounding,
  own dropout), and the logs are per execution.

Corrections from round 01 and from the pending round 02, each checked against the paper or the note.

- fact-hsu-membership-sample-gap. Theorem 4.1 proves impossibility with known covariance only for
  $d<c(n+n^2\rho^2+n^2/m)$. The matching attack for $d\gtrsim n+n^2\rho^2+n^2/m$ is attributed by HSU25 to Dwork, Smith,
  Steinke, Ullman and Vadhan (FOCS 2015) and not proven there, so with $m=2$ the dimension needed is of order
  $n+n^2\rho^2+n^2/2$.
- fact-unlearning-verification-fragile. Proposition 4.5 of ZCSL24 gives Algorithm 2 the time factor
  $p_u/P+(1-p_u)/(mP)$ on $P$ processes, equal to one at $P=m=1$ and below one when $P\ge2$, or when $m\ge2$ and $p_u<1$.
  Its work factor is the value at $P=1$. Proposition 4.4 holds under the assumptions of Proposition 4.3, vanilla SGD for
  the replay update and its step-size bounds.
- fact-small-seed-space-breaks-dp. Enumerating a finite seed space gives the exact view laws only when all other
  randomness is integrated exactly, and the top oracle only when one decoder recovers the seed under both hypotheses.
  A decoder with error $e$ under each hypothesis gives advantage at least $\mathrm D^\top_1-2e$.

Corrections to round 00's register items.

- fact-audit-independent-batches. Its last paragraph should read as in the response to
  ch-shared-batch-marginal-vs-paired of `round-01/builder.md`.
- fact-one-shot-estimate-consistency. "Clopper and Pearson style" should read "Jeffreys interval for the
  false-negative rate and the exact null for the false-positive rate", and Theorem 3.3 holds at fixed $\sigma>0$
  and $\delta\in(0,1)$.

Prior-work pointers from astra's review, not read by this space and so recorded, not verified. Dong, Roth and Su,
Gaussian differential privacy, JRSS B 2022, arXiv 1905.02383, Theorem 2.10, Theorem 3.2 and Corollary 3.3, as the
composition ingredients of thm-dataflow-composition. Kaufmann, Cappé and Garivier, JMLR 2016, Lemma 1, the change of
measure for expected sample counts, whose mutual absolute continuity does not cover the singular construction of
thm-exact-twin-price. Gilbert and McMillan, Allerton 2018, Theorems 10 and 12, sample-access impossibility, not the
named-seed bound.

Search rows. None new in this round. The reading of SAB24 extends search-oracle-measurement-library-auditing of
round 00.

Problems.

- New, for `problems.md`: prob-revealed-seed-rerun-price. Under hardware randomness, how many reruns at a revealed
  seed does an adversary fixed before the learning function need to approach the top optimum
  $\mathrm D^\top_1(K)$? Posed by argon in round 00 (ch-seed-attack-already-known). Weight side. Literature unchecked.
- prob-coupled-reruns-rarely-differ. Add SAB24 §6 to its literature: the hardware part is settled for the tested
  models and GPU types by deterministic settings or logged rounding. The data part, the distance of a leave-one-out
  twin from the base run, stays open and is the quantity the measurement designs of this space ask for.
