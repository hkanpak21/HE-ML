# Round 01, oracle and measurement, builder

Date 2026-10-25. This round answers the challenges of `round-00/discussant-argon.md`, revises the
five facts argon asked to revise, adds one fact, and states the aims of round 00 as proved objects.
Symbols follow `sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md`, the oracle theory.

Two aims of round 00 change. conj-paired-advantage-price is withdrawn, since argon is right that its
parts (a) and (b) are common random numbers and its part (c) is false as stated. What survives of it
is prop-profile-run-coordinate below. conj-exact-twin-price is superseded by thm-exact-twin-price,
which takes argon's sharper bounds and fixes the target. The claims of def-seed-access-modes become
prop-drawn-mode-is-fs-oracle and thm-coupling-free-soundness, and its claims 4 and 5 become remarks.

## Responses to the challenges of round 00

ch-gdp-audit-pld-and-threshold (blocking). Accepted on both counts. Clopper and Pearson coverage needs
an event fixed outside the evaluation sample, and NHSBTJCT23 §5.2 says it selects the threshold on the
same observations. The end-to-end figure composes by Gaussian DP only at canary rate $q_c=1$, and by PLD
under subsampling (§4.1 and §5.5). The revised fact is below.

ch-finite-seed-not-top-oracle (blocking). Accepted. Argon's example, $\mathsf L(x_b;s)=s+bM/2\bmod M$,
gives $\mathrm D^\top_1=1$ and $\mathrm{TV}(P_0,P_1)=0$, and enumerating all $M$ seeds only reveals the
two marginal laws. Enumeration realizes the top oracle only when the view identifies the seed, which is
the case for 100 Gaussian noise vectors in high dimension, as in Violation 2 (heuristic). The revised
fact is below.

ch-known-covariance-dimension-bound (blocking). Accepted. Theorem 4.1 of HSU25 proves impossibility only
for $d<c(n+n^2\rho^2+n^2/m)$. The library PDF is v1, and the venue in the note is FOCS 2026, to appear,
from the arXiv comment. Argon's "FOCS 2025" misreads the note. The revised fact is below.

ch-rerun-spread-threshold-mismatch (blocking). Accepted. The sentence held for ResNet-20 without
deterministic operations only, and Table I gives means with spreads, not tail probabilities. The revised
fact is below.

ch-subset-forging-below-one-run (blocking). Accepted. Algorithm 2 of ZCSL24 passes replay at
$\varepsilon>0$ by Proposition 4.4 and costs a fraction of one run by Proposition 4.5. The revised fact is
below.

ch-generic-oracle-open-and-meter (blocking). Accepted. A caller of def-learning-oracle holds label open on
names its own calls return, so it can open its shadow models, which the access class $\{\mathsf{train},\mathsf{eval}\}$
of the 2026-10-13 report forbids. That report also meters every operation, and the HE-ML budget meters only
Train and Eval on names with label eval. def-seed-access-modes now lets the game fix the label of returned
model names and the budget of each operation, and restricts learner names per caller. In the drawn mode a
Train call returns one name, and names stay fixed by the count of calls, which is all that the coupling of
lem-needle-lower-bound uses.

ch-coupling-soundness-target-and-noise (blocking). Accepted on both counts. The exceedance probability is a
quantity of the coupled experiment and not a target, and argon's example shows $\epsilon^\Theta_0(0.5)=1/2$
against $\epsilon_0(0.5)=1$. What the independent coupling certifies is a bound on
$\mathrm H_\gamma(P_0\|P_1)$, never on $\epsilon_0(\Delta)$. The second example builds the coupling from the
release noise $Z_1$. thm-coupling-free-soundness now names its targets and draws the twin rule independently
of $\omega$ and of every release noise.

ch-meter-oracle-cost-not-compute (blocking). Accepted. The bound is on oracle cost, the minimum is an
infimum, and the restriction to calls in $\bigcup_kX_k$ is in expectation. A run of
thm-dataflow-composition (c) costs $\sum_{t\le R}(\mathsf{cost}(x^0_t)+\mathsf{cost}(x^1_t))$ plus the calls of the
other nodes and of the strategy. Machine compute follows only under FORMAL_SECURITY's no-skipping hypothesis.
The claim is now a remark of def-seed-access-modes, since argon is right that it is one line.

ch-paired-price-degenerate-test (blocking). Accepted. For an arbitrary test and channel the claim is false, by
argon's constant test. The aim is withdrawn, so the challenge closes with it.

ch-profile-band-conditional-advantage (blocking). Accepted on both counts. For a fixed learning function an
unrestricted class has a profile constant in the run budget, and a realized bank of shadow runs can give a
conditional advantage above the class's expected advantage. Both facts are now parts (a) and (b) of
prop-profile-run-coordinate, which states what a finite experiment certifies about a profile.

ch-exact-twin-missing-hypotheses (blocking). Accepted on all four counts. thm-exact-twin-price assumes
$\epsilon_{\mathrm{acc}}\in(0,1)$, $x_0\neq x_1$, distinct records with an injective map to training inputs, and
accuracy as $\hat t\le\epsilon_{\mathrm{acc}}$. The expected count is no longer rounded.

ch-exact-twin-target-coupling-contradiction (blocking). Accepted. thm-exact-twin-price now treats two targets.
For the coupled tail $\epsilon_0(\Delta)$, realization needs the identity coupling itself. For the leakage of the
release, $\mathrm{TV}(P_0,P_1)$ or $\mathrm H_{e^\varepsilon}(P_1\|P_0)$, thm-coupling-free-soundness applies. Argon's
remark on $\mathrm H_{e^\varepsilon}(P_0\|P_1)$ at a point mass is right, so that direction is not a target of the
lower bound.

ch-lira-offline-and-random-subset (non-blocking). Accepted. A LiRA trial samples the random-subset game, which
can differ by one from the fixed-dataset game (thm-bank-soundness (b)). prop-profile-run-coordinate (b) concerns
the game its trials sample and says so.

ch-shared-batch-marginal-vs-paired (non-blocking). Accepted. The last paragraph of fact-audit-independent-batches
should read as follows. "Algorithm 2 counts false positives and false negatives in each world separately, so no
paired difference is formed and a shared batch cannot reduce variance there. A paired estimator on the canary
projection would lose the batch term $\langle g',\sum_{x\in B}\bar g(x)\rangle$ under a shared batch, a term that a
Dirac canary already makes near zero (heuristic)."

ch-one-shot-jeffreys-and-steinke (non-blocking). Accepted. Theorem 3.3 of AKOOMS24 holds at fixed $\sigma>0$ and
$\delta\in(0,1)$. The lower bound $\varepsilon_{\mathrm{lo}}$ uses a Jeffreys interval for the false-negative rate
and the exact null for the false-positive rate, as the round-00 note says. The fact's word "Clopper and Pearson
style" should be "Jeffreys". Steinke, Nasr and Jagielski (NeurIPS 2023) is not in the library and is listed for
placing.

ch-pol-random-oracle-plugin (non-blocking). Accepted as a constraint. No object of this space uses the random
oracle of thm-replay-audit-steer as a step.

