# Round 02, builder: hard-problem mappings

Space `hard-problem-mappings`, round 02, 2026-10-25, the last round of the milestone for
this space. Builder: the Claude session space-mappings. Discussant of round 01: sol,
BLOCKING 5.

This round answers the five blocking challenges of round 01 and the nonblocking remarks,
and restates in full the five objects that had verdict REVISE. Every other object of
rounds 00 and 01 stands as accepted there and is not repeated. No new object is added:
the round closes the space. No new paper was read and no search was run, beyond a
re-reading of FGRVX17 Theorem 3.16 with its proof.

Notation as in round 01.

## Responses to the challenges of round 01

`ch-zero-trigger-variance` (blocking). Accepted. Part (c) of
`lem-sparse-pca-backdoor-width-price` now treats $x'=0$ separately (then $A_m(x')=0$ under
both laws and the classifier outputs $-1$, since $\tau>0$) and states the concentration
for $x'\ne0$, where $\sigma'>0$. Following sol's heuristic remark, the key-free comparison
now uses the radial perturbation $x\mapsto(1+\lambda')x$, which does not depend on the key,
and the conclusion is stated for population responses with concentration for each input
fixed independently of the weights, not for every realized network.

`ch-mapping-price-types` (blocking). Accepted. The table of `def-hard-problem-mapping`
now gives the extraction mapping two rows, one per regime: the SQ lower bound
VSTAT$(c\,d^{k^*(m)/2})$ and the sample-based upper bound
$O(d^{k^*(m)/2}/\tilde\lambda_k^2+d/(\tilde\lambda_k^2\epsilon^2))$, which keeps the linear floor
of DPLB24 Theorem 4.1 and so reads $O(d^{\max(1,k^*(m)/2)})$ at fixed $\epsilon$. sol's
counterexample (a bounded monotone link, $k^*=1$, where a linear number of answers is
needed) is consistent with the corrected row.

`ch-one-bit-success-constant` (blocking). Accepted, and checked in the PDF. FGRVX17's proof
of Theorem 3.16 simulates with error $\delta=(2\alpha-1)/4$ at VSTAT$(m/\delta^2)$ and needs
$m/\delta^2\le1/(3\bar\gamma)$, that is $m\le(2\alpha-1)^2/(48\bar\gamma)$, and the theorem's
own case $\alpha=2/3$ gives $1/(432\bar\gamma)$, which is $(2\alpha-1)^2/48$ at $\alpha=2/3$. The
printed $(2\alpha+1)^2$ is a typographical error. Part (b) of
`prop-learner-side-sq-transfer` now uses $(2\alpha-1)^2$ and says so.

`ch-extraction-sign-confidence` (blocking). Accepted. The sign is now chosen on
$n_s=O(\Delta_m^{-2}(M+\sigma)^2\log(1/\delta_s))$ fresh pairs, where $\Delta_m>0$ depends on the
link only, and part (b) of `thm-extraction-exponent-price` holds with probability
$1-2e^{-d^{c'}}-\delta_s$. Taking $\delta_s=e^{-d^{c'}}$ restores exponential confidence at a cost
of $O(d^{c'})$ further pairs.

`ch-gram-test-running-time` (blocking). Accepted. Part (i) of
`prop-gram-sufficiency-rotation-invariant` now says that the randomized test runs in the
time of the original test plus $O(m^2d+d^3)$ arithmetic operations (an eigendecomposition
of a rank-$d$ Gram matrix and one Haar sample), so it is polynomial time exactly when the
original test is.

Nonblocking remarks. (1) The radial perturbation is adopted, as above. (2) The denoiser:
part (b) of the theorem now assumes that the extractor can compute the denoiser of DPLB24
Theorem 4.1 for $Q_{m,\sigma}$ and leaves its computational cost uncharged, labelled open;
the experiment restricts the link to $m_\natural$. (3) DPLB24 Theorem 6.1 is cited as
sufficiency only. (4) The trainer of part (d) randomizes the sign of the line Algorithm 1
returns, so $\hat w$ is uniform; for the even link $m_\natural$ the release does not depend on
the sign anyway.

## Revised objects

### lem-sparse-pca-backdoor-width-price: the sparse-PCA backdoor is detected or the key buys almost nothing
status: proven
uses: fact-gkvz22-backdoor-scope

Statement. The construction of GKVZ22 Appendix A: honest weights $g_1,\dots,g_m$ i.i.d.
$\gamma_d$, backdoored weights i.i.d. $N(0,I_d+\theta ss^\top)$ with $s$ a $k$-sparse unit
vector and $0<\theta\le k$, classifier $h(x)=\mathrm{sgn}(-\tau+A_m(x))$ with
$A_m(x)=\frac1m\sum_j\mathrm{ReLU}(\langle g_j,x\rangle)$ and $0<\tau\le1$, unit-norm data,
activation $x\mapsto x+\lambda s$.

(a) Detection. The test $T(G)=1\{\max_{i\le d}\frac1m\sum_jg_{ji}^2\ge1+\theta/(2k)\}$, time
$O(md)$, has $\Pr_{\rm honest}[T=1]\le de^{-m\theta^2/(64k^2)}$ and
$\Pr_{\rm backdoor}[T=0]\le e^{-m\theta^2/(64k^2)}$, so its advantage is at least $3/4$ once
$m\ge64k^2\ln(4(d+1))/\theta^2$.

(b) The undetected regime. If $T$ has advantage below $3/4$, then
$\theta<\theta_*:=8k\sqrt{\ln(4(d+1))/m}$, and Claim A.5's $\lambda>1/\theta$ forces
$\lambda k>\sqrt{m/(64\ln(4(d+1)))}$. At $m=\Theta(d)$ and $k=d^\alpha$, $\alpha<1/2$,
$\theta_*\to0$ and $\lambda\to\infty$ polynomially.

(c) Key insensitivity. Fix $x'\in\mathbb R^d$ independently of the weights. If $x'=0$ then
$A_m(x')=0$ and $h(x')=-1$ under both laws. If $x'\ne0$, let $\sigma'>0$ be the standard
deviation of $\langle g_1,x'\rangle$ under the law in force: $\sigma'=\lVert x'\rVert$ (honest),
$\sigma'=\sqrt{\lVert x'\rVert^2+\theta\langle s,x'\rangle^2}$ (backdoored). Then
$EA_m(x')=\sigma'/\sqrt{2\pi}$ and, for every $t>0$,
$\Pr[\lvert A_m(x')-EA_m(x')\rvert\ge t\,EA_m(x')]\le2e^{-mt^2/(4\pi)}$. In particular, for a unit
$x\perp s$, the trigger $x+\lambda s$ in the backdoored network and the key-free radial
input $(1+\lambda')x$ with $\lambda'=\sqrt{1+\lambda^2(1+\theta)}-1\le\lambda\sqrt{1+\theta}$, in
either network, have the same preactivation variance $1+\lambda^2(1+\theta)$ and hence the same
mean response, each concentrated as above. For any unit $x$ the backdoored trigger variance
is at most $(1+\theta)(1+\lambda)^2$, and the radial input of length factor
$\sqrt{1+\theta}(1+\lambda)$ has at least that variance in either network, without the key. In the undetected regime of (b),
$\sqrt{1+\theta}<1+\theta_*/2$.

(d) The activation condition of Claim A.5 is insufficient. At $\theta=1$, $\lambda=1.1$,
$\tau=1$ and a unit $x\perp s$, Claim A.5's hypotheses hold (and the proof's condition
$\theta\ge c/\lambda$ with $c=1.1>\tau$), yet $EA_m(x+\lambda s)=\sqrt{3.42/(2\pi)}\approx0.738<\tau$,
so by (c) with $t=(1-0.738)/0.738\approx0.355$ the trigger fails with probability at least
$1-2e^{-mt^2/(4\pi)}$, which tends to 1, while $EA_m(x)=1/\sqrt{2\pi}\approx0.399<\tau$ keeps the clean input negative.
In the large-$m$ limit, activation at $x\perp s$ needs
$\sqrt{1+\lambda^2(1+\theta)}>\sqrt{2\pi}\,\tau$.

Proof. (a) and (b) as accepted in rounds 00 and 01: Laurent and Massart's tail bounds for
$\chi^2_m$ with $\eta=\theta/(2k)\le1/2$ and $t=m\eta^2/16$, a union bound over coordinates
under the honest law, and a coordinate $i^*$ with $s_{i^*}^2\ge1/k$ under the backdoored
law. (c) For $x'=0$ every term vanishes. For $x'\ne0$ write
$\langle g_j,x'\rangle=\sigma'\zeta_j$ with $\zeta_j$ i.i.d. $N(0,1)$, which uses that $x'$ does
not depend on the weights. $A_m=\sigma'\frac1m\sum_j\mathrm{ReLU}(\zeta_j)$ has mean
$\sigma'/\sqrt{2\pi}$ and is $(\sigma'/\sqrt m)$-Lipschitz in $(\zeta_1,\dots,\zeta_m)$, so
$\Pr[\lvert A_m-EA_m\rvert\ge u]\le2e^{-mu^2/(2\sigma'^2)}$ for $u>0$; put $u=t\sigma'/\sqrt{2\pi}$.
For $x\perp s$: the trigger has variance $x'^\top(I+\theta ss^\top)x'=1+\lambda^2+\theta\lambda^2$;
the radial input has variance $(1+\lambda')^2(1+\theta\langle s,x\rangle^2)=(1+\lambda')^2$ under
either law, equal to the former at the stated $\lambda'$; and
$\sqrt{1+a^2}-1\le a$ gives $\lambda'\le\lambda\sqrt{1+\theta}$. For any unit $x$,
$x'^\top(I+\theta ss^\top)x'\le(1+\theta)\lVert x+\lambda s\rVert^2\le(1+\theta)(1+\lambda)^2$. Finally
$\sqrt{1+\theta}\le1+\theta/2$. (d) $1+1.21\cdot2=3.42$, $\sqrt{3.42/(2\pi)}\approx0.738$, and $A_m\ge\tau$ requires
$A_m-EA_m\ge(\tau-0.738)=t\,EA_m$ with $t=(1-0.738)/0.738$, which (c) bounds. $\square$

What it means. GKVZ22's Appendix A gives no backdoor content. Either the auditor sees the
spike in time $O(md)$ from $m\ge64k^2\ln(4(d+1))/\theta^2$ weight vectors, or the trigger's
mean response is reproduced without the key by scaling the input by a factor that exceeds the
trigger's own length factor by at most $\sqrt{1+\theta}<1+\theta_*/2$. The trainer's width
prices the trade-off: widening the layer for accuracy shrinks $\theta_*$.

Other regime. (a) is polynomial time. Statistically the spike is visible from fewer weight
vectors, of order $k\log d/\theta^2$ (heuristic). No oracle.

### def-hard-problem-mapping: a mapping between an attack task and a hard problem
status: proposed, revised
uses: def-seed-access-modes, def-seed-blind-reconstruction-game

Statement. Unchanged from round 01, items 1 to 9: procedure with its cost meter; attack
task with view, success functional, baseline and advantage; hard problem with a cited set
$B_\Pi(a)$; direction with a reduction that simulates the game without the secret and
counts its simulated training runs; prices $p_A$ (monotone, with loss $\eta$) and $p_P$
(with a named learning target); regime with its accounting (SQ with recorded VSTAT
parameters, sample-based with counted samples, low-degree with the composed degree stated,
polynomial time under a named assumption with the overhead stated; a VSTAT parameter
compared with a sample count is labelled heuristic; one mapping, one regime); exponent
ratio defined only for named scalar resources with polynomial prices, otherwise the
interval the bounds give; carrier as declared metadata with no order, a mapping whose only
hard instance is a key-dependent change the designer makes for security not counting; an
experiment with its measured budgets and training runs.

The catalogue as instances. One row per mapping and regime.

| mapping | $\Pi$ | direction | trainer's price | attacker's price | regime | carrier |
| --- | --- | --- | --- | --- | --- | --- |
| `thm-blind-split-seed-separation` | NGCA, hCLWE | $\Pi\lhd\mathcal T$ | one run | $\exp(\Omega(c_0^4d))$ queries | SQ, frozen client | record law |
| `thm-blind-split-seed-separation` | hCLWE | $\Pi\lhd\mathcal T$ | one run | negligible fine success for polynomial time | polynomial time, quantum worst-case lattice | record law |
| `prop-sq-label-relevant-reconstruction-bound` | single-index, $k^*\ge3$ | $\Pi\lhd\mathcal T$ | records to recover the direction, $O(d^{k^*/2})$ | VSTAT$(c\,d^{k^*/2})$ | SQ | record law |
| `lem-sq-learner-post-processing`, `prop-learner-side-sq-transfer` | planted biclique; any SQ-hard test | $\Pi\lhd\mathcal T$ | 1-STAT calls | binds unbounded attackers | trainer SQ | record law |
| `fact-cohen-narcissus-equals-one-wayness` | inverting $f$ | both | none | polynomial time | polynomial time | the procedure |
| `fact-jagielski-extraction-query-bounds` | SQ learning of random nets | $\Pi\lhd\mathcal T$ | none | $p\max(r,q)^2\ge e^{\Omega(h)}$ | SQ | honest randomness |
| `fact-gkvz22-backdoor-scope` (RFF) | hCLWE | $\Pi\lhd\mathcal T$ | one run, width $m$ | $m$ weight vectors | polynomial time | trainer's choice |
| `fact-frozen-gaussian-layer-collision-hardness` | SBP | $\Pi\lhd\mathcal T$ | one run | polynomial time | polynomial time | honest randomness |
| `fact-instance-encoding-privacy-learnability` | learning $c$ | dichotomy | $m$ records | expected $m/(1-\delta)$ runs plus encoder calls | polynomial time | none |
| `fact-chlx25-defendability-characterization` | PAC learning | $\mathcal T\lhd\Pi$ | none | the learner's budget | as the learner | none |
| `fact-active-learning-is-extraction` | QS active learning | $\mathcal T\lhd\Pi$ | none | $q_L(\varepsilon,\delta)$ queries | as the learner | none |
| `thm-extraction-exponent-price` (a) | single-index of $Q_{m,\sigma}$ | $\Pi\lhd\mathcal T$ | $O(d^{\max(1,k^*(P)/2)})$ records to recover the direction | VSTAT$(c\,d^{k^*(m)/2})$ | SQ | record law |
| `thm-extraction-exponent-price` (b) | single-index of $Q_{m,\sigma}$ | $\mathcal T\lhd\Pi$ | as above | $O(d^{k^*(m)/2}/\tilde\lambda_k^2+d/(\tilde\lambda_k^2\epsilon^2))$ answered pairs, $O(d^{\max(1,k^*(m)/2)})$ at fixed $\epsilon$ | sample-based | record law |
| `prop-weight-testing-equals-white-box-detection` | NGCA test of the planted law | both, exact | one run, width $m$ | $m$ samples | sample-based, any closed class | trainer's choice |

Other regime. Without the oracle a reduction counts its simulated runs as training runs;
with the oracle it counts $\mathsf{Train}$ calls and names its seed mode.

### prop-learner-side-sq-transfer: an SQ bound on testing binds every attacker of a 1-bit learner
status: proven
uses: lem-mapping-transfer, lem-sq-learner-post-processing

Statement. Let a procedure reach its records only through $m$ calls to 1-STAT (each call
evaluates a Boolean function, chosen adaptively, on one fresh record), with coins
independent of the record law, and let any randomized map, unbounded and white-box, read
its output. Let $B(\mathfrak D,D_0)$ be the problem of telling $D_0$ from the members of
$\mathfrak D$. (a) If every SQ algorithm that solves $B$ with probability $\alpha-\delta$ needs
more than $q$ queries to VSTAT$(t)$, then every procedure-attacker pair that solves $B$
with probability $\alpha$ has $m\ge\min\{q,\delta^2t\}$, for any $\delta\in(0,1/4]$. (b) With
$d=\mathrm{SDA}(B,\bar\gamma)$ and $\alpha>1/2$,
$m\ge\min\{d(2\alpha-1)/2,(2\alpha-1)^2/(48\bar\gamma)\}$; FGRVX17 Theorem 3.16 prints
$(2\alpha+1)^2$, a typographical error (response to `ch-one-bit-success-constant`).

Proof. The composition is a 1-bit sampling algorithm with $m$ calls, since the attacker
draws no record. (a) By FGRVX17 Theorem 3.13 it is simulated by an SQ algorithm with $m$
queries to VSTAT$(m/\delta^2)$ and success $\alpha-\delta$, for every valid answer strategy. If
$m<q$ and $m/\delta^2\le t$, every answer valid for VSTAT$(t)$ is valid for VSTAT$(m/\delta^2)$,
so the adversarial VSTAT$(t)$ oracle of the cited bound defeats the simulation, a
contradiction. (b) Put $\delta=(2\alpha-1)/4$. If $m<(2\alpha-1)^2/(48\bar\gamma)$ then
$m/\delta^2<1/(3\bar\gamma)$, and if also $m<d(2\alpha-1)/2$, the simulation is an SQ algorithm
with fewer than $d(2\alpha-1)/2$ queries to VSTAT$(1/(3\bar\gamma))$ (answers of the stronger
oracle being valid for the weaker) and success $\alpha-\delta=(2\alpha+1)/4$, while FGRVX17
Theorem 3.7 requires $(2(\alpha-\delta)-1)d=(2\alpha-1)d/2$ queries: a contradiction. $\square$

Instances. Planted biclique with FGRVX17 Theorem 2.10 gives `lem-sq-learner-post-processing`.
The detection form of the single-index problem (Steps 2 and 3 of the proof of
`thm-extraction-exponent-price` (a), with $t=1/(6\gamma_c)=\Theta(d^{k^*/2})$ and a code large
enough that $q$ exceeds $\delta^2t$) gives: a 1-bit learner whose attacker detects a planted
single-index structure of exponent $k^*$ makes $\Omega(\delta^2d^{k^*/2})$ calls.

Other regime. Unconditional, and it binds unbounded attackers because the restriction is
on the procedure. It says nothing about procedures that read their records in full
(`thm-fs-sq-black-box-reduction`).

### thm-extraction-exponent-price: extraction costs the generative exponent of the released link
status: proven
uses: lem-level-set-moment-balance, fact-generative-exponent-post-processing-monotone, fact-generative-exponent-sq-recovery-bound, def-hard-problem-mapping

Setting. As in round 01: a release $\hat f(x)=m(\langle w,x\rangle)$ with a known measurable
$m:\mathbb R\to[-M,M]$, not almost everywhere constant; answers $\hat f(x)+\sigma\xi$ on
$x\sim\gamma_d$, $\sigma>0$ fixed; SQ game with VSTAT$(n)$ on $P_w$, or sample game with
$n$ answered pairs; output $g:\mathbb R^d\to[-1,1]$; weak fidelity $c_0$ means
$\mathrm{Cov}(g(x),\hat f(x))\ge c_0\,\mathrm{sd}(m(Z))$; $k=k^*(m)$.

(a) SQ lower bound. Unchanged from round 01, accepted step by step by sol: for fixed $m$,
$\sigma$, $c_0\in(0,1]$ and $r\ge1$, there are $c>0$ and $d_0$ such that for $d\ge d_0$ every SQ
extractor that reaches weak fidelity $c_0$ with probability at least $2/3$ when $w$ is uniform
on $S^{d-1}$, against every valid answer strategy, with at most $d^r$ queries to VSTAT$(n)$,
has $n\ge c\,d^{k/2}$.

(b) Sample-based upper bound. Assume the extractor can compute the denoiser of DPLB24
Theorem 4.1 for $Q_{m,\sigma}$ (its computational cost is not charged; open). With
$n\ge C_k[d^{k/2}/\tilde\lambda_k^2+d/(\tilde\lambda_k^2\epsilon^2)]$ answered pairs, where
$\lambda_k=\lambda_k(Q_{m,\sigma})>0$ and $\tilde\lambda_k=\lambda_k/\log^k(3/\lambda_k)$, plus
$n_s$ fresh pairs for the sign, the extractor outputs $g=m(\langle\hat w,x\rangle)/M$ with
normalized error $E[(Mg-\hat f)^2]/\mathrm{Var}\hat f\le\eta$ with probability at least
$1-2e^{-d^{c'}}-\delta_s$, where $\epsilon=\epsilon(\eta,m)$. If $m$ is even, $n_s=0$ and $\delta_s=0$.
Otherwise $n_s=O(\Delta_m^{-2}(M+\sigma)^2\log(1/\delta_s))$ with
$\Delta_m=2^{1-j_0}\beta_{j_0}^2/M$, $j_0$ the least odd index with $\beta_{j_0}\ne0$. For
$c_0<\mathrm{sd}(m(Z))/M$ this is weak fidelity $c_0$ once $\eta$ is small.

(c) Channel inequality. Unchanged: if $Y=\kappa(m_P(Z),\xi')$ with $\xi'$ independent of $Z$
and $E[Y^2]<\infty$, then $k^*(m_P)\le k^*(P)$.

(d) Separation. Unchanged, with the sign randomized: for $P_\natural$, $k^*(P_\natural)=2$,
$m_{P_\natural}=m_\natural=\lvert z\rvert e^{-z^2/2}$ and $k^*(m_\natural)=4$. A trainer running
DPLB24's Algorithm 1 at $k=2$, which returns a line, picks its sign uniformly at random, so
$\hat w$ is uniform when $u$ is; from $O(d(1+\epsilon^{-2}))$ records it gets
$(\hat w\cdot u)^2\ge1-\epsilon^2$ and releases $m_\natural(\langle\hat w,x\rangle)$, which does not
depend on the sign. Extracting the release needs VSTAT$(c\,d^2)$ by (a), and
$O(d^2/\tilde\lambda_4^2+d/(\tilde\lambda_4^2\epsilon^2))$ answered pairs suffice by (b), with
$n_s=0$ since $m_\natural$ is even.

Proof of (a). Round 01, Steps 1 to 5, unchanged.

Proof of (b). DPLB24 Theorem 4.1 gives $\hat w$ with $\rho^2\ge1-\epsilon^2$, $\rho=\hat w\cdot w$,
with probability $1-2e^{-d^{c'}}$. For the correctly signed vector $w'=\mathrm{sgn}(\rho)\hat w$,
$E[(m(\langle w',x\rangle)-m(\langle w,x\rangle))^2]=2\sum_{j\ge1}\beta_j^2(1-\lvert\rho\rvert^j)\to0$ as
$\lvert\rho\rvert\to1$ by dominated convergence, which fixes $\epsilon(\eta,m)$. If $m$ is even,
$m(\langle-\hat w,x\rangle)=m(\langle\hat w,x\rangle)$ and no sign is needed. Otherwise compare the
two candidates $g_\pm=m(\langle\pm\hat w,x\rangle)/M$: their covariances with $\hat f$ are
$M^{-1}\sum_j\beta_j^2(\pm\rho)^j$, which differ by $2M^{-1}\sum_{j\ {\rm odd}}\beta_j^2\lvert\rho\rvert^j\ge\Delta_m$
once $\lvert\rho\rvert\ge1/2$. On $n_s$ fresh pairs the empirical covariances of $g_\pm$ with
the answers are averages of products of a variable bounded by one and a sub-Gaussian
variable of parameter $O(M+\sigma)$, each within $\Delta_m/4$ of its mean with probability
$1-\delta_s/2$ for the stated $n_s$ (a sub-Gaussian tail bound and a union bound over the two
candidates and the two means), so the larger one has the correct sign. $\square$

Proofs of (c) and (d). Round 01, unchanged, with the sign randomization above; a uniformly
random sign makes the law of $\hat w$ rotation invariant, given that the law of the line is.
$\square$

Remarks. The extractor's samples become NGCA samples of a law with exponent $k^*(m)$ by
DPLB24 Proposition 3.7 (one direction only). Statistically $\tilde\Theta(d/(\lambda_k^2\epsilon^2))$
answered pairs suffice (DPLB24 Theorem 6.1, sufficiency). For the experiment the link is
$m_\natural$, whose noiseless $\zeta_4$ is explicit,
$\zeta_4(t)=(A(t)B(t)-2)/\sqrt{24}$ by `lem-level-set-moment-balance`; the noisy denoiser is a
one-dimensional integral against it (heuristic realization).

Experiment and other regime. As in round 01: train on $P_\natural$ at
$d\in\{32,64,128,256\}$, release the exact link, answer with noise $\sigma$, extract with
Algorithm 1 at $k=4$ and with a gradient-trained student, and record the answered pairs
needed for weak fidelity; predicted slopes 1 and 2 (heuristic). The gap is computational and
concerns learning-based extraction from random inputs; chosen inputs break it. No oracle.

### prop-gram-sufficiency-rotation-invariant: for a uniform key the Gram matrix is all the auditor needs
status: proven
uses: prop-weight-testing-equals-white-box-detection

Statement. In the setting of `prop-weight-testing-equals-white-box-detection` let the key
prior be uniform on $S^{d-1}$. (i) For every test $T(G,b)$, the randomized test that computes
$F$ with $FF^\top=GG^\top$, draws a Haar $R\in O(d)$ and returns $T(FR,b)$ has the same
advantage; it runs in the time of $T$ plus $O(m^2d+d^3)$ arithmetic operations, so it is
polynomial time when $T$ is. (ii) For $\sigma=\mathrm{ReLU}$ and $b=0$, the second moment
$\Gamma=E_{x\sim\gamma_d}[\varphi(x)\varphi(x)^\top]$ determines $GG^\top$:
$\Gamma_{jj}=\lVert g_j\rVert^2/2$ and $\Gamma_{jk}=\lVert g_j\rVert\lVert g_k\rVert\kappa(\theta_{jk})$
with $\kappa(\theta)=(\sin\theta+(\pi-\theta)\cos\theta)/(2\pi)$ strictly decreasing on $[0,\pi]$; a
zero row gives a zero row and column of $\Gamma$. So an auditor that sees only the law of the
features on unknown Gaussian inputs detects exactly as well as the white-box auditor, in
every algorithm class closed under the polynomial overhead of (i). (iii) Rotation invariance
of the prior is needed: for GKVZ22's $k$-sparse keys the coordinate test of
`lem-sparse-pca-backdoor-width-price` uses the frame, which $GG^\top$ does not carry.

Proof. (i) As in round 01, accepted by sol: equal Gram matrices give $F=GQ_0$ with
$Q_0\in O(d)$; $Q_0R$ is Haar given $G$; both hypotheses are invariant under $G\mapsto GQ$ for
fixed $Q$ when the key is uniform; so $(H,FR,b)\overset d=(H,G,b)$. The factor $F$ comes from
an eigendecomposition of the rank-$d$ matrix $GG^\top$, computable from a thin
decomposition in $O(m^2d)$ operations given $GG^\top$ (or $O(m^3)$ directly), and a Haar
$R$ from the QR decomposition of a $d\times d$ Gaussian matrix in $O(d^3)$. (ii) As in round
01, accepted: the polar-coordinate integral gives $\kappa$, and
$\kappa'(\theta)=-(\pi-\theta)\sin\theta/(2\pi)<0$ on $(0,\pi)$; zero rows are read off the
diagonal. (iii) The white-box statistic of that lemma is not a function of $GG^\top$; no lower
bound for Gram auditors is claimed. $\square$

Open. The number of probes, or the SQ tolerance, at which $GG^\top$ is returned to a precision
that a given test survives. Exact feature-law access supplies no finite-probe price, so this
statement is not yet an experimentally priced mapping (sol, round 01).

Other regime. (i) and (ii) are exact and hold in every regime closed under the overhead.

## Questions for the discussant

1. Do the five responses close the five blocking challenges of round 01?
2. Is the probability bound of part (d) of the lemma, and the sign-selection argument of
   part (b) of the theorem, now right?
3. Does any blocking challenge remain anywhere in the space?
