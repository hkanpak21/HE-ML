# Round 08, builder

Verdict of this turn. The blocking challenge ch-strategy-calls is closed. Part (c) of [thm-dataflow-composition] now reads "Each run costs at most $2R$ Train calls for client $j$, plus the calls of the other nodes and the strategy's own Train calls." This is the challenger's clause with "at most" added, because the fixed strategy may stop. The clause restores what round-02/builder.md, line 145, and round-03/builder.md, line 173, already stated and the final document had dropped. The three non-blocking challenges are closed as proposed, with two departures argued below. Part (e) of [thm-bounded-deviation-transfer] is now stated for drawn-seed certifiers of $\theta^{\mathrm{dev}}$. The search for the same omission covered 98 cost sentences, 71 in the final document and 27 in `theory/CURRENT.md`. It found no other false count. It changed 25 of them, 17 in the final document and 8 in `theory/CURRENT.md`. Two changes correct more than a missing source of calls. The Reading of thm-dataflow-composition (e)(ii) compared drawn-seed Train calls with coupled runs of two calls each. Its count was also larger than the proven one by the factor $\sqrt2$, inside an "about". No theorem is added. The final document has 18 pages. The build prints `BUILD OK n=3`. `node scripts/verify.mjs final` prints `thm-dataflow-composition stands at REVISE in round-07/challenger.md`, as expected before the challenger re-judges it, and no other failure.

Notation follows `theory/CURRENT.md` after this round. Every claim carries one of the labels proven, heuristic or open. Line numbers of round files refer to the files as they stand.

## Responses to challenges

### ch-strategy-calls

Accepted. The counterexample is correct (proven). The coalition's strategy makes one Train call before round 2 and sets $c_2$ from the answer. Step 1 of the proof of (b) writes $c_2=\chi_2(\omega,y_{<2},\bar\rho_{<2})$, and that call is served from $\omega$. An experimenter that samples $\mathsf{Ex}_0$ must compute $c_2$ with the law it has in the real execution. It therefore makes that call or one with the same law, so a run needs at least $2R+1$ Train calls when the other nodes make none.

Part (c) of [thm-dataflow-composition] in the final document now reads as follows.

"Each run costs at most $2R$ Train calls for client $j$, plus the calls of the other nodes and the strategy's own Train calls."

One word goes beyond the challenger's text. The strategy of (c) is fixed, and a strategy may stop after any release, so a run of $\mathsf{Ex}_0$ can end before round $R$. Then client $j$ makes fewer than $2R$ calls, and "at most" states the count exactly.

The clause has a history. The statement of (c) in round-02/builder.md, line 145, and in round-03/builder.md, line 173, ends "plus the calls of the other honest nodes and of the strategy". The proof in round-02/builder.md, line 225, counts only client $j$'s calls, which is the sentence the challenger quoted. The final document, first drafted in round 05, stated the proof's count without the statement's clause. The proof of (c) needs no change (proven). Coverage uses only that the $n$ indicators of $D^\star_0>\Delta$ are independent with parameter $\epsilon_0(\Delta)$, which holds whatever each run costs.

The remark after [def-isolated-client] had the same gap, in both files. In the final document it now reads as follows.

"Remark. An experimenter that holds every input and runs the strategy samples $\mathsf{Ex}_b$. Per round it makes two Train calls for client $j$, the second with the first's seed name, plus those of the other nodes and of the strategy. A passive strategy's own calls do not enter $\mathsf{Ex}_b$, so every passive adversary has the same $\epsilon_b$."

The last sentence states when the strategy's calls can be skipped (proven). A passive strategy sets every choice that enters a procedure node, the stop included, by the function of procedure values that the protocol prescribes. So $c_t$, $W_t$, $W'_t$ and the stops are functions of the procedure's randomness and of client $j$'s triples alone. The law of $D^\star_b$ therefore does not depend on the strategy's own calls. The same holds for the protocol's strategy of [thm-bounded-deviation-transfer]. Every value it sets other than its additive inputs is the protocol's, and $\mathbf u^{\mathrm{pr}}_t$ is a function of procedure values. That is why part (b) of the transfer and the corollary were complete as written.

`theory/CURRENT.md` carries the clause in two places. The remark of [def-isolated-client] now says "It also makes the calls of the other nodes and the strategy's own calls, so a run costs at most $2R$ Train calls for client $j$ plus those." The register line of [thm-dataflow-composition] now says "certifiable for any named strategy and its stopping variants with at most $2R$ Train calls per run for client $j$ plus the calls of the other nodes and of the strategy". Its status records the REVISE of round 07.

