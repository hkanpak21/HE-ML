# Theory context

Every agent reads this file first, in every session: Claude sessions, their
subagents, Codex and Antigravity. It holds what is true of the theory work at
any time. What changes from session to session lives in `STATE.md` beside it.

## What we are building

A theory of the security of learning procedures, measured in the units of
learning itself. The objective, adopted by Halil on 2026-10-25, is to price an
adversary against a learning procedure in the same units as the procedure's own
training (samples, training runs, queries, compute of a stated learner class),
prove the prices by reduction to learning problems with known thresholds, with
or without the learning oracle, and measure the same prices by experiment, the
oracle supplying the training runs. The two sides of every question are the
statistical one (what an unbounded attacker can do from the information
available) and the computational one (what an efficient or learning-bounded
attacker can do). Halil's constraints:

- A cheap cryptographic plug-in does not count. Finding that some aspect of a
  model reduces to or yields a pseudorandom generator or a one-way function
  would count.
- Every quantity must be realizable or approximately realizable by experiment.
- Polynomial-time adversaries are fine. Definitions alone are not results.
- Beautiful mathematics comes first. Any of the three rules above may be broken
  for a result whose mathematics is beautiful, and ugly mathematics is not
  wanted even when it obeys them (Halil, 2026-10-25).

The knowledge base of the line, with every fact about prior work, every past
search and every open problem, is `sink/formalizing/`. Its `README.md` holds the
search gate, which every agent obeys before any literature search.

## Halil's framing of the computational view, 2026-10-25

Quoted from the session of that day, spelling kept. These two passages set what
the theory is for.

> "can we pose these as a computational problem. Eg there can be cases where it
> is asymptotically achievable but it turns out it needs exponentially many
> evaluations of the function which we can label this as inefficient and build
> the theory around these. A weaker adversary who needs to obey to laws of
> computation ... Eg we can pick a computational problem family and we can
> reduce a learning security problem to it with or without using the ai oracle
> we have developed?"

> "given an adversary with some objectives can we measure its success in terms
> of copmutational efficiency and reduce these to results we already know of.
> ... Given a learning algorithm for me to reconstruct an image from a result of
> the model what I would need is a model as strong as the initial classifier
> ... I can pose the learning problem of adverseries reconstructor model again
> as a learning problem with inputs as intermediate vectors and result as raw
> data of the initial model. ... I get no query bounds, no geometric bounds pure
> learning on both sides and in case I can reduce the reconstruction work to
> learning problem that is being attacked I can have a clear lowerbound which is
> the performance of initial model."

On practical efficiency, from the same day: training one MNIST model is cheap,
training every leave-one-out twin a certificate needs is not, and the learning
oracle is what hands those twins over. A result that needs the oracle should say
what it would cost to approximate the oracle by real training.

## Halil's instructions of 2026-10-25

- "the reading should be omniscent to all agents for all agents and also it
  should be time independent". Every agent reads this file and `STATE.md`, and
  any space can run at any time without depending on the order of runs.
- "I dont want to see any .tex files out there or tex artifacts rather I only
  want to manage only one folder where I have my pdfs to be read". Halil reads
  `lib/theory/` only, and it holds PDFs only.
- "only compile that folder on results that you think I should read such as
  important definitions and results we get". A reading PDF is written only for
  a result worth Halil's time.
- "within that same folder have a booklet where we gather everything from start
  to finish regarding our theory". `lib/theory/booklet.pdf` is the whole theory.
- "start building up the theory based on our discussions again within the same
  round formatting". Rounds follow the builder and challenger protocol below,
  taken from `sink/2026-10-16-formal-tuning/README.md`.
- "you can orchestrate more than one sessions for different thinking spaces".
- "use GPT 6 astra from codex cli and argon from aggy cli for discussions ...
  use these models for discussion only, for development use here". See the
  section Discussants.
- "instead of astra let us use sol 6.1 which is cheaper and better", later the
  same day, and argon may bypass permissions. See the section Discussants.
- On the decisions put to him that evening. The objective of booklet chapter 1
  is adopted as written. On the oracle definitions: "im unsure whether we
  should fix it currently while developing the theory". So both seed-access
  modes stay available and each result names the mode it needs. On hardness
  that comes from a data law: "indeed even better if we can realize hard
  problems out there in the literature. We need such mappings we cannot just
  say our problem is wrong because XYZ". On the next target: "You may decide
  on what to follow up with".
