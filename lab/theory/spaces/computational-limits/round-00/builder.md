# Round 00, builder: computational limits, the literature round

Space `computational-limits`, round 00, 2026-10-25. Builder: the Claude session
space-computational. This is the first round, so no challenge is open.

The round states what the literature proves on the space's question, judges the
unverified proof note `FS:.tools/proof.tex`, names the gaps, and proposes three
aims. Every theorem number below was read in the paper on 2026-10-25. Papers
read from the library PDFs: FGRVX17, AKMSS21, LJDD19, BRST21, DPLB24,
CDGJMMSTT21, CGJMMT21, CKMMNST25, EKC22, NRNT25, with pointer checks in BB20 and
HS24. Two papers outside the library were read on the web: DKRS23 through its
arXiv HTML page (statement only, formulas paraphrased by the fetch tool, to be
checked against the PDF) and LKR06 through the authors' PDF (Sections 3 and 4).
The search gate of `sink/formalizing/README.md` was applied first. The rows
`search-learning-lower-bound-attacker`, `search-seed-attacker-resource` and
`search-sq-limits-sgd` cover the general questions. No row covered rotation
perturbation, independent component analysis or non-Gaussian component analysis
as a price of blind inversion, so three web searches and two page reads were run.
Their rows are in `summary.md`.

Notation used throughout. $d$ is the input dimension, $x\in\mathbb R^d$ a client
record, $D$ its law, $W\in\mathbb R^{m\times d}$ the first-layer weight,
$z$ the representation the server receives, $O(d)$ the orthogonal group, and
$\gamma_d=N(0,I_d)$. For $V\in\mathbb R^{d\times r}$ with $V^\top V=I_r$ and a
law $A$ on $\mathbb R^r$, $P^A_V$ is the law of $x$ with $V^\top x\sim A$ and the
projection on $\mathrm{span}(V)^\perp$ standard Gaussian and independent (the
hidden-subspace law of DKRS23, Definition 1.2).

## Literature

### fact-fgrvx17-planted-clique-sq-bound: statistical query bounds for planted biclique
status: borrowed
uses: none

Feldman, Grigorescu, Reyzin, Vempala and Xiao, J. ACM 64(2), 2017, held copy
arXiv 1201.1214v6, key FGRVX17. Problem 1.1 fixes $S\subseteq[n]$, $|S|=k$, and
the law $D_S$ on $\{0,1\}^n$ that is uniform with probability $1-k/n$ and, with
probability $k/n$, sets the coordinates of $S$ to $1$ and the rest uniform. $U$
is uniform on $\{0,1\}^n$. Definition 2.2: STAT($\tau$) returns any value within
$\tau$ of $E_D[h]$ for $h:X\to[-1,1]$. Definition 2.3: VSTAT($t$) returns any
value in $[p-\tau',p+\tau']$ with $p=E_D[h]$ and
$\tau'=\max\{1/t,\sqrt{p(1-p)/t}\}$. Definition 2.4: 1-STAT evaluates a Boolean
$h$ on a fresh sample. Theorem 2.9: for every constant $\delta>0$, every
$k\le n^{1/2-\delta}$ and every $r>0$, solving the distributional planted
$k$-biclique problem with probability $2/3$ needs $n^{\Omega(\log r)}$ queries to
VSTAT($n^2/(rk^2)$), and the same holds for distinguishing any $D_S$ from $U$.
Theorem 5.4 is the randomized decision version. Theorem 2.10: a 1-bit sampling
algorithm that distinguishes $U$ from every $D_S$ with probability $2/3$ needs
$\Omega(n^2/k^2)$ calls to 1-STAT. Theorem 3.2 and Corollary 3.12 bound search
problems through the statistical dimension, the latter from pairwise
correlations (Definitions 3.8 and 3.9). Section 2.4 gives the matching upper
bound: $n$ queries $h_i(x)=x_i$ to VSTAT($16n^2/k^2$), tolerance $k/(4n)$,
recover $S$. Appendix A relates the average-case bipartite problem to the
distributional one with $t=n$ samples, a statement about samples, not about
statistical access to one graph.

Two corrections to the registers (proven by reading). The held copy has no
Theorem 1.1 of the form $q\tau^2\ge\Omega(n^{2\delta})$, which
`fact-fgrvx17-theorem-one-quoted-form` records from the proof note. Every bound
is against an oracle that may answer adversarially within its tolerance, except
Theorem 2.10, which is against the honest 1-STAT.

Other regime. These are query bounds against statistical algorithms with
unbounded computation between queries. They price computation only through
access, so they speak about efficient adversaries only through the heuristic
that natural algorithms are statistical.

### fact-sq-simulates-minibatch-sgd: when statistical queries bind gradient training
status: borrowed
uses: none

Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, held copy arXiv
2108.04190v2, key AKMSS21. A bSGD($T,\rho,b,p,r$) method runs
$w^{(t+1)}=w^{(t)}-\gamma g_t$ where $g_t\in\rho\mathbb Z^p$ and
$\|g_t-\nabla L_{S_t}\|_\infty\le 3\rho/4$ for the clipped gradient on a fresh
batch of $b$ samples (equations 1 to 3). Its error is
$E[\sup L_D(f_{w^{(T)}})]$, the supremum over all valid roundings. An
SQ($k,\tau,r$) method's error is $E_R[\sup L_D(f)]$ over all valid answers.
Theorem 1c: there is a constant $C$ such that for all $\delta>0$ and all
$T,\rho,b,p,r$ with $b\rho^2>C\log(Tp/\delta)$, SQ($Tp,\rho/8,r$) is at least as
powerful as bSGD($T,\rho,b,p,r$) up to $\delta$. Theorem 1a (the register's
`fact-fine-precision-sgd-simulates-pac`): for $\rho<1/(8b)$, bSGD simulates any
PAC($m,r$) method up to $\delta$ with $T'=O(mn/\delta)$.