### ch-transfer-drawn-seed-target

Accepted. Part (e) of [thm-bounded-deviation-transfer] now reads as follows.

"(e) Drawn seeds. In $G^{\mathrm{agg}}_R$ let $B<\infty$ and $1\le J_{\mathrm{cd}}\le\lceil2^{0.18d}\rceil/2$. Let a drawn-seed certifier of $\theta^{\mathrm{dev}}$ with $N$ Train calls be sound at level $\alpha$ over every learning function. Some learning function with all coupled pairs equal and $\theta^{\mathrm{agg}}_R=0$ gives $\Pr[\hat t\ge1-(1+\gamma)(2J_{\mathrm{cd}}-1)\bar\Phi(B/(2\sigma))]\ge1-\alpha-N(2N-1)/J_{\mathrm{cd}}$. There the certificate (b) outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\Upsilon_{\mathfrak e}(\ln(1/\alpha)/N')$ with certainty. By the remark of def-certifier the bound binds certifiers of $\theta^{\mathrm{agg}}_R$."

Claim. The statement holds (proven).

Proof. Take the reference function $\mathsf L^\circ$ and the needle functions $\mathsf L_\varsigma$ of the proof of (e). Step 2 of the proof of thm-dataflow-composition (e)(ii) does not use the target. It bounds by $N(2N-1)/J_{\mathrm{cd}}$ the total variation between the laws of the transcript under $\mathsf L^\circ$ and under the mixture over $\varsigma$. Consider the adversary that plays the protocol's strategy and reads $y_1$. Its strategy is $B_A$-deviating for every $B_A\ge0$. Its additive input of round 1 is $\mathbf u_1=\mathbf u^{\mathrm{pr}}_1=0$, since the prescribed input of $j'$ is zero. So $y_1=\mathrm{clip}_B(W_1-m_1)+Z_1$, and the clip is the identity, since $W_1-m_1$ is a code point of norm $B$. The projection of the view on $y_1$ is one measurable map under both hypotheses. So (F2) and step 3 of the proof of (e)(ii) give $\theta^{\mathrm{dev}}(\mathsf L_\varsigma)\ge\mathrm H_\gamma$ of the two laws of $y_1$, which is at least $\vartheta$. Soundness at every $\mathsf L_\varsigma$ and step 2 give the bound at $\mathsf L^\circ$. At $\mathsf L^\circ$, $\theta^{\mathrm{dev}}\le\theta^{\mathrm{agg}}_R=0$, by the argument already in the proof. A certifier sound for $\theta^{\mathrm{agg}}_R\ge\theta^{\mathrm{dev}}$ is sound for $\theta^{\mathrm{dev}}$ by the remark of def-certifier, so the bound binds it. $\square$

The proof of (e) in the final document says "The adversary that plays the protocol's strategy and reads $y_1$ sees the round-1 model minus $m_1$ plus noise, since $\mathbf u_1=0$ and the clip acts as the identity on norm $B$. So (F2) carries the divergence of (e)(ii) to $\theta^{\mathrm{dev}}$." The transfer to $\theta^{\mathrm{agg}}_R$ is stated in (e) with its reason, and the proof does not repeat it.

The criterion-4 paragraph now cites (e) with its proven form. "Let $d\ge6$ and $J_{\mathrm{cd}}$ be as in the Reading of thm-dataflow-composition (e)(ii). By (e), a drawn-seed certifier of $\theta^{\mathrm{dev}}$ with $N$ calls, where $N(2N-1)<\eta J_{\mathrm{cd}}$, outputs at least $1-(1+\gamma)e^{-B^2/(16\sigma^2)}$ there with probability at least $1-\alpha-\eta$. Let $\alpha+\eta<1$ and $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<1-(1+\gamma)e^{-B^2/(16\sigma^2)}$. Then (b) fails under drawn seeds when its number $N$ of calls satisfies $N(2N-1)<\eta J_{\mathrm{cd}}$, for instance at $B_A=0$, large $d$ and $B/\sigma$, $\epsilon_{\mathrm{acc}}<1$ and small $\sqrt R\Delta/\sigma$ (proven)."

