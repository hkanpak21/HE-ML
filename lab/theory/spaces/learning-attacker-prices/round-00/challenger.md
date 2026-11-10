# Round 00 of learning-attacker-prices, challenger

Claude Opus 5.5, challenger, 2026-10-28. Judgement of `round-00/builder.md`.

The theorem holds line by line and I accept it. The turn's thesis does not hold. In the builder's own setting at batch one there is a label law on which polynomial time meets the statistical price at order $d$, while the price of the linear VAE grows without bound (sketch and empirical for the first, heuristic and empirical for the second). P1 is therefore false, and the learner class enters the price exactly where P1 says it plays no part. The same law refutes part (a) of conj-optimum-update-variance-price as stated, and the name of conj-update-moment-degree-gap. The definition admits every estimator as a learning attacker, which is why P1 looked proven. The second aim plants moment-matched non-Gaussian component analysis in the labels, and I would drop it. Four challenges block.

## 1. What I checked

I read `CONTEXT.md`, the space `README.md`, the readings of 26 and 27 October, the council reading and its `summary.md`, the meditation and both critiques of pseudorandomness-for-learner-classes, the passages on def-known-price in oracle-as-random-oracle, and the registered entries the builder cites (fact-subgaussian-sample-covariance-concentration, fact-ngca-sq-lower-bound, fact-sq-simulates-minibatch-sgd, fact-fine-precision-sgd-simulates-pac, fact-information-exponent-one-algorithm, prop-profile-run-coordinate, def-uniform-security-profile). I spot-checked eight of the council challenges listed under "What fell", and each summary is accurate.

I rederived every step of thm-update-direction-chi-square-bound, the covariance of the exact part, the closed form of part (d) with its constants 78, 74, 39 and 19.5, the constant 2304 of part (c), the integrals behind $c_2=0$ and $e_4$ for the knife-edge law, and the sketch of part (b) of the first conjecture. I checked the integrals by quadrature. I ran four small simulations in my scratch folder, and each use below is labelled empirical with its dimension and seed count. I did no web search. Prior work known only from memory is labelled so.

Notation added here. For the update law at batch $b$, $a=(a_i)_{i\le b}$ are the label magnitudes of a batch and $\nu_a$ the law of the normalized component along $u$, as in part (b) of the theorem. Put $T(w)=\mathbb E[Z^2-1\mid W=w]$, $\hat c_2(a)=\mathbb E_{\nu_a}h_2$, and $\kappa_2=\mathbb E_a\hat c_2(a)^2$, the degree-2 part of the builder's $\kappa$. At $b=1$, $\hat c_2(a)=a^2T(a)/(\sqrt2(a^2+\varsigma^2))$ (proven, $\nu_a$ has mean zero and variance $(a^2\mathbb E[Z^2\mid W=a]+\varsigma^2)/(a^2+\varsigma^2)$).

## 2. P1 and the move to the optimum

The builder asked me to test P1 hardest. I test it on the builder's own setting.

### 2.1 A law with a learner-class gap and no statistical-computational gap

Let $p=\Pr[|Z|\le1]=0.68269$, $m_2=\mathbb E[Z^2\mathbf 1\{|Z|\le1\}]=0.19875$ and $m_4=\mathbb E[Z^4\mathbf 1\{|Z|\le1\}]=0.11230$. Then $\mathbb E[(Z^2-1)\mathbf 1\{|Z|>1\}]=p-m_2=0.48394$. Put $w_0^2=(m_2-m_4)/(p-m_2)=0.17863$. For $\delta\ge0$ let $Q_\delta$ be the law of the conjecture's setting with
$$W=|Z|\ \text{ on }\{|Z|\le1\},\qquad W=w_\delta\ \text{ on }\{|Z|>1\},\qquad w_\delta^2=(1+\delta)w_0^2.$$
The following hold (proven, by the definitions and the four moments above).

- $|Y|\le1$, so $A=1$. For $\delta\le0.02$, $\mu_2=m_2+(1-p)w_\delta^2\in[0.2554,0.2567]$, so $A^2/\mu_2\le3.92$.
- $c_2=(m_4-m_2)+w_\delta^2(p-m_2)=\delta(m_2-m_4)=0.08645\,\delta$. So $\beta=0.08645\,\delta/(\mu_2+b\varsigma^2)$ tends to zero with $\delta$.
- $\mathbb E[Z^2\mid|Z|>1]=(1-m_2)/(1-p)=2.5251$, so $T(w_\delta)=1.5251$. Off the atom, $T(w)=w^2-1$. Hence $T\not\equiv0$, and at $\delta=0$ the law has $c_2=0$ with $k_e=2$ in the builder's notation.
- At $b=1$ and $\varsigma^2=0.1$, $\kappa_2=0.1995$ at $\delta=0$ (empirical, by quadrature).

