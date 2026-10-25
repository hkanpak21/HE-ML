# Round 02, oracle and measurement, builder

Date 2026-10-25. This round answers the challenges of `round-01/discussant-astra.md` and re-presents
every object that is to be judged for acceptance: three revised facts and five objects. Each object below
is complete in its statement. Where a proof is unchanged from round 01, it is given in full again with the
changes marked by the sentence that introduces them. Symbols follow
`sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md`, the oracle theory.

The facts fact-gdp-audit-observation-count, fact-rerun-reproduction-error and
fact-controlled-nondeterminism-exact-replication of round 01, and the seven facts accepted in round 00, stand as
written there with the corrections listed in the two summaries.

## Responses to the challenges of round 01

ch-seed-enumeration-conditions (blocking). Accepted on both counts. Enumerating the seed gives the exact view
laws only when every other source of randomness can be integrated exactly. Exact top access needs one decoder
of the seed from the view that works under both hypotheses. Nearly singular laws give approximate recovery
with an error term. The revised fact states both and proves the error term.

ch-known-covariance-noise-range (blocking). Accepted. The dimension condition is now stated in full, with the
matching attack attributed to Dwork, Smith, Steinke, Ullman and Vadhan (FOCS 2015) as HSU25 attributes it.

ch-forging-strict-cost (blocking). Accepted. The factor of Proposition 4.5 equals one at $P=m=1$. The revised fact
states the factor as a time under $P$ processes, its value as a work factor at $P=1$, and the parameter range in
which it is below one.

ch-meter-domain-and-equivalence (blocking). Accepted on both counts. The remark of def-seed-access-modes is now the
multiplicative inequality, vacuous when the infimum is zero. The meter has two coordinates, work and examples
submitted, which is how `def:cost` of `oracle.tex` accounts. "Fails" for drawn-mode callers now reads "is
inapplicable as stated".

ch-profile-adaptive-shadow-cost (blocking). Accepted. prop-profile-run-coordinate (b) now distinguishes two-phase
families, whose shadow runs precede and ignore the challenge and can serve both hypotheses of a trial, from general
families, whose trial runs two complete executions and pays both.

ch-paired-discordance-baseline (blocking). Accepted. Astra's complement example has variance one under a shared seed
against one half under independence. The remark now says that a coupling reduces the variance of a trial relative to
independent executions exactly when it makes the two outputs positively correlated, and gives the variance with both
acceptance probabilities.

ch-one-sided-twin-asymmetry (blocking). Accepted. Astra's certifier, four base calls and 368 twin calls at $\varepsilon=1$,
$\alpha=0.05$, $\epsilon_{\mathrm{acc}}=0.01$, is sound for $\mathrm H_{e^\varepsilon}(P_1\|P_0)$ over every learning function and
refutes the base-input bound, which asked for 298. thm-exact-twin-price now states the base-input bound for the coupled
tail and for total variation only. For the one-sided target it states the bound at the numerator input, and the
counterexample is part (c).

Non-blocking points of astra's review, all taken. The identification of (F9) holds modulo a null set, and the
perturbed functions now equal the reference function there. The generic training oracle carries a utility condition,
a restriction on admissible learning functions that prop-drawn-mode-is-fs-oracle now states. The reverse bound of
thm-coupling-free-soundness uses the twin rule with its coordinates exchanged, a twin rule need not be implementable
through Train, and the top-oracle condition is a shared seed with correct conditional hardware marginals. The
simulation of prop-profile-run-coordinate (a) keeps a private table of virtual names and is a statement in the
measurable-strategy model, not an efficient simulation. The realization paragraph of thm-exact-twin-price names the
controlled pipeline as the deployed one.

## Revised facts

### fact-small-seed-space-breaks-dp: a noise seed with 100 values is detected by the audit

status: borrowed
uses: none

NHSBTJCT23 (USENIX Security 2023), §6.3, Violation 2. A DP-SGD implementation whose noise seed takes only 100 values,
so that only 100 noise vectors occur, is detected as violating its claimed $\varepsilon=1.27$ by the Gaussian-DP audit and
by Lu et al.'s method, and is missed by $(\varepsilon,\delta)$ audits (Fig. 8).

Proof. Read in the paper, §6.3.

Other regime. Enumerating a finite seed space gives the view laws $P_0$ and $P_1$ exactly only when every other source of
randomness, hardware randomness, batching drawn outside that seed and channel noise, is integrated exactly, for instance
when the seed drives all of it under deterministic kernels. It gives the top oracle exactly only when one decoder $\hat s$ of
the seed from the view satisfies $\hat s(Y)=s$ under both hypotheses. If instead $\Pr[\hat s(Y)\neq s]\le e$ under each
hypothesis, an adversary holding $(\hat s(Y),Y)$ is within total variation $e$ of one holding $(s,Y)$ under each
hypothesis, so its best advantage is at least $\mathrm D^\top_1-2e$ (proven, by the triangle inequality for total
variation). Argon's example $\mathsf L(x_b;s)=s+bM/2\bmod M$ has $\mathrm D^\top_1=1$ and $\mathrm{TV}(P_0,P_1)=0$, and no decoder
works under both hypotheses there. In Violation 2 the 100 noise vectors are far apart in high dimension, which explains the
detection (heuristic). This is the empirical side of open problem 9 of the oracle theory.

### fact-hsu-membership-sample-gap: sample-based membership inference needs order $n+n^2\rho^2$ samples

status: borrowed
uses: none

HSU25 (Haghifam, Smith and Ullman, FOCS 2026 to appear, arXiv 2508.19458 v1, the version the library holds). Definition 2.1
asks a test, given $m$ auxiliary samples, the noisy mean and a candidate, to answer correctly with probability at least 0.51
on each side. Theorem 3.1 proves that for $d>c_1(n+n^2\rho^2)$ and $m\le c_2(n+n^2\rho^2)$ no such test exists against the
noisy empirical mean of Definition 2.4 over all Gaussians, and Theorem 1.1 is its informal version. Theorem 3.3 is a matching
attack, for $0<\rho<1$, $m\ge cd$ and $d\ge c(n+n^2\rho^2)$, against the symmetric estimators of Definition 3.2, so the orders
match at the critical dimension $d\asymp n+n^2\rho^2$. Theorem 4.1, whose informal version is Theorem 1.2, proves for identity
covariance, $n\ge4$ and $m\ge2$, that no test exists when $d<c(n+n^2\rho^2+n^2/m)$. The matching attack for
$d\gtrsim n+n^2\rho^2+n^2/m$ is attributed by the paper to Dwork, Smith, Steinke, Ullman and Vadhan (FOCS 2015) and is not
proven there. With known covariance and $m=2$ the dimension at which a test exists is therefore of order $n+n^2\rho^2+n^2/2$,
which is of order $n^2$ when $\rho$ is bounded and of order $n^2\rho^2$ when $\rho$ grows. §1.2.1 notes that a test with a
statistic free of the population and a calibrated threshold needs $O(1)$ trained models, that is $O(n)$ samples.

