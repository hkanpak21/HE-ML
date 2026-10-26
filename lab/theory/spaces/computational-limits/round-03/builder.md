# Round 03, builder: computational limits, the aims of milestone 2

Space `computational-limits`, round 03, 2026-10-25, the aims round of the
milestone "mappings to known hard problems" (`lab/theory/milestone.json`, rounds
03 to 05). Builder: the Claude session space-computational. No challenge is
open: round 02 ended with BLOCKING 0, and its objects are merged in chapter 5 of
`lib/theory/booklet.pdf`. Halil's decisions of 2026-10-25 (`CONTEXT.md`) set this
round's direction: hardness from a data law counts, mappings onto hard problems
of the literature are wanted, the attacker class is the two games of
`def-seed-blind-reconstruction-game` never mixed, and beautiful mathematics comes
first.

Reads of this round. From the library: ZSWB22 (Model 3.2, Assumption 3.1,
Algorithm 1, Theorem 3.3, Claim 2.7, Model 4.3, Corollary 4.4). From the web,
PDFs not placed: DvW22 (Ducas and van Woerden, EUROCRYPT 2022, the CWI copy,
Sections 2 and 3 to Lemma 3.13), Duc24 (Ducas, Designs, Codes and Cryptography
2024, the open-access copy, Section 1 and Theorems 1 and 2), DK22 (Diakonikolas
and Kane, COLT 2022, arXiv 2112.09104v1, Sections 1 and 2 in full), WDS19 (Wu,
Dimakis and Sanghavi, NeurIPS 2019, arXiv 1909.01812, from its HTML page:
Definition 1, Theorem 1, Claim 1, Section 4, paraphrased by the fetch tool). The
search gate found no row on lattice isomorphism, rectified Gaussian learning or
lattice-based NGCA. Four searches were run, their rows are in `summary.md`. The
copy of Bennett, Ganju, Peetathawatchai and Stephens-Davidowitz (EUROCRYPT 2023)
could not be fetched, and it is cited only through Duc24's account of it.

Normalizations. For pancakes this round follows each paper's own convention and
says which. Records of the ZLIP aim use $\rho_s(x)=e^{-\pi\|x\|^2/s^2}$ and the
discrete Gaussian $D_{\mathbb Z^d,s}$ of DvW22. ZSWB22's discrete Gaussian $\nu$ of
"width 1" on $(1/\gamma)\mathbb Z$ has mass proportional to $e^{-x^2/2}$.

## Literature

### fact-lip-average-case: the lattice isomorphism problem in quadratic-form language
status: borrowed
uses: none

Ducas and van Woerden, EUROCRYPT 2022, key DvW22. Definition 2.1: LIP asks, for
isomorphic lattices $L,L'\subset\mathbb R^n$, for $O\in O_n(\mathbb R)$ with $L'=OL$,
and for bases $B,B'$ for $O$ and $U\in GL_n(\mathbb Z)$ with $B'=OBU$. Definition
2.2: wc-sLIP$^Q$ asks, given $Q'\in[Q]$, for $U\in GL_n(\mathbb Z)$ with
$Q'=U^\top QU$, and the solutions are $\{VU:V\in\mathrm{Aut}(Q)\}$ with
$\mathrm{Aut}(Q)$ finite. Lemma 2.9: for $s\ge\|B_Q^*\|\sqrt{\ln(2n+4)/\pi}$, exact
samples of $D_{Q,s,c}$ in polynomial time. Definition 3.3: the Gaussian form
distribution $D_s([Q])$ draws $m=\lceil2n/C\rceil$ vectors from $D_{Q,s}$,
$C=1-(1+e^{-\pi})^{-1}$, until they span, and returns the form $R=U^\top QU$ of
$\mathrm{Extract}(Q,Y)$, built from the Hermite normal form of $Y$ (Lemmas 3.1 and
3.2, so $R$ depends only on the class). Lemma 3.4: for
$s\ge\max\{\lambda_n(Q),\|B_Q^*\|\sqrt{\ln(2n+4)/\pi}\}$, Algorithm 1 returns $(R,U)$
in expected polynomial time with $R\sim D_s([Q])$ and $U$ uniform over the
isomorphisms from $Q$ to $R$. Lemma 3.6: for $s\ge\max\{\lambda_n(Q),\eta_\epsilon(Q)\}$,
$\Pr_{Q'\sim D_s([Q])}[\|B^*_{Q'}\|>s\sqrt n]\le\frac{1+\epsilon}{1-\epsilon}100n2^{-n}$.
Definition 3.7: ac-sLIP$^Q_s$ asks, given $Q'\sim D_s([Q])$, for $U$ with
$Q'=U^\top QU$. Lemma 3.9: an ac-sLIP$^Q_s$ oracle for $s\ge2^{\Theta(n)}\lambda_n(Q)$
solves wc-sLIP$^Q$ with the same success and polynomial overhead. Lemma 3.10: for
$s\ge\lambda_n(Q)$, at the additive cost of an SIVP oracle with factor
$s/(\lambda_n(Q)\sqrt{\ln(2n+4)/\pi})$.

