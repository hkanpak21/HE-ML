# Round 05, challenger

Verdict of this turn. [thm-bounded-deviation-transfer] is correct in parts (a) to (e) and the corollary (proven, checked step by step below). It earns NONTRIVIAL, with a criterion-4 witness inherited from the pair code that holds in a stated regime. The node-indexed randomness of step 1 of [thm-dataflow-composition] (b) is legitimate by lazy sampling and changes no statement. It also repairs a pathwise step that the stopping clause of part (c) of that theorem already needed. All six definitions are accepted for the second consecutive time. Three challenges are blocking, and all three are in the final draft, not in the theory. The draft reverses the sentence on where the noise must sit for the scalar attack (ch-scalar-direction). Its opening summaries drop the hypotheses that make them true (ch-opening-hypotheses). Its tightness proof fails at $R=1$, because the draft dropped the hypothesis $R\ge2$ (ch-tightness-round-count). Each needs a one-sentence fix. Two further findings correct claims that the challenger role itself introduced in round 04. First, the first-order tightness sentence of part (c) is vacuous, since every admissible transfer function satisfies it. The content of (c) is a factor-form statement, given under ch-tightness-first-order. Second, the capacity value of open problem 5 ignores that the coalition sees its own releases and can cancel the release noise. At $R=3$ a feedback code beats that value for $c>(1+\sqrt2)/2$ (heuristic, ch-feedback-capacity).

Every non-trivial claim carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the argument is written here and the builder must write it out. Notation follows `theory/CURRENT.md` after round 05, and $\mathrm e$ denotes Euler's number where it could be confused with $\mathfrak e$. I opened no outside source this round. Shannon's coding theorem for the additive white Gaussian noise channel, with maximal error probability, is cited from memory and used only in heuristic claims.

## Status of the round-04 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-reference-strategy | not blocking | fixed | the clause that defines the prescribed input admits nodes the coalition cannot read (ch-prescribed-input-scope, not blocking) |
| ch-open-problem-five | not blocking | fixed as asked | the value I asked for is likely wrong at bounded $R$ (ch-feedback-capacity, not blocking) |
| ch-lower-bound-transfer | not blocking | fixed | none |
| ch-scalar-noise-placement | not blocking | fixed in the theory | the final draft states it reversed (ch-scalar-direction, blocking) |
| ch-euclidean-norm-proof | not blocking | fixed | none |
| ch-poisson-reason | not blocking | fixed | none |
| ch-symbol-clash | reopened | fixed for the round-04 list | the final draft carries new clashes (ch-draft-symbols, not blocking) |

Detail on ch-scalar-noise-placement. The builder's formula is right (proven). With the noise inside the ciphertext the decryptors see $a(\tilde u+Z_1)+e^{(a)}$, so dividing by $a$ leaves $\tilde u+Z_1+e^{(a)}/a$. The projection test then errs with probability $\bar\Phi((\mathfrak d/2-e_{\max}/a)/\sigma)$ under each hypothesis, which tends to $\bar\Phi(\mathfrak d/(2\sigma))$ as $a$ grows. So the scalar removes at most the decryption error. The theory and round-05/builder.md say this correctly. The draft does not.

Detail on ch-lower-bound-transfer. The new second sentence is exact. If $g_*P'_b=P_b$ for both $b$ with one measurable $g$, then $\mathrm H_\gamma(P_0\|P_1)=\mathrm H_\gamma(g_*P'_0\|g_*P'_1)\le\mathrm H_\gamma(P'_0\|P'_1)\le\theta'(\mathsf L)$, and the map may depend on $\mathsf L$ and on the adversary, since the inequality is needed for each $\mathsf L$ separately (proven).

## Definitions

### [def-learning-oracle]

Only notation changed, $\Pi_x$ and $n_{\mathrm{bit}}$. Well posed. Accepted in rounds 02 to 05. ACCEPT.

### [def-learning-oracle-model]

The definition is unchanged. The transfer remark is now exact (proven, above). The inversion remark keeps only its first sentence, which needs no object from later theorems. One term is undefined here and in the draft. "The learner names of nodes that $A$ owns or ships" uses "ships", which round 01 meant as "supplies the training code of a node it does not own". The draft must say so (ch-draft-wording). ACCEPT.

### [def-degenerate-oracles]

Unchanged and well posed. ACCEPT.

### [def-certifier]

Unchanged and well posed. ACCEPT.

### [def-model-bank]

Unchanged and well posed. The draft names it by slug without stating it (ch-draft-pointers). ACCEPT.

### [def-isolated-client]

Only the history sentence is dropped. I re-checked well-posedness against the new setting of [thm-bounded-deviation-transfer]. Coalition input nodes whose only child is $r_t$ are parents of $r_t$ other than $v_t$, so condition 3 holds with $O_t=u_t+o_t$, and condition 4 is untouched because the coalition owns no $v_t$ and no $r_t$ (proven, by inspection). This is the second consecutive acceptance. ACCEPT.

Simplicity. The six definitions are the smallest that carry the presented proofs. The hypothesis class $\mathcal H$ in a training input enters no presented proof, but it costs one symbol and the interface report needs it, so I do not ask for its removal.

## Proofs

### Bounded-deviation transfer [thm-bounded-deviation-transfer]