- The attacker class for lower bounds, chosen the same evening: two games, never
  mixed. Population statistical-query attackers of frozen clients give
  unconditional bounds, and polynomial-time attackers with the record-level
  view give bounds conditional on lattice or other named hardness.
- Later that night: "please proceed the development and simplfy whenever
  possible". Every space prefers the simplest statement and proof that carries
  a result, and cuts objects that do not earn their place.
- "I dont want ugly mathematics in short. Any of these bulletpoints can be
  violated for the sake of beautiful mathematics", on the three constraints of
  the section above.
- "fill them on the fly in detail instead of using a herd of subagents", for
  paper notes, see the repo `CLAUDE.md`.

## Where things are

| Path | Holds | Written by |
| --- | --- | --- |
| `lib/theory/booklet.pdf` | the whole theory, start to finish | `tools/build.py` only |
| `lib/theory/booklet-changes.pdf` | the booklet's changes since the last commit | `tools/build.py --changes` |
| `lib/theory/YYYY-MM-DD-<slug>.pdf` | a reading Halil should read | `tools/build.py`, from `readings/` |
| `lab/theory/CONTEXT.md` | this file | Halil's instructions only |
| `lab/theory/STATE.md` | the current state, at most 80 lines | the integrator, rewritten each session |
| `lab/theory/booklet/` | the booklet source, one main file and chapter files | the integrator only |
| `lab/theory/readings/YYYY-MM-DD-<slug>.md` | sources of the reading PDFs | the integrator |
| `lab/theory/spaces/<space>/` | one thinking space: `README.md` and `round-NN/` folders | that space's session only |
| `lab/theory/tools/` | `build.py`, `discuss.sh`, `argon_audit.py`, `prompt-template.md`, `verify.mjs` | the integrator |
| `lab/theory/discussants.csv` | one row per external discussion call | `tools/discuss.sh` |
| `lab/theory/GATES.md` | the completion ledger of the current milestone | the integrator |
| `lab/theory/milestone.json` | the open milestone: its spaces with their first and last rounds | the integrator |
| `lab/theory/gates/YYYY-MM-DD-<slug>.md` | the ledgers of closed milestones, never rewritten | the integrator |
| `lab/theory/integration-log.md` | what the integrator re-derived before each merge, and what it took on trust | the integrator, appended |

Nothing in `lib/theory/` is edited by hand. Nothing else in the repository
holds theory sources.

## Objects and statuses

Every definition, borrowed result, lemma, theorem and conjecture has a permanent
slug: `def-`, `fact-`, `lem-`, `thm-`, `prop-`, `conj-`, then two to six
lowercase words read off its content. A slug is never changed or reused. A
borrowed result uses the `facts.md` slug of `sink/formalizing/` when one exists.
The status of an object is one of the following.

| Status | Meaning |
| --- | --- |
| open | stated, no argument |
| sketch | an argument with a gap |
| accepted | its latest verdict is ACCEPT, in a round with BLOCKING 0 or in a space whose last round ends with BLOCKING 0 |
| checked | Halil read it and said so in a session |
| borrowed | from a paper, with library key, theorem number and fact slug |
| refuted | shown false, kept with its counterexample |

An agent never marks anything checked.

## Spaces and rounds

A space is one line of thought, run by one Claude session at a time. Spaces run
in parallel and in any order. Each has `lab/theory/spaces/<space>/README.md`
with its question, its scope and its owner session, and numbered round folders.

A round `round-NN/` holds three files.

1. `builder.md`, by the space's Claude session: responses to every open
   challenge by slug, then new or revised objects, each with slug, statement,
   status, uses, proof or sketch, and a paragraph on what the object would mean
   without the oracle or in the other regime (statistical against
   computational).
2. `prompt-<discussant>.md` and `discussant-<discussant>.md`: the discussion
   turn, run by `tools/discuss.sh`. The discussant reads the builder file and
   the space's earlier rounds, and ends with the verdict block below.
3. `summary.md`, by the builder after the discussion: one paragraph on what
   changed, the slugs accepted, the challenges still open.

The verdict block is a `text` code block under `## Verdicts`, one line per
object, `VERDICT <slug> ACCEPT|REVISE|REJECT`, and one line `BLOCKING <n>`
counting the open challenges that would make a statement false or a definition
ill-posed. A challenge is named `ch-<slug>`.

Round `round-00` of a space is its literature round. Its builder file states
what the literature proves on the space's question, with exact hypotheses, the
library key and theorem number of each statement, and the `facts.md` slug where
one exists. It then names the gaps and proposes aims, each a `conj-` or `def-`
object with what would count as settling it, its regime, and how an experiment
would measure it. Later rounds prove or refute toward the aims the discussion
kept.