Reading for this space. An SQ lower bound on an attack task binds an attacker
trained by mini-batch SGD only when $b\rho^2>C\log(Tp/\delta)$, and only in the
worst-case-rounding sense of the error definition (proven, from the
definitions). Training in single precision has an absolute rounding step near
$2^{-24}$ on gradients clipped to $[-1,1]$, so $b\rho^2\ll1$ for any batch in use
and the regime of Theorem 1a holds (heuristic: it identifies the paper's
abstract rounding model with floating-point arithmetic, which rounds relative to
magnitude).

Other regime. Theorem 1a makes fine-precision SGD as strong as any sample-based
learner, so for such attackers only bounds against all polynomial-time
algorithms, or information-theoretic bounds, apply.

### fact-lei-random-expansive-layers-invertible: the seed-known inverter
status: borrowed
uses: none

Lei, Jalal, Dhillon and Dimakis, NeurIPS 2019, held copy arXiv 1906.07437v2,
key LJDD19. Assumption 1: a weight matrix $W\in\mathbb R^{n_i\times n_{i-1}}$
has i.i.d. Gaussian entries and $n_i=c_0n_{i-1}$ with $c_0\ge2.1$. Theorem 3: if
every layer of a ReLU network $G$ satisfies Assumption 1, then for any input
$z^*$ and $x=G(z^*)$, with probability $1-e^{-\Omega(k)}$ over the weights, $z^*$
is recovered by layer-wise linear equations ($k$ the input dimension). Lemma 1
gives injectivity of one layer: at least $k$ coordinates are positive with
probability $1-\exp(-\Omega(k))$, and any $k$ Gaussian rows are invertible.
Theorems 1 and 2: deciding whether a preimage exists is NP-complete for
constructed two-layer (binary input) and four-layer (real input) networks. The
probability is over $W$ for each fixed input, so $N$ records cost a union bound
$Ne^{-\Omega(k)}$.

Other regime. The result needs the weights. It is the seed-known side of any
seed separation and says nothing about an attacker without $W$.

### fact-clwe-hardness: homogeneous CLWE is a hard hidden-direction law
status: borrowed
uses: none

Bruna, Regev, Song and Tang, STOC 2021, held copy arXiv v2, key BRST21.
Definition 2.19: $H_{w,\beta,\gamma}$ on $\mathbb R^n$ has density proportional
to $\rho(y)\sum_{k\in\mathbb Z}\rho_\beta(k-\gamma\langle y,w\rangle)$, a mixture of
Gaussian layers of width $\beta/\sqrt{\beta^2+\gamma^2}$ and spacing
$\gamma/(\beta^2+\gamma^2)$ along $w$, standard Gaussian on $w^\perp$. It is
$P^A_w$ for a one-dimensional pancake law $A$. Definition 2.21: hCLWE is to tell
$H_{w,\beta,\gamma}$ for a uniformly random unit $w$ from $\gamma_n$. Corollary
4.2: for $\beta\in(0,1)$, $\gamma\ge2\sqrt n$ and $\gamma/\beta$ polynomially
bounded there is a polynomial-time quantum reduction from
DGS$_{2\sqrt{2n}\eta_\varepsilon(L)/\beta}$ to hCLWE. Claim 2.22 turns a
worst-case direction into a uniform one by a random rotation, the same symmetry
the aims below use. Theorem 7.5: for $\gamma=n^\varepsilon$, $\varepsilon<1/2$,
hCLWE is solved in time $\exp(O(n^{2\varepsilon}))$. Corollary 9.4 extends the
hardness to hidden subspaces of dimension $m$ with $n-m=\Omega(n^c)$.

Other regime. The hardness is computational. Statistically, $H_{w,\beta,\gamma}$
and $\gamma_n$ are far apart in total variation for small $\beta$, so an
unbounded algorithm finds $w$.

### fact-hclwe-sq-correlation-bound: pairwise correlations of pancake laws
status: borrowed
uses: fact-fgrvx17-planted-clique-sq-bound

BRST21, Proposition 8.3: for unit $v,w$, $\gamma\ge1$, $\beta\in(0,1)$ and any
$\alpha\ge0$ with $\gamma^2(1-\alpha^2)\ge1$,
$|\chi_{\gamma_n}(H_v,H_w)|\le2(\gamma/\beta)^2$ if $v=w$ and
$\le8\exp(-\pi\gamma^2(1-\alpha^2))$ if $|\langle v,w\rangle|\le\alpha$.
Theorem 8.1: for $\gamma\ge2$, a randomized SQ algorithm with tolerance
$\tau\ge4\exp(-\pi\gamma^2/4)$ that solves hCLWE with probability $\eta>1/2$
needs at least $(2\eta-1)\exp(cn)\tau^2\beta^2/(4\gamma^2)$ queries, through
Lemma 8.2 (FGRVX17 Lemma 3.10).

Other regime. Unconditional for SQ, consistent with the lattice-based hardness
of the previous object.

