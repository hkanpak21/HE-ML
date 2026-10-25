# Round 02 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25.

This round repairs the three statements that the round-01 discussant blocked, answers
its nonblocking challenges, and carries the fourteen objects it accepted. It is short
on purpose. Where a proof is unchanged, the object points to the section of
`round-01/builder.md` that holds it, which the round-01 discussant checked line by
line. Notation is that of rounds 00 and 01. A status of sketch below marks an object
not yet accepted. The builder knows no gap in the arguments of
`lem-scrambled-seed-urn` and `thm-shadow-run-price-finite-views` as revised here.

## Responses to challenges

ch-urn-common-nuisance. Accepted. The counterexample is right. The lemma now assumes
that the two compared learning functions share the seed law, the evaluation map, the
injection $s$, and every response at inputs other than $x_0$, and that they differ only
in the label law at $x_0$. The theorem's family satisfies this, since $\mathsf L(x_1;\cdot)$
and the model at other inputs do not depend on $\sigma$.

ch-urn-filtration. Accepted. The proof now conditions on the augmented history, which
holds the seed value of every Train call, also when the adversary holds the seed only by
name. Open can then reveal nothing outside the augmented history. The proof uses the
hybrid bound for kernels in place of a coupling, so no measurable selection is needed.

ch-profile-comparator. Accepted. Property 1 is split. For a plain-channel observation of
the whole released value the informed optimum is $\mathrm{TV}$ under the bottom oracle
and the top divergence under the top oracle, and it is attained with no call. For the
query channel with a finite query set and output space it is the best strategy tree
within the allowance, attained by hard-wiring that tree. For a general interface the
singleton regret is zero as an infimum, because an adversary that knows the instance
simulates any finite-budget informed adversary's samples and Train calls with its own
randomness, and it need not be attained.

ch-label-policy-optimum. Accepted. The discussant's two-bit example is right. Part (f)
now states the table's total variation as the bottom-oracle optimum and the top
divergence of the table channel as the top-oracle optimum, and it separates the size of
the query set $U$ from the allowance $q_E$. The factor $\ln|U|$ is stated as a gap
between the known bounds, not as a necessity.

ch-shadow-small-budgets. Accepted. Part (a) now needs $N\ge2$. For $N\le1$ the
constant output $0$ has gap $\mathrm{TV}(P_0,P_1)\le1$.

ch-shadow-policy-quantifiers. Accepted. Part (b) is now stated once per policy. Under
each policy, every adversary of that policy has a hard instance in the family, and the
proof gives it.

ch-reconstruction-majority-omission. Accepted, recorded without reading. The revised
fact cites the unnumbered result on a majority adversary in Appendix B.5 of ML24 as the
discussant reports it, and separates it from the unrestricted Theorem 10.

ch-reconnn-seed-interpretation. Accepted. The carried fact keeps its wording as a
statement about one attack in two experiments, and this round says so in its paragraph
on the other regime. Knowing the initialization is part of knowing the seed when
training also shuffles.

ch-sandwich-endpoint-details. Accepted. The revised proof treats $S^\star=\bar\kappa$
directly and passes to a tail of the approximating sequence when $S^\star>\bar\kappa$.
The reading now says that the gain above the floor can come from removing head error as
well as from residual information, while the gain above $\bar\kappa$ needs residual
information.

Three domain remarks without names, all accepted. HSU25 Definition 2.4 takes $\rho>0$,
and the carried fact states it. DN03 Theorem 5 takes $\delta>0$, and the carried fact
states it. XD23 treats randomized mechanisms in §4.2 and Corollary 2, and the carried
fact calls itself the deterministic specialization.

## Objects revised in this round

### fact-reconstruction-query-lower-bounds: how many of the trainer's outputs a reconstruction attacker must see

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Statement. Key ML24, arXiv 2303.16372v6. The game and Theorem 9 are as stated in
`round-01/builder.md`. Theorem 10, the claimed matching upper bound for every
$\varepsilon\ge0$ and $\delta\in[0,1]$, is not established, since the adversary of the
proof in Appendix B.5 uses the true target. Corollary 12 is not established, since the
proof of Lemma 16 in Appendix B.3 bounds the total variation from the wrong side. The
same Appendix B.5 holds, per the round-01 discussant, an unnumbered result on a
target-independent majority adversary for privacy parameter at least $0.042$ (pages 26
and 27). The builder has not read that passage. It does not give the uniform rate of
Theorem 10.

Proof. Borrowed for Theorem 9. The two gaps were read by the builder.

The other regime. The unit counts the trainer's outputs that the attacker observes, and
the bound needs differential privacy inside training.

