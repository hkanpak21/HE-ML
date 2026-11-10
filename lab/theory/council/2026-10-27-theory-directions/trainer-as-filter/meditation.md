# The trainer as filter and the price of memorization

## The question

The attacker sees a function of the trainer's output, so a restriction on the trainer may bound every attacker of it. Item 21 (`prop-learner-side-sq-transfer`) proves this for a trainer that reads fresh records through one-bit statistical queries. The question is which restriction still filters when the trainer memorizes, which quantity prices memorization once a record is split into a population part and a random-oracle individual part, what a canary's exposure measures, and whether the frame says more than the data-processing inequality and the SQ simulation of SGD.

## Meditation

Records $z_1,\dots,z_n$ are i.i.d. from a law $D$ on a standard Borel space $\mathcal Z$. $S=(z_i)_{i\le n}$ is the training set, $M$ the trainer's output, and $V$ any randomized function of $M$, the attacker's view. A population secret is tested as a null law $D_0$ against a family $D_1,\dots,D_L$, with $D$ uniform on the family. Write $\chi(D_l,D_m)=\mathbb E_{D_0}[(dD_l/dD_0-1)(dD_m/dD_0-1)]$, let $\gamma$ bound $|\chi|$ off the diagonal and $\beta$ on it, and put $\bar\gamma=\gamma+\beta/L$. For every $\phi\in L^2(D_0)$,
$$\frac1L\sum_{l\le L}(D_l\phi-D_0\phi)^2\le\bar\gamma\,\|\phi\|^2_{L^2(D_0)},$$
because with $h_l=dD_l/dD_0-1$ the left side is $L^{-1}\sum_l\langle h_l,\phi\rangle^2$, the operator $\sum_lh_l\langle h_l,\cdot\rangle$ has the nonzero spectrum of the matrix $\chi$, and Gershgorin bounds its top eigenvalue by $\beta+(L-1)\gamma$ (proven). This inequality carries every SQ bound below, and $\bar\gamma$ is their only hardness parameter. Approximate structure can supply small correlations, and no planted problem is needed.

The first finding is negative. No filter theorem can be stated in terms of what the output carries. A trainer that runs a test on its own sample and outputs the verdict has a one-bit output, and an $\varepsilon$-DP release of a low-sensitivity statistic hands a planted parity to the identity attacker from $O(d+1/\varepsilon)$ records at constant error (`prop-output-bounds-do-not-filter`, proven). The slogan "what the trainer did not learn stays hidden" is false as written. What holds is that what the trainer's class cannot compute stays hidden. Every positive filter restricts what the trainer holds while it trains: its access to records (item 21), its state in a single pass, or the information its trajectory carries. For the state, a streaming trainer with fewer than $d^2/20$ bits of state, followed by any reader of its final state, is a branching program that Raz's bound excludes, so no attacker recovers a planted parity from fewer than $2^{\Omega(d)}$ records (proven given `fact-raz-theorem-stronger-than-abstract`).

The positive results here rest on one device. Run the trainer's update with the null law's population gradient in place of the minibatch gradient. This null trajectory depends on the coins alone. The records in the batch of step $t$ are then i.i.d. and independent of the point at which they are evaluated, whatever the schedule of reuse. A transfer from a fixed sample to the population normally fails on adaptivity, and here no adaptivity exists, because the comparison runs along a path the data never touched. The refuted `thm-fs-sq-black-box-reduction` compared along the trainer's own path, which the data did touch.

In the rounding model of AKMSS21, where an adversary chooses each valid rounding, the device gives `thm-null-trajectory-filter`. Its bound contains neither $n$ nor the number of passes, so multi-pass coarse SGD is filtered exactly as single-pass SGD is (proven). Its part (b) is the sharper point. Under the same condition some valid rounding makes the output a function of the coins and $D$ alone, so in this model nothing about the sample leaks (proven). The bridge `fact-sq-simulates-minibatch-sgd` therefore covers SGD only in a model in which memorization cannot be stated. Halil's objection to it is correct, and the variable that matters is the quantifier over roundings.

