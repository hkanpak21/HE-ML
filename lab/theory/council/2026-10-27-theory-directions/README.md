# Council of 2026-10-27: directions of the theory

Halil, 2026-10-27: "We have a bunch of nice output in thery right now. Instead of us
blindly picking what we have initialize an agentic coucil to discuss these topics.
Initialize opus agents for each and make them meditate on their selection of topic
and then send each of their resulting meditations on this topic to argon, fable and
sol 6.1 agents for them to read and have an critique upon. Then we talk agaibn".

The topics come from the discussion of 26 and 27 October, whose state Halil reads in
`lib/theory/2026-10-27-what-you-want.pdf` (source `readings/2026-10-27-what-you-want.md`)
and `lib/theory/2026-10-27-definitions.pdf` (source `readings/2026-10-27-definitions.md`).

## Topics

| Folder | Question in one line |
| --- | --- |
| `pseudorandomness-for-learner-classes/` | Can learnability and security be one notion, pseudorandomness of a target family for a learner class against a random-oracle reference, with trainer, attacker and auditor as three parties of one setup? |
| `degree-of-a-channel/` | Where does hardness live without planting? The channel from a secret to the attacker's view, with the seed as noise, priced by its degree or statistical dimension for a shadow-learning attacker. |
| `trainer-as-filter/` | What composition theorem makes the trainer a filter, so that what it did not learn stays hidden, for trainers that memorize, and how does the split of a record into a population part and a random-oracle individual part price memorization? |
| `oracle-as-random-oracle/` | What does reading the learning oracle as a lazily sampled random oracle buy, with programming as the rule for the designer's modifications, and what does an experiment measure in this frame? |

## Protocol

1. A meditator (Claude Opus 5.5) per topic writes `<topic>/meditation.md`. It reads the
   files its brief names, thinks the topic through, and ends with numbered claims in the
   object heading format of `CONTEXT.md`, each with a status in the four words.
2. Three critics read each meditation and judge every claim by its slug.
   - fable (Claude Fable 5.1, a subagent) writes `<topic>/fable.md`.
   - sol (gpt-6.1-sol, `tools/discuss.sh`) writes `<topic>/sol.md` from `<topic>/prompt-critique.md`.
   - argon (gemini-4-argon-high, `tools/discuss.sh`) writes `<topic>/argon.md` from the same prompt.
3. The integrator reads all of it and writes a reading for Halil. Then Halil and the
   integrator talk.

Halil set aside the budget of one discussant call per round for this council. argon is
out of quota, and Halil stopped its queued calls on 2026-10-27: "no need in case we dont
have quota it should come tomorrow". Its four critiques run on 2026-10-28 or later, with
`<topic>/prompt-critique.md` unchanged, and the reading of the council is written from
the fable and sol critiques first.

## Out of scope

The natural-data oracle, `prob-natural-data-oracle`, is parked by Halil and no topic
develops it.
