# Round 00, builder: hard-problem mappings, the literature round

Space `hard-problem-mappings`, round 00, 2026-10-25. Builder: the Claude session
space-mappings. This is the first round, so no challenge is open.

The round states the mappings that the literature and the first milestone
already give, corrects one of them, names the gaps, and proposes three aims.
Every theorem number below was read in the paper on 2026-10-25, from the library
PDFs: JCBKP20 (Sections 3.2 to 3.4, Appendix A), DGKP20 (Sections 2 to 4, held
copy arXiv 1904.03866v1), GKVZ22 (Sections 2.2, 3.2, 4.1, 6, Appendix A, held
copy arXiv 2204.06974v2), BRV26 (held copy, the anonymous ICLR 2026 submission:
Section 1, Definitions 4 to 6, Assumptions 1 and 2, Theorems 2, 5, 6 and 7,
Corollary 3), CHLX25 (Sections 3 to 5), CKMMNST25 (Appendix C), CDGJMMSTT21
(Sections 2 and 3) and DPLB24 (Definition 1.1, Section 2, Sections 3.1 and 3.2,
Theorems 4.1 and 5.2, Appendices B and E.2). The search gate of
`sink/formalizing/README.md` was applied first. Rows
`search-extraction-games-occupied`, `search-extraction-query-lower-bound`,
`search-sq-lower-bound-backdoor-poisoning`, `search-crypto-hardness-membership-inference`
and `search-unlearning-verification-hardness` answer the general questions. No
row covered extraction priced by a learning exponent, backdoor detection as
non-Gaussian component analysis, or the regime of the sparse-PCA backdoor, so
three web searches were run. Their rows are in `summary.md`.

Notation. $d$ is the input dimension, $\gamma_d=N(0,I_d)$, $\phi$ the standard
normal density, $h_k$ the normalized Hermite polynomials
($E_{\gamma_1}[h_jh_k]=\delta_{jk}$). For a unit $v$ and a law $A$ on
$\mathbb R$, $P^A_v$ is the law of $g\in\mathbb R^d$ with $\langle v,g\rangle\sim A$
and the projection of $g$ on $v^\perp$ standard Gaussian and independent (the
hidden-direction law of DKRS23, Definition 1.2, with $r=1$). $\Pi\lhd\mathcal T$
says that an attacker for the task $\mathcal T$ yields a solver for the hard
problem $\Pi$ (hardness transfers to the attack, a lower bound on its price).
$\mathcal T\lhd\Pi$ says the converse (an upper bound). The *carrier* of a
mapping is where the hard instance enters the game: the record law, the honest
randomness of the procedure, the choice of a trainer who is the adversary, or a
primitive the designer places in the procedure. These words are defined in
`def-hard-problem-mapping` below and keep one meaning in this space.

## Part 1. The mappings the first milestone gives

These objects stand as the booklet states them. The table only reads each one as a
mapping. "Trainer's price" is what the procedure spends at the instance.

| slug | procedure | attack task | hard problem | direction | trainer's price | attacker's price | regime | carrier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `thm-blind-split-seed-separation` with `prop-sq-blind-reconstruction-bound` and `prop-fine-reconstruction-to-hclwe` | split learning, Gaussian ReLU client of expansion at least 2.1 | fine reconstruction of records by a seed-blind server | hCLWE (BRST21 Corollary 4.2) and NGCA (DKRS23 Theorem 1.5) | $\Pi\lhd\mathcal T$ | one run | $\exp(\Omega(c_0^4d))$ SQ queries, or a quantum lattice algorithm, against one linear solve per record with the seed | SQ for frozen clients, polynomial time under worst-case lattice hardness | record law |
| `prop-sq-label-relevant-reconstruction-bound` | frozen linear client, Gaussian records, single-index labels | reconstruction of the label-relevant coordinate | single-index model, generative exponent $k^*\ge3$ (DPLB24 Theorem 3.2) | $\Pi\lhd\mathcal T$ (and an upper bound by DPLB24 Theorem 4.1) | $d^{k^*/2}$ records to learn the task | $c\,d^{k^*/2}$ VSTAT samples | SQ, sample-based upper bound | record law (the label law) |
| `thm-reconstruction-from-conditional-mean` | frozen linear client, Gaussian records | label-relevant reconstruction from the trained top model | none, the attack uses the trainer's predictor | $\mathcal T\lhd$ learning | excess risk $\varepsilon$ | one pass over $N$ representations, error $2(\sqrt\varepsilon+\eta_N)/\lvert\beta_1\rvert$ | any attacker | none |
| `lem-sq-learner-post-processing` | a learner with 1-STAT access to planted-biclique or uniform rows | property inference: is a biclique planted in the training data | planted biclique (FGRVX17 Theorem 2.10) | $\Pi\lhd\mathcal T$ | $\Omega(n^2/k^2)$ 1-STAT calls | binds every unbounded attacker | the trainer is SQ, the attacker unbounded | record law |
| `thm-fs-sq-black-box-reduction` | refuted | | | | | | | |
| `fact-cohen-narcissus-equals-one-wayness` | the release $x\mapsto f(x)$ of a well-spread efficient $f$ | Narcissus reconstruction of a preimage | inverting $f$ | both | none | polynomial time | polynomial time | the procedure is $f$ |

`fact-cohen-narcissus-equals-one-wayness` was re-read today (CKMMNST25 Definitions
C.1, C.3 and C.4, Theorem C.5). Theorem C.5 needs $f$ efficiently computable and
well spread, the relation $R(x,x')=1$ iff $f(x)=f(x')$, and the family
$\{(U_\lambda,U_\lambda)\}$. The booklet statement matches.

## Part 2. Mappings in the literature, read today

### fact-jagielski-extraction-query-bounds: the price of extracting random and constructed networks
status: borrowed
uses: none

