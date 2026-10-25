# Round 03, challenger

Verdict of this turn. Eleven of the twelve round-02 challenges are fixed, and ch-symbol-clash is reopened because the new text brings back eight clashes. I checked every new or rewritten proof step by step. They are the state-chain rewrite of [thm-dataflow-composition] (b), the reverse-order bound, (a)(ii) and (a)(iii), [lem-needle-lower-bound], [thm-active-choice-dichotomy] and [thm-record-level-certificate]. I found no error in a proof step. I found one gap in a definition, and it makes a stated result false. [def-isolated-client] never says that the input node holding $D_j$ is hidden from the coalition. A procedure that releases that node through the plain channel meets conditions 1 to 4, and [thm-dataflow-composition] (b) fails for it. The fix is one clause, and it is the only blocking challenge (ch-dataset-node-channel). Two sentences outside the theorem statements claim more than the proofs give, and one bound is loose. The register says that the worst admissible strategy against a stateless client is non-adaptive. That is false for the divergence, and a three-line counterexample below shows it. The equality holds for the exceedance term only (ch-adaptivity-scope). The tree certificate pays a factor $e^\varepsilon$ in the reverse order that it does not need (ch-tree-symmetry). The Reading of the scalar attack (a)(iii) applies it to CKKS, whose ciphertext modulus rules out its hypothesis, every $a\ge1$. A finite-$a$ form fixes it (ch-finite-scalar-attack). [thm-active-choice-dichotomy] and [thm-record-level-certificate] earn NONTRIVIAL. In both, criterion 4 is inherited from [thm-dataflow-composition] (e)(i), which the bar allows. Dropping invert is acceptable if the final document states the one-line reduction below and leaves model extraction out of scope (ch-invert-remark). Steering sets one problem, which closes open problem 5 in the direction its stated obstacle denies. The remaining rounds should harden and consolidate.

Every non-trivial claim carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the idea is written here and the builder must write it out. Notation follows `theory/CURRENT.md`. I opened no outside source this round. One standard fact used below, the concentration of the Gaussian norm, $\Pr[\|g\|>\sqrt d+u]\le e^{-u^2/2}$ for $g\sim\mathcal N(0,I_d)$, is cited from memory.

## Status of the round-02 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-stateful-client | not blocking | fixed | none in the state chain. The rewrite exposed an older gap, ch-dataset-node-channel |
| ch-realization-scope | not blocking | fixed | the four clauses are in (a)(i). (a)(ii) adds an interactive notion. (a)(iii) needs a finite-$a$ form, ch-finite-scalar-attack |
| ch-per-pair-scope | not blocking | fixed | none |
| ch-separation-regime | not blocking | fixed | none |
| ch-dkw-atoms | not blocking | fixed | none. The quantile clause is correct |
| ch-estimator-dimension | not blocking | fixed | none. I checked the projection and the Chebyshev term |
| ch-replay-deterministic-match | not blocking | fixed | none. The constant $2/(1-e^{-1})<3.2$ is correct for $q_R\ge1$ |
| ch-oblivious-prover-scope | not blocking | fixed | the corrected statement of (e) still writes $r$ for the number of replays, which the table renames $n_{\mathrm{rep}}$ |
| ch-passive-queries | not blocking | fixed | none |
| ch-definition-simplify | not blocking | fixed | none |
| ch-symbol-clash | not blocking | reopened | the table exists, and the round-03 text breaks it in eight places |
| ch-prior-work-quotes | not blocking | fixed | open problem 2(i) quotes my round-02 lower bound, which no builder file has proven |

Detail on two rows. For ch-dkw-atoms, the identity $\{F^-(V)\le x\}=\{V\le F(x)\}$ holds for every right-continuous nondecreasing $F$, and the rest of the clause follows (proven). For ch-estimator-dimension, $\hat h_b(y)=\frac1n\sum_k\psi(y,X^b_k)$ with $\psi(y,x)=\exp(\langle y,x\rangle/\sigma^2-\|x\|^2/(2\sigma^2))$ depends on $y$ only through $\Pi_Vy$. The integrand lies in $[0,\hat h_0(Y)]$, its second moment is at most $e^{B^2/\sigma^2}$, and Chebyshev gives the stated term (proven).

## Definitions

### [def-learning-oracle]

Well posed (proven, by inspection). Train now says that a seed passed by value or by name is the seed the run uses, which round 02 asked for. The remarks hold the idealizations and nothing in the definition depends on them. ACCEPT.

### [def-learning-oracle-model]

Well posed (proven, by inspection). Passive is now defined by the choices that enter procedure nodes. No theorem needs more. The impossibility pattern of the remark now allows a stated procedure, and the three lower bounds of this round use that allowance (answer to question 2 below).

The cut of invert. The adversary-interface report (`lib/reports/src/2026-10-16-halil-adversary-interface.tex`, the list of games and the FedAvg section) uses invert for record reconstruction, gradient inversion and model extraction. Dropping the goal from the definitions loses no theorem, since none uses it. The final document should still say what the theorems give for inversion. For a dataset target, the theory covers invert through one inequality (proven, by the definition of $\mathrm H_\gamma$). Let $B$ be any measurable set of views, for instance the views from which the adversary's guess lies within a tolerance of the record that $H_1$ removes. Then

$$P_0(B)\le e^{\varepsilon}P_1(B)+\mathrm H_{e^\varepsilon}(P_0\|P_1).$$

So every bound of the theory bounds the success of inversion under $H_0$ by $e^\varepsilon$ times the success under $H_1$, where the target is absent, plus the bound. Averaged over records, [thm-record-level-certificate] (a) gives $\frac1{|D|}\sum_i\mathrm H^{\to}_i(\varepsilon)\le\delta_R(\varepsilon)+\bar\epsilon+F^{\to}(\varepsilon,\bar\epsilon)$, since every $\mathrm H^{\to}_i$ is at most one (proven). That turns the fraction certificate into a bound on the average reconstruction advantage over the records of $D$. Model extraction targets the model and has no pair of hypotheses, so no theorem covers it. Stating this in one remark is enough (ch-invert-remark). ACCEPT.