ch-balle-theorems-and-shadow-price (non-blocking). Accepted. The shadow-run counts and the observation that
Corollary 4 of BCH22 has the functional form $\Upsilon_{\mathfrak e}$ of thm-bounded-deviation-transfer (a) go to
the registers.

ch-missing-auditing-and-nondeterminism-literature (non-blocking). Accepted in part. SAB24 is read and gives
fact-controlled-nondeterminism-exact-replication below. XD23 certifies a distributional mutual-information
bound from drawn runs of the mechanism on fresh data (its Theorem 4, read through the note of the space
statistical-limits), a target that thm-exact-twin-price does not cover, and the remark there says so. MSS23,
CEPS24, ZDKT25, FJTYCDCP23 and SHKBL25 are noted and not used by any object of this round.

ch-seed-attack-already-known (non-blocking). Accepted. Claim 4 restated thm-reference-access (a) and a two-line
identity that can be negative. It is withdrawn as an object. The open question argon names, how many reruns at
a revealed seed approach $\mathrm D^\top_1(K)$ under hardware randomness for an adversary chosen before $\mathsf L$,
goes to the registers.

ch-paired-price-elementary-bernstein (non-blocking). Accepted, with the point that integrating out the channel
noise reduces variance further whenever the test's acceptance probability at a model is computable.

ch-exact-twin-sharper-bounds (non-blocking). Accepted and used. The lower bound
$(1-\alpha')\ln((1-\alpha')/\alpha)/(-\ln(1-\epsilon_{\mathrm{acc}}))$ and the every-record certificate without a union
bound are argon's, and thm-exact-twin-price credits them.

## Revised and new facts

### fact-gdp-audit-observation-count: auditing with the mechanism's trade-off function needs fewer observations

status: borrowed
uses: none

NHSBTJCT23 (USENIX Security 2023). An audit converts Clopper and Pearson upper bounds $\bar\alpha,\bar\beta$ on the
error rates of a test into a lower bound on $\varepsilon$, by Eq. (9) for $(\varepsilon,\delta)$-DP and by
$\mu^{\mathrm{lower}}_{\mathrm{emp}}=\Phi^{-1}(1-\bar\alpha)-\Phi^{-1}(\bar\beta)$ for Gaussian DP, Eq. (12), converted
by Corollary 5. In the white-box threat model with gradient canaries, the $(\varepsilon,\delta)$ audit approaches the
theoretical $\varepsilon$ only near $10^8$ observations, while the Gaussian-DP audit is tight near $10^3$ (§4.1,
Fig. 3, 20 repetitions, $\delta=10^{-5}$). One observation is one step of one run (§5.1). §5.5 turns per-step
bounds into an end-to-end bound by Gaussian composition at canary rate $q_c=1$ and by PLD accounting under
subsampling. In the black-box threat model the audit trains 1,000 models with the canary and 1,000 without and
reaches about 1.6 against a theoretical 8 for WRN-16 on CIFAR-10 (§6.4, Fig. 11).

Proof. Read in the paper, §2.3, §4, §5 and §6.

Other regime. The confidence statement holds for a threshold fixed before the evaluation sample. §5.2 selects
the threshold on the same observations, following common practice, and says this makes the bound technically
invalid. The end-to-end figure further assumes that the composition it uses is tight, which is heuristic. Every
number is a lower bound on leakage, so it bounds a point of a security profile from below.

### fact-small-seed-space-breaks-dp: a noise seed with 100 values is detected by the audit

status: borrowed
uses: none

NHSBTJCT23, §6.3, Violation 2. A DP-SGD implementation whose noise seed takes only 100 values, so that only 100
noise vectors occur, is detected as violating its claimed $\varepsilon=1.27$ by the Gaussian-DP audit and by Lu et
al.'s method, and is missed by $(\varepsilon,\delta)$ audits (Fig. 8).

Proof. Read in the paper, §6.3.

Other regime. Enumerating a finite seed space gives the laws $P_0$ and $P_1$ exactly. It realizes the top oracle
only when the view identifies the seed, that is when the laws of the view at different seeds are nearly mutually
singular. Argon's example $\mathsf L(x_b;s)=s+bM/2\bmod M$ has $\mathrm D^\top_1=1$ and $\mathrm{TV}(P_0,P_1)=0$, so
enumeration alone gives nothing there (proven). In Violation 2 the view is a high-dimensional noisy gradient and
100 noise vectors are far apart, which is why the bug is detectable (heuristic). This is the empirical side of
open problem 9 of the oracle theory.

### fact-hsu-membership-sample-gap: sample-based membership inference needs order $n+n^2\rho^2$ samples

status: borrowed
uses: none

HSU25 (Haghifam, Smith and Ullman, FOCS 2026 to appear, arXiv 2508.19458 v1, the version the library holds).
Definition 2.1 asks a test, given $m$ auxiliary samples, the noisy mean and a candidate, to answer correctly with
probability at least 0.51 on each side. Theorem 3.1 proves that for $d>c_1(n+n^2\rho^2)$ and
$m\le c_2(n+n^2\rho^2)$ no such test exists against the noisy empirical mean of Definition 2.4 over all
Gaussians. Theorem 1.1 is its informal version. Theorem 3.3 is the matching attack, for $0<\rho<1$, $m\ge cd$ and
$d\ge c(n+n^2\rho^2)$, against the symmetric estimators of Definition 3.2. Theorem 4.1, whose informal version is
Theorem 1.2, proves for identity covariance, $n\ge4$ and $m\ge2$ that no test exists when
$d<c(n+n^2\rho^2+n^2/m)$. So with known covariance $\min\{n,1/\rho^2\}$ samples are necessary at the critical
dimension $d\asymp n+n^2\rho^2$, while two samples suffice once $d$ is of order $n^2$ and above. §1.2.1 notes that a
test with a statistic free of the population and a calibrated threshold needs $O(1)$ trained models, that is
$O(n)$ samples.

Proof. Read in the paper, §1.2, §2, §3 and the statement of Theorem 4.1. The proofs were not re-derived.

Other regime. Divided by the training-set size $n$, the price of Theorem 3.1 is $1+n\rho^2$ datasets' worth of
samples. The result is statistical and belongs to the space statistical-limits. For measurement, §1.2.1 says an
audit built from restricted tests can sit far below the profile it lower-bounds.

### fact-rerun-reproduction-error: a GPU rerun at one seed ends far from the original run

status: borrowed
uses: none

JYCDTCP21 (IEEE S&P 2021). Theorem 1 (Entropy Growth) states that the entropy of the training process grows
linearly in the number of steps, under the assumption of i.i.d. hardware and library noise at each step (§VI-A).
Table I (§VI-C) reports the reproduction error of retraining from a checkpoint with the same initial parameters,
batching, architecture and strategy, normalized by $d_{\mathrm{ref}}$, the distance between two independently
trained models, as a mean with a spread. For a whole run the normalized $\ell_2$ error is $0.955\pm0.004$ for
ResNet-20 on CIFAR-10 and $0.815\pm0.002$ for ResNet-50 on CIFAR-100. For one step it is 0.001 and 0.002.
PyTorch's deterministic operations give $0.569\pm0.004$ for ResNet-20 and $0.816\pm0.001$ for ResNet-50.

