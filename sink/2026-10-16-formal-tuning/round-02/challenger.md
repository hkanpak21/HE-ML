# Round 02, challenger

Verdict of this turn. Every challenge of round 01 is fixed, and no challenge is blocking after this review. Both flagship results are correct as stated. I checked [thm-dataflow-composition] (a) to (e) and [thm-replay-audit-steer] (a) to (e) step by step and found no gap in a proof. The hybrid of [thm-dataflow-composition] (b) lives on one probability space, takes the tail along the trajectory of the first argument of the hockey-stick divergence, and proves adaptive composition with a single kernel. The builder's rebuttal of my dimension conjecture is correct, because (e)(iii) is correct. The conjecture survives in a corrected form, exponential in the smaller of $d$ and $B^2/\sigma^2$, with a proof sketch below. Four theorems earn NONTRIVIAL. They are [thm-coupling-certificate], [thm-black-box-certifiability], [thm-dataflow-composition] and [thm-replay-audit-steer]. Three of the four tags rest on item 3 of [def-degenerate-oracles], which makes the drawn-seed discipline the degenerate case for experimenters and auditors. Only the tag of [thm-black-box-certifiability] survives if the orchestrator overrules that item. Twelve challenges are new and none is blocking. Two of them bear on Halil's own procedures. Condition 2 of the isolation setting excludes a client that keeps local state across rounds, and the realization notion of part (a) has content only for a coalition that follows the aggregation sub-protocol. Steering proposes two problems, a dichotomy for active coalitions with restricted choices and a certificate for the records of a dataset.

Every non-trivial claim below carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the idea of the proof is written here and the builder must write it out. Notation follows `theory/CURRENT.md` and round-02/builder.md. The single source I reopened this round is the arXiv PDF of Gilbert and McMillan (arXiv 1806.06427), for the two theorem statements quoted under [lem-atomless-two-point].

## Status of the round-01 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-query-universe | blocking | fixed | none. The query channel carries a query set, and the proof of (o) removes refused calls |
| ch-degenerate-oracles-undefined | not blocking | fixed | none. Facts (i) to (iii) and item 3 are in the definition, and every corrected paragraph uses them |
| ch-computational-adversary | not blocking | fixed | the realization notion of part (a) has a non-interactive simulator, see ch-realization-scope |
| ch-upper-bound-pattern | not blocking | fixed | none |
| ch-identity-coupling-scope | not blocking | fixed | none. The tightness clause of [thm-dataflow-composition] (b) makes it exact |
| ch-paragraph-corrections | not blocking | fixed | none. I checked all five corrected texts |
| ch-definition-cuts | not blocking | fixed | none. Further cuts are in ch-definition-simplify |
| remarks without a slug | not blocking | fixed | the Theorem 12 hypothesis of Gilbert and McMillan is missing, see ch-prior-work-quotes |

The steering of round 01 was followed. The random-table argument for explicit seeds is written, [thm-dataflow-composition] is proven with the trajectory I asked for, and [thm-replay-audit-steer] is proven with the bound in Train calls that round 01 left open.

## Definitions

### [def-learning-oracle]

Well posed (proven, by inspection). The label none is gone, a grant is an operation of the oracle that is not a call, Eval takes model names only, and the fidelity of hardware randomness is labeled heuristic. Two remarks, neither blocking. First, the Train call does not say that a seed or a seed name passed as $s$ is the seed the run uses. One clause fixes it. Second, the last two sentences of the setting cite [thm-reference-access] from inside a definition, and a remark should hold them (ch-definition-simplify). ACCEPT.

### [def-learning-oracle-model]

Well posed (proven, by inspection). The query set fixes ch-query-universe, and the computational clause is the one that [thm-dataflow-composition] (a) uses. Pattern 1 is consistent with every upper bound in the register. I checked it against [thm-replay-audit-steer] (a), which depends on queries to the random oracle and not on $q_T$, and against (e), which depends on $q_T$ and is an impossibility over a random family, pattern 3. Three remarks, none blocking.

1. Passive strategies (ch-passive-queries). Queries are listed among the choices. So an adversary that follows the protocol and makes one Eval call that the protocol does not prescribe is active. No theorem uses that reading, and [thm-dataflow-composition] (c) needs only that the choices which enter procedure nodes follow the protocol.
2. The goal invert is used by no theorem. By the rule of round 01 it waits until a theorem uses it.
3. The quantifier patterns are a convention for reading statements. They fit better in a remark after the definition.

ACCEPT.

### [def-degenerate-oracles]

Well posed. Fact (ii) is correct (proven). For one fixed learning function, a strategy defined in terms of $\mathsf L$ is a measurable map from transcripts to actions, hence an oracle algorithm. Fact (iii) is the sentence of round 01. Item 3 encodes my ruling of round 01. The README's criterion 4 names only the two adversary-side oracles, so item 3 extends the bar, and the orchestrator decides whether the extension stands. Facts (i) to (iii) are statements with proofs inside a definition, and a remark should hold them (ch-definition-simplify). ACCEPT.

### [def-certifier]

Well posed. $N$ counts all Train calls, and a certifier reaches $\mathsf L$ only through $\mathcal O$. One remark. The definition fixes $x_0,x_1$ and a channel $K$ before the target. [thm-dataflow-composition] (d)(ii) certifies $\theta^{\mathrm{act}}$, a supremum over the strategies of a whole procedure, which is not of the form $\mathrm H_\gamma(P_0\|P_1)$ with $P_b=\int K(\cdot\mid m)\,Q_{x_b}(dm)$. The soundness clause never uses the channel form. The target should be any functional $\theta(\mathsf L)\in[0,1]$, with the channel form as the main example (ch-definition-simplify). A caller that opens a seed name and never reuses it falls in the coupled discipline, which is harmless. ACCEPT.

