# Round 00, oracle and measurement, builder

Date 2026-10-25. This is the literature round of the space. It states what the two
repositories and the library prove on the space's question, names the gaps, and proposes
three aims. No challenge is open, since no earlier round exists.

Symbols follow `sink/2026-10-16-formal-tuning/final/learning-oracle-theory.md`, cited below as
the oracle theory. In particular $\mathsf L$ is the learning function, $\rho\sim\mu$ the seed,
$\xi\sim\pi$ the hardware randomness, $\Pi_x$ the law of the model at training input $x$,
$P_0,P_1$ the view laws, $\epsilon_b(\Delta)$ the exceedance probability, $\alpha$ the error
probability of a certifier and $\epsilon_{\mathrm{acc}}$ its accuracy. A *run* is one execution of
a training pipeline at one training input, and one Train call of the oracle is one run.

Search gate. Before reading, `sink/formalizing/searches.md` and `facts.md` were grepped for
auditing, training runs, seeds, couplings, reruns, nondeterminism and profiles. The rows
`search-coupling-certificate-novelty` and `search-record-level-certificate-prior` record that the
auditing literature was not read. This round reads the auditing, proof-of-learning and
unlearning papers that the library holds. No web search was run. The rows are in `summary.md`.

## What the repositories hold

The oracle theory (HE-ML, accepted 2026-10-17) counts Train calls and proves the following about
measurement. thm-coupling-certificate (b) certifies $\mathrm H_\gamma(P_0\|P_1)$ for every learning
function from $2n$ coupled calls, and (a)(iii) with lem-atomless-two-point shows that drawn seeds
certify nothing below one through a deterministic channel with atomless view laws.
thm-dataflow-composition (c) certifies $\epsilon_0(\Delta)$ with $\lceil\ln(1/\alpha)/\epsilon_{\mathrm{acc}}\rceil$
coupled runs at a function where no run exceeds $\Delta$, and (e) shows that drawn seeds pay a number of
calls exponential in $\min\{d,B^2/\sigma^2\}$. lem-needle-lower-bound bounds every certifier by
$\alpha+N/J$. thm-black-box-certifiability (a) certifies label-only leakage from both sides with drawn
seeds. thm-replay-audit-steer bounds steering under replay at a random-oracle seed by the reach
$p_\tau(T)$. thm-record-level-certificate certifies the fraction of records that leak, at a cost free of
the dataset size. No result of the theory states what a call costs in real training, and no result
gives a lower bound that matches the coupled certificate's $\lceil\ln(1/\alpha)/\epsilon_{\mathrm{acc}}\rceil$.

FORMAL_SECURITY holds two oracles, located through `sink/formalizing/results.md`.

1. def-passive-learning-oracle, `FS:exp/survey/paper/parked/formalization/oracle.tex`, Definition
   "Passive learning oracle" (label `def:passive`) with Definition "Metered cost" (label `def:cost`). On a
   corpus it draws fresh coins, runs a recipe that the game names and returns the trace. Two calls on one
   corpus return independent traces. Parties do not author recipes. The meter is the work of the recipe on
   the corpus. The text after `def:cost` blocks wrapping recipes and laundering initializations, and the
   section on the oracle states that the oracle "manufactures no hardness".
2. def-generic-training-oracle, `FS:exp/survey/lib/reports/src/2026-10-13-halil-ai-oracle-definition.tex`,
   section "The oracle". It keeps handles to parameter vectors and offers train, eval, the input gradient,
   the parameter gradient and reveal. Train returns a fresh handle and is "never opened".

FORMAL_SECURITY also proposes the security profile, the curve from a budget $b$ to the success
$\epsilon(b)$, as "the measurable object" (`FS:exp/docs/CONTEXT.md`, terminology ledger, status
proposed), recorded as def-security-profile-curve with status open. No file in either repository states
an estimator or a certificate for it.

## Literature

Each fact below was read in the PDF of `lib/literature/pdfs/<venue>/`, and its note was filled in this
session.

