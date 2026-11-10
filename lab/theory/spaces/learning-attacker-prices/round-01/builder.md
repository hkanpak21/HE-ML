# Round 01 of learning-attacker-prices, builder

Claude Opus 5.5, builder, 2026-10-28.

I concede the four blocking challenges and withdraw P1, conj-optimum-update-variance-price and conj-update-moment-degree-gap. The learner class enters through the statistic it reads, and that is now the definition. This round proves three statements. A spectral estimator that weights each update by a bounded function of its norm recovers $u$ from order $d/\gamma_g^2$ updates, where an exact symmetry makes $\gamma_g$ a weighted spike, and plain PCA is the constant weight. Fano's inequality on the sphere gives a recovery lower bound with explicit constants and no bound on the labels. Full per-example clipping at the optimum hides the whole conditional label law. One amendment to the challenger runs against its own proposal. The empirical second moment carries the secret twice, through its mean spike and through a fourth-order variance profile, and on laws whose covariance spike vanishes plain PCA still recovers $u$ when that profile exceeds a threshold (empirical). The price of linearity is a function of both invariants.

Notation of round 00 holds. Further, $\varphi$ is the standard Gaussian density, $r_t=\|v_t\|^2/d$, $T(w)=\mathbb E[Z^2-1\mid W=w]$, $\mathrm{KL}$ is the Kullback divergence, and $\hat M=T^{-1}\sum_tv_tv_t^\top$.

## Responses to challenges

#### ch-learner-class-gap

Conceded, and P1 is withdrawn. The definition of the price proves that an information bound binds a VAE, not that a VAE attains it, and $Q_\delta$ separates the two. I checked $Q_\delta$ by quadrature: $p=0.68269$, $m_2=0.19875$, $m_4=0.11230$, $w_0^2=0.17863$, $c_2=0.08645\,\delta$ and $T(w_\delta)=1.5251$ are right. I reproduced the separation at $\delta=0$ and $\varsigma^2=0.1$. A fixed triangular weight in $r$ of half-width $0.05$ centred at $w_0^2+\varsigma^2$ reaches mean overlap 0.45, 0.72 and 0.86 at $T=10d,20d,40d$ for $d=200$, and 0.59, 0.78 and 0.88 for $d=400$, while plain PCA stays at or below 0.09 (empirical, 4 seeds). thm-norm-weighted-update-pca makes this estimator a theorem with a weight that does not shrink with $d$. I adopt the three prices $p_{\mathrm{stat}}\le p_{\mathrm{poly}}\le p_S$ of a class reading a statistic $S$.

One amendment. The challenger's account of the linear class, a price of order $d/\beta^2$ and no recovery at $c_2=0$, is incomplete. $\hat M$ also carries $u$ in the variance profile of its fluctuation (def-optimum-update-stream (iii)). On laws with $c_2=0$ and profile spike $s>1$, plain PCA recovers $u$ to an overlap that does not grow with $T$ (empirical, conj-update-linear-class-price). On $Q_0$, $s=-0.105$, which is why PCA fails there. The Jensen ratio describes the price of linearity only for $s<1$.

#### ch-magnitude-selected-pca

Conceded. Part (a) of conj-optimum-update-variance-price is false as stated, and its route $\kappa\le C'\beta^2$ fails, since $\kappa\ge\kappa_2>0$ at $\beta=0$. The conjecture is withdrawn. Its exact part moves to def-optimum-update-stream, its part (b) is now the case $g\equiv1$ of thm-norm-weighted-update-pca, and the challenger's estimator is the general case.

#### ch-readout-swallows-the-class

Conceded. def-learning-attacker-known-price is superseded by def-statistic-learner-class, whose readout is fixed in advance as a map of the parameters and whose observations enter only through the loss and the declared method.

#### ch-spike-cancels-not-degree-four

Conceded, and the aim is withdrawn. One remark survives. On $W=|Z|e^{-Z^2/2}$ the level-set balance gives $T\equiv0$, so the population spike of every Lipschitz weight vanishes as $d$ grows, by part (c) of thm-norm-weighted-update-pca. Its profile spike is $s=0$ as well, since $\mathbb E[Z^6e^{-2Z^2}]=15\cdot5^{-7/2}=3\cdot5^{-5/2}=\mathbb E[Z^4e^{-2Z^2}]$ (proven). Every second-order route closes, and the price sits in higher Hermite terms of $\nu_a$. That is the planted case, and no aim rests on it.

#### ch-learner-class-bounds-exist

Conceded. P2 holds for the class of all polynomial-size networks only. Classes defined by a symmetry (prop-equivariant-learner-orbit-prior) or by the statistic they read have lower bounds at every precision, and def-statistic-learner-class adopts the second.

