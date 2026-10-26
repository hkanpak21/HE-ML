# Round 04, builder: computational limits, the proofs of milestone 2

Space `computational-limits`, round 04, 2026-10-25. Builder: the Claude session
space-computational. Discussant of round 03: sol. Halil's instruction of tonight,
"proceed the development and simplify whenever possible", sets the form: six
objects, four of them new, and the rest withdrawn. Added read: Haviv and Regev,
On the Lattice Isomorphism Problem, SODA 2014, arXiv 1311.0366 (Section 5.1,
Lemmas 5.1 and 5.4), on sol's pointer.

Computation model for the lattice statements: the real RAM, exact arithmetic on
client weights and representations. A finite-precision version is open.

## Responses to round 03

`ch-zlip-width-equivalence` (blocking). Accepted. `thm-zlip-reductions` states two
reductions with the width loss $\sqrt{d\ln(2d+4)/\pi}$ and no equivalence.
`ch-zlip-arithmetic-cost` (blocking). Accepted: widths are polynomial in $d$, the
model is the real RAM, and all costs are $\mathrm{poly}(d)$.
`ch-zlip-fresh-coordinate-samples` (blocking). Accepted: three independent blocks,
one for the basis, one for the form, fresh blocks for Extract, and the rounding is
quantified.
`ch-zlip-generation-prior-art` (not blocking). Accepted: Haviv and Regev Lemma 5.4,
`fact-discrete-gaussian-samples-generate`.
`ch-zlip-certificate-check` (not blocking). Accepted: the reducer checks
integrality, unimodularity and the Gram identity.
`ch-zswb-label-hypotheses` (blocking). Accepted: the revised fact conditions on a
nonzero label among the last $d$ and states rational proportionality.
`ch-hidden-label-scale` (blocking). Accepted: a primitive-label lemma inside
`prop-blind-lll-label-recovery` fixes the scale by the gcd.
`ch-games-hidden-client` (blocking). Accepted: the SQ clause names the hidden
right-rotation-invariant client.
`ch-sq-fine-output-range` (blocking). Accepted. The SQ side is now a detection
task, which the bounded interface handles, and it separates the games on one task.
`ch-coarse-sample-budget` (blocking). Accepted: the correlation is uncentred,
outputs are nonzero, and each run has $N\ge Cd\log^2(\gamma/\beta)$ records.
`ch-sq-agreement-oracle` (not blocking). Accepted: the agreement lemma is stated for
the sample game only, and nothing is claimed about SQ recovery-to-testing in general.
`ch-dk-assumption-scope` (blocking), `ch-kernel-finite-precision` (not blocking):
`fact-ngca-lattice-basis-reduction` is withdrawn. ZSWB22 covers the law used here,
and DK22 is not needed. The correction (finite support gives only the arithmetic
condition of Assumption 1.2) goes to the registers.
`ch-spherical-origin-mass` (blocking), `ch-relu-output-guarantee` (blocking),
`ch-relu-estimator-bias`, `ch-generative-hardness-reference` (not blocking):
`conj-blind-relu-client-inversion` and `fact-rectified-gaussian-gram-estimation`
are withdrawn from this milestone. Sol's approximate-inversion formulation goes to
the registers as the statement of `prob-blind-inversion-relu-clients`, with the
corrected reference (Chen, Li and Li, NeurIPS 2022, Theorem 3.1, not read).
The three remaining aims of round 03 are superseded by the objects below.

## Objects

### fact-lll-recovers-discrete-hidden-labels: LLL reads integer labels off a Gaussian background
status: borrowed, revised
uses: none

ZSWB22, Model 3.2 and Algorithm 1 as in round 03. Theorem 3.3 with Lemma 3.4,
stated for the case used here: if some label among $x_2,\dots,x_{d+1}$ is nonzero,
then with probability $1-e^{-\Omega(d)}$ over the Gaussian parts, LLL returns an
integer vector $t_1$ rationally proportional to $(x_1,\dots,x_{d+1})$, in polynomial
time. If all of $x_2,\dots,x_{d+1}$ vanish, $[z_2\cdots z_{d+1}]$ is singular and the
algorithm fails (sol's counterexample, which also affects the paper's Lemma 6.3).
Model 4.3 and Corollary 4.4 as in round 03.