An honest trainer meets one rounding. Gaussian noise $\mathcal N(0,\sigma^2I_p)$ added at each step is an honest model in which the device still works, and it gives `thm-noisy-trainer-two-term-filter`. The squared advantage of every white-box attacker is at most a population term $TC^2\bar\gamma/\sigma^2$ plus half of $\mathcal I=2TC^2/(b\sigma^2)$, where $T$ is the step count, $C$ the clipping norm, $b$ the batch size, and $\mathcal I$ bounds the information of the whole trajectory about $S$ (proven). The first term is the SQ price. The second is the trajectory's memorization budget, and it does not involve the secret. The second term cannot be dropped. One step of noisy full-batch gradient descent into a hashed table stores all $2d$ records and hands a planted parity to the attacker at $\mathcal I=\Theta(d^2\log d)$, while the population term is $2^{-\Omega(d)}$ (`prop-hashed-memory-breaks-sq-filter`, proven). The bound is vacuous from $\mathcal I=2$ on, so for parity the threshold lies between $2$ and $\Theta(d^2\log d)$, which is the gap of Next.

For the individual part the quantity is $\mathrm{mem}_i=I(r_i;M\mid u_i)$, with $u_i$ the population part of record $i$ and $r_i$ its random-oracle part. The split needs no modelling assumption. The noise-outsourcing lemma writes every record law as $g(u,r)$ with $r$ uniform and independent of $u$, for any chosen statistic $u=s(z)$, and $\mathrm{mem}_i=I(z_i;M\mid u_i)$ for every such $g$ (`def-random-oracle-record-split`, proven). The statistic is the only choice. In supervised learning the Bayes posterior of the label is canonical. In self-supervised learning every coordinate is a label, no statistic is canonical, and the designer chooses one, which is what a canary does. When the trainer can compute $s$, zero memorization of the individual part costs no accuracy (proven, by resampling). When it cannot, accurate learners can be forced to memorize, by the result of Brown, Bun, Feldman, Smith and Talwar (from memory, unverified).

A canary is a programmed record. The designer sets $H(c)$ to a value it draws uniformly and records, and the joint law of everything is unchanged (`prop-canary-is-programmed-record`, proven). Its exposure is the attacker's list-decoding profile on the individual part. Measured exposure gives a lower band on $\mathrm{mem}_c$, from one run in expectation, and an upper band needs runs at one seed with two canary values, which is the coupling certificate (`lem-exposure-information-sandwich`, proven). As in items 1 and 9, fresh runs give lower bands only, and upper bands need twins, at about the price of `thm-exact-twin-price` per canary (heuristic, the twin there differs by a record and here by a value).

Every statement above binds unbounded white-box attackers, because the restriction sits on the trainer. Beyond item 21 the frame gives multi-pass robust SGD, honest noisy SGD with its memorization term, and bounds on the individual part. An attacker that also holds $m$ fresh records gains, under the null rounding, exactly what those records give alone (proven, the output is then a function of the coins). The frame stops in two places. It says nothing about honest trainers with $\mathcal I\gg1$, which is real training, where only $\mathrm{mem}_i$ can be measured. It says nothing about the split-learning server of items 12 to 18, which sees per-record messages and so does not read a trainer's output.

## Claims

### def-random-oracle-record-split: the random-oracle split of a record
status: proven
uses: none

Let $s:\mathcal Z\to\mathcal U$ be a measurable statistic, the population part. A random-oracle split of $D$ along $s$ is a measurable $g:\mathcal U\times[0,1]\to\mathcal Z$ such that, for $u\sim s_\#D$ and $r\sim\mathrm{Unif}[0,1]$ independent, $g(u,r)\sim D$ and $s(g(u,r))=u$ almost surely. Record $i$ is $z_i=g(u_i,r_i)$ with $r_i=H(i)$ for a random oracle $H$. The memorization of record $i$ by a trainer with output $M$ is $\mathrm{mem}_i=I(r_i;M\mid u_i)$. Three claims follow.

(a) A split exists for every $D$ and $s$.
(b) $\mathrm{mem}_i=I(z_i;M\mid u_i)$ for every split, so it depends on $D$, $s$ and the trainer only.
(c) If the trainer can compute $s$ and sample the law of a record given its population part, every trainer $T$ has a trainer $T'$ with the same output law, hence the same risk, and $\mathrm{mem}_i(T')=0$ for every $i$.