### [def-degenerate-oracles]

Well posed. The remark records the orchestrator's ruling, and item 3 now has standing. ACCEPT.

### [def-certifier]

Well posed. The functional target covers $\theta^{\mathrm{act}}_{\mathcal C}$, $\theta^{\mathrm{agg}}$, $\theta^{\max}$, $\theta^+$ and $\theta^{\mathrm{frac}}$, all used this round. One remark, not blocking. [thm-record-level-certificate] (a) certifies a family of targets indexed by $(\varepsilon,\bar\epsilon)$ on one event, which is more than soundness for one target. The theorem states the simultaneity itself, so the definition need not change. ACCEPT.

### [def-model-bank]

Well posed. The twin-augmented bank of [thm-record-level-certificate] (d) passes seed names, which the empirical oracle refuses. Its proof routes the bank through a coupled design, which lists every seed as a fixed value, so lem-bank-fidelity applies (proven, by inspection). ACCEPT.

### [def-isolated-client]

The state chain, the stop, the twin with its own chain and the coupled tail are well formed. I checked the subscripts of $\beta_t$ against the twin in $\mathsf{Ex}_0$ and in $\mathsf{Ex}_1$. They match, with the states exchanged in $\mathsf{Ex}_1$. The remark on passive strategies is correct, since a prescribed choice is a function of procedure values and not of revealed seeds.

The gap. Under [def-learning-oracle-model] the dataset $D_j$ is the value of an input node, because $x_v$ is formed from parent values and choices. Conditions 1 to 4 constrain who reads that node and how $v_t$ reaches the coalition. No condition constrains the channel through which the input node itself reaches the coalition. Counterexample (proven). Take $R=1$, a learning function that ignores the dataset, and a procedure that releases the input node of $D_j$ through the plain channel. Conditions 1 to 4 hold, $\epsilon_0(\Delta)=0$ for every $\Delta$, and the bound of (b) tends to zero as $\Delta\to0$. The view contains $D_j$, so $\mathrm H_\gamma(P_0\|P_1)=1$. The proof of (b) fails at its step 1, which claims that every node other than the $v_t$ and the $r_t$ has a value free of $b$. The input node of $D_j$ is such a node. The round-02 setting had the same gap, and I missed it then. REVISE, with the one-clause fix of ch-dataset-node-channel. The three theorems that use the definition stand once the clause is added, and their proofs need one word in step 1.

Simplicity. The per-round thresholds and the remark on the experimenter could move to [thm-dataflow-composition]. Not blocking.

## Proofs

### Needle lower bound [lem-needle-lower-bound]

Claim. A certifier sound over a class that contains $K$ functions, each differing from a reference function only on its own set of training inputs and each with target at least $\vartheta$, outputs at least $\vartheta$ at the reference with probability at least $1-\alpha-N/K$.

Check (proven). The two runs share coins and the triple of each call. Names are call counts, so equal transcripts give equal stores. A Train call outside $X_k$, an Eval call and an Open call get equal answers. The runs agree up to the first Train call in $X_k$, which is the same call in both. The counting $\sum_k\mathbf 1[\mathrm{Hit}_k]\le N$ uses that the sets are disjoint and that each call names one input. A seed passed by value, a refused call and an Eval at a needle model after the hit all fall under the induction. The reference function need not be in the class, and the statement does not ask for it.

Weakest step. None of substance. The lemma is the adversary argument of query complexity, and the builder claims no novelty.

Non-triviality. Not claimed and not met. Criterion 4 fails, since the lemma holds in both disciplines. ACCEPT.

### Dataflow composition, revised [thm-dataflow-composition]

Claim. As in round 02, now for clients with state and a stop, in both orders of the hockey-stick divergence, with ciphertext reductions for following and deviating coalitions and an attack on unverified decryption.

Part (b), step 1 (proven, given ch-dataset-node-channel). The maps $\chi_t,o_t,\mathrm{st}_t,\Psi$ exist. Under the seed-revealing policy the adversary may recompute the whole chain under deterministic kernels, because it holds $w_0$ and every revealed seed. Its answers are still functions of $\omega$ and $\bar\rho_{\le t}$, which is all the claim needs. The new children of $v_t$ are $r_t$ and $v_{t+1}$, both outside the coalition.

Steps 2 and 3 (proven). The hybrid carries both chains along its own trajectory. Until the first exceedance its second chain is the twin chain of $\mathsf{Ex}_0$, and the induction carries $\tilde c_t=c_t$, $\tilde W^0_t=W_t$, $\tilde W^1_t=W'_t$ and the stop together. At $t^\star$ both chains agree up to round $t^\star-1$, so $\tilde d_{t^\star}=d_{t^\star}$. The sum bound needs $c_t$, $W_{t-1}$, $W'_{t-1}$ and the event that round $t$ runs to be $\mathcal F_t$-measurable, and they are.

Step 4 (proven). Given $g_t\sim\mathcal N(a,1)$ the release is $\mathcal N(O_t+F^1_t,\sigma^2I_d)$ whatever $s_t$ and $\mathbf n_t$ are. So the conditional law of the outputs given both chains involves only the $D^1_j$ chain, which the kernel extends as the $H_1$ execution does. Marginalizing the auxiliary chain gives $L_1$. Given $g_t\sim\mathcal N(0,1)$ the mean is $O_t+F^1_t-c'_t$, the hybrid release. Both orders of (G1) hold, since the reflection $y\mapsto s-y$ exchanges $\mathcal N(0,1)$ and $\mathcal N(s,1)$.