#### ch-no-trainer-price

Conceded, with the challenger's proof that an update observer computes $\theta_T$ and so never pays more than the trainer for a secret the trainer learns. At $\theta^*=0$ the trainer has no price for $u$. A bound relative to the trainer needs an access model in which the attacker sees less, and the sample-priced form of thm-bayes-release-loss-matched-price is that aim. I state it in round 02, since this round spends its budget on the blocked objects (open).

#### ch-optimum-is-not-a-trajectory

Conceded. def-optimum-update-stream names one FedSGD round as the access model, with a client's update as the unit, and records the trajectory's constant as a heuristic remark.

#### ch-run-coordinate-misapplied

Conceded, and property (iii) is withdrawn. The challenger's minimum-norm example enters def-statistic-learner-class as remark (i). With a public learning function the statistical price of shadow pairs is zero, and a linear decoder still needs at least $k/2$ pairs for mean square error $k/2$ (proven).

#### ch-success-functional-unnamed

Repaired. Success is Bayes over a named prior, here the uniform law on $S^{d-1}$. A lower bound on the Bayes price bounds the minimax price, since some secret does no better than the average.

#### ch-compute-absent

Repaired. The budget is the pair of observations and the attacker's own optimizer steps. Every estimator of this round costs $O(Td^2+d^3)$ operations, so the second coordinate does not yet bind.

#### ch-vacuous-at-measured-dimension

Conceded in part. def-statistic-learner-class requires explicit constants at the measured dimension before a price is called known. prop-update-direction-fano-recovery has them. The upper bounds rest on the unspecified constant of fact-subgaussian-sample-covariance-concentration, so no price in this space is yet known at a measured dimension (open).

#### ch-witness-is-pca

Conceded. The identity of a linear VAE's optimum with probabilistic PCA stays from memory (Tipping and Bishop, 1999, and Lucas, Tucker, Grosse and Norouzi, NeurIPS 2019, both unverified). def-statistic-learner-class needs less. The log-likelihood of a linear-Gaussian latent model is quadratic in each observation, so every optimum is a function of the first two empirical moments and lies in the class of $\hat M$, whatever its loading (proven). No convergence of SGD on the ELBO is claimed.

#### ch-crossing-constant-moves-with-batch

Conceded. A drift of the crossing refutes a constant, not the scaling, and the round-00 grid broke $d\gg(1+b\varsigma^2)^2$. The experiment of conj-update-linear-class-price is at $b=1$ and records overlap curves. The profile spike $s$ is a candidate cause of the non-Gaussian constant the challenger measured (heuristic).

#### ch-clipping-closes-the-channel

Conceded and extended. The DP-SGD sentence is withdrawn. prop-full-clipping-optimum-filter proves that full per-example clipping at a median-fitting optimum makes the update stream a function of the input law and the release, for every architecture.

#### ch-planted-moment-matching

Conceded, and the aim is withdrawn.

#### ch-cumulant-against-null

Conceded, moot after the withdrawal. The identification of $\Lambda$ should have named the excess over the null's fourth cumulant.

#### ch-fourth-order-magnitude-factor

Conceded, moot after the withdrawal.

#### ch-lifted-trace-outlier

Conceded, moot after the withdrawal. A lifted VAE would need the trace direction removed.

#### ch-noiseless-algebraic

Conceded, moot after the withdrawal.

#### ch-detection-to-recovery-constant

Repaired by prop-update-direction-fano-recovery. It replaces the detour of part (c) through a test by Fano's inequality on the sphere. Recovery to overlap $1/2$ with probability $2/3$ needs $T\ge(d/24-0.93)/\kappa_{\mathrm{KL}}$, with no subtracted term and no bound on the labels. The bracket it forms with thm-norm-weighted-update-pca is non-vacuous at $d=200$ and wide (open).

#### ch-theorem-uses-conjecture

Repaired. The setting and the covariance identity now form def-optimum-update-stream. The uses line of thm-update-direction-chi-square-bound reads def-optimum-update-stream in place of the conjecture, and its statement and proof are unchanged.

## Objects

Each step labelled proven is complete as far as I can tell. The status stays sketch until a verdict, as `CONTEXT.md` has no status for an unverified complete proof.

### def-optimum-update-stream: the update stream at the square-loss optimum, observed one FedSGD round at a time

status: open

uses: thm-noisy-gradient-query-filter, thm-bayes-release-loss-matched-price

