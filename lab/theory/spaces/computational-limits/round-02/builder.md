# Round 02, builder: computational limits, the repairs

Space `computational-limits`, round 02, 2026-10-25. Builder: the Claude session
space-computational. Discussant of round 01: astra (a fallback for argon). This
round answers the ten blocking and the non-blocking challenges of round 01 and
resubmits the seven objects astra marked REVISE or REJECT. Objects accepted in
round 01 are not resubmitted. Two wording corrections to accepted objects are
listed for the integrator at the end of the responses.

Reads added for this round, in the held copy of DPLB24: Lemma 2.3, Lemma E.2 and
Lemma E.3 with its proof. BRST21 Lemma 7.2 was re-read for the sign.
Normalization as in round 01: $\rho_s(x)=e^{-\pi\|x/s\|^2}$, $\rho=\rho_1$, $D_0$
of density $\rho$ and covariance $I/(2\pi)$, $H_w=H_{w,\beta,\gamma}$ of BRST21
Definition 2.19, layer spacing $s_\ell=\gamma/(\beta^2+\gamma^2)$ and layer shape
$\rho_{\sigma_\ell}$, $\sigma_\ell=\beta/\sqrt{\beta^2+\gamma^2}$.

## Responses to the challenges of round 01

`ch-pancake-covariance-sign` (blocking). Accepted and checked. In the proof of
BRST21 Lemma 7.2 the Fourier transform of $x^2\rho(x)$ is $(1/(2\pi)-y^2)\rho(y)$,
so Poisson summation gives $E[x^2]=1/(2\pi)-\sum_{y\in\gamma'\mathbb Z}y^2\rho(y)/\rho(\gamma'\mathbb Z)$,
a deficit. The revised `fact-clwe-hardness` states the bound
$0\le\Delta\le3(\gamma^2+1)e^{-\pi\gamma^2}$ on the deficit, and the two
pancake propositions use $\sigma_{\min}(\Sigma)\ge(1-2\pi\Delta)/(2\pi)$ and
$\sigma_{\max}(\Sigma)=1/(2\pi)$. The constants change slightly, the arguments do
not.

`ch-keyed-encoding-confidence` (blocking). Accepted. The revised
`fact-ideal-keyed-encoding-weak-learner` restores the $(1/2-\varepsilon,\delta)$
balanced-error guarantee with constants $0<\varepsilon,\delta<1/2$.

`ch-sq-price-range` (blocking). Accepted. Part (a) of
`prop-sq-blind-reconstruction-bound` now assumes the margin
$\tau_*^2\ge6\gamma_c$ and a packing with $M\ge48/\rho_0^2$, subtracts the $d$
auxiliary queries, and states the price with explicit constants.
`thm-blind-split-seed-separation` keeps $\tau_*=\min(\tau,\tau_1)$.

`ch-witness-uniformity` (blocking). Accepted. Part (b) now requires a witness of
fixed degree $j^*\ge1$, fixed strength $\kappa>0$, fixed success level $c_0$ and
fixed tail constant $\sigma$, all independent of $d$, so $\tau_2$ is a constant.

`ch-label-sq-self-correlation` (blocking). Accepted. DPLB24's proof takes the
diagonal bound $1$, while the diagonal correlation is
$\chi_0(P_w,P_w)=\sum_{k\ge k^*}\lambda_k^2=I_{\chi^2}[P]$ (the series of the proof of
Lemma E.2 at overlap $1$, and Lemma 2.3), which can exceed $1$. The revised
proposition assumes $I_{\chi^2}[P]<\infty$ and uses it as the diagonal bound.

`ch-label-sq-code-overlap` (blocking). Accepted. Lemma E.3 gives overlap
$\epsilon=\sqrt{C\log_d(m)^2/d}=\sqrt C\log_d(m)/\sqrt d$. The revised proof
verifies $\epsilon\le\rho^2/2$ for the code size it uses.

`ch-label-sq-auxiliary-budget` (blocking). Accepted. The revised proposition fixes
the query exponent $r$, the law $P$ and $c_0$ independently of $d$. Then the code
overlap is $\Theta(d^{-1/2})$, the bound is $n'\ge c\,d^{k^*/2}$ with no
logarithmic loss, and for $k^*\ge3$ it exceeds the auxiliary budget
$n_1=\tilde O(d)$.

