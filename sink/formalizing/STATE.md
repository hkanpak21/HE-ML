# State of the line on formalizing AI security

updated: 2026-10-25
by: HE-ML session of 2026-10-25, after building this folder

## The question

Measure an adversary against a learning procedure by computational and learning
resources, and reduce its security problems to known learning problems, with or
without the learning oracle. A cheap cryptographic plug-in does not count. A
finding that some aspect of a model reduces to or yields a pseudorandom generator
would count. The framework must be realizable, or approximately realizable, by
experiments (Halil, 2026-10-25). Central problem:
`prob-reduce-security-to-known-learning-problems`.

## What stands

- HE-ML learning-oracle theory: 15 accepted items, 8 non-trivial, audit FINAL
  ACCEPT on 2026-10-17 with seven minor fixes unapplied. Entry `def-learning-oracle`.
  Its upper bounds hold without the oracle given seed control. Its lower bounds
  and the named-seed separation need it.
- HE-ML adversary interface and the coded sweep of 350 papers, `results.md`
  section Adversary interface.
- FORMAL_SECURITY programme on the computational security of learning: the
  quantizer `R`, the security profile, the three attack-surface axes, oracle
  drafts, an SQ hardness proof. `results.md` section FORMAL_SECURITY programme,
  digest `sources/2026-10-25-formal-security-programme.md`.
- Library: 590 papers in `lib/literature/pdfs/<venue>/`, 268 facts, 66 searches.

## Decisions waiting for Halil

1. Two oracle definitions disagree. `def-learning-oracle` lets callers name
   seeds, which is the source of its separation results. `def-passive-learning-oracle`
   and `def-generic-training-oracle` in FORMAL_SECURITY draw fresh coins and
   forbid naming seeds. Pick one, or keep both as two access modes.
2. First target. `prob-split-learning-seed-separation` is the candidate.
   `FS:.tools/proof.tex` already bounds black-box attackers of SQ-implementable
   learners (unverified, `prob-attacker-lower-bound-from-hard-learning` is
   partial). Read it before any new proof.
3. Attacker class for lower bounds: statistical-query learners, with the
   regime limit of Abbe et al. Theorem 1c, see `fact-` entries under the
   statistical-query heading.

## Priority problems

1. `prob-reduce-security-to-known-learning-problems` (central, open).
2. `prob-split-learning-seed-separation` (supporting, open), with
   `prob-split-transcript-leaks-seed` and `prob-statistical-queries-for-regression`.
3. `prob-attacker-lower-bound-from-hard-learning` (supporting, partial).
4. `prob-same-units-matched-budget-separation` (supporting, open).

## Searched already, do not repeat

The learning-bounded privacy scan of 2026-10-25 (eight rows), the zero-citer
sweep of 2026-08-20, the compute-amount sweep and the four refuted novelty
checks of July 2026, the HE-ML venue sweep of 2026-10-16. Grep `searches.md`.

## Known defects, not yet fixed

- The sweep report's deviating-share headline, frame 9 of the 16 October deck.
- The seven minor audit findings of the learning-oracle final document.
- `CONTEXT.md` says 13 papers dropped after reading, the records show 14.
- The working copy of `lib/literature/ledger.csv`, rewritten 2026-10-19 by an
  unknown session, drops the two Salem et al. rows that the last commit has.
- The adversary interface report claims a collapse holds exactly when a
  sufficient statistic exists, which is false.
- FORMAL_SECURITY: `index.md` and `overview.md` stale since April, 167 wiki
  edits of 2026-09-03 unlogged, `LEARNING_aioracles.md` and `scratchpad.md`
  missing, a disputed attribution of the polynomial-link rate.
- `dauntless.pdf` (Xiao and Devadas, IACR ePrint 2021/1074) needs a manual download.

## Next actions

1. Halil settles decisions 1 to 3.
2. A session reads `FS:.tools/proof.tex` against
   `prob-attacker-lower-bound-from-hard-learning` and records the verdict.
3. Then builder and challenger rounds on the chosen target, with this folder's
   search gate in every brief.