Step 5 and the reverse order (proven). (F1) is the identity $Q(B)-\gamma P(B)=(Q(B)-\gamma M(B))+\gamma(M(B)-P(B))$. For the term $\gamma\epsilon_1$ in the first order, the hybrid built around $H_1$ releases $O_t+F^0_t+\mathrm{clip}_\Delta(F^1_t-F^0_t)+Z_t$. The kernel with $c'_t=-\mathrm{clip}_\Delta(F^1_t-F^0_t)$ maps $\mathcal N(a\mathbf 1,I_R)$ to $L_0$ and $\mathcal N(0,I_R)$ to that hybrid, so $\mathrm H_\gamma(L_0\|L^{(1)}_{\mathrm{hyb}})\le\delta_{\mathcal N}(\varepsilon;\sqrt Ra)$. (F1) then gives $\mathrm H_\gamma(L_0\|L_1)\le\delta_{\mathcal N}+\gamma\epsilon_1$. Sharpness of the factor is checked under [thm-record-level-certificate] (b)(ii).

Weakest step of (b). Step 1, as in round 02. It carries the isolation hypothesis, and it is where the dataset-node gap sits.

Part (c) (proven). The experimenter holds both states with label open and forms both training inputs. The stopping variant is a pointwise comparison on the space of step 1, so $\epsilon_0$ of a stopping strategy is at most that of the protocol's strategy.

Part (a)(i) (proven, given $\epsilon_\Sigma$). The four clauses are in place, and the proof uses each of them.

Part (a)(ii) (proven, given $\epsilon^{\mathrm{dev}}_\Sigma$). I checked the four conditions for $G^{\mathrm{dev}}_{\mathrm{rel}}$ and the order $a_{t,i}\prec r_t\prec\tilde r_t$, which matches the order in which $\mathcal F^{\mathrm{dev}}$ takes inputs, releases $y_t$ and delivers. The environment runs the oracle simulator and needs $D^b_j$, which it holds. Two remarks, neither blocking. First, $\mathcal F^{\mathrm{dev}}$ delivers one value to every honest party, so a realization needs agreement among the honest parties, which is a sixth item for the heuristic list. Second, $\mathcal S$ needs the coalition's keys, and the statement should say that $\mathcal S$ simulates the key setup. Weakest step. The identity between the run of $\mathcal Z_b$ with $(\mathcal F^{\mathrm{dev}},\mathcal S)$ and the run of $\mathcal A'$, which holds only if $\mathcal S$ submits all coalition inputs before $y_t$ exists. $\mathcal F^{\mathrm{dev}}$ enforces that order, so the identity holds.

Part (a)(iii) (proven, under its hypothesis). Data processing to $y^{(a)}/a$, almost sure convergence to $\tilde u$, and (F5) give the limit. I checked (F5). The function $g$ is continuous because $F$ and $V^c$ are disjoint closed sets, and $\lvert g-\mathbf 1_B\rvert\le\mathbf 1_{V\setminus F}$ gives the slack $\gamma\lambda$. The hypothesis "for every public scalar $a\ge1$" is never met by CKKS. Decryption works modulo the current ciphertext modulus $q_\ell$, so $a$ times the scaled message wraps once $a$ exceeds about $q_\ell/(2\,\mathrm{scale}\,\lVert\tilde u\rVert_\infty)$ (heuristic, a statement about the scheme). The limit is then not available, and the Reading of (a)(iii) applies the statement outside its hypothesis. A finite-$a$ statement removes the limit, (F5) and the modulus problem together (ch-finite-scalar-attack). Let $\tilde u$ take the value $\tilde u_b$ under $H_b$, with $\ell=\lVert\tilde u_1-\tilde u_0\rVert>0$ and $\mathbf n=(\tilde u_1-\tilde u_0)/\ell$. The test $B=\{\langle y^{(a)}-a\tilde u_0,\mathbf n\rangle\le a\ell/2\}$ gives, for every $a$ with $a\ell>2e_{\max}$,

$$\mathrm H_\gamma\big(P^{(a)}_0\|P^{(a)}_1\big)\ge1-(1+\gamma)\,\bar\Phi\Big(\frac{a\ell/2-e_{\max}}{\sigma}\Big)$$

(proven, since $\lvert\langle e^{(a)},\mathbf n\rangle\rvert\le e_{\max}$ and $\langle Z_1,\mathbf n\rangle\sim\mathcal N(0,\sigma^2)$ under both hypotheses). With the largest $a$ the modulus allows, the noise that protects client $j$ has scale $\sigma/a$. The proven content of (a)(iii) survives in this form.

Part (d) (proven). (d)(ii) is now an instance of [lem-needle-lower-bound] with one-point sets.

Non-triviality, re-confirmed. The proof of (b) changed and the tag rests on the same facts as in round 02. Criteria 1 to 3 hold, and criterion 4 holds through (c) against (e)(i) under item 3 of [def-degenerate-oracles]. ACCEPT NONTRIVIAL, with ch-dataset-node-channel and ch-finite-scalar-attack due.

### Active-choice dichotomy [thm-active-choice-dichotomy]

Claim. Against a stateless client the worst exceedance term over admissible strategies is a product of per-round worst tails, attained by non-adaptive strategies. Against a client with state the tree execution bounds every admissible strategy. Certifying either costs Train calls linear in the distinct choices or in the choice sequences, and this is optimal at a reference function. An infinite set, or a choice through the aggregate, makes the cost infinite.

Part (a)(i) (proven). The upper bound uses $\Pr[E_t\mid\mathcal F_t]\le\bar\beta_t(\Delta)$ on the event that round $t$ runs, and $\Pr[E^c_t\mid\mathcal F_t]=1$ off it. $G_{t-1}$ is $\mathcal F_t$-measurable because $E_s$ is a function of $c_s$, $\zeta_s$ and the event that round $s$ runs. The lower bound uses independent $\zeta_t$ under a fixed sequence. The statement for $\epsilon_1$ holds because the pair $(\mathsf L(x(c,D^1_j);\rho,\xi^1),\mathsf L(x(c,D^0_j);\rho,\xi^0))$ has the same law as in $\mathsf{Ex}_0$ after relabelling the two independent draws of hardware randomness.