### fact-lira-priced-in-training-runs: LiRA prices membership inference in shared shadow runs

status: borrowed
uses: none

CCNSTT22 (Carlini, Chien, Nasr, Song, Terzis and Tramèr, IEEE S&P 2022). The online attack of
Algorithm 1 trains $N$ shadow models on random halves of the data distribution's sample, fits two
Gaussians to the target's logit-scaled confidence under the IN and OUT models, and applies a likelihood
ratio test (Section IV-C). The same $N$ shadow models serve every target, since each target lies in $N/2$
of the shadow training sets (Section IV-C, paragraph "Our complete online attack"). The evaluation uses
$N=256$, and $N=64$ for ImageNet (Section V-A and the caption of Fig. 5). At false-positive rate 0.1%, the
true-positive rate gains little beyond 64 shadow models and falls quickly below that number (Fig. 9,
Section VI-B). The shadow runs are drawn independently, with no shared seed.

Proof. Read in the paper, Sections IV to VI. The section numbers agree with the note that the space
`statistical-limits` wrote from its own reading on the same day.

Other regime. The price is in runs of the trainer's own pipeline, so it is a price in the units of this
theory. The attack is a bottom-oracle attack in the drawn mode. The paper proves nothing, and every
number is empirical on CIFAR-10, CIFAR-100, ImageNet and WikiText-103.

### fact-gdp-audit-observation-count: auditing with the mechanism's trade-off function needs fewer runs

status: borrowed
uses: none

NHSBTJCT23 (Nasr, Hayes, Steinke, Balle, Tramèr, Jagielski, Carlini and Terzis, USENIX Security 2023).
An audit converts Clopper and Pearson upper bounds $\bar\alpha,\bar\beta$ on the false-positive and
false-negative rates of a test into an empirical lower bound on $\varepsilon$, by Eq. (9) for $(\varepsilon,\delta)$-DP
and by $\mu^{\mathrm{lower}}_{\mathrm{emp}}=\Phi^{-1}(1-\bar\alpha)-\Phi^{-1}(\bar\beta)$ for Gaussian DP,
Eq. (12). In the white-box threat model with gradient canaries, the $(\varepsilon,\delta)$ audit approaches the
theoretical $\varepsilon$ only near $10^8$ observations, while the Gaussian-DP audit is tight with $10^3$
(Section 4.1, Fig. 3, 20 runs, $\delta=10^{-5}$). One observation is one step of one run, so the white-box audit
needs two runs, and the end-to-end bound composes per-step bounds by assuming that Gaussian composition is
tight (Section 5.5). In the black-box threat model the audit trains 1,000 models with the canary and 1,000
without (Section 6.4), and reaches about 1.6 against a theoretical 8 on CIFAR-10 with WRN-16 (Fig. 11).

Proof. Read in the paper, Sections 2.3, 4, 5 and 6.

Other regime. The lower bound is sound for the per-step mechanism. The end-to-end figure is heuristic, since
it assumes tight composition. Everything is a lower bound on leakage, so it lower-bounds a point of a
security profile and never certifies an upper bound.

### fact-audit-independent-batches: the audit draws batches and noise independently across worlds

status: borrowed
uses: none

NHSBTJCT23, Section 5.1. In Algorithm 2 the trainer samples two batches $B$ and $B'$ independently at each
step. The authors report that they "experimented with both configurations", identical and independent
batches, "and did not observe any significant difference", and kept independent batches since that carries
fewer assumptions. Section 6.1 states that in all experiments the initial parameters are equal between runs
while "the random processes use different seeds".

Proof. Read in the paper, Sections 5.1 and 6.1.

Other regime. This is the one place in the library where an audit couples the two worlds. It couples the
batches and the initialization and never the privacy noise. With independent noise in each world, sharing
the batch leaves the per-step observation's two laws unchanged, so no variance reduction is expected
(heuristic). It is empirical, on CIFAR-10.

### fact-small-seed-space-breaks-dp: a noise seed with 100 values is detected by the audit

status: borrowed
uses: none

