# Round 01 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25.

This round answers the eighteen challenges of `round-00/discussant-astra.md`,
restates the facts with the hypotheses the discussant asked for, and proves the
two aims the discussion kept. The main object is
`thm-shadow-run-price-finite-views`, the training-run price of distinguishing two
training inputs on a finite view space, with a new hard family that survives
chosen, opened and reused seeds. It rests on `lem-scrambled-seed-urn`. The
reconstruction aim becomes `prop-reconstruction-label-sandwich`, stated as a
baseline proposition without the Markov hypothesis. The profile
`def-uniform-security-profile` is revised as supporting notation. The round-00
objects `conj-shadow-run-price-finite-views` and
`conj-reconstruction-label-sandwich` are superseded by the theorem and the
proposition, which carry new slugs because their statements changed.

Notation is that of `round-00/builder.md`. In addition, for a finite view space
$\mathcal V$ with $k=|\mathcal V|$ elements, $k'=2\lfloor k/2\rfloor$. For a
learning function $\mathsf L$ and a channel $\kappa$, $P_b=\kappa_*\Pi_{x_b}$ is the
view law at $x_b$. Under the bottom oracle the best advantage is
$\mathrm{TV}(P_0,P_1)$, and under the top oracle it is the top divergence
$\mathrm D^\top_1(\kappa)$, both by step 3 of the proof of `thm-coupling-certificate`
(b). The gap of an adversary $\mathcal A$ at $\mathsf L$ under a policy is that
policy's best advantage minus $\mathrm{Adv}_{\mathsf L}(\mathcal A)$.

## Responses to challenges