### [def-model-bank]

Well posed, and simpler than in round 01. The empirical oracle matches a fixed entry only on a seed passed by value, and a coupled design lists its seeds as fixed values, which [lem-bank-fidelity] covers unchanged. The symbol $\Delta$ for a design collides with the threshold $\Delta$ of [thm-dataflow-composition] (ch-symbol-clash). ACCEPT.

## Proofs

### Dataflow composition [thm-dataflow-composition]

Claim. For a client isolated behind Gaussian releases, the view of every coalition, passive or active, under either adversary-side degenerate oracle, has hockey-stick divergence at most a Gaussian term in $\sqrt R\,\Delta/\sigma$ plus the probability that a coupled execution along the first hypothesis sees two releases more than $\Delta$ apart. That probability is certifiable at a cost free of the dimension.

Assumptions. Conditions 1 to 4 of the isolation setting, fidelity of hardware randomness, fixed honest inputs other than $D_j$, and for (a) a realization error $\epsilon_\Sigma$ of the aggregation sub-protocol.

Probability space. One space carries $\omega$, the triples $\zeta_t=(\rho_t,\xi^0_t,\xi^1_t)$ and the noise $Z_t$, all independent, with the law of $\omega$ free of $b$. The execution under $H_0$, the execution under $H_1$, the hybrid and $\mathsf{Ex}_0$ all live on it. Under $H_b$ the node $v_t$ uses $(\rho_t,\xi^b_t)$ and nothing else that depends on $b$. I checked that this space is legitimate.

Part (b), step 1 (proven). The induction over the order of $G$ is correct. I checked the three places where the adversary might reach something that depends on $b$ other than through the releases. The value of $v_t$ goes through channel none and has $r_t$ as its only child. Under the seed-revealing policy a Train call with the seed name of $v_t$ returns $\mathsf L(x;\rho_t,\xi')$ with $\xi'$ taken from $\omega$, a function of $(\omega,\Lambda_t)$ that does not involve $D_j$. A coalition node that is a parent of $r_t$ runs after $v_t$, so $A_t$ may depend on $\Lambda_t$, and the map $\alpha_t$ takes $\Lambda_{\le t}$.

Steps 2 and 3 (proven). The hybrid releases $F^1_t-\mathrm{clip}_\Delta(\tilde d_t)$, which equals $F^0_t$ while $\|\tilde d_t\|\le\Delta$. The two recursions agree until the first exceedance. The first exceedance is the same round seen from both sides, because both are computed from the same past and the same $\zeta_t$. The event of disagreement is therefore $\{D^\star_0>\Delta\}$, with $D^\star_0$ computed in $\mathsf{Ex}_0$, whose twin uses $\xi^1_t$ and the choice $c_t$ of the $H_0$ trajectory. This answers the question of round 01. The tail is taken along the trajectory of the first argument, the coupling inequality costs no factor $e^\varepsilon$, and the second order uses $\mathsf{Ex}_1$. The conditional step $\Pr[\|d_t\|>\Delta\mid\mathcal F_t]=\beta_t(c_t,\Delta)$ is correct, because $c_t$ is $\mathcal F_t$-measurable and $\zeta_t$ is independent of $\mathcal F_t$.

Step 4 (proven). I verified the kernel. Given $g_t\sim\mathcal N(\mu,1)$, the variable $U_t=(s_t/\mu)(g_t-\mu)+\sqrt{1-s_t^2/\mu^2}\,Z'_t$ is standard normal, and given $g_t\sim\mathcal N(0,1)$ it is $\mathcal N(-s_t,1)$. The vector $\sigma U_te_t+\sigma(I_d-e_te_t^\top)Z''_t$ is then $\mathcal N(0,\sigma^2I_d)$ or $\mathcal N(-c'_t,\sigma^2I_d)$, because $e_t$ is a unit vector fixed before $g_t$ and the two components are independent. The coordinate $g_t$ is independent of the kernel's past and of $\zeta_t$, because both input laws are products. The kernel draws $\zeta_t$ itself, so its conditional law given the past is $\mu\otimes\pi\otimes\pi$ in both runs, and the chain rule gives $L_1$ and $L_M$. This is a direct proof of adaptive composition for mixtures of Gaussian shifts bounded by $\Delta$. It no longer rests on results of Dong, Roth and Su recalled from memory. The variant with a noise level $\sigma_t$ per round is the same kernel with $\mu_t=\Delta/\sigma_t$ (proven).

Step 5 and tightness (proven). The split inequality holds for $\gamma\ge1$. In the tightness instance $D^\star_b=\Delta$ in every round, so $\epsilon_b(\Delta)=0$, and for fixed $\mathsf L$ the transcript of the opener is a bijective image of $(\rho_t,z_t)_{t\le R}$. Its divergence is $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$, which equals the bound. Under the realizable policy the divergence is $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sqrt{\sigma^2+s^2})$. The bound is exact under the top oracle and loose under the bottom oracle by the noise that the shared seed cancels.

Weakest step of (b). Step 1. The induction is short and carries the whole isolation hypothesis. It is correct as stated. It is also where condition 2 does its work, and condition 2 is stronger than the setting's remark says (ch-stateful-client below).

Counterexamples tried against (b), none succeeds.

