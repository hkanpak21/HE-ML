# Round 00, summary: hard-problem mappings, the literature round

Discussant: sol (gpt-6.1-sol). argon is out of quota until about 2026-10-27 13:30,
so this space runs on sol. Verdicts: 1 ACCEPT, 9 REVISE, 0 REJECT, BLOCKING 9.

What changed. The builder read the first milestone's results as mappings (a table of
six entries), stated six literature facts with theorem numbers read in the papers,
proved one lemma on GKVZ22's sparse-PCA backdoor, listed the gaps, and proposed three
aims: a uniform definition of a mapping, the extraction conjecture, and the backdoor
detection conjecture. sol accepted the DPLB24 fact and confirmed the level-set identity
behind the extraction conjecture line by line (the level sets of $\lvert z\rvert\phi(z)$
carry exactly the Gaussian's first two moments, so the Bayes link of a law of
generative exponent 2 has generative exponent 4). sol found three source errors the
catalogue had imported or understated. GKVZ22 Appendix A contains a parameter error:
at the printed parameters the spiked weights are detected by the builder's own
coordinate-variance test, and the activation condition is insufficient (with
$\theta=1$, $\lambda=1.1$, $\tau=1$ and a unit input orthogonal to the key, the triggered
preactivation has variance 3.42 and mean ReLU 0.738, below the threshold), so the
lemma's sentence "Claim A.5 is true as stated" is withdrawn. CDGJMMSTT21 measures
advantage as success minus one half in Definition 5 but proves Theorem 4 for a
difference of acceptance probabilities, twice that. BRV26's Corollary 3 needs
LeakyReLU slope at least 1/100 and bounded condition numbers. sol judged the
backdoor conjecture's Gram claim and transpose transfer false as stated, and the
definition's exponent ratio undefined.

Slugs accepted. None yet. `fact-generative-exponent-post-processing-monotone` has
verdict ACCEPT in a round with BLOCKING 9, so it becomes accepted only if the space's
last round ends with BLOCKING 0.

Challenges open, all answered in round 01.

| challenge | blocks | object |
| --- | --- | --- |
| `ch-sparse-pca-source` | yes | `fact-gkvz22-backdoor-scope`, `lem-sparse-pca-backdoor-width-price` |
| `ch-sparse-pca-quantifiers` | yes | `lem-sparse-pca-backdoor-width-price` part (c) |
| `ch-collision-parameters` | yes | `fact-frozen-gaussian-layer-collision-hardness` |
| `ch-encoding-normalization` | yes | `fact-instance-encoding-privacy-learnability` |
| `ch-mapping-price-types` | yes | `def-hard-problem-mapping` |
| `ch-extraction-game` | yes | `conj-extraction-priced-by-generative-exponent` |
| `ch-feature-equivalence` | yes | `conj-backdoor-detection-is-ngca` (b) |
| `ch-transpose-transfer` | yes | `conj-backdoor-detection-is-ngca` (c) |
| `ch-row-sq-transfer` | yes | `conj-backdoor-detection-is-ngca` (d) |
| `ch-extraction-catalogue` | no | `fact-jagielski-extraction-query-bounds` |
| `ch-defense-price` | no | `fact-chlx25-defendability-characterization` |
| `ch-carrier-policy` | no | `def-hard-problem-mapping` |

sol also named two missing mappings (CCGJY20 Observation 1, DPLB24 Proposition 3.7)
and asked that the absence claims of Part 3 be read as "not found within the recorded
search scope". sol recommends round 01 prove the extraction separation first, keep the
definition short with one transfer lemma, and split the backdoor conjecture.

## For the registers

New facts, proposed for `sink/formalizing/facts.md`.

- `fact-frozen-gaussian-layer-collision-hardness`. BRV26 (held anonymous ICLR 2026
  copy): under Assumption 2 (symmetric bounded perceptron hardness, which the paper
  derives from worst-case lattice problems by citation), a frozen compressing Gaussian
  first layer with bilipschitz later layers on integer inputs resists approximate
  collisions, and a statistically undetectable backdoor gives exponentially closer
  collisions (Definitions 5 and 6, Theorems 2, 5 and 7, Corollary 3 with LeakyReLU
  slope at least 1/100 and condition numbers at most $2^{n^{1/5}}$). Read full,
  2026-10-25, this space.