ch-hsu-estimator-access. Accepted, both parts. Definition 3.2 of HSU25 takes
estimators of the form $\mathcal A(S)=\bar{\mathcal A}(\frac1n\sum_ix_i)$, which the
paper calls symmetric (footnote 1), and the revised fact says so. The claim that a
known estimator makes training runs free is withdrawn. The noise of
$\mathcal A_{n,\rho}$ has covariance $\rho^2\Sigma$ with $\Sigma$ the unknown
population covariance, so the attacker cannot run the estimator. Under the learning
oracle the converse holds. Train calls at any fixed dataset return draws of
$\rho\Sigma^{1/2}g$ with $g\sim\mathcal N(0,I_d)$, and so leak $\Sigma$. Theorem 3.1
of HSU25 therefore says nothing about an attacker with Train access (proven, the
theorem's experiment gives the attacker no access to the mechanism). Whether order
$d$ Train calls with order $\min\{n,1/\rho^2\}$ samples then suffice is posed as
`prob-train-access-collapses-sample-price` in `round-00/summary.md` (heuristic, by
the known-covariance attack that HSU25 attributes to Dwork et al.). The profile now
records HSU25 at $N=0$ only.

ch-hsu-covariance-order. Accepted. Remark 4.2 says that order $n$ samples suffice
for $\rho>1/\sqrt n$, and the necessary order at $d\asymp d^\star$ is
$\min\{n,1/\rho^2\}$, which is below $n$ in that regime. The revised fact states the
sufficiency claim as Remark 4.2 does. The sentence on ignorance is restricted. An
attacker that knows the whole experiment, data law and mechanism together, needs no
reference sample, and the price of Theorem 3.1 is the price of not knowing $\Sigma$
in that experiment.

ch-yeom-cost-and-normalization. Accepted. The revised fact states a loss with values
in $[0,B]$, $B>0$, an attack that evaluates the model once, computes the loss and
flips one biased coin, and an advantage equal to $R_{\mathrm{gen}}/B$, which is the
generalization error itself when $B=1$. It is an achievable baseline for one attack.

ch-lira-parametric-necessity. Accepted. `thm-reference-access` excludes a rate
uniform over all learning functions with atomless views. It does not exclude finite
accuracy at one law or over a restricted family. The revised fact says that some
restriction of the class is needed for a uniform finite price (proven, by
`thm-reference-access`), and that the Gaussian family is LiRA's choice of
restriction (heuristic as an explanation of its counts).

ch-lira-out-exclusion. Accepted. Definition 1 of CCNSTT22 draws the OUT point from
the distribution conditioned on not lying in $D$, and its bit is $b=1$ for members.
Yeom's Experiment 1 draws $z\sim\mathcal D$ without that condition, with $b=0$ for
members. The two games agree when a fresh point lies in the training set with
probability zero, for instance for an atomless $\mathcal D$, after the bit is
renamed (proven, the conditioning event then has probability one).

ch-balle-prior-knowledge. Accepted. The adversary of Definition 2 knows $\pi$ and
$D^-$, as the paragraph after Definition 2 states with its footnote. Its uncertainty
is the realized target $Z\sim\pi$. The revised fact says so. Attainment of the
supremum by a measurable maximum a posteriori map is not claimed.

ch-balle-radius-hypotheses. Accepted. The revised fact restores every domain.
Theorem 2 needs $\alpha>1$. Proposition 6 fixes a constant $\eta\in(0,1)$, and
Proposition 7 a constant $\eta>0$ with an isotropic Gaussian prior and
$\sigma\ge2\eta/\sqrt d$. Theorem 5 fixes $\varepsilon\ge0$, $\eta\in(0,1)$,
$\gamma\in[0,1]$ and the $0/1$ error. The sentence on coupled certificates is
restricted. A coupled certificate bounds the hockey-stick divergence between two
fixed training inputs, so it bounds reconstruction only for the priors on two points
that Theorem 5 uses, after averaging over the prior.

ch-reconstruction-query-tightness. Accepted, and checked. The builder read Appendix
B.5 of ML24. The adversary there defines its bits by whether an output equals the
true target $z$, so it is not one adversary of the minimax game. The builder also
read Appendix B.3. The proof of Lemma 16 asserts
$\mathrm{TV}\le P[M(D)\in S]-P[M(D')\in S]$ for an arbitrary $S$, the wrong
direction, and bounds a maximum by a feasible point of a minimization. So Theorem 10
and Corollary 12 are stated in ML24 and not established there (proven, by the text
of both appendices). The revised fact keeps Theorem 9 alone, whose two-point proof
in Appendix B.2 the discussant checked.

ch-dinur-resource-comparison. Accepted. Theorems 2 and 3 of DN03 differ in the
number of answers as well as in running time, so they do not separate statistical
from computational reconstruction at a fixed observation budget. Theorem 5 is
stated for the two-phase game of Definition 4. The revised fact says both.

ch-pac-suboptimal-adversaries. Accepted. The discussant's counterexample is right.
Theorem 1 of XD23 states a privacy parameter, not a bound on every adversary's
failure. The revised fact states it for adversaries whose success is at least the
optimal prior success, the optimal one included, and states Corollary 1 for every
adversary.

ch-gaussian-covariance-domain. Accepted. The revised fact assumes $\Sigma_B$
positive definite and $\mathbb E\|M(X)\|_2^2<\infty$. It also notes that one run of
Algorithm 1 is one evaluation of the mechanism, a training run only when the
mechanism is training.

ch-profile-comparator. Accepted. The comparator is now defined per policy and per
interface. It ranges over adversaries with the same policy and the same Eval
allowance on served names that may depend on the instance. The degeneracy of a
singleton class is stated for one learning node seen through a channel, where step 3
of `thm-coupling-certificate` (b) makes the informed optimum attainable with no
Train call and no sample.

ch-profile-infinite-budgets. Accepted. Budgets are now finite, in $\mathbb N^2$.
The claim about an infinite-budget experiment is withdrawn. The revised definition
keeps only the limit statement that part (a) of the theorem proves on finite views.

ch-profile-hsu-transfer. Accepted. The threshold form now takes a criterion that
may impose several conditions, such as HSU25's two conditional probabilities. The
regret form for HSU25 follows from its proof, not its statement, since the proof
bounds the total variation between the two mixtures by $0.02$ (§2.3 and §3.2.4) and
Lemma 2.6 then makes every test's advantage at most $0.02$ on some instance. The
profile states this with that pointer. The direction of the experiment paragraph is
corrected.

ch-shadow-adaptive-seeds. Accepted, and the conjecture's proof is repaired by a new
family. The discussant's attack is right. Train accepts a seed value, a seed name or
a request to draw, and Open returns stored seeds. With deterministic kernels a
quantile map from seed to model reveals the planted signs at a chosen seed. The new
family for deterministic kernels labels a fine grid of seed cells by a uniformly
random bijection, so that any set of distinct cells receives labels drawn without
replacement from an urn whose proportions are the planted law
(`lem-scrambled-seed-urn`). Chosen, opened and reused seeds then give at most one
fresh draw per Train call, up to a total variation that vanishes with the grid. For
general kernels a family that ignores the seed and draws the view from hardware
randomness gives exact fresh draws. The top-oracle part now uses one Train call, as
the discussant notes, and its comparator is the top optimum. The label-only case is
stated through an explicit embedding with deterministic evaluation. The relation to
the agnostic learning rate is stated in the theorem's paragraph on prior work.

ch-sandwich-domain-and-tightness. Accepted. The Markov hypothesis is dropped, since
neither proof uses it. The proposition now takes any joint law of $(X,Y,Z)$ on a
Polish $\mathcal X$, a finite $\mathcal Y$ restricted to labels of positive
probability, and a standard Borel $\mathcal Z$. The release $Z=Y$ then needs no
kernel. The logarithmic form is stated for $\bar\kappa\in(0,1)$, and it holds
without the condition $S^\star\ge\bar\kappa$.

ch-sandwich-decoder-floor. Accepted. The experimental claim was false. Every decoder
obeys the ceiling, and the floor is attained by the class-centre decoder built from
a head. The experiment paragraph now says this.

ch-sandwich-experimental-identification. Accepted. The proposition now states which
quantities have a sampling guarantee. The floor with centres from a finite candidate
set fixed in advance is a valid floor and is estimable by Hoeffding's inequality
with a union bound. The ceiling needs the supremum over all balls and a conditional
mutual information, and the space claims no estimation rate for either.

## Facts, revised or carried

### fact-hsu-membership-sample-gap: reference samples that membership inference needs against noisy mean estimation

status: borrowed

uses: none

Statement. Key HSU25, arXiv 2508.19458v1, the version in the library. The game is
Definition 2.1 as stated in round 00. The estimator $\mathcal A_{n,\rho}$ outputs
$\frac1n\sum_iX_i+\rho Z$ with $Z\sim\mathcal N(0,\Sigma)$, where $\Sigma$ is the
population covariance (Definition 2.4). $\mathcal P_d$ is all Gaussians with
positive definite covariance, and $d^\star=n+n^2\rho^2$.

1. Theorem 3.1. There are universal $c_1,c_2$ with the following property. If
   $d>c_1d^\star$ and $m\le c_2d^\star$, no $(\mathcal P_d,\{\mathcal A_{n,\rho}\},n,m)$
   sample-based attack exists. The proof bounds the total variation between the two
   mixture laws of $(\mathbf Y^m,\hat\mu,\text{target})$ under a spiked-covariance
   prior by $0.02$ (§3.2.4), so by Lemma 2.6 every test has advantage at most
   $0.02$ on some population of the family.
2. Theorem 3.3. For $0<\rho<1$, $m\ge cd$ and $d\ge c\,d^\star$ an attack exists
   against the class $\mathfrak A_{n,d,\rho}$ of Definition 3.2. A member factors
   through the empirical mean, $\mathcal A(S)=\bar{\mathcal A}(\frac1n\sum_ix_i)$,
   and lies within squared Mahalanobis distance $2\rho^2d$ of it with probability
   at least $0.99$.
3. Proposition 2.5. An attacker that knows $\mathcal D$ succeeds when
   $d\ge c\,d^\star$, a part the paper attributes to Dwork et al. without proof.

Theorem 1.1 is the paper's informal version of Theorem 3.1. The two bounds match only
at $d\asymp d^\star$ (Remark 3.4). For $d\gg d^\star$ the best attack known to the
paper uses order $d$ samples.

Proof. Borrowed (proven in HSU25, appendix proofs not read in this session).

The other regime. The attacker of Definition 2.1 cannot run the estimator, since
the noise needs $\Sigma$. Under the learning oracle a Train call at any dataset
returns a draw of the noise, so the theorem gives no lower bound for an attacker
with Train access. The attack of Theorem 3.3 runs in polynomial time.

### fact-hsu-gap-prices-covariance: with the covariance known the sample price falls to order min of n and inverse squared noise

status: borrowed

uses: fact-hsu-membership-sample-gap

Statement. Key HSU25, Theorem 4.1. For the identity-covariance family
$\mathcal P^{\mathrm{id.cov}}_d$, a universal $c$, $n\ge4$, $m\ge2$ and
$d<c\,(n+n^2\rho^2+n^2/m)$, no $(\mathcal P^{\mathrm{id.cov}}_d,\{\mathcal A_{n,\rho}\},n,m)$
sample-based attack exists. The paper attributes the converse, an attack once
$d\gtrsim n+n^2\rho^2+n^2/m$, to Dwork et al. without proof. At $d\asymp d^\star$
Theorem 4.1 therefore forces $m\gtrsim\min\{n,1/\rho^2\}$. Remark 4.2 states that for
$\rho>1/\sqrt n$ knowing the covariance lowers the required samples from
$\Omega(n^2\rho^2)$ to $O(n)$, an upper bound.

Proof. Borrowed (proven in HSU25, appendix not read).

The other regime. In the experiment that both theorems analyse, the price of
Theorem 3.1 at $d\asymp d^\star$ is the price of not knowing $\Sigma$ (proven, by
Theorems 3.1 and 4.1 in that regime). An attacker that knows the data law and the
mechanism needs no sample, so in this experiment every sample price is a price of
not knowing part of the experiment.

### fact-yeom-dp-bounds-membership-advantage: differential privacy bounds the advantage of an informed membership attacker

status: borrowed

uses: none

Statement. Unchanged from round 00. Key YGFJ18, Experiment 1, Definition 4 and
Theorem 1. An $\varepsilon$-DP learner, with DP over replacement of one record, gives
$\mathrm{Adv}^M\le e^\varepsilon-1$ for every adversary of Experiment 1, which receives
$\mathcal D$.

Proof. Borrowed (proven in YGFJ18, proof read).

The other regime. Unchanged. The bound holds against unbounded adversaries and prices
no learning resource.

### fact-yeom-generalization-error-gives-advantage: a loss-threshold attack gains the normalized generalization error

status: borrowed

uses: fact-yeom-dp-bounds-membership-advantage

Statement. Key YGFJ18, Theorem 2. Let the loss be nonnegative with
$\ell(A_S,z)\le B$ for a constant $B>0$, all $S$ and all $z$ drawn from $S$ or
$\mathcal D$. Adversary 1 evaluates the model at $z$, computes $\ell(A_S,z)$ and
outputs $1$ with probability $\ell(A_S,z)/B$. Its advantage equals
$R_{\mathrm{gen}}(A)/B$, with $R_{\mathrm{gen}}$ the average generalization error of
Definition 3. For the $0/1$ loss and $B=1$ it is the generalization error.

Proof. Borrowed (proven in YGFJ18, proof read).

The other regime. The attack uses one model evaluation, one loss computation and one
biased coin, and no sample or training run. It shows what one attack achieves, not a
bound on all attacks.

### fact-lira-priced-in-training-runs: the likelihood-ratio attack spends 64 to 256 shadow training runs

status: borrowed

uses: fact-lira-low-fpr-yeom-game

Statement. Key CCNSTT22. Algorithm 1 (§IV-C) and its offline variant as stated in
round 00. §V-A uses $N=64$ shadow models for ImageNet and $N=256$ otherwise, each
example IN for half. §VI-B and Fig. 9 report diminishing gains beyond $64$ and quick
loss below, and a pooled variance that is better below $64$. §VI-D reports no change
with disjoint shadow data (CINIC-10, 128 OUT models). All empirical.

Proof. Borrowed, empirical on the datasets and models of §V.

The other regime. By `thm-reference-access` no rate holds uniformly over all learning
functions with atomless views, so a uniform finite price needs some restriction of the
class (proven). LiRA's Gaussian model of the per-example confidence is its
restriction (heuristic, as an explanation of the counts). Its counts are not
certificates of nearness to the total variation.

### fact-lira-low-fpr-yeom-game: the LiRA game excludes members from the OUT draw

status: borrowed

uses: fact-yeom-dp-bounds-membership-advantage

Statement. Key CCNSTT22, Definition 1 in §III-A. The challenger samples $D$ and
trains $f_\theta$. It flips $b$. For $b=0$ it draws a fresh point from the
distribution with $(x,y)\notin D$, and for $b=1$ a point of $D$. The adversary has
query access to the distribution and to $f_\theta$. The paper says the game is
inspired by Yeom et al. and Jayaraman et al. Against Yeom's Experiment 1 the bit is
renamed and the OUT draw is conditioned on missing $D$, so the two games agree when
that event has probability one, for instance for an atomless distribution.

Proof. Borrowed (a definition, read in full). The agreement is proven by the
conditioning remark.

The other regime. Query access to the distribution is the resource HSU25 prices in
samples. LiRA spends it on shadow training sets and reports runs.

### fact-balle-reconstruction-robustness-definition: reconstruction robustness and its oblivious baseline

status: borrowed

uses: none

Statement. Key BCH22. Definition 1 is the informed adversary, holding $D^-$, the
released $\theta$, the training algorithm and optional side knowledge. Definition 2
calls $M$ $(\eta,\gamma)$-ReRo for a prior $\pi$ and an error $\ell$ when every
deterministic $R:\Theta\to\mathcal Z$ and every $D^-$ give
$\Pr_{Z\sim\pi,\theta\sim M(D^-\cup\{Z\})}[\ell(Z,R(\theta))\le\eta]\le\gamma$. The
adversary knows $\pi$ and $D^-$, and its uncertainty is the target $Z$. The baseline
$\kappa_{\pi,\ell}(\eta)=\sup_{z_0}\Pr_{Z\sim\pi}[\ell(Z,z_0)\le\eta]$ is defined in
§VII-B without a number.

Proof. Borrowed (definitions, read). Randomized attacks give the same supremum by
averaging over their coins. Attainment by a measurable posterior maximizer is not
claimed.

The other regime. The definition is statistical and prices neither learning the
prior nor training a reconstructor.

### fact-balle-dp-bounds-reconstruction: Rényi and pure differential privacy bound reconstruction by the baseline

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Statement. Key BCH22, §VII. Write $\kappa=\kappa_{\pi,\ell}(\eta)$ with $\eta>0$.

1. Theorem 2. For $\alpha>1$ and $\varepsilon\ge0$, an $(\alpha,\varepsilon)$-RDP
   mechanism is $(\eta,\gamma)$-ReRo with $\gamma=(\kappa e^\varepsilon)^{(\alpha-1)/\alpha}$.
2. Corollary 3. An $\varepsilon$-DP mechanism is $(\eta,\kappa e^\varepsilon)$-ReRo.
3. Corollary 4. A $\rho$-zCDP mechanism with $\rho<\log(1/\kappa)$ is ReRo with
   $\gamma=\exp(-(\sqrt{\log(1/\kappa)}-\sqrt\rho)^2)$.
4. Proposition 6. For a constant $\eta\in(0,1)$, the uniform prior on the unit ball
   of $\mathbb R^d$ and $\ell_2$ error, $\varepsilon=o(d)$ or $\rho=o(d)$ gives
   $\gamma=e^{-\Omega(d)}$. Proposition 7. For a constant $\eta>0$, the prior
   $\mathcal N(w,\sigma^2I_d)$ with $\sigma\ge2\eta/\sqrt d$ and $\ell_2$ error, the same.
5. Theorem 5. For $\varepsilon\ge0$, $\eta\in(0,1)$, $\gamma\in[0,1]$ and the $0/1$
   error, ReRo against every prior on two points with mass $1/(e^\varepsilon+1)$ on
   one of them gives $(\varepsilon,\max\{0,(e^\varepsilon+1)\gamma-e^\varepsilon\})$-DP.

Proof. Borrowed (proven in BCH22, appendix proofs of Theorems 2 and 5, Corollary 4
and Proposition 6 read).

The other regime. All bounds hold against unbounded attackers and need a known privacy
parameter. A coupled certificate of the learning-oracle theory bounds the divergence
between two fixed inputs, which controls reconstruction for the two-point priors of
Theorem 5 and not for a general prior.

### fact-reconstruction-query-lower-bounds: how many of the trainer's outputs a reconstruction attacker must see

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Statement. Key ML24, arXiv 2303.16372v6. In the game of §3 the adversary receives $n$
independent draws $h_1,\dots,h_n\sim M(D^-\cup\{z\})$ with $D^-$ known, and the value
is $V(M,n)=\inf_{\mathcal A}\sup_z\mathbb E[\rho(\mathcal A(h_{1:n}),z)^2]$. Theorem 9
states, for a compact metric space, $\varepsilon\ge0$, $\delta\in[0,1]$ and every
$(\varepsilon,\delta)$-DP learner,
$V(M,n)\gtrsim\mathrm{diam}(\mathcal Z)^2(2(1-\delta)/(e^\varepsilon+1))^n$. The
query form needs nondegenerate parameters and a target error below the diameter.
Theorem 10, the claimed matching upper bound, and Corollary 12, the Rényi extension,
are stated in ML24 and not established. The adversary of Appendix B.5 uses the true
target, and the proof of Lemma 16 in Appendix B.3 bounds the total variation from the
wrong side.

Proof. Borrowed for Theorem 9 (the two-point proof of Appendix B.2, checked by the
discussant of round 00 and not read by the builder). The two gaps were read by the
builder.

The other regime. The unit counts outputs of the trainer that the attacker observes,
not runs it makes, and the bound needs DP inside training.

### fact-dinur-nissim-reconstruction-thresholds: reconstruction thresholds for subset sums

status: borrowed

uses: none

Statement. Key DN03. Definitions 1 to 3 and Theorems 2 and 3 as in round 00.
Theorem 2 uses all $2^n$ answers and exponential time, Theorem 3 uses
$n(\log n)^2$ random answers and a linear program. Theorem 5 states
$(T(n),\delta)$-privacy in the two-phase game of Definition 4, where the adversary
names an index after querying and then receives every other bit, for the uniform
prior, $T(n)>\mathrm{polylog}(n)$ and perturbation $\tilde O(\sqrt{T(n)})$.

Proof. Borrowed (proven in DN03, statements and the proof of Theorem 2 read).

The other regime. Theorems 2 and 3 change both the number of answers and the running
time, so they are not a separation of statistical from computational reconstruction
at a fixed observation budget.

### fact-pac-privacy-mutual-information-bound: mutual information bounds the gain of a reconstruction that beats the prior guess

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Statement. Key XD23. For a mechanism $M$, a data law $\mathcal D$ known to the
adversary and a criterion $\rho$, let $1-\delta^\rho_o$ be the optimal prior success
(Definition 3). Theorem 1 states that $M$ is $(\delta,\rho,\mathcal D)$ PAC private,
meaning no adversary succeeds with probability at least $1-\delta$, for every
$\delta$ with $\delta\le\delta^\rho_o$ and $\mathrm{kl}(\delta\|\delta^\rho_o)>I(X;M(X))$.
Equivalently, an adversary whose failure $\delta$ satisfies $\delta\le\delta^\rho_o$,
the optimal adversary included, has $\mathrm{kl}(\delta\|\delta^\rho_o)\le I(X;M(X))$.
Corollary 1, $\delta^\rho_o-\delta\le\sqrt{I(X;M(X))/2}$, holds for every adversary.
Remark 1 conditions both sides on extra side knowledge.

Proof. Borrowed (proven in XD23, Appendix A not read). The restriction to adversaries
at least as good as the prior guess is the discussant's correction of round 00, with
the constant-release counterexample.

The other regime. Statistical, and it needs the data law known. §2 of XD23 states that
the framework cannot quantify the hardness added by ignorance of the law.

### fact-pac-privacy-gaussian-release-bound: a Gaussian release has mutual information set by its covariance

status: borrowed

uses: fact-pac-privacy-mutual-information-bound

Statement. Key XD23. Theorem 3. For a deterministic $M$ with
$\mathbb E\|M(X)\|_2^2<\infty$ and independent $B\sim\mathcal N(0,\Sigma_B)$ with
$\Sigma_B$ positive definite,
$I(X;M(X)+B)\le\frac12\log\det(I_d+\Sigma_{M(X)}\Sigma_B^{-1})$. Theorem 4. If
$\|M(X)\|_2\le r$, Algorithm 1 evaluates $M$ on $m$ independent draws of $X$,
estimates $\Sigma_{M(X)}$, and returns $\Sigma_B$ with $I(X;M(X)+B)\le v+\beta$ with
confidence $1-\gamma$ once the parameter $c$ satisfies display (6).

Proof. Borrowed (proven in XD23, appendices C and D not read).

The other regime. One run of Algorithm 1 is one evaluation of $M$, a training run when
$M$ is training and a forward pass when $M$ is a representation. It certifies the
release, not an attack.

### fact-zhao-accuracy-forces-attribute-leakage: an accurate representation must leak a correlated attribute

status: borrowed

uses: none

Statement. Unchanged from round 00, with both attribute groups of positive
probability. Key ZCTG20, Theorems 3.2 and 3.3, for $\mathcal H_A$ all measurable
binary classifiers on $\mathcal Z$.

Proof. Borrowed (proven in ZCTG20, appendix proofs read).

The other regime. Unchanged. Statistical, no class restriction.

### fact-balle-reconnn-priced-in-shadow-runs: reconstruction by a learned reconstructor costs thousands of shadow runs and needs the initialization

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Statement. Key BCH22, §IV-B and §VI-B. The attack trains $k$ shadow models
$\bar\theta_i=A(D^-\cup\{\bar z_i\})$ and fits a reconstructor network to the pairs
$(\bar\theta_i,\bar z_i)$. With full-batch training from an initialization known to
the adversary, reconstructions beat the nearest-neighbour oracle on average from
$8$K shadow models on MNIST and from $10$K on CIFAR-10, and high-fidelity MNIST
reconstructions appear from $1$K (Fig. 5). With a fresh random initialization per
model the attack fails on MNIST. Table III gives MSE between $0.0691$ and $0.0695$
then, against $0.0041$ to $0.0089$ with the initialization known, and a pool of $5$M
shadow pairs over $500$ initializations per target did not help.

Proof. Borrowed, empirical on MNIST and CIFAR-10 with the models of §V.

The other regime. This is the reconstructor-as-learner of Halil's example, trained on
weights rather than on an intermediate representation, priced in shadow training
runs. The dependence on the initialization is the seed acting as a resource, which the
top oracle models and which part (d) of `thm-shadow-run-price-finite-views` prices in
the distinguishing game.

## Objects

### def-uniform-security-profile: the uniform regret profile of an unbounded adversary in learning units

status: open

uses: thm-coupling-certificate, def-degenerate-oracles, fact-hsu-membership-sample-gap

Statement. Fix a procedure, a coalition, a channel interface with its Eval allowance
on served names, a game and a policy $\mathsf P\in\{\text{bottom},\text{top}\}$. An
instance $\iota$ fixes the learning function, the laws of seeds and hardware
randomness, the procedure's data and a reference law $\mathcal D_\iota$ from which
reference samples are drawn. A budget is $\beta=(m,N)\in\mathbb N^2$, ordered
coordinatewise, of $m$ reference samples from $\mathcal D_\iota$ and at most $N$
Train calls. $\mathcal A_{\mathsf P}(\beta)$ is the set of adversaries under
$\mathsf P$ with the given interface and budget, which stop with probability one
and are chosen before the instance. For distinguishing, $\mathrm{Succ}_\iota$ is the
advantage. For inverting it is the success probability on the game's event.

1. The informed optimum $\mathrm{Opt}_{\mathsf P}(\iota)$ is the supremum of
   $\mathrm{Succ}_\iota(\mathcal A)$ over adversaries under $\mathsf P$ with the same
   interface and any finite budget, which may depend on $\iota$.
2. The uniform regret at a budget, over a class $\mathfrak J$, is
   $$g_{\mathfrak J,\mathsf P}(\beta)=\inf_{\mathcal A\in\mathcal A_{\mathsf P}(\beta)}\ \sup_{\iota\in\mathfrak J}\big(\mathrm{Opt}_{\mathsf P}(\iota)-\mathrm{Succ}_\iota(\mathcal A)\big).$$
   It is nonincreasing in $\beta$.
3. The attained price at accuracy $a\ge0$ is the set of minimal elements of
   $F(a)=\{\beta:\exists\mathcal A\in\mathcal A_{\mathsf P}(\beta)\ \forall\iota\in\mathfrak J,\ \mathrm{Opt}_{\mathsf P}(\iota)-\mathrm{Succ}_\iota(\mathcal A)\le a\}$.
   It is finite by Dickson's lemma, and empty when $F(a)$ is. The approximate price
   uses $\{\beta:g_{\mathfrak J,\mathsf P}(\beta)\le a\}$ instead.
4. The threshold price of a criterion $C$, a finite list of conditions on the run's
   outcome laws such as HSU25's two conditional probabilities, is the set of minimal
   $\beta$ for which one adversary in $\mathcal A_{\mathsf P}(\beta)$ meets $C$ on every
   $\iota\in\mathfrak J$, possibly empty.

Properties, with labels.

1. Singleton classes. For one learning node seen through a channel, an adversary that
   depends on $\iota$ attains $\mathrm{Opt}_{\mathsf P}(\iota)$ with no sample and no
   Train call, by hard-wiring the test of (F1) under the bottom oracle and the test on
   $(\rho,Y)$ under the top oracle (proven, step 3 of the proof of
   `thm-coupling-certificate` (b), whose bottom-oracle optimum is
   $\mathrm{TV}(P_0,P_1)$ and top-oracle optimum $\mathrm D^\top_1$). So
   $g_{\{\iota\},\mathsf P}\equiv0$, and every positive regret is a price of not knowing
   which member of the class is the instance.
2. Finite views. For one learning node through a deterministic channel onto $k$ views,
   $g_{\mathfrak J_{\mathrm{all}},\text{bottom}}(0,N)\le2\sqrt{k/\lfloor N/2\rfloor}$, so
   it tends to zero along finite budgets (proven, `thm-shadow-run-price-finite-views`
   (a)).
3. HSU25 at $N=0$. Let $\mathfrak J$ hold the populations $\mathcal N(\mu,\Sigma)$ of
   $\mathcal P_d$ with the estimator $\mathcal A_{n,\rho}$, and let the attacker have no
   Train access, which is $N=0$. For $d>c_1d^\star$, every budget $(m,0)$ with
   $m\le c_2d^\star$ is outside the threshold price of HSU25's criterion, and its regret
   form is at least $\mathrm{Opt}-0.02$ on some instance (proven, by HSU25 Theorem 3.1
   and its proof as cited in `fact-hsu-membership-sample-gap`). With Train access the
   question is `prob-train-access-collapses-sample-price`.

Sketch of well-posedness. Success is defined for every adversary that stops with
probability one, since its run is a measurable function of countably many
independent draws (`def-learning-oracle-model`). The infimum and supremum are over
sets of reals in $[-1,1]$. Monotonicity holds because a budget-$\beta$ adversary is a
budget-$\beta'$ adversary for $\beta'\ge\beta$. Dickson's lemma gives finitely many
minimal elements of any subset of $\mathbb N^2$.

What would settle it. Acceptance as well posed. The definition is notation and is a
result only together with the theorem that computes it on one axis.

Regime. Statistical. Budgets count samples and training runs, and adversaries are
unbounded.

Experiment. Run a fixed attack at a grid of budgets on instances sampled from the
class. Its measured worst regret over the sampled instances, after estimation error,
is a lower bound on that attack's worst regret over the class and an upper bound on
the uniform regret of the sampled subclass. Lower bounds on the price come from
theorems. The space `oracle-and-measurement` owns the measurement.

The other regime. A bounded adversary cannot hard-wire an arbitrary test, so its
profile is not degenerate on a singleton, and a comparison there needs a bound on
advice or description size. That object belongs to the space `computational-limits`.

### lem-scrambled-seed-urn: a random scramble of seed cells turns chosen and opened seeds into fresh draws

status: sketch

uses: def-learning-oracle

Statement. Let $\mathcal V$ be finite, $p$ a law on $\mathcal V$, and $M$ an integer
with $Mp(v)\in\mathbb N$ for all $v$. Partition $[0,1)$ into the cells
$c(t)=\lfloor Mt\rfloor\in\{0,\dots,M-1\}$, and fix a labelling
$\lambda:\{0,\dots,M-1\}\to\mathcal V$ with $|\lambda^{-1}(v)|=Mp(v)$. For a bijection
$\pi$ of $\{0,\dots,M-1\}$ and seeds $\rho=(\rho_a,\rho_b)$ uniform on $[0,1)^2$, let a
learning function with deterministic kernels give at a fixed training input $x_0$ the
model $s(\lambda(\pi(c(\rho_b))))$, for a fixed injection $s$ of $\mathcal V$ into the
model space, and give at every other input a model that does not depend on $\pi$.
Fix an adversary that makes at most $N<M$ Train calls, any Eval and Open calls, and
chooses seeds, seed names and inputs adaptively, also after an observed challenge
value $v$ that the run takes as given. Let $T_v$ be the law of its transcript when
$\pi$ is uniform and independent of everything else. Let $\tilde T_v$ be the law of
the transcript in the lazy process, which answers a Train call at $x_0$ whose seed
lies in a cell not met by an earlier call at $x_0$ with $s(V)$ for a fresh
$V\sim p$, answers a call at an earlier cell with the earlier model, and answers every
other call as the oracle does. Then

$$\mathrm{TV}(T_v,\tilde T_v)\le\frac{N^2}{2(M-N)},$$

and, for two laws $p,p'$ on $\mathcal V$ and the lazy processes $\tilde T_v,\tilde T'_v$
built from them with the same adversary,
$\mathrm{KL}(\tilde T_v\|\tilde T'_v)\le N\,\mathrm{KL}(p\|p')$.

Proof. The adversary sees $\pi$ only through the labels of the cells it meets at
$x_0$, since every other answer is free of $\pi$, Eval on a model $s(u)$ is a function
of $u$ and fresh evaluation randomness, and Open returns a seed it already holds or a
model $s(u)$. Order the Train calls at $x_0$ that meet a new cell. Given the transcript
before the $t$-th such call, the cells met so far are $c_1,\dots,c_{t-1}$, their labels
are $u_1,\dots,u_{t-1}$, and the new cell is $c_t$. Under the uniform $\pi$ conditioned
on $\lambda(\pi(c_j))=u_j$ for $j<t$, the value $\pi(c_t)$ is uniform on the $M-t+1$
cells outside $\pi(\{c_1,\dots,c_{t-1}\})$, so the new label has law
$q_t(v)=(Mp(v)-r_v)/(M-t+1)$, where $r_v$ counts the $u_j$ equal to $v$. Then

$$\mathrm{TV}(q_t,p)=\frac12\sum_v\frac{|r_v-(t-1)p(v)|}{M-t+1}\le\frac{t-1}{M-t+1}.$$

Every other step has the same conditional law in both processes. Couple the two
processes step by step with maximal couplings of the conditional laws. They differ
only if some new-cell step uncouples, so the total variation of the transcripts is at
most $\sum_{t\le N}\frac{t-1}{M-N}\le\frac{N^2}{2(M-N)}$. For the second claim, the
chain rule for KL over the adaptive steps gives the sum over steps of the expected
conditional KL. A new-cell step at $x_0$ contributes $\mathrm{KL}(p\|p')$, a repeated
cell contributes zero since the answer is a function of the past, and every other step
contributes zero since its conditional law is the same under $p$ and $p'$. At most $N$
steps are new-cell steps. $\square$

The gap that keeps the status at sketch is the measurability of the step-by-step
coupling for an adversary with uncountably many seed choices, which is handled by
conditioning on the finite sequence of cells met, a countable object, and is not
written out here.

The other regime. The lemma is what makes the learning oracle's seed interface, which
lets callers name and open seeds, no stronger than a stream of fresh draws against an
unknown scramble. A computationally bounded adversary facing a pseudorandom scramble
in place of a uniform one is the cryptographic version, which Halil's rule excludes as
a plug-in, and which this space does not use.

### thm-shadow-run-price-finite-views: the training-run price of distinguishing two training inputs on k views

status: sketch

uses: lem-scrambled-seed-urn, thm-coupling-certificate, thm-black-box-certifiability, thm-reference-access, def-degenerate-oracles, def-uniform-security-profile

Setting. One learning node trains $x_b$ under $H_b$, with $x_0\neq x_1$ known to the
adversary. Its model $W$ reaches the adversary only as $y=\kappa(W)$ through the
plain channel, for a measurable map $\kappa$ from the model space onto a finite set
$\mathcal V$ with $k\ge2$ elements, and a fixed injection $s:\mathcal V\to\mathcal M$
with $\kappa\circ s=\mathrm{id}$. An adversary makes at most $N$ Train calls, any Eval
and Open calls, chooses training inputs, seed values, seed names and draws
adaptively, and may call before and after seeing $y$. $\mathfrak J_{\mathrm{all}}$ is
the class of all learning functions with this model space, and $\mathfrak J_{\mathrm{det}}$
its members with deterministic kernels.

Statement.

(a) Upper bound. For every learning function, the adversary that makes
$n=\lfloor N/2\rfloor$ drawn-seed Train calls at each of $x_0,x_1$, opens the models,
forms the empirical view laws $\hat p_0,\hat p_1$ and outputs $1$ iff
$\hat p_1(y)>\hat p_0(y)$ has
$\mathrm{TV}(P_0,P_1)-\mathrm{Adv}\le2\sqrt{k/n}$, in expectation over its shadow draws.

(b) Lower bound, general kernels, both oracles. Let $k\ge4$. For every $N\ge1$ and every
adversary with at most $N$ Train calls, some $\mathsf L\in\mathfrak J_{\mathrm{all}}$ has
gap at least

$$\min\Big\{\frac18,\ \frac1{32}\sqrt{\frac{3k'}{N}}\Big\}$$

under the bottom oracle, and the same function has the same gap under the top oracle.

(c) Lower bound, deterministic kernels, bottom oracle. For every adversary with at most
$N$ Train calls and every $\zeta>0$, some $\mathsf L\in\mathfrak J_{\mathrm{det}}$ has
bottom-oracle gap at least $\min\{\frac18,\frac1{32}\sqrt{3k'/N}\}-\zeta$.

(d) Top oracle, deterministic kernels. The adversary that calls
$\mathsf{Train}(x_0,s^\ast)$ on the honest seed name $s^\ast$, opens the model $m_0$ and
outputs $1$ iff $y\neq\kappa(m_0)$ has advantage equal to the top optimum
$\mathrm D^\top_1(\kappa)=\Pr_\rho[\kappa(\mathsf L(x_0;\rho))\neq\kappa(\mathsf L(x_1;\rho))]$,
which is at least $\mathrm{TV}(P_0,P_1)$, for every $\mathsf L\in\mathfrak J_{\mathrm{det}}$.
It makes one Train call.

(e) Price. Let $0<a<\frac18$ and $k\ge4$. Under the bottom oracle, over
$\mathfrak J_{\mathrm{all}}$ or $\mathfrak J_{\mathrm{det}}$, an adversary whose gap is at
most $a$ at every member makes at least $3k'/(1024a^2)$ Train calls, and
$2\lceil4k/a^2\rceil$ drawn-seed calls suffice in expectation. Under the top oracle over
$\mathfrak J_{\mathrm{det}}$, one Train call reaches the top optimum. Under the top oracle
over $\mathfrak J_{\mathrm{all}}$ the lower bound $3k'/(1024a^2)$ remains.

(f) Label-only views. Let $U$ be a finite query set with $|U|=q$, $C\ge2$ outputs, and
deterministic evaluation $\mathsf{ev}(t,u)=t(u)$ on models that include the tables
$t\in[C]^U$. Serve the model through the query channel with allowance $Q\ge q$. Then the
label-only optimum is $\mathrm{Adv}^{\mathrm{bb}}(q)=\mathrm{TV}$ of the laws of the
table, and the bounds of (a) to (e) hold with $k=C^q$. For a larger query set the lower
bound of (b) and (c) still holds with $k=C^q$, and the upper bound of
`thm-black-box-certifiability` (b) exceeds it by a factor of order
$\ln|U|/(C-1)+1$.

Proof of (a). For every set $A\subseteq\mathcal V$ and laws $P,\hat p$,
$|P(A)-\hat p(A)|\le\frac12\|P-\hat p\|_1$. Let $A^\ast=\{P_1>P_0\}$ and
$\hat A=\{\hat p_1>\hat p_0\}$. Then

$$P_1(\hat A)-P_0(\hat A)\ge\hat p_1(\hat A)-\hat p_0(\hat A)-\tfrac12\|\hat p_1-P_1\|_1-\tfrac12\|\hat p_0-P_0\|_1\ge\mathrm{TV}(P_0,P_1)-\|\hat p_1-P_1\|_1-\|\hat p_0-P_0\|_1,$$

since $\hat p_1(\hat A)-\hat p_0(\hat A)\ge\hat p_1(A^\ast)-\hat p_0(A^\ast)$. Drawn seeds
give independent views at each input by fidelity, and
$\mathbb E\|\hat p_b-P_b\|_1\le\sum_v\sqrt{P_b(v)/n}\le\sqrt{k/n}$ by Jensen's and
Cauchy and Schwarz's inequalities. The challenge is independent of the shadow draws,
so the advantage is the expectation of $P_1(\hat A)-P_0(\hat A)$. $\square$

Proof of (b). Step 1, the decision rule. Fix a learning function. Under the bottom
oracle the randomness of the adversary's own calls and its coins, together $\omega$, is
independent of the honest seed and hardware by fidelity, and the honest node reaches
the adversary only through $y$. So the output is $F(\omega,y)$ for a measurable $F$,
and with $\varphi(v)=\Pr_\omega[F(\omega,v)=1]$,
$\mathrm{Adv}=\sum_v\varphi(v)(P_1(v)-P_0(v))$. Under the top oracle the same holds for
a learning function that ignores the seed, with the honest seed added to $\omega$,
since then the seed is independent of $y$ and of every answer.

Step 2, the family. Pair the first $k'$ views as $(2i-1,2i)$ for $i\le r=k'/2$, and give
any remaining view mass zero. For $\sigma\in\{\pm1\}^r$ and $\delta\in(0,\frac12]$ let

$$P^\sigma_0(2i-1)=\frac{1+\sigma_i\delta}{k'},\qquad P^\sigma_0(2i)=\frac{1-\sigma_i\delta}{k'},\qquad P_1(v)=\frac1{k'}\ \text{for}\ v\le k'.$$

Let $\Xi=[0,1)$ with Lebesgue law and let $\mathsf L^\sigma(x_0;\rho,\xi)=s(Q^\sigma(\xi))$
and $\mathsf L^\sigma(x_1;\rho,\xi)=s(Q_1(\xi))$, with $Q^\sigma$ and $Q_1$ the quantile
maps of $P^\sigma_0$ and $P_1$ in the order of $\mathcal V$, and let every other input
train to one fixed model. Each Train call at $x_0$ returns $s$ of a fresh draw of
$P^\sigma_0$ whatever its seed, and every other answer has a law free of $\sigma$. Then
$\mathrm{TV}(P^\sigma_0,P_1)=\frac12\sum_v|P^\sigma_0(v)-P_1(v)|=\frac\delta2$ and, by
Step 1,

$$\mathrm{Adv}^\sigma=\frac\delta{k'}\sum_{i\le r}\sigma_is^\sigma_i,\qquad s^\sigma_i=\varphi^\sigma(2i)-\varphi^\sigma(2i-1),\qquad\mathrm{gap}^\sigma=\frac\delta{k'}\sum_{i\le r}(1-\sigma_is^\sigma_i).$$

Step 3, two runs. For $i\le r$ run the adversary twice, independently, against
$\mathsf L^\sigma$, with challenge $2i$ in the first run and $2i-1$ in the second, and let
$Z_i\in\{-1,0,1\}$ be the first output minus the second. Then $\mathbb E^\sigma Z_i=s^\sigma_i$.
Let $\sigma^\pm$ agree off coordinate $i$ and have $\sigma_i=\pm1$. Only the at most $2N$
Train calls at $x_0$ have laws that depend on $\sigma$, so the chain rule gives
$\mathrm{KL}\le2N\,\mathrm{KL}(P^{\sigma^+}_0\|P^{\sigma^-}_0)$ for the two pair
transcripts. Here
$\mathrm{KL}(P^{\sigma^+}_0\|P^{\sigma^-}_0)=\frac{2\delta}{k'}\ln\frac{1+\delta}{1-\delta}\le\frac{16\delta^2}{3k'}$,
since $\ln\frac{1+\delta}{1-\delta}\le2\ln3\cdot\delta\le\frac83\delta$ on $(0,\frac12]$ by
convexity. Pinsker's inequality bounds the total variation of the pair transcripts by
$4\delta\sqrt{N/(3k')}$, and $|s^{\sigma^+}_i-s^{\sigma^-}_i|$ by twice that.

Step 4, averaging. For fixed $\sigma_{-i}$,
$\frac12[(1-s^{\sigma^+}_i)+(1+s^{\sigma^-}_i)]\ge1-4\delta\sqrt{N/(3k')}$. Averaging over
$\sigma$ uniform and summing over $i$,

$$\mathbb E_\sigma\,\mathrm{gap}^\sigma\ge\frac\delta2\Big(1-4\delta\sqrt{\frac N{3k'}}\Big).$$

If $N\ge3k'/16$ take $\delta=\frac18\sqrt{3k'/N}\le\frac12$, which gives
$\mathbb E_\sigma\mathrm{gap}^\sigma\ge\frac\delta4=\frac1{32}\sqrt{3k'/N}$. If $N<3k'/16$
take $\delta=\frac12$, which gives more than $\frac18$. Some $\sigma$ attains the
average. Under the top oracle the family ignores the seed, so the top optimum equals
$\mathrm{TV}$ and Step 1 applies with the honest seed in $\omega$. $\square$

Proof of (c). Replace the family of (b) by the scrambled family of
`lem-scrambled-seed-urn`, with $\Xi$ a point, seeds $(\rho_a,\rho_b)$ uniform on
$[0,1)^2$, $\mathsf L^{\sigma,\pi}(x_0;\rho)=s(\lambda_\sigma(\pi(c(\rho_b))))$ with
$|\lambda_\sigma^{-1}(v)|=MP^\sigma_0(v)$, $\mathsf L(x_1;\rho)=s(Q_1(\rho_a))$, and a fixed
model elsewhere. Take $\delta$ rational and $M$ a multiple of $k'$ times its
denominator, which costs at most $\zeta/2$ in the bound by continuity in $\delta$. The
view laws are $P^\sigma_0$ and $P_1$ for every $\pi$, so Step 1 holds for each instance
$(\sigma,\pi)$ and $\mathrm{gap}^{\sigma,\pi}=\frac\delta{k'}\sum_i(1-\sigma_is^{\sigma,\pi}_i)$.
Average over $\pi$ uniform. The average of $s^{\sigma,\pi}_i$ is the difference of the
output probabilities under the mixture laws $T^\sigma_{2i}$ and $T^\sigma_{2i-1}$ of the
lemma. Run Step 3 with these mixtures, independent across the two runs. By the lemma
each mixture is within $N^2/(2(M-N))$ of its lazy process, whose KL to the lazy process
of $\sigma'$ is at most $N\,\mathrm{KL}(P^\sigma_0\|P^{\sigma'}_0)$. So the pair total
variation is at most $4\delta\sqrt{N/(3k')}+2N^2/(M-N)$, and
$M\ge N+8N^2/\zeta$ makes the average gap at least the bound of (b) minus $\zeta$.
Some instance attains the average. $\square$

Proof of (d). Under deterministic kernels the honest model is
$\mathsf L(x_b;\rho^\ast)$, and the call returns $m_0=\mathsf L(x_0;\rho^\ast)$. Under
$H_0$, $y=\kappa(m_0)$ and the output is $0$. Under $H_1$ the output is $1$ exactly when
$\kappa(\mathsf L(x_1;\rho^\ast))\neq\kappa(\mathsf L(x_0;\rho^\ast))$. So the advantage is
the divergence probability through $\kappa$, which equals the coupled divergence
$\beta_1(\kappa)$ for a deterministic channel and hence the top divergence under
deterministic kernels, and is at least $\mathrm{TV}(P_0,P_1)$, both by
`thm-coupling-certificate` (b). By the same theorem it is the best top-oracle
advantage. $\square$

Proof of (e). If every member has gap at most $a<\frac18$, then (b) or (c) gives
$a\ge\frac1{32}\sqrt{3k'/N}-\zeta$ for every $\zeta>0$, since the bound $\frac18$ is
excluded, and so $N\ge3k'/(1024a^2)$. Part (a) with $n=\lceil4k/a^2\rceil$ gives gap at
most $a$. Parts (d) and (b) give the top-oracle statements. $\square$

Proof of (f). Let the served model be a table $t$ with law $P_b$ on $[C]^U$. An
adversary with allowance $Q\ge q$ reads $t$ by querying each point once, and a strategy
tree of depth $q$ that queries the $q$ points along every path and outputs
$\mathbf 1[t\in A^\ast]$ attains $\mathrm{TV}$, while no tree exceeds it by data
processing. So $\mathrm{Adv}^{\mathrm{bb}}(q)=\mathrm{TV}(P_0,P_1)$, and every adversary's
output is a function of $t$ and its own transcript, which is the setting of (a) to (e)
with $\mathcal V=[C]^U$ and $\kappa$ the table. For $|U|>q$, let the family vary the
table on $q$ fixed points and keep the other values fixed, which gives the same lower
bound. Finally $\ln|\mathfrak T_q|\le\frac{C^q-1}{C-1}\ln|U|+C^q\ln2$ from the count of
`thm-black-box-certifiability`, which gives the stated factor. $\square$

Status. Sketch, because (c) inherits the measurability gap of `lem-scrambled-seed-urn`.
Parts (a), (b), (d), (e) for $\mathfrak J_{\mathrm{all}}$ and (f) are proofs.

Prior work and novelty. The passive version, where the attacker receives $n$
independent views at each input and nothing else, is agnostic learning of the class of
all subsets of $\mathcal V$, whose dimension is $k$. The rate $\Theta(k/a^2)$ for that
problem is classical, and the round-00 discussant points to Daniely, Sabato, Ben-David
and Shalev-Shwartz, JMLR 2015, Theorem 5, which this session has not read. The content
here is the oracle part. Parts (b) and (c) show that chosen, opened and reused seeds,
inputs chosen after the challenge, and coupled calls do not beat the passive rate, and
(c) needs the scramble for that. Part (d) shows that the honest seed collapses the price
to one call under deterministic kernels (proven above). No published statement of the
oracle part is known to the space (open as a novelty claim, no search run).

Meaning in the trainer's units. The trainer spends one training run. Under the bottom
oracle an attacker that must come within $a$ of the best advantage on every learning
function with $k$ views spends order $k/a^2$ runs. LiRA's $64$ to $256$ runs per
benchmark (`fact-lira-priced-in-training-runs`) sit below this worst case because its
Gaussian model restricts the class, and BCH22's thousands of shadow runs and its failure
without the initialization (`fact-balle-reconnn-priced-in-shadow-runs`) match the
direction of part (d) in a reconstruction game (heuristic, the games differ).

The other regime. Without the oracle the attacker samples the learning function, and
`thm-perfect-substitution` makes the bottom oracle the real procedure, so (b) and (c) are
lower bounds on the shadow training runs of every attack that treats training as a black
box. A computationally bounded attacker pays at least this price. The space
`computational-limits` asks when it pays more. Degenerate oracles. The lower bound of (c)
fails under the top oracle by (d), which meets the non-triviality bar of
`def-non-triviality-bar` for a statement about adversaries.

### prop-reconstruction-label-sandwich: the trainer's error and the representation's residual information bracket an unbounded reconstructor

status: sketch

uses: fact-balle-reconstruction-robustness-definition, fact-pac-privacy-mutual-information-bound, fact-pac-privacy-gaussian-release-bound, fact-zhao-accuracy-forces-attribute-leakage

Statement. Let $(\mathcal X,d)$ be a Polish metric space, $\mathcal Y$ finite and
$\mathcal Z$ standard Borel, and let $(X,Y,Z)$ have any joint law on
$\mathcal X\times\mathcal Y\times\mathcal Z$. Let $\mathcal Y^+$ be the labels of positive
probability. For $\eta>0$ and $y\in\mathcal Y^+$ let
$\kappa_y(\eta)=\sup_{x_0\in\mathcal X}\Pr[d(X,x_0)\le\eta\mid Y=y]$ and
$\bar\kappa(\eta)=\sum_{y\in\mathcal Y^+}\Pr[Y=y]\kappa_y(\eta)$. Let
$S^\star(\eta)=\sup_R\Pr[d(X,R(Z))\le\eta]$ over measurable $R:\mathcal Z\to\mathcal X$,
let $\varepsilon^\star=\inf_{\hat y}\Pr[\hat y(Z)\neq Y]$ over measurable
$\hat y:\mathcal Z\to\mathcal Y$, and let $I(X;Z\mid Y)=\sum_{y\in\mathcal Y^+}\Pr[Y=y]\,\mathrm{KL}(P_{XZ\mid y}\|P_{X\mid y}\otimes P_{Z\mid y})$,
possibly infinite.

1. Floor. $S^\star(\eta)\ge\bar\kappa(\eta)-\varepsilon^\star$. For every measurable head
   $h$ with error $\varepsilon_h$ and every $\zeta>0$ the decoder $R_h(z)=x_{h(z)}$, with
   $x_y$ within $\zeta$ of the supremum in $\kappa_y$, succeeds with probability at least
   $\bar\kappa(\eta)-\varepsilon_h-\zeta$.
2. Ceiling. If $S^\star(\eta)\ge\bar\kappa(\eta)$ then
   $\mathrm{kl}(S^\star(\eta)\|\bar\kappa(\eta))\le I(X;Z\mid Y)$. Hence always
   $S^\star\le\bar\kappa+\sqrt{I(X;Z\mid Y)/2}$, and, if $0<\bar\kappa<1$,
   $S^\star\le(I(X;Z\mid Y)+\ln2)/\ln(1/\bar\kappa)$.
3. Gaussian release. If $Z=f(X)+B$ with $f:\mathcal X\to\mathbb R^D$ measurable,
   $\mathbb E\|f(X)\|^2<\infty$, $B\sim\mathcal N(0,\Sigma_B)$ with $\Sigma_B$ positive
   definite and $B$ independent of $(X,Y)$, then
   $I(X;Z\mid Y)\le\sum_{y\in\mathcal Y^+}\Pr[Y=y]\,\frac12\ln\det(I+\Sigma_{f\mid y}\Sigma_B^{-1})$,
   with $\Sigma_{f\mid y}$ the covariance of $f(X)$ given $Y=y$.
4. Tightness. If $Z=Y$ then $\varepsilon^\star=0$, $I(X;Z\mid Y)=0$ and
   $S^\star=\bar\kappa$. If $Z=f(X)$ for an injective Borel $f$, then $S^\star(\eta)=1$
   for every $\eta>0$.

Proof. Regular conditional laws exist on these spaces, and every success event
$\{d(X,R(Z))\le\eta\}$ is measurable, since $d$ is continuous and $R$ measurable.

Floor. The decoder $R_h$ takes finitely many values, so it is measurable. Its success is
at least $\Pr[d(X,x_Y)\le\eta,\ h(Z)=Y]\ge\Pr[d(X,x_Y)\le\eta]-\Pr[h(Z)\neq Y]\ge\bar\kappa-\zeta-\varepsilon_h$.
A Bayes classifier attains $\varepsilon^\star$, and $\zeta\to0$ gives the first claim.

Ceiling. Let $Q(dx,dy,dz)=\Pr[Y\in dy]P_{X\mid y}(dx)P_{Z\mid y}(dz)$, so
$\mathrm{KL}(P_{XYZ}\|Q)=I(X;Z\mid Y)$. For every $R$, the event $E_R$ has
$Q(E_R)=\sum_y\Pr[Y=y]\int P_{Z\mid y}(dz)\Pr[d(X,R(z))\le\eta\mid Y=y]\le\bar\kappa$. Data
processing for the indicator of $E_R$ gives
$\mathrm{kl}(P(E_R)\|Q(E_R))\le I(X;Z\mid Y)$. If $P(E_R)\ge\bar\kappa$, then
$\mathrm{kl}(P(E_R)\|\bar\kappa)\le\mathrm{kl}(P(E_R)\|Q(E_R))$, since
$q\mapsto\mathrm{kl}(p\|q)$ is nonincreasing on $[0,p]$. Take $R_j$ with
$P(E_{R_j})\to S^\star$, and use lower semicontinuity of $\mathrm{kl}(\cdot\|\bar\kappa)$
on $[\bar\kappa,1]$. Pinsker's inequality $\mathrm{kl}(p\|q)\ge2(p-q)^2$ gives the second
form, and the case $S^\star<\bar\kappa$ is trivial. For the third form,
$\mathrm{kl}(p\|q)\ge p\ln(1/q)-\ln2$, which bounds $S^\star$ when $S^\star\ge\bar\kappa$.
When $S^\star<\bar\kappa$ the bound holds too, since
$\bar\kappa\le\ln2/\ln(1/\bar\kappa)$ on $(0,1)$, as $u\ln(1/u)\le1/e<\ln2$.

Gaussian release. Fix $y\in\mathcal Y^+$. Given $Y=y$, $Z$ has a density and covariance
$\Sigma_{f\mid y}+\Sigma_B$, and given $(X,Y)$ it is Gaussian with covariance $\Sigma_B$.
So $I(X;Z\mid Y=y)=h(Z\mid Y=y)-h(B)$ with both entropies finite, and the Gaussian
maximizes entropy at fixed covariance, which gives
$\frac12\ln\det(\Sigma_{f\mid y}+\Sigma_B)-\frac12\ln\det\Sigma_B$.

Tightness. For $Z=Y$, the ceiling gives $S^\star\le\bar\kappa$ and the floor gives
$S^\star\ge\bar\kappa$. For injective Borel $f$ on a Polish space the inverse on the
image is Borel (Lusin and Souslin), so $R=f^{-1}$ recovers $X$. $\square$

Status. Sketch, pending a discussant's check of the measurability steps. The proof is
elementary. The ceiling is Theorem 1 of XD23 with side knowledge $Y$ (its Remark 1),
applied to an adversary that does not hold $Y$.

Reading in the trainer's terms. The floor is Halil's lower bound in the statistical
regime, in the exact form an unbounded reconstructor permits. It recovers at least
the class-conditional prior of the label the trained head predicts, less the head's
error. The ceiling says the gain over that floor is paid for only by what the
representation carries beyond the label. Part 4 shows that for a deterministic
injective representation the statistical baseline is total, so the content of the
reconstruction example lies in the computational regime, or in noisy, quantized or
many-to-one representations. The proposition does not show that learning a
reconstructor needs the trainer's samples, capacity or training cost.

Experiment. Train a split network on MNIST with Gaussian noise of positive definite
covariance at the cut. Measure the head's test error. Fix a finite candidate set
$\mathcal C$ of centres in advance, such as held-out training points, and estimate the
class-conditional ball masses on $\mathcal C$ from $m_y$ samples per class. Hoeffding's
inequality and a union bound give a deviation of
$\sqrt{\ln(2|\mathcal C||\mathcal Y|/\alpha)/(2m_y)}$ for all of them with probability
$1-\alpha$ (proven, standard), and the floor with $\mathcal C$ in place of $\mathcal X$ is
a valid floor, attained by the class-centre decoder. Every learned decoder obeys the
ceiling. The ceiling needs $\bar\kappa$ over all balls and the class-conditional
covariances, and the space claims no estimation rate for the supremum over balls
(open).

The other regime. A bounded reconstructor may fall far below $S^\star$, and whether it
must, when the representation is injective, is the question of the space
`computational-limits`. This proposition is the statistical floor and ceiling it is
compared with.
