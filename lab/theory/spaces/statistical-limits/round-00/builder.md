# Round 00 of statistical-limits, the literature round

Builder: the space session of `statistical-limits`, 2026-10-25.

This round states what the literature proves about an unbounded adversary that
attacks a learning procedure, priced in samples, training runs or queries. Every
statement below was read on 2026-10-25 in the PDF under
`lib/literature/pdfs/<venue>/`, and its note under `lib/literature/notes/<venue>/`
was filled in the same session. The round then names the gaps and proposes three
aims. No challenge is open, since this is the first round of the space.

Notation used throughout. $\mathrm{TV}$ is total variation and $\mathrm{KL}$ the
Kullback and Leibler divergence. For $p,q\in[0,1]$, $\mathrm{kl}(p\|q)$ is the
divergence between Bernoulli laws of means $p$ and $q$. $I(\cdot;\cdot)$ and
$I(\cdot;\cdot\mid\cdot)$ are mutual and conditional mutual information in nats.
The oracle vocabulary (learning function $\mathsf L$, Train, Eval, bottom and top
oracle, drawn-seed and coupled discipline, deterministic kernels) is that of the
accepted objects `def-learning-oracle`, `def-learning-oracle-model` and
`def-degenerate-oracles` in `lib/theory/booklet.pdf`.

## Responses to challenges

None. This is the first round of the space.

## Literature on membership inference priced in samples and training runs

### fact-hsu-membership-sample-gap: reference samples that membership inference needs against noisy mean estimation

status: borrowed

uses: none

Statement. Key HSU25, Haghifam, Smith and Ullman, The Sample Complexity of
Membership Inference and Privacy Auditing. The library holds arXiv 2508.19458v1 of
26 August 2025, and every number below is from that version. The setting is
Definition 2.1. Fix $n,m,d$, a family $\mathcal P$ of laws on $\mathbb R^d$ and a
class of mean estimators. A map $\psi_m$ of $m$ auxiliary samples
$\mathbf Y^m=(Y_1,\dots,Y_m)$, the release $\hat\mu$ and a target point is an
$m$-sample-based attack when, for every estimator $\mathcal A$ in the class and
every $\mathcal D\in\mathcal P$, with
$(X_0,X_1,\dots,X_n,Y_1,\dots,Y_m)\sim\mathcal D^{\otimes(n+m+1)}$ and
$\hat\mu=\mathcal A(X_1,\dots,X_n)$, both of the following hold.

$$\Pr[\psi_m(\mathbf Y^m,\hat\mu,X_0)=\mathrm{OUT}]\ge0.51,\qquad\Pr[\psi_m(\mathbf Y^m,\hat\mu,X_1)=\mathrm{IN}]\ge0.51.$$

The estimator $\mathcal A_{n,\rho}$ of Definition 2.4 outputs
$\hat\mu=\frac1n\sum_{i\le n}X_i+\rho Z$ with $Z\sim\mathcal N(0,\Sigma)$ independent
of the data. $\mathcal P_d$ is the family of all Gaussians $\mathcal N(\mu,\Sigma)$
on $\mathbb R^d$ with $\Sigma$ positive definite (Definition 2.3). Write
$d^\star=n+n^2\rho^2$.

1. Proposition 2.5. There is a universal $c$ such that an attacker that knows
   $\mathcal D$ succeeds in the sense of Definition 2.1 when $d\ge c\,d^\star$, and
   $\mathrm{TV}((X_1,\hat\mu),(X_0,\hat\mu))\le\sqrt{d/d^\star}$. The paper attributes
   the first part to Dwork, Smith, Steinke, Ullman and Vadhan and calls the second
   a simple calculation. It proves neither.
2. Theorem 3.1. There are universal $c_1,c_2$ such that, if $d>c_1d^\star$ and
   $m\le c_2d^\star$, no $(\mathcal P_d,\{\mathcal A_{n,\rho}\},n,m)$-sample-based
   attack exists.
3. Theorem 3.3. There is a universal $c>1$ such that, for $0<\rho<1$, $m\ge cd$ and
   $d\ge c\,d^\star$, a $(\mathcal P_d,\mathfrak A_{n,d,\rho},n,m)$-sample-based attack
   exists, where $\mathfrak A_{n,d,\rho}$ (Definition 3.2) holds the symmetric
   estimators whose output lies within Mahalanobis distance $\sqrt{2\rho^2d}$ of the
   empirical mean with probability at least $0.99$. Remark 3.4 notes that the two
   bounds match at $d\asymp d^\star$.

The paper calls its Theorem 1.1 the informal version of Theorem 3.1, so the two
numbers the registers record name one result.

Proof. Borrowed (proven in HSU25, appendix proofs not read in this session). The
hard instances have spiked covariance $I_d+\sigma^2UU^\top$ with the range of $U$
uniform over $k$-dimensional subspaces. Le Cam's mixture bound (Lemma 2.6) reduces
the claim to a bound on the total variation between two mixtures. A reduction from
$m$ auxiliary samples to none in dimension $d-2m$ (display (5) of §1.3.1) carries
the main step.

The other regime. The attacker of Definition 2.1 is unbounded and knows the
estimator. It can therefore simulate any number of training runs on its own
samples, and the price is in samples alone with training runs free. Under the
learning oracle the attacker reaches the learning function only through Train, so
the price gains a second coordinate, which `def-uniform-security-profile` below
makes explicit. The attack of Theorem 3.3 is an empirical covariance followed by an
inner-product test, which runs in polynomial time (proven, by the construction in
§3). In this instance the statistical and the computational sample prices
therefore agree up to constants.

