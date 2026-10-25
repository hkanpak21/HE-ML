# Round 06, builder

Verdict of this turn. The three blocking challenges are closed, each with the one-sentence fix that round 05 asked for. ch-scalar-direction now states where the noise must sit. ch-opening-hypotheses restores the hypotheses of every opening summary, and ch-tightness-round-count restores $R\ge2$. The eight other challenges are accepted, two of them with one part disputed. Under ch-draft-symbols the proposed name $\mathbf b_t$ would clash by font with the hypothesis bit $b$, so the symbol is removed instead. Under ch-feedback-capacity the option "add $R\to\infty$" is rejected, because a steering code keeps the feedback gain as $R\to\infty$ (heuristic, computed below). Two pieces of mathematics change. Part (c) of [thm-bounded-deviation-transfer] now states the factor form, proven below. Open problem 5 now compares $N^\star$ with a feedback needle count $J^{\mathrm{fb}}$, and $N^\star\ge(1-\alpha-\alpha')J^{\mathrm{fb}}$ is proven below. No new theorem is added. Every symbol clash that the challenger listed, and six more, are resolved in `final/learning-oracle-theory.md` and in `theory/CURRENT.md`. The final document has 18 pages, and `node scripts/verify.mjs final` prints `FINAL OK theorems=5 nontrivial=5 items=21`.

Notation follows `theory/CURRENT.md` after this round. Every claim carries one of the labels proven, heuristic or open.

## Responses to challenges

### ch-scalar-direction

Accepted. The paragraph "The other parts, stated" of [thm-dataflow-composition] in the final document now reads as follows. "Unchecked decryption lets a public scalar divide the protecting noise when the decryptors add it at decryption. Noise that client $j$ adds inside its ciphertext scales with the update, and the scalar then removes at most the decryption error (proven, round-04/builder.md and round-05/builder.md)." The register line of the theorem in `theory/CURRENT.md` carried the same omission. It now says that the scalar leaks the encoded update when the decryptors add the noise at decryption. When client $j$ adds the noise inside its ciphertext, the scalar removes at most the decryption error.

### ch-opening-hypotheses

Accepted, all four items. The opening list of the final document now reads as follows.

1. "Coupling certificate. One training node leaks at most the coupled divergence, which coupled Train calls certify for every learning function. Through a deterministic channel with atomless view laws, drawn seeds certify nothing below one (proven)."
2. "Black-box certifiability. Label-only leakage at a fixed number of queries is certifiable from both sides. With deterministic evaluation and atomless model laws, no experiment with drawn seeds certifies that it equals white-box leakage (proven)."
3. Item 3 now names the exceedance probability, so that item 4 can use the term. "Over $R$ Gaussian releases, leakage is at most a Gaussian privacy term plus the exceedance probability, the probability that coupled updates differ by more than a threshold. Coupled runs of a fixed strategy certify that probability free of $d$ (proven)."
4. "Bounded-deviation transfer. If a coalition's additive inputs stay within $B_A$ of the prescribed ones, its exceedance probability is at most a fixed function of the protocol's, set by $\mathfrak e=(R-1)B_A^2/(2\sigma^2)$. Coupled runs of the protocol certify it at level $\alpha$ with about $e^{\mathfrak e}\ln(1/\alpha)$ runs, free of $d$. In the aggregation instance, a certifier sound for every learning function and accurate where the leakage is zero needs $e^{(1-o(1))\mathfrak e}$ Train calls when $\mathfrak e/d\to0$ (proven)."
5. "Replay-audit steering. With seeds from a random oracle, a prover lands training in a target set with probability at most a multiple of its reach. Under deterministic kernels grinding attains it within a factor $3.2$ if the reach times the number of oracle queries is at most one (proven)."

Two additions go beyond the challenger's text, and both restore a hypothesis. First, item 4 says "accurate where the leakage is zero". Without it the sentence is false, since a certifier that always outputs one is sound and makes no Train call (proven, by inspection). The corollary defines $N^\star$ over certifiers that are sound and accurate at $\mathsf L^\circ$, where $\theta^{\mathrm{agg}}_R=0$. Second, item 5 states the condition $q_{\mathsf{RO}}\,p_\tau(T)\le1$ of [thm-replay-audit-steer] (c) in words. The sentence that defines $R$, $\sigma$, $d$ and $B_A$ now also defines $\alpha$ as the error probability of a certifier, since item 4 uses it.

### ch-tightness-round-count

Accepted. Part (c) of [thm-bounded-deviation-transfer] in the final document begins "In $G^{\mathrm{agg}}_R$ let $R\ge2$, $B_A>0$ and $B\ge2\Delta$." The proof now says where it uses $R\ge2$. "The coordinate $\langle m_R-m_1,\mathbf e_1\rangle$ is $\mathcal N(0,(R-1)\sigma^2)$ under the protocol's strategy, with $R-1\ge1$." It also fixes $\mathbf u_R=0$, which the round-05 draft left open. It says that rounds $t<R$ have no exceedance, because $\mathsf L$ returns the starting model at their inputs, whose learner names differ from $\ell_R$.

### ch-tightness-first-order

Accepted. The challenger is right that the limsup sentence holds for every admissible function, since $F(p)\ge p$ and $\ln(1/p)/\ln(1/\Upsilon_{\mathfrak e}(p))\to1$ at fixed $\mathfrak e$ (proven, round-05/challenger.md). The last sentence of (c) is replaced by the factor form.

Statement. In $G^{\mathrm{agg}}_R$ let $R\ge2$, $B_A>0$ and $B\ge2\Delta$. Let $F$ satisfy $\epsilon_0(\Delta)\le F(\epsilon^{\mathrm{pr}}_0(\Delta))$ in every instance of $G^{\mathrm{agg}}_R$ with these $R$, $B_A$, $\sigma$, $\Delta$ and $B$. Then for every $p\in(0,\bar\Phi(\sqrt{2\mathfrak e}+1))$

$$F(p)\ \ge\ \frac{e^{-2}\,\Upsilon_{\mathfrak e}(p)}{8\ln(1/p)},\qquad\text{while}\qquad\frac{\Upsilon_{\mathfrak e}(p)}{p}=\exp\Big(2\sqrt{\mathfrak e\ln(1/p)}-\mathfrak e\Big).$$

So no such $F$ improves on $\Upsilon_{\mathfrak e}$ by more than a factor $8e^2\ln(1/p)$, while $\Upsilon_{\mathfrak e}(p)/p$ is unbounded as $p\to0$. Label. Proven.

Proof. The map $\iota\mapsto\bar\Phi(\iota)$ is a bijection from $(\sqrt{2\mathfrak e}+1,\infty)$ onto $(0,\bar\Phi(\sqrt{2\mathfrak e}+1))$, so $p=\bar\Phi(\iota)$ for one $\iota>\sqrt{2\mathfrak e}+1>1$. The first part of (c) gives an instance with $\epsilon^{\mathrm{pr}}_0(\Delta)=p$ and $\ln(1/\epsilon_0(\Delta))\le\ln(1/\Upsilon_{\mathfrak e}(p))+2\ln(\iota+1)+2$. By (F6)(iii) of the final document, $p\le\frac12e^{-\iota^2/2}$, so $\ln(1/p)\ge\iota^2/2$. Since $\iota>1$, $(\iota+1)^2<4\iota^2\le8\ln(1/p)$, so $2\ln(\iota+1)\le\ln(8\ln(1/p))$. Since $F(p)\ge\epsilon_0(\Delta)$, $\ln(1/F(p))\le\ln(1/\Upsilon_{\mathfrak e}(p))+\ln(8\ln(1/p))+2$, which is the first display. For the second, $\ln(1/p)\ge\iota^2/2>(\sqrt{2\mathfrak e}+1)^2/2>\mathfrak e$, so the positive part in $\Upsilon_{\mathfrak e}$ is the square itself. Then $\ln(\Upsilon_{\mathfrak e}(p)/p)=\ln(1/p)-(\sqrt{\ln(1/p)}-\sqrt{\mathfrak e})^2=2\sqrt{\mathfrak e\ln(1/p)}-\mathfrak e$, which tends to infinity as $p\to0$ when $\mathfrak e>0$. And $\mathfrak e>0$ since $R\ge2$ and $B_A>0$. $\square$

The same change reaches three other places. The "Without the oracle" paragraph of the final document now says "Part (c) shows that no transfer function beats $\Upsilon_{\mathfrak e}$ by more than a factor logarithmic in $1/\epsilon^{\mathrm{pr}}_0(\Delta)$. Part (d) and the corollary show that the logarithm of the cost of (b) is optimal to first order when $\mathfrak e\ll d$." The second sentence keeps "first order", which is correct for the price, since $\ln N^\star=(1+o(1))\mathfrak e$. The register line of `theory/CURRENT.md` now says "The transfer function is tight up to a factor logarithmic in the inverse of the protocol's exceedance probability." The verdict paragraph of round-05/builder.md says that the transfer function "cannot be improved to first order in the exponent". That file is a record and stays as it is. The claim is withdrawn as vacuous and replaced by the factor form above.

### ch-feedback-capacity

Accepted in part. The conjectured value $\ln(1+2\mathfrak a)/(2\mathfrak a)$, with $\mathfrak a=\mathfrak e/d$, is the capacity without feedback, and the coalition sees every release. I checked the challenger's $R=3$ computation. With $B_A^2=\mathfrak a d\sigma^2$, the second input $\mathbf u_2=\mathbf a_2-Z_1$ with $\|\mathbf a_2\|^2\approx B_A^2-d\sigma^2$ leaves $m_3-m_1=\mathbf u_1+\mathbf a_2+Z_2$. The signal-to-noise ratio per coordinate is $(\sqrt{\mathfrak a}+\sqrt{\mathfrak a-1})^2$, which exceeds $2\mathfrak a$ exactly when $2\sqrt{\mathfrak a(\mathfrak a-1)}>1$, that is when $\mathfrak a>(1+\sqrt2)/2$ (proven, by algebra). At $\mathfrak a=4$ the two values per unit of $\mathfrak e$ are $0.338$ and $0.275$ (computed). The capacity reading of these values is heuristic, as the challenger says.

The first option, "add $R\to\infty$ to the limit", is rejected. The challenger's reason for it is that each round's budget $B_A^2=2\mathfrak a d\sigma^2/(R-1)$ covers a vanishing fraction of that round's noise. That is true, and it does not stop the gain. The noise of $m_R$ grows like the square root of the number of rounds, while a coalition that corrects at every round moves $m_R$ linearly. A steering code keeps the gain as $R\to\infty$ (heuristic, below).

The steering code (heuristic). Measure lengths in units of $(R-1)B_A$ and time in units of $R-1$ rounds, so that the noise adds squared norm $d\sigma^2(R-1)/((R-1)B_A)^2=1/(2\mathfrak a)$ per unit of time. The coalition aims at a codeword $\mathbf w$ of norm $a$ and plays $\mathbf u_t=-B_A X_t/\|X_t\|$ with $X_t=m_t-m_1-\mathbf w$, a $B_A$-deviating strategy. Write $X_t$ as $p$ times the unit vector along $-\mathbf w$ plus an orthogonal part of squared norm $q$. In dimension $d$ both coordinates concentrate, with relative fluctuations of order $d^{-1/2}$, so the mean-field equations

$$\frac{dp}{dt}=-\frac{p}{\sqrt{p^2+q}},\qquad\frac{dq}{dt}=-\frac{2q}{\sqrt{p^2+q}}+\frac1{2\mathfrak a},\qquad p(0)=a,\ q(0)=0,$$

describe the path as $R\to\infty$. At $t=1$, $m_R-m_1$ is $(a-p(1))$ times the unit vector along $\mathbf w$ plus a nearly isotropic vector of squared norm $q(1)$. Codewords on a sphere then give about $\exp(\frac d2\ln(1+(a-p(1))^2/q(1)))$ decodable cells, as for a Gaussian channel with that signal-to-noise ratio. Each cell is a needle set of the proof of (d). The table gives the best value of $\ln(1+(a-p(1))^2/q(1))/(2\mathfrak a)$ over $a$, by Euler steps of the equations with step $1/20000$ and a grid over $a$ (computed).

| $\mathfrak a$ | steering, $R\to\infty$ | without feedback | cancellation at $R=3$ | proven lower bound $(1+2\sqrt{\mathfrak a})^{-2}$ |
| --- | --- | --- | --- | --- |
| $0.5$ | $0.980$ | $0.693$ | none, it needs $\mathfrak a\ge1$ | $0.172$ |
| $1$ | $0.930$ | $0.549$ | $0.347$ | $0.111$ |
| $2$ | $0.803$ | $0.402$ | $0.480$ | $0.068$ |
| $4$ | $0.605$ | $0.275$ | $0.338$ | $0.040$ |
| $8$ | $0.405$ | $0.177$ | $0.215$ | $0.023$ |

Every steering value lies below one, as the proven upper bound $\limsup\ln N^\star/\mathfrak e\le1$ requires. The values are heuristic in three places. The mean-field equations replace a random path by its drift, the residual is treated as isotropic, and the count of cells uses the Gaussian capacity formula with maximal error.

The second option is adopted, with the capacity made into a defined quantity. Let $\mathsf L^\circ$ be the reference function of part (d). Let $J^{\mathrm{fb}}$ be the largest number of disjoint Borel sets such that, at $\mathsf L^\circ$, some $B_A$-deviating strategy without oracle calls puts $m_R$ in each with probability at least $1-\eta/2$. The restriction to strategies without oracle calls keeps a strategy's behaviour the same at $\mathsf L^\circ$ and at the needle functions, and the steering code makes no oracle call. Open problem 5 asks whether $\ln N^\star/\mathfrak e$ and $\ln J^{\mathrm{fb}}/\mathfrak e$ have the same limit at fixed $\mathfrak a$. One direction holds at every $\mathfrak e$.

Claim. Under the hypotheses of the corollary of [thm-bounded-deviation-transfer], $N^\star\ge(1-\alpha-\alpha')J^{\mathrm{fb}}$. Label. Proven.

Proof. Let $V_1,\dots,V_J$ be pairwise disjoint Borel sets of models. For each $k$ let a $B_A$-deviating strategy $\mathfrak S_k$ without oracle calls put $m_R$ in $V_k$ with probability at least $1-\eta/2$ at $\mathsf L^\circ$. Let $X_k$ and $\mathsf L_k$ be as in the proof of (d), with $V_k$ in place of the threshold cells. The $X_k$ are disjoint Borel sets, by Lusin and Souslin, and $\mathsf L_k$ agrees with $\mathsf L^\circ$ outside $X_k$. Take the adversary that plays $\mathfrak S_k$ with $\mathbf u_R=0$, reads the releases and makes no other oracle call. In a round $t<R$ the training input carries the learner name $\ell_t\neq\ell_R$, so $\mathsf L_k$ returns the starting model and $y_t=\mathbf u_t+Z_t$ under both hypotheses. The input $\mathbf u_t$ is a function of the adversary's coins and of $y_{<t}$. So the joint law of the coins and $y_{<R}$ is the same under both hypotheses and the same as at $\mathsf L^\circ$. The model $m_R=m_1+\sum_{t<R}y_t$ is a function of $y_{<R}$. In round $R$, $y_R=Z_R$ under $H_0$, and $y_R=B\mathbf e_1\mathbf 1[m_R\in V_k]+Z_R$ under $H_1$, since $\mathrm{clip}_B(B\mathbf e_1)=B\mathbf e_1$. The averaging identity (F5), with the coins and $y_{<R}$ as the common coordinate, and (F6)(i) give $\mathrm H_\gamma(P_0\|P_1)=\Pr[m_R\in V_k]\,\delta_{\mathcal N}(\varepsilon;B/\sigma)\ge\vartheta$, with $\vartheta=(1-\eta/2)\delta_{\mathcal N}(\varepsilon;B/\sigma)$. So $\theta^{\mathrm{agg}}_R(\mathsf L_k)\ge\vartheta$ for every $k$. By [lem-needle-lower-bound] every certifier sound at level $\alpha$ over every learning function satisfies $\Pr_{\mathsf L^\circ}[\hat t\ge\vartheta]\ge1-\alpha-N/J$. A certifier accurate at $\mathsf L^\circ$ outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<\vartheta$ with probability at least $1-\alpha'$, so $\alpha'\ge1-\alpha-N/J$. Taking $J=J^{\mathrm{fb}}$ gives the claim. $\square$

The proof of (d) is this proof with the threshold cells and the straight strategies $\mathbf u_t=B_A\mathbf q_k$. So $J^{\mathrm{fb}}\ge J_3$, and the lower bound $(1+2\sqrt{\mathfrak a})^{-2}$ is a lower bound on $\liminf\ln J^{\mathrm{fb}}/\mathfrak e$ as well. The upper bound of the corollary gives $\limsup\ln J^{\mathrm{fb}}/\mathfrak e\le1$. By the table, the limit of $\ln J^{\mathrm{fb}}/\mathfrak e$, where it exists, is at least the steering value, so it exceeds the value without feedback at every ratio computed (heuristic). It is at most one (proven).

Open problem 5 in `theory/CURRENT.md` now states the question, the claim above as known, the three heuristic computations and the obstacle. The final document states a short form with the same question and the same labels.

### ch-prescribed-input-scope

Accepted. The setting of [thm-bounded-deviation-transfer] now reads as follows. "It is a measurable function of the values of the nodes that the coalition owns or receives through the plain channel before $r_t$ runs, other than these input nodes." The proof is unchanged. Consider every node other than the input node of $D_j$, the $v_t$ and the $r_t$. Step 1 of the proof of [thm-dataflow-composition] (b) writes its value as a measurable function of $\omega$, the releases so far and the revealed seeds. A release received through the plain channel is one of those releases. So the prescribed input is one map of $(\Omega,y_{<t})$ under both strategies (proven). The narrower clause excludes the input node of $D_j$ and every $v_t$, which reach the coalition through channel none by condition 4 of [def-isolated-client]. A protocol whose prescription reads them cannot be played by the coalition, as the challenger showed.

### ch-drawn-seed-regime

Accepted. The paragraph "Degenerate oracles" of [thm-bounded-deviation-transfer] now reads as follows. "At the reference function of (e), the certificate (b) is accurate to $\epsilon_{\mathrm{acc}}$ with $2R\lceil\ln(1/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)\rceil$ Train calls. A drawn-seed certifier needs about $\sqrt{\eta/2}\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$ calls there to output below $1-(1+\gamma)e^{-B^2/(16\sigma^2)}$ with probability above $\alpha+\eta$, by the Reading of thm-dataflow-composition (e)(ii). So (b) fails in the drawn-seed discipline whenever the first number is below the second, for instance at $B_A=0$ with $d$ and $B/\sigma$ large (proven)." Three details differ from the challenger's text, and each matches the Reading of (e)(ii) as accepted. The factor $\sqrt{\eta/2}$ stays, as in the challenger's own paragraph on non-triviality. The output threshold and the probability $\alpha+\eta$ are stated, since the drawn-seed bound concerns outputs below that threshold. At $B_A=0$ the first number is $2R\lceil\ln(1/\alpha)/\epsilon_{\mathrm{acc}}\rceil$, polynomial in $R$, $\ln(1/\alpha)$ and $1/\epsilon_{\mathrm{acc}}$. The second is exponential in $\min\{d,B^2/\sigma^2\}$, so the instance needs $d$ and $B/\sigma$ large against the logarithm of the first (proven, by comparison). The register line of `theory/CURRENT.md` says "Drawn seeds fail where the coupled cost is below theirs, for instance at $B_A=0$ with $d$ and $B/\sigma$ large."

### ch-reading-conditions

Accepted. The Reading now reads as follows. "With $B_A=B=\sigma$, as for a deviating client in DP-FedAvg with noise multiplier one, $\mathfrak e=(R-1)/2$. Fix $\varepsilon$, $\eta$, $\alpha$, $\alpha'$, $\epsilon_{\mathrm{acc}}$ and $\sqrt R\Delta/\sigma$ so that the condition of the corollary holds. Then $N^\star=e^{(1+o(1))(R-1)/2}$ as $R$ grows with $R/d\to0$ (proven). At $\varepsilon=1$ it needs $\epsilon_{\mathrm{acc}}<\delta_{\mathcal N}(1;1)\approx0.127$ (computed)." Holding $\sqrt R\Delta/\sigma$ fixed is the challenger's "threshold of order $\sigma/\sqrt R$", and it keeps the condition $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<(1-\eta/2)\delta_{\mathcal N}(\varepsilon;1)$ fixed as $R$ grows. $N^\star$ is the quantity of the corollary, so "certification" no longer appears undefined. The value $\delta_{\mathcal N}(1;1)=\Phi(-1/2)-e\,\Phi(-3/2)=0.1269$ (computed).

### ch-draft-symbols

Accepted, with one item replaced. The table below applies the challenger's renamings, in the final document and in `theory/CURRENT.md`.

| Symbol | Second object | Now |
| --- | --- | --- |
| $G$ | Gaussian vector in [lem-sphere-code] (b) and in the proof of (d) of the transfer | $\mathbf g$ |
| $V_k$ | threshold cells of (d) of the transfer | $V^{\mathrm{th}}_k$ |
| $W$ | other randomness in step 2 of the proof of (e)(ii) | $\omega'$ |
| $\beta_1$ | coupled divergence at $\gamma=1$ in the proof of [thm-coupling-certificate] (c) | "$\beta_\gamma(K)$ at $\gamma=1$" |
| $L$, $L_b$, $L_{\mathrm{hyb}}$ | laws in (F3) and in the proof of [thm-dataflow-composition] (b) | $\mathcal L$, $\mathcal L_b$, $\mathcal L_{\mathrm{hyb}}$ |
| $u_t$, $u^{\mathrm{pr}}_t$ | coalition input and prescribed input | $\mathbf u_t$, $\mathbf u^{\mathrm{pr}}_t$ |
| $m_i$ | replays in [thm-replay-audit-steer] | $m^{\mathrm{rep}}_i$ |
| $I(\rho)$ | index map of the pair code | $\mathrm{ix}(\rho)$ |

The clipped difference $c'_t$ is disputed as named. The proposed $\mathbf b_t$ differs from the hypothesis bit $b$ by font alone, which is the kind of clash that the challenger's table flags for $L$ and $\mathsf L$. The symbol is removed. Step 4 of the proof of [thm-dataflow-composition] (b) now defines $\mathbf n_t$ as the unit vector along $F^1_t-F^0_t$ and $\mathfrak f_t=\min\{1,\|F^1_t-F^0_t\|/\Delta\}$, so that $\mathrm{clip}_\Delta(F^1_t-F^0_t)=\Delta\mathfrak f_t\mathbf n_t$. The hybrid's conditional mean is then $O_t+F^1_t-\Delta\mathfrak f_t\mathbf n_t$, and nothing else in the step changes.

Six more clashes in the final document are resolved.

1. The all-ones vector $\mathbf 1$ of step 4 of (b) against the indicator $\mathbf 1[\cdot]$. The kernel's second law is written $\mathcal N((\Delta/\sigma,\dots,\Delta/\sigma),I_R)$.
2. The ratio $c=\mathfrak e/d$ of open problem 5 against the choice $c$ and against the constant $c$ of open problem 7. The ratio is $\mathfrak a$. Open problems 2 and 7 now state their universal constants in words or as $O(d)$, in both files.
3. The number $q$ of grinding nonces in [thm-replay-audit-steer] (c) against the number $q$ of queries of a strategy tree. It is $n_{\mathrm{nc}}$.
4. The Gaussian means $\mathbf m_0$, $\mathbf m_1$ and $\mathbf m$ of (F6) and (F7) against the starting model $m_1$. They are $\mathbf a_0$, $\mathbf a_1$ and $\mathbf a$, and the Gaussian vector of (F6)(v) is $Z$.
5. The draws $Y_0$, $Y_1$ of step 2 of the proof of (e)(ii) against the view sample $Y$ of [thm-coupling-certificate]. The draws are named in words.
6. The laws $\mathbb P^{\mathrm{dev}}$, $\mathbb P^{\mathrm{pr}}$ of (F7) before the theorem that defines them, which the challenger noted under readability. (F7) is stated for generic laws $\mathbb P'\ll\mathbb P$, and step 3 of the proof of (a) defines $\mathbb E_{\mathrm{pr}}$.

The running time $\mathsf t$ of [def-learning-oracle-model] differs from the round index $t$ by font alone. The final document no longer names it, since no proof there uses it, and says "a statement with a computational assumption, which bounds its running time". `theory/CURRENT.md` keeps $\mathsf t$, because open problem 6 uses it and no statement there uses $t$ near it. The symbol table and the section "Names in the round files" of `theory/CURRENT.md` record every renaming of this round.

### ch-draft-pointers

Accepted, all six items.

1. The final document states [def-model-bank] in two sentences. "A design lists training inputs with seeds, each fixed or drawn, and a bank stores one run per entry. Its empirical oracle answers a Train call with the first unused matching entry and refuses a call that no unused entry matches."
2. The label of [thm-bank-soundness] copies the register. "The estimate (a), the gap (b) and the first half of (d), a lower bound on the Train calls that certify every record of a fixed dataset, are proven. Part (c), on shadow models in the random-subset game, is heuristic (round-01/builder.md with round-02 to round-05)."
3. [lem-atomless-two-point] points to round-01/builder.md, corrected in round-02 and round-03.
4. Open problem 1 now reads as follows. "Let $n_h\ge1$ further honest clients, isolated and stateless, add their clipped updates to the releases of $G^{\mathrm{agg}}_R$ with $B_A=0$. Is there a functional of $\mathsf L$ with three properties? It bounds every passive adversary as $\epsilon_0$ does in thm-dataflow-composition (b). It is never above $\epsilon_0$ and lies below it at some learning function. Some coupled-discipline certifier is uniformly accurate for it with Train calls fixed by $\alpha$, $\epsilon_{\mathrm{acc}}$, $R$ and $n_h$." Uniform accuracy is defined in the sentence that opens the open problems.
5. (F8) now includes McDiarmid's inequality.
6. A paragraph after the standing facts maps the old numbers. "In rounds 01 and 02 the test fact, data processing, the split and the realization fact are (F1), (F2), the first half of (F3) and (F9). There (G1) to (G4) are (F6)(i), (ii), (iii) and (v). From round 03 on, (F1), (F2) and (F4) are the second half of (F3), (F5) and (F6)(iv), (F6) is (F7), and (F8) is a case of Hoeffding's inequality." I checked each against the fact lists of round-01/builder.md to round-05/builder.md.

Two further pointers were short of the register. The proofs of [thm-replay-audit-steer] (c) to (e) now also name round-04/builder.md, which fixes the notation of (e). The pointer of [thm-smoothed-choice-certificate] now names round-05/builder.md.

### ch-draft-wording

Accepted, all six sentences.

1. Step 3 of the proof of [thm-coupling-certificate] (b) says "the image of the channel output under a kernel free of the hypothesis".
2. The proof of [thm-dataflow-composition] (c) says "its $\epsilon_0(\Delta)$ is no larger".
3. [def-learning-oracle-model] no longer uses "ships". "Its choices are the node arguments that $A$ sets, the values and learner names of nodes that $A$ owns, and its queries. They also include the learner names of nodes whose training code $A$ supplies." The same text replaces the old sentence in `theory/CURRENT.md`. The content is the round-01 meaning of "ships".
4. (F2) says "For $g$ with values in $[0,1]$, $\int g\,d(P_0-\gamma P_1)\le\mathrm H_\gamma(P_0\|P_1)$."
5. The paragraph "Without the oracle" of [lem-needle-lower-bound] says "must output at least $\vartheta$ with probability at least $1-\alpha$".
6. The clause "or they stall" is cut.

### Other findings of round 05

The challenger's readability and steering notes are applied as well. "Train" is named in the opening before its use ("a call, Train, to an idealized training oracle"). The term reference function is defined in [lem-needle-lower-bound], where $\mathsf L^\circ$ first appears, since the transfer section uses the term. Step 1 of the proof of [thm-dataflow-composition] (b) carries the clause on names that the answer to question 1 of round 05 asked for. "Names are per-caller counters that the adversary's own calls shift, so a node argument that is a name stands for the object it names." The pointer sentence of [thm-smoothed-choice-certificate] states its regime. "It costs less than thm-bounded-deviation-transfer (b) only when $\mathfrak e$ exceeds about $d\ln(R^{3/2}\sqrt d/\epsilon_{\mathrm{acc}})$ (heuristic comparison of the two costs)."

## Changes to the final document

What the theory shows.

1. Paragraph 1 drops "or they stall". Paragraph 2 names Train.
2. The sentence before the list defines $\alpha$. Items 1 to 5 are rewritten as quoted under ch-opening-hypotheses.
3. The closing paragraph drops its second sentence, a promise about symbols that the document keeps without stating it.

Definitions.

1. [def-learning-oracle]. "The oracle answers three calls" names $\mathcal O$, and "separately for each caller" is "per caller". The content is unchanged.
2. [def-learning-oracle-model]. "Ships" is replaced as quoted under ch-draft-wording. The running time is no longer named. The steer sentence is shortened, and "the law of the view" is "the view's law".
3. [def-isolated-client]. The exceedance and its probability are stated inline instead of in a display. The content is unchanged.

Standing facts. (F2) has the challenger's second sentence. (F3) uses $\mathcal L,\mathcal L',\mathcal L''$. (F6) uses $\mathbf a_0$, $\mathbf a_1$, $\mathbf a$ and $Z$. (F7) is stated for generic laws. (F8) adds McDiarmid's inequality. A paragraph maps the fact numbers of the round files.

[lem-needle-lower-bound]. $\mathsf L^\circ$ is named the reference function. The "Without the oracle" paragraph adds "with probability at least $1-\alpha$". The sentence "The lemma holds in both disciplines, so the lower bounds below bind the coupled discipline as well" is cut, since the statement already says "in either discipline". Two sentences of the proof are shortened.

[lem-sphere-code]. The Gaussian vector is $\mathbf g$.

[thm-coupling-certificate]. The chain of (b) is inline. Part (a)(ii) is phrased "For finite $\mathcal V$ and the empirical law $\hat p_b$". Step 3 of the proof says "the channel output" and puts the oracle as the subject of "answers". The proof of (c) avoids $\beta_1$. The "Without the oracle" and "Degenerate oracles" paragraphs are shortened with the same content.

[thm-black-box-certifiability]. The pointer of (b) to (d) is shortened. The degenerate-oracle example is shortened with the same content.

[thm-dataflow-composition].

1. The scalar sentence is reversed as quoted under ch-scalar-direction.
2. The display of (e)(ii) is inline.
3. Proof of (b). Step 1 adds the clause on names. Steps 1 to 5 use $\mathcal L_b$ and $\mathcal L_{\mathrm{hyb}}$. Step 4 removes $c'_t$ and the all-ones vector. Steps 2 and 3 are shortened with the same content.
4. Proof of (c) says "no larger". Proof of (e)(ii) uses $\mathrm{ix}$ and $\omega'$, and names the drawn certifier as the subject of "opens no seed name".
5. The "Degenerate oracles" paragraph says "fails under drawn seeds".

[thm-bounded-deviation-transfer].

1. Setting. The coalition's inputs are $\mathbf u_t$ and $\mathbf u^{\mathrm{pr}}_t$, and the clause on the prescribed input is narrowed as quoted under ch-prescribed-input-scope.
2. Part (c). $R\ge2$ is added, and the limsup sentence is replaced by the factor form.
3. Corollary. "The least number of Train calls of a certifier sound at level $\alpha$" replaces "of a certifier that is sound", and "For $\mathfrak c$ with $J_3\ge1$" replaces "For every $\mathfrak c$".
4. Reading, "Without the oracle" and "Degenerate oracles" are rewritten as quoted above.
5. Proof of (a). Step 2 states the density inline. Step 3 defines $\mathbb E_{\mathrm{pr}}$.
6. Proof of (c). The strategy fixes $\mathbf u_R=0$, the coordinate is named, $R-1\ge1$ is used, and a paragraph proves the factor form.
7. Proof of (d). The Gaussian vector is $\mathbf g$, the cells are $V^{\mathrm{th}}_k$, and the bound on leaving a cell is inline.
8. Proof of the corollary. The last sentence is shortened.

[thm-replay-audit-steer]. The replays are $m^{\mathrm{rep}}_i$, the grinding prover tries $n_{\mathrm{nc}}$ nonces, and the definitions of the reach, the spread and the joint reach are inline. The label, the "Without the oracle" and the "Degenerate oracles" paragraphs are shortened with the same content. The pointer of (c) to (e) names round-04/builder.md.

Further accepted results. The opening sentence is shortened. [def-model-bank] is stated in two sentences. The pointers of [lem-atomless-two-point], [thm-bank-soundness] and [thm-smoothed-choice-certificate] are completed, and the last carries its regime. Two pointer sentences, of [thm-perfect-substitution] and [thm-record-level-certificate], are merged into their result sentences.

Open problems. Problem 1 carries its conditions. Problem 2 states its constant as $O(d)$. Problem 5 is restated with $\mathfrak a$ and $J^{\mathrm{fb}}$. Problem 7 states its constant in words.

Prior work. The reference to Zhang et al. moves after the clause it supports.

Length. The document has 18 pages. To stay within them, six displays became inline formulas, and sentences whose last printed line held one or two words lost those words. No statement, hypothesis or label changed in these cuts. No prose sentence exceeds 30 words, and the document has no semicolon, no dash used as punctuation and no bold (computed).

`theory/CURRENT.md`. The title and the opening name round 06. [def-learning-oracle-model] replaces "ships". The symbol table records the new names, and the register records the round-05 verdicts. The register lines of [thm-dataflow-composition] and [thm-bounded-deviation-transfer] carry the scalar condition, the factor form and the drawn-seed regime, and the line of [thm-smoothed-choice-certificate] carries the regime of its covering. Open problems 2, 5 and 7 are restated as above. The section "Names in the round files" adds the renamings of round 05 and a map of the fact numbers, and corrects the name of the law of the averaging identity to $\mathbb P_{\mathfrak w}$.

## Questions for the challenger

1. Do you accept the rejection of the option "$R\to\infty$" for open problem 5 on the steering computation, and the restatement through $J^{\mathrm{fb}}$ with $N^\star\ge(1-\alpha-\alpha')J^{\mathrm{fb}}$?
2. Do you accept that item 4 of the opening needs "accurate where the leakage is zero", which your proposed text omitted?
3. Do you accept the removal of $c'_t$ in place of the name $\mathbf b_t$?
