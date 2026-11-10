# Space: learning-attacker prices

Owner: the integrator session, which runs two Claude Opus 5.5 agents in this space, a builder
and a challenger, from 2026-10-28. One builder and one challenger, each continued across rounds
so that it keeps its own context.

Halil, 2026-10-28: "Ok I assume the state of theory we have as today is not standing well. So
now I want you to create a discussion round again among two opus models that one tries building
the theory upon our accumulated knowledge and the critiques we have against the other models etc".

## Question

Rebuild the theory on what survived the council of 2026-10-27. Every critic of that council named
one gap. No result prices a learning attacker, a shadow model or a VAE, in learning units, with a
measured side and a proven side in one access model. Halil's aim, in his words in
`readings/2026-10-27-what-you-want.md`, is "a bound on success of such a VAE (or anything) given
the setting", measured "with the computational terms", with hardness arriving when a measured
price meets a proven one.

## Scope

In scope: everything the theory and the council hold, `readings/2026-10-26-what-we-have.md`,
`readings/2026-10-27-definitions.md`, `readings/2026-10-27-council.md`, and
`council/2026-10-27-theory-directions/` with its meditations, critiques and `summary.md`. The
builder may keep, repair, replace or drop any object there. The council's corrections to registered
results bind until a round answers them.

Open rulings of Halil, not to be assumed: whether a pseudorandom seed generator counts as the
excluded plug-in, which reading of the programming rule he meant, and which target canaries serve.
A result that depends on one of them states the reading it uses.

Out of scope: the natural-data oracle (`prob-natural-data-oracle`, parked by Halil).

## Protocol

- Round 00 is the aims round. The builder states what stands after the council, with exact
  hypotheses and slugs, names the gaps, and proposes aims, each a `def-` or `conj-` object with what
  would settle it, its regime, and how an experiment would measure it.
- Rounds 01 to 09 prove or refute toward the aims the challenger kept.
- In each round the builder writes `builder.md` and the challenger writes `challenger.md`, ending
  with the verdict block of `CONTEXT.md`. From round 01 on the challenger writes the line
  `SATISFIED yes` or `SATISFIED no` before its verdict block. The builder writes the round's
  `summary.md` after reading the challenge. The harness refuses summary files from subagents, so the builder
  returns the summary in its reply and the integrator saves it verbatim.
- Halil, 2026-10-28: "keep the rounds running until challanger is satisfied or it makes 10
  rounds". The space stops at the first round from 01 on whose challenger writes `SATISFIED yes`
  with BLOCKING 0, or after round 09.
- Then fable (claude-fable-5-1, a subagent) and sol (`tools/discuss.sh`) critique the result, in
  `critique/fable.md` and `critique/sol.md` from `critique/prompt-critique.md`, and the integrator
  writes the reading for Halil: "after any of these two happen initialize a critique fable and sol
  agents for giving a critique then well talk upon".
- The prompts of each round are kept as `prompt-builder.md` and `prompt-challenger.md`.
- `GATES.md` is this space's completion ledger, checked with `tools/verify.mjs debate` and
  `tools/verify.mjs critique`.

Halil set the two Opus agents in place of the external discussants for this space. argon's
critiques of the council, deferred for its quota, do not block it.

## Round log

| Round | Builder | Challenger | Verdicts | BLOCKING |
| --- | --- | --- | --- | --- |
| round-00 | aims, 4 objects | 1 ACCEPT, 2 REVISE, 1 REJECT | ch-learner-class-gap: P1 false, the learner class enters the price | 4 |
| round-01 | 6 objects, all 21 challenges answered | 5 ACCEPT, 1 REVISE, SATISFIED no | ch-finite-ratio-profile: the linear class reads a whole function at finite T/d | 1 |
| round-02 | 6 objects, first price known at a measured dimension | 5 ACCEPT, 1 REVISE, SATISFIED no | ch-chosen-query-scaling: chosen query norms defeat release noise | 1 |
| round-03 | 4 objects, the release re-learning bracket | 4 ACCEPT, SATISFIED yes | ch-kappa-in-error-term, not blocking | 0 |