NHSBTJCT23, Section 6.3, Violation 2. A DP-SGD implementation whose noise seed takes only 100 values, so that
only 100 noise vectors occur, is detected as violating its claimed $\varepsilon=1.27$ by the Gaussian-DP audit
and by the method of Lu et al., and not by $(\varepsilon,\delta)$ audits (Fig. 8). The authors relate it to a
seed reused across parameter sets in a published JAX example.

Proof. Read in the paper, Section 6.3.

Other regime. A finite seed space is a resource for an adversary who can enumerate it. With $2^{n_{\mathrm{bit}}}$
seeds, enumeration realizes the top oracle at $2^{n_{\mathrm{bit}}}$ runs (heuristic, it assumes deterministic
kernels). This is the empirical side of open problem 9 of the oracle theory, on finite seeds.

### fact-one-shot-estimate-consistency: one-run estimation is consistent and is not a bound

status: borrowed
uses: none

AKOOMS24 (Andrew, Kairouz, Oh, Oprea, McMahan and Suriyakumar, ICLR 2024). Algorithm 1 inserts $k$ canary
vectors drawn uniformly from the sphere $S^{d-1}$ into one run of the Gaussian sum mechanism and fits a
Gaussian to the $k$ cosines between canaries and output. Theorem 3.3 assumes $\|X_d\|=o(\sqrt d)$ for the
sum $X_d$ of the real vectors, $k=o(d)$ and $k=\omega(1)$, and proves that the estimate converges in
probability, as $d\to\infty$, to the $\varepsilon$ of $\mathcal N(0,\sigma^2)$ against $\mathcal N(1,\sigma^2)$
at the target $\delta$. For DP-FedAvg (Algorithm 2, Section 4) no theorem is given. The paper also reports a
Clopper and Pearson style lower bound $\varepsilon_{\mathrm{lo}}$ from the same cosines, whose maximum with
1,000 canaries at $\alpha=0.05$ is 6.24 under perfect separation (Section 5, text by Table 4). Section 5.3
states "We still cannot rule out that our method is not overestimating $\varepsilon$".

Proof. Read in the paper, Sections 3 to 5.

Other regime. Theorem 3.3 is proven and asymptotic, with no rate. The FL estimate is empirical. A finite
experiment's certified lower bound has a ceiling set by its number of observations, 6.24 here, so a
certificate of a large leakage needs more observations than any one run provides.

### fact-hsu-membership-sample-gap: sample-based membership inference needs order $n+n^2\rho^2$ samples

status: borrowed
uses: none

HSU25 (Haghifam, Smith and Ullman, FOCS 2026 to appear, arXiv 2508.19458 v2). Definition 2.1 asks a
membership test, given $m$ auxiliary samples, the noisy mean and a candidate, to answer correctly with
probability at least 0.51 on each side. Theorem 3.1 proves that for $d>c_1(n+n^2\rho^2)$ and
$m\le c_2(n+n^2\rho^2)$ no such test exists against the noisy empirical mean of Definition 2.4 over all
Gaussians. Theorem 1.1 is its informal version. Theorem 3.3 is the matching attack with $m\ge cd$ samples for
$d\ge c(n+n^2\rho^2)$. Theorem 4.1, whose informal version is Theorem 1.2, shows that with known covariance
$\min\{n,1/\rho^2\}$ samples are necessary, matching Dwork et al. Section 1.2.1 notes that a test of the
restricted form, a statistic free of the distribution with a calibrated threshold, needs $O(1)$
independent trained models, which is $O(n)$ samples.

Proof. Read in the paper, Sections 1.2, 2 and 3, and the statement of Theorem 4.1. The proofs were not
re-derived.

Other regime. Divided by the training-set size $n$, the price is $1+n\rho^2$ datasets' worth of samples, the
trainer's own unit. The result is statistical and belongs to the space `statistical-limits`. For measurement
it says that an audit with restricted tests can sit far below the profile it lower-bounds, as the paper says
in Section 1.2.1.

