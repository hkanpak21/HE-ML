# Round 07, challenger

Verdict of this turn. Both blocking challenges of round 06 are closed, and so are the five non-blocking ones. The disputed name goes to the builder. The new proof that $\theta^{\mathrm{agg}}_R=0$ at the reference function of part (e) of [thm-bounded-deviation-transfer] is correct (proven). The sharpened factor $e\sqrt{8\ln(1/p)}$ is correct (proven, and computed on a grid). Both added conditions, $\alpha+\eta<1$ and $d\ge6$, are needed and suffice (proven). I checked the fourteen summary sentences that the builder found false, every sentence of the opening, and eleven sentences marked complete. All fourteen corrections are faithful, and no summary in the sample drops a hypothesis of its theorem. One reading of item 3 of the opening is wider than its theorem, which I record as not blocking (ch-opening-isolation). The six definitions are accepted for the fourth consecutive round. The full reading of the final document found one false clause inside a theorem statement. Part (c) of [thm-dataflow-composition] gives the cost of a run without the Train calls of the strategy itself (ch-strategy-calls, blocking, one clause). The criterion-4 paragraph of the transfer compares a certificate of $\theta^{\mathrm{dev}}$ with a lower bound stated for $\theta^{\mathrm{agg}}_R$. The comparison is true by the proof of (e) but not by its statement (ch-transfer-drawn-seed-target, not blocking). My own round-06 witness had the same gap. `node scripts/verify.mjs final` prints `FINAL OK theorems=5 nontrivial=5 items=21`.

Every non-trivial claim carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the argument is written here and the builder must write it out. "Computed" marks a number from a short script run this round. Notation follows `theory/CURRENT.md` after round 07. I opened no outside source.

## Status of the round-06 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-opening-finite-queries | blocking | closed, with two further clauses that I accept | none |
| ch-drawn-seed-accuracy-level | blocking | closed, with $\alpha+\eta<1$, $d\ge6$ and $\theta^{\mathrm{agg}}_R=0$ proven in (e) | the drawn-seed target is unnamed (ch-transfer-drawn-seed-target, not blocking) |
| ch-choice-source | not blocking | closed in both files, and step 1 of the proof of (b) cites condition 1 | none |
| ch-opening-scope | not blocking | closed, all three clauses | none |
| ch-tightness-inline | not blocking | closed, with the sharper constants in the statement | none |
| ch-residual-symbols | not blocking | closed, six items as proposed and one by the builder's alternative | one font clash of the same kind (ch-final-readability, item 3) |
| ch-final-wording | not blocking | closed, items 1 to 3 as written, item 4 moved | none |

### ch-opening-finite-queries

Item 2 now names a finite query set with finitely many outputs, and the common value below one. Both clauses restore hypotheses of [thm-black-box-certifiability] (proven, by comparison with its setting and with part (c), $\mathrm{Adv}^{\mathrm{bb}}(Q)+\lambda<1$).

The builder's counterexample for infinitely many outputs is correct (proven, sketch). Under the reference function the $2N$ cell indices are independent and uniform over $M$ cells. Under the mixture over a uniform half $S$, the draws at $x_0$ are uniform over the cells of $S$ and those at $x_1$ over its complement. Both laws are invariant under permutations of the cells, so given $2N$ distinct cells both are uniform over injective tuples. The total variation is then at most the larger collision probability, which is $\binom{2N}2/M=N(2N-1)/M$ under the reference function and $2\binom N2/(M/2)=2N(N-1)/M$ under the mixture. So the stated bound $N(2N-1)/M$ holds. Without finitely many outputs the theorem's $\mathfrak T_q$ is not defined, so the clause is needed in either reading.

### ch-drawn-seed-accuracy-level

The paragraph "Degenerate oracles" of [thm-bounded-deviation-transfer] now has the accuracy-level condition and the value $\theta^{\mathrm{agg}}_R=0$. The two conditions that the builder added are both needed (proven).

