# Summary of the council of 2026-10-27

Written by the integrator after the four meditations (Claude Opus 5.5) and the critiques of
fable (claude-fable-5-1) and sol (gpt-6.1-sol). argon's four critiques are pending, deferred by
Halil to 2026-10-28 or later. No object of this council is accepted in the sense of
`CONTEXT.md`, since the council is not a round of a space. Nothing here enters the booklet or
the registers until Halil has read the reading `lib/theory/2026-10-27-council.pdf` and ruled.

## Verdicts

BLOCKING counts: fable 2, 1, 0, 6 and sol 9, 5, 4, 11, in the order of the tables.

### pseudorandomness-for-learner-classes

| Claim | fable | sol |
| --- | --- | --- |
| def-class-pseudorandom-channel | REVISE | REVISE |
| prop-distinguishing-versus-weak-learning | REVISE | REVISE |
| prop-class-pseudorandomness-collapse | REVISE | REVISE |
| thm-bayes-release-loss-matched-price | ACCEPT | REVISE |
| prop-extraction-gap-information-exponent | ACCEPT | REVISE |
| thm-noisy-gradient-query-filter | ACCEPT | ACCEPT |
| prop-equivariant-learner-orbit-prior | ACCEPT | REVISE |

### degree-of-a-channel

| Claim | fable | sol |
| --- | --- | --- |
| def-shadow-learning-game | REVISE | REVISE |
| thm-shadow-price-is-generative-exponent | ACCEPT | ACCEPT |
| prop-overlap-grading-carries-price | ACCEPT | REVISE |
| prop-approximate-degree-price | REVISE | ACCEPT |
| prop-orthogonal-averaging-cancels-one-degree | REVISE | REJECT |
| prop-seed-cannot-index-the-family | REVISE | REVISE |
| prop-targeted-reader-no-learning-price | ACCEPT | ACCEPT |
| conj-degree-energy-estimator-meets-price | none | REVISE |

### trainer-as-filter

| Claim | fable | sol |
| --- | --- | --- |
| def-random-oracle-record-split | REVISE | ACCEPT |
| prop-canary-is-programmed-record | REVISE | REVISE |
| lem-exposure-information-sandwich | REVISE | ACCEPT |
| thm-null-trajectory-filter | ACCEPT | ACCEPT |
| thm-noisy-trainer-two-term-filter | ACCEPT | REVISE |
| prop-hashed-memory-breaks-sq-filter | ACCEPT | ACCEPT |
| prop-output-bounds-do-not-filter | ACCEPT | REVISE |

### oracle-as-random-oracle

| Claim | fable | sol |
| --- | --- | --- |
| prop-programming-preserves-prices | REVISE | REVISE |
| prop-key-free-defence-rule | REVISE | REJECT |
| prop-canary-audit-unbiased-not-sound | REVISE | REVISE |
| thm-short-seed-dichotomy | ACCEPT | REVISE |
| prop-replay-audit-uninstantiable | REVISE | ACCEPT |
| prop-seed-grip-duality | ACCEPT | REVISE |
| prop-rise-decomposition-replace-one | REVISE | REVISE |
| def-known-price | REVISE | REVISE |

Accepted by both critics: `thm-noisy-gradient-query-filter`, `thm-shadow-price-is-generative-exponent`,
`prop-targeted-reader-no-learning-price`, `thm-null-trajectory-filter`,
`prop-hashed-memory-breaks-sq-filter`. Rejected by one: `prop-orthogonal-averaging-cancels-one-degree`
and `prop-key-free-defence-rule`, both by sol.

## Findings that bear on registered results

Each needs Halil's reading and, for a merge, a round or the integrator's re-derivation.

1. `thm-extraction-exponent-price` (item 20 of the reading of 26 October). For square-loss
   population gradient trainers, extraction of a Bayes release costs what training costs
   (`thm-bayes-release-loss-matched-price`). The item-20 gap needs a trainer that reads $y^2$,
   and it is bounded by the information exponent of the label law
   (`prop-extraction-gap-information-exponent`). fable adds that every even link strictly
   monotone on $[0,\infty)$ has generative exponent at most 2, so the degree-4 link is a knife
   edge. The integrator checked the level-set argument: each level set is $\{\pm a(t)\}$ and
   $\mathbb E[h_2(Z)\mid t]=(a(t)^2-1)/\sqrt2$.
2. `lem-sq-learner-post-processing` and `prop-learner-side-sq-transfer` (item 21). Their SGD
   clause holds in the worst-rounding model of AKMSS21 only, where memorization cannot be
   stated (`thm-null-trajectory-filter` (b)). No bound on the trainer's output composes with an
   SQ bound (`prop-output-bounds-do-not-filter`).
3. `thm-blind-orbit-limit`, `thm-blind-orbit-price` and the seed separation (items 12 and 15).
   They are results for SGD, since Adam is equivariant under signed permutations only (meditator
   of degree-of-a-channel, both critics, sol citing Li, Zhang and Arora). A real seed is a short
   key, and for seeds whose representation laws are separated about 400 representations identify
   a 64-bit seed (`thm-short-seed-dichotomy`, recomputed by fable as 397.3). sol notes that seeds
   with identical representation laws, such as a client and its negation, stay unidentified.
4. The sentence of the reading of 27 October that an efficient learner outputs a cheap predictor
   holds for circuits and fails for uniform descriptions (fable).
5. Decision 3 of the definitions reading, the exponent as unit. The price exponent at one degree
   depends on the geometry of the hidden index, $d^{k/2}$ in a Gaussian frame and $d^{k}$ in a
   subset frame (`prop-overlap-grading-carries-price`).

## Where the critics converge

Every critique names one gap. No claim prices a learning attacker, a shadow model or a VAE, in
learning units with both sides in one access model. The one object of the council with that shape
is the Next of pseudorandomness-for-learner-classes: on $Y=\langle u,X\rangle\xi$ a linear SGD
trainer's drift is free of $u$, while the covariance of its batch updates carries $2uu^\top$
(recomputed by fable), with an open recovery threshold near $T\asymp d(1+b\varsigma^2)^2$.

## Rulings asked of Halil

1. Whether assuming that the implementation's seed generator is pseudorandom for the attacker
   composed with one training run counts as the excluded plug-in.
2. Which reading of the programming rule he meant: a value indistinguishable from an honest
   sample, which admits measurement devices and changes no price, or a modification that gives a
   known law, which would admit release noise as a defence.
3. Whether canaries should be honest draws, measuring the average leakage of an honest record, or
   out-of-distribution records, measuring the worst case as differential-privacy audits do.

## Citations by the critics

sol cited papers with theorem numbers and links (Dwork, Kim, Reingold, Rothblum and Yona STOC 2021,
DPLB24, Li, Zhang and Arora ICLR 2021, Shalev-Shwartz, Shamir and Shammah ICML 2017, Abbe and Sandon
NeurIPS 2020, Steinke and Zakynthinou COLT 2020, Devroye and Lugosi 2001, Blackwell 1953). None was
opened by the integrator, so none is a fact of `sink/formalizing/` until a session reads it.