### fact-rerun-reproduction-error: a rerun at one seed ends almost as far as an independent model

status: borrowed
uses: none

JYCDTCP21 (Jia, Yaghini, Choquette-Choo, Dullerud, Thudi, Chandrasekaran and Papernot, IEEE S&P 2021).
Theorem 1 (Entropy Growth) states that the entropy of the training process grows linearly in the number of
steps $T$, under the assumption of i.i.d. noise from hardware and low-level libraries at each step
(Section VI-A). Table I (Section VI-C) reports the reproduction error of retraining from a checkpoint with the
same initial parameters, batching, architecture and training strategy, normalized by $d_{\mathrm{ref}}$, the
distance between two models trained independently. For a whole run ($k=E\cdot S$) the normalized
$\ell_2$ error is 0.955 ($\pm0.004$) for ResNet-20 on CIFAR-10 and 0.815 ($\pm0.002$) for ResNet-50 on
CIFAR-100. For one step ($k=1$) it is 0.001 and 0.002. PyTorch's deterministic operations lower the whole-run
error to 0.569 for ResNet-20 and leave it at 0.816 for ResNet-50, at "a large computational cost" and an
accuracy drop above one percentage point.

Proof. Read in the paper, Sections IV to VI and Table I.

Other regime. Theorem 1 is proven inside its noise model, which is heuristic for real hardware. Table I is
empirical. Read in the oracle theory, it measures the spread $\mathrm{sp}_\tau$ of a whole run, close to one for
every $\tau$ below $0.9\,d_{\mathrm{ref}}$ in $\ell_2$, and the spread of one step, near zero.

### fact-pol-bare-cost-inequalities: proof of learning states its cost requirements as desiderata

status: borrowed
uses: none

JYCDTCP21, Section IV. Property 1 requires $\mathbb E[C_V]\le\mathbb E[C_T]$ for the verifier's and the
trainer's cost, and Property 2 requires $\mathbb E[C_T]\le\mathbb E[C_A]$ for any spoofing strategy. Definition 1
defines a proof of learning as the tuple $(W,I,H,A)$ of checkpoints, data indices, data signatures and
auxiliary information. Capability 3 of the threat model denies the adversary the trainer's randomness, "batching,
parameter initialization, chosen random seeds" and hardware randomness. Conjecture 1 (Section VII) is unproved.

Proof. Read in the paper, Sections IV and VII.

Other regime. The secret of the scheme is the trainer's seed, with no random oracle and no commitment.
thm-replay-audit-steer replaces it by a seed that a random oracle derives from a commitment, which gives a
proven bound.

### fact-unlearning-verification-fragile: a prover that picks the batches passes exact replay

status: borrowed
uses: none

ZCSL24 (Zhang, Chen, Shen and Li, ICML 2024). Definition 4.1 calls a proof of retraining valid when every
step is reproducible within $\varepsilon$ and no batch contains unlearned data. Algorithm 1 retrains while
replacing each unlearned point in the original batch by its nearest same-class neighbour in the retained data.
Proposition 4.2 proves that it returns a valid proof at $\varepsilon=0$. Proposition 4.3 bounds the gradient
norm reached on the full dataset under smoothness assumptions. Proposition 4.5 states that Algorithm 1 costs
the time $\mathcal T(n)$ of naive retraining and that the forging Algorithm 2 costs
$(p_u/P+(1-p_u)/(mP))\,\mathcal T(n)$. The text calls these results Theorems 4.2 to 4.5.

Proof. Read in the paper, Sections 3 and 4.

Other regime. The prover's freedom is the batch order, a part of the seed. The attack costs one run, the same
as honest retraining, so a meter in runs does not separate it from honest work.

### fact-unlearning-algorithm-level: forging makes unlearning undefinable from logs of minibatch SGD

status: borrowed
uses: none