Other regime. LIP is an algebraic search problem with no statistical gap: the
form determines the lattice up to isometry, and the hardness is computational.

### fact-zlip-best-algorithms: the price of rotations of $\mathbb Z^n$
status: borrowed
uses: fact-lip-average-case

Ducas, Provable lattice reduction of $\mathbb Z^n$ with blocksize $n/2$, Designs,
Codes and Cryptography 2024, key Duc24. ZLIP is LIP for $Q=I_n$. Theorems 1 and
2: a specialization of the slide reduction algorithm outputs an orthogonal basis
of a lattice isometric to $\mathbb Z^n$ after $O(n^2\log\max_i\|b_i\|)$ iterations,
each using an SVP oracle in dimension at most $n/2+1$. Section 1 records, citing
Bennett, Ganju, Peetathawatchai and Stephens-Davidowitz (EUROCRYPT 2023), a
provable $2^{n/2+o(n)}$ algorithm through a constant-factor Gap-SVP reduction, and,
citing Ducas, Postlethwaite, Pulles and van Woerden (ASIACRYPT 2022), a heuristic
cost of $2^{0.146n+o(n)}$ for BKZ with blocksize $n/2+o(n)$. No polynomial-time
algorithm is known (Duc24, Section 1.1, recorded from that account).

Other regime. Computational only.

### fact-lll-recovers-discrete-hidden-labels: LLL reads integer labels off a Gaussian background
status: borrowed
uses: none

Zadik, Song, Wein and Bruna, COLT 2022, key ZSWB22. Assumption 3.1: $\Sigma\succeq0$
is $u$-weakly separable if $\Sigma u=0$ and its other eigenvalues lie in
$[d^{-C},d^C]$. Model 3.2: for a known spacing $a\in[d^{-c},d^c]$, integers
$x_i\in[-2^d,2^d]$, a unit $u$ and a $u$-weakly separable $\Sigma$, the samples are
$z_i\sim N(ax_iu,\Sigma)$. Theorem 3.3: Algorithm 1 on $n=d+1$ samples returns, with
probability $1-e^{-\Omega(d)}$ and in polynomial time, $\epsilon\in\{\pm1\}$ with
$\hat x_i=\epsilon x_i$ for all $i$ and $\hat u=\epsilon u$. Algorithm 1 forms the
coefficients $\lambda$ of the linear dependency $\sum_i\lambda_iz_i=0$, runs LLL on
a lattice built from the truncations of $\lambda$ alone, and only then solves a
linear system for $u$. Model 4.3 is homogeneous CLWE without noise, labels from
the discrete Gaussian $\nu$ of width 1 on $(1/\gamma)\mathbb Z$, and Corollary 4.4
solves it in polynomial time with $d+1$ samples for $\gamma=\mathrm{poly}(d)$.

