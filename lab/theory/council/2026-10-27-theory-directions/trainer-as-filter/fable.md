---
model: claude-fable-5-1
discussant: fable
date: 2026-10-27
prompt: lab/theory/council/2026-10-27-theory-directions/trainer-as-filter/prompt-critique.md
---

# Critique of the meditation on the trainer as filter

## Verdict in one paragraph

Every proof in the meditation holds as written, and I recomputed every constant. Nothing is false and no definition is ill-posed, so no challenge below blocks. The honest answer to the council's question is negative and the meditation gives it, though not in one sentence. No composition theorem makes a memorizing trainer a filter. A filter exists only for a trainer whose channel from the sample to its trajectory carries at most about two nats in total, which is $\mathcal I\lesssim2$, and such a trainer learns little. Beyond that regime the frame offers one quantity, the per-record conditional information $\mathrm{mem}_i$, which is the Gaussian-mechanism accountant of differentially private training read in nats. The strongest idea is the null trajectory, because it removes adaptivity without fresh samples and because its part (b) shows that the rounding model behind `fact-sq-simulates-minibatch-sgd` cannot state memorization. The meditation misses that its three pieces compose into the one inequality Halil asked for, a bound on the list-decoding success of any attacker, a VAE included, in the hyperparameters of noisy training, and it misses that this inequality is differential-privacy auditing restated.

Known results I name below are from memory and unverified unless they carry a library key. I never invent a theorem number.

## Claims

### def-random-oracle-record-split

Statement true as written. The definition is well posed for every fixed statistic $s$ (proven, the three parts below).

Part (a) is the noise-outsourcing lemma for standard Borel spaces. Kallenberg, Foundations of Modern Probability, second edition, 2002, states it as a transfer lemma, and Austin's survey of exchangeability states it under the name noise outsourcing (both from memory, numbers unverified). The chained-quantile sketch is a correct proof for $\mathbb R^d$. The extension by Borel isomorphism is correct. The requirement $s(g(u,r))=u$ almost surely follows from $g(s(Z),r)=Z$ almost surely by applying $s$ (proven).

Part (b) is correct. Conditional on $u_i$, the record $z_i$ is a function of $r_i$, which gives $I(z_i;M\mid u_i)\le I(r_i;M\mid u_i)$. The pair $(z_{-i},\text{coins})$ is independent of $(u_i,r_i,z_i)$, so $r_i\to z_i\to M$ is a Markov chain given $u_i$ and the reverse inequality holds (proven, two lines of the chain rule).

Part (c) is correct and its content is small. The hypothesis is that the trainer can sample the conditional law of a record given its population part. For the statistic the meditation calls canonical, the Bayes posterior of the label, that conditional law is the law of $x$ given $\eta(x)$, which is the data law up to the fibres of $\eta$. A trainer that holds the data law needs no sample at all, since it can draw a fresh training set and run $T$ on it with the same output law. Part (c) is that remark with the marginal of $u$ kept from the sample (proven). Its only non-vacuous case is a statistic $s$ that leaves a simple conditional law, label noise given $\eta(x)$ for instance. There the statement is the known relabelling argument.

Status label. Proven is right for the three parts. The sentence "In supervised learning the Bayes posterior of the label is canonical" in the Meditation section carries no label and is not proven. It conceals the choice that decides what the theory calls memorization. If $s(z)=\eta(x)$, then $u_i$ is a vector of class probabilities, $\mathrm{mem}_i$ is close to $I(z_i;M)$, and reconstructing $x_i$ from the model counts as memorization. If $s(z)=(x,\eta(x))$, then $\mathrm{mem}_i=I(y_i;M\mid x_i)$ counts label noise only, and a model that stores every training image memorizes nothing. The two readings are both defensible and they define different objects (proven, by the two computations).

Known or new. The quantity $\mathrm{mem}_i$ is a per-record conditional mutual information. Bassily, Moran, Nachum, Shafer and Yehudayoff, ALT 2018, bound $I(S;M)$ for learners that use little information. Steinke and Zakynthinou, COLT 2020, condition on a supersample and make the selector bit the hidden part. Feldman, STOC 2020, defines a per-record memorization score as a leave-one-out change in the label probability, which is an influence and not an information (all from memory, unverified). The random oracle adds nothing to any of these, and the meditation says so in its pushback 4. The split is a restatement.

Challenges.