### fact-ngca-sq-lower-bound: non-Gaussian component analysis is SQ-hard under moment matching
status: borrowed
uses: none

Diakonikolas, Kane, Ren and Sun, NeurIPS 2023, arXiv 2403.04744, key DKRS23,
read from the arXiv HTML page on 2026-10-25 and not placed in the library.
Definition 1.3: NGCA testing tells $\gamma_n$ from $P^A_V$ for a uniformly random
$V\in\mathbb R^{n\times m}$ with orthonormal columns. Theorem 1.5: let
$\lambda\in(0,1)$, $d$ even, $m,d\le n^\lambda/\log n$, $0<\nu<2$,
$0<c<(1-\lambda)/4$ and $n$ large. If
$|E_A f-E_{\gamma_m}f|\le\nu$ for every polynomial $f$ of degree at most $d$ with
$E_{\gamma_m}f^2=1$, then any SQ algorithm that solves NGCA testing with
probability $2/3$ needs a query of tolerance
$O_{m,d}(n^{-((1-\lambda)/4-c)d})+(1+o(1))\nu$ or $2^{n^{\Omega(c)}}$ queries.
No chi-square condition on $A$ is needed, which the paper names as the
difference from the earlier result of Diakonikolas, Kane and Stewart. The
symbols here follow the paper ($n$ ambient dimension, $d$ moment degree). The
statement was paraphrased by the fetch tool from rendered formulas and must be
checked against the PDF before any proof rests on its constants.

Other regime. Statistically $P^A_V$ is identifiable with $O(n)$ samples for
most $A$, so this is a statistical-computational gap in the SQ model.

### fact-generative-exponent-sq-recovery-bound: the price of finding a label-relevant direction
status: borrowed
uses: fact-fgrvx17-planted-clique-sq-bound

Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, key DPLB24. Definition 1.1:
in a Gaussian single-index model $x\sim\gamma_d$ and
$(\langle w^*,x\rangle,y)\sim P$, with first marginal $\gamma_1$, finite
$E[Y^2]$ and $P$ not a product. Definition 2.4: the generative exponent is
$k^*(P)=\min\{k\ge1:\lambda_k\ne0\}$, $\lambda_k=\|\zeta_k\|_{P_y}$,
$\zeta_k(y)=E[h_k(Z)\mid Y=y]$ with normalized Hermite $h_k$. Theorem 3.2: with
$q=d^r$ queries, $r\le d^{1/4}$ and $\lambda_{k^*}^2\ge rd^{-1/2}$, returning
$\hat w$ with $|\hat w\cdot w^*|\ge\tilde\omega(d^{-1/2})$ from VSTAT($n$)
needs $n\ge c_{k^*}\lambda_{k^*}^{-2}(d/r^2)^{k^*/2}$. Remark 3.3: the proof
compares with the null $\gamma_d\otimes P_y$, so it measures detection first.
Theorem 4.1: a partial-trace algorithm with
$n\ge C_k[d^{k/2}/\tilde\lambda_k^2+d/(\tilde\lambda_k^2\epsilon^2)]$ returns
$\hat w$ with $(\hat w\cdot w^*)^2\ge1-\epsilon^2$ with probability
$1-2e^{-d^c}$. Proposition 3.7: an SQ algorithm for NGCA with a planted law of
exponent $k$, built by rejection on $\{\zeta_k>0\}$, solves the single-index
model of generative exponent $k$.

Other regime. Theorem 6.1 of the paper gives an information-theoretic $O(d)$
upper bound, so the gap is computational.

### fact-ica-breaks-rotation-perturbation: blind rotation is undone for non-Gaussian data
status: borrowed
uses: none

Liu, Kargupta and Ryan, Random Projection-Based Multiplicative Data
Perturbation for Privacy Preserving Distributed Data Mining, IEEE TKDE 18(1),
2006, pp. 92 to 106, key LKR06. Sections 3 and 4 argue that a perturbation
$u=Rx$ with $R$ a random orthogonal matrix is undone up to permutation and
scaling by independent component analysis when the attributes are independent
and non-Gaussian and $R$ has full column rank, and that Gaussian sources cannot
be separated. Their remedy is a projection to fewer dimensions. The argument is
heuristic and empirical, with an identifiability theorem quoted from Cao et al.
No complexity bound is given.

Other regime. This is the attack side, priced nowhere. It shows that the
qualitative statement "the seed protects only nearly Gaussian data" is known,
and that the open part is its price.

### fact-instance-encoding-privacy-learnability: privacy of encodings reduces to learnability
status: borrowed
uses: none

Carlini, Deng, Garg, Jha, Mahloujifar, Mahmoody, Song, Thakurta and Tramèr,
IEEE S&P 2021, key CDGJMMSTT21. Definition 1 (decomposable, $r$-local dataset
encodings), Definition 3 (accuracy on encoded instances), Definition 5 (instance
distinguishing game), Definition 6 (instance recovering). Theorem 3: plain
accuracy $0.51$ on two balanced concepts gives a dataset-distinguishing attack
of advantage at least $(0.99-2\delta(n))/(3n)$ in about the learner's time.
Theorem 4: an $(m,\gamma)$-rich class and encoded accuracy give an instance
distinguishing attack of advantage $0.99-\epsilon(n)/\gamma$ that has oracle
access to the encoder $E(\cdot)$, the learner, the concepts and a sampler for $D$.
Theorem 5: for one balanced concept, either an efficient distinguishing attack
of advantage $1/2-\epsilon(m)-\tau$ exists or an efficient learner of accuracy
$1-\tau$ does. Section 2 states that the results do not rule out privacy
against instance-recovering attacks.