TJSP22 (Thudi, Jia, Shumailov and Papernot, USENIX Security 2022). A forging map replaces the data points of a
zero-error log on $D$ by points of $D'$ while keeping each step within $\varepsilon$ (Section 4.1). Theorem 2
(Probabilistic Forging) bounds below the probability that $D'$ forges $D$ for mean-sampler updates with batch
size $b$. Theorem 3 (Existence of Forging Adversary) proves that an adversary free to choose $b$ and to sample
indefinitely forges almost every dataset at every $\varepsilon>0$. Corollary 2 concludes that unlearning over
the logs of minibatch SGD is not well defined.

Proof. Read in the paper, Sections 4 and 5.

Other regime. Forging needs the prover to choose batch size and batches. A replay at a seed derived from a
random oracle and a committed dataset, as in thm-replay-audit-steer, removes that choice.

### fact-balle-known-initialization-reconstruction: a known initialization is what makes reconstruction work

status: borrowed
uses: none

BCH22 (Balle, Cherubin and Hayes, IEEE S&P 2022). In the table of factors of Section VI, the reconstructor
network reaches MSE 0.0089 on MNIST with the default setting and 0.0695 when the adversary does not know the
released model's initial parameters, where the attack fails (row "Random initialization"). Appendix A,
Table III repeats the comparison over learning rates and momenta. Its text says "with and without random
initialization was 0.0089 and 0.0695", which inverts the table, where the random-initialization rows carry MSE
near 0.069 and the others at most 0.0089.

Proof. Read in the paper, Section VI and Appendix A.

Other regime. Empirical, on MNIST and CIFAR-10. Knowing the initialization is a partial top oracle that reveals
part of the seed.

### fact-known-initialization-separates-membership: with a shared initialization the loss laws separate

status: borrowed
uses: none

BCH22, Appendix A, Fig. 11. On MNIST, 1,000 released models are trained with a target point and 1,000 without, in
two settings. When every model has the same initialization, the two laws of the target's loss are "perfectly
separable". When each model draws a new seed, they "nearly perfectly overlap".

Proof. Read in the paper, Appendix A.

Other regime. Empirical. In the oracle theory's terms the figure shows a large top divergence
$\mathrm D^\top_1$ next to a small total variation $\mathrm{TV}(P_0,P_1)$ for a real pipeline, the gap that
thm-coupling-certificate (c)(i) proves possible. The shared object is the initialization only, so the figure
lower-bounds what a full seed would give.

## Gaps

1. The two oracles are not related by any statement. HE-ML names seeds and counts calls. FORMAL_SECURITY draws
   coins, returns traces and meters work. No statement says which accepted result survives under drawn coins, and
   why.
2. No statement prices a Train call in real training or says what real reruns must satisfy for a certificate to
   stay sound. fact-rerun-reproduction-error shows that a whole GPU rerun at one seed lands near
   $0.96\,d_{\mathrm{ref}}$ from the original, so the identity coupling of the theory is far from deterministic on
   real hardware.
3. The security profile has no estimator and no certificate. The auditing papers measure single points from
   below with independent runs (fact-gdp-audit-observation-count, fact-lira-priced-in-training-runs). No paper in
   the library prices a point uniformly over learning functions, or prices the gain from a shared seed in
   measurement. The one coupled design, fact-audit-independent-batches, shares the batch and not the noise.
4. No lower bound matches the coupled certificate's $\lceil\ln(1/\alpha)/\epsilon_{\mathrm{acc}}\rceil$ runs. Cheaper
   surrogates for a twin, such as a fine-tune from the trained model or an influence-function step (ZCSL24,
   Section 2.1), have no status in the theory. Halil's point that every leave-one-out twin costs a run has no
   theorem behind it.
5. The seed as a resource is measured (fact-balle-known-initialization-reconstruction,
   fact-known-initialization-separates-membership, fact-small-seed-space-breaks-dp) and formal only through the top
   oracle. Under hardware randomness the value of a revealed seed to an adversary who reruns has no bound.

## Aims

### def-seed-access-modes: one learning oracle with two seed-access modes

status: open
uses: def-learning-oracle, def-certifier, def-degenerate-oracles, def-passive-learning-oracle, def-generic-training-oracle