- An active adversary under the top oracle that picks $c_t$ from the opened seeds $\Lambda_{<t}$. The map $\chi_t$ takes $\Lambda_{<t}$.
- A coalition client that chooses its own update in round $t$ after seeing $\rho_t$, to cancel or amplify client $j$'s update in the sum. The map $\alpha_t$ takes $\Lambda_{\le t}$, and the bound treats $A_t$ as known to the adversary.
- Deterministic kernels with $\mathsf L(x(c,D^0_j);\rho)=\mathsf L(x(c,D^1_j);\rho)$ except on a seed event of probability $p$ per round, where the releases differ by a large amount. Letting $\Delta\to0$, the bound tends to $\epsilon_0=1-(1-p)^R$, and the opener under the top oracle attains it (proven, by computation). The bound is tight to the term.
- A client with persistent state. It is outside condition 2, and the theorem does not claim it. The setting's remark does.

Part (a) (proven, given $\epsilon_\Sigma$). The environment $\mathcal Z_b$ implements $\mathcal O$ with the simulator of [thm-perfect-substitution] and runs every honest node outside $\Sigma$, so it runs in time $t_{\mathcal A}+(q+n_G)T_{\mathsf L}+t_G$. The identities $\Pr[\mathcal Z_b\to1\mid\Sigma]=\Pr_{G_{\mathrm{enc}},H_b}[\mathcal A\to1]$ and $\Pr[\mathcal Z_b\to1\mid\mathcal F,\mathcal S_\Sigma]=\Pr_{G_{\mathrm{rel}},H_b}[\mathcal A'\to1]$ hold by construction, and the arithmetic of the second display is correct. The loss is evaluated at a time that counts every run of $\mathsf L$ the reduction makes, which is the oracle-relative reading that ch-computational-adversary asked for.

Weakest step of (a). The realization notion. Its simulator $\mathcal S_\Sigma$ is non-interactive and sees only $y_t$ and the coalition's inputs and keys. Against an environment that plays the coalition's parties in $\Sigma$ arbitrarily, threshold decryption does not realize $\mathcal F$ with small error (proven, sketch). A coalition party that sends its decryption share last sees the honest shares and computes the output $y_t$. It then adds to its own share an encoding of $g(y_t)$ for a fixed nonzero map $g$, and the released value becomes $y_t+g(y_t)$. $\mathcal F$ cannot produce that value, because it fixes the coalition's inputs before $y_t$ exists, and an environment that tests for it distinguishes. Part (a) stays true, since it is conditional on $\epsilon_\Sigma$. The heuristic label "threshold CKKS with smudging realizes $\mathcal F$ with small $\epsilon_\Sigma$" is false for such environments. Three more clauses are needed for the heuristic, all in ch-realization-scope.

Part (c) (proven). Over independent runs the indicators of $\{D^\star_0>\Delta\}$ are independent Bernoulli variables, and the one-sided Clopper and Pearson bound has coverage at least $1-\alpha$. For (c)(ii), $\hat S$ and $\epsilon_0$ are one minus an empirical and a true distribution function, and one event of probability at least $1-\alpha$ covers every $\Delta$. Weakest step. $D^\star_0$ has atoms, at zero for the reference functions of (e) for instance, and Massart's form of the DKW inequality is usually stated for continuous distribution functions. It holds for every distribution function (proven). Write $X_i=F^{-1}(V_i)$ with $V_i$ uniform, so that $\{X_i\le x\}=\{V_i\le F(x)\}$. The supremum over $x$ is then a supremum of the uniform empirical process over the range of $F$, which is at most the supremum over $[0,1]$. One clause should say so (ch-dkw-atoms). I did not reopen Massart's paper.

Part (d) (proven). (d)(i) is a direct computation, $\mathrm{TV}=2\Phi(L/(2\sigma))-1$. (d)(ii) is a needle argument. The transcript against $\mathsf L^\circ$ is independent of $c^\star$, so a Train call names $c^\star$ with probability at most $N/K$, and off that event the runs against $\mathsf L^\circ$ and $\mathsf L_{c^\star}$ coincide. A certifier cannot learn $c^\star$ through Eval either, because every model it holds under $\mathsf L^\circ$ is a starting model it supplied. The argument uses only $K$ distinct points of the choice set, and steering uses that.

Part (e) (proven). Step 1. Both laws of $(Y_0,Y_1)$ are images of indices and signs, and given $2N$ distinct indices the signs are independent and uniform under the mixture, because distinct coordinates of $\varsigma$ are. The collision probability is at most $\binom{2N}2/K$. Step 3. The nearest-code-point test errs only when $\sigma\lvert G_1\rvert\ge L/2$, which gives $\theta\ge1-2(1+\gamma)\bar\Phi(L/(2\sigma))$. Step 4. I recomputed the three tail probabilities, the union bound, and the arithmetic with $K=\lfloor e^{B^2/(16\sigma^2)}\rfloor$ and (G3). Step 5. The identity $\phi_\sigma(y-x)=\phi_\sigma(y)\psi(y,x)$, the moment $\mathbb E_Y\psi(Y,x)^2=e^{\|x\|^2/\sigma^2}$ from (G4), Jensen and Fubini for $\mathbb E D_b$, and McDiarmid with bounded differences $2/n$, hence $\sum_kc_k^2=4/n$ and the tail $e^{-n\kappa^2/2}$, are all correct.

Weakest step of (e). Step 5 defines $\hat\theta$ as an exact Gaussian integral in dimension $d$. Certifiers have no computational bound in the model, so the statement stands. A usable estimator needs one sentence. $\hat h_b(y)$ depends on $y$ only through its projection on the span of the $2n$ samples, so $\hat\theta$ is an integral in dimension at most $2n$, and a Monte Carlo evaluation adds a term of its own (ch-estimator-dimension).

Regime of the separation. At $B/\sigma=O(1)$, part (e)(iii) certifies to accuracy $\epsilon_{\mathrm{acc}}$ with $O(\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha))$ drawn-seed runs per input (proven, from (e)(iii)). So drawn seeds lose nothing in the regime where the noise is calibrated to the clip and worst-case accounting is already useful. The separation of (e)(ii) lives in the regime $B/\sigma\to\infty$, where the free bound $\delta_{\mathcal N}(\varepsilon;2B/\sigma)$ tends to one. There the threshold $1-\frac{1+\gamma}2e^{-B^2/(16\sigma^2)}$ of (e)(ii) lies below the free bound at fixed $\varepsilon$ (proven, from the closed form and (G3), since one minus the free bound is at most of order $e^{-B^2/(2\sigma^2)}$). So a drawn-seed certifier with few runs is pinned between the two, both $1-e^{-\Theta(B^2/\sigma^2)}$. The "Reading of (e)" should state the regime (ch-separation-regime).

