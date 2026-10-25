# Formalizing AI security, the shared context

This folder holds the context of Halil's line on formalizing AI security across
sessions. The line spans two repositories: HE-ML (this one) and
`~/Documents/RESEARCH/FORMAL_SECURITY`, whose wiki and programme are read here
and never edited from here. The design and its sources are in
`sources/2026-10-25-context-practices.md`.

A session that works on this line follows the routine below. The registers are
the single source of truth for what is known, proven, searched and open.

## Routine

1. Start. Read `STATE.md` whole. If its `updated:` date is older than the last
   heading of `log.md`, read the log back to that date and rewrite `STATE.md`
   before any other work. Then read only the register entries the task names,
   found by grep on their slugs. Done when you can name the active target and
   the slugs the task touches.
2. Search gate. Before any literature search, web search or subagent sweep, grep
   `searches.md` and `facts.md` for the question. A row whose scope covers the
   question answers it: cite the row and do not search. Otherwise run the search,
   then append its row to `searches.md`, empty results included, before using
   what it found. A subagent's brief carries the matching rows, and the subagent
   returns its new rows for the parent to append.
3. Derivation. Before proving anything, read its `results.md` entry and the
   `tried:` lines of its problem. A `proven` entry is used, never proved again.
   Reading. A session that reads a paper writes its note at
   `lib/literature/notes/<venue>/<Key>.md` in the same session, in detail, and
   adds or verifies the `facts.md` entries the reading settles.
4. Status change. Edit the entry and add a dated `history:` line in the same
   edit.
5. End. Append one entry to `log.md`, rewrite `STATE.md`, run
   `python3 sink/formalizing/tools/lint.py` from the repository root until it
   prints `LINT OK`. Done when the log entry names every slug whose status
   changed and every search row added.

## Files

| File | Holds | Edited by |
| --- | --- | --- |
| `STATE.md` | the current state, at most 80 lines | rewritten whole at each session end |
| `results.md` | our definitions, theorems, lemmas, conjectures | an entry per object, history kept |
| `facts.md` | facts about prior work, each with its pointer | an entry per fact, corrections kept |
| `searches.md` | every search ever run on this line, empty ones included | rows appended only |
| `problems.md` | open problems and targets, solved ones archived | an entry per problem |
| `log.md` | one entry per session | appended only |
| `sources/` | dated digests and research records the registers cite | written once, corrected by dated note |
| `tools/lint.py` | the checks of the section Lint | changed only with this README |

Papers live in the library of this repository, `lib/literature/pdfs/<venue>/`
with a note at `lib/literature/notes/<venue>/<Key>.md`. A note imported from
FORMAL_SECURITY points to the wiki page that holds its reading notes.

## Slugs

Every entry is a level-two heading `## <slug>` followed by `key: value` lines.
A slug is two to six lowercase hyphenated words read off the content, so a
session can predict it and grep for it before making a new one. Prefixes give
the kind: `def-`, `thm-`, `lem-`, `prop-`, `conj-` in `results.md`, `fact-` in
`facts.md`, `prob-` in `problems.md`, `search-` in `searches.md`. A slug is
permanent. A rename adds an `alias:` line and keeps the old slug findable. An
entry that is refuted, retracted, superseded, solved or withdrawn stays in its
file with its reason. Slugs existing elsewhere keep their spelling here: the
learning-oracle theory's `thm-coupling-certificate` stays
`thm-coupling-certificate`.

A value that runs over several lines continues on lines indented by two spaces.
`history:` and `corrections:` hold one dated line each, `- YYYY-MM-DD text`.
A path names its repository: `HE-ML:<path>` or `FS:<path>`, with an optional
`#<section>`.

## Entry formats

`results.md`, one entry per object of our own.

- `kind:` definition, theorem, lemma, proposition, conjecture or construction.
- `statement:` the object in words, usable without its proof.
- `where:` the file and section that state it with full mathematics.
- `uses-to-state:` and `uses-to-prove:` slugs, or none.
- `status:` proven, heuristic, empirical, open, refuted or retracted.
- `evidence:` the proof's location for proven, the assumption for heuristic, the
  run for empirical, the counterexample for refuted, the error found for
  retracted.
- `checked-by:` a person or a review with its date, or unchecked. An agent's
  proof counts as checked only after a person or a named review accepted it.
- `oracle:` needs-oracle, holds-without-oracle or n/a.
- `history:` dated lines.

`facts.md`, one entry per claim about one prior work.

- `claim:` one sentence.
- `paper:` authors, venue, year, and the library key when the paper is placed.
- `pointer:` theorem, section or page.
- `read:` full, abstract or recorded, with who and when. Recorded means copied
  from an earlier record without reopening the paper.
- `status:` verified, recorded, disputed or superseded.
- `record:` the file where the fact was first written.
- `corrections:` dated lines, or none. A correction keeps the old wording.

A fact enters only from a source that someone opened. Memory is never a source.

`searches.md`, one table row per search: date, slug, question, tool and index,
query as run, scope (venues, years, filters), hits, kept (keys, fact slugs or
nil), coverage (exhausted, or partial with the reason), and the earlier row it
updates. Screening decisions on single papers stay in
`lib/literature/screening.csv`, and the row points there.

`problems.md`, one entry per problem.

- `statement:` the question, answerable yes or no where possible.
- `posed:` who and when.
- `weight:` central (the line fails without it), supporting (a central problem
  needs it) or side (worth recording, not planned).
- `status:` open, partial, solved, refuted-as-posed or withdrawn.
- `literature:` the search slugs behind the belief that it is open, or
  unchecked.
- `tried:` dead ends with pointers to their sketches.
- `depends-on:` slugs.
- `claimed-by:` one holder and a date, or none.
- `where:` the file that states it in full.
- `history:` dated lines.

Solved and withdrawn problems move to the section Archive at the end of the
file.

`log.md` entries open with `## [YYYY-MM-DD] <session> | <kind> | <headline>`,
kind one of research, proof, search, ingest, decision, lint. Each lists what was
read, the slugs changed with old and new status, the search rows added, dead
ends and loose ends.

## Lint

`tools/lint.py` checks that slugs are unique across the registers and match the
slug rule, that every slug named in a uses, depends or alias line exists, that
statuses come from the closed lists above, that every `HE-ML:` path exists, that
facts carry paper, pointer and read lines, that problems carry a literature
line, that every search row has a date, a query and a scope, and that `STATE.md`
is at most 80 lines and no older than the last log entry. It prints `LINT OK`
only when every check passes.

## Where this folder sits

`sink/` is the drop zone of this repository, and `sink/INGEST.md` records why
this folder stays. Nothing in the research skill reads it. The repository's
`CLAUDE.md` points here, and `CONTEXT.md` keeps the binding terminology of
HE-ML. A term this line fixes enters `CONTEXT.md` when Halil fixes it.