- `ch-canonical-statistic-ambiguous`. The claim that the Bayes posterior is canonical is unlabelled and false as a uniqueness claim, since two natural statistics give different $\mathrm{mem}_i$. The definition should name $s$ as a parameter in the notation, $\mathrm{mem}_i^{(s)}$, and the frame should say which $s$ it prices. Does not block, the definition is well posed per $s$.
- `ch-random-oracle-wrapper`. The phrase random oracle and the oracle $H$ carry no content beyond a uniform variable per index. Drop them and keep the noise-outsourcing split. Does not block.
- `ch-part-c-hypothesis`. Part (c) should state that its hypothesis is knowledge of the conditional law of $z$ given $u$, and should note that for the posterior statistic this is knowledge of the data law up to fibres. Does not block.

### prop-canary-is-programmed-record

Statement true as written under its hypothesis. Part (a) is lazy sampling. Programming one point of a uniform function with a fresh uniform value leaves the joint law unchanged (proven, trivial). Part (b) is `prop-best-advantage-equals-total-variation`, the Neyman and Pearson lemma, restated. Part (c) is the definition of a top-$k$ list. The exposure $X=\ln N-\ln\pi_V(\kappa)$ is the exposure of Carlini, Liu, Erlingsson, Kos and Song, USENIX Security 2019, in nats instead of bits (from memory, unverified).

The hypothesis is narrower than the definition it uses. `def-random-oracle-record-split` has $r$ uniform on $[0,1]$. This proposition has $r$ uniform on a finite set $R$ of size $N$. A split of $D$ along $s$ with a finite uniform $r$ exists exactly when the conditional law of $z$ given $u$ is uniform on $N$ atoms for almost every $u$ (proven, since $g(u,\cdot)$ pushes the uniform law on $R$ to that conditional law). For a designer's template whose secret is a uniform $N$-ary string this holds by construction. For a natural record law it fails. The proposition is then vacuous for natural data, and the sentence "Under Halil's rule a canary measures the memorization of a typical record" holds only for data laws of the template kind.

The consequence the meditation half-states should be stated in full. Under the admissibility rule, a canary is an honest draw from $D$ whose individual part the designer records. A Secret Sharer canary, a template sentence with a random number, is not a draw from a natural text law, so under part (b) it is inadmissible, and the AKOOMS24 canary clients are inadmissible by the simpler reason that a uniform unit vector scaled to the clipping norm does not have the law of an honest clipped update (proven, the two laws differ, so an unbounded party has positive advantage). The meditation's heuristic reason, that honest updates vary across rounds, is not needed, and on the Stack Overflow data of AKOOMS24 each client participates in exactly one round, so it does not apply there (empirical, from the ledger row of `AKOOMS24`). The frame therefore cannot interpret any exposure number in the literature. It measures its own object, the memorization of a typical record, and that object has no published measurement yet.

Status label. Proven is right. The remark about AKOOMS24 is labelled heuristic and I would relabel it proven with the law-mismatch argument.

Known or new. A restatement of lazy sampling and of the test fact. Its value is as a remark under the admissibility rule of `CONTEXT.md`, and I would keep it as one.

Challenges.

- `ch-finite-uniform-hypothesis`. State the hypothesis as a property of $D$ along $s$, or widen the definition to an arbitrary law of $r$, under which noise outsourcing still holds for any atomless $r$. Does not block, the statement is true under its hypothesis.
- `ch-literature-canaries-inadmissible`. Say in the statement that the Secret Sharer and AKOOMS24 canaries are inadmissible under part (b), so that no existing exposure measurement is a measurement of $\mathrm{mem}_c$. Does not block.
- `ch-extra-record-changes-n`. The remark that an added canary changes $n$ is correct and should be in the statement, since every experiment in the literature adds canaries. Does not block.

### lem-exposure-information-sandwich

Statement true as written. I checked every part.

Part (a). The event $\{\kappa\in L_k(V)\}$ has probability $p_k$ under the joint law and $k/N$ under the product law, because $\kappa$ is uniform and independent of $V$ under the product and the list has exactly $k$ members. The data-processing inequality for the Kullback divergence gives $\mathrm{kl}(p_k\|k/N)\le I(\kappa;V)$. The inequality $\mathrm{kl}(p\|q)\ge p\ln(1/q)-\ln2$ follows from the binary entropy being at most $\ln2$ and from $(1-p)\ln(1/(1-q))\ge0$ (proven). This is the list-decoding form of Fano's inequality. It needs $\pi_V$ to be a bijection of $R$ onto $[N]$, so ties must be broken.