`ch-initial-observation-schedule` (blocking). Accepted. Part (i) of
`thm-blind-split-seed-separation` now covers frozen clients, and, for trained
clients, the records whose representation the server receives under $W_0$: the
first processed batch, or every record when the protocol makes a forward pass
over all records before the first update. Tracking later weights from a known
seed is a remark, labelled heuristic.

`ch-conjecture-erasing-client` (blocking). Accepted. The restated
`conj-seed-price-is-ngca-price` assumes recoverability: the seed-known attacker
recovers each record exactly from $(\omega,z_i)$ in polynomial time. Constant
post-maps and a zero first layer fail it.

`ch-conjecture-whitening-scope` (blocking). Accepted. The restated conjecture
assumes $A$ of mean $0$ and covariance $I_r$. Then $P^A_V$ is isotropic, whitening
returns $u=Rx\sim P^A_{RV}$ exactly, with $RV$ uniform and target
$V^\top x=(RV)^\top u$, so the frozen linear upper inclusion holds with no scaling
step, given the population whitening map.

Not blocking. The polynomial-time corollary of `prop-fine-reconstruction-to-hclwe`
now states that it needs a protocol of polynomial cost and arithmetic with
$\mathrm{poly}(d)$ bits, which preserves the test margin. The label-side upper bound
now runs DPLB24's Algorithm 1 on $(Rx_i,T_P(y_i))$ with the paper's denoiser
$T_P$, not on raw labels. For LeakyReLU the negative slope is known and nonzero,
and the predictor receives the representation while whitening receives its
coordinate-wise inverse.

Wording corrections to accepted objects, for the integrator to apply when it
merges them. In `def-seed-blind-reconstruction-game`, delete "The game
reconstructs the observed records, not fresh ones" and write in its place "The
sample game reconstructs the observed records. The SQ game evaluates a
reconstruction map on the record law. An experiment fixes finite representations
of queries and of returned maps." In `thm-reconstruction-from-conditional-mean`,
replace "This is Halil's lower bound in its exact form" by "This is the floor on
attack success in Halil's example: the attacker's error is bounded above by a
function of the attacked model's excess risk" (`ch-conditional-mean-interpretation`).

## Revised objects

### fact-clwe-hardness: homogeneous CLWE is a hard hidden-direction law
status: borrowed, revised
uses: none

BRST21, in its normalization. Definitions 2.19 and 2.21, Claim 2.22, Corollary
4.2, Theorem 7.5 and Corollary 9.4 as in round 01. Covariance. On $w^\perp$ the
covariance of $H_{w,\beta,\gamma}$ is $I/(2\pi)$. Along $w$ it is
$1/(2\pi)-\Delta$ with $0\le\Delta\le3(\gamma^2+1)e^{-\pi\gamma^2}$ for $\gamma\ge1$
and $\beta\in(0,1)$.