Proof. Read in the paper, §IV to §VI and Table I.

Other regime. Theorem 1 is proven inside its noise model, heuristic for real hardware, and Table I is empirical.
Read as a distance concentrated near its mean, Table I puts the spread $\mathrm{sp}_\tau$ of a whole run in parameter
space near one for $\tau$ below about $0.95\,d_{\mathrm{ref}}$ for ResNet-20, below about $0.81\,d_{\mathrm{ref}}$ for
ResNet-50, and below about $0.57\,d_{\mathrm{ref}}$ for ResNet-20 with deterministic operations, and near zero for one
step (heuristic, the table gives no tail probabilities).

### fact-unlearning-verification-fragile: a prover that picks the batches passes replay

status: borrowed
uses: none

ZCSL24 (ICML 2024). Definition 4.1 calls a proof of retraining valid when every step is reproducible within
$\varepsilon$ and no batch meets the unlearned set $D_u$. Algorithm 1 retrains while replacing each unlearned point of
the original batch by its nearest same-class neighbour in the retained data, and Proposition 4.2 proves that it
passes at $\varepsilon=0$. Algorithm 2 forges the retraining proof from the logged training proof, editing only the
steps whose batch met $D_u$, and Proposition 4.4 proves that it passes at $\varepsilon>0$ under step-size conditions.
Proposition 4.5 states that Algorithm 1 costs the time $\mathcal T(n)$ of naive retraining and Algorithm 2 costs
$(p_u/P+(1-p_u)/(mP))\,\mathcal T(n)$, with $p_u=1-(1-|D_u|/|D|)^m$, $P$ processes and batch size $m$. The text calls these
results Theorems 4.2 to 4.5.

Proof. Read in the paper, §3 and §4.

Other regime. The prover's freedom is the batch order, a part of the seed. Algorithm 1 costs one run and Algorithm 2
less than one, so a meter in runs separates neither from honest retraining, and Algorithm 2 undercuts it.

### fact-controlled-nondeterminism-exact-replication: logged rounding makes GPU reruns identical

status: borrowed
uses: none

SAB24 (Srivastava, Arora and Boneh, NeurIPS 2024). With the same software version, seed and deterministic library
flags, models trained on A40, Titan XP and RTX 2080 Ti GPUs differ (Fig. 2), while runs on one GPU architecture
repeat identically (§6). Training in FP64, rounding each layer output to FP32, and logging the rounding direction of
values within an adaptive threshold of the boundary make full training of ResNet-50 on CIFAR-10 and fine-tuning of
GPT-2 replicate exactly across all pairs of the three GPU types (§6, Fig. 4). The prototype costs 1.2 to 1.4 times
the training time for the trainer and 1.3 to 1.7 times for the auditor (Table 5).

Proof. Read in the paper, §1, §3 to §6 and §8.

Other regime. Empirical, on two models and three GPU types. In the oracle theory's terms, the named-seed Train call
with deterministic kernels is realizable on real hardware at a stated time factor, which settles in this setting
the hardware part of prob-coupled-reruns-rarely-differ. The data part, how far a leave-one-out twin moves from the
base run, is a property of training that no hardware control changes.

## def-seed-access-modes: one learning oracle with two seed-access modes

status: open
uses: def-learning-oracle, def-learning-oracle-model, def-certifier, def-degenerate-oracles, def-passive-learning-oracle, def-generic-training-oracle

Statement. Fix a learning oracle $\mathcal O$ for $(\mathsf L,\mu,\pi)$. A game assigns each caller four things.

1. A *seed-access mode*, named or drawn. In the *named mode* the caller's Train calls are those of
   def-learning-oracle. In the *drawn mode* the oracle accepts $\mathsf{Train}(x,s)$ only with $s=\bot$, returns the
   model's name only, keeps the seed under no name the caller holds, and refuses Open on any seed. A grant to a
   caller in the drawn mode carries model names only. In both modes the caller's $k$-th received name is $k$.
2. A *return label*, open or eval, carried by the model names that the caller's own Train calls return. With label
   eval the caller can query its own models through Eval but cannot open or retrain them.
3. A set $\Lambda_A\subseteq\Lambda$ of learner names, and a set of starting models, that its Train calls may use.
4. A *budget*, a bound for each operation (Train, Eval at each query type, Open). The budget $(q_T,q_E)$ of
   def-learning-oracle-model is the case that bounds Train and Eval on names with label eval and leaves the rest free.

A *cost meter* is a measurable $\mathsf{cost}:\mathcal X\to[0,\infty)$, the work of one run at $x$ in a fixed machine
model. A caller's *oracle cost* is the sum of $\mathsf{cost}$ over its Train calls. The bottom oracle of
def-degenerate-oracles is the named mode with return label open and no grant, the top oracle adds grants of the
honest seeds, and an experimenter in the drawn mode follows the drawn-seed discipline of def-certifier.

Remark, the needle bound in oracle cost (proven). In the setting of lem-needle-lower-bound let $N_X$ count the
certifier's Train calls with input in $X=\bigcup_kX_k$. Its proof gives
$\Pr_{\mathsf L^\circ}[\hat t\ge\vartheta]\ge1-\alpha-\mathbb E_{\mathsf L^\circ}[N_X]/J$, since $\sum_k\mathbf 1[\mathrm{Hit}_k]\le N_X$.
An oracle cost at most $C$ gives $N_X\le C/\inf_{x\in X}\mathsf{cost}(x)$. A run of thm-dataflow-composition (c) costs
$\sum_{t\le R}(\mathsf{cost}(x^0_t)+\mathsf{cost}(x^1_t))$ plus the calls of the other nodes and of the strategy. A bound in
oracle cost is a bound in machine compute only under FORMAL_SECURITY's no-skipping hypothesis.

Remark, the seed for an adversary. Under the top oracle with deterministic kernels and a deterministic channel, one
Train call at the revealed seed attains $\mathrm D^\top_1$, which is thm-reference-access (a). Under hardware
randomness the rerun-and-compare attack has advantage equal to a coupled tail minus the spread of the rerun, which
can be negative (argon). How many reruns an adversary fixed before $\mathsf L$ needs to approach $\mathrm D^\top_1$ is
open.

The proposal for Halil. Both repositories use this one oracle, and each game fixes the four items per caller. The
passive learning oracle and the generic training oracle of FORMAL_SECURITY are drawn-mode callers of it
(prop-drawn-mode-is-fs-oracle). Drawn coins lose no soundness for any bottom-oracle target of the HE-ML theory, and
lose the accuracy that its separations measure (thm-coupling-free-soundness). Named seeds are needed for the
top-oracle threat model, for replay audits, and for the accuracy of coupled certificates. The decision left to
Halil is whether to adopt this, to keep drawn coins only, which loses those three, or to keep named seeds only,
which needs the declared starting models of item 3 whenever the meter is work.