Other regime. The attacks of Theorems 4 and 5 query the encoder on chosen
inputs. In split learning that is the seed-known or chosen-input attacker. The
blind server of the aims below has no such oracle.

### fact-ideal-keyed-encoding-weak-learner: an ideal keyed encoding hands over the concept
status: borrowed
uses: none

Carlini, Garg, Jha, Mahloujifar, Mahmoody and Tramèr, arXiv 2108.07256, key
CGJMMT21. Definition 2 (weakly ideal encoder: equal encodings for equal labels,
labels preserved). Theorem 1: a learner of balanced error $1/2-\varepsilon$ over
the encoded law gives an oracle-aided PPT predictor of risk at most $\tau$ from
two labelled examples, in time poly$(m,1/\epsilon,1/\delta,1/\tau)$.

Other regime. A statement about efficient extraction given the encoder as an
oracle. It does not price an attacker without that oracle.

### fact-cohen-narcissus-equals-one-wayness: reconstruction security against the narcissus baseline
status: borrowed
uses: none

Cohen, Kaplan, Mansour, Moran, Nissim, Stemmer and Tsfadia, ITCS 2025, arXiv
2405.15753, key CKMMNST25. Definition 1.6: $M$ is $(\varepsilon,\delta,\mathcal F)$-
$R$-Narcissus-resilient if for all $D\in\mathcal F$ and all attackers $A$,
$\Pr[R(S,z)=1]\le e^\varepsilon\Pr[R(T,z)=1]+\delta$ with $S,T\sim D$
independent, $y\leftarrow M(S)$, $z\leftarrow A(y)$. Definition C.1 is the
computational version against polynomial-time attackers. Definition C.4: $f$ is
well-spread if every output has negligible probability. Theorem C.5: for an
efficiently computable well-spread $f$ and $R(x,x')=1$ iff $f(x)=f(x')$, $f$ is
one-way iff $M_f$ is computationally Narcissus-resilient for $(U_\lambda,U_\lambda)$.

Other regime. The relation of Theorem C.5 is equality of images, which is
preimage finding. A reconstruction relation, closeness to the record, is a
different relation, and the theorem says nothing about it.

### fact-unsplit-unknown-client-inversion: blind inversion works on images
status: borrowed
uses: none

Erdoğan, Küpçü and Çiçek, UnSplit, WPES 2022, key EKC22. The attacker knows the
client architecture only and alternates gradient steps on a guessed input and
guessed client weights (equations 2 and 3, a total-variation prior, Adam at
learning rate $10^{-3}$). Table 2 reports input MSE before and after client
training for split depths 1 to 6 on MNIST, Fashion-MNIST and CIFAR10, for
example $0.070$ and $0.048$ at depth 1 on MNIST, with convolutional clients
(Figures 2 and 3). Empirical.

Other regime. Image data are far from Gaussian at low degree, so the aims below
predict this success. The client is convolutional, outside the symmetry the aims
use.

### fact-nrnt25-private-layer-hardness-route: reconstruction hardness argued for one attack route
status: borrowed
uses: none

Nguyen, Ren, Nie and Trieu, PoPETs 2025(3), key NRNT25. Definition 1.1:
$(\epsilon,\delta)$-reconstruction hardness asks that no algorithm of polynomial
data and time complexity output $\hat X_t$ within distance $\epsilon$ with
probability $1-\delta$. Proposition 3: with a public discriminator and its
gradients, the record is recovered exactly. Section 4.4: with the first $M$
discriminator layers private, hardness is argued for an attack that first
approximates the private layers and then inverts, citing approximation hardness
of learning ReLU networks (Proposition 5, from learning with rounding,
Proposition 6, SQ bounds for random deep networks). My reading: the argument
covers that attack route, not every polynomial-time attacker, since no
reduction from an arbitrary reconstructor to the cited learning problems is
given.

Other regime. The cited hardness results are computational. The paper gives no
statistical counterpart.

## The judgement of FS:.tools/proof.tex

The note of 2026-04-23 claims an SQ-hardness reduction for black-box attacks on
SQ-implementable learners. Verdict: its main theorem is false as stated, its
proof applies FGRVX17 to an access model that paper does not treat, and the part
that survives is a one-line post-processing fact about the learner, not about
the attacker.

### thm-fs-sq-black-box-reduction: the proof note's main theorem
status: refuted as stated (counterexample proven below)
uses: fact-fgrvx17-planted-clique-sq-bound

Statement (theirs, Theorem 2 of the note). $G$ is drawn from $G(n,1/2)$ or from
$G(n,1/2)$ with a planted $k$-clique. The vertex-row encoding $D_G$ draws
$v\in[n]$ uniformly and outputs the adjacency row $G[v,\cdot]$ with a label
computed from it. A deterministic learner $L$ asks $q_L$ statistical queries of
tolerance $\tau_L$ to $D_G$, and a black-box adversary $A$ queries the model.
The note claims $\mathrm{Adv}(A)\le\mathrm{Adv}_{SQ}(n,k,q_L,\tau_L)$, and in
particular that for $q_L=\mathrm{poly}(n)$ at constant tolerance no black-box
adversary has constant advantage, whatever its own query count.