The disputed conjecture. I accept the rebuttal. My round-01 question asked whether drawn-seed certifiers at clipped norm $B$ need $e^{cd}$ runs. At a fixed ratio $B/\sigma$, part (e)(iii) certifies in every dimension with $O(e^{B^2/\sigma^2})$ runs for constant accuracy, so the answer is no (proven). The dimension still enters through the hypothesis $d\ge K$ of (e)(ii), and the conjecture holds in a corrected form (proven, sketch).

Corrected statement. Let $K=\lfloor\min(e^{d/64},e^{B^2/(64\sigma^2)})\rfloor$. For every $d$, every drawn-seed certifier of $\theta$ with $N$ Train calls, sound at level $\alpha$ over $\mathfrak L_B$, has at some reference function in $\mathfrak L_B$

$$\Pr\Big[\hat t\ge1-\tfrac{1+\gamma}2e^{-B^2/(64\sigma^2)}\Big]\ge1-\alpha-\frac{N(2N-1)}{K}.$$

Sketch. Replace the orthonormal vectors of step 4 by unit vectors $u_1,\dots,u_K$ with $\lvert\langle u_i,u_k\rangle\rvert\le1/4$ for $i\neq k$. Independent uniform vectors in $\{\pm d^{-1/2}\}^d$ form such a code with positive probability when $K<e^{d/64}$, because Hoeffding's inequality gives $\Pr[\lvert\langle u,v\rangle\rvert>1/4]\le2e^{-d/32}$ and there are fewer than $K^2/2$ pairs. Set $u^\pm_i=\pm Bu_i$ and let $T_\varsigma(y)=1$ when $\max_i\varsigma_i\langle y,u_i\rangle>B/2$. Under $P^\varsigma_0$ the test fails with probability at most $\bar\Phi(B/(2\sigma))$. Under $P^\varsigma_1$ the coordinate $i=I$ exceeds $B/2$ with probability $\bar\Phi(3B/(2\sigma))$. A coordinate $i\neq I$ has $\varsigma_i\langle y,u_i\rangle\le B/4+\sigma g_i$ with $g_i$ standard normal, so it exceeds $B/2$ with probability at most $\bar\Phi(B/(4\sigma))$. Hence $\theta(\mathsf L_\varsigma)\ge1-(1+\gamma K)\bar\Phi(B/(4\sigma))$, and (G3) with $K\le e^{B^2/(64\sigma^2)}$ gives the threshold. Step 1 of (e) needs only $2K$ distinct points, and step 2 transfers the bound.

Reading. To leave the neighbourhood of one, drawn seeds need at least $e^{c\min(d,B^2/\sigma^2)}$ runs, and $O(e^{B^2/\sigma^2})$ runs suffice for constant accuracy. My conjecture holds when $B^2/\sigma^2\ge d$, the regime in which the noise per coordinate is small against the update norm. Whether an upper bound exponential in $d$ alone holds in that regime is open. The builder's open question on the constant in the exponent should be restated with both parameters.

Paragraphs. "Without the oracle" and "Degenerate oracles" are correct, with the regime sentence added. The four scope limits are correct. I did not read the works cited under Prior work this round. Their roles are background, and the source of the heuristic label of (a).

Non-triviality. Criterion 1 holds, since $\epsilon_0(\Delta)$ is the exceedance probability of an execution in which each learning node is called twice with one seed name. Criterion 2 holds. Without the oracle a bound needs the law of the sequence of trained models, or a worst-case bound on the release, which an unclipped release does not have and which is vacuous at large $B/\sigma$. Criterion 3 holds, since (b) holds for every learning function and every strategy and depends on $\mathsf L$ only through $\epsilon_b(\Delta)$, which (c) certifies. Criterion 4 holds through item 3 of [def-degenerate-oracles]. Part (c) fails in the drawn-seed discipline, because no drawn-seed certifier sound over every learning function certifies below $1-\eta$ at the reference functions of (e)(i), where the coupled certificate gives $\ln(1/\alpha)/N$. Part (b) alone does not meet criterion 4, as the builder says. At $R=1$ the theorem is the Gaussian case of [thm-coupling-certificate] (b). Its own content is the adaptive multi-round composition with an oracle-measured term along the trajectory, the channel reduction and the active limit. ACCEPT NONTRIVIAL. The non-blocking corrections ch-stateful-client, ch-realization-scope, ch-per-pair-scope, ch-separation-regime, ch-dkw-atoms and ch-estimator-dimension are due before the final document.

### Replay-audit steering [thm-replay-audit-steer]

Claim. Steering a model into $T$ past an auditor that replays the run at a random-oracle seed succeeds with probability at most the number of seed candidates times the number of replays times the reach. A grinding prover attains the same order, a prover without the learning function pays in Train calls, and no drawn-seed auditor separates completeness from soundness.

Assumptions. A committed dataset, a proper metric space, a closed target, a random oracle with values of law $\mu$, and fidelity of hardware randomness, so that the auditor's replays are independent of the prover's calls.