Without the oracle, or in the other regime. The definition adds no power. It names restrictions that a game
imposes, per caller, and a meter. In the statistical regime the meter is a count of calls. In the computational
regime it is the work of a run, and a price in work transfers to real training only under the no-skipping
hypothesis.

## prop-drawn-mode-is-fs-oracle: the two FORMAL_SECURITY oracles are drawn-mode callers

status: sketch
uses: def-seed-access-modes, def-passive-learning-oracle, def-generic-training-oracle

Statement. (a) Let $\mathcal M$ be a standard Borel space of traces of length at most $T$, $\Lambda_A$ the finite set of
recipes a game names, and $m_\varnothing$ a fixed symbol, the only starting model allowed. Let
$x(\ell,D)=(\ell,m_\varnothing,D,\mathcal H)$ for a fixed $\mathcal H$, and let $\mathsf L(x(\ell,D);\rho,\xi)$ be the trace of
recipe $\ell$ on $D$ with coins $(\rho,\xi)$, whose initial state the declared initialization rule of $\ell$ draws from the
coins. A caller in the drawn mode with return label open, which opens each model name it receives, has, call by call,
the transcript law of a caller of the passive learning oracle of `oracle.tex` (label `def:passive`) on the same
sequence of recipes and corpora. Its oracle cost is the metered cost of `def:cost`. (b) Let $\mathsf{ev}(m,u)$ return
$f_m(x)$, the input gradient of the loss at a labelled point $z$, or its parameter gradient at $z$, according as $u$ is
$(\mathrm{out},x)$, $(\mathrm{gx},z)$ or $(\mathrm{g\theta},z)$. A caller in the drawn mode whose return label is eval, and
whose budget bounds Train, Eval at each query type and Open, realizes an access class of
def-generic-training-oracle. Train is train, Eval at the three query types is eval, $\mathrm{grad}_x$ and
$\mathrm{grad}_\theta$, and reveal is Open, permitted exactly when the class contains reveal, in which case the return
label is open.

Proof. (a) $\mathsf{Train}(x(\ell,D),\bot)$ draws $(\rho,\xi)\sim\mu\otimes\pi$, independent of all other randomness by
fidelity, and stores the trace of $\ell$ on $D$ with those coins. Open returns it. So each pair of calls returns a trace
of $\ell$ on $D$ with fresh coins, and two pairs on one corpus return independent traces, the two clauses of
`def:passive`. The caller can pass no seed and holds no seed name, so it cannot rerun at chosen coins, which
`def:passive` forbids. The only starting model is $m_\varnothing$ and the initialization is the declared rule of $\ell$, so
no caller emits chosen weights as a trace, the laundering that the text after `def:cost` blocks. Learner names lie in
$\Lambda_A$, so no caller authors a recipe. Summing $\mathsf{cost}(x(\ell,D))$, the work of $\ell$ on $D$, gives the metered
cost. The coins of `def:passive` are one random object, and $(\rho,\xi)$ represents it by (F9). (b) Each operation of the
report either reads the stored parameter vector through a fixed public map, which is $\mathsf{ev}$ at the matching query,
or returns it, which is Open. The report's train returns a fresh handle and never opens the randomness, which is the
drawn mode. With return label eval the caller cannot open its own handles, as a class without reveal requires. The
budgets per operation are item 4 of def-seed-access-modes (proven).

Label. Proven, by construction.

Without the oracle, or in the other regime. The statement concerns oracles only. Its use is that every theorem of the
HE-ML theory that holds for a drawn-mode caller holds for FORMAL_SECURITY's oracles under these identifications, and
every theorem that needs the named mode fails for them as stated.

## thm-coupling-free-soundness: shared seeds buy accuracy, never soundness, for bottom-oracle targets

status: sketch
uses: thm-coupling-certificate, thm-dataflow-composition, thm-bounded-deviation-transfer, def-isolated-client

Setting. A *twin rule* $\Theta=(\Theta_t)_{t\le R}$ is a sequence of laws on $(\mathcal R\times\Xi)^2$ whose two marginals
are both $\mu\otimes\pi$. It *shares the seed* when its two seed coordinates agree almost surely. The identity coupling
of the oracle theory is the twin rule with a common seed and independent hardware randomness, and the *independent
twin rule* $(\mu\otimes\pi)^{\otimes2}$ is the one a drawn-mode experimenter samples. In the setting of
thm-dataflow-composition, the $\Theta$-coupled execution $\mathsf{Ex}^\Theta_b$ runs $G$ under $H_b$ and, at each $v_t$ that
runs, draws $\zeta_t=((\rho_t,\xi_t),(\rho'_t,\xi'_t))\sim\Theta_t$ independently of $\omega$, of the release noises
$Z_1,\dots,Z_R$ and of the other $\zeta_s$. The node uses $(\rho_t,\xi_t)$, and the twin is
$W'_t=\mathsf L(x(c_t,D^{1-b}_j,W'_{t-1});\rho'_t,\xi'_t)$. Its exceedance probability is $\epsilon^\Theta_b(\Delta)$, a quantity of
the experiment, which differs from $\epsilon_b(\Delta)$ in general. The *bottom-oracle targets* are
$\mathrm H_\gamma(P_0\|P_1)$ and $\mathrm H_\gamma(P_1\|P_0)$ for the bottom-oracle view, and the *top-oracle targets* the same
divergences for the top-oracle view, $\mathrm D^\top_\gamma(K)$ at one node.