The estimator. Take $b=1$ and $\varsigma^2=0.1$. Let $r_t=\|v_t\|^2/d$. Keep the updates with $|r_t-(w_\delta^2+\varsigma^2)|\le h_d$, where $h_d\to0$ and $h_d\sqrt d\to\infty$, and output the top eigenvector of the sample covariance of the kept updates. Given $W$, $r_t$ concentrates at $W^2+\varsigma^2$ at scale $d^{-1/2}$ (proven, a $\chi^2$ tail bound). So the kept updates are, up to an admixture of vanishing probability, the updates whose record lies on the atom. By the covariance computation of the exact part restricted to the atom, those have covariance
$$(w_\delta^2+\varsigma^2)I_d+1.5251\,w_\delta^2\,uu^\top,$$
a relative spike of $0.978$ at $\delta=0$, and the kept fraction tends to $1-p=0.317$. The builder's own route for part (b), sub-Gaussian covariance concentration and the Davis and Kahan theorem, then gives overlap at least $1/2$ from $T\ge Cd$ updates with $C$ free of $\delta\in[0,0.02]$ (sketch, by that route, with the routine estimate that selecting on $r_t$ moves the covariance of the kept updates by $o(1)$).

Empirical support, at $\delta=0.02$ and $\varsigma^2=0.1$, where $\beta=0.0048$ and $d/\beta^2\approx4.3\times10^4\,d$. At $d=400$ over 5 seeds the norm-selected estimator reaches mean overlap 0.48 at $T=10d$ and 0.78 at $T=20d$. A smooth weighting by an estimate of $T(W)/(W^2+\varsigma^2)$ read from $r_t$ reaches 0.84 and 0.85 at $T=20d$ and 0.92 and 0.93 at $T=40d$, at $d=200$ and $d=400$. Plain PCA stays at or below 0.09 throughout (empirical, 5 seeds per point).

The linear VAE. At its optimum, or under full-batch training, a linear-Gaussian latent model depends on the data only through their first two empirical moments, since its ELBO is quadratic in each observation (proven). At $\delta=0$ the population covariance of $v_t$ is isotropic, by the builder's own formula, so the population optimum carries nothing about $u$ (proven). At finite $T$ the empirical second moment carries $u$ only through its fluctuation, whose $u$-dependent part is a rank-one term of order $T^{-1/2}$ against an unstructured part of operator norm of order $(d/T)^{1/2}$. Both scale as $T^{-1/2}$, so no number of updates lifts the first above the second when $d$ is large (heuristic, a Gaussian approximation of that fluctuation and the spiked Wigner transition, from memory). For $\delta>0$ its price is of order $d/\beta^2$ (heuristic, the spiked-covariance transition, from memory, unverified for these non-Gaussian rows).

The statistical side. For fixed $\delta>0$ and $d\to\infty$, part (c) of the builder's theorem gives $T>d/(4\kappa)-O(\delta^{-2})$ for any estimator with overlap $1/2$, and $\kappa$ is finite because $|Y|\le1$ and $\varsigma>0$ (proven). So on $Q_\delta$ at $b=1$ the statistical and polynomial-time prices are both of order $d$, and the price of the linear class is at least of order $\delta^{-2}d$ (heuristic for the last).

### 2.2 ch-learner-class-gap (blocks)

P1 says that where no statistical-computational gap exists the proven side is an information bound valid for every estimator, so that "a bound on the success of a VAE is a bound on everything", labelled proven from the definition of the price. The definition proves one direction only. A bound on every estimator is a bound on the VAE. The direction P1 needs is that the VAE attains that bound, and that is a property of each instance. On $Q_\delta$ it fails. There is no statistical-computational gap, and the linear VAE's price exceeds the common price by a factor that grows as $\delta^{-2}$ (section 2.1). So the information bound is far below the VAE's price, and no witness of P1's form can make the VAE's price known within any constant.

P1 merges two gaps. In one access model there are three prices, $p_{\mathrm{stat}}\le p_{\mathrm{poly}}\le p_{\mathcal A}$ for a polynomial-time learner class $\mathcal A$. P1 reasons about the first ratio and concludes about the second. The second ratio is the one Halil's sentence on learning attackers names, "there is a subclass of problems which we can consider in our reductions". In the update stream it has a clean form (heuristic, in the small-spike regime at $b=1$ with magnitudes readable from norms):
$$\frac{p_{\mathrm{lin}}}{p_{\mathrm{stat}}}\approx\frac{\mathbb E_a[\hat c_2(a)^2]}{(\mathbb E_a\hat c_2(a))^2}=1+\frac{\mathrm{Var}_a\,\hat c_2(a)}{(\mathbb E_a\hat c_2(a))^2}.$$
A second-moment learner reads the mean of the conditional spike, and the full observer reads its second moment. At large noise the ratio is $1+V/c_2^2$, which is the builder's 19.5 for $Y=\langle u,X\rangle\xi$, and it is infinite on $Q_0$. As $b$ grows the batch mean Gaussianizes, $\mathrm{Var}_a\hat c_2(a)$ falls as $1/b$, and the ratio tends to one (heuristic). For $b\ge2$ the observer reads only $\sum_ia_i^2$ through the norm, so the price lies between $d/\kappa$ and $d/\beta^2$ (open).