Other regime. The SQ and low-degree lower bounds for these laws stay formally
true. The paper states that inverse-polynomial noise breaks the method.

### fact-ngca-lattice-basis-reduction: NGCA is easy for discrete hidden laws
status: borrowed
uses: none

Diakonikolas and Kane, COLT 2022, key DK22. Definition 1.1: $P^A_v$ has
projection $A$ on $v$ and a standard Gaussian on $v^\perp$. Assumption 1.2: every
sample of $A$ is within $\epsilon$ of some $\sum_{j\le k}n_jr_j$ with $|r_j|=O(1)$,
$n_j\in\mathbb Z$, $|n_j|\le B$, together with $\Pr[|X|>1/d]>1/d$ and
$\Pr[|X|>\mathrm{poly}(d)]<1/d$. Every law of support size at most $k$ satisfies it
with $\epsilon=0$. Theorem 1.3: for $\epsilon<2^{-\Omega(dk^2)}B^{-\Omega(k)}$, an
algorithm with $m=2d$ samples and time $\mathrm{poly}(d,k,\log B)$ outputs $v^*$ within
$\ell_2$ error $N^{-1}2^{O(m^2k^2/(m-d))}B^{O(mk/(m-d))}$ of $\pm v$ with constant
probability. Its steps 3 to 9 use the samples only through the right kernel $V$ of
the sample matrix (Section 2), and step 10 is a least-squares regression. Remark
2.2: any $m>d$ works with a stronger condition on $\epsilon$.

Other regime. The SQ lower bound of DKRS23 covers discrete $A$ and stays true.

### fact-rectified-gaussian-gram-estimation: a ReLU layer on Gaussian inputs gives up its Gram matrix
status: borrowed
uses: none

Wu, Dimakis and Sanghavi, NeurIPS 2019, key WDS19, read from the arXiv HTML
page with the formulas paraphrased. Definition 1: $x=\mathrm{ReLU}(Wz+b)$ with
$z\sim N(0,I_k)$. Claim 1: $W$ is identifiable only through $WW^\top$. Theorem 1:
for $b\ge0$, Algorithm 1 with $\tilde O(\varepsilon^{-2}\ln(d/\delta))$ samples returns
$\hat\Sigma,\hat b$ with $\|\hat\Sigma-WW^\top\|_F\le\varepsilon\|W\|_F^2$ and
$\|\hat b-b\|_2\le\varepsilon\|W\|_F$. The row norms come from truncated univariate
Gaussian estimation on the samples with $x_i>0$, and the angles from the orthant
identity $\Pr[x_i>b_i,x_j>b_j]=(\pi-\theta_{ij})/(2\pi)$ (Fact 1, Lemma 2).

Other regime. The orthant identity holds for every spherically symmetric input
law, since the event depends only on the direction of $z$. It fails for laws with
a hidden non-Gaussian direction, the case aim 1 needs.

## Gaps left by milestone 1, and the new facts

1. The upper inclusion of `conj-seed-price-is-ngca-price` is proven only for
   frozen linear clients (`prob-blind-inversion-relu-clients`).
2. Every hard record law so far is a pancake law with inverse-polynomial noise.
   The literature now supplies two further families. Exactly discrete hidden
   coordinates are easy for lattice reduction (DK22, ZSWB22). A record that is
   discrete in every coordinate, for instance a quantized Gaussian, is a point of
   $\mathbb Z^d$, and a hidden rotation of it is an instance of ZLIP (DvW22,
   Duc24).
3. Coarse reconstruction of pancake records in polynomial time
   (`prob-coarse-reconstruction-lattice-hardness`) is open.
4. Trained clients beyond the records seen under $W_0$: the lower bounds of the
   first milestone already cover them through `lem-equivariant-view-coupling`,
   and the seed-known side is open. This aim is deferred.

## Aims