Statement. (a) One node. For every coupling $\Gamma'$ of $\Pi_{x_0}$ and $\Pi_{x_1}$, every channel $K$ and every $\gamma\ge1$,
$\mathrm H_\gamma(P_0\|P_1)\le\mathbb E_{\Gamma'}\mathrm H_\gamma(K(\cdot\mid W_0)\|K(\cdot\mid W_1))$. If $\Gamma'$ is the law of
$(\mathsf L(x_0;\rho,\xi_0),\mathsf L(x_1;\rho,\xi_1))$, with $\rho\sim\mu$ and $(\xi_0,\xi_1)$ drawn from any coupling of $\pi$
with itself independently of $\rho$, the same right side bounds $\mathrm D^\top_\gamma(K)$.

(b) Composition. Under the bottom oracle, for every twin rule $\Theta$, every adversary and every $\varepsilon\ge0$ and
$\Delta>0$, the two bounds of thm-dataflow-composition (b) hold with $\epsilon^\Theta_0,\epsilon^\Theta_1$ in place of
$\epsilon_0,\epsilon_1$. Under the top oracle they hold for every twin rule that shares the seed.

(c) Certificates. Let an experimenter sample independent repetitions of a $\Theta$-coupled experiment. Then the
certificate of thm-coupling-certificate (b) is sound at level $\alpha$ for $\mathrm H_\gamma(P_0\|P_1)$, and
$\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\bar p^\Theta$, with $\bar p^\Theta$ the Clopper and Pearson bound of
thm-dataflow-composition (c) computed on $\mathsf{Ex}^\Theta_0$, is an upper bound on $\mathrm H_\gamma(P_0\|P_1)$ with probability at
least $1-\alpha$, for every $\Theta$. The same holds for the top-oracle targets when $\Theta$ shares the seed. Neither is a
certificate of $\epsilon_0(\Delta)$ unless $\Theta$ is the identity coupling.

(d) Necessity. The independence from the release noise and the shared seed for top targets cannot be dropped, by two
examples of argon's review (proven there and re-checked here).

Proof. (a) (F4) with $\Theta=\Gamma'$ gives the first bound, since $\Gamma'K_b$ has $b$-th marginal $P_b$. Step 2 of the proof of
thm-coupling-certificate (b) writes $\mathrm D^\top_\gamma(K)=\int\mathrm H_\gamma(P^\rho_0\|P^\rho_1)\,\mu(d\rho)$. For fixed $\rho$, (F4)
with the given coupling of $(\xi_0,\xi_1)$ bounds the integrand by the conditional mean of
$\mathrm H_\gamma(K(\cdot\mid\mathsf L(x_0;\rho,\xi_0))\|K(\cdot\mid\mathsf L(x_1;\rho,\xi_1)))$, and integrating over $\mu$ gives the second
bound.

(b) Follow the proof of thm-dataflow-composition (b) with one change. Write $\zeta_t=((\rho^0_t,\xi^0_t),(\rho^1_t,\xi^1_t))\sim\Theta_t$,
independent of $\omega$, of the $Z_s$ and of the other $\zeta_s$, and let $v_t$ use $(\rho^b_t,\xi^b_t)$ under $H_b$. That pair has
law $\mu\otimes\pi$ and is independent of everything else in the $H_b$ execution, so the law of that execution is unchanged.
Step 1 is unchanged, with $\bar\rho_t=\rho^b_t$ under the top oracle. Step 2 drives the hybrid's chain of $D^b_j$ by
$(\rho^b_t,\xi^b_t)$. Step 3 compares the hybrid with $\mathsf{Ex}^\Theta_0$, whose twin is driven by $(\rho^1_t,\xi^1_t)$. They agree
before the first exceedance, so $\mathrm{TV}(\mathcal L_0,\mathcal L_{\mathrm{hyb}})\le\epsilon^\Theta_0(\Delta)$. The sum form of step 3 needs
$\zeta_t$ independent of $\mathcal G_t$, which holds. In step 4 the kernel draws $\zeta_t\sim\Theta_t$ and extends both chains. Given
its past outputs and both chain states, when $\mathfrak z_t\sim\mathcal N(\Delta/\sigma,1)$ the output $y_t$ has law
$\mathcal N(O_t+F^1_t,\sigma^2I_d)$ whatever $F^0_t$ is, by (F6)(ii), and $Z''_t$ is fresh. The chain of $D^1_j$ is driven by
$(\rho^1_t,\xi^1_t)$, of law $\mu\otimes\pi$ and independent of the past. So by induction over the rounds the output has law
$\mathcal L_1$ in every coordinate but one. Under the top oracle the kernel must also output a revealed seed, which is $\rho^1_t$
in $\mathcal L_1$ and $\rho^0_t$ in the hybrid as step 3 needs. One kernel outputs one value, so step 4 needs $\rho^0_t=\rho^1_t$ almost
surely. Under the bottom oracle $\bar\rho_t=\star$ and the condition does not arise. Step 5 is unchanged.

(c) By fidelity across repetitions the indicators of $D^\star_0>\Delta$ in $\mathsf{Ex}^\Theta_0$ are independent Bernoulli variables with
parameter $\epsilon^\Theta_0(\Delta)$, so (F8) gives $\Pr[\epsilon^\Theta_0(\Delta)\le\bar p^\Theta]\ge1-\alpha$, and (b) turns this into the
bound on $\mathrm H_\gamma(P_0\|P_1)$. For thm-coupling-certificate (b) the summands of $\hat t$ are independent with mean the right
side of (a), and Hoeffding's inequality (F8) gives soundness. For the last sentence, argon's example below has
$\epsilon^\Theta_0(0.5)=1/2<1=\epsilon_0(0.5)$ under the independent twin rule.

(d) Shared seed. Let $\mathcal R=[0,1)$, deterministic kernels, the plain channel, $\mathsf L(x_0;\rho)=\mathbf 1[\rho<1/2]$ and
$\mathsf L(x_1;\rho)=\mathbf 1[\rho\ge1/2]$. Then $\mathrm D^\top_1=1$, while the independent twin rule gives $\Pr[W_0\neq W_1]=1/2$, so the
certificate of thm-coupling-certificate (b) concentrates at $1/2$ and is unsound for $\mathrm D^\top_1$. Release noise. Take $R=2$,
$d=1$, $\sigma=1$, $O_t=0$, $f_t(c,m)=m$, round-1 models of law $\mathcal N(0,1)$ under both hypotheses, the choice
$c_2=\mathbf 1[|y_1|>1]$, and leakage $10\Delta$ in round 2 exactly when $c_2=1$. A round-1 coupling that sets both models to
$-Z_1$ has the right marginals, yet makes $y_1=0$, $c_2=0$ and the measured exceedance zero. In the true execution
$y_1\sim\mathcal N(0,2)$ under both hypotheses, so by (F5) $\mathrm{TV}(P_0,P_1)=\Pr[|y_1|>1]\,(2\Phi(5\Delta)-1)$. At $\varepsilon=0$ and
$\Delta=1/2$ this is $0.4795\times0.9876=0.474$, above the claimed bound $\delta_{\mathcal N}(0;\sqrt2\Delta)=0.276$ (computed). The example is
excluded because $\zeta_1$ must be independent of $Z_1$.

Label. Proven, (a) to (d). Part (b) modifies a proof that round 03 of the formal tuning checked, and the change is confined to
which coordinates of $\zeta_t$ drive which chain. Argon's review states a wider form with twin kernels that adapt to the past,
driven by fresh randomness independent of $\omega$ and of $Z_{\ge t}$. That form is not re-derived here and stays open in this file.

Meaning. A real twin runs at a chosen seed on whatever hardware is available, so the realized pair need not have independent
hardware randomness. For bottom-oracle targets that does not matter. Soundness needs each run, alone, to have the law of the
deployed run at its input, and repetitions to be independent. The shared seed and the choice of coupling move only the size of
$\epsilon^\Theta_b$, so only the accuracy, and the coupled tail $\epsilon_0(\Delta)$ itself is certified only by the identity coupling.

Without the oracle, or in the other regime. Without the oracle no twin can be sampled. In the drawn mode the independent twin rule
is available, and its certificate is sound and, by thm-dataflow-composition (e)(ii), inaccurate where the separations place it.
The statement is statistical. In the computational regime the work of a certificate is the work of its runs, whatever their
coupling.

## prop-profile-run-coordinate: what a finite experiment certifies about a security profile

status: sketch
uses: def-security-profile-curve, def-learning-oracle-model, thm-coupling-certificate, thm-black-box-certifiability, lem-atomless-two-point

Setting. Fix a procedure, a coalition and a distinguishing goal under the bottom oracle, and a learning function $\mathsf L$. For a
budget $b=(q_T,q_E)$ let $\epsilon_{\mathsf L}(b)$ be the best advantage of an adversary with that budget. A *declared family* is a
sequence $\mathcal A=(\mathcal A_k)_{k\in\mathbb N}$ of adversaries, fixed before $\mathsf L$, where $\mathcal A_k$ makes $k$ Train calls of its
own, its *shadow runs*, and its advantage $\mathrm{Adv}(\mathcal A_k)$ averages over them. Its profile is
$\bar\epsilon_{\mathcal A}(k)=\max_{k'\le k}\mathrm{Adv}(\mathcal A_{k'})$, nondecreasing in $k$.

