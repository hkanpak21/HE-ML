# Session log

Append only. One entry per session, newest last. Entries before 2026-10-25 are
reconstructed from the records named in them. FORMAL_SECURITY keeps its own
history in `FS:wiki/log.md` and `FS:exp/docs/OLD_SESSIONS.md`, digested in
`sources/`.

## [2026-10-16] HE-ML | research | literature sweep and adversary interface (reconstructed)

Read: eleven top venues for 2023 to 2026, 574 screening decisions, 350 papers
coded into `lib/literature/ledger.csv`. Wrote the adversary interface report and
the sweep report, and the group-meeting deck. Loose ends: the sweep report's
deviating-share headline is wrong (70 rows coded "none" counted as deviating),
and frame 9 of the deck tests the HE trend on rows that are not independent.
Source: `sources/2026-10-25-he-ml-digest.md` sections 2 and 6.

## [2026-10-17] HE-ML | proof | learning-oracle theory, ten builder and challenger rounds (reconstructed)

Read: the learning-oracle definition report. Results: 15 accepted items, 8 of
them non-trivial, in `HE-ML:sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md`,
audit FINAL ACCEPT with seven minor findings not yet applied. Loose ends: the
nine open problems of the final document.

## [2026-10-25] HE-ML | ingest | shared context for formalizing AI security

Read: both repositories through four digest subagents, a scan of learning-bounded
privacy literature, and a survey of how mathematicians keep context. Created this
folder: README with routine and formats, lint, `results.md` (206 entries),
`facts.md` (268), `problems.md` (94), `searches.md` (66 rows), seven dated
sources. Copied 225 papers into `lib/literature/pdfs/<venue>/` with notes, 590 in
the library now, manifest in `sources/2026-10-25-pdf-import.csv`. Decisions by
Halil: measure adversaries by computational and learning resources and reduce
security problems to known learning problems, with or without the oracle. A
cheap cryptographic plug-in does not count. The framework must be realizable by
experiments. Status changes: none, every entry is new. Search rows added: the
scan's eight rows. Loose ends: the two oracle definitions conflict on seed
naming. `FS:.tools/proof.tex` already bounds black-box attackers of
SQ-implementable learners, unverified. `dauntless.pdf` from the scan was a
Cloudflare page, the paper (IACR ePrint 2021/1074) needs a manual download. The
FORMAL_SECURITY files `LEARNING_aioracles.md` and `scratchpad.md`, which its
CLAUDE.md calls the highest-signal files, do not exist.

## [2026-10-25] HE-ML | proof | first theory rounds merged from lab/theory

Read: the round files of the three thinking spaces of `HE-ML:lab/theory/spaces/`
(statistical-limits, computational-limits, oracle-and-measurement), rounds 00 to
02 each, all ending with BLOCKING 0. The spaces read about thirty library papers
and filled their notes. Discussants: astra (gpt-6-astra) and argon
(gemini-4-argon-high, then gemini-4-argon-medium), logged in
`HE-ML:lab/theory/discussants.csv`. The integrator re-derived every merged proof
and took the cited lattice and SQ theorems as the spaces read them.

Status changes: `thm-sq-hardness-black-box-attacks` proven to refuted (alias
`thm-fs-sq-black-box-reduction`). `prob-split-learning-seed-separation`,
`prob-split-transcript-leaks-seed`, `prob-statistical-queries-for-regression` and
`prob-shadow-model-lower-bound` open to partial. Facts recorded or disputed to
verified: `fact-lira-priced-in-training-runs`, `fact-pol-bare-cost-inequalities`,
`fact-unlearning-verification-fragile`, `fact-unlearning-algorithm-level`,
`fact-lira-low-fpr-yeom-game`, `fact-balle-reconstruction-robustness-definition`,
`fact-reconstruction-query-lower-bounds`. New: 20 facts, 20 results, 5 problems.
Search rows added: `search-oracle-measurement-library-auditing`,
`search-rotation-perturbation-ica-attack`, `search-ngca-privacy-reconstruction-bound`,
`search-split-learning-rotation-reconstruction`, `search-orthogonal-equivariance-training`,
`search-shadow-run-lower-bound`.

Dead ends: the round-00 Assouad family for the shadow-run price (one chosen-seed
call breaks it), `conj-reconstruction-at-training-cost` part (b) (refuted),
`conj-paired-advantage-price` (common random numbers). Loose ends: the papers to
place listed in `STATE.md`, the factor ln|U| of the label-only price, the upper
inclusion of `conj-seed-price-is-ngca-price`, and Halil's four decisions.