Part (a) (proven). Lazy sampling gives $R$ its law. The replay randomness $\xi_{k,i}$ is independent of the prover's view. The union bound does not care about adaptivity, because each $F_{k,i}$ is an event of $(\rho_k,\xi_{k,i})$ alone, with law $\mu\otimes\pi$, whatever $K^*$ is.

Part (b) (proven). The first replay alone suffices.

Part (c) (proven). The triples $(\rho_k,\xi'_k,\xi_{k,1})$ are independent across $k$. The stopping event at $k$ is a function of the prover's first $k$ runs and is independent of $\xi_{k,1}$. The sum is geometric. The Borel selection of nearest points is cited from memory, and in $\mathbb R^p$ with a norm it is elementary.

Part (d) (proven). The acceptance probability $\mathrm{acc}(m,\rho)$ is the same function under every member, because drawn-seed answers at $x$ are uniform whatever $a$ is and answers at other inputs are constant. The auditor holds $\rho$ as a value, but without $a$ it cannot compute $\rho+a\bmod1$, and the discipline forbids passing $\rho$ to Train. The map $(a,\rho)\mapsto(\rho+a\bmod1,\rho)$ preserves Lebesgue measure, and Fubini gives a point $t$ with $w(t)\ge1-s-\kappa$.

Part (e) (proven). $\mathbb E_U\,p_\tau(T;\mathsf L_U)=p_\tau(T;\mathsf L)$ by the computation given. Lazy sampling for the table makes the value at each first-used prefix uniform, and the value at a new $J^*$ uniform and independent of the prover's transcript. Queries to $R$ drop out, because grinding $R$ can only move $J^*$ onto a trained prefix or a fresh one, and the union counts both cases.

Counterexamples tried, none succeeds against a statement.

- A prover that queries $R$ at other commitments. Each query counts in $q_R$.
- A prover that outputs a point of $T$ outside the support of the model law. A win still forces a replay within $\tau$ of $T$.
- A prover that calls $\mathsf{Train}(x,\rho)$ many times at the auditor's seed to learn the replay law. Its calls use hardware randomness independent of the auditor's.
- In (d), an auditor whose acceptance rule uses $\rho$. That is covered by $\mathrm{acc}(m,\rho)$.

Weakest step. The "Reading of (a) and (c)", which says the two match up to the change from $\tau$ to $\tau/2$. That gap has no bound in ratio. If $T$ lies at distance $3\tau/4$ from the support of the model law and some mass lies within $\tau$ of $T$, then $p_{\tau/2}(T)=0<p_\tau(T)$, and the attack of (c) gets nothing while (a) allows a positive probability (proven, by the example). Under deterministic kernels the match is exact (proven, sketch). Every replay equals the run at its seed, so (a) improves to $(q_R+1)\,p_\tau(T)$ without the factor $r$. The prover that stops at the first run within $\tau$ of $T$ and outputs a nearest point wins with probability $1-(1-p_\tau(T))^q$. For $q\,p_\tau(T)\le1$ the two agree up to the factor $1/(1-e^{-1})$. With hardware randomness the gap between $\tau$ and $\tau/2$ is open (ch-replay-deterministic-match).

Scope of (e). The proof uses only that the prover does not know $U$. So (e) holds for every prover that knows the base function $\mathsf L$ but not $U$, which is stronger than the stated "reaches the learning function only through $\mathcal O$" (ch-oblivious-prover-scope).

Non-triviality. Criterion 1 holds, since the reach, the spread and the joint reach are defined by drawn-seed and coupled Train calls, and the audit replays at an explicit seed. Criterion 2 holds. A bound on steering without the oracle needs the law of the trained model near $T$ and the law of replays at one seed, and the builder reports from Fang et al. that the proof-of-learning literature has no such bound. I did not read Fang et al. Criterion 3 holds, since the bound uses $\mathsf L$ only through $p_\tau$, $s_\tau$ and $p^\circ_\tau$. Criterion 4 holds through item 3 of [def-degenerate-oracles]. By (d), every complete drawn-seed auditor accepts a target of reach zero with probability close to its completeness. Part (a) is the grinding bound of the Fiat and Shamir transform, and the depth of the theorem is in (d) and (e). ACCEPT NONTRIVIAL. The corrections ch-replay-deterministic-match and ch-oblivious-prover-scope are due before the final document.

### Black-box certifiability [thm-black-box-certifiability]

Part (o) (proven). Refused calls return a symbol free of the model and the hypothesis, so they can be removed. Padding with a fixed query of $U$, which is nonempty, turns the interaction into a tree of $\mathcal T_{q_E}$. The advantage is $\mathbb E_\omega A(\tau_\omega)\le\mathrm{Adv}^{\mathrm{bb}}(q_E)$, and $\omega$ may contain knowledge of $\mathsf L$. The counterexample of ch-query-universe no longer applies, since its informative query lies outside $U$ and is refused.

The top counterexample is correct (proven). With $\mathsf{ev}(m,u)$ the $u$-th binary digit of $m$ and the first digit in $U$, both model laws are uniform, so $\mathrm{Adv}^{\mathrm{bb}}(q)=0$, and the opener wins with one query. Parts (a) to (d) are unchanged, with $n$ calls per input.

Weakest step. Part (b) has no matching lower bound, and the certificate of (a) costs about $C^{q_E}\ln\lvert U\rvert$ runs. Both are stated as scope.

Non-triviality. Criterion 1 holds, since $\mathrm{Adv}^{\mathrm{bb}}$ is certified by Train calls in (a) and bounded through coupled calls in (d). Criterion 2 holds, since a bound on what $q_E$ label queries reveal needs the law of the trained model's outputs on $U$. Criterion 3 holds, since (o) and (a) are uniform over learning functions and depend on them only through $C$, $\lvert U\rvert$ and $q_E$. Criterion 4 holds on the adversary side, since (o) fails under the top oracle. This tag does not depend on item 3 of [def-degenerate-oracles]. ACCEPT NONTRIVIAL.

### Coupling certificate [thm-coupling-certificate]

Checked the corrections. The count convention of (a) matches [def-certifier]. Step 5 now says "a supremum over adversaries for one fixed learning function". The scope states both consequences of ch-identity-coupling-scope. "Without the oracle" is restricted to deterministic channels and gives the Gaussian picture of [thm-dataflow-composition] (e), which needs the regime sentence of ch-separation-regime. "Degenerate oracles" uses item 3. Under my ruling of round 01 the tag is due. Criteria 1 to 3 hold as found in round 01. Criterion 4 holds through item 3, by (a)(iii). ACCEPT NONTRIVIAL.

### Reference access [thm-reference-access]

Part (c) for explicit seeds is correct (proven). Weakest step. The claim that the modified transcript is free of $J$. I checked it. Given $J$, the entries the modified experiment uses are independent draws with the same law whatever $J$ is, so the conditional law of the modified transcript given $J$ does not depend on $J$. Each call's prefix is a function of the transcript before it, so it equals $J$ with probability $2^{-k}$, and the union over at most $q$ calls at the honest input gives $q2^{-k}$. The real and modified experiments agree until the first hit. The corrected paragraph on degenerate oracles is correct. ACCEPT.

### Atomless two-point lemma [lem-atomless-two-point]

Step 2 now puts the evaluation randomness into $W$. The new certifier in the remark on randomized channels is sound (proven). I checked the case split at $\mathrm{TV}(Q_0,Q_1)\le\epsilon_n$ and the bound $\sum_{m'}a_0(m')^na_1(m')^n\le\frac\alpha2\sum_{m'}\max_ba_b(m')\le\alpha$. The corrected "Without the oracle" and "Degenerate oracles" paragraphs are correct.

Prior work. I reopened arXiv 1806.06427. Theorem 10 reads "No ε-pDP property tester with proximity parameter α has finite query complexity", as the builder quotes. Theorem 12 carries the hypothesis $e^\varepsilon/2+\delta+\alpha<1$, which the builder's paragraph omits (ch-prior-work-quotes). ACCEPT.

### Bank soundness [thm-bank-soundness]

The rotation example is correct (proven). Both models are uniform in the fixed game, the coupled pair differs by $1/2$ at every seed, and both views of the random-subset game are uniform. The warning on selecting tests on the bank is the one round 01 asked for. ACCEPT.

### Perfect substitution [thm-perfect-substitution]

The two corrected sentences are correct, and "stops with probability one" now comes from [def-learning-oracle-model]. ACCEPT.

### Bank fidelity [lem-bank-fidelity]

Unchanged, and still correct for the reduced [def-model-bank]. ACCEPT.

## New challenges

### ch-stateful-client

Not blocking. Targets the setting of [thm-dataflow-composition]. The sentence "Local steps of client $j$ between two releases form one learning function, so condition 2 loses no generality" is false. A client that keeps a local adapter, optimizer state or error-feedback memory from round $t$ to round $t+1$ makes $v_t$ a parent of $v_{t+1}$, and condition 2 fails. The adapter of `CONTEXT.md` is kept local, so a multi-round procedure built on it falls outside condition 2.

The theorem extends (proven, sketch). Let $v_t$ read the state $W_{t-1}$ of client $j$, with children $r_t$ and $v_{t+1}$. In $\mathsf{Ex}_0$ the twin carries its own state, $W'_t=\mathsf L(x(c_t,D^1_j,W'_{t-1});\rho_t,\xi'_t)$. The hybrid carries both state chains along its own trajectory. Until the first exceedance it is the $H_0$ execution, and its second chain is the twin chain of $\mathsf{Ex}_0$, so step 3 holds. In step 4 the kernel carries both chains, and under $H_1$ the chain for $D^0_j$ is auxiliary and does not change the output law. The tail of the sum bound becomes a coupled tail at two training inputs with different starting states, $\beta_t(c_t,W_{t-1},W'_{t-1},\Delta)$.

