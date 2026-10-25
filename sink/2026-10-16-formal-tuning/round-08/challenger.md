# Round 08, challenger

Verdict of this turn. The blocking challenge of round 07, ch-strategy-calls, is closed, and so are the three non-blocking ones. Restated part (e) of [thm-bounded-deviation-transfer] is true, and its proof in the final document is complete (proven). The corrected Reading of [thm-dataflow-composition] (e)(ii) is right, and the old first argument of the minimum was larger than the proven one by exactly $\sqrt2$ (proven, and computed). Open problem 2 of `theory/CURRENT.md` states the proven count but drops the soundness of the certifier (not blocking). All 25 changed cost sentences match their statements, and the five complete entries I sampled omit no source of calls. The six definitions are accepted for the fifth consecutive round. For hardening I re-derived from scratch the full proofs of [thm-dataflow-composition], parts (b), (c) and (e)(ii), and of [thm-bounded-deviation-transfer], parts (a) to (e) and the corollary, as the final document writes them. Both hold. I found no false statement, no wrong step and no ill-posed definition. Three challenges remain, none blocking. In part (e) of the transfer one expression is undefined when $N'<\ln(1/\alpha)$ (ch-upsilon-domain). The remark after def-isolated-client in the final document gives a wrong reason and leaves the passive stop implicit (ch-passive-stop). Three wording items remain (ch-closing-clarity). `node scripts/verify.mjs final` prints `FINAL OK theorems=5 nontrivial=5 items=21`.

Every non-trivial claim carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the argument is written here and the builder must write it out. "Computed" marks a number from a short script run this round. Notation follows `theory/CURRENT.md` after round 08. I opened no outside source.

## Status of the round-07 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-strategy-calls | blocking | closed, with "at most", which is needed | none |
| ch-transfer-drawn-seed-target | not blocking | closed, (e) restated for $\theta^{\mathrm{dev}}$, proof complete | domain of $\Upsilon_{\mathfrak e}$ in (e) (ch-upsilon-domain) |
| ch-opening-isolation | not blocking | closed as proposed | none |
| ch-final-readability | not blocking | closed, all four items | none |

### ch-strategy-calls

Part (c) of [thm-dataflow-composition] now reads "Each run costs at most $2R$ Train calls for client $j$, plus the calls of the other nodes and the strategy's own Train calls." This answers the counterexample of round 07 (proven). The word "at most" is needed, since a run ends at a stop and client $j$ then makes $2t<2R$ calls. The clause restores the statements of round-02/builder.md, line 145, and round-03/builder.md, line 173, which I read. Both say "plus the calls of the other honest nodes and of the strategy". The proof of (c) needs no change (proven). Coverage uses only that the $n$ indicators of $D^\star_0>\Delta$ are independent Bernoulli variables with parameter $\epsilon_0(\Delta)$.

One reading point, not a challenge. Part (c) states a cost per run. It does not claim that its experimenter is a certifier with a fixed $N$ in the sense of def-certifier. A strategy may make an almost surely finite but unbounded number of calls, and then no fixed $N$ exists. Since (c) makes no such claim, nothing in it is false.

The remark after [def-isolated-client] and the register line carry the clause in both files. The register line also covers "its stopping variants" for any named strategy. That is true (proven). The proof of (c) compares a strategy with its stopping variant on the space of step 1 of the proof of (b), and it uses nothing about the strategy before the stop.

### ch-transfer-drawn-seed-target

Part (e) now targets $\theta^{\mathrm{dev}}$ and carries the bound to $\theta^{\mathrm{agg}}_R$ by the remark of def-certifier. I re-derived the statement from the definitions (proven). The steps follow.

