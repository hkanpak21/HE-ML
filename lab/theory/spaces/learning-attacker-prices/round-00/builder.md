# Round 00 of learning-attacker-prices, builder

Claude Opus 5.5, builder, 2026-10-28. The aims round.

The council left exact statements and no theory, and none of its statements prices an attacker that learns. This round proposes three aims and proves one bound. The aims replace the council's trajectory object by the stream of updates at the trainer's optimum, where the population drift vanishes and every update is batch noise. There the covariance of the noise carries the secret, and a linear VAE recovers it. An information bound proven here limits every observer, and the main conjecture is that the two meet within a constant, in the trainer's own unit, the step. Hardness appears only for a knife-edge label law, or in a finite window of dimensions near one.

Throughout, $\gamma_d$ is the standard Gaussian law on $\mathbb R^d$, $h_k$ the normalized Hermite polynomial of degree $k$, $\chi^2(\nu\|\gamma_1)=\int(d\nu/d\gamma_1)^2d\gamma_1-1$, $\mathrm{TV}$ the total variation distance, and $S^{d-1}$ the unit sphere.

## 1. What stands

Registered statuses are those of `sink/formalizing/results.md`. For council objects "both" means accepted by fable and sol.

| Result | Hypotheses that carry it | Status after the council |
| --- | --- | --- |
| thm-coupling-certificate, thm-dataflow-composition, thm-bounded-deviation-transfer, thm-exact-twin-price | named-seed coupled runs, and deterministic channels with atomless laws for the drawn-seed obstruction | accepted, untouched |
| thm-black-box-certifiability, thm-shadow-run-price-finite-views | finitely many queries and views | accepted, untouched |
| prop-profile-run-coordinate | an attacker that knows the learning function | accepted, and it carries pushback P3 |
| prop-reconstruction-label-sandwich | a finite label | accepted |
| thm-blind-orbit-limit, thm-blind-orbit-price, prop-whitening-orbit-sample-price | $O(d)$-equivariant training from an $O(d)$-invariant atomless start, Gaussian records | accepted for SGD only (correction 3), inapplicable to a short seed with separated representation laws (thm-short-seed-dichotomy) |
| thm-blind-split-seed-separation with its SQ and hCLWE parts, thm-coarse-reconstruction-lattice-hard | as above, pancake records, exact arithmetic for the lattice parts | accepted in that scope, the polynomial-time part on real seeds waits for ruling 1 |
| prop-blind-lll-label-recovery | exactly discrete hidden labels, exact arithmetic | accepted |
| thm-zlip-reductions | quantized records | sketch, one blocking challenge open |
| thm-reconstruction-from-conditional-mean, prop-sq-label-relevant-reconstruction-bound | frozen linear client, and VSTAT units for the second | accepted |
| thm-train-access-price-frontier, thm-same-units-gap-gaussian-mechanism | noise calibrated to the population covariance | accepted, the hypothesis waits for Halil's decision 1 |
| thm-extraction-exponent-price | SQ extractor on random inputs against a trainer that reads $y^2$ | accepted, not a learning one-way function (correction 1) |
| prop-learner-side-sq-transfer, lem-sq-learner-post-processing | a procedure that reads data through one-bit statistical queries | accepted, the SGD clause holds for a defending rounding only (correction 2) |
| thm-bayes-release-loss-matched-price | finite square risks and gradients that commute with expectation (sol), population or correlational units (fable) | fable accept, sol revise, accepted here with both repairs |
| prop-extraction-gap-information-exponent | a Gaussian single-index law | fable accept, sol revise, the inequalities stand and an exact SQ price stays open |
| thm-noisy-gradient-query-filter | population gradients, injected noise $\varsigma>0$, clipping for part (c) | both, read as an SQ bound with the architecture's own queries (fable) |
| thm-shadow-price-is-generative-exponent | Gaussian frame family, passive learner, VSTAT units | both, it is DPLB24 Theorem 3.2 with the secret as label |
| prop-approximate-degree-price | the hypothesis $\lambda_j^2\le\lambda_k^2\epsilon_d^{k-j}$ of fable | sol accept, fable revise, accepted here in fable's form |
| prop-overlap-grading-carries-price | validation precision charged in (b) (sol) | fable accept, sol revise, accepted here with sol's repair |
| prop-targeted-reader-no-learning-price | a known procedure and two laws | both |
| prop-seed-cannot-index-the-family | the drawn mode | part (a) stands, a persistent seed is a shared index (both critics) |
| thm-null-trajectory-filter | adversarial rounding, one defending rounding | both, without the sentence that memorization cannot be stated |
| thm-noisy-trainer-two-term-filter, prop-hashed-memory-breaks-sq-filter | information bounds conditioned on the population law (sol) | fable accept and sol revise for the first, both for the second, the first vacuous once $\mathcal I\ge2$ |
| thm-short-seed-dichotomy | separated representation laws | fable accept, sol revise, accepted here with that hypothesis |
| lem-exposure-information-sandwich, def-random-oracle-record-split | ties broken, the statistic $s$ a named parameter | sol accept, fable revise, accepted here with fable's repairs |
| conj-seed-price-is-ngca-price | an idealized seed | open, to be restated with the seed's size |