Other regime. As in round 03.

### fact-discrete-gaussian-samples-generate: polynomially many discrete Gaussian samples generate the lattice
status: borrowed
uses: none

Haviv and Regev, SODA 2014, key HR14. Lemma 5.4: for a lattice $L$ of rank $n$ with
$\det(L)\ge1$ and $s\ge bl(L)$ (the length of a shortest basis), a set of
$n^2+n\log(s\sqrt n)(n+20\log\log(s\sqrt n))$ independent samples of $D_{L,s}$ fails to
generate $L$ with probability $2^{-\Omega(n)}$. For $\mathbb Z^n$, $bl=1$.

Other regime. A probabilistic lattice fact, no complexity assumption.

### lem-agreement-detection: weak recovery of a hidden direction gives detection
status: proven
uses: none

Statement. Let $\{P_w\}_{w\in S^{d-1}}$ be laws on $\mathbb R^d$ with $Q_\#P_w=P_{Qw}$ for
$Q\in O(d)$, and $P_0$ a rotation-invariant law. Let an algorithm $\mathcal A$ map $N$
samples to $o\in\mathbb R^d\setminus\{0\}$ with $|\langle o,w\rangle|\ge\rho\|o\|$, with probability
at least $p$ for every $w$. The tester draws two independent blocks of $N$ samples,
independent Haar $Q_1,Q_2$, sets $\hat o_j=Q_j^\top\mathcal A(Q_jS_j)/\|\mathcal A(Q_jS_j)\|$,
and outputs $1$ iff $|\langle\hat o_1,\hat o_2\rangle|\ge\rho^2/2$. Then
$\Pr_{P_0}[1]\le2e^{-d\rho^4/8}$ and $\Pr_{P_w}[1]\ge p^2-2e^{-(d-1)\rho^4/8}$.

Proof. Null: $P_0$ is rotation-invariant, so $Q_jS_j$ has the law of $S_j$ and is
independent of $Q_j$. Hence $\hat o_j$ is $Q_j^\top$ applied to a unit vector
independent of $Q_j$, a uniform unit vector, and $\hat o_1,\hat o_2$ are independent.
For independent uniform unit vectors, $\Pr[|\langle\hat o_1,\hat o_2\rangle|\ge t]\le2e^{-dt^2/2}$.
Planted: $Q_jS_j$ is a block from $P_{Q_jw}$, so with probability at least $p$,
$|\langle\hat o_j,w\rangle|\ge\rho$. Write $\hat o_j=\kappa_jw+\sqrt{1-\kappa_j^2}\,e_j$ with
$e_j\perp w$. For $P$ fixing $w$, $(Q_jP^{-1},PS_j)$ has the law of $(Q_j,S_j)$, since
$P_\#P_w=P_w$, and produces the output $P\hat o_j$. So the law of $\hat o_j$ is invariant
under the stabilizer of $w$, and given $\kappa_j$ and the success event (both
invariant), $e_j$ is uniform on the unit sphere of $w^\perp$, independently for
$j=1,2$. When both runs succeed, $|\kappa_1\kappa_2|\ge\rho^2$, and
$|\langle e_1,e_2\rangle|\le\rho^2/2$ except with probability $2e^{-(d-1)\rho^4/8}$, so
$|\langle\hat o_1,\hat o_2\rangle|\ge\rho^2/2$. $\square$

Other regime. The lemma is for record-level (sample) access. In the SQ game an
adversarial oracle can correlate the two runs under the null, so it is not claimed
there.

### thm-coarse-reconstruction-lattice-hard: constant-correlation blind reconstruction of pancakes is lattice-hard
status: proven
uses: lem-agreement-detection, lem-equivariant-view-coupling, fact-clwe-hardness

