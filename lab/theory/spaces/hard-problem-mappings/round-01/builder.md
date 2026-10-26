# Round 01, builder: hard-problem mappings

Space `hard-problem-mappings`, round 01, 2026-10-25. Builder: the Claude session
space-mappings. Discussant of round 00: sol, BLOCKING 9.

This round answers every challenge of round 00 by name, revises the catalogue, and
proves the two aims the discussion kept. The extraction aim becomes a theorem: a
trained single-index predictor released with a known link costs an SQ extractor the
generative exponent of that link, never more than the trainer's when the labels are
a channel of the regression function, and twice the trainer's exponent for an
explicit law. The definition of a mapping is shortened and gets its transfer lemma.
The backdoor conjecture is split into three statements, as sol asked.

Papers read for this round, beyond round 00: CCGJY20 (Definitions 2 and 3,
Experiment 1, Observation 1, Proposition 1), FGRVX17 (Theorems 3.2, 3.7, 3.13, 3.16,
3.17, Lemma 3.10, Corollary 3.12), CDGJMMSTT21 (Appendix A.2 and A.3), DPLB24
(Proposition 3.7 with Appendix E.4). No new literature search was run.

Notation as in round 00. In addition: for a measurable $m:\mathbb R\to[-M,M]$ and
$\sigma>0$, $Q_{m,\sigma}$ is the law of $(Z,m(Z)+\sigma\xi)$ with $Z,\xi$ i.i.d.
$N(0,1)$; for a unit $w$, $P_w$ is the law of $(x,m(\langle w,x\rangle)+\sigma\xi)$
with $x\sim\gamma_d$; $P_0=\gamma_d\otimes(Q_{m,\sigma})_y$ is the product null.
$k^*(m)$ is the generative exponent of $(Z,m(Z))$ (DPLB24 Definition 2.4). The
$\beta_j$ are the Hermite coefficients of $m$, and $U_\rho$ is the Ornstein-Uhlenbeck
operator, $E[m(Z)m(Z')]=\sum_j\beta_j^2\rho^j$ for $\rho$-correlated standard
Gaussians.

## Responses to the challenges of round 00

`ch-sparse-pca-source` (blocking). Accepted. The sentence "Claim A.5 is true as
stated" is withdrawn. `fact-gkvz22-backdoor-scope` now says Appendix A contains a
parameter error, and `lem-sparse-pca-backdoor-width-price` gains part (d), sol's
counterexample to the activation condition, with its cause: the sketch's bound
$\sigma\ge\lambda\theta$ on the preactivation standard deviation omits the factor
$1/\sqrt{2\pi}$ of the mean ReLU.

`ch-sparse-pca-quantifiers` (blocking). Accepted. Part (c) is now stated for each
input and direction fixed independently of the weights, and uses the actual
standard deviation of the preactivation for both the mean and the deviation, as sol
suggested. It is restated as key insensitivity: the key buys a factor $\sqrt{1+\theta}$
in perturbation norm, and the price of not being detected is that this factor tends
to 1.

`ch-collision-parameters` (blocking). Accepted. Corollary 3 is stated with its
hypotheses ($\alpha\in[1/100,1)$, $\gamma\in[1,2^{n^{1/5}}]$, $B\le\mathrm{poly}(n)$).
Theorem 2's distance is stated only as the paper's own sentence: both divergences are
$o(1)$ when $m=\omega(1)$ and $m=o(n)$. The authors and venue are the library
record's, not established by the anonymous held copy.

`ch-encoding-normalization` (blocking). Accepted, and confirmed in Appendix A. The
proof of Theorem 4 bounds $\Pr[\text{accept}\mid x_0]-\Pr[\text{accept}\mid x_1]\ge0.99-\epsilon(n)/\gamma$,
which is twice the advantage of Definition 5. The proof of Theorem 5 bounds the same
kind of difference and prints "$\le\frac12-\epsilon(m)-\tau$" where its conclusion
needs "$\ge$". The fact now states both in Definition 5's units and counts training
runs and encoder calls separately.

`ch-mapping-price-types` (blocking). Accepted. The revised definition keeps prices
as budget vectors at fixed success levels, defines an exponent ratio only for a named
scalar resource on each side over a family indexed by $d$, and treats a VSTAT
parameter as an oracle parameter: a comparison of a VSTAT parameter with a sample
count is labelled heuristic. Low-degree reductions must state the degree they map
to. The round-00 table entry for `prop-sq-label-relevant-reconstruction-bound` said
"records to learn the task"; it now says "records to recover the hidden direction",
since `conj-reconstruction-at-training-cost` shows the two differ.

`ch-carrier-policy` (nonblocking). Accepted. The carrier is declared metadata with
no order and no composition rule. The rule of `CONTEXT.md` is stated as excluding a
mapping whose only hard instance is a key-dependent change the designer makes to the
procedure for security; an inherent hard object of a standard procedure counts,
which keeps BRV26 in.

`ch-extraction-game` (blocking). Accepted. The extractor's output must satisfy
$\lvert g\rvert\le1$, and weak fidelity is $\mathrm{Cov}(g(x),\hat f(x))\ge c_0\,\mathrm{sd}(\hat f(x))$.
The uniform bound defeats the scaling attack: a fixed-direction copy has covariance
$O(d^{-2})$ with the target. The detector built from an extractor uses centred
covariance. The full-fidelity score is the normalized error
$E[(Mg-\hat f)^2]/\mathrm{Var}\hat f$. The link is fixed and known, the trainer is
rotation equivariant, and the SQ lower bound and the sample-based upper bound are
separate parts of `thm-extraction-exponent-price`. The theorem covers the exact
release $m(\langle w,x\rangle)$; a fitted network that only approximates it is
outside, as sol warned.

`ch-feature-equivalence` (blocking). Accepted. The Gram statement is restricted to
ReLU features without offsets, for which the second moment of the features
determines the Gram matrix through the arc-cosine kernel, derived in
`prop-gram-sufficiency-rotation-invariant`. The precision with which $N$ probes or
statistical queries return the Gram matrix, and whether a given test survives that
precision, is left open there.

`ch-transpose-transfer` (blocking). Accepted. `lem-feature-matrix-transpose` keeps
the identity (no offsets) and transfers only the inversion statement: an auditor
that knows $N\ge2.1d$ Gaussian probes recovers every weight row, as the seed-known
server recovers every record. No transfer to detection or to key recovery is
claimed.

`ch-row-sq-transfer` (blocking). Accepted. The white-box statement
`prop-weight-testing-equals-white-box-detection` is sample-based, with the
auditor's sample count equal to the width $m$, and claims nothing for SQ auditors.
SQ lower bounds for NGCA are cited only as statements about SQ testers of the row
law. The Gram statement assumes a rotation-invariant prior on the key, which
excludes GKVZ22's sparse keys, and part (iii) of it says why that matters. The word
backdoor is reserved for a planted law with a proved trigger; the general statement
is about weight-law tampering.

`ch-extraction-catalogue` (nonblocking). Accepted. The fact now says the DGKP20
bound is on the product of the query count and the squared inverse tolerance or
advantage, that Lemma 17's linear function uses the teacher's weights and is no
learner, and that JCBKP20 Theorem 2 shows NP-hardness of inequivalence (coNP-hardness
of equivalence under many-one reductions).

`ch-defense-price` (nonblocking). Accepted. The multiplier is removed and the
construction of Corollary 5.2 is described instead.

Missing mappings. Added: `fact-active-learning-is-extraction` (CCGJY20 Observation
1 and Proposition 1). DPLB24 Proposition 3.7 is used inside
`thm-extraction-exponent-price` (it is in the pointer of the registers' entry for
`fact-generative-exponent-sq-recovery-bound`, so it gets no new slug).

Absence claims. Accepted. Each "no result" sentence of round 00 Part 3 reads "not
found within the scope of the cited search rows".

## Revised literature

### fact-jagielski-extraction-query-bounds: the price of extracting random and constructed networks
status: borrowed, revised
uses: none

JCBKP20 (USENIX Security 2020). Theorem 1 (formal in Appendix A, Definition A.1,
Lemmas 1 and 2): a class of width-$3k$ depth-2 ReLU networks on $[0,1]^d$ with
precision-$p$ inputs, $d\ge k$, needs $\Theta(p^k)$ logit queries for functionally
equivalent extraction, in the worst case over the class. Theorem 2 (Appendix A): by
a reduction from subset sum, deciding that two given networks on $\{0,1\}^d$ are
inequivalent is NP-hard, so equivalence is coNP-hard under many-one reductions.
Theorem 3 is informal, has no formal version, and imports DGKP20.

DGKP20 (held copy arXiv 1904.03866v1). With Gaussian rows (needed by Lemma 3
through Lemma 1, although Section 2 says uniform $[0,1]$ entries), sign activations,
inputs uniform on a halfspace of $\{\pm1\}^n$, and depth $h=o(\sqrt n)$ (Theorem 9,
with $O(\log\log n)$ burn-in layers and the residual terms $he^{-\Omega(n)}+de^{-\Omega(\sqrt n)}$),
Lemma 12 bounds the average squared correlation by $\lvert g\rvert_2^2/N+\lvert g\rvert_1^2e^{-h}$,
and Theorem 15 turns it into $p\max(r,q)^2\ge e^{\Omega(h)}$ for an SQ learner with
$p$ queries of tolerance $1/r$ reaching accuracy $1/2+1/q$. Theorems 16 (DGKP20) and
3 (JCBKP20) print $e^{O(h)}$; the derivation gives $e^{\Omega(h)}$. The bound
constrains the product of queries and squared inverse tolerance or advantage, not
the sample count by itself. Lemma 17's linear function $W^{(h+1)}\cdots W^{(1)}x$
has correlation $e^{-O(h)}$ but is built from the teacher's weights, so it shows the
correlation is reachable, not that a learner reaches it.

As a mapping: SQ learning of random deep sign networks $\lhd$ learning-based
fidelity extraction from random inputs, identity reduction, trainer's price none,
carrier the honest randomness of the weights, regime SQ. It says nothing about
extractors that choose their inputs.

Other regime. SQ only. JCBKP20 Section 6 extracts two-layer networks with chosen
queries outside SQ.

### fact-gkvz22-backdoor-scope: backdoors planted in the weight law of random features
status: borrowed, revised
uses: none

GKVZ22 (held copy arXiv 2204.06974v2). Definition 4.6 (white-box and black-box
undetectability by polynomial-time distinguishers with samples of $D$; statistic
access defined, not achieved). Theorem 6.4: under Assumption 6.3 (normalized head,
margin at least inverse polynomial on all inputs), with $d$, $1/\varepsilon$ and
$\log(1/\delta)$ polynomially related, Backdoor-RFF, which draws the random Fourier
features from the sparse Gaussian pancakes of Lemma 6.2 instead of $\gamma_d$, is a
$\gamma$-backdoor ($d^{1/c}$ in $\ell_0$, $2d^{1/2c}$ in $\ell_2$) with respect to
Train-RFF of width $m=\Theta(d\log(d/\varepsilon\delta)/\varepsilon^2)$, white-box
undetectable under Hypothesis 3.7; the reduction runs the head's training on the given
feature vectors. Lemma 6.6 derives the dense pancakes from BRST21's homogeneous CLWE
with $\gamma\ge2\sqrt d$. Theorem 5.4 (black box, signatures) is a primitive.

Appendix A contains a parameter error. Claim A.5 (random ReLU features drawn from
$N(0,I_d+\theta ss^\top)$, $s$ $d^\alpha$-sparse, $0<\alpha<1/2$, $\theta=O(1)$,
$\lambda>1/\theta$, unit-norm data, Lemma A.3 at $m=\Theta(d)$, Assumption A.4) fails at
its printed parameters in two ways, both proven in
`lem-sparse-pca-backdoor-width-price`: a coordinate-variance test detects the spike
for constant $\theta$, and the activation condition does not guarantee activation.

As mappings: hCLWE $\lhd$ white-box detection for Train-RFF, carrier the trainer's
choice, auditor's samples $m$ weight vectors; the converse is row reading
(`prop-weight-testing-equals-white-box-detection`). Appendix A gives no mapping.

Other regime. Polynomial time under Hypothesis 3.7. An unbounded auditor detecting
the pancake law at the widths of Train-RFF is heuristic (information threshold of
order $d$ up to logarithms, assumed).

### fact-frozen-gaussian-layer-collision-hardness: a frozen Gaussian layer carries a lattice problem
status: borrowed, revised
uses: none

BRV26, authors and ICML 2026 venue from the library record; the held copy is the
anonymous ICLR 2026 submission, whose numbering is used. Definition 5 (symmetric
bounded perceptron, SBP): on $A\sim N(0,1)^{m\times n}$ find
$x\in[-B:B]^n\setminus\{0\}$ with $\lVert Ax\rVert_\infty\le\kappa\sqrt n$. Assumption
2: no p.p.t. algorithm finds such $x$ with $\lVert Ax\rVert_\infty\le m^{-\varepsilon}$
except with negligible probability, for every $\varepsilon>0$ and $B,n\le\mathrm{poly}(m)$;
the paper says it holds if worst-case lattice problems are hard, citing Vafa and
Vaikuntanathan 2025 and Bogdanov et al. 2025 (not read). Theorem 2: BackdoorMatrix
outputs $A$ and a uniform $z\in\{\pm1\}^n$ with $\lVert Az\rVert_\infty\le O(\sqrt n\,2^{-n/m})$,
and both statistical divergences of $A$ from $N(0,1)^{m\times n}$ are $o(1)$ when
$m=\omega(1)$ and $m=o(n)$. Definition 6, Theorem 5 (models $g(Ax)$ with $g$
$(\alpha,\beta)$-bilipschitz, $m=n^{\Omega(1)}$, $m=o(n)$, strength
$\Omega(\alpha2^{n/m}/(\beta\sqrt n\,m^{1/2+\varepsilon}))$ under Assumption 2), Theorem 7
(depth-$d$ LeakyReLU$_\alpha$ networks with later condition numbers at most $\gamma$,
strength $\Omega(\alpha^d2^{n/m}/(\sqrt n\,m^{1/2+\varepsilon}\gamma^{d-1}))$). Corollary 3:
for $m=n^{1/2}$, $d=n^{1/4}$, $\alpha\in[1/100,1)$, $\gamma\in[1,2^{n^{1/5}}]$ and
$B\le\mathrm{poly}(n)$, strength $2^{\Omega(m)}$. Small $\alpha$ or large $\gamma$ destroys
the exponential strength.

As a mapping: SBP $\lhd$ collision finding against $g(Ax)$, by bilipschitzness, with
the coordinate bound doubled ($x_1-x_2\in[-2B:2B]^n$), the training operator efficient
and bilipschitz. Carrier: the honest randomness of the frozen layer.

Other regime. Collisions exist and exhaustive search finds them, so the hardness is
computational. The backdoor's undetectability is statistical.

### fact-instance-encoding-privacy-learnability: privacy of an instance encoding against learnability
status: borrowed, revised
uses: none

CDGJMMSTT21 (IEEE S&P 2021). Definition 5 measures advantage as success probability
minus $1/2$. Theorem 4 (rich class, encoded accuracy $(\epsilon,\delta)$): its proof
(Appendix A.2) bounds the difference of acceptance probabilities by
$0.99-\epsilon(n)/\gamma$, so the Definition-5 advantage is at least
$(0.99-\epsilon(n)/\gamma)/2$. The attack trains $m$ classifiers on $n$ encoded records
each, an expected $m/(1-\delta(n))$ training runs, with oracle access to $E(\cdot)$,
$L$, the concepts and a sampler of $D$. Theorem 5 (one balanced concept,
decomposable encoding, balanced encoded accuracy $(\epsilon,\delta)$): for every
$\tau$, either an attack with oracle access to $L$, $E$ and $D_c$ has Definition-5
advantage at least $(1/2-\epsilon(m)-\tau)/2$ (Appendix A.3 bounds the difference of
acceptance probabilities and prints the inequality reversed), repeating training runs
of $(E,L)$ on $m$ records until the balanced error is at most $\epsilon(m)$ and using
$k=-20\ln(\tau)/\tau^2$ encoder calls per prediction; or an efficient protocol learns
$c$ from $m$ samples to accuracy $1-\tau$.

As a mapping: if learning $c$ to accuracy $1-\tau$ from $m$ samples is hard, every
accurate decomposable instance encoding has an efficient distinguishing attack.
Carrier: none. Regime: polynomial time with oracles.

Other regime. The encoder oracle is what a seed-known split server has and a
seed-blind one lacks.

### fact-chlx25-defendability-characterization: backdoor defense against learnability
status: borrowed, revised
uses: none

CHLX25 (ITCS 2025). Definition 3.1, in which the detector also wins when the
attacker's $f^*$ is not $\varepsilon$-valid (the clause Theorem 5.3 exploits).
Theorem 4.1: best confidence $\max\{1/2,1-\Theta(\mathrm{VC}(F)\varepsilon)\}$ as
$\mathrm{VC}(F)\to\infty$. Corollary 5.2: efficient PAC learnability implies efficient
defendability (Definition 5.1); the detector runs the proof of Theorem 4.1 with the
PAC learner as prediction strategy at error and confidence $\delta/12$, a prediction
sample size large in $1/\varepsilon$ and in the learner's polynomial, and more than
$200\log(1/\delta)$ votes. Theorem 5.3 (random oracle model): defendable and not
learnable. Theorem 5.5: under OWF and iO, polynomial-size circuits are not
efficiently defendable.

As a mapping: detection $\lhd$ PAC learning, prices as in the construction. Theorem
5.5 is carried by obfuscation in the attacker's hands.

Other regime. Theorem 4.1 is statistical.

### fact-active-learning-is-extraction: query-synthesis active learning is extraction
status: borrowed
uses: none

Chandrasekaran, Chaudhuri, Giacomelli, Jha and Yan, USENIX Security 2020, key
CCGJY20, held copy arXiv 1811.02054v6. Definition 2: an active learning system in the
query-synthesis (QS) scenario learns every $f^*\in F$ to error $\varepsilon$ with
probability $1-\delta$ from $q_L(\varepsilon,\delta)$ membership queries. Experiment 1
and Definition 3: $\varepsilon$-extraction of complexity $q$ and confidence $\gamma$
against $F$. Observation 1: a QS active learner of query complexity
$q_L(\varepsilon,\delta)$ is an adversary implementing $\varepsilon$-extraction with
complexity $q_L(\varepsilon,\delta)$ and confidence $1-\delta$. Proposition 1: against
answers flipped with probability $\rho<1/2$, complexity
$\frac{8}{(1-2\rho)^2}q(\varepsilon,\delta)\ln\frac{q(\varepsilon,\delta)}\delta$ with
confidence $1-2\delta$.

As a mapping: extraction $\lhd$ QS active learning, with equal query budgets, chosen
inputs, carrier none. The converse is neither proved nor claimed by the authors.

Other regime. Information-free simulation; holds in every regime that contains the
learner.

### lem-sparse-pca-backdoor-width-price: the sparse-PCA backdoor is detected or the key buys almost nothing
status: proven
uses: fact-gkvz22-backdoor-scope

Statement. The construction of GKVZ22 Appendix A: honest weights $g_1,\dots,g_m$ i.i.d.
$\gamma_d$, backdoored weights i.i.d. $N(0,I_d+\theta ss^\top)$ with $s$ a $k$-sparse unit
vector and $0<\theta\le k$, classifier
$h(x)=\mathrm{sgn}(-\tau+A_m(x))$ with $A_m(x)=\frac1m\sum_j\mathrm{ReLU}(\langle g_j,x\rangle)$ and
$0<\tau\le1$, unit-norm data, activation $x\mapsto x+\lambda s$.

(a) Detection. The test $T(G)=1\{\max_{i\le d}\frac1m\sum_jg_{ji}^2\ge1+\theta/(2k)\}$, time
$O(md)$, has $\Pr_{\rm honest}[T=1]\le de^{-m\theta^2/(64k^2)}$ and
$\Pr_{\rm backdoor}[T=0]\le e^{-m\theta^2/(64k^2)}$, so its advantage is at least $3/4$
once $m\ge64k^2\ln(4(d+1))/\theta^2$.

(b) The undetected regime. If $T$ has advantage below $3/4$, then
$\theta<\theta_*:=8k\sqrt{\ln(4(d+1))/m}$; with Claim A.5's $\lambda>1/\theta$,
$\lambda k>\sqrt{m/(64\ln(4(d+1)))}$. At $m=\Theta(d)$ and $k=d^\alpha$, $\alpha<1/2$,
$\theta_*\to0$ polynomially and $\lambda\to\infty$ polynomially.

(c) Key insensitivity. Fix a unit $x$, a unit $u$ and $\lambda>0$ independently of the
weights, and let $x'=x+\lambda u$. Under either weight law let $\sigma'$ be the standard
deviation of $\langle g_1,x'\rangle$. Then $E A_m(x')=\sigma'/\sqrt{2\pi}$ and
$\Pr[\lvert A_m(x')-EA_m(x')\rvert\ge t\,EA_m(x')]\le2e^{-mt^2/(4\pi)}$. Under the honest
law $\sigma'=\lVert x'\rVert$; under the backdoored law
$\sigma'=\sqrt{\lVert x'\rVert^2+\theta\langle s,x'\rangle^2}\in[\lVert x'\rVert,\sqrt{1+\theta}\lVert x'\rVert]$.
For $x\perp s$, the backdoored network's mean response to the trigger $x+\lambda s$
equals the honest (and the backdoored) network's mean response to $x+\lambda'u$ for any
unit $u\perp x$, $u\perp s$, at $\lambda'=\lambda\sqrt{1+\theta}$. So a key-free
perturbation longer by the factor $\sqrt{1+\theta}$ does what the key does, and in the
undetected regime of (b) that factor is below $1+\theta_*/2$.

(d) The activation condition of Claim A.5 is insufficient. At $\theta=1$,
$\lambda=1.1$, $\tau=1$ and a unit $x\perp s$, Claim A.5's hypotheses hold (and the
proof's condition $\theta\ge c/\lambda$ with $c=1.1>\tau$), yet
$EA_m(x+\lambda s)=\sqrt{3.42/(2\pi)}\approx0.738<\tau$, so by (c) the trigger fails
with probability tending to 1 as $m$ grows, while $EA_m(x)=1/\sqrt{2\pi}\approx0.399<\tau$
keeps the clean input negative. In the large-$m$ limit, activation at $x\perp s$ needs
$\sqrt{1+\lambda^2(1+\theta)}>\sqrt{2\pi}\,\tau$.

Proof. (a) and (b) as in round 00, accepted line by line by sol: Laurent and
Massart's tail bounds for $\chi^2_m$ with $\eta=\theta/(2k)\le1/2$ and $t=m\eta^2/16$,
a union bound over coordinates under the honest law, and the coordinate $i^*$ with
$s_{i^*}^2\ge1/k$ under the backdoored law. (c) Write
$\langle g_j,x'\rangle=\sigma'\zeta_j$ with $\zeta_j$ i.i.d. $N(0,1)$ (this uses that $x'$
does not depend on the weights). Then $A_m=\sigma'\frac1m\sum_j\mathrm{ReLU}(\zeta_j)$ has
mean $\sigma'/\sqrt{2\pi}$ and is a $(\sigma'/\sqrt m)$-Lipschitz function of
$(\zeta_1,\dots,\zeta_m)$, so Gaussian concentration gives
$\Pr[\lvert A_m-EA_m\rvert\ge s]\le2e^{-ms^2/(2\sigma'^2)}$; put $s=t\sigma'/\sqrt{2\pi}$. The
variances are $x'^\top x'$ and $x'^\top(I+\theta ss^\top)x'$. For $x\perp s$ the trigger
gives $\sigma'^2=1+\lambda^2(1+\theta)$, and $x+\lambda'u$ with $u\perp x,s$ gives
$1+\lambda'^2$ under both laws; they agree at $\lambda'^2=\lambda^2(1+\theta)$. Finally
$\sqrt{1+\theta}\le1+\theta/2$. (d) $1+1.21\cdot2=3.42$; the rest is (c) with $t$ fixed
and $m\to\infty$. $\square$

What it means. GKVZ22's Appendix A gives no backdoor content. Either the auditor sees
the spike in time $O(md)$ from $m\ge64k^2\ln(4(d+1))/\theta^2$ weight vectors, or the
key's effect is a factor $\sqrt{1+\theta}<1+\theta_*/2$ in perturbation norm, which any
input-norm increase reproduces. The width of the trainer prices the trade-off: a
trainer who widens the layer for accuracy shrinks $\theta_*$. The detection threshold
agrees with the regime $\theta=o(k\sqrt{\log d/t})$ that Choudhary et al. (arXiv
2605.04209, Assumption 1) state for sparse-PCA hardness. Key insensitivity and the
activation counterexample were not found within the scope of
`search-sparse-pca-backdoor-regime`.

Other regime. (a) is polynomial time. Statistically the spike is visible from fewer
weight vectors, of order $k\log d/\theta^2$ (heuristic, the information threshold of
sparse PCA). No oracle.

## The definition of a mapping

### def-hard-problem-mapping: a mapping between an attack task and a hard problem
status: proposed, revised
uses: def-seed-access-modes, def-seed-blind-reconstruction-game

Statement. A *mapping* fixes the following, for a family indexed by a dimension $d$.

1. Procedure $\mathcal P$, with the cost meter of `def-seed-access-modes`. The trainer's
   budget is a vector $b_P$ (records, training runs, width, work).
2. Attack task $\mathcal T$: a game with a view (white-box release, representations,
   an evaluation interface on chosen or random inputs, statistical queries to a law the
   release determines, or $\mathsf{Train}$ calls), a success functional, a baseline, and
   the advantage as their difference. The adversary is a third party or a trainer who
   plants; for planting, the auditor's advantage is the quantity.
3. Hard problem $\Pi$: a distributional decision or search problem with a cited
   threshold, a set $B_\Pi(a)$ of budget vectors at which no solver of the stated regime
   reaches advantage $a$.
4. Direction and reduction. $\Pi\lhd\mathcal T$: an algorithm $\mathcal R$ with access to
   an attacker and to $\Pi$'s instance (samples or an oracle) that simulates the game
   without the secret, counting every training run it simulates, and maps the
   attacker's output to a $\Pi$-output. $\mathcal T\lhd\Pi$: the converse, a $\Pi$-solver
   turned into an attacker.
5. Prices. $p_A$ maps the attacker's budget and advantage $(b_A,a)$ to the solver's
   $(b_\Pi,a-\eta)$, monotone in each coordinate. $p_P$ states $b_P$ at the instance and,
   when $\mathcal P$ learns, the threshold of a named learning target (direction
   recovery, prediction to a stated risk), which are different targets.
6. Regime and its accounting. One of: population SQ, with each attacker query answered
   by a bounded number of queries to $\Pi$'s oracle whose VSTAT parameters are recorded
   in $p_A$; sample-based, with samples counted; low-degree, with the degree $D'$ of the
   composed test stated for each attacker degree $D$; polynomial time under a named
   assumption, with the overhead stated. A VSTAT parameter is an oracle parameter; a
   statement that compares it with a sample count is labelled heuristic. One mapping
   lives in one regime.
7. Exponent ratio. Defined only when the mapping names a scalar resource on each side,
   fixed success levels, and prices $d^{e_A+o(1)}$ and $d^{e_P+o(1)}$ with $e_P>0$; then
   it is $e_A/e_P$. With only bounds, it is the interval the bounds give.
8. Carrier, declared metadata with no order: the record law, the honest randomness of
   the procedure, the choice of a trainer who plants, or a key-dependent change the
   designer makes for security. A mapping whose only hard instance is of the last kind
   does not count (`CONTEXT.md`); an inherent hard object of a standard procedure counts.
9. Experiment: a finite instantiation with its measured budgets and the training runs it
   costs.

What it settles. With `lem-mapping-transfer`, every entry of the table below fills the
nine fields; the entries of rounds 00 and 01 are its instances.

| mapping | $\Pi$ | direction | trainer's price | attacker's price | regime | carrier |
| --- | --- | --- | --- | --- | --- | --- |
| `thm-blind-split-seed-separation` | hCLWE, NGCA | $\Pi\lhd\mathcal T$ | one run | $\exp(\Omega(c_0^4d))$ queries (SQ), or quantum lattice | SQ; polynomial time | record law |
| `prop-sq-label-relevant-reconstruction-bound` | single-index, $k^*\ge3$ | $\Pi\lhd\mathcal T$ | records to recover the direction, $O(d^{k^*/2})$ | VSTAT$(c\,d^{k^*/2})$ | SQ | record law |
| `lem-sq-learner-post-processing`, `prop-learner-side-sq-transfer` | planted biclique; any SQ-hard test | $\Pi\lhd\mathcal T$ | 1-STAT calls | binds unbounded attackers | trainer SQ | record law |
| `fact-cohen-narcissus-equals-one-wayness` | inverting $f$ | both | none | polynomial time | polynomial time | the procedure |
| `fact-jagielski-extraction-query-bounds` | SQ learning of random nets | $\Pi\lhd\mathcal T$ | none | $p\max(r,q)^2\ge e^{\Omega(h)}$ | SQ | honest randomness |
| `fact-gkvz22-backdoor-scope` (RFF) | hCLWE | $\Pi\lhd\mathcal T$ | one run, width $m$ | $m$ weight vectors, polynomial time | polynomial time | trainer's choice |
| `fact-frozen-gaussian-layer-collision-hardness` | SBP | $\Pi\lhd\mathcal T$ | one run | polynomial time | polynomial time | honest randomness |
| `fact-instance-encoding-privacy-learnability` | learning $c$ | dichotomy | $m$ records | $O(m/\delta+m/\tau^2)$ oracle time | polynomial time | none |
| `fact-chlx25-defendability-characterization`, `fact-active-learning-is-extraction` | PAC or QS learning | $\mathcal T\lhd\Pi$ | none | learner's budget | as the learner | none |
| `thm-extraction-exponent-price` | single-index, $k^*(m)$ | both | $O(d^{\max(1,k^*(P)/2)})$ records | VSTAT$(c\,d^{k^*(m)/2})$; $O(d^{k^*(m)/2})$ samples | SQ; sample-based | record law |
| `prop-weight-testing-equals-white-box-detection` | NGCA test of the planted law | both, exact | one run, width $m$ | $m$ samples | sample-based, any class | trainer's choice |

Other regime. Without the oracle a reduction counts its simulated runs as training
runs; with the oracle it counts $\mathsf{Train}$ calls and names its seed mode.

### lem-mapping-transfer: a mapping transfers thresholds
status: proven
uses: def-hard-problem-mapping

Statement. Let $\Pi\lhd\mathcal T$ in regime $R$ with price map $p_A$ and loss $\eta$, and
let $B_\Pi(a)$ be the cited set of solver budgets at which no $R$-solver reaches
advantage $a$. Then every $R$-attacker with advantage at least $a+\eta$ has a budget
$b_A$ with $p_A(b_A)\notin B_\Pi(a)$. If $\mathcal T\lhd\Pi$ with price map $q$ and loss
$\eta'$, a solver with budget $b$ and advantage $a$ gives an attacker with budget $q(b)$
and advantage $a-\eta'$.

Proof. The reduction applied to the attacker is, by item 6 of the definition, an
$R$-solver of budget $p_A(b_A)$ and advantage at least $a$; if $p_A(b_A)\in B_\Pi(a)$
this contradicts the cited threshold. The second part is the definition read
forward. $\square$

Other regime. The lemma is regime-free: it holds in each regime separately and never
across two.

### prop-learner-side-sq-transfer: an SQ bound on testing binds every attacker of a 1-bit learner
status: proven
uses: lem-mapping-transfer, lem-sq-learner-post-processing

Statement. Let a procedure reach its records only through $m$ calls to 1-STAT (each
call evaluates a Boolean function, chosen adaptively, on one fresh record), with coins
independent of the record law, and let any randomized map, unbounded and white-box, read
its output. Let $B(\mathfrak D,D_0)$ be the decision problem of telling $D_0$ from the
members of $\mathfrak D$ (property inference on the training law). (a) If every SQ
algorithm that solves $B$ with probability $\alpha-\delta$ needs more than $q$ queries to
VSTAT$(t)$, then every procedure-attacker pair that solves $B$ with probability $\alpha$
has $m\ge\min\{q,\delta^2t\}$, for any $\delta\in(0,1/4]$. (b) In terms of the statistical
dimension with average correlation, $m\ge\min\{d(2\alpha-1)/2,(2\alpha+1)^2/(48\bar\gamma)\}$
with $d=\mathrm{SDA}(B,\bar\gamma)$.

Proof. The composition of the procedure and the attacker is a 1-bit sampling algorithm
with $m$ calls, since the attacker draws no record. (b) is FGRVX17 Theorem 3.16 applied
to it. (a) By FGRVX17 Theorem 3.13 it is simulated by an SQ algorithm with $m$ queries to
VSTAT$(m/\delta^2)$ and success $\alpha-\delta$. If $m<q$ and $m/\delta^2\le t$, every answer
valid for VSTAT$(t)$ is valid for VSTAT$(m/\delta^2)$, so the adversarial oracle of the
cited bound defeats the simulation, a contradiction. $\square$

Instances. Planted biclique with FGRVX17 Theorem 2.10 gives `lem-sq-learner-post-processing`.
NGCA with four matched moments (`fact-ngca-sq-lower-bound`) and the detection form of the
single-index problem (step 3 of the proof of `thm-extraction-exponent-price`, with
$t=c\,d^{k^*/2}$) give property-inference bounds of the same kind: a 1-bit learner whose
attacker detects a planted single-index structure of exponent $k^*$ makes at least
$c\,\delta^2d^{k^*/2}$ calls.

Other regime. The bound is unconditional and binds unbounded attackers, because the
restriction is on the procedure. It says nothing about procedures that read their records
in full, the refuted note's lesson (`thm-fs-sq-black-box-reduction`).

## Extraction priced by the model's own link

### lem-level-set-moment-balance: the level sets of |z| phi(z) carry the Gaussian's first two moments
status: proven
uses: none

Statement. Let $Z\sim\gamma_1$ and $G(r)=r\phi(r)$ for $r\ge0$. For $t\in(0,G(1))$ let
$a<1<b$ be the two solutions of $G(r)=t$, and $A=1-a^2$, $B=b^2-1$. Conditionally on
$G(\lvert Z\rvert)=t$, $Z$ takes the values $\pm a$ with total probability $B/(A+B)$ and
$\pm b$ with total probability $A/(A+B)$, signs equally likely. Hence
$E[Z\mid t]=E[Z^3\mid t]=0$, $E[Z^2\mid t]=1$, $E[Z^4\mid t]=1+AB$, so
$E[h_j(Z)\mid t]=0$ for $j=1,2,3$ and $E[h_4(Z)\mid t]=(AB-2)/\sqrt{24}$. Consequently
$m_\natural(z)=\lvert z\rvert e^{-z^2/2}$ has $k^*(m_\natural)=4$.

Proof. $G'(r)=\phi(r)+r\phi'(r)=\phi(r)(1-r^2)$, so $G$ increases strictly on $[0,1]$,
decreases strictly on $[1,\infty)$, and $G(0)=\lim_{r\to\infty}G(r)=0$. By the change of
variables on each monotone branch, for bounded $u$,
$E[u(Z)\mid G(\lvert Z\rvert)=t]$ averages $u$ over $\{\pm a,\pm b\}$ with weights
proportional to $\phi(r)/\lvert G'(r)\rvert=1/\lvert1-r^2\rvert$, that is $1/A$ at $\pm a$
and $1/B$ at $\pm b$, normalized to $B/(A+B)$ and $A/(A+B)$. Then
$E[Z^2\mid t]=\frac{(1-A)B+(1+B)A}{A+B}=1$ and
$E[Z^4\mid t]=\frac{(1-A)^2B+(1+B)^2A}{A+B}=\frac{(A+B)(1+AB)}{A+B}=1+AB$. Odd moments vanish
by symmetry. With $h_4=(z^4-6z^2+3)/\sqrt{24}$ the stated value follows; as $t\to0$,
$A\to1$ and $B\to\infty$, so it is not almost surely zero. Since $m_\natural=\sqrt{2\pi}\,G(\lvert z\rvert)$
has these level sets, $\zeta_j=0$ for $j\le3$ and $\lambda_4>0$ for $(Z,m_\natural(Z))$.
This agrees with DPLB24 Example 2.7 (ii) and Corollary 2.8, as $m_\natural^2=z^2e^{-z^2}$.
A numerical check at $t\in\{0.01,0.05,0.1,0.2,0.24\}$ returned $E[Z^2\mid t]=1$ to ten
digits and $E[Z^4\mid t]=1+AB$ (empirical, a scratch computation). $\square$

The identity $\frac{d}{dr}(r\phi(r))=\phi(r)(1-r^2)$ is the whole argument: the
Jacobian weights of a level set are the reciprocals of $1-a^2$ and $b^2-1$, which is
exactly what balances the second moment.

Other regime. A statement about one law; regime-free.

### thm-extraction-exponent-price: extraction costs the generative exponent of the released link
status: proven
uses: lem-level-set-moment-balance, fact-generative-exponent-post-processing-monotone, fact-generative-exponent-sq-recovery-bound, def-hard-problem-mapping

Setting. A trainer releases $\hat f(x)=m(\langle w,x\rangle)$ for a known measurable
$m:\mathbb R\to[-M,M]$, not almost everywhere constant, and a unit $w$. The extraction
game $\Gamma_{\rm ext}(\sigma)$, $\sigma>0$ fixed: the interface answers random inputs
$x\sim\gamma_d$ with $\hat f(x)+\sigma\xi$. In the SQ game the extractor's queries
$h:\mathbb R^d\times\mathbb R\to[0,1]$ are answered by VSTAT$(n)$ on $P_w$; in the sample game
it receives $n$ answered pairs. It outputs $g:\mathbb R^d\to[-1,1]$ and has weak fidelity
$c_0$ if $\mathrm{Cov}(g(x),\hat f(x))\ge c_0\,\mathrm{sd}(m(Z))$. Let $k=k^*(m)$.

(a) SQ lower bound. Fix $m$, $\sigma$, $c_0\in(0,1]$ and $r\ge1$. There are $c>0$ and $d_0$
such that for $d\ge d_0$ every SQ extractor that reaches weak fidelity $c_0$ with
probability at least $2/3$, when $w$ is uniform on $S^{d-1}$, with at most $d^r$ queries
to VSTAT$(n)$, has $n\ge c\,d^{k/2}$.

(b) Sample-based upper bound. With
$n\ge C_k[d^{k/2}/\tilde\lambda_k^2+d/(\tilde\lambda_k^2\epsilon^2)]+O(\eta^{-2})$ answered pairs,
where $\lambda_k=\lambda_k(Q_{m,\sigma})>0$ and $\tilde\lambda_k=\lambda_k/\log^k(3/\lambda_k)$, the
extractor that runs DPLB24's Algorithm 1 and then fixes the sign outputs $g=m(\langle\hat w,x\rangle)/M$
with normalized error $E[(Mg-\hat f)^2]/\mathrm{Var}\hat f\le\eta$ with probability
$1-2e^{-d^{c'}}$, where $\epsilon=\epsilon(\eta,m)$; for $c_0<\mathrm{sd}(m(Z))/M$ this is weak
fidelity $c_0$ once $\eta$ is small.

(c) Channel inequality. If the training labels satisfy $Y=\kappa(m_P(Z),\xi')$ for a
measurable $\kappa$ and $\xi'$ independent of $Z$, with $E[Y^2]<\infty$, then
$k^*(m_P)\le k^*(P)$. Extracting the Bayes predictor then never needs a larger exponent
than recovering the direction from labels.

(d) Separation. For $P_\natural$, the law of $(Z,Z\varepsilon)$ with
$\Pr[\varepsilon=1\mid Z]=(1+\mathrm{sgn}(Z)e^{-Z^2/2})/2$ (independent symmetric label noise
allowed), $k^*(P_\natural)=2$ and $m_{P_\natural}=m_\natural$, $k^*(m_\natural)=4$. A
rotation-equivariant trainer running DPLB24's Algorithm 1 at $k=2$ recovers $\hat w$ with
$(\hat w\cdot u)^2\ge1-\epsilon^2$ from $O(d(1+\epsilon^{-2}))$ records and releases
$m_\natural(\langle\hat w,x\rangle)$; extracting that release needs VSTAT$(c\,d^2)$ by (a) and
$O(d^2)$ answered pairs suffice by (b).

Proof of (a). Step 1, the noisy law. $Q_{m,\sigma}\in\mathcal G$, and
$k^*(Q_{m,\sigma})=k$ by DPLB24 Theorem 5.2. Its $\chi^2$ information is finite: for
$\lvert a\rvert,\lvert b\rvert\le M$,
$\phi_\sigma(y-a)/\phi_\sigma(y-b)=\exp((a-b)(2y-a-b)/(2\sigma^2))\le\exp(2M(\lvert y\rvert+M)/\sigma^2)=:\psi(y)$,
so $dQ_{m,\sigma}/d(\gamma_1\otimes(Q_{m,\sigma})_y)\le\psi(y)$ and
$1+I_{\chi^2}\le E[\psi(Y)^2]<\infty$, $Y$ having Gaussian tails. Put
$\beta_c=I_{\chi^2}[Q_{m,\sigma}]$ and $\lambda=\lambda_k(Q_{m,\sigma})$, constants in $d$.

Step 2, a code. By DPLB24 Lemma E.3 there are $N=d^\ell$ unit vectors with pairwise
$\lvert w_i\cdot w_j\rvert\le\epsilon:=\sqrt C\ell/\sqrt d$ (valid for $N\le d^{d^{1/4}}$). By
the series in the proof of Lemma E.2 (DPLB24 Lemma 3.1),
$\lvert\chi_{P_0}(P_{w_i},P_{w_j})\rvert\le\lambda^2\epsilon^k+\epsilon^{k+1}/(1-\epsilon)\le2\lambda^2\epsilon^k=:\gamma_c$
for $i\ne j$, once $\lambda^2\ge2\epsilon$ and $\epsilon\le1/2$; on the diagonal
$\chi_{P_0}(P_w,P_w)=\beta_c$ (Lemma 2.3).

Step 3, the decision bound. The set $\{P_{w_i}\}$ is $(\gamma_c,\beta_c)$-correlated
relative to $P_0$, so FGRVX17 Lemma 3.10 with $\gamma'=\gamma_c$ gives
$\mathrm{SDA}(B,2\gamma_c)\ge N\gamma_c/(\beta_c-\gamma_c)$, and FGRVX17 Theorem 3.7: an SQ
algorithm telling $P_0$ from a uniform member of the code with success $\alpha>1/2$ needs
at least $(2\alpha-1)N\gamma_c/\beta_c$ queries to VSTAT$(1/(6\gamma_c))$, hence to any
VSTAT$(t)$ with $t\le1/(6\gamma_c)$ (its answers include those of VSTAT$(1/(6\gamma_c))$).

Step 4, from fidelity to detection. Given the oracle of $P_{w_i}$ or $P_0$, draw a Haar
$R$ and answer each extractor query $h$ by querying $h(Rx,y)$, a valid VSTAT answer for
$h$ under $P_{Rw_i}$ (or $P_0$, which is rotation invariant); $Rw_i$ is uniform. Let $g$ be
the output and $\tilde g(x)=g(Rx)$, so $\mathrm{Cov}(\tilde g(x),m(\langle w_i,x\rangle))$ equals
the extractor's covariance. Then make three queries, the rescalings to $[0,1]$ of
$\tilde g(x)$, $\mathrm{clip}_L(y)$ and $\tilde g(x)\mathrm{clip}_L(y)/L$, at VSTAT$(n_1)$, and
declare "planted" iff the estimated covariance exceeds $c_0\,\mathrm{sd}(m(Z))/2$. Under $P_0$,
$y$ is independent of $x$ and the covariance is 0. Under $P_{w_i}$,
$\mathrm{Cov}(\tilde g,\mathrm{clip}_L(y))\ge c_0\,\mathrm{sd}(m(Z))-2e(L)$ with
$e(L)=\sup_{\lvert a\rvert\le M}E\lvert a+\sigma\xi-\mathrm{clip}_L(a+\sigma\xi)\rvert\to0$. Each
answer errs by at most $1/\sqrt{n_1}$, so the estimate errs by at most $8L/\sqrt{n_1}$.
Choosing $L$ with $e(L)\le c_0\,\mathrm{sd}/8$ and $n_1=\lceil(64L/(c_0\,\mathrm{sd}))^2\rceil$,
constants in $d$, the detector is right on $P_0$ always and on $P_{w_i}$ whenever the
extractor succeeds, so $\alpha\ge5/6$. It makes $q+3$ queries to VSTAT$(n')$,
$n'=\max(n,n_1)$, whose answers are valid VSTAT$(n)$ answers for the extractor.

Step 5. Take $\ell=r+k/2+1$. If $n'\le1/(6\gamma_c)$, Step 3 requires
$q+3\ge\frac23N\gamma_c/\beta_c=\frac43\lambda^2C^{k/2}\ell^kd^{r+1}/\beta_c$, which exceeds
$d^r+3$ for $d$ large. So $n'>1/(6\gamma_c)=d^{k/2}/(12\lambda^2C^{k/2}\ell^k)$; as $n_1$ is a
constant, $n'=n$ for $d$ large. The conditions $\epsilon\le1/2$, $\lambda^2\ge2\epsilon$ and
$N\le d^{d^{1/4}}$ hold for $d$ large. Hence $n\ge c\,d^{k/2}$ with
$c=1/(12\lambda^2C^{k/2}\ell^k)$. $\square$

Proof of (b). DPLB24 Theorem 4.1 applies to $P_w$, a Gaussian single-index model with
$k^*=k$ and $\lambda_k>0$ (Step 1), with the denoiser for $Q_{m,\sigma}$, which the
extractor can compute since $m$ and $\sigma$ are known. It returns $\hat w$ with
$(\hat w\cdot w)^2\ge1-\epsilon^2$ with probability $1-2e^{-d^{c'}}$. Let $\rho=\hat w\cdot w$.
Then $E[(m(\langle\hat w,x\rangle)-m(\langle w,x\rangle))^2]=2\sum_{j\ge1}\beta_j^2(1-\rho^j)$, which
tends to 0 as $\rho\to1$ by dominated convergence ($\sum\beta_j^2<\infty$), and equals the
same with $-\rho$ after the sign flip; $O(\eta^{-2})$ further pairs choose the sign of
larger empirical covariance (unnecessary for even $m$). $\square$

Proof of (c). $Z\to m_P(Z)\to Y$ is a Markov chain and $E[m_P(Z)^2]\le E[Y^2]<\infty$, so
the remark after DPLB24 Proposition 2.6 gives $k^*(Z,Y)\ge k^*(Z,m_P(Z))$. $\square$

Proof of (d). The map $(z,y)\mapsto(-z,y)$ preserves $P_\natural$ (round 00, accepted), so
$\zeta_j=0$ for odd $j$; $\lvert Y\rvert=\lvert Z\rvert$ gives $\zeta_2(Y)=(Y^2-1)/\sqrt2$, $\lambda_2=1$
(with symmetric noise $T(y)=y^2$ keeps $E[T(Y)h_2(Z)]=\sqrt2$), so $k^*(P_\natural)=2$, and
$E[Y\mid Z]=\lvert Z\rvert e^{-Z^2/2}$. $k^*(m_\natural)=4$ is `lem-level-set-moment-balance`.
DPLB24 Theorem 4.1 at $k=2$ gives the trainer's rate. Algorithm 1 is rotation equivariant
(it applies the denoiser to labels and Hermite tensors to inputs), so for $u$ uniform the
law of $\hat w$ is rotation invariant, $\hat w$ is uniform, and (a) applies to the release
with $k=4$. (b) gives the upper bound. $\square$

The mapping, in the fields of `def-hard-problem-mapping`. Procedure: single-index
training with a known link and an equivariant estimator; task: learning-based fidelity
extraction from random inputs with noisy answers; $\Pi$: the single-index problem of
$Q_{m,\sigma}$, in both directions (by (a) and (b)), and through DPLB24 Proposition 3.7
the extractor's samples become NGCA samples of a law with exponent $k^*(m)$; regime: SQ
for the lower bound, sample-based for the upper; carrier: the record law (the label law
fixes the link). Exponent ratio for $P_\natural$, with the trainer's records against the
extractor's VSTAT parameter: at least $2$, since the trainer's exponent is at most 1 and
the extractor's at least 2; this compares a sample count with a VSTAT parameter, so it is
heuristic (`def-hard-problem-mapping`, item 6). The extractor's sample-based upper bound
$O(d^2)$ shows its exponent is exactly 2 under the same heuristic. A lower bound on the
trainer's records is not claimed. The extractor needs a larger exponent than the
trainer because the Bayes predictor averages out the sign that the labels carry: the
labels reveal $\lvert\langle u,x\rangle\rvert$, the release only a function whose level sets
hide the first three moments.

Experiment. $d\in\{32,64,128,256\}$; train Algorithm 1 at $k=2$ on $Cd\log d$ records of
$P_\natural$; release $m_\natural(\langle\hat w,x\rangle)$ exactly (the architecture is
enforced, sol's caveat); answer random Gaussian inputs with noise $\sigma$; run Algorithm 1
at $k=4$ and a gradient-trained student; record the answered pairs needed for weak
fidelity $c_0$. Prediction (heuristic): slope 1 for the trainer and 2 for the extractor in
$\log$-$\log$ coordinates. One training run per $d$, no oracle.

Other regime. Statistically the extractor needs $\tilde\Theta(d/(\lambda_4^2\epsilon^2))$ answered
pairs (DPLB24 Theorem 6.1), so the gap is computational. With chosen inputs the release
gives $w$ coordinate by coordinate, an extraction $\lhd$ query-synthesis mapping of the
kind of `fact-active-learning-is-extraction` (heuristic, not worked out), so the
separation is a statement about learning-based extraction only.

### conj-extraction-priced-by-generative-exponent: extraction costs the generative exponent of the model's own link
status: withdrawn, superseded by thm-extraction-exponent-price
uses: thm-extraction-exponent-price

The conjecture of round 00 is proven for releases with a known link in the repaired game
(`thm-extraction-exponent-price`). Its open remainder, a fitted network that approximates
$m(\langle w,x\rangle)$ only in $L^2$, is not kept as an aim: the exact moment cancellations
need not survive the approximation.

Other regime. As for the theorem.

## Weight-law tampering, split into three statements

### prop-weight-testing-equals-white-box-detection: white-box detection of a planted weight law is testing the rows
status: proven
uses: fact-gkvz22-backdoor-scope

Statement. A random-feature release $(G,b,w)$: $G\in\mathbb R^{m\times d}$ with rows $g_j$,
offsets $b\sim\beta^{\otimes m}$ independent of $G$, head $w=H(G,b,S;\omega)$ with
$S\sim D^n$ and coins $\omega$ independent of $G$. Under $H_0$ the rows are i.i.d.
$\gamma_d$; under $H_1$ they are i.i.d. $P^A_s$ with $s$ drawn from a prior $\pi$ on
$S^{d-1}$. Let $\mathcal C$ be a class of algorithms that can sample $\beta$, $D$ and
$\omega$ and run $H$ (for instance all algorithms, or polynomial-time ones when $H$ is
efficient and $D$ samplable). Then the best advantage in $\mathcal C$ of telling $H_0$ from
$H_1$ given $(G,b,w)$ equals the best advantage in $\mathcal C$ of telling
$\gamma_d^{\otimes m}$ from $E_{s\sim\pi}(P^A_s)^{\otimes m}$ given $m$ samples.

Proof. Given $m$ samples, use them as $G$, draw $b$, $S$, $\omega$, compute $w$: the triple
has exactly the release's law under each hypothesis (GKVZ22's argument in Theorem 6.4,
for any $A$). Given a release, discard $(b,w)$ and pass $G$. Both maps preserve
advantages and stay in $\mathcal C$. $\square$

What it says. The auditor's sample count is the trainer's width $m$, and the
detection price of every planted weight law is its NGCA testing price at $m$ samples. It
is a statement about weight-law tampering. A backdoor also needs a trigger with a proved
effect; in this catalogue only GKVZ22's pancake law has one (Theorem 6.4).

Other regime. Sample-based; it holds in every algorithm class closed as stated. SQ
lower bounds for NGCA (`fact-ngca-sq-lower-bound`) concern SQ testers of the row law and
transfer to this auditor only under the heuristic that VSTAT$(m)$ models $m$ samples.

### prop-gram-sufficiency-rotation-invariant: for a uniform key the Gram matrix is all the auditor needs
status: proven
uses: prop-weight-testing-equals-white-box-detection

Statement. In the setting above let $\pi$ be uniform on $S^{d-1}$. (i) For every test
$T(G,b)$, the randomized test that computes $F$ with $FF^\top=GG^\top$, draws a Haar
$R\in O(d)$ and returns $T(FR,b)$ has the same advantage, and runs in polynomial time
given $GG^\top$. (ii) For $\sigma=\mathrm{ReLU}$ and $b=0$, the second moment
$\Gamma=E_{x\sim\gamma_d}[\varphi(x)\varphi(x)^\top]$ determines $GG^\top$:
$\Gamma_{jj}=\lVert g_j\rVert^2/2$ and $\Gamma_{jk}=\lVert g_j\rVert\lVert g_k\rVert\kappa(\theta_{jk})$
with $\kappa(\theta)=(\sin\theta+(\pi-\theta)\cos\theta)/(2\pi)$ strictly decreasing on
$[0,\pi]$. So an auditor that sees only the law of the features on unknown Gaussian inputs
detects exactly as well as the white-box auditor. (iii) Rotation invariance of the prior is
needed: for GKVZ22's $k$-sparse keys the coordinate test of
`lem-sparse-pca-backdoor-width-price` uses the frame, which $GG^\top$ does not carry.

Proof. (i) If $FF^\top=GG^\top$ with $F,G\in\mathbb R^{m\times d}$, then $F=GQ_0$ for some
$Q_0\in O(d)$ (equal Gram matrices give equal singular values and left singular vectors on
the range, and the right factors differ by an orthogonal map, extended to $O(d)$ when the
rank is below $d$). Given $G$, $Q_0R$ is Haar. Under $H_0$, $GQ\overset d=G$ for every
fixed $Q\in O(d)$; under $H_1$, the rows of $GQ$ are i.i.d. $P^A_{Q^\top s}$ and $Q^\top s$ is
uniform. So $(H,FR,b)\overset d=(H,G,b)$ for the hypothesis $H$, and the advantage is
unchanged. $F$ comes from an eigendecomposition of $GG^\top$. (ii) For unit $e,e'$ at
angle $\theta$ in $\mathbb R^2$ and $\zeta\sim\gamma_2$, in polar coordinates
$\zeta=\rho(\cos\phi,\sin\phi)$ the product $(\zeta\cdot e)_+(\zeta\cdot e')_+$ is nonzero for $\phi$ in an
arc of length $\pi-\theta$, and
$E[(\zeta\cdot e)_+(\zeta\cdot e')_+]=\frac1{2\pi}\int_0^\infty\rho^3e^{-\rho^2/2}d\rho\int_{\theta-\pi/2}^{\pi/2}\cos\phi\cos(\phi-\theta)\,d\phi=\frac1{2\pi}\cdot2\cdot\frac{\sin\theta+(\pi-\theta)\cos\theta}2$.
Scaling by the norms gives $\Gamma$. $\kappa'(\theta)=-(\pi-\theta)\sin\theta/(2\pi)<0$ on
$(0,\pi)$, so $\Gamma$ determines every norm and angle, hence $GG^\top$; then (i). (iii) is
the remark that the white-box statistic of that lemma is not a function of $GG^\top$; no
lower bound for Gram auditors is claimed. $\square$

Open. How many probes, or which SQ tolerance, return $GG^\top$ to a precision that a given
test survives. The derivative $\kappa'(\pi/2)=-1/4$ makes angles near $\pi/2$, typical of
Gaussian rows, well conditioned (heuristic), but the precision a test needs depends on
the planted law: noiseless pancakes are broken by lattice reduction from exact rows
(`fact-lll-beats-sos-noiseless`), which a perturbed factor may defeat.

Other regime. (i) and (ii) are exact and regime-free. The same identity appears for split
clients in round 03 of statistical-limits (`prop-relu-client-second-moment-identifies-weights`,
sketch there).

### lem-feature-matrix-transpose: an auditor of a planted layer is a split server, transposed
status: proven
uses: def-seed-blind-reconstruction-game, fact-lei-random-expansive-layers-invertible

Statement. For any $\sigma:\mathbb R\to\mathbb R$ applied entrywise and matrices
$G\in\mathbb R^{m\times d}$, $X\in\mathbb R^{N\times d}$, $\sigma(GX^\top)^\top=\sigma(XG^\top)$. So if
$G$ has i.i.d. rows from $P^A_s$ and $X$ i.i.d. rows from $\gamma_d$, the auditor's feature
matrix $\sigma(GX^\top)$ (column $i$ the features of probe $x_i$) is the transpose of the
representation matrix of a split server whose Gaussian client of width $N$, without
offsets, received $m$ records from $P^A_s$. Under this dictionary the probes are the
client's weights, the weight rows are the records, an auditor who knows its probes is a
seed-known server, and one who sees features on unknown inputs is a seed-blind server.
For $\sigma=\mathrm{ReLU}$ and $N\ge2.1d$, an auditor who knows its Gaussian probes recovers
every row $g_j$ exactly by layer-wise linear equations, with probability at least
$1-me^{-\Omega(d)}$, as the seed-known server recovers records
(`fact-lei-random-expansive-layers-invertible`).

Proof. $(\sigma(GX^\top))_{ji}=\sigma(\langle g_j,x_i\rangle)=(\sigma(XG^\top))_{ij}$. The law
statement is the definition of the two games with the roles of the factors exchanged. For
the inversion, each row $g_j$ is independent of $X$ and $\sigma(Xg_j)$ is the output of one
random expansive ReLU layer at input $g_j$, so LJDD19's guarantee applies to each $j$, and
a union bound over the $m$ rows gives the probability. $\square$

What it does not say. It transfers no detection or key-recovery statement: recovering the
rows leaves the planted direction as hidden as the white-box auditor finds it, and the
first milestone's seed-known inversion reconstructs records, not a direction inside their
law (sol, `ch-transpose-transfer`).

Other regime. The identity is exact. The inversion is polynomial time and needs the probes.

### conj-backdoor-detection-is-ngca: detection of a weight-law backdoor is NGCA at the trainer's width
status: withdrawn, replaced by prop-weight-testing-equals-white-box-detection, prop-gram-sufficiency-rotation-invariant, lem-feature-matrix-transpose
uses: prop-weight-testing-equals-white-box-detection

Part (a) of round 00 is `prop-weight-testing-equals-white-box-detection`. Part (b) holds
for ReLU without offsets and uniform keys (`prop-gram-sufficiency-rotation-invariant`)
and is false for activations that erase the weights (sol's constant activation). Part (c)
keeps only the identity and the inversion (`lem-feature-matrix-transpose`). Part (d)'s SQ
clause is dropped.

Other regime. As for the three statements.

## Questions for the discussant

1. Does Step 4 of the proof of `thm-extraction-exponent-price` (a) correctly turn weak
   fidelity with $\lvert g\rvert\le1$ into a decision procedure, and does Step 5 respect the
   hypotheses of FGRVX17 Theorem 3.7 and Lemma 3.10?
2. Is the separation of part (d) right as a statement about the trainer's records against
   the extractor's VSTAT parameter, and is the heuristic label on the ratio the right one?
3. Does `lem-sparse-pca-backdoor-width-price` now read GKVZ22 Appendix A fairly, and do its
   quantifiers hold?
4. Is the revised definition well posed, and is the table a faithful reading of each
   entry?