Proof. Read in the paper, §1.2, §2, §3 and the statement of Theorem 4.1. The proofs were not re-derived.

Other regime. The fact prices auxiliary samples for an attacker that knows the estimator and computes without bound, and it
prices no training runs. Divided by $n$, the price of Theorem 3.1 is $1+n\rho^2$ datasets' worth of samples. The result belongs
to the space statistical-limits. For measurement, §1.2.1 says that an audit built from restricted tests can sit far below the
profile it lower-bounds.

### fact-unlearning-verification-fragile: a prover that picks the batches passes replay

status: borrowed
uses: none

ZCSL24 (ICML 2024). Definition 4.1 calls a proof of retraining valid when every step is reproducible within $\varepsilon$ and no
batch meets the unlearned set $D_u$. Algorithm 1 retrains while replacing each unlearned point of the original batch by its
nearest same-class neighbour in the retained data, and Proposition 4.2 proves that it passes at $\varepsilon=0$. Algorithm 2 forges
the retraining proof from the logged training proof, editing only the steps whose batch met $D_u$, and Proposition 4.4 proves that
it passes at $\varepsilon>0$ under the assumptions of Proposition 4.3, vanilla SGD for the replay update and the stated step-size
bounds. Proposition 4.5 states that Algorithm 1 takes the time $\mathcal T(n)$ of naive retraining and Algorithm 2 the time
$(p_u/P+(1-p_u)/(mP))\,\mathcal T(n)$ on $P$ parallel processes, with $p_u=1-(1-|D_u|/|D|)^m$ and batch size $m$. The text calls these
results Theorems 4.2 to 4.5.

Proof. Read in the paper, §3 and §4.

Other regime. The time factor of Algorithm 2 is at most one, equals one at $P=m=1$, and is below one when $P\ge2$, or when
$m\ge2$ and $p_u<1$ (proven, from the formula). Its work factor is the value at $P=1$, $p_u+(1-p_u)/m$. The prover's freedom is the
batch order, a part of the seed. Algorithm 1 costs one run and Algorithm 2 at most one, so a meter in runs separates neither from
honest retraining.

## def-seed-access-modes: one learning oracle with two seed-access modes

status: open
uses: def-learning-oracle, def-learning-oracle-model, def-certifier, def-degenerate-oracles, def-passive-learning-oracle, def-generic-training-oracle

Statement. Fix a learning oracle $\mathcal O$ for $(\mathsf L,\mu,\pi)$. A game assigns each caller four things.

1. A *seed-access mode*, named or drawn. In the *named mode* the caller's Train calls are those of def-learning-oracle. In the
   *drawn mode* the oracle accepts $\mathsf{Train}(x,s)$ only with $s=\bot$, returns the model's name only, keeps the seed under no
   name the caller holds, and refuses Open on any seed. A grant to a caller in the drawn mode carries model names only. In both
   modes the caller's $k$-th received name is $k$.
2. A *return label*, open or eval, carried by the model names that the caller's own Train calls return. With label eval the caller
   can query its own models through Eval but cannot open or retrain them.
3. A set $\Lambda_A\subseteq\Lambda$ of learner names, and a set of starting models, that its Train calls may use.
4. A *budget*, a bound for each operation (Train, Eval at each query type, Open). The budget $(q_T,q_E)$ of
   def-learning-oracle-model is the case that bounds Train and Eval on names with label eval and leaves the rest free.

A *cost meter* is a measurable map $\mathsf{cost}=(\mathsf{work},\mathsf{size}):\mathcal X\to[0,\infty)^2$, where $\mathsf{work}(x)$ is the work
of one run at $x$ in a fixed machine model and $\mathsf{size}(x)$ the number of examples in the dataset of $x$. A caller's *oracle
cost* is the coordinatewise sum of $\mathsf{cost}$ over its Train calls. The bottom oracle of def-degenerate-oracles is the named mode
with return label open and no grant, the top oracle adds grants of the honest seeds, and an experimenter in the drawn mode follows
the drawn-seed discipline of def-certifier.

Remark, the needle bound in oracle cost (proven). In the setting of lem-needle-lower-bound let $N_X$ count the certifier's Train
calls with input in $X=\bigcup_kX_k$. Its proof gives $\Pr_{\mathsf L^\circ}[\hat t\ge\vartheta]\ge1-\alpha-\mathbb E_{\mathsf L^\circ}[N_X]/J$,
since $\sum_k\mathbf 1[\mathrm{Hit}_k]\le N_X$. A certifier whose work is at most $C$ satisfies $N_X\inf_{x\in X}\mathsf{work}(x)\le C$, which
is vacuous when the infimum is zero. A run of thm-dataflow-composition (c) costs $\sum_{t\le R}(\mathsf{cost}(x^0_t)+\mathsf{cost}(x^1_t))$ plus
the calls of the other nodes and of the strategy. A bound in oracle cost is a bound in machine compute only under
FORMAL_SECURITY's no-skipping hypothesis.

Remark, the seed for an adversary. Under the top oracle with deterministic kernels and a deterministic channel, one Train call at
the revealed seed attains $\mathrm D^\top_1$, which is thm-reference-access (a). Under hardware randomness the rerun-and-compare
attack has advantage equal to a coupled tail minus the spread of the rerun, which can be negative. How many reruns an adversary fixed
before $\mathsf L$ needs to approach $\mathrm D^\top_1$ is open.

The proposal for Halil. Both repositories use this one oracle, and each game fixes the four items per caller. The passive learning
oracle and the generic training oracle of FORMAL_SECURITY are drawn-mode callers of it (prop-drawn-mode-is-fs-oracle). Drawn coins
lose no soundness for any bottom-oracle target of the HE-ML theory, and lose the accuracy that its separations measure
(thm-coupling-free-soundness). Named seeds are needed for the top-oracle threat model, for replay audits, and for the accuracy of
coupled certificates. The decision left to Halil is whether to adopt this, to keep drawn coins only, which makes those three
inapplicable, or to keep named seeds only, which needs the declared starting models of item 3 whenever the meter is work.

Without the oracle, or in the other regime. The definition adds no power. It names restrictions that a game imposes, per caller, and
a meter. In the statistical regime the meter is a count of calls. In the computational regime it is the work and the examples of the
runs, and a price in work transfers to real training only under the no-skipping hypothesis.

## prop-drawn-mode-is-fs-oracle: the two FORMAL_SECURITY oracles are drawn-mode callers

status: sketch
uses: def-seed-access-modes, def-passive-learning-oracle, def-generic-training-oracle