### conj-quantized-records-zlip-equivalence: a hidden rotation of quantized Gaussian records is a ZLIP secret
status: sketch
uses: lem-equivariant-view-coupling, fact-lip-average-case, fact-zlip-best-algorithms

Setting. Records $x_1,\dots,x_N$ i.i.d. from $D_{\mathbb Z^d,s}$, the discrete
Gaussian on $\mathbb Z^d$, a product of $d$ copies of $D_{\mathbb Z,s}$ with covariance
$\sigma_s^2I$, $\sigma_s^2=\mathrm{Var}(D_{\mathbb Z,s})$. Protocols of $\mathcal P_{O(d)}$
with no side data. Target $g(x)=x$, success up to $K=\mathrm{Aut}(I_d)$, the signed
permutation matrices. Exact success: some $P\in K$ has $t_i=Px_i$ for every $i$.

(a) Lower bound, any client of $\mathcal P_{O(d)}$, frozen or trained. Let
$s_0\ge\max\{1,\eta_\epsilon(\mathbb Z^d)\}$ and $s=s_0\sqrt{d\ln(2d+4)/\pi}$. A
seed-blind attacker of time $T$ with exact success probability $p$ on
$N\ge\lceil2d/C\rceil$ records gives an algorithm for ac-sLIP$^{I_d}_{s_0}$ of time
$T+T_{\rm run}+\mathrm{poly}(d,\log s)$ and success $p-O(d2^{-d})$.

(b) Upper bound, frozen injective linear client, exact arithmetic. If the records
generate $\mathbb Z^d$, a seed-blind server with $N=\mathrm{poly}(d,s)$ records and an
oracle for ac-sLIP$^{I_d}_s$ achieves exact success with the oracle's success
probability, up to $o(1)$, at polynomial overhead.

So for frozen linear clients the seed is worth exactly an average-case ZLIP
instance, and for every client at least one. By `fact-zlip-best-algorithms` the
best known blind attack costs $2^{0.146d+o(d)}$ heuristically and $2^{d/2+o(d)}$
provably, against one linear solve per record for the seed-known server.