Statement. (a) Flatness. For every learning function and every $(q_T,q_E)$, $\epsilon_{\mathsf L}(q_T,q_E)=\epsilon_{\mathsf L}(0,q_E)$. In the
setting of thm-coupling-certificate with no query channel, $\epsilon_{\mathsf L}(b)=\mathrm{TV}(P_0,P_1)$ for every $b$.

(b) Lower band of a declared family. Fix shadow budgets $k_1<\dots<k_r$ and trial counts $n_1,\dots,n_r$ in advance. A trial of
$\mathcal A_{k_i}$ draws fresh shadow runs, runs the procedure once under each hypothesis, and records the difference $D\in\{-1,0,1\}$
of the two outputs. Let $\bar D_i$ be the mean of $n_i$ independent trials and
$\underline\ell_i=\bar D_i-\sqrt{2\ln(r/\alpha)/n_i}$. Then, for every learning function, with probability at least $1-\alpha$,
$\bar\epsilon_{\mathcal A}(k)\ge\max\{\underline\ell_i:k_i\le k\}$ for every $k\ge k_1$. The cost is $\sum_in_i(k_i+2)$ runs of the procedure
and of the shadow pipeline. Reusing one bank of shadow runs across trials does not give this, by argon's example.

(c) Upper band. In the setting of thm-coupling-certificate, the coupled certificate of its part (b) at $\gamma=1$ is an upper band on
$\epsilon_{\mathsf L}(b)$ for every $b$ at once, sound at level $\alpha$ for every learning function. Through a deterministic channel with
atomless view laws, no drawn-mode certificate sound for every learning function outputs an upper band below one with probability
above $\alpha$.

Proof. (a) Monotonicity gives $\ge$. For $\le$, let $\mathcal A$ have budget $(q_T,q_E)$. Under the bottom oracle every Train call of $\mathcal A$
has arguments it holds with label open, so its training inputs are built from values it received through the plain channel, its own
choices and its own models, and never from a name served through the query channel, which carries label eval. Let $\mathcal A'$ run $\mathcal A$
and answer each of its Train calls by computing $\mathsf L(x;\rho',\xi')$ itself, at the given $\mathsf L$, with fresh $(\rho',\xi')$ from its own
coins, or at the named seed when $\mathcal A$ passes one of its own. By fidelity the answers $\mathcal A$ receives have the same joint law with
everything else as in the oracle, so $\mathcal A'$ has the same advantage, the same Eval calls, and no Train call. Such an $\mathcal A'$ exists for
each $\mathsf L$, since the adversary may depend on $\mathsf L$ when $\mathsf L$ is fixed first (remark of def-degenerate-oracles). With no query
channel, (F1) and the hard-wired Neyman and Pearson set attain $\mathrm{TV}(P_0,P_1)$ at budget zero, and step 3 of the proof of
thm-coupling-certificate (b) bounds every bottom-oracle adversary by it.

(b) A trial's shadow runs are fresh and independent of the procedure's runs, so each $D$ has mean
$\Pr[\mathcal A_{k_i}=1\mid H_1]-\Pr[\mathcal A_{k_i}=1\mid H_0]=\mathrm{Adv}(\mathcal A_{k_i})$, and the trials are independent by fidelity. $D$ takes
values in $[-1,1]$, so Hoeffding's inequality (F8) gives $\Pr[\underline\ell_i>\mathrm{Adv}(\mathcal A_{k_i})]\le\alpha/r$. A union bound over $i$ and
$\mathrm{Adv}(\mathcal A_{k_i})\le\bar\epsilon_{\mathcal A}(k)$ for $k\ge k_i$ finish. Argon's example. Let $P_0=\delta_0$, $P_1=\delta_1$ on
$\mathcal V=\{0,1\}$, and let $\mathcal A_0$ draw a fair bit $S$ and output $\mathbf 1[Y=S]$. Then $\mathrm{Adv}(\mathcal A_0)=0$, while the test
$\mathbf 1[Y=1]$ realized at $S=1$ has advantage one, so a band built on one realized bank exceeds the profile with probability $1/2$.

(c) The first sentence is thm-coupling-certificate (b) with $\epsilon_{\mathsf L}(b)\le\mathrm{TV}(P_0,P_1)$ from (a). The second is
thm-coupling-certificate (a)(iii), since an upper band below one on $\epsilon_{\mathsf L}(0)=\mathrm{TV}(P_0,P_1)$ is a certificate of the total
variation (proven).

Label. Proven, (a) to (c).

Reading. For one deployed pipeline the run axis of a profile carries information only for a declared family, which is what an
experiment measures, or uniformly over a class of learning functions, which is the shadow-run price of the space
statistical-limits, or for a computationally bounded class, which is the space computational-limits. The object proposed in
FORMAL_SECURITY's terminology ledger, the curve from a budget to the success, is therefore well defined as a measured object only
with its family named. A finite experiment certifies a lower band for that family, at the cost of fresh shadow runs per trial, and
an upper band for the whole class only from coupled runs.

Remark, paired trials. Running the two hypotheses of a trial at one seed leaves the mean of $D$ unchanged and lowers its variance to
at most the discordance, the probability that the two outputs differ. This is common random numbers, and an empirical Bernstein
interval turns it into a trial count of order $(\mathrm{dis}+\epsilon_{\mathrm{acc}})\ln(1/\alpha)/\epsilon^2_{\mathrm{acc}}$, as argon's
review notes. The measured discordance against $2p(1-p)$, its value for independent runs, is the gain a shared seed gives the
measurement.

Without the oracle, or in the other regime. Without the oracle a declared family still has its band from real shadow runs, which is
what LiRA's evaluations report (fact-lira-priced-in-training-runs), with one bank reused, so that what they report is the advantage
conditional on that bank. In the computational regime the family's budget is its shadow work, and part (a) does not apply, since a
bounded adversary cannot hard-wire an unbounded table.

## thm-exact-twin-price: certifying leakage at a zero-leakage function costs exact twin runs

status: sketch
uses: thm-dataflow-composition, lem-needle-lower-bound, thm-coupling-free-soundness, def-seed-access-modes

