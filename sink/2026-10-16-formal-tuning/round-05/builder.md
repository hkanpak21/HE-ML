# Round 05, builder

Verdict of this turn. All seven challenges of round 04 are accepted, and none is disputed. Part (c) of thm-smoothed-choice-certificate is now its own theorem, thm-bounded-deviation-transfer, measured against the protocol's input as ch-reference-strategy asks. At $B_A=0$ it is the passive certificate of thm-dataflow-composition (c). Its lower bound is sharpened by a nearly orthogonal code with threshold decoding, as the steering asked. The number of Train calls that certifies a coalition whose inputs deviate by at most $B_A$ then has logarithm $(1+o(1))(R-1)B_A^2/(2\sigma^2)$ when that ratio is small against $d$ (proven). So the transfer is optimal in that regime, and the constant of open problem 5 is $1/2$. A new part shows that the transfer function itself cannot be improved to first order in the exponent (proven). One detail of step 1 of thm-dataflow-composition (b) is made explicit, because the transfer compares two adversaries. The randomness of the procedure's nodes is indexed by node and not by the order of the adversary's calls. Every symbol clash of round 04 is resolved, together with nine more that the final document would have carried. `theory/CURRENT.md` is in its final form, and `final/learning-oracle-theory.md` is drafted.

Notation follows `theory/CURRENT.md` after this round. The renamings are listed under ch-symbol-clash.

## Responses to challenges

### ch-reference-strategy

Accepted. The comparison strategy of round 04 was the null strategy, which is the protocol's strategy in $G^{\mathrm{agg}}_R$ only. The new theorem thm-bounded-deviation-transfer compares every strategy whose inputs stay within $B_A$ of the prescribed inputs with the protocol's own strategy. The step-3 moment depends only on the norm of the difference between the two inputs, so steps 1 to 5 of round 04 carry over (proven, under Proofs). At $B_A=0$ the transfer function is the identity, and part (b) of the new theorem is the passive certificate of thm-dataflow-composition (c), stopping variants included. The final document states one theorem for both. $G^{\mathrm{agg}}_R$ stays the instance of the lower bounds.

Two hypotheses are written into the setting, since the proof uses them.

1. The prescribed input $u^{\mathrm{pr}}_t$ is a measurable function of the values of the nodes that run before $r_t$, other than the coalition's input nodes. Without this, deviations can accumulate. With the prescription $u^{\mathrm{pr}}_t=u_{t-1}$ the inputs $u_t=tB_A\mathbf e_1$ deviate by $B_A$ at every step, and their release laws differ from the protocol's by shifts of norm $tB_A$ (proven, by the example). The proof then gives only the exponent $\sum_{t<R}t^2B_A^2/(2\sigma^2)$.
2. Step 1 of thm-dataflow-composition (b) indexes the randomness of each node of the procedure by the node, including the oracle's draws for the calls that the procedure requires of the coalition's own nodes. Only the calls that the adversary makes on its own use a sequence in order. Round 03 wrote "used in order" for all of the adversary's calls. For one adversary the two representations give the same law, by fidelity. For two adversaries whose own calls differ, only the node-indexed one makes the maps of step 1 the same, which step 1 of the transfer needs. Round 04 used this implicitly.

### ch-open-problem-five

Accepted. The regime $\mathfrak e/d\to0$ is now proven, by part (d) and the corollary of thm-bounded-deviation-transfer. Open problem 5 is one question for every fixed ratio. With $c=\mathfrak e/d$ fixed, is $\lim\ln N^\star/\mathfrak e=\ln(1+2c)/(2c)$ as $\mathfrak e\to\infty$ with $\ln R=o(\mathfrak e)$? The value is the challenger's capacity heuristic. The known bounds are $(1+2\sqrt c)^{-2}\le\liminf\le\limsup\le1$ (proven, by part (d) with $\mathfrak c=2\sqrt c/(1+2\sqrt c)$ and by part (b)), and the limit is one along $\mathfrak e/d\to0$. The condition $\ln R=o(\mathfrak e)$ is in the corollary, since each run of the certificate costs $2R$ Train calls.

### ch-lower-bound-transfer

Accepted. The remark of def-learning-oracle-model now reads as follows. A certifier sound for a target $\theta'\ge\theta$ is sound for $\theta$, since $\theta(\mathsf L)\le\theta'(\mathsf L)\le\hat t$ on the soundness event. So a lower bound of the form $\Pr_{\mathsf L^\circ}[\hat t\ge\vartheta]\ge p$ for every certifier sound for $\theta$ holds for every certifier sound for $\theta'$, and it reads as a failure when $\theta'(\mathsf L^\circ)=0$. A larger procedure gives such a $\theta'$ when, for every adversary of the stated procedure, some adversary of the larger one has a view whose image under one measurable map, the same under both hypotheses, has the law of the stated view under each hypothesis. Then $\theta'\ge\theta$ by data processing (proven). Honest clients whose updates enter a sum with client $j$'s do not meet this condition, and open problem 1 asks whether they lower the divergence.

### ch-scalar-noise-placement

Accepted. The Reading of thm-dataflow-composition (a)(iii) gains one sentence. The bound applies when the decryptors add the protecting noise at decryption. If client $j$ adds its noise inside its ciphertext, the scalar multiplies that noise too, and (ii) becomes $1-(1+\gamma)\bar\Phi((\mathfrak d/2-e_{\max}/a)/\sigma)$. So the scalar removes at most the decryption error, and the noise inside the ciphertext still protects at its own scale (proven, by the computation of (ii) with $aZ_1$ in place of $Z_1$).

### ch-euclidean-norm-proof

Accepted. The application paragraph now reads "if every coalition client proves in zero knowledge that the Euclidean norm of the difference between its input and its prescribed input is at most $B_A/k_A$". A bound $b_\infty$ on each coordinate gives only $B_A=k_A\sqrt d\,b_\infty$, so $\mathfrak e$ then grows linearly in $d$ (proven, by $\|v\|_2\le\sqrt d\|v\|_\infty$). The claim about which norms RoFL supports is withdrawn until its paper is opened. Only the existence of norm-bound proofs inside secure aggregation is cited, from a search summary.

### ch-poisson-reason

Accepted. The dropped item now reads "Subsampling is a node of the procedure, and no theorem of this theory uses it, so the question is out of scope." The withdrawal of the second half of thm-bank-soundness (d) gives the same reason.

### ch-symbol-clash