Sketch of (a). Given $Q'\sim D_{s_0}([I])$, write $Q'=U^\top U$ with $U$ unknown.
With probability $1-O(d2^{-d})$, $\|B^*_{Q'}\|\le s_0\sqrt d$ (Lemma 3.6), so
Lemma 2.9 samples $c_1,\dots,c_N\sim D_{Q',s}$. Let $B'$ be the Cholesky factor of
$Q'$ and $O=B'U^{-1}$, which is orthogonal. The vectors $x_i=Uc_i\in\mathbb Z^d$ have
mass proportional to $\rho_s(B'c_i)=\rho_s(Ox_i)=\rho_s(x_i)$, so they are i.i.d.
$D_{\mathbb Z^d,s}$, and the reducer holds $y_i=B'c_i=Ox_i$. It runs the protocol from
fresh coins on the $y_i$. By `lem-equivariant-view-coupling` with the fixed
rotation $O$ (conditional on $Q'$), the view and the records have the law of the
real game, so with probability $p$ the attacker returns $t_i=PUc_i$ for every $i$.
For $d$ indices with $C_d=[c_{i_1}\cdots c_{i_d}]$ invertible,
$U'=T_dC_d^{-1}=PU$ is unimodular and $U'^\top U'=U^\top P^\top PU=Q'$. The reducer
checks this equation, so a wrong output is never returned.

Sketch of (b). The server finds $d$ independent representations $Z_d=WX_d$,
writes every $z_j=Z_d\alpha_j$ with $\alpha_j=X_d^{-1}x_j$ rational, takes a basis
$B=WU$ of the lattice the $z_j$ generate ($=W\mathbb Z^d$ if the records generate
$\mathbb Z^d$) by a Hermite normal form over the $\alpha_j$, and reads integer
coordinates $k_j$ with $z_j=Bk_j$, $x_j=Uk_j$. The form $Q_B=U^\top U$ is integral
and equals $\sigma_s^2(E[kk^\top])^{-1}$, so the empirical second moment of the
$k_j$, rounded, gives it exactly once its error is below $1/2$, which polynomially
many records achieve. The $k_j$ are i.i.d. $D_{Q_B,s}$, so $\mathrm{Extract}(Q_B,Y)$ on
a block of them is a sample $R\sim D_s([I])$ with a known $U_E$, $R=U_E^\top Q_BU_E$.
The oracle returns $U_R$ with $R=U_R^\top U_R$, and $U'=U_RU_E^{-1}$ satisfies
$U'^\top U'=Q_B$, so $U'U^{-1}$ is an integral orthogonal matrix, a signed
permutation $P$, and $t_j=U'k_j=Px_j$.

What would settle it. A proof of (a) with the sampling and full-rank events, a
proof of (b) with a lemma that $O(d\log d)$ samples of $D_{\mathbb Z^d,s}$ above
smoothing generate $\mathbb Z^d$ with high probability (or a version of (b) for the
generated sublattice), and the precision needed for the rational coordinates. A
refutation: a polynomial-time blind attack that does not solve ZLIP.

Regime. Polynomial time, conditional on the hardness of ac-sLIP$^{I}_{s_0}$, which
DvW22 propose as an assumption. The SQ game for these records is not addressed.
Statistically the records are determined up to $K$ by the view (exact
reconstruction is possible for an unbounded server with a frozen linear client).

Experiment. Quantize Gaussian records to integers, pass them through a Gaussian
linear layer, and run the published ZLIP and BKZ attacks of Duc24's references in
dimensions 20 to 60, measuring time against $d$ next to the seed-known linear
solve. The record law is natural: images are quantized, though not Gaussian.

Without the oracle. No learning oracle. The reduction costs one training run.

### conj-sq-sample-games-separate: the two games separate on noiseless pancakes
status: sketch
uses: fact-lll-recovers-discrete-hidden-labels, fact-ngca-sq-lower-bound, lem-equivariant-view-coupling, prop-sq-blind-reconstruction-bound

Setting. Records from ZSWB22 Model 4.3 with $\gamma=\mathrm{poly}(d)$, $\gamma\ge2\sqrt d$: label
$\ell_i\sim\nu$ on $(1/\gamma)\mathbb Z$, record $x_i\sim N(\ell_iv,I-vv^\top)$, which is
$P^\nu_v$. A frozen client $z=Wx$ with $W$ of full column rank. Target
$g(x)=\langle v,x\rangle=\ell$, $K=\{\pm1\}$.

(a) Sample game. A polynomial-time seed-blind server recovers every label exactly
up to one global sign from $d+1$ representations, with probability $1-e^{-\Omega(d)}$.

(b) SQ game. Every SQ attacker that reaches fine success, $\|R(z)-\kappa\ell\|_{L^2}\le c/\gamma$,
needs $2^{d^{\Omega(1)}}$ queries or a tolerance $d^{-\omega(1)}$.

Sketch. (a) The coefficients $\lambda$ of a linear dependency among $d+1$ samples
are the same for $z_i=Wx_i$ as for $x_i$, because $W$ is injective. ZSWB22's
Algorithm 1 computes its LLL lattice from $\lambda$ alone, so on representations it
computes the same integer vector $t_1$ as on the records, and Theorem 3.3 gives
$t_1=c\ell$ for an integer $c$, so the labels follow from $t_1$ up to sign and a
scale that the known spacing $1/\gamma$ fixes (dividing by the gcd, or by the known
second moment). Model 4.3 is an instance of Model 3.2 by ZSWB22 Claim 4.5. (b)
$\nu$ matches the moments of $N(0,1)$ of every fixed degree $k$ up to
$e^{-\Omega(\gamma^2)}$ by Poisson summation, so DKRS23 Theorem 1.5 holds for every
fixed $k$ with negligible slack. A fine reconstruction map gives $\hat s$ with
$\|\hat s\mp v\|=O(1/\gamma)$ by $d$ truncated queries of tolerance
$\tilde O(1/(\gamma\sqrt d))$, and a single query of
$\cos(2\pi\gamma\langle\hat s,u\rangle)$ then separates $P^\nu_v$ from $\gamma_d$: under the
null its mean is exponentially small for every fixed $\hat s$, under the planted
law it is a constant. This test is robust to an adversarial oracle, because its
null value does not depend on how $\hat s$ was chosen. DKRS23 applied with $k$ large
then bounds the tolerance by $d^{-((1-\lambda)/4-c)k}$ for every fixed $k$.

What would settle it. The two proofs, with the scale step of (a) and the
constants of (b). A refutation of (a) would be a failure of the kernel invariance,
which does not happen for injective linear clients.

Regime. Both games, on one protocol and one record law. With inverse-polynomial
noise on the labels (hCLWE) both games are hard (`thm-blind-split-seed-separation`),
without noise the sample game is easy and the SQ game is not. The SQ price
therefore overstates the seed's worth on exactly discrete data, which is why the
two games are never mixed.

Experiment. Records with integer hidden labels and a Gaussian background through a
Gaussian linear layer. Run ZSWB22's Algorithm 1 on the representations and compare
with moment and ICA attacks, which fail.

Without the oracle. No oracle.

### conj-coarse-reconstruction-lattice-hard: constant-correlation blind reconstruction of pancakes is lattice-hard
status: sketch
uses: lem-equivariant-view-coupling, fact-clwe-hardness, prop-fine-reconstruction-to-hclwe

Statement. Let a protocol of $\mathcal P_{O(d)}$ run on records from $H_{v,\beta,\gamma}$
with $\beta\in(0,1)$, $\gamma\ge2\sqrt d$, $\gamma/\beta$ polynomial (BRST21 normalization),
without side data. If a polynomial-time seed-blind attacker outputs $t_{1:N}$ whose
empirical correlation with $\langle v,x_i\rangle$ is at least $c_0$ in absolute value
with probability $p$, for a constant $c_0>0$, then hCLWE$_{\beta,\gamma}$ has a
polynomial-time algorithm of advantage $p^2-e^{-\Omega(c_0^4d)}$.

Sketch, the agreement test. The reducer splits its hCLWE samples into two
independent halves $S_1,S_2$, draws independent Haar rotations $Q_1,Q_2$ and fresh
protocol coins, runs the protocol and the attacker on $Q_jS_j$, forms
$\hat w_j=U_j^\top t^{(j)}$ from that run's samples $U_j$ and outputs $t^{(j)}$, and
sets $O_j=Q_j^\top\hat w_j/\|\hat w_j\|$. It answers "planted" iff
$|\langle O_1,O_2\rangle|\ge c_0^2/8$. Under $D_0$, $Q_jS_j$ has the law of $S_j$ and is
independent of $Q_j$, so $O_1,O_2$ are independent uniform unit vectors and
$|\langle O_1,O_2\rangle|<c_0^2/8$ except with probability $2e^{-dc_0^4/128}$. Under
$H_w$, the input of run $j$ is a sample of $H_{Q_jw}$ with $Q_jw$ uniform, so with
probability $p$ the empirical correlation is at least $c_0$, and then
$|\langle O_j,w\rangle|\ge c_0/2$ by the covariance of `fact-clwe-hardness` and the
concentration of $U_j$ (the $w$-component of $\hat w_j$ is at least
$c_0\|t\|\|a\|$, the rest at most $\|t\|\,\|U_{j,\perp}\|$). The law of $O_j$ is
invariant under the rotations fixing $w$, so its component in $w^\perp$ is uniform
and independent of the other run's, and
$|\langle O_1,O_2\rangle|\ge c_0^2/4-O(\sqrt{\log d/d})$ when both runs succeed.
The advantage is at least $p^2-e^{-\Omega(c_0^4d)}$, and BRST21 Corollary 4.2
makes $p$ negligible unless the lattice problems are quantum-easy.

The same test gives a general lemma, which round 04 will state: in the sample game,
for any family of record laws closed under rotation with a rotation-invariant
null, constant-correlation recovery of the hidden direction yields detection with
advantage $p^2-e^{-\Omega(c_0^4d)}$. It needs no witness of non-Gaussianity. In the SQ
game it is not valid as it stands, because an adversarial oracle may correlate
the two runs under the null.

What would settle it. The proof with the constants. A refutation would need a
polynomial-time weak reconstructor of pancakes, which would break hCLWE.

Regime. Polynomial time, lattice-conditional. It closes
`prob-coarse-reconstruction-lattice-hardness` if proven.

Experiment. None beyond `prop-fine-reconstruction-to-hclwe`: the statement is a
reduction.

Without the oracle. No oracle.

### conj-blind-relu-client-inversion: a seed-blind server inverts an expansive ReLU client up to rotation
status: open
uses: fact-rectified-gaussian-gram-estimation, lem-whitening-gives-rotated-records, conj-seed-price-is-ngca-price

Statement. Let the client be frozen, $z=\mathrm{ReLU}(Wx)$, $W$ with i.i.d. Gaussian
entries, $m=c_0'd$, $c_0'\ge2.1$, and the records i.i.d. from an isotropic
$P^A_V$ with $A$ sub-Gaussian and $r=O(1)$. There is a polynomial-time seed-blind
algorithm that, from $\mathrm{poly}(d,1/\varepsilon)$ representations, outputs a map
$\hat T$ with $\hat T(z_i)=\hat Rx_i$ and $\|\hat R-R\|\le\varepsilon$ for an orthogonal
$R$ that is Haar and independent of the records.

Route. For Gaussian records WDS19 recovers $WW^\top$ through the orthant
identity, which holds exactly for spherically symmetric laws. For $P^A_V$ the
two-dimensional projections of the record on pairs of rows of $W$ carry the
hidden law only through $(\langle w_i,V\rangle,\langle w_j,V\rangle)$, of size
$O(\sqrt{r/d})$, so the orthant identity holds up to an error of order $1/d$ per
pair (heuristic). The obstruction is that entrywise errors of order $1/d$ over an
$m\times m$ Gram matrix need not be small in operator norm unless their structure
is controlled. With $\hat G$, the server inverts each representation on its
positive coordinates (LJDD19's linear system inside $\mathrm{range}(\hat G)$) and
whitens. The NGCA step must then tolerate a residual linear distortion of norm
$\varepsilon$.

What would settle it. A bound on the structured error of the orthant estimates,
or an exact identity for the Gram matrix from the law of $\mathrm{ReLU}(Wx)$ for
isotropic records, followed by a robustness statement for NGCA under
$\varepsilon$-distortion. A refutation would be a recoverable expansive client for
which learning $W$ up to rotation from representations is itself hard, for
instance hard under the generative-model lower bounds of Chen, Li, Li and Meka
(NeurIPS 2022), which the space has not read.

Regime. Computational. Statistically $WW^\top$ is identifiable for isotropic
records with a density (heuristic).

Experiment. Estimate $WW^\top$ from ReLU representations of NGCA records with the
orthant estimator, measure the operator-norm error against $d$, then run NGCA on
the whitened estimates.

Without the oracle. No oracle.

## Plan for rounds 04 and 05

Round 04 proves the three sketched aims as `thm-` and `lem-` objects: the
agreement lemma, the coarse-reconstruction theorem, the games separation, and
both directions of the ZLIP equivalence with a generation lemma for discrete
Gaussian records. Aim 1 is attempted in round 04 or 05, as a proof for a
restricted record family or as a precise obstruction.