In `builder.md` each object starts with a heading `### <slug>: <name>`,
followed by the lines `status:` and `uses:` (slugs, or `none`), then the
statement, then the proof or sketch, then the paragraph on the other regime. A
verdict line names the object by the same slug. A literature statement the space
relies on is a `fact-` object, with the library key and theorem number in its
statement.

Round files are Markdown with mathematics in single and double dollars. Every
non-trivial claim in them carries one of four labels: proven (with the proof or
a cited theorem), heuristic (with what is assumed), empirical (with on what), or
open. The status of an object and the label of a claim are different things.

A space proposes and the integrator merges. A space never edits the booklet,
`STATE.md`, this file or `sink/formalizing/`. New facts or search rows it finds
go in its `summary.md`, under `## For the registers`, for the integrator to
move.

## Discussants

Development, meaning proofs, booklet text and builds, is done by Claude only.
The two external models only discuss, in the discussant role.

| Name | Command behind `tools/discuss.sh` | Plan |
| --- | --- | --- |
| sol | `codex exec -m gpt-6.1-sol -c model_reasoning_effort="high" -s read-only` (Codex CLI 0.164.0 or later) | ChatGPT, 20 dollars a month |
| argon | `agy -p --model gemini-4-argon-high --mode plan --dangerously-skip-permissions`, one call at a time | Antigravity, 20 dollars a month |

Halil set this on 2026-10-25: "instead of astra let us use sol 6.1 which is
cheaper and better", and argon may bypass permissions. astra (gpt-6-astra) is
retired from the rotation. Its files of the first milestone stand.

sol runs in a read-only sandbox, reads any file and can run read-only commands,
PDF text extraction included. A call costs about 30,000 tokens of overhead before
any work. Codex 0.155.1 rejected gpt-6.1-sol, and 0.164.0 accepts it.

argon runs headless with permissions bypassed, so it can open PDFs with
`pdftotext`. Its workspace is the repository, the PDF folder behind the
`lib/literature/pdfs` symlink, `~/Documents/RESEARCH/FORMAL_SECURITY` and a scratch
folder of its own for each call. `discuss.sh` tells it to judge the objects one at
a time and append each judgement to the scratch file before starting the next. The
reason is a measured failure. On 2026-10-25 argon-high, judging a whole round in
one turn, thought for 22,000 to 27,000 tokens without streaming any, and the
client's 5-minute stream idle timeout cut every attempt. The scratch file becomes
the discussant file. After every call `tools/argon_audit.py` reads the agy
transcript and rejects the call if argon wrote outside its scratch folder or ran a
command that changes files. The audit line goes into the discussant file's header.

The budget per space: one discussant call per round, alternating sol and argon,
and both only in the round that closes a milestone. Every call appends a row to
`discussants.csv`. If a call fails on a usage limit, the round continues with the
other discussant, and the summary says so. An answer without a verdict block is a
failed call. `discuss.sh` keeps it as `<output>.noverdict` and logs it, and the
round retries or falls back.

Usage: `lab/theory/tools/discuss.sh <sol|argon> <prompt.md> <output.md>`. A
prompt names the discussant's role, the files to read by path, the question,
and the verdict format. It never pastes file contents.

## Session routine

1. Start. Read this file, `STATE.md`, and for a space its `README.md` and its
   last round's `summary.md`. Before any literature search, follow the search
   gate of `sink/formalizing/README.md`. A space records the rows of a new
   search in its `summary.md`, never in `searches.md` itself.
   A session that reads a paper fills its note at
   `lib/literature/notes/<venue>/<Key>.md` in the same session, in detail, with
   the exact statements and theorem numbers it used. It reads the note from disk
   right before writing and adds to it, so another session's text survives.
2. Work in rounds, as above.
3. End. A space session writes its `summary.md` and stops. The integrator merges
   accepted objects into the booklet, runs `python3 lab/theory/tools/build.py
   --changes`, rewrites `STATE.md`, and writes a reading PDF only for a result
   worth Halil's time.

## The integrator

The integrator is the Claude session that owns the booklet. It reads every
space's summaries, merges accepted objects with their status, keeps one name for
one thing across spaces, moves register entries into `sink/formalizing/`, and
decides what reaches `lib/theory/`. When two spaces define one object
differently, it records both and asks Halil.