What (a)(i) does not say. The equality concerns the exceedance term only. The register and the opening of the builder's file say that the worst admissible strategy against a stateless client is non-adaptive. For the divergence that is false (proven, by computation). Take $\varepsilon=0$, so $\mathrm H_1=\mathrm{TV}$, the realizable policy, $R=2$, $\mathcal C_1=\{c_1\}$ and $\mathcal C_2=\{c_X,c_Y\}$. Choose the learning function and identity release maps so that, with the release noise negligible against the separation of the supports, the first release takes two values $a$ and $b$ with probabilities $(0.6,0.4)$ under $H_0$ and $(0.4,0.6)$ under $H_1$. Under $c_X$ the second release is $0$ under $H_0$, and $0$ or $v$ with probability one half each under $H_1$. Under $c_Y$ the roles of the hypotheses are exchanged. Writing $\mathrm{TV}=\sum_{y_1,y_2}(P_0(y_1)M^0(y_2)-P_1(y_1)M^1(y_2))_+$, the non-adaptive strategies give $0.5$ each, and a strategy that randomizes with coins in the view gives at most $0.5$. The adaptive strategy that plays $c_X$ after $a$ and $c_Y$ after $b$ gives $0.4+0.2=0.6$. Releases with Gaussian noise attain values arbitrarily close to these as the supports separate. Adaptivity buys nothing in the bound and can buy something in the divergence (ch-adaptivity-scope).

Part (a)(ii) (proven). The prefix used in round $t$ has length $t$ and is a function of $\omega$, $Z_{<t}$ and the triples at prefixes used before. Lazy sampling gives the triple at the new prefix its law independently of the past, which is the conditional law of $\zeta_t$ in step 1. The chain and the twin are the tree values at the prefix, so $D^\star_0\le D^{\mathbb T}$ pointwise.

The reverse order of (a)(ii) needs no factor $e^\varepsilon$ (proven). The same tree embeds $\mathsf{Ex}_1$. Along the $H_1$ trajectory set $\xi^1_t=\xi'_{\mathbf c_{\le t}}$ for the base and $\xi^0_t=\xi_{\mathbf c_{\le t}}$ for the twin. The base chain of $\mathsf{Ex}_1$ is then $W'_{\mathbf c_{\le t}}$ and its twin is $W_{\mathbf c_{\le t}}$, by the same induction. So $D^\star_1\le D^{\mathbb T}$ pointwise, $\epsilon_1(\Delta)\le\epsilon^{\mathbb T}(\Delta)$, and [thm-dataflow-composition] (b) gives $\theta^{\mathrm{act},\leftarrow}_{\mathcal C}\le\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon^{\mathbb T}(\Delta)$. The output $\delta_{\mathcal N}+\gamma\bar p$ of (b)(ii) for the reverse target can be replaced by $\delta_{\mathcal N}+\bar p$. The shared base of [thm-record-level-certificate] does not have this symmetry, because its base is $H_0$ for every record, which is why the factor is sharp there (ch-tree-symmetry).

Part (b) (proven). Union bound over $K=\sum_t\lvert\mathcal C_t\rvert$ pairs $(t,c)$, monotonicity of $x\mapsto1-\prod_t(1-x_t)$, and $1-(\alpha/K)^{1/n}\le\ln(K/\alpha)/n$. One sample at $c$ serves every round with $c\in\mathcal C_t$, since the union bound needs no independence.

Part (c) (proven). At $\mathsf L^\circ$ every release is $Z_t$, and $(\omega,y,\bar\rho)$ has one law under both hypotheses. The seed-revealing adversary learns nothing from $\bar\rho_t$ at $\mathsf L^\circ$, since every run returns the starting model. The needles for (i) are one-point sets, which are disjoint because $x$ is injective in $c$. For (ii), the state records the choice history, so $x_{\mathbf c}$ is reached in round $R$ under $H_1$ only along $\mathbf c$, and the points $x_{\mathbf c}$ are distinct. Data processing to the shifted coordinate gives $\delta_{\mathcal N}(\varepsilon;L/\sigma)$.

Part (d) (proven). $\Pr[\lVert Z\rVert>r]\le\eta/2$ by Markov, the balls around $\mathbf p_k=4kr\,e_1$ are disjoint and miss $c_1=0$, and (F2) with $y_1$ as the common coordinate gives $\Pr[\lVert Z_1\rVert<r]\,\delta_{\mathcal N}(\varepsilon;L/\sigma)$. In the bounded variant the packing count $J'(2r)^d\ge B_A^d$ and the removal of the one ball that may contain the origin are correct. One remark, not blocking. With release maps clipped at $B$, as in DP-FedAvg, the needle shift is at most $B$, and the lower bound becomes $\Pr[\hat t\ge(1-\eta/2)\,\delta_{\mathcal N}(\varepsilon;B/\sigma)]\ge1-\alpha-N/J$. The problem under Steering needs this form.

The corollary (proven). The constant $\lvert\mathbb T\rvert\le2\prod_t\lvert\mathcal C_t\rvert$ holds when every $\lvert\mathcal C_t\rvert\ge2$.

"Application to the aggregation sub-protocol". Correct as an instance (proven). The sentence "verifiable aggregation is therefore exactly what collapses the admissible set" claims more than the proof gives. The proof shows that output substitution makes certification impossible and that abort with prescribed inputs keeps it possible. "Exactly" needs a converse, and none is proven. Replace it by those two facts.

Weakest step. The embedding of (a)(ii). Lazy sampling over a table indexed by prefixes is correct, but only because a prefix of length $t$ is first used in round $t$. A procedure in which one learning node runs twice in a round, or in which the coalition can repeat a prefix through a stop and a restart, would break it. def-isolated-client excludes both.

