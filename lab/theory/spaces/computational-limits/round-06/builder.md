# Round 06, builder: computational limits, one repair

Space `computational-limits`, round 06, 2026-10-26, a short round the integrator
added to milestone 2 for one object. Builder: the Claude session
space-computational. Discussant of round 05: sol. This round answers
`ch-zlip-model-realization` and `ch-zlip-variance-access` and re-presents
`thm-zlip-reductions` alone. The model stays the exact-arithmetic model $\mathsf M$ of
round 05, read as sol read it: a uniform stochastic algebraic RAM with unit-cost
$+,-,\times,\div$, square roots and comparisons, independent standard Gaussian draws,
and finitely many program constants.

## Responses to round 05

`ch-zlip-model-realization` (blocking). Accepted, with sol's argument: no run of
bounded length, in $\mathsf M$ or on a Turing machine with finitely many coins, outputs
an exact sample of an infinitely supported law. The repair has three parts.

1. Time is counted in expectation. An exact sampler can only run in expected
   polynomial time, so DvW22 Lemma 2.9 is used in that sense, and DvW22 Lemma 3.4
   states expected time itself.
2. $\mathsf M$ runs every probabilistic Turing algorithm with polynomial expected
   overhead. A fair coin is the sign of a Gaussian draw. A real known to be an
   integer of absolute value at most $2^b$ is found by binary search with $b+1$
   comparisons, and a rational with denominator at most $2^b$ by the same search on
   its continued fraction. So the Hermite normal form, Extract, rounding, the
   integrality checks and the sampler of Lemma 2.9 run in $\mathsf M$.
3. The one-dimensional discrete Gaussian primitive proposed in round 05 is not
   needed after 1 and 2. Adding it would give the same bounds.

`ch-zlip-variance-access` (not blocking). Accepted. The record law is known to the
attacker, so $\sigma_s^2=\mathrm{Var}(D_{\mathbb Z,s})$ is part of the server's input. A certified
substitute also works: $s^2/(2\pi)$ has relative error at most $13s^2e^{-\pi s^2}$ (BRST21
Lemma 7.2's Poisson identity on $(1/s)\mathbb Z$), which is below $1/(16s^2d)$ once
$e^{-\pi s^2}\le1/(208s^4d)$.

## Object

### thm-zlip-reductions: blind reconstruction of quantized Gaussian records against ZLIP
status: proven
uses: lem-equivariant-view-coupling, fact-lip-average-case, fact-discrete-gaussian-samples-generate, fact-zlip-best-algorithms

Setting. The model $\mathsf M$, time counted in expectation. Records i.i.d. from
$D_{\mathbb Z^d,s}$ with $\max\{1,\eta_{1/2}(\mathbb Z^d)\}\le s\le\mathrm{poly}(d)$, covariance $\sigma_s^2I$, and
$\sigma_s^2$ given. Exact success: some signed permutation $P$ has $t_i=Px_i$ for every
record. ac-sLIP$^{I}_s$ is DvW22 Definition 3.7 with $Q=I_d$.

(a) Lower bound, any client of $\mathcal P_{O(d)}$ computable in $\mathsf M$, no side data.
For $s_0\ge\max\{1,\eta_{1/2}(\mathbb Z^d)\}$ and $s=s_0\sqrt{d\ln(2d+4)/\pi}$, an attacker of expected
time $T$ with exact success $p$ on $N\ge\lceil2d/C\rceil$ records gives an algorithm for
ac-sLIP$^{I}_{s_0}$ of expected time $T+T_{\rm run}+\mathrm{poly}(d)$ and success $p-O(d2^{-d})$.

(b) Upper bound, a frozen client $z=Wx$ with $W$ of full column rank. With
$\mathrm{poly}(d,\log(1/\delta))$ records and an oracle for ac-sLIP$^{I}_s$ of success $q$, the
server reaches exact success with probability at least $q-2^{-\Omega(d)}-\delta$, at
$\mathrm{poly}(d,\log(1/\delta))$ expected overhead.

So if average-case ZLIP at polynomial widths has no expected-polynomial-time
algorithm in $\mathsf M$, no such seed-blind attacker reconstructs quantized Gaussian
records, while for a frozen injective linear client the seed-known server recovers
each record by one linear solve. The best attacks known are those of
`fact-zlip-best-algorithms`, as Duc24 reports them, the $2^{0.146n}$ figure heuristic.

Proof. The reductions are those of round 05, whose mathematics sol accepted line
by line. Only the time accounting changes. In (a), the sampler of DvW22 Lemma 2.9
for $D_{Q',s}$ runs in expected polynomial time on the integral form $Q'$, through
the simulation of item 2. Cholesky factorization, the protocol run, the attacker
and the solve $U'=T_dC_d^{-1}$ are $\mathsf M$ operations. The checks that $U'$ is
integral and unimodular use the binary search of item 2 on entries bounded by
$2^{\mathrm{poly}(d)}$. In (b), the rational coordinates of the representations have
denominators dividing $\det X_d$, at most $(s\sqrt d)^d$, so they are recovered exactly
by item 2. The Hermite normal form, the rounding of $\hat Q_X$ and Extract are
deterministic integer algorithms, and $\sigma_s^2$ is given. The expected times add,
and every failure probability is that of round 05. $\square$

Other regime. As in round 05: the population law of the frozen linear view
determines the records up to $P$, and the gap is computational.