Claim. In every procedure that isolates client $j$ behind Gaussian releases, a coalition whose additive inputs stay within $B_A$ of the prescribed inputs has exceedance probability at most $\Upsilon_{\mathfrak e}$ of the protocol's, coupled runs of the protocol certify this at a cost free of $d$, and in $G^{\mathrm{agg}}_R$ every certifier sound over every learning function pays $e^{(1\pm o(1))\mathfrak e}$ Train calls when $\mathfrak e/d\to0$.

Assumptions. Def-isolated-client, with or without state, under the bottom or the top oracle. The coalition acts on the release only through input nodes whose single child is $r_t$, and their sum enters $O_t$ additively. Every other argument and value it sets is the protocol's, and it may stop after a release. The prescribed input $u^{\mathrm{pr}}_t$ is a measurable function of the values of nodes that run before $r_t$, other than the coalition's input nodes. The release noise is Gaussian and independent of everything else.

Threat model. An unbounded adaptive coalition that sees every release and, under the top oracle, client $j$'s seed of round $t$ before it sets the input of round $t$. Its own oracle calls and queries are unrestricted.

#### Setting

The clause on $u^{\mathrm{pr}}_t$ does what the proof needs (proven). Every node value other than the coalition's input values is a function of $(\Omega,y_{<t})$ by one map under both strategies, by step 1. So the prescribed input is that map composed with the prescription, also the same under both. A prescription cannot reach the coalition's earlier inputs through other nodes either. The only node that reads $Z_{t-1}$ is $r_{t-1}$, so no node value isolates $u_{t-1}$ from $y_{t-1}$. This closes the accumulation route that the builder's example $u^{\mathrm{pr}}_t=u_{t-1}$ uses.

The clause admits more than it should, which is a matter of meaning and not of truth. "Nodes that run before $r_t$" includes the input node of $D_j$ and $v_t$. A prescription that reads $W_t$ is a valid reference law, and (a) and (b) still hold for it, because the experimenter of (b) holds every input. Such a protocol cannot be played by the coalition, and then the sentence of (a) on $B_A=0$ describes an empty class (ch-prescribed-input-scope).

#### Part (a), the transfer

Step 0 (proven). The continued strategy is $B_A$-deviating, and on the node-indexed space it computes the same values as the stopping one until the stop. So the stopping strategy's exceedance is a maximum over a subset of the continued strategy's rounds.

Step 1 (proven). I checked the three facts and the induction. The new ingredient over round 04 is the third fact. Under the order-based assignment of round 03, a coalition-owned learning or evaluation node takes the next triple of the adversary's sequence. An adversary that makes one extra call of its own before that node shifts the triple, so the node's value is a different function of $\Omega$ under the two strategies, and the event $\{D^\star_0>\Delta\}$ is not one set $\mathbb A$. Under the node-indexed assignment it is one set. The exceedance reads $c_t,W_t,W'_t$ for $t\le R$, and $c_R$ is the value of a parent of $v_R$ or a choice made before $v_R$ runs, so $\mathbb A$ is a set of $(\Omega,y_{<R})$.

Step 2 (proven). $(\Omega,y_{<t})$ is a function of $(\Omega,Z_{<t})$, and $Z_t$ is independent of $(\Omega,Z_{<t})$. The kernels are Gaussian with positive densities, so $\mathbb P^{\mathrm{dev}}\ll\mathbb P^{\mathrm{pr}}$ and the density is the product of the $R-1$ ratios.

Step 3 (proven). I recomputed the moment. With $\delta_t=u_t-u^{\mathrm{pr}}_t$ and $Z=y_t-\bar y_t-u^{\mathrm{pr}}_t\sim\mathcal N(0,\sigma^2I_d)$ given $\mathcal F^{\mathrm{rel}}_t$, the ratio is $\exp(\langle Z,\delta_t\rangle/\sigma^2-\|\delta_t\|^2/(2\sigma^2))$, and its power $\varpi$ has conditional mean $\exp(\varpi(\varpi-1)\|\delta_t\|^2/(2\sigma^2))$ by (F6)(v) of the draft. The tower property over $t<R$ gives $\exp(\varpi(\varpi-1)\mathfrak e)$.

Step 4 (proven). Hölder's inequality with $\mathbf 1_{\mathbb A}^{\varpi/(\varpi-1)}=\mathbf 1_{\mathbb A}$ gives the first display. For the closed form, the logarithm of the bound is $-\mathfrak l+\mathfrak l/\varpi+(\varpi-1)\mathfrak e$, with derivative $\mathfrak e-\mathfrak l/\varpi^2$. If $\mathfrak l\le\mathfrak e$ the derivative is nonnegative on $\varpi\ge1$, so the infimum is $0$ at $\varpi\to1$. If $\mathfrak l>\mathfrak e>0$ the minimum at $\varpi=\sqrt{\mathfrak l/\mathfrak e}$ has value $-\mathfrak l+2\sqrt{\mathfrak l\mathfrak e}-\mathfrak e=-(\sqrt{\mathfrak l}-\sqrt{\mathfrak e})^2$. If $\mathfrak e=0$ the infimum $-\mathfrak l$ is approached as $\varpi\to\infty$. In each case the value is $\ln\Upsilon_{\mathfrak e}(p)$. The bounds on $\theta^{\mathrm{dev}}$ and $\theta^{\mathrm{dev},\leftarrow}$ follow from [thm-dataflow-composition] (b) through its terms $\epsilon_0$ and $\epsilon_1$, applied to the original adversary, which is an adversary of $G$. The continued strategy of step 0 never needs to be playable.