Smallest fix. Replace the sentence by "Condition 2 excludes client state kept across rounds." Better fix. State the extension above, since it costs one more chain in the proof and covers stateful clients.

### ch-realization-scope

Not blocking. Targets the realization notion of [thm-dataflow-composition] (a) and the heuristic label on threshold CKKS. Smallest fix, four clauses.

1. The environment plays the coalition's parties in $\Sigma$ by the protocol. Part (a) then covers adversaries that follow $\Sigma$, whose choices elsewhere may still be active. The rushing counterexample under Proofs shows that the non-interactive simulator cannot serve a coalition that deviates inside $\Sigma$.
2. The noise $Z_t$ of $\mathcal F$ is the honest parties' share, since a coalition party knows the smudging or privacy noise it adds itself.
3. The law of $e_t$ is independent of the inputs. CKKS encoding and rescaling errors depend on the message, and the statistical distance that smudging buys is charged to $\epsilon_\Sigma$.
4. $\mathcal A'$ obtains the coalition's keys from $\mathcal S_\Sigma$ or from a setup that $G_{\mathrm{rel}}$ keeps, since $G_{\mathrm{rel}}$ has no keys of its own.

### ch-per-pair-scope

Not blocking. Targets the statements of [thm-dataflow-composition] (b) and (c). Both bound the divergence for the one pair $(D^0_j,D^1_j)$. Differential privacy quantifies over all neighbouring pairs. No certifier sound over every learning function certifies a supremum over an infinite set of pairs (proven, sketch, the needle of (d)(ii) with the dataset in place of the starting model). Smallest fix. One sentence in the setting that names the guarantee as a guarantee for the fixed pair. Steering below proposes the record-level form.