Proof. (a) For $\mathcal Z=\mathbb R$ take $g(u,\cdot)$ the quantile function of the law of $z$ given $s(z)=u$. For $\mathbb R^d$ chain conditional quantiles coordinate by coordinate. A standard Borel space is Borel isomorphic to a Borel subset of $\mathbb R$. This is the noise-outsourcing lemma (Kallenberg, from memory). (b) The trainer reads $r_i$ only through $z_i$, so $I(r_i;M\mid u_i)\le I(z_i;M\mid u_i)$, and $z_i$ is a function of $(u_i,r_i)$, which gives the reverse inequality. (c) Put $T'(S)=T\big((g(u_i,r'_i))_i\big)$ with fresh independent $r'_i$. The family $(u_i,r'_i)_i$ has the law of $(u_i,r_i)_i$, so $T'(S)$ has the law of $T(S)$. $T'(S)$ is a function of $(u_i)_i$ and of randomness independent of $(r_i)_i$, so $I(r_i;T'(S)\mid u_i)=0$. $\square$

### prop-canary-is-programmed-record: a canary is an admissible programming
status: proven
uses: def-random-oracle-record-split, prop-best-advantage-equals-total-variation

Let individual parts be uniform on a finite set $R$ with $|R|=N$. A canary at index $c$ is the designer's programming $H(c):=\kappa$, with $\kappa$ drawn uniformly from $R$ and recorded, and optionally $u_c$ drawn from $s_\#D$ and recorded. (a) The joint law of the training set, the seeds and every party's view equals the honest one. Every bound proven for the honest procedure therefore holds with the canary in place, and the designer knows $\kappa$. (b) If the programmed record has another law given some party's view, that party tells the programmed procedure from the honest one with advantage equal to the total variation between its two view laws, so the canary is not admissible. (c) For a ranking $\pi_V$ of $R$ computed from $V$, the exposure is $X=\ln N-\ln\pi_V(\kappa)$, and $\Pr[X\ge\ln(N/k)]$ is the probability that $\kappa$ lies in the list $L_k(V)$ of the first $k$ candidates.

Proof. (a) Programming a random oracle at a point with a fresh uniform value leaves its law unchanged. This is lazy sampling. (b) is `prop-best-advantage-equals-total-variation`. (c) $\pi_V(\kappa)\le k$ exactly when $\kappa\in L_k(V)$. $\square$

A canary added as an extra record changes $n$, so it is admissible only if it replaces an honest index or $n$ is random and unobserved. The canary clients of AKOOMS24 (Section 4) return one fixed random unit vector at every participation, which a server tells apart from honest updates (heuristic, it assumes honest updates vary across rounds), so their exposure measures a record outside the honest law. Under Halil's rule a canary measures the memorization of a typical record.

### lem-exposure-information-sandwich: exposure is sandwiched by memorization and the coupled tail
status: proven
uses: prop-canary-is-programmed-record, thm-coupling-certificate

Let $\kappa$ be uniform on $R$, $|R|=N$, $p_k=\Pr[\kappa\in L_k(V)]$, $\mathrm{kl}(p\|q)=p\ln\frac pq+(1-p)\ln\frac{1-p}{1-q}$, and $H_N=\sum_{j\le N}1/j\le1+\ln N$. Then:

(a) $\mathrm{kl}(p_k\|k/N)\le I(\kappa;V)$ for every $k$, so $p_k\le(I(\kappa;V)+\ln2)/\ln(N/k)$.
(b) $\mathbb EX\le I(\kappa;V)+\ln H_N$.
(c) $p_k\le k/N+\bar\epsilon$ and $\mathbb EX\le1+\bar\epsilon\ln N$, with $\bar\epsilon$ the probability that runs at one seed with independent canary values $\kappa,\kappa'$ output different models.
(d) For independent canaries $\kappa_1,\dots,\kappa_m$ in one run, $m\,\mathrm{kl}(\bar p_k\|k/N)\le\sum_jI(\kappa_j;V)\le I(\kappa_1,\dots,\kappa_m;V)$, with $\bar p_k$ the mean of the $m$ list probabilities.

Proof. (a) The event $\{\kappa\in L_k(V)\}$ has probability $p_k$ under $P_{\kappa V}$ and $k/N$ under $P_\kappa\otimes P_V$, and $I(\kappa;V)$ is the divergence between these two laws, so the data-processing inequality applies. Then use $\mathrm{kl}(p\|q)\ge p\ln(1/q)-\ln2$. (b) For each $v$, $Q_v(\kappa')=1/(H_N\,\pi_v(\kappa'))$ is a law on $R$. Gibbs' inequality gives $H(\kappa\mid V)\le\mathbb E\ln\pi_V(\kappa)+\ln H_N$, and $H(\kappa\mid V)=\ln N-I(\kappa;V)$. (c) With $A_\kappa=\{v:\kappa\in L_k(v)\}$, $p_k-k/N=\mathbb E_\kappa[P_{V\mid\kappa}(A_\kappa)-P_V(A_\kappa)]\le\mathbb E_{\kappa,\kappa'}\mathrm{TV}(P_{V\mid\kappa},P_{V\mid\kappa'})$ by convexity, and part (b) of `thm-coupling-certificate` bounds each total variation by the divergence probability. Integrate $\Pr[X\ge t]\le e^{-t}+\bar\epsilon$ over $[0,\ln N]$. (d) Independence gives $I(\kappa_j;V\mid\kappa_{<j})\ge I(\kappa_j;V)$, then use the chain rule, (a) and convexity of $\mathrm{kl}$. $\square$

Parts (a) and (d) turn measured exposure into lower bands on memorization. Part (c) gives the only upper band and needs named seeds. A confidence bound for $\bar p_k$ from the dependent canaries of one run is open.

### thm-null-trajectory-filter: robust coarse SGD is a filter under any reuse
status: proven
uses: none

Setting. A trainer runs $T$ steps on $p$ parameters. Step $t$ uses a set $B_t\subseteq[n]$ of $b$ indices fixed by the coins, under any schedule and any number of passes. It forms $\psi_{B_t}(w_t)=b^{-1}\sum_{i\in B_t}\psi(w_t,z_i)$ with $\psi(w,z)\in[-1,1]^p$ the clipped gradient, picks $g_t\in\rho\mathbb Z^p$ with $\|g_t-\psi_{B_t}(w_t)\|_\infty\le3\rho/4$, and sets $w_{t+1}=F_t(w_t,g_t)$. This is bSGD of AKMSS21 with fresh samples replaced by arbitrary reuse. Write $\psi_Q(w)=\mathbb E_{z\sim Q}\psi(w,z)$. The robust advantage of a trainer and attacker pair is the infimum, over all rules choosing a valid $g_t$ from everything, of $|\Pr_{D_0}[A=1]-\Pr_D[A=1]|$.

Statement. Let $\eta=\sqrt{2\ln(2Tp/\delta)/b}<\rho/4$. (a) For every attacker, unbounded and white-box, the robust advantage is at most $2\delta+Tp\,\bar\gamma/(\rho/4-\eta)^2$. Neither $n$ nor the number of passes enters. (b) For every $D$ some valid rule makes the output a function of the coins and $D$ outside an event of probability $\delta$, so the mean total variation between output laws on two independent samples is at most $2\delta$.

Proof. Let $w^0_0=w_0$, let $g^0_t$ be the point of $\rho\mathbb Z^p$ nearest to $\psi_{D_0}(w^0_t)$, and $w^0_{t+1}=F_t(w^0_t,g^0_t)$. This path depends on the coins only. The records indexed by $B_t$ are i.i.d. from the law in force and independent of $w^0_t$, so Hoeffding's inequality and a union over $Tp$ coordinates give $\|\psi_{B_t}(w^0_t)-\psi_D(w^0_t)\|_\infty\le\eta$ for all $t$, except with probability $\delta$. The averaged Gershgorin bound with $\|\phi\|_{L^2(D_0)}\le1$ and Chebyshev's inequality give $\Pr_D[|D\phi-D_0\phi|>\tau]\le\bar\gamma/\tau^2$ for each of the $Tp$ coordinate queries $\phi$ along the path, so all are within $\tau=\rho/4-\eta$ except with probability $\kappa=Tp\bar\gamma/\tau^2$. Outside both events $g^0_t$ lies within $\rho/2+\tau+\eta\le3\rho/4$ of $\psi_{B_t}(w^0_t)$, so it is valid at every step. The rule that plays $g^0_t$ when valid makes the transcript a function of the coins outside probability $\delta+\kappa$ under $D$ and $\delta$ under $D_0$, which gives (a). For (b) round $\psi_D$ instead, with $\tau=0$. $\square$

The model is that of `fact-sq-simulates-minibatch-sgd`, and the condition $\rho>4\eta$ is $b\rho^2>32\ln(2Tp/\delta)$, the form of AKMSS21 Theorem 1c. The proof does not use that theorem.

### thm-noisy-trainer-two-term-filter: population term plus memorization budget
status: proven
uses: def-random-oracle-record-split, thm-null-trajectory-filter

Setting. As in `thm-null-trajectory-filter`, with $\psi$ clipped to Euclidean norm $C$ and the rounding replaced by $w_{t+1}=F_t(w_t,\psi_{B_t}(w_t)+\xi_t)$, $\xi_t\sim\mathcal N(0,\sigma^2I_p)$ independent. $E_i$ counts the batches that hold record $i$, and $\mathcal I=2TC^2/(b\sigma^2)$.

Statement. For every attacker of the output, unbounded and white-box:
(a) its advantage in telling $D_0$ from $D$ is at most $\sqrt{TC^2\bar\gamma/\sigma^2+\mathcal I/2}$.
(b) $I(S;M)\le\mathcal I$ even when $M$ is the whole trajectory.
(c) $\mathrm{mem}_i\le2E_iC^2/(b^2\sigma^2)$.

Proof. (a) Let $P^0$ be the law of the null trajectory, driven by $\psi_{D_0}(w)+\xi_t$, and $P^S$ the law of the run on $S$. The chain rule for Markov kernels and the data-processing inequality through $F_t(w,\cdot)$ give $\mathrm{KL}(P^0\|P^S)\le(2\sigma^2)^{-1}\sum_t\mathbb E_{P^0}\|\psi_{D_0}(w^0_t)-\psi_{B_t}(w^0_t)\|^2$. The null point is independent of $S$, so the mean over $S$ of the summand is $\|\psi_{D_0}-\psi_D\|^2+\mathrm{tr}\,\mathrm{Cov}_D(\psi)/b\le\|\psi_{D_0}-\psi_D\|^2+C^2/b$ at that point. The averaged Gershgorin bound, coordinate by coordinate, gives $\mathbb E_D\|\psi_{D_0}-\psi_D\|^2\le\bar\gamma\,\mathbb E_{D_0}\|\psi\|^2\le\bar\gamma C^2$. Joint convexity of KL moves the mean over $S$ inside, so $\mathbb E_D\mathrm{KL}(P^0\|P^D)\le TC^2(\bar\gamma+1/b)/(2\sigma^2)$ and $\mathrm{KL}(P^0\|P^{D_0})\le TC^2/(2b\sigma^2)$. Pinsker's inequality and the triangle inequality give (a). (b) Replacing $z_i$ moves $\psi_{B_t}(w)$ by at most $2C/b$ at every $w$ when $i\in B_t$, so $\mathrm{KL}(P^S\|P^{S'})\le2E_iC^2/(b^2\sigma^2)$, and the bound holds at every point of the run. Hence $I(z_i;M\mid z_{-i})\le2E_iC^2/(b^2\sigma^2)$. For independent records $I(S;M)\le\sum_iI(z_i;M\mid z_{-i})$, and $\sum_iE_i=Tb$. (c) By part (b) of `def-random-oracle-record-split` and independence, $\mathrm{mem}_i\le I(z_i;M\mid u_i,z_{-i})$, which the same divergence bound controls. $\square$

