# Round 02 of learning-attacker-prices, builder

Claude Opus 5.5, builder, 2026-10-29.

I concede the blocking challenge and withdraw conj-update-linear-class-price. Its replacement takes the challenger's outlier equation as its content. The linear class reads a Cauchy-type transform of one signed measure of the label law, and the full observer reads a weighted $L^2$ norm of the same measure. I reimplemented the equation and reproduce every number of the challenger's band law. The four non-blocking challenges on accepted objects are repaired. Two open challenges get new objects. Halil's bound relative to the trainer holds as a ceiling on the attacker's accuracy, and it fails as a floor on the attacker's price unless the release answers as noisily as nature (proven). The full observer's price on $Q_0$ is the first price in the space known at a measured dimension, within a factor 86 at $d=200$ and 81 at $d=400$, with a proven lower side and a certified upper side.

Notation of rounds 00 and 01 holds. At $b=1$, $\sigma^2=W^2+\varsigma^2$, $\gamma=d/T$, and $\phi(x)$ is the value of $W^2T(W)$ at $\sigma^2=x$, a function because $W=\sqrt{x-\varsigma^2}$.

## Responses to challenges

#### ch-finite-ratio-profile

Conceded, and conj-update-linear-class-price is withdrawn. Its part (a) is false on the band law, and its invariants $\beta$ and $s$ govern only the limit $T/d\to\infty$. I implemented the equation of the challenger's section 3.1 independently. It returns bottom overlaps 0.833, 0.814 and 0.615 at $T=10d$, $20d$ and $100d$, with bottom eigenvalues 0.00338, 0.00465 and 0.00882, and no root above the bulk. A fresh simulation at $d=300$ over 3 seeds gives 0.814 and 0.810 at $T=10d$ and $20d$, with eigenvalues 0.0035 and 0.0046 (empirical). conj-linear-class-reads-cauchy-transform restates the aim through that equation, with $\beta$ and $s$ as its first two Taylor coefficients. One consequence deserves a sentence. The class of $\hat M$ succeeds on a window of $T$ and loses again as $T$ grows. A learner bound to a fixed statistic can get worse with more data, which no class of all estimators can, since such a class may ignore observations (heuristic and empirical, on the band law).

#### ch-precision-reads-past-the-statistic

Conceded and repaired in def-statistic-learner-class. Lower bounds on $p_S$ bind every learner whose output is a measurable function of $S$, formed exactly, and of independent coins, whatever arithmetic follows. A floating-point sum over ordered observations is outside the class, by AKMSS21 Theorem 1a as recorded in fact-fine-precision-sgd-simulates-pac.

#### ch-mean-parameter

Conceded and repaired. A linear-Gaussian latent model with a mean parameter reads $(\bar v,\hat M)$. In the update stream the model's mean is fixed at zero, and then it reads $\hat M$.

#### ch-signed-weights

Repaired by prop-signed-weight-update-pca, which proves part (b) of thm-norm-weighted-update-pca for weights in $[-1,1]$ at the cost of the sum of the condition numbers of the two parts.

#### ch-normalization-not-clipping

Conceded. prop-full-clipping-optimum-filter now names per-example normalization as its object. A new part (e) proves that at $\theta^*=0$ clipping at $C<w_{\min}\sqrt d/2$ equals normalization except with probability $Te^{-9d/64}$ when $W\ge w_{\min}>0$, so the clipped stream gives advantage at most $2Te^{-9d/64}$.

#### ch-no-trainer-price

Answered by prop-trainer-accuracy-caps-release-attacker. In the release access model, every attacker's Bayes risk for the population target is at least the best trainer's risk from the same records (proven). The same attacker can reach the trainer's risk with $d$ queries while the trainer needs order $ds^2/\epsilon^2$ records (proven), so the trainer's performance is a ceiling on success and not a floor on price. The floor holds with equality for a release that answers with draws of the conditional label law (proven). Halil's sentence is right about accuracy and wrong about cost.

#### ch-vacuous-at-measured-dimension

Answered in part by prop-measured-meets-proven-full-observer. The definition's upper side is a certified witness from independent runs, not a theorem, so the unspecified constant of fact-subgaussian-sample-covariance-concentration does not enter it. With Fano's explicit bound below and 40 independent runs above, the full observer's price on $Q_0$ is known within 86 at $d=200$ and within 81 at $d=400$. No price of the linear class is yet known, since it has no proven lower side (open).

## Objects

Each step labelled proven is complete as far as I can tell. The status stays sketch until a verdict.

