# Positioning

Five slots. Fill every one before writing any methodology. The claim in slot 4
is the claim in `CONTEXT.md` and in the abstract, in the same words.

## 1. Setting

FILL. The problem, the parties, and what each one is assumed to know.

## 2. What exists

FILL. The two or three closest works, by citation key, each with a note under
`lib/literature/notes/`. A work named here without a note is not yet read.

## 3. The gap

FILL. A factual limitation with a pointer to where the work states it or where
it stops. Never "nobody has tried". Say whether the limitation is stated by the
authors or found by us, because those are different facts.

## 4. The claim

FILL. The narrowest claim worth publishing, in one sentence. Carry the
qualifiers that make it true, and carry them here rather than adding them later
under review.

## 5. Why it is hard

FILL. The obstacle that makes the claim non-trivial. If there is none, the gap
is probably already closed.

## Status

Written on FILL. Approved on FILL.

## Searches, and what they returned

2026-10-16. Black-box against white-box membership inference. Occupied.
Sablayrolles et al., ICML 2019, give the Bayes-optimal attack under a posterior
assumption, and it depends on the loss alone. Suri, Zhang and Evans, TMLR 2024
(arXiv:2406.11544), argue the assumption fails for SGD and give a white-box
attack (IHA). Neither note is written yet.

2026-10-16. "Federated learning attacks are evaluated under unrealistic
assumptions." Occupied. Wainakh et al., Sensors 2023 (48 papers, six evaluation
fallacies, excluded venue). Huang et al., NeurIPS 2021, for gradient inversion.
Shejwalkar et al., IEEE S&P 2022, for poisoning. A poisoning SoK benchmark,
arXiv:2502.03801, venue not verified. A 2026 preprint, arXiv:2603.20615.

2026-10-16. Final model against all iterates (hidden state). Cebere, Bellet and
Papernot, ICLR 2025: with a crafted gradient at every step, releasing only the
final model does not improve the privacy guarantee.

2026-10-16. One game framework for inference risks. Occupied for one trained
model. Salem et al., IEEE S&P 2023 (SCEKPSTZ23, read in full), put membership,
attribute and property inference, DP distinguishability and reconstruction into
one game anatomy and prove reductions and separations among them. Their Sec.
VI-D states that the games do not express concurrent computation and so do not
cover federated learning. The multi-party protocol, its channels and the steer
goal stay open.