Statement. Fix a learning oracle $\mathcal O$ for $(\mathsf L,\mu,\pi)$. A game serves each caller in one of two
*seed-access modes*. In the *named mode* the caller's calls are those of def-learning-oracle. In the *drawn mode*
the oracle accepts $\mathsf{Train}(x,s)$ only with $s=\bot$, returns only the model name, keeps the seed under no
name that the caller holds, and refuses Open on seeds. Grants to a caller in the drawn mode carry model names
only. A *cost meter* is a measurable $\mathsf{cost}:\mathcal X\to[0,\infty)$, the work of one run at $x$ in a fixed
machine model, and a caller's oracle cost is the sum of $\mathsf{cost}$ over its Train calls. The call count is the
meter $\mathsf{cost}\equiv1$.

The proposal for Halil is that both repositories use this one oracle, with the mode fixed per caller by the
game. Round 01 is to prove five claims.

1. Restriction (proof to come). Let $\mathcal M$ be the space of traces, $\Lambda$ the game's named recipes, and
   $\mathsf L(x;\rho,\xi)$ the trace of recipe $\ell$ on $D$ with coins $(\rho,\xi)$, with every starting model
   fixed to the declared initialization rule of $\ell$. A drawn-mode caller that opens its model names then has,
   call by call, the transcript law of a caller of def-passive-learning-oracle, at metered cost $\sum\mathsf{cost}(x)$. With
   $\mathsf{ev}(m,u)$ returning the output, the input gradient or the parameter gradient as $u$ selects, the
   operations of def-generic-training-oracle are drawn-mode Train calls, Eval calls and Open.
2. Soundness needs no names (proof to come). Every certificate of the oracle theory whose target is a quantity
   of the bottom oracle stays sound when the identity coupling of the twins is replaced by any coupling whose two
   marginals, round by round and given the past, are the run laws. This includes independent drawn runs.
   Targets of the top oracle need twins that share the seed.
3. Accuracy needs names. The separations of the oracle theory already show it:
   thm-coupling-certificate (a)(iii), thm-dataflow-composition (e), thm-bounded-deviation-transfer (e) and
   thm-replay-audit-steer (d) (proven there).
4. The seed for an adversary (proof to come). Under the top oracle, with deterministic kernels and a
   deterministic channel $\kappa$, an adversary that opens the honest seed and makes one Train call attains the
   top optimum $\mathrm D^\top_1(\kappa)$. Under hardware randomness, the attack that reruns at the revealed seed and
   accepts within tolerance $\tau$ has advantage
   $\Pr_\Gamma[\mathrm{dist}(\kappa(W^\Gamma_0),\kappa(W^\Gamma_1))>\tau]-\mathrm{sp}_\tau(x_1)$, where $\mathrm{sp}_\tau(x_1)$ is the
   spread of thm-replay-audit-steer read on the view at $x_1$.
5. The meter (proof to come). lem-needle-lower-bound with $N$ calls in $\bigcup_kX_k$ gives the compute lower
   bound $N\min_{x\in\bigcup_kX_k}\mathsf{cost}(x)$, and the coupled certificates cost $n(\mathsf{cost}(x_0)+\mathsf{cost}(x_1))$
   for $n$ pairs.

What would settle it. Proofs of claims 1, 2, 4 and 5, and Halil's decision among three options. Keep both modes in
one oracle, the proposal. Adopt drawn coins only, which keeps every soundness statement by claim 2 and loses
claim 3, the top-oracle threat model and the replay audit. Adopt named seeds only, which needs the declared
initializations of claim 1 whenever the meter is work.

Regime. Both. Claims 2 to 4 are statistical. Claim 5 carries the price into the work of a stated machine model.

Measurement. Claims 1 to 3 need no experiment. Claim 4 is measured by coupled reruns with and without
deterministic kernels, which estimate the coupled tail and the spread. fact-rerun-reproduction-error gives the
spread of a whole run as close to one and the spread of one step as near zero.