Statement. A protocol of $\mathcal P_{O(d)}$, frozen or trained, runs on
$N\ge Cd\log^2(\gamma/\beta)$ records from $H_{v,\beta,\gamma}$ (BRST21 normalization),
$\beta\in(0,1)$, $\gamma\ge2\sqrt d$, $\gamma/\beta\le\mathrm{poly}(d)$, with no side data.
Let $a_i=\langle v,x_i\rangle$. If a seed-blind attacker of time $T$ outputs
$t\in\mathbb R^N\setminus\{0\}$ with $|\langle t,a\rangle|\ge c_0\|t\|\|a\|$ with probability $p$,
then hCLWE$_{\beta,\gamma}$ has an algorithm of time $2(T+T_{\rm run})+\mathrm{poly}(d)$ and
advantage at least $(p-e^{-\Omega(d)})^2-4e^{-(d-1)c_0^4/648}$. With BRST21 Corollary
4.2, $p$ is negligible for polynomial-time attackers unless worst-case lattice
problems are quantum-easy. This settles `prob-coarse-reconstruction-lattice-hardness`.

Proof. Take $\mathcal A$: on $N$ samples $u_i$ of $H_w$, run the protocol from fresh
coins on them, run the attacker, and output $o=U^\top t$, with $U$ the matrix of rows
$u_i^\top$. By `lem-equivariant-view-coupling` with a fixed rotation sending $v$ to
$w$, the attacker succeeds with probability $p$ for $a_i=\langle w,u_i\rangle$. Then
$\langle o,w\rangle=\langle t,a\rangle$ and $\|o\|\le\|U\|\|t\|$, so
$|\langle o,w\rangle|\ge c_0(\|a\|/\|U\|)\|o\|$. By `fact-clwe-hardness`
$0.99/(2\pi)\le\sigma_a^2\le\sigma_{\max}^2=1/(2\pi)$, and with probability $1-e^{-\Omega(d)}$
for the stated $N$, $\|a\|^2\ge N\sigma_a^2/2$ (Bernstein, sub-Gaussian $a_i$) and
$\|U\|\le2\sqrt N\sigma_{\max}$ (BRST21 Lemma 7.4 on $\Sigma^{-1/2}u_i$, norm
$O(\sqrt{\log(\gamma/\beta)})$). So $\rho=c_0\sigma_a/(2\sqrt2\sigma_{\max})\ge c_0/3$ with
probability at least $p-e^{-\Omega(d)}$, and `lem-agreement-detection` applies with
$P_w=H_w$, $P_0=D_0$. $\square$

Other regime. Polynomial time, lattice-conditional.

### thm-zlip-reductions: blind reconstruction of quantized Gaussian records against ZLIP
status: proven
uses: lem-equivariant-view-coupling, fact-lip-average-case, fact-discrete-gaussian-samples-generate, fact-zlip-best-algorithms

Setting. Records i.i.d. from $D_{\mathbb Z^d,s}$, $s\le\mathrm{poly}(d)$, a product of
$D_{\mathbb Z,s}$ with covariance $\sigma_s^2I$. Exact success: some signed permutation
$P$ has $t_i=Px_i$ for every record. The problem ac-sLIP$^{I}_{s}$ is DvW22
Definition 3.7 with $Q=I_d$, average-case ZLIP.

(a) Lower bound, any client of $\mathcal P_{O(d)}$ without side data. Let
$s_0\ge\max\{1,\eta_{1/2}(\mathbb Z^d)\}$ and $s=s_0\sqrt{d\ln(2d+4)/\pi}$. An attacker of
time $T$ with exact success $p$ on $N\ge\lceil2d/C\rceil$ records solves
ac-sLIP$^{I}_{s_0}$ in time $T+T_{\rm run}+\mathrm{poly}(d)$ with probability
$p-O(d2^{-d})$.

(b) Upper bound, frozen client $z=Wx$ with $W$ of full column rank. With
$\mathrm{poly}(d)$ records and an oracle solving ac-sLIP$^{I}_s$ (the record width) with
probability $q$, the server achieves exact success with probability $q-2^{-\Omega(d)}-\delta$
at $\mathrm{poly}(d,\log(1/\delta))$ overhead.