### def-uniform-security-profile: the uniform regret profile of an unbounded adversary in learning units

status: open

uses: thm-coupling-certificate, thm-black-box-certifiability, def-degenerate-oracles, fact-hsu-membership-sample-gap

Statement. Items 1 to 4 (informed optimum, uniform regret, attained price, threshold
price) are unchanged from `round-01/builder.md`.

Properties, with labels.

1. Singleton classes. (i) For any interface, an adversary that knows $\iota$ and has
   budget $\beta$ simulates every finite-budget informed adversary, drawing reference
   samples from $\mathcal D_\iota$ and computing $\mathsf L$ on its own randomness, also
   at the honest seed it opens under the top oracle. So
   $g_{\{\iota\},\mathsf P}(\beta)=0$ as an infimum at every budget (proven, by this
   simulation, since a simulated answer has the law of the oracle's answer by
   fidelity). (ii) For one learning node whose whole value reaches the adversary
   through a channel $K$ on the plain channel, the optimum is $\mathrm{TV}(P_0,P_1)$
   under the bottom oracle and $\mathrm D^\top_1(K)$ under the top oracle, and an
   adversary that hard-wires the optimal test attains it with no sample and no call
   (proven, step 3 of `thm-coupling-certificate` (b)). (iii) For the query channel with
   a finite query set, finitely many outputs and allowance $q_E$, the bottom-oracle
   optimum is $\mathrm{Adv}^{\mathrm{bb}}(q_E)$, a maximum over finitely many strategy
   trees, attained by hard-wiring a best tree (proven,
   `thm-black-box-certifiability` (o)).
2. Finite views. Unchanged from round 01.
3. HSU25 at $N=0$. Unchanged from round 01, with $\rho>0$.

Sketch of well-posedness, what would settle it, regime and experiment are unchanged
from round 01.

The other regime. Unchanged from round 01.

### lem-scrambled-seed-urn: a random scramble of seed cells turns chosen and opened seeds into fresh draws

status: sketch

uses: def-learning-oracle

Statement. Let $\mathcal V$ be finite and $M$ an integer. Partition $[0,1)$ into cells
$c(t)=\lfloor Mt\rfloor\in[M]=\{0,\dots,M-1\}$. A learning setting $\Lambda$ fixes a seed
law $\mu$ on $[0,1)^2$ with uniform second coordinate, an evaluation map, an injection
$s:\mathcal V\to\mathcal M$, a training input $x_0$, and a response at every input other
than $x_0$, a measurable map of the seed and the input that the setting fixes. For a law
$p$ on $\mathcal V$ with $Mp(v)\in\mathbb N$, a labelling $\lambda$ of $[M]$ with
$|\lambda^{-1}(v)|=Mp(v)$ and a bijection $\pi$ of $[M]$, the learning function
$\mathsf L^{p,\pi}_\Lambda$ has deterministic kernels, returns
$s(\lambda(\pi(c(\rho_b))))$ at $x_0$ for the seed $\rho=(\rho_a,\rho_b)$, and gives the
setting's response elsewhere. Fix an adversary with at most $N<M$ Train calls, any Eval
and Open calls, adaptive choices of inputs, seed values, seed names and draws, run
against a fixed challenge value $v$. Let $T_v$ be the law of its transcript under
$\mathsf L^{p,\pi}_\Lambda$ with $\pi$ uniform and independent of everything else. Let
$\tilde T_v$ be the law of its transcript under the lazy oracle, which answers a Train
call at $x_0$ whose seed lies in a cell not met by an earlier Train call at $x_0$ with
$s(V)$ for a fresh $V\sim p$, answers a call at $x_0$ in an earlier cell with the earlier
model, and answers every other call as $\mathsf L^{p,\pi}_\Lambda$ does. Then:

1. $\mathrm{TV}(T_v,\tilde T_v)\le N^2/(2(M-N))$.
2. For a second law $p'$ and the lazy oracle $\tilde T'_v$ built from $p'$ with the same
   setting $\Lambda$ and the same adversary,
   $\mathrm{KL}(\tilde T_v\|\tilde T'_v)\le N\,\mathrm{KL}(p\|p')$.

Proof. Represent the run as a sequence of steps. Step $j$ is either an action of the
adversary, a kernel of the augmented history, or an answer of the oracle, a kernel of the
augmented history and the instance. The augmented history $h_j$ holds every action and
answer so far and the seed value of every Train call made so far, also when the
adversary holds it only by name. All spaces are standard Borel, so these kernels exist.
Pad the run after it stops with a fixed symbol, so that it is an infinite sequence.