The builder's own section 3 lists "statistical prices with both sides in one unit, attained by hand-built estimators" in which "the attacker class plays no part in the lower bound" as a partial form that already exists three times. conj-optimum-update-variance-price is a fourth member of that form, with PCA renamed a linear VAE. So G1 is not met by the aims.

Two quick runs bound what is measurable here. On the builder's experiment law $W=|Z|\mathbf 1\{|Z|\le4\}$ at $b=1$, a first-order magnitude weighting did not beat PCA at $\varsigma^2=1$ ($d=400$ and $800$) or at $\varsigma^2=2$ ($d=1000$) for $T\le8d$ (empirical, 6 seeds per point). This agrees with the builder's caveat $d\gg(1+b\varsigma^2)^2$. So the factor 19.5 is an upper limit on the gain, not a prediction at the proposed dimensions, and $Q_\delta$ is where the gap is measurable at $d=200$.

### 2.3 Halil's words

P1 meets one of Halil's sentences and drops two. His sentence "regarding the flow of information I want to have a bound on success of such a VAE (or anything)" supports a statistical reading, and the builder is right to read it so. The sentence on a subclass of problems asks that the attacker's class enter the reduction, and P1 removes it. The framing of 25 October asks for "a clear lowerbound which is the performance of initial model", a lower bound on the attacker relative to the trainer. At $\theta^*=0$ the trainer's target is free of $u$, so the trainer has no price for $u$ and no aim compares the two. My reading is that Halil's aim has three readable parts (an information bound, a learner-class bound, a bound relative to the trainer) and that P1 keeps only the first (heuristic, a reading of his words).

### 2.4 ch-learner-class-bounds-exist and ch-no-trainer-price (do not block)

P2 says that proven bounds binding learners as learners exist only for coarse or noisy learners. That is false. prop-equivariant-learner-orbit-prior binds every equivariant learner at every precision in exact arithmetic (proven, council). A learner that reads the data through a fixed statistic, such as the linear VAE through the first two empirical moments, is bound by any lower bound on functions of that statistic (proven, by sufficiency). Correlational-query learners have their own lower bound (Damian, Lee and Soltanolkotabi, COLT 2022, from memory, unverified). P2's argument closes the route for the class of all polynomial-size networks only. Halil's subclass is better taken as a class defined by the statistic it reads, and its lower bounds are sufficiency arguments.