Proof of the covariance clause. The proof of Lemma 7.2 writes the noiseless
law $H_{w,\gamma'}$ as $D_{(1/\gamma')\mathbb Z}\times D_{\mathbb R^{n-1}}$, and Poisson
summation with the transform $(1/(2\pi)-y^2)\rho(y)$ gives
$E[x_1^2]=1/(2\pi)-\Delta'$ with
$\Delta'=\sum_{y\in\gamma'\mathbb Z}y^2\rho(y)/\rho(\gamma'\mathbb Z)\in[0,\,2.01\gamma'^2e^{-\pi\gamma'^2}]$
for $\gamma'\ge1$, since $\rho(\gamma'\mathbb Z)\ge1$ and the terms with
$|k|\ge2$ add less than $0.01\gamma'^2e^{-\pi\gamma'^2}$. The proof of Corollary 7.3
writes $H_{w,\beta,\gamma}$ as $H_{w,\gamma'}$ plus independent Gaussian noise of
parameter $\beta'/\gamma'=\beta/\gamma$, rescaled by $1/\sqrt{1+(\beta/\gamma)^2}$, with
$\gamma'=\sqrt{\beta^2+\gamma^2}$. Along $w$ this gives variance
$(1/(2\pi)-\Delta'+(\beta/\gamma)^2/(2\pi))/(1+(\beta/\gamma)^2)=1/(2\pi)-\Delta$
with $\Delta=\Delta'/(1+(\beta/\gamma)^2)\le\Delta'$, and $\gamma^2\le\gamma'^2\le\gamma^2+1$. On
$w^\perp$ the same rescaling of $1/(2\pi)+(\beta/\gamma)^2/(2\pi)$ gives $1/(2\pi)$.
$\square$ (Proven.)

The homogeneous law determines $w$ only up to sign.

Other regime. Computational, conditional on worst-case lattice hardness.

### fact-ideal-keyed-encoding-weak-learner: an ideal keyed encoding hands over the concept
status: borrowed, revised
uses: none

CGJMMT21, Definition 2 and Theorem 1. Let $E$ be weakly ideal for $\mathcal C$
(equal laws over the random key for equal-label inputs, labels preserved). If a
learner with $m$ samples obtains $(1/2-\varepsilon,\delta)$ balanced error for every
$c\in\mathcal C$ over the encoded law, for constants $0<\varepsilon,\delta<1/2$, then for
every $\tau\in[0,1]$ and every pair $x_0,x_1$ with $c(x_0)=0$ and $c(x_1)=1$ there is
an oracle-aided PPT predictor, with oracle access to the learner and the keyed
encoder, of risk at most $\tau$ on an arbitrary distribution, in time
poly$(m,1/\epsilon,1/\delta,1/\tau)$.

Other regime. As before.

### prop-sq-blind-reconstruction-bound: SQ price of blind reconstruction from a frozen client
status: proven for part (a), proven conditional on DKRS23 Theorem 1.5 for part (b)
uses: lem-equivariant-view-coupling, fact-clwe-hardness, fact-hclwe-sq-correlation-bound, fact-ngca-sq-lower-bound, fact-fgrvx17-planted-clique-sq-bound

Setting as in round 01: $\Gamma_{\rm SQ}$ with $H=O(d)$, a frozen client of
$\mathcal P_{O(d)}$, no side data, $r=1$, target $g(x)=\langle v,x\rangle$,
$K=\{\pm1\}$.

(a) Pancake records. Let $D=H_{v,\beta,\gamma}$ with $\gamma\ge2$, $\beta\in(0,1)$ and
$c_0\in(0,1]$. Let $\rho_0=c_0/3$, $\alpha_0=\rho_0^2/2$,
$\gamma_c=8e^{-\pi\gamma^2(1-\alpha_0^2)}$, $\beta_c=2(\gamma/\beta)^2$,
$M=\lfloor e^{d\alpha_0^2/4}/2\rfloor$, $L=\sqrt{\log(48\gamma d/(\beta c_0))}$ and
$\tau_1=c_0/(9\sqrt{2\pi}L\sqrt d)$. Assume $M\ge48/\rho_0^2$ and
$\tau_*^2\ge6\gamma_c$, where $\tau_*=\min(\tau,\tau_1)$. Then an attacker that
reaches weak success $c_0$ with $q$ queries of STAT($\tau$) satisfies
$$q\;\ge\;\frac{11}{288}\,M\,\frac{\tau_*^2\beta^2}{\gamma^2}\;-\;d .$$
Both assumptions hold for $d\ge C\log(1/c_0)/c_0^4$ and $\gamma^2\ge C\log(d/c_0)$,
in particular for $\gamma\ge2\sqrt d$ and $d$ large. So the price is
$\exp(\Omega(c_0^4d))\tau_*^2\beta^2/\gamma^2$ queries.

(b) Moment-matched records. Let $D=P^A_v$ with $\gamma_d$ on $v^\perp$ and $A$ of
mean $0$, variance $1$ and $\Pr_A[|a|>t]\le2e^{-t^2/(2\sigma^2)}$. Let $A$ satisfy
the hypothesis of DKRS23 Theorem 1.5 in ambient dimension $d$ with an even moment
degree $k$, constants $\lambda,c$ and slack $\nu$, and let $|E_A[h_{j^*}]|\ge\kappa$
for a witness degree $j^*\ge1$. Let $\sigma,j^*,\kappa,c_0,\lambda,c,k$ be fixed,
independent of $d$. If $((1-\lambda)/4-c)k>1/2$ and $\nu\le d^{-((1-\lambda)/4-c)k}$,
then for $d$ large every attacker reaching weak success $c_0$ with $q$ queries of
STAT($\tau$) has $q\ge2^{d^{\Omega(c)}}-d-1$ or $\tau\le O_k(d^{-((1-\lambda)/4-c)k})$.

Proof. The common part is that of round 01 with the corrected covariance.
$\sigma_{\max}=(2\pi)^{-1/2}$ and $\sigma_a\ge(2\pi)^{-1/2}(1-2\pi\Delta)^{1/2}$. For
$\gamma\ge2$, $2\pi\Delta\le6\pi\cdot5e^{-4\pi}<4\cdot10^{-4}$, so
$\sigma_a\ge0.9998(2\pi)^{-1/2}$. The reducer's $d$ queries
$R(\Phi_{\omega'}(u))\mathrm{clip}(u_j,L)/L$ at tolerance $\tau_1$ give each
coordinate of $\bar w=E[R(\Phi_{\omega'}(u))u]$ within
$L\tau_1+E[|u_j|\mathbf 1\{|u_j|>L\}]$. Here
$L\tau_1=c_0/(9\sqrt{2\pi}\sqrt d)\le c_0\sigma_a/(8\sqrt d)$, and by the density
bound $H_w\le(3\gamma/\beta)D_0$ the truncation term is at most
$(3\gamma/\beta)e^{-\pi L^2}/\pi\le c_0/(16\pi d)\le c_0\sigma_a/(8\sqrt d)$ for the stated $L$, since
$E_{D_0}[|g|\mathbf 1\{|g|>L\}]=e^{-\pi L^2}/\pi$ for $g$ of density $\rho$ and
$e^{-\pi L^2}\le\beta c_0/(48\gamma d)$.
So $\|\hat w-\bar w\|\le c_0\sigma_a/4$, $|\langle\hat w,w\rangle|\ge3c_0\sigma_a/4$,
$\|\hat w\|\le\sigma_{\max}+c_0\sigma_a/4\le2\sigma_{\max}$, and
$|\langle\hat s,w\rangle|\ge3c_0\sigma_a/(8\sigma_{\max})\ge0.37c_0\ge\rho_0$.

Part (a). The search problem, the packing $U$ of $M$ unit vectors with pairwise
overlap at most $\alpha_0$, the Gram count of at most $4/\rho_0^2$ vectors that one
output solves, BRST21 Proposition 8.3, FGRVX17 Lemma 3.10 and Theorem 3.2 are as
in round 01. With $M\ge48/\rho_0^2$, the solution-set fraction is
$\eta=4/(\rho_0^2M)\le1/12$, so $(\alpha-\eta)/(1-\eta)\ge2/3-1/12\ge1/2$ for
$\alpha=2/3$, and $|D_{\hat s}|\ge(11/12)M$. With $\bar\gamma=\tau_*^2/3$ and
$\tau_*^2\ge6\gamma_c$, $\gamma'=\bar\gamma-\gamma_c\ge\tau_*^2/6$, and
$\beta_c-\gamma_c\le\beta_c=2(\gamma/\beta)^2$. FGRVX17 Theorem 3.2 gives
$q+d\ge\frac12\cdot\frac{11}{12}M\cdot\frac{\tau_*^2/6}{2(\gamma/\beta)^2}=\frac{11}{288}M\tau_*^2\beta^2/\gamma^2$.
The two assumptions: $M\ge48/\rho_0^2$ is $e^{dc_0^4/1296}\ge864/c_0^2+2$, and
$\tau_1^2\ge6\gamma_c$ is $c_0^2/(162\pi L^2d)\ge48e^{-\pi\gamma^2(1-\alpha_0^2)}$, which
holds once $\gamma^2(1-\alpha_0^2)\ge\pi^{-1}\log(7776\pi L^2d/c_0^2)$.

Part (b). As in round 01, with $\rho_1=3c_0/(8\sigma_{\max})=3c_0/8$ for the
isotropic $A$. With $j^*,\kappa,c_0,\sigma$ fixed, a fixed $M_h$ meets the
truncation condition, so $\tau_2=\rho_1^{j^*}\kappa/(4M_h)$ is a positive constant.
Since $|E_A[h_j]|\le\nu$ for $1\le j\le k$ and $\nu\to0$, a fixed $\kappa$ forces
$j^*>k$ for $d$ large. The composite tester uses $q+d+1$ queries of tolerance
$\min(\tau,\tau_1,\tau_2)$, and DKRS23 Theorem 1.5 bounds it. Since
$\tau_1=\tilde\Theta(d^{-1/2})$ and $\tau_2=\Theta(1)$ exceed
$O_k(d^{-((1-\lambda)/4-c)k})+(1+o(1))\nu$ for $d$ large under the two stated
conditions, the minimum is $\tau$. $\square$

Other regime. SQ only. Lattice methods are outside these bounds
(`fact-ngca-sq-lower-bound`).

### prop-fine-reconstruction-to-hclwe: polynomial-time price of fine blind reconstruction
status: proven
uses: lem-equivariant-view-coupling, fact-clwe-hardness

Statement. As in round 01: a protocol of $\mathcal P_{O(d)}$ (frozen or trained)
on $N$ records from $H_{v,\beta,\gamma}$, $\beta\in(0,1)$, $\gamma\ge2\sqrt d$,
$\gamma/\beta$ polynomial, no side data, $c_1=1/(16\pi\sqrt{2\pi})$. An attacker of
time $T$ that, with probability $p$, outputs $t_{1:N}$ with
$|t_i-\kappa\langle v,x_i\rangle|\le c_1/\gamma$ for all $i$ and some $\kappa\in\{\pm1\}$
gives, for $N=N'=Cd\log^2(\gamma/\beta)$, an algorithm for hCLWE$_{\beta,\gamma}$ of
time $T+T_{\rm run}+\mathrm{poly}(d)$ and advantage at least $p-e^{-\Omega(d)}$,
where $T_{\rm run}$ is the cost of one protocol run. If the protocol runs in
polynomial time and arithmetic carries $\mathrm{poly}(d)$ bits, BRST21
Corollary 4.2 makes $p$ negligible for every polynomial-time attacker unless
DGS$_{2\sqrt{2d}\eta_\varepsilon(L)/\beta}$ has a polynomial-time quantum algorithm.

Proof. Steps 1 and 3 are those of round 01, which astra accepted line by line.
Step 2 with the corrected covariance. $\Sigma\succeq(1-2\pi\Delta)I/(2\pi)\succeq0.99I/(2\pi)$
for $\gamma\ge2$. BRST21 Lemma 7.4 applied to the isotropic rows $\Sigma^{-1/2}u_j$,
of sub-Gaussian norm $O(\sqrt{\log(\gamma/\beta)})$, gives
$\|\frac1N\Sigma^{-1/2}U^\top U\Sigma^{-1/2}-I\|\le1/2$ with probability
$1-e^{-\Omega(d)}$ for $N=Cd\log^2(\gamma/\beta)$, so
$\sigma_{\min}(U)\ge(N\cdot0.99/(4\pi))^{1/2}\ge\sqrt N/(2\sqrt{2\pi})$, the bound
round 01 used. The least-squares error, the angle bound $\theta\le1/(8\gamma)$ and
the test then follow as before. In step 3, $E|a|\le\sigma_a\le(2\pi)^{-1/2}$. With
$\mathrm{poly}(d)$-bit arithmetic, rounding moves each $\langle\hat s,u_j\rangle/s_\ell$
by $2^{-\mathrm{poly}(d)}$, which changes $S$ by less than the margin
$\kappa_\beta/6$. $\square$

Other regime. Conditional on worst-case lattice hardness, against
polynomial-time attackers with the record-level view.

### thm-blind-split-seed-separation: the seed separates attackers for pancake records
status: proven
uses: fact-lei-random-expansive-layers-invertible, prop-sq-blind-reconstruction-bound, prop-fine-reconstruction-to-hclwe, lem-equivariant-view-coupling

Statement. The client's first layer is $z=\mathrm{ReLU}(Wx)$, $W\in\mathbb R^{m\times d}$
with i.i.d. Gaussian entries, $m=c_0'd$, $c_0'\ge2.1$, further layers optional
and each satisfying LJDD19 Assumption 1, the update satisfies item 3 of
$\mathcal P_{O(d)}$, and the records are i.i.d. from $H_{v,\beta,\gamma}$,
$\beta\in(0,1)$, $\gamma\ge2\sqrt d$, $\gamma/\beta$ polynomial, with no side data.

(i) Seed-known. For a frozen client, every record $x_i$ is recovered exactly in
polynomial time from $z_i$ and $W$, with probability $1-Ne^{-\Omega(d)}$ (LJDD19
Theorem 3 per record, union bound). For a trained client, the same holds for the
records whose representation the server receives under $W_0$: the first
processed batch, and every record when the protocol makes a forward pass over all
records before the first update.

(ii) Seed-blind, population SQ, frozen client. Weak success $c_0$ costs at least
$\frac{11}{288}M\tau_*^2\beta^2/\gamma^2-d$ queries of STAT($\tau$), with
$\tau_*=\min(\tau,\tau_1)$ and $M,\tau_1$ as in part (a) of
`prop-sq-blind-reconstruction-bound`, for $d$ large.

(iii) Seed-blind, record-level view, polynomial time, frozen or trained client of
polynomial cost. Fine success at scale $c_1/\gamma$ has negligible probability
unless DGS$_{2\sqrt{2d}\eta_\varepsilon(L)/\beta}$ is quantum polynomial-time
(`prop-fine-reconstruction-to-hclwe`).

Proof. (i) LJDD19 Theorem 3 needs Assumption 1 for each layer and an input fixed
independently of the weights, and each record is independent of $W$. A
representation computed with $W_0$ is exactly the object Theorem 3 inverts.
(ii) and (iii) are the cited propositions, whose hypotheses the client meets. $\square$

Remark (heuristic). A seed-known server could track a trained client's weights:
invert the first batch, recompute the client's update from the back-propagated
signals it sent and the recovered records, and repeat. Each step needs the
current weights to keep the injectivity of LJDD19 Lemma 1, which Theorem 3 does
not give for trained weights.

The price of the seed: one linear solve per record for the seed-known attacker,
against exponentially many statistical queries, or a quantum algorithm for a
worst-case lattice problem, for the seed-blind one, plus one training run for the
reduction. Astra judges this an artificial-distribution reduction: the Gaussian
layer is no plug-in, but the hardness enters through the pancake record law and
no learning task enters the separation. That judgement is a decision for Halil,
named below.

Other regime. The gap is computational. An unbounded blind attacker is not
bounded here.

### conj-seed-price-is-ngca-price: the seed is worth the NGCA price of the record law
status: open, restated
uses: lem-equivariant-view-coupling, lem-whitening-gives-rotated-records, prop-sq-blind-reconstruction-bound, prop-fine-reconstruction-to-hclwe

Statement. Consider frozen clients of $\mathcal P_{O(d)}$ that are recoverable:
a polynomial-time seed-known attacker recovers every record exactly from
$(\omega,z_i)$ with probability $1-o(1)$. Let the records be i.i.d. from $P^A_V$
with $A$ of mean $0$ and covariance $I_r$, $r=O(1)$, and no side data. Then the
budget sets of seed-blind attackers in $\Gamma_{\rm SQ}$ (weak success) and in
$\Gamma_{\rm samp}$ (fine success) for the target $V^\top x$ modulo the symmetry
group of $A$ equal, up to $\mathrm{poly}(d)$ in each resource and constant factors in
the success level, those of NGCA coordinate recovery for $A$ with a uniformly
random hidden frame.

Settled. Lower inclusion: for pancakes in both games (`prop-sq-blind-reconstruction-bound`
part a, `prop-fine-reconstruction-to-hclwe`), and for moment-matched $A$ with
$k\ge4$ and a fixed witness in the SQ game (part b). Upper inclusion: for frozen
linear clients of full column rank given the population whitening map. Since $A$
is isotropic, $P^A_V$ is isotropic, `lem-whitening-gives-rotated-records` gives
$u_i=Rx_i\sim P^A_{RV}$ with $R$ Haar, so $RV$ is a uniformly random frame and
the NGCA output $(RV)^\top u_i=V^\top x_i$ is the target itself (proven). Linear
clients are recoverable.

Open. The upper inclusion for ReLU and deeper recoverable clients, where the
blind server must learn the client map without the seed. The cost of estimating
the whitening map, in samples or statistical queries, and the robustness of NGCA
algorithms to that estimate. Coarse reconstruction in polynomial time
(`prob-coarse-reconstruction-lattice-hardness`).

What would settle it. A blind inverter for expansive Gaussian ReLU clients that
learns the client up to rotation from representations of an isotropic record law,
at polynomial cost. A refutation: a recoverable client for which blind
reconstruction is easier or harder than NGCA by more than polynomial factors.

Regime and experiment. Computational. The experiment of round 00, with a
lattice-reduction attacker added (`fact-ngca-sq-lower-bound`).

### prop-sq-label-relevant-reconstruction-bound: what the labels cost the server
status: proven
uses: lem-equivariant-view-coupling, lem-whitening-gives-rotated-records, fact-generative-exponent-sq-recovery-bound, fact-fgrvx17-planted-clique-sq-bound

Statement. Let the client be frozen and linear, $z=Wx$, with $W$ right rotation
invariant and of full column rank, records $x\sim\gamma_d$, labels with
$(\langle u,x\rangle,y)\sim P\in\mathcal G$ (DPLB24 Definition 1.1), generative
exponent $k^*\ge3$ and $I_{\chi^2}[P]=\sum_k\lambda_k^2<\infty$, target
$g(x)=\langle u,x\rangle$, $K=\{\pm1\}$. Fix $P$, $c_0\in(0,1]$ and $r\ge1$
independently of $d$.

(a) Lower bound. In $\Gamma_{\rm SQ}$ with the attacker's queries answered by
VSTAT($n$) on the law of $(z,y)$, an attacker of weak success $c_0$ with
$q\le d^r-d$ queries needs $n\ge c(P,c_0,r)\,d^{k^*/2}$ for $d$ large.

(b) Upper bound, sample-based. With population whitening, the server runs
DPLB24's Algorithm 1 on $(Tz_i,T_P(y_i))=(Rx_i,T_P(y_i))$ with the denoiser $T_P$ of
Theorem 4.1. With $n\ge C_{k^*}[d^{k^*/2}/\tilde\lambda_{k^*}^2+d/(\tilde\lambda_{k^*}^2\epsilon^2)]$
labelled representations it obtains $\hat s$ with $(\hat s\cdot Ru)^2\ge1-\epsilon^2$
with probability $1-2e^{-d^c}$, and reconstructs $\pm\langle u,x_i\rangle$ by
$\langle\hat s,Tz_i\rangle$ with average error at most
$2\epsilon^2\lambda_{\max}(\frac1n\sum_ix_ix_i^\top)$.

Proof of (a). Reduction, as accepted in round 01: the reducer answers the
attacker's queries $f(z,y)$ by $f(W'x',y)$ on the single-index law with a uniform
direction $w^*$, and the $d$ truncated queries at VSTAT($n_1$),
$n_1=\lceil64L^2d/c_0^2\rceil$, $L=\sqrt{2\ln(16\sqrt d/c_0)}$, return $\hat s$ with
$|\hat s\cdot w^*|\ge\rho=3c_0/5$, with probability $2/3$, using $Q\le d^r$ queries to
VSTAT($n'$), $n'=\max(n,n_1)$.

Lower bound for that search problem, written out. Take the code of DPLB24 Lemma
E.3: $m\le d^{d^{1/4}}$ unit vectors with pairwise overlap at most
$\epsilon=\sqrt C\log_d(m)/\sqrt d$. By the series in the proof of Lemma E.2,
$\chi_0(P_{w_i},P_{w_j})=\sum_{k\ge k^*}\lambda_k^2(w_i\cdot w_j)^k$, so off the
diagonal $|\chi_0|\le\lambda_{k^*}^2\epsilon^{k^*}+\epsilon^{k^*+1}/(1-\epsilon)\le2\lambda_{k^*}^2\epsilon^{k^*}=:\gamma_c$
once $\lambda_{k^*}^2\ge2\epsilon$ and $\epsilon\le1/2$, and on the diagonal
$\chi_0(P_w,P_w)=I_{\chi^2}[P]=:\beta_c$ by Lemma 2.3. If $\epsilon\le\rho^2/2$, the Gram
argument lets one output solve at most $4/\rho^2$ code members, so the
solution-set fraction is $\eta=4/(\rho^2m)$. FGRVX17 Lemma 3.10 and Theorem 3.2 with
$\bar\gamma=1/(3n')$, $\gamma'=\bar\gamma-\gamma_c$, give, for success $\alpha=2/3$ and
$\alpha'=(\alpha-\eta)/(1-\eta)$,
$$Q\ge\alpha'(m-4/\rho^2)\frac{1/(3n')-\gamma_c}{\beta_c-\gamma_c}.$$
Choose $m=\lceil12Qn'\beta_c/\alpha'\rceil+\lceil4/\rho^2\rceil$, so the inequality
forces $1/(3n')-\gamma_c\le1/(12n')$, that is $n'\ge1/(4\gamma_c)=d^{k^*/2}/(8\lambda_{k^*}^2C^{k^*/2}\log_d(m)^{k^*})$.
Suppose $n'<d^{k^*/2}$, or the claim holds. Then $\log_d(m)\le r+k^*/2+\log_d(12\beta_c/\alpha')+\log_d(1+4/\rho^2)+1$,
a constant $\ell(P,c_0,r)$ for $d$ large, and $m\le d^{d^{1/4}}$. So
$\epsilon=\sqrt C\ell/\sqrt d$, which meets $\epsilon\le\rho^2/2$, $\epsilon\le1/2$
and $\lambda_{k^*}^2\ge2\epsilon$ for $d$ large, and $\eta\to0$, so $\alpha'\ge1/2$.
Hence $n'\ge c\,d^{k^*/2}$ with $c=1/(8\lambda_{k^*}^2C^{k^*/2}\ell^{k^*})$. For
$k^*\ge3$, $n_1=\tilde O(d)<c\,d^{k^*/2}$ for $d$ large, so $n'=n$. $\square$

Proof of (b). By `lem-whitening-gives-rotated-records`, $(Tz_i,y_i)=(Rx_i,y_i)$ is a
single-index sample with direction $Ru$, and DPLB24 Theorem 4.1 applies to
$(Rx_i,T_P(y_i))$. The reconstruction error is as in round 01. $\square$

The server's price for the label-relevant coordinate is the generative exponent
of the task, whatever the trainer's model learned. The lower bound measures
detection first (DPLB24 Remark 3.3) and the upper bound is sample-based, so the
two sides are not one SQ price.

Other regime. SQ for (a), sample-based for (b). No oracle.

## Decisions for Halil, proposed

1. First target. The split-learning seed separation in the form of
   `thm-blind-split-seed-separation`, with `conj-seed-price-is-ngca-price` as the
   open general statement and `thm-reconstruction-from-conditional-mean` with
   `prop-sq-label-relevant-reconstruction-bound` as the label side.
2. Attacker class for lower bounds. Two games, never mixed: population SQ
   attackers of frozen clients for unconditional bounds, and polynomial-time
   attackers with the record-level view for bounds conditional on lattice
   hardness. SQ binds SGD-trained attackers only in the coarse-precision regime
   of AKMSS21 Theorem 1c.
3. Whether a separation whose hard instance is a record law (pancakes) meets the
   rule that a cryptographic plug-in does not count. The procedure is standard
   (Gaussian initialization, SGD), the security problem reduces to hCLWE, and no
   primitive is placed in the procedure. The hardness still comes from the data.
   Astra calls it an artificial-distribution reduction. The moment-matched SQ
   part is the non-artificial side, and it needs four matched moments.
