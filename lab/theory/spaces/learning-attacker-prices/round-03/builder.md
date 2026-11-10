# Round 03 of learning-attacker-prices, builder

Claude Opus 5.5, builder, 2026-10-29.

I concede the blocking challenge and the reading of Halil's sentence. The repair is stronger than a corrected remark. In the Gaussian linear model, re-learning from a trained release is now priced on both sides. Under an average power constraint on the queries and answer noise of nature's variance, every attacker needs at least about $n/\kappa$ answers to come within a factor $1+\kappa$ of the trainer's risk. Least squares on random queries meets that bound within $1+O(d/n)$ (proven, given one Wishart moment recalled from memory). Without the constraint or without the noise, $d$ queries suffice. So the trainer's performance fixes the attacker's accuracy from both sides, and it prices the attacker exactly when the answers carry nature's noise at nature's power. I take the challenger's two proven additions into the conjecture on the linear class, with credit, and add one consequence. The class's mean-square success at a given budget is bounded by a quantity a simulation measures. The value $\kappa_{\mathrm{KL}}$ on $Q_0$ is recomputed with integrands in closed form, and both earlier grids were low.

Notation of rounds 00 to 02 holds.

## Responses to challenges

#### ch-chosen-query-scaling

Conceded. The remark of prop-trainer-accuracy-caps-release-attacker is false in its own setting. Queries $te_j$ make the release noise negligible, and $d$ of them reach $2R_n$ (the challenger's proof, which I checked). The proposition is superseded by thm-release-relearning-price-bracket. Its part (b) records the counterexample. Its part (c) proves the floor under the average power constraint $\mathbb E\sum_j\|x_j\|^2\le Nd$, by AM and HM on the posterior covariance with Jensen's inequality, without the van Trees inequality. Its part (d) shows that least squares meets that floor. The constraint is the scale of the input law, and part (b) shows it cannot be dropped.

#### ch-third-reading

Conceded. The trainer's performance enters an attacker's price in three ways, and the answer to Halil is built on all three.

- A ceiling on the attacker's accuracy for the trainer's target (data processing, part (a) of the new theorem).
- A floor on the attacker's success. For Halil's own example it is registered as thm-reconstruction-from-conditional-mean, whose statement calls it "the floor on attack success in Halil's example", with prop-reconstruction-label-sandwich as its companion. In the release model, part (b) of the new theorem is a second instance, since an exact release lets $d$ queries attain the trainer's risk.
- A floor on the attacker's cost. It fails for reconstruction (conj-reconstruction-at-training-cost, refuted) and for an exact or scalable release (part (b)). It holds, and it is attained, when the answers carry nature's noise at nature's power (parts (c) to (e)).

So the trainer's performance fixes the attacker's accuracy from above and from below, and it fixes the attacker's cost only under the conditions in which answers resemble records. I also concede that the old part (c) described nature, not a release, since a fresh draw of $Y$ given $X$ needs $u$. It is dropped.

#### ch-b-in-order-versus-exact

Repaired. Part (b) of conj-linear-class-reads-cauchy-transform now states the challenger's reduction in mean-square overlap, which is proven, and conjectures only the delocalization of bulk eigenvectors.

#### ch-quadrature-is-not-a-proof

Repaired, with a correction. I rewrote both densities in closed form. On the atom of $Q_0$ the likelihood ratio is
$$q(x)=\frac{\bar\Phi((1-cx)/\tau)+\bar\Phi((1+cx)/\tau)}{1-p},\qquad c=\frac{w_0}{\sigma},\ \tau=\frac{\varsigma}{\sigma},\ c^2+\tau^2=1,$$
with $\bar\Phi$ the Gaussian upper tail. Off the atom, $\nu_a$ is the two-point Gaussian mixture of part (d) of thm-update-direction-chi-square-bound. Adaptive Gauss and Kronrod quadrature of these closed-form integrands gives $\mathrm{KL}=0.248296$ on the atom and $0.081324$ off it, with estimated absolute errors below $10^{-12}$, and $\kappa_{\mathrm{KL}}=0.160111$ (numerical). Both earlier grids were low, mine at 0.1596 and the challenger's at 0.1599, because the grid in $z$ for the atom's mixture was coarse. I state the value $\kappa_{\mathrm{KL}}\le0.1602$. The lower sides become $T\ge46.25$ at $d=200$ and $T\ge98.27$ at $d=400$, and the ratios 86.5 and 81.4. Its status is a numerical value with an error estimate, and the lower side is proven given that value. That is weaker than a proof, and the object says so.

#### ch-declaration-order

Answered. The weight of half-width $0.05$ was fixed in round 01, from the challenger's estimator and 4 exploratory seeds at $T\in\{10d,20d,40d\}$. The point $T=20d$ was declared before the 40 certified runs of round 02, which used the fresh seed 20261029. The descriptive counts at $10d$ and $15d$ came from the same execution and do not enter the band. Exploratory runs informed the choice of the declared point, and they are independent of the certified runs, so the band is sound. The challenger's replication with another seed certifies it independently.

#### ch-no-trainer-price

Answered for the Gaussian linear model by thm-release-relearning-price-bracket. The attacker re-learns from answers of a trained release, both sides are proven, and the witness is a learner of the trainer's own class, least squares. The statement for a nonlinear architecture trained by SGD on the answers stays open.

#### ch-vacuous-at-measured-dimension

Open for the linear class, with a path. By the challenger's reduction, the mean-square success of every function of $\hat M$ at a budget $T$ is at most $\mathbb E[\max_k\langle e_k,u\rangle^2]$, which a simulation measures because $u$ is known there (part (b) of the conjecture, proven). That certifies failure at each simulated budget. A price needs failure at every smaller budget, and since the class's success is not monotone in $T$, a grid of budgets does not cover the gaps between them.

## Objects

Each step labelled proven is complete as far as I can tell. The status stays sketch until a verdict.

### thm-release-relearning-price-bracket: re-learning a trained linear release costs the trainer's records exactly when its answers carry nature's noise at nature's power

status: sketch

uses: def-statistic-learner-class, thm-bayes-release-loss-matched-price, thm-reconstruction-from-conditional-mean

Setting. Records $(X_i,Y_i)$, $i\le n$, with $X_i\sim\gamma_d$, $Y_i=\langle u,X_i\rangle+sN_i$, $N_i\sim N(0,1)$, a prior $u\sim N(0,\tau^2I_d)$, and $n\ge d+2$. The trainer outputs the posterior mean $\hat u=(X^\top X+(s^2/\tau^2)I_d)^{-1}X^\top Y$, with posterior covariance $\Sigma_{\mathrm{post}}=(X^\top X/s^2+I_d/\tau^2)^{-1}$ and Bayes risk $R_n=\mathbb E\,\mathrm{tr}\,\Sigma_{\mathrm{post}}$. The release answers a query $x$ with $\langle\hat u,x\rangle+s_rN'$, with fresh $N'\sim N(0,1)$ and $s_r\ge0$. An attacker makes $N$ queries, each a function of the earlier answers and of coins independent of everything else, and outputs $\tilde u$. Put $\iota_m=\mathbb E\,\mathrm{tr}\big((G^\top G)^{-1}\big)$ for $G$ an $m\times d$ matrix of independent standard Gaussians, which is finite for $m\ge d+2$ and equals $d/(m-d-1)$ (the mean of the inverse Wishart law, from memory, unverified).

Statement.

- (a) Ceiling. Every attacker has $\mathbb E\|\tilde u-u\|^2\ge R_n$, and $ds^2\tau^2/(n\tau^2+s^2)\le R_n\le s^2\iota_n$.
- (b) No floor without noise or without a power bound. If $s_r=0$, $d$ queries in general position give $\tilde u=\hat u$ and attain $R_n$. If $s_r>0$ and the queries are unbounded, the queries $te_1,\dots,te_d$ give $\mathbb E\|\tilde u-\hat u\|^2=ds_r^2/t^2$, so $d$ queries reach $(1+\kappa)R_n$ once $t^2\ge ds_r^2/(\kappa R_n)$.
- (c) Floor under an average power constraint. Let $s_r>0$ and $\mathbb E\sum_{j\le N}\|x_j\|^2\le Nd$. Then $\mathbb E\|\tilde u-u\|^2=R_n+\mathbb E\|\tilde u-\hat u\|^2$, and
$$\mathbb E\|\tilde u-\hat u\|^2\ge\frac d{1/\tau^2+s^2\iota_n/(d\tau^4)+N/s_r^2}.$$
So an attacker with $\mathbb E\|\tilde u-u\|^2\le(1+\kappa)R_n$ needs
$$N\ge s_r^2\Big(\frac d{\kappa s^2\iota_n}-\frac1{\tau^2}-\frac{s^2\iota_n}{d\tau^4}\Big).$$
- (d) Least squares meets it. The attacker that queries $N\ge d+2$ inputs $x_j\sim\gamma_d$, which satisfy the power constraint with equality, and outputs least squares on the answers has $\mathbb E\|\tilde u-u\|^2=R_n+s_r^2\iota_N$. It reaches $(1+\kappa)R_n$ once $s_r^2\iota_N\le\kappa ds^2/(n+s^2/\tau^2)$.
- (e) The bracket. With $\iota_m=d/(m-d-1)$ and $s_r=s$, the least $N$ that reaches $(1+\kappa)R_n$ satisfies
$$\frac{n-d-1}\kappa-\frac{s^2}{\tau^2}-\frac{s^4}{\tau^4(n-d-1)}\le N\le d+1+\frac{n+s^2/\tau^2}\kappa,$$
so the re-learning price is $n/\kappa$ within a factor $1+O(d/n+s^2/(n\tau^2))$.

Proof.

Step 1, part (a) (proven). The answers are a function of the records, the queries, the release noise and the attacker's coins. So $\tilde u$ is an estimator from the records and independent randomness, and its risk is at least the Bayes risk $R_n$. The map $S\mapsto\mathrm{tr}(S^{-1})$ is convex on positive definite matrices and $\mathbb EX^\top X=nI_d$, so Jensen's inequality gives $R_n\ge d/(n/s^2+1/\tau^2)$. Since $\Sigma_{\mathrm{post}}\preceq s^2(X^\top X)^{-1}$, $R_n\le s^2\iota_n$.

Step 2, part (b) (proven). With $s_r=0$, $d$ answers in general position form a linear system with the unique solution $\hat u$. With queries $te_j$, the coordinate estimate (answer$)/t$ has error $s_rN'_j/t$.

Step 3, the decomposition (proven). Given the records, $u-\hat u$ has mean zero, and the release noise and the attacker's coins are independent of $u$. So $\mathbb E\langle\tilde u-\hat u,u-\hat u\rangle=0$, which gives $\mathbb E\|\tilde u-u\|^2=R_n+\mathbb E\|\tilde u-\hat u\|^2$.

Step 4, part (c) (proven). Give the attacker the trainer's design $X$ as well, which can only lower its risk for $\hat u$. Given $X$, $\hat u$ is linear in the Gaussian pair $(u,N)$, so $\hat u\sim N(0,S_X)$ with $S_X=\tau^2I_d-\Sigma_{\mathrm{post}}$ by the law of total covariance. With $A=X^\top X/s^2$, $S_X=\tau^2(A+I_d/\tau^2)^{-1}A$, so $S_X^{-1}=I_d/\tau^2+s^2(X^\top X)^{-1}/\tau^4$. Each answer is $\langle\hat u,x_j\rangle$ plus independent Gaussian noise, and each $x_j$ is a function of earlier answers and independent coins. So the conditional law of $\hat u$ given $X$, the answers and the coins is Gaussian, with covariance $(S_X^{-1}+\sum_jx_jx_j^\top/s_r^2)^{-1}$, adaptivity included. The best estimator's risk is the mean of its trace. For a positive definite $M$, AM and HM on its eigenvalues give $\mathrm{tr}(M^{-1})\ge d^2/\mathrm{tr}(M)$, and here $\mathrm{tr}(M)=\mathrm{tr}(S_X^{-1})+\sum_j\|x_j\|^2/s_r^2$. The map $y\mapsto d^2/y$ is convex on $(0,\infty)$, so Jensen's inequality over $X$ and the queries gives
$$\mathbb E\|\tilde u-\hat u\|^2\ge\frac{d^2}{d/\tau^2+s^2\iota_n/\tau^4+Nd/s_r^2},$$
which is the display of (c). If $\mathbb E\|\tilde u-u\|^2\le(1+\kappa)R_n$, Step 3 gives $\mathbb E\|\tilde u-\hat u\|^2\le\kappa R_n\le\kappa s^2\iota_n$, and solving for $N$ gives the bound on $N$.

Step 5, part (d) (proven). Least squares gives $\tilde u-\hat u=(X'^\top X')^{-1}X'^\top s_rN'$, with $X'$ the query matrix, independent of $\hat u$. So $\mathbb E\|\tilde u-\hat u\|^2=s_r^2\iota_N$, and Step 3 adds $R_n$. The condition follows from $R_n\ge ds^2/(n+s^2/\tau^2)$ of (a).

Step 6, part (e) (proven, given $\iota_m=d/(m-d-1)$). Substitute in (c) and (d) with $s_r=s$. In (c), $d/\iota_n=n-d-1$. In (d), $s^2d/(N-d-1)\le\kappa ds^2/(n+s^2/\tau^2)$ holds once $N-d-1\ge(n+s^2/\tau^2)/\kappa$. $\square$

Halil's sentence. The least-squares attacker is a learner of the trainer's own class, a linear model in square loss trained to its optimum on the answers. Part (e) shows that this learner pays the trainer's records, divided by the slack $\kappa$ it accepts, and that no attacker of bounded power pays less. That is the floor "which is the performance of initial model" in the sense of cost. Parts (a) and (b) show that the same performance caps the attacker's accuracy and, for an exact release, is attained by it. With thm-reconstruction-from-conditional-mean for his reconstruction example, the trainer's performance fixes the attacker's accuracy from both sides. It fixes the attacker's cost only when the release answers like nature, with nature's noise at inputs no larger than nature's.

Other regime and the oracle. Parts (a), (c) and the lower half of (e) bind every attacker, unbounded ones included, so they are statistical. Part (d) is a polynomial-time learner. The statement is about a linear Gaussian model and needs no oracle. For a nonlinear architecture the oracle would supply the trained release and the learner's runs, and the analogue of (c) is open.

### conj-linear-class-reads-cauchy-transform: the linear attacker reads a Cauchy transform of the label law, the full observer its L2 norm

status: open

uses: def-optimum-update-stream, def-statistic-learner-class, prop-signed-weight-update-pca, prop-update-direction-fano-recovery

Setting, exact part, part (c), limits, grounds and experiment as accepted in round 02. Three changes follow.

Scope (the challenger's note). With $\varsigma=0$ and an atom of $W$ at zero, the lower edge exists only for $\gamma<\Pr[W>0]$.

At most one outlier on each side (proven, given the two deterministic equivalents, the challenger's computation). On $(g_-,0)\cup(0,g_+)$,
$$\frac\gamma{g^2}+\Psi'(g)=\Big(\frac\gamma{g^2}-\mathbb E\Big[\frac{\sigma^4}{(1-\sigma^2g)^2}\Big]\Big)+\mathbb E\Big[\frac{(\sigma^2+W^2T(W))\sigma^2}{(1-\sigma^2g)^2}\Big]>0,$$
since the bracket is positive inside the edges and $\sigma^2+W^2T(W)=\mathbb E[a^2\mid W]\ge0$. So $\gamma/g-\Psi(g)$ is strictly decreasing on each side, from $+\infty$ at $0^+$ and to $-\infty$ at $0^-$. Part (a) becomes a closed test at the edges. There is an outlier above the bulk exactly when $g_+\Psi(g_+)>\gamma$, and below it exactly when $g_-\Psi(g_-)>\gamma$.

Part (b), restated in mean-square overlap.

- (b1) Proven (the challenger's reduction). Let $u$ be uniform, let $F$ map $\hat M$ and independent coins to $S^{d-1}$, and let $e_k$ be an eigenbasis of $\hat M$, with simple spectrum almost surely. Then
$$\mathbb E\langle F,u\rangle^2\le\mathbb E\Big[\max_k\mathbb E[\langle e_k,u\rangle^2\mid\hat M]\Big]\le\mathbb E\Big[\max_k\langle e_k,u\rangle^2\Big],$$
and the first bound is attained by the eigenvector of largest conditional overlap. Proof. The challenger's averaging $\bar F=R^\top F(R\hat MR^\top)$, with $R$ Haar, keeps $\mathbb E\langle F,u\rangle^2$. The reflections $J$ in eigenvectors of $\hat M$ commute with $\hat M$, so the coefficients of $\bar F$ in the eigenbasis are conditionally uncorrelated. $\bar F$ is conditionally independent of $u$ given $\hat M$, so $\mathbb E[\langle\bar F,u\rangle^2\mid\hat M]=\sum_kp_k\,\mathbb E[\langle e_k,u\rangle^2\mid\hat M]$ with $p_k\ge0$ and $\sum_kp_k=1$. The second bound is that a maximum of conditional means is at most the conditional mean of the maximum. By Markov's inequality, $\Pr[|\langle F,u\rangle|\ge\epsilon]\le\mathbb E[\max_k\langle e_k,u\rangle^2]/\epsilon^2$.
- (b2) Conjecture. Bulk eigenvectors delocalize, so $\mathbb E[\max_k\langle e_k,u\rangle^2]$ tends to the squared outlier overlap of (a), or to zero when (a) has no root. The class's mean-square price is then the least $T/d$ at which (a) gives that overlap.

Consequence for measurement (proven). The right side of (b1) involves no conditional law. A simulation that knows $u$ estimates it with a Hoeffding band, since the variable lies in $[0,1]$. That band certifies the failure of the whole class of $\hat M$ at a given budget, and it is the measured lower side the linear class lacked.

What settles it. As in round 02, with (b) reduced to (b2), bulk delocalization for this scale-mixture family (open).

Other regime and the oracle. Unchanged.

### prop-measured-meets-proven-full-observer: on Q0 the full observer's price is known within 87 at d=200

status: sketch

uses: def-statistic-learner-class, prop-update-direction-fano-recovery, thm-norm-weighted-update-pca, def-optimum-update-stream

Statement. As accepted in round 02, with (a) and (c) replaced and one sentence added to (b).

- (a) $\kappa_{\mathrm{KL}}\le0.1602$, from the value $0.160111$ computed by adaptive quadrature of closed-form integrands with estimated error below $10^{-12}$ (numerical). Every estimator then needs $T\ge(d/24-\frac43\log2)/0.1602$, that is $T\ge46.25$ at $d=200$ and $T\ge98.27$ at $d=400$ (proven, given the value).
- (b), added sentence. The weight was fixed in round 01 and the point $T=20d$ before the 40 certified runs, which used a fresh seed. Exploratory and descriptive runs do not enter the band.
- (c) The price of the full observer is known within $4000/46.25=86.5$ at $d=200$ and within $8000/98.27=81.4$ at $d=400$.

Proof. As in round 02, with the closed-form likelihood ratio of the response to ch-quadrature-is-not-a-proof on the atom. The constant $\frac43\log2=0.9242$ is $\log2$ plus $p\cdot\frac12\log2$ at $p=\frac23$. $\square$

Other regime and the oracle. Unchanged.

### def-statistic-learner-class: a learning attacker, the statistic it reads, and the price of its class

status: open

uses: def-uniform-security-profile, prop-profile-run-coordinate, def-optimum-update-stream

Statement. As accepted in round 02, with one sentence added after the remark on monotonicity. "The class $\mathcal A_S$ reads the statistic of all $n$ observations. Its closure under subsampling, $\mathcal A_S^{\downarrow}$, reads the statistic of a subset chosen by coins independent of the observations, and $p_{S^{\downarrow}}$ is the left end of an interval, since a member at budget $n$ is a member at every larger budget. Prices in this space are those of $\mathcal A_S$ unless $\mathcal A_S^{\downarrow}$ is named."

Other regime and the oracle. Unchanged.
