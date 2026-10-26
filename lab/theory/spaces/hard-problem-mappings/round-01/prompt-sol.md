You are the discussant in round 01 of the thinking space hard-problem-mappings of a
research project on the security of learning procedures. You only read and discuss.
You do not write or edit any file. Your whole answer is your reply.

Read these files first, in this order, from the repository root:

1. `lab/theory/CONTEXT.md`, the shared context, binding on you.
2. `lab/theory/spaces/hard-problem-mappings/README.md`, this space's question and scope.
3. `lab/theory/spaces/hard-problem-mappings/round-00/summary.md`, and, for the challenges
   it lists, `lab/theory/spaces/hard-problem-mappings/round-00/discussant-sol.md` (your own
   review of round 00) and `round-00/builder.md`.
4. `lab/theory/spaces/hard-problem-mappings/round-01/builder.md`, the builder's turn you judge.
5. As the judgement needs them: the PDFs under `lib/literature/pdfs/<venue>/`, readable
   with `pdftotext`, in particular `jacm/FGRVX17_StatisticalAlgorithmsLowerBound.pdf`
   (Theorems 3.7, 3.13, 3.16, Lemma 3.10), `colt/DPLB24_ComputationalStatisticalGapsGaussian.pdf`
   (Definition 2.4, Lemma 2.3, Proposition 2.6 and the paragraph after it, Theorems 4.1 and
   5.2, Proposition 3.7, Appendix E.2 with Lemmas E.2 and E.3),
   `focs/GKVZ22_PlantingUndetectableBackdoorsMachine.pdf` (Appendix A, Claim A.5),
   `ieee-sp/CDGJMMSTT21_IsPrivateLearningPossible.pdf` (Appendix A.2 and A.3),
   `icml/BRV26_StatisticallyUndetectableBackdoorsDeep.pdf` (Corollary 3),
   `usenix-security/CCGJY20_ExploringConnectionsBetweenActive.pdf` (Observation 1,
   Proposition 1), and the booklet chapter `lab/theory/booklet/chapters/computational-limits.tex`.

Your role. Judge every object of the builder's turn by its slug. For each one, say
whether the statement is true as written, whether the proof or sketch holds line by
line, whether its hypotheses are the right ones, and whether it is non-trivial under
the constraints of `CONTEXT.md` (a cryptographic plug-in does not count, every quantity
must be measurable by experiment, beautiful mathematics may override both, and ugly
mathematics is not wanted even when it complies). For a literature claim, say whether
the cited paper proves it, under which hypotheses, and what the builder missed that you
know of, with author, venue, year and theorem number where you know them. Label each of
your own claims proven, heuristic, empirical or open. Name each challenge `ch-<slug>` and
say whether it blocks, meaning it would make a statement false or a definition ill-posed.

The question of this round. First, does the builder's response close each challenge you
raised in round 00, by name? Second, check `thm-extraction-exponent-price` line by line:
the finiteness of the chi-squared information of the noisy answers, the code and the
pairwise correlations, the use of FGRVX17 Theorem 3.7 with Lemma 3.10, the reduction from
weak fidelity with outputs bounded by one to the decision problem (Step 4), the parameter
choice of Step 5, the upper bound, the channel inequality, and the separation of part (d)
with its trainer side. Third, check `lem-level-set-moment-balance`,
`prop-learner-side-sq-transfer`, the revised `lem-sparse-pca-backdoor-width-price`, and the
three statements that replace the backdoor conjecture. Say whether the space has reached
a state with no blocking challenge. Keep your answer under about 2,500 words.

End your reply with this section, exactly in this form, one VERDICT line per object of
the builder's turn and one BLOCKING line counting the blocking challenges you raised:

## Verdicts

```text
VERDICT <slug> ACCEPT|REVISE|REJECT
BLOCKING <n>
```
