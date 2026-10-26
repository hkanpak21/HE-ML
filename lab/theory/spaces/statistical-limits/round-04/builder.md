# Round 04 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25. Following Halil's instruction of
tonight, "simplify whenever possible", this round is short. It proves the lower bound of aim 1
for a representation-only view, restates the frontier of aim 3 in the regime where it holds, and
withdraws the aim-2 proposition that round 03 refuted. Notation is that of `round-03/builder.md`.

## Responses to challenges

ch-affine-shape-output. Accepted. The output's coordinates depend on the client. Its class under
$O(d)$ is a function of the affine shape of the records. Part (ii) of
`prop-whitening-orbit-sample-price` holds with equality, as the discussant shows, since the
cross-moment of the whitened and the centred records is $S^{1/2}$.

ch-orbit-price-side-data. Accepted. Invariant side data such as $\|x_i\|^2$ give exact
reconstruction up to rotation. The lower bound is now `thm-blind-orbit-price`, for a
representation-only view, and it bounds an observable target, the inverse square root of the
representations' covariance, under the Procrustes loss of arbitrary server outputs. The
Gaussian-weight form is dropped.

ch-train-zero-reference. Accepted. For constant $\rho$ and $d\gtrsim n^2$ the discussant's
attack needs no reference sample. Part (d) of `thm-train-access-price-frontier` is now stated
for $\rho=n^{-a}$, $0<a<\frac12$, with the domains of HSU25 propagated (`ch-hsu-frontier-domain`).

ch-hsu-input-covariance-transfer. Accepted. The claim about a mechanism with input-estimated
covariance is withdrawn, since that mechanism has a different release law.

ch-label-first-coefficient, ch-label-prediction-not-direction, ch-label-evaluation-domain,
ch-single-index-resource-classes, ch-single-index-proof-attribution. Accepted. The builder
withdraws `prop-label-relevant-attacker-at-most-trainer` and
`fact-single-index-information-theoretic-rate`.

ch-relu-kernel-derivative. Accepted. $\kappa'(\theta)=-(\pi-\theta)\sin\theta/(2\pi)$.
ch-relu-population-price. Accepted as open. The other-regime sentence on isotropic laws now
says that an approximate kernel identity needs a hypothesis on the law.
ch-gaussian-comparison-meter. Accepted. The meter is one unit per reference sample and per
Train call, the trainer's covariance calibration is free, and the error is Mahalanobis risk.
ch-hsu-proof-margin. Accepted, recorded in the round-03 summary.

## Objects

### prop-whitening-orbit-sample-price: empirical whitening of a frozen affine client returns the affine shape of the records

status: sketch

uses: thm-blind-orbit-limit, lem-whitening-gives-rotated-records

Statement and proof as in `round-03/builder.md`, with two changes. In (i), the last sentence now
says that the server's output is $Pw_{1:N}$ with $P\in O(d)$ depending on the client, so its
$O(d)$-class is a function of the affine shape of the record tuple, whatever $W$ and $b$ are. In
(ii), the first inequality is an equality, because $\frac1N\sum_iw_i(x_i-\bar x)^\top=S^{1/2}$ is
positive definite, so the Procrustes optimum is $Q=P^\top$.

### thm-blind-orbit-price: the statistical price of blind reconstruction up to rotation is order d squared over N

status: sketch

uses: prop-whitening-orbit-sample-price, prop-reconstruction-label-sandwich, fact-subgaussian-sample-covariance-concentration

Setting. Fix $O\in\mathbb R^{m\times d}$ with orthonormal columns. The class $\mathcal W$ holds the
frozen linear clients $z=OR^{-1}x$ with $R$ symmetric and eigenvalues in $[\frac34,\frac54]$. There
is no side data. Records $x_1,\dots,x_N$ are i.i.d. from $\gamma_d$. A server is any measurable map
from $z_{1:N}$ to $\hat x_{1:N}$, and it may know $O$ and $\mathcal W$. Its orbit error is
$\mathcal E_N=\min_{Q\in O(d)}\frac1N\sum_i\|Q\hat x_i-x_i\|^2$.

Statement. There are absolute constants $c,C>0$ such that, for $d\ge5$ and $N\ge Cd$:

1. Every server has, at some client in $\mathcal W$, $\Pr[\mathcal E_N>c\,d^2/N]>\frac12$, so
   $\sup_{\mathcal W}\mathbb E\,\mathcal E_N\ge\frac c2d^2/N$.
2. Empirical whitening has $\mathbb E\,\mathcal E_N\le(d^2+2d)/N$ at every client of full column
   rank (`prop-whitening-orbit-sample-price`).

So the minimax orbit price is $\Theta(d^2/N)$, and $N=\Theta(d/\epsilon^2)$ records are necessary and
sufficient for relative orbit error $\mathbb E\,\mathcal E_N/d\le\epsilon^2$.

Proof of 1. Step 1, the view. $y_i=O^\top z_i=R^{-1}x_i$, so every server is a function of
$Y=(y_1,\dots,y_N)$, and the $y_i$ are i.i.d. from $\mathcal N(0,R^{-2})$.

