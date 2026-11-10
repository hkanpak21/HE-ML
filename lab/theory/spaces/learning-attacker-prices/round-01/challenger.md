# Round 01 of learning-attacker-prices, challenger

Claude Opus 5.5, challenger, 2026-10-29. Judgement of `round-01/builder.md`, after `round-00/summary.md`.

Five of the six objects stand, and I accept them. The object I tested hardest does not stand as stated. The builder's amendment is right in its mechanism, and I concede an error of round 00. The empirical second moment reads the variance profile of its own fluctuation, and at $c_2=0$ a profile spike $s>1$ gives plain PCA an outlier as $T/d\to\infty$ (heuristic, rederived independently in section 3). Part (b) of conj-update-linear-class-price survives on that ground. Part (a) does not. At finite $T/d$ the linear class reads a whole function of the label law, not two numbers. On a law with $c_2=0$ and $s=0.756$ the bottom eigenvector of $\hat M$ has overlap 0.83 at $T=10d$, at $d=300$ and at $d=600$, against 0.833 predicted by that function (heuristic and empirical). One challenge blocks.

## 1. What I checked

I read the summary of round 00 and the builder's turn. I rederived properties (ii) and (iii) of def-optimum-update-stream, every step of thm-norm-weighted-update-pca with its constants $C_1=128C^2c_0^4/9$, $\frac38$, 24 and 12, the quadrature values 0.0801 and 0.0756 and the threshold $2.2\times10^8$, every step of prop-update-direction-fano-recovery with the constant 0.93, the limit 39 and the figure $0.83\,\varsigma^4$, the four parts of prop-full-clipping-optimum-filter, and the identity $15\cdot5^{-7/2}=3\cdot5^{-5/2}$ behind $s=0$ on the knife-edge law. I derived an outlier equation for $\hat M$ at finite $T/d$ (section 3.1), checked it against the builder's measurements and against my own simulations, and searched it for a counterexample. The simulations ran in my scratch folder, and each use below states its dimension and seed count. I did no web search. Prior work known only from memory is labelled so.

## 2. My open challenges

Resolved, by withdrawal or repair that I checked: ch-learner-class-gap, ch-magnitude-selected-pca, ch-readout-swallows-the-class (the class is now indexed by the statistic it reads), ch-spike-cancels-not-degree-four, ch-run-coordinate-misapplied (with my bound corrected to "at least $k-N$"), ch-learner-class-bounds-exist, ch-optimum-is-not-a-trajectory, ch-success-functional-unnamed, ch-compute-absent, ch-witness-is-pca, ch-crossing-constant-moves-with-batch, ch-clipping-closes-the-channel, ch-detection-to-recovery-constant, ch-theorem-uses-conjecture. The challenges ch-planted-moment-matching, ch-cumulant-against-null, ch-fourth-order-magnitude-factor, ch-lifted-trace-outlier and ch-noiseless-algebraic are moot after the withdrawal of their aim.

Two remain open and do not block. They are ch-no-trainer-price, deferred by the builder to round 02, and ch-vacuous-at-measured-dimension, since every upper bound in the space carries the unspecified constant of fact-subgaussian-sample-covariance-concentration. The builder says both plainly.

On the knife-edge remark under ch-spike-cancels-not-degree-four, I confirm $s=0$ there (proven, $\mathbb E[Z^6e^{-2Z^2}]=\mathbb E[Z^4e^{-2Z^2}]$). The equation of section 3.1 gives more. $T\equiv0$ makes the function $\Psi$ below vanish identically, so no second-order route opens at any $T/d$ (heuristic).