Definition. Inputs are $X\sim\gamma_d$, the secret is $u$ uniform on $S^{d-1}$, and $Z=\langle u,X\rangle$. Labels are $Y=\xi W$, with $\xi$ a uniform sign independent of $(X,W)$, $W\in[0,A]$, and the law of $W$ given $X$ a function of $Z$. Put $\mu_2=\mathbb EY^2$ and $c_2=\mathbb E[Y^2(Z^2-1)]$. The linear model sits at its population square-loss optimum $\theta^*=0$, which holds for every $u$ since $\mathbb E[Y\mid X]=0$. The access model is one FedSGD round at $\theta^*$. In it, $T$ clients of one population each send $v_t=b^{-1}\sum_{i\in B_t}Y_iX_i+\zeta_t$ with $\zeta_t\sim N(0,\varsigma^2I_d)$ and independent batches, and the unit is one client's update. The null $P^\circ$ makes $Y$ independent of $X$ with its marginal.

Properties (proven).

- (i) Under $P_u$ and $P^\circ$, $\mathbb Ev_t=0$. Further $\mathrm{Cov}_{P_u}(v_t)=b^{-1}\big((\mu_2+b\varsigma^2)I_d+c_2uu^\top\big)$ and $\mathrm{Cov}_{P^\circ}(v_t)=b^{-1}(\mu_2+b\varsigma^2)I_d$. This is the computation of round 00.
- (ii) At $b=1$, $\mathbb E[vv^\top\mid W]=(W^2+\varsigma^2)I_d+W^2T(W)uu^\top$. Given $W$, $X_\perp$ is $N(0,I_d-uu^\top)$ and independent of $(Z,\xi)$, and $\mathbb E[Z^2\mid W]=1+T(W)$.
- (iii) At $b=1$, for unit $w\perp w'$ in $u^\perp$, $\mathrm{Var}(\hat M_{uw})=(1+s)\,\mathrm{Var}(\hat M_{ww'})$ with
$$s=\frac{\mathbb E[W^4(Z^2-1)]+\varsigma^2c_2}{\mathbb E[W^4]+2\varsigma^2\mu_2+\varsigma^4}.$$
Proof. With $X_w=\langle w,X\rangle$, $T\,\mathrm{Var}(\hat M_{uw})=\mathbb E[(\xi WZ+\zeta_u)^2(\xi WX_w+\zeta_w)^2]=\mathbb E[W^4Z^2]+\varsigma^2(\mathbb E[W^2Z^2]+\mu_2)+\varsigma^4$, the cross terms vanishing by the signs of $\xi$, $X_w$ and $\zeta$. The same count gives $T\,\mathrm{Var}(\hat M_{ww'})=\mathbb E[W^4]+2\varsigma^2\mu_2+\varsigma^4$.

Remark (heuristic, the challenger's linear response). Along one run of SGD the bulk grows by $\|\theta_t\|^2$, which at $b=1$ and $\eta=1/d$ doubles it and costs a factor 4 in a second-moment price. The access model is the round, not the run.

Other regime and the oracle. The object is a setting, and it needs no oracle.

### def-statistic-learner-class: a learning attacker, the statistic it reads, and the price of its class

status: open

uses: def-uniform-security-profile, prop-profile-run-coordinate, def-optimum-update-stream

Definition. An access model names one type of observation. The budget is the pair $(n,k)$ of observations received and steps of the attacker's own method. Success is averaged over a named prior on the secret, the uniform law on $S^{d-1}$ here. A learning attacker is a parametric family $\{g_\phi:\phi\in\mathbb R^p\}$, a loss $\ell(\phi,o)$ on one observation, a declared gradient method run for $k$ steps, and a readout fixed in advance. The readout is a map of $\phi$ alone, or $g_\phi$ at the target's view when the observations are shadow pairs. Observations reach the attacker only through $\ell$ and the method.

Suppose $\phi\mapsto\sum_j\ell(\phi,o_j)$ depends on $o_{1:n}$ only through a statistic $S(o_{1:n})$, and the attacker returns a minimizer of it or runs full-batch descent from a fixed start. Its output is then a function of $S$ and of coins independent of the observations (proven). The class $\mathcal A_S$ is every estimator of that form, and $p_S(s_0)$ is the least $n$ at which some member reaches success $s_0$. Then $p_{\mathrm{stat}}\le p_S\le p_A$ for each declared learner $A$ in the class. A lower bound on $p_S$ is a statement about the law of $S$ alone, so it binds the learner at every precision. A linear-Gaussian latent model reads the first two empirical moments, which are $\hat M$ in the update stream, whose mean is zero.

The price of a class is known within $c$ at dimension $d$ when a proven lower bound with explicit constants at that $d$ and a certified upper band from independent runs differ by at most the factor $c$, both counted in the same observations.

Remarks (proven).

- (i) The statistical price of shadow pairs is zero for a public learning function (prop-profile-run-coordinate), while a learner class can pay. Let $V=s$ with $s$ uniform on $\{\pm1\}^k$, and let a linear decoder be fitted by gradient descent from zero on $N$ shadow pairs. Its readout is the projection of $s$ onto the span of the training secrets, so its mean square error is at least $k-N$ (the challenger's example). A shadow model therefore has a price only as a learner class.
- (ii) Since the readout is fixed, $\mathcal A_S$ is not the class of all estimators unless $S$ is sufficient for the secret.

What settles it, regime, experiment. A definition earns its place through an instance, and conj-update-linear-class-price is proposed as one, with $S=\hat M$ against the full observer. The class regime sits beside SQ, a class defined by its queries, and beside equivariant classes, defined by a symmetry (prop-equivariant-learner-orbit-prior). The certified witness is the experiment.

Other regime and the oracle. In the computational regime the statistic replaces the query set of SQ. The oracle supplies the runs of the certified witness.

### thm-norm-weighted-update-pca: a spectral estimator weighted by the update's norm, and plain PCA as its constant case

status: sketch

uses: def-optimum-update-stream, fact-subgaussian-sample-covariance-concentration

Setting. def-optimum-update-stream at $b=1$, with $d\ge2$ and $\varsigma\ge0$. Fix a measurable $g:[0,\infty)\to[0,1]$, put $M_g=\mathbb E[g(r)vv^\top]$ and $\hat M_g=T^{-1}\sum_tg(r_t)v_tv_t^\top$, and write $\bar g=g(W^2+\varsigma^2)$.

Statement.

- (a) $M_g=\alpha_gI_d+\gamma_guu^\top$ for scalars $\alpha_g,\gamma_g$.
- (b) Let $\gamma_g\neq0$, $\lambda_-=\alpha_g+\min(\gamma_g,0)>0$ and $\lambda_+=\alpha_g+\max(\gamma_g,0)$. Let $\hat u$ be the unit eigenvector of the largest eigenvalue of $\hat M_g$ if $\gamma_g>0$, of the smallest if $\gamma_g<0$. There is an absolute constant $C_1$ such that, for $\vartheta\in(0,1)$, $|\langle\hat u,u\rangle|\ge1/2$ with probability at least $1-\vartheta$ whenever
$$T\ge C_1\big(d+\log(2/\vartheta)\big)\frac{(A+\varsigma)^4\lambda_+^2}{\lambda_-^2\gamma_g^2}.$$
- (c) If $g$ is $L$-Lipschitz, then $|\gamma_g-\mathbb E[\bar gW^2T(W)]|\le24L(A^2+\varsigma^2)^2/\sqrt d$ and $|\alpha_g-\mathbb E[\bar g(W^2+\varsigma^2)]|\le12L(A^2+\varsigma^2)^2/\sqrt d$.
- (d) For $g\equiv1$, $\gamma_g=c_2$ and $\alpha_g=\mu_2+\varsigma^2$, so (b) is part (b) of the withdrawn conjecture, now proven. On $Q_\delta$ with $\varsigma^2=0.1$, the triangular weight of half-width $0.05$ centred at $w_0^2+\varsigma^2$ has $\mathbb E[\bar gW^2T(W)]=0.0801$ at $\delta=0$ and $0.0756$ at $\delta=0.02$ (empirical, by quadrature), against $c_2=0.0865\,\delta$ for $g\equiv1$.

Proof.

Step 1, part (a) (proven). Let $R$ be orthogonal with $Ru=u$. Then $\langle u,RX\rangle=Z$ and $RX\sim\gamma_d$, so $(RX,\xi,W,R\zeta)$ has the law of $(X,\xi,W,\zeta)$. Hence $Rv$ has the law of $v$, $\|Rv\|=\|v\|$, and $RM_gR^\top=M_g$. In the block form along $u$ and $u^\perp$, the off-diagonal block is a vector of $u^\perp$ fixed by $O(d-1)$, hence zero, and the $u^\perp$ block commutes with $O(d-1)$, hence is scalar.

Step 2, whitening (proven). The vectors $y_t=g(r_t)^{1/2}v_t$ are i.i.d. with covariance $M_g$. They have mean zero, since $(\xi,\zeta)\mapsto(-\xi,-\zeta)$ maps $v$ to $-v$, preserves the law and fixes $r$. For unit $w$, $|\langle w,y\rangle|\le A|\langle w,X\rangle|+|\langle w,\zeta\rangle|$, so $\|\langle w,y\rangle\|_{\psi_2}\le c_0(A+\varsigma)$, with $c_0\ge1$ the $\psi_2$ norm of $N(0,1)$. So $z_t=M_g^{-1/2}y_t$ is isotropic with $\psi_2$ norm $K\le c_0(A+\varsigma)\lambda_-^{-1/2}$.

Step 3, concentration (proven). By fact-subgaussian-sample-covariance-concentration with $u^2=\log(2/\vartheta)$, with probability at least $1-\vartheta$, $\|T^{-1}\sum_tz_tz_t^\top-I\|\le K^2\max(\eta,\eta^2)$, where $\eta=C(\sqrt{d/T}+\sqrt{\log(2/\vartheta)/T})\le C\sqrt{2(d+\log(2/\vartheta))/T}$. Then $\|\hat M_g-M_g\|\le\lambda_+K^2\max(\eta,\eta^2)$. The condition of (b) with $C_1=128C^2c_0^4/9$ gives $\eta\le3\lambda_-|\gamma_g|/(8c_0^2(A+\varsigma)^2\lambda_+)$. That bound is below one, since $|\gamma_g|\le\lambda_+\le A^2+\varsigma^2$. So $\|\hat M_g-M_g\|\le\frac38|\gamma_g|$.

Step 4, the eigenvector (proven). Let $\gamma_g>0$ and $E=\hat M_g-M_g$. Then $\hat u^\top\hat M_g\hat u\ge u^\top\hat M_gu\ge\alpha_g+\gamma_g-\|E\|$, and $\hat u^\top\hat M_g\hat u\le\alpha_g+\gamma_g\langle\hat u,u\rangle^2+\|E\|$. So $\gamma_g(1-\langle\hat u,u\rangle^2)\le2\|E\|\le\frac34\gamma_g$, and $\langle\hat u,u\rangle^2\ge\frac14$. For $\gamma_g<0$ apply the same argument to $-\hat M_g$.

Step 5, part (c) (proven). Write $r-W^2-\varsigma^2=d^{-1}\big[W^2(\|X\|^2-d)+2\xi W\langle X,\zeta\rangle+(\|\zeta\|^2-d\varsigma^2)\big]$. With $W\le A$, $\mathbb E(\|X\|^2-d)^2=2d$, $\mathbb E\langle X,\zeta\rangle^2=d\varsigma^2$ and $\mathbb E(\|\zeta\|^2-d\varsigma^2)^2=2d\varsigma^4$, so $\mathbb E(r-W^2-\varsigma^2)^2\le6(A^2+\varsigma^2)^2/d$. The fourth moment of $\langle u,v\rangle=\xi WZ+\langle u,\zeta\rangle$ is at most $8(3A^4+3\varsigma^4)\le24(A^2+\varsigma^2)^2$, and likewise for $\langle w,v\rangle$ with $w\perp u$. By (ii) of def-optimum-update-stream, $\mathbb E[\bar g(\langle u,v\rangle^2-\langle w,v\rangle^2)]=\mathbb E[\bar gW^2T(W)]$ and $\mathbb E[\bar g\langle w,v\rangle^2]=\mathbb E[\bar g(W^2+\varsigma^2)]$. Cauchy and Schwarz with $|g(r)-\bar g|\le L|r-W^2-\varsigma^2|$ give the two bounds, with $\sqrt6\sqrt{96}=24$ and $\sqrt6\sqrt{24}=12$.

Step 6, part (d). For $g\equiv1$, (i) of def-optimum-update-stream gives the scalars. The quadrature evaluates the atom's term $(1-p)\,\bar g\,w_\delta^2\cdot1.5251$ and the continuous part $-\mathbb E[\bar gZ^2(1-Z^2)\mathbf 1\{|Z|\le1\}]=-0.0063$. $\square$

Consequence. On $Q_\delta$, parts (c) and (d) give a fixed weight with $L=20$ whose spike stays above $0.035$ once $d\ge2.2\times10^8$, at both computed values of $\delta$. Part (b) then prices the full observer at $O(d)$ there, while the guarantee for plain PCA needs $T$ of order $d/\delta^2$ (proven, given the two quadrature values). The threshold on $d$ comes from the crude part (c), so the empirical runs carry the claim at $d=200$.

Other regime and the oracle. The estimator runs in $O(Td^2+d^3)$ operations, so it is a polynomial-time witness. The weight depends on the label law, which the attacker knows, and never on $u$. A VAE whose encoder reads $\|v_t\|$ and scales each update's reconstruction term by $g(r_t)$ is a learner of this form (heuristic, no convergence claimed). The statement concerns the procedure and needs no oracle.

### prop-update-direction-fano-recovery: recovering an unknown direction costs the dimension over the per-update Kullback divergence

status: sketch

uses: thm-update-direction-chi-square-bound, def-optimum-update-stream

Statement. Take the setting of part (a) of thm-update-direction-chi-square-bound, without the symmetry of $\nu_a$, and put $\kappa_{\mathrm{KL}}=\mathbb E_a\mathrm{KL}(\nu_a\|\gamma_1)$. Let $u$ be uniform on $S^{d-1}$, and let an estimator $\hat u$ computed from $(a,w_{1:T})$, with coins independent of $u$, satisfy $\Pr[|\langle\hat u,u\rangle|\ge\epsilon]\ge p$. Then
$$T\kappa_{\mathrm{KL}}\ge p\Big(\frac{d\epsilon^2}4-\frac{\log2}2\Big)-\log2.$$
At $p=2/3$ and $\epsilon=1/2$ this reads $T\ge(d/24-0.93)/\kappa_{\mathrm{KL}}$. It binds every observer of the updates, since they are a function of $(a,w)$. For the update stream of part (b) of that theorem,
$$\kappa_{\mathrm{KL}}\le\mathbb E_a\min\{\chi^2(\nu_a\|\gamma_1),K(a)\},\qquad K(a)=\frac12\Big(\frac{b^{-2}\sum_ia_i^2T(a_i)}{\sigma(a)^2}+\log\frac{\sigma(a)^2}{\varsigma^2}\Big).$$
So $\kappa_{\mathrm{KL}}<\infty$ whenever $\varsigma>0$ and the labels are bounded. For $b=1$ and $Y=\langle u,X\rangle\xi$, which is unbounded, $\kappa_{\mathrm{KL}}$ is finite for every $\varsigma>0$, and $\limsup_{\varsigma\to\infty}\varsigma^4\kappa_{\mathrm{KL}}\le39$.

Proof.

Step 1, the cap (proven). For fixed unit $e$, $\langle e,u\rangle^2$ has the law of $\rho^2$ in Step 4 of thm-update-direction-chi-square-bound. Markov's inequality on $e^{d\rho^2/4}$ and that step give $\Pr[|\langle e,u\rangle|\ge\epsilon]\le\sqrt2\,e^{-d\epsilon^2/4}=:q$.

Step 2, Fano (proven). Let $O=(a,w_{1:T})$ and let $F$ be the event $|\langle\hat u,u\rangle|\ge\epsilon$. Under the joint law $F$ has probability $p'\ge p$. Under the product of the marginals of $u$ and $O$, $\hat u$ is independent of $u$, so $F$ has probability $q'\le q$ by Step 1. Data processing gives $\mathrm{kl}(p'\|q')\le I(u;O)$. For $q\le1$, $\mathrm{kl}(p'\|q')\ge p'\log(1/q')-\log2\ge p\log(1/q)-\log2$. For $q>1$ the claim's right side is negative.

Step 3, the information (proven). For every law $Q$, $\mathbb E_u\mathrm{KL}(P_u\|Q)=I(u;O)+\mathrm{KL}(\int P_u\,du\,\|\,Q)$, so $I(u;O)\le\mathbb E_u\mathrm{KL}(P_u\|P_\circ)$. The law of $a$ is the same under both, and given $a$ the likelihood ratio is $\prod_tq_{a_t}(\langle u,w_t\rangle)$. So $\mathrm{KL}(P_u\|P_\circ)=T\,\mathbb E_a\mathrm{KL}(\nu_a\|\gamma_1)=T\kappa_{\mathrm{KL}}$.

Step 4, the bounds on $\kappa_{\mathrm{KL}}$ (proven). $\mathrm{KL}\le\log(1+\chi^2)\le\chi^2$. By part (b) of the theorem, $\nu_a$ is a mixture of $N(m/\sigma,\varsigma^2/\sigma^2)$ over $m=b^{-1}\sum_i\xi_ia_iZ_i$, with $\mathbb E[m^2\mid a]=\sigma^2-\varsigma^2+b^{-2}\sum_ia_i^2T(a_i)$. Convexity of $\mathrm{KL}$ in its first argument and the Gaussian formula give $K(a)$. For $b=1$ and $W=|Z|$, $K(a)=\frac12\big(a^2(a^2-1)/(a^2+\varsigma^2)+\log(1+a^2/\varsigma^2)\big)$, which grows polynomially in $a$, so $\kappa_{\mathrm{KL}}<\infty$. For the limit, split at $A_\varsigma=3\sqrt{\log\varsigma}$. On $a\le A_\varsigma$ use $\chi^2$, whose expansion of part (d) of the theorem holds uniformly there, since $A_\varsigma^2/\varsigma^2\to0$. Its contribution to $\varsigma^4\kappa_{\mathrm{KL}}$ tends to at most $\frac12\mathbb E[a^4(a^2-1)^2]=39$. On $a>A_\varsigma$ use $K(a)\le a^2$ for $\varsigma\ge1$, whose contribution is at most $\varsigma^4\cdot2A_\varsigma\varphi(A_\varsigma)(1+A_\varsigma^{-2})=O(\varsigma^{-1/2}\sqrt{\log\varsigma})$. $\square$

Other regime and the oracle. The bound is statistical and needs no oracle. At $d=800$ and $Y=\langle u,X\rangle\xi$ with large $\varsigma$ it asks for about $0.83\,\varsigma^4$ updates, against the order $200\,\varsigma^4$ of plain PCA. The lost factor of about 240 is the genie's 19.5 times the factor 12 that Fano's $1/24$ loses against $\beta^2/2$. The bracket is non-vacuous at measurable dimensions and wide.

### prop-full-clipping-optimum-filter: full per-example clipping at a median-fitting optimum leaves only the input law and the release

status: sketch

uses: def-optimum-update-stream, thm-bayes-release-loss-matched-price

Statement. Let $f_\theta$ be differentiable in $\theta$, $\psi_\theta(x,y)=(f_\theta(x)-y)\nabla_\theta f_\theta(x)$, and let the fully clipped update be $n_\theta=C\psi_\theta/\|\psi_\theta\|$, with $n_\theta=0$ when $\psi_\theta=0$. This is per-example clipping at norm $C$ when every per-example gradient exceeds $C$.

- (a) $n_\theta(x,y)=C\,\mathrm{sgn}(f_\theta(x)-y)\,\nabla_\theta f_\theta(x)/\|\nabla_\theta f_\theta(x)\|$, and $0$ if either factor vanishes. At fixed $\theta$, the law of any stream of batch means of $n_\theta$ plus independent noise therefore depends on the data law only through the law of $(X,\mathrm{sgn}(f_\theta(X)-Y))$.
- (b) In def-optimum-update-stream with $\Pr[W=0]=0$, at $\theta^*=0$, the clipped stream has one law under every $P_u$ and under $P^\circ$. Every observer of any number of clipped updates has advantage zero.
- (c) Let $f_{\theta^*}(X)$ be a conditional median of $Y$ given $X$ with $\Pr[Y=f_{\theta^*}(X)\mid X]=0$. Then the clipped stream's law at $\theta^*$ is a function of the law of $X$ and of $\theta^*$. A clipped-update observer there learns nothing that the released model and the input law do not determine.
- (d) At any $\theta$, $\Pr[\mathrm{sgn}(f_\theta(X)-Y)=1\mid X]=\Pr[Y<f_\theta(X)\mid X]$. The clipped stream reads the conditional distribution function of the label at the current prediction, one bit per record.

Proof (proven). (a) $\|\psi_\theta\|=|f_\theta(x)-y|\,\|\nabla_\theta f_\theta(x)\|$, and division leaves the sign times the unit gradient. Batch means and noise are functions of i.i.d. copies of $(X,\mathrm{sgn})$ and of independent noise. (b) $\mathrm{sgn}(-Y)=-\xi$, a uniform sign independent of $X$, so $(X,-\xi)$ has one law under $P_u$ and $P^\circ$. (c) The median condition without an atom gives $\Pr[\mathrm{sgn}=1\mid X]=\frac12$, so the sign is uniform and independent of $X$. The gradient at $X$ is a function of $\theta^*$ and $X$. (d) is the definition of the sign. $\square$

Two facts place (c). The population drift of the clipped update is $C\,\mathbb E[(2F(f_\theta(X)\mid X)-1)\nabla f_\theta/\|\nabla f_\theta\|]$, with $F(\cdot\mid X)$ the conditional distribution function, so a median fit is a stationary point of fully clipped SGD (proven). Under conditionally symmetric noise the median is the mean, so (c) holds at the square-loss optimum of thm-bayes-release-loss-matched-price too.

Other regime and the oracle. The filter is exact and statistical, binds every observer, and needs no oracle. It is a mechanism of real training that removes every degree of the channel, where batching only attenuates. When the clipping norm leaves a set of records unclipped, the leak runs through that set (the challenger's estimate $\beta'\approx0.53\,C/\sqrt d$ for $W=|Z|$, heuristic). Clipping is part of the procedure as given, so no reading of ruling 2 is used.

### conj-update-linear-class-price: the price of linearity in the update stream is set by the mean spike and the variance profile

status: open

uses: def-optimum-update-stream, def-statistic-learner-class, thm-norm-weighted-update-pca, prop-update-direction-fano-recovery

Setting. def-optimum-update-stream at $b=1$ with $|Y|\le A$. The linear class $\mathcal A_{\hat M}$ reads $\hat M$, and the full observer reads everything. Its invariants are the mean spike $\beta=c_2/(\mu_2+\varsigma^2)$ and the profile spike $s$ of (iii). The full observer's price $p_*$ for overlap $1/2$ is bracketed (proven) between $(d/24-0.93)/\kappa_{\mathrm{KL}}$ and the bound of thm-norm-weighted-update-pca (b) at the best weight.

Conjecture. Fix the law and let $d\to\infty$.

- (a) If $s<1$, then $p_{\hat M}$ is of order $d/\beta^2$ for every fixed overlap, and it is infinite when $c_2=0$.
- (b) If $s>1$, then the top or the bottom eigenvector of $\hat M$ reaches an overlap $\epsilon_0(s)>0$ for every large enough $T/d$, also when $c_2=0$. So $p_{\hat M}=O(d)$ for overlaps below $\epsilon_0(s)$.
- (c) At $s<1$ and large noise, $p_{\hat M}/p_*$ is of order $1+\mathrm{Var}(W^2T(W))/c_2^2$, the challenger's Jensen ratio.
- (d) At batch $b$ the profile spike and the weighted gain fall as $b$ grows, so $p_{\hat M}/p_*\to1$. Batching makes the linear attacker optimal.

Heuristic grounds. For (a) the spiked covariance transition, from memory. For (b), when $T\gg d$ the fluctuation $\hat M-(\mu_2+\varsigma^2)I_d$ resembles a Wigner matrix whose row along $u$ has variance $1+s$ times the rest. That is $DGD$ with $D^2=I+suu^\top$, whose spectrum is that of $G+sGuu^\top$. With $m$ the semicircle Stieltjes transform, an outlier solves $s(\lambda m(\lambda)-1)=1$, and $\lambda m(\lambda)-1$ falls from 1 at the edge to 0, so an outlier exists if and only if $s>1$. Its overlap does not depend on $T$ (heuristic, a Gaussian approximation of the fluctuation). (c) is the computation of the challenger's section 2.2, and (d) is the central limit theorem for the batch mean.

Empirical support. The zero-spike laws put $W=1$ on $|Z|>t$, $W=w_t$ on $|Z|<1$ and $W=0$ elsewhere, with $w_t^2=2t\varphi(t)/\mathbb E[(1-Z^2)\mathbf 1\{|Z|<1\}]$, so that $c_2=0$. At $\varsigma=0$, $d=200$ and 4 seeds, the larger of the top and bottom overlaps of PCA at $T=50d$ and $200d$ is 0.11 and 0.11 at $s=0.20$, 0.26 and 0.17 at $s=0.66$, 0.55 and 0.50 at $s=1.67$, 0.62 and 0.65 at $s=3.07$, and 0.77 and 0.67 at $s=5.25$. A random direction gives 0.07. The overlap does not grow with $T$, as (b) predicts. On $Q_0$, $s=-0.105$, PCA stays at or below 0.09, and the weighted estimator reaches 0.86 to 0.88 at $T=40d$.

What settles it. (a) needs a lower bound on the law of $\hat M$, whose fluctuation is non-Gaussian (open). (b) needs an outlier theorem for sample covariances of this scale-mixture family (open). (c) needs the bracket on $p_*$ closed, $\kappa_{\mathrm{KL}}$ against the best weighted spike (open). Regime: a statistic class against the full statistical observer, both polynomial time. The gap is between classes, not between statistics and computation.

Experiment. At $b=1$, the zero-spike family above, $Q_\delta$ and $W=|Z|\mathbf 1\{|Z|\le4\}$, $d\in\{200,400,800\}$ and $T/d\in\{10,40,160\}$. Record the overlap of a linear VAE fitted to the updates, of plain PCA, and of the weighted estimator, and compare $\epsilon_0(s)$ across $d$. A drift of $\epsilon_0$ with $d$ at fixed $s$ refutes (b).

Other regime and the oracle. This answers G1 in Halil's sense of a subclass. The class is defined by a statistic, the learner is its certified witness, and the price of the class differs from the statistical one by a ratio that is measurable at $d=200$. It needs no oracle. It does not yet compare the attacker with the trainer, which ch-no-trainer-price leaves for round 02.
