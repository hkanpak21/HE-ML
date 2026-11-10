---
model: claude-fable-5-1
discussant: learning-attacker-class
date: 2026-10-30
round: 04
---

# The learning attacker class, round 04, towards the idea

The verdict first. Halil's idea has worked when a declared gradient attacker, at batch one and fine precision with no injected noise, has a proven price in observations that exceeds every observer's price by a power of the dimension, on a channel real training produces, with a measured side meeting the proven side within a stated factor. No tool of the final statement reaches that attacker, by clause 8, and the one exponent gap the theory knows between a gradient learner and every observer is an information-exponent gap, which rests on vanishing low moments and is the knife edge the council rejected. What the tools reach now is the idea in constants, a bound on a linear attacker's success within a factor $1+\mathrm{Var}(W^2T(W))/c_2^2$ of every observer on a generic law, and the one claim about a mechanism of real training that plants nothing. Batching removes the attacker's class from the price. Section 3 states it as the theorem to prove and section 4 gives the experiment that would refute it. Items refer to `readings/2026-10-29-what-we-have.md`, clauses to `statement/final.md`.

## 1. What would count as the idea having worked

Halil's idea, in his words, is a bound on the success of a VAE or anything, given the setting, regarding the flow of information, measured in computational terms, with hardness arriving afterwards and never borrowed from a planted problem (`2026-10-27-what-you-want.md`, section 1). In `halil-ideas.md` it is a learning-constrained attacker meeting a bound sharper than the geometric one (item 1), an oracle that counts the attacker's runs, seeds and datasets (item 7), hardness that training itself creates (item 9), a price stated as a capacity relative to the target (item 11), and the class practitioners run, a linear readout of the representation (item 12). Under the final statement the idea is one theorem.

### thm-natural-attacker-price: the target
status: open
uses: def-learning-attacker, def-uniform-security-profile, clause 8, clause 13

Statement. There exist a declared trainer on a stated record law and task with no structure placed for the purpose, a channel that its training produces, the seed-blind representation stream or the update stream, a secret functional, and the attacker class $\mathcal L_0$ of batch-one gradient learners at fine precision without injected noise on a declared family, such that four things hold. (a) Every estimator reaches success $s$ at every frame from $n_*(d)=\Theta(d^{e_*})$ observations, and the exponent $e_*$ is proven for the law. (b) Every member of $\mathcal L_0$ needs $n_{\mathcal L}(d)\ge c\,d^{e_{\mathcal L}}$ observations with $e_{\mathcal L}>e_*$, and the proof binds $\mathcal L_0$ through its dynamics and not through what it reads. (c) A declared member of $\mathcal L_0$ reaches $s$ on the oracle at a measured $n_{\mathrm{hi}}(d)\le C\,n_{\mathcal L}(d)$ at three dimensions, with $C$ stated. (d) The gap $e_{\mathcal L}-e_*$ is attributed to a named mechanism of training.

Part (a) the theory has, by Fano and the second-moment method (items 29 to 31, proven). Part (c) the oracle supplies for any declared member, by clause 21 (proven). Part (b) is the core of clause 18, and nothing in the statement reaches it. Part (d) is where the planting rule bites. The only exponent gap known between a gradient learner and every observer is the gap between the information exponent $l$ of the regression function and the generative exponent $k^*$ of the label law, with online SGD on one neuron paying $d^{l-1}$ for $l\ge3$ (Ben Arous, Gheissari and Jagannath, JMLR 2021, from memory, unverified, not in the library) while every observer pays $d^{k^*/2}\le d$ for a deterministic link, since the transform $Y\mapsto Y^2$ gives degree two (proven, DPLB24 Proposition 2.6 and Example 2.7). But $l\ge3$ means the regression function has no degree-one and no degree-two Hermite component, which is the moment balance the council named a plant in item 25 unless training itself produces it. So the idea has worked in exponents when a training-produced regression function with $l\ge3$ is exhibited, or a mechanism other than the information exponent is found, and both are open.