### ch-separation-regime

Not blocking. Targets "Reading of (e)" in [thm-dataflow-composition] and "Without the oracle" in [thm-coupling-certificate]. Smallest fix. One sentence. At $B/\sigma=O(1)$ drawn seeds certify cheaply by (e)(iii), and the separation holds as $B/\sigma\to\infty$, the regime where worst-case accounting is vacuous.

### ch-dkw-atoms

Not blocking. Targets the proof of [thm-dataflow-composition] (c)(ii). Smallest fix. One clause saying that Massart's inequality holds for every distribution function, by the quantile transform under Proofs.

### ch-estimator-dimension

Not blocking. Targets [thm-dataflow-composition] (e)(iii). Smallest fix. One sentence saying that $\hat\theta$ is an integral over the span of the $2n$ samples, and that a Monte Carlo evaluation adds its own term.

### ch-replay-deterministic-match

Not blocking. Targets "Reading of (a) and (c)" in [thm-replay-audit-steer]. Smallest fix. Replace "match up to the change from $\tau$ to $\tau/2$" by the deterministic-kernel statement under Proofs, and record the gap between $\tau$ and $\tau/2$ under hardware randomness as open.

### ch-oblivious-prover-scope

Not blocking. Targets the statement of [thm-replay-audit-steer] (e). Smallest fix. Write "every prover that may know $\mathsf L$ but not $U$".

### ch-passive-queries

Not blocking. Targets [def-learning-oracle-model]. Smallest fix. "A strategy is passive when the choices that enter procedure nodes are the functions of procedure values that the protocol prescribes." Queries then leave the definition of passive.

### ch-definition-simplify

Not blocking. Cuts that lose no theorem and leave the definitions in their simplest form.

1. [def-learning-oracle]. Move the atomless-idealization sentences to a remark.
2. [def-learning-oracle-model]. Drop the goal invert until a theorem uses it. Move the quantifier patterns to a remark.
3. [def-degenerate-oracles]. Keep the two policies, the two disciplines and the rule of which object tests which statement. Move facts (i) to (iii) to a remark.
4. [def-certifier]. Let the target be any functional $\theta(\mathsf L)\in[0,1]$, and give the channel form as an example.

### ch-symbol-clash

Not blocking for the rounds, due before the final document. Several symbols name two objects. $\sigma$ is the evaluation randomness and the noise scale. $\mu$ is the seed law and $\Delta/\sigma$ in step 4. $\Delta$ is a design and a threshold. $\Lambda$ is the set of learner names and the revealed seeds. $\tau$ is a tree and a tolerance. $R$ is the number of rounds and the random oracle. $c$ is a choice and a commitment. $K$ is a channel and a count of code points. $\Phi$ is a transcript map and the normal distribution function. $T$ is a target set, a time and a test. $\pi$ is the hardware law and the prefix map. $\kappa$ is a channel, a deviation and a slack. Smallest fix. The final document carries one symbol table with one object per symbol, and the proofs rename locally.

### ch-prior-work-quotes

Not blocking. Targets the prior-work paragraph of [lem-atomless-two-point]. Add the hypothesis $e^\varepsilon/2+\delta+\alpha<1$ to the statement of Theorem 12 of Gilbert and McMillan. Every result cited from memory in the final document, Massart's constant and the Kuratowski and Ryll-Nardzewski selection theorem among them, needs its source opened or the label "from memory" kept.

## Steering

The single-node theory and both flagship results satisfy me. What the theory now lacks for Halil's aim is the passage from one pair and one honest strategy to the two quantifiers that a privacy claim about a real procedure carries. These are all records of a dataset, and the deviations of a malicious server. Both problems below use the sum bound of [thm-dataflow-composition] (b), which no result has used yet.

### Problem [thm-active-choice-dichotomy]

Setting. $G$ isolates client $j$. For each round the procedure fixes a set $\mathcal C_t\subseteq\mathcal C$ of admissible choices, and an active strategy picks $c_t\in\mathcal C_t$ adaptively. Examples are a server that must start each round from a published checkpoint, and a coalition client that may inject one of finitely many record sets. Let $\theta^{\mathrm{act}}_{\mathcal C}$ be the supremum of $\mathrm H_{e^\varepsilon}(P_0\|P_1)$ over these strategies.

(a) For every such strategy, $\epsilon_0(\Delta)\le\sum_{t\le R}\sup_{c\in\mathcal C_t}\beta_t(c,\Delta)$. Hence $\theta^{\mathrm{act}}_{\mathcal C}$ is at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$ plus that sum (proven, one line from the sum bound of (b)).

(b) Certificate. For finite sets $\mathcal C_t$, $n$ coupled pairs at each pair $(t,c)$, with Clopper and Pearson bounds at level $\alpha/\sum_t\lvert\mathcal C_t\rvert$, certify the bound of (a) for all strategies at once. The cost is $2n\sum_t\lvert\mathcal C_t\rvert$ Train calls, and the number of adaptive strategies, which grows with the depth $R$ of the strategy tree, does not enter (proven, sketch). When $f_t$ and the training inputs do not depend on $t$, the cost is $2n\lvert\mathcal C\rvert$.

(c) Lower bound. Take $R=1$. Let a certifier of $\theta^{\mathrm{act}}_{\mathcal C}$, in either discipline and sound over every learning function, output below $1-\eta$ with probability at least $1-\alpha$ at the reference function $\mathsf L^\circ$ of (d)(ii). Then $N\ge(1-2\alpha-\eta)\lvert\mathcal C\rvert$, and for infinite $\mathcal C$ no such certifier exists (proven, sketch, the needle of (d)(ii) with $c^\star$ uniform on $\mathcal C$).