1. The family. $\mathsf L^\circ$ and the needle functions $\mathsf L_\varsigma$ differ only at the two inputs $x((1,m_1),D^b_j)$, and every member returns the starting model at learner names $\ell_t$ with $t\ge2$. Under every $B_A$-deviating strategy client $j$'s round-1 input is one of the two, since the server sets $m_1$ and the strategy sets no argument of client $j$'s node.
2. Each needle function leaks. Under the protocol's strategy $\mathbf u_1=\mathbf u^{\mathrm{pr}}_1=0$, and $\Vert W_1-m_1\Vert=B$, so the clip is the identity and $y_1=\mathbf p+Z_1$ for the code point $\mathbf p$. The projection of the view on $y_1$ is one measurable map under both hypotheses. (F2) and step 3 of the proof of (e)(ii) give $\theta^{\mathrm{dev}}(\mathsf L_\varsigma)\ge\vartheta$.
3. The drawn-seed transcript. Step 2 of the proof of (e)(ii) does not use the target. It bounds the total variation between the transcript laws under $\mathsf L^\circ$ and under the uniform mixture over $\varsigma$ by $\binom{2N}{2}/J_{\mathrm{cd}}=N(2N-1)/J_{\mathrm{cd}}$. A drawn-seed certifier that passes a model name as the starting model still names a training input by value, so each answer at one of the two inputs is a fresh draw of its law. Soundness at each $\mathsf L_\varsigma$, averaged over $\varsigma$, gives the bound at $\mathsf L^\circ$.
4. The reference function. At $\mathsf L^\circ$ the round-1 model is $m_1+\mathbf p^{\mathrm{sg}(\rho)}_{\mathrm{ix}(\rho)}$ at both inputs, so $\theta^{\mathrm{agg}}_R(\mathsf L^\circ)=0$ under both oracles. Under the top oracle a Train call with the honest seed name returns the same value at both inputs. Every coupled pair coincides, so no run of $\mathsf{Ex}_b$ exceeds $\Delta$ and $\bar\epsilon_b\le1-\alpha^{1/N'}\le\ln(1/\alpha)/N'$.
5. The larger target. $\theta^{\mathrm{agg}}_R\ge\theta^{\mathrm{dev}}$ at every learning function, so a certifier sound for $\theta^{\mathrm{agg}}_R$ is sound for $\theta^{\mathrm{dev}}$ and the bound binds it.

The proof in the final document states steps 2 and 4 and points to (e)(ii) for step 3. Step 1 is implicit in "placed in round 1", and step 5 is in the statement. That suffices.

The criterion-4 paragraph now compares two certifiers of one target. Its threshold follows from (e) (proven). With $J_{\mathrm{cd}}\le e^{B^2/(16\sigma^2)}$, (F6)(iii) gives $(2J_{\mathrm{cd}}-1)\bar\Phi(B/(2\sigma))\le J_{\mathrm{cd}}e^{-B^2/(8\sigma^2)}\le e^{-B^2/(16\sigma^2)}$. A larger threshold implies the smaller one, so the probability bound carries over. The second argument of $J_{\mathrm{cd}}$ is always at least one, and the first is at least one exactly from $d=6$, since $2^{0.08}=1.057$ and $2^{-0.1}=0.933$ (computed). A drawn-seed certifier with $N(2N-1)<\eta J_{\mathrm{cd}}$ outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}$ with probability below $\alpha+\eta$, while (b) does so with probability one. The witness of round-07/builder.md is unchanged and correct.

### The Reading of (e)(ii) and open problem 2

The necessary condition is right (proven). Part (e)(ii) gives $\Pr[\hat t<\vartheta]\le\alpha+N(2N-1)/J_{\mathrm{cd}}$. If the left side exceeds $\alpha+\eta$, then $N(2N-1)>\eta J_{\mathrm{cd}}$. Since $N(2N-1)<2N^2$, this forces $N>\sqrt{\eta J_{\mathrm{cd}}/2}$, which is a proven bound and not only an estimate. With $J_{\mathrm{cd}}\le2^{0.18d-1}$ the first branch gives $\sqrt{\eta J_{\mathrm{cd}}/2}\le\sqrt{\eta/2}\,2^{0.09d-1/2}$. The old expression $\sqrt{\eta/2}\,2^{0.09d}$ was larger by $\sqrt2$ (proven). At $\eta=1$ and $d\in\{20,50,100\}$ the exact value of $\sqrt{J/2}$ for $J=2^{0.18d-1}$ is $1.741$, $11.31$ and $256$, equal to the new expression, against $2.462$, $16.0$ and $362.0$ for the old one (computed). The "about" now covers only the floors.