Three attempts to break (a), all failed. First, a coalition that owns a learning node, sends an honest clipped update as its prescribed input, and makes extra own Train calls before that node runs. Under node indexing the node's value is the same function of $\Omega$, so the bound holds. Under the round-03 indexing step 1 would fail pathwise. Second, a prescription that reads a release, $u^{\mathrm{pr}}_t=y_{t-1}$. It is a function of $(\Omega,y_{<t})$ by one map, so each step's deviation is still at most $B_A$ in conditional mean shift, and the exponent is unchanged. Third, a coalition that uses its inputs to cancel the release noise it has observed. The change of measure is conditional on the past, so it covers every adaptive strategy, and the bound holds.

#### Part (b), the certificate

Proven. Coverage is the Clopper and Pearson property for independent runs, and $\Upsilon_{\mathfrak e}$ is nondecreasing on $[0,1]$. With no exceedance, $\bar\epsilon_b=1-\alpha^{1/N'}\le\ln(1/\alpha)/N'$, and the condition on $N'$ gives $\sqrt{\ln(1/\bar\epsilon_b)}-\sqrt{\mathfrak e}\ge\sqrt{\ln(1/\epsilon_{\mathrm{acc}})}$, so $\Upsilon_{\mathfrak e}(\bar\epsilon_b)\le\epsilon_{\mathrm{acc}}$.

#### Part (c), tightness

The construction and the display are correct for $R\ge2$ (proven). Under the protocol's strategy $\langle m_R-m_1,\mathbf e_1\rangle\sim\mathcal N(0,(R-1)\sigma^2)$, and under $u_t=B_A\mathbf e_1$ its mean is $(R-1)B_A=\sqrt{2\mathfrak e}\,\sigma\sqrt{R-1}$. The two Mills-ratio bounds give the display with room. I computed both sides at $\mathfrak e\in\{0.5,2,8\}$ and $\iota$ up to $20$, and the slack was below $0.9$ against an allowance of at least $4.2$ (computed).

The last sentence of (c) is vacuous (proven). Every admissible $F$ satisfies $F(p)\ge p$, because the protocol's strategy is itself $B_A$-deviating, so some instance has $\epsilon_0=\epsilon^{\mathrm{pr}}_0=p$. And $\ln(1/p)/\ln(1/\Upsilon_{\mathfrak e}(p))\to1$ as $p\to0$ at fixed $\mathfrak e$. So "$\limsup\le1$" holds for the identity, which is not admissible, and it separates nothing. The phrase "tight to first order in the exponent" came from my round-04 sketch, and it was wrong to call that the content. The display carries the content. The gain of the transfer over the identity is the factor $\Upsilon_{\mathfrak e}(p)/p=\exp(2\sqrt{\mathfrak e\ln(1/p)}-\mathfrak e)$ for $\ln(1/p)\ge\mathfrak e$, which is unbounded. The display shows that every admissible $F$ pays all of it up to a factor logarithmic in $1/p$. The factor form is under ch-tightness-first-order.

The draft states (c) without $R\ge2$. At $R=1$ the threshold is $0$ and the sum of noises is empty, so the construction gives $\epsilon^{\mathrm{pr}}_0=0$, not $\bar\Phi(\iota)$, and the proof as written is false there (ch-tightness-round-count). The statement itself is true at $R=1$, since $\mathfrak e=0$ and a seed-dependent needle of mass $\bar\Phi(\iota)$ in round 1 realizes it (proven, sketch), but restoring $R\ge2$ is the smaller fix.

#### Part (d), the sharp lower bound

The code (proven). $d\langle\mathbf q_k,\mathbf q_l\rangle$ is a sum of $d$ independent signs, Hoeffding's inequality with range $2$ per term gives $2e^{-\mathfrak c^2d/2}$, and $J(J-1)e^{-\mathfrak c^2d/2}<J^2e^{-\mathfrak c^2d/2}\le1$ for $2\le J\le e^{\mathfrak c^2d/4}$. The first argument of $J_3$ uses $\lfloor\cdot\rfloor$ where my sketch used $\lceil\cdot\rceil-1$, which is equivalent up to the integer case and safe.

The cells and the threshold decoding (proven). The coordinate along $\mathbf q_k$ fails with probability $\Phi(-\mathfrak q_\eta)=\eta/4$. A competitor $l$ wins only if $\langle G,\mathbf q_l\rangle>\mathfrak m-\mathfrak q_\eta\mathfrak v-\mathfrak m\langle\mathbf q_k,\mathbf q_l\rangle\ge(1-\mathfrak c)\mathfrak m-\mathfrak q_\eta\mathfrak v$, and $\langle G,\mathbf q_l\rangle\sim\mathcal N(0,\mathfrak v^2)$ since $\|\mathbf q_l\|=1$. The choice of the second argument of $J_3$ makes the union at most $\eta/4$. $J_3\ge1$ forces the positive part to be positive, so (F6)(iii) applies.

The needles (proven). Distinct learner names keep rounds $t<R$ outside every $X_k$, so $y_t=B_A\mathbf q_k+Z_t$ under both hypotheses and $m_R$ is a function of $y_{<R}$. The averaging identity with $y_{<R}$ as common coordinate gives $\Pr[m_R\in V_k]\,\delta_{\mathcal N}(\varepsilon;B/\sigma)$.

The expansion and the constant $1/2$ (proven). With $\mathfrak c=2\sqrt{\mathfrak e/d}$ the first argument is $\lfloor e^{\mathfrak e}\rfloor$. The square expands to at least $2(1-\mathfrak c)^2\mathfrak e-2\sqrt{2\mathfrak e}\,\mathfrak q_\eta$ when $\mathfrak q_\eta\le(1-\mathfrak c)\sqrt{2\mathfrak e}$, and $\ln J'\le(1-\mathfrak c)^2\mathfrak e+\ln(\eta/2)<\mathfrak e$ makes the second argument the minimum. $\lfloor J'\rfloor\ge J'/2$ for $J'\ge1$. So $\ln J_3\ge\mathfrak e(1-4\sqrt{\mathfrak e/d})-\mathfrak q_\eta\sqrt{2\mathfrak e}+\ln(\eta/4)$. In units of $(R-1)B_A^2/\sigma^2$ this is $1/2-o(1)$ when $\mathfrak e/d\to0$, and the upper bound of the corollary gives $1/2+o(1)$ when $\ln R=o(\mathfrak e)$. The constant $1/2$ is proven in that regime.

#### Part (e), drawn seeds

Proven. The pair code sits in round 1 translated by $m_1$, the clip is the identity on norm $B$, the protocol's input $u_1=0$ is admissible at every $B_A\ge0$, and the adversary that reads $y_1$ sees the view of [thm-dataflow-composition] (e)(ii). Projection gives the divergence by data processing. The family agrees at every training input other than the two round-1 inputs at $m_1$, so the collision bound applies. At the reference function every coupled pair coincides, and under the top oracle the seed reveals nothing about the hypothesis, so $\theta^{\mathrm{agg}}_R=0$.

#### The corollary and the fixed-ratio remark

The corollary is correct (proven). The lower bound is (d) read at an accurate certifier. The upper bound runs both certificates at level $\alpha/2$ with $2R$ calls per run and $n_{\mathrm{oth}}=0$, so $N=4RN'$. The asymptotics use $\ln\lceil aE\rceil\le\ln(a+1)+\ln E$ for $E\ge1$.

The fixed-ratio remark is correct (proven). With $\mathfrak c=2\sqrt c/(1+2\sqrt c)$, the first argument has exponent $\mathfrak c^2d/4=\mathfrak e/(1+2\sqrt c)^2$, and the second has $(1-\mathfrak c)^2\mathfrak e=\mathfrak e/(1+2\sqrt c)^2$ up to $O(\sqrt{\mathfrak e})$. The builder's crossover with the sphere code of [thm-smoothed-choice-certificate] (d) is right. $J_1$ has exponent $\min\{0.1248\,d,\mathfrak e/4\}$, which beats $\mathfrak e/(1+2\sqrt c)^2$ exactly for $1/4<c<1.45$ (computed, crossover at $c\approx1.45$).

#### Weakest step

Step 1 of (a). It is correct as written, and it is the only step that depends on how the randomness is represented. Its correctness rests on two clauses that the final document must state in the setting, the node-indexed representation and the prescription as a function of node values other than the coalition's input nodes. As a statement, the weakest part is the last sentence of (c), which is true and empty.

#### Non-triviality, judged strictly

Criterion 1. $\epsilon^{\mathrm{pr}}_b$ is defined by the coupled execution, two Train calls per round that share a seed name. Met.

Criterion 2. Part (a) is a change-of-measure inequality that holds for any concrete learning function. The theorem is the pair of (a) and (b). It certifies privacy against every $B_A$-deviating adaptive coalition. Doing this for a trained transformer without seed control needs the law of the trained model at every starting model the coalition can reach, a ball of dimension $d$ around a Gaussian random walk, and with state every reachable history. Met.

Criterion 3. The bound and the certificate depend on $\mathsf L$ only through $\epsilon^{\mathrm{pr}}_b$, and the cost is free of $d$, $B$, the state and the architecture. Met.

Criterion 4. The witness is (e), in the drawn-seed discipline under item 3 of [def-degenerate-oracles]. It holds only in a regime, which the draft does not say. At the reference function of (e), the coupled certificate reaches accuracy $\epsilon_{\mathrm{acc}}$ with $2R\lceil\ln(1/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)\rceil$ calls. A drawn-seed certifier needs about $\sqrt{\eta/2}\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$ (proven, by (b) and (e)). So the certificate fails under drawn seeds exactly when the first number is below the second. That holds at $B_A=0$ and at every $B_A$ with $\mathfrak e$ well below $\min\{0.06\,d,B^2/(32\sigma^2)\}$, and in particular for $B_A\ll B/\sqrt R$ (heuristic comparison of exponents). Beyond it, (d) makes both disciplines pay $e^{(1-o(1))\mathfrak e}$, and no separation is claimed. Criterion 4 asks for failure in one instance, so it is met. The witness is shared with [thm-dataflow-composition], and the audit should not read the two NONTRIVIAL tags as independent evidence on criterion 4.

ACCEPT NONTRIVIAL.

### Dataflow composition, randomness by node [thm-dataflow-composition]

The answer to the builder's question 1 is yes. The clarification is legitimate, changes no statement, and the transfer's use of it is correct.

Legitimacy (proven). Each node runs at most once, and whether it runs is decided by values computed before it. Serve each node's required call from a triple indexed by the node, and the adversary's own calls from an independent sequence in order. Then each call receives a triple that is independent of everything revealed before it, with law $\mu\otimes\pi\otimes\nu$, by lazy sampling. So the joint law of the execution and the transcript is the one fidelity prescribes, whichever assignment is used. One caveat on wording. Names are per-caller counters, and the adversary's own calls shift the integers that the coalition's required calls receive. "The same maps" is therefore a statement about stored objects, and a node argument that is a name stands for the object it names. One clause in step 1 says so.

Earlier proofs (proven, by inspection of each). No proof relied on the order-based form in a way that the node-indexed form breaks.

1. Steps 2 to 5 of (b) and the sum bound fix one adversary, so either assignment works.
2. The stopping clause of (c), "every strategy that agrees with the protocol's until a stop", compares two adversaries pathwise. When the coalition owns a learning or evaluation node and the stopping adversary makes own calls before the stop, the order-based form breaks that comparison, and the node-indexed form repairs it. The clarification was needed there as well, not only in round 04.
3. [thm-active-choice-dichotomy] (a)(i) computes the law of a non-adaptive strategy directly from the $\zeta_t$, and (a)(ii) uses its own table indexed by prefixes. Neither compares two adversaries pathwise.
4. [thm-smoothed-choice-certificate] (a) compares a strategy with its continuation, played by the same adversary until the stop.
5. [lem-needle-lower-bound] couples two certifier runs by call order, on its own space. The runs make identical calls until the hit, so call order is the right index there.

The Reading of (a)(iii) is correct in the round file (proven, above). ACCEPT NONTRIVIAL.

### Smoothed-choice certificate after the split [thm-smoothed-choice-certificate]

Parts (a), (b), (d) and (e) stand as accepted in round 04. Without part (c), criterion 4 rests on the covering certificate (b) with (e), as round 04 already found for (b). The crossover between $J_1$ and $J_3$ is checked above. One clause for the draft. The covering certificate beats the transfer only when $\mathfrak e$ exceeds about $d\ln(R^{3/2}\sqrt d/\epsilon_{\mathrm{acc}})$ (heuristic comparison of costs, round 04), and the pointer sentence of the draft should say so, since otherwise a reader cannot tell why the theorem is listed. ACCEPT NONTRIVIAL.

### Bank soundness, reason [thm-bank-soundness]

The reason now reads as asked. ACCEPT.

### Record-level certificate, the average form [thm-record-level-certificate]

The average form moved from the inversion remark into the register line, where its three objects are defined. Its proof is the definition of $\mathrm H_\gamma$ averaged over the records (proven, round 04). ACCEPT NONTRIVIAL.

## The final draft

I read `final/learning-oracle-theory.md` against three standards. Its PDF has 18 pages (computed). It has no dash, no bold and no semicolon in prose. Italics appear only at definitions (computed, by search). No prose sentence exceeds 30 words, except where a heading or a display merges with the sentence in my count (computed).

Fidelity. I compared every statement and every full proof with the accepted text of the rounds.

1. Full proofs. Correct as written: [lem-needle-lower-bound], [lem-sphere-code], [thm-coupling-certificate] (a) and (b), [thm-black-box-certifiability] (o) and (a), [thm-dataflow-composition] (b), (c) and (e)(ii), [thm-bounded-deviation-transfer] (a), (b), (d), (e) and the corollary, and [thm-replay-audit-steer] (a) and (b) (proven, checked line by line). I re-derived (F3) in both orders, the kernel of (F6)(ii), the Balle and Wang form of (F6)(i), and Hoeffding's constant in the proof of black-box (a). The draft's own fact numbering is used consistently. The single exception is the proof of [thm-bounded-deviation-transfer] (c), which fails at $R=1$ (ch-tightness-round-count).
2. Stated parts. One sentence is reversed. "Unchecked decryption lets a public scalar divide the protecting noise, unless the noise is added at decryption" says the opposite of the accepted Reading (ch-scalar-direction). [thm-bank-soundness] carries the bare label proven, while part (c) is heuristic. Several pointers name fewer rounds than the register (ch-draft-pointers).
3. The opening. Items 1, 2 and 5 drop hypotheses without which they are false, and item 4 states the price while omitting the transfer, which is the theorem (ch-opening-hypotheses).
4. Withdrawn or rejected content. None appears. thm-own-data-only is absent, and the second half of [thm-bank-soundness] (d) is absent.
5. Constants. $0.18$, $0.1887$, $J_{\mathrm{cd}}$, $J_3$, the expansion with $\ln(\eta/4)$, $4R$, and the Reading's $\sqrt{\eta/2}\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$ match the rounds. The DP-FedAvg Reading drops the conditions of the corollary (ch-reading-conditions).

Simplicity. The five definitions are the smallest that carry the presented proofs. The query channel, the allowance and label eval are used only by [thm-black-box-certifiability], which is a reason to keep that section (see Steering). Nothing in the draft is there only because the rounds had it, with two exceptions. The first is the vacuous last sentence of (c), which should be replaced, not cut. The second is the pointer sentence for [thm-smoothed-choice-certificate], which needs its regime to justify itself.

Readability. The opening is checkable in two minutes, except that a reader cannot find the main new bound in it. Every symbol is defined before use, with three exceptions. "Train" appears in the opening before def-learning-oracle, "ships" is never defined, and $\mathbb P^{\mathrm{dev}},\mathbb P^{\mathrm{pr}}$ name generic laws in (F7) before the theorem gives them their meaning. One name per thing fails in nine places (ch-draft-symbols). A reader who follows a pointer into a round file meets the old fact numbers, for instance (G3) for the draft's (F6)(iii), with no map (ch-draft-pointers).

## New challenges

### ch-scalar-direction

BLOCKING. A false statement in the draft. Targets the paragraph "The other parts, stated" of [thm-dataflow-composition] in `final/learning-oracle-theory.md`. The draft says: "Unchecked decryption lets a public scalar divide the protecting noise, unless the noise is added at decryption." The accepted Reading says the reverse. The attack divides the noise exactly when the decryptors add it at decryption, and noise added by the client inside its ciphertext is scaled with the update. Smallest fix. "Unchecked decryption lets a public scalar divide the protecting noise when the decryptors add that noise at decryption. Noise that client $j$ adds inside its ciphertext is scaled with the update, and the scalar then removes at most the decryption error."

### ch-opening-hypotheses

BLOCKING. Three summaries in "What the theory shows" are false as written, and a fourth misstates the theorem.

1. Item 1, "while drawn seeds certify nothing below one on atomless views". This is false for a general channel. A constant channel has atomless views and $\theta\equiv0$, which a certifier that outputs $0$ certifies. The accepted statement, (a)(iii), needs a deterministic channel. Fix. "Through a deterministic channel with atomless view laws, drawn seeds certify nothing below one."
2. Item 2, "no experiment with drawn seeds certifies that it equals white-box leakage". This is false for atomic model laws. The accepted (c) needs deterministic evaluation and atomless model laws. Fix. Add "with deterministic evaluation and atomless model laws".
3. Item 5, "which grinding attains". Under hardware randomness grinding attains a multiple of the reach at $\tau/2$, discounted by the spread, and whether the gap closes is open problem 7. Fix. "which grinding attains within a factor $3.2$ under deterministic kernels".
4. Item 4 states the price and omits the transfer. Fix. "Bounded-deviation transfer. If a coalition's additive inputs stay within $B_A$ of the prescribed ones, its exceedance probability is at most a fixed transform $\Upsilon_{\mathfrak e}$ of the protocol's, with $\mathfrak e=(R-1)B_A^2/(2\sigma^2)$. Coupled runs of the protocol certify it with about $e^{\mathfrak e}\ln(1/\alpha)$ runs, free of $d$. In the aggregation instance no certifier sound for every learning function needs fewer than $e^{(1-o(1))\mathfrak e}$ Train calls when $\mathfrak e/d\to0$ (proven)."

### ch-tightness-round-count

BLOCKING. A proof in the draft is false for a case its statement covers. Targets [thm-bounded-deviation-transfer] (c) in the draft, "In $G^{\mathrm{agg}}_R$ let $B_A>0$ and $B\ge2\Delta$." At $R=1$ the construction gives $\epsilon^{\mathrm{pr}}_0(\Delta)=0$. Smallest fix. "In $G^{\mathrm{agg}}_R$ let $R\ge2$, $B_A>0$ and $B\ge2\Delta$", as in round-05/builder.md.

### ch-tightness-first-order

Not blocking. Due before the final document. Targets the last sentence of (c), the register line ("tight to first order in the exponent"), the sentence "Parts (c) and (d) show that neither the transfer nor its price improves to first order" and the Verdict of round-05/builder.md. The limsup sentence holds for every admissible $F$, since $F(p)\ge p$ and $\ln(1/p)/\ln(1/\Upsilon_{\mathfrak e}(p))\to1$ (proven, under Proofs). Smallest fix. Replace the last sentence of (c) by the following, with its two-line proof.

"So every function $F$ with $\epsilon_0(\Delta)\le F(\epsilon^{\mathrm{pr}}_0(\Delta))$ in all these instances satisfies, for every $p\in(0,\bar\Phi(\sqrt{2\mathfrak e}+1))$,
$$F(p)\ \ge\ \frac{\mathrm e^{-2}\,\Upsilon_{\mathfrak e}(p)}{8\ln(1/p)},\qquad\text{while}\qquad\frac{\Upsilon_{\mathfrak e}(p)}{p}=\exp\big(2\sqrt{\mathfrak e\ln(1/p)}-\mathfrak e\big)\ \text{ for }\ln(1/p)\ge\mathfrak e."$$

Proof (proven, sketch). Let $p=\bar\Phi(\iota)$, so $\iota>\sqrt{2\mathfrak e}+1>1$. (F6)(iii) gives $\ln(1/p)\ge\iota^2/2$, so $\iota+1\le2\iota\le2\sqrt{2\ln(1/p)}$ and $2\ln(\iota+1)\le\ln(8\ln(1/p))$. The display of (c) then gives $\ln(1/F(p))\le\ln(1/\Upsilon_{\mathfrak e}(p))+\ln(8\ln(1/p))+2$. In words, the transfer gains over the identity a factor that grows like $\exp(2\sqrt{\mathfrak e\ln(1/p)})$, and no admissible transfer function keeps more than a logarithmic share of that factor. The register line should read "The transfer function is tight up to a factor logarithmic in the inverse of the protocol's exceedance probability."

### ch-feedback-capacity

Not blocking. Due before the final document. Targets open problem 5 in `theory/CURRENT.md` and in the draft, and my own round-04 heuristic behind it. The conjectured value $\ln(1+2c)/(2c)$ is the capacity of the channel from the sum of the coalition's inputs to $m_R$ without feedback. At every needle function and at $\mathsf L^\circ$, rounds $t<R$ release $y_t=u_t+Z_t$, so the coalition learns $Z_t$ exactly and can cancel it in later inputs.

Counter-heuristic at $R=3$ (heuristic, from Shannon's coding theorem with maximal error, cited from memory, and [lem-needle-lower-bound]). Here $\mathfrak e=B_A^2/\sigma^2$ and $c=\mathfrak e/d$. Let $u_1$ carry a codeword and $u_2=a_2-Z_1$, with $\|a_2\|^2\approx B_A^2-d\sigma^2$ in high dimension. Then $m_3-m_1=u_1+a_2+Z_2$, the signal-to-noise ratio per coordinate is $(\sqrt c+\sqrt{c-1})^2$, and needles on decoding cells of a capacity-achieving code give $\liminf\ln N^\star/\mathfrak e\ge\ln(1+(\sqrt c+\sqrt{c-1})^2)/(2c)$. This exceeds $\ln(1+2c)/(2c)$ exactly when $c>(1+\sqrt2)/2\approx1.207$. At $c=4$ the two values are $0.338$ and $0.275$ (computed). The gain from cancellation vanishes as $R\to\infty$ at fixed $c$, because each round's budget $B_A^2=2cd\sigma^2/(R-1)$ then covers a vanishing fraction of the noise (heuristic count). Smallest fix. Either add "$R\to\infty$" to the limit of open problem 5, or replace the conjectured value by "the capacity, per unit of $\mathfrak e$, of the channel from the coalition's inputs to $m_R$ with the releases fed back", and record the $R=3$ computation as heuristic. The proven bounds $(1+2\sqrt c)^{-2}\le\liminf\le\limsup\le1$ are unaffected.

### ch-prescribed-input-scope

Not blocking. Targets the setting of [thm-bounded-deviation-transfer] in the theory and the draft, "a measurable function of the values of the nodes that run before $r_t$, other than these input nodes". The clause admits the input node of $D_j$ and $v_t$, which yields protocols the coalition cannot play (proven, under Proofs). Smallest fix. "a measurable function of the values of the nodes that the coalition owns or receives through the plain channel before $r_t$ runs, other than these input nodes". The proof is unchanged, since these are node values.

### ch-drawn-seed-regime

Not blocking. Targets "The certificate (b) fails in the drawn-seed discipline at every $B_A\ge0$, by (e)" in the draft, and the same phrase in round-05/builder.md. The separation holds only where the coupled cost is below the drawn-seed cost (proven, under Non-triviality). Smallest fix. "At the reference function of (e), the certificate (b) is accurate to $\epsilon_{\mathrm{acc}}$ with $2R\lceil\ln(1/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)\rceil$ Train calls, while every drawn-seed certifier needs about $\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$. So (b) fails in the drawn-seed discipline whenever the first number is below the second, for instance at $B_A=0$."

### ch-reading-conditions

Not blocking. Targets the Reading of [thm-bounded-deviation-transfer] in the draft, "certification costs $e^{(1+o(1))(R-1)/2}$ Train calls as $R$ grows with $R/d\to0$". "Certification" is undefined, and the corollary's condition on $\Delta$ and $\epsilon_{\mathrm{acc}}$ is missing. At $B/\sigma=1$ and $\varepsilon=1$ the condition needs $\epsilon_{\mathrm{acc}}$ below about $0.12$, since $\delta_{\mathcal N}(1;1)\approx0.127$ (computed). Smallest fix. "the least number of Train calls of a certifier that is sound for every learning function and accurate to $\epsilon_{\mathrm{acc}}$ at the reference function is $e^{(1+o(1))(R-1)/2}$ as $R$ grows with $R/d\to0$, for fixed $\epsilon_{\mathrm{acc}},\alpha,\alpha',\eta$ that meet the condition of the corollary with a threshold $\Delta$ of order $\sigma/\sqrt R$".

### ch-draft-symbols

Not blocking. Due before the final document. One name, two objects, in the draft.

| Symbol | First object | Second object, where | Fix |
| --- | --- | --- | --- |
| $G$ | procedure | Gaussian vector in [lem-sphere-code] (b) and in (d) of the transfer | $\mathbf g$ |
| $V_k$ | Voronoi cells, [lem-sphere-code] | threshold cells, (d) of the transfer | $V^{\mathrm{th}}_k$ |
| $W$ | value $W_t$ of $v_t$ | other randomness, proof of (e)(ii), step 2 | $\omega'$ |
| $c'_t$ | (reads as) a second choice | clipped difference, step 4 of the proof of (b) | $\mathbf b_t$ |
| $\beta_1$ | coupled tail of round 1 | coupled divergence at $\gamma=1$, proof of [thm-coupling-certificate] (c) | "$\beta_\gamma(K)$ at $\gamma=1$" |
| $L$ | learning function $\mathsf L$ (font only) | laws $L_b$, $L_{\mathrm{hyb}}$, $L,L',L''$ of (F3) | $\mathcal L_b$, $\mathcal L_{\mathrm{hyb}}$ |
| $u$ | query $u\in\mathcal U$ | coalition input $u_t\in\mathbb R^d$ | $\mathbf u_t$, bold like $\mathbf p_k$ and $\mathbf q_k$ |
| $m_1$ | starting model of round 1 | first replay in [thm-replay-audit-steer] | $m^{\mathrm{rep}}_i$ |
| $I$ | index map $I(\rho)$ | identity matrix $I_d$ | $\mathrm{ix}(\rho)$ |

### ch-draft-pointers

Not blocking. Due before the final document. Six items, each a one-clause fix.

1. "Model banks [def-model-bank]" names a definition that the draft never states. Either state it in two sentences or drop the slug and keep the name.
2. [thm-bank-soundness] is labelled "(proven, round-01/builder.md)". The register says proven for (a), (b) and the first half of (d), heuristic for (c), with proofs in rounds 01 to 05. Copy that.
3. [lem-atomless-two-point] points to round-01 only. Add "with corrections in round-02 and round-03".
4. Open problem 1 in the draft drops condition (ii), never above $\epsilon_0$, and the meaning of "certifiable", a uniformly accurate coupled-discipline certifier with calls fixed by $\alpha$, $\epsilon_{\mathrm{acc}}$, $R$ and $n_h$. Add both clauses.
5. The proof of [thm-coupling-certificate] (a)(ii) uses McDiarmid's inequality, which is not among the standing facts. Add it to (F8).
6. The round files number the facts differently, for instance (G3) for the draft's (F6)(iii) and (F2) for the draft's (F5). Add one sentence under Standing facts that maps the old numbers to the new.

### ch-draft-wording

Not blocking. Six sentences.

1. Proof of [thm-coupling-certificate] (b), step 3, "So its transcript is the image of its view under a kernel free of the hypothesis." The view is the transcript, so the sentence is circular. Fix. "the image of the channel output".
2. Proof of [thm-dataflow-composition] (c), "its $\epsilon_0(\Delta)$ is smaller". Fix. "is no larger".
3. [def-learning-oracle-model], "nodes that $A$ owns or ships". Fix. "nodes that $A$ owns or whose training code $A$ supplies".
4. (F2), "integrates against $P_0-\gamma P_1$ to at most the mass of its positive set". Fix. "For $g$ with values in $[0,1]$, $\int g\,d(P_0-\gamma P_1)\le\mathrm H_\gamma(P_0\|P_1)$."
5. [lem-needle-lower-bound], "a sound certifier must output at least $\vartheta$". Fix. "must output at least $\vartheta$ with probability at least $1-\alpha$".
6. Opening, "or they stall". Cut the clause.

## Steering

### Answers to the builder's questions

1. Yes. The node-indexed form is a clarification that changes no statement, it is legitimate by lazy sampling, and step 1 of the transfer uses it correctly. It also repairs the stopping clause of [thm-dataflow-composition] (c). Add the clause on names.
2. Keep [thm-black-box-certifiability] (o) and (a). They are the only presented proofs that use the query channel, the allowance and label eval. Without them those clauses would be carried in the definitions for pointers only. [thm-perfect-substitution] stays a pointer, cited once in the remark of [def-degenerate-oracles]. [thm-active-choice-dichotomy] (a)(i) would repeat the message of the transfer section.
3. No, not at bounded $R$. The capacity value ignores feedback, and the $R=3$ computation under ch-feedback-capacity beats it for $c>1.207$ (heuristic). Restate the problem with $R\to\infty$, or with the feedback capacity as the conjectured value.

### What round 06 must do

No new theorem. The builder closes the three blocking challenges, which are one sentence each, and the eight non-blocking ones, in the draft and in `theory/CURRENT.md`. Two of them change mathematics, the factor form of (c) under ch-tightness-first-order and the restated open problem 5. The challenger of round 06 then reads the revised draft as the final document. It re-checks the factor form, confirms the six definitions a third time, and runs `node scripts/verify.mjs final`.

For the final document to pass an audit, five things must hold. Every opening summary carries the hypotheses of its theorem. Every full proof is correct in every case its statement covers. Every pointer names the rounds that the register names. The table under ch-draft-symbols is applied. And the criterion-4 regime of the transfer is stated where the draft claims the failure. The orchestrator's gate G7 asks for a line-by-line check of each NONTRIVIAL proof in the draft. The list under "Fidelity, full proofs" above gives the order, and the proof of (c) of the transfer must be included after its fix.

### Convergence

This is review round five of at least six. Definitions. All six are accepted here and in round 04, so the condition on definitions holds now and must hold again in round 06. Results. Fifteen results stand accepted, eight of them NONTRIVIAL (counted from the latest verdicts of rounds 00 to 05), far above six and three. Blocking. Three, all in the draft, all fixable in one sentence. If round 06 closes them and introduces no new blocking challenge, the stopping rule is met after round 06, and the audit can follow.

## Verdicts

Six definitions and five revised or new results are judged. The other results keep their round-04 verdicts. Three challenges are blocking: ch-scalar-direction, ch-opening-hypotheses and ch-tightness-round-count.

```text
VERDICT def-learning-oracle ACCEPT
VERDICT def-learning-oracle-model ACCEPT
VERDICT def-degenerate-oracles ACCEPT
VERDICT def-certifier ACCEPT
VERDICT def-model-bank ACCEPT
VERDICT def-isolated-client ACCEPT
VERDICT thm-bounded-deviation-transfer ACCEPT NONTRIVIAL
VERDICT thm-smoothed-choice-certificate ACCEPT NONTRIVIAL
VERDICT thm-dataflow-composition ACCEPT NONTRIVIAL
VERDICT thm-bank-soundness ACCEPT
VERDICT thm-record-level-certificate ACCEPT NONTRIVIAL
BLOCKING 3
```
