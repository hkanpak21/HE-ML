---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-25
prompt: lab/theory/spaces/computational-limits/round-05/prompt-sol.md
---

Proven. The uniform replacement closes `ch-coarse-zero-output`. The width restriction closes `ch-zlip-small-width`. Conditioning hardness on M closes the earlier inference between different computation models. One blocking implementation issue remains for the ZLIP reduction.

Proven. M admits a standard interpretation as a uniform stochastic algebraic RAM. Each listed operation costs one step, Gaussian draws are independent, and programs have finitely many fixed constants. This interpretation supports the coarse reduction. The ZLIP reduction still needs an explicit runtime convention for exact sampling.

`thm-coarse-reconstruction-lattice-hard`

Proven. I accept the statement under that interpretation of M. Its proof holds line by line.

Proven. On the correlation-success event, the inner product of the extracted direction with the hidden direction is nonzero. The extracted direction therefore cannot vanish. Replacing a vanishing output by an independent uniform direction preserves the success lower bound.

Proven. The replacement also preserves the null argument. Gaussian normalization generates a uniform direction using the listed primitives. Gaussian orthogonalization generates the Haar rotations used by the agreement tester, outside a probability-zero singularity event.

Proven. The remaining steps retain their round 04 justification. Equivariant coupling transports success to every hidden direction. Concentration converts reconstruction correlation into directional overlap. Independent protocol runs then give the agreement advantage and the stated exponential constant.

Proven. The hypotheses have the right scope. A fixed positive correlation constant gives a non-negligible detection advantage from non-negligible reconstruction success. No side data and membership in the equivariant protocol class support the coupling. Polynomial protocol runtime remains necessary for the polynomial-time security consequence.

Proven. Bruna, Regev, Song and Tang, STOC 2021, Corollary 4.2, proves the cited quantum reduction under the stated parameter restrictions. It does not simulate arbitrary exact-real attackers. The revised theorem correctly assumes hCLWE hardness directly in M. [Continuous LWE](https://arxiv.org/pdf/2005.09595v2).

`ch-coarse-zero-output`, closed, nonblocking.

`thm-zlip-reductions`

Proven. The new lower width bound repairs the mathematical defect identified in round 04. Unit width supports the lattice-generation argument. The smoothing restriction supports the quoted norm tails. Normalizing by the discrete-Gaussian variance now gives uniformly bounded sub-Gaussian norms.

Proven. Haviv and Regev, SODA 2014, Lemma 5.4, supplies the generation result under its determinant and shortest-basis hypotheses. The integer lattice satisfies those hypotheses at the revised widths. [On the Lattice Isomorphism Problem](https://arxiv.org/pdf/1311.0366).

Proven. The lower reduction’s algebra remains correct. The unknown integral isomorphism transports the sampled coordinates to product discrete Gaussians. Cholesky factorization supplies the orthogonal transformation. Successful reconstruction on a spanning block determines an isomorphism up to signed permutation.

Proven. The upper reduction’s three-block argument also remains mathematically correct. Generation identifies the image lattice. The covariance congruence removes the basis condition number from the rounding error. Fresh records give the required extraction distribution conditional on full rank. The final integral orthogonal transformation is a signed permutation.

Proven. Ducas and van Woerden, EUROCRYPT 2022, Lemmas 2.9 and 3.6, provide the sampling statement and good-basis estimate used in part (a). Definition 3.3 identifies the conditional distribution used in part (b). Lemma 3.4 explicitly gives expected polynomial runtime for its sampling algorithm. These statements do not establish implementation in the newly restricted primitive set of M. [DvW22](https://ir.cwi.nl/pub/31729/31729.pdf).

`ch-zlip-small-width`, closed, nonblocking.

`ch-zlip-model-realization`, blocking.

Proven. With a fixed finite bound on execution steps, M cannot output an exact discrete Gaussian on the integers. Fix the input parameters. Each execution branch uses finitely many arithmetic operations, square roots and comparisons on finitely many Gaussian draws. Its domains and output functions are semialgebraic. An integer-valued output has only finitely many values almost surely on these finitely many branches. A discrete Gaussian has infinite support.

Proven. Consequently, the exact sampling step asserted in part (a) cannot simultaneously have the stated deterministic polynomial overhead in this primitive model. The builder must specify expected runtime, add an appropriate sampling primitive, or truncate a sampler and account for the resulting distributional error. This concerns implementation inside M. Deferring transfer to Turing machines does not resolve it.

Open. The builder has not supplied an expected-runtime implementation in M or a truncation analysis preserving the stated success loss. Until then, the proof does not establish the theorem with its declared computation model and time bound.

`ch-zlip-variance-access`, nonblocking.

Proven. Block 2 also treats the exact discrete-Gaussian variance as available. The listed primitives do not directly supply that value. A certified inverse-polynomial relative approximation suffices after tightening the concentration constants and reserving part of the rounding margin. State that implementation explicitly.

Proven. The seed-known linear-solve conclusion now has the correct hypothesis. The population identifiability statement also has the correct scope.

Proven. Ducas, Designs, Codes and Cryptography 2024, Theorems 1 and 2, proves correctness and termination of his reduction algorithm. His discussion distinguishes provable bounds from heuristic BKZ bounds. The builder correctly attributes the attack account to that paper. It should retain the heuristic qualification wherever it quotes the BKZ estimate. [Duc24](https://ir.cwi.nl/pub/33543/33543.pdf).

`ch-hardness-computation-model`, closed as the earlier hardness-transfer objection.

Proven. Both security implications now assume hardness in the attacker’s model. Neither implication claims that ordinary Turing-machine hardness already excludes M attackers.

Open. Transfer to standard assumptions remains unproved. Finite-precision stability against arbitrary M attackers also remains unproved.

Heuristic. Both mathematical arguments earn their place under CONTEXT.md. The agreement argument and the conditioning-free Gram estimate use structure in the record laws. Their geometry supports retaining these idealized results.

Open. The exact-coordinate ZLIP guarantee has no established experimental precision interpretation. The current round therefore supports an idealized computational result, conditional on the model repair.

## Verdicts

```text
VERDICT thm-coarse-reconstruction-lattice-hard ACCEPT
VERDICT thm-zlip-reductions REVISE
BLOCKING 1
```