The five corrections of the council bind, and I accept all five.

1. Item 20 is not a learning one-way function. I checked fable's argument. A level set of an even link strictly monotone on $[0,\infty)$ is $\{\pm a(t)\}$, on which $\mathbb E[h_2(Z)\mid t]=(a(t)^2-1)/\sqrt2$, nonzero off one level (proven). The same balance returns in conj-update-moment-degree-gap.
2. Item 21's SGD clause holds for one defending rounding, in sol's form. Other valid roundings may memorize.
3. Items 12 and 15 are results about SGD from an $O(d)$-invariant start, and their statistical and SQ parts do not apply to a short seed with separated representation laws.
4. A learner of time $t$ outputs a predictor of size at most $t$ as a circuit, not as a uniform program.
5. The degree is not a unit, by the two frames of prop-overlap-grading-carries-price. I use one named unit per access model and a ratio at matched success, fixed in def-learning-attacker-known-price.

## 2. What fell

- def-class-pseudorandom-channel as a contribution. It is outcome indistinguishability of the constant predictor (sol cites Dwork, Kim, Reingold, Rothblum and Yona, STOC 2021, unread here), and its chosen-input mode is undefined (ch-chosen-input-reference).
- Its security reading. An instance that is its own secret is pseudorandom while fully disclosed (ch-secret-index).
- The learning one-way setup. A constant view channel satisfies it (ch-degenerate-gap), and thm-bayes-release-loss-matched-price empties it for square-loss gradient trainers.
- "Learnable exactly when not pseudorandom". The law $Y=\langle u,X\rangle\xi$ admits no square-loss gain, yet SQ detects it at exponent 2.
- prop-class-pseudorandomness-collapse (c) under the prior-averaged advantage. $Y=Z+\varepsilon$ has $k^*=1$ and passes every affine test (ch-collapse-prior-average).
- The filter slogan in its output reading. A trainer that outputs a test's verdict hands over a planted parity. Part (c) of prop-output-bounds-do-not-filter fell too, since small output information still constrains a random hypothesis (ch-output-impossibility).
- "Memorization cannot be stated in the rounding model". A rule that reads a sample bit can choose another valid rounding (ch-rounding-quantifier).
- prop-orthogonal-averaging-cancels-one-degree. A norm-only release with three matched moments has degree 4 (sol), and a ReLU view has raw degree 1 (fable).
- The degree-4 ceiling for natural data. The ICA fact assumes independent attributes (sol).
- The claim that real training cancels low-degree signal. No mechanism was found (both critics), and sol notes that the reason to stop searching fell with the symmetry ceiling. The batch attenuation of conj-update-moment-degree-gap is such a mechanism, though it attenuates and does not cancel.
- prop-key-free-defence-rule. A party that knows the input recovers additive noise (ch-key-free-information), and exact rounding yields discrete layers that LLL solves (ch-rounding-is-noiseless-clwe).
- prop-programming-preserves-prices (c) and (d). An admissible programming can move a price from 100 to 0 (ch-price-units), and (d) omits the setup's time (ch-prg-time-accounting).
- def-known-price (b). A certifier's output is not a statement valid at the instance (ch-certified-is-not-proven).
- prop-rise-decomposition-replace-one (c). One example and two constant predictors give memorization 0.18 against capacity 0.10 (ch-erm-capacity-bound).
- The exactness of the grip. Equal-probability buckets keep the oracle while the grip tends to one (ch-grip-equivalence).
- conj-degree-energy-estimator-meets-price, its meeting clause. The U-statistic estimates $\mu_j^2\le\sigma_\phi^2\lambda_j^2$, and detection is not decoding (both critics).
- prop-canary-is-programmed-record (b). A constant view keeps advantage zero while the record's conditional law changes (ch-programming-view-law).

## 3. The gap

Halil's aim, read as one object, has five parts. They are a setting, a secret, an access model whose unit is a learning unit, a learning attacker, and two numbers in that unit. One number is a proven lower bound $n_{\mathrm{lo}}$, the other a certified budget $n_{\mathrm{hi}}$ at which a declared learner succeeds, with $n_{\mathrm{hi}}\le c\,n_{\mathrm{lo}}$. What stands supplies three partial forms.

- Statistical prices with both sides in one unit, attained by hand-built estimators. These are thm-blind-orbit-price (whitening, in representations), thm-same-units-gap-gaussian-mechanism (a whitened test, in samples and $\mathsf{Train}$ calls), thm-shadow-run-price-finite-views (frequency counts, in $\mathsf{Train}$ calls) and thm-exact-twin-price (the auditor). No learner is a witness, and the attacker class plays no part in the lower bound.
- SQ prices, thm-shadow-price-is-generative-exponent and its instances, with the lower side in VSTAT units. They reach a gradient attacker only through fact-sq-simulates-minibatch-sgd, which needs $b\rho^2$ above a logarithm and grants a defending rounding. The proven side and a measured learning curve then sit in different access models.
- Population identities, thm-bayes-release-loss-matched-price and thm-noisy-gradient-query-filter, whose unit is a population gradient step.