The population term is the analogue of $Tp\bar\gamma/\rho^2$ in `thm-null-trajectory-filter`, and the memorization term has no analogue in the robust model.

### prop-hashed-memory-breaks-sq-filter: the memorization term cannot be dropped
status: proven
uses: thm-noisy-trainer-two-term-filter

Consider planted parity in dimension $d$. $D_0$ is uniform on $\{0,1\}^{d+1}$, and $D_v$ draws $x$ uniformly and sets $y=\langle v,x\rangle\bmod2$, for $v\neq0$. Its family has $\gamma=0$, $\beta=1$, $L=2^d-1$. Take $n=2d$ records, a table $W$ of $K=8n^2$ rows of $d+1$ parameters, a pairwise independent hash $h:\{0,1\}^d\to[K]$ drawn by the coins, the sign encoding $e(z)\in\{\pm1\}^{d+1}$, and the loss $-\langle W_{h(x)},e(z)\rangle$, so $C=\sqrt{d+1}$. Run noisy full-batch gradient descent ($b=n$) for any $T\ge1$ steps from $W=0$ with $\sigma^2=T/(16n^2\ln(8n(d+1)))$. For $d\ge d_0$ an attacker of the output has advantage at least $3/4$, while $TC^2\bar\gamma/\sigma^2=O(d^3\log d\cdot2^{-d})$ and $\mathcal I=\Theta(d^2\log d)$.