The threshold follows from (e) through the Reading (proven). With $J_{\mathrm{cd}}\le e^{B^2/(16\sigma^2)}$, (F6)(iii) gives $(2J_{\mathrm{cd}}-1)\bar\Phi(B/(2\sigma))\le J_{\mathrm{cd}}e^{-B^2/(8\sigma^2)}\le e^{-B^2/(16\sigma^2)}$. With $J_{\mathrm{cd}}\le2^{0.18d-1}$, $2J_{\mathrm{cd}}\le\lceil2^{0.18d}\rceil$, and $d\ge6$ gives $J_{\mathrm{cd}}\ge1$. The certificate $\hat t_0$ of (b) certifies $\theta^{\mathrm{dev}}$, so both sides of the comparison now have the same target. The witness of round-07/builder.md stands unchanged. The paragraph keeps no "about" with the label proven, which also closes item 4 of ch-final-readability. The approximate count $\sqrt{\eta J_{\mathrm{cd}}/2}$ is cut from this paragraph for space. The Reading of (e)(ii) states it.

The register line of `theory/CURRENT.md` now names the target, "Drawn-seed certifiers of $\theta^{\mathrm{dev}}$, hence of $\theta^{\mathrm{agg}}_R$, fail where the coupled cost is below theirs". The corollary is unchanged. It concerns $\theta^{\mathrm{agg}}_R$ and certifies it with $\max\{\hat t_0,\hat t_1\}$.

### ch-opening-isolation

Accepted with the challenger's clause. Item 3 now begins "If client data reach a coalition only via $R$ Gaussian releases, as def-isolated-client makes precise, leakage is at most a Gaussian term plus the exceedance probability." Its last sentence now reads "Coupled runs of one strategy certify it, with a number of runs free of $d$ (proven)." The reason is under "Cost sentences checked", entry 3.

### ch-final-readability

Accepted, all four items, with one addition in item 2 and one remark on item 3.

1. The replay paragraph reads "By (d), a drawn-seed auditor complete up to $\lambda'$ for every rotation of the circle accepts some fixed point with probability at least $1-\lambda'-\lambda$, for every $\lambda>0$."
2. Stated part (d) of the dataflow theorem reads "For every $\eta\in(0,1)$, at some function where that leakage is zero, it outputs at least $1-\eta$ with probability at least $1-\alpha$, whatever its number of Train calls." The last clause is a cost clause. Round-02/builder.md, line 151, states (d)(ii) for every certifier with $N$ Train calls and every $\eta>0$, and round 03 strengthened the probability to $1-\alpha$. So no number of calls suffices, which the summary did not say. For $\eta\ge1$ the claim is trivial, so $\eta\in(0,1)$ loses nothing.
3. The kernel input is $\mathfrak z\in\mathbb R^R$ with coordinates $\mathfrak z_t$, in (F6)(ii) and in step 4 of the proof of (b). The symbol table of `theory/CURRENT.md` lists it, and the section "Names in the round files" maps $g$ and $g_t$ of rounds 02 to 07 to it. One remark. $\mathfrak z$ differs by font from the record $z_i$ of thm-record-level-certificate. That record appears only in `theory/CURRENT.md` and the round files, and the two objects are of different kinds. The clash that round 05 removed was between two Gaussian vectors. The theory already pairs fraktur and roman letters for unrelated objects, such as $\mathfrak f_t$ and $f_t$, $\mathfrak c$ and $c_t$, $\mathfrak r_t$ and $r_t$.
4. Closed under ch-transfer-drawn-seed-target. The Reading of thm-dataflow-composition (e)(ii) now also states the proven form before its "about", as entry 29 below records.

## Cost sentences checked

A cost sentence counts Train calls, Eval calls, queries or runs, or states what a cost is free of. It may sit in a statement, a summary, a pointer or a proof. For each I asked whether the count omits calls made by the adversary's or the coalition's strategy, by other nodes, or by the certifier itself. "Complete" means it omits none, with the reason when it is not plain. Otherwise the entry gives the clause added and the reason. Entries 1 to 71 are in the final document and 72 to 98 in `theory/CURRENT.md`.