Three things are missing.

- G1. An instance of the whole object with a learner as the certified witness.
- G2. A channel whose structure training produces. Every graded price so far lives in moments of the record law along a hidden direction.
- G3. A proven lower bound in samples against a fine-precision gradient attacker where statistical and computational prices differ.

Three pushbacks set what the aims can deliver.

P1. Where no statistical-computational gap exists, the proven side is an information bound valid for every estimator. A VAE then enters only as the certified witness, and "a bound on the success of a VAE" is a bound on everything (proven, from the definition of the price). This is the form of Halil's aim that can be met, and conj-optimum-update-variance-price is proposed to meet it.

P2. G3 has no known route. For the class of all polynomial-size networks, fine-precision SGD simulates every PAC learner on Boolean data (fact-fine-precision-sgd-simulates-pac, AKMSS21 Theorem 1a). A lower bound against that class is therefore a lower bound against polynomial time (proven, by the simulation), which no known technique proves without a named assumption. For one fixed architecture the question is open, and known lower bounds price one algorithm at a time (fact-information-exponent-one-algorithm). Proven bounds that bind learners as learners exist only for coarse or noisy ones, and practical attacks are neither.

P3. An attacker that knows the learning function gains nothing from $\mathsf{Train}$ calls (prop-profile-run-coordinate). A shadow-model attacker therefore has a price in runs only for what it does not know, an index its observations share or the learning function itself. In the update stream the unit is the trainer's own step, so trainer and attacker share one unit without exponents.

The aims use no reading of Halil's three open rulings. No seed enters, since the model sits at its optimum. The injected noise $\varsigma$ belongs to the procedure being priced, which is never compared with a noiseless one, so the programming rule is not invoked. No canary is used.

I replace the council's convergent object for three reasons. Its trajectory carries a nuisance $\theta_t$ that the observer knows and that adds nothing. At the optimum the updates are i.i.d. and their law has an exact conditional structure (thm-update-direction-chi-square-bound (b)), and the statement concerns a trainer that has learned all it can. I also widen the law from $Y=\langle u,X\rangle\xi$ to every symmetric heteroscedastic single-index law, which shows that the channel is generic at degree 2.

## 4. Aims

### def-learning-attacker-known-price: a learning attacker, and a price known in one access model

status: open

uses: def-uniform-security-profile, prop-profile-run-coordinate, prop-seed-cannot-index-the-family, def-known-price

Definition. An *access model* $\mathfrak O$ names one type of observation, and its unit is the number $n$ of observations received. Four types serve here, an update of the target's training step, an answer of a release at a random input, a released model of one run on the target's population, and a shadow pair $(s,V)$ from one $\mathsf{Train}$ call at a secret $s$ the attacker chooses. A *learning attacker* in $\mathfrak O$ is a parametric family $\{g_\phi:\phi\in\mathbb R^p\}$, a loss on observations, a gradient method with its batch, step count and precision or noise, and a readout from the trained parameters and the target's view to an estimate $\hat s$. A linear VAE fitted to the observations and read through its loading is one. A decoder trained on shadow pairs and read at the target's view is another. Fix a success functional $\mathrm{succ}$ and a level $s_0$. The price of a class $\mathcal A$ is
$$p_{\mathcal A}(s_0)=\min\{n:\text{some }A\in\mathcal A\text{ with }n\text{ observations has }\mathrm{succ}(A)\ge s_0\}.$$
A proven witness is a theorem that every member of a class $\mathcal A'\supseteq\mathcal A$ has success below $s_0$ when $n<n_{\mathrm{lo}}$. A certified witness is a declared $A\in\mathcal A$ with $n_{\mathrm{hi}}$ observations and a lower confidence band at least $s_0$, sound at level $\alpha$, from independent runs. The price of $\mathcal A$ is known within $c$ in $\mathfrak O$ when $n_{\mathrm{hi}}\le c\,n_{\mathrm{lo}}$, both counted in the unit of $\mathfrak O$. The regime is statistical when $\mathcal A'$ holds every estimator.

Properties (proven). (i) On the event, of probability at least $1-\alpha$, that the band holds, $n_{\mathrm{lo}}\le p_{\mathcal A}(s_0)\le n_{\mathrm{hi}}$. The certified witness is random, so the bracket holds on its event only, which answers ch-certified-is-not-proven. (ii) In the statistical regime the class $\mathcal A$ enters $n_{\mathrm{hi}}$ alone. (iii) For an attacker that knows the learning function, shadow pairs at chosen secrets carry no price (prop-profile-run-coordinate). They carry one only for an index hidden from it and shared by its observations, which a drawn seed is not (prop-seed-cannot-index-the-family (a)), or for an unknown learning function (def-uniform-security-profile).

What settles it. A definition earns its place through an instance with both witnesses and a learner as the certified one, and conj-optimum-update-variance-price is proposed as that instance. It applies in every regime, and its experiment is the certified witness itself.