Setting. As in thm-dataflow-composition (e)(ii), one release $y=W+Z$ with $Z\sim\mathcal N(0,\sigma^2I_d)$, a fixed choice $c$,
$\mathcal M=\mathbb R^d$ and $x_b=x(c,D^b_j)$, with $x_0\neq x_1$. Two kinds of target are considered, the coupled tail
$\theta_{\mathrm{ex}}=\epsilon_0(\Delta)$ for a fixed $\Delta>0$, and the leakage of the release, $\theta_{\mathrm{rel}}=\mathrm{TV}(P_0,P_1)$ or
$\theta_{\mathrm{rel}}=\mathrm H_{e^\varepsilon}(P_1\|P_0)$ for a fixed $\varepsilon\ge0$. Let $\mathsf L^\circ$ have deterministic kernels and
$\mathsf L^\circ(x_0;\rho)=\mathsf L^\circ(x_1;\rho)$ for every $\rho$, so both targets vanish there. Fix $\epsilon_{\mathrm{acc}}\in(0,1)$,
$\alpha>0$ and $\alpha'\ge0$ with $\alpha+\alpha'<1$. A certifier is *accurate at $\mathsf L^\circ$* when
$\Pr_{\mathsf L^\circ}[\hat t\le\epsilon_{\mathrm{acc}}]\ge1-\alpha'$. Let $N_b$ count its Train calls at $x_b$, and
$c_{\mathrm{acc}}=-\ln(1-\epsilon_{\mathrm{acc}})$.

Statement. (a) One pair. Every certifier of either target, in either mode and passing seeds by value or not, sound at level $\alpha$
over every learning function with deterministic kernels and accurate at $\mathsf L^\circ$, satisfies
$\mathbb E_{\mathsf L^\circ}[N_1]\ge(1-\alpha')\ln((1-\alpha')/\alpha)/c_{\mathrm{acc}}$ and the same for $N_0$. Calls at every other training input,
which include fine-tunes from a trained model, warm starts and approximate-unlearning steps, do not enter the bound. For
$\theta_{\mathrm{ex}}$ some certifier sound over every learning function is accurate at $\mathsf L^\circ$ with
$\mathbb E[N_0]=\mathbb E[N_1]=(1-\alpha')\lceil\ln((1-\alpha')/\alpha)/c_{\mathrm{acc}}\rceil$. For $\theta_{\mathrm{rel}}$ the same holds with
$\epsilon_{\mathrm{acc}}$ replaced by $\epsilon_{\mathrm{acc}}-\eta$ in $c_{\mathrm{acc}}$, for every $\eta\in(0,\epsilon_{\mathrm{acc}})$.

(b) Every record. Let $D$ hold $n_D$ distinct records $z_1,\dots,z_{n_D}$ and let $D'\mapsto x(c,D')$ be injective on
$\{D\}\cup\{D\setminus\{z_i\}\}_i$. Put $x^{(0)}=x(c,D)$ and $x^{(i)}=x(c,D\setminus\{z_i\})$, take as target the maximum over $i$ of the
target of record $i$, and let $\mathsf L^\circ$ return one model at all $n_D+1$ inputs for each seed. Under the hypotheses of (a), the
calls at $x^{(1)},\dots,x^{(n_D)}$ together have expectation at least $n_D(1-\alpha')\ln((1-\alpha')/\alpha)/c_{\mathrm{acc}}$, and those at
$x^{(0)}$ at least $(1-\alpha')\ln((1-\alpha')/\alpha)/c_{\mathrm{acc}}$. For $\theta_{\mathrm{ex}}$, $N=\lceil\ln(1/\alpha)/c_{\mathrm{acc}}\rceil$
common seeds, one base run and $n_D$ twin runs at each, give a certificate sound at level $\alpha$ and accurate at $\mathsf L^\circ$ with
$\alpha'=0$, at $N(n_D+1)$ calls.

Proof of (a), target $\theta_{\mathrm{ex}}$. The construction is argon's. Identify $(\mathcal R,\mu)$ with $[0,1)$ and Lebesgue measure by (F9).
Fix $p\in(\epsilon_{\mathrm{acc}},1)$, an integer $M$ with $m=\lceil pM\rceil<M$, the cells $I_r=[(r-1)/M,r/M)$, and a unit vector
$\mathbf e$. For an $m$-subset $B$ of $\{1,\dots,M\}$ let $S_B=\bigcup_{r\in B}I_r$ and let $\mathsf L_B$ agree with $\mathsf L^\circ$ except that
$\mathsf L_B(x_1;\rho)=\mathsf L^\circ(x_1;\rho)+2\Delta\mathbf e\,\mathbf 1[\rho\in S_B]$. It has deterministic kernels, and the twin of $x_0$ at
seed $\rho$ differs from the node's model by $2\Delta\mathbf 1[\rho\in S_B]$, so $\theta_{\mathrm{ex}}(\mathsf L_B)=m/M\ge p>\epsilon_{\mathrm{acc}}$.

Couple the certifier's runs against $\mathsf L^\circ$ and $\mathsf L_B$ with common coins and a common triple per call, as in the proof of
lem-needle-lower-bound. A call at an input other than $x_1$, a call at $x_1$ whose seed lies outside $S_B$, and every Eval and Open call
on what these return get the same answer in both runs. A seed is drawn, named or passed by value, and in each case it is a function of
the history and of fresh draws, and the run against $\mathsf L^\circ$ does not depend on $B$. So the runs agree, and output the same
$\hat t$, unless one of the at most $N_1$ cells that the seeds of the $\mathsf L^\circ$ run's calls at $x_1$ visit lies in $B$. Let
$E=\{\hat t\le\epsilon_{\mathrm{acc}}\}$ in the $\mathsf L^\circ$ run, with probability $q\ge1-\alpha'$. Soundness at $\mathsf L_B$ and
$\epsilon_{\mathrm{acc}}<m/M$ give $\Pr_{\mathsf L_B}[\hat t<m/M]\le\alpha$. For $B$ uniform, averaging gives
$$\alpha\ge\mathbb E_{\mathsf L^\circ}\Big[\mathbf 1_E\,\mathbf 1[N_1<M-m]\prod_{j=0}^{N_1-1}\Big(1-\frac m{M-j}\Big)\Big],$$
since the probability that $B$ avoids $K\le N_1$ given cells is $\binom{M-K}m/\binom Mm$, at least the product. If
$\mathbb E_{\mathsf L^\circ}[N_1]=\infty$ there is nothing to prove, so $N_1<\infty$ almost surely. The law of the $\mathsf L^\circ$ run does not
depend on $M$, so dominated convergence as $M\to\infty$, with $m/M\to p$, gives $\mathbb E[\mathbf 1_E(1-p)^{N_1}]\le\alpha$. Jensen's
inequality for the convex map $u\mapsto(1-p)^u$ under the law given $E$ gives $(1-p)^{\mathbb E[N_1\mid E]}\le\alpha/q$, so
$\mathbb E[N_1]\ge q\ln(q/\alpha)/(-\ln(1-p))$. The map $q\mapsto q\ln(q/\alpha)$ increases on $q>\alpha/e$, and $q\ge1-\alpha'>\alpha$, so
$\mathbb E[N_1]\ge(1-\alpha')\ln((1-\alpha')/\alpha)/(-\ln(1-p))$. Letting $p\downarrow\epsilon_{\mathrm{acc}}$ gives the bound. Perturbing $x_0$ instead
of $x_1$ gives the bound for $N_0$.