Jagielski, Carlini, Berthelot, Kurakin and Papernot, USENIX Security 2020, key
JCBKP20. Section 3.2 defines functionally equivalent extraction
($\hat O(x)=O(x)$ for all $x$) and fidelity extraction (maximize
$\Pr_{x\sim D_F}[S(\hat O(x),O(x))]$, with $S$ label agreement). Theorem 1,
proven in Appendix A through Definition A.1 and Lemmas 1 and 2: there is a class
of width-$3k$ depth-2 ReLU networks on $[0,1]^d$ with precision-$p$ inputs,
$d\ge k$, that needs $\Theta(p^k)$ logit queries to extract (functionally
equivalent), because $p^k$ disjoint $k$-rectangle functions are each ruled out by
one query at most. Theorem 2, proven in Appendix A by a reduction from subset sum:
testing whether two networks on $\{0,1\}^d$ are functionally equivalent is
NP-hard. Theorem 3 is stated informally only, has no formal version in the
appendix, and imports reference [27], Das, Gollapudi, Kumar and Panigrahy: random
networks on $\{0,1\}^d$ with range $\{0,1\}$ and depth $h$ "require $\exp(O(h))$
samples to learn in the SQ learning model", and Section 3.3 says SQ-expressible
fidelity extraction inherits this.

The source of Theorem 3 is DGKP20 (held copy arXiv 1904.03866v1). Its setting
(Section 2): inputs $x\in\{\pm1\}^n$, depth $h$, layers $x^{(i+1)}=\mathrm{sgn}(W^{(i)}x^{(i)})$,
top layer $1\times n$. Section 2 says the entries of $W^{(i)}$ are uniform on
$[0,1]$, while the introduction says i.i.d. Gaussian and Lemma 3 applies Lemma 1
($\Pr_{r\sim N(0,1)^n}[\mathrm{sgn}(x\cdot r)\neq\mathrm{sgn}(y\cdot r)]=\theta(x,y)/\pi$)
with the rows of $W^{(i)}$ as $r$, which needs Gaussian rows. Theorem 9: for
non-collinear $x,y$, $\lvert E[c_{d+h}]\rvert\le e^{-\Omega(h)}+he^{-\Omega(n)}+de^{-\Omega(\sqrt n)}$,
with $d=O(\log\log n)$ burn-in layers (Lemma 6). Lemma 12: over the $N=2^{n-1}$
inputs of one halfspace, $E_W[E_x[g(x)f_{W,h}(x)]^2]\le\lvert g\rvert_2^2/N+\lvert g\rvert_1^2e^{-h}$
for every fixed $g$. Theorem 15 turns an average squared correlation below
$\epsilon(n,s)$ into the bound $p(n,s)\max(r(n,s),q(n,s))^2>1/\epsilon(n,s)$ on an
SQ learner with $p$ queries of tolerance $1/r$ reaching accuracy $1/2+1/q$
(through BFJKMR94 Theorem 31, quoted as Theorem 14). Theorem 16: for learning a
random depth-$h$ network, $p(n,h)\max(r(n,h),q(n,h))^2>e^{O(h)}$, which the text
reads as "the number of queries $p$ is exponential in $h$". Lemma 17 gives the
converse: the linear map $W^{(h+1)}\cdots W^{(1)}x$ has correlation $e^{-O(h)}$, so
accuracy $1/2+e^{-O(h)}$ is reachable in polynomial time.

Reading, proven from the text. The exponent is printed as $O(h)$ in JCBKP20
Theorem 3 and in DGKP20 Theorem 16. What Lemma 12 with Theorem 15 gives is
$p\max(r,q)^2\ge(\lvert g\rvert_2^2/N+e^{-h})^{-1}=e^{\Omega(h)}$ for
$h\le n-1$, so the intended reading is $e^{\Omega(h)}$. The lower bound holds for
uniform inputs on a halfspace of the cube, for learning a random member of the
class (an average-case statement over $W$), for sign activations, and for
$h=o(\sqrt n)$ through Theorem 9.

As a mapping. Procedure: draw a random network, no data and no training.
Attack task: fidelity extraction by an extractor that sees the network only
through statistical queries on uniformly random inputs. Hard problem: SQ learning
of random deep sign networks, a statistical-dimension bound with no named
problem behind it. Direction $\Pi\lhd\mathcal T$, with the identity map. Trainer's
price: none. Attacker's price: $e^{\Omega(h)}$ queries times squared inverse
tolerance. Carrier: the honest randomness (the weights). It says nothing about
extractors that choose their queries, and Theorem 1 covers chosen queries only
for constructed networks, in the worst case.

Other regime. The bound is SQ only. JCBKP20 itself (Section 6) extracts two-layer
networks by chosen queries and least squares, outside SQ. No polynomial-time
hardness of extracting a random network is known to me.

### fact-gkvz22-backdoor-scope: backdoors planted in the weight law of random features
status: borrowed
uses: none

Goldwasser, Kim, Vaikuntanathan and Zamir, key GKVZ22, held copy arXiv
2204.06974v2 (the FOCS 2022 venue is not stated in the PDF). Definition 4.6: a
backdoor (Backdoor, Activate) is undetectable for Train if the ensembles of
hypotheses $T_D$ (from Train) and $B_D$ (from Backdoor) are indistinguishable for
every data law $D$, by polynomial-time distinguishers with samples of $D$, white
box (full description) or black box (query access). Statistic-access
undetectability is defined and not achieved. Train-RFF (Algorithms 2 and 3) samples
$m=m(d,\varepsilon,\delta)=\Theta(d\log(d/\varepsilon\delta)/\varepsilon^2)$ features
$\cos(2\pi(\langle g,\cdot\rangle+b))$, $g\sim\gamma_d$, $b\sim[0,1]$, the width the
paper takes from RR07 for uniform convergence to the Gaussian kernel, and trains a
linear head by any routine. Backdoor-RFF (Algorithms 4 to 6) draws
$g\sim GP_d(\mathrm{bk})$, the sparse Gaussian pancakes of Lemma 6.2, and activates
by $x\mapsto x+\mathrm{bk}$. Theorem 6.4: under Assumption 6.3 (the head has
margin $m^{-O(1)}$ on all inputs) and with $d,1/\varepsilon,\log(1/\delta)$
polynomially related, Backdoor-RFF is a $\gamma$-backdoor with $\gamma=d^{1/c}$ in
$\ell_0$ and $2d^{1/2c}$ in $\ell_2$, white-box undetectable under Hypothesis 3.7
(SIVP $\notin$ BQP or GapSVP $\notin$ BQP). The proof: a distinguisher of the two
hypotheses gives a distinguisher of $\gamma_d$ against $GP_d(\omega)$, because the
reduction can run Train-RandomFeatures itself on the given feature vectors.
Lemma 6.6 obtains the dense pancakes from BRST21's homogeneous CLWE, conditioned
near $1/2$ instead of $0$, with $\gamma\ge2\sqrt d$. Appendix A, Claim A.5: for
$k=d^\alpha$, $0<\alpha<1/2$, $\theta=O(1)$, $\lambda>1/\theta$ and data on the
unit sphere, sampling the ReLU features from $N(0,I_d+\theta ss^\top)$ ($s$ a
$k$-sparse unit vector) and activating by $x\mapsto x+\lambda s$ is a one-way
backdoor with $\gamma=k$ in $\ell_0$ and $\lambda$ in $\ell_2$, white-box
undetectable under Assumption A.4 (planted clique $\notin$ BPP for $k=o(n^{1/2})$)
through Lemma A.3 (BB19, $m=\Theta(d)$), with advantage $o(1)$ only (Appendix A,
crediting CG24). Theorem 5.4 (black box, any model) uses digital signatures.