Without the oracle. Claim 1 is FORMAL_SECURITY's own setting, where every lower bound comes from what the views
withhold. Claim 2 then says that the drawn coins of FORMAL_SECURITY lose no soundness in the bottom world and lose
the accuracy that the separations measure. In the computational regime the meter is FORMAL_SECURITY's metered
cost, and the no-skipping hypothesis decides whether a price in work transfers to real training.

### conj-paired-advantage-price: the price of one point of the security profile, with and without shared seeds

status: open
uses: def-security-profile-curve, def-certifier, thm-coupling-certificate, lem-atomless-two-point

Statement. Fix one learning node with inputs $x_0\neq x_1$ and a channel $K$ given by $K(\cdot\mid m)$, the law of
$\kappa(m,\mathfrak u)$ for a measurable $\kappa$ and channel noise $\mathfrak u$ of a known law that the experimenter samples. Fix a test $t:\mathcal V\to\{0,1\}$ in advance, an attack whose own
shadow runs are already spent. Let $\mathrm{Adv}(t)=\Pr[t(Y_1)=1]-\Pr[t(Y_0)=1]$, and let the *discordance* be
$\mathrm{dis}_t=\Pr[t(\kappa(W^\Gamma_0,\mathfrak u))\neq t(\kappa(W^\Gamma_1,\mathfrak u))]$ under the identity coupling with common
channel noise.

(a) Named mode. From $n$ coupled pairs, at $2n$ Train calls, some two-sided interval for $\mathrm{Adv}(t)$, sound at
level $\alpha$ over every learning function, has half-width at most
$C_1\sqrt{\mathrm{dis}_t\ln(4/\alpha)/n}+C_2\ln(4/\alpha)/n$ with probability at least $1-\alpha$, for universal
constants $C_1,C_2$.

(b) Drawn mode. Some class of learning functions contains a reference function with $\mathrm{dis}_t=0$, at which
every drawn-mode estimator that is within $\epsilon_{\mathrm{acc}}$ of $\mathrm{Adv}(t)$ with probability at least
$1-\alpha$ over the class makes $\Omega(\ln(1/\alpha)/\epsilon_{\mathrm{acc}}^2)$ Train calls. The named mode needs
$O(\ln(1/\alpha)/\epsilon_{\mathrm{acc}})$ there.

(c) The certified band. For attacks $t_1,\dots,t_k$ fixed in advance at budgets $b_1\le\dots\le b_k$, with lower
confidence bounds $\underline\ell_i$ at level $\alpha/k$, the step function $b\mapsto\max\{\underline\ell_i:b_i\le b\}$
lies below the profile $\epsilon(b)$ at every $b$ with probability at least $1-\alpha$, at a cost of
$\sum_i2n_i$ runs plus the attacks' shadow runs. Through a deterministic channel with atomless view laws, no
drawn-mode certificate gives an upper band below one at any budget, and the coupled certificate of
thm-coupling-certificate (b) gives the upper band $\beta_1(K)$, constant in $b$.

What would settle it. Proofs of (a) to (c) with explicit constants, and a measurement of $\mathrm{dis}_t$ for a
real attack.

Regime. Statistical. The experimenter is unbounded and the count is of runs.

Measurement. For LiRA's test at a target record, train coupled pairs on $D$ and $D\setminus\{z\}$ at one seed on
MNIST and CIFAR-10. Measure $\mathrm{dis}_t$ in three pipelines, full training with nondeterministic kernels, full
training with deterministic kernels, and one round of federated local training. Compare it with
$2p(1-p)$, the discordance of independent runs, where $p$ is the acceptance rate. fact-rerun-reproduction-error
predicts a discordance near the independent value for the first pipeline and a small one for the third
(heuristic).

Without the oracle. A drawn-mode experimenter is what the auditing literature uses, with 1,000 runs per world
(fact-gdp-audit-observation-count). Part (b) prices that choice at a factor of order $1/\epsilon_{\mathrm{acc}}$ where
coupled pairs agree. In the computational regime, the profile's budget includes the attack's shadow runs, and
fact-lira-priced-in-training-runs shows how one bank of shadow runs serves every target.