Part (b). $Q_v(\kappa')=1/(H_N\pi_v(\kappa'))$ sums to one over $R$. Gibbs' inequality gives $H(\kappa\mid V=v)\le\mathbb E[\ln\pi_v(\kappa)\mid v]+\ln H_N$. Averaging and $H(\kappa\mid V)=\ln N-I(\kappa;V)$ give $\mathbb EX\le I(\kappa;V)+\ln H_N$ (proven). I do not know this inequality in print. It is the most useful line of the lemma, because it converts the mean exposure, the quantity experiments report, into a lower band on information with a slack of $\ln(1+\ln N)$.

Part (c). $p_k-k/N=\mathbb E_\kappa[P_{V\mid\kappa}(A_\kappa)-P_V(A_\kappa)]$ with $P_V=\mathbb E_{\kappa'}P_{V\mid\kappa'}$, so the difference is at most $\mathbb E_{\kappa,\kappa'}\mathrm{TV}(P_{V\mid\kappa},P_{V\mid\kappa'})$. The identity coupling of `thm-coupling-certificate` (b) bounds each total variation by the probability that the coupled models differ, and $V$ is a post-processing of $M$ (proven). The integral $\int_0^{\ln N}(e^{-t}+\bar\epsilon)\,dt=1-1/N+\bar\epsilon\ln N$ gives $\mathbb EX\le1+\bar\epsilon\ln N$ (proven, recomputed). One scope point is missing. With hardware randomness $\xi$ and a continuous model space, two runs at one seed differ with probability one, so $\bar\epsilon=1$ and part (c) is true and empty. It has content for deterministic kernels, or with a threshold $\Delta$ and a view that is Lipschitz in the model, which is how `thm-coupling-certificate` and `thm-dataflow-composition` state their Gaussian case.

Part (d). Independence of the canaries gives $I(\kappa_j;V\mid\kappa_{<j})=I(\kappa_j;V,\kappa_{<j})\ge I(\kappa_j;V)$, the chain rule sums them, and convexity of $\mathrm{kl}$ in its first argument gives the factor $m$ (proven).

Two links the title promises are not in the statement. The lemma bounds $I(\kappa;V)$, and the title says memorization. The missing line is $I(\kappa;V)\le I(\kappa;M)\le I(\kappa;M\mid u_c)=\mathrm{mem}_c$, where the last step uses independence of $\kappa$ and $u_c$ (proven, one line). With it, parts (a), (b) and (d) are lower bands on $\mathrm{mem}_c$. Part (c) bounds $p_k$ by the coupled tail and not by $\mathrm{mem}_c$, so the lemma is two one-sided bounds on two different quantities and not a sandwich of exposure between them.

Status label. Proven is right.

Known or new. Part (a) is known as the list form of Fano's inequality. Part (c) is a corollary of `thm-coupling-certificate`. Part (d) is the chain rule. Part (b) is new to me and worth keeping. Steinke, Nasr and Jagielski, NeurIPS 2023, give the confidence argument for many canaries in one run under a differential privacy hypothesis on the trainer (from memory, unverified). Part (a) needs no such hypothesis, and that is the small added value the meditation should claim explicitly.

Challenges.

- `ch-exposure-upper-band-deterministic-only`. State part (c) for deterministic kernels, or with a threshold and a Lipschitz view, since otherwise $\bar\epsilon=1$. Does not block.
- `ch-sandwich-missing-link`. Add $I(\kappa;V)\le\mathrm{mem}_c$ to the statement and rename the lemma, since exposure is not sandwiched between memorization and the tail. Does not block.
- `ch-ranking-ties`. Require $\pi_V$ to be a bijection or fix a tie-breaking rule, else $|L_k(V)|\ne k$ and the product-law probability is not $k/N$. Does not block.

### thm-null-trajectory-filter

Statement true as written. I checked the proof step by step.

The averaged Gershgorin bound. With $h_l=dD_l/dD_0-1$, the Gram matrix $\chi_{lm}=\langle h_l,h_m\rangle_{L^2(D_0)}$ has the nonzero spectrum of $\sum_lh_l\langle h_l,\cdot\rangle$, and Gershgorin gives $\lambda_{\max}\le\beta+(L-1)\gamma$. Dividing by $L$ gives $\bar\gamma=\gamma+\beta/L$ (proven). This is the average-correlation bound behind the statistical dimension of FGRVX17, in a clean form.

The Hoeffding step. Each coordinate of $\psi$ lies in $[-1,1]$, so a batch mean of $b$ records deviates from its mean by more than $\eta$ with probability at most $2\exp(-b\eta^2/2)$. Setting this to $\delta/(Tp)$ gives $\eta^2=2\ln(2Tp/\delta)/b$, as stated (proven, recomputed). The step is legitimate under any reuse because the evaluation point $w^0_t$ is a function of the coins alone, so the $b$ records of $B_t$ are i.i.d. and independent of it. This is the whole content of the device, and it is correct.