Counterexample (proven). Take $\tau_L=1/3$ and the exact oracle, which returns
the vertex average itself and is a valid STAT($\tau$) oracle for every $\tau$.
The same works with an honest oracle that averages each query over
$B=\lceil32n^2\ln n\rceil$ fresh draws from $D_G$: by Hoeffding every answer is
within $1/(4n)$ of the vertex average with probability $1-2n^{-4}$, and rounding
to a multiple of $1/n$ makes it exact for all $O(n^2)$ queries with probability
$1-O(n^{-2})$. Let $T=[\ell]$ with $\ell=\lceil3\log_2n\rceil$.

1. The learner builds the trie of row prefixes on $T$. For each length
   $j\le\ell$ and each surviving prefix $b$ it asks
   $f_b(x)=\mathbf 1[x_{1..j}=b]$, whose exact answer is the number of rows with
   that prefix over $n$. This takes at most $2n\ell$ queries.
2. For each full prefix $p$ and each column $c\in[n]$ it asks
   $g_{p,c}(x)=x_c\mathbf 1[x_T=p]$. If every prefix has count one, the answers
   are the rows themselves. The model $M$ stores the multiset of rows as a
   lookup function. In all $q_L\le2n\ell+n^2$ queries, every answer in $[0,1]$.
3. Distinct prefixes. Under the null, two rows $u\ne v$ agree on $T$ only if
   $G[u,j]=G[v,j]$ for every $j\in T\setminus\{u,v\}$, independent fair bits, so
   with probability at most $2^{2-\ell}$. A union bound over pairs gives failure
   at most $4/n$. Under the planted law the same holds on the event
   $T\cap S=\emptyset$, of probability at least $1-\ell k/n$, since then no edge
   with an endpoint in $T$ is planted.
4. The adversary reads the multiset of rows from $M$ and outputs $1$ iff some
   $C\subseteq[n]$ with $|C|=k$ has, for every $c\in C$, a row $r$ with
   $r_C=\mathbf 1_C-e_c$. Under the planted law $C=S$ passes, because a clique
   vertex's row is $1$ on $S$ except at itself (no loops). Under the null, a
   passing $C$ needs $k$ distinct rows (the patterns differ) whose $k\times k$
   restriction contains at least $(k^2-k)/2$ distinct edges with prescribed
   values. A union bound over $C$ and the row assignment gives probability at
   most $n^{2k}2^{-(k^2-k)/2}$, which tends to $0$ for $k>4\log_2n+1$.

So $\mathrm{Adv}(A)\ge1-o(1)$ at $k=n^{1/2-\delta}$, with $q_L=O(n^2)$ queries of
constant tolerance. The particular clause is false. The inequality is false for
every reading of $\mathrm{Adv}_{SQ}$ that is $o(1)$ at $q=O(n^2)$ and
$\tau=1/3$, which is the reading the note needs, and it is vacuous under the
only other reading, the best case over oracles.

Where the argument fails, with the remaining defects.

- Step 4 applies FGRVX17 to "vertex-SQ access to $G$", the empirical law of the
  $n$ rows of one symmetric matrix. FGRVX17 bounds statistical access to $D_S$,
  a law of independent rows, and its Appendix A concerns $n$ samples, not
  statistical access to them.
- Step 3 equates the two advantages for each fixed oracle, while the SQ lower
  bound holds for the worst oracle only. The two cannot be chained, and a real
  learner meets one particular oracle.
- The quoted form $\mathrm{Adv}_{SQ}\le O(q\tau^2n/k^2)$ grows with $\tau$,
  backwards, since a coarser tolerance cannot help. The calibration remark
  inherits the inversion. In the distributional problem at $n=10^4$ and
  $k=n^{0.4}\approx40$, tolerance $k/(4n)\approx9.95\cdot10^{-4}$ recovers $S$
  with $n$ queries (FGRVX17 Section 2.4), while the remark calls
  $\tau_L\in[10^{-5},10^{-3}]$ a regime of meaningful security.
- The remark that white-box adversaries escape the proof is wrong. Step 2(3)
  hands $B$ the whole model, so the argument, where valid, covers white-box and
  unbounded adversaries alike.
- The membership corollary is ill-posed, since every row is in $D_G$ by
  construction. The extraction corollary's
  $I(G;M)\le q_L\log(1/\tau_L)$ needs answers discretized to $\log(1/\tau_L)$
  bits, and exact answers break it.
- The abstract says "under the planted-clique conjecture", but the argument
  would be unconditional, and the Hirahara and Shimizu equivalences (HS24
  Theorem 1.3) play no role in it.
- The Brennan and Bresler pointer: BB20 carries its SQ bounds for the secret
  leakage variant in Section 12.3 (Corollaries 12.17 and 12.18, for specific
  leakage laws), not in a Theorem 5.1.

Other regime. The counterexample's adversary is unbounded. A polynomial-time
adversary on the same model would face the planted clique conjecture after
reading the graph, which is the only place computation enters, and the note
does not use it.

### lem-sq-learner-post-processing: what survives of the proof note
status: proven
uses: fact-fgrvx17-planted-clique-sq-bound, fact-sq-simulates-minibatch-sgd

Statement. Let $k\le n^{1/2-\delta}$ for a constant $\delta>0$. Let $L$ be a
learner whose only access to its training law $P\in\{U\}\cup\{D_S:|S|=k\}$ is
$m$ calls to 1-STAT, with internal coins independent of $P$. Let $A$ be any
randomized map from the output of $L$, weights included, to $\{0,1\}$, with no
bound on its computation. If $A\circ L$ outputs $0$ on $U$ and $1$ on every
$D_S$, each with probability at least $2/3$, then $m=\Omega(n^2/k^2)$. If
instead $L$ asks $q$ queries to VSTAT($n^2/(rk^2)$) and success is required
against every valid oracle, FGRVX17 Theorem 5.4 bounds $A\circ L$ with the same
parameters.

