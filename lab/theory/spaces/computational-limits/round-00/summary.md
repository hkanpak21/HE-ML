# Round 00, summary

Space `computational-limits`, 2026-10-25. Discussant astra (gpt-6-astra).
Verdicts: ACCEPT 6, REVISE 12, REJECT 0. BLOCKING 12.

The round set out thirteen literature facts, the judgement of
`FS:.tools/proof.tex`, and three aims. Astra accepted the refutation of the
proof note's main theorem, line by line, and accepted the residue lemma. It
accepted four facts as stated and asked for revisions of nine, three of them
blocking: the Gaussian normalization of BRST21 (its unit Gaussian has covariance
$I/(2\pi)$), the hypotheses of CDGJMMSTT21 Theorem 3, and the degenerate cases
of NRNT25 Proposition 3. It found the identifiability claim drawn from LKR06 too
broad, since a spherically symmetric non-Gaussian law is invariant under every
rotation. It pointed to prior art for the symmetry mechanism: Li, Zhang and
Arora (arXiv 2010.08515, Theorem C.1 and Remark C.1) prove that a
rotation-invariant initialization with an equivariant update gives an
orthogonally equivariant learner. On the aims it raised seven blocking
challenges: the simulation ignores labels and other side information
(`ch-transcript-side-information`), symmetric hidden laws make signed
reconstruction impossible (`ch-hidden-frame-symmetry`), invariance does not give
invertibility (`ch-whitening-and-invertibility`), a record-level view is not an
SQ interface (`ch-sq-attacker-interface`), the testing transfer used unbounded
queries and the wrong tolerance (`ch-ngca-testing-transfer`), the game's price
is undefined in degenerate cases (`ch-seed-price-definition`), and part (b) of
the third aim is false, because optimal square-loss prediction can be constant
while the label still reveals the hidden coordinate up to sign
(`ch-learning-is-not-direction-recovery`), with a sample-complexity gap in part
(a) (`ch-population-to-sample-reconstruction`). The discussion keeps the two
reconstruction aims, restated in separate SQ and sample games, with the
symmetry argument credited to Li, Zhang and Arora and the contribution placed
in the reduction and its prices. Round 01 answers every challenge by name.

## Slugs accepted

- `fact-fgrvx17-planted-clique-sq-bound`
- `fact-lei-random-expansive-layers-invertible`
- `fact-cohen-narcissus-equals-one-wayness`
- `fact-unsplit-unknown-client-inversion`
- `thm-fs-sq-black-box-reduction`, accepted as refuted: the proof note's theorem is false as stated
- `lem-sq-learner-post-processing`

## Challenges open

Blocking: `ch-gaussian-normalization`, `ch-nongaussian-identifiability`,
`ch-encoding-theorem-hypotheses`, `ch-gradient-inversion-degeneracy`,
`ch-seed-price-definition`, `ch-transcript-side-information`,
`ch-hidden-frame-symmetry`, `ch-whitening-and-invertibility`,
`ch-sq-attacker-interface`, `ch-ngca-testing-transfer`,
`ch-population-to-sample-reconstruction`, `ch-learning-is-not-direction-recovery`.

Not blocking: `ch-floating-point-identification`, `ch-pointwise-inversion`,
`ch-ngca-statistical-scope`, `ch-generative-upper-bound-scope`,
`ch-ideal-encoding-quantifiers`, `ch-unsplit-explanation`,
`ch-honest-oracle-qualification`, `ch-postprocessing-simulation-scope`.

## For the registers

New facts, each read in the paper this session.

- `fact-ngca-sq-lower-bound`: DKRS23 (Diakonikolas, Kane, Ren and Sun, NeurIPS
  2023, arXiv 2403.04744), Theorem 1.5 and Definitions 1.2 and 1.3, NGCA testing
  is SQ-hard under approximate moment matching to degree $d$, no chi-square
  condition. Read from the arXiv HTML. Astra confirmed the statement against the
  PDF. Note `lib/literature/notes/neurips/DKRS23.md`, PDF not placed.
- `fact-ica-breaks-rotation-perturbation`: LKR06 (Liu, Kargupta and Ryan, IEEE
  TKDE 18(1), 2006), Sections 3 and 4, ICA undoes a random orthogonal
  perturbation of independent non-Gaussian attributes, heuristic and empirical.
  Note `lib/literature/notes/tkde/LKR06.md`, PDF not placed.
- `fact-orthogonal-equivariance-of-training`: Li, Zhang and Arora, arXiv
  2010.08515 (ICLR 2021 as astra gives it, the arXiv page names no venue),
  Definition 3.2 (equivariant algorithm), Theorem C.1 (invariant initialization
  and an invariant update give an equivariant algorithm), Remark C.1 (stochastic
  and trajectory-dependent updates), Corollary C.2 (gradient descent from i.i.d.
  Gaussian initialization is orthogonally equivariant), Remark C.2 (momentum),
  Table 1 (Adam and AdaGrad are only permutation and sign-flip equivariant),
  Theorem 5.2 ($\Omega(d^2)$ samples for orthogonally equivariant learners on a
  quadratic task). Read from the arXiv HTML in round 01's preparation, note
  to be written in round 01.