1. $d\ge6$. The second number comes from the Reading of [thm-dataflow-composition] (e)(ii), which takes $J_{\mathrm{cd}}=\min\{\lfloor2^{0.18d-1}\rfloor,\lfloor e^{B^2/(16\sigma^2)}\rfloor\}$. That is at least one only when $2^{0.18d-1}\ge1$, so from $d=6$, since $2^{0.08}=1.057$ (computed). It also satisfies $2J_{\mathrm{cd}}\le\lceil2^{0.18d}\rceil$, the hypothesis of (e).
2. $\alpha+\eta<1$. Part (e) gives $\Pr[\hat t\ge\vartheta]\ge1-\alpha-N(2N-1)/J_{\mathrm{cd}}$. The certificate (b) outputs below the threshold with probability one. A drawn-seed certifier with $N(2N-1)<\eta J_{\mathrm{cd}}$ does so with probability below $\alpha+\eta$. The two differ only when $\alpha+\eta<1$.

The proof of $\theta^{\mathrm{agg}}_R=0$ in part (e) is correct (proven). At the reference function the round-1 model at $x((1,m_1),D^b_j)$ is $m_1+\mathbf p^{\mathrm{sg}(\rho)}_{\mathrm{ix}(\rho)}$ for both $b$, and every other training input returns its starting model. So every release is $\mathbf u_t+\mathrm{clip}_B(W_t-m_t)+Z_t$ with the same law under both hypotheses, for every $B_A$-deviating strategy. Under the top oracle a Train call with the honest seed name returns a model that depends on the dataset only at $x((1,m_1),D^0_j)$ and $x((1,m_1),D^1_j)$, where it gives the same value. The adversary's calls are functions of its view, so by induction over the schedule the view has one law under both hypotheses. The proof in the final document compresses this induction into two sentences, and the step is routine.

The witness for criterion 4 in round-07/builder.md is correct. With $N=2R\lceil4\ln(1/\alpha)\rceil$ and $N<\sqrt{\eta J_{\mathrm{cd}}/2}$, $N(2N-1)<2N^2<\eta J_{\mathrm{cd}}$ (proven). The target of the comparison is the subject of ch-transfer-drawn-seed-target.

### ch-choice-source

Condition 1 of [def-isolated-client] now excludes $v_{t-1}$ and the input node of $D_j$ as sources of $c_t$, in both files. With condition 2 this suffices (proven). Every path from the input node of $D_j$ or from a $v_s$ to $v_t$ runs through $v_{t-1}$ or through some $r_s$ with $s<t$. A parent other than $v_{t-1}$ and the input node is therefore a measurable function of $\omega$, the releases $y_{<t}$ and the revealed seeds, which is what step 1 of the proof of (b) uses. The value of $r_{t-1}$ remains admissible, and $G^{\mathrm{agg}}_R$ uses it through the server.

### ch-opening-scope

Item 1 states the computability of the channel divergence. Item 4 states the accuracy level below a fixed fraction of one clipped release's leakage, the clip, $\alpha+\alpha'<1$, the count $e^{(1+o(1))\mathfrak e}\ln(1/\alpha)$ and the condition that no run exceeds the threshold. Each clause matches part (b) or the corollary (proven, by comparison). The exact count $\ln(1/\alpha)\exp(\mathfrak e+2\sqrt{\mathfrak e\ln(1/\epsilon_{\mathrm{acc}})}+\ln(1/\epsilon_{\mathrm{acc}}))$ is $\ln(1/\alpha)e^{(1+o(1))\mathfrak e}$ as $\mathfrak e\to\infty$ at fixed $\epsilon_{\mathrm{acc}}$ (proven).

### ch-tightness-inline and the sharpened factor

The derivation in the proof of (c) is correct as written (proven). Each step checks.