Other regime and the oracle. In the computational regime $\mathcal A'$ is a class, SQ, low-degree, or polynomial time under a named assumption. The definition then demands that both witnesses count the same observations, so a VSTAT bound alone never makes a price known in a sample access model. The oracle supplies the runs of the certified witness and nothing else.

### conj-optimum-update-variance-price: at the optimum, an observer of updates pays the dimension over the squared variance spike, and a linear VAE pays it

status: open

uses: def-learning-attacker-known-price, thm-update-direction-chi-square-bound, thm-noisy-gradient-query-filter, thm-bayes-release-loss-matched-price, fact-subgaussian-sample-covariance-concentration

Setting. Inputs are $X\sim\gamma_d$, the secret is $u$ uniform on $S^{d-1}$, and $Z=\langle u,X\rangle$. Labels are $Y=\xi W$, where $\xi$ is a uniform sign independent of $(X,W)$, $W\ge0$, and the law of $W$ given $X$ is a function of $Z$. Put $\mu_2=\mathbb EY^2$ and $c_2=\mathbb E[Y^2(Z^2-1)]$. Since $\mathbb E[Y\mid X]=0$, the linear model $f_\theta(x)=\langle\theta,x\rangle$ has population square-loss optimum $\theta^*=0$ for every $u$ (proven). The observer receives $T$ updates at the optimum,
$$v_t=\frac1b\sum_{i\in B_t}Y_iX_i+\zeta_t,\qquad t=1,\dots,T,$$
with fresh batches $B_t$ of $b$ records and $\zeta_t\sim N(0,\varsigma^2I_d)$. Up to the factor $-\eta$, $v_t$ is a step of noisy mini-batch SGD at $\theta^*$, or the batch gradient of one of $T$ clients of one population in a FedSGD round. The null $P^\circ$ makes $Y$ independent of $X$ with the same marginal. Put $\beta=c_2/(\mu_2+b\varsigma^2)$.

Exact part (proven). Under $P_u$ and $P^\circ$ the update has mean zero, so the drift carries nothing, and noisy population descent releases a $u$-free model (thm-noisy-gradient-query-filter with $\bar\kappa_f=0$). The covariances are
$$\mathrm{Cov}_{P_u}(v_t)=\frac{\mu_2+b\varsigma^2}{b}\big(I_d+\beta uu^\top\big),\qquad\mathrm{Cov}_{P^\circ}(v_t)=\frac{\mu_2+b\varsigma^2}{b}I_d.$$
Proof. Write $X=Zu+X_\perp$ with $X_\perp$ independent of $(Z,W,\xi)$. Then $\mathbb E[Y^2XX^\top]=\mathbb E[Y^2Z^2]uu^\top+\mu_2(I_d-uu^\top)=\mu_2I_d+c_2uu^\top$. For $Y=\langle u,X\rangle\xi$ this is the spike $2uu^\top$ that fable recomputed. Data and a Bayes release give square-loss SGD the same drift (thm-bayes-release-loss-matched-price), and their update laws differ first through such second moments and then through higher conditional moments of the label (proven, since the $k$-th moment of $(f_\theta(x)-y)\nabla f_\theta(x)$ involves conditional moments of $Y$ of order at most $k$).

Conjecture. Assume $|Y|\le A$ almost surely and $0<\beta\le2$. For each $\epsilon\in(0,1)$ there are $c_\epsilon,C,d_0>0$, depending only on $\epsilon$ and $A^2/\mu_2$, such that for $d\ge d_0$:

- (a) every estimator $\hat u(v_{1:T})$ has $\Pr[|\langle\hat u,u\rangle|\ge\epsilon]<2/3$ when $T\le c_\epsilon d/\beta^2$,
- (b) the top unit eigenvector $\hat u$ of $T^{-1}\sum_tv_tv_t^\top$ has $\Pr[|\langle\hat u,u\rangle|\ge1/2]\ge2/3$ when $T\ge Cd/\beta^2$.

The estimator of (b) is the loading of a linear VAE with one latent dimension at its optimum, which is probabilistic PCA (Tipping and Bishop, 1999, from memory, unverified). So the price of an update observer is $\Theta(d(\mu_2+b\varsigma^2)^2/c_2^2)$ steps, known within a constant, with a linear VAE as the certified witness. For $c_2<0$ the bottom eigenvector replaces the top one.

What settles it. Part (a) at large noise follows from parts (b) and (c) of thm-update-direction-chi-square-bound once $\kappa\le C'\beta^2$ is shown, since the subtracted term of (c) is at most $2304(A^2/\mu_2)^2/(\beta^2\epsilon^4)$. That is a second-order expansion of $\chi^2(\nu_a\|\gamma_1)$, whose leading term is $(\beta^2/2)(1+V/(bc_2^2))$ with $V=\mathrm{Var}(W^2(\mathbb E[Z^2\mid W]-1))$ (heuristic, and part (d) of that theorem is its case $b=1$). At small $b\varsigma^2$ the $\chi^2$ route fails, since $\kappa$ grows without bound as $\varsigma\to0$, and another argument is needed (open). At $b=1$ and $\varsigma=0$ the observer holds $X$ up to sign together with $|Y|$, that is $T$ samples of the single-index law of $|Y|$, and (a) there is the weak recovery threshold of that law, linear in $d$ for phase retrieval (heuristic, from memory). Part (b) has a short route (sketch). The vector $\mathrm{Cov}_{P_u}(v)^{-1/2}v$ is isotropic and sub-Gaussian with norm $K=O(A/\sqrt{\mu_2})$. fact-subgaussian-sample-covariance-concentration bounds the operator error of the sample covariance by $\|\mathrm{Cov}_{P_u}(v)\|\,K^2C''\sqrt{d/T}$ for $T\ge d$. The Davis and Kahan $\sin\theta$ theorem (from memory) turns an error below $\frac{\sqrt3}{4}$ of the eigengap $c_2/b$ into overlap at least $1/2$. With $\beta\le2$ this needs $T\ge C'''K^4d/\beta^2$.