Statement. (a) Let $\mathcal M$ be a standard Borel space of traces of length at most $T$, $\Lambda_A$ the finite set of recipes a
game names, and $m_\varnothing$ a fixed symbol, the only starting model allowed. Let $x(\ell,D)=(\ell,m_\varnothing,D,\mathcal H)$ for a fixed
$\mathcal H$, and let $\mathsf L(x(\ell,D);\rho,\xi)$ be the trace of recipe $\ell$ on $D$ with coins $(\rho,\xi)$, whose initial state the
declared initialization rule of $\ell$ draws from the coins. A caller in the drawn mode with return label open, which opens each model
name it receives, has, call by call, the transcript law of a caller of the passive learning oracle of `oracle.tex` (label
`def:passive`) on the same sequence of recipes and corpora. Its oracle cost, the sums of $\mathsf{work}$ and of $\mathsf{size}$, is the
metered cost of `def:cost`, the work of the recipe on the corpus together with the size of the corpus. (b) Let $\mathsf{ev}(m,u)$
return $f_m(x)$, the input gradient of the loss at a labelled point $z$, or its parameter gradient at $z$, according as $u$ is
$(\mathrm{out},x)$, $(\mathrm{gx},z)$ or $(\mathrm{g\theta},z)$. Fix the architecture, the training procedure and the utility condition
$\alpha$ of def-generic-training-oracle, the last as a restriction on the admissible learning functions. A caller in the drawn mode,
with return label eval and a budget on Train, on Eval at each query type and on Open, realizes an access class of that report. Train is
train, Eval at the three query types is eval, $\mathrm{grad}_x$ and $\mathrm{grad}_\theta$, and reveal is Open, permitted exactly when the
class contains reveal, in which case the return label is open.

Proof. (a) $\mathsf{Train}(x(\ell,D),\bot)$ draws $(\rho,\xi)\sim\mu\otimes\pi$, independent of all other randomness by fidelity, and
stores the trace of $\ell$ on $D$ with those coins. Open returns it. So each pair of calls returns a trace of $\ell$ on $D$ with fresh
coins, and two pairs on one corpus return independent traces, the two clauses of `def:passive`. The caller can pass no seed and holds
no seed name, so it cannot rerun at chosen coins, which `def:passive` forbids. The only starting model is $m_\varnothing$ and the
initialization is the declared rule of $\ell$, so no caller emits chosen weights as a trace, the laundering that the text after
`def:cost` blocks. Learner names lie in $\Lambda_A$, so no caller authors a recipe. Summing $\mathsf{work}(x(\ell,D))$ and $\mathsf{size}(x(\ell,D))=|D|$
gives the two parts of the metered cost. The coins of `def:passive` are one random object, and $(\rho,\xi)$ represents it by (F9).
(b) Each operation of the report either reads the stored parameter vector through a fixed public map, which is $\mathsf{ev}$ at the
matching query, or returns it, which is Open. The report's train returns a fresh handle and never opens the randomness, which is the
drawn mode. With return label eval the caller cannot open its own handles, as a class without reveal requires. The budgets per
operation are item 4 of def-seed-access-modes. The utility condition restricts which learning functions the game admits and does not
change the interface (proven).

Label. Proven, by construction.

Without the oracle, or in the other regime. The statement concerns oracles only. Its use is that every theorem of the HE-ML theory that
holds for a drawn-mode caller holds for FORMAL_SECURITY's oracles under these identifications, and every theorem that needs the named
mode is inapplicable to them as stated.

## thm-coupling-free-soundness: shared seeds buy accuracy, never soundness, for bottom-oracle targets

status: sketch
uses: thm-coupling-certificate, thm-dataflow-composition, thm-bounded-deviation-transfer, def-isolated-client

Setting. A *twin rule* $\Theta=(\Theta_t)_{t\le R}$ is a sequence of laws on $(\mathcal R\times\Xi)^2$ whose two marginals are both
$\mu\otimes\pi$. It *shares the seed* when its two seed coordinates agree almost surely. The identity coupling of the oracle theory is the
twin rule with a common seed and independent hardware randomness. The *independent twin rule* is $(\mu\otimes\pi)^{\otimes2}$. Both are
implementable through Train, by one call with $s=\bot$ and a second with the returned seed name or with $s=\bot$. A general twin rule need
not be implementable, and the theorem concerns an experimenter that can sample the rule it uses. In the setting of
thm-dataflow-composition, the $\Theta$-coupled execution $\mathsf{Ex}^\Theta_0$ runs $G$ under $H_0$ and, at each $v_t$ that runs, draws
$\zeta_t=((\rho_t,\xi_t),(\rho'_t,\xi'_t))\sim\Theta_t$ independently of $\omega$, of the release noises $Z_1,\dots,Z_R$ and of the other
$\zeta_s$. The node uses $(\rho_t,\xi_t)$, and the twin is $W'_t=\mathsf L(x(c_t,D^1_j,W'_{t-1});\rho'_t,\xi'_t)$. The execution
$\mathsf{Ex}^\Theta_1$ runs $G$ under $H_1$ with the two coordinates exchanged, the node using $(\rho'_t,\xi'_t)$ and the twin, on $D^0_j$,
using $(\rho_t,\xi_t)$. Their exceedance probabilities are $\epsilon^\Theta_0(\Delta)$ and $\epsilon^\Theta_1(\Delta)$, quantities of the
experiments, which differ from $\epsilon_0(\Delta)$ and $\epsilon_1(\Delta)$ in general. The *bottom-oracle targets* are
$\mathrm H_\gamma(P_0\|P_1)$ and $\mathrm H_\gamma(P_1\|P_0)$ for the bottom-oracle view, and the *top-oracle targets* the same divergences for
the top-oracle view, $\mathrm D^\top_\gamma(K)$ at one node.