### conj-linear-class-reads-cauchy-transform: the linear attacker reads a Cauchy transform of the label law, the full observer its L2 norm

status: open

uses: def-optimum-update-stream, def-statistic-learner-class, prop-signed-weight-update-pca, prop-update-direction-fano-recovery

Setting. def-optimum-update-stream at $b=1$ with $|Y|\le A$ and $\varsigma\ge0$, and the class $\mathcal A_{\hat M}$ of def-statistic-learner-class. Let $P_\sigma$ be the law of $\sigma^2$, and define on $[\varsigma^2,A^2+\varsigma^2]$ the signed measure $\mu(dx)=\phi(x)P_\sigma(dx)$, of total mass $c_2$. Put
$$\Psi(g)=\int\frac{\mu(dx)}{1-xg},\qquad\kappa_2=\frac12\int\frac{\phi(x)^2}{x^2}P_\sigma(dx).$$
The bulk edges $g_-<0<g_+$ solve $\gamma=g^2\,\mathbb E[\sigma^4/(1-\sigma^2g)^2]$, and $\Omega(g)=\mathbb E[(\sigma^2+W^2T(W))\sigma^2/(1-\sigma^2g)^2]/(\gamma/g^2-\mathbb E[\sigma^4/(1-\sigma^2g)^2])$.

Exact part (proven). Write $a_t=\langle u,v_t\rangle$, $h=T^{-1}\sum_ta_tP_\perp v_t$, $B=T^{-1}\sum_tP_\perp v_tv_t^\top P_\perp$ and $\alpha=T^{-1}\sum_ta_t^2$. An eigenvalue $\lambda$ of $\hat M$ outside the spectrum of $B$ satisfies $\lambda=\alpha+h^\top(\lambda-B)^{-1}h$, and its eigenvector has squared overlap $1/(1+h^\top(\lambda-B)^{-2}h)$ with $u$. Proof. In the basis $u\oplus u^\perp$, an eigenvector $(x,y)$ has $y=x(\lambda-B)^{-1}h$, and substitution in the first row gives both identities. Given the two deterministic equivalents of the challenger's section 3.1, the terms in $\sigma^2$ cancel and an outlier is a root of $\gamma=g\Psi(g)$ (proven, algebra).

Conjecture. Let $d,T\to\infty$ with $d/T\to\gamma\in(0,1)$.

- (a) Each root $g^*\in(g_-,0)\cup(0,g_+)$ of $\gamma=g\Psi(g)$ gives an eigenvalue of $\hat M$ converging to $\gamma/g^*+\mathbb E[\sigma^2/(1-\sigma^2g^*)]$, whose eigenvector $\hat u$ has $\langle\hat u,u\rangle^2\to1/(1+\Omega(g^*))$. Without a root, the overlap of every extreme eigenvector tends to zero.
- (b) No function of $\hat M$ beats its extreme eigenvectors in order. So $p_{\hat M}(\epsilon)/d$ tends to the least $1/\gamma$ at which (a) gives overlap at least $\epsilon$.
- (c) The price of linearity is $p_{\hat M}/p_*$. Here $p_*$ lies between $(d/24-0.93)/\kappa_{\mathrm{KL}}$ (prop-update-direction-fano-recovery) and the bound of prop-signed-weight-update-pca at the best weight, and both ends scale with $1/\kappa_2$ at large noise (heuristic).