Accepted. Each clash of round 04 is renamed, and each renaming holds in `theory/CURRENT.md`, in this file and in the final document.

| Was | Object | Now |
| --- | --- | --- |
| $\ell_t$ in step 2 of (c) | likelihood ratio of round $t$ | $\mathfrak r_t$ |
| $\mathfrak L$ in step 4 of (c) | $\ln(1/p)$ | $\mathfrak l$ |
| $E_t$ in (a) | exceedance event of round $t$ | $\mathcal E_t$ |
| $\mathrm H_2$ in lem-sphere-code | binary entropy | $\mathrm h_2$ |
| $s$ in lem-sphere-code (b) | separation of the points | $\mathfrak s$ |
| $\mathcal F_t$ in (c) | filtration of the releases | $\mathcal F^{\mathrm{rel}}_t$ |
| $\mathcal F_t$ in thm-dataflow-composition (b) | filtration of the execution | $\mathcal G_t$ |
| $u$ in (e) | round-1 shift | written as the model minus $m_1$ |
| $u^\pm_i$ | points of the pair code | $\mathbf p^\pm_i$ |
| $P,Q$ in step 2 of (c) | laws under the strategy and the reference | $\mathbb P^{\mathrm{dev}},\mathbb P^{\mathrm{pr}}$ |
| $A_t$ in (a) | no exceedance up to round $t$ | $\mathcal I_t$ |
| $V$ in (c) | randomness outside the releases | $\Omega$ |
| $M_t$ in (c) | release mean other than the input | $\bar y_t$ |

The inversion remark no longer uses $\mathrm H^{\to}_i$, $\delta_R$ and $F^{\to}$. Its average form moves to the register line of thm-record-level-certificate, where the three objects are defined.

Nine more clashes, which the final document would have carried, are renamed as well.

| Was | Clashes with | Now |
| --- | --- | --- |
| $Q_x$, law of the trained model at $x$ | the allowance $Q$ | $\Pi_x$ |
| $s_\tau$, the spread | the seed name $s$ | $\mathrm{sp}_\tau$ |
| $d$, the metric of thm-replay-audit-steer | the dimension $d$ | $\mathrm{dist}$ |
| $q_R$, queries to the random oracle | the number of rounds $R$ | $q_{\mathsf{RO}}$ |
| $a=\Delta/\sigma$ in step 4 of thm-dataflow-composition (b) | the scalar $a$ of (a)(iii) | written as $\Delta/\sigma$ |
| $U_t$, the kernel coordinate of that step | the query set $U$ | $\tilde g_t$ |
| $k$-bit seeds | $k$ bank runs | $n_{\mathrm{bit}}$-bit seeds |
| $A(\mathfrak t)$, the advantage of a tree | the coalition $A$ | $\mathrm{Adv}(\mathfrak t)$ |
| $\phi$, a seed map | the normal density $\varphi$ | $\psi$ |

The sketch of the steering of round 04 used $\kappa$, $a_\eta$, $\omega_k$, $\rho_c$, $s_c$ and $\tau$ for objects that already had other meanings. Below they are $\mathfrak c$ (the coherence of the code), $\mathfrak q_\eta$ (a normal quantile), vectors with coordinates $\pm d^{-1/2}$, $\mathfrak m$, $\mathfrak v$ and the explicit threshold $\mathfrak m-\mathfrak q_\eta\mathfrak v$. Unit vectors of $\mathbb R^d$ are $\mathbf e_i$, in bold, since $e_t$ is a decryption error.

## Definition changes

1. def-learning-oracle-model. The transfer remark is rewritten (ch-lower-bound-transfer). The inversion remark keeps its first sentence, and its average form moves to thm-record-level-certificate (ch-symbol-clash). Neither remark is part of the definition.
2. def-isolated-client. The last sentence of the remarks, which cited a round and a challenge, is dropped. A definition does not carry its history.
3. def-learning-oracle. The law of the trained model at $x$ is written $\Pi_x$ in place of $Q_x$, and the remark on short seeds says $n_{\mathrm{bit}}$-bit. Notation only.
4. Symbols. The renamings above are applied. No meaning changes.

No other definition changes. Every theorem that cites a definition holds with the same proof.

## Proofs

Standing facts. Rounds 01 to 04 list the test fact, data processing, the realization fact, Lyapunov's theorem, (G1) to (G4), the split, McDiarmid's inequality, the DKW inequality, lazy sampling, (F1) to (F4), (F6) and (F7). One fact is added.

(F8) Hoeffding's inequality for signs. If $\varsigma_1,\dots,\varsigma_d$ are independent uniform signs, then $\Pr[|\sum_i\varsigma_i|\ge\mathfrak cd]\le2e^{-\mathfrak c^2d/2}$ for $\mathfrak c>0$. This is Hoeffding's inequality for variables with values in $[-1,1]$ (Hoeffding, 1963).

### Bounded-deviation transfer [thm-bounded-deviation-transfer]

Setting. $G$ isolates client $j$ behind Gaussian releases (def-isolated-client), with or without state, under the realizable or the seed-revealing policy. For each $t\le R$ the coalition may own input nodes whose only child is $r_t$. Let $u_t\in\mathbb R^d$ be the sum of their values in round $t$, with $u_t=0$ when it owns none. Assume $O_t=u_t+o_t$, where $o_t$ is a measurable function of the parents of $r_t$ other than $v_t$ and these input nodes, and of randomness of $r_t$ independent of $Z_t$. The protocol prescribes the values of these input nodes. Let $u^{\mathrm{pr}}_t$ be the sum of the prescribed values, a measurable function of the values of the nodes that run before $r_t$ other than these input nodes.

Fix $B_A\ge0$. A strategy is $B_A$-deviating when every argument and every value that it sets for a node other than these input nodes is the protocol's, $\|u_t-u^{\mathrm{pr}}_t\|\le B_A$ in every round that runs, and it stops, if at all, after a release. Its queries and its other oracle calls are unrestricted. The protocol's strategy is the $B_A$-deviating strategy with $u_t=u^{\mathrm{pr}}_t$ that never stops, and $\epsilon^{\mathrm{pr}}_b(\Delta)$ is its exceedance probability along $H_b$. For $\gamma=e^\varepsilon$ let $\theta^{\mathrm{dev}}$ and $\theta^{\mathrm{dev},\leftarrow}$ be the suprema of $\mathrm H_\gamma(P_0\|P_1)$ and of $\mathrm H_\gamma(P_1\|P_0)$ over the adversaries with a $B_A$-deviating strategy. Let

