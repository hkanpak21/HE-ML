# Round 05, builder: computational limits, the last repairs of milestone 2

Space `computational-limits`, round 05, 2026-10-25, the last round of the
milestone. Builder: the Claude session space-computational. Discussant of round
04: sol. This round resubmits the two theorems sol marked REVISE and answers its
three blocking challenges. The four objects accepted in round 04 are not
resubmitted, and their non-blocking wording points are listed in the round-04
summary for the integrator.

## Responses to round 04

`ch-coarse-zero-output` (blocking). Accepted. The direction algorithm of
`thm-coarse-reconstruction-lattice-hard` returns an independent uniform unit
vector when $U^\top t=0$. On the success event $U^\top t\ne0$, since
$|\langle U^\top t,w\rangle|=|\langle t,a\rangle|\ge c_0\|t\|\|a\|>0$, and the replacement is
rotation invariant, so the null symmetry of `lem-agreement-detection` is kept.
$c_0>0$ is a fixed constant.

`ch-zlip-small-width` (blocking). Accepted, with sol's counterexample at width
$d^{-1/4}$. Both parts of `thm-zlip-reductions` now assume the record width
$s\ge\max\{1,\eta_{1/2}(\mathbb Z^d)\}$, which part (a) already implies through
$s=s_0\sqrt{d\ln(2d+4)/\pi}$ with $s_0\ge1$. Block 3 is one fresh block that aborts on
deficient rank, sol's simplification.

`ch-hardness-computation-model` (blocking for the security conclusions).
Accepted. Both theorems are reductions between algorithms of one model $\mathsf M$:
exact arithmetic on real numbers with $+,-,\times,\div$, square roots and
comparisons, and samples of the standard Gaussian, on which the protocol, the
attacker and every reducer run. The security conclusions are now conditional on
hardness in $\mathsf M$, stated as an assumption. The transfer to the standard
assumptions on Turing machines (BRST21 Corollary 4.2, DvW22) needs a
finite-precision simulation of the protocol and the attacker, which is open and
goes to the registers. The seed-known sentence is restricted to frozen injective
linear clients.

## Objects

### thm-coarse-reconstruction-lattice-hard: constant-correlation blind reconstruction of pancakes is as hard as hCLWE
status: proven
uses: lem-agreement-detection, lem-equivariant-view-coupling, fact-clwe-hardness

Statement. In the model $\mathsf M$, a protocol of $\mathcal P_{O(d)}$ computable in
$\mathsf M$, frozen or trained, runs on $N\ge Cd\log^2(\gamma/\beta)$ records from
$H_{v,\beta,\gamma}$ (BRST21 normalization), $\beta\in(0,1)$, $\gamma\ge2\sqrt d$,
$\gamma/\beta\le\mathrm{poly}(d)$, with no side data. Let $a_i=\langle v,x_i\rangle$ and
$c_0>0$ fixed. If a seed-blind attacker of time $T$ outputs $t\in\mathbb R^N\setminus\{0\}$ with
$|\langle t,a\rangle|\ge c_0\|t\|\|a\|$ with probability $p$, then hCLWE$_{\beta,\gamma}$
(BRST21 Definition 2.21) has an algorithm in $\mathsf M$ of time
$2(T+T_{\rm run})+\mathrm{poly}(d)$ and advantage at least
$(p-e^{-\Omega(d)})^2-4e^{-(d-1)c_0^4/648}$. So if hCLWE$_{\beta,\gamma}$ has no
polynomial-time algorithm in $\mathsf M$ with non-negligible advantage, no
polynomial-time attacker in $\mathsf M$ reconstructs pancake records to any constant
correlation.

Proof. The direction algorithm $\mathcal A$: on $N$ samples $u_i$ of $H_w$, run the
protocol from fresh coins on them and the attacker on the view, and output
$o=U^\top t$ (rows of $U$ are the $u_i^\top$), or an independent uniform unit vector
if $U^\top t=0$. By `lem-equivariant-view-coupling` with a fixed rotation sending
$v$ to $w$, the attacker succeeds with probability $p$ for $a_i=\langle w,u_i\rangle$.
On success, $\langle o,w\rangle=\langle t,a\rangle$ and $\|o\|\le\|U\|\|t\|$, so
$|\langle o,w\rangle|\ge c_0(\|a\|/\|U\|)\|o\|$, and $o\ne0$. By `fact-clwe-hardness`,
$0.99/(2\pi)\le\sigma_a^2\le\sigma_{\max}^2=1/(2\pi)$. With probability $1-e^{-\Omega(d)}$
for the stated $N$, $\|a\|^2\ge N\sigma_a^2/2$ (Bernstein, sub-Gaussian $a_i$) and
$\|U\|\le2\sqrt N\sigma_{\max}$ (BRST21 Lemma 7.4 on $\Sigma^{-1/2}u_i$, sub-Gaussian norm
$O(\sqrt{\log(\gamma/\beta)})$). So $|\langle o,w\rangle|\ge\rho\|o\|$ with
$\rho=c_0\sigma_a/(2\sqrt2\sigma_{\max})\ge c_0/3$ with probability at least $p-e^{-\Omega(d)}$
for every $w$. The family $P_w=H_w$ satisfies $Q_\#H_w=H_{Qw}$ and $P_0=D_0$ is rotation
invariant, so `lem-agreement-detection` with $\rho=c_0/3$ gives the tester, whose
two runs cost $2(T+T_{\rm run})$ and whose remaining steps (Haar rotations, inner
products, one comparison) are polynomial in $\mathsf M$. $\square$

This settles `prob-coarse-reconstruction-lattice-hardness` in $\mathsf M$.