1. $p=\bar\Phi(\iota)$ and $r=\iota-\sqrt{2\mathfrak e}$, so $1<r\le\iota$ from $\iota>\sqrt{2\mathfrak e}+1$.
2. (F6)(iii) gives $\ln(1/p)\ge\iota^2/2+\ln2\ge\iota^2/2>\mathfrak e$. Hence $\sqrt{\ln(1/p)}-\sqrt{\mathfrak e}\ge(\iota-\sqrt{2\mathfrak e})/\sqrt2=r/\sqrt2>0$ and $\ln(1/\Upsilon_{\mathfrak e}(p))\ge r^2/2$.
3. The lower Mills bound gives $\ln(1/\bar\Phi(r))\le r^2/2+\ln((1+r^2)/r)+\ln\sqrt{2\pi}$, and $r+1/r<r+1\le\iota+1$ for $r>1$, with $\ln\sqrt{2\pi}=0.919<1$ (computed).
4. For the factor form, $\iota+1<2\iota$ for $\iota>1$, and $4\iota^2\le8\ln(1/p)$ by step 2. So $\ln(\iota+1)\le\ln\sqrt{8\ln(1/p)}$ and $\Upsilon'(p)\ge\epsilon_0(\Delta)\ge e^{-1}\Upsilon_{\mathfrak e}(p)/\sqrt{8\ln(1/p)}$.

I evaluated both inequalities on 3992 points, $\mathfrak e\in\{0.1,0.3,0.5,1,2,5,10,16\}$ and $\iota$ from $\sqrt{2\mathfrak e}+1.05$ in steps of $0.05$. The smallest slack is $1.758$ in the first inequality and $2.379$ in the logarithm of the second (computed). The new factor is smaller than the old one $8e^2\ln(1/p)$ by the factor $e\sqrt{8\ln(1/p)}>2e$ on the range (proven). Non-vacuity holds since $2\sqrt{\mathfrak e\ln(1/p)}-\mathfrak e$ grows like the square root of $\ln(1/p)$ and $\ln(e\sqrt{8\ln(1/p)})$ like its logarithm (proven).

### The dispute on ch-residual-symbols

The builder is right (proven, by the symbol table). $h$ is the model name of [def-learning-oracle], and $M$, $M'$ and $M_k$ are runs in [thm-replay-audit-steer], so both names I proposed clash. Leaving the test function of (F2) unnamed is exact, since (F2) needs only a measurable function with values in $[0,1]$. Stating (F7) on measurable sets loses nothing, because step 4 of the proof of (a) applies it to the set $\mathbb A$ alone.

### ch-final-wording

Items 1 to 3 read as I proposed. The fact map in `theory/CURRENT.md` is complete against the fact lists named there, and the final document points to it in one sentence. That serves the reader of the round files, who reads `theory/CURRENT.md` anyway. I accept the move.

## Summary sentences

The sample covers the fourteen entries marked false, all sentences of "What the theory shows", and eleven entries marked complete. The eleven are the black-box sentences on (c) and (d), [lem-needle-lower-bound] "With $N$ runs", [thm-coupling-certificate] "On the adversary side", the dataflow "Reading of (e)(ii)", the transfer "Part (b) certifies it", "Then $N^\star=e^{(1+o(1))(R-1)/2}$", the replay "Without the random oracle", [lem-atomless-two-point], [def-model-bank] with [lem-bank-fidelity], the two heuristic sentences of open problem 5 and the remark on inversion. For each, I compared the sentence with the statement it summarizes, in the final document or in the round file of its pointer.

### The fourteen false sentences

All fourteen corrections restore the missing hypothesis, and each reason in the builder's brackets is correct (proven, by the counterexample or the comparison named).

| Sentence | Correction checked against | Reason checked |
| --- | --- | --- |
| Opening, "Train calls certify those quantities" | thm-dataflow-composition (d), thm-active-choice-dichotomy | no certificate covers all active strategies or an infinite admissible set |
| Opening, "The main results follow" | items 1 to 6 | items have two to six sentences |
| Item 2, finite query set | setting of thm-black-box-certifiability | counterexample above, and round-06/challenger.md |
| Item 4, "follow the protocol except for additive inputs" | the $B_A$-deviating condition | a coalition that also sets choices escapes the bound by thm-dataflow-composition (d) |
| Item 5, "the dataset be committed" | setting of thm-replay-audit-steer | a prover that picks its dataset after the seed is outside (a) |
| thm-coupling-certificate, "Without the oracle" | (a)(iii) | a clipped Gaussian release is atomless and (e)(iii) certifies it from drawn seeds |
| thm-coupling-certificate, "Degenerate oracles" | (a)(iii) at $\gamma=1$ | same counterexample |
| thm-dataflow-composition, "do not replace the oracle at a cost free of $d$ and $B$" | (e)(i), (e)(ii), (e)(iii) | (e)(iii) replaces it at a cost exponential in $B^2/\sigma^2$ |
| thm-dataflow-composition, "for a fixed strategy" | (c), (d) | by (d) no certificate covers all strategies |
| thm-bounded-deviation-transfer, part (c) summary | statement (c) | at $2B<\Delta$ no run exceeds $\Delta$, so $\Upsilon'=0$ is valid |
| thm-bounded-deviation-transfer, "(b) fails under drawn seeds" | (b), (e) | ch-drawn-seed-accuracy-level |
| thm-replay-audit-steer, "Without the oracle" | (d) | a learning function that ignores its seed is replayed exactly by drawn seeds |
| thm-bank-soundness, the estimate | round-01/builder.md, line 394 of its setting, "a finite set of tests fixed before the bank is built" | a test chosen on the bank voids the estimate |
| thm-active-choice-dichotomy | round-03/builder.md and round-04/builder.md | a certifier that always outputs one makes no call |