- `fact-nrnt25-private-layer-hardness-route`: NRNT25 (Nguyen, Ren, Nie and
  Trieu, PoPETs 2025(3)), Definition 1.1 and Propositions 3 to 6, hardness of
  reconstruction argued for one attack route through private layers.
- Correction to `fact-fgrvx17-theorem-one-quoted-form`: the held copy of FGRVX17
  (arXiv v6) has no Theorem 1.1 of the form $q\tau^2\ge\Omega(n^{2\delta})$. The
  planted-biclique bounds are Theorems 2.9, 2.10 and 5.4.
- Correction to the FORMAL_SECURITY proof note's BB20 pointer: the SQ bounds for
  the secret-leakage variant are BB20 Section 12.3, Corollaries 12.17 and 12.18.
- Refined pointers for existing facts: `fact-sq-simulates-minibatch-sgd`
  (AKMSS21 Theorem 1c with the worst-case-rounding error definition),
  `fact-clwe-hardness` (BRST21 Corollary 4.2, Claim 2.22, Theorem 7.5,
  Corollary 9.4, with the $\rho(x)=e^{-\pi\|x\|^2}$ normalization),
  `fact-generative-exponent-measures-detection` (DPLB24 Theorem 3.2 is stated
  for weak recovery and proved against a product null, Remark 3.3).

Status change proposed for the integrator.

- `prob-attacker-lower-bound-from-hard-learning`: the FORMAL_SECURITY proof
  note on which its partial status rests is refuted as stated
  (`thm-fs-sq-black-box-reduction`, counterexample in round-00 `builder.md`,
  accepted by astra). What survives is `lem-sq-learner-post-processing`, a
  post-processing bound on the learner's access, valid against unbounded
  attackers. The problem should return to open, with the proof note recorded in
  its `tried:` line.

New search rows, for `searches.md`.

| date | slug | question | tool and index | query as run | scope | hits | kept | coverage | updates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-25 | search-rotation-perturbation-ica-attack | Is reconstruction under a secret rotation, attacked by ICA, known in privacy-preserving data mining? | WebSearch, standard mode | rotation perturbation privacy attack independent component analysis non-Gaussian data recovery random orthogonal transform | web, no filter | 10 | LKR06, fact-ica-breaks-rotation-perturbation. Mohaisen and Hong, arXiv 0906.0202, listed and not read | partial, one query, older literature | none |
| 2026-10-25 | search-ngca-privacy-reconstruction-bound | Does any work use NGCA lower bounds to price privacy or reconstruction from random linear encodings? | WebSearch, standard mode, then the arXiv HTML of 2403.04744 | non-Gaussian component analysis lower bound privacy random linear encoding reconstruction hardness statistical query | web, no filter | 10 | DKRS23, fact-ngca-sq-lower-bound. No privacy use found | partial, one query | none |
| 2026-10-25 | search-split-learning-rotation-reconstruction | Is a provable reconstruction barrier for split learning from the rotation invariance of a Gaussian initialization known? | WebSearch, standard mode | split learning unknown client weights rotation invariance Gaussian initialization reconstruction impossible provable | web, no filter | 9 | nil. Empirical attacks only (FORA, CVPR 2024, arXiv 2405.04115, and arXiv 2209.10119), not read | partial, one query | search-seed-attacker-resource |
| 2026-10-25 | search-orthogonal-equivariance-training | Is orthogonal equivariance of fully connected training from a rotation-invariant initialization known? | WebFetch of arXiv HTML 2010.08515, on the discussant's pointer | none, a direct read | one paper | 1 | Li, Zhang and Arora, fact-orthogonal-equivariance-of-training | exhausted for the mechanism, not for later uses in privacy | none |

New problems, for `problems.md`.

- `prob-reconstruction-hardness-without-one-wayness` (side): does
  computational Narcissus resiliency for a reconstruction relation, in a trained
  or initialized model, imply a one-way function? The blind first layer of
  `conj-seed-price-is-ngca-price` resists fine reconstruction under hCLWE while
  its map has easy preimages, so CKMMNST25 Theorem C.5 does not apply. Posed by
  this space, 2026-10-25.
- `prob-coarse-reconstruction-lattice-hardness` (supporting): is reconstruction
  of a pancake coordinate to constant correlation hard for polynomial-time
  algorithms under a lattice assumption? The lattice reduction of round 00
  reaches only reconstruction to accuracy of order $1/\gamma$. Posed by this
  space, 2026-10-25.

For the statistical space: for a Gaussian record law and a rotation-invariant
first layer, an unbounded blind server learns the records only up to a common
rotation, their Gram structure. The space `statistical-limits` owns that
statement.
