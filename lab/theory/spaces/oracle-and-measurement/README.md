# Space: oracle and measurement

Owner: session space-oracle (local_b77570c4), started 2026-10-25 by the integrator.
One session at a time.

Discussants: argon in `round-00`, then alternating astra and argon.

## Question

How do the learning oracle and experiments realize, or approximate, the prices
that the spaces `statistical-limits` and `computational-limits` define? What does
a measured security profile, the curve from an adversary's budget to its success,
certify and at what cost in real training? How does knowledge of the training
seed change the learning problem an adversary faces? Halil's point on practical
efficiency in `CONTEXT.md` is the model case: the oracle hands over every
leave-one-out twin, real training does not, and a result that uses the oracle
should say what approximating it by real training costs.

## Scope

In scope: the two oracle definitions that disagree (`def-learning-oracle` of
HE-ML lets callers name seeds, `def-passive-learning-oracle` and
`def-generic-training-oracle` of FORMAL_SECURITY forbid it), with a proposal for
Halil and no decision taken here; the cost of `Train` and `Eval` calls in real
compute and lower bounds on their number; the security profile as a measurable
object; certificates and their sample cost; the seed as a resource; and the
experiments that would realize a price of the other two spaces.

Out of scope: proving statistical or computational lower bounds themselves
(the other two spaces). A result that needs one names the other space's slug.

## Where to start

- `sink/formalizing/STATE.md`, decision 1.
- `sink/formalizing/results.md`, sections Learning oracle (HE-ML) and Adversary
  interface (HE-ML), and the FORMAL_SECURITY programme section.
- `sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md`, the accepted
  oracle theory, and its seven unapplied audit findings.
- `sink/formalizing/facts.md`, sections: Learned or idealized oracles, The seed as
  a resource and split learning, Extraction, proof of learning and unlearning,
  Membership inference and sample complexity (the entries priced in training
  runs).
- `sink/formalizing/problems.md`: `prob-security-profile-curve`,
  `prob-comp-stat-envelope-measurement`, `prob-eval-and-train-call-lower-bounds`,
  `prob-compute-pricing-lower-bound`, `prob-acceptable-ai-oracle`,
  `prob-parked-oracle-uninstantiability`, `prob-training-as-oracle-prior-art`,
  `prob-drawn-seed-price-above-d`, `prob-multi-round-drawn-seeds`,
  `prob-coupled-reruns-rarely-differ`, `prob-seed-maps-exact-coupling`.

## Round log

The space session appends one line per round: the folder, the date, the
discussant, the verdict counts and the BLOCKING count.

- `round-00`, 2026-10-25, argon, ACCEPT 7, REVISE 7, REJECT 1, BLOCKING 12.
- `round-01`, 2026-10-25, astra, ACCEPT 4, REVISE 7, REJECT 0, BLOCKING 7.
- `round-02`, 2026-10-25, argon, ACCEPT 8, REVISE 0, REJECT 0, BLOCKING 0. Two earlier argon calls on this round timed out with no output. The third, with gemini-4-argon-medium, gave the verdict. The space stops here.
