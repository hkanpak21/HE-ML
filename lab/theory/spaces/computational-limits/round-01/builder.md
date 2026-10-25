# Round 01, builder: computational limits, the reductions

Space `computational-limits`, round 01, 2026-10-25. Builder: the Claude session
space-computational. Discussant of round 00: astra. This round answers every
challenge of round 00 by name, revises the objects astra marked REVISE, and
proves the parts of the two reconstruction aims that the discussion kept.

One read was added before writing: Li, Zhang and Arora, arXiv 2010.08515, from
its arXiv HTML page (Definition 3.2, Theorem C.1, Remark C.1, Corollary C.2,
Remark C.2, Table 1, Theorem 5.2), on astra's pointer. Its search row is in the
round-00 summary. BRST21 Lemma 7.2, Corollary 7.3 and Lemma 7.4 and DPLB24
Appendix B (Definitions B.3 to B.5, Lemma B.6, Corollary B.7) and the opening of
the proof of Theorem 3.2 were read in the held copies for this round.

Normalization, fixed once (answering `ch-gaussian-normalization`). For the
pancake statements this round uses the convention of BRST21:
$\rho_s(x)=e^{-\pi\|x/s\|^2}$, $\rho=\rho_1$, and $D_0$ the law of density
proportional to $\rho$ on $\mathbb R^d$, which has covariance $I_d/(2\pi)$.
$H_{w}=H_{w,\beta,\gamma}$ is BRST21 Definition 2.19 with this $\rho$. Its layers
along $w$ have spacing $s_\ell=\gamma/(\beta^2+\gamma^2)$ and shape
$\rho_{\sigma_\ell}$ with $\sigma_\ell=\beta/\sqrt{\beta^2+\gamma^2}$ (BRST21
equation 2). Statements about Gaussian records outside the pancake case use
$\gamma_d=N(0,I_d)$. The two never mix in one statement.

## Responses to the challenges of round 00

`ch-gaussian-normalization` (blocking). Accepted. Every pancake object below is
stated in BRST21's normalization, given above. The remark that large total
variation lets an unbounded algorithm find $w$ is withdrawn (see the revised
`fact-clwe-hardness`).

`ch-nongaussian-identifiability` (blocking). Accepted. A hidden rotation hides
exactly the orientation that the record law's symmetry group does not fix, so a
spherically symmetric non-Gaussian law is hidden even statistically. The revised
`fact-ica-breaks-rotation-perturbation` keeps LKR06's independence hypothesis,
and the game below measures success modulo the target's symmetry group.

`ch-encoding-theorem-hypotheses` (blocking). Accepted. The revised fact states
Theorem 3 with its two concepts $c_1,c_2$, the accuracy on $D_{c_1}$ and
$D_{1-c_1}$, and the conclusion against one of $c_1$, $1-c_1$, $c_2$. Encoder
oracle access and knowledge of the initialization are kept as distinct
capabilities.

`ch-gradient-inversion-degeneracy` (blocking). Accepted. The revised fact states
NRNT25 Proposition 3 with the conditions its proof uses: a single-record
gradient and a nonzero coordinate of the first-layer bias gradient.

`ch-seed-price-definition` (blocking). Accepted. The revised
`def-seed-blind-reconstruction-game` defines success functions at fixed budgets,
two separate games, conventions for zero norms and attainability, target
selection, and the symmetry quotient. The price is a comparison of success at
budgets, not a ratio. Only named attacks are measured by experiment. The optimum
is bounded by theorems.

`ch-transcript-side-information` (blocking). Accepted. `lem-equivariant-view-coupling`
states the full hypotheses (pre-map, every optimizer state, server behaviour,
what the view excludes) and handles labels through a subgroup $H$ of rotations
that leaves the label map invariant. A reduction from unlabeled NGCA samples is
claimed only when the labels are $H$-invariant, so the reducer can compute them.
Radial normalization is now allowed as a pre-map.

`ch-hidden-frame-symmetry` (blocking). Accepted. Success is measured up to a
finite group $K$ of target symmetries, for pancakes $K=\{\pm1\}$, in both games.
The reductions use only sign-invariant tests.

`ch-whitening-and-invertibility` (blocking). Accepted. `lem-whitening-gives-rotated-records`
assumes a frozen affine first layer of full column rank and population
whitening, and states the Haar property for frozen layers only. The upper-bound
half for trained or nonlinear clients is left open in the revised
`conj-seed-price-is-ngca-price`.

`ch-sq-attacker-interface` (blocking). Accepted. The SQ game is a separate
population game for frozen clients: the attacker has a STAT oracle for the
conditional law of the representation given the realized initialization, and no
record-level view. The sample game covers record-level attackers, with
polynomial-time bounds only.

`ch-ngca-testing-transfer` (blocking). Accepted. All auxiliary queries are
truncated and bounded, the composite tolerance is the minimum, the additive
$\nu$ of DKRS23 is kept, and a quantitative non-Gaussian witness is assumed.
For pancakes the transfer goes to a search lower bound directly and needs no
testing step (`prop-sq-blind-reconstruction-bound`, part a).

`ch-population-to-sample-reconstruction` (blocking). Accepted.
`thm-reconstruction-from-conditional-mean` gives the finite-sample statement
with a bounded predictor, held-out representations, Chebyshev concentration, the
zero-risk boundary, and LeakyReLU inversion before whitening. The training
records are handled by a uniform operator-norm bound.

`ch-learning-is-not-direction-recovery` (blocking). Accepted, with the
counterexample: $y=g\xi$ for $g=\langle u,x\rangle$ and an independent sign $\xi$
has $E[y\mid x]=0$ and generative exponent 2. Part (b) of
`conj-reconstruction-at-training-cost` is withdrawn. Two objects replace the
aim: `thm-reconstruction-from-conditional-mean` (what a good conditional-mean
predictor hands over) and `prop-sq-label-relevant-reconstruction-bound` (what
the labels cost the server, priced by $k^*$ whatever the trainer learned). No
common price of training and reconstruction is claimed.

`ch-floating-point-identification` (not blocking). Accepted. The identification
is labelled heuristic in the revised fact, and "only" is replaced by the
narrower claim astra gives.

`ch-pointwise-inversion` (not blocking). Accepted. The seed-known clause of
`thm-blind-split-seed-separation` is stated per record, with records independent
of the weights, and a union bound.

`ch-ngca-statistical-scope` (not blocking). Accepted. The statistical remark is
removed. The revised fact adds the known lattice caveat: SQ hardness of a
moment-matched law does not bind lattice-reduction attacks on noiseless or
discrete laws (`fact-lll-beats-sos-noiseless`, ZSWB22 Theorem 1.1, as recorded).

`ch-generative-upper-bound-scope` (not blocking). Accepted. The revised fact
states the denoiser, the logarithmic loss in $\tilde\lambda_k$, and that the
paper gives no SQ estimation algorithm.

`ch-ideal-encoding-quantifiers` (not blocking). Accepted, in the revised fact.

`ch-unsplit-explanation` (not blocking). Accepted. UnSplit is consistent with
the aims and not predicted by them, since its clients are convolutional.

`ch-honest-oracle-qualification` (not blocking). Accepted. The exact oracle is
the counterexample. The honest-batch version holds on an event of probability
$1-O(n^{-2})$, and the trie is capped at $n$ prefixes per level, so a wrong count
cannot make it run longer. This edits the proof of `thm-fs-sq-black-box-reduction`
without changing its verdict, which astra accepted.

`ch-postprocessing-simulation-scope` (not blocking). Accepted. In
`lem-sq-learner-post-processing` the SGD clause reads: a bSGD($T,\rho,b,p,r$)
learner with $b\rho^2>C\log(Tp/\delta)$ is simulated within $\delta$ by an SQ
method with $Tp$ queries of STAT($\rho/8$), which an oracle VSTAT($t$) answers for
$t\ge(4/\rho)^2$ after mapping queries to $[0,1]$, and the clause speaks about
worst-case roundings, never about one floating-point trajectory. The 1-STAT
budget is a budget of fresh one-bit samples and not a bound for unrestricted
sample access. The lemma is otherwise unchanged and was accepted.