A correction to my round 00. I argued that at $c_2=0$ the $u$-dependent part of the fluctuation of $\hat M$ is a rank-one term along $\mathrm{vec}(uu^\top)$, so that no number of updates lifts it above the bulk. That was wrong. The $u$-dependent part is the inflated variance of the whole row of $\hat M$ along $u$, which is a perturbation of the same operator size as the bulk (proven at the level of entry variances, the builder's (iii)). On $Q_0$ my conclusion survives, because the equation of section 3.1 has no outlier root at any $T/d\in[1.6,1000]$ for $Q_0$ at $\varsigma^2\in\{0,0.1\}$ (heuristic, numerical root search), which agrees with PCA's failure in both our simulations. The reason is the equation, not $s<1$ (section 3.3).

## 3. Part (b) and the price of the linear class

### 3.1 The outlier equation

At $b=1$ write $\sigma^2=W^2+\varsigma^2$ and $a_t=\langle u,v_t\rangle=\xi_tW_tZ_t+\langle u,\zeta_t\rangle$. Given $(W_t,\xi_t,Z_t,\langle u,\zeta_t\rangle)$, the component of $v_t$ in $u^\perp$ is $\sigma_tg_t$ with $g_t\sim N(0,I_d-uu^\top)$, and $\mathbb E[a_t^2\mid W_t]=\sigma_t^2+W_t^2T(W_t)$ (proven, by (ii) of def-optimum-update-stream). Split $\hat M$ along $u$ into $\alpha=T^{-1}\sum_ta_t^2$, $h=T^{-1}\sum_ta_t\sigma_tg_t$ and $B=T^{-1}\sum_t\sigma_t^2g_tg_t^\top$. An eigenvalue $\lambda$ of $\hat M$ outside the spectrum of $B$ satisfies $\lambda=\alpha+h^\top(\lambda-B)^{-1}h$, and its eigenvector has squared overlap $1/(1+h^\top(\lambda-B)^{-2}h)$ with $u$ (proven, the Schur complement).

Put $\gamma=d/T$ and $g=T^{-1}\mathrm{tr}(\lambda-B)^{-1}$. Two deterministic equivalents are needed (heuristic, the generalized Marchenko and Pastur equation of Silverstein and Bai and an anisotropic law for weighted sample covariances, both from memory, unverified):
$$\lambda=\frac\gamma g+\mathbb E\Big[\frac{\sigma^2}{1-\sigma^2g}\Big],\qquad h^\top(\lambda-B)^{-1}h\approx\mathbb E\Big[\frac{a^2\sigma^2g}{1-\sigma^2g}\Big].$$
With $\alpha\to\mathbb E[\sigma^2]+c_2$ and $\mathbb E[a^2\mid W]=\sigma^2+W^2T(W)$, the terms in $\sigma^2$ cancel exactly, and an outlier is a root of
$$\gamma=g\,\Psi(g),\qquad\Psi(g)=\mathbb E\Big[\frac{W^2T(W)}{1-\sigma^2g}\Big],$$
with $g\in(0,g_+)$ for an outlier above the bulk and $g\in(g_-,0)$ for one below, where the edges $g_\pm$ solve $\gamma=g^2\,\mathbb E[\sigma^4/(1-\sigma^2g)^2]$. The overlap follows from the Schur formula by differentiating the second equivalent in $\lambda$.

Two checks. For constant $\sigma^2=\sigma_0^2$, $\Psi(g)=c_2/(1-\sigma_0^2g)$ and the root meets the edge exactly at $\gamma=(c_2/\sigma_0^2)^2$, the spiked-covariance transition (proven, given the two equivalents). The equation also reproduces the builder's measured overlaps. On the zero-spike law with $t=3$, where $s=5.28$, it predicts a bottom overlap of 0.758 at $T=50d$ and 0.707 at $T=200d$. The builder measured 0.77 and 0.67 for the larger of top and bottom at $d=200$.

### 3.2 What it confirms

$\Psi(g)=c_2+g\big(\mathbb E[W^4(Z^2-1)]+\varsigma^2c_2\big)+O(g^2)$ and $\mathbb E[\sigma^4]=\mathbb E[W^4]+2\varsigma^2\mu_2+\varsigma^4$. So the first two Taylor coefficients of $\Psi$ are $c_2$ and $s\,\mathbb E[\sigma^4]$, with exactly the builder's $s$ of (iii) (proven, by expansion). As $\gamma\to0$ at $c_2=0$, the root is $g\approx(\gamma/(s\,\mathbb E\sigma^4))^{1/2}$ and the edge $g_+\approx(\gamma/\mathbb E\sigma^4)^{1/2}$, so an outlier exists if and only if $s>1$, on both sides of the bulk (heuristic). This is the builder's criterion, reached without the Gaussian surrogate of the fluctuation. In units where the bulk has edges $\pm2$, the outliers sit at $\pm(\sqrt s+1/\sqrt s)$, and their eigenvectors have
$$\epsilon_0(s)=\sqrt{\frac{s-1}{2s}}$$
as overlap (heuristic, the same limit). This is 0.637 at $s=5.28$, and finite $T/d$ moves it by about 0.1 in the builder's range. For small $c_2$ at a fixed $s<1$, the transition of PCA sits at $T/d\approx\mathbb E[\sigma^4](1-s)^2/c_2^2$ (heuristic). The factor $\mathbb E[\sigma^4]/(\mu_2+\varsigma^2)^2$ is the kurtosis of the scale. That gives a cause for the non-Gaussian constant I measured in round 00.

So part (b) holds as a heuristic in the limit $T/d\to\infty$ taken after $d\to\infty$, with the formulas above as its content.

### 3.3 ch-finite-ratio-profile (blocks)

Part (a) states that for a fixed law with $s<1$ the linear price is of order $d/\beta^2$ for every fixed overlap and infinite at $c_2=0$. It is false. At a finite $T/d$ the bottom edge discounts heavy records quadratically, by $(1-\sigma^2g)^{-2}$, and the spike only linearly, by $(1-\sigma^2g)^{-1}$. A thin band of heavy records with $\mathbb E[Z^2-1\mid\text{band}]<1$ keeps $s$ below one and still gives an outlier.

The law. Let $p=\Pr[|Z|<1]=0.6827$ and $T_c=\mathbb E[Z^2\mid|Z|<1]-1=-0.709$. Take the band $1.32\le|Z|\le1.35$, with probability $p_b=0.0098$ and $T_b=\mathbb E[Z^2\mid\text{band}]-1=0.782$. Put $W=1$ on the band, $W=w_c$ on $\{|Z|<1\}$ with $w_c^2=p_bT_b/(p|T_c|)=0.0159$, $W=0$ elsewhere, and $\varsigma=0$. Then $c_2=w_c^2pT_c+p_bT_b=0$ exactly (proven), $A=1$, and
$$s=\frac{w_c^4pT_c+p_bT_b}{w_c^4p+p_b}=0.756$$
(proven, arithmetic).

The prediction (heuristic, section 3.1). There is no outlier above the bulk at any $T/d$. Below it, the bottom eigenvector of $\hat M$ has overlap 0.833 at $T=10d$, 0.814 at $T=20d$ and 0.615 at $T=100d$, with bottom eigenvalue 0.0034 at $T=10d$ and 0.0046 at $T=20d$.

The measurement (empirical). At $d=300$ over 4 seeds the bottom overlaps are 0.829, 0.808 and 0.612 at $T=10d$, $20d$ and $100d$. At $d=600$ over 3 seeds they are 0.825 and 0.826 at $T=10d$ and $20d$, with mean bottom eigenvalues 0.00336 and 0.00455 against a next eigenvalue of 0.00442 and 0.00619. A second band, $1.30\le|Z|\le1.38$ with $s=0.726$, gives 0.654, 0.612 and 0.226 at $d=300$ against predictions 0.668, 0.626 and 0.374.

The overlap agrees with the prediction to within 0.01 at two dimensions, so it does not drift with $d$. Hence $p_{\hat M}(1/2)\le10d$ on this law, while part (a) asserts it is infinite. Perturbing the band weight gives $c_2=\delta>0$ small with the outlier intact (heuristic, continuity of the root), so the clause "of order $d/\beta^2$ for every fixed overlap" fails as well. The criterion "exactly when $s>1$" holds only in the limit $T/d\to\infty$. The overlap is not monotone in $T$. It rises to about 0.83 near $T=10d$ and falls toward zero as $T/d$ grows, so the linear class's price is a window in $T$, not a threshold. The example needs small injected noise. The best predicted bottom overlap over $T/d$ is 0.62 at $\varsigma^2=0.01$ and 0.47 at $\varsigma^2=w_c^2=0.016$, and the outlier disappears between $\varsigma^2=0.02$ and $0.03$ (heuristic, numerical root search).

### 3.4 The repair

The linear class reads the signed measure $W^2T(W)\,dP$ pushed forward to $\sigma^2$, through its Cauchy-type transform $\Psi$, at the spectral edge. The full observer reads the same measure in $L^2$, since $\kappa_2=\frac12\mathbb E[(W^2T(W))^2/\sigma^4]$ at $b=1$. I would restate the conjecture with that pair as its content, as follows.

- (a') For a fixed law, the bottom or top eigenvector of $\hat M$ reaches overlap $\epsilon$ at $T/d=1/\gamma$ exactly when the equation of section 3.1 has a root with that overlap (heuristic, to be proven). $\beta$ and $s$ govern the limit $T/d\to\infty$ only.
- (b') The class price $p_{\hat M}$ equals the spectral price. This needs a lower bound on every function of $\hat M$, which is open, as the builder says of (a).
- (c') The price of linearity is the ratio between the least $T$ allowed by (a') and the full observer's price, of order $d/\kappa_2$ where that is attained (open).

The Jensen ratio of round 00 is the large-noise case of (c'), where $\sigma^2$ is nearly constant and $\Psi(g)\approx c_2/(1-\varsigma^2g)$.

## 4. The objects of round 01

### def-optimum-update-stream

(i) is the round-00 computation (proven). (ii) holds, since $\mathbb E[XX^\top\mid W]=I_d+T(W)uu^\top$ when $X_\perp$ is independent of $(Z,W,\xi)$ (proven). (iii) holds as stated. I recomputed $T\,\mathrm{Var}(\hat M_{uw})=\mathbb E[W^4Z^2]+\varsigma^2(\mu_2+c_2)+\varsigma^2\mu_2+\varsigma^4$ and $T\,\mathrm{Var}(\hat M_{ww'})=\mathbb E[W^4]+2\varsigma^2\mu_2+\varsigma^4$, with every cross term vanishing (proven). The bound $s\ge-1$ needed for the profile to be a variance follows from $Z^2-1\ge-1$. (iii) is a ratio of entry variances, and its spectral meaning holds only as $T/d\to\infty$ (section 3). The remark on the trajectory carries my linear-response constant correctly as a heuristic.

Verdict ACCEPT.

### def-statistic-learner-class

The class is well defined. If the summed loss depends on the observations only through $S$ and the method returns a minimizer chosen without the observations or runs full-batch descent from a fixed start, its output is a function of $S$ and independent coins (proven). Remark (i) is right with "at least $k-N$" (proven). Remark (ii) is right. The repair answers ch-readout-swallows-the-class. A learning attacker as such is still as large as every estimator, since a mixture with $n$ components fitted by maximum likelihood reads the empirical measure, which is sufficient. Classes are now indexed by $S$, so this is harmless, and remark (ii) says it.

ch-precision-reads-past-the-statistic (does not block). The sentence that a lower bound on $p_S$ "binds the learner at every precision" is false for an implementation that sums per-observation terms in floating point. Its output depends on the ordered observations through rounding, not on $S$ alone. AKMSS21 builds rounding channels that carry exactly such information (fact-fine-precision-sgd-simulates-pac). The sentence holds for every learner whose output is a measurable function of $S$ and independent coins, whatever arithmetic it uses after it forms $S$ exactly, and it should say that.

ch-mean-parameter (does not block). A linear-Gaussian latent model with a mean parameter reads $(\bar v,\hat M)$, not $\hat M$. The sentence "which are $\hat M$ in the update stream, whose mean is zero" conflates the empirical mean with its expectation. Either fix the model's mean at zero or set $S=(\bar v,\hat M)$. The price is unaffected in order (heuristic, $\bar v$ is one sample of a spiked law).

Other regime. The class regime sits beside SQ as the builder says, and section 3 is an instance of a statistic class whose price is set by a transform of the label law, which is the kind of result the definition is for.

Verdict ACCEPT.

### thm-norm-weighted-update-pca

Part (a) holds (proven). An orthogonal $R$ fixing $u$ fixes $Z$, so $(RX,W)$ has the law of $(X,W)$ because $W$ depends on $X$ only through $Z$. The off-diagonal block vanishes and the $u^\perp$ block is scalar.

Part (b) holds (proven, line by line). The vector $y_t$ has mean zero by the sign flip of $(\xi,\zeta)$, and its $\psi_2$ norm is at most $c_0(A+\varsigma)$ because $g\le1$. Whitening by $M_g^{-1/2}$ costs $\lambda_-^{-1/2}$. With $C_1=128C^2c_0^4/9$ the condition gives $\eta\le3\lambda_-|\gamma_g|/(8c_0^2(A+\varsigma)^2\lambda_+)$, since $\sqrt{18/128}=\frac38$. This is below one because $|\gamma_g|\le\lambda_+\le A^2+\varsigma^2\le(A+\varsigma)^2$ and $c_0\ge1$. Then $\|\hat M_g-M_g\|\le\frac38|\gamma_g|$, and the two-sided Rayleigh argument gives $\langle\hat u,u\rangle^2\ge\frac14$ without the Davis and Kahan theorem.

Part (c) holds (proven). $\gamma_g=u^\top M_gu-w^\top M_gw$ and $\alpha_g=w^\top M_gw$. Replacing $g(r)$ by $\bar g$ leaves $\mathbb E[\bar gW^2T(W)]$ and $\mathbb E[\bar g\sigma^2]$ by (ii). The stated $\mathbb E(r-W^2-\varsigma^2)^2\le6(A^2+\varsigma^2)^2/d$ holds, and in fact the three cross terms vanish, which gives $2(A^2+\varsigma^2)^2/d$. The constants $\sqrt6\sqrt{96}=24$ and $\sqrt6\sqrt{24}=12$ are right.

Part (d) holds. I recomputed the atom's term at $\delta=0$ as $(1-p)w_0^2\cdot1.5251=m_2-m_4=0.08645$ and the continuous part as $-0.0063$, so 0.0801. At $\delta=0.02$ the weight is $0.9286$ on the atom, giving 0.0819 and 0.0756 in total. For the consequence, $L=20$ and $(A^2+\varsigma^2)^2=1.21$ give $580.8/\sqrt d\le0.0406$ from $d\ge2.05\times10^8$, so the stated $2.2\times10^8$ is sufficient.

ch-signed-weights (does not block). Weights in $[0,1]$ cannot represent the signed linearized optimum $\omega\propto W^2T(W)/\sigma^4$. So the theorem witnesses an upper bound on $p_*$ that need not reach the order $d/\kappa_2$ of part (c) of the conjecture. Splitting $g=g_+-g_-$ and applying Step 3 to each part extends (b) to bounded signed weights at the cost of a constant (heuristic, the two errors add).

Novelty. Weighted spectral estimators are standard for single-index and phase-retrieval models (from memory, unverified). The exact symmetry of (a) and the explicit perturbation of (c) for this stream are new to the record.

Verdict ACCEPT.

### prop-update-direction-fano-recovery

Step 1 holds. Markov's inequality with $\mathbb Ee^{d\rho^2/4}\le\sqrt2$ from Step 4 of the theorem gives the cap (proven). Step 2 holds. Coins independent of $(u,O)$ do not change $I(u;O)$, $\mathrm{kl}(p'\|q')\ge p'\log(1/q')-\log2$ because the binary entropy is at most $\log2$, and monotonicity in $p'\ge p$ and $q'\le q\le1$ finishes it (proven). Step 3 is the golden formula with $Q=P_\circ$ (proven). At $p=\frac23$ and $\epsilon=\frac12$ the constant is $0.231+0.693=0.924$, so 0.93 is conservative.

Step 4 holds (proven). Convexity of KL over the Gaussian mixture gives $K(a)$, with $\mathbb E[m^2\mid a]=\sigma^2-\varsigma^2+b^{-2}\sum_ia_i^2T(a_i)$. For the limit, the expansion of part (d) is uniform on $a\le3\sqrt{\log\varsigma}$ because the neglected terms are smaller by a factor of order $a^4/\varsigma^2\to0$. The tail costs $O(\varsigma^{-1/2}\sqrt{\log\varsigma})$. The figure $(33.33-0.93)/39=0.83$ and the factor $200/0.83\approx240$ are right.

The proposition repairs ch-detection-to-recovery-constant. The argument is the standard Fano bound with a spherical cap (from memory, unverified), and its value here is that its constants are explicit and it needs no bound on the labels.

Verdict ACCEPT.

### prop-full-clipping-optimum-filter

(a) holds, since $\|\psi_\theta\|=|f_\theta(x)-y|\,\|\nabla_\theta f_\theta(x)\|$ (proven). (b) holds. At $\theta^*=0$ the normalized update is $-C\xi X/\|X\|$, and $(X,-\xi)$ has one law under $P_u$ and $P^\circ$ (proven). (c) holds. A conditional median with no atom makes the residual's sign a fair coin independent of $X$ (proven). (d) is the definition. The drift $C\,\mathbb E[(2F(f_\theta(X)\mid X)-1)\nabla f_\theta/\|\nabla f_\theta\|]$ is right, so a median fit is stationary (proven).

ch-normalization-not-clipping (does not block). The object of (b) and (c) is per-example normalization. Clipping at $C$ equals it only on the event that every per-example gradient exceeds $C$. At a median fit with labels that have a continuous conditional law, residuals near zero have positive probability, so clipping at any $C>0$ leaves a positive fraction of records unclipped, and (c) never describes clipping exactly. At $\theta^*=0$ in the update stream, $\|\psi\|=W\|X\|$, so clipping is full with high probability when $W\ge w_{\min}>0$ and $C<w_{\min}\sqrt d/2$ (heuristic, $\|X\|$ concentrates). The statement should name normalization as its object and the clipping regime as a hypothesis. The other-regime paragraph already says that the leak runs through the unclipped set.

A remark on scope, not a challenge. The normalized stream reveals each client's gradient direction, so a secret carried by the input law is not hidden. The proposition says this in its title.

Verdict ACCEPT.

### conj-update-linear-class-price

Part (a) is false (ch-finite-ratio-profile, blocks, section 3.3). Part (b) holds as a heuristic in the limit $T/d\to\infty$, and section 3.2 supplies its location and its $\epsilon_0(s)$. Part (c) is plausible at large noise, where $\sigma^2$ is nearly constant and finite-ratio effects vanish. Its premise "$s<1$" should read "no root of the outlier equation", and its $p_*$ needs the signed weights of ch-signed-weights. Part (d) is a reasonable heuristic. The profile and the magnitude gain both come from fourth-order fluctuations of the batch mean, which fall as $1/b$.

The empirical support is accurate as reported, and section 3.1 reproduces it quantitatively. The experiment should add the band law of section 3.3 and record overlap against $T/d$, since the window is the new prediction. "A drift of $\epsilon_0$ with $d$ at fixed $s$ refutes (b)" is the right refutation rule. A drift with $T/d$ refutes nothing, since the equation predicts one.

Verdict REVISE.

## 5. The space after round 01

The space now holds what round 00 lacked. There is a class of learning attackers defined by the statistic it reads, a proven polynomial-time witness for the full observer, a recovery lower bound with explicit constants, a proven filter from training, and an instance in which the linear class and the full observer differ, with both measured at $d=200$ to $600$. Halil's "subclass of problems" has an exact meaning here. The class is the set of functions of $\hat M$, and its price is set by a transform of the label law that the full observer reads differently.

Three things keep me from signing it. The price of the linear class is stated through the wrong invariants (section 3.3). No price is yet known within a constant at a measured dimension, because every upper bound carries an unspecified constant, and the Fano bracket is wide. The relative bound Halil named, attacker against trainer, is deferred to round 02. The first must be repaired for BLOCKING 0. The second and third can stand with an honest status.

Halil's constraints are met. No hardness is planted, no cryptographic plug-in is used, and no ruling is assumed. Clipping enters as part of the procedure given, as the builder says. The mathematics of section 3.1 is, to my eye, the most beautiful object the space has produced. One Schur complement shows the linear attacker reading a Cauchy transform of the label law while the full observer reads its $L^2$ norm.

## 6. Challenges

| Challenge | Object | Blocks | Status |
| --- | --- | --- | --- |
| ch-finite-ratio-profile | conj-update-linear-class-price (a) | yes | new |
| ch-precision-reads-past-the-statistic | def-statistic-learner-class | no | new |
| ch-mean-parameter | def-statistic-learner-class | no | new |
| ch-signed-weights | thm-norm-weighted-update-pca | no | new |
| ch-normalization-not-clipping | prop-full-clipping-optimum-filter | no | new |
| ch-no-trainer-price | the aims | no | open, deferred to round 02 |
| ch-vacuous-at-measured-dimension | def-statistic-learner-class | no | open |
| the fourteen of round 00 listed in section 2 | | | resolved |
| the five tied to the withdrawn aim | | | moot |

## Satisfied

SATISFIED no

One blocking challenge remains, ch-finite-ratio-profile. The conjecture that carries the space's answer to Halil sets the linear class's price by $\beta$ and $s$, and a law with $s<1$ and $c_2=0$ refutes it at finite $T/d$. A further round that restates it through the outlier equation of section 3.1 would change that verdict.

## Verdicts

```text
VERDICT def-optimum-update-stream ACCEPT
VERDICT def-statistic-learner-class ACCEPT
VERDICT thm-norm-weighted-update-pca ACCEPT
VERDICT prop-update-direction-fano-recovery ACCEPT
VERDICT prop-full-clipping-optimum-filter ACCEPT
VERDICT conj-update-linear-class-price REVISE
BLOCKING 1
```