Proof. The queries of $A\circ L$ are those of $L$, chosen from earlier answers
and from coins independent of $P$, and $A$ makes no further call. So $A\circ L$
is a 1-bit sampling algorithm with $m$ calls, or an SQ algorithm with the same
$q$ queries, and FGRVX17 Theorem 2.10, or Theorem 5.4, applies. By AKMSS21
Theorem 1c a bSGD learner with $b\rho^2>C\log(Tp/\delta)$ is simulated by an SQ
method with $Tp$ queries of tolerance $\rho/8$, so the VSTAT clause covers it in
the worst-case-rounding sense. $\square$

The content is that a learner which cannot detect the planted structure cannot
hand it to anyone. The bound is priced in the trainer's units (its fresh
samples) and holds against unbounded white-box attackers, so it is a statistical
statement about the trainer, and it is non-trivial under Halil's constraints
only as a pricing convention. The VSTAT clause speaks about some valid answer
sequence, not about the run that happened. A mini-batch SGD learner that reuses
samples or reads real-valued per-sample gradients is not a 1-bit sampling
algorithm, so the honest clause does not cover it.

Other regime. No oracle is used. The lemma belongs with the statistical space,
which owns unbounded attackers, and is recorded here because it fixes the
attacker-class question: an SQ bound on the learner binds every attacker, an SQ
bound on the attacker binds only SQ attackers.

## Gaps

1. No paper reduces a known hard learning problem to a reconstruction attack on
   a network for every attacker of a stated class
   (`fact-no-hard-learning-attacker-lower-bound`, empirical, search-based). The
   nearest are a hardness argument for one attack route (NRNT25), distinguishing
   attacks that need the encoder as an oracle (CDGJMMSTT21 Theorems 4 and 5,
   CGJMMT21 Theorem 1), and definitions with an equivalence to one-wayness for
   the preimage relation (CKMMNST25 Theorem C.5).
2. The seed. Blind rotation is undone by ICA for non-Gaussian data (LKR06,
   heuristic), blind inversion works on images (EKC22, empirical), and the
   known initialization helps reconstruction (Balle, Cherubin and Hayes,
   `fact-balle-known-initialization-reconstruction`, empirical). The price of
   the seed is stated nowhere.
3. SQ against SGD. An SQ bound binds an SGD attacker only in the coarse
   precision regime of AKMSS21 Theorem 1c, with worst-case rounding. The only
   honest oracle with a planted-structure bound is 1-STAT. A result for real
   attackers needs a polynomial-time reduction, with SQ as unconditional
   evidence beside it.
4. Regression targets (`prob-statistical-queries-for-regression`). Search
   bounds from pairwise correlations (FGRVX17 Corollary 3.12, BRST21
   Proposition 8.3) cover weak recovery of a direction. A reconstruction measured
   by correlation should transfer to them with $O(d)$ extra queries. That
   transfer is a round-01 target.
5. One-wayness. CKMMNST25 Theorem C.5 needs the preimage relation. The candidate
   below has reconstruction hardness borrowed from the data law, and its view
   map has easy preimages (any basis of the observed span gives one, for a
   linear first layer, proven by construction). So aim (c) of the brief has no
   candidate in this round, and the question is recorded for the registers.

## Aims

The three aims make Halil's reconstruction example formal in the split-learning
setting. The reconstructor is a learner from representations to records. Its
learning problem, after a symmetry argument, is non-Gaussian component analysis
on the record law when the server has no labels, and it is the trainer's own
single-index problem for the label-relevant part. Both are known families with
known thresholds.

### def-seed-blind-reconstruction-game: the reconstruction game with and without the seed
status: proposed
uses: fact-cohen-narcissus-equals-one-wayness

