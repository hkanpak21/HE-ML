# Round 03 of learning-attacker-prices, challenger

Claude Opus 5.5, challenger, 2026-10-29. Judgement of `round-03/builder.md`, after `round-02/summary.md`.

The four objects stand, and no challenge blocks. I tested part (c) of thm-release-relearning-price-bracket hardest and could not break it. The Gaussian conditional law under an adaptive design, the identity for $S_X^{-1}$, AM and HM on the trace, and Jensen's inequality are each right. The bound sits 5 percent below the Bayes risk of an attacker that is given the trainer's design, in a simulation at $d=10$, $n=60$ and $N=200$ (empirical). The inverse-Wishart moment the proof recalls from memory is right. A four-line proof from the Schur complement removes the recall, so the theorem is proven outright. The builder's constant $\kappa_{\mathrm{KL}}=0.160111$ is right, and my value of round 02 was low. I write SATISFIED yes, with reasons in the last section.

## 1. What I checked

I read the summary of round 02 and the builder's turn. I rederived every step of the release theorem, namely the ceiling and the bounds on $R_n$, the counterexample of (b), the decomposition, the posterior covariance under adaptivity, the closed form of $S_X^{-1}$, the AM and HM bound with Jensen's inequality, the solution for $N$, least squares, and both ends of the bracket in (e). I checked the moment $\iota_m=d/(m-d-1)$ by Monte Carlo and by the proof in section 3.2. I checked the bound of (c) against least squares and against the Bayes attacker that knows the trainer's design. I recomputed the atom's KL on $Q_0$ from the closed-form likelihood ratio by adaptive quadrature. I checked the restated part (b) of the conjecture and the subsampling closure of the definition. I did no web search.

## 2. My open challenges

ch-chosen-query-scaling is resolved. The remark is withdrawn, the counterexample is part (b) of the new theorem, and part (c) proves the floor under the repair I proposed, a power bound at the scale of the input law. The builder proves it without the van Trees inequality I suggested.

ch-third-reading is resolved. The three readings are stated with their statuses, the old part (c) is dropped as a description of nature, and the theorem's paragraph on Halil's sentence uses the three readings correctly.

ch-b-in-order-versus-exact is resolved by (b1) and (b2) of the conjecture.

ch-quadrature-is-not-a-proof is resolved, and I concede a point. With the closed-form likelihood ratio on the atom, adaptive quadrature gives $\mathrm{KL}=0.248296$ in my run as in the builder's. So $\kappa_{\mathrm{KL}}=0.081324+0.317311\cdot0.248296=0.160111$ (empirical, numerical). My round-02 grid in $z$ was coarse, and my 0.1599 was low. The ratio $q$ is right. With $c^2+\tau^2=1$, $(Z,Y)$ is a standard bivariate Gaussian pair with correlation $c$, so $Z\mid Y=y\sim N(cy,\tau^2)$, and $q(y)=\Pr[|Z|>1\mid Y=y]/(1-p)$ (proven). The object labels the value numerical and the lower side proven given it, which is honest.

ch-declaration-order is resolved. The weight was fixed in round 01, the point $T=20d$ before the certified runs, and the certified seed was fresh. Exploratory runs that inform a declaration do not void a band computed from independent runs.

ch-no-trainer-price is resolved for the Gaussian linear model. The nonlinear case is stated as open.

ch-vacuous-at-measured-dimension stays open for the linear class, with an honest status and a path, the measurable upper band of (b1). It does not block.

## 3. Part (c) of the release theorem

### 3.1 The proof, line by line

The decomposition holds when the attacker is given $X$ as well (proven). Given the records, $u-\hat u$ has mean zero, and the attacker's estimate, now a function of $X$, the answers and coins, is still independent of $u$ given the records. So the lower bound on $\mathbb E\|\tilde u-\hat u\|^2$ for attackers that know $X$ is a lower bound for the real attacker.

$S_X=\tau^2I_d-\Sigma_{\mathrm{post}}$ is the law of total covariance with $\Sigma_{\mathrm{post}}$ deterministic given $X$ (proven). Then $S_X=\tau^2(A+I_d/\tau^2)^{-1}A$ and $S_X^{-1}=I_d/\tau^2+A^{-1}/\tau^4=I_d/\tau^2+s^2(X^\top X)^{-1}/\tau^4$ (proven, rederived). The likelihood of the answers given $\hat u$ is a product of Gaussian factors in $\langle\hat u,x_j\rangle$, and the law of each query given the past does not involve $\hat u$. So the posterior of $\hat u$ is Gaussian with precision $S_X^{-1}+\sum_jx_jx_j^\top/s_r^2$, adaptivity included (proven). AM and HM give $\mathrm{tr}(M^{-1})\ge d^2/\mathrm{tr}(M)$. Then $\mathbb E\,\mathrm{tr}(M)=d/\tau^2+s^2\iota_n/\tau^4+\mathbb E\sum_j\|x_j\|^2/s_r^2$, and Jensen's inequality for $y\mapsto d^2/y$ gives the display of (c) (proven). Solving with $\kappa R_n\le\kappa s^2\iota_n$ gives the bound on $N$. Its direction is right, since an upper bound on $R_n$ weakens the requirement.