The idea in constants the theory already holds. On a generic law of `def-optimum-update-stream` at batch one, the price of the linear attacker, PCA or a linear VAE, exceeds the price of every observer by the factor $1+\mathrm{Var}(W^2T(W))/c_2^2$, which is $19.5$ for $Y=\langle u,X\rangle\xi$ at large noise (proven in the proportional limit, the debate critique, pending the search on spectral initialization). This is a bound on a VAE's success given the setting, in units of updates observed, with the attacker's class entering the constant and nothing planted. It is Halil's sentence without hardness, and hardness cannot arrive from a constant.

## 2. What the tools reach now, and what blocks the rest

Reached.

- Every-observer prices on channels real training produces, exact in exponent and bracketed in constants, items 11, 15 and 29 to 31 (proven, with the bracket of 86 empirical).
- The statistic class, PCA and the linear VAE, priced by the outlier equation of item 32, with its finite identities proven, two deterministic equivalents heuristic, and the separation from every observer infinite on the knife edge $c_2=0$ and a constant on generic laws (proven in the limit, pending the search).
- The noisy gradient attacker priced in steps through its update class, clause 13, at degrees one to three with exact Haar eigenvalues (proven), above three in order (heuristic). Its class enters through the injected noise and the update norm, and it plants nothing at degrees one and two.
- The attacker that is a trainer, clause 12, exact in the Gaussian linear model and for correlational classes (proven), which is the one place where a lower bound for the trainer's class transfers to the attacker.
- Capacity as a coordinate, clause 3, with the parameter count lowering the noisy attacker's price by at most its own factor (proven given clause 13).

Blocked.

