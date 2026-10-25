# Space: computational limits

Owner: session space-computational (local_5201ce4d), started 2026-10-25 by the integrator.
One session at a time.

Discussants: astra in `round-00`, then alternating argon and astra.

## Question

What does an adversary that must compute efficiently, or must itself learn, a
learner trained by gradient methods or a statistical-query or low-degree
algorithm, achieve against a learning procedure? Which known learning problems
does an attack task reduce to or from, with or without the learning oracle, and
where does the computational price depart from the statistical one? Halil's
reconstruction example in `CONTEXT.md` is the model case: the reconstructor is
itself a learner from intermediate vectors to raw data, and a reduction between
its learning problem and the trainer's would give a lower bound priced by the
performance of the attacked model.

## Scope

In scope: statistical-query and low-degree lower bounds and their reach to
gradient methods, learning exponents (information, generative, leap) and the
sharp sample thresholds they set, inversion of networks, the seed as a resource
and split learning, restricted-class attackers and usable information, fine-
grained and memory-bounded cryptography, and the question of when some aspect of
a trained model is, or yields, a pseudorandom generator or a one-way function
(as narcissus resiliency is equivalent to one-wayness, Cohen et al.). Placing a
cryptographic primitive into a procedure is out of scope by Halil's rule.

Out of scope: unbounded adversaries (space `statistical-limits`) and measurement
(space `oracle-and-measurement`). A result that needs one of them names the
other space's slug and leaves the work there.

## Where to start

- `sink/formalizing/STATE.md`, decisions 2 and 3, and the central problem.
- `sink/formalizing/facts.md`, sections: Statistical-computational gaps and
  low-degree models, Learning exponents, Inverting networks and the reach of
  statistical queries, The seed as a resource and split learning, Restricted-
  class attackers and usable information, Fine-grained and memory-bounded
  cryptography, Backdoors and undetectability.
- `sink/formalizing/problems.md`: `prob-reduce-security-to-known-learning-problems`
  (central), `prob-split-learning-seed-separation`, `prob-split-transcript-leaks-seed`,
  `prob-statistical-queries-for-regression`, `prob-attacker-lower-bound-from-hard-learning`,
  `prob-same-units-matched-budget-separation`, `prob-separation-against-jagielski-sq-bound`,
  `prob-op1-robust-comp-stat-gap`, `prob-sq-reduction-per-round-observation`,
  `prob-comp-mem-reduces-to-hclwe`, `prob-filter-compute-ratio-fine-grained`.
- `FS:.tools/proof.tex` in `~/Documents/RESEARCH/FORMAL_SECURITY`, an unverified
  bound against black-box attackers of SQ-implementable learners. Read it before
  any new proof of that kind, and judge it.
- The library, `lib/literature/notes/<venue>/<Key>.md` and the PDFs beside them.
  Read the paper itself for any statement the round relies on.

## Round log

The space session appends one line per round: the folder, the date, the
discussant, the verdict counts and the BLOCKING count.

- `round-00`, 2026-10-25, astra (gpt-6-astra): ACCEPT 6, REVISE 12, REJECT 0. BLOCKING 12.
- `round-01`, 2026-10-25, astra (gpt-6-astra) as fallback after three failed argon calls: ACCEPT 13, REVISE 6, REJECT 1. BLOCKING 10.
- `round-02`, 2026-10-25, argon (gemini-4-argon-medium): ACCEPT 7, REVISE 0, REJECT 0. BLOCKING 0. The space stops here.
