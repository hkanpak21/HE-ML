# Round 03 of statistical-limits: the aims of milestone 2

Builder: the space session of `statistical-limits`, 2026-10-25.

This round states the three aims of milestone 2 named in the README, and proves the parts
that the builder can already prove, so that rounds 04 and 05 can spend themselves on what
stays open. No challenge is open from round 02. Two facts enter, read on 2026-10-25 in the
library PDFs, with their notes filled in the same session. The objects of other spaces used
here are accepted objects of the booklet, named by slug: `def-seed-blind-reconstruction-game`,
`lem-equivariant-view-coupling`, `lem-whitening-gives-rotated-records`,
`thm-reconstruction-from-conditional-mean`, `prop-sq-label-relevant-reconstruction-bound`,
`thm-blind-split-seed-separation` and `fact-lei-random-expansive-layers-invertible`, from the
space `computational-limits`. From this space, `fact-hsu-membership-sample-gap`,
`fact-hsu-gap-prices-covariance` and `def-uniform-security-profile`.

Notation. $\gamma_d$ is the standard Gaussian law on $\mathbb R^d$, $\sigma$ the uniform law on
the unit sphere $S^{d-1}$, $\|\cdot\|$ the Euclidean or operator norm and $\|\cdot\|_F$ the
Frobenius norm. For records $x_1,\dots,x_N$, $\bar x$ is their mean and
$S=\frac1N\sum_i(x_i-\bar x)(x_i-\bar x)^\top$ their sample covariance. For the mean estimation
problem of HSU25, $d^\star=n+n^2\rho^2$.

## Responses to challenges

None. Round 02 ended with no challenge.

## Facts entering this round

### fact-subgaussian-sample-covariance-concentration: the sample covariance of sub-gaussian rows concentrates in operator norm

status: borrowed

uses: none

Statement. Key BRST21, Bruna, Regev, Song and Tang, Continuous LWE, STOC 2021, Lemma 7.4,
which the paper quotes from Vershynin, High-Dimensional Probability (2018), Theorem 4.6.1. Let
$A$ be an $N\times d$ matrix whose rows are independent, mean zero, sub-gaussian and
isotropic in $\mathbb R^d$, and $K=\max_i\|A_i\|_{\psi_2}$. For every $u\ge0$, with
probability at least $1-2e^{-u^2}$,

$$\Big\|\frac1NA^\top A-I_d\Big\|\le K^2\max(\delta,\delta^2),\qquad\delta=C\Big(\sqrt{\frac dN}+\frac u{\sqrt N}\Big),$$

for an absolute constant $C>0$.

Proof. Borrowed. BRST21 states it without proof and cites Vershynin. The book is not in the
library, and this session has not read it.

The other regime. A statement about samples. It holds whatever the estimator's running time,
and the estimator here is the sample covariance itself.

### fact-single-index-information-theoretic-rate: an inefficient estimator recovers a single-index direction from order d samples

status: borrowed

uses: none