## Revised literature objects

### fact-sq-simulates-minibatch-sgd: when statistical queries bind gradient training
status: borrowed, revised
uses: none

AKMSS21 Theorems 1a and 1c as stated in round 00, with the error of a bSGD method
defined as $E[\sup L_D]$ over valid roundings. Revised reading. A generic SQ
lower bound does not cover the whole fine-precision bSGD class, because Theorem
1a lets constructed models simulate PAC learning when $\rho<1/(8b)$. Bounds for
narrower architectures, dynamics or attacker classes remain possible. That
single-precision training sits in the regime of Theorem 1a is heuristic: it
needs an arithmetic model that the paper's uniform rounding lattice does not
supply.

Other regime. As in round 00.

### fact-clwe-hardness: homogeneous CLWE is a hard hidden-direction law
status: borrowed, revised
uses: none

BRST21, in its normalization (above). Definitions 2.19 and 2.21, Claim 2.22,
Corollary 4.2 (for $\beta\in(0,1)$, $\gamma\ge2\sqrt n$, $\gamma/\beta$ polynomial,
a polynomial-time quantum reduction from DGS$_{2\sqrt{2n}\eta_\varepsilon(L)/\beta}$
to hCLWE), Theorem 7.5 ($\exp(O(n^{2\varepsilon}))$ time for
$\gamma=n^\varepsilon$, $\varepsilon<1/2$), Corollary 9.4 (hidden subspaces).
Lemma 7.2 and Corollary 7.3: the covariance $\Sigma$ of $H_{w,\beta,\gamma}$, for
$\gamma\ge1$, satisfies $\|\Sigma-I_n/(2\pi)\|\ge\gamma^2e^{-\pi(\beta^2+\gamma^2)}$,
and the proof of Lemma 7.2 shows the excess along $w$ is the nonnegative
quantity $\sum_{y\in\gamma\mathbb Z}y^2\rho(y)/(1+\rho(\gamma\mathbb Z\setminus\{0\}))$
in the noiseless case. Hence $\Sigma\succeq I_n/(2\pi)$, with the excess at most
$4\gamma^2e^{-\pi\gamma^2}$ for $\gamma\ge1$ (proven from the displayed identity
and Corollary 7.3's rescaling). The homogeneous law determines $w$ only up to
sign. The round-00 sentence that an unbounded algorithm finds $w$ is withdrawn.

Other regime. Computational, conditional on worst-case lattice hardness.

### fact-hclwe-sq-correlation-bound: pairwise correlations of pancake laws
status: borrowed, revised
uses: fact-fgrvx17-planted-clique-sq-bound

BRST21 Proposition 8.3 and Theorem 8.1 as in round 00, now explicitly with the
reference $D_0$ of covariance $I_n/(2\pi)$ and the widths and spacing of BRST21's
normalization.

Other regime. Unconditional for SQ.

### fact-ngca-sq-lower-bound: non-Gaussian component analysis is SQ-hard under moment matching
status: borrowed, revised
uses: none

DKRS23 Theorem 1.5 and Definitions 1.2 and 1.3 as in round 00, which astra
checked against the PDF. Revised interpretation. The theorem bounds SQ
algorithms only. Lattice-reduction algorithms solve some discrete or noiseless
moment-matched instances with $O(n)$ samples while SQ bounds stay formally true
(ZSWB22, COLT 2022, Theorem 1.1, `fact-lll-beats-sos-noiseless`, recorded), so an
SQ separation does not predict security against every polynomial-time attacker,
and experiments must include a non-statistical attacker. The round-00 sentence
on statistical identifiability is withdrawn.

Other regime. SQ only.

### fact-generative-exponent-sq-recovery-bound: the price of finding a label-relevant direction
status: borrowed, revised
uses: fact-fgrvx17-planted-clique-sq-bound

DPLB24 as in round 00, with these scope lines. Theorem 4.1 needs the denoiser
$T$ it constructs and pays $\tilde\lambda_k=\lambda_k/\log^k(3/\lambda_k)$, and
its sample bound has the term $d/(\tilde\lambda_k^2\epsilon^2)$ besides
$d^{k/2}/\tilde\lambda_k^2$. The partial-trace algorithm is sample-based, not an
SQ algorithm, so the paper gives no matching SQ estimation upper bound, and
Remark 3.3 leaves the SQ detection-estimation gap open. The proof of Theorem 3.2
uses Lemma B.6, which is FGRVX17 Corollary 3.12, through Corollary B.7, and the
pairwise bound $\chi^2_0(D_{w_1},D_{w_2})\le\lambda_{k^*}^2m^{k^*}+m^{k^*+1}/(1-m)$
for $m=w_1\cdot w_2$ (equation 53, from Lemma E.2).

Other regime. As in round 00.

### fact-ica-breaks-rotation-perturbation: blind rotation is undone for independent non-Gaussian attributes
status: borrowed, revised
uses: none

LKR06 Sections 3 and 4. A random orthogonal perturbation $u=Rx$ of a record whose
attributes are statistically independent and non-Gaussian is undone by ICA up
to permutation and scaling, given full column rank. Their Theorem 4.3 is a
decomposability statement for the mixing matrix, not a computational guarantee.
Revised reading: a hidden rotation hides the orientation that the record law's
symmetry group leaves free. Laws with independent non-Gaussian coordinates have a
finite symmetry group up to signs and permutations and lose the orientation.
Spherically symmetric laws keep it hidden even statistically. Heuristic and
empirical in the paper.

Other regime. The attack side, unpriced.

### fact-instance-encoding-privacy-learnability: privacy of encodings reduces to learnability
status: borrowed, revised
uses: none

CDGJMMSTT21. Theorem 3: let $c_1,c_2$ be distinct non-constant concepts ($c_2$
neither $c_1$ nor $1-c_1$) with $E[c_1(D)]=E[c_2(D)]=1/2$. If the protocol is
$(0.51,\delta)$-accurate on plain data over $D_{c_1}$ and $D_{1-c_1}$, a
dataset-distinguishing adversary against one of $c_1$, $1-c_1$, $c_2$ has
advantage at least $(0.99-2\delta(n))/(3n)$, in about the learner's time.
Theorem 4: for an $(m,\gamma)$-rich class (Definition 7) and encoded accuracy
$(\epsilon,\delta)$, an instance distinguishing attack (Definition 5) of advantage
$0.99-\epsilon(n)/\gamma$ with oracle access to $E(\cdot)$, $L$, $F$ and a sampler
for $D$, in expected time $O(m/(1-\delta(n)))$. Theorem 5: for an efficient
protocol with decomposable instance encoding, balanced $(\epsilon,\delta)$
accuracy on encodings for a balanced concept $c$, either an attack with oracle
access to $L$, $E$ and $D_c$ of average advantage $1/2-\epsilon(m)-\tau$ in
expected time $O(m/\delta(m)+m/\tau^2)$, or an efficient learner of accuracy
$1-\tau$. Encoder access and knowledge of the initialization are distinct
capabilities: the first evaluates chosen inputs without revealing the seed, the
second need not evaluate a trained encoder whose current parameters are hidden.

Other regime. As in round 00.

### fact-ideal-keyed-encoding-weak-learner: an ideal keyed encoding hands over the concept
status: borrowed, revised
uses: none

CGJMMT21. Definition 2: $E$ is weakly ideal for $\mathcal C$ if for every
$c\in\mathcal C$ the encodings of two inputs with equal labels are equal in
distribution over the random key, and labels are preserved. Theorem 1: if a
learner with $m$ samples has balanced error $1/2-\varepsilon$ over the encoded law
for every $c\in\mathcal C$, then for every $\tau$ and every pair with labels $0$
and $1$ there is a PPT predictor with oracle access to the learner and the keyed
encoder whose risk is at most $\tau$ on an arbitrary evaluation distribution, in
time poly$(m,1/\epsilon,1/\delta,1/\tau)$.

Other regime. As in round 00.

### fact-nrnt25-private-layer-hardness-route: reconstruction hardness argued for one attack route
status: borrowed, revised
uses: none

NRNT25 as in round 00, with Proposition 3 restated. The paper states that with a
public discriminator and public gradients the record is recovered. Its proof
divides the first-layer weight gradient by the bias gradient, so it needs a
single-record gradient and a nonzero coordinate of the first-layer bias
gradient. Zero gradients, for example through an inactive ReLU path, reveal
nothing.

Other regime. As in round 00.

### fact-orthogonal-equivariance-of-training: the symmetry mechanism is known
status: borrowed
uses: none

Li, Zhang and Arora, arXiv 2010.08515 (ICLR 2021 as astra gives it, the arXiv
page names no venue), key LZA21. Definition 3.2: an algorithm is $G$-equivariant
if training on $\{(g(x_i),y_i)\}$ and composing with $g$ gives, in distribution,
the hypothesis trained on $\{(x_i,y_i)\}$. Theorem C.1: if a group $G_W$ acts on
weights through an isomorphism $\tau$ with
$M[\tau(g)W](g(x))=M[W](x)$, the update rule is invariant under the joint
action, and the initialization law is $G_W$-invariant, the algorithm is
$G$-equivariant, by induction on the iterates. Remark C.1 extends it to
stochastic and trajectory-dependent updates. Corollary C.2: (stochastic)
gradient descent from i.i.d. Gaussian initialization is orthogonally
equivariant. Remark C.2: momentum. Table 1: Adam and AdaGrad are permutation and
sign-flip equivariant only. Theorem 5.2: orthogonally equivariant learners need
$\Omega(d^2)$ samples on a quadratic task where a convolutional network needs
$O(1/\varepsilon\log(1/\varepsilon))$.

Other regime. A statement about the law of the learned function. It says
nothing about attackers or about the joint law of a transcript and the data.

## The game, revised

### def-seed-blind-reconstruction-game: the reconstruction games with and without the seed
status: proposed, revised
uses: fact-cohen-narcissus-equals-one-wayness, fact-orthogonal-equivariance-of-training

Protocol class $\mathcal P_H$, for a closed subgroup $H\le O(d)$.

1. The client applies a pre-map $\pi:\mathbb R^d\to\mathbb R^d$ with
   $\pi(Qx)=Q\pi(x)$ for $Q\in H$ (the identity, radial normalization), then
   $a=W\pi(x)+b$ with $W\in\mathbb R^{m\times d}$, then any map
   $z=\psi_\theta(a)$. Every client computation depends on the record only
   through $a$.
2. The initialization $\omega=(W_0,b_0,\theta_0,\text{other states},\text{server coins},\text{schedule})$
   is independent of the records and satisfies
   $(W_0Q,\text{rest})\overset d=(W_0,\text{rest})$ for $Q\in H$. The optimizer
   state of $W$ starts at $0$.
3. The update of $(W,s)$, with $G$ the gradient in $W$ and $s$ its optimizer
   state, satisfies $\mathcal U_t(WQ,GQ,sQ;c)=\mathcal U_t(W,G,s;c)\,Q$ for
   $Q\in H$ and all coins $c$. Other parameters update from quantities that
   depend on the record only through $a$.
4. The server may follow any strategy, honest or not. Its view $\mathcal V$ is
   every representation it receives, every message it sends, its coins and
   state, and the side data. The view never contains $W_t$, any gradient in $W$,
   any record, or any pair (record, representation).
5. Records $x_1,\dots,x_N$ are i.i.d. from $D$. Side data are
   $y_i=Y(x_i,\xi_i)$ with independent $\xi_i$ and $Y(Qx,\xi)=Y(x,\xi)$ for
   $Q\in H$. The attacker knows $D$, $Y$ and the protocol.

A target is a measurable $g:\mathbb R^d\to\mathbb R^s$ with
$0<\|g\|_{L^2}^2=E\|g(x)\|^2<\infty$, with a finite group $K\le O(s)$ of
symmetries under which success is measured ($K=\{\pm1\}$ for a symmetric hidden
law). The game reconstructs the observed records, not fresh ones.

Sample game $\Gamma_{\rm samp}(N,T)$. The attacker receives $\mathcal V$ of one
run on $N$ records, runs in time $T$, and outputs $t_1,\dots,t_N$. For a scale
$\epsilon>0$ let $F_\epsilon$ be the event that some $\kappa\in K$ has
$\|t_i-\kappa g(x_i)\|\le\epsilon$ for every $i$. Fine success is
$S_{\rm fine}(\epsilon;N,T)=\sup_A\big(\Pr[F_\epsilon]-\Pr[F'_\epsilon]\big)$,
where $F'_\epsilon$ is $F_\epsilon$ with every $x_i$ replaced by an independent
$x'_i\sim D$ (the Narcissus baseline, CKMMNST25 Definition 1.6 with
$\varepsilon=0$), the supremum over attackers of time $T$.

Population SQ game $\Gamma_{\rm SQ}(q,\tau)$, frozen clients only (no update).
The attacker has $q$ queries to STAT($\tau$) for the law of
$(z,y)=(\Phi_\omega(x),Y(x,\xi))$ given the realized $\omega$, where
$\Phi_\omega=\psi_{\theta_0}(W_0\pi(\cdot)+b_0)$, and no other access. It outputs
a measurable $R:\mathcal Z\times\mathcal Y\to[-1,1]^s$. Its weak success is
$\max_{\kappa\in K}E\langle R(z,y),\kappa g(x)\rangle/\|g\|_{L^2}$. It reaches
$c_0$ if its weak success is at least $c_0$ with probability at least $2/3$ over
$\omega$ and its coins, for every valid oracle.

Seed-known variants give the attacker $\omega$ as well. The price of the seed at
a success level is the pair of budget sets at which the seed-known and the
seed-blind attackers reach it. A theorem bounds a set from one side. An
experiment measures the success of named attacks at given budgets, which bounds
the seed-blind set from the other side only.

What would settle it. Well posed as stated. Useful if the theorems below hold in
it, which this round claims.

Regime. The sample game against unbounded attackers is statistical and belongs
to `statistical-limits`. Polynomial-time and SQ attackers are this space's.

Experiment. Named attacks' success at budgets, by Monte Carlo over records,
initialization and coins.

Without the oracle. No learning oracle is needed.

## New objects

### lem-equivariant-view-coupling: the server's view is a function of rotated records
status: proven
uses: def-seed-blind-reconstruction-game, fact-orthogonal-equivariance-of-training

Statement. Fix a protocol in $\mathcal P_H$ and $Q\in H$. Write
$\mathcal V(\omega;x_{1:N},y_{1:N})$ for the view of the run with coins $\omega$
on records $x$ and side data $y$, and $\omega_Q$ for $\omega$ with $W_0$
replaced by $W_0Q^\top$. Then pathwise
$\mathcal V(\omega;x,y)=\mathcal V(\omega_Q;Qx,y)$. Consequently, for any joint
law of $(x,y)$ independent of $\omega$,
$(\mathcal V(\omega;x,y),x,y)\overset d=(\mathcal V(\omega;Qx,y),x,y)$.

Proof. Induction on the step $t$, with hypothesis: in the run on $(Qx,y)$ from
$\omega_Q$ the first-layer weight and its state are $W_tQ^\top$ and $s_tQ^\top$,
and every other quantity equals its value in the run on $(x,y)$ from $\omega$.
At $t=0$ this is the definition of $\omega_Q$ and $s_0=0$. At step $t$, the
pre-activation is $W_tQ^\top\pi(Qx_i)+b_t=W_tQ^\top Q\pi(x_i)+b_t=a_i$, so every
representation, every server message (a function of the view so far and the
server's coins) and every back-propagated signal $\delta_i=\partial\ell/\partial a_i$
agree. The weight gradient is $\sum_i\delta_i\pi(Qx_i)^\top=G_tQ^\top$, and item 3
of the protocol class with $Q^\top\in H$ gives
$\mathcal U_t(W_tQ^\top,G_tQ^\top,s_tQ^\top;c)=\mathcal U_t(W_t,G_t,s_t;c)Q^\top$.
Other parameters see only $a$ and the messages, so they agree. The view contains
no first-layer quantity, so the two views are equal. For the second claim,
$\omega_Q\overset d=\omega$ by item 2 applied to $Q^\top$, and $\omega_Q$ is a
function of $\omega$, hence independent of $(x,y)$. $\square$

The pathwise identity keeps the side data $y$ fixed and does not use item 5 of
the protocol class. Item 5 is needed only when a simulator must compute the side
data from rotated records, as in the corollary.

The induction is that of LZA21 Theorem C.1, applied to the whole transcript, to
an adaptive server, and to side data, and stated as a pathwise coupling of the
view with the records rather than as equivariance of the output.

Corollary (the reduction). Let $Q$ be Haar on $H$, independent of everything,
and $u_i=Qx_i$. The simulator $\mathrm{Sim}(u,\xi)$ runs the protocol from fresh
coins on $(u_i,Y(u_i,\xi_i))$. For every attacker $A$ and target $g$, the joint
law of $(A(\mathcal V),g(x_{1:N}))$ equals that of
$(A(\mathrm{Sim}(u,\xi)),g(Q^\top u_{1:N}))$, because $Y(u_i,\xi_i)=y_i$ by
$H$-invariance. The $u_i$ are i.i.d. from $Q_\#D$ given $Q$. The overhead is one
run of the protocol, the trainer's own cost. If
$D=D_{\rm lab}\otimes P^A_V$ with $V$ in the orthogonal complement of the label
subspace $U_y$ and $H=\{Q:Q|_{U_y}=\mathrm{id}\}$, then $QV$ is a uniformly random
frame in $U_y^\perp$ and $g(Q^\top u)=(QV)^\top u$ for $g(x)=V^\top x$: the
attacker's task becomes NGCA coordinate recovery in dimension $d-\dim U_y$.

What breaks it, each by a hypothesis of $\mathcal P_H$: Adam, RMSProp, AdaGrad,
sign updates, coordinate clipping and $\ell_1$ penalties on $W$ (item 3, LZA21
Table 1), pixel-wise augmentation, coordinate-wise normalization and
convolutional first layers (item 1), publication of $W_t$ or its gradients, and a
server that knows some records or pairs (item 4), labels that depend on the
hidden part (item 5).

Other regime. The lemma is distributional and holds for unbounded attackers. It
is the common first step of the statistical and the computational statements.

### lem-whitening-gives-rotated-records: a frozen linear client hands over Haar-rotated records
status: proven
uses: def-seed-blind-reconstruction-game

Statement. Let the client be frozen with $\pi=\mathrm{id}$ and $\psi=\mathrm{id}$,
so $z=Wx+b$, with $W\in\mathbb R^{m\times d}$ of full column rank almost surely
and $(WQ,b)\overset d=(W,b)$ for all $Q\in O(d)$. Let $E[x]=0$ and
$E[xx^\top]=I_d$. Let $\Sigma_z=WW^\top$ (the covariance of $z$), $B$ an
orthonormal basis of $\mathrm{range}(\Sigma_z)$ chosen by a fixed measurable rule
from that subspace, and $T=B^\top\Sigma_z^{+1/2}$. Then
$T(z-E[z])=Rx$ with $R=B^\top W(W^\top W)^{-1/2}\in O(d)$, $R$ is a function of
$W$ alone, and $R$ is Haar-distributed and independent of the records. For a
LeakyReLU first layer the coordinate-wise inverse is applied first.

Proof. $E[z]=b$. With the polar decomposition $W=OS$,
$S=(W^\top W)^{1/2}$, $O=WS^{-1}$ has orthonormal columns and $WW^\top=OS^2O^\top$,
so $\Sigma_z^{+1/2}=OS^{-1}O^\top$ and $\Sigma_z^{+1/2}W=O$. $B$ and $O$ are
orthonormal bases of the same $d$-dimensional subspace, so $R=B^\top O\in O(d)$
and $T(z-b)=Rx$. For $Q\in O(d)$, $\mathrm{range}(WQ)=\mathrm{range}(W)$, so $B$ is
unchanged, and $O(WQ)=WQ(Q^\top S^2Q)^{-1/2}=WQQ^\top S^{-1}Q=OQ$. Hence
$R(WQ)=R(W)Q$, and $WQ\overset d=W$ gives $RQ\overset d=R$ for all $Q$. A
probability measure on $O(d)$ invariant under right translations is the Haar
measure. $R$ is a function of $W$, which is independent of the records. $\square$

With $N$ samples the server estimates $\Sigma_z$ and $b$, and the error of the
estimated $T$ is a separate, standard covariance-estimation term (heuristic
here, not used below in any proven bound).

Other regime. Statistical and computational alike: it is the upper-bound half
of the seed price for frozen linear clients.

### prop-sq-blind-reconstruction-bound: SQ price of blind reconstruction from a frozen client
status: proven for part (a), proven conditional on DKRS23 Theorem 1.5 for part (b)
uses: lem-equivariant-view-coupling, fact-hclwe-sq-correlation-bound, fact-ngca-sq-lower-bound, fact-fgrvx17-planted-clique-sq-bound

Setting. $\Gamma_{\rm SQ}$ with $H=O(d)$, a frozen client of $\mathcal P_{O(d)}$,
no side data, $r=1$, target $g(x)=\langle v,x\rangle$, $K=\{\pm1\}$.

(a) Pancake records. Let $D=H_{v,\beta,\gamma}$ with $\gamma\ge2$, $\beta\in(0,1)$,
$c_0\in(0,1]$, $\rho_0=c_0/3$, $\alpha_0=\rho_0^2/2$,
$\gamma_c=8\exp(-\pi\gamma^2(1-\alpha_0^2))$, $\beta_c=2(\gamma/\beta)^2$,
$M=\lfloor e^{d\alpha_0^2/4}/2\rfloor$, $L$ the truncation level defined in the
proof and $\tau_1=c_0/(8\sqrt{2\pi}\,L\sqrt d)$. An attacker that reaches weak
success $c_0$ with $q$ queries of STAT($\tau$) satisfies, whenever
$\tau_*^2=\min(\tau,\tau_1)^2>3\gamma_c$,
$$q+d\;\ge\;\frac{\alpha-\eta}{1-\eta}\Big(M-\frac{4}{\rho_0^2}\Big)\frac{\tau_*^2/3-\gamma_c}{\beta_c-\gamma_c},\qquad\alpha=\frac23,\ \eta=\frac{4}{\rho_0^2M}.$$
So $q\ge\exp(\Omega(c_0^4d))\,\tau_*^2\beta^2/\gamma^2$, unless the tolerance is
below $\sqrt{3\gamma_c}=O(e^{-\pi\gamma^2(1-\alpha_0^2)/2})$.

(b) Moment-matched records. Let $D=P^A_v$ with $\gamma_d$ on $v^\perp$ and $A$ of
mean $0$, variance $1$, with $\Pr_A[|a|>t]\le2e^{-t^2/(2\sigma^2)}$ for a constant
$\sigma$. Let $A$ satisfy the hypothesis of DKRS23 Theorem 1.5 with ambient
dimension $d$, an even moment degree $k$ and slack $\nu$, and let a witness
degree $j^*$ and $\kappa>0$ satisfy $|E_A[h_{j^*}]|\ge\kappa$, with $h_j$ the
normalized Hermite polynomials. If $((1-\lambda)/4-c)k>1/2$ and
$\nu\le d^{-((1-\lambda)/4-c)k}$, then for $d$ large every attacker reaching
weak success $c_0$ with $q$ queries of STAT($\tau$) has $q\ge2^{d^{\Omega(c)}}-d-1$
or $\tau\le O_k(d^{-((1-\lambda)/4-c)k})$.

Proof. Common part: the reducer $B$ has STAT access to an unknown law $P$ on
$\mathbb R^d$. It samples $\omega'$ from the initialization law and runs the
attacker, answering each attacker query $f:\mathcal Z\to[-1,1]$ by its own query
$f\circ\Phi_{\omega'}$ at the same tolerance. The answer is valid for the
attacker, since $E_P[f\circ\Phi_{\omega'}]=E[f]$ under $\Phi_{\omega'\#}P$. If
$P=H_w$ (or $P^A_w$) with $w=Qv$ for some $Q\in O(d)$, then
$\Phi_{\omega'\#}P=\Phi_{\omega''\#}D$, where $\omega''$ is $\omega'$ with $W'$
replaced by $W'Q$, so that $\Phi_{\omega''}(x)=\Phi_{\omega'}(Qx)$ and
$\omega''\overset d=\omega'$ (the frozen case of `lem-equivariant-view-coupling`,
applied to $Q^\top$), and the target transforms as
$\langle v,Q^\top u\rangle=\langle w,u\rangle$. So with probability at least $2/3$
the returned $R$ satisfies $|E_P[R(\Phi_{\omega'}(u))\langle w,u\rangle]|\ge c_0\sigma_a$,
where $\sigma_a^2=E_P\langle w,u\rangle^2$. Let $\bar w=E_P[R(\Phi_{\omega'}(u))u]$.
Then $|\langle\bar w,w\rangle|\ge c_0\sigma_a$ and, for unit $e$,
$\langle\bar w,e\rangle\le E|\langle e,u\rangle|\le\sigma_{\max}$, the square root
of the top covariance eigenvalue. $B$ asks the $d$ bounded queries
$h_j(u)=R(\Phi_{\omega'}(u))\,\mathrm{clip}(u_j,L)/L$ at tolerance $\tau_1$, with
$L$ chosen so that $E[|u_j|\mathbf 1\{|u_j|>L\}]\le c_0\sigma_a/(8\sqrt d)$, and
forms $\hat w$. Then $\|\hat w-\bar w\|\le\sqrt d(L\tau_1+c_0\sigma_a/(8\sqrt d))\le c_0\sigma_a/4$
once $L\tau_1\le c_0\sigma_a/(8\sqrt d)$, so $|\langle\hat w,w\rangle|\ge3c_0\sigma_a/4$
and $\|\hat w\|\le\sigma_{\max}+c_0\sigma_a/4\le2\sigma_{\max}$, hence
$\hat s=\hat w/\|\hat w\|$ has $|\langle\hat s,w\rangle|\ge3c_0\sigma_a/(8\sigma_{\max})$.

Part (a). By `fact-clwe-hardness`, $\Sigma\succeq I/(2\pi)$ and the excess is at
most $4\gamma^2e^{-\pi\gamma^2}$, so $\sigma_a\ge(2\pi)^{-1/2}$ and
$3\sigma_a/(8\sigma_{\max})\ge1/3$ for $\gamma\ge2$, giving
$|\langle\hat s,w\rangle|\ge\rho_0$, and $\tau_1$ as stated meets the condition
$L\tau_1\le c_0\sigma_a/(8\sqrt d)$. Tails: the density of $H_w$ is at most
$(3\gamma/\beta)\rho$ pointwise, since $\sum_k\rho_\beta(k-\gamma t)\le2.1$ for
$\beta<1$ and the normalizer of BRST21 equation 3 is at least
$\beta/\sqrt{\beta^2+\gamma^2}\ge\beta/(\sqrt2\gamma)$. So $u_j$ has tails at most
$(3\gamma/\beta)$ times those of $D_0$, and $L=O(\sqrt{\log(d\gamma/(\beta c_0))})$
suffices. So $B$ solves the search problem $Z$: output a unit $\hat s$ with
$|\langle\hat s,w\rangle|\ge\rho_0$, with probability at least $2/3$, using $q+d$
queries of STAT($\tau_*$). Lower bound for $Z$: take a set $U$ of $M$ unit vectors
with pairwise $|\langle w,w'\rangle|\le\alpha_0$, which exists because two
uniform unit vectors have $\Pr[|\langle w,w'\rangle|>\alpha_0]\le2e^{-d\alpha_0^2/2}$
and a union bound over $M^2$ pairs leaves positive probability. For a solution
$\hat s$, the $w\in U$ with $\langle\hat s,w\rangle\ge\rho_0$ number at most
$1/(\rho_0^2-\alpha_0)$: if there are $p$ of them, $p\rho_0\le\|\sum w\|$ and
$\|\sum w\|^2\le p+p^2\alpha_0$. With the opposite sign, at most $4/\rho_0^2$ in
all, so $D_{\hat s}=\{H_w:w\in U\}\setminus Z_{\hat s}$ has at least
$(1-\eta)M$ members. By BRST21 Proposition 8.3, with $\gamma^2(1-\alpha_0^2)\ge1$,
$D_{\hat s}$ is $(\gamma_c,\beta_c)$-correlated relative to $D_0$, so FGRVX17
Lemma 3.10 gives $\mathrm{SDA}(D_{\hat s},D_0,\gamma_c+\gamma')\ge|D_{\hat s}|\gamma'/(\beta_c-\gamma_c)$
for every $\gamma'>0$. FGRVX17 Theorem 3.2 then bounds every randomized SQ
algorithm that solves $Z$ with probability $\alpha>\eta$ by
$(\alpha-\eta)/(1-\eta)$ times that many calls to VSTAT($1/(3\bar\gamma)$),
$\bar\gamma=\gamma_c+\gamma'$. A STAT($\tau_*$) algorithm with queries in
$[-1,1]$ is a VSTAT($t$) algorithm for $t\ge1/\tau_*^2$, since VSTAT($t$) answers
the query mapped to $[0,1]$ within $1/(2\sqrt t)$. Choosing
$\bar\gamma=\tau_*^2/3$, so $\gamma'=\tau_*^2/3-\gamma_c>0$, gives the bound.

Part (b). $B$ adds one query. Let $\hat s$ be as above and
$\tilde h=\mathrm{clip}(h_{j^*},M_h)/M_h$ with $M_h$ such that
$E[|h_{j^*}(X)|\mathbf 1\{|h_{j^*}(X)|>M_h\}]\le\rho_1^{j^*}\kappa/8$ both for
$X\sim\gamma_1$ and for $X=\rho a+\sqrt{1-\rho^2}g$, $a\sim A$, $g\sim\gamma_1$,
$|\rho|\le1$, which a polylogarithmic $M_h$ achieves by the tail of $A$, where
$\rho_1=3c_0/(8\sigma_{\max})$. $B$ asks $\tilde h(\langle\hat s,u\rangle)$ at
tolerance $\tau_2=\rho_1^{j^*}\kappa/(4M_h)$ and outputs "planted" iff
$M_h|\text{answer}|>\rho_1^{j^*}\kappa/2$. Under $P=\gamma_d$, $\hat s$ is fixed
before this query and $\langle\hat s,u\rangle\sim\gamma_1$, so
$E[h_{j^*}]=0$ and $B$ outputs "Gaussian" always. Under $P=P^A_w$ and the
attacker's success, $\langle\hat s,u\rangle=\rho a+\sqrt{1-\rho^2}g$ with
$\rho=\langle\hat s,w\rangle$, $|\rho|\ge\rho_1$, and the Ornstein-Uhlenbeck
identity $E_g[h_j(\rho a+\sqrt{1-\rho^2}g)]=\rho^jh_j(a)$ gives
$|E[h_{j^*}]|=|\rho|^{j^*}|E_A[h_{j^*}]|\ge\rho_1^{j^*}\kappa$. The truncation and
the tolerance leave a margin, so $B$ outputs "planted". $B$ solves NGCA testing
with probability at least $2/3$ under each hypothesis with $q+d+1$ queries of
tolerance $\min(\tau,\tau_1,\tau_2)$, stopping the attacker after $q$ queries if it
has not halted. DKRS23 Theorem 1.5 gives
$q+d+1\ge2^{d^{\Omega(c)}}$ or
$\min(\tau,\tau_1,\tau_2)\le O_k(d^{-((1-\lambda)/4-c)k})+(1+o(1))\nu$. Since
$\tau_1=\tilde\Theta(d^{-1/2})$ and $\tau_2=\Theta(1)$ exceed the right side for
large $d$ under the two stated conditions, $\tau$ does not. $\square$

Remarks. The condition $((1-\lambda)/4-c)k>1/2$ needs $k\ge4$: the $d$ queries
of tolerance $d^{-1/2}$ that turn a reconstruction into a direction cost more
than the lower bound allows when fewer moments match, so for $k=2$ the bound is
vacuous. The pancake case needs no witness and no moment count, because BRST21
Proposition 8.3 controls the pairwise correlations at every overlap.

Other regime. SQ only. Statistically, pancake records with $\gamma\ge2\sqrt d$
are identifiable by unbounded search, a statement left to `statistical-limits`.
By `fact-ngca-sq-lower-bound`, lattice methods are outside these bounds.

### prop-fine-reconstruction-to-hclwe: polynomial-time price of fine blind reconstruction
status: proven
uses: lem-equivariant-view-coupling, fact-clwe-hardness

Statement. Let a protocol of $\mathcal P_{O(d)}$ (frozen or trained) run on $N$
records from $D=H_{v,\beta,\gamma}$ with $\beta\in(0,1)$, $\gamma\ge2\sqrt d$ and
$\gamma/\beta$ polynomial, without side data. Let $c_1=1/(16\pi\sqrt{2\pi})$. If a
seed-blind attacker of time $T$ outputs $t_{1:N}$ such that, with probability
$p$, some $\kappa\in\{\pm1\}$ has $|t_i-\kappa\langle v,x_i\rangle|\le c_1/\gamma$ for
every $i$, then for $N=N'=Cd\log^2(\gamma/\beta)$ there is an algorithm of time
$T+T_{\rm run}+\mathrm{poly}(d)$ for hCLWE$_{\beta,\gamma}$ (BRST21 Definition 2.21)
with advantage at least $p-e^{-\Omega(d)}$, where $T_{\rm run}$ is the cost of one
protocol run. By BRST21 Corollary 4.2, $p$ is negligible for every
polynomial-time attacker unless DGS$_{2\sqrt{2d}\eta_\varepsilon(L)/\beta}$ has a
polynomial-time quantum algorithm.

Proof. $B$ receives $N+N'$ samples $u_j$ from $P\in\{H_w,D_0\}$, $w$ uniform.

1. $B$ runs $\mathrm{Sim}$ on $u_{1:N}$ and the attacker. If $P=H_w$, fix a
   rotation $Q_w$ with $Q_wv=w$. Then $u_j=Q_wx_j$ with $x_j\sim D$ i.i.d., and by
   `lem-equivariant-view-coupling` the attacker's output has the same joint law
   with $(x_j)$ as in the real game, with target
   $\langle v,Q_w^\top u_j\rangle=\langle w,u_j\rangle$. So with probability $p$,
   $t=\kappa U w+e$ with $\|e\|_\infty\le c_1/\gamma$, $U$ the $N\times d$ matrix of
   the $u_j$.
2. $B$ computes $\hat w=(U^\top U)^{-1}U^\top t$ and $\hat s=\hat w/\|\hat w\|$,
   and outputs "Gaussian" if $U^\top U$ is singular or $\hat w=0$. Under $H_w$,
   $\Sigma\succeq I/(2\pi)$ (`fact-clwe-hardness`), the rows are sub-Gaussian
   with norm $O(\sqrt{\log(\gamma/\beta)})$ by the density bound of
   `prop-sq-blind-reconstruction-bound`, and BRST21 Lemma 7.4 (Vershynin's
   Theorem 4.6.1) applied to $\Sigma^{-1/2}u$ gives
   $\sigma_{\min}(U)\ge\sqrt N/(2\sqrt{2\pi})$ with probability $1-e^{-\Omega(d)}$
   for $N=Cd\log^2(\gamma/\beta)$. On both events
   $\|\hat w-\kappa w\|\le\|e\|_2/\sigma_{\min}(U)\le2\sqrt{2\pi}c_1/\gamma$, and
   then $\hat s=\kappa(\cos\theta\,w+\sin\theta\,e_\perp)$ with $e_\perp\perp w$ a
   unit vector and $\theta\le\pi\|\hat w-\kappa w\|\le2\pi\sqrt{2\pi}c_1/\gamma=1/(8\gamma)$.
3. $B$ computes $S=\frac1{N'}\sum_{j>N}\cos(2\pi\langle\hat s,u_j\rangle/s_\ell)$ on
   fresh samples and outputs "planted" iff $S\ge\kappa_\beta/6$, with
   $\kappa_\beta=\exp(-\pi\beta^2(\beta^2+\gamma^2)/\gamma^2)\ge e^{-2\pi}$.

Under $D_0$, $\hat s$ is fixed before the fresh samples and
$\langle\hat s,u\rangle$ has density proportional to $\rho$, so
$E\cos(2\pi\langle\hat s,u\rangle/s_\ell)=e^{-\pi/s_\ell^2}\le e^{-\pi\gamma^2}$, as
$s_\ell\le1/\gamma$. Under $H_w$ on the events of step 2,
$\langle\hat s,u\rangle=\kappa(\cos\theta\,a+\sin\theta\,g')$ with $a=\langle w,u\rangle$
and $g'=\langle e_\perp,u\rangle$ independent of $a$ with density proportional to
$\rho$. Cosine is even, so $\kappa$ drops out, and
$E\cos(2\pi(\cos\theta\,a+\sin\theta\,g')/s_\ell)=E_a[\cos(2\pi\cos\theta\,a/s_\ell)]\,e^{-\pi\sin^2\theta/s_\ell^2}$,
because the sine term has mean zero by the symmetry of $g'$. Conditioned on its
layer, $a$ is centred at a multiple of $s_\ell$ with shape $\rho_{\sigma_\ell}$, so
$E_a\cos(2\pi a/s_\ell)=e^{-\pi\sigma_\ell^2/s_\ell^2}=\kappa_\beta$, and
$|E_a\cos(2\pi\cos\theta\,a/s_\ell)-\kappa_\beta|\le2\pi(1-\cos\theta)E|a|/s_\ell\le\pi\theta^2\cdot2\gamma\cdot E|a|=O(1/\gamma)$,
using $s_\ell\ge1/(2\gamma)$. And $e^{-\pi\sin^2\theta/s_\ell^2}\ge e^{-4\pi\gamma^2\theta^2}\ge e^{-\pi/16}$.
So $E[S]\ge\kappa_\beta/3$ for large $d$. Hoeffding on the $N'$ fresh bounded terms
gives false acceptance at most $e^{-\Omega(N'\kappa_\beta^2)}$ under $D_0$ and
acceptance with probability at least $p-e^{-\Omega(d)}$ under $H_w$. $\square$

Remarks. Reconstruction to accuracy of order $1/\gamma\le1/(2\sqrt d)$ is fine,
while the pancake coordinate has standard deviation near $(2\pi)^{-1/2}$. Whether
coarse reconstruction, to constant correlation, is hard for polynomial time is
`prob-coarse-reconstruction-lattice-hardness`, open. Side data on a known label
subspace are handled by $H=\{Q:Q|_{U_y}=\mathrm{id}\}$ and hCLWE in dimension
$d-\dim U_y$, the reducer appending the label coordinates itself, as in BRST21
Lemma 9.3's padding (sketch, not claimed here).

Other regime. Conditional on worst-case lattice hardness, against
polynomial-time attackers with the record-level view, trained clients included.

### thm-blind-split-seed-separation: the seed separates attackers for pancake records
status: proven
uses: fact-lei-random-expansive-layers-invertible, prop-sq-blind-reconstruction-bound, prop-fine-reconstruction-to-hclwe, lem-equivariant-view-coupling

Statement. Let the client's first layer be $z=\mathrm{ReLU}(Wx)$ with
$W\in\mathbb R^{m\times d}$ of i.i.d. Gaussian entries, $m=c_0'd$, $c_0'\ge2.1$,
further layers optional and each satisfying LJDD19 Assumption 1, an update rule
satisfying item 3 of $\mathcal P_{O(d)}$, and records i.i.d. from
$H_{v,\beta,\gamma}$, $\beta\in(0,1)$, $\gamma\ge2\sqrt d$, $\gamma/\beta$
polynomial, without side data.

(i) Seed-known. For each record $x_i$, independent of the weights, the round-0
representation determines $x_i$ by layer-wise linear equations with probability
$1-e^{-\Omega(d)}$ (LJDD19 Theorem 3), so all $N$ records are recovered exactly
in polynomial time with probability $1-Ne^{-\Omega(d)}$, frozen or trained.

(ii) Seed-blind, population SQ, frozen client. Weak success $c_0$ costs
$\exp(\Omega(c_0^4d))\tau^2\beta^2/\gamma^2$ queries of STAT($\tau$) for any
$\tau\ge\tau_1$ (part a of `prop-sq-blind-reconstruction-bound`).

(iii) Seed-blind, record-level view, polynomial time, frozen or trained. Fine
success at scale $c_1/\gamma$ has negligible probability unless
DGS$_{2\sqrt{2d}\eta_\varepsilon(L)/\beta}$ is quantum polynomial-time
(`prop-fine-reconstruction-to-hclwe`).

Proof. (i) is LJDD19 Theorem 3 applied per record (Assumption 1 holds, the
records are independent of $W$), with a union bound, and for a trained client the
first representation the server receives is computed with $W_0$. (ii) and (iii)
are the cited propositions, whose hypotheses the ReLU client meets: the Gaussian
law of $W$ is right rotation invariant, $\pi=\mathrm{id}$, and the view excludes
first-layer quantities. $\square$

The price of the seed, in the units of the space: one record costs the
seed-known attacker one linear solve, while the seed-blind attacker pays
exponentially many statistical queries, or breaks a lattice problem, plus one
training run for the reduction. The separation comes from the record law, which
is artificial (pancakes), and from the standard Gaussian initialization, which is
not a plug-in. For record laws that depart from Gaussian at low degree, such as
images, the bounds of part (b) of `prop-sq-blind-reconstruction-bound` are weak
or vacuous, consistent with EKC22 and CGJMMT21.

Other regime. An unbounded seed-blind attacker is not bounded by this theorem.
The gap is computational.

Without the oracle. The reductions cost one honest training run each, no oracle.

### conj-seed-price-is-ngca-price: the seed is worth the NGCA price of the record law
status: open, revised (lower-bound half proven in the cases above)
uses: lem-equivariant-view-coupling, lem-whitening-gives-rotated-records, prop-sq-blind-reconstruction-bound, prop-fine-reconstruction-to-hclwe

Statement. For protocols of $\mathcal P_H$ and records
$D_{\rm lab}\otimes P^A_V$ with $V\perp U_y$, the budget sets of seed-blind
attackers for weak (SQ game) or fine (sample game) reconstruction of $V^\top x$
modulo the symmetry group of $A$ coincide, up to one training run and poly$(d)$,
with those of NGCA coordinate recovery for $A$ in dimension $d-\dim U_y$.

Settled so far. The lower-bound inclusion: proven for frozen clients in the SQ
game (pancakes, and moment-matched $A$ with $k\ge4$) and for fine reconstruction
of pancakes in the sample game. The upper-bound inclusion: proven for frozen
linear clients of full column rank with population whitening
(`lem-whitening-gives-rotated-records`). Open: the upper bound for ReLU and
trained clients (the residual rotation need not be independent of the records,
per `ch-whitening-and-invertibility`), the effect of finite-sample whitening, and
coarse reconstruction in polynomial time.

What would settle it. A whitening argument for ReLU clients through the recovery
of $WW^\top$ from truncated moments, and a lattice reduction from constant
correlation. A refutation: a moment-matched law with a polynomial-time blind
attack that does not solve NGCA, or a client of $\mathcal P_H$ whose view leaks
more than rotated records, which the coupling lemma excludes.

Regime and experiment. As in round 00, with a lattice-reduction attacker added
(`fact-ngca-sq-lower-bound`).

### thm-reconstruction-from-conditional-mean: a good conditional-mean predictor hands over the label direction
status: proven
uses: lem-whitening-gives-rotated-records, def-seed-blind-reconstruction-game

Statement. Let the client be frozen and linear of full column rank (or LeakyReLU,
inverted coordinate-wise), records $x\sim\gamma_d$, side data
$y=Y(\langle u,x\rangle,\xi)$ for an unknown unit $u$, $m(t)=E[y\mid\langle u,x\rangle=t]$
with $m\in L^2(\gamma_1)$ and $\beta_1=E[m(g)g]\ne0$. The server holds a top model
$f$ with $|f|\le B$, the predictor $F(x)=f(Wx+b)$, its excess square risk
$\varepsilon=E(F(x)-m(\langle u,x\rangle))^2$, the population whitening $T$, and the
representations of $N$ records independent of $F$ (held-out batches or
inference inputs). Let $\eta_N=B\sqrt{d/(N\delta)}$. If $\sqrt\varepsilon+\eta_N<|\beta_1|/2$,
then with probability at least $1-\delta$ the server's unit vector
$\hat s=\hat w_R/\|\hat w_R\|$, $\hat w_R=\frac1N\sum_jf(z_j)T(z_j-b)$, satisfies
$\|R^\top\hat s-\mathrm{sign}(\beta_1)u\|\le2(\sqrt\varepsilon+\eta_N)/|\beta_1|$, and
the reconstructions $t(x)=\langle\hat s,T(z-b)\rangle$ satisfy
$E_x(t(x)-\mathrm{sign}(\beta_1)\langle u,x\rangle)^2\le4(\sqrt\varepsilon+\eta_N)^2/\beta_1^2$
for a record independent of $\hat s$, and, for any $n$ records $x_{1:n}$, also those
the model was trained on,
$\frac1n\sum_i(t(x_i)-\mathrm{sign}(\beta_1)\langle u,x_i\rangle)^2\le\|R^\top\hat s-\mathrm{sign}(\beta_1)u\|^2\,\lambda_{\max}\big(\frac1n\sum_ix_ix_i^\top\big)$.

Proof. By `lem-whitening-gives-rotated-records`, $T(z-b)=Rx$, so
$R^\top\hat w_R=\hat w:=\frac1N\sum_jF(x_j)x_j$ and $\|\hat w_R\|=\|\hat w\|$. Its
mean is $E[F(x)x]=E[m(\langle u,x\rangle)x]+E[(F-m)x]$. The first term is $\beta_1u$,
since for unit $e\perp u$ the Gaussian $\langle e,x\rangle$ is independent of
$\langle u,x\rangle$ with mean zero. For unit $e$,
$E[(F-m)\langle e,x\rangle]\le\sqrt\varepsilon$ by Cauchy-Schwarz and
$E\langle e,x\rangle^2=1$. By Chebyshev,
$\Pr[\|\hat w-E\hat w\|>\eta_N]\le E[F^2\|x\|^2]/(N\eta_N^2)\le B^2d/(N\eta_N^2)=\delta$.
So $\hat w=\beta_1u+e'$ with $\|e'\|\le\sqrt\varepsilon+\eta_N<|\beta_1|/2$, and
$\|\hat w/\|\hat w\|-\mathrm{sign}(\beta_1)u\|\le2\|e'\|/|\beta_1|$ by the triangle
inequality and $|\|\hat w\|-|\beta_1||\le\|e'\|$. Then
$t(x)=\langle\hat s,Rx\rangle=\langle R^\top\hat s,x\rangle$, and
$t(x)-\mathrm{sign}(\beta_1)\langle u,x\rangle=\langle R^\top\hat s-\mathrm{sign}(\beta_1)u,x\rangle$.
For an independent record its second moment is the squared norm. For any $n$
records the average is a quadratic form in the empirical second moment matrix,
bounded by its top eigenvalue whatever the dependence on the records.
$\square$

For $x_i\sim\gamma_d$, $\lambda_{\max}(\frac1n\sum x_ix_i^\top)\le(1+C\sqrt{d/n}+C\sqrt{\log(1/\delta)/n})^2$
with probability $1-\delta$ (BRST21 Lemma 7.4), so the training records are
reconstructed as well as fresh ones once $n\gtrsim d$. This is Halil's lower
bound in its exact form: the server's reconstruction error is at most
$4(\sqrt\varepsilon+\eta_N)^2/\beta_1^2$, set by the performance of the attacked
model. CDGJMMSTT21 Theorems 4 and 5 give a distinguishing analogue with an
encoder oracle. This theorem needs no encoder oracle and prices reconstruction
of a real-valued coordinate.

Other regime. The bound holds for any server, efficient or not, and costs it one
pass over $N$ representations. It is an upper bound on attack cost.

### prop-sq-label-relevant-reconstruction-bound: what the labels cost the server
status: proven, with the randomized form of the lower bound argued here
uses: lem-equivariant-view-coupling, lem-whitening-gives-rotated-records, fact-generative-exponent-sq-recovery-bound, fact-fgrvx17-planted-clique-sq-bound

Statement. Let the client be frozen and linear, $z=Wx$, with $W$ right rotation
invariant and of full column rank, records $x\sim\gamma_d$, labels with
$(\langle u,x\rangle,y)\sim P$ in DPLB24's class $\mathcal G$ with generative
exponent $k^*\ge3$, and target $g(x)=\langle u,x\rangle$, $K=\{\pm1\}$.

(a) Lower bound. In $\Gamma_{\rm SQ}$ with the attacker's queries answered by
VSTAT($n$) on the joint law of $(z,y)$, an attacker that reaches weak success
$c_0$ with $q$ queries gives an algorithm that returns $\hat s$ with
$|\hat s\cdot w^*|\ge3c_0/5$ for the single-index model with uniform direction
$w^*$, with $q+d$ queries to VSTAT($\max(n,n_1)$), $n_1=\lceil64L^2d/c_0^2\rceil$,
$L=\sqrt{2\ln(16\sqrt d/c_0)}$, with probability $2/3$. If $q+d=d^{r}$ with
$r\le d^{1/4}$ and $\lambda_{k^*}^2\ge rd^{-1/2}$, DPLB24 Theorem 3.2's argument
gives $\max(n,n_1)\ge c_{k^*}\lambda_{k^*}^{-2}(d/r^2)^{k^*/2}$ up to the factor
$(\alpha-\eta)/(1-\eta)$, hence for $k^*\ge3$ and $d$ large
$n\ge c_{k^*}\lambda_{k^*}^{-2}(d/r^2)^{k^*/2}/2$.

(b) Upper bound, sample-based. With population whitening the server runs
DPLB24's Algorithm 1 on $(T z_i,y_i)=(Rx_i,y_i)$, a single-index model with
direction $Ru$, and with $n\ge C_k[d^{k^*/2}/\tilde\lambda_{k^*}^2+d/(\tilde\lambda_{k^*}^2\epsilon^2)]$
labelled representations obtains $\hat s$ with $(\hat s\cdot Ru)^2\ge1-\epsilon^2$
with probability $1-2e^{-d^c}$ (DPLB24 Theorem 4.1), and reconstructs
$\pm\langle u,x_i\rangle$ by $\langle\hat s,Tz_i\rangle$ with average error at most
$2\epsilon^2\lambda_{\max}(\frac1n\sum x_ix_i^\top)$.

Proof. (a) The reducer samples $W'$, answers an attacker query
$f(z,y)\in[0,1]$ by the query $f(W'x',y)$ on the single-index law, and the frozen
case of `lem-equivariant-view-coupling` with $Q$ such that $Qu=w^*$ shows the
attacker sees the law of its real game, with target
$\langle u,Q^\top x'\rangle=\langle w^*,x'\rangle$. With probability $2/3$ its $R$
has $|E[R(W'x',y)\langle w^*,x'\rangle]|\ge c_0$. The $d$ queries
$R(W'x',y)\mathrm{clip}(x'_j,L)/L$, mapped to $[0,1]$, are answered by
VSTAT($n_1$) within $1/(2\sqrt{n_1})$, so the coordinates of $E[Rx']$ are known
within $L/\sqrt{n_1}$, and the Gaussian truncation error is at most
$2e^{-L^2/2}\le c_0/(8\sqrt d)$. So $\|\hat w-E[Rx']\|\le c_0/4$, and as in
`prop-sq-blind-reconstruction-bound` $|\hat s\cdot w^*|\ge(3c_0/4)/(5/4)=3c_0/5$,
which exceeds DPLB24's threshold $\tilde\omega(d^{-1/2})$ for constant $c_0$. DPLB24
prove Theorem 3.2 through Lemma B.6, which is FGRVX17 Corollary 3.12 for
algorithms that always succeed. For success $2/3$ we replace it by FGRVX17
Theorem 3.2 with Lemma 3.10 on the same spherical code $w_1,\dots,w_m$ with
pairwise overlaps at most $\epsilon=C\log_d(m)^2/d$: a solution $\hat s$ is valid
for at most $2/(\rho^2-\epsilon)$ of the $w_i$, $\rho=3c_0/5$, by the Gram argument,
so the solution-set bound is $\eta=2/((\rho^2-\epsilon)m)$, and their inequality
(54) holds with the extra factor $(\alpha-\eta)/(1-\eta)$, which changes only
$c_{k^*}$. For $k^*\ge3$, $n_1=\tilde O(d)$ is below the bound, so $n$ carries it.
(b) By `lem-whitening-gives-rotated-records` $(Tz_i,y_i)=(Rx_i,y_i)$ is a
single-index sample with direction $Ru$, and DPLB24 Theorem 4.1 applies. Then
$\langle\hat s,Rx\rangle-\pm\langle u,x\rangle=\langle R^\top\hat s\mp u,x\rangle$ and
$\|R^\top\hat s\mp u\|^2\le2-2\sqrt{1-\epsilon^2}\le2\epsilon^2$ for the right sign,
and the average over records is bounded as in
`thm-reconstruction-from-conditional-mean`. $\square$

The server's price for the label-relevant coordinate is the generative exponent
of the task, whatever the trainer's model learned: astra's example
$y=\langle u,x\rangle\xi$ has a constant Bayes predictor and $k^*=2$, so
`thm-reconstruction-from-conditional-mean` gives nothing there, while (b) still
applies. The lower bound measures detection first (DPLB24 Remark 3.3), and the
upper bound is sample-based, so the two sides are not one SQ price.

Other regime. SQ for (a), sample-based for (b). No oracle.

### conj-reconstruction-at-training-cost: withdrawn as stated
status: refuted as stated (part b), superseded
uses: thm-reconstruction-from-conditional-mean, prop-sq-label-relevant-reconstruction-bound

Part (b) of round 00 claimed that blind reconstruction of the label-relevant
coordinate is equivalent to learning the task. Astra's counterexample refutes it
(proven): $y=\langle u,x\rangle\xi$ with an independent sign $\xi$ has Bayes
square-loss predictor $0$, so learning the task needs nothing, while the label
law reveals $\langle u,x\rangle$ up to sign at generative exponent $2$. Part (a)
is now `thm-reconstruction-from-conditional-mean`, with the sample complexity
astra asked for, and the label side is
`prop-sq-label-relevant-reconstruction-bound`. Nothing of the aim remains open
under this slug.

Other regime. Not applicable.