The added sentence "Each run needs only client $j$'s two Train calls, since the choice is fixed" is true (proven). With $R=1$, $O_1=0$ and a fixed $c$, $D^\star_0=\Vert W'_1-W_1\Vert$, and two calls give the indicator its law whatever the other nodes do.

Open problem 2 in `theory/CURRENT.md` states the same count with $J_{\mathrm{cd}}$ defined. Its first sentence reads "Over $\mathfrak L_B$, a drawn-seed certifier that outputs below ... needs $N$ Train calls with $N(2N-1)>\eta J_{\mathrm{cd}}$." Without "sound at level $\alpha$" it is false (proven, by example). When the threshold is positive, the certifier that outputs zero makes no call and outputs below it with probability one. The words "Over $\mathfrak L_B$" suggest the soundness class but do not state soundness. The fix is in ch-closing-clarity. The final document's open problem 2 does not restate the count, so the final document is unaffected.

### ch-opening-isolation

Item 3 now cites def-isolated-client and attaches "free of $d$" to the number of runs. Both are correct (proven, by comparison with (b) and (c)). The number of runs that reaches accuracy $\epsilon_{\mathrm{acc}}$ is $\lceil\ln(1/\alpha)/\epsilon_{\mathrm{acc}}\rceil$ when no run exceeds, and a run of an arbitrary strategy includes calls whose number the strategy fixes.

### ch-final-readability

All four items read as proposed. In item 2 the clause "whatever its number of Train calls" matches round-02/builder.md, line 151, where (d)(ii) holds for every $N$, and the quantifier order there is the certifier first, then $\eta$, then the function. I accept the builder's remark on $\mathfrak z$ against $z_i$. The record $z_i$ appears only in `theory/CURRENT.md` and the round files, and it is a data point, not a Gaussian vector.

## Cost sentences

I checked all 25 changed entries against the statement or the round file that each names. The column "Checked against" names the source I read.