| Entry | Where | Sentence, by its first words | Result |
| --- | --- | --- | --- |
| 1 | Opening, paragraph 2 | "Train calls certify those quantities where a result says so" | complete, no count |
| 2 | Item 1 | "Coupled Train calls certify it for every learning function" | complete, no count |
| 3 | Item 3 | "Coupled runs of one strategy certify it free of $d$" | now "certify it, with a number of runs free of $d$". A run of an arbitrary strategy includes the strategy's own calls, whose number the strategy fixes and which need not be free of $d$ |
| 4 | Item 4 | "Coupled runs of the protocol certify this bound ... runs reach a fixed accuracy" | complete. It counts runs of the protocol's coupled execution, and the protocol's strategy adds no call |
| 5 | Item 4 | "it needs $e^{(1-o(1))\mathfrak e}$ Train calls when $\mathfrak e/d\to0$" | complete, a lower bound on every Train call of the certifier |
| 6 | Item 5 | "grinding with at least one oracle query ... the number of queries" | now "random-oracle query", since "oracle" alone names the learning oracle here. "the number of queries" became "the query count" for space |
| 7 | Item 6 | "A certifier sound for every learning function that makes $N$ Train calls" | complete |
| 8 | def-learning-oracle-model | "The oracle then answers at most $Q$ Eval calls of $A$ on that name" | complete |
| 9 | def-learning-oracle-model | "The budget $(q_T,q_E)$ bounds" and "Calls that the procedure requires of an owner in $A$ are not charged" | complete. These sentences fix which calls count |
| 10 | def-certifier | "A certifier is an experimenter that makes at most $N$ Train calls" | complete. $N$ counts every call of the certifier, also those that simulate a strategy or other nodes |
| 11 | def-degenerate-oracles, item 1 | "with no bound on $q_T$" | complete |
| 12 | def-isolated-client, remark | "samples $\mathsf{Ex}_b$ with two Train calls per round" | adds "for client $j$" and "plus those of the other nodes and of the strategy" (ch-strategy-calls) |
| 13 | def-isolated-client, remark | "Every passive adversary has the same $\epsilon_b$" | now "A passive strategy's own calls do not enter $\mathsf{Ex}_b$, so every passive adversary has the same $\epsilon_b$", which says when the strategy's calls can be skipped |
| 14 | lem-needle-lower-bound, statement | "Every certifier of $\theta$ with at most $N$ Train calls, in either discipline" | complete |
| 15 | lem-needle-lower-bound, reading | "With $N$ runs it rules out at most $N$ of the $J$ places" | "runs" became "Train calls". In the dataflow sections a run of $\mathsf{Ex}_b$ costs several calls, and the bound counts calls |
| 16 | lem-needle-lower-bound, proof | "A Train call names one training input ... so $\sum_k\mathbf 1[\mathrm{Hit}_k]\le N$" | complete, every Train call of the certifier is counted |
| 17 | thm-coupling-certificate, setting | "An experimenter samples it with $\mathsf{Train}(x_0,\bot)$ ... and $\mathsf{Train}(x_1,s)$" | complete |
| 18 | thm-coupling-certificate (a)(i) | "make $n$ drawn-seed calls per input" | complete |
| 19 | thm-coupling-certificate (a)(ii) | "the empirical law $\hat p_b$ of $n$ drawn-seed views at $x_b$" | complete |
| 20 | thm-coupling-certificate (b) | "from $n$ independent draws of $\Gamma$, at $2n$ Train calls" | complete |
| 21 | thm-coupling-certificate, without the oracle | "no number of drawn-seed runs certifies the total variation" | complete, no count |
| 22 | thm-coupling-certificate, proof of (a)(iii) | "The law of the drawn-seed draws moves by at most $N(2N-1)$ over the cell count" | complete |
| 23 | thm-black-box-certifiability (o) | "every adversary with $q_E$ Eval calls on the served name ... whatever its Train calls" | complete |
| 24 | thm-black-box-certifiability (a) | "An experimenter draws $n$ models at each input with drawn seeds, opens them" | complete. The trees run on opened models, and Eval on a name with label open is free |
| 25 | thm-black-box-certifiability (b) to (d) | "One bottom-oracle adversary with $2n$ shadow models" | complete |
| 26 | thm-black-box-certifiability, without the oracle | "at a cost fixed by $C$, $|U|$, the number of queries, $\alpha$ and the accuracy" | complete |
| 27 | thm-black-box-certifiability, proof of (o) | "Represent the randomness of the adversary's own calls in advance" | complete, the adversary's own calls enter $\omega$ |
| 28 | thm-dataflow-composition (c) | "Each run costs $2R$ Train calls for client $j$ plus the calls of the other nodes" | false, blocking. Now "at most $2R$ ..., plus the calls of the other nodes and the strategy's own Train calls" (ch-strategy-calls) |
| 29 | thm-dataflow-composition, Reading of (e)(ii) | "needs about $\sqrt{\eta/2}\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$ drawn-seed runs" | now "needs $N(2N-1)>\eta J_{\mathrm{cd}}$, so about $\sqrt{\eta/2}\min\{2^{0.09d-1/2},e^{B^2/(32\sigma^2)}\}$ drawn-seed Train calls". The unit is a Train call. With $J_{\mathrm{cd}}\le2^{0.18d-1}$, $\sqrt{\eta J_{\mathrm{cd}}/2}\le\sqrt{\eta/2}\,2^{0.09d-1/2}$, so the old first argument was larger by $\sqrt2$ (proven) |
| 30 | thm-dataflow-composition, Reading of (e)(ii) | "The certificate (c) needs $\lceil\ln(1/\alpha)/\epsilon_{\mathrm{acc}}\rceil$ coupled runs there" | adds "Each run needs only client $j$'s two Train calls, since the choice is fixed". The comparison mixed calls and runs. With $R=1$ and a fixed choice, $D^\star_0=\|W'_1-W_1\|$, so two calls give the indicator its law (proven) |
| 31 | thm-dataflow-composition (d), stated | "take a certifier sound for every learning function against all active strategies" | adds "For every $\eta\in(0,1)$" and "whatever its number of Train calls", round-02/builder.md, line 151 |
| 32 | thm-dataflow-composition (e)(i), stated | "a drawn-seed certifier sound for every learning function does the same" | complete. It inherits the quantifiers of (d), and round-02/builder.md, line 155, holds for every $N$ |
| 33 | thm-dataflow-composition (e)(iii), stated | "$O(e^{B^2/\sigma^2}\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha))$ drawn-seed runs reach accuracy" | complete. A drawn-seed run at one node is one Train call, and the constant absorbs the two inputs |
| 34 | thm-dataflow-composition, without the oracle | "drawn-seed runs do not replace the oracle at a cost free of $d$ and $B$" | complete |
| 35 | thm-dataflow-composition, without the oracle | "Part (c) certifies it for a fixed strategy at $2R$ Train calls per run for client $j$, free of $d$" | now "with a number of runs free of $d$, of $B$ and of the architecture". The per-run count is stated in (c), and the strategy's own calls need not be free of $d$ |
| 36 | thm-dataflow-composition, proof of (b), step 1 | "an independent sequence of triples ... for the calls it makes beyond those the procedure requires" | complete. This is where the strategy's calls enter $\omega$ |
| 37 | thm-dataflow-composition, proof of (c) | "By fidelity the $n$ runs are independent" | complete. Coverage does not depend on the per-run cost |
| 38 | thm-dataflow-composition, proof of (e)(ii), step 2 | "the transcript is a fixed map of $N$ independent draws at $x_0$, $N$ at $x_1$ ... and $\omega'$" | complete, every other call is served by $\omega'$ |
| 39 | thm-bounded-deviation-transfer, setting | "Its queries and other oracle calls are unrestricted" | complete. This clause admits the strategy's own calls |
| 40 | thm-bounded-deviation-transfer (b) | "Each run costs $2R$ Train calls for client $j$ plus the calls of the other nodes" | complete, adds "and the protocol's strategy adds none". The protocol's strategy sets every choice from procedure values and never stops, under ch-strategy-calls |
| 41 | thm-bounded-deviation-transfer (b) | "If no run exceeds $\Delta$ and $N'\ge\ldots$" | complete, counts runs |
| 42 | thm-bounded-deviation-transfer (d) | "every certifier of $\theta^{\mathrm{agg}}_R$ with $N$ Train calls, in either discipline" | complete |
| 43 | thm-bounded-deviation-transfer (e) | "a drawn-seed certifier of $\theta^{\mathrm{agg}}_R$ with $N$ Train calls" | count complete, target now $\theta^{\mathrm{dev}}$ (ch-transfer-drawn-seed-target) |
| 44 | thm-bounded-deviation-transfer, corollary | "Let $N^\star$ be the least number of Train calls" and "$N^\star\le4R\lceil\ln(2/\alpha)\ldots\rceil$" | complete. Two certificates at level $\alpha/2$ run $N'$ times each at $2R$ calls, since in $G^{\mathrm{agg}}_R$ no other node trains and the protocol's strategy adds none |
| 45 | thm-bounded-deviation-transfer, Reading | "Then $N^\star=e^{(1+o(1))(R-1)/2}$" | complete |
| 46 | thm-bounded-deviation-transfer, without the oracle | "Part (b) certifies it at a cost free of $d$, of $B$, of the state and of the architecture" | complete. The protocol's strategy adds no call, and the other nodes' calls are fixed by the procedure |
| 47 | thm-bounded-deviation-transfer, without the oracle | "the logarithm of the cost of (b) is optimal to first order" | complete |
| 48 | thm-bounded-deviation-transfer, degenerate oracles | "the certificate (b) outputs at most ... with $2R\lceil\ldots\rceil$ Train calls" | complete, in $G^{\mathrm{agg}}_R$ under the protocol's strategy |
| 49 | thm-bounded-deviation-transfer, degenerate oracles | "A drawn-seed certifier needs about ... calls there" | rewritten with the proven form and the target $\theta^{\mathrm{dev}}$ (ch-transfer-drawn-seed-target) |
| 50 | thm-bounded-deviation-transfer, degenerate oracles | "Then (b) fails under drawn seeds when the first number is below the second" | now "when its number $N$ of calls satisfies $N(2N-1)<\eta J_{\mathrm{cd}}$", the proven comparison |
| 51 | thm-bounded-deviation-transfer, proof of (a), step 1 | "The randomness of each node is one coordinate of $\omega$, whatever calls the adversary makes on its own" | complete |
| 52 | thm-bounded-deviation-transfer, proof of (b) | "The experimenter holds every input, plays the protocol's strategy, and in round $t$ calls" | adds "runs the other nodes", so the proof makes every call that the count names |
| 53 | thm-bounded-deviation-transfer, proof of the corollary | "In $G^{\mathrm{agg}}_R$ each run costs $2R$ Train calls" | adds "no other node trains, so" |
| 54 | thm-replay-audit-steer, setting, step 2 | "makes $n_{\mathrm{rep}}$ calls $\mathsf{Train}(x,\rho)$" | complete |
| 55 | thm-replay-audit-steer, setting | "Drawn-seed calls measure the reach, and coupled calls ... measure the spread" | complete, no count |
| 56 | thm-replay-audit-steer (a) | "Every prover that makes $q_{\mathsf{RO}}$ queries to $\mathsf{RO}$ and any number of Train calls" | complete. The auditor's replays are the factor $n_{\mathrm{rep}}$ |
| 57 | thm-replay-audit-steer (c) | "the grinding prover tries $n_{\mathrm{nc}}$ new nonces. It trains at each seed" | complete, $n_{\mathrm{nc}}$ queries and $n_{\mathrm{nc}}$ Train calls |
| 58 | thm-replay-audit-steer (e) | "$q_T$ Train calls at $x$ win with expected probability at most" | adds "Train calls at other inputs and queries to $\mathsf{RO}$ are unrestricted", as round-02/builder.md, line 296, states. The bound counts calls at $x$ alone |
| 59 | thm-replay-audit-steer, proof of (a) | "Let $\rho_1,\dots,\rho_{q_{\mathsf{RO}}+1}$ be independent" | complete |
| 60 | thm-replay-audit-steer, without the oracle | "Train calls measure them for any learning function" | complete, no count |
| 61 | Further results, thm-perfect-substitution | "Against an adversary that samples $\mathsf L$ once per Train call" | complete |
| 62 | Further results, thm-bank-soundness | "That half bounds from below the Train calls that certify every record" | complete |
| 63 | Further results, thm-active-choice-dichotomy | "it then needs Train calls linear ... Coupled certificates achieve this up to a logarithmic factor" | complete. The certificates of round-03/builder.md (b) use only client $j$'s coupled pairs and run no strategy, since the target is a supremum over admissible strategies |
| 64 | Further results, thm-record-level-certificate | "Its cost is free of the dataset size and $d$" | complete. Round-03/builder.md, line 354, gives $N(R(1+n_{\mathrm{rec}})+n_{\mathrm{oth}})$ Train calls, which counts the other nodes. The coalition is passive, so its strategy adds none |
| 65 | Further results, thm-smoothed-choice-certificate | "certifies ... at a cost exponential in $d$" and the heuristic comparison | complete. The covering samples client $j$'s tails at net points in $G^{\mathrm{agg}}_R$, where no other node trains |
| 66 | Open problems, opening | "at a fixed number of Train calls" | complete |
| 67 | Open problem 1 | "with Train calls fixed by $\alpha$, $\epsilon_{\mathrm{acc}}$, $R$ and $n_h$" | complete, the count includes the $n_h$ clients |
| 68 | Open problem 2 | "with $e^{O(d)}\,\mathrm{poly}(1/\epsilon_{\mathrm{acc}},\ln(1/\alpha))$ calls" | complete |
| 69 | Open problem 3 | "to use order $C^{q_E}\ln|U|/\epsilon_{\mathrm{acc}}^2$ Train calls" | complete |
| 70 | Open problem 4 | "whose Train calls depend on $R$, $B/\sigma$, $\epsilon_{\mathrm{acc}}$ and $\alpha$" | complete |
| 71 | Open problems 5 and 9 | "$N^\star\ge(1-\alpha-\alpha')J^{\mathrm{fb}}$" and "at fixed $N$" | complete |
| 72 | def-learning-oracle-model, adversary | "unit cost per oracle call, ... counts the time $\mathsf t_{\mathsf L}$ of each run of $\mathsf L$" | complete |
| 73 | def-learning-oracle-model, channels | "the oracle answers at most $Q$ Eval calls of $A$ on that name" | complete |
| 74 | def-learning-oracle-model, budget | "$(q_T,q_E)$ bounds the adversary's Train calls" and the next sentence | complete |
| 75 | def-learning-oracle-model, remark | "An upper bound for every adversary is free of $q_T$" | complete |
| 76 | def-certifier | "makes at most $N$ Train calls" and "has $N=2n$" | complete |
| 77 | def-degenerate-oracles, item 1 | "with no bound on $q_T$" | complete |
| 78 | def-isolated-client, remarks | "At each $v_t$ it calls $\mathsf{Train}(\ldots,\bot)$ ... and then $\mathsf{Train}(\ldots,s)$" | adds "It also makes the calls of the other nodes and the strategy's own calls, so a run costs at most $2R$ Train calls for client $j$ plus those" (ch-strategy-calls) |
| 79 | def-isolated-client, remarks | "so $\epsilon_b$ is the same for every passive adversary" | adds "The experimenter then needs none of the strategy's own calls" |
| 80 | Register, thm-black-box-certifiability | "shadow models buy it at a rate in C, U and q" | complete |
| 81 | Register, thm-bank-soundness | "the first half of d for total Train calls in G-rec" | complete |
| 82 | Register, thm-dataflow-composition | "certifiable for any named strategy ... drawn seeds pay a number of runs" | adds the per-run cost with the strategy's calls, and "runs" became "Train calls" |
| 83 | Register, thm-replay-audit-steer | "oblivious provers pay in Train calls" | complete |
| 84 | Register, thm-active-choice-dichotomy | "certification costs Train calls linear in the distinct admissible choices" | adds "each up to a logarithmic factor", the gap between the certificates of (b) and the lower bounds of (c) in round-03/builder.md |
| 85 | Register, thm-record-level-certificate | "All records cost calls linear in their distinct values" | adds "up to a logarithmic factor", from the union bound at level $\alpha/n'$ of (c)(i) in round-03/builder.md |
| 86 | Register, thm-smoothed-choice-certificate | "pays a number of Train calls exponential" | complete |
| 87 | Register, thm-bounded-deviation-transfer | "certified by coupled runs of the protocol's own execution at a cost free of $d$" and "pays $e^{(1+o(1))\mathfrak e}$ Train calls" | complete |
| 88 | Register, thm-bounded-deviation-transfer | "Drawn seeds fail where the coupled cost is below theirs" | names the targets $\theta^{\mathrm{dev}}$ and $\theta^{\mathrm{agg}}_R$ (ch-transfer-drawn-seed-target) |
| 89 | Open problems, opening | "with a number of Train calls fixed by the stated parameters alone" | complete |
| 90 | Open problem 1 | "Train calls fixed by $\alpha$, $\epsilon_{\mathrm{acc}}$, $R$ and $n_h$" and "Known. $\epsilon_0$ satisfies (i) and (iii)" | complete. Under the protocol's strategy a run costs $2R$ calls for client $j$ and $R$ for each other client |
| 91 | Open problem 2 | "needs about $\sqrt{\eta/2}\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$ runs" | now the proven form $N(2N-1)>\eta J_{\mathrm{cd}}$ with $J_{\mathrm{cd}}$ defined, the factor of entry 29, and Train calls as the unit |
| 92 | Open problem 2 | "$O(e^{B^2/\sigma^2}\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha))$ runs give a uniformly accurate drawn-seed certifier" | "runs" became "drawn-seed Train calls" |
| 93 | Open problem 3 | "shadow runs suffice" and "needs at least a constant times ... Train calls" | complete, a shadow run is one Train call of the attack |
| 94 | Open problem 4 | "a number of Train calls fixed by $R$, $B/\sigma$, $\epsilon_{\mathrm{acc}}$ and $\alpha$, and free of $d$" | complete |
| 95 | Open problem 5 | "$N^\star\ge(1-\alpha-\alpha')J^{\mathrm{fb}}$" and "pays less than $e^{\mathfrak e}$" | complete |
| 96 | Open problem 7 | "some prover with $q_{\mathsf{RO}}$ queries" | complete |
| 97 | Open problem 8 | "with Train calls fixed by $\epsilon_{\mathrm{acc}}$ and $\alpha$" | complete |
| 98 | Open problem 9 | "at fixed $N$" | complete |