Non-triviality. Criterion 1 holds. The tails and the tree execution are defined by Train calls that reuse a seed name. Criterion 2 holds. A bound over adaptive strategies without the oracle needs the law of the trained model at every admissible training input and, with state, at every admissible history. Criterion 3 holds. (a) and (b) hold for every learning function and depend on it only through $\bar\beta_t$ or $\epsilon^{\mathbb T}$. Criterion 4 holds through (b) under item 3 of [def-degenerate-oracles], by the instance $R=1$, $\lvert\mathcal C_1\rvert=1$, where (e)(i) of [thm-dataflow-composition] defeats every drawn-seed certifier. The criterion-4 content is inherited, and the new content, the tree embedding and the matching lower bounds, holds in both disciplines. The final document should say so. ACCEPT NONTRIVIAL, with ch-adaptivity-scope and ch-tree-symmetry due.

### Record-level certificate [thm-record-level-certificate]

Claim. One shared base execution with $m$ twins certifies, for every learning function, the fraction of records of a fixed dataset whose divergence exceeds the Gaussian term plus a threshold, in both orders. The reverse order pays a sharp factor $e^\varepsilon$. All records cost calls linear in their distinct values, records outside the dataset cannot be certified, a twin-augmented bank brackets the random-subset game, and drawn seeds fail.

Part (a) (proven). Given $I$, the base with twin $k$ is $\mathsf{Ex}_0$ for pair $i_k$, and the other twins drop out because they use independent hardware randomness and no node reads them. The Clopper and Pearson union bound gives $E_1$ given $I$. The values $\epsilon^{i_k}_0$ are i.i.d. draws from a law with atoms, and DKW with the quantile clause gives $E_2$. On $E_1\cap E_2$ every counted record has $\epsilon^i_0(\Delta)>\bar\epsilon$, in the reverse order because $e^\varepsilon\epsilon^i_0>e^\varepsilon\bar\epsilon$ is the same inequality. Neither event depends on $(\varepsilon,\bar\epsilon)$, so the bound is simultaneous. Indices drawn twice get two twins, which is harmless. The two-sided DKW constant 2 is used where the one-sided form would do, and Massart's paper was not opened (from memory, with a search summary).

Dependence between twins of one run. They share $\rho_t$, the base chain and the trajectory, so they are dependent. No step uses independence across $k$. $E_1$ uses a union bound, and $E_2$ concerns the sampling of indices, which is independent of the runs. The claim of round 02 stands (proven).

Part (b)(i) (proven). [thm-dataflow-composition] (b).

Part (b)(ii), sharpness (proven). I recomputed the instance. Along $H_0$, round 1 has difference $\Delta_1$, which does not exceed $\Delta_1$, and round 2 exceeds exactly when $Z_1>\tau$, so $\epsilon_0=\bar\Phi(\tau)$. The set $B=\{y_1>\tau,\ y_2>L/2\}$ gives $\bar\Phi(\tau-\Delta_1)\Phi(L/2)-\gamma\bar\Phi(\tau)\bar\Phi(L/2)$. The Mills bounds (F4) are correct, including $g'(u)=-2\varphi(u)/(1+u^2)^2$. The ratio $\bar\Phi(x-\Delta)/\bar\Phi(x)$ tends to $e^{\varepsilon'}$ with $x=\varepsilon'/\Delta$. The ratio $\delta_{\mathcal N}(\varepsilon;s)/\bar\Phi(x)$ tends to zero because $u^2-x^2$ grows like $(\varepsilon^2\Delta^2/s^2-\varepsilon'^2)/\Delta^2$. I checked the illustration numerically. $\delta_{\mathcal N}(1;\sqrt2)=0.2862$, $\bar\Phi(1)=0.1587$, their sum is $0.4449$, the left side is $0.49999973$, and the bound with factor $e$ is $0.7175$ (computed).

Scope of "sharp". The factor $e^\varepsilon$ is sharp for the bound with a threshold per round. For one threshold the instance gives $C<e^{\varepsilon/\sqrt2}$ at $R=2$. The scalar form of (b)(i), which uses $\delta_R(\varepsilon)=\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$, is still sharp in the supremum over $R$ (proven, sketch). Let rounds $1$ to $R-1$ each shift the release by $\Delta$ under $H_1$, with coupled difference $\Delta$, and let the choice of round $R$ read $S=(R-1)^{-1/2}\sum_{t<R}y_t/\sigma$ against $\tau$. Under $H_1$, $S\sim\mathcal N(\sqrt{R-1}\,\Delta/\sigma,1)$. The computation of (b)(ii) with $\Delta'=\sqrt{R-1}\,\Delta/\sigma$ in place of $\Delta_1$, and $s=\sqrt{R/(R-1)}\,\Delta'$, gives every $C<e^{\varepsilon\sqrt{(R-1)/R}}$. Letting $R$ grow reaches every $C<e^\varepsilon$. One sentence should say so (ch-scalar-sharpness).

Part (b)(iii) (proven). Counting.

Part (c) (proven). Equal values give equal $D^{-i}$, so $n'$ twins suffice. The needles are one-point sets at distinct datasets, and (G1) is symmetric for the other order. For records outside $D$, $D\cup\{z\}$ is distinct for distinct $z$ as a multiset.

Part (d), the bracket (proven). Bernoulli inclusion at rate one half, the law of [thm-bank-soundness], makes $S_l$ given $i\notin S_l$ a rate-one-half subset of the other records, which is the law of $S$ in $G^{\mathrm{rs}}_i$. So the left inequality is the test fact and the mixture inequality, and the right one is [thm-coupling-certificate] (b) at $\gamma=1$ with one-sided Hoeffding given the pattern. The bracket would fail for a bank that draws exact halves, since then $S_l$ given $i\in S_l$ and given $i\notin S_l$ have different sizes. The statement inherits the Bernoulli law from the bank and should say so in one clause. Weakest step. The bracket compares $\hat A_i(\tau)$, an estimate on the base runs, with an upper bound on the same runs and their twins. The two error events are separate, so the bracket holds with probability $1-3\alpha$ when both are wanted, and the Reading of (d) should state that level.

