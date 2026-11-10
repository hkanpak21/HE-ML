# Refinement of 2026-10-30: the statement of the theory and its three theorems

Halil, 2026-10-30: "Proceed another set of discussion rounds on this with 3 fable agents I want
more rounds of refinement".

The set starts from `council/2026-10-29-statement-of-the-theory/statement/final.md`, the statement
in 26 clauses, and from the three statements to prove of that discussion's round 04. Halil read
them in `lib/theory/2026-10-30-statement-of-the-theory.pdf`. His four decisions there are open,
and no discussant settles them for him.

## Discussants

Three new subagents on Claude Fable 5.1 (`claude-fable-5-1`), fresh, so that no one reviews work
it wrote in the first discussion. Each keeps its context across the rounds of this set. Each owns
one theorem and the clauses of the statement nearest it, and is known by the slug of its theorem.

| Owner | Theorem | Source | Clauses in its charge |
| --- | --- | --- | --- |
| `stealth-cap` | `thm-stealth-uncertainty-cap-linearized` | `the-steering-attacker/round-04.md` | 7, 14, 15, 22, 23 |
| `noise-exponent-gap` | `thm-noise-exponent-gap` | `defence-as-honest-constraint/round-04.md` | 5, 6, 16, 17, 24, 25 |
| `batching-removes-class` | `thm-batching-removes-the-class` | `learning-attacker-class/round-04.md` | objective, 1 to 4, 8 to 13, 18 to 21, 26 |

The owner of `batching-removes-class` is also the editor of the statement, since its clauses hold
the definitions.

## Protocol

Each round has two steps.

1. Owner step, in parallel. Each owner writes `<owner>/round-NN.md`. It answers every challenge
   raised against its work in the previous round, gives its theorem's latest version in full with
   each step of the proof labelled, and proposes amendments to any clause of the statement, with
   the replacement text in full. From round 02 on, the editor first writes `statement/round-NN.md`,
   the statement with the previous round's surviving amendments integrated and a Dissent section.
2. Review step, in parallel. Each owner writes `<owner>/review-NN.md` on the other two owners'
   round files. It gives a verdict on each theorem and on each amendment, names each challenge
   `ch-<slug>` with whether it blocks, and ends with a Verdicts block and a BLOCKING count.

An amendment survives when no reviewer rejects it. When a reviewer amends it, the editor merges
the two texts. A rejected amendment returns to its proposer, who may revise it in the next round.

The set stops at the first round from 02 on in which every review ends BLOCKING 0, every theorem
verdict is ACCEPT, and no surviving amendment changes the content of a claim or its status, or at
the end of round 05. The editor then writes `statement/final.md`.

Discussants may run numerical checks of constants and identities, with scripts in
`<owner>/checks/` and the result reported in the round file. They run no experiment of the
oracle and no literature search in this set. A result cited from memory stays flagged as such.

Every file opens with the header `model`, `discussant`, `date`, `round` and, for the editor's
files, `role: editor`. When the harness refuses a write by a subagent, the subagent returns the
full text in its reply, and the integrator saves it verbatim and says so in the file.

## Inputs

`lab/theory/CONTEXT.md`, `readings/2026-10-27-what-you-want.md` (Halil's aim in his words),
`council/2026-10-29-statement-of-the-theory/halil-ideas.md` (the integrator's paraphrase of his
ideas from a meeting, below `CONTEXT.md` on conflict), `readings/2026-10-29-what-we-have.md`,
`readings/2026-10-30-statement-of-the-theory.md`, and the first discussion's files.

## Round log

| Round | Owner step | Review step | BLOCKING by reviewer | Converged |
| --- | --- | --- | --- | --- |