As mappings. RFF: hCLWE $\lhd$ white-box detection, carrier the choice of the
trainer who is the adversary (the law of the random weights), trainer's price one
run of width $m$, auditor's samples $m$ weight vectors. The converse, detection
$\lhd$ distinguishing $\gamma_d$ from the pancake law with $m$ samples, is
immediate: read the rows. Signatures: a primitive, so outside the rule of
`CONTEXT.md`. Sparse PCA: see `lem-sparse-pca-backdoor-width-price`.

Other regime. Every statement is polynomial time under a named assumption. An
unbounded auditor detects the pancake backdoor: heuristic, assuming the
information-theoretic sample complexity of hCLWE detection is $\tilde O(d)$,
below the width $m$ of Train-RFF. No SQ statement is made in GKVZ22.

### fact-frozen-gaussian-layer-collision-hardness: a frozen Gaussian layer carries a lattice problem
status: borrowed
uses: none

Bogdanov, Rosen and Vafa, key BRV26, ICML 2026 per the library record, held copy
the anonymous ICLR 2026 submission, so the numbering below is that copy's.
Definition 5: the symmetric bounded perceptron (SBP) problem asks, on
$A\sim N(0,1)^{m\times n}$, for $x\in[-B:B]^n\setminus\{0\}$ with
$\lVert Ax\rVert_\infty\le\kappa\sqrt n$. Assumption 2: for every p.p.t. algorithm,
$\varepsilon>0$ and $B,n\le\mathrm{poly}(m)$, the probability of outputting such
an $x$ with $\lVert Ax\rVert_\infty\le m^{-\varepsilon}$ is negligible. The paper
states that Assumption 2 holds if worst-case lattice problems are hard, citing
Vafa and Vaikuntanathan 2025 and Bogdanov et al. 2025 (not read). Theorem 2: for
$m\le n$ a p.p.t. BackdoorMatrix outputs $A$ and $z\in\{\pm1\}^n$, $z$ uniform,
with $\lVert Az\rVert_\infty\le O(\sqrt n\,2^{-n/m})$ and total variation from
$N(0,1)^{m\times n}$ at most $O(\sqrt{m/n}\log(n/m))+e^{-\Omega(m)}$ (as printed,
with the logarithm's argument garbled in extraction). Definition 6: a
statistically undetectable backdoor has $d_{TV}(F,\hat F)=o(1)$ on white-box
descriptions, collisions $\lVert\hat F(x')-\hat F(x)\rVert_2\le\delta_0$ for
$x'=\mathrm{Activate}(\mathrm{bk},x)$, and approximate collision resistance at
$\delta_1$ against p.p.t. adversaries with white-box access. Theorem 5: for models
$g(Ax)$ with $g$ $(\alpha,\beta)$-bilipschitz and $m=n^{\Omega(1)}$, $m=o(n)$, under
Assumption 2, the strength is $\delta_1/\delta_0=\Omega(\alpha2^{n/m}/(\beta\sqrt n\,m^{1/2+\varepsilon}))$.
Theorem 7: for depth-$d$ networks with a frozen Gaussian first layer, later
linear maps of condition number at most $\gamma$ and LeakyReLU$_\alpha$
activations, the strength is $\Omega(\alpha^d2^{n/m}/(\sqrt n\,m^{1/2+\varepsilon}\gamma^{d-1}))$.
Corollary 3: $m=n^{1/2}$, $d=n^{1/4}$ give strength $2^{\Omega(m)}$.

As a mapping. Procedure: any training of the later layers on top of a frozen
compressing Gaussian layer, on integer inputs. Attack task: find two distinct
inputs in $[-B:B]^n$ whose outputs are within $\delta_1$ (an invariance-based
adversarial example). Hard problem: SBP. Direction $\Pi\lhd\mathcal T$, by
bilipschitzness: a colliding pair $(x_1,x_2)$ gives $A(x_1-x_2)$ small. Carrier:
the honest randomness, since the hard instance is the honest Gaussian layer itself.
The backdoor is carried by the trainer's choice of the layer's law and is
undetectable even statistically.

Other regime. Statistically, collisions exist and an unbounded adversary finds
them by exhaustive search (Section 1.1), so the content is computational. The
backdoor's undetectability is information-theoretic.

### fact-instance-encoding-privacy-learnability: privacy of an instance encoding against learnability
status: borrowed
uses: none

Carlini et al., IEEE S&P 2021, key CDGJMMSTT21 (note filled by the
computational-limits session, re-read today). Definition 5: the adversary picks
$D$, a concept $c$ and $x_0,x_1$ with $c(x_0)=c(x_1)$, gets the encoding of $x_b$
among $n-1$ fresh records, and guesses $b$. Theorem 4: for an $(m,\gamma)$-rich
class (Definition 7) and encoded accuracy $(\epsilon,\delta)$, an attack with oracle
access to $E(\cdot)$, $L$, $F$ and a sampler of $D$ reaches advantage
$0.99-\epsilon(n)/\gamma$ in expected time $O(m/(1-\delta(n)))$. Theorem 5: for one
balanced concept and a decomposable instance encoding with balanced encoded
accuracy $(\epsilon,\delta)$, for every $\tau$ either an attack with oracle access
to $L$, $E$ and $D_c$ has average advantage at least $1/2-\epsilon(m)-\tau$ in
expected time $O(m/\delta(m)+m/\tau^2)$, or an efficient protocol learns $c$ from
$m$ samples to accuracy $1-\tau$ in time $O(m/\tau^3)$.

As a mapping. Theorem 5 is a dichotomy: if learning $c$ to accuracy $1-\tau$ from
$m$ samples is hard, every accurate instance encoding has an efficient
distinguishing attack. Hardness of the learning problem helps the attacker.
Trainer's price $m$ samples, attacker's price $O(m/\delta+m/\tau^2)$ time with an
encoder oracle. Carrier: none, the statement holds for every encoding.

Other regime. Polynomial time with oracles. The encoder oracle is what a
seed-known split server has and a seed-blind one lacks (the note's finding).

### fact-chlx25-defendability-characterization: backdoor defense against learnability
status: borrowed
uses: none

Christiano, Hilton, Lecomte and Xu, ITCS 2025, key CHLX25. Definition 3.1: the
attacker picks $D$ and $f\in F$, a trigger $x^*\sim D$ is drawn, the attacker picks
$f^*$, which is $\varepsilon$-valid if $\Pr_D[f^*\ne f]\le\varepsilon$ and
$f^*(x^*)\ne f(x^*)$; the detector gets $(f,x)$ with $x\sim D$ or $(f^*,x^*)$, the
representation, $\mathrm{Ex}(f',D)$, and must accept the first and reject the second.
Theorem 4.1: the best confidence of $\varepsilon$-defendability is
$\max\{1/2,1-\Theta(\mathrm{VC}(F)\varepsilon)\}$ as $\mathrm{VC}(F)\to\infty$.
Corollary 5.2: efficient PAC learnability implies efficient defendability
(Definition 5.1, $\varepsilon<1/p(n,1/\delta)$). Theorem 5.3: in the random oracle
model there is a class that is efficiently defendable and not efficiently PAC
learnable. Theorem 5.5: under one-way functions and iO, polynomial-size circuits
are not efficiently defendable.

As mappings. Detection $\lhd$ PAC learning (Corollary 5.2), with the detector's
samples about $1/\varepsilon$ times the learner's. The obstruction of Theorem 5.5
is carried by obfuscation, a primitive of the attacker. Neither part involves a
training procedure or a data law that carries hardness.

Other regime. Theorem 4.1 is the statistical regime, with no learning procedure
in the game.

### fact-generative-exponent-post-processing-monotone: label post-processing never lowers the generative exponent
status: borrowed
uses: fact-generative-exponent-sq-recovery-bound

Damian, Pillaud-Vivien, Lee and Bruna, COLT 2024, key DPLB24. Definition 1.1: the
class $\mathcal G$ of laws $\nu$ of $(Z,Y)$ with $\nu_z=\gamma_1$,
$E[Y^2]<\infty$ and $D_{\chi^2}(\nu\Vert\gamma_1\otimes\nu_y)>0$. Definition 2.4:
$\zeta_k(y)=E[h_k(Z)\mid Y=y]$, $\lambda_k=\lVert\zeta_k\rVert_{P_y}$,
$k^*(P)=\min\{k\ge1:\lambda_k\ne0\}$. Lemma 2.3:
$I_{\chi^2}[P]=\sum_{k\ge1}\lambda_k^2$. Proposition 2.6:
$k^*(P)=\inf_{T\in L^2(P_y)}l^*((\mathrm{Id}\otimes T)_\#P)$, and the paragraph after
it: if $Y\to Y'$ is a Markov chain with $E[(Y')^2]<\infty$ then
$k^*(Z,Y')\ge k^*(Z,Y)$. Example 2.7 (ii): $\sigma(z)=z^2e^{-z^2}$ has $k^*=4$.
Corollary 2.8: $k^*$ is invariant under bijections $\varphi$ of the label with
$\varphi,\varphi^{-1}\in L^2(P_y)$. Theorem 5.2: for deterministic $\sigma$ and
$\tau\ge0$, the law of $(u,\sigma(u)+\tau v)$, $(u,v)\sim\gamma_2$, has the
generative exponent of $(u,\sigma(u))$. Theorem 4.1: with a denoiser $T$ and
$n\ge C_k[d^{k/2}/\tilde\lambda_k^2+d/(\tilde\lambda_k^2\epsilon^2)]$,
$\tilde\lambda_k=\lambda_k/\log^k(3/\lambda_k)$, Algorithm 1 returns $\hat w$ with
$(\hat w\cdot w^*)^2\ge1-\epsilon^2$ with probability $1-2e^{-d^c}$.

A caveat, proven from the text of Appendix E.2 and already recorded in the space
computational-limits (`ch-label-sq-self-correlation`): the proof of Theorem 3.2
takes the diagonal bound $\beta=1$ in Definition B.4, while
$\chi_0(P_w,P_w)=I_{\chi^2}[P]$, which can exceed 1 and is infinite for
deterministic labels. A bound for a deterministic link therefore needs label noise
or another argument. This space uses the form of
`prop-sq-label-relevant-reconstruction-bound`, which assumes
$I_{\chi^2}[P]<\infty$ and uses it as $\beta$.

Other regime. Proposition 2.6 and the Markov remark are information statements
about the law and hold in every regime. Theorem 4.1 is sample-based and runs in
time $\tilde O(d^{k/2+1})$ (Remark 4.2).

### lem-sparse-pca-backdoor-width-price: the sparse-PCA backdoor is detected or needs no key
status: proven
uses: fact-gkvz22-backdoor-scope

Statement. Take the construction of GKVZ22 Appendix A (Algorithms 7 to 10):
honest weights $g_1,\dots,g_m$ i.i.d. $\gamma_d$, backdoored weights i.i.d.
$N(0,I_d+\theta ss^\top)$ with $s$ a $k$-sparse unit vector, $0<\theta\le k$,
classifier $h(x)=\mathrm{sgn}(-\tau+\frac1m\sum_j\mathrm{ReLU}(\langle g_j,x\rangle))$
with $0<\tau\le1$, data on the unit sphere, activation $x\mapsto x+\lambda s$.

(a) Detection. The test $T(G)=1\{\max_{i\le d}\frac1m\sum_jg_{ji}^2\ge1+\theta/(2k)\}$,
computable in time $O(md)$, satisfies $\Pr_{\rm honest}[T=1]\le de^{-m\theta^2/(64k^2)}$
and $\Pr_{\rm backdoor}[T=0]\le e^{-m\theta^2/(64k^2)}$. So if
$m\ge64k^2\ln(4(d+1))/\theta^2$ the advantage of $T$ is at least $3/4$.

(b) The price of not being detected. If $T$ has advantage below $3/4$, then
$\theta<8k\sqrt{\ln(4(d+1))/m}$, and Claim A.5's condition $\lambda>1/\theta$
forces $\lambda k>\sqrt{m/(64\ln(4(d+1)))}$. With GKVZ22's $m=\Theta(d)$
(Lemma A.3) and $k=d^\alpha$, $\alpha<1/2$, this is
$\lambda=\Omega(d^{1/2-\alpha}/\sqrt{\log d})$, polynomially larger than the norm
of the data.

(c) No key is needed. For honest weights, every unit $x$, every unit $u$ and every
$\lambda$ with $\lambda-1>2\sqrt{2\pi}\,\tau$, if $m\ge16\pi\ln(1/\delta)$ then
$h(x+\lambda u)=1$ with probability at least $1-\delta$. The same holds for the
backdoored weights. So in the regime of (b) every input moved by $\lambda$ in any
direction is classified positive by honest and backdoored networks alike.

Proof. (a) Let $V\sim\chi^2_m$. Laurent and Massart's inequalities give
$\Pr[V-m\ge2\sqrt{mt}+2t]\le e^{-t}$ and $\Pr[m-V\ge2\sqrt{mt}]\le e^{-t}$. Put
$\eta=\theta/(2k)\le1/2$ and $t=m\eta^2/16$. Under the honest law each
$\frac1m\sum_jg_{ji}^2=V_i/m$, and $2\sqrt{mt}+2t=m\eta/2+m\eta^2/8<m\eta$, so
$\Pr[V_i/m\ge1+\eta]\le e^{-m\eta^2/16}$, and a union bound over $i$ gives the first
inequality. Under the backdoored law pick $i^*$ with $s_{i^*}^2\ge1/k$, which
exists since $s$ is a $k$-sparse unit vector. Then $g_{ji^*}\sim N(0,\sigma^2)$
with $\sigma^2=1+\theta s_{i^*}^2\ge1+2\eta$, and
$\Pr[\sigma^2V/m<1+\eta]\le\Pr[V/m<1-\eta/(1+2\eta)]\le\Pr[m-V\ge m\eta/2]\le e^{-m\eta^2/16}$,
using $\eta/(1+2\eta)\ge\eta/2$ for $\eta\le1/2$. Since $m\eta^2/16=m\theta^2/(64k^2)$,
both errors are at most $(d+1)e^{-m\theta^2/(64k^2)}\le1/4$ under the stated $m$.
(b) is (a) read backwards with $\lambda>1/\theta$. (c) Let $x'=x+\lambda u$ and
$\rho=\lVert x'\rVert\ge\lambda-1$. Under the honest law
$\langle g_j,x'\rangle\sim N(0,\rho^2)$ and $E\,\mathrm{ReLU}(N(0,\rho^2))=\rho/\sqrt{2\pi}$.
The average $\frac1m\sum_j\mathrm{ReLU}(\langle g_j,x'\rangle)$ is a
$(\rho/\sqrt m)$-Lipschitz function of the Gaussian vector $(g_1,\dots,g_m)$, so
Gaussian concentration gives a lower deviation $t$ with probability at most
$e^{-mt^2/(2\rho^2)}$. With $t=\rho/(2\sqrt{2\pi})$ and $m\ge16\pi\ln(1/\delta)$ the
average exceeds $\rho/(2\sqrt{2\pi})>\tau$ with probability $1-\delta$. Under the
backdoored law $\langle g_j,x'\rangle\sim N(0,\rho^2+\theta\langle s,x'\rangle^2)$,
whose mean ReLU is at least $\rho/\sqrt{2\pi}$, and the Lipschitz constant is at
most $\rho\sqrt{1+\theta}/\sqrt m$; the same argument holds with $m$ larger by the
factor $1+\theta$. $\square$

What it means. GKVZ22's Claim A.5 is true as stated. The mapping it suggests,
planted clique $\lhd$ backdoor detection, carries no backdoor content: either the
auditor detects the planted spike in time $O(md)$ from $m=\Omega(k^2\log d/\theta^2)$
weight vectors, or the activation moves inputs by a distance $\lambda>\sqrt{m/(64\ln(4(d+1)))}/k$
at which the key is irrelevant. The trade-off is priced in the trainer's width $m$:
undetectability against $T$ forces $\lambda k\gtrsim\sqrt{m/\log d}$, and a trainer
who widens the layer for accuracy ($m\gg d$) makes the backdoor easier to see.
The detection threshold matches the regime $\theta=o(k\sqrt{\log d/t})$ that
Choudhary et al. (arXiv 2605.04209, Assumption 1, not read beyond the HTML) state
for sparse-PCA hardness. Part (c), the key-free activation, was not found in the
literature.

Other regime. (a) is a polynomial-time test, so it bounds every computational
notion of undetectability. Statistically, a spike of strength $\theta$ is
detectable from fewer samples, of order $k\log d/\theta^2$ (heuristic, the standard
information threshold of sparse PCA, not proven here). No oracle is involved.

## Part 3. Gaps

Each line names an attack task and what is missing. The search rows cited are in
`sink/formalizing/searches.md` or in this round's `summary.md`.

- Membership inference. No computational hardness under a named assumption
  (`search-crypto-hardness-membership-inference`, nil), and no mapping onto a hard
  learning problem (`fact-no-hard-learning-attacker-lower-bound`). A structural
  reason: membership is a property of one record, and the population SQ game of
  `def-seed-blind-reconstruction-game` sees only laws, so a membership mapping must
  live in the polynomial-time game or price shadow runs (the space
  statistical-limits). Heuristic.
- Unlearning verification. No hardness theorem (`search-unlearning-verification-hardness`,
  nil). The twin prices of `thm-exact-twin-price` are statistical.
- Poisoning and backdoor insertion as an attack on an honest trainer. No SQ or
  low-degree bound (`search-sq-lower-bound-backdoor-poisoning`, nil).
- Extraction. The only lower bounds are worst-case over constructed networks
  (JCBKP20 Theorem 1), NP-hardness of testing equivalence (Theorem 2), and the SQ
  bound for untrained random networks (DGKP20 Theorem 16). Nothing prices the
  extraction of a trained model in the trainer's units, and nothing compares the
  extractor's sample price with the trainer's. Aim
  `conj-extraction-priced-by-generative-exponent`.
- Backdoor detection. The literature gives one-directional reductions for
  random-feature layers with planted weight laws (GKVZ22, BRV26), each for one law.
  No statement prices detection as one hard problem for every planted law, and none
  relates the auditor to the attacker of the first milestone. Aim
  `conj-backdoor-detection-is-ngca`.
- Property inference. Only `lem-sq-learner-post-processing`, for planted biclique.
  Its proof uses nothing about bicliques beyond FGRVX17 Theorem 2.10, so every SQ
  testing bound against 1-STAT learners transfers to a property-inference bound
  against unbounded attackers (heuristic, to be stated as an instance of the
  transfer lemma of `def-hard-problem-mapping`).
- A tried dead end. BRV26's collision hardness gives no reconstruction mapping for
  a compressing Gaussian client on uniform integer records: for
  $f(x)=\lfloor Ax/\delta\rceil$ on $[-B:B]^n$, every reconstructor, unbounded,
  recovers $x$ exactly with probability at most $\lvert\mathrm{Im}f\rvert/(2B+1)^n$,
  which is negligible once $m\log(Bn\log(mn)/\delta)=o(n)$ (with high probability
  $\lVert Ax\rVert_\infty\le Bn\sqrt{2\ln(2mn)}$, which bounds the number of cells),
  because $x$ is uniform on its fiber given $f(x)$. The hardness of finding another preimage is then not a
  privacy statement. Proven, in two lines.

## Part 4. Aims

### def-hard-problem-mapping: a mapping between an attack task and a hard problem
status: open
uses: def-seed-access-modes, def-seed-blind-reconstruction-game, def-uniform-security-profile

Statement. Fix a security parameter $d$. A *mapping* is a tuple
$\mathfrak M=(\mathcal P,\mathcal T,\Pi,\lhd,\iota,\rho,p_P,p_A,R,\kappa,\mathcal E)$.

1. Procedure $\mathcal P$: a randomized map from $n_P$ records and the procedure's
   coins (seed, initialization, hardware randomness) to a release, with the cost
   meter of `def-seed-access-modes`. The trainer's budget is
   $b_P=(n_P,N_P,\mathrm{work})$: records, training runs and work per run.
2. Attack task $\mathcal T$: a game in which a challenger draws records from a law
   $D$ in a class $\mathfrak D$, runs $\mathcal P$, and gives the adversary a view
   (the white-box release, representations, an evaluation interface, statistical
   queries to a population law the release determines, or $\mathsf{Train}$ calls),
   and scores the output by a success functional minus a baseline fixed by the game
   (a prior, the Narcissus baseline, or the null). The advantage is the difference.
   The adversary is a third party, or the trainer itself when it plants, and then
   the auditor's advantage is the quantity of interest.
3. Hard problem $\Pi$: a distributional decision problem ($\mathfrak D_0$ against
   $\{\mathfrak D_s\}_{s\in S}$) or search problem, with a cited threshold: a set
   $B_\Pi(a,R)$ of budgets in its own units (samples, VSTAT parameter and query
   count, degree, time) at which no solver of regime $R$ reaches advantage $a$.
4. Direction. $\Pi\lhd\mathcal T$: a reduction turns every attacker into a solver.
   $\mathcal T\lhd\Pi$: a reduction turns every solver into an attacker. The mapping
   is two-sided when both hold with prices equal up to polynomial factors.
5. Instance and solution maps. For $\Pi\lhd\mathcal T$, the reduction gets
   $\Pi$'s samples or oracle, simulates the game on the instance $\iota(s)$ (it
   draws records, runs $\mathcal P$ itself, counting each run), never uses $s$, and
   maps the attacker's output by $\rho$.
6. Prices. $p_A$ maps the attacker's budget and advantage $(b_A,a)$ to the solver's
   $(b_\Pi,a-\eta)$. $p_P$ states $b_P$ at the instance and, when $\mathcal P$
   learns a task, that task's threshold at the same instance. Both are in the
   trainer's units: records, training runs, queries counted as samples through the
   VSTAT parameter, and learner work. When both prices are polynomial in $d$, the
   *exponent ratio* of $\mathfrak M$ is
   $\lim_d\log p_A/\log p_P$.
7. Regime $R$: population SQ, low-degree, polynomial time under a named
   assumption, or information-theoretic. The reduction maps attackers of regime
   $R$ to solvers of regime $R$, and one mapping lives in one regime.
8. Carrier $\kappa$: the record law ($\iota$ changes $D$ only, and $\mathcal P$ is
   fixed before and independent of $s$), the honest randomness (the hard instance
   is the procedure's own random object, no $s$ is planted), the trainer's choice
   (a trainer who is the adversary sets the law of the procedure's randomness as a
   function of $s$), or a primitive (the designer changes $\mathcal P$ as a function
   of a key). A mapping carried by a primitive does not count (`CONTEXT.md`).
9. Experiment $\mathcal E$: a finite instantiation, with $d$, $n_P$, the sampler of
   $\iota$, the attackers run, their measured budgets, and the training runs it
   costs.

What would settle it. (i) A transfer lemma: if $\Pi\lhd\mathcal T$ in regime $R$
with $p_A$ and loss $\eta$, every $R$-attacker of advantage $a+\eta$ has a budget
$b_A$ with $p_A(b_A)\notin B_\Pi(a,R)$, and a composition lemma for chains of
mappings, carriers composing to the strongest (primitive over trainer's choice over
record law over honest randomness). (ii) Every entry of Parts 1 and 2 fills the
nine fields without change, the carrier deciding each entry with no ambiguity. (iii)
The statement of Halil's rule as a property of $\kappa$.

Regime and experiment. A definition, so no regime of its own. Field 9 makes every
mapping carry its experiment.

Other regime. Without the oracle a reduction counts its simulated runs as real
training runs. With the oracle of `def-learning-oracle`, field 5 lets the reduction
call $\mathsf{Train}$, and $p_A$ counts calls. The definition does not fix the seed
mode: each mapping names the mode it needs (decision 2 of `STATE.md`).

### conj-extraction-priced-by-generative-exponent: extraction costs the generative exponent of the model's own link
status: open
uses: fact-generative-exponent-sq-recovery-bound, fact-generative-exponent-post-processing-monotone, prop-sq-label-relevant-reconstruction-bound, fact-jagielski-extraction-query-bounds

Setting. Records $x\sim\gamma_d$, labels with $(\langle u,x\rangle,y)\sim P\in\mathcal G$
(DPLB24 Definition 1.1), $u$ uniform on $S^{d-1}$, and $m_P(z)=E_P[Y\mid Z=z]$. The
trainer releases $\hat f(x)=m(\langle w,x\rangle)$ for a bounded link $m$ and a unit
$w$ (the Bayes predictor has $m=m_P$, $w=u$). The extraction game
$\Gamma_{\rm ext}(\sigma_E)$: the extractor's interface answers random inputs with
$\hat f(x)+\sigma_E\xi$, $\xi\sim N(0,1)$, $\sigma_E>0$ fixed. In the sample game
it gets $n$ answered pairs; in the SQ game its queries are answered by VSTAT$(n)$ on
the law of $(x,\hat f(x)+\sigma_E\xi)$. It wins with weak fidelity $c_0$ if it outputs
a bounded $g$ with $\mathrm{Cov}(g(x),\hat f(x))\ge c_0\sqrt{\mathrm{Var}\,\hat f(x)}$.
Write $Q_m$ for the law of $(Z,m(Z))$.

Claims. (a) If $k^*(Q_m)=k\ge3$, every SQ extractor with at most $d^r$ queries
reaching weak fidelity $c_0$ needs $n\ge c(m,\sigma_E,c_0,r)\,d^{k/2}$, and with
$n=O(d^{k/2})$ answered pairs the sample-based extractor that runs DPLB24's
Algorithm 1 recovers $w$ and reaches fidelity tending to 1. (b) If
$Z\to m_P(Z)\to Y$ is a Markov chain, $k^*(Q_{m_P})\le k^*(P)$: extracting the Bayes
predictor never costs a larger exponent than training. (c) For the law $P_\natural$
of $(Z,Z\varepsilon)$ with $\Pr[\varepsilon=1\mid Z]=(1+\mathrm{sgn}(Z)e^{-Z^2/2})/2$,
$k^*(P_\natural)=2$ while the Bayes link $m_\natural(z)=\lvert z\rvert e^{-z^2/2}$ has
$k^*(Q_{m_\natural})=4$. So the trainer learns from $\tilde O(d)$ records and the
extractor needs of order $d^2$ answered queries: exponent ratio 2.

Sketch, with the parts already proven. (b) is DPLB24's Markov remark after
Proposition 2.6 applied to $Z\to m_P(Z)\to Y$, which reads
$k^*(Z,Y)\ge k^*(Z,m_P(Z))$: proven. For (c), two facts are proven here.

First, $k^*(P_\natural)=2$. The map $(z,y)\mapsto(-z,y)$ preserves $P_\natural$:
given $-Z$, the sign has $\Pr[\varepsilon'=1]=(1-\mathrm{sgn}(Z)e^{-Z^2/2})/2$, so
$\varepsilon'\overset d=-\varepsilon$ and $(-Z)\varepsilon'\overset d=Z\varepsilon$.
Hence $\zeta_k=0$ for every odd $k$. Since $\lvert Y\rvert=\lvert Z\rvert$,
$\zeta_2(Y)=(Y^2-1)/\sqrt2$ and $\lambda_2=1$. With symmetric label noise added, $T(y)=y^2$
still has $E[T(Y)h_2(Z)]=\sqrt2\neq0$, so $\lambda_2>0$ and $k^*=2$ still. And
$E[Y\mid Z]=Z\,\mathrm{sgn}(Z)e^{-Z^2/2}=m_\natural(Z)$.

Second, the level sets of $\lvert z\rvert\phi(z)$ carry the Gaussian's first two
moments exactly. Let $G(r)=r\phi(r)$ on $r\ge0$. Then $G'(r)=\phi(r)(1-r^2)$, so $G$
rises on $[0,1]$, falls on $[1,\infty)$, and $G(0)=G(\infty)=0$. For
$t\in(0,G(1))$, $G^{-1}(t)=\{a,b\}$ with $a<1<b$, and the law of $Z$ given
$G(\lvert Z\rvert)=t$ has atoms $\pm a$, $\pm b$ with weights proportional to
$\phi(a)/\lvert G'(a)\rvert=1/(1-a^2)$ and $1/(b^2-1)$, split evenly between the
signs. Put $A=1-a^2$ and $B=b^2-1$. Then $E[Z\mid\cdot]=0$,
$$E[Z^2\mid\cdot]=\frac{(1-A)/A+(1+B)/B}{1/A+1/B}=1,\qquad E[Z^4\mid\cdot]=\frac{(1-A)^2/A+(1+B)^2/B}{1/A+1/B}=1+AB,$$
so $E[h_1\mid\cdot]=E[h_2\mid\cdot]=E[h_3\mid\cdot]=0$ (the last by symmetry) and
$E[h_4(Z)\mid\cdot]=(AB-2)/\sqrt{24}$, which is not almost surely zero (as
$t\to0$, $A\to1$ and $B\to\infty$). Since $m_\natural=\sqrt{2\pi}\,G(\lvert z\rvert)$ is
a function of $G(\lvert z\rvert)$ with the same level sets, $k^*(Q_{m_\natural})=4$.
This agrees with DPLB24 Example 2.7 (ii) and Corollary 2.8, since
$m_\natural^2=z^2e^{-z^2}$ and squaring is a bijection on $[0,\infty)$. The identity
$\frac{d}{dr}(r\phi(r))=\phi(r)(1-r^2)$ is the whole reason: the Jacobian weights of a
level set are the reciprocals of $1-a^2$ and $b^2-1$, which balance the second moment.

Open, for round 01: (a). The lower bound needs a reduction from weak fidelity to
the decision version of the single-index problem against the null
$\gamma_d\otimes(Q_m)_y$ (one correlation query $E[g(x)y]$ separates the two, since
under the null it vanishes), the SQ dimension of that decision problem with
diagonal bound $I_{\chi^2}[Q_m*\sigma_E]<\infty$ (finite because $m$ is bounded and
$\sigma_E>0$), and DPLB24 Theorem 5.2 for $k^*$ of the noisy answers. The upper bound
is DPLB24 Theorem 4.1 with $k=k^*$ on the answered pairs.

What would settle it. Proofs of (a) and of the two bounds of (c) with explicit
constants, or a counterexample.

Regime. SQ for the lower bound, sample-based for the upper bound, low-degree under
DPLB24 Conjecture 3.4. The extractor never chooses its inputs. With chosen inputs,
$\hat f(te_i)=m(tw_i)$ reveals $w$ coordinate by coordinate from $O(d)$ queries per
scan (heuristic), so the separation is a statement about learning-based extraction,
the class JCBKP20 Theorem 3 addresses.

Experiment. Train on $P_\natural$ at $d\in\{32,64,128,256\}$ with $n_P=Cd\log d$
records (a single-index fit with known link, or a two-layer network), release
$\hat f$, answer random Gaussian inputs with noise $\sigma_E$, run a student
(gradient descent on square loss, and the partial-trace algorithm), and record the
answered queries needed for fidelity $c_0$. The prediction is slope 1 in
$\log n_P$ against $\log d$ and slope 2 for the extractor. One training run per $d$,
no oracle.

Other regime. Statistically the extractor needs $\tilde\Theta(d/(\lambda_k^2\epsilon^2))$ answered
queries (DPLB24 Theorem 6.1, an inefficient estimator), so the gap is computational,
as for every $k^*>2$. Without label noise in the interface the diagonal of the SQ
dimension is infinite and claim (a) needs another argument.

### conj-backdoor-detection-is-ngca: detection of a weight-law backdoor is NGCA at the trainer's width
status: open
uses: fact-gkvz22-backdoor-scope, fact-ngca-sq-lower-bound, fact-clwe-hardness, def-seed-blind-reconstruction-game, lem-sparse-pca-backdoor-width-price

Setting. A random-feature procedure of width $m$: weights $g_1,\dots,g_m$ i.i.d.
from a weight law, features $\varphi_j(x)=\sigma(\langle g_j,x\rangle+b_j)$ with
fixed $\sigma$ and offsets, a head trained by any efficient routine on data from
$D$. The honest law is $\gamma_d$. A weight-law backdoor replaces it by $P^A_s$
with $A\ne\gamma_1$ and $s$ uniform on $S^{d-1}$.

Claims. (a) White box. Detection with advantage $a$ and NGCA testing of $A$
($\gamma_d^{\otimes m}$ against $(P^A_s)^{\otimes m}$) with advantage $a$ are
two-sided equivalent, with one simulated training run and polynomial overhead.
(b) Gram access. An auditor that sees only the law of $\varphi(x)$ for
$x\sim\gamma_d$, unknown to it, learns at most $(GG^\top,b)$, and for detection it is
exactly as strong as the white-box auditor, because both hypotheses are invariant
under $G\mapsto GQ$, $Q\in O(d)$, and a fresh Haar rotation of any factor of
$GG^\top$ restores the law of $G$. (c) Transpose duality. For entrywise $\sigma$,
$\sigma(GX^\top)$ with $G$ backdoored ($m$ rows) and $X$ Gaussian ($N$ rows) is the
transpose in law of the seed-blind server's representation matrix of
`def-seed-blind-reconstruction-game` for a Gaussian client of width $N$ and $m$
records from $P^A_s$. An auditor who chooses its probes plays the seed-known
server, one who sees features on unknown inputs plays the seed-blind server, and
the results of `thm-blind-split-seed-separation` transfer to reconstruction of the
key's projections $\langle s,g_j\rangle$. (d) Prices. The auditor's sample budget
is the trainer's width $m$. For pancakes, detection is polynomial-time hard under
`fact-clwe-hardness` and SQ-hard; for $A$ matching four or more moments it is
SQ-hard by `fact-ngca-sq-lower-bound`; for the spiked law it is governed by
`lem-sparse-pca-backdoor-width-price`.

Sketch. (a), first direction: given $m$ samples, use them as the weights, draw the
offsets and data, train the head, hand the model to the detector (GKVZ22's proof of
Theorem 6.4, with any $A$). Second direction: read the rows and run the NGCA test.
(b): for any test $T$, $E_QT(GQ)$ has the same advantage and is a function of
$GG^\top$; from $GG^\top=U\Lambda U^\top$ the auditor forms $G'=U\Lambda^{1/2}$
(rank $d$), and $G'R$ with $R$ Haar has the law of $G$ under each hypothesis. The
missing step is how much of $GG^\top$ statistical queries of tolerance $\tau$ return
for a given $\sigma$ (for ReLU without offsets the second moments of $\varphi$ are
the arc-cosine kernel of $g_i\cdot g_j$, $\lvert g_i\rvert$, $\lvert g_j\rvert$). (c)
is an identity of laws. (d) collects cited thresholds.

What would settle it. Proofs of (a) to (c) with the overhead stated, and for (b)
the precision at which an SQ auditor of tolerance $\tau$ keeps the NGCA price, or a
counterexample.

Regime. Polynomial time under hCLWE for pancakes, SQ for moment-matched laws. Never
both in one statement.

Experiment. Plant $A$ in the weights of a random-feature layer of width $m$ for
$m/d\in\{1,4,16\}$, run moment tests, PCA and, for noiseless pancakes, LLL, and
record the detection rate against $m$. No oracle.

Other regime. Statistically, detection needs a number of weight vectors set by the
information threshold of NGCA for $A$, which for pancakes is of order $d$ up to
logarithms (heuristic). A trainer whose width exceeds it is detectable by an
unbounded auditor, so undetectability is computational at every useful width.

## Questions for the discussant

1. Is the reading of JCBKP20 Theorem 3 and DGKP20 Theorem 16 right: the exponent
   should read $\Omega(h)$, and DGKP20's weights must be Gaussian for Lemma 3?
2. Does `lem-sparse-pca-backdoor-width-price` hold as stated, and does it misread
   GKVZ22's Claim A.5 or its threshold $\tau$?
3. Is the nine-field definition the right uniform statement, and is the carrier
   field a faithful formal reading of Halil's rule?
4. Which of the two conjectures should round 01 prove first, and is the separation of
   claim (c) of the extraction conjecture known to you?