Other regime. Polynomial time, conditional on hCLWE in $\mathsf M$. An unbounded
attacker is not bounded here.

### thm-zlip-reductions: blind reconstruction of quantized Gaussian records against ZLIP
status: proven
uses: lem-equivariant-view-coupling, fact-lip-average-case, fact-discrete-gaussian-samples-generate, fact-zlip-best-algorithms

Setting. The model $\mathsf M$. Records i.i.d. from $D_{\mathbb Z^d,s}$ with
$\max\{1,\eta_{1/2}(\mathbb Z^d)\}\le s\le\mathrm{poly}(d)$, a product of $D_{\mathbb Z,s}$ with
covariance $\sigma_s^2I$. Exact success: some signed permutation $P$ has $t_i=Px_i$
for every record. ac-sLIP$^{I}_{s}$ is DvW22 Definition 3.7 with $Q=I_d$.

(a) Lower bound, any client of $\mathcal P_{O(d)}$ computable in $\mathsf M$, with no
side data. Let $s_0\ge\max\{1,\eta_{1/2}(\mathbb Z^d)\}$ and $s=s_0\sqrt{d\ln(2d+4)/\pi}$. An
attacker of time $T$ with exact success $p$ on $N\ge\lceil2d/C\rceil$ records gives an
algorithm in $\mathsf M$ for ac-sLIP$^{I}_{s_0}$ of time $T+T_{\rm run}+\mathrm{poly}(d)$ and
success $p-O(d2^{-d})$.

(b) Upper bound, a frozen client $z=Wx$ with $W$ of full column rank. With
$\mathrm{poly}(d,\log(1/\delta))$ records and an oracle for ac-sLIP$^{I}_s$ at the record
width $s$ with success $q$, the server achieves exact success with probability at
least $q-2^{-\Omega(d)}-\delta$, at $\mathrm{poly}(d,\log(1/\delta))$ overhead in $\mathsf M$.

So if average-case ZLIP at polynomial widths has no polynomial-time algorithm in
$\mathsf M$, no polynomial-time seed-blind attacker in $\mathsf M$ reconstructs quantized
Gaussian records, while for a frozen injective linear client the seed-known server
recovers each record by one linear solve. The best attacks known are those of
`fact-zlip-best-algorithms`, as Duc24 reports them.

Proof of (a). As in round 04, which sol accepted line by line. Given
$Q'\sim D_{s_0}([I])$, DvW22 Lemma 3.6 with $\epsilon=1/2$ gives $\|B^*_{Q'}\|\le s_0\sqrt d$
except with probability $300d2^{-d}$, Lemma 2.9 samples $c_i\sim D_{Q',s}$, the Cholesky
factor $B'$ makes $O=B'U^{-1}$ orthogonal for the unknown $U$ with $Q'=U^\top U$, the
records $x_i=Uc_i$ are i.i.d. $D_{\mathbb Z^d,s}$, the protocol runs on $y_i=B'c_i=Ox_i$,
`lem-equivariant-view-coupling` transports the attacker's success, and an
invertible block gives $U'=T_dC_d^{-1}=PU$, output only if it is integral,
unimodular and satisfies $U'^\top U'=Q'$. $\square$

Proof of (b). Block 1: HR14 Lemma 5.4 with $bl(\mathbb Z^d)=1\le s$: $\mathrm{poly}(d)$ records
generate $\mathbb Z^d$ except with probability $2^{-\Omega(d)}$. Exact linear algebra and a
Hermite normal form on the rational coordinates of the $z_j$ in a basis of their
span give a basis $B=WU$ of $W\mathbb Z^d$, $U$ unimodular, and integer coordinates
$k=B^{-1}z$ with $x=Uk$. Fix $d$ independent records $X_d=UM$ of block 1, $M$ known,
with $\|x_a\|\le s\sqrt d$ (a union bound on the tails of DvW22 Lemma 2.7). Block 2:
$\hat Q_X=M^\top\sigma_s^2\hat E_k^{-1}M=X_d^\top(\sigma_s^2\hat E_x^{-1})X_d$, so the entries of
$\hat Q_X-X_d^\top X_d=X_d^\top\Delta X_d$ are at most $\|\Delta\|\|x_a\|\|x_b\|$ with
$\Delta=\sigma_s^2\hat E_x^{-1}-I$. For $s\ge1$ the normalized records $x/\sigma_s$ are isotropic
and sub-Gaussian with a constant norm, so $\|\Delta\|\le1/(4s^2d)$ with probability
$1-\delta$ for $N_2=O(s^4d^2(d+\log(1/\delta)))$, and rounding gives $Q_X=X_d^\top X_d$, hence
$Q_B=U^\top U=M^{-\top}Q_XM^{-1}$. Block 3: one fresh block of $\lceil2d/C\rceil$ records,
whose coordinates are i.i.d. $D_{Q_B,s}$ given blocks 1 and 2, with abort if it does
not span (probability at most $e^{-2d}$, DvW22 Lemma 3.4). $\mathrm{Extract}(Q_B,Y)$
returns $R\sim D_s([I])$ (DvW22 Definition 3.3) and $U_E$ with $R=U_E^\top Q_BU_E$. The
oracle's $U_R$, with $R=U_R^\top U_R$ checked, gives $U'=U_RU_E^{-1}$ with
$U'^\top U'=U^\top U$, so $U'U^{-1}$ is an integral orthogonal matrix, a signed permutation
$P$, and $t=U'k=Px$ for every record. $\square$

Other regime. The population law of the frozen linear view determines the records
up to $P$. The gap is computational.