Statement. (a) One node. For every coupling $\Gamma'$ of $\Pi_{x_0}$ and $\Pi_{x_1}$, every channel $K$ and every $\gamma\ge1$,
$\mathrm H_\gamma(P_0\|P_1)\le\mathbb E_{\Gamma'}\mathrm H_\gamma(K(\cdot\mid W_0)\|K(\cdot\mid W_1))$. If $\Gamma'$ is the law of
$(\mathsf L(x_0;\rho,\xi_0),\mathsf L(x_1;\rho,\xi_1))$ for a joint law of $(\rho,\xi_0,\xi_1)$ in which each $(\rho,\xi_b)$ has law
$\mu\otimes\pi$, the same right side bounds $\mathrm D^\top_\gamma(K)$.

(b) Composition. Under the bottom oracle, for every twin rule $\Theta$, every adversary, every $\varepsilon\ge0$ and every $\Delta>0$,
$\mathrm H_\gamma(P_0\|P_1)\le\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\min\{\epsilon^\Theta_0(\Delta),\gamma\epsilon^\Theta_1(\Delta)\}$ and
$\mathrm H_\gamma(P_1\|P_0)\le\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\min\{\epsilon^\Theta_1(\Delta),\gamma\epsilon^\Theta_0(\Delta)\}$, with
thresholds per round as in thm-dataflow-composition (b). Under the top oracle the same holds for every twin rule that shares the seed.
The sum-of-tails bound of thm-dataflow-composition (b) is not claimed for general $\Theta$.

(c) Certificates. Let an experimenter sample independent repetitions of a $\Theta$-coupled experiment. The certificate of
thm-coupling-certificate (b), computed on draws of $\Gamma'$, is sound at level $\alpha$ for $\mathrm H_\gamma(P_0\|P_1)$, under its computability
assumption on the channel divergence. With $\bar p^\Theta$ the Clopper and Pearson bound of thm-dataflow-composition (c) computed on
$\mathsf{Ex}^\Theta_0$, $\min\{1,\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\bar p^\Theta\}$ is an upper bound on $\mathrm H_\gamma(P_0\|P_1)$ with
probability at least $1-\alpha$, for every $\Theta$. The same holds for the top-oracle targets when $\Theta$ shares the seed. Under a rule
other than the identity coupling these give, in general, no certificate of $\epsilon_0(\Delta)$.

(d) Necessity. The independence from the release noise and the shared seed for top targets cannot be dropped.

Proof. (a) (F4) with $\Theta=\Gamma'$ gives the first bound, since $\Gamma'K_b$ has $b$-th marginal $P_b$. Step 2 of the proof of
thm-coupling-certificate (b) writes $\mathrm D^\top_\gamma(K)=\int\mathrm H_\gamma(P^\rho_0\|P^\rho_1)\,\mu(d\rho)$, with $P^\rho_b$ the law of the
view given the seed. For $\mu$-almost every $\rho$, the conditional law of $(\xi_0,\xi_1)$ given $\rho$ has marginals $\pi$, so (F4) with it
bounds the integrand by the conditional mean of $\mathrm H_\gamma(K(\cdot\mid\mathsf L(x_0;\rho,\xi_0))\|K(\cdot\mid\mathsf L(x_1;\rho,\xi_1)))$, and
integrating over $\mu$ gives the second bound.

(b) Follow the proof of thm-dataflow-composition (b) with one change, which is which coordinates drive which chain. Write
$\zeta_t=((\rho^0_t,\xi^0_t),(\rho^1_t,\xi^1_t))\sim\Theta_t$, independent of $\omega$, of the $Z_s$ and of the other $\zeta_s$, and let $v_t$ use
$(\rho^b_t,\xi^b_t)$ under $H_b$. That pair has law $\mu\otimes\pi$ and is independent of everything else in the $H_b$ execution, so the law of
that execution is unchanged. Step 1 is unchanged, with $\bar\rho_t=\rho^b_t$ under the top oracle. Step 2 drives the hybrid's chain of $D^b_j$ by
$(\rho^b_t,\xi^b_t)$. Step 3 compares the hybrid with $\mathsf{Ex}^\Theta_0$, whose twin is driven by $(\rho^1_t,\xi^1_t)$. Before the first
exceedance the clip does nothing, so the two have the same choices, chains, releases and stops, and
$\mathrm{TV}(\mathcal L_0,\mathcal L_{\mathrm{hyb}})\le\epsilon^\Theta_0(\Delta)$. In step 4 the kernel draws $\zeta_t\sim\Theta_t$ and extends both chains.
Given its past outputs, both chain states and $\zeta_t$, when $\mathfrak z_t\sim\mathcal N(\Delta/\sigma,1)$ the output $y_t$ has law
$\mathcal N(O_t+F^1_t,\sigma^2I_d)$ whatever $F^0_t$ is, by (F6)(ii), and $Z''_t$ is fresh. That law does not depend on the chain of $D^0_j$, which
can therefore be discarded. The chain of $D^1_j$ is driven by $(\rho^1_t,\xi^1_t)$, of law $\mu\otimes\pi$ and independent of the past, so by
induction over the rounds the output has law $\mathcal L_1$ in every coordinate but one. Under the top oracle the kernel must also output a
revealed seed, which is $\rho^1_t$ in $\mathcal L_1$ and $\rho^0_t$ in the hybrid as step 3 needs. One kernel outputs one value, so step 4 needs
$\rho^0_t=\rho^1_t$ almost surely. Under the bottom oracle $\bar\rho_t=\star$ and the condition does not arise. Step 5 is unchanged. The bounds with
$\epsilon^\Theta_1$ repeat the construction with the roles of the hypotheses exchanged, the hybrid agreeing with $\mathsf{Ex}^\Theta_1$, whose node
is driven by the second coordinate, which is why the coordinates of $\mathsf{Ex}^\Theta_1$ are exchanged. A twin rule need not be exchangeable,
so the two bounds use the two executions as defined.

(c) By fidelity across repetitions the indicators of $D^\star_0>\Delta$ in $\mathsf{Ex}^\Theta_0$ are independent Bernoulli variables with parameter
$\epsilon^\Theta_0(\Delta)$, so (F8) gives $\Pr[\epsilon^\Theta_0(\Delta)\le\bar p^\Theta]\ge1-\alpha$, and (b) with $\mathrm H_\gamma\le1$ gives the bound. For
thm-coupling-certificate (b), the summands of $\hat t$ are independent, lie in $[0,1]$, and have mean the right side of (a), so Hoeffding's
inequality (F8) gives soundness. For the last sentence, argon's example in (d) has $\epsilon^\Theta_0(0.5)=1/2$ under the independent twin rule
and $\epsilon_0(0.5)=1$.

(d) Shared seed. Let $\mathcal R=[0,1)$, deterministic kernels, the plain channel, $\mathsf L(x_0;\rho)=\mathbf 1[\rho<1/2]$ and
$\mathsf L(x_1;\rho)=\mathbf 1[\rho\ge1/2]$. Then $\mathrm D^\top_1=1$, while the independent twin rule gives $\Pr[W_0\neq W_1]=1/2$, so the certificate of
thm-coupling-certificate (b) concentrates at $1/2$ and is unsound for $\mathrm D^\top_1$. As a release on $\mathbb R$ with $R=1$ and $\Delta=0.5$, the
identity coupling has $|W_1-W_0|=1$ always and the independent rule half the time. Release noise. Take $R=2$, $d=1$, $\sigma=1$, $O_t=0$,
$f_t(c,m)=m$, round-1 models of law $\mathcal N(0,1)$ under both hypotheses, the choice $c_2=\mathbf 1[|y_1|>1]$, and models in round 2 that differ by
$10\Delta$ between the hypotheses exactly when $c_2=1$. A round-1 coupling that sets both models to $-Z_1$ has the right marginals, yet makes
$y_1=0$, $c_2=0$ and the measured exceedance zero. In the true execution $y_1\sim\mathcal N(0,2)$ under both hypotheses, so by (F5)
$\mathrm{TV}(P_0,P_1)=\Pr[|y_1|>1]\,(2\Phi(5\Delta)-1)$, which at $\varepsilon=0$ and $\Delta=1/2$ is $0.4795\times0.9876=0.474$, above the claimed
$\delta_{\mathcal N}(0;\sqrt2\Delta)=0.276$ (computed). The example is excluded because $\zeta_1$ must be independent of $Z_1$.

Label. Proven, (a) to (d). Part (b) modifies a proof that round 03 of the formal tuning checked, and astra re-checked the change line by line in
round 01. Argon's review states a wider form with twin kernels that adapt to the past, driven by fresh randomness independent of $\omega$ and of
$Z_{\ge t}$. That form is not re-derived here and stays open in this file.

Meaning. A real twin runs at a chosen seed on whatever hardware is available, so the realized pair need not have independent hardware randomness.
For bottom-oracle targets that does not matter. Soundness needs each run, alone, to have the law of the deployed run at its input, and repetitions
to be independent. The shared seed and the choice of coupling move only the size of $\epsilon^\Theta_b$, so only the accuracy, and the coupled tail
$\epsilon_0(\Delta)$ itself is certified, in general, only under the identity coupling.

Without the oracle, or in the other regime. Without the oracle no twin can be sampled. In the drawn mode the independent twin rule is available,
and its certificate is sound and, by thm-dataflow-composition (e)(ii), inaccurate where the separations place it. The statement is statistical.
In the computational regime the work of a certificate is the work of its runs, whatever their coupling.

## prop-profile-run-coordinate: what a finite experiment certifies about a security profile

status: sketch
uses: def-security-profile-curve, def-learning-oracle-model, thm-coupling-certificate, lem-atomless-two-point

Setting. Fix a procedure, a coalition and a distinguishing goal under the bottom oracle, and a learning function $\mathsf L$. For a budget
$b=(q_T,q_E)$ let $\epsilon_{\mathsf L}(b)$ be the best advantage of an adversary with that budget. A *declared family* is a sequence
$\mathcal A=(\mathcal A_k)_{k\in\mathbb N}$ of adversaries, fixed before $\mathsf L$, where $\mathcal A_k$ makes $k$ Train calls of its own, its *shadow runs*,
and its advantage $\mathrm{Adv}(\mathcal A_k)$ averages over them. The family is *two-phase* when each $\mathcal A_k$ first makes its $k$ Train calls, with
inputs and seeds that depend on no procedure value, and then outputs a bit from the procedure's channel outputs and its own models with no
further Train call. Its profile is $\bar\epsilon_{\mathcal A}(k)=\max_{k'\le k}\mathrm{Adv}(\mathcal A_{k'})$, nondecreasing in $k$.