Why it matters. The price of certifying privacy against an active coalition is linear in the number of admissible choices and infinite for an infinite set. In the oracle model, this is what verifiable aggregation buys, since it collapses $\mathcal C_t$ to the protocol's value and reduces the active case to the passive one. It also gives the literature study a formal test of which malicious-server threat models admit a certificate from training runs. Criterion 4 is inherited from (e)(i) at $\lvert\mathcal C\rvert=1$. The builder should say whether (a) and (b) are a corollary or a theorem. The content I expect is the independence of the strategy tree in (b) and the matching bound (c).

### Problem [thm-record-level-certificate]

Setting. Client $j$ holds a fixed dataset $D$. For a record $z\in D$ the pair is $H_0$ with $D_j=D$ and $H^z_1$ with $D_j=D\setminus\{z\}$. The coalition is passive. The $H_0$ execution is the same for every record, so one run of $\mathsf{Ex}_0$ can carry one twin per record and per round.

(a) Shared base. Draw records $z_1,\dots,z_m$ uniformly from $D$. Run $\mathsf{Ex}_0$ $N$ times, each run carrying the $m$ twins, at a cost of $R(1+m)$ Train calls per run for client $j$. Let $\bar p_i$ be the Clopper and Pearson bound at level $\alpha/(2m)$ for $\epsilon^{z_i}_0(\Delta)$, and $\hat\beta$ the fraction of $i$ with $\bar p_i>\bar\epsilon$. With probability at least $1-\alpha$, the fraction of records $z\in D$ with $\mathrm H_{e^\varepsilon}(P_0\|P^z_1)>\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\bar\epsilon$ is at most $\hat\beta+\sqrt{\ln(2/\alpha)/(2m)}$ (proven, sketch). The per-record bounds hold together by a union bound over the $m$ sampled records. Hoeffding's inequality over the sampling of records then bounds the population fraction. The twins of one run are dependent, and this does not matter, because each bound uses one record across independent runs.

(b) The other order. $\mathrm H_{e^\varepsilon}(P^z_1\|P_0)$ needs $\mathsf{Ex}^z_1$, a separate base execution per record, at a cost of $2R$ Train calls per record and run. The order of the hockey-stick divergence therefore decides the cost of a record-level certificate. State this asymmetry. Whether the reverse order can be bounded from the shared base is open.

(c) Records outside $D$. For replacement neighbours, or any infinite record space, no certifier sound over every learning function certifies the supremum over records (proven, sketch, the needle of (d)(ii)). The record-level guarantee is then the strongest form available uniformly over learning functions.

(d) Optional, only if it comes cheaply. Relate (a) to the estimand of [thm-bank-soundness], so that a membership-inference evaluation on a bank and the certificate speak about the same record-level quantity.

Why it matters. It turns the single-pair certificate into a statement about a whole fine-tuning dataset, at a cost linear in the number of sampled records and free of the dimension. That is the form a privacy claim about a transformer procedure takes in a paper. Criterion 4 is inherited from (e)(i).

### The open items

- The sum channel matters for Halil's procedures, since threshold CKKS aggregation releases a sum and the theorem credits nothing to the other clients. It may stay open in a finished theory if the final document states the obstacle exactly. The coupled execution shares the other clients' randomness. Crediting their contributions needs a coupling that moves their seeds, which is the seed-map problem of [thm-coupling-certificate] (c)(ii) for the other clients (heuristic, the reduction is not written). In the drawn-seed discipline, crediting their sum is a smoothed-divergence estimate of the kind that (e) prices (heuristic).
- The matching lower bounds may be recorded as open. These are the exponent in (e), now in both $d$ and $B^2/\sigma^2$, and the lower bound for [thm-black-box-certifiability] (b). No later theorem needs them.
- Bank soundness (d) may be recorded as open. No proposed theorem depends on it.
- A drawn-seed certifier for $R$ rounds whose cost is free of $d$ may be recorded as open, at low priority. It concerns the bottom experimenter, which the theory uses only as a degenerate case.

### Answers to the builder's questions

1. Yes. Part (e)(i) alone meets the ruling of round 01, exactly as (a)(iii) does for [thm-coupling-certificate]. Parts (e)(ii) and (e)(iii) add the quantitative picture, with the regime of ch-separation-regime.
2. Yes, item 3 of [def-degenerate-oracles] settles it under the same ruling. If the orchestrator overrules item 3, the tags of [thm-coupling-certificate], [thm-dataflow-composition] and [thm-replay-audit-steer] fall, and the tag of [thm-black-box-certifiability] stands.
3. Neither first. Take the two problems above, record the sum channel as open with its obstacle stated, and move the multi-round drawn-seed certifier to the open list.

## Verdicts

Five definitions and ten results are judged. Four results are NONTRIVIAL. No challenge is blocking.

```text
VERDICT def-learning-oracle ACCEPT
VERDICT def-learning-oracle-model ACCEPT
VERDICT def-degenerate-oracles ACCEPT
VERDICT def-certifier ACCEPT
VERDICT def-model-bank ACCEPT
VERDICT lem-atomless-two-point ACCEPT
VERDICT thm-coupling-certificate ACCEPT NONTRIVIAL
VERDICT thm-perfect-substitution ACCEPT
VERDICT thm-reference-access ACCEPT
VERDICT thm-own-data-only REJECT
VERDICT lem-bank-fidelity ACCEPT
VERDICT thm-black-box-certifiability ACCEPT NONTRIVIAL
VERDICT thm-bank-soundness ACCEPT
VERDICT thm-dataflow-composition ACCEPT NONTRIVIAL
VERDICT thm-replay-audit-steer ACCEPT NONTRIVIAL
BLOCKING 0
```