### fact-hsu-gap-prices-covariance: with the covariance known the sample price falls to the trainer's

status: borrowed

uses: fact-hsu-membership-sample-gap

Statement. Key HSU25, Theorem 4.1. Let $\mathcal P^{\mathrm{id.cov}}_d$ be the
Gaussians $\mathcal N(\mu,I_d)$ (Definition 2.3). There is a universal $c$ such
that, if $n\ge4$, $m\ge2$ and $d<c\,(n+n^2\rho^2+n^2/m)$, no
$(\mathcal P^{\mathrm{id.cov}}_d,\{\mathcal A_{n,\rho}\},n,m)$-sample-based attack
exists. The paper attributes to Dwork et al. an attack that succeeds once
$d\gtrsim n+n^2\rho^2+n^2/m$, and it does not prove that direction. At
$d\asymp d^\star$ an attack then needs $m\gtrsim\min\{n,1/\rho^2\}$ samples, and by
the attributed attack this many suffice. Remark 4.2 compares the two regimes. For
$\rho>1/\sqrt n$, knowing the covariance lowers the price from order $n^2\rho^2$ to
order $n$.

Proof. Borrowed (proven in HSU25, the KL chain rule over a Gaussian prior on $\mu$
in the proof sketch of Theorem 4.1, appendix not read).

The other regime. Theorem 3.1 against Theorem 4.1 shows what the sample price of
Theorem 3.1 measures. It measures the attacker's ignorance of $\Sigma$, not a
difficulty of the attack itself (proven in the regime $d\asymp d^\star$ by the two
theorems). The register's wording, a price of ignorance and not of difficulty, is
therefore exact. A price of an unbounded attacker in samples is always a price of
not knowing the data law, since an attacker that knows it needs no samples. Its
size depends on which part of the law the attacker lacks.

### fact-yeom-dp-bounds-membership-advantage: differential privacy bounds the advantage of an informed membership attacker

status: borrowed

uses: none

Statement. Key YGFJ18, Yeom, Giacomelli, Fredrikson and Jha, Privacy Risk in
Machine Learning, IEEE CSF 2018, unabridged version. Experiment 1 draws
$S\sim\mathcal D^n$, sets $A_S=A(S)$, draws $b$ uniform in $\{0,1\}$, draws $z$
uniform from $S$ if $b=0$ and $z\sim\mathcal D$ if $b=1$, and hands the adversary
$(z,A_S,n,\mathcal D)$. Definition 4 sets
$\mathrm{Adv}^M=2\Pr[\text{the adversary guesses }b]-1$, which equals
$\Pr[\hat b=0\mid b=0]-\Pr[\hat b=0\mid b=1]$. Theorem 1 states that an
$\varepsilon$-differentially private $A$ gives $\mathrm{Adv}^M\le e^\varepsilon-1$
for every adversary.