Statement. (a) Flatness. For every learning function and every $(q_T,q_E)$, $\epsilon_{\mathsf L}(q_T,q_E)=\epsilon_{\mathsf L}(0,q_E)$. In the setting of
thm-coupling-certificate with no query channel, $\epsilon_{\mathsf L}(b)=\mathrm{TV}(P_0,P_1)$ for every $b$.

(b) Lower band of a declared family. Fix shadow budgets $k_1<\dots<k_r$ and trial counts $n_1,\dots,n_r$ in advance. For a two-phase family a
trial of $\mathcal A_{k_i}$ makes fresh shadow runs and then one execution of the procedure under each hypothesis, both tested with the same shadow
models. For a general family a trial makes two complete and independent executions of $\mathcal A_{k_i}$ against the procedure, one under each
hypothesis, each with its own shadow runs. A trial records the difference $D\in\{-1,0,1\}$ of the output under $H_1$ and the output under $H_0$.
Let $\bar D_i$ be the mean of $n_i$ independent trials and $\underline\ell_i=\bar D_i-\sqrt{2\ln(r/\alpha)/n_i}$. Then, for every learning function,
with probability at least $1-\alpha$, $\bar\epsilon_{\mathcal A}(k)\ge\max\{\underline\ell_i:k_i\le k\}$ for every $k\ge k_1$. A trial costs $k_i$ shadow
runs and two executions of the procedure for a two-phase family, and $2k_i$ shadow runs and two executions for a general one.

(c) Upper band. In the setting of thm-coupling-certificate, the coupled certificate of its part (b) at $\gamma=1$ is an upper band on
$\epsilon_{\mathsf L}(b)$ for every $b$ at once, sound at level $\alpha$ for every learning function. Through a deterministic channel with atomless
view laws, no drawn-mode certificate sound for every learning function outputs an upper band below one with probability above $\alpha$.

Proof. (a) Monotonicity gives $\ge$. For $\le$, let $\mathcal A$ have budget $(q_T,q_E)$. Under the bottom oracle every Train call of $\mathcal A$ has
arguments it holds with label open, so its training inputs are built from values it received through the plain channel, its own choices,
models of its own calls, and models and seeds of the nodes its coalition owns, and never from a name served through the query channel, which
carries label eval. Let $\mathcal A'$ run $\mathcal A$ and keep a private table of virtual names in the order $\mathcal A$ expects them. It answers each
Train call of $\mathcal A$ by computing $\mathsf L(x;\rho',\xi')$ itself, at the given $\mathsf L$, with fresh hardware randomness and either a fresh seed from
its own coins or the seed that a virtual or a coalition seed name stands for, which it reads by Open. It answers later Open and Eval calls on
virtual names from the table, supplies the value of a virtual model when one enters a procedure choice, and passes calls on real query-channel
names to the oracle, within their allowances. By fidelity the answers $\mathcal A$ receives have the same joint law with everything else as in the
oracle, so $\mathcal A'$ has the same advantage, the same Eval calls, and no charged Train call. Such an $\mathcal A'$ exists for each $\mathsf L$, since the
adversary may depend on $\mathsf L$ when $\mathsf L$ is fixed first (remark of def-degenerate-oracles). This is a statement about measurable strategies,
not an efficient simulation. With no query channel, (F1) and the hard-wired Neyman and Pearson set attain $\mathrm{TV}(P_0,P_1)$ at budget zero, and
step 3 of the proof of thm-coupling-certificate (b) bounds every bottom-oracle adversary by it.

(b) In a two-phase trial the shadow models are independent of the two executions of the procedure and serve both, so
$\mathbb E[D]=\mathbb E_S[\Pr[\mathcal A_{k_i}=1\mid H_1,S]-\Pr[\mathcal A_{k_i}=1\mid H_0,S]]=\mathrm{Adv}(\mathcal A_{k_i})$. In a general trial the two executions are
independent complete runs of the attack, so $\mathbb E[D]=\mathrm{Adv}(\mathcal A_{k_i})$ directly. Trials are independent by fidelity. $D$ takes values in
$[-1,1]$, so Hoeffding's inequality (F8) gives $\Pr[\underline\ell_i>\mathrm{Adv}(\mathcal A_{k_i})]\le\alpha/r$. A union bound over $i$ and
$\mathrm{Adv}(\mathcal A_{k_i})\le\bar\epsilon_{\mathcal A}(k)$ for $k\ge k_i$ finish. Two remarks show why the two kinds of trial differ. A general adversary may choose
its shadow inputs from the challenge, so one bank drawn before the challenge need not implement it under either hypothesis. One bank reused across
trials does not give a band either. Let $P_0=\delta_0$, $P_1=\delta_1$ on $\mathcal V=\{0,1\}$, and let $\mathcal A_0$ draw a fair bit $S$ and output
$\mathbf 1[Y=S]$. Then $\mathrm{Adv}(\mathcal A_0)=0$, while the test realized at $S=1$ has advantage one, so a band built on one realized bank exceeds the
profile with probability $1/2$.