- `fact-generative-exponent-post-processing-monotone`. DPLB24 Proposition 2.6 and the
  paragraph after it, Example 2.7 (ii), Corollary 2.8, Theorems 4.1, 5.2 and 6.1, and
  the diagonal caveat of Appendix E.2. Read full, 2026-10-25, this space.

Corrections to existing facts.

- `fact-jagielski-extraction-query-bounds`: JCBKP20 Theorem 3 is informal with no
  formal version; its exponent and DGKP20 Theorem 16's are printed $O(h)$ where Lemma
  12 with Theorem 15 gives $e^{\Omega(h)}$; DGKP20 Section 2 says uniform $[0,1]$
  weights while Lemma 3 needs Gaussian rows; the bound is on queries times squared
  inverse tolerance; Theorem 2 shows NP-hardness of inequivalence (coNP-hardness of
  equivalence under many-one reductions). Source: round-00 builder and discussant.
- `fact-gkvz22-backdoor-scope`: Appendix A (Claim A.5 with Lemma A.3) contains a
  parameter error, detectable at its printed parameters and with an insufficient
  activation condition. Source: `lem-sparse-pca-backdoor-width-price` and sol.
- `fact-instance-encoding-privacy-learnability`: Theorems 4 and 5 are proven for a
  difference of acceptance probabilities, twice the advantage of Definition 5.
- `fact-chlx25-defendability-characterization`: Corollary 5.2 gives no universal
  sample multiplier between detector and learner.

Search rows, proposed for `sink/formalizing/searches.md`.

| date | slug | question | tool and index | query | scope | hits | kept | coverage | updates |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-25 | search-extraction-generative-exponent | Is the sample price of extracting or distilling a trained single-index predictor, against the trainer's price, known through the generative exponent? | WebSearch, standard mode | distillation or model extraction sample complexity single-index model generative exponent teacher predictions versus labels | web, no venue filter | 9 | nil. DPLB24 (already held), Cotter et al. arXiv 2102.06849 and arXiv 2301.12245 (distillation, no single-index exponent), not read | partial, one query | none |
| 2026-10-25 | search-backdoor-detection-ngca | Is backdoor detection in random-feature models priced as non-Gaussian component analysis of the weight law? | WebSearch, standard mode | backdoor detection random features non-Gaussian component analysis hardness weights planted direction statistical query | web, no venue filter | 9 | nil. GKVZ22 and DKRS23 (held), separately | partial, one query | none |
| 2026-10-25 | search-sparse-pca-backdoor-regime | Has the regime of GKVZ22's sparse-PCA ReLU backdoor (detection by coordinate variance, size of the activation) been criticized? | WebSearch, standard mode, then WebFetch of two arXiv pages | "undetectable backdoors" random ReLU sparse PCA detection diagonal thresholding critique | web, no venue filter | 10 | Choudhary, Patlan, Palumbo, Hooda, Fawaz and Jha, arXiv 2605.04209 (Assumption 1 states sparse-PCA hardness for theta = o(k sqrt(log d / t)), Theorem 6.5, HTML read in part); Eggen, Reiestad, Gjøsteen and Strümke, arXiv 2605.13214 (abstract) | partial, no critique of Claim A.5 found | none |

Problems, proposed for `sink/formalizing/problems.md`.

- A candidate supporting problem under `prob-reduce-security-to-known-learning-problems`:
  does extraction of a trained model from random queries ever cost a larger sample
  exponent than training, and when? Round 01 states a theorem for known links.
- Tried line for `prob-reconstruction-hardness-without-one-wayness`: a compressing
  Gaussian client on uniform integer records gives no computational reconstruction
  bound, since exact reconstruction is already statistically impossible
  (round-00 builder, Part 3).
- Tried line for `prob-detection-band-hardness` and the backdoor problems: GKVZ22's
  sparse-PCA construction fails at its printed parameters
  (`lem-sparse-pca-backdoor-width-price`).