Proof of (a), target $\theta_{\mathrm{rel}}$. Use the same family with the shift $2\Delta\mathbf e$ replaced by $s\mathbf e$. Let $Q_B$ be the law of
$\mathsf L^\circ(x_0;\rho)+Z$ given $\rho\in S_B$. The laws $P_0$ and $P_1$ agree off the seeds in $S_B$, so
$\mathrm{TV}(P_0,P_1)=\mu(S_B)\,\mathrm{TV}(Q_B,Q_B(\cdot-s\mathbf e))$, and the last factor tends to one as $s\to\infty$ for each $B$. For
$\mathrm H_{e^\varepsilon}(P_1\|P_0)$, the event $\{y:\langle y,\mathbf e\rangle>s/2\}$ has $P_1$-probability tending to $\mu(S_B)$ and
$P_0$-probability tending to zero. There are finitely many $B$ for each $M$, so some $s_M$ makes $\theta_{\mathrm{rel}}(\mathsf L_B)>\epsilon_{\mathrm{acc}}$ for
all of them once $p$ is fixed above $\epsilon_{\mathrm{acc}}$ with margin, say $\theta_{\mathrm{rel}}\ge(1+\epsilon_{\mathrm{acc}}/p)\,m/(2M)$. The rest of the
proof is unchanged.

Proof of the upper bounds in (a). Target $\theta_{\mathrm{ex}}$. With probability $\alpha'$ output one at no call. Otherwise run the certificate of
thm-dataflow-composition (c) at level $\alpha/(1-\alpha')$ with $n=\lceil\ln((1-\alpha')/\alpha)/c_{\mathrm{acc}}\rceil$ coupled pairs. It fails to
cover with probability at most $(1-\alpha')\cdot\alpha/(1-\alpha')=\alpha$, since an output of one always covers. At $\mathsf L^\circ$ every pair
coincides, no run exceeds $\Delta$, and the bound $1-(\alpha/(1-\alpha'))^{1/n}$ is at most $\epsilon_{\mathrm{acc}}$ by the choice of $n$. Target
$\theta_{\mathrm{rel}}$. thm-dataflow-composition (b) with $R=1$ gives $\mathrm H_{e^\varepsilon}(P_1\|P_0)\le\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)+\epsilon_1(\Delta)$
and $\mathrm{TV}(P_0,P_1)\le\delta_{\mathcal N}(0;\Delta/\sigma)+\epsilon_0(\Delta)$. Choose $\Delta$ with $\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)\le\eta$, which exists
since $\delta_{\mathcal N}(\varepsilon;r)\to0$ as $r\to0$, and certify the exceedance term as above at accuracy $\epsilon_{\mathrm{acc}}-\eta$ (proven).

Proof of (b). Use the family $\mathsf L_{k,B}$ that perturbs only $x^{(k)}$ on $S_B$, with $k$ uniform on $\{1,\dots,n_D\}$ and independent of $B$.
Its target is that of record $k$, at least $m/M$ for $\theta_{\mathrm{ex}}$. With $N^{(k)}$ the calls at $x^{(k)}$ in the $\mathsf L^\circ$ run, the argument
of (a) gives $\alpha\ge\mathbb E[\mathbf 1_E\frac1{n_D}\sum_k(1-p)^{N^{(k)}}]\ge\mathbb E[\mathbf 1_E(1-p)^{N_{\mathrm{tw}}/n_D}]$ in the limit, by convexity of
$u\mapsto(1-p)^u$, with $N_{\mathrm{tw}}=\sum_kN^{(k)}$, and the rest of (a) gives the first bound. Perturbing $x^{(0)}$ moves every record's pair at
once and gives the bound at $x^{(0)}$. For the upper bound, let $\bar p_k$ be the level-$\alpha$ Clopper and Pearson bound for record $k$ from the
$N$ common seeds and output $\max_k\bar p_k$. For a fixed $k^\star$ attaining the maximal target,
$\Pr[\max_k\bar p_k<\theta]\le\Pr[\bar p_{k^\star}<\epsilon^{(k^\star)}_0(\Delta)]\le\alpha$, and each record's indicators are independent across seeds.
At $\mathsf L^\circ$ no pair exceeds, and the output is $1-\alpha^{1/N}\le\epsilon_{\mathrm{acc}}$ (proven, the certificate without a union bound is
argon's).

Label. Proven, (a) and (b), for both targets in (a) and for $\theta_{\mathrm{ex}}$ in the upper bound of (b).

Numbers. At $\alpha=\alpha'=10^{-3}$ and $\epsilon_{\mathrm{acc}}=10^{-2}$, (a) gives at least 686.5 expected calls at each of $x_0$ and $x_1$, and 688
pairs suffice. For 60,000 distinct records, (b) gives at least $4.12\times10^7$ expected twin calls, and
$688\times60{,}001\approx4.13\times10^7$ calls suffice (computed). Each count multiplies the cost of one run, by the remark of
def-seed-access-modes. thm-record-level-certificate certifies the fraction of records whose tail exceeds a threshold at a cost free of $n_D$, so
the price of the every-record certificate is the price of its worst-case target.

Realization (heuristic). With the seed fixed, a Train call is one run of the pipeline. For $\theta_{\mathrm{rel}}$, thm-coupling-free-soundness makes the
certificate sound under any coupling with the right marginals, so realization needs each run to have the deployed law at its input and
repetitions to be independent, which on GPUs is the fidelity assumption of def-learning-oracle. Accuracy at a zero-leakage function needs the
pairs to coincide, which needs deterministic kernels. For $\theta_{\mathrm{ex}}$ the certificate needs the identity coupling itself.
fact-controlled-nondeterminism-exact-replication realizes deterministic kernels on one GPU type, and across types at 1.2 to 1.7 times the
training time, and fact-rerun-reproduction-error shows that whole uncontrolled GPU reruns do not coincide.

Remark, scope. The bound holds because soundness ranges over every learning function, so the model at $x_1$ is unlinked from the model at any
surrogate input. A class restricted by a known stability bound on $\|\mathsf L(x_1;\rho)-\mathsf L(x';\rho)\|$ for a surrogate $x'$ would let surrogate
calls count (argon). XD23 certifies a different target, a mutual-information bound averaged over a data law, from drawn runs of the mechanism, and
this theorem says nothing about it.

Without the oracle, or in the other regime. Without named seeds, thm-dataflow-composition (e) prices the twin certificate above the coupled one in
the drawn mode. With the oracle, (a) says the oracle supplies no twin for free. Each twin is one call, a surrogate is a call at another input and
counts for nothing, and what the oracle supplies is the named seed, which real training also offers. The statement is statistical. By the remark
of def-seed-access-modes it becomes a bound in oracle cost, and a bound in compute under the no-skipping hypothesis.