Numerical check (empirical, 3000 draws, $d=10$, $n=60$, $\tau=s=s_r=1$, $N=200$ Gaussian queries). $R_n=0.1990$. The extra risk is 0.0529 for least squares and 0.0526 for the Bayes attacker given $X$, against the bound 0.0497. So the bound is tight to about 6 percent, and the order of the three numbers is the one the proof predicts.

I tried three counterexamples, and each fails.

- Uneven power. An attacker that puts all its power into $d$ large queries is still bound, since the bound depends on the queries only through $\mathbb E\sum_j\|x_j\|^2$. The cap is per query on average, so $N$ queries carry power at most $Nd$. This is exactly what part (b)'s scaling attack violates.
- Repeated queries. Averaging repeated answers at one input is covered, since the noise is fresh and the precision adds.
- Queries that depend on $X$. They are covered, because the attacker in Step 4 already knows $X$.

### 3.2 The inverse-Wishart moment, proven

Let $G$ be $m\times d$ with independent standard Gaussian entries, $m\ge d+2$, and $W=G^\top G$. Then $(W^{-1})_{11}=1/(W_{11}-W_{12}W_{22}^{-1}W_{21})$. The denominator is $\|(I_m-P)g_1\|^2$, where $g_1$ is the first column of $G$ and $P$ projects onto the span of the other $d-1$ columns. That span has dimension $d-1$ almost surely and is independent of $g_1$, so the denominator is $\chi^2_{m-d+1}$. Since $\mathbb E[1/\chi^2_k]=1/(k-2)$ for $k>2$, $\mathbb E(W^{-1})_{11}=1/(m-d-1)$. By exchangeability of the columns every diagonal entry has this mean, and $\iota_m=d/(m-d-1)$ (proven). Monte Carlo gives 2.506, 0.345 and 0.612 at $(d,m)=(10,15),(10,40),(30,80)$, against 2.500, 0.345 and 0.612 (empirical, 4000 draws). The builder may replace "from memory, unverified" by this proof, and parts (a), (d) and (e) are then proven without recall.

### 3.3 Scope, not challenges to the truth

ch-kappa-in-error-term (does not block). The bracket of (e) has ratio $1+O\big((1+\kappa)(d+s^2/\tau^2)/n\big)$, since the upper end carries an additive $d+1$ that is not divided by $\kappa$. The stated $1+O(d/n+s^2/(n\tau^2))$ holds for $\kappa=O(1)$, and the statement should say so. For $\kappa\ge n/d$ the price is of order $d$, not $n/\kappa$.

ch-price-is-power (does not block). Under the cap, the theorem prices total query power, measured in record equivalents at the scale of the input law. The number of answers equals that price only when the queries have nature's norm. The sentence on Halil should say "answers at nature's power" every time, as it already does once.

ch-release-noise-reading (does not block). The price scales as $s_r^2/s^2$. The theorem prices a given release, so it uses no reading of Halil's ruling 2. Recommending $s_r=s$ to a designer as a way to restore the floor would be the broad reading of the programming rule, release noise as a defence. The object should state that it prices and does not recommend.

The noise model. The release draws fresh noise per answer. A randomized model sampled once, whose noise is fixed per input, is a different release. Then repeated queries do not average, while nearby queries are correlated. The theorem does not cover it, and its title should not suggest otherwise.

## 4. The objects of round 03

### thm-release-relearning-price-bracket

(a) holds. $\Sigma_{\mathrm{post}}\preceq s^2(X^\top X)^{-1}$ gives $R_n\le s^2\iota_n$ (proven). (b) holds (proven, as in round 02). (c) holds (section 3.1). (d) holds. $\tilde u-\hat u=(X'^\top X')^{-1}X'^\top s_rN'$ is independent of $\hat u$, so its mean square is $s_r^2\iota_N$, and the sufficient condition uses $R_n\ge ds^2/(n+s^2/\tau^2)$ (proven). (e) holds. $d/\iota_n=n-d-1$ gives the lower end, and $s^2d/(N-d-1)\le\kappa ds^2/(n+s^2/\tau^2)$ gives the upper end (proven, with section 3.2).

The statement is the first in the space in which a learning attacker is priced in learning units with both sides proven and the trainer's price as the reference. Its mathematics is short and clean. Its novelty is in its use here. The lower bound is the classical A-optimal design argument for a Gaussian linear model (from memory, unverified).

Verdict ACCEPT.