The Chebyshev step. For a coordinate query $\phi$ with $\|\phi\|_{L^2(D_0)}\le1$, the averaged Gershgorin bound and Markov's inequality on the squared deviation give $\Pr_l[|D_l\phi-D_0\phi|>\tau]\le\bar\gamma/\tau^2$, and the union over $Tp$ queries gives $\kappa=Tp\bar\gamma/\tau^2$ (proven).

Validity. Outside both events, $\|g^0_t-\psi_{B_t}(w^0_t)\|_\infty\le\rho/2+\tau+\eta=3\rho/4$ under $D$, and $\le\rho/2+\eta\le3\rho/4$ under $D_0$ because $\eta<\rho/4$ (proven, recomputed). The rule plays $g^0_t$ while valid, so the transcript equals the null path outside probability $\delta+\kappa$ under $D$ and $\delta$ under $D_0$, and the two output laws are within total variation $2\delta+\kappa$ (proven). Part (b) rounds $\psi_D$ along the $D$-null path, needs $\eta\le\rho/4$ only, and makes the output a function of the coins and $D$ outside probability $\delta$ (proven).

The condition $b\rho^2>32\ln(2Tp/\delta)$ is the form of AKMSS21 Theorem 1c, and the library note of `AKMSS21` confirms that the paper's error takes the supremum over valid roundings, which is the quantifier the meditation keeps. The proof does not use the theorem, as it says.

Status label. Proven is right.

Known or new. The argument is the adversarial-oracle proof of every SQ lower bound. Answer each query as if the law were $D_0$, observe that the algorithm's path is then data-free, and bound the probability that some answer was invalid for the true law. FGRVX17 and the SDA bounds of Feldman's later papers run exactly this way (from memory). AKMSS21 Theorem 1c with the SQ bound of planted parity gives the same $Tp\bar\gamma/\rho^2$ form for fresh batches. What is new is one observation, that reuse costs nothing when the comparison runs along a data-free path, and the explicit statement (b) that the robust model leaks nothing about the sample. The second is the sharper point and it has a consequence for the theory. The SGD clause of item 21 and of `lem-sq-learner-post-processing` should read "every coarse SGD trainer has a defending rounding", as the meditation's pushback 2 says, and I agree with that pushback in full (proven, by part (b)).

Challenges.

- `ch-robust-is-defender-best`. The word robust names an infimum over rounding rules, which is the best case for the defender and the worst for the attacker. From a security standpoint it is the least robust reading. Name it the defended advantage, or the best-rounding advantage, so a reader does not take it for a worst-case bound. Does not block.
- `ch-rule-knows-secret`. The rule in (a) uses $D_0$ and the coins and never the secret, which is a stronger and more meaningful statement than the definition's "from everything" suggests, while the rule in (b) uses $D$. State the two quantifiers apart. Does not block.
- `ch-coin-dependent-loss`. The setting fixes $\psi$ as one function of $(w,z)$. `prop-hashed-memory-breaks-sq-filter` uses a loss that depends on a hash drawn by the coins. Either let $\psi$ depend on the coins in both theorems, which the proofs allow since they condition on the coins throughout, or derandomize the counterexample. Does not block, see the fix under that proposition.

### thm-noisy-trainer-two-term-filter

Statement true as written, and the bound in (a) is looser than what the proof gives.

Part (a). The chain rule for two Markov chains with the same coins and Gaussian transitions gives $\mathrm{KL}(P^0\|P^S)\le(2\sigma^2)^{-1}\sum_t\mathbb E_{P^0}\|\psi_{D_0}(w^0_t)-\psi_{B_t}(w^0_t)\|^2$, and the maps $F_t$ are post-processing (proven). At a fixed point $w$ independent of $S$, $\mathbb E_S\|\psi_{D_0}(w)-\psi_{B_t}(w)\|^2=\|\psi_{D_0}(w)-\psi_D(w)\|^2+\mathrm{tr}\,\mathrm{Cov}_D(\psi(w,\cdot))/b$, and the trace is at most $C^2$ (proven, bias plus variance). Coordinate by coordinate, the averaged Gershgorin bound gives $\mathbb E_l\|\psi_{D_0}-\psi_{D_l}\|^2\le\bar\gamma C^2$ (proven). Convexity of the Kullback divergence in its second argument moves the mean over $S$ inside, so $\mathbb E_l\mathrm{KL}(P^0\|P^{D_l})\le TC^2(\bar\gamma+1/b)/(2\sigma^2)$ and $\mathrm{KL}(P^0\|P^{D_0})\le TC^2/(2b\sigma^2)$ (proven, recomputed). Pinsker, Jensen on the square root and the triangle inequality then give advantage at most $\tfrac12\big(\sqrt{a+c}+\sqrt c\big)$ with $a=TC^2\bar\gamma/\sigma^2$ and $c=TC^2/(b\sigma^2)=\mathcal I/2$. Since $\sqrt c\le\sqrt{a+c}$, this is at most $\sqrt{a+c}$, which is the stated bound (proven). The stated form loses a factor of about two in the regime where the memorization term dominates.