Statement. A client holds $x_1,\dots,x_N$ i.i.d. from a law $D$ on
$\mathbb R^d$ that the attacker knows. The client network computes
$z=\psi_\theta(Wx+b)$, $W\in\mathbb R^{m\times d}$. The initialization
$(W_0,b_0,\theta_0)$ satisfies $(W_0Q,b_0,\theta_0)\overset d=(W_0,b_0,\theta_0)$
for every $Q\in O(d)$ (right rotation invariance, true for i.i.d. Gaussian
entries independent of the rest). Training is split learning with update rule
$\mathcal T$. The server's view $\mathcal V$ is every representation it
receives, every gradient it returns, its own parameters and the labels it holds.
A target is a map $g:\mathbb R^d\to\mathbb R^s$. The seed-blind attacker sees
$\mathcal V$. The seed-known attacker also sees $(W_0,b_0,\theta_0)$ and the coins
of $\mathcal T$. The attacker names an index $i$ and outputs $t$. Fine success at
scale $\epsilon$ is
$\Pr[\|t-g(x_i)\|\le\epsilon]-\Pr[\|t-g(x')\|\le\epsilon]$ for an independent
$x'\sim D$, the narcissus baseline of CKMMNST25 Definition 1.6 with
$\varepsilon=0$. Weak success is the correlation
$E\langle t,g(x_i)\rangle/(\|t\|_{L^2}\|g(x_i)\|_{L^2})$ of a reconstruction map
applied to every record. The price of the seed at success $s$ is the ratio of
the resources (samples, time, statistical queries, training runs) that the best
seed-blind and the best seed-known attacker need to reach $s$.

What would settle it. The definition is well posed once the update rule and the
view are fixed. It is useful if aims 2 and 3 can be proved in it and if it
separates the two attackers on some natural law.

Regime. Both. Against unbounded attackers the price is the statistical one,
owned by `statistical-limits`. Against SQ or polynomial-time attackers it is
this space's object.

Experiment. Every term is measurable: run split training, record the view, run
blind and seed-known attackers, and estimate both success terms by Monte Carlo
over $(x_i,x')$.

Without the oracle. The game needs no learning oracle. Honest training runs
produce the view.

### conj-seed-price-is-ngca-price: the seed is worth the NGCA price of the data law
status: open
uses: def-seed-blind-reconstruction-game, fact-ngca-sq-lower-bound, fact-clwe-hardness, fact-hclwe-sq-correlation-bound, fact-lei-random-expansive-layers-invertible

Statement. Assume right rotation invariance of the initialization and an
equivariant update for $W$: $\mathcal U(WQ,GQ,sQ)=\mathcal U(W,G,s)Q$ for every
$Q\in O(d)$, where $G$ is the gradient in $W$ and $s$ its optimizer state. SGD,
momentum, Frobenius weight decay and global-norm clipping satisfy it. Adam,
RMSProp, sign updates, coordinate clipping, $\ell_1$ penalties and any operation
on $x$ inside the protocol do not. Let $D=P^A_V$ with $A$ on $\mathbb R^r$ of
mean $0$ and covariance $I_r$, $r=O(1)$, and target $g(x)=V^\top x$.

(a) Simulation. For every fixed $Q\in O(d)$, running the protocol on
$(Qx_i)$ from a fresh initialization gives a view whose joint law with $(x_i)$
equals that of the real view with $(x_i)$. Hence every seed-blind attacker gives
an algorithm that, from samples of $P^A_{QV}$ with $Q$ Haar, recovers the
hidden-frame coordinates $(QV)^\top u_i$ with the same success, at the cost of
one training run.

(b) SQ price, frozen client. If $A$ matches Gaussian moments up to degree $k$
in the sense of DKRS23 Theorem 1.5, with $k$ above a constant that depends on
$\lambda$ and $c$ there, every SQ seed-blind attacker of weak success
$c_0=\Omega(1)$ needs $2^{d^{\Omega(1)}}$ queries or tolerance $d^{-\Omega(k)}$,
while the seed-known attacker recovers each $x_i$ exactly in polynomial time
(a linear solve, or LJDD19 Theorem 3 for expansive Gaussian ReLU layers).

(c) Polynomial-time price. For $r=1$ and $A$ the pancake law of
$H_{e_1,\beta,\gamma}$ with $\gamma\ge2\sqrt d$ and $\gamma/\beta$ polynomial, no
polynomial-time seed-blind attacker reconstructs $\langle v,x_i\rangle$ for all
records to accuracy $c_1/\gamma$, for a constant $c_1$, unless hCLWE is easy,
hence unless the lattice problems of BRST21 Corollary 4.2 are quantum-easy.

(d) Upper bound, linear first layer. A seed-blind attacker whitens the view,
obtains $u_i=Rx_i$ with $R$ Haar, and runs any NGCA algorithm. It reconstructs
$V^\top x_i$ up to the symmetry group of $A$ at the cost of that algorithm plus
poly$(d)$.

Sketch. (a) For the first layer, $(WQ^\top)(Qx)=Wx$, the back-propagated
signal is unchanged, and the gradient becomes $GQ^\top$, so the equivariant
update keeps the trajectory of every other quantity identical. Since
$W_0Q^\top\overset d=W_0$ and is independent of $(Q,x)$, the claim follows
(proven in outline, written in full in round 01). (b) For a frozen client the
view is i.i.d. $z_i=\psi(Wx_i+b)$, so a query $f(z)$ becomes the fixed query
$f\circ\psi(W'\cdot+b')$ on $u$ for a simulated $W'$. A reconstruction map $R$
of weak success $c_0$ gives $\hat w=E[R(z)u]$ with
$\langle\hat w/\|\hat w\|,v\rangle\ge c_0$ from $d$ queries of tolerance
$c_0/(2B\sqrt d)$ for a bound $B$ on $|R|$. A single query of the first
non-matching Hermite degree $k'$ along $\hat w$ then separates $P^A_v$ from
$\gamma_d$, because $E[h_{k'}(c a+\sqrt{1-c^2}g)]=c^{k'}E_A[h_{k'}]$ for
independent $a\sim A$, $g\sim\gamma_1$. This is an NGCA test with tolerance
$\max(d^{-1/2},c_0^{k'})$ up to constants, against DKRS23 (heuristic until the
truncation of $h_{k'}$ and the constants are checked). (c) From fine
reconstructions, least squares gives $\hat w$ with
$\|\hat w-w\|\le\epsilon(1+o(1))$, and a periodic statistic
$\cos(2\pi\gamma'\langle\hat w,u\rangle)$ on fresh samples separates the pancake
law from $\gamma_d$ once $\epsilon\gamma'$ is a small constant (heuristic until
round 01). (d) Whitening and Haar invariance of $R$ by right equivariance
(proven in outline).

What would settle it. Proofs of (a) to (d) with explicit constants. A
refutation would be a moment-matched law with a polynomial-time blind attack,
or a widely used optimizer satisfying the stated equivariance on which the
simulation fails.

Regime. Computational, unconditional for SQ and conditional on worst-case
lattice hardness for polynomial time. For $A$ Gaussian the record is hidden even
from unbounded blind attackers except for its Gram structure, a statistical
statement for `statistical-limits`.

Experiment. Synthetic $x=(a,g)$ with $a\sim A_k$ matching Gaussian moments to
degree $k$ (a centred skewed law for $k=2$, Rademacher for $k=3$, pancakes for
large effective $k$), a Gaussian first layer, linear and ReLU, SGD on a task that
depends on $g$ only. Blind attacks: FastICA, cumulant-tensor methods, an
UnSplit-style joint optimization, a pseudo-client fitted to public samples of $D$.
Seed-known attack: the linear solve or LP inversion. Measure weak and fine
success against $N/d^{k/2}$. On MNIST, estimate the first non-vanishing whitened
Hermite moment along ICA directions to predict that the seed buys nothing. A
CPU run per point at $d\le200$.

Without the oracle. The simulation replaces the oracle by one honest training
run on rotated data, so the price of approximating the oracle is one run.

### conj-reconstruction-at-training-cost: the label-relevant part costs what training costs
status: open
uses: def-seed-blind-reconstruction-game, fact-generative-exponent-sq-recovery-bound, fact-instance-encoding-privacy-learnability

Statement. Let the first layer be linear or bijective (LeakyReLU), $x\sim\gamma_d$,
labels $y=h(\langle u,x\rangle,\xi)$ with $(\langle u,x\rangle,y)\sim P$ of
generative exponent $k^*$, and let the server hold the labels. Then:

(a) If the trained predictor $F$ has excess square risk $\varepsilon$ and the
link has information exponent $1$ with first Hermite coefficient $\beta_1$, the
server computes from its view and $O(d/\varepsilon)$ of its own representations a
unit $\hat u$, in whitened coordinates, with
$E(\langle\hat u,Rx\rangle-\langle u,x\rangle)^2\le4\varepsilon/\beta_1^2$ for
$\sqrt\varepsilon<\beta_1/2$, up to the sign when the sign of $\beta_1$ is
unknown.

(b) In general, seed-blind reconstruction of $\langle u,x_i\rangle$ up to the
symmetries of the link is equivalent, up to poly$(d)$, to learning the task. The
reconstructor's learning problem and the trainer's are one single-index problem
after whitening, so both are priced by $k^*$: SQ needs
$N\gtrsim d^{k^*/2}$ (DPLB24 Theorem 3.2) and the partial-trace algorithm
succeeds there (DPLB24 Theorem 4.1).

With aim 2 this gives a three-part account of what a blind server recovers:
label-relevant coordinates at the trainer's price, label-irrelevant
non-Gaussian coordinates at the NGCA price, Gaussian label-irrelevant
coordinates not at all.

Sketch. (a) By Stein's identity $E[F^*(x)x]=\beta_1u$ for the Bayes predictor
$F^*$, and $\|E[(F-F^*)x]\|\le\sqrt\varepsilon$ by Cauchy-Schwarz with
$E[xx^\top]=I$, so $\hat u=E[F(x)x]/\|E[F(x)x]\|$ meets the bound. The server
evaluates $E[f_{top}(z)Tz]$ with its whitening $T$ (proven in outline, the
sample complexity remains). (b) Learning from reconstruction: regress $y$ on
$\langle\hat u,Rx\rangle$, a one-dimensional problem. Reconstruction from
learning: (a) for information exponent $1$, the Hermite tensor of order $k^*$
of the predictor in general (heuristic).

What would settle it. A proof of (a) with the sample complexity, a proof of (b)
for even links ($k^*=2$, top eigenvector of $E[F(xx^\top-I)]$), and a statement
for ReLU first layers through the recovery of $WW^\top$ from truncated
moments. A refutation would be a learner of small excess risk whose top model
reveals nothing usable about $u$.

Regime. Computational for the cost, statistical for the information. This is
the upper bound on attack cost in Halil's example: the attacker's success is
bounded below by the model's performance. CDGJMMSTT21 Theorems 4 and 5 give a
distinguishing analogue that queries the encoder. This aim needs no encoder
oracle and prices reconstruction.

Experiment. Split training with a Gaussian linear or LeakyReLU first layer on a
single-index task with links of exponent 1, 2 and 3, and a recorded excess
risk. Reconstruct $\langle u,x_i\rangle$ from the top model and the view, and plot
reconstruction error against excess risk and against $N/d^{k^*/2}$. CPU scale.

Without the oracle. No oracle is needed. One training run produces the model.

## Decisions for Halil, proposed

1. First target. `conj-seed-price-is-ngca-price` with
   `conj-reconstruction-at-training-cost` beside it. Together they are
   `prob-split-learning-seed-separation` with the seed priced by the record
   law's moment-matching degree, and they answer
   `prob-split-transcript-leaks-seed` for rotation-equivariant training: the
   transcript is simulable from rotated records, so it leaks nothing beyond
   them.
2. Attacker class for lower bounds. Reductions that turn any attacker into an
   NGCA solver, instantiated twice: SQ (unconditional, DKRS23, frozen clients)
   and polynomial time (lattice, pancake records, fine reconstruction). SQ binds
   SGD attackers only in the coarse precision regime of AKMSS21 Theorem 1c,
   which a lower bound must state.
