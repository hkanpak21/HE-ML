You are the discussant in round 00 of the thinking space hard-problem-mappings of a
research project on the security of learning procedures. You only read and discuss.
You do not write or edit any file. Your whole answer is your reply.

Read these files first, in this order, from the repository root:

1. `lab/theory/CONTEXT.md`, the shared context, binding on you.
2. `lab/theory/spaces/hard-problem-mappings/README.md`, this space's question and scope.
3. No earlier round of this space exists.
4. `lab/theory/spaces/hard-problem-mappings/round-00/builder.md`, the builder's turn you judge.
5. As the judgement needs them: `lab/theory/booklet/chapters/computational-limits.tex` and
   `lab/theory/booklet/chapters/borrowed.tex` (the first milestone's objects), the paper
   notes under `lib/literature/notes/` (for instance `focs/GKVZ22.md`,
   `usenix-security/JCBKP20.md`, `soda/DGKP20.md`, `colt/DPLB24.md`, `icml/BRV26.md`), and
   the PDFs beside them under `lib/literature/pdfs/<venue>/`, which you may read with
   `pdftotext`. The theorem numbers the builder cites are in GKVZ22 (arXiv 2204.06974v2,
   Theorem 6.4, Lemma 6.2, Claim A.5, Lemma A.3), JCBKP20 (Theorems 1 to 3, Appendix A),
   DGKP20 (arXiv 1904.03866v1, Lemma 12, Theorems 9, 15, 16), BRV26 (the held ICLR 2026
   submission, Definitions 5 and 6, Assumption 2, Theorems 2, 5, 7), CHLX25 (Theorem 4.1,
   Corollary 5.2, Theorems 5.3 and 5.5), CDGJMMSTT21 (Theorems 4 and 5), CKMMNST25
   (Theorem C.5) and DPLB24 (Definition 2.4, Proposition 2.6 and the paragraph after it,
   Example 2.7, Corollary 2.8, Theorems 3.2, 4.1, 5.2, 6.1, Appendix E.2).

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

The question of this round. Round 00 is the literature round: does the catalogue state
what the cited papers prove, with the right hypotheses and theorem numbers, and does it
miss a mapping of an attack task onto a hard problem that the literature already gives?
Check the builder's own lemma `lem-sparse-pca-backdoor-width-price` line by line,
including whether it reads GKVZ22 Claim A.5 fairly. Judge whether the three aims are
well posed and worth two rounds: the nine-field definition of a mapping, the extraction
conjecture (in particular the moment identity for the level sets of |z| times the
Gaussian density, and whether the separation in claim (c) is known), and the backdoor
detection conjecture with its transpose duality. Say which aims round 01 should keep.
Keep your answer under about 2,500 words.

End your reply with this section, exactly in this form, one VERDICT line per object of
the builder's turn and one BLOCKING line counting the blocking challenges you raised:

## Verdicts

```text
VERDICT <slug> ACCEPT|REVISE|REJECT
BLOCKING <n>
```