Regime. Statistical. The witness runs in time $O(Td^2)$, so the computational price equals the statistical one. There is no gap and no hardness.

Experiment. No oracle is needed, since the trainer is linear and an update costs $b$ samples. Take $W=|Z|\mathbf 1\{|Z|\le4\}$, $d\in\{100,200,400,800\}$, $b\in\{1,8,64\}$ and $b\varsigma^2\in[0.1,100]$. Fit a linear VAE to $v_{1:T}$ by SGD on its ELBO, read its loading, and record $|\langle\hat u,u\rangle|$ over 50 seeds. The prediction is that the curves collapse in $T\beta^2/d$ and cross $1/2$ at one constant. A drift of the crossing with $b$ at fixed $b\varsigma^2$ refutes the scaling. A spectral estimator that weights each update by a function of $\|v_t\|$ should gain up to the factor $1+V/(bc_2^2)$ in $T$, which is 19.5 at $b=1$ for $Y=\langle u,X\rangle\xi$, when $d\gg(1+b\varsigma^2)^2$, since $\|v_t\|$ then reveals the label magnitudes (heuristic).

Other regime and the oracle. The statement concerns the procedure itself and holds without the oracle. The secret is a property of the client's population, the target of property inference, which differential privacy is not designed to bound. In DP-SGD notation $\varsigma=\sigma C/b$ for noise multiplier $\sigma$ and clipping norm $C$, so $b\varsigma^2=\sigma^2C^2/b$, and at batches in the hundreds the noise barely delays the leak (heuristic, clipping ignored). Released models of $N$ independent runs in place of updates would price the observer in $\mathsf{Train}$ calls, with the spike of the release's second moment in place of $\beta$ (open, not developed here).

### conj-update-moment-degree-gap: when the variance spike cancels, the update stream has degree four and a gap of a factor d

status: open

uses: conj-optimum-update-variance-price, thm-update-direction-chi-square-bound, lem-level-set-moment-balance, prop-approximate-degree-price, fact-ngca-sq-lower-bound

Setting. That of conj-optimum-update-variance-price. Since $\xi$ is an independent sign, $YX=W\,(\xi X)$, and $(W,\xi X)$ has the law of $(W,X)$ symmetrized under $X\mapsto-X$. So the observer sees the law of $W$ given $Z$ only through its even part in $Z$ (proven). Let $k_e$ be the least even $k\ge2$ such that $\mathbb E[h_k(Z)\mid W]\neq0$ with positive probability, and put $e_k=\mathbb E[W^kh_k(Z)]$. A generic law has $k_e=2$ and $c_2=\sqrt2\,e_2\neq0$, the case of conj-optimum-update-variance-price (heuristic, a genericity statement). The law $W=|Z|e^{-Z^2/2}$ has $k_e=4$, since a standard Gaussian conditioned on a level set of $|z|e^{-z^2/2}$ keeps its first three moments (lem-level-set-moment-balance). Its spike vanishes, because $\mathbb E[Z^{2m}e^{-Z^2}]=(2m-1)!!\,3^{-(2m+1)/2}$ gives $\mathbb E[Z^4e^{-Z^2}]=\mathbb E[Z^2e^{-Z^2}]$ (proven). The covariance of every update is then $\frac{\mu_2+b\varsigma^2}{b}I_d$, so a linear VAE on $v_t$ has a $u$-free optimum (proven). The same integrals at rate $5/2$ give $e_4=-120\cdot5^{-9/2}/\sqrt{24}\neq0$ (proven).

Conjecture, for $k_e=4$ and $e_4\neq0$. Put $\Lambda=b^2(\mu_2+b\varsigma^2)^4/e_4^2$, the inverse square of the normalized fourth cumulant of $v_t$ along $u$ up to a constant factor (heuristic as an identification, from $\kappa_4(\bar g)=\kappa_4(g)/b^3$ for the mean $\bar g$ of $b$ copies of $g$).

- (a) The statistical price is $\Theta(d\Lambda)$ updates up to logarithmic factors.
- (b) For $D\le(\log d)^2$, the degree-$D$ likelihood ratio of $v_{1:T}$ against $P^\circ$ has bounded norm when $T\le d^2\Lambda/(\log d)^{C}$.
- (c) A linear VAE fitted to the lifted updates $\mathrm{vec}(v_tv_t^\top)$ recovers $u$ to overlap $1/2$ from $\tilde O(d^2\Lambda)$ updates.