The builder's table cites round-02/builder.md for the test hypothesis of thm-bank-soundness. The hypothesis is first stated in the setting of round-01/builder.md. The pointer in the final document names round-01, so nothing needs to change there.

### The opening

Every sentence of the opening was checked. The three framing sentences of paragraph 1 summarize no theorem. Paragraphs 2 and 3 match criteria 1 to 4 of README.md and def-degenerate-oracles. Items 1, 2, 4, 5 and 6 carry every hypothesis of their statements, read with the convention of paragraph 2 that "certify" means soundly for every learning function (proven, by comparison). Item 4 omits $\ln R=o(\mathfrak e)$ correctly, since only the upper bound needs it and item 4 states the lower bound.

Item 3 is complete on one reading and wider on another (ch-opening-isolation, not blocking). Its hypothesis, "client data reach a coalition only via $R$ Gaussian releases", is informal. Its conclusion names the exceedance probability, which def-isolated-client defines with twins that share $c_t$ with the real chain. The round-06 counterexample with $c_t=W_{t-1}$ satisfies the informal hypothesis, has $\epsilon_b(\Delta_0)=0$, and leaks more than $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta_0/\sigma)$ (proven, sketch, round-06/challenger.md). Read with "coupled updates" as two full chains with shared seeds, the sentence is true for that example. The opening defines neither reading, so the sentence is not false as written. One clause aligns it with the definition.

### The eleven complete entries

All eleven are complete (proven, by comparison). The black-box sentence on (c) matches round-02/builder.md, line 348, including "over every learning function" in the soundness condition. I also checked the corrected sentence on (b) against its line 346, a deterministic bound on the expected advantage, uniform over learning functions.

## Definitions

Fourth reading. Only [def-isolated-client] changed this round, and only in condition 1 and its remark.

### [def-learning-oracle]

Unchanged. Well posed. ACCEPT.

### [def-learning-oracle-model]

Unchanged. Well posed. ACCEPT.

### [def-degenerate-oracles]

Unchanged in `theory/CURRENT.md`. The final document's remark now names the adversary that samples $\mathsf L$, which matches thm-perfect-substitution. Well posed. ACCEPT.

### [def-certifier]

Unchanged. Well posed. ACCEPT.

### [def-model-bank]

Unchanged. Well posed. ACCEPT.

### [def-isolated-client]

Condition 1 now carries the exclusion, and the argument under ch-choice-source shows that conditions 1 and 2 together give step 1 of the proof of [thm-dataflow-composition] (b) (proven). The remark's sentence on $c_t=D_j$ is true as an existence claim. With $f_t(c,m)=t\,\phi(c)$ the release means differ by $t\|\phi(D^0_j)-\phi(D^1_j)\|$ while $D^\star_b=0$. Remarks are not part of the definition. ACCEPT.

Simplicity. The six definitions remain the smallest that carry the presented proofs.

## The final document

I read `final/learning-oracle-theory.md` in full, 18 pages (pdfinfo). The proofs that changed this round were checked line by line: the proof of (c) and of (e) of the transfer, step 1 of the proof of [thm-dataflow-composition] (b), and step 3 of the proof of [thm-coupling-certificate] (b). All are correct as written (proven). I rechecked the expansion and the cell bound in the proof of (d) of the transfer, the corollary, (F2), (F3), (F6)(i), (F6)(ii) and (F7), with no finding.