Statement. Key DPLB24, Damian, Pillaud-Vivien, Lee and Bruna, Computational-Statistical Gaps
in Gaussian Single-Index Models, COLT 2024, Theorem 6.1. For the single-index model of the
paper with generative exponent $k^\star$ and the associated coefficient $\lambda_{k^\star}$,
for every $k\ge1$ there is a procedure that returns $\hat w$ with $(w^\star\cdot\hat w)^2\ge1-\epsilon^2$
with probability at least $1-2e^{-d}$ once $n=\tilde\Theta(d/(\lambda_k^2\epsilon^2))$. The
estimator optimizes a correlation over the sphere and applies a corrector step from Damian and
others (the paper's [DH21, Theorem 5]). The paper calls it inefficient and pairs it with the SQ
and low-degree lower bounds of order $d^{k^\star/2}$ to state a computational-statistical gap
for $k^\star>2$ (§6 and §7).

Proof. Borrowed. §6 states it and refers the proof to its appendix, which this session has not
read.

The other regime. The rate is statistical. The efficient rate is $d^{k^\star/2}$, which
`prop-sq-label-relevant-reconstruction-bound` of `computational-limits` carries over to the
split-learning server.

## Aim 1. The statistical baseline of blind reconstruction

### thm-blind-orbit-limit: an unbounded seed-blind server learns the records only up to the symmetry of the record law

status: sketch

uses: def-seed-blind-reconstruction-game, lem-equivariant-view-coupling

Setting. A protocol of the class $\mathcal P_H$ of `def-seed-blind-reconstruction-game`, frozen
or trained, with records $x_1,\dots,x_N$ i.i.d. from $D$ and side data as in its item 5. The
symmetry group of the record law is the closed subgroup $G_D=\{Q\in H:Q_\#D=D\}$, with Haar
probability $\nu_{G_D}$. A seed-blind server is any measurable map $A$ of the view
$\mathcal V$, with no bound on computation.

Statement.

(a) Invariance. For every $Q\in G_D$,
$(\mathcal V,x_1,\dots,x_N)\overset d=(\mathcal V,Qx_1,\dots,Qx_N)$.

(b) No reconstruction beyond the orbit. For every server output $t_{1:N}=A(\mathcal V)$ and every
$\epsilon>0$,

$$\Pr\big[\|t_i-x_i\|\le\epsilon\ \text{for all}\ i\big]\le\mathbb E\,c_{G_D}(x_1,\epsilon),\qquad c_G(x,\epsilon)=\sup_{y}\nu_G\{Q:\|y-Qx\|\le\epsilon\}.$$

(c) Gaussian records. If $H=G_D=O(d)$, which holds for $D=\gamma_d$ and orthogonally
equivariant training from Gaussian initialization, then for every server and every
$\epsilon\le\sqrt d/(2\sqrt2)$, and already for the first record,

$$\Pr[\|t_1-x_1\|\le\epsilon]\le\tfrac12e^{-d/16}+2e^{-0.31d}.$$

(d) What can be learned. The tuple modulo the diagonal action of $G_D$ is not excluded by (a).
For $G_D=O(d)$ its maximal invariant is the Gram matrix $(\langle x_i,x_j\rangle)_{i,j}$, and
`prop-whitening-orbit-sample-price` and `prop-relu-client-second-moment-identifies-weights`
below give servers that approach it.

Proof. (a) By `lem-equivariant-view-coupling`, for fixed $Q\in H$,
$(\mathcal V(\omega;x,y),x,y)\overset d=(\mathcal V(\omega;Qx,y),x,y)$. Item 5 of the protocol
class makes the side data $y_i=Y(x_i,\xi_i)=Y(Qx_i,\xi_i)$. Write $x'_i=Qx_i$. For
$Q\in G_D$ the tuple $x'$ is again i.i.d. from $D$, independent of $(\omega,\xi)$, so
$(\mathcal V(\omega;x',Y(x',\xi)),Q^\top x')$ has the law of $(\mathcal V,Q^\top x)$, while by
the lemma it has the law of $(\mathcal V,x)$. Replacing $Q$ by $Q^\top\in G_D$ gives (a).

(b) The event is a measurable function of $(\mathcal V,x)$, so by (a) its probability is the
same with $x_i$ replaced by $Qx_i$ for every $Q\in G_D$. Average over $Q\sim\nu_{G_D}$,
independent of everything, and drop all conditions but the first:
$\Pr[F_\epsilon]=\mathbb E\,\nu_{G_D}\{Q:\|t_i-Qx_i\|\le\epsilon\ \forall i\}\le\mathbb E\,\nu_{G_D}\{Q:\|t_1-Qx_1\|\le\epsilon\}\le\mathbb E\,c_{G_D}(x_1,\epsilon)$,
by Fubini, since $Q$ is independent of $(t,x)$.

(c) For $G=O(d)$ and $x\neq0$, $Qx$ is uniform on the sphere of radius $r=\|x\|$. For
$\epsilon<r$, $\|y-r\theta\|\le\epsilon$ forces
$\langle y/\|y\|,\theta\rangle\ge(\|y\|^2+r^2-\epsilon^2)/(2r\|y\|)\ge\sqrt{1-\epsilon^2/r^2}$, the
minimum over $\|y\|$ being at $\|y\|=\sqrt{r^2-\epsilon^2}$. So $c_{O(d)}(x,\epsilon)$ is at most
the $\sigma$-measure of a cap $\{\theta:\langle e,\theta\rangle\ge s\}$ with $s=\sqrt{1-\epsilon^2/r^2}$.
Write $\theta=g/\|g\|$ with $g\sim\gamma_d$. Then
$\sigma\{\langle e,\theta\rangle\ge s\}\le\Pr[g_1\ge s\sqrt d/2]+\Pr[\|g\|^2<d/4]\le\frac12e^{-s^2d/8}+e^{-0.318d}$,
using $\Pr[g_1\ge t]\le\frac12e^{-t^2/2}$ and the Chernoff bound
$\Pr[\|g\|^2\le d/4]\le e^{3d/8}(1+3)^{-d/2}=e^{-(\ln2-3/8)d}$. On the event $\|x_1\|\ge\sqrt d/2$,
$\epsilon\le\sqrt d/(2\sqrt2)$ gives $s^2\ge1/2$. The same Chernoff bound gives
$\Pr[\|x_1\|<\sqrt d/2]\le e^{-0.318d}$, and (b) finishes. (d) For $G=O(d)$, two tuples have
the same Gram matrix exactly when one is the image of the other under some $Q\in O(d)$, which is
the standard characterization of congruent point configurations. $\square$

Status. Sketch until a round accepts it. No gap is known to the builder.

What would settle the aim. Parts (a) to (c) are proved here. The aim is settled when the
sample price of reaching the orbit limit is bounded on both sides, which
`prop-whitening-orbit-sample-price` does from above for frozen linear clients and
`conj-blind-orbit-price-lower-bound` asks from below.

Regime. Statistical. The server is unbounded.

Experiment. Train a split network with an orthogonally equivariant optimizer on Gaussian
records, run any reconstruction attack, and check that its rate of reconstructing a record
within $\sqrt d/(2\sqrt2)$ is exponentially small in $d$, while its error modulo rotation, which
an experiment computes by orthogonal Procrustes, can be small.

The other regime. The bound holds for every server, so it holds for efficient ones. It is the
statistical form of the remark of `computational-limits` that Gaussian records are learned only
up to a common rotation, and it is total. No number of records, no training, and no computation
moves a seed-blind server past the orbit. For a record law with a smaller symmetry group, such as
the pancake law $H_{v,\beta,\gamma}$ with $G_D=\{Q:Qv=\pm v\}$, the theorem allows the hidden
coordinate to be learned, and its price is computational (`thm-blind-split-seed-separation`).

### prop-whitening-orbit-sample-price: empirical whitening of a frozen affine client returns the affine shape of the records

status: sketch

uses: thm-blind-orbit-limit, lem-whitening-gives-rotated-records

Setting. A frozen client $z=Wx+b$ with $W\in\mathbb R^{m\times d}$ of full column rank and any
$b$, both unknown to the server. Records $x_1,\dots,x_N$ with $N\ge d+1$ and $S$ invertible. The
server computes $\bar z$, $\hat\Sigma=\frac1N\sum_i(z_i-\bar z)(z_i-\bar z)^\top$, an orthonormal
basis $B$ of the range of $\hat\Sigma$ by a fixed measurable rule, and
$u_i=B^\top\hat\Sigma^{+1/2}(z_i-\bar z)$.

Statement.

(i) Exact identity. $u_i=Pw_i$ for all $i$, where $w_i=S^{-1/2}(x_i-\bar x)$ are the empirically
whitened records and $P\in O(d)$ depends on $W$ and the records. The server's output is
therefore a function of the affine shape of the record tuple alone, whatever $W$ and $b$ are.

(ii) Orbit error. For records with mean zero and identity covariance, the orbit error
$\mathcal E_N=\min_{Q\in O(d)}\frac1N\sum_i\|Qu_i-x_i\|^2$ satisfies

$$\mathcal E_N\le\frac1N\sum_i\|w_i-x_i\|^2=\sum_{k\le d}\big(1-\sqrt{\lambda_k(S)}\big)^2+\|\bar x\|^2\le\|S-I_d\|_F^2+\|\bar x\|^2.$$

(iii) Gaussian records. For $x_i\sim\gamma_d$,
$\mathbb E\,\mathcal E_N\le\frac{(N-1)d^2}{N^2}+\frac{2d}N\le\frac{d^2+2d}N$, so the relative
mean-square orbit error $\mathbb E\mathcal E_N/d$ is at most $\epsilon^2$ once $N\ge(d+2)/\epsilon^2$.

Proof. (i) With $W=OA$, $A=(W^\top W)^{1/2}$ and $O$ of orthonormal columns,
$z_i-\bar z=OA(x_i-\bar x)$ and $\hat\Sigma=O(ASA)O^\top$, so
$\hat\Sigma^{+1/2}=O(ASA)^{-1/2}O^\top$ and $u_i=B^\top O\,(ASA)^{-1/2}A(x_i-\bar x)$. Here
$R=B^\top O\in O(d)$, as in `lem-whitening-gives-rotated-records`. The matrix
$K=(ASA)^{-1/2}A$ satisfies $KSK^\top=I_d$, so $U=KS^{1/2}$ is orthogonal and $K=US^{-1/2}$. Hence
$u_i=RUS^{-1/2}(x_i-\bar x)$ and $P=RU$. (ii) Take $Q=P^\top$. Since $\sum_i(x_i-\bar x)=0$,
$\frac1N\sum_i\|S^{-1/2}(x_i-\bar x)-x_i\|^2=\frac1N\sum_i\|(S^{-1/2}-I)(x_i-\bar x)\|^2+\|\bar x\|^2=\mathrm{tr}\big((S^{-1/2}-I)S(S^{-1/2}-I)\big)+\|\bar x\|^2$,
which is $\mathrm{tr}((I-S^{1/2})^2)+\|\bar x\|^2$. Finally $|1-\sqrt\lambda|\le|1-\lambda|$ for
$\lambda\ge0$. (iii) For Gaussian records $S$ has the law of $\frac1N\sum_{j<N}g_jg_j^\top$ with
$g_j$ i.i.d. from $\gamma_d$, and $\bar x$ is independent of $S$ with
$\mathbb E\|\bar x\|^2=d/N$. With $G=\sum_{j<N}g_jg_j^\top$,
$\mathbb E\,\mathrm{tr}(G^2)=(N-1)(d^2+2d)+(N-1)(N-2)d$ from $\mathbb E\|g\|^4=d^2+2d$ and
$\mathbb E\langle g_j,g_l\rangle^2=d$ for $j\neq l$, and $\mathbb E\,\mathrm{tr}G=(N-1)d$. So
$\mathbb E\|G/N-I\|_F^2=\frac{(N-1)(d^2+Nd)}{N^2}-\frac{2(N-1)d}N+d=\frac{(N-1)d^2}{N^2}+\frac dN$. $\square$

Status. Sketch until a round accepts it. No gap is known to the builder.

Heuristic refinement. Near $\lambda=1$, $(1-\sqrt\lambda)^2=(1-\lambda)^2/(1+\sqrt\lambda)^2\approx(1-\lambda)^2/4$,
so $\mathbb E\mathcal E_N\approx d^2/(4N)$ for $N\gg d$ (heuristic, the eigenvalues of $S$ lie
near one when $N\gg d$).

The other regime. The server is efficient, a covariance and a square root. A seed-known server
recovers every record exactly, so for frozen linear clients the seed is worth the orbit
(by `thm-blind-orbit-limit`) plus an error of order $d^2/N$ per record (by this proposition).

### prop-relu-client-second-moment-identifies-weights: a frozen Gaussian ReLU client is identified up to rotation by its second moment

status: sketch

uses: thm-blind-orbit-limit, fact-lei-random-expansive-layers-invertible

Setting. A frozen client $z=\mathrm{ReLU}(Wx)$ with $W\in\mathbb R^{m\times d}$ of rank $d$
and rows $w_1,\dots,w_m$, nonzero and pairwise non-parallel, and records $x\sim\gamma_d$. Let
$\Gamma=\mathbb E[zz^\top]$, the population second moment of the representations.

Statement.

(i) Kernel identity. $\Gamma_{jj}=\|w_j\|^2/2$, and for $j\neq k$ with
$\cos\theta_{jk}=\langle w_j,w_k\rangle/(\|w_j\|\|w_k\|)$,
$\Gamma_{jk}=\|w_j\|\|w_k\|\,\kappa(\theta_{jk})$ with
$\kappa(\theta)=(\sin\theta+(\pi-\theta)\cos\theta)/(2\pi)$, strictly decreasing on $[0,\pi]$.

(ii) Identification. $\Gamma$ determines $WW^\top$, and so determines $W$ up to right
multiplication by an element of $O(d)$.

(iii) Blind inversion at the population level. Let $W$ have i.i.d. Gaussian entries with
$m\ge2.1d$, which meets Assumption 1 of LJDD19. A server that knows $\Gamma$ computes
$\tilde W$ with $\tilde W\tilde W^\top=WW^\top$, so $\tilde W=WQ$ for some $Q\in O(d)$, and
solves $\mathrm{ReLU}(\tilde W\tilde x)=z_i$ on the positive coordinates. It returns
$\tilde x_i=Q^\top x_i$ for every record, with probability at least $1-Ne^{-\Omega(d)}$, in
polynomial time. So the orbit limit of `thm-blind-orbit-limit` is attained.

Proof. (i) For $(a,b)$ jointly Gaussian with variances $s_a^2,s_b^2$ and correlation
$\cos\theta$, write $a=s_a\langle g,e\rangle$ and $b=s_b\langle g,e'\rangle$ with $g\sim\gamma_2$
and unit vectors at angle $\theta$. In polar coordinates $g=r(\cos\phi,\sin\phi)$,
$\mathbb E[\mathrm{ReLU}(a)\mathrm{ReLU}(b)]=\frac{s_as_b}{2\pi}\int_0^\infty r^3e^{-r^2/2}dr\int_{\theta-\pi/2}^{\pi/2}\cos\phi\cos(\phi-\theta)\,d\phi$,
since both factors are positive exactly on that arc of length $\pi-\theta$. The radial integral is
$2$, and the angular one is
$\frac12(\pi-\theta)\cos\theta+\frac14[\sin(2\phi-\theta)]_{\theta-\pi/2}^{\pi/2}=\frac12((\pi-\theta)\cos\theta+\sin\theta)$.
So the expectation is $s_as_b\kappa(\theta)$. With $\theta=0$ it gives $\Gamma_{jj}=\|w_j\|^2/2$.
Also $\kappa'(\theta)=-(\pi-\theta)\sin\theta<0$ on $(0,\pi)$. (ii) $\Gamma_{jj}$ gives
$\|w_j\|$, and $\kappa$ is injective, so $\Gamma_{jk}$ gives $\theta_{jk}$ and hence
$\langle w_j,w_k\rangle$. Two $m\times d$ matrices of rank $d$ with the same Gram matrix
$WW^\top$ differ by right multiplication by an orthogonal matrix. (iii) $\tilde W$ is any
factor of $WW^\top$, from an eigendecomposition. For each record,
$\mathrm{ReLU}(\tilde W\tilde x)=z_i$ has the solution $\tilde x=Q^\top x_i$, and it is the only
one with probability $1-e^{-\Omega(d)}$ by LJDD19 Lemma 1 and Theorem 3
(`fact-lei-random-expansive-layers-invertible`), since $x_i$ is independent of $W$ and the
solution set of the system on the positive coordinates is invariant under the change of variables
by $Q$. A union bound over the records finishes. $\square$

Status. Sketch until a round accepts it. No gap is known to the builder in (i) to (iii). The
sample price, with $\Gamma$ estimated from $N$ representations, is open.

The other regime. At the population level the inversion is polynomial, so for Gaussian records a
frozen Gaussian ReLU client protects nothing beyond the orbit against an efficient server. The
open upper inclusion of `conj-seed-price-is-ngca-price` (`prob-blind-inversion-relu-clients` of
`computational-limits`) concerns non-Gaussian isotropic record laws, where the kernel identity of
(i) holds only approximately. This proposition is the Gaussian case of it, exact, and it is a lead
for that space.

### conj-blind-orbit-price-lower-bound: the order d squared over N is the statistical price of the orbit

status: open

uses: prop-whitening-orbit-sample-price, thm-blind-orbit-limit

Statement. Let the frozen client be linear, $z=Wx+b$, and the records Gaussian. (a) Minimax
form. There is an absolute $c>0$ such that, for $N\ge2d$, every seed-blind server has
$\sup_W\mathbb E\,\mathcal E_N\ge c\,d^2/N$, where the supremum ranges over full-column-rank $W$
with $\|W^\top W-I\|\le1/2$. (b) Gaussian-weight form. For $W$ with i.i.d. Gaussian entries and
$m=c'd$, every seed-blind server has $\mathbb E\,\mathcal E_N\ge c\,d^2/(N+m)$ for $N\ge2d$.

What would settle it. (a) A reduction from orbit reconstruction to estimation of the covariance
$W^\top W$ in Frobenius norm from $N$ Gaussian samples, followed by a Fano bound over a packing of
covariances, which this space would prove since no covariance-estimation lower bound is in the
library. (b) A mutual-information argument. The view of a frozen linear client determines the
row space of the record matrix and, up to the same rotation, the product $WS^{1/2}$, whose rows
are $m$ samples of $\mathcal N(0,S)$ given $S$. So the information about the anisotropy of $S$
is that of $m$ samples against a prior of $N$, and the posterior spread stays of order
$\sqrt{d/(N+m)}$ in operator norm (heuristic). A refutation would be a server that beats
empirical whitening by more than a constant factor when $N\ge2d$.

Regime. Statistical. Experiment. Compare empirical whitening with a Bayes-motivated estimator
that also uses the spectrum of $\hat\Sigma$, at $d\in\{32,64,128\}$ and $N/d\in\{2,8,32\}$.

## Aim 3. Train access and the sample price of HSU25

### thm-train-access-price-frontier: Train calls replace population samples in the membership price of noisy mean estimation

status: sketch

uses: fact-hsu-membership-sample-gap, fact-hsu-gap-prices-covariance, fact-subgaussian-sample-covariance-concentration, def-uniform-security-profile

Setting. The population is $\mathcal N(\mu,\Sigma)$ with $\Sigma$ positive definite, both
unknown. The learning function is the estimator of HSU25 Definition 2.4,
$\mathsf L_\Sigma(D;\xi)=\frac1n\sum_{x\in D}x+\rho\Sigma^{1/2}\xi$ with $\rho>0$ and
hardware randomness $\xi\sim\gamma_d$, for a dataset $D$ of $n$ points. The modelling hypothesis
is that Train runs the estimator with the population's noise covariance, as the estimator is
defined. The attacker of HSU25 Definition 2.1 receives the release $\hat\mu=\mathsf L_\Sigma(S_n;\xi)$,
a target, $m$ reference samples, and may make $N$ Train calls on datasets of its choice under the
bottom oracle. The criterion $C_{\rm HSU}$ asks for false-positive rate at most $0.49$ and true-positive rate
at least $0.51$ at every population of the family.

Statement.

(a) Unknown covariance, lower bound. If $d>c_1d^\star$ and $m+2N\le c_2d^\star$, with $c_1,c_2$
the constants of HSU25 Theorem 3.1, no attack meets $C_{\rm HSU}$ over $\mathcal P_d$.

(b) Known covariance, lower bound. Over $\mathcal P^{\mathrm{id.cov}}_d$, if $n\ge4$, $m\ge2$ and
$d<c(n+n^2\rho^2+n^2/m)$ with $c$ the constant of HSU25 Theorem 4.1, no attack meets
$C_{\rm HSU}$, whatever $N$ is.

(c) Upper bound, a Train-access attack. Let $d\ge2100\,d^\star$, $m-1\ge\min\{n,1/\rho^2\}$ and
$N\ge C_0d$ for an absolute constant $C_0$. The attack below meets $C_{\rm HSU}$ over
$\mathcal P_d$. It makes $N$ Train calls on one fixed dataset $D_0$ and computes
$W_j=\mathsf L(D_0;\cdot)-\frac1n\sum_{x\in D_0}x$ and $\hat S=\frac1{N\rho^2}\sum_{j\le N}W_jW_j^\top$.
It holds out one reference sample $Y_0$, averages the other $m-1$ into $\bar\mu$, and accepts the
target $X$ as a member iff
$$T=(\hat\mu-\bar\mu)^\top\hat S^{-1}(X-Y_0)\ \ge\ \frac d{2n}.$$

(d) The frontier. Let $\rho<1$ and $d=\kappa d^\star$ with
$\kappa\ge\max\{c_1,c_3,2100\}$ and $\kappa>c$, where $c_3$ is the constant of HSU25 Theorem 3.3 and
$c$ that of Theorem 4.1. With Train access the sample price is $\Theta_\kappa(\min\{n,1/\rho^2\})$
reference samples, bought with $\Theta_\kappa(d^\star)$ Train calls, against $\Theta_\kappa(d^\star)$
samples with no Train call (HSU25 Theorems 3.1 and 3.3). In combined units, samples plus Train calls, the price is
$\Theta_\kappa(d^\star)$ either way. So Train access collapses the sample price, and it does not
lower the price in combined units.

Proof. (a) Simulation. A Train call on a dataset $D$ returns $\frac1n\sum_{x\in D}x+\rho\Sigma^{1/2}\xi$
with $\xi$ fresh. For two fresh reference samples $Y,Y'$, $(Y-Y')/\sqrt2\sim\mathcal N(0,\Sigma)$,
so $\frac1n\sum_{x\in D}x+\rho(Y-Y')/\sqrt2$ has the law of the answer and is independent of
everything else, as the answer is. An attacker with $m$ samples and $N$ Train calls is therefore a
randomized attacker with $m+2N$ samples and no Train call, with the same success at every
population. HSU25 Theorem 3.1 excludes it. Its proof bounds the total variation between the two
mixture laws of the attacker's observation by $0.02$ (§3.2.4), and Le Cam's bound of Lemma 2.6
holds for randomized tests by averaging over their coins, so the exclusion covers randomized
attackers (`fact-hsu-membership-sample-gap`). (b) Over $\mathcal P^{\mathrm{id.cov}}_d$ the noise
law $\mathcal N(0,\rho^2I_d)$ is known, so Train calls are simulated with no sample at all, and
HSU25 Theorem 4.1 applies (`fact-hsu-gap-prices-covariance`).

(c) Whitened coordinates. Let $\hat G=\Sigma^{-1/2}\hat S\Sigma^{-1/2}=\frac1N\sum_jg_jg_j^\top$
with $g_j=\Sigma^{-1/2}W_j/\rho$ i.i.d. from $\gamma_d$, and $A=\hat G^{-1}$, independent of the
release, the target and the reference samples. With $a=\Sigma^{-1/2}(\hat\mu-\bar\mu)$ and
$b=\Sigma^{-1/2}(X-Y_0)$, $T=a^\top Ab$, and $\mu$ cancels. By
`fact-subgaussian-sample-covariance-concentration` with $u=2.4$, the event
$\mathcal G=\{\|\hat G-I\|\le\frac12\}$ has probability at least $0.99$ once $N\ge C_0d$, and on
it the eigenvalues of $A$ lie in $[\frac23,2]$, so $\mathrm{tr}A\ge\frac{2d}3$ and
$\mathrm{tr}A^2\le4d$. Let $s^2=\frac1n+\rho^2+\frac1{m-1}$. Then $n^2s^2\le2d^\star$, because
$m-1\ge\min\{n,1/\rho^2\}$ gives $n^2/(m-1)\le\max\{n,n^2\rho^2\}$.

OUT. The target is fresh, so $a\sim\mathcal N(0,s^2I)$ and $b\sim\mathcal N(0,2I)$ are
independent given $A$. Then $\mathbb E[T\mid A]=0$ and $\mathbb E[T^2\mid A]=2s^2\mathrm{tr}A^2$.
By Chebyshev on $\mathcal G$, the false-positive rate is at most
$0.01+2s^2\cdot4d\cdot(2n/d)^2=0.01+32n^2s^2/d\le0.01+64d^\star/d\le0.05$.

IN. The target is $X_1$, a member. Write $G_1=\Sigma^{-1/2}(X_1-\mu)$, $h=\Sigma^{-1/2}(Y_0-\mu)$
and $a=G_1/n+a'$ with $a'\sim\mathcal N(0,s'^2I)$, $s'^2=\frac{n-1}{n^2}+\rho^2+\frac1{m-1}\le s^2$,
independent of $(G_1,h)$. Then
$T=\frac1nG_1^\top AG_1+a'^\top AG_1-\frac1nG_1^\top Ah-a'^\top Ah$. The four terms are
pairwise uncorrelated given $A$, since each pair has a factor odd in one of the independent
symmetric vectors $a'$ and $h$. Their variances are $2\mathrm{tr}A^2/n^2$, $s'^2\mathrm{tr}A^2$,
$\mathrm{tr}A^2/n^2$ and $s'^2\mathrm{tr}A^2$. So $\mathbb E[T\mid A]=\mathrm{tr}A/n\ge\frac{2d}{3n}$,
which exceeds the threshold by $\frac d{6n}$ on $\mathcal G$, and
$\mathrm{Var}(T\mid A)\le(3/n^2+2s^2)4d$. By Chebyshev on $\mathcal G$, the false-negative rate is
at most $0.01+144(3+2n^2s^2)/d\le0.01+(432+576d^\star)/d\le0.01+1008/2100=0.49$, using
$d^\star\ge1$. So the true-positive rate is at least $0.51$ and the false-positive rate at most
$0.05$, at every population.

(d) At $d=\kappa d^\star$, (a) forces $m+2N>c_2d^\star$. Part (b) forces
$n^2/m\le d/c-d^\star$ for any attack over $\mathcal P_d$, which contains
$\mathcal P^{\mathrm{id.cov}}_d$, and $n^2/d^\star\ge\frac12\min\{n,1/\rho^2\}$, so
$m\ge\frac c{2\kappa}\min\{n,1/\rho^2\}$ once $\kappa>c$. Part (c) gives the point
$(m,N)=(\lceil\min\{n,1/\rho^2\}\rceil+1,\lceil C_0\kappa d^\star\rceil)$. HSU25 Theorem 3.3, whose class
$\mathfrak A_{n,d,\rho}$ contains the estimator, gives the point $(\lceil c_3\kappa d^\star\rceil,0)$,
since $\rho<1$ and $d\ge c_3d^\star$. $\square$

Status. Sketch until a round accepts it. The proof uses the constant $C$ and the sub-gaussian norm
$K$ of `fact-subgaussian-sample-covariance-concentration` only through $C_0$, and the constants
$c_1,c_2,c$ of HSU25 as the paper leaves them.

What would settle the aim. The theorem answers `prob-train-access-collapses-sample-price` in the
affirmative under the modelling hypothesis. In the vocabulary of `def-uniform-security-profile` it
computes the threshold price of $C_{\rm HSU}$ on both axes up to constants in the regime
$d\asymp d^\star$. The aim is settled if a round accepts it.

Regime. Statistical for (a) and (b). The attack of (c) runs in polynomial time, so the frontier is
also the price of efficient attackers.

Experiment. Implement $\mathsf L_\Sigma$ with a random $\Sigma$ in dimension $d=\kappa d^\star$,
run the attack of (c) at a grid of $(m,N)$ and measure its two error rates. The predicted
boundary is $m+N\approx d^\star$ with $m\gtrsim\min\{n,1/\rho^2\}$.

The other regime. The hypothesis matters. A mechanism that calibrates its noise to a covariance
estimated from its own input, rather than to the population's, gives Train calls on chosen data
no information about $\Sigma$, and then the sample price of HSU25 stands. That choice of mechanism
is a modelling decision, recorded for Halil in the summary.

## Aim 2. The same-units comparison of trainer and attacker

### thm-same-units-gap-gaussian-mechanism: in noisy mean estimation the attacker pays a factor one plus n rho squared over the trainer

status: sketch

uses: thm-train-access-price-frontier, fact-hsu-membership-sample-gap

Statement. In the setting of `thm-train-access-price-frontier`, with $\rho<1$ and $d=\kappa d^\star$
for $\kappa$ as in its part (d), the trainer's procedure costs $n$ samples and one training run. Every
membership attack meeting $C_{\rm HSU}$ costs more than $\frac{c_2}2d^\star$ in combined units,
samples plus Train calls, and some polynomial-time attack costs at most $C_\kappa d^\star$. So the
attacker's price exceeds the trainer's by the factor
$\frac{c_2}2\cdot\frac{n+n^2\rho^2}{n+1}\ge\frac{c_2}4(1+n\rho^2)$. With $\rho=n^{-a}$ for
$0<a<\frac12$, the trainer's sample exponent is $1$ and the attacker's exponent in combined units is
$2-2a$, while its exponent in samples alone, with Train access, is $2a$.

Proof. By (a), (c) and (d) of `thm-train-access-price-frontier`, $m+2N>c_2d^\star$ gives
$m+N>\frac{c_2}2d^\star$, and $\frac{n+n^2\rho^2}{n+1}\ge\frac12(1+n\rho^2)$ for $n\ge1$. With
$\rho=n^{-a}$, $d^\star=n+n^{2-2a}\asymp n^{2-2a}$ and $\min\{n,1/\rho^2\}=n^{2a}$. $\square$

Status. Sketch until a round accepts it.

Meaning. This is a natural procedure, the Gaussian mechanism for mean estimation with noise
calibrated to the population covariance, where the attacker's price exceeds the trainer's by a named
margin, $1+n\rho^2$, measured by the experiment of the frontier. It sharpens the placeholder
`conj-same-units-gap` in one direction. The lower bound holds for unbounded attackers, the upper bound
is attained by an efficient one, and the margin grows with the noise, which also costs the trainer
accuracy, since its error is $d(\rho^2+1/n)$. It does not settle the placeholder's own form, which
asks about a low-rank adapter and gradient-trained membership adversaries.

The other regime. The margin is statistical and survives every computational bound, because the
efficient attack meets it.

### prop-label-relevant-attacker-at-most-trainer: for the label-relevant coordinate of split learning the attacker never pays more than the trainer

status: sketch

uses: thm-reconstruction-from-conditional-mean, prop-sq-label-relevant-reconstruction-bound, lem-whitening-gives-rotated-records, fact-single-index-information-theoretic-rate

Setting. The single-index split-learning mapping of `computational-limits`. The client is frozen and
linear of full column rank, records are Gaussian, labels are $y=Y(\langle u,x\rangle,\xi)$ with
generative exponent $k^\star\ge3$, and the target is $\pm\langle u,x_i\rangle$.

Statement.

(a) With the trained head. If the trainer's predictor has excess square risk $\varepsilon_h$ with
$\sqrt{\varepsilon_h}<|\beta_1|/4$, a server with the head and the population whitening reconstructs
the target with error at most $4(\sqrt{\varepsilon_h}+\eta_N)^2/\beta_1^2$ from $N$ unlabelled
representations, with $\eta_N=B\sqrt{d/(N\delta)}$, so $N=16B^2d/(\delta\beta_1^2)$ representations
suffice (`thm-reconstruction-from-conditional-mean`).

(b) The trainer's price is at least the price of the direction. The direction estimate of
`thm-reconstruction-from-conditional-mean` is the vector of $d$ expectations
$\mathbb E[f(z)(T(z-b))_k]$, $k\le d$, of the bounded head $f$ against the whitened representation.
So a trainer that reaches a head meeting (a) through statistical queries, followed by these $d$
queries, truncated as in the proof of `prop-sq-label-relevant-reconstruction-bound`, is an SQ
procedure that recovers the direction. By that proposition its VSTAT parameter is at least
$c\,d^{k^\star/2}$, for $d$ large, whatever its own number of queries below $d^r-d$.

(c) Without the head. A server with labelled representations pays the price of learning the direction
itself, $\tilde\Theta(d)$ samples statistically (`fact-single-index-information-theoretic-rate`
applied to $(Rx_i,y_i)$) and order $d^{k^\star/2}$ under SQ
(`prop-sq-label-relevant-reconstruction-bound`), the same orders as the trainer's own task.

Proof. (a) is the cited theorem with $N$ chosen so that $\eta_N\le|\beta_1|/4$. (b) The proof of
`thm-reconstruction-from-conditional-mean` shows that the population vector
$\mathbb E[F(x)x]=\beta_1u+e'$ with $\|e'\|\le\sqrt{\varepsilon_h}$, so the $d$ truncated queries
return it to tolerance $O(d^{-1/2})$ and the normalized vector is within $2(\sqrt{\varepsilon_h}+O(d^{-1/2}))/|\beta_1|$
of $\pm u$. The composite is an SQ direction-recovery procedure, and the cited lower bound applies to
it. The truncation and the tolerance follow the reduction in that proposition's proof and are not
written out again here. (c) By
`lem-whitening-gives-rotated-records`, $(Rx_i,y_i)$ is a single-index sample with direction $Ru$, and
both cited results apply to it. $\square$

Status. Sketch until a round accepts it. Part (b) assumes the trainer is an SQ procedure, which
`fact-sq-simulates-minibatch-sgd` of `computational-limits` limits to its coarse-precision regime.

Meaning. For the label-relevant coordinate the same-units comparison goes the wrong way for
security. The trainer pays at least the direction price, of order $d^{k^\star/2}$ under SQ, and a
server holding the trained head pays order $d$ representations. The comparison refutes a same-units
gap in favour of the defender for the label-relevant coordinate. Any gap must come from information
the task does not need. In the statistical regime that information is hidden only up to
$G_D$ (`thm-blind-orbit-limit`), and for the pancake records of `thm-blind-split-seed-separation` its
price is computational, exponential in SQ queries against one training run, while its statistical
price is open (`prob-statistical-price-hidden-coordinate`, proposed in the summary).

The other regime. Parts (a) and (c) hold for every server. Part (b) is an SQ statement.