(c) The first sentence is thm-coupling-certificate (b) with $\epsilon_{\mathsf L}(b)\le\mathrm{TV}(P_0,P_1)$ from (a). The second is
thm-coupling-certificate (a)(iii), since an upper band below one on $\epsilon_{\mathsf L}(0)=\mathrm{TV}(P_0,P_1)$ is a certificate of the total variation
(proven).

Label. Proven, (a) to (c).

Reading. For one deployed pipeline the run axis of a profile carries information only for a declared family, which is what an experiment
measures, or uniformly over a class of learning functions, which is the shadow-run price of the space statistical-limits, or for a computationally
bounded class, which is the space computational-limits. The object proposed in FORMAL_SECURITY's terminology ledger, the curve from a budget to the
success, is well defined as a measured object only with its family named. A finite experiment certifies a lower band for that family, with fresh
shadow runs in every trial, and an upper band for the whole class only from coupled runs.

Remark, paired trials. Under any coupling of the two executions of a trial whose marginals are right, the mean of $D$ is the advantage and
$\mathrm{Var}(D)=p_0(1-p_0)+p_1(1-p_1)-2\,\mathrm{Cov}(T_0,T_1)$, with $T_b$ the output under $H_b$ and $p_b$ its mean. The variance is at most the
discordance $\Pr[T_0\neq T_1]$. A shared seed lowers the variance against independent executions exactly when it makes $\mathrm{Cov}(T_0,T_1)>0$, and
astra's complement example, $T_1=1-T_0$ with $p_0=p_1=1/2$, raises it from one half to one. The measured covariance therefore reports what a shared seed
gives the measurement. With a positive covariance, an empirical Bernstein interval turns the smaller variance into a smaller trial count, which is
common random numbers.

Without the oracle, or in the other regime. Without the oracle a declared family still has its band from real shadow runs. LiRA's evaluations use one
bank for all targets (fact-lira-priced-in-training-runs), so what they report is the advantage conditional on that bank. In the computational regime
the family's budget is its shadow work, and part (a) does not apply, since a bounded adversary cannot hard-wire an unbounded table.

## thm-exact-twin-price: certifying leakage at a zero-leakage function costs exact twin runs

status: sketch
uses: thm-dataflow-composition, lem-needle-lower-bound, thm-coupling-free-soundness, def-seed-access-modes