The gap between (a) and (b) is a factor $d$, and its learning witness is again a VAE, on quadratic features.

What settles it. Given the label magnitudes, each update is an exact NGCA sample whose hidden law matches $\gamma_1$ in its first three moments (proven, by part (b) of thm-update-direction-chi-square-bound and $\mathbb E[Z^2\mid W]=1$). Part (a) of that theorem gives the lower half of (a) once $\kappa$ is shown to be of order $\Lambda^{-1}$. The upper half needs a net search over directions (from memory for NGCA). Part (b) needs the low-degree bound of NGCA for hidden laws that vary across samples, one step beyond the fixed-law SQ bound of fact-ngca-sq-lower-bound (open). Part (c) is the matrix unfolding of a fourth-order spike, and its analysis under heavy tails is open.

Regime. Low-degree, with SQ as a companion.

Experiment. Take $d\in\{20,40,80,160\}$, $b\in\{1,4\}$ and $W=|Z|e^{-Z^2/2}$. Fit a linear VAE to $v_t$ and to $\mathrm{vec}(v_tv_t^\top)$, and record the $T$ at which the overlap crosses $1/2$. The prediction is no crossing for the first and a crossing proportional to $d^2\Lambda$ for the second. The statistical side is measurable only for $d\le10$, by maximizing the empirical fourth cumulant over a net.

Pushback. The balance $c_2=0$ is one equation on the label law, the knife edge of correction 1, so a generic law gives no gap and no hardness. For a law with small $c_2=\delta\neq0$ the variance spike reopens the second-order channel. The gap between the polynomial-time and the statistical price is then a factor $\min(d,d^*)$ with $d^*=e_4^2/(\delta^2b^2(\mu_2+b\varsigma^2)^2)$ (heuristic, the degree profile of prop-approximate-degree-price). Batch and noise shrink the window. A designer could impose $c_2=0$ by transforming the labels, but whether that counts as a defence depends on ruling 2, so the aim takes the label law as given.

Other regime and the oracle. This is the computational aim, and its statistical side is part (a). It holds without the oracle. The degree comes from the label law, and the batch noise only attenuates it, so the council's complaint that graded prices live in the record law applies here too.

## 5. Proven now

### thm-update-direction-chi-square-bound: an observer needs updates of the order of the dimension over the per-update directional chi-square

status: sketch

uses: thm-shadow-price-is-generative-exponent, prop-class-pseudorandomness-collapse, conj-optimum-update-variance-price

Every step of the proof is labelled proven. The status stays sketch until a verdict, as the round protocol requires.

Statement.

(a) Let $a_1,\dots,a_T$ be i.i.d. auxiliary variables whose law does not depend on $u$. Given $a=(a_t)_t$, let $w_1,\dots,w_T\in\mathbb R^d$ be independent. Under $P_u$ each $w_t$ has density $\gamma_d(w)\,q_{a_t}(\langle u,w\rangle)$, where $q_a=d\nu_a/d\gamma_1$ for a symmetric law $\nu_a$ on $\mathbb R$. Under $P_\circ$ each $w_t$ has law $\gamma_d$. Put $\kappa=\mathbb E_a\,\chi^2(\nu_a\|\gamma_1)$. If $u$ is uniform on $S^{d-1}$ and $T\kappa\le d/4$, then the joint laws of $(a,w_{1:T})$ satisfy
$$\mathrm{TV}\Big(\int P_u\,du,\,P_\circ\Big)\le\sqrt{\frac{T\kappa}{2d}}.$$

(b) In the setting of conj-optimum-update-variance-price with $\varsigma>0$, let $a_t=(|Y_i|)_{i\in B_t}$ and $\sigma(a_t)^2=b^{-2}\sum_ia_{t,i}^2+\varsigma^2$. Then $w_t=v_t/\sigma(a_t)$ satisfies the hypotheses of (a), with $P_\circ$ induced by $P^\circ$. The law $\nu_a$ is that of $\sigma(a)^{-1}\big(b^{-1}\sum_i\xi_ia_iZ_i+\varsigma N\big)$, with independent signs $\xi_i$, each $Z_i$ drawn from the law of $Z$ given $W=a_i$, and $N\sim N(0,1)$, all independent. So every observer of $v_{1:T}$ has advantage at most $\sqrt{T\kappa/(2d)}$ in telling $P_u$, with $u$ uniform, from $P^\circ$. For any $A>0$, the bound holds with $\kappa_A=\mathbb E[\chi^2(\nu_a\|\gamma_1)\mid\max_ia_i\le A]$ in place of $\kappa$ and an added term $Tb\Pr[|Y|>A]$.

(c) Let $|Y|\le A$ and $c_2\neq0$. If an estimator from $T$ updates has $\Pr[|\langle\hat u,u\rangle|\ge\epsilon]\ge2/3$, then
$$T>\frac d{4\kappa}-\frac{2304\,(A^2+b\varsigma^2)^2}{c_2^2\epsilon^4}.$$