Step 1, the conditional laws. Fix a history $h$ before a Train call at $x_0$. Its
augmented part determines the cells $c_1,\dots,c_{t-1}$ met by earlier Train calls at
$x_0$, their labels $u_1,\dots,u_{t-1}$, and the cell $c$ of the present seed. Every other
answer in $h$ is a function of the seeds and the inputs that the setting fixes, or of a
stored model $s(u_j)$ and fresh evaluation randomness, so it does not depend on $\pi$.
Bayes' rule over the finite set of bijections therefore gives, under the uniform $\pi$
given $h$, the uniform law on bijections with $\lambda(\pi(c_j))=u_j$ for $j<t$. If $c$ is
a new cell, $\pi(c)$ is uniform on the $M-t+1$ cells outside
$\pi(\{c_1,\dots,c_{t-1}\})$ under that law, so the label has law
$q_h(v)=(Mp(v)-r_v)/(M-t+1)$, with $r_v$ the number of $u_j$ equal to $v$, and
$\mathrm{TV}(q_h,p)\le(t-1)/(M-t+1)$, as computed in round 01. If $c$ is an earlier cell,
both oracles return the earlier model. Every step that is not a Train call at $x_0$ has
the same kernel under both oracles.

Step 2, the hybrid bound. Let $P_{1:j}=P_{1:j-1}\otimes K_j$ be the law of the first $j$
steps under the scrambled oracle and $Q_{1:j}=Q_{1:j-1}\otimes K'_j$ under the lazy one. The
triangle inequality through $P_{1:j-1}\otimes K'_j$ and data processing under $K'_j$ give

