---
model: gpt-6.1-sol
discussant: sol
date: 2026-10-26
prompt: lab/theory/spaces/computational-limits/round-06/prompt-sol.md
---

Proven. The variance input closes `ch-zlip-variance-access` for part (b). The repair does not yet close `ch-zlip-model-realization`. The algebraic reductions retain their round 05 justification, but the expected runtime requires further argument.

`ch-zlip-model-realization`, blocking, remains open.

Proven. Gaussian signs generate independent fair coins. M can simulate a probabilistic Turing machine step by step once its input has a finite encoding. Expected runtime removes the earlier obstruction from infinite output support.

Proven. These facts do not establish the sampler invocation as written. The statement permits arbitrary real widths. A bound on the numerical size of a real does not give it a finite Turing encoding. Integer and rational recovery therefore does not, by itself, supply the sampler’s width input.

Open. The builder needs either an explicit representation hypothesis for the width or a simulation that supplies certified approximations from its M register. The latter must bound the expected precision requested by the exact sampler. This is an implementation obligation within M, independent of transfer to finite precision attackers.

Proven. DvW22 Lemma 2.9 states exact sampling under its Gram–Schmidt width hypothesis. Lemma 3.4 separately bounds the expected number of attempts needed to obtain full rank. Neither statement supplies the missing representation argument for this particular simulation. [DvW22, Sections 2.3 and 3.1](https://ir.cwi.nl/pub/31729/31729.pdf).

Proven. The expected runtime also needs control outside the good event of Lemma 3.6. The current proof invokes the sampler after a bound that holds with high probability. A high probability runtime bound does not imply an expected runtime bound. Costs on the exceptional event can dominate the expectation.

Proven. This part has a direct repair. Compute the Gram–Schmidt lengths and abort when they exceed the threshold used in the proof. The existing exceptional probability can cover that abort. The sampler then runs only where its width hypothesis holds.

Proven. The coordinate size claims also require qualification. Discrete Gaussian records have unbounded support. Consequently, the asserted determinant bound is a bound on the earlier norm event, not an unconditional bound. Exact rational recovery needs both denominator control and control of the integer part. A denominator bound alone does not bound the number of comparisons needed to locate an arbitrarily large rational.

Open. To finish this challenge, state explicit abort rules or prove expected bounds for the encoding lengths used by rational recovery, Hermite normal form and Extract. The current sentence that expected times add is valid only after these component bounds exist.

`ch-zlip-variance-access`, closed, nonblocking for part (b).

Proven. Giving the exact discrete Gaussian variance as an M input makes the covariance normalization executable using the listed arithmetic primitives. The accepted concentration and rounding argument then applies without a variance approximation.

Proven. The proposed substitute is unnecessary under that hypothesis. Its displayed sufficient condition is an additional restriction. The builder has not derived that condition from the theorem’s existing width restriction.

`ch-zlip-public-parameters`, nonblocking clarification.

Open. The statement should specify whether the variance input belongs only to part (b). If the attacker in part (a) also receives it, the reduction must supply it. Declaring the law known does not establish exact computation of its variance in M. Restricting the supplied variance to part (b), or giving identical public parameters to the source problem, resolves this ambiguity.

Proven. The retained Cholesky identity, equivariant coupling, lattice generation argument, covariance congruence and signed permutation conclusion require no algebraic change. The unresolved issue is whether the declared procedures attain the stated expected overhead under the declared inputs.

## Verdicts

```text
VERDICT thm-zlip-reductions REVISE
BLOCKING 1
```