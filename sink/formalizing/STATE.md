# State of the line on formalizing AI security

updated: 2026-10-25
by: HE-ML integrator session of 2026-10-25, after merging the first theory rounds

## The question

Measure an adversary against a learning procedure by computational and learning
resources, and reduce its security problems to known learning problems, with or
without the learning oracle. A cheap cryptographic plug-in does not count. A
finding that some aspect of a model reduces to or yields a pseudorandom generator
would count. The framework must be realizable, or approximately realizable, by
experiments (Halil, 2026-10-25). Central problem:
`prob-reduce-security-to-known-learning-problems`.

## What stands

- The theory now lives in `HE-ML:lab/theory/` (context, rounds, booklet source),
  and Halil reads it in `HE-ML:lib/theory/booklet.pdf`. Its first rounds, three
  spaces of three rounds each, ended with BLOCKING 0 on 2026-10-25. Their objects
  are in `results.md` under Oracle and measurement (in the Learning oracle
  section), Computational limits and Statistical limits.
- Headline results, all proven in round files, accepted by discussants, re-derived
  by the integrator, unchecked by Halil: `thm-blind-split-seed-separation`,
  `thm-exact-twin-price`, `thm-shadow-run-price-finite-views`,
  `thm-coupling-free-soundness`, `thm-reconstruction-from-conditional-mean`.
- `thm-sq-hardness-black-box-attacks`, the FORMAL_SECURITY proof note, is refuted
  by counterexample (alias `thm-fs-sq-black-box-reduction`).
- Registers: 288 facts, 226 results, 99 problems, 72 searches. Library: 590 papers.

## Decisions waiting for Halil

1. The two oracle definitions. Proposal: one oracle with a named and a drawn
   seed-access mode (`def-seed-access-modes`). FORMAL_SECURITY's oracles are
   drawn-mode callers (`prop-drawn-mode-is-fs-oracle`), and drawn coins lose no
   soundness for bottom-oracle targets (`thm-coupling-free-soundness`).
2. First target. Proposal: the split-learning seed separation in the form of
   `thm-blind-split-seed-separation`, with `conj-seed-price-is-ngca-price` as its
   general statement.
3. Attacker class for lower bounds. Proposal: two games, never mixed. Population
   SQ attackers of frozen clients for unconditional bounds, polynomial-time
   attackers with the record-level view for bounds conditional on lattice hardness.
4. Whether a separation whose hard instance is a record law (pancakes) meets the
   rule that a cryptographic plug-in does not count.

## Priority problems

1. `prob-reduce-security-to-known-learning-problems` (central, open, two
   reductions now exist).
2. `prob-split-learning-seed-separation` (supporting, partial), with
   `prob-blind-inversion-relu-clients` and `prob-coarse-reconstruction-lattice-hardness`.
3. `prob-train-access-collapses-sample-price` (supporting, open).
4. `prob-same-units-matched-budget-separation` (supporting, open).

## Searched already, do not repeat

The scan of 2026-10-25 (eight rows), the six rows of the theory spaces, the
zero-citer sweep of 2026-08-20, the July 2026 novelty checks, the HE-ML venue
sweep of 2026-10-16. Grep `searches.md`.

## Known defects, not yet fixed

- The sweep report's deviating-share headline, frame 9 of the 16 October deck.
- The seven minor audit findings of the learning-oracle final document.
- `CONTEXT.md` says 13 papers dropped after reading, the records show 14.
- The adversary interface report claims a collapse holds exactly when a
  sufficient statistic exists, which is false.
- FORMAL_SECURITY: `index.md` and `overview.md` stale since April, 167 wiki
  edits of 2026-09-03 unlogged, `LEARNING_aioracles.md` and `scratchpad.md`
  missing, a disputed attribution of the polynomial-link rate.
- Papers to place, named by the spaces: Steinke, Nasr and Jagielski (NeurIPS
  2023), Jagielski, Ullman and Oprea (NeurIPS 2020), Gilbert and McMillan (2018),
  Sablayrolles et al. (ICML 2019), Guo et al. (ICML 2022), Daniely et al. (JMLR
  2015), van Rooyen and Williamson (arXiv 1402.4884), PDFs of DKRS23, LKR06, LZA21.
- `dauntless.pdf` (Xiao and Devadas, IACR ePrint 2021/1074) needs a manual download.

## Next actions

1. Halil reads the booklet and settles decisions 1 to 4.
2. The next milestone of `lab/theory/` opens on the chosen target.