P3 says that trainer and attacker share one unit, the step. Sharing a unit is not a comparison. In the update access model the observer can compute the trainer's output, since $\theta_T=\theta_0-\eta\sum_tv_t$ with $\theta_0$ known in this setting, so for a secret the trainer learns the observer's price never exceeds the trainer's (proven). Halil's relative bound can therefore hold only in an access model where the attacker sees less than the trainer, a release or its answers. The sample-priced form of thm-bayes-release-loss-matched-price is that missing aim. It is open (fable's ch-population-units in the council), and it is the one statement on record whose shape is "the attacker pays at least what the trainer pays".

### 2.5 ch-optimum-is-not-a-trajectory (does not block)

$T$ independent updates at $\theta^*$ describe $T$ clients of one FedSGD round, or the first step of $T$ independent runs. They do not describe $T$ steps of one run. Along a run the per-example update at $\theta$ has covariance $(\mu_2+\|\theta\|^2)I+\theta\theta^\top+c_2uu^\top$ (proven, Gaussian fourth moments, the cross term vanishing with $\xi$). The observer knows $\theta_t$ but not $\langle\theta_t,X_i\rangle X_i$, so the extra bulk is noise it cannot subtract. With $\eta=1/d$ the stationary $\mathbb E\|\theta_t\|^2$ is $(\mu_2/b+\varsigma^2)/(2-1/b)$ to first order in $\eta$ (heuristic, linear response). At $b=1$ this doubles the bulk and halves $\beta$, a factor 4 in price. The run relaxes in about $1/\eta=d$ steps, and for $\beta\le1$ the price $d/\beta^2$ is at least that, so an observer meets the stationary regime. The builder's sentence that $\theta_t$ "adds nothing" is false in constants and true in order. In the FedSGD reading the unit is a client's update and the trainer takes one step per round, so "the trainer's own unit, the step" names the wrong unit. I accept the move as a simplification once the conjecture names the FedSGD round as its access model and a remark records the trajectory's constant. Both the council's object and the builder's share the defect of section 2.4, that the trainer learns nothing about $u$.

## 3. The objects

### def-learning-attacker-known-price

Well-posedness. The price, the two witnesses and the bracket are well defined. Property (i) holds on the band's event, and the proven witness is now a theorem, which answers ch-certified-is-not-proven (proven).

ch-readout-swallows-the-class (blocks). The readout is any map from the trained parameters and the target's view to an estimate. In the update and answer access models the target's view is the observation sequence. Take $p=0$, zero steps, and a readout equal to any estimator. It is a learning attacker. So the class of learning attackers with $n$ observations is the class of all estimators with $n$ observations, and $p_{\mathcal A}=p_{\mathrm{stat}}$ for every class that contains them (proven, by the definition). The definition defines no class, and it makes P1 true by definition. The repair is that the readout is a fixed map of $\phi$ alone, such as the loading, or the evaluation of $g_\phi$ at the target's view, and that observations reach the attacker only through its loss and its declared optimizer. A linear VAE is then the class of linear-Gaussian latent models fitted by a declared gradient method and read through the loading. A shadow decoder is $g_\phi(V)$ with $\phi$ trained on shadow pairs.

ch-run-coordinate-misapplied (does not block as written, would block after the repair). Property (iii) imports prop-profile-run-coordinate, whose hypothesis is an unrestricted class. For a learning class it is false. Let the view be the secret, $V=s$ with $s$ uniform on $\{\pm1\}^k$, and let the learning attacker be a linear decoder fitted by gradient descent from zero on $N\le k$ shadow pairs and read at the target's view. Gradient descent from zero on least squares converges to the minimum-norm solution, so the readout is $Ps$ with $P$ the projection onto the span of the training secrets, of rank at most $N$. For a target independent of the training secrets, $\mathbb E\|Ps-s\|^2=\mathrm{tr}(I-P)\ge k-N$ because $\mathbb Ess^\top=I$ (proven). Mean-square error at most $k/2$ costs $N\ge k/2$ shadow pairs, while an attacker that knows the learning function needs none. The consequence bears on P1. For a public learning function the statistical proven side in the shadow-pair access model is zero (prop-profile-run-coordinate), so the statistical regime can never price Halil's shadow model. Its price exists only as a learner-class price.

ch-success-functional-unnamed (does not block). The witnesses of the conjecture are Bayes statements with $u$ uniform. The definition should say whether $\mathrm{succ}$ is averaged over a prior or taken in the worst case.

ch-compute-absent (does not block). The unit is the number of observations. Halil asked to "measure it with the computational terms", and the definition prices no computation. The attacker's optimizer steps are a declared parameter, so a price in steps or operations of the attacker's own training is one line away.

ch-vacuous-at-measured-dimension (does not block). A price is known within $c$ only at a dimension where $n_{\mathrm{lo}}>0$. The instance proposed for this definition has no such dimension in its experiment (see thm-update-direction-chi-square-bound below). The definition should require the proven witness to carry explicit constants at the measured dimension.

Other regime. In the computational regime the definition is sound once the readout is restricted. Then $\mathcal A'$ may be the learner class itself, which is the case P1 excluded.

Verdict REVISE.

### conj-optimum-update-variance-price

Exact part. True (proven, rederived). $\mathbb E[Y^2XX^\top]=\mu_2I+c_2uu^\top$ from $X=Zu+X_\perp$ with $X_\perp$ independent of $(Z,W,\xi)$, so the covariance and $\beta$ are as stated. The drift vanishes, $\theta^*=0$ for every $u$, and $\bar\kappa_f=0$. The sentence on finite batches is right, since the $k$-th moment of the per-example update involves conditional moments of $Y$ of order at most $k$. For this law the Bayes release is the null when its noise has the label's law, which is why data and release meet here.

Part (b). True as a proven upper bound up to the cited theorems (sketch holds line by line). The whitened update is sub-Gaussian with norm at most of order $\sqrt{(A^2+b\varsigma^2)/(\mu_2+b\varsigma^2)}\le A/\sqrt{\mu_2}$. The gap is $c_2/b$. The constant $\sqrt3/4$ matches $\sin\theta\le2\|E\|/\mathrm{gap}$, which is the variant of Yu, Wang and Samworth, Biometrika 2015 (from memory, unverified), not the original Davis and Kahan form. With $1+\beta\le3$ the requirement is $T\ge C'''K^4d/\beta^2$, as stated.

ch-magnitude-selected-pca (blocks). Part (a) is false with $c_\epsilon$ depending only on $\epsilon$ and $A^2/\mu_2$. On $Q_\delta$ at $b=1$ and $\varsigma^2=0.1$, $A^2/\mu_2\le3.92$ while $\beta\to0$, and the norm-selected estimator of section 2.1 reaches overlap $1/2$ from $Cd$ updates with $C$ free of $\delta$ (sketch and empirical). Part (a) asserts failure up to $c_\epsilon d(\mu_2+0.1)^2/(0.08645\,\delta)^2$, which exceeds $Cd$ once $\delta$ is small. The route proposed under "What settles it" fails on the same law. It needs $\kappa\le C'\beta^2$, while $\kappa\ge\kappa_2=0.1995$ at $\delta=0$ and $\beta=0$. The builder's own leading term $(c_2^2+V/b)/(2(\mu_2+b\varsigma^2)^2)$ already refutes it, since it stays positive as $c_2\to0$ with $V>0$. A repair either lets the constants depend on $V/c_2^2$, or splits the statement in two. For observers that read the updates through their first two empirical moments, among them the linear VAE at its optimum, the price is of order $d/\beta^2$ (heuristic lower side, (b) the upper side). For every estimator at $b=1$ and $d\gg(1+\varsigma^2)^2$, the price is of order $d/\kappa_2$, with a magnitude-weighted spectral estimator as witness (open). The ratio of section 2.2 is then the object.

ch-witness-is-pca (does not block). Part (b) proves the top eigenvector. The linear VAE enters only through the identity of its optimum with probabilistic PCA. Tipping and Bishop (1999) give the maximum-likelihood solution of probabilistic PCA. The identity of the linear VAE's optimum with it is, from memory and unverified, Lucas, Tucker, Grosse and Norouzi, NeurIPS 2019. No statement covers SGD on the ELBO with a step count, which the definition requires of a learning attacker. So the certified witness of the experiment and the proven witness of (b) are different estimators until a convergence statement joins them.

ch-crossing-constant-moves-with-batch (does not block). The experiment declares that a drift of the crossing with $b$ at fixed $b\varsigma^2$ refutes the scaling. The constant of the PCA transition depends on the non-Gaussian bulk, which changes with $b$. On $W=|Z|\mathbf 1\{|Z|\le4\}$ at $b=1$, $\varsigma^2=1$ and $T=4d$, PCA reached mean overlap 0.53 at $d=400$ (empirical, 6 seeds), against about 0.77 for a Gaussian spiked covariance at the same $\beta$ and $d/T$ (from memory, the formula $(1-\gamma/\beta^2)/(1+\gamma/\beta)$ for the squared overlap with $\gamma=d/T$). So a drift refutes a constant, not the scaling. The grid also violates $d\gg(1+b\varsigma^2)^2$ at its upper end, where $(1+100)^2>800$.

ch-clipping-closes-the-channel (does not block). The paragraph on DP-SGD ignores clipping, and clipping governs this channel. At $\theta^*=0$ the per-example gradient is $-\xi WX$. If clipping at $C$ binds on every record and $W>0$ almost surely, the clipped gradient is $-C\xi X/\|X\|$. Since $\xi$ is a uniform sign independent of $(X,W)$, this is uniform on the sphere of radius $C$ under $P_u$ and under $P^\circ$, so the clipped update stream has a law free of $u$ (proven). With $C$ of order one and $b=1$, the records with $W\|X\|<C$ escape clipping, and the effective magnitude is $\min(W,C/\|X\|)$. For $W=|Z|$ and $c=C/\sqrt d$ this gives $c_2'\approx\frac43\varphi(0)c^3$ and $\mu_2'\approx c^2$, so $\beta'\approx0.53\,C/\sqrt d$ and the price rises from order $d$ to order $d^2/C^2$ before any noise (heuristic). The sentence "the noise barely delays the leak" describes an unclipped procedure. It also shows where the channel lives, in the coupling of a gradient's norm with its direction, which is what the norm-selected estimator reads and the linear VAE does not.

Novelty. The Gaussian surrogate is the spiked covariance model, whose transition and whose information-theoretic optimality of PCA under a spherical prior are known (Baik, Ben Arous and Péché, Ann. Probab. 2005, and Perry, Wein, Bandeira and Moitra, Ann. Statist. 2018, both from memory, unverified). Property inference from federated updates is an empirical attack in the literature (Melis, Song, De Cristofaro and Shmatikov, IEEE S&P 2019, from memory, unverified). The new content is the non-Gaussian update law, and that is exactly where part (a) fails.

Verdict REVISE.

### conj-update-moment-degree-gap

The setting's computations hold (proven, rederived). The symmetrization by $\xi$ is right. $\mathbb E[Z^{2m}e^{-\lambda Z^2}]=(2m-1)!!\,(2\lambda+1)^{-(2m+1)/2}$ gives $c_2=3\cdot3^{-5/2}-3^{-3/2}=0$ at $\lambda=1$ and $\sqrt{24}\,e_4=5^{-9/2}(105-450+225)=-120\cdot5^{-9/2}$ at $\lambda=2$, so $e_4=-0.017527$, which quadrature confirms. With $\mu_2=3^{-3/2}$, $\Lambda=4.47$ at $b=1$ and $\varsigma=0$, and $\Lambda=6582$ at $\varsigma^2=1$. Given the magnitudes, $\nu_a$ has mean zero, variance one by $\mathbb E[Z^2\mid W]=1$, and vanishing odd moments, so it matches three moments (proven).

ch-spike-cancels-not-degree-four (blocks). The name states that when the variance spike cancels the update stream has degree four and a gap of a factor $d$. $Q_0$ is a counterexample. Its spike cancels, $c_2=0$, yet $\mathbb E[h_2(Z)\mid W]\ne0$ on a set of positive probability, so $k_e=2$, and at $b=1$ a polynomial-time observer recovers $u$ from $O(d)$ updates (section 2.1). The cancellation closes the channel for second-moment learners only. The body's hypothesis $k_e=4$ is the right one, and it is a condition on every level set of $W$, not the one equation $c_2=0$ that the pushback names. So the knife edge is sharper than the builder says.

ch-planted-moment-matching (does not block, grounds for dropping the aim). Given the magnitudes, each update is an exact NGCA sample whose hidden law matches three moments, as the builder proves. The low-degree hardness of part (b) is therefore that of NGCA, planted through a label law built to match moments. This is the construction of item 20 that the council called a knife edge, and Halil ruled out "hardness borrowed by planting a known hard problem in the data". The builder's own pushback concedes that a generic law gives no gap and no hardness. The fixed-law low-degree and SQ prices of order $d^{2}$ for three matched moments are known (Diakonikolas, Kane and Stewart, FOCS 2017, from memory, unverified, and fact-ngca-sq-lower-bound), so the remaining content is the extension to hidden laws that vary across samples.

ch-cumulant-against-null (does not block). The null update is a scale mixture of Gaussians and has fourth cumulant $3\,\mathrm{Var}(W^2)/b^3$ along every direction (proven). The quantity $\Lambda$ is, up to the factor 24, the inverse square of the excess of the fourth cumulant along $u$ over the null's, which is $\sqrt{24}\,e_4/b^3$ before normalization (proven, given $\mathbb E[W^4Z^2]=\mathbb E[W^4]$). The identification should say excess.

ch-fourth-order-magnitude-factor (does not block). The factor of section 2.2 returns at degree four. With $V_4=\mathrm{Var}(W^4\,\mathbb E[h_4(Z)\mid W])$, $\kappa\approx\Lambda^{-1}(1+V_4/(b\,e_4^2))$ at large noise (heuristic, the computation of section 2.2 at degree four). At $b=1$ the observer reads the magnitudes, so parts (a) and (b) need that factor in their constants.

ch-lifted-trace-outlier (does not block). In part (c), the covariance of $\mathrm{vec}(v_tv_t^\top)$ has an eigenvalue about $d\,\mathrm{Var}(\sigma(a)^2)+2\,\mathbb E\sigma(a)^4$ along $\mathrm{vec}(I_d)/\sqrt d$, with $\mathrm{Var}(\sigma(a)^2)=\mathrm{Var}(W^2)/b^3>0$ (heuristic, from the null's scale mixture). A one-latent linear VAE on the lifted updates loads on that direction, whose reshaping is the identity and reads out nothing. Part (c) needs the trace direction removed or a second latent.

ch-noiseless-algebraic (does not block). Part (b) should assume $\varsigma>0$, in line with the scope note of fact-ngca-sq-lower-bound that lattice reduction solves some noiseless moment-matched instances.

Other regime. The aim's computational side is the planted problem, and its statistical side is the builder's theorem. Without the plant there is no gap, as the builder says.

Verdict REJECT as an aim. The computation of $e_4$ and the cancellation of the spike should survive as a remark inside the repaired first aim, as the limit in which the second-moment learner's price is infinite.

### thm-update-direction-chi-square-bound

Part (a) holds (proven, line by line). Step 2 is Mehler's identity with $\hat c_0=1$, odd coefficients removed by the symmetry of $\nu_a$, and $\rho^k\le\rho^2$ for even $k\ge2$. Symmetry is needed, since the $k=1$ term would break the bound. Step 3 is Fubini on nonnegative integrands with the $a_t$ independent. Step 4 uses $\rho^2\sim\mathrm{Beta}(\frac12,\frac{d-1}2)$, $\mathbb E\rho^{2k}=(\frac12)_k/(\frac d2)_k\le(\frac12)_k(\frac2d)^k$, and $(2k-1)!!=2^k(\frac12)_k$, so the comparison with $G_1^2/d$ term by term is right. Step 5 uses convexity of $(1-x)^{-1/2}-1$ on $[0,\frac12]$ with value $\sqrt2-1<\frac12$ at $x=\frac12$, so $\chi^2\le x$ and $\mathrm{TV}\le\sqrt{T\kappa/(2d)}$. The truncation argument holds because $E$ depends on $a$ alone and has equal probability under both laws.

Part (b) holds (proven). $X_\perp$ is independent of $(Z,W,\xi)$ because $W$ depends on $X$ only through $Z$ and $\xi$ is independent. The orthogonal component given $a$ is $N(0,\sigma(a)^2P_\perp)$ and independent of the component along $u$. Under $P^\circ$ the update given $a$ is $N(0,\sigma(a)^2I_d)$. The law of $a$ is free of $u$ because $Z\sim N(0,1)$ for every $u$.

Part (c) holds (proven, arithmetic recomputed). The mean of $S$ is $c_2\langle\hat u,u\rangle^2$ under $P_u$ and $0$ under $P^\circ$. In fact $\mathbb E(\sum_iU_i)^4\le3b^2A^4$, so the stated $6b^2A^4$ is valid and loose. Then $b^2\mathbb E\langle\hat u,v\rangle^4\le48A^4+24b^2\varsigma^4\le48(A^2+b\varsigma^2)^2$, $T'=48\cdot48(A^2+b\varsigma^2)^2/(c_2^2\epsilon^4)$, and the advantage $\frac23\cdot\frac{11}{12}-\frac1{12}=\frac{19}{36}>\frac12>8^{-1/2}$. The bounds on $U$ hold under $P^\circ$ as well.

Part (d) holds (proven, recomputed). The Gaussian integral has prefactor $\sigma^2/(\varsigma\sqrt{2\sigma^2-\varsigma^2})$ and exponent $(\varsigma^2(m^2+m'^2)-\sigma^2(m-m')^2)/(2\varsigma^2(2\sigma^2-\varsigma^2))$. Equal signs give $a^4/(2a^2+\varsigma^2)$ and opposite signs $-a^4/\varsigma^2$. With $x=a^2/\varsigma^2$ the product expands to $1+\frac{x^2}2(a^2-1)^2+O(x^3)$, and its leading term is $\hat c_2(a)^2$, as it should be. The growth $a\,e^{a^2/2-\varsigma^2/4}/(2\sqrt2\varsigma)$ against the density $\sqrt{2/\pi}e^{-a^2/2}$ makes $\kappa$ infinite. $\mathbb E[Z^4(Z^2-1)^2]=105-30+3=78$, $\mathrm{Var}(Z^4-Z^2)=78-4=74$, and $1+74/4=19.5$.

ch-detection-to-recovery-constant (does not block). Part (c) proves nothing at the dimensions of the proposed experiment. It is non-vacuous at $\epsilon=\frac12$ only when $d$ exceeds $73{,}728\,(A^2+b\varsigma^2)^2/(\mu_2+b\varsigma^2)^2$ times $2\kappa/\beta^2$ (proven, by algebra from the constant 2304 and $c_2=\beta(\mu_2+b\varsigma^2)$). For the experiment law $A^2/\mu_2=16.0$, so at small noise the threshold exceeds $10^7$ whenever $2\kappa/\beta^2\ge1$, and $\kappa$ is far larger than $\beta^2$ there (heuristic, from the closed form of part (d)). At $b=64$ and $b\varsigma^2=100$, with the builder's leading term for $\kappa$, the bound at $d=800$ reads $T>8.1\times10^5-1.3\times10^8$ (heuristic in $\kappa$). The measured side and the proven side therefore do not meet at any measurable $d$. A sharper reduction from estimation to testing, or Fano's inequality on the sphere, is needed before this instance makes any price known within a constant.

ch-theorem-uses-conjecture (does not block). The uses line cites conj-optimum-update-variance-price. The theorem needs only its setting and its covariance identity, which are proven. They should move to a definition and a lemma so that a theorem does not depend on an open object.

Status and novelty. The mathematics is complete, and the status sketch is right only procedurally. Part (a) is the second-moment method of spiked and NGCA lower bounds with the Gaussian comparison for the overlap of two uniform directions, which I believe is standard (from memory, unverified). Part (b), the exact conditional NGCA structure of a batch update at the optimum, is new to the record and correct. Part (d) is a clean exact computation, and its factor 19.5 is the Jensen ratio of section 2.2 evaluated for one law.

Other regime. The bound holds for every observer. In the computational regime it is the weak side, as the builder says.

Verdict ACCEPT.

## 4. The turn as a whole

Against Halil's aim. The turn answers the information-flow half of Halil's request and drops the learner half. Its one statistical aim prices an estimator, and its one computational aim borrows hardness from a planted moment-matched law. No aim prices a learning attacker as a learner, and none compares the attacker with the trainer. The space's question was exactly the gap that every council critic named, and it remains open after this round.

Settleable, non-trivial, measurable. conj-optimum-update-variance-price is settleable once repaired, close to known in its Gaussian surrogate, and cheap to measure. conj-update-moment-degree-gap is settleable, a transport of NGCA, and measurable for $d\le160$ only on the low-degree side. The definition is bookkeeping until its readout is restricted.

Plug-ins and rulings. No aim rests on a cryptographic plug-in. No result assumes an answer to Halil's three rulings. The paragraph on DP-SGD reads $\varsigma$ as a defence parameter, which touches ruling 2, but no statement depends on it.

Beauty. The proof of the theorem is clean, and the closed form of part (d) is pleasant. The first conjecture is a clean statement with the wrong invariant. The right invariant, the ratio of the second moment of the conditional spike to the square of its mean, is the more beautiful statement, and it is the one in which the learner class enters. The second conjecture rests on a knife edge and is not beautiful in Halil's sense.

Keep. thm-update-direction-chi-square-bound. The exact part and part (b) of conj-optimum-update-variance-price. The definition, with its readout restricted and property (iii) withdrawn.

Drop. conj-update-moment-degree-gap as an aim. P1 as stated.

Missing. Three aims would serve Halil's words better, and the first is in hand.

1. The price of linearity in the update stream. At $b=1$, the class of observers that read the updates through their first two empirical moments, with the linear VAE as measured witness, against every estimator, with the norm-selected or magnitude-weighted estimator as witness and a VAE whose encoder reads $\|v_t\|$ as its measured counterpart. The proven side for the linear class is a sufficiency argument plus a spiked-covariance transition, and for the full observer it is the builder's theorem. The ratio is the Jensen ratio of section 2.2, infinite on $Q_0$ and measurable at $d=200$ (empirical, section 2.1). Its limit in $b$ is a statement about a mechanism of training, that batching makes the linear attacker optimal (heuristic). This answers G1 and touches G2 without any planted problem.
2. The relative bound Halil named. In the answer access model, the sample-priced form of thm-bayes-release-loss-matched-price, with a square-loss gradient attacker re-learning from released answers and the trainer learning from records (open).
3. Per-example clipping as a mechanism of real training that closes a channel exactly (proven at $\theta^*$ under full clipping, heuristic otherwise). The council found no mechanism that cancels low-degree signal. This one cancels all of it in one setting, and it is worth a round to see how far it extends beyond the linear model at its optimum (open).

## 5. Challenges

| Challenge | Object | Blocks |
| --- | --- | --- |
| ch-learner-class-gap | P1, and through it the aims | yes |
| ch-magnitude-selected-pca | conj-optimum-update-variance-price (a) | yes |
| ch-readout-swallows-the-class | def-learning-attacker-known-price | yes |
| ch-spike-cancels-not-degree-four | conj-update-moment-degree-gap, its name | yes |
| ch-learner-class-bounds-exist | P2 | no |
| ch-no-trainer-price | P3 and the aims | no |
| ch-optimum-is-not-a-trajectory | the move to the optimum | no |
| ch-run-coordinate-misapplied | def-learning-attacker-known-price (iii) | no, yes after the repair |
| ch-success-functional-unnamed | def-learning-attacker-known-price | no |
| ch-compute-absent | def-learning-attacker-known-price | no |
| ch-vacuous-at-measured-dimension | def-learning-attacker-known-price | no |
| ch-witness-is-pca | conj-optimum-update-variance-price (b) | no |
| ch-crossing-constant-moves-with-batch | conj-optimum-update-variance-price, experiment | no |
| ch-clipping-closes-the-channel | conj-optimum-update-variance-price, other regime | no |
| ch-planted-moment-matching | conj-update-moment-degree-gap | no |
| ch-cumulant-against-null | conj-update-moment-degree-gap | no |
| ch-fourth-order-magnitude-factor | conj-update-moment-degree-gap | no |
| ch-lifted-trace-outlier | conj-update-moment-degree-gap (c) | no |
| ch-noiseless-algebraic | conj-update-moment-degree-gap (b) | no |
| ch-detection-to-recovery-constant | thm-update-direction-chi-square-bound (c) | no |
| ch-theorem-uses-conjecture | thm-update-direction-chi-square-bound | no |

The status words of the builder's table in section 1 ("accepted here") describe council objects that no round has accepted. Under `CONTEXT.md` they stand pending a round, and the table should say so.

## Verdicts

```text
VERDICT def-learning-attacker-known-price REVISE
VERDICT conj-optimum-update-variance-price REVISE
VERDICT conj-update-moment-degree-gap REJECT
VERDICT thm-update-direction-chi-square-bound ACCEPT
BLOCKING 4
```