Proof. With no collision of rows, which fails with probability at most $n^2/(2K)+n^22^{-d}=1/16+o(1)$, row $h(x_i)$ equals $\gamma_{\mathrm{lr}}\big((T/n)e(z_i)+\sqrt T\sigma\,G_i\big)$ with $G_i$ standard Gaussian and $\gamma_{\mathrm{lr}}$ the step size, and empty rows hold noise only. Since $\sqrt T\sigma=(T/n)/\sqrt{16\ln(8n(d+1))}$, Gaussian tails and a union over $n(d+1)$ coordinates recover every sign, and $\chi^2$ concentration over $d+1$ coordinates with a union over $K=O(d^2)$ rows separates occupied rows by their norm, both with probability $1-o(1)$. The attacker then solves the $2d\times d$ system over $\mathbb F_2$. Under $D_v$ it is consistent. Under $D_0$ the matrix is rank deficient with probability at most $(2^d-1)2^{-2d}$, and a full-rank system is consistent with probability $2^{-d}$. The two parameter values follow by substitution. $\square$

So `thm-noisy-trainer-two-term-filter` (a) fails without its $\mathcal I$ term. Reuse is not needed, since one step suffices.

### prop-output-bounds-do-not-filter: no bound on the output composes with an SQ bound
status: proven
uses: thm-null-trajectory-filter