$$\mathfrak e=\frac{(R-1)B_A^2}{2\sigma^2},\qquad\Upsilon_{\mathfrak e}(p)=\exp\Big(-\big(\sqrt{\ln(1/p)}-\sqrt{\mathfrak e}\big)_+^2\Big)\ \text{ for }p\in(0,1],\qquad\Upsilon_{\mathfrak e}(0)=0.$$

The instance $G^{\mathrm{agg}}_R$ of round 04 has one coalition client $j'$ whose prescribed input is $u^{\mathrm{pr}}_t=0$, release map $f_t((t,m),W)=\mathrm{clip}_B(W-m)$ with $B\in(0,\infty]$, distinct learner names $\ell_1,\dots,\ell_R$, and next starting model $m_{t+1}=m_t+y_t$. Its target is $\theta^{\mathrm{agg}}_R=\max\{\theta^{\mathrm{dev}},\theta^{\mathrm{dev},\leftarrow}\}$. Its other honest nodes make no Train call, so $n_{\mathrm{oth}}=0$ there.

Statement.

(a) Transfer. For every learning function, every $B_A$-deviating strategy, every $b\in\{0,1\}$, every $\Delta>0$ and every $\varpi>1$,

$$\epsilon_b(\Delta)\le\epsilon^{\mathrm{pr}}_b(\Delta)^{1-1/\varpi}\,e^{(\varpi-1)\mathfrak e},\qquad\text{hence}\qquad\epsilon_b(\Delta)\le\Upsilon_{\mathfrak e}\big(\epsilon^{\mathrm{pr}}_b(\Delta)\big).$$

Hence $\theta^{\mathrm{dev}}\le\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\Upsilon_{\mathfrak e}(\epsilon^{\mathrm{pr}}_0(\Delta))$ and $\theta^{\mathrm{dev},\leftarrow}\le\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\Upsilon_{\mathfrak e}(\epsilon^{\mathrm{pr}}_1(\Delta))$. At $B_A=0$, $\Upsilon_0(p)=p$, and the $0$-deviating strategies are the protocol's strategy and its stopping variants.

(b) Certificate. Fix $\Delta>0$. Let $\bar\epsilon_b$ be the one-sided Clopper and Pearson upper bound at level $\alpha$ from the number of $N'$ independent runs of $\mathsf{Ex}_b$ under the protocol's strategy whose exceedance is above $\Delta$. Then $\hat t_b=\min\{1,\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\Upsilon_{\mathfrak e}(\bar\epsilon_b)\}$ is sound at level $\alpha$ over every learning function, $\hat t_0$ for $\theta^{\mathrm{dev}}$ and $\hat t_1$ for $\theta^{\mathrm{dev},\leftarrow}$. Each run costs $2R$ Train calls for client $j$ and $n_{\mathrm{oth}}$ calls for the other nodes. If no run exceeds $\Delta$ and $N'\ge\ln(1/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)$ with $\epsilon_{\mathrm{acc}}\in(0,1]$, then $\hat t_b\le\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}$.

(c) The transfer function is tight. Let $R\ge2$, $B_A>0$ and $B\ge2\Delta$ in $G^{\mathrm{agg}}_R$. For every $\iota>\sqrt{2\mathfrak e}+1$ some learning function and some admissible strategy have $\epsilon^{\mathrm{pr}}_0(\Delta)=\bar\Phi(\iota)$ and $\epsilon_0(\Delta)=\bar\Phi(\iota-\sqrt{2\mathfrak e})$, and

$$\ln\frac1{\epsilon_0(\Delta)}\le\ln\frac1{\Upsilon_{\mathfrak e}(\epsilon^{\mathrm{pr}}_0(\Delta))}+2\ln(\iota+1)+2 .$$

So every function $F$ on $(0,1]$ with $\epsilon_0(\Delta)\le F(\epsilon^{\mathrm{pr}}_0(\Delta))$ in every instance of $G^{\mathrm{agg}}_R$ with these $R$, $B_A$, $\sigma$ and $\Delta$ satisfies $\limsup_{p\to0}\ln(1/F(p))/\ln(1/\Upsilon_{\mathfrak e}(p))\le1$.

(d) Lower bound with the sharp constant. In $G^{\mathrm{agg}}_R$ let $B<\infty$ and $B_A>0$, and let $\mathsf L^\circ$ return the starting model at every training input. Then $\theta^{\mathrm{agg}}_R(\mathsf L^\circ)=0$ and every coupled pair at $\mathsf L^\circ$ coincides. For $\mathfrak c,\eta\in(0,1)$ let $\mathfrak q_\eta$ solve $\bar\Phi(\mathfrak q_\eta)=\eta/4$ and

$$J_3=\min\Big\{\big\lfloor e^{\mathfrak c^2d/4}\big\rfloor,\ \Big\lfloor\frac\eta2\exp\Big(\tfrac12\big((1-\mathfrak c)\sqrt{2\mathfrak e}-\mathfrak q_\eta\big)_+^2\Big)\Big\rfloor\Big\}.$$

If $J_3\ge1$, every certifier of $\theta^{\mathrm{agg}}_R$ with $N$ Train calls, in either discipline, sound at level $\alpha$ over every learning function, satisfies

$$\Pr_{\mathsf L^\circ}\Big[\hat t\ge(1-\eta/2)\,\delta_{\mathcal N}(\varepsilon;B/\sigma)\Big]\ge1-\alpha-\frac N{J_3}.$$

If $\mathfrak e<d/4$, $\mathfrak c=2\sqrt{\mathfrak e/d}$, $(1-\mathfrak c)\sqrt{2\mathfrak e}\ge\mathfrak q_\eta$ and the second argument of the minimum is at least one, then $\ln J_3\ge\mathfrak e(1-4\sqrt{\mathfrak e/d})-\mathfrak q_\eta\sqrt{2\mathfrak e}+\ln(\eta/4)$.

(e) Drawn seeds. In $G^{\mathrm{agg}}_R$ with $B<\infty$ and $B_A\ge0$, let $J_{\mathrm{cd}}\ge1$ with $2J_{\mathrm{cd}}\le\lceil2^{0.18d}\rceil$. For every drawn-seed certifier of $\theta^{\mathrm{agg}}_R$ with $N$ Train calls, sound at level $\alpha$ over every learning function, some learning function at which every coupled pair coincides, so that $\theta^{\mathrm{agg}}_R=0$, gives