Part (e) (proven). At $\mathsf L^\circ$ the model ignores the dataset, so every coupled pair coincides and $\theta^{\mathrm{frac}}=0$. Under $\mathsf L_\varsigma$ every input $x(c_1,D')$ with $D'\neq D$ has the same deterministic model as a function of the seed. So one sequence $Y_1$ answers all of them, and the transcript is $\Psi(Y_0,Y_1,W)$. Under $\mathsf L^\circ$ both sequences are i.i.d. uniform over index and sign. Under the mixture over $\varsigma$, given distinct indices, the signs are i.i.d. uniform. So the distance is at most $N(2N-1)/K$.

Non-triviality. Criteria 1 to 3 hold as the builder states. The shared base needs a seed name reused across $m+1$ calls per round, and the bound depends on $\mathsf L$ only through $\epsilon^i_0$. Criterion 4 holds through (e) under item 3 of [def-degenerate-oracles], at every dataset. The new content is the shared base with its fraction certificate, the sharp reverse factor, the tiers and the bracket. ACCEPT NONTRIVIAL, with ch-scalar-sharpness due.

### Replay-audit steering, corrections [thm-replay-audit-steer]

The deterministic-kernel match is correct (proven). Under deterministic kernels the replays equal the run, the events $F_{k,i}$ coincide, and the stopping prover wins with probability $1-(1-p_\tau(T))^q\ge(1-e^{-1})qp_\tau(T)$ for $qp_\tau(T)\le1$. The closedness of $T$ in a proper metric space gives the nearest point. The widened scope of (e) is correct, since lazy sampling needs only that $U$ is independent of the prover. Non-triviality re-confirmed. ACCEPT NONTRIVIAL.

### Bank soundness, label [thm-bank-soundness]

The first half of the round-01 conjecture, as the builder states it, is proven through [thm-record-level-certificate] (c)(ii). Two remarks, not blocking. The conjecture counted calls per seed, while (c)(ii) bounds the total number of Train calls, so the label should read "total Train calls" (ch-bank-call-count). The lower bound holds in $G^{\mathrm{rec}}$, whose view is a Gaussian release. The fixed game of the bank uses an arbitrary fixed channel, so the transfer holds for that channel only, which the impossibility pattern allows. ACCEPT.

### Coupling certificate and atomless two-point lemma [thm-coupling-certificate] [lem-atomless-two-point]

Paragraph corrections only. The separation-regime sentences and the corrected quotation of Theorem 12 of Gilbert and McMillan, with $e^\varepsilon/2+\delta+\alpha<1$, are correct as I read them in round 02. [thm-coupling-certificate] ACCEPT NONTRIVIAL, re-confirmed. [lem-atomless-two-point] ACCEPT.

## New challenges

### ch-dataset-node-channel

BLOCKING. Targets [def-isolated-client] and step 1 of the proof of [thm-dataflow-composition] (b). The counterexample under Definitions makes (b) false for a procedure that meets conditions 1 to 4. Smallest fix. Add to condition 4 "and the input node that holds $D_j$ is owned by client $j$ and reaches the coalition through channel none". In step 1, write "every node other than the input node of $D_j$, the $v_t$ and the $r_t$". [thm-active-choice-dichotomy] and [thm-record-level-certificate] need no change beyond citing the corrected definition.

### ch-adaptivity-scope

Not blocking, due before the final document. Targets the register line of [thm-active-choice-dichotomy] and the opening of round-03/builder.md. "Against a stateless client the worst admissible strategy is non-adaptive" is false for the divergence, by the counterexample under Proofs. Smallest fix. "Against a stateless client the worst exceedance term over admissible strategies is attained by non-adaptive strategies."

### ch-tree-symmetry

Not blocking. Targets [thm-active-choice-dichotomy] (a)(ii) and (b)(ii). The tree execution embeds $\mathsf{Ex}_1$ as well as $\mathsf{Ex}_0$, so the reverse target needs no factor $e^\varepsilon$. Smallest fix. Replace $\gamma\epsilon^{\mathbb T}$ and $\gamma\bar p$ by $\epsilon^{\mathbb T}$ and $\bar p$, with the two-sentence proof under Proofs. The contrast with the shared base, which needs the factor, is worth one sentence.

### ch-finite-scalar-attack

Not blocking, due before the final document. Targets [thm-dataflow-composition] (a)(iii) and its Reading. CKKS decryption wraps modulo $q_\ell$, so "for every public scalar $a\ge1$" fails, and the limit statement does not apply to the scheme it is meant for. Smallest fix. State the finite-$a$ bound under Proofs, valid for every $a$ with $a\ell>2e_{\max}$. Say in the Reading that the largest admissible $a$ is set by the modulus (heuristic) and that the effective noise scale is $\sigma/a$. (F5) is then no longer needed.

### ch-scalar-sharpness

Not blocking. Targets [thm-record-level-certificate] (b)(ii) and the register line "the reverse order at the sharp factor $e^\varepsilon$". As proven, sharpness holds for thresholds per round, and for one threshold up to $e^{\varepsilon/\sqrt2}$ at $R=2$. Smallest fix. Add the $R$-round variant under Proofs, which makes the factor sharp for one threshold in the supremum over $R$, or restrict the register line to thresholds per round.

### ch-invert-remark

Not blocking, due before the final document. Targets [def-learning-oracle-model]. Smallest fix. One remark after the goals. It states the inequality $P_0(B)\le e^\varepsilon P_1(B)+\mathrm H_{e^\varepsilon}(P_0\|P_1)$ for a win event $B$ of inversion, the average form through [thm-record-level-certificate] (a), and the exclusion of model extraction.

### ch-bank-call-count

Not blocking. Targets the label of [thm-bank-soundness]. Smallest fix. "Proven, the first half of (d) for total Train calls in the procedure $G^{\mathrm{rec}}$."

### ch-symbol-clash

Reopened, not blocking, due before the final document. The table promises one object per symbol, and the round-03 text breaks it in eight places. $K$ is a channel, the number $\sum_t\lvert\mathcal C_t\rvert$, the number of needle sets and the number of code points in (e). $\tau$ is a tolerance, a threshold parameter of $G^{\mathrm{two}}$ and a test. $\lambda$ is a law in (F2), a slack in (a)(i) and in (F5), and a deviation in DKW and Hoeffding. $r$ is a radius and still the number of replays in the corrected statement of (e). $k$ is a needle index, a coalition client, a number of bank runs and a twin index. $g$ is the kernel input, the test function of (F5) and the distance function of (d). $C$ is a constant in (b)(ii) and the number of outputs. $L$ is a needle shift beside $\mathsf L$. $n_G$ is defined for $G_{\mathrm{enc}}$ and reused for per-run calls. Smallest fix. Rename locally in the final document.

### ch-open-problems-exact

Not blocking, due before the final document. Targets the nine open problems of `theory/CURRENT.md`. An open problem can be recorded in a final document only as a question whose answer is yes or no, or as a quantity to determine, with the class of learning functions, the discipline and the accuracy named. My reading of each item follows.

| Item | Exact enough | Smallest fix |
| --- | --- | --- |
| 1, sum channel | no | Ask whether, with the other honest clients isolated and stateless, some functional $\epsilon^\Sigma(\Delta)$ of $\mathsf L$ defined by Train calls satisfies $\mathrm H_\gamma(P_0\|P_1)\le\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon^\Sigma(\Delta)$ for every strategy and is certifiable over every learning function, with $\epsilon^\Sigma<\epsilon_0$ at some learning function |
| 2(i), drawn-seed exponent | yes as a question | the lower bound $e^{c\min(d,B^2/\sigma^2)}$ is my round-02 sketch, unwritten by the builder. Prove it or label it "proven, sketch, challenger round 02" |
| 2(ii), shadow lower bound | almost | name the target rate, $\Omega(C^{q_E}\ln\lvert U\rvert/\epsilon_{\mathrm{acc}}^2)$ Train calls for some family |
| 3, Poisson subsampling | no | the class is undefined, and the builder says the model has none. Define the class or drop the item |
| 4, multi-round drawn seeds | almost | ask for a drawn-seed certifier over $\mathfrak L_B$ with $R$ rounds whose number of Train calls depends on $R$, $B/\sigma$, $\epsilon_{\mathrm{acc}}$ and $\alpha$ and not on $d$ |
| 5, continuous choices | no | the stated obstacle is not the obstacle. See Steering |
| 6, threshold CKKS | almost | name the protocol with its six additions (agreement included) and the claim, realization of $\mathcal F^{\mathrm{dev}}_{\mathrm{abort}}$ under RLWE with negligible $\epsilon^{\mathrm{dev}}_\Sigma$ |
| 7, $\tau$ against $\tau/2$ | almost | ask whether some prover wins with probability at least $c\min\{1,q_Rp_\tau(T)\}$ for a universal $c$ under hardware randomness, or whether some family makes every prover's success $o(q_Rp_\tau(T))$ |
| 8, seed maps | no | define near-optimal, for instance top divergence within $\epsilon'$ of the infimum over seed maps with probability $1-\alpha$, and the class. Over every learning function the answer may already be no by a needle argument (heuristic) |
| 9, $k$-bit seeds | yes | none |

## Steering

The theory is close to complete. It has five definitions accepted twice, a sixth that needs one clause, and six NONTRIVIAL theorems. One gap remains that matters for Halil's procedures and that the existing tools can close. It is the continuous active choice that reaches the client through the aggregate, open problem 5. Its stated obstacle is that Train calls at finitely many points do not bound a coupled tail over a ball. The obstacle does not apply. The target needs only the Gaussian average of the tail, and that average is Lipschitz in the centre. I set one problem and no second one.

### Problem [thm-smoothed-choice-certificate]

Setting. $G^{\mathrm{agg}}_R$ extends $G^{\mathrm{agg}}$ of [thm-active-choice-dichotomy] to $R$ rounds. It has one honest stateless client $j$, an honest server and a coalition client whose inputs satisfy $\lVert u_t\rVert\le B_A$ and may be chosen adaptively. The release maps are $f_t(c,m)=\mathrm{clip}_B(m-c)$, $O_t=u_t$, $c_1$ is fixed and $c_{t+1}=c_t+y_t$. With $Z\sim\mathcal N(0,\sigma^2I_d)$, the smoothed tail of round $t$ is

$$h_t(z)=\mathbb E\,\beta_t(z+Z,\Delta),$$

and for $t\ge2$ let $\varrho_t=(t-1)(B_A+B)+\sigma\sqrt{t-2}\,\big(\sqrt d+\sqrt{2\ln(R/\alpha_{\mathrm{esc}})}\big)$.

(a) Bound (proven, sketch). For every admissible strategy,

$$\epsilon_0(\Delta)\le1-\prod_{t\le R}\big(1-\bar h_t\big)+\alpha_{\mathrm{esc}},\qquad\bar h_1=\beta_1(c_1,\Delta),\quad\bar h_t=\sup_{\lVert z-c_1\rVert\le\varrho_t}h_t(z).$$

Sketch. Let $z_t=c_{t-1}+u_{t-1}+\mathrm{clip}_B(W_{t-1}-c_{t-1})$, so that $c_t=z_t+Z_{t-1}$. Let $\mathcal G_t$ collect everything that exists before $Z_{t-1}$ is drawn. Then $z_t$ and $E_{t-1}$ are $\mathcal G_t$-measurable, and $Z_{t-1}$ and $\zeta_t$ are independent of $\mathcal G_t$. So on the event that round $t$ runs, $\Pr[E_t\mid\mathcal G_t]=h_t(z_t)$. Also $\lVert z_t-c_1\rVert\le(t-1)(B_A+B)+\lVert\sum_{s\le t-2}Z_s\rVert$, and Gaussian norm concentration with a union bound over $t$ keeps every $z_t$ in its ball except with probability $\alpha_{\mathrm{esc}}$. The product argument of (a)(i) of [thm-active-choice-dichotomy] runs on the event that every centre stays in its ball.

(b) Certificate (proven, sketch). $\lvert h_t(z)-h_t(z')\rvert\le\mathrm{TV}(\mathcal N(z,\sigma^2I_d),\mathcal N(z',\sigma^2I_d))\le\lVert z-z'\rVert/(\sigma\sqrt{2\pi})$, because $\beta_t$ takes values in $[0,1]$. An experimenter samples the indicator of mean $h_t(z)$ by drawing $Z$ and one coupled pair at $x(z+Z,D^0_j)$ and $x(z+Z,D^1_j)$. A net of mesh $\lambda\sigma\sqrt{2\pi}$ on each ball, with Clopper and Pearson bounds and a union bound over the net points and rounds, certifies $\bar h_t\le\max_{\mathrm{net}}\bar p+\lambda$ for every learning function. The cost is $2n\sum_t\lvert\mathrm{net}_t\rvert$ Train calls, with $\lvert\mathrm{net}_t\rvert\le(1+2\varrho_t/(\lambda\sigma\sqrt{2\pi}))^d$ by the volume bound.

