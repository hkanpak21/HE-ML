# Round 03, summary

Space `computational-limits`, 2026-10-25, the aims round of milestone 2.
Discussant sol (gpt-6.1-sol), the only discussant until argon's quota returns.
Verdicts: ACCEPT 2, REVISE 7, REJECT 0. BLOCKING 11.

The round stated four aims with five literature facts. Sol accepted the LIP
framework of Ducas and van Woerden and the ZLIP algorithm facts, and kept three
aims after repairs. The ZLIP mapping holds as two reductions with a width loss of
$\sqrt{d\ln(2d+4)/\pi}$, not as an equivalence, and its upper direction needs fresh
sample blocks, a quantified rounding step and a stated arithmetic model. The
generation lemma it needs is Haviv and Regev, SODA 2014, Lemma 5.4. The separation
of the two games on noiseless pancakes holds after a primitive-label lemma fixes
the label scale, and it is a transfer of DKRS23's discussion of LLL-based NGCA to
a hidden client, not a new separation. The agreement test holds in the sample game
once each run has enough records. Sol asked that aim 1 be recast as quantitative
approximate inversion, and corrected three facts on degenerate cases (zero labels
in ZSWB22 Model 3.2, a point mass in DK22's Assumption 1.2, an atom at the origin
for the orthant identity). Round 04 follows Halil's instruction to simplify: it
proves three of the aims in four objects and withdraws aim 1 and the two facts it
needed.

## Slugs accepted

- `fact-lip-average-case`
- `fact-zlip-best-algorithms`

## Challenges open

Blocking: `ch-zswb-label-hypotheses`, `ch-dk-assumption-scope`,
`ch-spherical-origin-mass`, `ch-zlip-width-equivalence`,
`ch-zlip-fresh-coordinate-samples`, `ch-zlip-arithmetic-cost`,
`ch-hidden-label-scale`, `ch-games-hidden-client`, `ch-sq-fine-output-range`,
`ch-coarse-sample-budget`, `ch-relu-output-guarantee`.

Not blocking: `ch-kernel-finite-precision`, `ch-zlip-generation-prior-art`,
`ch-zlip-certificate-check`, `ch-sq-agreement-oracle`, `ch-relu-estimator-bias`,
`ch-generative-hardness-reference`.

## For the registers

New facts, read in the paper this session.

- `fact-lip-average-case`: DvW22 (Ducas and van Woerden, EUROCRYPT 2022),
  Definitions 2.1, 2.2, 3.3, 3.7, Lemmas 2.9, 3.4, 3.6, 3.9, 3.10. Note
  `lib/literature/notes/eurocrypt/DvW22.md`, PDF not placed. Accepted.
- `fact-zlip-best-algorithms`: Duc24 (Ducas, Designs, Codes and Cryptography
  2024), Theorems 1 and 2, with the provable $2^{n/2+o(n)}$ and heuristic
  $2^{0.146n+o(n)}$ costs as Duc24 reports them, dated 2026-10-25. Note
  `lib/literature/notes/dcc/Duc24.md` (new venue folder `dcc`). Accepted.
- `fact-lll-recovers-discrete-hidden-labels`: ZSWB22 Model 3.2, Theorem 3.3,
  Lemma 3.4, Model 4.3, Corollary 4.4, with sol's correction that Theorem 3.3 fails
  when the labels $x_2,\dots,x_{d+1}$ all vanish (also an indexing slip in the
  paper's Lemma 6.3), and that the LLL output is rationally proportional to the
  labels. Note `lib/literature/notes/colt/ZSWB22.md`, now full-read.
- DK22 (Diakonikolas and Kane, COLT 2022), Theorem 1.3 and Section 2, read and
  noted at `lib/literature/notes/colt/DK22.md`. Correction for any register entry:
  a law of support size at most $k$ satisfies only the arithmetic condition of
  Assumption 1.2, not its anti-concentration and concentration conditions, and
  the generators $r_j$ must be known.
- WDS19 (Wu, Dimakis and Sanghavi, NeurIPS 2019), Theorem 1, Claim 1, Fact 1,
  noted at `lib/literature/notes/neurips/WDS19.md`. Correction: the orthant
  identity holds for spherically symmetric laws with no atom at the origin.

Problem restatement proposed: `prob-blind-inversion-relu-clients`, in sol's
quantitative form. Find a polynomial-time map whose mean squared reconstruction
error, after one common orthogonal alignment, is small relative to the record
energy, for a frozen expansive Gaussian ReLU client, with stated confidence,
expansion, tail parameters and precision. Start with Gaussian records, where Gram
estimation (WDS19) must be turned into stable inversion through the active
submatrices, then a stated NGCA family. Pointer, not read: Chen, Li and Li,
NeurIPS 2022, Theorem 3.1, SQ hardness for constructed generators whose outputs
are sums of ReLUs, as sol gives it.

New search rows, for `searches.md`.

| date | slug | question | tool and index | query as run | scope | hits | kept | coverage | updates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-25 | search-zlip-hardness-status | How hard is the lattice isomorphism problem for rotations of $\mathbb Z^n$? | WebSearch, standard mode | Just how hard are rotations of Z^n lattice isomorphism problem algorithms cryptography | web, no filter | 10 | Duc24, fact-zlip-best-algorithms. Bennett et al. EUROCRYPT 2023 and ePrint 2023/1735 listed, not read | partial, one query | none |
| 2026-10-25 | search-lip-cryptography-average-case | Where are average-case LIP and its sampling defined? | WebSearch, standard mode, two queries, then the CWI copy | Ducas van Woerden lattice isomorphism problem cryptography EUROCRYPT 2022 average-case discrete Gaussian basis | web, no filter | 9 | DvW22, fact-lip-average-case | partial, IACR copies refuse the fetch tool | none |
| 2026-10-25 | search-ngca-lattice-basis-reduction | Is NGCA with a discrete hidden law solved by lattice methods? | WebSearch, standard mode | Non-Gaussian component analysis via lattice basis reduction Diakonikolas Kane polynomial time discrete | web, no filter | 9 | DK22 | exhausted for the question | none |
| 2026-10-25 | search-relu-generative-gram | Can the Gram matrix of a one-layer ReLU generative model be learned from samples? | WebSearch, standard mode | Learning distributions generated by one-layer ReLU networks Wu Dimakis Sanghavi truncated Gaussian estimation | web, no filter | 10 | WDS19 | partial, one query | none |
| 2026-10-25 | search-discrete-gaussian-generation | How many discrete Gaussian samples generate a lattice? | WebFetch of arXiv 1311.0366 on the discussant's pointer | none, a direct read | one paper | 1 | Haviv and Regev SODA 2014 Lemma 5.4 | exhausted for the question | none |

Discussant calls: one sol call, exit 0.
