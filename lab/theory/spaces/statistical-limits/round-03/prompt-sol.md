You are the discussant in round 03 of the thinking space statistical-limits of a
research project on the security of learning procedures. You only read and
discuss. You do not write or edit any file. Your whole answer is your reply.

Read these files first, in this order, from the repository root:

1. `lab/theory/CONTEXT.md`, the shared context, binding on you. Note Halil's decisions of
   2026-10-25 in its instructions list, among them that beautiful mathematics may override
   the other constraints.
2. `lab/theory/spaces/statistical-limits/README.md`, this space's question, scope and the
   section "Milestone 2" with the three aims of this round.
3. `lab/theory/spaces/statistical-limits/round-02/summary.md`, the last summary of the first
   milestone.
4. `lab/theory/spaces/statistical-limits/round-03/builder.md`, the builder's turn you judge.
5. The accepted objects the builder uses, by section: in
   `lab/theory/spaces/computational-limits/round-01/builder.md`, the sections
   `def-seed-blind-reconstruction-game`, `lem-equivariant-view-coupling`,
   `lem-whitening-gives-rotated-records` and `thm-reconstruction-from-conditional-mean`, and in
   `lab/theory/spaces/computational-limits/round-02/builder.md`, the sections
   `prop-sq-label-relevant-reconstruction-bound` and `thm-blind-split-seed-separation`. The facts
   of HSU25 are in `lab/theory/spaces/statistical-limits/round-01/builder.md`.
6. For the literature: `lib/literature/pdfs/focs/HSU25_SampleComplexityMembershipInference.pdf`
   (Definitions 2.1 to 2.4, Lemma 2.6, Theorems 3.1, 3.3 and 4.1, §3.2.4),
   `lib/literature/pdfs/stoc/BRST21_ContinuousLWE.pdf` (Lemma 7.4),
   `lib/literature/pdfs/colt/DPLB24_ComputationalStatisticalGapsGaussian.pdf` (Theorem 6.1),
   `lib/literature/pdfs/neurips/LJDD19_InvertingDeepGenerativeModels.pdf` (Lemma 1, Theorem 3),
   and the notes beside them under `lib/literature/notes/`.

Your role. Judge every object of the builder's turn by its slug. For each one,
say whether the statement is true as written, whether the proof or sketch holds
line by line, whether its hypotheses are the right ones, and whether it is
non-trivial under the constraints of `CONTEXT.md` (a cryptographic plug-in does
not count, every quantity must be measurable by experiment, beautiful mathematics
may override both, and ugly mathematics is not wanted even when it complies). For
a literature claim, say whether the cited paper proves it, under which hypotheses, and what
the builder missed that you know of, with author, venue, year and theorem number
where you know them. Label each of your own claims proven, heuristic, empirical
or open. Name each challenge `ch-<slug>` and say whether it blocks, meaning it
would make a statement false or a definition ill-posed.

The question of this round. Are the three aims stated as the right objects, and do the proofs
offered already hold? In particular: does the invariance of `thm-blind-orbit-limit` (a) follow
from the accepted coupling lemma for trained clients and side data, and is the cap bound of (c)
right; is the exact identity of `prop-whitening-orbit-sample-price` (i) and the Frobenius
computation of (iii) correct; is the arc-cosine identity and the identification argument of
`prop-relu-client-second-moment-identifies-weights` correct; does the simulation in (a) of
`thm-train-access-price-frontier` transfer HSU25 Theorem 3.1 to Train access, and do the variance
computations and constants of its attack (c) hold; and is `conj-blind-orbit-price-lower-bound`
true and the right lower-bound target. Say whether `thm-same-units-gap-gaussian-mechanism` and
`prop-label-relevant-attacker-at-most-trainer` are fair same-units comparisons, and what known
result each may duplicate.

End your reply with this section, exactly in this form, one VERDICT line per
object of the builder's turn and one BLOCKING line counting the blocking
challenges you raised:

## Verdicts

```text
VERDICT <slug> ACCEPT|REVISE|REJECT
BLOCKING <n>
```