(d) For $b=1$ and $Y=\langle u,X\rangle\xi$, with $\sigma^2=a^2+\varsigma^2$,
$$\chi^2(\nu_a\|\gamma_1)=\frac{a^2+\varsigma^2}{\varsigma\sqrt{2a^2+\varsigma^2}}\cdot\frac{e^{a^4/(2a^2+\varsigma^2)}+e^{-a^4/\varsigma^2}}{2}-1=\frac{a^4(a^2-1)^2}{2\varsigma^4}+O(\varsigma^{-6})$$
at fixed $a$. The untruncated $\kappa$ is infinite. For fixed $A$, $\varsigma^4\kappa_A\to\frac12\mathbb E[a^4(a^2-1)^2\mid a\le A]$ as $\varsigma\to\infty$, and this limit tends to 39 as $A\to\infty$. Against $\beta^2/2=2/(1+\varsigma^2)^2$ the ratio tends to $19.5=1+\mathrm{Var}(Z^4-Z^2)/c_2^2$.

Proof.

Step 1, the structure in (b) (proven). Write $X_i=Z_iu+X_{i\perp}$ and $P_\perp=I_d-uu^\top$. Given $a$, the component of $v_t$ along $u$ is $b^{-1}\sum_i\xi_ia_iZ_i+\langle u,\zeta_t\rangle$, and the orthogonal component is $b^{-1}\sum_i\xi_ia_iX_{i\perp}+P_\perp\zeta_t$. Given $a$ and $(\xi_i,Z_i)_i$, each $\xi_iX_{i\perp}$ has law $N(0,P_\perp)$, because $X_\perp$ is symmetric and independent of $(Z,W,\xi)$. So the orthogonal component has law $N(0,\sigma(a)^2P_\perp)$ and is independent of the component along $u$, whose law is symmetric because the $\xi_i$ are. Under $P^\circ$ the sign of $Y_i$ is independent of $X_i$, so given $a$ the update has law $N(0,\sigma(a)^2I_d)$. The law of $a$ is that of $|Y|$ under both $P_u$ and $P^\circ$, and it does not depend on $u$. Batches and noise are fresh at each step, so the $w_t$ are independent given $a$. The density of $w_t$ given $a_t$ is $\gamma_d(w)q_{a_t}(\langle u,w\rangle)$, and $\nu_a$ has a density because $\varsigma>0$.