(a) If some test on $n$ records tells $D_0$ from $D$ with errors at most $\alpha$, the trainer that outputs its verdict has $H(M)\le\ln2$, and the identity attacker has advantage at least $1-2\alpha$. (b) For planted parity let $f(S)=\max_vn^{-1}\#\{i:y_i=\langle v,x_i\rangle\}$ and $M=\mathbf 1\{f(S)+\mathrm{Lap}(1/(\varepsilon n))>13/16\}$. Then $M$ is $\varepsilon$-differentially private, and its identity attacker has advantage at least $1-2\alpha$ once $n\ge\max\{32(d\ln2+\ln(1/\alpha)),\,16\ln(1/\alpha)/(3\varepsilon)\}$. Every SQ procedure with $q$ queries of tolerance $\tau$ has robust advantage at most $q/((2^d-1)\tau^2)$. (c) Hence no bound on the entropy, the mutual information or the central privacy loss of the output composes with an SQ lower bound.

Proof. (a) Immediate. (b) $f$ has sensitivity $1/n$, so the Laplace release is $\varepsilon$-DP and the threshold is post-processing. Under $D_v$, $f=1$. Under $D_0$, Hoeffding's inequality and a union over $2^d$ values of $v$ give $f\le5/8$ except with probability $\alpha$. The Laplace noise exceeds $3/16$ in either direction with probability $\frac12e^{-3\varepsilon n/16}\le\alpha/2$. The SQ bound is the Chebyshev step of `thm-null-trajectory-filter` against the oracle that answers with $D_0$. $\square$

## Pushbacks on the frame

1. Drop the slogan "what the trainer did not learn stays hidden", which `prop-output-bounds-do-not-filter` refutes. Its true form, "what the trainer's class cannot compute stays hidden", makes the filter theorem the closure of a learner class under post-processing, which for SQ holds by definition. The content of the frame is the data-processing inequality plus the borrowed simulation theorems that place a trainer in a class (FGRVX17 Theorem 3.13, AKMSS21 Theorem 1c, Raz). What is new here is small and exact. The null trajectory removes adaptivity, the SQ term and the memorization budget add in one inequality, and exposure is sandwiched between memorization and the coupled tail.