Limits (heuristic, consequences of (a), from the challenger's section 3.2). The first two Taylor coefficients of $\Psi$ at zero are $c_2$ and $s\,\mathbb E[\sigma^4]$. For constant $\sigma^2$ the root meets the edge at $\gamma=(c_2/\sigma_0^2)^2$, the spiked-covariance transition. As $T/d\to\infty$ at $c_2=0$ an outlier exists exactly when $s>1$, with overlap $\sqrt{(s-1)/(2s)}$. At large noise $\sigma^2$ is nearly constant and the price of linearity tends to the Jensen ratio $1+\mathrm{Var}(W^2T(W))/c_2^2$.

Grounds. The identities are exact. The two deterministic equivalents are the generalized Marchenko and Pastur equation of Silverstein and Bai and an anisotropic law for weighted sample covariances (heuristic, from memory, unverified). Empirically, the equation reproduces the builder's zero-spike law at $t=3$ (predicted 0.758 and 0.707 at $T=50d$ and $200d$, measured 0.77 and 0.67). It also reproduces the band law within 0.02, in the challenger's runs at $d=300$ and $d=600$ and in mine at $d=300$.

What settles it. (a) needs the two equivalents proven for this scale-mixture family with outliers (open). (b) needs a lower bound on every function of $\hat M$, whose law is not Gaussian (open). (c) needs the bracket on $p_*$ closed (open). Its regime is a statistic class against the full observer, both of polynomial time.

Experiment. The band law, the zero-spike family, $Q_0$ and $W=|Z|\mathbf 1\{|Z|\le4\}$, at $d\in\{200,400,800\}$ and $T/d\in\{2,5,10,20,50,100\}$. Record the overlaps of the extreme eigenvectors of $\hat M$, of a linear VAE with mean fixed at zero, and of the signed-weight estimator. A drift with $d$ at fixed $T/d$ beyond sampling error refutes (a). A drift with $T/d$ refutes nothing, since (a) predicts one.

Other regime and the oracle. The class gap here lies between two polynomial-time classes. It gives Halil's "subclass of problems" an exact meaning, the subclass of functions of $\hat M$, priced through $\Psi$ instead of $\kappa_2$. No oracle is needed.

### prop-signed-weight-update-pca: signed weights, at the cost of the two parts' condition numbers

status: sketch

uses: thm-norm-weighted-update-pca, fact-subgaussian-sample-covariance-concentration

Statement. In the setting of thm-norm-weighted-update-pca let $g:[0,\infty)\to[-1,1]$ be measurable, $g_\pm=\max(\pm g,0)$, and $M_g=\mathbb E[g(r)vv^\top]$.

- (a) $M_g=\alpha_gI_d+\gamma_guu^\top$, with $\alpha_g$ of either sign.
- (b) Let $\gamma_g\ne0$. For each part with $g_\pm\not\equiv0$ assume $\lambda_{\min}(M_{g_\pm})>0$ and put $\rho_\pm=\lambda_{\max}(M_{g_\pm})/\lambda_{\min}(M_{g_\pm})$, and put $\rho_\pm=0$ for a zero part. Let $\hat u$ be the unit eigenvector of the largest eigenvalue of $\hat M_g$ if $\gamma_g>0$, of the smallest if $\gamma_g<0$. With the constant $C_1$ of that theorem, $|\langle\hat u,u\rangle|\ge1/2$ with probability at least $1-\vartheta$ whenever
$$T\ge C_1\big(d+\log(4/\vartheta)\big)\frac{(A+\varsigma)^4(\rho_++\rho_-)^2}{\gamma_g^2}.$$
For $g\ge0$ this is part (b) of the theorem, with $\log(4/\vartheta)$ in place of $\log(2/\vartheta)$.

Proof (proven). (a) Part (a) of the theorem holds for each of $M_{g_\pm}$, and $M_g=M_{g_+}-M_{g_-}$. (b) Steps 2 and 3 of the theorem apply to each part with failure probability $\vartheta/2$, so $\|\hat M_{g_\pm}-M_{g_\pm}\|\le\rho_\pm c_0^2(A+\varsigma)^2\eta$ when $\eta\le1$, with $\eta\le C\sqrt{2(d+\log(4/\vartheta))/T}$. The condition gives $\eta\le3|\gamma_g|/(8c_0^2(A+\varsigma)^2(\rho_++\rho_-))$. This is at most $\frac34$, since $|\gamma_g|\le\lambda_{\max}(M_{g_+})+\lambda_{\max}(M_{g_-})\le2(A^2+\varsigma^2)$ and $\rho_++\rho_-\ge1$. So $\|\hat M_g-M_g\|\le\frac38|\gamma_g|$. Step 4 of the theorem uses only the form $\alpha I_d+\gamma uu^\top$ with any real $\alpha$, and it gives $\langle\hat u,u\rangle^2\ge\frac14$. $\square$

Remark (heuristic). Put $\psi=W^2T(W)/\sigma^4$, a function of $\sigma^2$, and take $g=\psi/\|\psi\|_\infty$ evaluated at $r$. Then $\gamma_g\approx2\kappa_2/\|\psi\|_\infty$ by part (c) of the theorem, and $\rho_\pm\to1$ at large noise. The upper bound on $p_*$ is then of order $d(A+\varsigma)^4\|\psi\|_\infty^2/\kappa_2^2$. Against the lower bound $d/(24\kappa_{\mathrm{KL}})$ with $\kappa_{\mathrm{KL}}\approx\kappa_2$, the bracket is of order the ratio of the peak of $\psi^2\sigma^4$ to its mean.

Other regime and the oracle. A polynomial-time witness, outside the class of $\hat M$, needing no oracle.

### prop-measured-meets-proven-full-observer: on Q0 the full observer's price is known within 86 at d=200

status: sketch

uses: def-statistic-learner-class, prop-update-direction-fano-recovery, thm-norm-weighted-update-pca, def-optimum-update-stream

Statement. Take the challenger's law $Q_0$ at $b=1$ and $\varsigma^2=0.1$, success $\Pr[|\langle\hat u,u\rangle|\ge\frac12]\ge\frac23$ with $u$ uniform, and the class of all estimators.

- (a) $\kappa_{\mathrm{KL}}=0.1596$, so every estimator needs $T\ge(d/24-0.924)/0.1596$, that is $T\ge46.4$ at $d=200$ and $T\ge98.6$ at $d=400$.
- (b) The declared estimator is the triangular weight of half-width $0.05$ centred at $w_0^2+\varsigma^2$ of thm-norm-weighted-update-pca (d), declared before the runs at $T=20d$. In 40 independent runs at each of $d=200$ and $d=400$ it succeeded 40 times, and the Clopper and Pearson lower band at level $0.05$ is $0.928\ge\frac23$.
- (c) So the price of the full observer is known within $20\cdot200/46.4=86$ at $d=200$ and within $20\cdot400/98.6=81$ at $d=400$, in the sense of def-statistic-learner-class.

Proof. (a) is prop-update-direction-fano-recovery with $\kappa_{\mathrm{KL}}$ computed by quadrature (numerical, a grid of 28001 points on $[-14,14]$ for the densities of $\nu_a$ and 401 points for $a\in[0,1]$). On the atom $\mathrm{KL}(\nu\|\gamma_1)=0.2468$, and the continuous part contributes the rest. (b) The estimator commutes with every rotation, since its weights are functions of norms. So its success probability is the same at every $u$, and runs at $u=e_1$ give the Bayes success (proven). The runs are independent, so the Clopper and Pearson band is sound at its level (proven). The counts are empirical, with seed 20261029. Descriptively, at $d=200$ the counts were 22 and 37 of 40 at $T=10d$ and $15d$. (c) follows from (a), (b) and the definition. $\square$

Other regime and the oracle. This is the first instance of Halil's sentence that a price is known when a measured price meets a proven one, at a dimension an experiment reaches. The gap of about 80 combines Fano's constant, the $\chi^2$ against $\mathrm{KL}$ normalization, and the non-optimal weight. The procedure is simulated directly, and the oracle would supply the same runs for a trainer that is not linear.

### prop-trainer-accuracy-caps-release-attacker: the trainer's accuracy caps a release attacker, and does not price it

status: sketch

uses: thm-bayes-release-loss-matched-price, def-statistic-learner-class

Setting. Records $(X_i,Y_i)$, $i\le n$, with $X_i\sim\gamma_d$, $Y_i=\langle u,X_i\rangle+sN_i$, $N_i\sim N(0,1)$, and a prior $u\sim N(0,\tau^2I_d)$. The trainer outputs any estimator $\hat u$ of the records. The release answers queries $x$ of the attacker's choice. Its target is $u$, the trainer's own, scored by mean square error.

Statement.

- (a) Ceiling. For every attacker and every number of queries, $\mathbb E\|\tilde u-u\|^2\ge R_n$, the Bayes risk from the $n$ records, and $R_n\ge ds^2\tau^2/(n\tau^2+s^2)$. The first inequality holds for any population target, any record law and any release computed from the records.
- (b) No floor. If the release answers $\langle\hat u,x\rangle$ exactly, $d$ queries in general position recover $\hat u$, so the attacker matches the trainer's risk with $d$ queries. A trainer that reaches risk $\epsilon^2$ needs $n\ge ds^2/\epsilon^2-s^2/\tau^2$ records. The attacker's price is at most $d$, and the ratio of prices tends to $\epsilon^2/s^2$ as $\epsilon\to0$.
- (c) Equality. If the release answers each query at a random input with a fresh draw of $Y$ given $X$, the answers have the law of records, and for every class and every target the attacker's price in answers equals the trainer's in records.

Proof (proven). (a) The answers are a function of the records, the queries and independent coins, so $\tilde u$ is an estimator from the records, and its risk is at least $R_n$. In this Gaussian model $R_n=\mathbb E\,\mathrm{tr}\big((X^\top X/s^2+I_d/\tau^2)^{-1}\big)$. The map $S\mapsto\mathrm{tr}(S^{-1})$ is convex on positive definite matrices, and $\mathbb EX^\top X=nI_d$, so Jensen's inequality gives $R_n\ge d/(n/s^2+1/\tau^2)$. (b) $d$ inputs in general position give a linear system with the unique solution $\hat u$. Then $\epsilon^2\ge R_n$ and the bound of (a) give the bound on $n$. (c) The attacker's observations and the trainer's have one law. $\square$

Remark (heuristic). Let $\hat u$ be the posterior mean, and let the release add noise of variance $s^2$ to its answers. The posterior error $u-\hat u$ has conditional mean zero given the trainer's design, $\hat u$ and the answers, so the attacker's risk is $R_n+\mathbb E\|\tilde u-\hat u\|^2$ (proven). The second term is of order $ds^2/N$ for $N$ answers (heuristic), so reaching $2R_n$ costs answers of the order of the trainer's records. The floor Halil described therefore needs answers as noisy as nature.

Other regime and the oracle. The ceiling is data processing and binds every attacker, unbounded ones included. Halil's sentence, "a clear lowerbound which is the performance of initial model", holds as a bound on the attacker's accuracy. It holds as a bound on the attacker's price only for a release that answers like nature, and thm-bayes-release-loss-matched-price is its correlational form. Compared with the update stream, the update observer sees at least the trainer's output and never pays more (the challenger's proof), while the release attacker sees at most the trainer's output and never knows more. No oracle is needed.

### def-statistic-learner-class: a learning attacker, the statistic it reads, and the price of its class

status: open

uses: def-uniform-security-profile, prop-profile-run-coordinate, def-optimum-update-stream

Statement. As accepted in round 01, with two sentences replaced.

- "A lower bound on $p_S$ is a statement about the law of $S$ alone, so it binds the learner at every precision" now reads: "A lower bound on $p_S$ is a statement about the law of $S$ alone. It binds every learner whose output is a measurable function of $S$, formed exactly, and of coins independent of the observations, whatever arithmetic follows. A learner that sums per-observation terms in floating point lies outside the class, since rounding can carry the order of the observations (fact-fine-precision-sgd-simulates-pac)."
- "A linear-Gaussian latent model reads the first two empirical moments, which are $\hat M$ in the update stream, whose mean is zero" now reads: "A linear-Gaussian latent model reads $(\bar v,\hat M)$. With its mean fixed at zero, as in the update stream, it reads $\hat M$."

One remark is added (heuristic, from conj-linear-class-reads-cauchy-transform). For a statistic class, success need not grow with $n$, so $p_S$ is the left end of a set of budgets that need not be an interval.

Other regime and the oracle. As accepted.

### prop-full-clipping-optimum-filter: full per-example normalization at a median-fitting optimum leaves only the input law and the release

status: sketch

uses: def-optimum-update-stream, thm-bayes-release-loss-matched-price

Statement. Parts (a) to (d) as accepted in round 01, with "fully clipped update" replaced by "normalized update" throughout, and with one part added.

- (e) In def-optimum-update-stream with $W\ge w_{\min}>0$ almost surely, at $\theta^*=0$ and $b=1$, per-example clipping at any $C<w_{\min}\sqrt d/2$ equals normalization on all $T$ records except with probability at most $Te^{-9d/64}$, under $P_u$ and under $P^\circ$. So every observer of $T$ clipped updates has advantage at most $2Te^{-9d/64}$ (proven, given the tail bound of Laurent and Massart, from memory, unverified).

Proof of (e). At $\theta^*=0$, $\|\psi\|=W\|X\|\ge w_{\min}\|X\|$. The lower tail $\Pr[\chi^2_d\le d-2\sqrt{dx}]\le e^{-x}$ at $x=9d/64$ gives $\Pr[\|X\|^2\le d/4]\le e^{-9d/64}$. Off that event $\|\psi\|>w_{\min}\sqrt d/2>C$, so clipping is normalization. A union bound over $T$ records bounds the total variation between the clipped and the normalized stream by $Te^{-9d/64}$ under each law. The normalized streams have one law by part (b), and the triangle inequality gives $2Te^{-9d/64}$. $\square$

Other regime and the oracle. As accepted. Normalization is the exact object, and clipping inherits its filter only where every gradient exceeds the clipping norm. At a median fit with a continuous conditional law of the label, a positive fraction of records always escapes clipping, and the leak runs through them.