One clause of a theorem statement is false as written (ch-strategy-calls). Part (c) of [thm-dataflow-composition] reads "Fix a strategy, ... Each run costs $2R$ Train calls for client $j$ plus the calls of the other nodes." A strategy is an adversary, and the setting of the transfer says that its oracle calls are unrestricted. An experimenter that samples $\mathsf{Ex}_0$ must compute $c_t$. Step 1 of the proof of (b) writes $c_t=\chi_t(\omega,y_{<t},\bar\rho_{<t})$, where $\omega$ serves the adversary's own Train calls. Those calls are not node calls. Counterexample (proven). Let the coalition's strategy make one Train call at a fixed input before round 2 and set $c_2$ from the answer, in a procedure whose other nodes make no Train call. Each run of $\mathsf{Ex}_0$ then needs at least $2R+1$ Train calls, against the stated $2R$. The proof of (c) in round-02/builder.md says "Each round costs two Train calls for client $j$" and does not address the strategy's calls. The soundness and the other cost statements are unaffected. Part (b) of the transfer and the corollary run the protocol's strategy, which makes no such call, and the "Without the oracle" paragraph says "for client $j$".

The criterion-4 paragraph of the transfer does not name the target of its drawn-seed certifier (ch-transfer-drawn-seed-target). The certificate (b) is sound for $\theta^{\mathrm{dev}}$ through $\hat t_0$, and part (e) is stated for certifiers of $\theta^{\mathrm{agg}}_R\ge\theta^{\mathrm{dev}}$. The remark of def-certifier carries lower bounds from a target to larger targets, not to smaller ones. So (e) as stated does not bind drawn-seed certifiers of $\theta^{\mathrm{dev}}$. The claim is still true (proven). In the proof of (e) the needle functions leak to the adversary that reads $y_1$ in the order $\mathrm H_\gamma(P_0\|P_1)$, so $\theta^{\mathrm{dev}}(\mathsf L_\varsigma)\ge\vartheta$, and the same transfer step applies. Stating (e) for $\theta^{\mathrm{dev}}$ gives the paragraph its premise and implies the present (e) by the remark.

Readability, not blocking (ch-final-readability). Four items.

1. Replay, "Without the oracle". "By (d), such an auditor complete up to $\lambda'$ for every rotation of the circle, accepts some fixed point ..." puts a comma between subject and verb, and "such an auditor" points back to a sentence that names no auditor class.
2. Dataflow, stated part (d). "it outputs at least $1-\eta$" leaves $\eta$ unquantified.
3. The kernel input $g\in\mathbb R^R$ of (F6)(ii) and step 4 of the proof of (b) differs from the Gaussian vector $\mathbf g$ of lem-sphere-code by font alone. That is the clash that round 05 removed for $\mathbf b_t$ against $b$.
4. "needs about ... calls" in the criterion-4 paragraph carries the label proven. The proven form is $N(2N-1)\ge\eta J_{\mathrm{cd}}$.

No semicolon, no dash used as punctuation, and no bold (computed). With mathematics removed, no prose sentence exceeds 30 words (computed). Counting each formula as one word, eight sentences have 31 to 34 words, all of them lists of objects. Symbols are defined before use.

## New challenges

### ch-strategy-calls

BLOCKING. A false clause in a theorem statement. Target: [thm-dataflow-composition] (c) in the final document, "Each run costs $2R$ Train calls for client $j$ plus the calls of the other nodes." The counterexample is under "The final document".

Smallest fix. "Each run costs $2R$ Train calls for client $j$, plus the calls of the other nodes and the strategy's own Train calls." The remark after def-isolated-client in the final document has the same gap, "samples $\mathsf{Ex}_b$ with two Train calls per round", which as a remark is not blocking. Fix it to "with two Train calls per round for client $j$, plus the strategy's own calls". If the register line or `theory/CURRENT.md` states the per-run cost, the same clause applies there.

### ch-transfer-drawn-seed-target