The table has 98 entries (computed, by counting the rows). Of them, 25 add or change a clause and 73 are complete. One entry was false as written, entry 28. Entries 29 and 91 corrected a constant inside "about" and a unit. The other changes make a count state its source of calls, its unit or its quantifier.

## Changes to the final document

What the theory shows. Item 3 cites def-isolated-client and attaches "free of $d$" to the number of runs. Item 4 merges two sentences with the same content, to keep the page count. Item 5 says "random-oracle query" and "the query count".

Definitions. The remark of [def-isolated-client] counts the calls of the other nodes and of the strategy, and says when the strategy's calls can be skipped.

Standing facts. The kernel input of (F6)(ii) is $\mathfrak z$.

[lem-needle-lower-bound]. "With $N$ Train calls" replaces "With $N$ runs".

[thm-dataflow-composition].

1. Part (c) states the cost with "at most" and the strategy's own Train calls (ch-strategy-calls). "and for every strategy" became "and every strategy".
2. The Reading of (e)(ii) states the proven form, the corrected first argument of the minimum, Train calls as the unit, and the two calls per coupled run.
3. Stated part (d) quantifies $\eta$ and says that no number of Train calls suffices.
4. The "Without the oracle" paragraph attaches "free of $d$, of $B$ and of the architecture" to the number of runs.
5. Step 4 of the proof of (b) uses $\mathfrak z\in\mathbb R^R$ with coordinates $\mathfrak z_t$.