Step 2, one update (proven). Let $\hat c_k(a)=\mathbb E_{\nu_a}h_k$. Symmetry gives $\hat c_k(a)=0$ for odd $k$, and Parseval gives $\sum_{k\ge1}\hat c_k(a)^2=\chi^2(\nu_a\|\gamma_1)$. For unit $u,u'$ with $\rho=\langle u,u'\rangle$, the pair $(\langle u,G\rangle,\langle u',G\rangle)$ with $G\sim\gamma_d$ is standard Gaussian with correlation $\rho$. Mehler's identity, as in part 2 of thm-shadow-price-is-generative-exponent, gives
$$\mathbb E\big[q_a(\langle u,G\rangle)\,q_a(\langle u',G\rangle)\big]=1+\sum_{k\text{ even},\,k\ge2}\hat c_k(a)^2\rho^k\le1+\rho^2\chi^2(\nu_a\|\gamma_1),$$
since $0\le\rho^k\le\rho^2$ for even $k\ge2$.

Step 3, $T$ updates (proven). The likelihood ratio of the mixture to $P_\circ$ is $L=\int\prod_tq_{a_t}(\langle u,w_t\rangle)\,du$. This is the second-moment method of prop-class-pseudorandomness-collapse (a) with non-identical samples. Fubini, Step 2 and the independence of the $a_t$ give
$$\mathbb E_{P_\circ}L^2=\mathbb E_{u,u'}\prod_t\mathbb E_{a_t}\Big(1+\sum_{k\ge2}\hat c_k(a_t)^2\rho^k\Big)\le\mathbb E_{u,u'}(1+\rho^2\kappa)^T\le\mathbb E_{u,u'}\,e^{T\kappa\rho^2}.$$

Step 4, the sphere (proven). For independent uniform $u,u'$, $\rho^2$ has law $\mathrm{Beta}(\frac12,\frac{d-1}2)$. Hence $\mathbb E\rho^{2k}=(\frac12)_k/(\frac d2)_k\le(\frac12)_k(\frac2d)^k=\mathbb E(G_1^2/d)^k$ for $G_1\sim N(0,1)$, where $(x)_k$ is the rising factorial. Both moment series have nonnegative terms, so $\mathbb Ee^{\lambda\rho^2}\le\mathbb Ee^{\lambda G_1^2/d}=(1-2\lambda/d)^{-1/2}$ for $0\le\lambda<d/2$.

Step 5, conclusion of (a) and (b) (proven). Put $x=2T\kappa/d\le\frac12$. Then $\chi^2=\mathbb E_{P_\circ}L^2-1\le(1-x)^{-1/2}-1\le x$, by convexity and the value $\sqrt2-1<\frac12$ at $x=\frac12$. So $\mathrm{TV}\le\frac12\sqrt{\chi^2}\le\sqrt{T\kappa/(2d)}$. Each $v_t=\sigma(a_t)w_t$ is a function of $(a,w)$, so data processing removes $a$. For the truncation, the event $E=\{\max_{t,i}a_{t,i}\le A\}$ depends on $a$ alone and has the same probability under both laws, at least $1-Tb\Pr[|Y|>A]$. Conditioning on $E$ keeps the $a_t$ i.i.d. and leaves Step 1 unchanged, and $\mathrm{TV}(P,Q)\le\Pr[E^c]+\mathrm{TV}(P(\cdot\mid E),Q(\cdot\mid E))$.

Step 6, part (c) (proven). Draw $T'$ fresh updates and form $S=\frac1{T'}\sum_{t'}\big(b\langle\hat u,v_{t'}\rangle^2-\mu_2-b\varsigma^2\big)$. By the covariance of conj-optimum-update-variance-price its mean is $c_2\langle\hat u,u\rangle^2$ under $P_u$ and $0$ under $P^\circ$. With $U_i=Y_i\langle\hat u,X_i\rangle$, $\mathbb EU_i^2\le A^2$ and $\mathbb EU_i^4\le3A^4$, so $\mathbb E(\sum_iU_i)^4\le6b^2A^4$ and $b^2\mathbb E\langle\hat u,v\rangle^4\le8b^2(6A^4/b^2+3\varsigma^4)\le48(A^2+b\varsigma^2)^2$. Chebyshev's inequality then puts $S$ within $|c_2|\epsilon^2/2$ of its mean with probability at least $11/12$ once $T'=2304(A^2+b\varsigma^2)^2/(c_2^2\epsilon^4)$. The test that accepts when $|S|>|c_2|\epsilon^2/2$ has advantage at least $\frac23\cdot\frac{11}{12}-\frac1{12}=\frac{19}{36}>\frac12$. If $(T+T')\kappa\le d/4$, part (b) bounds every advantage by $8^{-1/2}<\frac12$, a contradiction.

Step 7, part (d) (proven). Here $W=|Z|$, and $Z$ given $W=a$ is $\pm a$, so $\nu_a$ is the law of $(\pm a^2+\varsigma N)/\sigma$. Let $\varphi_s$ be the centred Gaussian density of variance $s^2$. For $2\sigma^2>\varsigma^2$,
$$\int\frac{\varphi_\varsigma(x-m)\varphi_\varsigma(x-m')}{\varphi_\sigma(x)}dx=\frac{\sigma^2}{\varsigma\sqrt{2\sigma^2-\varsigma^2}}\exp\frac{\varsigma^2(m^2+m'^2)-\sigma^2(m-m')^2}{2\varsigma^2(2\sigma^2-\varsigma^2)}.$$
Averaging over $m,m'\in\{\pm a^2\}$ gives the closed form, with exponent $a^4/(2a^2+\varsigma^2)$ for equal signs and $-a^4/\varsigma^2$ for opposite ones. Put $x=a^2/\varsigma^2$. The prefactor is $1+x^2/2+O(x^3)$, the average of the exponentials is $1-a^2x^2+a^4x^2/2+O(x^3)$, and their product is $1+\frac{x^2}{2}(a^2-1)^2+O(x^3)$, uniformly for $a\le A$. For large $a$ the closed form grows as $a\,e^{a^2/2-\varsigma^2/4}/(2\sqrt2\,\varsigma)$, against the density $\sqrt{2/\pi}\,e^{-a^2/2}$ of $a$, so $\kappa=\infty$. The moments $\mathbb EZ^4=3$, $\mathbb EZ^6=15$ and $\mathbb EZ^8=105$ give $\mathbb E[a^4(a^2-1)^2]=78$ and $\mathrm{Var}(Z^4-Z^2)=74$, and $c_2=2$. $\square$

Other regime and the oracle. The bound holds for every observer, unbounded ones included, so it is statistical, and it needs no oracle. It sees only the total $\chi^2$ of an update and not its degree, so in the computational regime it is the weaker side, which is all conj-update-moment-degree-gap asks of it. Part (a) is the second-moment method of NGCA lower bounds, and I do not know this form in print (from memory, unverified). The new parts are the exact conditional structure (b) of an SGD update at the optimum, and the numbers of (d). The auxiliary $a$ costs the factor 19.5 of (d) against plain PCA at $b=1$, and a norm-weighted spectral estimator may recover part of it (heuristic).

## Sources cited from memory

None of these was opened. Each is a candidate search row for the summary.

- Tipping and Bishop, J. R. Stat. Soc. B, 1999. Probabilistic PCA and the linear VAE's optimum.
- Davis and Kahan, SIAM J. Numer. Anal., 1970. The $\sin\theta$ theorem.
- Mondelli and Montanari, Found. Comput. Math., 2019. The weak recovery threshold of phase retrieval.
- Baik, Ben Arous and Péché, Ann. Probab., 2005. The spiked covariance transition, for the collapse predicted in conj-optimum-update-variance-price.
- Ganju, Wang, Yang, Gunter and Borisov, ACM CCS 2018. Property inference with shadow models.