Setting. As in thm-dataflow-composition (e)(ii), one release $y=W+Z$ with $Z\sim\mathcal N(0,\sigma^2I_d)$, a fixed choice $c$, $\mathcal M=\mathbb R^d$ and
$x_b=x(c,D^b_j)$, with $x_0\neq x_1$. Three targets are considered. The coupled tail $\theta_{\mathrm{ex}}=\epsilon_0(\Delta)$ for a fixed $\Delta>0$, the
total variation $\theta_{\mathrm{tv}}=\mathrm{TV}(P_0,P_1)$ of the release, and its one-sided hockey-stick divergence
$\theta_{\mathrm{hs}}=\mathrm H_{e^\varepsilon}(P_1\|P_0)$ for a fixed $\varepsilon\ge0$. Let $\mathsf L^\circ$ have deterministic kernels and
$\mathsf L^\circ(x_0;\rho)=\mathsf L^\circ(x_1;\rho)$ for every $\rho$, so all three vanish there. Fix $\epsilon_{\mathrm{acc}}\in(0,1)$, $\alpha>0$ and $\alpha'\ge0$ with
$\alpha+\alpha'<1$. A certifier is *accurate at $\mathsf L^\circ$* when $\Pr_{\mathsf L^\circ}[\hat t\le\epsilon_{\mathrm{acc}}]\ge1-\alpha'$. Let $N_b$ count its Train
calls at $x_b$, $c_{\mathrm{acc}}=-\ln(1-\epsilon_{\mathrm{acc}})$ and $\Lambda_{\alpha,\alpha'}=(1-\alpha')\ln((1-\alpha')/\alpha)$.

Statement. (a) One pair. Let a certifier, in either mode and passing seeds by value or not, be sound at level $\alpha$ over every learning function
with deterministic kernels and accurate at $\mathsf L^\circ$. For each of the three targets, $\mathbb E_{\mathsf L^\circ}[N_1]\ge\Lambda_{\alpha,\alpha'}/c_{\mathrm{acc}}$.
For $\theta_{\mathrm{ex}}$ and $\theta_{\mathrm{tv}}$, also $\mathbb E_{\mathsf L^\circ}[N_0]\ge\Lambda_{\alpha,\alpha'}/c_{\mathrm{acc}}$. Calls at every other training input, which
include fine-tunes from a trained model, warm starts and approximate-unlearning steps, do not enter these bounds. For $\theta_{\mathrm{ex}}$ some
certifier sound over every learning function is accurate at $\mathsf L^\circ$ with
$\mathbb E[N_0]=\mathbb E[N_1]=(1-\alpha')\lceil\ln((1-\alpha')/\alpha)/c_{\mathrm{acc}}\rceil$. For $\theta_{\mathrm{tv}}$ and $\theta_{\mathrm{hs}}$ the same holds with
$\epsilon_{\mathrm{acc}}$ replaced by $\epsilon_{\mathrm{acc}}-\eta$ in $c_{\mathrm{acc}}$, for every $\eta\in(0,\epsilon_{\mathrm{acc}})$.

(b) Every record. Let $D$ hold $n_D$ distinct records $z_1,\dots,z_{n_D}$ and let $D'\mapsto x(c,D')$ be injective on $\{D\}\cup\{D\setminus\{z_i\}\}_i$. Put
$x^{(0)}=x(c,D)$ and $x^{(i)}=x(c,D\setminus\{z_i\})$, record $i$ having $D^0_j=D$ and $D^1_j=D\setminus\{z_i\}$, take as target the maximum over $i$ of
the target of record $i$, and let $\mathsf L^\circ$ return one model at all $n_D+1$ inputs for each seed. Under the hypotheses of (a), for each of the three
targets the calls at $x^{(1)},\dots,x^{(n_D)}$ together have expectation at least $n_D\Lambda_{\alpha,\alpha'}/c_{\mathrm{acc}}$, and for $\theta_{\mathrm{ex}}$ and
$\theta_{\mathrm{tv}}$ the calls at $x^{(0)}$ have expectation at least $\Lambda_{\alpha,\alpha'}/c_{\mathrm{acc}}$. With $N=\lceil\ln(1/\alpha)/c_{\mathrm{acc}}\rceil$
common seeds, one base run and $n_D$ twin runs at each give a certificate of $\theta_{\mathrm{ex}}$ sound at level $\alpha$ and accurate at $\mathsf L^\circ$
with $\alpha'=0$, at $N(n_D+1)$ calls, and the same holds for $\theta_{\mathrm{tv}}$ and $\theta_{\mathrm{hs}}$ with $\epsilon_{\mathrm{acc}}-\eta$ in place of
$\epsilon_{\mathrm{acc}}$.

(c) The base input for the one-sided target. Some certifier of $\theta_{\mathrm{hs}}$ at $\varepsilon=1$, sound at level $0.05$ over every learning function and
accurate at $\mathsf L^\circ$ with $\epsilon_{\mathrm{acc}}=0.01$ and $\alpha'=0$, makes four calls at $x_0$, while $\Lambda_{0.05,0}/c_{0.01}$ is about 298. So no
bound at the base input of the kind in (a) holds for $\theta_{\mathrm{hs}}$.

Proof of (a), lower bound at $x_1$ for $\theta_{\mathrm{ex}}$. The construction is argon's. By (F9) identify $(\mathcal R,\mu)$, outside a $\mu$-null set $\mathcal N_0$,
with $[0,1)$ and Lebesgue measure. Fix $p\in(\epsilon_{\mathrm{acc}},1)$, an integer $M$ with $m=\lceil pM\rceil<M$, the cells $I_r=[(r-1)/M,r/M)$, and a unit vector
$\mathbf e$. For an $m$-subset $B$ of $\{1,\dots,M\}$ let $S_B=\bigcup_{r\in B}I_r$, viewed in $\mathcal R\setminus\mathcal N_0$, and let $\mathsf L_B$ agree with $\mathsf L^\circ$
except that $\mathsf L_B(x_1;\rho)=\mathsf L^\circ(x_1;\rho)+2\Delta\mathbf e\,\mathbf 1[\rho\in S_B]$. At seeds in $\mathcal N_0$, which a caller may pass by value, $\mathsf L_B$
equals $\mathsf L^\circ$. It has deterministic kernels, and the twin of $x_0$ at seed $\rho$ differs from the node's model by $2\Delta\mathbf 1[\rho\in S_B]$, so
$\theta_{\mathrm{ex}}(\mathsf L_B)=m/M\ge p>\epsilon_{\mathrm{acc}}$.

Couple the certifier's runs against $\mathsf L^\circ$ and $\mathsf L_B$ with common coins and a common triple per call, as in the proof of lem-needle-lower-bound. A
call at an input other than $x_1$, a call at $x_1$ whose seed lies outside $S_B$, and every Eval and Open call on what these return get the same answer in
both runs. A seed is drawn, named or passed by value, and in each case it is a function of the history and of fresh draws, and the run against $\mathsf L^\circ$
does not depend on $B$. So the runs agree, and output the same $\hat t$, unless one of the at most $N_1$ cells that the seeds of the $\mathsf L^\circ$ run's calls at
$x_1$ visit lies in $B$. Let $E=\{\hat t\le\epsilon_{\mathrm{acc}}\}$ in the $\mathsf L^\circ$ run, with probability $q\ge1-\alpha'$. Soundness at $\mathsf L_B$ and
$\epsilon_{\mathrm{acc}}<m/M$ give $\Pr_{\mathsf L_B}[\hat t<m/M]\le\alpha$. For $B$ uniform, averaging gives
$$\alpha\ge\mathbb E_{\mathsf L^\circ}\Big[\mathbf 1_E\,\mathbf 1[N_1<M-m]\prod_{j=0}^{N_1-1}\Big(1-\frac m{M-j}\Big)\Big],$$
since the probability that $B$ avoids $K\le N_1$ given cells is $\binom{M-K}m/\binom Mm$, at least the product. If $\mathbb E_{\mathsf L^\circ}[N_1]=\infty$ there is
nothing to prove, so $N_1<\infty$ almost surely. The law of the $\mathsf L^\circ$ run does not depend on $M$, so dominated convergence as $M\to\infty$, with
$m/M\to p$, gives $\mathbb E[\mathbf 1_E(1-p)^{N_1}]\le\alpha$. Jensen's inequality for the convex map $u\mapsto(1-p)^u$ under the law given $E$ gives
$(1-p)^{\mathbb E[N_1\mid E]}\le\alpha/q$, so $\mathbb E[N_1]\ge q\ln(q/\alpha)/(-\ln(1-p))$. The map $q\mapsto q\ln(q/\alpha)$ increases on $q>\alpha/e$, and
$q\ge1-\alpha'>\alpha$, so $\mathbb E[N_1]\ge\Lambda_{\alpha,\alpha'}/(-\ln(1-p))$. Letting $p\downarrow\epsilon_{\mathrm{acc}}$ gives the bound.

Proof of (a), the other lower bounds. For $\theta_{\mathrm{ex}}$ at $x_0$, perturb $x_0$ instead, $\mathsf L_B(x_0;\rho)=\mathsf L^\circ(x_0;\rho)+2\Delta\mathbf e\,\mathbf 1[\rho\in S_B]$,
which moves the node's model by the same amount, so $\theta_{\mathrm{ex}}(\mathsf L_B)=m/M$ and the proof is unchanged. For $\theta_{\mathrm{tv}}$ and $\theta_{\mathrm{hs}}$
at $x_1$, use the shift $s\mathbf e$ in place of $2\Delta\mathbf e$. Let $Q_B$ be the law of $\mathsf L^\circ(x_0;\rho)+Z$ given $\rho\in S_B$. The laws $P_0$ and $P_1$ agree
on the part carried by seeds outside $S_B$, so $\mathrm{TV}(P_0,P_1)=\mu(S_B)\,\mathrm{TV}(Q_B,Q_B(\cdot-s\mathbf e))$, and a probability law on $\mathbb R^d$ and its
translate by $s\mathbf e$ have total variation tending to one as $s\to\infty$. For $\theta_{\mathrm{hs}}$, the half-space $\{y:\langle y,\mathbf e\rangle>s/2\}$ has
$P_1$-probability tending to $\mu(S_B)$ and $P_0$-probability tending to zero as $s\to\infty$. There are finitely many $B$ for each $M$, so some $s_M$ makes
both targets at least $\frac12(1+\epsilon_{\mathrm{acc}}/p)\,m/M\ge\frac12(p+\epsilon_{\mathrm{acc}})>\epsilon_{\mathrm{acc}}$ for every $B$, and the rest of the proof is
unchanged. For $\theta_{\mathrm{tv}}$ at $x_0$, perturb $x_0$ by $s\mathbf e$, and total variation is symmetric. This step fails for $\theta_{\mathrm{hs}}$, since
perturbing the denominator law $P_0$ adds mass that the factor $e^\varepsilon$ can cover, which is what (c) exploits.

Proof of the upper bounds in (a). For $\theta_{\mathrm{ex}}$, with probability $\alpha'$ output one at no call. Otherwise run the certificate of
thm-dataflow-composition (c) at level $\alpha/(1-\alpha')$ with $n=\lceil\ln((1-\alpha')/\alpha)/c_{\mathrm{acc}}\rceil$ coupled pairs. It fails to cover with
probability at most $(1-\alpha')\cdot\alpha/(1-\alpha')=\alpha$, since an output of one always covers. At $\mathsf L^\circ$ every pair coincides, no run exceeds
$\Delta$, and the bound $1-(\alpha/(1-\alpha'))^{1/n}$ is at most $\epsilon_{\mathrm{acc}}$ by the choice of $n$. For $\theta_{\mathrm{tv}}$ and $\theta_{\mathrm{hs}}$,
thm-dataflow-composition (b) with $R=1$ gives $\mathrm{TV}(P_0,P_1)\le\delta_{\mathcal N}(0;\Delta/\sigma)+\epsilon_0(\Delta)$ and
$\mathrm H_{e^\varepsilon}(P_1\|P_0)\le\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)+\epsilon_1(\Delta)$. At $R=1$ with a fixed choice, the identity-coupled pairs of
$\mathsf{Ex}_0$ and of $\mathsf{Ex}_1$ have one law up to the order of their coordinates, so $\epsilon_1(\Delta)=\epsilon_0(\Delta)$ and one set of pairs serves
both. Choose $\Delta$ with $\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)\le\eta$, possible since $\delta_{\mathcal N}(\varepsilon;r)\to0$ as $r\to0$, and output
$\min\{1,\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)+\bar p\}$, with $\varepsilon=0$ for total variation, with $\bar p$ the bound above at accuracy $\epsilon_{\mathrm{acc}}-\eta$
(proven).

Proof of (b). Use the family $\mathsf L_{k,B}$ that perturbs only $x^{(k)}$ on $S_B$, with $k$ uniform on $\{1,\dots,n_D\}$ and independent of $B$. Its target is
that of record $k$, at least $m/M$ for $\theta_{\mathrm{ex}}$ and above $\epsilon_{\mathrm{acc}}$ for the other two after the shift of (a). With $N^{(k)}$ the calls at
$x^{(k)}$ in the $\mathsf L^\circ$ run, the argument of (a) gives
$\alpha\ge\mathbb E[\mathbf 1_E\frac1{n_D}\sum_k(1-p)^{N^{(k)}}]\ge\mathbb E[\mathbf 1_E(1-p)^{N_{\mathrm{tw}}/n_D}]$ in the limit, by convexity of $u\mapsto(1-p)^u$, with
$N_{\mathrm{tw}}=\sum_kN^{(k)}$, and the rest of (a) gives the first bound. For $\theta_{\mathrm{ex}}$ and $\theta_{\mathrm{tv}}$, perturbing $x^{(0)}$ moves every
record's pair at once and gives the bound at $x^{(0)}$. For the upper bound, let $\bar p_k$ be the level-$\alpha$ Clopper and Pearson bound for record $k$ from
the $N$ common seeds, and output $\max_k\bar p_k$ for $\theta_{\mathrm{ex}}$ and $\min\{1,\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)+\max_k\bar p_k\}$ for the other two.
For a fixed $k^\star$ attaining the maximal target, the output undercovers only if $\bar p_{k^\star}$ undercovers the exceedance probability of record $k^\star$,
which has probability at most $\alpha$, since that record's indicators are independent across seeds. At $\mathsf L^\circ$ no pair exceeds, and the output is at
most $1-\alpha^{1/N}$ plus the allowance (proven, the certificate without a union bound is argon's).

Proof of (c). Astra's certifier, re-checked here. Let $\mathsf L^\circ$ return the zero model at both inputs. The certifier draws and opens four models at $x_0$ and 368
at $x_1$, and outputs $0.01$ if all are zero and one otherwise. Let $a$ and $b$ be the probabilities that $x_0$ and $x_1$ return exactly the zero model. If
$a\ge1/e$ and $b\ge0.99$, then $P_1(E)-eP_0(E)\le b\,\mathcal N(0,\sigma^2I_d)(E)-ea\,\mathcal N(0,\sigma^2I_d)(E)+(1-b)\le0.01$ for every event $E$, so
$\theta_{\mathrm{hs}}\le0.01$ and every output covers. If $a<1/e$, four zeros at $x_0$ have probability below $e^{-4}<0.0184$. If $b<0.99$, 368 zeros at $x_1$
have probability below $0.99^{368}<0.0248$. So whenever $\theta_{\mathrm{hs}}>0.01$ the output $0.01$ has probability below $0.05$. At $\mathsf L^\circ$ the output is
$0.01$ always, with four calls at $x_0$, while $\ln(1/0.05)/(-\ln0.99)=298.1$ (computed).

Label. Proven, (a) to (c).

Numbers. At $\alpha=\alpha'=10^{-3}$ and $\epsilon_{\mathrm{acc}}=10^{-2}$, (a) gives at least 686.5 expected calls at $x_1$, and at $x_0$ for the coupled tail and total
variation, and 688 pairs suffice for the coupled tail. For 60,000 distinct records, (b) gives at least $4.12\times10^7$ expected twin calls, and
$688\times60{,}001\approx4.13\times10^7$ calls suffice (computed). Each count multiplies the cost of one run, by the remark of def-seed-access-modes.
thm-record-level-certificate certifies the fraction of records whose tail exceeds a threshold at a cost free of $n_D$, so the price of the every-record
certificate is the price of its worst-case target.

Realization (heuristic). With the seed fixed, a Train call is one run of the pipeline. For $\theta_{\mathrm{tv}}$ and $\theta_{\mathrm{hs}}$, thm-coupling-free-soundness
makes the certificate sound under any implementable coupling with the right marginals, so realization needs each run to have the deployed law at its input and
repetitions to be independent, which on GPUs is the fidelity assumption of def-learning-oracle. Accuracy at a zero-leakage function needs the pairs to coincide,
which needs deterministic kernels. For $\theta_{\mathrm{ex}}$ the certificate needs the identity coupling itself. fact-controlled-nondeterminism-exact-replication
realizes deterministic kernels on one GPU type, and across types at 1.2 to 1.7 times the training time, for a pipeline modified in precision, rounding and
dropout. The certified pipeline is then that modified one, and it must be the deployed one. fact-rerun-reproduction-error shows that whole uncontrolled GPU
reruns do not coincide.

Remark, scope. The bound holds because soundness ranges over every learning function, so the model at $x_1$ is unlinked from the model at any surrogate input. A
class restricted by a known stability bound on $\|\mathsf L(x_1;\rho)-\mathsf L(x';\rho)\|$ for a surrogate $x'$ would let surrogate calls count (argon). XD23
certifies a different target, a mutual-information bound averaged over a data law, from drawn runs of the mechanism, and this theorem says nothing about it. The
proof is a rare-event change of measure. Kaufmann, Cappé and Garivier (JMLR 2016, Lemma 1), as astra points out, relate expected sample counts to discrimination
under mutual absolute continuity, which the singular construction here does not satisfy, so the finite-partition argument is needed for adaptive seeds passed
by value.

Without the oracle, or in the other regime. Without named seeds, thm-dataflow-composition (e) prices the twin certificate above the coupled one in the drawn mode.
With the oracle, (a) says the oracle supplies no twin for free. Each twin is one call, a surrogate is a call at another input and counts for nothing, and what the
oracle supplies is the named seed, which real training also offers. The statement is statistical. By the remark of def-seed-access-modes it becomes a bound in
oracle cost, and a bound in compute under the no-skipping hypothesis.