### conj-linear-class-reads-cauchy-transform

The scope note and the closed edge test are taken in correctly, and both are proven at the level of the two deterministic equivalents. (b1) holds (proven). The added second inequality, a maximum of conditional means at most the conditional mean of the maximum, is right, and Markov's inequality carries the bound to the success criterion. The consequence for measurement is right. A Hoeffding band on $\mathbb E[\max_k\langle e_k,u\rangle^2]$, from simulations that know $u$, bounds the mean-square success of every function of $\hat M$ at that budget.

ch-failure-threshold (does not block). The sentence that the band "certifies the failure of the whole class" needs its threshold. For the criterion $\Pr[|\langle F,u\rangle|\ge\epsilon]\ge\frac23$, failure is certified when the upper band lies below $\frac23\epsilon^2$, that is below $\frac16$ at $\epsilon=\frac12$.

The status, open, is honest. (a) rests on two equivalents from memory and on agreement with simulations to within 0.02 at three laws. (b2) is bulk delocalization.

Verdict ACCEPT.

### prop-measured-meets-proven-full-observer

(a). The value 0.160111 is right (section 2), and the stated bound $\kappa_{\mathrm{KL}}\le0.1602$ covers it. The arithmetic holds. $(8.3333-0.9242)/0.1602=46.25$ and $(16.6667-0.9242)/0.1602=98.27$. The constant $\frac43\log2=\log2+\frac23\cdot\frac12\log2=0.9242$. (b) is unchanged and sound, and my replication of round 02 stands beside it. (c). The ratios are $4000/46.25=86.5$ and $8000/98.27=81.4$, within the title's 87.

Verdict ACCEPT.

### def-statistic-learner-class

The added sentence is right (proven). A member of $\mathcal A_S^{\downarrow}$ at budget $n$ subsamples by coins independent of the observations, so it is a member at every larger budget, and $p_{S^{\downarrow}}$ is the left end of an interval. Naming $\mathcal A_S$ as the default keeps the window result of the band law meaningful.

Verdict ACCEPT.

## 5. The space after round 03

The space now holds a theory of learning attackers priced in learning units in two access models. Each claim carries a status I would sign.

- In the update stream at the optimum, a learning attacker is a class defined by the statistic it reads. The full observer's price on $Q_0$ is known within 87 at $d=200$, with a Fano lower side and a certified upper side (proven given one numerical constant, and empirical). The linear class's price is set by an outlier equation in which it reads a Cauchy transform of one signed measure of the label law, while the full observer reads that measure's $L^2$ norm (open, heuristic, with agreement to 0.02 in simulation, a proven edge test and a proven reduction of its optimality to delocalization). The two prices differ on laws built in the space, and the linear class can lose success as data grow.
- In the release model, the trainer's performance caps the attacker's accuracy, is attained by it for an exact release, and prices it at the trainer's records over the accepted slack exactly when the answers carry nature's noise at nature's power (proven, with a learner of the trainer's class as witness). For Halil's reconstruction example the floor on success is the registered thm-reconstruction-from-conditional-mean.
- Per-example normalization at a median fit hides every degree of the update channel, and clipping inherits this where it binds (proven).

What it does not hold is stated in the objects. These are the linear class's price at a measured dimension, nonlinear architectures, batches larger than one in the conjecture, and the deterministic equivalents, which stay heuristic. None of these is a defect of a stated claim. No hardness is planted, no cryptographic plug-in is used, and no ruling is assumed.

## 6. Challenges

| Challenge | Object | Blocks | Status |
| --- | --- | --- | --- |
| ch-kappa-in-error-term | thm-release-relearning-price-bracket (e) | no | new |
| ch-price-is-power | thm-release-relearning-price-bracket | no | new |
| ch-release-noise-reading | thm-release-relearning-price-bracket | no | new |
| ch-failure-threshold | conj-linear-class-reads-cauchy-transform (b1) | no | new |
| ch-vacuous-at-measured-dimension | the linear class | no | open, honest status |
| ch-chosen-query-scaling, ch-third-reading, ch-b-in-order-versus-exact, ch-quadrature-is-not-a-proof, ch-declaration-order, ch-no-trainer-price | | | resolved |

## Satisfied

SATISFIED yes

No blocking challenge remains, every kept aim is either proven or stands with an honest status, and the release theorem now gives Halil's floor on cost with both sides proven, its one recalled moment now proven here. The four open notes are one-line edits of scope and wording that would not change any verdict, and the open questions are stated as open in the objects.

## Verdicts

```text
VERDICT thm-release-relearning-price-bracket ACCEPT
VERDICT conj-linear-class-reads-cauchy-transform ACCEPT
VERDICT prop-measured-meets-proven-full-observer ACCEPT
VERDICT def-statistic-learner-class ACCEPT
BLOCKING 0
```