Proof. Borrowed (proven in YGFJ18, the proof below Theorem 1 replaces $z_i$ by an
independent $z'$ and applies the DP inequality, read in full).

The other regime. The adversary of Experiment 1 receives $\mathcal D$ itself, so
the experiment prices neither samples nor training runs. Theorem 1 holds for
unbounded adversaries and needs no computational assumption. It is the informed
end of every price in this space.

### fact-yeom-generalization-error-gives-advantage: a loss-threshold attack gains the generalization error

status: borrowed

uses: fact-yeom-dp-bounds-membership-advantage

Statement. Key YGFJ18, Theorem 2. If the loss satisfies $\ell(A_S,z)\le B$ for all
$S$ and all $z$ drawn from $S$ or from $\mathcal D$, Adversary 1 queries the model
at $z$ and outputs $1$ with probability $\ell(A_S,z)/B$. Its membership advantage
equals $R_{\mathrm{gen}}(A)/B$, the average generalization error of Definition 3
divided by $B$.

Proof. Borrowed (proven in YGFJ18, a two-line computation below Theorem 2, read).

The other regime. Adversary 1 makes one query and runs in constant time. It needs
no sample and no training run. So an overfit trainer hands every attacker,
bounded or not, an advantage equal to its generalization gap.

### fact-lira-priced-in-training-runs: the likelihood-ratio attack spends 64 to 256 shadow training runs

status: borrowed

uses: fact-lira-low-fpr-yeom-game

Statement. Key CCNSTT22, Carlini, Chien, Nasr, Song, Terzis and Tramèr, Membership
Inference Attacks From First Principles, IEEE S&P 2022. Algorithm 1 (§IV-C) trains
$N$ shadow models on datasets drawn from the data distribution, half with the target
example and half without. It fits a Gaussian to the logit-scaled confidences
$\phi(f(x)_y)=\log\frac{f(x)_y}{1-f(x)_y}$ of each half and returns the likelihood
ratio at the target model's confidence. The offline variant trains OUT models only
and applies the one-sided test of equation (4). §V-A uses $N=64$ for ImageNet and
$N=256$ for the other datasets, with each example in exactly half of the shadow
training sets, so one set of $N$ runs serves every target. §VI-B and Fig. 9 report,
for the true-positive rate at false-positive rate $0.1\%$, diminishing gains beyond
$64$ shadow models and quick deterioration below it. Below $64$ a variance pooled
over examples does better than a per-example variance, and at $1024$ shadow models
pooling lowers the true-positive rate from $8.4\%$ to $7.9\%$. §VI-D (Fig. 10,
CINIC-10, 128 OUT models) finds the attack unchanged when shadow and target training
sets are disjoint.

Proof. Borrowed. Every statement above is empirical, on the models and datasets of
§V. The paper states no theorem.

The other regime. The Gaussian fit replaces the law of the view by four numbers per
example. The accepted `thm-reference-access` shows that on atomless views no attack
reaches the total variation at a rate uniform over learning functions. So the price
LiRA pays is finite only because of its parametric assumption (heuristic, the
assumption is that logit-scaled confidences are Gaussian per example, which §IV-C
checks on CIFAR-10 in Fig. 4).

### fact-lira-low-fpr-yeom-game: the LiRA game is the Yeom game with a sampled training set

status: borrowed

uses: fact-yeom-dp-bounds-membership-advantage

Statement. Key CCNSTT22, Definition 1 in §III-A, not §VI-A as the register records.
The challenger samples a training set $D$ from the distribution and trains
$f_\theta\leftarrow\mathcal T(D)$. It flips $b$, and sends a fresh point from the
distribution if $b=0$ and a point of $D$ if $b=1$. The adversary has query access to
the distribution and to $f_\theta$ and outputs a guess. The paper says the game is
inspired by Yeom et al. and Jayaraman et al.

Proof. Borrowed (a definition, read in full).

The other regime. Query access to the distribution is the resource that HSU25 prices
in samples. In LiRA it is spent on shadow training sets, and the paper reports the
count of training runs and not the count of samples.

## Literature on reconstruction and information bounds on a release

### fact-balle-reconstruction-robustness-definition: reconstruction robustness and its oblivious baseline

status: borrowed

uses: none

Statement. Key BCH22, Balle, Cherubin and Hayes, Reconstructing Training Data with
Informed Adversaries, IEEE S&P 2022. Definition 1 is the informed adversary. It
holds the fixed dataset $D^-$ of $n-1$ points, the released parameters $\theta$, the
training algorithm and optional side knowledge. Definition 2 is reconstruction
robustness. For a prior $\pi$ on the data space $\mathcal Z$ and an error
$\ell:\mathcal Z\times\mathcal Z\to\mathbb R_{\ge0}$, a mechanism $M$ is
$(\eta,\gamma)$-ReRo when, for every $D^-$ and every map $R:\Theta\to\mathcal Z$,

$$\Pr_{Z\sim\pi,\ \theta\sim M(D^-\cup\{Z\})}[\ell(Z,R(\theta))\le\eta]\le\gamma.$$

The baseline, defined in §VII-B without a number, is
$\kappa_{\pi,\ell}(\eta)=\sup_{z_0\in\mathcal Z}\Pr_{Z\sim\pi}[\ell(Z,z_0)\le\eta]$,
the success of the best attack that ignores $\theta$. The register entry records a
dispute between Definition 1 and Definition 2. The PDF settles it. Definition 2 is
reconstruction robustness and Definition 1 the adversary.

Proof. Borrowed (definitions, read in full). The paper notes after Definition 2 that
a deterministic $R$ loses nothing, since the maximum a posteriori attack attains the
supremum.

The other regime. The definition quantifies over every map $R$, measurable or not
efficient, so it is statistical. It holds $D^-$ and the algorithm fixed and known.
The attacker's ignorance is confined to the prior $\pi$.

### fact-balle-dp-bounds-reconstruction: Rényi and pure differential privacy bound reconstruction by the baseline

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Statement. Key BCH22, §VII-B and §VII-C. Write $\kappa=\kappa_{\pi,\ell}(\eta)$.

1. Theorem 2. An $(\alpha,\varepsilon)$-RDP mechanism is $(\eta,\gamma)$-ReRo with
   $\gamma=(\kappa e^\varepsilon)^{(\alpha-1)/\alpha}$.
2. Corollary 3. An $\varepsilon$-DP mechanism is $(\eta,\kappa e^\varepsilon)$-ReRo.
3. Corollary 4. A $\rho$-zCDP mechanism with $\rho<\log(1/\kappa)$ is ReRo with
   $\gamma=\exp(-(\sqrt{\log(1/\kappa)}-\sqrt\rho)^2)$.
4. Propositions 6 and 7. For the uniform prior on the unit ball of $\mathbb R^d$, or
   a Gaussian prior with $\sigma\ge2\eta/\sqrt d$, and $\ell_2$ error, $\varepsilon=o(d)$
   or $\rho=o(d)$ gives $\gamma=e^{-\Omega(d)}$.
5. Theorem 5. Let $\Pi$ be the priors on two points $z\neq z'$ with mass
   $p=1/(e^\varepsilon+1)$ on $z$. A mechanism that is $(\eta,\gamma)$-ReRo for the
   $0/1$ error and every prior in $\Pi$ is $(\varepsilon,\delta)$-DP with
   $\delta=\max\{0,(e^\varepsilon+1)\gamma-e^\varepsilon\}$.

Proof. Borrowed (proven in BCH22, the appendix proofs of Theorem 2 and Theorem 5
read). Theorem 2 is a change of measure to $M(D_{z_0})$ followed by Hölder's
inequality.

The other regime. All five bounds hold against unbounded attackers and say nothing
about how many samples or runs an attacker spends. They need a mechanism with a
known privacy parameter. Without differential privacy inside training the
accepted oracle theory certifies the matching divergence from coupled runs, and
`prop-privacy-bound-bounds-inversion` turns it into a reconstruction bound.

### fact-reconstruction-query-lower-bounds: how many trained models a reconstruction attacker must see

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Statement. Key ML24, Mukherjee and Lokam, arXiv 2303.16372v6 of 11 January 2024.
The game of §3 fixes $D^-$, known to both sides. The learner trains on
$D^-\cup\{z\}$ for a target $z$ in a compact metric space $(\mathcal Z,\rho)$, and
the adversary receives $n$ independent draws $h_1,\dots,h_n\sim M(D^-\cup\{z\})$,
the paper's queries. The value is
$V(M,n)=\inf_{\mathcal A}\sup_{z}\mathbb E[\rho(\mathcal A(h_1,\dots,h_n),z)^2]$
(display (6)). Theorem 9 states, for every $(\varepsilon,\delta)$-DP learner, that
$V(M,n)\gtrsim\mathrm{diam}(\mathcal Z)^2\,(2(1-\delta)/(e^\varepsilon+1))^n$, so
reaching expected squared error $\beta^2$ needs
$n\ge\Omega\big(\ln(\mathrm{diam}(\mathcal Z)^2/\beta^2)/\ln\frac{e^\varepsilon+1}{2(1-\delta)}\big)$.
Theorem 10 attains this order for a two-point space with a randomized-response
learner. Corollary 12 extends the lower bound to $(\alpha,\varepsilon)$-RDP, and
Theorems 13 and 14 treat metric DP on locally compact spaces. The register's
pointer, Theorems 1 and 2, names the informal statements of §1.

Proof. Borrowed (proven in ML24, §3 and §4 read, appendix not read). §4.1 also
states that the lower bound of Guo et al. 2022, Theorem 1, is vacuous for
$\varepsilon<\ln(1+d/4)$, with the proof in Appendix B.6, not read.

The other regime. The unit of ML24 is the number of independent models trained on the
target's own dataset, which is a count of the trainer's runs that the attacker
observes, not of runs it makes. The bound needs differential privacy inside training.

### fact-dinur-nissim-reconstruction-thresholds: exponential and polynomial reconstruction thresholds for subset sums

status: borrowed

uses: none

Statement. Key DN03, Dinur and Nissim, Revealing Information while Preserving
Privacy, PODS 2003. A database is a bit vector $d\in\{0,1\}^n$ answered by an
algorithm $A$ within perturbation $E$ when $|A(q)-\sum_{i\in q}d_i|\le E$ for every
$q\subseteq[n]$ (Definitions 1 and 2). It is $t(n)$-non-private when for every
$\varepsilon>0$ a machine of time $t(n)$ outputs $c$ with Hamming distance below
$\varepsilon n$ from $d$ with probability at least $2/3$ (Definition 3). Theorem 2
(§3.1) says perturbation $o(n)$ gives $\exp(n)$-non-privacy, by querying all $2^n$
subsets. Theorem 3 (§3.2) says perturbation $o(\sqrt n)$ gives poly$(n)$-non-privacy,
by $n(\log n)^2$ random queries and a linear program. Theorem 5 gives, for the
uniform prior and time bound $T(n)>\mathrm{polylog}(n)$, a perturbation of order
$\tilde O(\sqrt{T(n)})$ that keeps $(T(n),\delta)$-privacy.

Proof. Borrowed (proven in DN03, statements and the proof of Theorem 2 read).

The other regime. This is the one place in the list where the statistical and the
computational price differ, by perturbation $o(n)$ against $o(\sqrt n)$. The unit is
queries to the database, not a learning resource.

### fact-pac-privacy-mutual-information-bound: mutual information bounds the posterior gain of any reconstruction

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Statement. Key XD23, Xiao and Devadas, PAC Privacy, CRYPTO 2023. For a mechanism
$M$, a data law $\mathcal D$ and a success criterion $\rho(\tilde X,X)\in\{0,1\}$,
Definition 3 sets the optimal prior success $1-\delta^\rho_o=\sup_{\tilde X}\Pr_{X\sim\mathcal D}[\rho(\tilde X,X)=1]$.
The adversary knows $\mathcal D$ and $M$ (Definition 1). Theorem 1 states that the
failure probability $\delta$ of every adversary satisfies

$$\mathrm{kl}(\delta\|\delta^\rho_o)\le I(X;M(X)).$$

Corollary 1 gives $\delta^\rho_o-\delta\le\sqrt{I(X;M(X))/2}$ by Pinsker's
inequality. Remark 1 states the version with side knowledge $\mathrm{Adv}$, with
$I(X;M(X)\mid\mathrm{Adv})$ and the prior success conditional on $\mathrm{Adv}$.

Proof. Borrowed (proven in XD23, by the data processing inequality for
$f$-divergences, Appendix A not read).

The other regime. The bound is statistical and needs the data law to be known to the
adversary. §2, paragraph Lack of Knowledge, says the framework cannot quantify the
extra hardness an adversary faces when it does not know $\mathcal D$, which is the
quantity HSU25 prices in samples.

### fact-pac-privacy-gaussian-release-bound: a Gaussian release has mutual information set by its covariance, certified by simulations

status: borrowed

uses: fact-pac-privacy-mutual-information-bound

Statement. Key XD23. Theorem 3. For every deterministic $M$ and independent
$B\sim\mathcal N(0,\Sigma_B)$,
$I(X;M(X)+B)\le\frac12\log\det(I_d+\Sigma_{M(X)}\Sigma_B^{-1})$. Theorem 4. If
$\|M(X)\|_2\le r$, Algorithm 1 runs $M$ on $m$ independent draws $X^{(k)}\sim\mathcal D$,
estimates $\Sigma_{M(X)}$ and returns a noise covariance with
$I(X;M(X)+B)\le v+\beta$ with confidence $1-\gamma$ once the security parameter $c$
satisfies display (6) in $d$, $m$, $r$ and $\log(4/\gamma)$.

Proof. Borrowed (proven in XD23, appendices C and D not read).

The other regime. The $m$ runs of Algorithm 1 are runs of the mechanism on fresh data
from $\mathcal D$, so the certificate is priced in the trainer's own training runs.
It certifies the mechanism and not an attack. The certificate holds for a black-box
$M$, which is the role of drawn-seed Train calls in the oracle theory.

### fact-zhao-accuracy-forces-attribute-leakage: an accurate representation must leak a correlated attribute

status: borrowed

uses: none

Statement. Key ZCTG20, Zhao, Chi, Tian and Gordon, Trade-offs and Guarantees of
Adversarial Representation Learning for Information Obfuscation, NeurIPS 2020
(arXiv 1906.07902v3). Binary target $Y$ and binary attribute $A$, a feature map
$f:\mathcal X\to\mathcal Z$ and a predictor $h$, with the Markov chain
$X\to Z=f(X)\to\hat Y$ (Lemma 3.4). $\mathcal D_a$ is the law conditional on $A=a$,
$\mathcal D_a^Y$ its marginal on $Y$, and $\mathrm{Err}_a$, $\mathrm{ACC}_a=1-\mathrm{Err}_a$
the conditional error and accuracy. The attribute advantage of Definition 2.2 is
$\mathrm{ADV}(\mathcal H_A)=\max_{h_A\in\mathcal H_A}|\Pr(h_A=1\mid A=1)-\Pr(h_A=1\mid A=0)|$.
Let $\mathcal H_A$ hold all classifiers on $\mathcal Z$, and let $D_{\mathrm{JS}}$ be
the Jensen and Shannon divergence and $d_{\mathrm{JS}}=\sqrt{D_{\mathrm{JS}}}$.
Theorem 3.2 states
$\mathrm{ACC}_0(h\circ f)+\mathrm{ACC}_1(h\circ f)\le2-\frac13D_{\mathrm{JS}}(\mathcal D_0^Y,\mathcal D_1^Y)+\mathrm{ADV}(\mathcal H_A\circ f)$
for every $h$. Theorem 3.3 states that, if
$\mathrm{ADV}(\mathcal H_A\circ f)\le D_{\mathrm{JS}}(\mathcal D_0^Y,\mathcal D_1^Y)$,
then $\mathrm{Err}_0+\mathrm{Err}_1\ge\frac12\big(d_{\mathrm{JS}}(\mathcal D_0^Y,\mathcal D_1^Y)-\sqrt{\mathrm{ADV}(\mathcal H_A\circ f)}\big)^2$.

Proof. Borrowed (proven in ZCTG20, the appendix proofs of Theorems 3.2 and 3.3
read). The key step bounds $D_{\mathrm{JS}}$ of the two induced feature laws by
their total variation, which equals the advantage of the full class.

The other regime. The attacker class is all classifiers, so the bound is
statistical. The register entry `fact-zhao-class-inference-advantage` records that
no lower bound of the paper uses a class restriction, and this reading confirms it.
The theorem is the attribute analogue of the floor that
`conj-reconstruction-label-sandwich` below states for reconstruction.

## Accepted objects this space builds on

The accepted learning-oracle theory supplies three statements on the attacker's
training runs, used by slug and not restated as facts. `thm-black-box-certifiability`
(b) gives one bottom-oracle adversary with $2n$ shadow models within
$2\sqrt{\ln(2|\mathfrak T_{q_E}|)/n}$ of the label-only optimum for every learning
function, and its matching lower bound is open (`prob-shadow-model-lower-bound`).
`thm-coupling-certificate` (b) makes the total variation of the view laws the
best bottom-oracle advantage and the top divergence the best top-oracle advantage.
`thm-reference-access` rules out a rate uniform over learning functions on atomless
views. `lem-needle-lower-bound` bounds certifiers, not adversaries.

## Gaps

1. No theorem prices the training runs of an attacker that reaches the learning
   function only through training. HSU25 prices samples with runs free.
   `thm-black-box-certifiability` (b) is an upper bound. CCNSTT22 measures runs
   under a parametric assumption. ML24 counts runs of the trainer that the attacker
   observes. The lower bound of `prob-shadow-model-lower-bound` is open.
2. The sample price of membership inference is known for one family, Gaussian mean
   estimation (HSU25). The held version v1 states no open problem, and the register
   entry `fact-hsu-single-mechanism-open` cites v2, which the library does not hold.
3. No bound in the list compares reconstruction from an intermediate representation
   with the trainer's own learning problem. BCH22, ML24 and XD23 bound
   reconstruction from a release that carries differential privacy or Gaussian
   noise. ZCTG20 bounds attribute inference against accuracy and not reconstruction.
   For a deterministic and injective representation an unbounded reconstructor wins
   with probability one, so each of these bounds is vacuous there (proven, the
   inverse map is a reconstruction).
4. The budget-to-success curve exists as a proposal for efficient adversaries
   (`def-security-profile-curve` of FORMAL_SECURITY, open). No object defines it for
   unbounded adversaries in learning units, and a naive definition degenerates, as
   `def-uniform-security-profile` shows.
5. The space needs papers the library does not hold. They are Sablayrolles et al., ICML 2019
   (the Bayes-optimal membership attack, recorded in the register), Guo et al. 2022
   (reconstruction bounds from Fisher information, which ML24 restates as its
   Theorem 11), and a textbook statement of the agnostic learning lower bound.

## Aims

### def-uniform-security-profile: the uniform security profile and the price of an unbounded adversary

status: open

uses: fact-hsu-membership-sample-gap, fact-yeom-dp-bounds-membership-advantage, thm-coupling-certificate

Statement. Fix a game, either distinguishing $H_0$ from $H_1$ with advantage
$\Pr[1\mid H_1]-\Pr[1\mid H_0]$ or inverting with success on an event. An instance
$\iota$ fixes everything the procedure draws from, the data laws, the learning
function and the laws of seeds and hardware randomness. Fix a class $\mathfrak J$
of instances and an oracle policy, bottom or top. A budget is a triple
$\beta=(m,N,q)\in\bar{\mathbb N}^3$, ordered coordinatewise, of $m$ reference
samples from the instance's data law, at most $N$ Train calls and at most $q$ Eval
calls on served names. $\mathcal A(\beta)$ is the set of computationally unbounded
adversaries within budget $\beta$, chosen before the instance.
$\mathrm{Succ}_\iota(\mathcal A)$ is the success of $\mathcal A$ on $\iota$.
$\mathrm{Opt}(\iota)$ is the supremum of $\mathrm{Succ}_\iota$ over adversaries that
may depend on $\iota$ and that receive the game's channel outputs and nothing else.
The uniform gap, the uniform security profile and the price at accuracy $a$ are

$$g_{\mathfrak J}(\beta)=\inf_{\mathcal A\in\mathcal A(\beta)}\ \sup_{\iota\in\mathfrak J}\big(\mathrm{Opt}(\iota)-\mathrm{Succ}_\iota(\mathcal A)\big),\qquad\mathrm{price}_{\mathfrak J}(a)=\min\{\beta:\ g_{\mathfrak J}(\beta)\le a\},$$

where the minimum is the set of minimal budgets in the coordinatewise order. A
threshold form serves HSU25. For $s>0$ and the subclass $\mathfrak J_s$ of instances
with $\mathrm{Opt}(\iota)\ge s'$ for a stated $s'>s$, the price at level $s$ is the
set of minimal $\beta$ such that one $\mathcal A\in\mathcal A(\beta)$ has
$\mathrm{Succ}_\iota(\mathcal A)\ge s$ on every $\iota\in\mathfrak J_s$.

Sketch of why the definition has this form.

1. A single instance gives nothing. If $\mathfrak J=\{\iota\}$, then
   $g_{\mathfrak J}(\beta)=0$ at every budget, since the adversary may hard-wire a
   near-optimal test for $\iota$ (proven, by the definition of $\mathrm{Opt}$, and
   attained at $\gamma=1$ by the set of (F1) of the oracle theory). So every
   unbounded profile is a property of a class, that is of what the adversary does not
   know, and every price in it is a price of ignorance paid in learning units.
2. The informed end. At $\beta=(\infty,\infty,q)$ with the instance's data law and
   learning function recoverable from unlimited samples and calls, the gap is the
   difference between $\mathrm{Opt}$ and what unlimited sampling attains, which is
   zero on finite views (proven, by the plug-in rate of `thm-coupling-certificate`
   (a)(ii) as $n\to\infty$) and need not be zero on atomless views
   (`thm-reference-access`).
3. HSU25 is a point. With $\mathfrak J$ the instances
   $(\mathcal N(\mu,\Sigma),\mathcal A_{n,\rho})$, $d>c_1d^\star$ and the algorithm
   known, Theorem 3.1 shows that every budget with $m\le c_2d^\star$ fails the
   threshold form at level $0.02$, whatever $N$ is, since a known algorithm makes
   training runs free (proven, by fact-hsu-membership-sample-gap). Theorem 4.1
   shows that the price moves to order $\min\{n,1/\rho^2\}$ when $\mathfrak J$ fixes
   $\Sigma=I_d$.
4. The learning-oracle results are points on the $N$ axis. With $\mathfrak J$ all
   learning functions and the query channel, `thm-black-box-certifiability` (b)
   bounds $g_{\mathfrak J}(0,2n,q_E)$ by $2\sqrt{\ln(2|\mathfrak T_{q_E}|)/n}$.

What would settle it. The definition is settled when a discussant round accepts it
as well posed, meaning that $\mathrm{Succ}$ is defined for every adversary in
$\mathcal A(\beta)$ and that minimal budgets exist, and when at least one theorem of
this space computes $\mathrm{price}_{\mathfrak J}$ to constant factors on one axis.
`conj-shadow-run-price-finite-views` is that theorem on the $N$ axis. A definition
alone is not a result, so the aim is the pair.

Regime. Statistical. The adversary is unbounded and the budget counts learning
resources only.

Experiment. On a class the experimenter can sample, such as the planted family of
`conj-shadow-run-price-finite-views` or the noisy mean estimator of HSU25, run a
fixed attack at a grid of budgets and record its worst gap over sampled instances.
The measured curve upper-bounds the attack's own gap and hence $g_{\mathfrak J}$
only on the sampled instances. Lower bounds on the price come from theorems. The
space `oracle-and-measurement` owns the measurement.

The other regime. For a computationally bounded adversary the profile is not
degenerate on a single instance, since a bounded adversary cannot hard-wire an
arbitrary test. The single-instance profile is then the object of
`def-security-profile-curve` and of the space `computational-limits`. The
statistical profile is the floor it is compared with.

### conj-shadow-run-price-finite-views: the training-run price of distinguishing two training inputs on finite views

status: sketch

uses: def-uniform-security-profile, thm-black-box-certifiability, thm-coupling-certificate, def-degenerate-oracles

Statement. One learning node trains $x_b$ under $H_b$, with $x_0\neq x_1$ known to
the adversary, and its model reaches the adversary through a deterministic channel
$\kappa$ onto a finite view space $\mathcal V$ with $k=|\mathcal V|\ge4$. $P_b$ is
the view law at $x_b$ and $\mathrm{Opt}=\mathrm{TV}(P_0,P_1)$ under the bottom
oracle. Let $\mathfrak J_{\mathrm{det}}$ be the learning functions with deterministic
kernels and $\mathfrak J_{\mathrm{all}}$ all learning functions. The conjecture has
three parts, with absolute constants $c,C>0$.

1. Upper bound, every learning function, bottom oracle. The adversary that makes
   $N/2$ drawn-seed Train calls at each input and accepts on
   $\{v:\hat p_1(v)>\hat p_0(v)\}$ for the empirical view laws has
   $\mathrm{TV}(P_0,P_1)-\mathrm{Adv}\le2\sqrt{2k/N}$. So
   $g_{\mathfrak J_{\mathrm{all}}}(0,N,0)\le2\sqrt{2k/N}$.
2. Lower bound, bottom oracle. For every $a\le1/8$, every adversary whose gap is at
   most $a$ on every member of $\mathfrak J_{\mathrm{det}}$ makes
   $N\ge c\,k/a^2$ Train calls, whatever inputs, seeds, Eval and Open calls it uses.
   The same holds over $\mathfrak J_{\mathrm{all}}$ under the top oracle.
3. Top oracle, deterministic kernels. Over $\mathfrak J_{\mathrm{det}}$ one adversary
   with two Train calls has gap zero. Its advantage is the divergence probability
   $\Pr_\rho[\kappa(\mathsf L(x_0;\rho))\neq\kappa(\mathsf L(x_1;\rho))]$, which is
   the top optimum by `thm-reference-access` and is at least
   $\mathrm{TV}(P_0,P_1)$ by `thm-coupling-certificate` (b).

So under the bottom oracle the price is $\Theta(k/a^2)$ Train calls, against the
trainer's one run, and the honest seed is worth $\Theta(k/a^2)$ Train calls when
training has deterministic kernels. For $q$ label queries at a fixed query set $U$
with $|U|=q$ and $C$ labels, $k=C^q$. This settles `prob-shadow-model-lower-bound`
when $|U|=q_E$ and leaves its factor $\ln|U|$ open.

Sketch. Part 1. For every set $A$,
$|P(A)-\hat p(A)|\le\frac12\|P-\hat p\|_1$, so the accepted set loses at most
$\|\hat p_0-P_0\|_1+\|\hat p_1-P_1\|_1$ against the optimal set, and
$\mathbb E\|\hat p_b-P_b\|_1\le\sqrt{2k/N}$ by Cauchy and Schwarz (proven, a
standard computation). Part 2 is an Assouad argument. Pair the views into $k/2$
pairs and, for a sign vector $\sigma\in\{\pm1\}^{k/2}$, let $P_0^\sigma$ put mass
$(1\pm\sigma_i\delta)/k$ on the two views of pair $i$ and let $P_1$ be uniform. The
seed is a pair $(\rho_a,\rho_b)$ uniform on $[0,1)^2$, the model at $x_0$ is the
$P_0^\sigma$-quantile of $\rho_b$, the model at $x_1$ the uniform quantile of
$\rho_a$, and every other input trains to one fixed model. Then each Train call at
$x_0$ on a seed not yet used at $x_0$ returns a fresh draw of $P_0^\sigma$, every
other call returns nothing that depends on $\sigma$, and reusing a seed across the
two inputs gives independent coordinates. The gap of any adversary is
$\frac\delta k\sum_i(1-\sigma_is_i)$ for scores $s_i\in[-1,1]$ read off two
independent runs of the adversary. Averaging over $\sigma_i$ and Pinsker's
inequality with the chain rule for $\mathrm{KL}$ over at most $2N$ calls give an
average gap at least $\frac\delta2(1-4\delta\sqrt{N/(3k)})$. The choice
$\delta=\frac18\sqrt{3k/N}$ gives $N\ge3k/(1024a^2)$. Under the top oracle with
hardware randomness carrying the draw, the honest seed carries no information and
the same count holds. Part 3. With the honest seed name the adversary trains both
inputs at the honest seed, reads $b$ when the two views differ, and outputs $0$
otherwise (proven, as in step 3 of `thm-coupling-certificate` (b)). The gap is that
the sketch of Part 2 must handle an adversary whose calls depend on the challenge
view, which the two independent runs do, and this step is not yet written out.

What would settle it. A full proof of the three parts settles it. An adversary with
$o(k/a^2)$ Train calls and gap at most $a$ on every member of
$\mathfrak J_{\mathrm{det}}$ refutes Part 2.

Regime. Statistical, unbounded adversary, priced in Train calls.

Experiment. Implement the planted family as a learning function, which is cheap,
and measure the plug-in attack's gap against $N$ for $k\in\{16,64,256\}$. The
predicted curve is $\Theta(\sqrt{k/N})$. On a real model, take label-only views of
an MNIST classifier at $q$ fixed queries, so $k\le10^q$, and measure the gap of the
plug-in attack against $N$ shadow runs. The space `oracle-and-measurement` owns the
measurement and the cost of real training runs.

The other regime. Without the oracle the adversary must sample the learning
function, and `thm-perfect-substitution` makes the bottom oracle the real
procedure. So Part 2 is a lower bound on the shadow training runs of every
real-world attack that treats training as a black box. A computationally bounded
adversary pays at least this price, and the space `computational-limits` asks when
it pays more.

### conj-reconstruction-label-sandwich: the trainer's error and the representation's residual information bracket an unbounded reconstructor

status: sketch

uses: fact-balle-reconstruction-robustness-definition, fact-pac-privacy-mutual-information-bound, fact-pac-privacy-gaussian-release-bound, fact-zhao-accuracy-forces-attribute-leakage

Statement. Let $(X,Y)$ have a joint law on $\mathcal X\times\mathcal Y$, with
$(\mathcal X,d)$ a metric space and $\mathcal Y$ finite. Let the release $Z$ be drawn
from a kernel applied to $X$, so that $Y\to X\to Z$ is a Markov chain. This covers the
intermediate representation of split learning, $Z=f(X)$ or $Z=f(X)+B$. For a
tolerance $\eta>0$ let

$$\kappa_y(\eta)=\sup_{x_0\in\mathcal X}\Pr[d(X,x_0)\le\eta\mid Y=y],\qquad\bar\kappa(\eta)=\sum_y\Pr[Y=y]\,\kappa_y(\eta),$$

the label baseline. It is at least the oblivious baseline $\kappa(\eta)$ of BCH22.
Let $S^\star(\eta)=\sup_R\Pr[d(X,R(Z))\le\eta]$ over measurable reconstructors $R$,
and let $\varepsilon^\star$ be the Bayes error of predicting $Y$ from $Z$, at most
the test error $\varepsilon_h$ of the trained head.

1. Floor. $S^\star(\eta)\ge\bar\kappa(\eta)-\varepsilon^\star\ge\bar\kappa(\eta)-\varepsilon_h$.
2. Ceiling. If $S^\star(\eta)\ge\bar\kappa(\eta)$ then
   $\mathrm{kl}(S^\star(\eta)\|\bar\kappa(\eta))\le I(X;Z\mid Y)$, hence
   $S^\star\le\bar\kappa+\sqrt{I(X;Z\mid Y)/2}$ and
   $S^\star\le(I(X;Z\mid Y)+\ln2)/\ln(1/\bar\kappa)$.
3. Gaussian release. For $Z=f(X)+B$ with $B\sim\mathcal N(0,\Sigma_B)$ independent,
   $I(X;Z\mid Y)\le\sum_y\Pr[Y=y]\,\frac12\ln\det(I+\Sigma_{f\mid y}\Sigma_B^{-1})$,
   where $\Sigma_{f\mid y}$ is the covariance of $f(X)$ given $Y=y$.
4. Tightness. The label release $Z=Y$ has $\varepsilon^\star=0$ and
   $S^\star=\bar\kappa$. A deterministic $f$ that is injective with a measurable
   inverse on the support has $S^\star=1$ for every $\eta>0$.

Sketch. Floor. Pick $x_y$ within $\zeta$ of the supremum in $\kappa_y$ and let
$R(z)=x_{\hat y(z)}$ for the Bayes classifier $\hat y$. Success is at least
$\Pr[d(X,x_Y)\le\eta]-\Pr[\hat y(Z)\neq Y]$, and $\zeta\to0$. Ceiling. Let $Q$ be the
law under which $X$ and $Z$ are independent given $Y$, with the same pair marginals.
Under $Q$ every $R$ succeeds with probability at most $\bar\kappa$, and
$\mathrm{KL}(P\|Q)=I(X;Z\mid Y)$, so data processing on the success indicator and the
monotonicity of $\mathrm{kl}(p\|\cdot)$ on $[0,p]$ give the bound. This is Theorem 1 of
XD23 with side knowledge $Y$ (its Remark 1), applied to an adversary that does not
hold $Y$ and can only do worse than one that does. Gaussian release. Condition on
$Y=y$, bound the entropy of $f(X)+B$ by that of a Gaussian of the same covariance,
and subtract the entropy of $B$. The gap of the sketch is the measurability of
$S^\star$ and of the near-optimal selection when $\mathcal X$ is not standard Borel,
which round 01 will fix by assuming a standard Borel space.

Reading in the trainer's terms. The floor is Halil's lower bound in the statistical
regime. A reconstructor recovers at least the class-conditional prior of the label
the trained model predicts, up to the trainer's own error. The ceiling says that an
unbounded reconstructor gains over that floor only through what the representation
carries beyond the label, $I(X;Z\mid Y)$. Every term is measurable. The head's test
error is a test, $\kappa_y$ is a supremum of class-conditional ball masses estimable
from data, and the class-conditional covariance of $f(X)$ is estimable from samples,
as Algorithm 1 of XD23 estimates the unconditional one (heuristic for the
estimation rates, which the sketch does not prove).

What would settle it. A proof of the four parts with stated measurability
hypotheses. The aim is non-trivial only if a discussant finds no published statement
of the floor in this form. If one exists, the aim reduces to a borrowed fact and the
space keeps the tightness part and the reading for the reconstruction example.

Regime. Statistical, unbounded reconstructor that knows the joint law and the
release kernel.

Experiment. Train a split network on MNIST with Gaussian noise of covariance
$\Sigma_B$ at the cut. Measure the head's test error, estimate $\kappa_y(\eta)$ from
held-out data, estimate the class-conditional covariances of the cut activations,
and run a learned decoder from $Z$ to $X$. The decoder's success must fall between
the floor and the ceiling. It only bounds $S^\star$ from below.

The other regime. Part 4 shows that for a deterministic injective representation the
statistical baseline is total, so Halil's reconstruction example carries content only
for a bounded reconstructor, or when the representation is noisy, quantized or has
large fibers. The computational question, whether a reconstructor that must itself
learn needs a model as strong as the trainer's, belongs to the space
`computational-limits`, and this aim is its statistical floor and ceiling.