### conj-exact-twin-price: realizing a coupled certificate costs exact twin runs that no surrogate replaces

status: open
uses: thm-dataflow-composition, lem-needle-lower-bound, thm-record-level-certificate, def-seed-access-modes

Statement. Work in the setting of thm-dataflow-composition (e)(ii), one release with a fixed choice,
$f_1(c,m)=m$ on $\mathcal M=\mathbb R^d$ and $x_b=x(c,D^b_j)$, with target $\epsilon_0(\Delta)$. Let
$\mathsf L^\circ$ satisfy $\mathsf L^\circ(x_0;\rho)=\mathsf L^\circ(x_1;\rho)$, so that $\epsilon_0(\Delta)=0$ there.

(a) One pair. Let a certifier, in either mode, be sound at level $\alpha$ over every learning function with
deterministic kernels, and output below $\epsilon_{\mathrm{acc}}$ at $\mathsf L^\circ$ with probability at least
$1-\alpha'$, where $\alpha+\alpha'<1$. Then its expected number of Train calls at $x_1$ under $\mathsf L^\circ$ is at
least $\ln(1/(\alpha+\alpha'))/(-\ln(1-\epsilon_{\mathrm{acc}}))$. Calls at every other training input count for
nothing in this bound. Such calls include a fine-tune from the trained model, a warm start and an
approximate-unlearning step. The certificate of thm-dataflow-composition (c) meets the bound with
$\lceil\ln(1/\alpha)/(-\ln(1-\epsilon_{\mathrm{acc}}))\rceil$ coupled pairs.

(b) Every record. Let $D$ hold $n_D$ records, $x^{(i)}=x(c,D\setminus\{z_i\})$, and the target be
$\max_i\epsilon^{(i)}_0(\Delta)$. Under the hypotheses of (a), the expected total number of calls at the inputs
$x^{(i)}$ is at least $n_D\ln(1/(\alpha+\alpha'))/(-\ln(1-\epsilon_{\mathrm{acc}}))$, and
$n_D\lceil\ln(n_D/\alpha)/(-\ln(1-\epsilon_{\mathrm{acc}}))\rceil$ coupled pairs suffice.

(c) Realization (heuristic). With the seed fixed, a Train call is one run of the pipeline at cost $\mathsf{cost}(x)$. By claim 2
of def-seed-access-modes, the bottom-oracle certificates stay sound under two conditions. Each run has the law of
the deployed run at its input, and repetitions are independent. The shared seed matters for accuracy only.

At $\alpha=\alpha'=10^{-3}$ and $\epsilon_{\mathrm{acc}}=10^{-2}$, (a) gives at least 619 calls at $x_1$ against
688 pairs that suffice. For MNIST's 60,000 records, (b) gives at least $3.71\times10^7$ twin calls against
$1.07\times10^8$ pairs that suffice (computed). thm-record-level-certificate certifies the fraction of leaking
records at a cost free of $n_D$, so the price of Halil's every-twin certificate is the price of the worst-case
target.

What would settle it. Proofs of (a) and (b). Part (c) stays heuristic, since the law of a GPU run is not known to
satisfy the fidelity of def-learning-oracle.

Regime. Statistical, in calls. The work is $\mathsf{cost}(x)$ per call, so the compute price is the call count times the cost
of one run.

Measurement. Time one MNIST run with and without deterministic kernels, multiply by the counts of (a) and (b), and
compare with the cost of thm-record-level-certificate at the same $\alpha$ and accuracy.

Without the oracle. Without named seeds, thm-dataflow-composition (e) already prices the twin certificate above
the coupled one. With the oracle, (a) says the oracle supplies no twin for free, since each twin is one call.
What the oracle supplies is the named seed, which real training also supplies, and the identity coupling, which
GPU training supplies only approximately (fact-rerun-reproduction-error). The lower bounds are statements about
experimenters and hold in the statistical regime. Their transfer to compute is claim 5 of def-seed-access-modes.