Not blocking. Due before the audit. Target: part (e) of [thm-bounded-deviation-transfer], its proof, and the criterion-4 paragraph. Smallest fix. In (e), "Let a drawn-seed certifier of $\theta^{\mathrm{dev}}$ with $N$ Train calls ...". After the statement, "By the remark of def-certifier the bound binds certifiers of $\theta^{\mathrm{agg}}_R$." In the proof, "So (F2) carries the divergence of (e)(ii) to $\theta^{\mathrm{dev}}$." In the paragraph, "A drawn-seed certifier of $\theta^{\mathrm{dev}}$ needs ...", citing "(e) with $J_{\mathrm{cd}}$ as in the Reading of thm-dataflow-composition (e)(ii)". The corollary is unaffected. It concerns $\theta^{\mathrm{agg}}_R$ throughout and certifies it with $\max\{\hat t_0,\hat t_1\}$.

### ch-opening-isolation

Not blocking. Target: item 3 of the opening, "If client data reach a coalition only via $R$ Gaussian releases". Smallest fix. "If client data reach a coalition only via $R$ Gaussian releases, as def-isolated-client makes precise, leakage is at most ...".

### ch-final-readability

Not blocking. The four items under "The final document". Smallest fixes.

1. "By (d), a drawn-seed auditor complete up to $\lambda'$ for every rotation of the circle accepts some fixed point with probability at least $1-\lambda'-\lambda$, for every $\lambda>0$."
2. "For every $\eta\in(0,1)$, at some function where that leakage is zero, it outputs at least $1-\eta$ with probability at least $1-\alpha$."
3. Rename the kernel input, for instance to $\mathfrak z\in\mathbb R^R$ with coordinates $\mathfrak z_t$, in (F6)(ii) and in step 4. The symbol is free in both files.
4. "A drawn-seed certifier with $N$ calls and $N(2N-1)<\eta J_{\mathrm{cd}}$, so about $\sqrt{\eta J_{\mathrm{cd}}/2}$ calls or fewer, outputs ...". Optional, since the Reading of (e)(ii) uses "about" with the same meaning.

## Assessment

Fidelity. Every statement and label in the final document matches the register of `theory/CURRENT.md`, and the register lines changed this round match the final text. Every full proof is correct as written (proven). The summary sentences in the sample are faithful, and the builder's fourteen corrections fix real errors (proven, each by the counterexample named). The search was worth its cost. Fourteen false sentences in a document that three rounds had accepted show that a summary sentence needs the same check as a statement.

Correctness. One clause of a theorem statement is false, the per-run cost of part (c) of [thm-dataflow-composition] for a strategy that makes its own Train calls. The clause has stood since round 02, and no reading before this one checked a cost against the strategy's calls. The fix is one clause and changes no proof. I set that theorem to REVISE until the clause is in. Its proofs are correct and criterion 4 holds, so it returns to ACCEPT NONTRIVIAL with the fix.

Simplicity. Unchanged from round 06. No object is carried without use, apart from the hypothesis class.

Readiness. The final document is not ready for the audit while ch-strategy-calls is open. If round 08 applies it with ch-transfer-drawn-seed-target and adds no error, the stopping rule holds after that round. The definitions have been accepted in four consecutive challenger files. Fifteen results have slug tags. Fourteen stand accepted and one is set to REVISE. Seven of the accepted results are NONTRIVIAL, and the revised one is the eighth once fixed.

## Verdicts

Six definitions and fifteen results with slug tags in the final document are judged as they stand there. One challenge is blocking: ch-strategy-calls.

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
VERDICT thm-dataflow-composition REVISE
VERDICT thm-bounded-deviation-transfer ACCEPT NONTRIVIAL
VERDICT thm-replay-audit-steer ACCEPT NONTRIVIAL
VERDICT thm-perfect-substitution ACCEPT
VERDICT thm-reference-access ACCEPT
VERDICT thm-bank-soundness ACCEPT
VERDICT thm-active-choice-dichotomy ACCEPT NONTRIVIAL
VERDICT thm-record-level-certificate ACCEPT NONTRIVIAL
VERDICT thm-smoothed-choice-certificate ACCEPT NONTRIVIAL
BLOCKING 1
```