| Entry | Sentence | Checked against | Result |
| --- | --- | --- | --- |
| 3 | Item 3, runs free of $d$ | dataflow (c) | faithful |
| 6 | Item 5, random-oracle query, query count | replay (c) | faithful. $2/(1-e^{-1})=3.164\le3.2$ (computed), with $q_{\mathsf{RO}}+1\le2q_{\mathsf{RO}}$ |
| 12 | Remark of def-isolated-client, calls per round | ch-strategy-calls | faithful |
| 13 | Same remark, passive case | def-learning-oracle-model, passive | conclusion true given the passive stop, reason misstated (ch-passive-stop) |
| 15 | lem-needle-lower-bound, Train calls | its proof, the hit count | faithful |
| 28 | Dataflow (c), cost per run | round-02 line 145, round-03 line 173 | faithful, "at most" needed |
| 29 | Reading of (e)(ii), count | (e)(ii) | faithful, factor $\sqrt2$ confirmed |
| 30 | Reading of (e)(ii), two calls per run | (e)(ii) setting | faithful |
| 31 | Dataflow (d), stated | round-02 (d)(ii), round-03 (d) | faithful, quantifier order kept |
| 35 | Dataflow, without the oracle | (c) | faithful |
| 40 | Transfer (b), the protocol's strategy adds none | setting of the transfer | faithful. It never stops, so a run has exactly $2R$ calls for client $j$ |
| 43 | Transfer (e), target | re-derivation above | faithful |
| 49 | Criterion-4 paragraph of the transfer | (e) and the Reading | faithful |
| 50 | Same paragraph, the comparison | (e) | faithful, subject of "its" unclear (ch-closing-clarity) |
| 52 | Proof of transfer (b), other nodes | count in (b) | faithful |
| 53 | Proof of the corollary, no other node trains | instance $G^{\mathrm{agg}}_R$ | faithful. Its nodes are the $v_t$, the $r_t$, the server's general node and the input nodes of $j'$ |
| 58 | Replay (e), stated | round-02 (e) | faithful, "any number of queries to $R$ and of Train calls at other inputs" |
| 78 | `theory/CURRENT.md` remark, cost per run | ch-strategy-calls | faithful |
| 79 | `theory/CURRENT.md` remark, passive case | passive definition | faithful given the passive stop |
| 82 | Register, dataflow | (c) and its proof | faithful |
| 84 | Register, active-choice | round-03 (b)(i), (c), corollary | faithful. Upper $2\lvert\mathcal C_\cup\rvert\lceil R\ln(n_{\mathcal C}/\alpha)/\epsilon_{\mathrm{acc}}\rceil$, lower $(1-\alpha-\alpha')\lvert\mathcal C_\cup\rvert$ |
| 85 | Register, record-level | round-03 (c)(i) | faithful, $\ln(n'/\alpha)/N$ against $N/n'$ |
| 88 | Register, transfer | (e) | faithful |
| 91 | `theory/CURRENT.md`, open problem 2, count | (e)(ii) | count faithful, soundness dropped (ch-closing-clarity) |
| 92 | `theory/CURRENT.md`, open problem 2, (e)(iii) | (e)(iii) | faithful. The final document calls the same count "runs" (ch-closing-clarity) |

Among the 73 entries marked complete I sampled five. Entry 33, (e)(iii), counts drawn-seed runs at one node, each one Train call. Entry 44, the corollary, has two certificates at level $\alpha/2$ with $N'$ runs of $2R$ calls each, so $4RN'$. Entry 48 counts $2R\lceil\ln(1/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)\rceil$ calls, which is (b) at level $\alpha$. Entry 64 matches round-03/builder.md (a), "$N(R(1+m)+n_G)$ Train calls", under the renaming of `theory/CURRENT.md`. Entry 9 fixes which calls the budget charges. All five are complete (proven, by comparison).

The audit was worth its cost. It found one false clause, entry 28, and one constant off by $\sqrt2$ inside an "about", entry 29. Its 25 changes introduced one new incomplete sentence, entry 91.

## Definitions

Fifth reading. Only the remark of [def-isolated-client] changed this round, in both files. A remark is not part of a definition.

### [def-learning-oracle]

Unchanged. Well posed. ACCEPT.

### [def-learning-oracle-model]

Unchanged. Well posed. ACCEPT.

### [def-degenerate-oracles]

Unchanged. Well posed. ACCEPT.

### [def-certifier]

Unchanged. Well posed. The remark on larger targets carries step 5 above (proven). ACCEPT.

### [def-model-bank]

Unchanged. Well posed. ACCEPT.

### [def-isolated-client]

The four conditions, the coupled execution, the exceedance and the coupled tail are unchanged and well posed. ACCEPT.

The remark in `theory/CURRENT.md` is correct as written, given one convention. The definition says that the procedure may stop "on a value that the coalition sets". The definition of a passive strategy covers "the choices that enter procedure nodes". Neither sentence says that the stop is such a choice. The builder's response to ch-strategy-calls reads it so ("the stop included"). On the other reading a passive coalition may stop early, and then $\epsilon_b$ differs between passive adversaries (proven, sketch). Take $R=2$ and a learning function whose only exceedance is in round 2. The passive adversary that stops after round 1 then has $\epsilon_b(\Delta)=0$, while the protocol's strategy has a positive value. No theorem becomes false on that reading. Every certificate bounds the exceedance of the strategy that never stops, and a stop only lowers $\epsilon_b$ by the proof of (c). The equality claim of the remark, and the phrase "the same for every passive adversary" in the setting of thm-record-level-certificate in round-03/builder.md, need the convention. ch-passive-stop asks for one sentence.

Simplicity. The six definitions remain the smallest that carry the presented proofs.

## Re-derived proofs

I chose the two results whose proofs carry the most steps and changed most often since round 05. They are [thm-dataflow-composition], whose proof of (b) underlies every other dataflow statement, and [thm-bounded-deviation-transfer], whose parts were restated in rounds 06, 07 and 08. For each I re-derived the full proof as written in the final document, from the definitions and the standing facts, before I compared it with the text.

### thm-dataflow-composition

Game. The distinguishing game of def-learning-oracle-model on the procedure $G$, under the bottom or the top oracle, with laws $P_0,P_1$ of the view. Reduction. Data processing from the law of $(\omega,y_{\le R},\bar\rho_{\le R})$ to the view. Hybrid. $\mathcal L_{\mathrm{hyb}}$, with releases $O_t+F^1_t-\mathrm{clip}_\Delta(F^1_t-F^0_t)+Z_t$.

Step 1 holds (proven). I checked each source of the adversary's state when it sets $c_t$. Its own calls are served from $\omega$. Under the top oracle a call with the seed name of $v_s$, $s<t$, returns $\mathsf L(x;\rho_s,\xi')$ with $\xi'$ from $\omega$, a function of $\bar\rho_{<t}$ and $\omega$. Answers of query channels use evaluation randomness in $\omega$. Other honest learning nodes, their seeds included, are carried by $\omega$. The seed of $v_t$ is revealed when $v_t$ runs, after $c_t$ is set, so $c_t$ depends on $\bar\rho_{<t}$ and $O_t$ on $\bar\rho_{\le t}$. Conditions 1, 2 and 4 exclude every path from $D_j$ or from $W_{t-1}$ to $c_t$ that avoids the releases.

Step 3 holds (proven). On one space the hybrid and $\mathsf{Ex}_0$ share $\omega$, the $\zeta_t$ and the $Z_t$. The twin of $\mathsf{Ex}_0$ uses $\xi^1_t$, which the $H_0$ run never reads, so the space carries $\mathsf{Ex}_0$. Before the first exceedance $t^\star$ the clip is the identity, so choices, chains, twins, releases and stops agree. At $t^\star$ the choice and both chains agree, so $\mathsf{Ex}_0$ has its first exceedance at $t^\star$ too, and the converse holds by the same induction. Hence the two agree off $\{D^\star_0>\Delta\}$, and the coupling inequality gives $\mathrm{TV}(\mathcal L_0,\mathcal L_{\mathrm{hyb}})\le\epsilon_0(\Delta)$. The sum form needs the event that round $t$ runs, $c_t$, $W_{t-1}$ and $W'_{t-1}$ to be $\mathcal G_t$-measurable. They are, since stops are functions of $(\omega,y_{<t},\bar\rho_{<t})$. In $\mathsf{Ex}_0$ the first state is the $D^0_j$ chain, which matches the order of arguments of $\beta_t$.

Step 4 holds (proven). This is the step where the argument is most delicate, since $\mathfrak f_t$ and $\mathbf n_t$ depend on the past and the kernel must be built round by round. With $\mathfrak z_t\sim\mathcal N(\Delta/\sigma,1)$, (F6)(ii) gives $\tilde g_t\sim\mathcal N(0,1)$, and $\sigma\tilde g_t\mathbf n_t+\sigma(I_d-\mathbf n_t\mathbf n_t^\top)Z''_t\sim\mathcal N(0,\sigma^2I_d)$ given the past, since $\tilde g_t$ and $Z''_t$ are independent and $\mathbf n_t$ is fixed by the past. So the kernel runs the generative process of $H_1$, with chain $\tilde W^1$ on $\xi^1_t$, and its output has law $\mathcal L_1$. With $\mathfrak z_t\sim\mathcal N(0,1)$ the mean moves by $-\Delta\mathfrak f_t\mathbf n_t=-\mathrm{clip}_\Delta(F^1_t-F^0_t)$, which is the hybrid. The edge case $F^1_t=F^0_t$ gives $\mathfrak f_t=0$ and the same law in both. After a stop the kernel ignores the remaining coordinates, which keeps it a kernel. (F2) in both orders and (F6)(i) in $\mathbb R^R$ give $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$.

Step 5 holds (proven). Both splits of (F3) follow from adding and subtracting $\mathcal L'(E)$. The exchanged hybrid $O_t+F^0_t+\mathrm{clip}_\Delta(F^1_t-F^0_t)+Z_t$ agrees with the $H_1$ run until the first exceedance of $\mathsf{Ex}_1$, and the kernel built from $F^0_t-F^1_t$ maps the two Gaussians to it and to $\mathcal L_0$. The four bounds combine to the two minima of the statement.

The proof of (c) and the proof of (e)(ii) hold (proven). In (e)(ii), lem-sphere-code (a) yields an integer number of points at least $2^{0.18d}$, hence at least $\lceil2^{0.18d}\rceil\ge2J_{\mathrm{cd}}$. The index and the sign are independent and uniform under Lebesgue measure. Given $2N$ distinct indices the signs are independent and uniform under both laws, and the collision probability is at most $\binom{2N}{2}/J_{\mathrm{cd}}$. The decoding test misses with probability at most $(2J_{\mathrm{cd}}-1)\bar\Phi(B/(2\sigma))$ under each hypothesis, by lem-sphere-code (b) with $\mathfrak s=B$.

Result. The proof holds as written. No gap.

### thm-bounded-deviation-transfer

Game. The distinguishing game on an isolated procedure with a $B_A$-deviating coalition. Reduction. A change of measure from the protocol's strategy to the deviating one on the event $\mathbb A$, then thm-dataflow-composition (b). No hybrid.

Part (a), step 0, holds (proven). Continuing with $\mathbf u_t=\mathbf u^{\mathrm{pr}}_t$ after the stop keeps the strategy $B_A$-deviating, and on the common space it runs every round the given strategy runs, so the exceedance can only grow.

Part (a), step 1, is the weakest point of the proof, and it holds (proven). The claim is that one family of maps gives $c_t$, $W_t$, $W'_t$, $\bar o_t$ and $\mathbf u^{\mathrm{pr}}_t$ as functions of $(\Omega,y_{<t})$ under both strategies. Three hypotheses of the setting carry it, and each is used. The coalition's input nodes of round $t$ have the single child $r_t$, so $\mathbf u_t$ reaches later nodes only through $y_t$. Every other value that the coalition sets is the protocol's function of procedure values. Each node's randomness is a coordinate of $\omega$, so the adversary's own calls shift no node's randomness. Putting all of $\zeta_t$ into $\Omega$ handles the top oracle, where $\mathbf u_t$ may depend on $\rho_t$, revealed before $r_t$ runs. $Z_t$ is randomness of $r_t$ and enters nothing before $\mathbf u_t$ is set.

Part (a), steps 2 to 4, hold (proven). Given $(\Omega,y_{<t})$ the release is $\mathcal N(\mathbf u_t+\bar y_t,\sigma^2I_d)$ under one law and $\mathcal N(\mathbf u^{\mathrm{pr}}_t+\bar y_t,\sigma^2I_d)$ under the other. (F7) bounds each conditional Rényi moment by $\exp(\varpi(\varpi-1)B_A^2/(2\sigma^2))$. The event $\mathbb A$ reads only $y_{<R}$, so $R-1$ factors enter and the exponent is $\varpi(\varpi-1)\mathfrak e$. Minimizing $-\mathfrak l(1-1/\varpi)+(\varpi-1)\mathfrak e$ over $\varpi>1$ gives $-(\sqrt{\mathfrak l}-\sqrt{\mathfrak e})^2$ at $\varpi=\sqrt{\mathfrak l/\mathfrak e}$ when $\mathfrak l>\mathfrak e>0$, the value $0$ when $\mathfrak l\le\mathfrak e$, and $-\mathfrak l$ when $\mathfrak e=0$. That is $\ln\Upsilon_{\mathfrak e}(p)$ in all three cases. As a consistency check, (a) holds on the instance of (c). At 1540 points with $\mathfrak e\in\{0.1,0.5,1,2,5,10,16\}$ and $\iota$ from $\sqrt{2\mathfrak e}+1.01$ in steps of $0.05$, the smallest value of $\ln(\Upsilon_{\mathfrak e}(\bar\Phi(\iota))/\bar\Phi(\iota-\sqrt{2\mathfrak e}))$ is $0.087$ (computed).

Part (b) holds (proven). With no exceedance $\bar\epsilon_b\le\ln(1/\alpha)/N'\le\exp(-(\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)$, so $\sqrt{\ln(1/\bar\epsilon_b)}-\sqrt{\mathfrak e}\ge\sqrt{\ln(1/\epsilon_{\mathrm{acc}})}$ and $\Upsilon_{\mathfrak e}(\bar\epsilon_b)\le\epsilon_{\mathrm{acc}}$.

Part (c) holds (proven). The exceedance of round $R$ is $\mathrm{clip}_B(2\Delta\mathbf e_1)=2\Delta\mathbf e_1$, since $B\ge2\Delta$. The coordinate $\langle m_R-m_1,\mathbf e_1\rangle$ has mean $(R-1)B_A=\sqrt{2\mathfrak e}\,\sigma\sqrt{R-1}$ under the given strategy. Each inequality of the proof checks, with $\ln\sqrt{2\pi}=0.919<1$ (computed) and $2\iota\le\sqrt{8\ln(1/p)}$ from $\ln(1/p)\ge\iota^2/2$.

Part (d) holds (proven). Hoeffding's inequality for $d$ signs gives $2e^{-\mathfrak c^2d/2}$, and $J(J-1)/2$ pairs give a bad pair with probability below $J^2e^{-\mathfrak c^2d/2}\le1$. The cell bound is $\eta/4$ for the own direction plus $(J-1)\bar\Phi((1-\mathfrak c)\sqrt{2\mathfrak e}-\mathfrak q_\eta)$ for the others, where $J_3\ge1$ forces the argument to be positive, so (F6)(iii) applies. The needle strategy $\mathbf u_t=B_A\mathbf q_k$ is $B_A$-deviating since $\mathbf u^{\mathrm{pr}}_t=0$. (F5) with the common coordinate $y_{<R}$ gives $\Pr[m_R\in V^{\mathrm{th}}_k]\,\delta_{\mathcal N}(\varepsilon;B/\sigma)$. In the expansion the step $J_3=\lfloor J'\rfloor$ needs $J'<e^{\mathfrak e}$. It holds, since $\ln J'\le\ln(\eta/2)+(1-\mathfrak c)^2\mathfrak e<\mathfrak e$. The step $\lfloor J'\rfloor\ge J'/2$ needs $J'\ge1$, which is the hypothesis on the second argument.

The corollary holds (proven). The lower bound is (d) read at an accurate certifier, $\alpha'\ge\Pr[\hat t\ge\vartheta]\ge1-\alpha-N/J_3$. The upper bound is $\max\{\hat t_0,\hat t_1\}$ at level $\alpha/2$ each, with $4RN'$ calls and no exceedance at $\mathsf L^\circ$. The asymptotic form needs $\mathfrak e\to\infty$, which the statement names, and the hypotheses of the corollary along the sequence, which the Reading secures by fixing $\sqrt R\Delta/\sigma$. $\delta_{\mathcal N}(1;1)=0.1269$ (computed), as the Reading says.

Part (e) holds, as re-derived under ch-transfer-drawn-seed-target, with the domain gap of ch-upsilon-domain.

Result. The proof holds as written. One gap in the statement of (e) is a domain gap, not a wrong step.

### Further checks

Beyond the two results I rechecked the following steps of other full proofs in the final document, with no finding (proven). They are the proof of lem-needle-lower-bound, the binomial bound and the Hamming packing of lem-sphere-code (a), with $1-\mathrm h_2(1/4)=0.1887$ (computed), the McDiarmid constant of thm-coupling-certificate (a)(ii), which is conservative, the union bound of thm-black-box-certifiability (a), the black-box example under the top oracle, and the lazy sampling of thm-replay-audit-steer (a).

## New challenges

### ch-upsilon-domain

Not blocking. Due before the audit. Target: the setting and part (e) of [thm-bounded-deviation-transfer] in both files. The setting defines $\Upsilon_{\mathfrak e}(p)$ for $p\in(0,1]$ and $p=0$. Part (e) writes $\Upsilon_{\mathfrak e}(\ln(1/\alpha)/N')$, whose argument exceeds one when $N'<\ln(1/\alpha)$, for instance at $N'=1$ and $\alpha<e^{-1}$. There the formula takes the square root of a negative number. The statement is not false on any reading, since the only monotone extension is $\Upsilon_{\mathfrak e}=1$ above one and $\hat t_b\le1$. It is undefined in that range. Smallest fix. In the setting, after "$\Upsilon_{\mathfrak e}(0)=0$", add "and $\Upsilon_{\mathfrak e}(p)=1$ for $p>1$". The extension is consistent, since $\Upsilon_{\mathfrak e}(1)=1$ for every $\mathfrak e\ge0$ (proven, and computed at $\mathfrak e=2$), and it keeps $\Upsilon_{\mathfrak e}$ nondecreasing.

### ch-passive-stop

Not blocking. Target: the remark after [def-isolated-client] in the final document, and the same remark in `theory/CURRENT.md`. The final sentence "A passive strategy's own calls do not enter $\mathsf{Ex}_b$, so every passive adversary has the same $\epsilon_b$" gives a wrong reason. The strategy's own calls do enter $\mathsf{Ex}_b$, served from $\omega$. What holds is that they do not change $D^\star_b$. The equality of $\epsilon_b$ follows from the prescribed choices and needs the prescribed stop, which no sentence states (counterexample under Definitions). Smallest fix, in the final document. "A passive strategy also takes the protocol's stop. Its choices fix the law of $D^\star_b$, so every passive adversary has the same $\epsilon_b$, and the experimenter need not make the strategy's own calls." In `theory/CURRENT.md` add the first of these sentences before "For a passive strategy the law of $D^\star_b$ ...".

### ch-closing-clarity

Not blocking. Three items, each with its smallest fix.

1. Open problem 2 of `theory/CURRENT.md` drops soundness (entry 91). Fix. "Over $\mathfrak L_B$, a drawn-seed certifier of $\theta$ sound at level $\alpha$ that outputs below ...".
2. One count has two names. Stated part (e)(iii) of [thm-dataflow-composition] in the final document says "drawn-seed runs", and open problem 2 of `theory/CURRENT.md` says "drawn-seed Train calls" for the same count (entries 33 and 92). Fix. "drawn-seed Train calls" in (e)(iii).
3. The criterion-4 paragraph of [thm-bounded-deviation-transfer] reads "Then (b) fails under drawn seeds when its number $N$ of calls satisfies $N(2N-1)<\eta J_{\mathrm{cd}}$." The pronoun "its" points to (b), whose number of calls is $2RN'$, while $N$ belongs to the drawn-seed certifier. Fix. "Then no drawn-seed certifier of $\theta^{\mathrm{dev}}$ with $N(2N-1)<\eta J_{\mathrm{cd}}$ matches the accuracy of (b)."

## Plan for rounds 09 and 10

1. Round 09, builder. Close the three challenges above in one pass, then freeze every statement, hypothesis and label of the final document. No new result, part or remark enters after round 09. Every later change is a clause that a challenge names.
2. Round 09, challenger. Check every stated-only part of the final document against the round file that proves it, quantifier by quantifier. These are (a), (d), (e)(i) and (e)(iii) of the dataflow theorem, (b) to (d) of the black-box theorem, (c) to (e) of the replay theorem, lem-atomless-two-point, and the paragraphs of "Further accepted results". The errors of rounds 07 and 08 (entries 28 and 31, and the fourteen summaries of round 07) all sat in sentences that summarize a round file. The full proofs now stand re-derived.
3. Round 10. Readability only, then the audit. Cut the two criterion-4 paragraphs of the dataflow and transfer theorems to their claims, with numbers moved to the statements they come from. The challenger then reads the final document once in full against the register for the audit.

## Verdicts

Six definitions and fifteen results with slug tags in the final document, judged as they stand there. No challenge is blocking. [thm-dataflow-composition] returns to ACCEPT NONTRIVIAL with the cost clause in place.

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
BLOCKING 0
```