Step 2, the absolute value is $\sqrt2$-Lipschitz. For real $d\times d$ matrices,
$\||A|-|B|\|_F\le\sqrt2\|A-B\|_F$ with $|A|=(A^\top A)^{1/2}$. At an invertible $A=U\Sigma V^\top$,
differentiate $A^\top A=|A|^2$ in a direction $\dot A$ and write $F=U^\top\dot AV$ and
$X=V^\top\dot{|A|}V$. Then $\Sigma X+X\Sigma=\Sigma F+F^\top\Sigma$, so
$X_{ij}=(\sigma_iF_{ij}+\sigma_jF_{ji})/(\sigma_i+\sigma_j)$, a convex combination, and
$X_{ij}^2\le F_{ij}^2+F_{ji}^2$. Summing, $\|X\|_F^2\le2\|F\|_F^2$. On the segment from $B$ to $A$
the determinant is a polynomial, so the segment meets singular matrices at finitely many points or,
after an arbitrarily small perturbation of $B$, at none. Integrating the derivative bound and using
continuity of $|\cdot|$ gives the claim (proven).

Step 3, from a reconstruction to $R$. Let $\hat L=\hat XY^\top(YY^\top)^{-1}$ and $\hat R=|\hat L|$.
By `fact-subgaussian-sample-covariance-concentration` with $u=2$, for $N\ge C_1d$ the event
$\mathcal G=\{\|XX^\top/N-I\|\le\frac12\}$ has probability at least $1-2e^{-4}$. On it
$\sigma_{\min}(X)\ge\sqrt{N/2}$ and $\sigma_{\min}(Y)\ge\frac45\sqrt{N/2}$. Let $Q$ attain the
orbit error and $E=\hat X-Q^\top X$, so $\|E\|_F^2=N\mathcal E_N$. Since $X=RY$,
$\hat L=Q^\top R+EY^\top(YY^\top)^{-1}$, and $|Q^\top R|=R$. By Step 2, on $\mathcal G$,
$\|\hat R-R\|_F\le\sqrt2\|E\|_F/\sigma_{\min}(Y)\le\frac52\sqrt{\mathcal E_N}$.

Step 4, a prior on $R$. Let $R=I+\tau\,\mathrm{Sym}(A)$ with $A$ a $d\times d$ matrix of i.i.d.
standard Gaussian entries, $\mathrm{Sym}(A)=(A+A^\top)/2$ and $\tau^2=1/(40N)$, conditioned on
$\mathcal C=\{\|\tau\mathrm{Sym}(A)\|\le\frac14\}$. The same fact applied to $A$, with $u=1.2$, gives
$\|A\|\le C_A\sqrt d$ with probability above $\frac12$, so $\Pr[\mathcal C]>\frac12$ once
$N\ge C_2d$. The prior lives on $\mathcal W$. With $D=d(d+1)/2$ coordinates, the diagonal entries of
$\tau\mathrm{Sym}(A)$ are $\mathcal N(0,\tau^2)$ and the off-diagonal ones $\mathcal N(0,\tau^2/2)$,
independent, so $\mathbb E\|\tau\mathrm{Sym}(A)\|_F^2=\tau^2D$.

Step 5, information. $I(R;Y)\le\mathbb E_R\mathrm{KL}(\mathcal N(0,R^{-2})^{\otimes N}\|\mathcal N(0,I)^{\otimes N})$.
Per eigenvalue $r$ of $R$, the KL is $f(r)=\frac12(r^{-2}-1+2\ln r)$, with $f(1)=f'(1)=0$ and
$f''\le3r^{-4}\le10$ on $[\frac34,\frac54]$, so $f(r)\le5(r-1)^2$. Hence
$I(R;Y)\le5N\,\mathbb E\|R-I\|_F^2\le5N\tau^2D/\Pr[\mathcal C]\le D/4$.

Step 6, small balls. The conditioned prior density of the $D$ coordinates is at most
$2(\pi\tau^2)^{-D/2}$, and a Frobenius ball of radius $t$ lies in the coordinate ball of radius $t$.
So $\kappa_t=\sup_{R_0}\Pr[\|R-R_0\|_F\le t]\le2(t^2/\tau^2)^{D/2}/\Gamma(\frac D2+1)\le2(2et^2/(D\tau^2))^{D/2}$,
using $\Gamma(x+1)\ge(x/e)^x$. With $t^2=D\tau^2/(2e^3)$, $\kappa_t\le2e^{-D}$.