$$\mathrm{TV}(P_{1:j},Q_{1:j})\le\mathrm{TV}(P_{1:j-1},Q_{1:j-1})+\int\mathrm{TV}(K_j(\cdot\mid h),K'_j(\cdot\mid h))\,P_{1:j-1}(dh)$$

(proven, standard). Summing over $j\le L$, the prefix of length $L$ is within
$\mathbb E_P\big[\sum_{j\le L}\mathrm{TV}(K_j(\cdot\mid h_{j-1}),K'_j(\cdot\mid h_{j-1}))\big]$,
the expectation along paths of the scrambled run. On each path the summand is zero except at
new-cell Train calls at $x_0$, of which there are at most $N$, and at the $t$-th of them it is
at most $(t-1)/(M-N)$ by Step 1. So every finite prefix of the two runs is within
$\sum_{t\le N}(t-1)/(M-N)\le N^2/(2(M-N))$. A bound with a supremum over histories at each
fixed step index would not suffice, since the index of the $t$-th new-cell call varies with
the path.
The cylinder sets form an algebra that generates the product $\sigma$-algebra, so the total
variation of the infinite sequences is the supremum over prefixes, and the transcript is a
measurable function of the sequence. This gives claim 1 by data processing.

Step 3, the KL bound. Under the two lazy oracles the kernels differ only at new-cell Train
calls at $x_0$, where they are $s_*p$ and $s_*p'$ whatever the history. The chain rule
gives, for every finite prefix, the sum over steps of the expected conditional KL, which is
at most $N\,\mathrm{KL}(p\|p')$. The KL of the infinite sequences is the supremum over the
increasing prefix $\sigma$-algebras, and data processing passes it to the transcript. $\square$

Status. Sketch until a round accepts it. No gap is known to the builder.

The other regime. The lemma makes the oracle's seed interface no stronger than a stream of
fresh draws against an unknown scramble. The round-01 discussant points to the
permutation against random function switching argument, of which this is the statistical
form, with no hardness assumption.

### thm-shadow-run-price-finite-views: the training-run price of distinguishing two training inputs on k views

status: sketch

uses: lem-scrambled-seed-urn, thm-coupling-certificate, thm-black-box-certifiability, thm-reference-access, def-degenerate-oracles, def-uniform-security-profile

Setting. As in `round-01/builder.md`.

Statement.

(a) Upper bound. Let $N\ge2$. For every learning function, the plug-in adversary with
$n=\lfloor N/2\rfloor$ drawn-seed Train calls at each input has
$\mathrm{TV}(P_0,P_1)-\mathrm{Adv}\le2\sqrt{k/n}$, in expectation over its shadow draws.
For $N\le1$ the constant output $0$ has gap $\mathrm{TV}(P_0,P_1)$.

(b) Lower bound, general kernels. Let $k\ge4$ and $N\ge1$. Under the bottom oracle, every
adversary with at most $N$ Train calls has, at some $\mathsf L^\sigma$ of the family of
round 01, gap at least $g_N=\min\{\frac18,\frac1{32}\sqrt{3k'/N}\}$. Under the top oracle,
every adversary of the top oracle with at most $N$ Train calls has, at some $\mathsf L^\sigma$
of the same family, a gap of at least $g_N$ against the top optimum, which equals
$\mathrm{TV}(P_0,P_1)$ on this family.

(c) Lower bound, deterministic kernels, bottom oracle. Every adversary with at most $N$
Train calls and every $\zeta>0$ have, at some $\mathsf L^{\sigma,\pi}$ of the scrambled
family of round 01, gap at least $g_N-\zeta$.

(d) Top oracle, deterministic kernels. Unchanged. One Train call at the honest seed
reaches the top optimum $\mathrm D^\top_1(\kappa)$, which is at least $\mathrm{TV}(P_0,P_1)$.

(e) Price. Unchanged. For $0<a<\frac18$ and $k\ge4$, under the bottom oracle over
$\mathfrak J_{\mathrm{all}}$ or $\mathfrak J_{\mathrm{det}}$, regret at most $a$ everywhere
needs at least $3k'/(1024a^2)$ Train calls, and $2\lceil4k/a^2\rceil$ drawn-seed calls
suffice in expectation. Under the top oracle, one call suffices over
$\mathfrak J_{\mathrm{det}}$, and $3k'/(1024a^2)$ calls remain necessary over
$\mathfrak J_{\mathrm{all}}$.

(f) Label-only views. Let $U$ be a finite query set, $C\ge2$ outputs, deterministic
evaluation $\mathsf{ev}(t,u)=t(u)$ on models that include the tables $t\in[C]^U$, and the
query channel with allowance $q_E\le|U|$. Under the bottom oracle the optimum is
$\mathrm{Adv}^{\mathrm{bb}}(q_E)$, and over learning functions that vary the table only on a
fixed set $U_0\subseteq U$ of $q_E$ points, it equals the total variation of the laws of
the table on $U_0$. On such functions the bounds of (a), (b), (c) and (e) hold with
$k=C^{q_E}$. Under the top oracle the optimum is the top divergence of the channel that
reads the table on $U_0$, which can exceed the total variation of the marginal table laws,
and part (d) applies to it with $\kappa$ the restriction to $U_0$. The upper bound of
`thm-black-box-certifiability` (b) at allowance $q_E$ is
$2\sqrt{\ln(2|\mathfrak T_{q_E}|)/n}$ with $\ln|\mathfrak T_{q_E}|\le\frac{C^{q_E}-1}{C-1}\ln|U|+C^{q_E}\ln2$,
so the known upper and lower bounds on the bottom-oracle price differ by a factor of order
$\ln|U|/(C-1)+1$. Whether that factor is needed is open.

Proofs. Parts (a), (b), (d) and (e) as in `round-01/builder.md`, section
`thm-shadow-run-price-finite-views`, with two changes. In (a) the empirical laws exist
because $n\ge1$. In (b) the quantifiers are per policy. Step 1 is the decision-rule
reduction for adversaries of one policy, and Steps 2 to 4 give each such adversary a hard
sign vector. Under the top oracle the family ignores the seed, so the honest seed is one
more auxiliary variable independent of the challenge, as the round-01 discussant noted.
Part (c) as in round 01, now with `lem-scrambled-seed-urn` in its revised form. Its
hypothesis holds, since the scrambled family shares the seed law, the evaluation map, the
injection and the responses at $x_1$ and at other inputs across $\sigma$. Part (f). Let the
family vary the table only on $U_0$ and keep fixed values elsewhere. A query outside $U_0$
then returns a value free of the instance, so the best strategy tree of depth $q_E$ reads
$U_0$ and outputs $\mathbf 1[t|_{U_0}\in A^\ast]$, and $\mathrm{Adv}^{\mathrm{bb}}(q_E)$ is
the total variation of the restricted table laws by data processing. Every adversary's output
is a function of $t|_{U_0}$ and its own transcript, which is the setting of (a) to (e) with
$\mathcal V=[C]^{U_0}$. Under the top oracle the discussant's example, two fair seed bits under
$x_0$ and their complements under $x_1$, has marginal total variation zero and top divergence
one, so the top optimum must be taken on the pair of seed and table. Part (d) gives one call
that reaches it under deterministic kernels. $\square$

Status. Sketch until a round accepts it. No gap is known to the builder.

Prior work and novelty. The passive rate is classical (Daniely, Sabato, Ben-David and
Shalev-Shwartz, JMLR 2015, Theorem 5, as the round-00 and round-01 discussants cite, not read
by the builder). The scrambling step is the statistical form of the switch from a random
permutation to a random function (Bellare and Rogaway, EUROCRYPT 2006, as the round-01
discussant cites, not read). The search row `search-shadow-run-lower-bound` of
`round-01/summary.md` found no lower bound on shadow training runs. The oracle part, that
chosen, opened and reused seeds do not beat the passive rate under the bottom oracle, while
the honest seed collapses it to one call under deterministic kernels, has no known published
statement (open as a novelty claim, one query run).

Meaning in the trainer's units and the other regime. Unchanged from round 01.

## Objects carried from round 01

Each object below received ACCEPT in round 01 and is unchanged, except where a line says
otherwise. Its statement, proof and paragraph on the other regime are in
`round-01/builder.md` under the same heading.

### fact-hsu-membership-sample-gap: reference samples that membership inference needs against noisy mean estimation

status: borrowed

uses: none

Unchanged, with $\rho>0$ stated, as HSU25 Definition 2.4 takes it.

### fact-hsu-gap-prices-covariance: with the covariance known the sample price falls to order min of n and inverse squared noise

status: borrowed

uses: fact-hsu-membership-sample-gap

Unchanged, with $\rho>0$, $n\ge4$ and $m\ge2$ as in HSU25 Theorem 4.1.

### fact-yeom-dp-bounds-membership-advantage: differential privacy bounds the advantage of an informed membership attacker

status: borrowed

uses: none

Unchanged.

### fact-yeom-generalization-error-gives-advantage: a loss-threshold attack gains the normalized generalization error

status: borrowed

uses: fact-yeom-dp-bounds-membership-advantage

Unchanged.

### fact-lira-priced-in-training-runs: the likelihood-ratio attack spends 64 to 256 shadow training runs

status: borrowed

uses: fact-lira-low-fpr-yeom-game

Unchanged.

### fact-lira-low-fpr-yeom-game: the LiRA game excludes members from the OUT draw

status: borrowed

uses: fact-yeom-dp-bounds-membership-advantage

Unchanged, with the domain the round-01 discussant noted. The OUT draw needs the
exclusion event to have positive probability, and the agreement with Yeom's game needs it
to have probability one.

### fact-balle-reconstruction-robustness-definition: reconstruction robustness and its oblivious baseline

status: borrowed

uses: none

Unchanged.

### fact-balle-dp-bounds-reconstruction: Rényi and pure differential privacy bound reconstruction by the baseline

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Unchanged.

### fact-dinur-nissim-reconstruction-thresholds: reconstruction thresholds for subset sums

status: borrowed

uses: none

Unchanged, with $\delta>0$ in Theorem 5, as DN03 states it.

### fact-pac-privacy-mutual-information-bound: mutual information bounds the gain of a reconstruction that beats the prior guess

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Unchanged.

### fact-pac-privacy-gaussian-release-bound: a Gaussian release has mutual information set by its covariance

status: borrowed

uses: fact-pac-privacy-mutual-information-bound

Unchanged. It is the deterministic specialization. XD23 §4.2 and Corollary 2 treat
randomized mechanisms, and Theorem 4 needs the bound $\|M(X)\|_2\le r$.

### fact-zhao-accuracy-forces-attribute-leakage: an accurate representation must leak a correlated attribute

status: borrowed

uses: none

Unchanged.

### fact-balle-reconnn-priced-in-shadow-runs: reconstruction by a learned reconstructor costs thousands of shadow runs and needs the initialization

status: borrowed

uses: fact-balle-reconstruction-robustness-definition

Unchanged. Its words "needs the initialization" describe one attack in the experiments of
BCH22 and do not assert that reconstruction without the initialization is statistically
impossible. Knowing the initialization is part of knowing the seed when training also
shuffles.

### prop-reconstruction-label-sandwich: the trainer's error and the representation's residual information bracket an unbounded reconstructor

status: sketch

uses: fact-balle-reconstruction-robustness-definition, fact-pac-privacy-mutual-information-bound, fact-pac-privacy-gaussian-release-bound, fact-zhao-accuracy-forces-attribute-leakage

Statement unchanged from round 01. Two changes. In the ceiling proof, if
$S^\star=\bar\kappa$ the divergence is zero. If $S^\star>\bar\kappa$, a tail of any
sequence $R_j$ with $P(E_{R_j})\to S^\star$ lies above $\bar\kappa$, where the bound for each
$R_j$ holds, and lower semicontinuity passes it to the limit. In the reading, the gain of an
unbounded reconstructor above the floor $\bar\kappa-\varepsilon^\star$ can come from removing
the head's error as well as from residual information, and only the gain above $\bar\kappa$
needs residual information $I(X;Z\mid Y)$.