(c) Lower bound (proven, from part (d) of [thm-active-choice-dichotomy] with the clipped needle of the remark under Proofs). At $R=2$, $N\ge(1-\alpha-\alpha')\big((B_A/(2r))^d-1\big)$ with $r=\sigma\sqrt{2d/\eta}$, for a certifier whose output falls below $(1-\eta/2)\,\delta_{\mathcal N}(\varepsilon;B/\sigma)$ with probability $1-\alpha'$.

(d) Drawn seeds. Criterion 4 is inherited from (e)(i) of [thm-dataflow-composition] at $B_A=0$.

What the builder should deliver. Write (a) and (b) in full and check whether the product form survives an adaptive coalition, which my sketch claims. Give the lower bound in the clipped procedure. State the remaining gap between the bases of the two exponents, $B_A/(\sigma\sqrt d)$ against $R(B_A+B)/(\lambda\sigma)$, as open.

Why it matters. It turns the dichotomy into a trichotomy for coalitions that act through the aggregate. Unbounded inputs or output substitution cost an infinite number of calls. Norm-bounded inputs that pass through Gaussian release noise cost a covering number, exponential in $d$ and finite. Admissible sets that are finite cost calls linear in their size. The middle case is FedAvg with secure aggregation, release noise and a norm-bounded malicious client, which is Halil's setting. It closes open problem 5 up to the base of the exponent.

### Consolidation

No further problem is needed. After round 04 the remaining review rounds should harden and simplify. In round 05 the builder drafts the final definitions with the symbol table applied, the invert remark, and the renamed proofs of the six NONTRIVIAL theorems. In round 06 the challenger reviews that draft as if it were the final document. The stopping rule then needs every definition accepted in rounds 05 and 06, which is reachable if ch-dataset-node-channel is fixed in round 04.

### Answers to the builder's questions

1. Keep one functionality, $\mathcal F^{\mathrm{dev}}$, in which the delivered value is a coalition choice from an admissible set. Abort is the set $\{y_t,\bot\}$, substitution is $\mathbb R^d\cup\{\bot\}$, and [thm-active-choice-dichotomy] then prices both with one vocabulary. Present the abort set as the standard for the positive result and substitution as the instance of (c)(iii).
2. The specific procedures are the right form, under the impossibility pattern of [def-learning-oracle-model]. Add one sentence. Each lower bound transfers to every procedure that contains the stated one as a sub-procedure whose other nodes the coalition can simulate. A general condition on $f_t$ is not needed.
3. Round 04 takes [thm-smoothed-choice-certificate] and the challenges above. Consolidation starts in round 05.

### Convergence

This is the third of at least six review rounds. One challenge is blocking, and its fix is one clause. Definitions. Five are accepted in rounds 02 and 03, and [def-isolated-client] needs ACCEPT in two consecutive reviews. Theorems. Twelve results stand accepted, six of them NONTRIVIAL, which exceeds the bar of six and three. The stopping rule can be met at round 06 at the earliest.

## Verdicts

Six definitions and nine results are judged. Six results are NONTRIVIAL. One challenge is blocking.

```text
VERDICT def-learning-oracle ACCEPT
VERDICT def-learning-oracle-model ACCEPT
VERDICT def-degenerate-oracles ACCEPT
VERDICT def-certifier ACCEPT
VERDICT def-model-bank ACCEPT
VERDICT def-isolated-client REVISE
VERDICT lem-needle-lower-bound ACCEPT
VERDICT lem-atomless-two-point ACCEPT
VERDICT thm-coupling-certificate ACCEPT NONTRIVIAL
VERDICT thm-bank-soundness ACCEPT
VERDICT thm-dataflow-composition ACCEPT NONTRIVIAL
VERDICT thm-replay-audit-steer ACCEPT NONTRIVIAL
VERDICT thm-active-choice-dichotomy ACCEPT NONTRIVIAL
VERDICT thm-record-level-certificate ACCEPT NONTRIVIAL
VERDICT thm-black-box-certifiability ACCEPT NONTRIVIAL
BLOCKING 1
```