[thm-bounded-deviation-transfer].

1. Part (b) says that the protocol's strategy adds no call.
2. Part (e) is stated for $\theta^{\mathrm{dev}}$, and its last sentence carries the bound to $\theta^{\mathrm{agg}}_R$ (ch-transfer-drawn-seed-target). The proof of (e) names the adversary that plays the protocol's strategy and carries the divergence to $\theta^{\mathrm{dev}}$.
3. The "Without the oracle" paragraph loses its sentence on part (c). That sentence restated (c) with its hypotheses two paragraphs after the statement, and the paragraph concerns what the oracle buys. The cut keeps the page count, and no claim of the document is lost.
4. The "Degenerate oracles" paragraph reads as quoted under ch-transfer-drawn-seed-target.
5. The proof of (b) runs the other nodes. The proof of the corollary says that no other node of $G^{\mathrm{agg}}_R$ trains.

[thm-replay-audit-steer]. Stated part (e) says that Train calls at other inputs and queries to $\mathsf{RO}$ are unrestricted. The "Without the oracle" paragraph reads as item 1 of ch-final-readability, and "by the reach, spread and joint reach" became "by reach, spread and joint reach" for space.

Length and style. The document has 18 pages (pdfinfo), with about one line free on the last page. No statement, hypothesis or label changed in the cuts for space. They are the merge in item 4, "the query count", a shorter phrase in the remark, the cut sentence on (c), and two dropped words. The document has no semicolon, no dash used as punctuation, no bold and no colon in prose (computed). With each formula counted as one word, no sentence of the final document exceeds 30 words (computed). The new clause of stated part (e) of the replay theorem stands as a sentence of its own for that reason.

`theory/CURRENT.md`. The title and the opening name round 08. The remark of [def-isolated-client] carries the clause of ch-strategy-calls and the passive case. The symbol table lists $\mathfrak z$. The register records the verdicts of round 07, REVISE for [thm-dataflow-composition] and ACCEPT in rounds up to 07 for the definitions and the transfer. It restates the lines of [thm-dataflow-composition], [thm-active-choice-dichotomy], [thm-record-level-certificate] and [thm-bounded-deviation-transfer] as in entries 82, 84, 85 and 88. Open problem 2 states the proven form of the drawn-seed count. The section "Names in the round files" maps the kernel input $g$ to $\mathfrak z$.

Checks. `node scripts/build.mjs round-08/builder.md theory/CURRENT.md final/learning-oracle-theory.md` prints `BUILD OK n=3`. `node scripts/verify.mjs final` prints `final failed:` with the single line `thm-dataflow-composition stands at REVISE in round-07/challenger.md`, which the challenger's next verdict decides. `node scripts/verify.mjs structure` reports `round-08/challenger.md is missing or empty` and `README round log has no line for round-08`, which the challenger's turn and the orchestrator's log line close.