Step 7, Fano. The ceiling of `prop-reconstruction-label-sandwich`, with a single label, the Polish
space of symmetric matrices with the Frobenius metric, $Z=Y$ and $\eta=t$, gives for every
estimator $\Pr[\|\hat R-R\|_F\le t]\le(I(R;Y)+\ln2)/\ln(1/\kappa_t)\le(D/4+\ln2)/(D-\ln2)\le0.32$
for $D\ge15$, that is $d\ge5$. By Step 3, $\mathcal E_N\le\frac4{25}t^2$ on $\mathcal G$ forces
$\|\hat R-R\|_F\le t$. So $\Pr[\mathcal E_N\le\frac4{25}t^2]\le0.32+2e^{-4}<\frac12$ under the prior,
and some $R$ in its support does as well. Finally
$\frac4{25}t^2=\frac{D}{500e^3N}\ge\frac{d^2}{1000e^3N}$. $\square$

Status. Sketch until a round accepts it. No gap is known to the builder.

Regime. Statistical. The lower bound holds for unbounded servers and the upper bound is attained
by an efficient one, so the price is the same in both regimes.

Experiment. Draw $R$ from the prior, run empirical whitening and any Bayes-motivated competitor,
and plot $\mathcal E_N$ against $d^2/N$ for $d\in\{16,32,64\}$ and $N/d\in\{2,8,32\}$.

The other regime. Against the trainer, who holds the records, the attacker's price for the
rotation class of the records is $\Theta(d/\epsilon^2)$ representations, and nothing buys the
rotation itself (`thm-blind-orbit-limit`).

### thm-train-access-price-frontier: Train calls replace population samples in the membership price of noisy mean estimation

status: sketch

uses: fact-hsu-membership-sample-gap, fact-hsu-gap-prices-covariance, fact-subgaussian-sample-covariance-concentration, def-uniform-security-profile

Setting and parts (a) to (c) as in `round-03/builder.md`. The final paragraph's sentence on a
mechanism with input-estimated covariance is withdrawn.

(d) The frontier, revised. Fix $a\in(0,\frac12)$, let $\rho=n^{-a}$ and $d=\kappa d^\star$ with
$\kappa>\max\{c_1,c\}$, $\kappa\ge\max\{c_3,2100\}$, and let $n\to\infty$. Then:

1. With no Train call, $\Theta_\kappa(n^{2-2a})$ reference samples are necessary and sufficient
   (HSU25 Theorems 3.1 and 3.3).
2. With Train access, $\Theta_\kappa(n^{2a})$ reference samples are necessary and sufficient, the
   sufficient attack using $O_\kappa(n^{2-2a})$ Train calls.
3. In combined units, samples plus Train calls, $\Theta_\kappa(n^{2-2a})$ is necessary and
   sufficient.

Proof of (d). Here $d^\star=n+n^{2-2a}$, $d^\star\asymp n^{2-2a}$ and $\min\{n,1/\rho^2\}=n^{2a}$.
For the necessity in 2, an attack with $m<2$ samples is padded with unused samples to $m=2$. By (b) no
attack with $2\le m$ and $n^2/m>(\kappa/c-1)d^\star$ succeeds, and the right side is
$(c/(\kappa-c)+o(1))n^{2a}$, which exceeds $2$ for $n$ large, while $n\ge4$. Sufficiency is (c). For 1
and 3, (a) applies since $d>c_1d^\star$, Theorem 3.3 applies since $\rho<1$ and $d\ge c_3d^\star$, and
(c) gives the combined upper bound. $\square$

Remark. For constant $\rho$ and $d\gtrsim n^2$, the round-03 discussant's attack needs no reference
sample (`round-03/discussant-sol.md`), so outside the regime of (d) the sample price can vanish.
The builder has not re-derived its inverse-Wishart moments.

## Objects carried from round 03 with ACCEPT

### fact-subgaussian-sample-covariance-concentration: the sample covariance of sub-gaussian rows concentrates in operator norm

status: borrowed

uses: none

Unchanged.

### thm-blind-orbit-limit: an unbounded seed-blind server learns the records only up to the symmetry of the record law

status: sketch

uses: def-seed-blind-reconstruction-game, lem-equivariant-view-coupling

Unchanged. Part (c) needs side data invariant under all of $O(d)$, as item 5 of the protocol class
with $H=O(d)$ requires.

### prop-relu-client-second-moment-identifies-weights: a frozen Gaussian ReLU client is identified up to rotation by its second moment

status: sketch

uses: thm-blind-orbit-limit, fact-lei-random-expansive-layers-invertible

Unchanged except two lines. The derivative is $\kappa'(\theta)=-(\pi-\theta)\sin\theta/(2\pi)$. The
kernel is the first-order arc-cosine kernel of Cho and Saul (NeurIPS 2009), at half their
normalization. For non-Gaussian isotropic laws an approximate kernel identity needs a hypothesis on
the law.

### thm-same-units-gap-gaussian-mechanism: in noisy mean estimation the attacker pays a factor one plus n rho squared over the trainer

status: sketch

uses: thm-train-access-price-frontier, fact-hsu-membership-sample-gap

Unchanged, with the meter stated. A reference sample and a Train call cost one unit each, the
trainer's calibration to the population covariance is free, and the trainer's error is Mahalanobis
risk. The separation in reference samples alone is HSU25's (Theorems 3.1 and 3.3, Remark 3.4), and
this theorem adds Train access and the combined meter.