Part (b). A change of one record moves $\psi_{B_t}(w)$ by at most $2C/b$ at every $w$ when $i\in B_t$, the Gaussian divergence at that shift is $2C^2/(b^2\sigma^2)$, and the chain rule over the $E_i$ steps gives $\mathrm{KL}(P^S\|P^{S'})\le2E_iC^2/(b^2\sigma^2)$ (proven). Convexity gives $I(z_i;M\mid z_{-i})$ at most the same, and for independent records the chain rule with $I(z_i;M\mid z_{<i})\le I(z_i;M\mid z_{-i})$ gives $I(S;M)\le\sum_iI(z_i;M\mid z_{-i})$. With $\sum_iE_i=Tb$ this is $\mathcal I$ (proven, recomputed). If the schedule is random the bound holds with $\mathbb E[E_i]$, since the coins are independent of $z_i$.

Part (c). $\mathrm{mem}_i\le I(z_i;M\mid u_i,z_{-i})=I(z_i;M\mid z_{-i})-I(u_i;M\mid z_{-i})\le I(z_i;M\mid z_{-i})$, because $u_i$ is a function of $z_i$ (proven, the meditation's one-line argument is right and this is the explicit form).

Status label. Proven is right.

Known or new. Parts (b) and (c) are the Gaussian-mechanism accountant of differentially private stochastic gradient descent, without privacy amplification by subsampling. The per-step quantity $2C^2/(b^2\sigma^2)$ is the zero-concentrated privacy parameter of one Gaussian step at sensitivity $2C/b$, in the sense of Bun and Steinke, TCC 2016, and $\mathrm{KL}\le\rho$ for a $\rho$-zCDP mechanism is the order-one case of their Rényi bound. Abadi et al., CCS 2016, and Mironov, CSF 2017, compute the same composition with amplification (all from memory, unverified). So $\mathrm{mem}_i$ in the honest regime is the per-record privacy budget read in nats, and the meditation should say so. Part (a) is new as a single inequality holding an SQ term and an information budget, and it is a direct consequence of the same null-trajectory computation. That is the meditation's one genuine positive result.

Two points on tightness. First, amplification. If the attacker does not see the batch indices, Poisson subsampling at rate $q=b/n$ lowers each per-step budget by about $q^2$ at large $\sigma$, so the bound of (c) is loose by about $q$ once $E_i\approx Tq$ (heuristic, it assumes the amplification regime of Abadi et al. and hidden batch membership). The meditation's model gives the white-box attacker the coins, so amplification is correctly absent there, and the statement should say which model it is in. Second, the regime. The bound is vacuous from $\mathcal I=2$ on. Every deployed differentially private run has per-record budget $\rho_i$ of order $0.1$ to $1$, so $\mathcal I=\sum_i\rho_i$ is of order $n$ and the two-term filter says nothing about it (empirical, from the reported budgets of the DP-SGD literature, from memory). The meditation's pushback 5 concedes this for real training and should concede it for private training too.

Challenges.

- `ch-two-term-is-dp-accounting`. Name (b) and (c) as the Gaussian accountant without amplification and cite it, so the theory does not present a known composition as new. Does not block.
- `ch-two-term-constant`. Replace $\sqrt{a+c}$ by $\tfrac12(\sqrt{a+c}+\sqrt c)$, which the proof already gives. Does not block.
- `ch-two-term-vacuous-for-dp`. State that $\mathcal I<2$ excludes every deployed private run, so the filter is a theorem about a regime no trainer uses, private or not. Does not block.

### prop-hashed-memory-breaks-sq-filter

Statement true as written. I recomputed every constant.

The family. $dD_v/dD_0-1=(-1)^{y+\langle v,x\rangle}$, so $\chi(D_v,D_{v'})=\mathbf 1\{v=v'\}$, hence $\gamma=0$, $\beta=1$, $\bar\gamma=1/(2^d-1)$ (proven).

Collisions. Pairwise independence gives at most $\binom n2/K\le n^2/(2K)=1/16$ for a hash collision, and $n^22^{-d}$ for two equal inputs (proven).

The rows. Summing $T$ steps, row $h(x_i)$ holds $\gamma_{\mathrm{lr}}\big((T/n)e(z_i)+\sqrt T\sigma G_i\big)$ with $G_i$ standard Gaussian, and with $\sigma^2=T/(16n^2\ln(8n(d+1)))$ one has $\sqrt T\sigma=(T/n)/\sqrt{16\ln(8n(d+1))}$ (proven, recomputed). A sign flips only when $|G|>4\sqrt{\ln(8n(d+1))}$, of probability at most $2(8n(d+1))^{-8}$, and the union over $n(d+1)$ coordinates is $o(1)$ (proven, the margin is very generous). An empty row has squared norm $(T/n)^2\chi^2_{d+1}/(16\ln(8n(d+1)))$ against $(T/n)^2(d+1)$ for an occupied one, so the separation needs $\chi^2_{d+1}$ to exceed about $8\ln(8n(d+1))$ times its mean, of probability $\exp(-\Omega(d\ln d))$, and the union over $K=O(d^2)$ rows is $o(1)$ (proven).

The attacker. The decoded rows give the $2d\times d$ system, which needs no knowledge of $h$. Under $D_v$ it is consistent. Under $D_0$ the matrix has rank below $d$ with probability at most $(2^d-1)2^{-2d}$, and a full-rank system is consistent with probability $2^{-d}$ (proven). Advantage at least $15/16-o(1)$, so at least $3/4$ for large $d$ (proven).

The parameters. $TC^2\bar\gamma/\sigma^2=16n^2(d+1)\ln(8n(d+1))/(2^d-1)=O(d^3\log d\cdot2^{-d})$ and $\mathcal I=32n(d+1)\ln(8n(d+1))=\Theta(d^2\log d)$ (proven, recomputed).

Status label. Proven is right.

Known or new. That a model can store its training set and that no bound on population hardness prevents it is folklore. The explicit parameters are useful for the conjecture of the Next section, and there the construction is not tight. Encode each record with a binary code of constant rate and constant-SNR decodability, $\ell(W,z)=-\langle W_{h(x)},\mathrm{code}(e(z))\rangle$ with code length $p'=O(d)$, so $C^2=p'$. Then $\sigma$ of order $1/n$ suffices for decoding, and $\mathcal I=2TC^2/(b\sigma^2)=\Theta(p'n)=\Theta(d^2)$ (proven given a code with those properties, which random linear codes have, from memory). So the memorization threshold for parity in this model lies at $\Theta(d^2)$ with the constant open, and the meditation's gap "between 2 and $\Theta(d^2\log d)$" is the gap "between $c_1d^2$ and $c_2d^2$" once the lower end is settled. The conjecture `conj-information-memory-parity-bound` is therefore a statement about a constant, and the coding construction gives an upper bound on the constant $c$ it may use, which should be computed before the conjecture is attacked.

Challenges.

- `ch-hash-in-coins`. The loss depends on a hash drawn by the coins, which the setting of `thm-noisy-trainer-two-term-filter` does not allow as written. Fix by letting $\psi$ depend on the coins in both theorems, or by using an exponential table indexed by $x$ itself, which the bound permits because $p$ never enters it. Does not block.
- `ch-coding-tightens-threshold`. Replace $\Theta(d^2\log d)$ by $\Theta(d^2)$ through the coding construction, and state the conjecture with the resulting constant. Does not block.

### prop-output-bounds-do-not-filter

Statement true as written.

Part (a) is immediate. Part (b). The statistic $f$ has sensitivity $1/n$, so Laplace noise of scale $1/(\varepsilon n)$ is $\varepsilon$-differentially private, and the threshold is post-processing (proven). Under $D_v$, $f=1$. Under $D_0$ each count is binomial with mean $n/2$, Hoeffding gives $\Pr[f_v\ge5/8]\le e^{-n/32}$, and the union over $2^d$ vectors is at most $\alpha$ once $n\ge32(d\ln2+\ln(1/\alpha))$ (proven, recomputed). The noise exceeds $3/16$ in a fixed direction with probability $\tfrac12e^{-3\varepsilon n/16}$, which is at most $\alpha/2$ once $n\ge16\ln(1/\alpha)/(3\varepsilon)$ (proven, recomputed). The two error rates are at most $3\alpha/2$ and $\alpha/2$, so the advantage is at least $1-2\alpha$ (proven). The SQ bound $q\bar\gamma/\tau^2=q/((2^d-1)\tau^2)$ is the Chebyshev step with the $D_0$ oracle (proven). Part (c) follows.

Status label. Proven is right.

Known or new. Part (b) restates two known facts. Parity is learnable under central differential privacy from $O(d/\varepsilon)$ samples, which is in Kasiviswanathan, Lee, Nissim, Raskhodnikova and Smith, FOCS 2008, the library key `KLNRS08`, whose note is unfilled, so I cannot give the theorem number. And central differential privacy never hides a population fact, which is the design of the notion. Part (c) is the correct conclusion that none of entropy, mutual information or central privacy loss of the output composes with an SQ bound, and `fact-ldp-equals-sq` is the right pointer for what does compose, local randomizers.

On the framing. The meditation calls this its first and negative finding and says it refutes the slogan. The slogan in `readings/2026-10-27-what-you-want.md` reads "what the trainer did not learn can stay pseudorandom to every attacker", and its natural reading is about the trainer's class, not about the output. The proposition refutes the output reading, which no file defended, and confirms the class reading. It is a clarification of a quantifier, which is worth one sentence and not a finding.

Challenges.

- `ch-slogan-strawman`. Present the proposition as fixing the quantifier of the slogan, not as refuting it. Does not block.
- `ch-klnrs-theorem-number`. Fill the `KLNRS08` note and cite the parity learner by theorem number before the proposition enters the booklet. Does not block.

## The meditation as a whole

### Does the direction serve Halil's aim

Halil's words set two targets. The first is "a bound on success of such a VAE (or anything) given the setting", stated through "the flow of information". The second is prices "in the units of learning", with "attacks on learning algorithms come from other learning algorithms" fixing the attacker class.

The meditation serves the first target and not the second. Every bound it proves holds for every attacker, unbounded and white-box, because the restriction sits on the trainer. A bound on every attacker is a bound on a VAE, and the exposure lemma makes it a bound on list-decoding success in terms of information flow. That is the first target met, in the regime where the trainer is noisy enough. The second target is absent. No object in the meditation has an attacker class or an attacker budget. Nothing is priced in samples, runs or queries of a learner. The filter theorems price the trainer's noise, which is the defence side of a same-units statement, and the attack side, what a learning attacker of a named class needs to reach exposure $X$, does not appear. The meditation drifts here from the aim toward the statistical side of `CONTEXT.md` alone (proven, by inspection of the quantifiers of the seven claims).

A second drift concerns the instance. Halil ruled out hardness borrowed by planting. Planted parity is the only instance in the meditation. As a counterexample in `prop-hashed-memory-breaks-sq-filter` and `prop-output-bounds-do-not-filter` it is legitimate, since a counterexample may be anything. As the sole carrier of the Next section it is a planted problem, and the memorization threshold the meditation wants to prove would be a theorem about parity and not about a data law. The frame's parameter $\bar\gamma$ admits approximate structure, as the meditation says, and no claim uses that admission.

On the constraints of `CONTEXT.md`. No cryptographic plug-in appears. The random oracle is a uniform variable per index and is used as a reference, not as an assumption. The canary obeys the programming rule of 2026-10-27, and the meditation correctly derives that the literature's canaries do not. Measurability holds for $T$, $C$, $b$, $\sigma$, $\mathcal I$, the exposure and the coupled tail, and fails for $\mathrm{mem}_i$ itself, which is reached only through its two bands. The null trajectory is clean mathematics. The split and the canary proposition are bookkeeping.

### The strongest idea

The null trajectory. It is a two-line device, it removes adaptivity without fresh samples, it makes reuse free, and it gives the only inequality in the theory so far in which a population price and an information budget appear side by side. Its part (b) is the sharpest sentence in the meditation, because it shows that the model behind `fact-sq-simulates-minibatch-sgd` cannot state memorization, which corrects a clause of item 21 that the theory would otherwise have carried into the booklet (proven, part (b) of `thm-null-trajectory-filter`). Second to it is part (b) of `lem-exposure-information-sandwich`, which turns the mean exposure, the number experiments report, into a lower band on information at a slack of $\ln(1+\ln N)$.

### What should be dropped

The random-oracle dressing of the split, which the meditation itself says adds nothing. The canary proposition as a standalone object, which should become a remark under the admissibility rule. The framing of `prop-output-bounds-do-not-filter` as a refutation. The phrase robust advantage, for the reason given under `ch-robust-is-defender-best`.

### What the meditation missed

1. The composition Halil asked for. The meditation holds three pieces and never joins them. From `lem-exposure-information-sandwich` (a), the link $I(\kappa;V)\le\mathrm{mem}_c$, and `thm-noisy-trainer-two-term-filter` (c), every attacker of a noisy trainer satisfies
$$\mathrm{kl}\big(p_k\,\|\,k/N\big)\le\frac{2E_cC^2}{b^2\sigma^2},$$
and so $p_k\le\big(2E_cC^2/(b^2\sigma^2)+\ln2\big)/\ln(N/k)$ (proven, by chaining the three). This is a bound on the list-decoding success of a VAE, or anything, given the setting, in measurable hyperparameters, with no hypothesis on the attacker. It is the one sentence that answers Halil's first target in the noisy regime. It is also differential-privacy auditing with the privacy parameter replaced by its Kullback form, and it should be presented as that.

2. The literature on the information needed for parity. The conjecture of the Next section is an information form of a memory bound. Steinhardt, Valiant and Wager, COLT 2016, bound the communication per sample needed to learn parity. Dagan and Shamir, COLT 2018, prove $\Omega(d^2)$ bits of memory or communication for detecting a correlation, which is the detection form the conjecture needs. Garg, Raz and Tal, STOC 2018, give the extractor framework (all from memory, unverified, none in the library). The search gate of `sink/formalizing/README.md` applies before the conjecture is attacked.

3. The verdict trainer bounds the conjecture's form. A trainer that outputs the consistency verdict has $I(S;M)\le\ln2$ and advantage near one, by the meditation's own part (a) of `prop-output-bounds-do-not-filter`. So no statement of the form "$I(S;M)\le cd^2$ implies no attacker wins" can be true for general trainers (proven). The conjecture must be about the noisy-gradient channel, and the question it asks is whether that channel forces $\Omega(d^2)$ nats of trajectory information to compute a one-bit verdict. The meditation states the conjecture for noisy SGD, which is the right scope, and should say why the scope cannot be widened.

4. The coding construction under `ch-coding-tightens-threshold`, which places the threshold at $\Theta(d^2)$ and makes the conjecture a statement about a constant.

5. The equivalence of (b) and (c) of the two-term theorem with the Gaussian accountant, under `ch-two-term-is-dp-accounting`, and the consequence that the honest filter is vacuous for every deployed private run as well as for every non-private one.

6. The canary mismatch under `ch-literature-canaries-inadmissible`. The frame's canary is an honest record whose individual part the designer records, and no published exposure measures it. The first experiment of the frame would have to be designed from scratch, which the meditation should say.

7. The ambiguity of the statistic under `ch-canonical-statistic-ambiguous`, which decides whether reconstruction of a training image counts as memorization at all.

### The honest answer to the council's question

No composition theorem makes a memorizing trainer a filter. For a trainer whose channel from the sample to its trajectory carries at most about two nats, the two-term filter holds and binds every attacker. For every trainer anyone runs, that budget is exceeded by orders of magnitude, and the frame leaves one quantity, the per-record information $\mathrm{mem}_i$, with exposure as its lower band at one run and twins as its upper band at about $700$ runs per record by `thm-exact-twin-price`. The split prices memorization in nats and not in learning units. Canaries measure a lower band on it, and only for canaries that are honest draws, which none in the literature are. The meditation reaches each of these conclusions and should state them as its opening paragraph.

## Challenges

| Challenge | Blocks |
| --- | --- |
| `ch-canonical-statistic-ambiguous` | no |
| `ch-random-oracle-wrapper` | no |
| `ch-part-c-hypothesis` | no |
| `ch-finite-uniform-hypothesis` | no |
| `ch-literature-canaries-inadmissible` | no |
| `ch-extra-record-changes-n` | no |
| `ch-exposure-upper-band-deterministic-only` | no |
| `ch-sandwich-missing-link` | no |
| `ch-ranking-ties` | no |
| `ch-robust-is-defender-best` | no |
| `ch-rule-knows-secret` | no |
| `ch-coin-dependent-loss` | no |
| `ch-two-term-is-dp-accounting` | no |
| `ch-two-term-constant` | no |
| `ch-two-term-vacuous-for-dp` | no |
| `ch-hash-in-coins` | no |
| `ch-coding-tightens-threshold` | no |
| `ch-slogan-strawman` | no |
| `ch-klnrs-theorem-number` | no |

## Verdicts

```text
VERDICT def-random-oracle-record-split REVISE
VERDICT prop-canary-is-programmed-record REVISE
VERDICT lem-exposure-information-sandwich REVISE
VERDICT thm-null-trajectory-filter ACCEPT
VERDICT thm-noisy-trainer-two-term-filter ACCEPT
VERDICT prop-hashed-memory-breaks-sq-filter ACCEPT
VERDICT prop-output-bounds-do-not-filter ACCEPT
BLOCKING 0
```