- The natural attacker. Fine-precision SGD on an engineered network simulates every PAC learner (proven, Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, Theorem 1a), so no access handle binds it, and its own sampling noise carries a second-degree channel that the update class misses (heuristic, the council's reading of the batch covariance), so the noise handle needs injected noise it does not supply. Clause 8 says this and section 1 restates it as the missing part (b).
- The dynamics tool. The only bounds on batch-one SGD as such are direct analyses of its trajectory on Gaussian single-index targets, with one neuron and a known link (from memory, unverified, none in the library). They bind one architecture on one law, and the library holds none of them read.
- The planting rule. Every exponent gap that sees a learner's class comes from vanishing low moments of a regression function or a label law along a hidden direction (proven for every instance in the register, items 25, 27, 32). On generic laws the class enters the price in constants only (proven in the limit for the linear class, heuristic beyond).
- Real data. No law is stated, so part (a) has no proof there and only the measured side exists, except for bounds uniform over every learning function (proven, clause 21).
- Hardness against every efficient learner. On a samplable law it is a one-way function (proven under the hypothesis, Hirahara and Nanashima, ECCC TR23-100, Theorem 2.4, as registered), which `CONTEXT.md` would count and nobody has exhibited (open).

The shape of what remains is this. The class of the attacker enters a price through what it reads, and on a generic law what a linear attacker reads differs from what every observer reads by a constant that is the non-Gaussian part of the update. A mechanism of training that Gaussianizes the update removes the class from the price, and a mechanism that keeps the update non-Gaussian at small batch keeps it. Batching is the first mechanism, and the statement below prices it.

## 3. One statement to prove

### thm-batching-removes-the-class: batching makes the linear attacker optimal
status: sketch
uses: def-optimum-update-stream, def-statistic-learner-class, thm-norm-weighted-update-pca, prop-update-direction-fano-recovery, conj-linear-class-reads-cauchy-transform, def-learning-attacker

Setting. The update stream of `def-optimum-update-stream` with inputs $X\sim\gamma_d$, labels $Y=\xi W$, $W=W(\langle u,X\rangle)\in[0,A]$, $\mu_2=\mathbb EW^2$ and $c_2=\mathbb E[W^2(Z^2-1)]\neq0$, so the law is generic and nothing is balanced. Each client adds per-example noise of variance $\sigma_0^2$ and averages a batch of $b$, so its update is $v=b^{-1}\sum_{i\le b}(Y_iX_i+\sigma_0\zeta_i)$ with covariance $\alpha_bI_d+\gamma_buu^\top$, $\alpha_b=(\mu_2+\sigma_0^2)/b$, $\gamma_b=c_2/b$, and spike-to-bulk ratio $\beta=c_2/(\mu_2+\sigma_0^2)$, which does not depend on $b$. The attacker observes $T$ updates from one run. Two classes. $\mathcal L_{\mathrm{lin}}$ is the declared learner with family the unit sphere, the square reconstruction loss of a linear autoencoder trained to its optimum, and readout its loading, which is the top eigenvector of the sample covariance of the $T$ updates, the linear VAE of item 32. $\mathcal A_*$ is every estimator. The price $p_{\mathcal C}(b,d)$ of a class is the least $T$ at which some member reaches overlap $\frac12$ with $u$ at every $u$ with probability $\frac23$.

Statement.

(a) For every fixed $d$, $p_{\mathrm{lin}}(b,d)/p_*(b,d)\to r(d)$ as $b\to\infty$, where $r(d)$ is the same ratio for the Gaussian spiked covariance model with spike $\beta$ in dimension $d$, and $r(d)\to1$ as $d\to\infty$.

(b) At finite $b$ the per-update chi-square of every observer along $u$ exceeds that of the Gaussian surrogate by the factor $1+\mathrm{Var}(W^2T(W))/(b\,c_2^2)+O(b^{-2})$, where $T(w)=\mathbb E[Z^2-1\mid W=w]$, and the threshold of $\mathcal L_{\mathrm{lin}}$ exceeds the spiked threshold $d/\beta^2$ by a factor $1+O\big(\mathrm{Var}(W^2)/(b(\mu_2+\sigma_0^2)^2)\big)$.

(c) Hence the class of the attacker enters the price only through the non-Gaussian part of the update, which is of order $1/b$, and at every batch the price of the linear attacker is $d/\beta^2$ within a factor that tends to one.

Plan of the proof.

1. Conditional structure (proven, by construction). Given the batch's magnitudes $(W_i)$ and signs, the component of $v$ orthogonal to $u$ is Gaussian with variance $\sigma_b^2=b^{-2}\sum_iW_i^2+\sigma_0^2/b$ in every direction, and the component along $u$ is $b^{-1}\sum_i\xi_iW_iZ_i$ plus independent noise. So $v$ is a scale mixture of Gaussians in $u^\perp$ and carries the frame only through its along-$u$ law and its scale.

2. Gaussianization (heuristic, the step expected to fail). As $b\to\infty$ at fixed $d$, $\sigma_b^2\to\alpha_b$ by the law of large numbers with fluctuation $\mathrm{Var}(W^2)/b^3$, and the along-$u$ component tends to $N(0,\alpha_b+\gamma_b)$ by the central limit theorem, with fourth cumulant $\kappa_4(\xi WZ)/b^3$. Normalized by $\alpha_b^2$ the cumulant is $O(1/b)$, so the per-update chi-square between the true law and its Gaussian surrogate is $O(1/b^2)$. Over the $T\asymp d/\beta^2$ updates the price needs, the compounded error is $O(d/b^2)$, which vanishes at fixed $d$ and needs $b\gg\sqrt d$ when $d$ grows with $b$.

3. The Gaussian limit (borrowed, from memory, unverified, needs the search gate). For the spiked covariance model with a spherical prior and spike $\beta\le1$, weak recovery is possible for every estimator exactly above the spectral threshold $T=d/\beta^2$ in the proportional limit, so $p_*=p_{\mathrm{lin}}(1+o(1))$ there (Perry, Wein, Bandeira and Moitra, Annals of Statistics 2018, and Onatski, Moreira and Hallin, Annals of Statistics 2013). This gives $r(d)\to1$.

4. The linear attacker at finite $b$ (heuristic, the outlier equation). The sample covariance of a scale mixture obeys the outlier equation of `conj-linear-class-reads-cauchy-transform`, whose deviation from the spiked threshold is governed by the variance of the scale, $\mathrm{Var}(W^2)/b^3$ against $\alpha_b^2$, which is the $O(1/b)$ factor of (b).

5. Every observer at finite $b$ (heuristic, the genie's norm). The full observer reads $b^{-1}\sum_iW_i^2$ from $\|v\|^2/d$ at relative precision $O(d^{-1/2})$, and the along-$u$ variance conditional on it fluctuates by $\mathrm{Var}(W^2T(W))/b^3$ around its mean $c_2/b^2$. The chi-square gain from the fluctuation against the chi-square of the mean spike is $\mathrm{Var}(W^2T(W))/(b\,c_2^2)$, which is the factor of (b) and reduces to the debate's $1+\mathrm{Var}(W^2T(W))/c_2^2$ at $b=1$ (proven there in the limit).

6. Assembly (proven given 2 to 5). Both prices tend to $d/\beta^2$ times $r(d)$ as $b\to\infty$ at fixed $d$, and (c) follows from (b).

The step expected to fail first is step 2, the order of the limits. The Gaussian approximation is per update, the price is a product over $T\asymp d$ updates, and the compounded chi-square error $O(d/b^2)$ is small only for $b\gg\sqrt d$. If the proportional regime $d\to\infty$ at fixed $b$ is wanted, the statement must be weakened to a ratio bounded by $1+C/b$ with $C$ depending on the law and not on $d$, which step 5 supports and step 4 does not yet.

What the theorem says for the idea. It is a theorem about a mechanism of real training, the batch, and it plants nothing. It says that the attacker's class enters the price only through the non-Gaussian part of the update, and that batching removes it, so Halil's class-sensitive bound can live only at small batch on labels whose magnitudes are far from constant. It answers item 12 in one case, the stitching attacker is near optimal on batched generic updates, and item 11 in one case, the capacity that matters is one nonlinear weight on the norm and not the parameter count. It is also a bound, not a hardness result, as section 1 says.

Regime. The statement is statistical. In the computational regime it says that at degree two the efficient and the statistical prices coincide, so no hardness lives on this channel at any batch (proven, DPLB24 at $k^*=2$). Without the oracle the updates are real client updates and the experiment is unchanged.

## 4. One experiment the learning oracle can run

What it measures. The least number $T$ of client updates at which the linear attacker, and separately the norm-weighted spectral estimator of item 30 as the attainable side of every observer, reach overlap $\frac12$ with the secret direction in at least 27 of 40 runs, as a function of the batch $b$, and the ratio of the two.

Declared parameters. Inputs $X\sim\gamma_d$ with $d\in\{200,400\}$. Labels $Y=\xi W$ with $W=\min(|Z|,4)$, the debate's generic law, whose $c_2$, $\mu_2$ and $\mathrm{Var}(W^2T(W))$ are computed by quadrature before the runs and recorded. Per-example noise $\sigma_0^2=\mu_2$, so $\beta=c_2/(2\mu_2)$ at every batch. Batches $b\in\{1,4,16,64\}$. The secret $u$ is drawn uniformly on the sphere per run by the oracle's seed, and each $\mathsf{Train}$ call returns one client update at the optimum $\theta^*=0$, so $T$ is the count of $\mathsf{Train}$ calls, which is the unit of item 7. Forty runs per cell, with a grid of $T$ from $d/4$ to $64d$ in factors of $\sqrt2$.

The attacker it runs. The linear attacker of $\mathcal L_{\mathrm{lin}}$, the top eigenvector of the sample covariance of the $T$ updates, read out as the direction estimate. Beside it the norm-weighted estimator with the signed weight of `prop-signed-weight-update-pca`, computed from the recorded law. Both are declared before the runs, and neither is tuned on them.

The outcome that would refute the statement. The statement predicts that the ratio of the two least $T$ falls with $b$ toward one, within $1+2\,\mathrm{Var}(W^2T(W))/(b\,c_2^2)$ at every $b$, and that it does not grow with $d$ at fixed $b$. A ratio that stays above $1+2\,\mathrm{Var}(W^2T(W))/(b\,c_2^2)$ at $b=64$ at both dimensions refutes part (b) and with it (c). A ratio that is larger at $d=400$ than at $d=200$ at $b=64$ by more than the binomial band of 40 runs refutes the uniformity that the proportional form of (a) needs, which is the failure step 2 predicts, and leaves the fixed-$d$ limit standing. A linear attacker that reaches overlap $\frac12$ below $d/(2\beta^2)$ at $b=64$ refutes the spiked threshold as the price of the class and sends the outlier equation back to the debate.
