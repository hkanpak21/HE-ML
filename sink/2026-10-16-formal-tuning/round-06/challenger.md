# Round 06, challenger

Verdict of this turn. The three blocking challenges of round 05 are closed in `final/learning-oracle-theory.md` and in `theory/CURRENT.md`, and so are the eight non-blocking ones. Both partial disputes go to the builder. The steering computation reproduces when I rerun it, so my round-05 option "add $R\to\infty$" was wrong. My heuristic there covered exact cancellation of seen noise, and partial correction escapes it. The new bound $N^\star\ge(1-\alpha-\alpha')J^{\mathrm{fb}}$ is correct (proven, checked below). The factor form of part (c) of [thm-bounded-deviation-transfer] is correct with room, and one more line sharpens it (proven). All six definitions are accepted for the third consecutive round. def-isolated-client gets one non-blocking clarification (ch-choice-source). Every proof shown in full in the final document is correct as written there. Two sentences outside the theorem statements are false as written. By the rule of this round both are blocking, and each needs one clause. The first opening summary of black-box certifiability drops the finite query set. That repeats the round-01 error of ch-query-universe in a new place (ch-opening-finite-queries). The criterion-4 paragraph of the transfer omits the condition that the coupled accuracy level lies below the drawn-seed threshold. My own round-05 text omitted it too (ch-drawn-seed-accuracy-level). `node scripts/verify.mjs final` prints `FINAL OK theorems=5 nontrivial=5 items=21`.

Every non-trivial claim carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the argument is written here and the builder must write it out. "Computed" marks a number I computed this round with a short script. Notation follows `theory/CURRENT.md` after round 06. I opened no outside source. Shannon's theorem that feedback does not raise the capacity of a memoryless channel is cited from memory and used only in a remark.

## Status of the round-05 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-scalar-direction | blocking | closed, final document and register line | none |
| ch-opening-hypotheses | blocking | closed for the four items named | the first sentence of item 2 drops the finite query set (ch-opening-finite-queries, blocking), and item 4 leaves the accuracy level implicit (ch-opening-scope, not blocking) |
| ch-tightness-round-count | blocking | closed, $R\ge2$ in the statement and used in the proof | none |
| ch-tightness-first-order | not blocking | closed, the factor form is correct | the Mills step is a pointer, and one line sharpens the factor (ch-tightness-inline, not blocking) |
| ch-feedback-capacity | not blocking | closed, the dispute goes to the builder | none |
| ch-prescribed-input-scope | not blocking | closed | none |
| ch-drawn-seed-regime | not blocking | closed as I asked | the condition on the accuracy level is missing, in my text and in the draft (ch-drawn-seed-accuracy-level, blocking) |
| ch-reading-conditions | not blocking | closed | none |
| ch-draft-symbols | not blocking | closed, the removal of $c'_t$ accepted | seven new clashes (ch-residual-symbols, not blocking) |
| ch-draft-pointers | not blocking | closed, all six items | the fact map omits three round facts (ch-final-wording, not blocking) |
| ch-draft-wording | not blocking | closed, all six sentences | none |

I checked each closure against the text. The scalar sentence of [thm-dataflow-composition] (a) now says that the scalar divides the noise when the decryptors add it at decryption, and removes at most the decryption error when client $j$ adds it inside its ciphertext. The register line of `theory/CURRENT.md` says the same. (F2) carries the integral form, the proof of (c) says "no larger", step 3 of the coupling proof says "the channel output", "ships" is gone from both files, lem-needle-lower-bound carries "with probability at least $1-\alpha$", and "or they stall" is cut.

### The dispute on ch-draft-symbols

The builder is right (proven, by inspection). The name $\mathbf b_t$ differs from the hypothesis bit $b$ by font alone, which is the clash my round-05 table flagged for $L$ against $\mathsf L$. The replacement is exact. With $\mathbf n_t$ the unit vector along $F^1_t-F^0_t$ and $\mathfrak f_t=\min\{1,\|F^1_t-F^0_t\|/\Delta\}$, the identity $\mathrm{clip}_\Delta(F^1_t-F^0_t)=\Delta\mathfrak f_t\mathbf n_t$ holds in the three cases $\|F^1_t-F^0_t\|\le\Delta$, $>\Delta$ and $=0$.

### The dispute on ch-feedback-capacity

The rejection of the option "$R\to\infty$" is right (heuristic). My round-05 count showed that exact cancellation of $Z_{t-1}$ needs a per-round budget of order $\sigma\sqrt d$, which vanishes as $R\to\infty$ at fixed $\mathfrak a$. It said nothing about partial correction. Over $R-1$ rounds the coalition moves $m_R$ by up to $(R-1)B_A$, and the noise adds squared norm $(R-1)d\sigma^2$. The ratio of the squared drift to the noise is $2\mathfrak a$ at every $R$, so the time-rescaled problem has a limit, and the steering code acts in that limit.

I checked the mean-field model. In units of $(R-1)B_A$ and $R-1$ rounds the drift has speed one, and the noise adds $d\sigma^2/((R-1)B_A^2)=1/(2\mathfrak a)$ per unit of time. Both equations follow from Itô's rule for $p$ and for the squared norm $q$ of the orthogonal part, with the $(d-1)/d$ factor of the noise dropped. I reran the Euler scheme with step $1/4000$ and a grid of step $0.05$ over $a$. The best values are $0.980$, $0.930$, $0.803$, $0.605$ and $0.404$ at $\mathfrak a=0.5,1,2,4,8$, which match the builder's table to within $0.001$ (computed). The columns without feedback, with cancellation at $R=3$ and of the proven lower bound match exactly (computed). The algebra for the threshold $(1+\sqrt2)/2$ is right, since $(\sqrt{\mathfrak a}+\sqrt{\mathfrak a-1})^2>2\mathfrak a$ reduces to $4\mathfrak a^2-4\mathfrak a-1>0$ (proven).

One remark for the open problem, not a challenge. Feedback does not raise the capacity of a memoryless channel. Here the gain is possible because the decoder sees only the final sum $m_R$, while the coalition sees every release. One clause in open problem 5 saying so would answer the first objection of a reader from information theory.

### The bound through $J^{\mathrm{fb}}$

The definition is well posed (proven). $J^{\mathrm{fb}}$ is integer valued, at least one, and bounded by $N^\star/(1-\alpha-\alpha')$ under the hypotheses of the corollary, by the claim itself. So the largest number exists.

The proof in round-06/builder.md is correct (proven, checked step by step).

1. The $X_k$ are pairwise disjoint Borel sets. The map $m\mapsto x((R,m),D^1_j)$ is measurable and injective between standard Borel spaces, so it maps Borel sets to Borel sets by the theorem of Lusin and Souslin.
2. A strategy without oracle calls sets $\mathbf u_t$ from its coins and $y_{<t}$. In rounds $t<R$ the learner name $\ell_t\neq\ell_R$ keeps every training input outside $X_k$, so $y_t=\mathbf u_t+Z_t$ under both hypotheses at $\mathsf L_k$ and at $\mathsf L^\circ$. The joint law of the coins and $y_{<R}$ is therefore one law, and $\Pr[m_R\in V_k]$ is the same at $\mathsf L_k$ as at $\mathsf L^\circ$.
3. Setting $\mathbf u_R=0$ keeps the strategy $B_A$-deviating and leaves $m_R$ unchanged. A strategy that stops after release $R-1$ never sets $m_R$, so the event $\{m_R\in V_k\}$ already implies that round $R$ runs.
4. In round $R$, (F5) with the coins and $y_{<R}$ as the common coordinate and (F6)(i) give $\mathrm H_\gamma(P_0\|P_1)=\Pr[m_R\in V_k]\,\delta_{\mathcal N}(\varepsilon;B/\sigma)\ge\vartheta$.
5. lem-needle-lower-bound and the condition $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<\vartheta$ give $\alpha'\ge1-\alpha-N/J$.

The straight strategies of part (d) hit the threshold cells, so $J^{\mathrm{fb}}\ge J_3$ (proven). The final document states the bound with its pointer and the heuristic values with their label. That is faithful.

## Definitions

Third reading. I compared `theory/CURRENT.md` with the round-05 text through the builder's change list and found only the replacement of "ships".

### [def-learning-oracle]

Unchanged. Well posed. ACCEPT, the third consecutive acceptance in this sequence of rounds.

### [def-learning-oracle-model]

The new sentence "They also include the learner names of nodes whose training code $A$ supplies" is the round-01 meaning of "ships", and it adds no object that later items lack. Well posed. ACCEPT.

### [def-degenerate-oracles]

Unchanged and well posed. ACCEPT.

### [def-certifier]

Unchanged and well posed. ACCEPT.

### [def-model-bank]

Unchanged and well posed. The final document states it in two sentences under the further results. That statement omits the matching rule on fixed and drawn seeds, which a pointer may omit. ACCEPT.

### [def-isolated-client]

Well posed under its own sentence on choices, and I accept it. One clause should become explicit (ch-choice-source, not blocking).

Clause 1 says that $c_t$ is "the value of a parent of $v_t$ or a choice of the coalition". The parents of $v_t$ include the input node of $D_j$ and $v_{t-1}$. Read alone, the clause admits $c_t=W_{t-1}$. Take one learner name $\ell$, $x(c,D,w)=(\ell,c,D,\mathcal H)$, $f_t(c,m)=m$, $O_t=0$ and $\mathsf L((\ell,m,D,\mathcal H);\rho,\xi)=m+\phi(D)$ with $\|\phi(D^1_j)-\phi(D^0_j)\|=\Delta_0$. Conditions 2 to 4 hold. Every twin starts from the real chain, so $D^\star_b=\Delta_0$ and $\epsilon_b(\Delta)=0$ for $\Delta\ge\Delta_0$. The release means differ by $t\Delta_0$ in round $t$, so the real divergence grows with $R^{3/2}\Delta_0$, while [thm-dataflow-composition] (b) would bound it by $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta_0/\sigma)$ (proven, sketch). The case $c_t=D_j$ breaks the theorem in the same way.

The preceding sentence of the definition excludes both cases. "A choice holds the starting model and everything else that the node's input takes from outside the client." Neither $W_{t-1}$ nor $D_j$ comes from outside the client, so neither is a choice. Step 1 of the proof of [thm-dataflow-composition] (b) uses this exclusion when it says that $c_t$ has the stated arguments, without citing it. The definition therefore makes no stated result false, and the challenge is not blocking. Three rounds of reading passed over the gap, so the clause belongs in the formal text.

ACCEPT.

Simplicity. The six definitions remain the smallest that carry the presented proofs.

## Proofs in the final document

I read each proof as written in `final/learning-oracle-theory.md`, with only the facts (F1) to (F9) of that document. I re-derived (F3) in both orders, the Rényi moment of (F7), the kernel of (F6)(ii) and the Mills bounds of (F6)(iv). The items stated with pointers ([thm-perfect-substitution], [thm-reference-access], [lem-atomless-two-point], [lem-bank-fidelity], [thm-bank-soundness], [thm-active-choice-dichotomy], [thm-record-level-certificate], [thm-smoothed-choice-certificate], and the stated parts of the theorems below) match their register lines in statement and label.

### [lem-needle-lower-bound]

Correct as written (proven). The two runs share coins and the triple of the $i$-th call, so they agree up to the first Train call into $X_k$, including calls whose starting model is a stored name, since stored objects agree while transcripts agree. Soundness at $\mathsf L_k$ and $\theta(\mathsf L_k)\ge\vartheta$ give $\Pr_{\mathsf L_k}[\hat t\ge\vartheta]\ge1-\alpha$. Each Train call meets at most one $X_k$, so $\sum_k\Pr_{\mathsf L^\circ}[\mathrm{Hit}_k]\le N$, and averaging over $k$ gives the bound.

### [lem-sphere-code]

Correct as written (proven). The volume bound follows from $p^i(1-p)^{d-i}\ge p^{pd}(1-p)^{(1-p)d}=2^{-d\mathrm h_2(p)}$ for $i\le pd$ and $p\le1/2$. Maximality puts every word within $\lceil d/4\rceil-1\le d/4$ of $\mathcal W$, and $1-\mathrm h_2(1/4)=0.1887$. For $d\le3$ the code is the whole cube, which also works. In (b), leaving $V_k$ needs $\langle\mathbf g,\mathbf e\rangle\ge\|\mathbf p_l-\mathbf p_k\|/2\ge\mathfrak s/2$ for some $l$, and $(J-1)\bar\Phi(\cdot)\le\frac J2e^{-\mathfrak s^2/(8\sigma'^2)}$ by (F6)(iii).

### [thm-coupling-certificate]

(a)(i) and (a)(ii) are correct (proven). In (a)(ii) each draw moves $\frac12\|\hat p_b-P_b\|_1$ by at most $1/n$. So McDiarmid's inequality over the $2n$ draws gives the deviation $\sqrt{\ln(1/\alpha)/n}$, below the stated $\sqrt{2\ln(2/\alpha)/n}$, and the certifier is sound with room. (a)(iii) is a pointer to lem-atomless-two-point.

(b) is correct (proven). Step 1 approximates every Borel set by a set of a countable generating algebra in the measure $K(\cdot\mid m_0)+K(\cdot\mid m_1)$, which moves $P_0(E)-\gamma P_1(E)$ by at most $\gamma$ times the error. Step 2 applies (F5) once and (F4) twice, with equality when $\Xi$ is a point. Step 4 applies Hoeffding's inequality to summands in $[0,1]$. One sentence of step 3 is too strong as written. "By (F2) in both directions its transcript has total variation $\mathrm D^\top_1(K)$" holds for an adversary that opens the seed name. Any other adversary's transcript is a kernel image of $(\rho,Y)$ with total variation at most $\mathrm D^\top_1(K)$. Opening is free, so the conclusion on the best advantage stands (ch-final-wording, item 1).

(c) is correct (proven). Under $\mathsf L(x_b;\rho)=\rho+b/2\bmod1$ both model laws are uniform, $W_0\neq W_1$ at every seed, and the top view $(\rho,\rho+b/2)$ separates the hypotheses.

### [thm-black-box-certifiability]

(o) is correct (proven). Under the bottom oracle the adversary holds only label eval on the served name, so it cannot train from the served model, and given $\omega$ its queries on that name form a tree in $\mathfrak T_{q_E}$ whose answers carry fresh evaluation randomness, as in the definition of $\mathrm{Adv}(\mathfrak t)$.

(a) is correct (proven). Each frequency deviates by more than $\lambda/2$ with probability at most $2e^{-n\lambda^2/2}$, the union over two frequencies and over $\mathfrak T_q$ gives $4|\mathfrak T_q|e^{-n\lambda^2/2}=\alpha$, and the maximum is 1-Lipschitz in the sup norm.

The degenerate-oracle example is correct. Adding one half modulo one flips the first binary digit.

### [thm-dataflow-composition]

Proof of (b), correct (proven). Step 1 rests on the node-indexed randomness, with the clause on names, and on the exclusion under ch-choice-source. Step 3 holds by induction in both directions, so the hybrid and $\mathsf{Ex}_0$ agree exactly off $\{D^\star_0>\Delta\}$. The conditional exceedance probability is $\beta_t(c_t,W_{t-1},W'_{t-1},\Delta)$, with the arguments in the order of the definition. In step 4, (F6)(ii) with $r=\Delta/\sigma$ maps $\mathcal N(\Delta/\sigma,1)$ to $\mathcal N(0,1)$, and then $\sigma\tilde g_t\mathbf n_t+\sigma(I_d-\mathbf n_t\mathbf n_t^\top)Z''_t\sim\mathcal N(0,\sigma^2I_d)$. Under $\mathcal N(0,1)$ the release mean is $O_t+F^1_t-\Delta\mathfrak f_t\mathbf n_t$, the hybrid's. (F6)(i) in $\mathbb R^R$ gives $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$ in both orders. Step 5 applies the two splits of (F3) exactly.

Proof of (c), correct (proven). The stopping clause compares two adversaries pathwise, which the node-indexed space of step 1 permits.

Proof of (e)(ii), correct (proven). $(\mathrm{ix},\mathrm{sg})$ is uniform on $\{1,\dots,J_{\mathrm{cd}}\}\times\{\pm1\}$. Given distinct indices the signs are independent and uniform under $\mathsf L^\circ$ and under the mixture, so the collision probability $\binom{2N}2/J_{\mathrm{cd}}=N(2N-1)/J_{\mathrm{cd}}$ bounds the total variation. Step 3 decodes $2J_{\mathrm{cd}}$ points at separation $B$. The reading uses $(2J_{\mathrm{cd}}-1)\bar\Phi(B/(2\sigma))\le J_{\mathrm{cd}}e^{-B^2/(8\sigma^2)}\le e^{-B^2/(16\sigma^2)}$, and $J_{\mathrm{cd}}\ge1$ holds from $d=6$, since $2^{0.08}>1$.

### [thm-bounded-deviation-transfer]

Proof of (a), correct (proven). Step 0 uses the continuation, which agrees with the stopping strategy until the stop on the node-indexed space. Step 1 gives one set $\mathbb A$ of $(\Omega,y_{<R})$, because $\Omega$ contains the $\zeta_t$, so the revealed seeds of the top oracle are functions of $\Omega$, and the narrowed prescription reads only nodes that step 1 covers. In step 3 the ratio is $\exp(\langle Y,\delta_t\rangle/\sigma^2-\|\delta_t\|^2/(2\sigma^2))$ with $Y\sim\mathcal N(0,\sigma^2I_d)$ under $\mathbb P^{\mathrm{pr}}$, and its $\varpi$-th moment is $\exp(\varpi(\varpi-1)\|\delta_t\|^2/(2\sigma^2))\le\exp(\varpi(\varpi-1)B_A^2/(2\sigma^2))$. Step 4 optimizes $-\mathfrak l(1-1/\varpi)+(\varpi-1)\mathfrak e$ in the three cases and recovers $\ln\Upsilon_{\mathfrak e}(p)$.

Proof of (b), correct (proven). Coverage, monotonicity of $\Upsilon_{\mathfrak e}$, and $1-\alpha^{1/N'}\le\ln(1/\alpha)/N'$ give soundness and accuracy.

Proof of (c), correct (proven). I checked the construction for $R\ge2$. Rounds $t<R$ train at learner names other than $\ell_R$ and have no exceedance. In round $R$ the twin differs by $2\Delta\mathbf e_1$ exactly on the threshold event, and the clip keeps it since $B\ge2\Delta$. The coordinate $\langle m_R-m_1,\mathbf e_1\rangle$ is $\mathcal N(0,(R-1)\sigma^2)$ under the protocol's strategy and has mean $(R-1)B_A=\sqrt{2\mathfrak e}\,\sigma\sqrt{R-1}$ under the given one. The inequality on $\ln(1/\epsilon_0(\Delta))$ is given through a pointer, and it follows in two lines from facts of the document (proven). Write $r=\iota-\sqrt{2\mathfrak e}$, so $1<r\le\iota$. From $\ln(1/p)\ge\iota^2/2$ and $\iota/\sqrt2>\sqrt{\mathfrak e}$,

$$\ln\frac1{\Upsilon_{\mathfrak e}(p)}=\Big(\sqrt{\ln(1/p)}-\sqrt{\mathfrak e}\Big)^2\ge\frac{r^2}2,\qquad\ln\frac1{\epsilon_0(\Delta)}=\ln\frac1{\bar\Phi(r)}\le\frac{r^2}2+\ln\Big(r+\frac1r\Big)+1\le\frac{r^2}2+\ln(\iota+1)+1,$$

the second by the lower Mills bound. So $\ln(1/\epsilon_0(\Delta))\le\ln(1/\Upsilon_{\mathfrak e}(p))+\ln(\iota+1)+1$, which implies the stated bound with $2\ln(\iota+1)+2$. A grid over $\mathfrak e\in\{0.1,\dots,16\}$ and $\iota$ up to $\sqrt{2\mathfrak e}+21$ shows slack at least $1.7$ against the sharper bound (computed).

The factor form, correct (proven). Every $p$ in the range is $\bar\Phi(\iota)$ for one $\iota>\sqrt{2\mathfrak e}+1$, by continuity and strict monotonicity of $\bar\Phi$. (F6)(iii) gives $\ln(1/p)\ge\iota^2/2$, and $\iota>1$ gives $(\iota+1)^2\le4\iota^2\le8\ln(1/p)$. So $F(p)\ge\epsilon_0(\Delta)\ge e^{-2}\Upsilon_{\mathfrak e}(p)/(8\ln(1/p))$. The identity $\ln(\Upsilon_{\mathfrak e}(p)/p)=2\sqrt{\mathfrak e\ln(1/p)}-\mathfrak e$ needs $\ln(1/p)>\mathfrak e$, which holds since $\iota^2/2>(\sqrt{2\mathfrak e}+1)^2/2>\mathfrak e$. The ratio is unbounded because $\mathfrak e>0$. The statement is not vacuous. The lower bound on $F(p)$ exceeds $p$ once $2\sqrt{\mathfrak e\ln(1/p)}-\mathfrak e>2+\ln(8\ln(1/p))$, which holds for all small $p$. With the sharper line above, the factor becomes $e\sqrt{8\ln(1/p)}$ (proven), which is optional (ch-tightness-inline).

Proof of (d), correct (proven). Hoeffding's inequality with range $2$ per sign gives $2e^{-\mathfrak c^2d/2}$, and $J(J-1)e^{-\mathfrak c^2d/2}<J^2e^{-\mathfrak c^2d/2}\le1$. Leaving $V^{\mathrm{th}}_k$ needs $\langle\mathbf g,\mathbf q_k\rangle\le-\mathfrak q_\eta\mathfrak v$, or $\langle\mathbf g,\mathbf q_l\rangle>(1-\mathfrak c)\mathfrak m-\mathfrak q_\eta\mathfrak v$ for some $l\neq k$, by $|\langle\mathbf q_k,\mathbf q_l\rangle|<\mathfrak c$. The choice of $J_3$ caps the union at $\eta/4$. $J_3\ge1$ forces $(1-\mathfrak c)\sqrt{2\mathfrak e}>\mathfrak q_\eta>0$, hence $R\ge2$, so (d) needs no explicit hypothesis on $R$. In the expansion, $\ln J'<\mathfrak e$ follows from $\frac12((1-\mathfrak c)\sqrt{2\mathfrak e}-\mathfrak q_\eta)^2\le(1-\mathfrak c)^2\mathfrak e$ and $\ln(\eta/2)<0$, under the stated hypothesis $(1-\mathfrak c)\sqrt{2\mathfrak e}\ge\mathfrak q_\eta$.

Proof of (e), correct (proven). The pair code sits in round 1 at the two inputs $x((1,m_1),D^b_j)$. The family agrees elsewhere, and the clip is the identity on norm $B$. At the reference function every coupled pair coincides, no run of $\mathsf{Ex}_b$ exceeds $\Delta$, and $\theta^{\mathrm{agg}}_R=0$, since the round-1 model is the same function of the seed under both hypotheses. The final document does not state $\theta^{\mathrm{agg}}_R=0$ there, and the criterion-4 paragraph needs it (ch-drawn-seed-accuracy-level).

Corollary, correct (proven). The lower bound is (d) read at an accurate certifier. The upper bound runs the two certificates of (b) at level $\alpha/2$ with $2R$ calls per run, so $N=4R\lceil\cdot\rceil$. The asymptotics follow from the expansion of (d) and $\ln(4R)=o(\mathfrak e)$. The Reading is correct, and $\delta_{\mathcal N}(1;1)=\Phi(-1/2)-e\,\Phi(-3/2)=0.1269$ (computed).

### [thm-replay-audit-steer]

Proof of (a), correct (proven). Lazy sampling with $q_{\mathsf{RO}}+1$ values gives the oracle its law. The auditor's hardware randomness indexed by $(k,i)$ is independent of the prover's transcript. A win puts some replay within $\tau$ of $T$, and the union over $(k,i)$ costs $(q_{\mathsf{RO}}+1)n_{\mathrm{rep}}p_\tau(T)$.

Proof of (b), correct (proven). Rejection implies that the first replay lies more than $\tau$ from the honest run at the same seed.

Stated part (c), checked (proven). The first success index and the conditional replay probability give $\frac{p^\circ_{\tau/2}(T)}{p}(1-(1-p)^{n_{\mathrm{nc}}})$. Under deterministic kernels and $q_{\mathsf{RO}}p_\tau(T)\le1$, $1-(1-p)^{q}\ge(1-e^{-1})qp$, so the ratio to $(q+1)p$ is at most $2/(1-e^{-1})<3.17$.

## New challenges

### ch-opening-finite-queries

BLOCKING. A false sentence in the final document. Target: item 2 of "What the theory shows", "Label-only leakage at a fixed number of queries is certifiable from both sides."

The theorem's setting has a finite query set $U$ and $C$ outputs, and part (a) pays $\ln|\mathfrak T_q|$. Without a finite query set the sentence is false (proven, sketch). Let $\mathcal U=\mathbb N$, $\mathcal Y=\{0,1\}$, $\mathcal M=\{0,1\}^{\mathbb N}$, $\mathsf{ev}(m,u)=m_u$, and let the reference function return independent fair bits drawn from the hardware randomness, ignoring the seed and the dataset. Its black-box advantage is $0$. For $k\le M$ let $\mathsf L_k$ agree with it except that coordinate $k$ equals $b$ at $x_b$, so one query at $k$ wins with advantage one. A certifier with $N$ calls sees at most $N$ models. Hardware randomness makes explicit seeds useless. The chi-square divergence between the mixture over $k$ and the reference law of the transcript is at most $(2^N-1)/M$. So every sound upper certifier outputs at least one at the reference function with probability at least $1-\alpha-o(1)$ as $M\to\infty$, in either discipline. This is the counterexample of ch-query-universe in round-01/challenger.md, moved from the adversary to the certifier.

Smallest fix. "Label-only leakage at a fixed number of queries from a finite query set is certifiable from both sides."

### ch-drawn-seed-accuracy-level

BLOCKING. A false sentence in the final document. Target: the paragraph "Degenerate oracles" of [thm-bounded-deviation-transfer], "So (b) fails in the drawn-seed discipline whenever the first number is below the second, for instance at $B_A=0$ with $d$ and $B/\sigma$ large (proven)."

The drawn-seed bound concerns outputs below $1-(1+\gamma)e^{-B^2/(16\sigma^2)}$, while (b) is accurate to the level $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}$. When that level is not below the threshold, the comparison says nothing. At $\epsilon_{\mathrm{acc}}=1$, which (b) admits, a drawn-seed certifier that outputs one with no Train call is sound and matches the accuracy of (b). The first number is then $2R\lceil\ln(1/\alpha)\rceil$ at $B_A=0$, below the second for large $d$ and $B/\sigma$. So the "whenever" claim fails there (proven). The text I proposed in round 05 had the same gap. The paragraph also uses $\theta^{\mathrm{agg}}_R=0$ at the reference function without stating it.

Smallest fix. "At the reference function of (e), where $\theta^{\mathrm{agg}}_R=0$, the certificate (b) outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}$ with $2R\lceil\ln(1/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)\rceil$ Train calls." Keep the next sentence. Then: "So (b) fails in the drawn-seed discipline whenever the first number is below the second and $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<1-(1+\gamma)e^{-B^2/(16\sigma^2)}$, for instance at $B_A=0$ with $d$ and $B/\sigma$ large, $\epsilon_{\mathrm{acc}}<1$ and $\sqrt R\Delta/\sigma$ small (proven)."

With the fix, criterion 4 holds (proven). Take $B_A=0$, $d\ge6$, $\epsilon_{\mathrm{acc}}=1/4$, $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)\le1/4$, and $B/\sigma$ and $d$ large enough that $(1+\gamma)e^{-B^2/(16\sigma^2)}<1/2$ and $2R\lceil4\ln(1/\alpha)\rceil$ is below $\sqrt{\eta J_{\mathrm{cd}}/2}$. Then (b) outputs at most $1/2$ with certainty at a function where the target is zero. A drawn-seed certifier with as many calls outputs above $1/2$ with probability at least $1-\alpha-\eta$, by (e).

### ch-choice-source

Not blocking. Due before the audit. Target: clause 1 of [def-isolated-client] in both files, "and $c_t$ is the value of a parent of $v_t$ or a choice of the coalition". The counterexample and the reason it is not blocking are under Definitions. Smallest fix. "and $c_t$ is the value of a parent of $v_t$ other than $v_{t-1}$ and the input node of $D_j$, or a choice of the coalition." Step 1 of the proof of [thm-dataflow-composition] (b) can then cite clause 1 where it says that $c_t$ has the stated arguments.

### ch-opening-scope

Not blocking. Three clauses in "What the theory shows".

1. Item 1, "which coupled Train calls certify for every learning function". Part (b) assumes that the divergence between two channel outputs is computable. The model never limits an experimenter's computation, so the sentence is not false, but the opening and the theorem should agree. Either add "when the divergence of the channel at two models is computable", or drop the hypothesis from (b) and say that experimenters are unbounded.
2. Item 4, "accurate where the leakage is zero". The lower bound needs accuracy finer than the leakage of one clipped release, the corollary's condition $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<(1-\eta/2)\delta_{\mathcal N}(\varepsilon;B/\sigma)$. Outside it the claim is open, not false. Fix. "accurate, to less than the leakage of one clipped release, where the leakage is zero". I accept the builder's addition of the phrase, which my text lacked (answer to question 2).
3. Item 4, "with about $e^{\mathfrak e}\ln(1/\alpha)$ runs". The exact count carries the factor $e^{2\sqrt{\mathfrak e\ln(1/\epsilon_{\mathrm{acc}})}+\ln(1/\epsilon_{\mathrm{acc}})}$, which is $e^{o(\mathfrak e)}$ but not a constant. Fix. "with $e^{(1+o(1))\mathfrak e}\ln(1/\alpha)$ runs at a fixed accuracy". I wrote "about" in round 05.

### ch-tightness-inline

Not blocking. Target: the proof of [thm-bounded-deviation-transfer] (c), "The inequality follows from (F6)(iv) ... (round-05/builder.md)." The step that makes it follow, $\ln(1/\Upsilon_{\mathfrak e}(p))\ge(\iota-\sqrt{2\mathfrak e})^2/2$, is not written. Smallest fix. Insert the two-line derivation under Proofs above, which also gives the sharper $\ln(\iota+1)+1$. The builder may keep the stated constants or replace them by $e^{-1}\Upsilon_{\mathfrak e}(p)/\sqrt{8\ln(1/p)}$. Both are proven.

### ch-residual-symbols

Not blocking. Due before the audit. One name, two objects, in the final document.

| Symbol | First object | Second object, where | Fix |
| --- | --- | --- | --- |
| $W_0$, $W_1$ | initial state $w_0$ and value of $v_1$, def-isolated-client | coupled pair at $x_0,x_1$, thm-coupling-certificate | $(M_0,M_1)$ or $(W^{\Gamma}_0,W^{\Gamma}_1)$ |
| $m_0$, $m_1$ | starting model of round 1 of $G^{\mathrm{agg}}_R$ | arguments of the divergence in thm-coupling-certificate (b), and $m_0$ in thm-replay-audit-steer | $(w,w')$ in (b), $m^{\mathrm{st}}$ in the replay setting |
| $o_t$ | contribution map of step 1 of the composition proof | value $O_t-\mathbf u_t$ in the transfer setting | $\bar o_t$ for the value |
| $F$ | transfer function, transfer (c) | $F^0_t,F^1_t$, composition proof | $\mathsf F$ or $\Upsilon'$ for the transfer function |
| $K$ | channel | index $K^*$ in the proof of replay (a) | $k^*$ |
| $g$ | test function in (F2) and (F7) | input vector $g\in\mathbb R^R$ of the kernel | $h$ for the test function |
| $\mathbf e_1$ | never defined | transfer (c) and (d) | "the first standard basis vector $\mathbf e_1$" at first use |

`theory/CURRENT.md` shares the $o_t$ and $F$ items and lists neither $F$ nor $\mathbf e_1$ in its table.

### ch-final-wording

Not blocking. Four sentences.

1. Step 3 of the proof of [thm-coupling-certificate] (b), "Under the top oracle the adversary sees $(\rho,Y)$ ... By (F2) in both directions its transcript has total variation $\mathrm D^\top_1(K)$." Fix. "Under the top oracle every transcript is the image of $(\rho,Y)$ under a kernel free of the hypothesis, and an adversary that opens the seed name holds $(\rho,Y)$. So (F2) and (F1) make $\mathrm D^\top_1(K)$ the best advantage."
2. "Degenerate oracles" of the transfer, "since neither reveals the release noise". The coalition learns past noise from the releases, as open problem 5 says. The reason that matters is that $Z_t$ is independent of all that the coalition holds when it sets $\mathbf u_t$. Fix. "since the noise of each release is independent of everything the coalition holds when it sets that round's input".
3. Same paragraph, "and (c) and (d) hold in both disciplines". Part (c) concerns no certifier. Fix. "and (d) holds in both disciplines".
4. The fact map after the standing facts omits (F3) and (F5) of round 03 and (F7) of round 04, which have no counterpart. Fix. Add "(F3) and (F5) of round 03, (F7) of round 04 and Lyapunov's theorem of round 01 have no counterpart here."

## Assessment

Answers to the builder's questions. 1. Yes on both. The steering computation justifies rejecting "$R\to\infty$" (heuristic), and the restatement through $J^{\mathrm{fb}}$ with $N^\star\ge(1-\alpha-\alpha')J^{\mathrm{fb}}$ is correct (proven). 2. Yes, and the phrase still needs the accuracy level (ch-opening-scope, item 2). 3. Yes.

Fidelity. Every statement and label in the final document matches the register of `theory/CURRENT.md`. Every full proof is correct as written in the final document, with the two imprecise steps of ch-final-wording item 1 and ch-tightness-inline, neither of which changes a conclusion. No withdrawn or rejected content appears. The two blocking findings are sentences outside the theorem statements. One is an opening summary, the other a criterion-4 argument, and both are labelled proven. I keep the verdicts on [thm-black-box-certifiability] and [thm-bounded-deviation-transfer] at ACCEPT NONTRIVIAL, because their statements and proofs are correct and criterion 4 holds with the corrected witness above.

Simplicity. The final document carries no object that its proofs do not use, apart from the hypothesis class, which costs one symbol. The steering computation stays in the round file, and open problem 5 carries a short form. That split is right.

Readability. No semicolon, no dash used as punctuation, no bold, and no prose sentence over 30 words (computed, by a script that strips mathematics). Symbols are defined before use except $\mathbf e_1$. The seven clashes of ch-residual-symbols remain. The opening is checkable in two minutes.

Readiness. The final document is not ready for audit as it stands, because two sentences are false. Both fixes are one clause, and neither touches a theorem statement or a proof. If round 07 applies them with ch-choice-source and ch-residual-symbols and adds no new error, the stopping rule holds after that round. The definitions have now been accepted in three consecutive challenger files. Fifteen results stand accepted, eight of them NONTRIVIAL.

## Verdicts

Six definitions and fifteen results with slug tags in the final document are judged as they stand there. Two challenges are blocking: ch-opening-finite-queries and ch-drawn-seed-accuracy-level.

```text
VERDICT def-learning-oracle ACCEPT
VERDICT def-learning-oracle-model ACCEPT
VERDICT def-degenerate-oracles ACCEPT
VERDICT def-certifier ACCEPT
VERDICT def-model-bank ACCEPT
VERDICT def-isolated-client ACCEPT
VERDICT lem-needle-lower-bound ACCEPT
VERDICT lem-sphere-code ACCEPT
VERDICT lem-atomless-two-point ACCEPT
VERDICT lem-bank-fidelity ACCEPT
VERDICT thm-coupling-certificate ACCEPT NONTRIVIAL
VERDICT thm-black-box-certifiability ACCEPT NONTRIVIAL
VERDICT thm-dataflow-composition ACCEPT NONTRIVIAL
VERDICT thm-bounded-deviation-transfer ACCEPT NONTRIVIAL
VERDICT thm-replay-audit-steer ACCEPT NONTRIVIAL
VERDICT thm-perfect-substitution ACCEPT
VERDICT thm-reference-access ACCEPT
VERDICT thm-bank-soundness ACCEPT
VERDICT thm-active-choice-dichotomy ACCEPT NONTRIVIAL
VERDICT thm-record-level-certificate ACCEPT NONTRIVIAL
VERDICT thm-smoothed-choice-certificate ACCEPT NONTRIVIAL
BLOCKING 2
```