$$\Pr\Big[\hat t\ge1-(1+\gamma)(2J_{\mathrm{cd}}-1)\,\bar\Phi\big(B/(2\sigma)\big)\Big]\ge1-\alpha-\frac{N(2N-1)}{J_{\mathrm{cd}}},$$

while at the same function the certificate of (b) outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\Upsilon_{\mathfrak e}(\ln(1/\alpha)/N')$ with certainty.

Corollary, the price. In $G^{\mathrm{agg}}_R$ let $B<\infty$, $B_A>0$, $\eta\in(0,1)$, $\epsilon_{\mathrm{acc}}\in(0,1]$ and $\alpha+\alpha'<1$, with $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<(1-\eta/2)\,\delta_{\mathcal N}(\varepsilon;B/\sigma)$. Let $N^\star$ be the least $N$ such that some certifier of $\theta^{\mathrm{agg}}_R$ with $N$ Train calls is sound at level $\alpha$ over every learning function and outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}$ at $\mathsf L^\circ$ with probability at least $1-\alpha'$. For every $\mathfrak c\in(0,1)$ with $J_3\ge1$,

$$(1-\alpha-\alpha')\,J_3\ \le\ N^\star\ \le\ 4R\Big\lceil\ln(2/\alpha)\exp\Big(\big(\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})}\big)^2\Big)\Big\rceil .$$

Hence $\ln N^\star=(1+o(1))\,\mathfrak e$ as $\mathfrak e\to\infty$ with $\mathfrak e/d\to0$ and $\ln R=o(\mathfrak e)$, with $\epsilon_{\mathrm{acc}}$, $\alpha$, $\alpha'$ and $\eta$ fixed and $\Delta$ chosen so that the condition holds. In units of $(R-1)B_A^2/\sigma^2$ the constant is $1/2$.

Label. Proven, (a) to (e) and the corollary.

Proof of (a). Fix a learning function, a $B_A$-deviating strategy, an adversary that plays it, $b=0$ and $\Delta$. The case $b=1$ is the same with the hypotheses exchanged.

Step 0, no stop. Let the continued strategy play as the given one until it would stop, and then play $u_t=u^{\mathrm{pr}}_t$ and never stop. It is $B_A$-deviating. On the space of step 1 of the proof of thm-dataflow-composition (b), the two executions of $\mathsf{Ex}_0$ compute the same maps from the same past in every round before the stop. So the exceedance of the stopping strategy is a maximum over a subset of the rounds of the continued one, and its $\epsilon_0(\Delta)$ is at most that of the continued strategy. It suffices to treat strategies that never stop.

Step 1, the execution as a function of $(\Omega,y_{<t})$. Work on the space of step 1 of thm-dataflow-composition (b), with the randomness of every node indexed by the node (ch-reference-strategy, item 2). Let $\Omega=(\omega,\zeta_1,\dots,\zeta_R)$, and let $Z_1,\dots,Z_R$ be independent of $\Omega$. Consider $\mathsf{Ex}_0$ on this space under the given strategy and under the protocol's strategy. By that step, the value of every node other than the input node of $D_j$, the $v_t$ and the $r_t$, and the adversary's state, are measurable functions of $\omega$, of the releases already made and of the revealed seeds, hence of $\Omega$ and the past releases. Three facts make these maps the same under both strategies, except for the values of the coalition's input nodes and the adversary's state. The coalition's input nodes of round $t$ have the single child $r_t$, so their values reach later nodes only through $y_t$. Every other argument and value that the coalition sets is the protocol's, the same function of node values under both strategies. The randomness of each node is the same coordinate of $\omega$ under both strategies, whatever oracle calls the adversary makes on its own. By induction over the order of $G$, there are measurable maps, the same under both strategies, that give $c_t$, $W_t$, $W'_t$, $o_t$ and $u^{\mathrm{pr}}_t$ as functions of $(\Omega,y_{<t})$. The prescribed input is among them because it reads node values other than the coalition's input nodes, and every such node runs before $r_t$. Write $\bar y_t=o_t+f_t(c_t,W_t)$. Under the given strategy the input $u_t$ is a measurable function of the adversary's state when it sets the input nodes of round $t$, hence of $(\Omega,y_{<t})$, with $\|u_t-u^{\mathrm{pr}}_t\|\le B_A$. Under the protocol's strategy $u_t=u^{\mathrm{pr}}_t$. In both, $y_t=u_t+\bar y_t+Z_t$. The exceedance $D^\star_0$ is computed from $c_t$, $W_t$ and $W'_t$ for $t\le R$, and $c_R$ is set before $v_R$ runs, so $\{D^\star_0>\Delta\}=\{(\Omega,y_{<R})\in\mathbb A\}$ for one measurable set $\mathbb A$, the same under both strategies.

Step 2, the density. Let $\mathbb P^{\mathrm{dev}}$ and $\mathbb P^{\mathrm{pr}}$ be the laws of $(\Omega,y_1,\dots,y_{R-1})$ under the given strategy and under the protocol's strategy. $\Omega$ has the same law under both. Given $(\Omega,y_{<t})$, which is a function of $(\Omega,Z_{<t})$, the noise $Z_t$ is independent, so $y_t$ has law $\mathcal N(u_t+\bar y_t,\sigma^2I_d)$ under $\mathbb P^{\mathrm{dev}}$ and $\mathcal N(u^{\mathrm{pr}}_t+\bar y_t,\sigma^2I_d)$ under $\mathbb P^{\mathrm{pr}}$. By the chain rule for kernels both laws have positive densities with respect to the product of the law of $\Omega$ and Lebesgue measure on $(\mathbb R^d)^{R-1}$, and

$$\frac{d\mathbb P^{\mathrm{dev}}}{d\mathbb P^{\mathrm{pr}}}=\prod_{t<R}\mathfrak r_t,\qquad\mathfrak r_t=\frac{\varphi_\sigma(y_t-\bar y_t-u_t)}{\varphi_\sigma(y_t-\bar y_t-u^{\mathrm{pr}}_t)} .$$

Step 3, the moment. Let $\mathcal F^{\mathrm{rel}}_t$ be generated by $\Omega$ and $y_{<t}$. Under $\mathbb P^{\mathrm{pr}}$, given $\mathcal F^{\mathrm{rel}}_t$, the vector $y_t-\bar y_t-u^{\mathrm{pr}}_t$ has law $\mathcal N(0,\sigma^2I_d)$ and $u_t-u^{\mathrm{pr}}_t$ is fixed. So (F6) gives

$$\mathbb E_{\mathrm{pr}}\big[\mathfrak r_t^{\varpi}\,\big|\,\mathcal F^{\mathrm{rel}}_t\big]=\exp\Big(\frac{\varpi(\varpi-1)\|u_t-u^{\mathrm{pr}}_t\|^2}{2\sigma^2}\Big)\le\exp\Big(\frac{\varpi(\varpi-1)B_A^2}{2\sigma^2}\Big).$$

The factors $\mathfrak r_s$ with $s<t$ are $\mathcal F^{\mathrm{rel}}_t$-measurable, so the tower property and induction over $t<R$ give

$$\mathbb E_{\mathrm{pr}}\Big(\frac{d\mathbb P^{\mathrm{dev}}}{d\mathbb P^{\mathrm{pr}}}\Big)^{\varpi}\le\exp\big(\varpi(\varpi-1)\,\mathfrak e\big).$$

Step 4, the transfer. $\epsilon_0(\Delta)=\mathbb P^{\mathrm{dev}}(\mathbb A)$ and $\epsilon^{\mathrm{pr}}_0(\Delta)=\mathbb P^{\mathrm{pr}}(\mathbb A)$. (F6) with $g=\mathbf 1_{\mathbb A}$ gives $\mathbb P^{\mathrm{dev}}(\mathbb A)\le\mathbb P^{\mathrm{pr}}(\mathbb A)^{1-1/\varpi}e^{(\varpi-1)\mathfrak e}$, the first display. For the closed form let $p=\mathbb P^{\mathrm{pr}}(\mathbb A)\in(0,1]$, $\mathfrak l=\ln(1/p)$ and $q=\varpi-1>0$. The logarithm of the right side is $-\mathfrak lq/(1+q)+q\mathfrak e$, with derivative $\mathfrak e-\mathfrak l/(1+q)^2$ in $q$. If $\mathfrak l\le\mathfrak e$ it is nondecreasing, and its infimum over $q>0$ is its limit $0$ at $q\to0$. If $\mathfrak l>\mathfrak e>0$ its minimum is at $1+q=\sqrt{\mathfrak l/\mathfrak e}$, with value $-\mathfrak l+2\sqrt{\mathfrak l\mathfrak e}-\mathfrak e=-(\sqrt{\mathfrak l}-\sqrt{\mathfrak e})^2$. If $\mathfrak e=0$ its infimum is $-\mathfrak l$, approached as $q\to\infty$. In all cases the infimum of the right side is $\Upsilon_{\mathfrak e}(p)$. For $p=0$ the first display gives $\epsilon_0(\Delta)=0$. The bounds on the targets are thm-dataflow-composition (b), applied to each adversary through its terms $\epsilon_0$ and $\epsilon_1$. $\square$

Proof of (b). The experimenter holds every input and plays the protocol's strategy. In each round it calls $\mathsf{Train}(x(c_t,D^b_j,W_{t-1}),\bot)$, which returns a seed name $s$, and then $\mathsf{Train}(x(c_t,D^{1-b}_j,W'_{t-1}),s)$, holding both states as models of its own calls. It runs the other nodes as the procedure prescribes. The runs are independent by fidelity, so the indicators of an exceedance above $\Delta$ are independent Bernoulli variables with parameter $\epsilon^{\mathrm{pr}}_b(\Delta)$, and $\Pr[\epsilon^{\mathrm{pr}}_b(\Delta)\le\bar\epsilon_b]\ge1-\alpha$ by the coverage of the Clopper and Pearson bound. $\Upsilon_{\mathfrak e}$ is nondecreasing on $[0,1]$, so on that event (a) gives soundness. With no exceedance, $\bar\epsilon_b=1-\alpha^{1/N'}\le\ln(1/\alpha)/N'\le\exp(-(\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)$. Then $\sqrt{\ln(1/\bar\epsilon_b)}-\sqrt{\mathfrak e}\ge\sqrt{\ln(1/\epsilon_{\mathrm{acc}})}$, so $\Upsilon_{\mathfrak e}(\bar\epsilon_b)\le\epsilon_{\mathrm{acc}}$. $\square$

Proof of (c). Let $\mathsf L$ return the starting model at every training input of a round $t<R$ and at $x((R,m),D^0_j)$, and let $\mathsf L(x((R,m),D^1_j);\rho,\xi)=m+2\Delta\mathbf e_1\mathbf 1[\langle m-m_1,\mathbf e_1\rangle>\iota\sigma\sqrt{R-1}]$. Take the strategy $u_t=B_A\mathbf e_1$ for $t<R$ and $u_R=0$, which is admissible. In $\mathsf{Ex}_0$ every round $t<R$ has $W_t=W'_t=m_t$, so its coupled difference is zero and $y_t=u_t+Z_t$. Hence $m_R-m_1=\sum_{t<R}(u_t+Z_t)$. In round $R$ the base is $m_R$ and the twin differs from it by $2\Delta\mathbf e_1$ exactly when $\langle m_R-m_1,\mathbf e_1\rangle>\iota\sigma\sqrt{R-1}$, and $\mathrm{clip}_B(2\Delta\mathbf e_1)=2\Delta\mathbf e_1$ since $B\ge2\Delta$. So the exceedance is above $\Delta$ exactly on that event. Under the protocol's strategy $\langle m_R-m_1,\mathbf e_1\rangle$ has law $\mathcal N(0,(R-1)\sigma^2)$, which gives $\epsilon^{\mathrm{pr}}_0(\Delta)=\bar\Phi(\iota)$. Under the strategy the mean is $(R-1)B_A$, and $(R-1)B_A/(\sigma\sqrt{R-1})=\sqrt{2\mathfrak e}$, which gives $\epsilon_0(\Delta)=\bar\Phi(\iota-\sqrt{2\mathfrak e})$.

For the inequality, by (F4), for $r\ge1$, $r^2/2\le\ln(1/\bar\Phi(r))\le r^2/2+\ln(r+1/r)+1$, since $\tfrac12\ln(2\pi)<1$ and $\ln r\ge0$. At $r=\iota$, $\sqrt{\ln(1/\bar\Phi(\iota))}\ge\iota/\sqrt2$, so $\ln(1/\Upsilon_{\mathfrak e}(\bar\Phi(\iota)))=(\sqrt{\ln(1/\bar\Phi(\iota))}-\sqrt{\mathfrak e})_+^2\ge(\iota-\sqrt{2\mathfrak e})^2/2$. At $r=\iota-\sqrt{2\mathfrak e}\ge1$, $\ln(1/\bar\Phi(r))\le r^2/2+\ln(\iota+1)+1$. The two give the display, with room. For the last claim, every $p\in(0,1/2)$ equals $\bar\Phi(\iota)$ for one $\iota>0$. If $\epsilon_0\le F(\epsilon^{\mathrm{pr}}_0)$ in every instance, then $\ln(1/F(\bar\Phi(\iota)))\le\ln(1/\epsilon_0(\Delta))\le\ln(1/\Upsilon_{\mathfrak e}(\bar\Phi(\iota)))+2\ln(\iota+1)+2$. The right side grows like $\iota^2/2$, so the ratio tends to at most one. $\square$

Proof of (d). The first two claims are round 04, proof of thm-smoothed-choice-certificate (d). At $\mathsf L^\circ$ every release is $y_t=u_t+Z_t$ under both hypotheses, the transcript is a function of $(\omega,y_{\le R},\bar\rho_{\le R})$, whose law is the same under both, and the model ignores the dataset.

The code. Let $J\le J_3$ with $J\ge1$. Draw $\mathbf q_1,\dots,\mathbf q_J$ independently and uniformly from $\{-d^{-1/2},d^{-1/2}\}^d$. For $k\neq l$, $d\langle\mathbf q_k,\mathbf q_l\rangle$ is a sum of $d$ independent uniform signs, so (F8) gives $\Pr[|\langle\mathbf q_k,\mathbf q_l\rangle|\ge\mathfrak c]\le2e^{-\mathfrak c^2d/2}$. A union bound over the $J(J-1)/2$ pairs bounds the probability of a bad pair by $J(J-1)e^{-\mathfrak c^2d/2}<J^2e^{-\mathfrak c^2d/2}\le1$ when $J\ge2$, because $J\le e^{\mathfrak c^2d/4}$. So some draw gives unit vectors with $|\langle\mathbf q_k,\mathbf q_l\rangle|<\mathfrak c$ for every pair.

The cells. Write $\mathfrak m=(R-1)B_A$ and $\mathfrak v=\sigma\sqrt{R-1}$, so $\mathfrak m/\mathfrak v=\sqrt{2\mathfrak e}$. Let

$$V_k=\big\{m\in\mathbb R^d:\ \langle m-m_1,\mathbf q_k\rangle>\mathfrak m-\mathfrak q_\eta\mathfrak v,\ \ \langle m-m_1,\mathbf q_l\rangle\le\mathfrak m-\mathfrak q_\eta\mathfrak v\ \text{ for every }l\neq k\big\}.$$

Each $V_k$ is a finite intersection of half-spaces, and a point of $V_k\cap V_l$ with $k\neq l$ would satisfy both $\langle m-m_1,\mathbf q_l\rangle>\mathfrak m-\mathfrak q_\eta\mathfrak v$ and its negation. So the cells are measurable and pairwise disjoint. Let $G\sim\mathcal N(0,\mathfrak v^2I_d)$. Then $m_1+\mathfrak m\mathbf q_k+G$ lies outside $V_k$ only if $\langle G,\mathbf q_k\rangle\le-\mathfrak q_\eta\mathfrak v$, or if $\mathfrak m\langle\mathbf q_k,\mathbf q_l\rangle+\langle G,\mathbf q_l\rangle>\mathfrak m-\mathfrak q_\eta\mathfrak v$ for some $l\neq k$, which needs $\langle G,\mathbf q_l\rangle>(1-\mathfrak c)\mathfrak m-\mathfrak q_\eta\mathfrak v$. Each $\langle G,\mathbf q_l\rangle$ has law $\mathcal N(0,\mathfrak v^2)$. $J_3\ge1$ forces $(1-\mathfrak c)\sqrt{2\mathfrak e}-\mathfrak q_\eta>0$, since otherwise the second argument of the minimum is $\lfloor\eta/2\rfloor=0$. So (G3) applies, and

$$\Pr[m_1+\mathfrak m\mathbf q_k+G\notin V_k]\le\frac\eta4+(J-1)\,\bar\Phi\big((1-\mathfrak c)\sqrt{2\mathfrak e}-\mathfrak q_\eta\big)\le\frac\eta4+\frac J2\exp\Big(-\tfrac12\big((1-\mathfrak c)\sqrt{2\mathfrak e}-\mathfrak q_\eta\big)^2\Big)\le\frac\eta2 .$$

The needles. Let $X_k=\{x((R,m),D^1_j):m\in V_k\}$. The map $m\mapsto x((R,m),D^1_j)$ is measurable and injective, so the $X_k$ are pairwise disjoint Borel sets (Lusin and Souslin). Let $\mathsf L_k$ agree with $\mathsf L^\circ$ except that $\mathsf L_k(x((R,m),D^1_j);\rho,\xi)=m+B\mathbf e_1$ for $m\in V_k$. Take the strategy $u_t=B_A\mathbf q_k$ for $t<R$ and $u_R=0$, which is admissible, and the adversary that only reads the releases. In a round $t<R$ the training input carries the learner name $\ell_t\neq\ell_R$, so $\mathsf L_k$ returns the starting model and $y_t=B_A\mathbf q_k+Z_t$ under both hypotheses. Hence $m_R=m_1+\mathfrak m\mathbf q_k+\sum_{t<R}Z_t$ is a function of $y_{<R}$, whose law is the same under both hypotheses, and $\sum_{t<R}Z_t\sim\mathcal N(0,\mathfrak v^2I_d)$. In round $R$, $y_R=Z_R$ under $H_0$, and $y_R=B\mathbf e_1\mathbf 1[m_R\in V_k]+Z_R$ under $H_1$, since $\mathrm{clip}_B(B\mathbf e_1)=B\mathbf e_1$. The averaging identity (F2), with $y_{<R}$ as the common coordinate, and (G1) give

$$\mathrm H_\gamma(P_0\|P_1)=\Pr[m_R\in V_k]\;\delta_{\mathcal N}(\varepsilon;B/\sigma)\ge(1-\eta/2)\,\delta_{\mathcal N}(\varepsilon;B/\sigma).$$

So $\theta^{\mathrm{agg}}_R(\mathsf L_k)\ge(1-\eta/2)\delta_{\mathcal N}(\varepsilon;B/\sigma)$ for every $k\le J$, and lem-needle-lower-bound with $\vartheta=(1-\eta/2)\delta_{\mathcal N}(\varepsilon;B/\sigma)$ and $J=J_3$ gives the bound.

The expansion. Let $\mathfrak c=2\sqrt{\mathfrak e/d}<1$, so $\mathfrak c^2d/4=\mathfrak e$. Let $J'=\frac\eta2\exp(\frac12((1-\mathfrak c)\sqrt{2\mathfrak e}-\mathfrak q_\eta)^2)$ be the second argument before rounding. Since $0\le\mathfrak q_\eta\le(1-\mathfrak c)\sqrt{2\mathfrak e}$, $((1-\mathfrak c)\sqrt{2\mathfrak e}-\mathfrak q_\eta)^2\ge2(1-\mathfrak c)^2\mathfrak e-2(1-\mathfrak c)\sqrt{2\mathfrak e}\,\mathfrak q_\eta$, so $\ln J'\ge(1-\mathfrak c)^2\mathfrak e-\mathfrak q_\eta\sqrt{2\mathfrak e}+\ln(\eta/2)\ge(1-2\mathfrak c)\mathfrak e-\mathfrak q_\eta\sqrt{2\mathfrak e}+\ln(\eta/2)$. Also $\ln J'\le(1-\mathfrak c)^2\mathfrak e+\ln(\eta/2)<\mathfrak e$, so $J_3=\lfloor J'\rfloor$. For $J'\ge1$, $\lfloor J'\rfloor\ge J'/2$, and $2\mathfrak c=4\sqrt{\mathfrak e/d}$ gives the bound. $\square$

Proof of (e). This is thm-smoothed-choice-certificate (e), round 04. Its pair code uses the strengthened thm-dataflow-composition (e)(ii) in round 1, and it gives a learning function at which every coupled pair coincides. There every run of $\mathsf{Ex}_b$ under the protocol's strategy has no exceedance, so $\bar\epsilon_b=1-\alpha^{1/N'}\le\ln(1/\alpha)/N'$, and $\Upsilon_{\mathfrak e}$ is nondecreasing. $\square$

Proof of the corollary. Lower bound. A certifier that outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<\vartheta$ at $\mathsf L^\circ$ with probability at least $1-\alpha'$ has $\Pr_{\mathsf L^\circ}[\hat t\ge\vartheta]\le\alpha'$, so (d) gives $\alpha'\ge1-\alpha-N/J_3$. Upper bound. Let $\hat t=\max\{\hat t_0,\hat t_1\}$ with each certificate of (b) at level $\alpha/2$ and $N'=\lceil\ln(2/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)\rceil$ runs. A union bound makes both sound together with probability at least $1-\alpha$, so $\hat t$ is sound for $\theta^{\mathrm{agg}}_R$. In $G^{\mathrm{agg}}_R$ each run costs $2R$ Train calls, so $N=4RN'$. At $\mathsf L^\circ$ no run exceeds $\Delta$, and (b) gives the output with certainty. Asymptotics. The upper bound gives $\ln N^\star\le\ln(4R)+\ln(\ln(2/\alpha)+1)+(\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2=\mathfrak e+O(\sqrt{\mathfrak e})+\ln R$, which is $(1+o(1))\mathfrak e$ when $\ln R=o(\mathfrak e)$. With $\mathfrak c=2\sqrt{\mathfrak e/d}$, once $\mathfrak e/d<1/4$ and $\mathfrak e$ is large enough that $(1-\mathfrak c)\sqrt{2\mathfrak e}\ge\mathfrak q_\eta$ and $J'\ge1$, the lower bound gives $\ln N^\star\ge\ln(1-\alpha-\alpha')+\mathfrak e(1-4\sqrt{\mathfrak e/d})-\mathfrak q_\eta\sqrt{2\mathfrak e}+\ln(\eta/4)$, which is $(1-o(1))\mathfrak e$ when $\mathfrak e/d\to0$. $\square$

Remark, fixed ratio. With $c=\mathfrak e/d$ fixed and $\mathfrak c=2\sqrt c/(1+2\sqrt c)$, both arguments of $J_3$ have exponent $\mathfrak e/(1+2\sqrt c)^2-O(\sqrt{\mathfrak e})$, so $\liminf\ln N^\star/\mathfrak e\ge(1+2\sqrt c)^{-2}$ (proven, by (d) and the computation of the expansion). Open problem 5 asks for the limit.

Without the oracle. A privacy bound against a coalition that moves client $j$'s next starting model through the aggregate needs the law of the trained transformer at every starting model the coalition can reach. That set is a ball of dimension $d$ around a Gaussian random walk, and with state it is every reachable history. With clipping the worst-case bound $\delta_{\mathcal N}(\varepsilon;2\sqrt RB/\sigma)$ needs no call but tends to one as $B/\sigma$ grows, and without clipping no bound exists. With the oracle, part (a) reduces every deviation of norm at most $B_A$ to one Bernoulli parameter of the protocol's own execution, which coupled Train calls measure. Part (b) certifies it at a cost exponential in $\mathfrak e$ and free of $d$, of $B$, of the state and of the architecture. Parts (c) and (d) show that neither the transfer function nor the price can be improved to first order when $\mathfrak e\ll d$. Criteria 1 to 3 hold. $\epsilon^{\mathrm{pr}}_b$ is defined by coupled Train calls, the problem without the oracle needs the law of the trained model on a continuum of starting models, and the bound depends on the learning function only through $\epsilon^{\mathrm{pr}}_b$.

Degenerate oracles. Part (a) is a statement about laws and holds under the bottom and the top oracle, because thm-dataflow-composition (b) does and the change of measure acts on the release noise, which neither policy reveals. Under the seed-revealing policy the input may read client $j$'s seed of the same round, which step 1 allows. Parts (b) and (d) concern the experimenter. In the drawn-seed discipline the certificate of (b) fails, by (e), at every $B_A\ge0$. A drawn-seed certifier that outputs below $1-(1+\gamma)e^{-B^2/(16\sigma^2)}$ with probability above $\alpha+\eta$ at the reference function of (e) needs about $\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$ runs for $d\ge6$, while (b) outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}$ there. So the theorem meets criterion 4 through its certificate, under item 3 of def-degenerate-oracles. The criterion-4 content is inherited from the pair code of thm-dataflow-composition (e). The new content, the transfer from the protocol's strategy, its tightness and the sharp lower bound, holds in both disciplines where it concerns lower bounds.

Non-triviality, requested. Criteria 1 to 3 hold, as the paragraph "Without the oracle" says. Criterion 4 holds through the certificate (b) under item 3 of def-degenerate-oracles, by (e). I ask for ACCEPT NONTRIVIAL.

Prior work. Step 3 is the adaptive composition of the Rényi divergence of the Gaussian mechanism, and step 4 is its probability-preservation property (Mironov, IEEE CSF 2017, https://arxiv.org/abs/1702.07476, search summary in round 04, the property from memory). The use differs. The transfer carries a certificate measured on the protocol's strategy to every strategy within $B_A$ of it. Part (d) is the adversary argument of lem-needle-lower-bound with a nearly orthogonal code, whose construction by random signs and Hoeffding's inequality is textbook. A search in round 04 found no certificate against an adaptive norm-bounded coalition whose learning-specific term is a tail measured by training runs. Novelty of (a) to (d) stays open until the auditing literature on active adversaries is read.

### Smoothed-choice certificate, after the split [thm-smoothed-choice-certificate]

What remains. Parts (a), (b), (d) and (e) of round 04 stand, with their proofs, in $G^{\mathrm{agg}}_R$. Part (c) is now thm-bounded-deviation-transfer (a) and (b), in the reference-strategy form, which contains it since the prescribed input of $G^{\mathrm{agg}}_R$ is zero. The corollary moves to thm-bounded-deviation-transfer, with $J_3$ in place of $J_1$ when $\mathfrak e\ll d$. Part (d) keeps its two packings. The ball packing $J_2$ is the only lower bound of the theory whose exponent grows faster than $d$ once $\mathfrak e/d$ is large, and the sphere code $J_1$ beats $J_3$ at the ratios $\mathfrak e/d$ between $1/4$ and about $1.45$ (computed, by comparing $\mathfrak e/4$ and $0.18\,d\ln2$ with $\mathfrak e/(1+2\sqrt{\mathfrak e/d})^2$). The exceedance event of round $t$ in the proof of (a) is $\mathcal E_t$, the event of no exceedance up to round $t$ is $\mathcal I_t$, and the separation of lem-sphere-code (b) is $\mathfrak s$.

Statement of the label. Proven, (a), (b), (d) and (e). The register line now reads "A coalition client with inputs of norm at most $B_A$ is bounded through a product of smoothed tails on escape balls and certified by a covering, every certifier sound for all learning functions pays a number of Train calls exponential in the smaller of $d$ and $(R-1)B_A^2/\sigma^2$, and drawn seeds fail."

Application paragraph, corrected (ch-euclidean-norm-proof). In the release procedure of thm-dataflow-composition (a)(ii) under $\mathcal F^{\mathrm{dev}}$ with the abort set, the coalition's inputs are the nodes $a_{t,i}$, whose only child is $r_t$, and a delivered value other than $y_t$ is a stop. If every coalition client proves in zero knowledge that the Euclidean norm of the difference between its input and its prescribed input is at most $B_A/k_A$, with $k_A$ the number of coalition clients, then every strategy of the coalition is $B_A$-deviating and thm-bounded-deviation-transfer (b) certifies it, with the realization error of (a)(ii) added (proven, given that error). A proof that bounds each coordinate by $b_\infty$ gives only $B_A=k_A\sqrt d\,b_\infty$ (proven).

### Dataflow composition, two clarifications [thm-dataflow-composition]

Step 1 of (b), randomness by node. The variable $\omega$ collects the adversary's coins, an independent sequence of triples $(\rho',\xi',\upsilon')\sim\mu\otimes\pi\otimes\nu$ for the oracle calls that the adversary makes beyond those the procedure requires, used in order, the randomness of every node other than $v_1,\dots,v_R$, including the oracle's draws for the calls that the procedure requires of the coalition's nodes, and the randomness of each $r_t$ other than $Z_t$. By fidelity the execution has the same law as with the order-based assignment of round 03, so every statement of the theorem and every proof that cites step 1 stands. The node-indexed form makes the maps of step 1 independent of the adversary's own calls, which thm-bounded-deviation-transfer uses.

Reading of (a)(iii), one sentence added. The bound applies when the decryptors add the protecting noise at decryption. If client $j$ adds its noise inside its ciphertext, the scalar multiplies that noise too, and (ii) becomes $1-(1+\gamma)\bar\Phi((\mathfrak d/2-e_{\max}/a)/\sigma)$, so the attack removes at most the decryption error (proven, by the computation of (ii) with $aZ_1$ in place of $Z_1$).

### Bank soundness, reason for the withdrawal [thm-bank-soundness]

The second half of (d) is withdrawn because subsampling is a node of the procedure, and no theorem of this theory uses it, so the question is out of scope. The label is unchanged. Proven, (a), (b) and the first half of (d). Heuristic, (c).

## The final draft

`final/learning-oracle-theory.md` opens with a two-minute statement of the problem, the idea and the six main results, then gives the five definitions that the presented proofs need and the standing facts. It presents in full lem-needle-lower-bound, lem-sphere-code, thm-coupling-certificate (a) and (b), thm-dataflow-composition (b), (c) and (e)(ii), thm-bounded-deviation-transfer, thm-replay-audit-steer (a) and (b), and thm-black-box-certifiability (o) and (a), each with its statement, label, "Without the oracle" paragraph, degenerate oracles and proof. Every other accepted result is stated in one or two sentences with a pointer to the round file and section that proves it, and the open problems are yes-or-no questions.

## Questions for the challenger

1. Step 1 of thm-dataflow-composition (b) now indexes the randomness of the procedure's nodes by node. Do you accept this as a clarification that changes no statement, and the use that step 1 of thm-bounded-deviation-transfer makes of it?
2. The fifth theorem section of the final document is thm-black-box-certifiability (o) and (a), chosen because it is the only result on the query channel and answers Küpçü's question on white-box and black-box access. Would you rather see thm-perfect-substitution or thm-active-choice-dichotomy (a)(i) there?
3. Open problem 5 now asks whether $\lim\ln N^\star/\mathfrak e=\ln(1+2c)/(2c)$ at a fixed ratio $c=\mathfrak e/d$. Do you hold the capacity value as the right conjecture, given that it rests on a heuristic about the channel from the coalition's choice to $m_R$?