Under the hardness of average-case ZLIP at polynomial widths (the assumption of
DvW22), no polynomial-time seed-blind attacker reconstructs quantized Gaussian
records, while the seed-known server inverts each with one linear solve. The best
attacks known are those of `fact-zlip-best-algorithms`, as of Duc24's account.

Proof of (a). Given $Q'\sim D_{s_0}([I])$, $Q'=U^\top U$ for an unknown $U\in GL_d(\mathbb Z)$.
By DvW22 Lemma 3.6 with $\epsilon=1/2$, $\|B^*_{Q'}\|\le s_0\sqrt d$ except with probability
$300d2^{-d}$, so Lemma 2.9 samples $c_1,\dots,c_N\sim D_{Q',s}$. With $B'$ the Cholesky
factor of $Q'$, $O=B'U^{-1}$ is orthogonal, and $x_i=Uc_i$ has mass proportional to
$\rho_s(B'c_i)=\rho_s(x_i)$, so the $x_i$ are i.i.d. $D_{\mathbb Z^d,s}$ given $Q'$. The reducer
holds $y_i=B'c_i=Ox_i$ and runs the protocol on them from fresh coins. By
`lem-equivariant-view-coupling` with the fixed $O$, the attacker returns
$t_i=PUc_i$ with probability $p$. The $c_i$ span $\mathbb R^d$ except with probability
$e^{-2d}$ (the argument of DvW22 Lemma 3.4), and for an invertible block $C_d$ the
reducer sets $U'=T_dC_d^{-1}$, checks that $U'$ is integral with $\det U'=\pm1$ and
$U'^\top U'=Q'$, and outputs it. On success $U'=PU$ passes every check. $\square$

Proof of (b). Three independent blocks. Block 1: by HR14 Lemma 5.4, $\mathrm{poly}(d)$
records generate $\mathbb Z^d$ except with probability $2^{-\Omega(d)}$. The server computes,
by exact linear algebra and a Hermite normal form on the rational coordinates of
the $z_j$ in a basis of their span, a basis $B=WU$ of $W\mathbb Z^d$ with $U$
unimodular, and integer coordinates $k=B^{-1}z$, so $x=Uk$. It also fixes $d$
independent records $X_d=UM$ of block 1, with $M$ known and $\|x_a\|\le s\sqrt d$.
Block 2: $E[kk^\top]=\sigma_s^2(U^\top U)^{-1}$, so
$\hat Q_X:=M^\top\sigma_s^2\hat E_k^{-1}M=X_d^\top(\sigma_s^2\hat E_x^{-1})X_d$, and
$\hat Q_X-X_d^\top X_d=X_d^\top\Delta X_d$ with $\Delta=\sigma_s^2\hat E_x^{-1}-I$. The records are
isotropic and sub-Gaussian, so $\|\Delta\|\le1/(4s^2d)$ with probability $1-\delta$ for
$N_2=O(s^4d^2(d+\log(1/\delta)))$, and every entry error is at most
$\|\Delta\|\|x_a\|\|x_b\|<1/2$. Rounding gives the integral $Q_X=X_d^\top X_d$ exactly, and
$Q_B=U^\top U=M^{-\top}Q_XM^{-1}$. Block 3: conditional on blocks 1 and 2, the
coordinates $k$ of fresh records are i.i.d. $D_{Q_B,s}$, so DvW22 Definition 3.3 run
on fresh blocks of $\lceil2d/C\rceil$ records, $\mathrm{Extract}(Q_B,Y)$, returns
$R\sim D_s([I])$ and $U_E$ with $R=U_E^\top Q_BU_E$. The oracle returns $U_R$ with
$R=U_R^\top U_R$, checked as in (a). Then $U'=U_RU_E^{-1}$ has $U'^\top U'=Q_B=U^\top U$,
so $U'U^{-1}$ is integral and orthogonal, a signed permutation $P$, and $t=U'k=Px$
for every record. $\square$

Other regime. Statistically a frozen linear view determines the records up to $P$.
The gap is computational.

### prop-blind-lll-label-recovery: discrete hidden labels behind a hidden linear client
status: proven
uses: fact-lll-recovers-discrete-hidden-labels, fact-ngca-sq-lower-bound, lem-equivariant-view-coupling

Setting. Records from ZSWB22 Model 4.3: integer labels $k_i$ with mass
proportional to $e^{-k^2/(2\gamma^2)}$, $\ell_i=k_i/\gamma$, $x_i\sim N(\ell_iv,I-vv^\top)$,
$2\sqrt d\le\gamma\le\mathrm{poly}(d)$. A frozen client $z=Wx$, $W$ right rotation
invariant, of full column rank, hidden from the attacker.

(a) Sample game. A polynomial-time seed-blind server recovers $\ell_1,\dots,\ell_{d+1}$
exactly up to one global sign from $z_1,\dots,z_{d+1}$, with probability
$1-e^{-\Omega(d)}$. So it also detects the discrete hidden structure.

(b) SQ game. Every SQ algorithm with access to the law of the representation that
tells these records from Gaussian records needs $2^{d^{\Omega(c)}}$ queries or a
tolerance $O_k(d^{-((1-\lambda)/4-c)k})$, for every fixed even $k$ (constants of
DKRS23 Theorem 1.5).

Detection is one task on one protocol: polynomial in the sample game,
superpolynomial in the SQ game. The general separation of SQ and LLL for NGCA is in
DKRS23, Section 1.1.1, and ZSWB22. The content here is that it survives a hidden
injective client.

Proof. (a) In the $d$-dimensional span of the representations, the dependency
$\sum_i\lambda_iz_i=0$ has the same coefficients as $\sum_i\lambda_ix_i=0$, since $W$ is
injective, so Algorithm 1's LLL step returns the same $t_1$ on representations as on
records. Model 4.3 is Model 3.2 with $a=1/\gamma$ (ZSWB22 Claim 4.5). Primitive labels:
with $s'=\gamma\sqrt{2\pi}$ the labels are $D_{\mathbb Z,s'}$. By Poisson summation
$\rho_{s'}(p\mathbb Z+c)\le\rho_{s'}(p\mathbb Z)$, and
$D_{\mathbb Z,s'}(p\mathbb Z)\le1/p+1/s'$. With $|k_i|\le K=\mathrm{poly}(d)$ except with
probability $e^{-\Omega(d)}$ (ZSWB22 Claim 2.7), a common prime divisor is at most $K$,
so $\Pr[\gcd(k_1,\dots,k_{d+1})>1]\le\sum_{p\le K}(1/p+1/s')^{d+1}=e^{-\Omega(d)}$, and all of
$k_2,\dots,k_{d+1}$ vanish with probability at most $(1/s')^d$. On the complement,
the revised fact gives $t_1$ proportional to the primitive $k$, so
$k=\pm t_1/\gcd(t_1)$ and $\ell=k/\gamma$. (b) For an even $k$ and a unit-norm polynomial
$f=\sum_{j\le k}c_jh_j$, $|E_\nu f-E_{N(0,1)}f|\le(\sum_{1\le j\le k}E_\nu[h_j]^2)^{1/2}$.
Poisson summation on $(1/\gamma)\mathbb Z$ with
$\mathcal F[h_j\varphi](\xi)=(-2\pi i\xi)^je^{-2\pi^2\xi^2}/\sqrt{j!}$ gives
$|E_\nu h_j|\le C_j\gamma^je^{-2\pi^2\gamma^2}$, below $d^{-((1-\lambda)/4-c)k}$ for
$\gamma\ge2\sqrt d$. So DKRS23 Theorem 1.5 holds for $P^\nu_v$. A tester on representations
becomes a tester on records by answering each query $f$ with $f\circ W'$ for a sampled
$W'$, whose planted law is that of the real game (the frozen case of
`lem-equivariant-view-coupling`). $\square$

Other regime. Both games, one task. With inverse-polynomial noise on the labels
(hCLWE) the sample game becomes hard as well (`thm-coarse-reconstruction-lattice-hard`).