2. Item 21's clause on SGD should read "every coarse SGD trainer has a defending rounding". In the model that grants it, memorization cannot be stated (`thm-null-trajectory-filter` (b)). The refuted `thm-fs-sq-black-box-reduction` failed on this quantifier, and the theory should not reintroduce it through the SGD clause.

3. Epochs are not the variable. Passes are free in the robust model and enter only through $T$ and $E_i$ in the noisy model. `prop-hashed-memory-breaks-sq-filter` memorizes in one step. The variable is $\mathcal I=2TC^2/(b\sigma^2)$, which combines noise, steps and batch, three of the factors Halil named.

4. The population part of a record is not shared. Only its law is. A model that learned the population reveals the law, not $u_i$, and membership of $u_i$ is a leakage the split does not price. The random oracle adds nothing to the noise-outsourcing lemma, since every law has the split. "The individual part fools every learner class" holds only for unseen records, where it is vacuous.

5. The honest filter needs $\sigma^2\gtrsim TC^2/b$. A trainer then makes progress only where the population gradient exceeds the batch fluctuation $C/\sqrt b$ (heuristic, it assumes progress needs drift above noise along the signal). This is the regime in which learning needs no memorization. Both filters are therefore theorems about regimes real training avoids. For real training, at fine precision and small batch with no added noise, the only quantity left is $\mathrm{mem}_i$, with canary lower bands and twin upper bands.

6. Central DP is not the quantity that composes with SQ, by `prop-output-bounds-do-not-filter` (b). Local DP is, by `fact-ldp-equals-sq` (recorded, not re-read), because it restricts access. The theory should not merge privacy of individuals and hardness of population secrets into one parameter. They are two terms.

## To read

- Abbe, Kamath, Malach, Sandon, Srebro, NeurIPS 2021 (library `AKMSS21`, proofs unread). Check that its error takes the worst rounding, the quantifier `thm-null-trajectory-filter` keeps, and whether it states the multi-pass case.
- Steinke and Zakynthinou, COLT 2020, conditional mutual information (from memory, unverified). Their supersample with a uniform selector is the random-oracle individual part for membership. Check whether `lem-exposure-information-sandwich` (a) is one of their bounds.
- Brown, Bun, Feldman, Smith, Talwar, STOC 2021, memorization of irrelevant training data (from memory, unverified). Check their lower bound on the information an accurate learner holds about its sample, the case of `def-random-oracle-record-split` (c) where $s$ is unknown.
- Feldman, STOC 2020, the long tail (from memory, unverified). Compare his per-record memorization score with $\mathrm{mem}_i$.
- Carlini, Liu, Erlingsson, Kos, Song, USENIX Security 2019, the Secret Sharer (from memory, unverified). Check that their exposure is $X$ in bits.
- Steinke, Nasr, Jagielski, NeurIPS 2023, auditing with one training run (from memory, unverified). Their confidence argument for many canaries may close the open part of `lem-exposure-information-sandwich` (d).
- Kasiviswanathan, Lee, Nissim, Raskhodnikova, Smith, FOCS 2008 (library `KLNRS08`, note unfilled). Check the efficient central-DP parity learner and the interactivity conditions of the simulation of local randomizers by SQ.
- Kallenberg, Foundations of Modern Probability, second edition, 2002 (from memory, unverified). The exact statement of the noise-outsourcing lemma.
- Garg, Raz, Tal, STOC 2018, extractor-based time-space bounds, and their two-pass follow-up (from memory, unverified). Check whether any bound covers many passes, which Next needs.

## Next

Prove or refute `conj-information-memory-parity-bound`. For noisy SGD as in `thm-noisy-trainer-two-term-filter` on planted parity in dimension $d$, there is a constant $c>0$ such that every attacker of the output has advantage at most $\sqrt{TC^2\bar\gamma/\sigma^2}+2^{-\Omega(d)}$ whenever $\mathcal I\le c\,d^2$. This is an information form of Raz's memory bound that survives reuse. `prop-hashed-memory-breaks-sq-filter` shows it fails at $\mathcal I=\Theta(d^2\log d)$. If true, the theory has a memorization threshold for a known hard problem, stated in steps, batch, noise and clipping norm on both sides.
