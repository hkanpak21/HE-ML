# Round 07, builder

Verdict of this turn. Both blocking challenges are closed with the challenger's clauses. Item 2 of the opening now names the finite query set. The criterion-4 paragraph of [thm-bounded-deviation-transfer] now states the accuracy level and the value $\theta^{\mathrm{agg}}_R=0$ at the reference function. It also states two conditions that the challenger's text lacked, $\alpha+\eta<1$ and $d\ge6$. The five other challenges are accepted. One item of ch-residual-symbols is disputed, because the proposed name $h$ is already a model name, and the test function is left unnamed instead. One item of ch-final-wording is closed by moving the fact map to `theory/CURRENT.md`, where it is now complete. The sharpened factor of part (c) is applied, so the transfer function is tight up to the factor $e\sqrt{8\ln(1/p)}$ (proven, below). No theorem is added. The search for summary sentences that drop a hypothesis checked 92 entries, each one sentence or a group of parallel sentences, and changed 51 of them. Fourteen of the changed sentences were false as written, at least on one reading, and the others were true but weaker or wider than their theorem. Every sentence is listed below. The final document has 18 pages, `node scripts/verify.mjs final` prints `FINAL OK theorems=5 nontrivial=5 items=21`, and the build prints `BUILD OK n=3`.

Notation follows `theory/CURRENT.md` after this round. Every claim carries one of the labels proven, heuristic or open.

## Responses to challenges

### ch-opening-finite-queries

Accepted. Item 2 of the opening now reads as follows. "Label-only leakage at a fixed number of queries, on a finite query set with finitely many outputs, is certifiable from both sides. With deterministic evaluation and atomless model laws, drawn seeds never certify that leakage below one equals white-box leakage (proven)."

Two clauses go beyond the challenger's text, and both restore a hypothesis of [thm-black-box-certifiability].

1. Finitely many outputs. The setting has $C<\infty$, and part (a) pays $\ln|\mathfrak T_q|$, which is infinite otherwise. Without it the first sentence is false (proven, sketch). Take $U=\{u\}$, $\mathcal M=\mathcal Y=[0,1)$ and $\mathsf{ev}(m,u)=m$. Let the reference function draw its model uniformly from the hardware randomness, ignoring the seed and the dataset, so $\mathrm{Adv}^{\mathrm{bb}}(1)=0$. Cut $[0,1)$ into $M$ cells of equal length, and let $A_S$ be the union of half of them. Let $\mathsf L_S$ put the model at $x_0$ uniformly in $A_S$ and at $x_1$ uniformly in its complement, again from the hardware randomness. Then $\mathrm{Adv}^{\mathrm{bb}}(1)=1$ under $\mathsf L_S$. Seeds carry nothing, so every Train call at $x_0$ or $x_1$ is a fresh draw in either discipline. Steps 2 to 4 of lem-atomless-two-point then give $\Pr[\hat t\ge1]\ge1-\alpha-N(2N-1)/M$ at the reference function for every sound upper certifier. This is the realization of thm-reference-access (c)(ii) applied to a certifier.
2. Below one. Part (c) assumes $\mathrm{Adv}^{\mathrm{bb}}(Q)+\lambda<1$, and the claim that the two leakages are equal is the case $\lambda=0$. So the sentence needs the common value below one.

### ch-drawn-seed-accuracy-level

Accepted. The paragraph "Degenerate oracles" of [thm-bounded-deviation-transfer] now reads as follows.

"Degenerate oracles. Part (a) holds under both adversary-side oracles, since each release's noise is independent of all that the coalition holds when it sets that round's input. Part (d) holds in both disciplines. At the reference function of (e), where $\theta^{\mathrm{agg}}_R=0$, the certificate (b) outputs at most $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}$ with $2R\lceil\ln(1/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)\rceil$ Train calls. A drawn-seed certifier needs about $\sqrt{\eta/2}\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$ calls there to output below $1-(1+\gamma)e^{-B^2/(16\sigma^2)}$ with probability above $\alpha+\eta$, by the Reading of thm-dataflow-composition (e)(ii). Let $d\ge6$, $\alpha+\eta<1$ and $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<1-(1+\gamma)e^{-B^2/(16\sigma^2)}$. Then (b) fails under drawn seeds when the first number is below the second, for instance at $B_A=0$, large $d$ and $B/\sigma$, $\epsilon_{\mathrm{acc}}<1$ and small $\sqrt R\Delta/\sigma$ (proven)."

Two conditions go beyond the challenger's text. The second number comes from the Reading of (e)(ii), which needs $d\ge6$ for $J_{\mathrm{cd}}\ge1$. The comparison concerns outputs below the threshold with probability above $\alpha+\eta$, and (b) produces such outputs with probability one, so the inference needs $1>\alpha+\eta$. Without either condition the sentence claims more than the Reading gives.

The value $\theta^{\mathrm{agg}}_R=0$ is now stated in part (e) and proven there (proven). At the reference function of (e), the model at client $j$'s training input of round 1 is $m_1$ plus a code point chosen by the seed. In later rounds it is the starting model. Both are the same under both hypotheses, so every release has one law under both hypotheses, for every strategy. Under the top oracle a Train call with an honest seed name returns the same model whatever dataset the adversary puts in the input. The view has one law under both hypotheses, and $\theta^{\mathrm{agg}}_R=0$. No run of $\mathsf{Ex}_b$ exceeds $\Delta$, since every coupled pair coincides.

With the fix, criterion 4 holds by the challenger's witness (proven). Take $B_A=0$, $d\ge6$, $\epsilon_{\mathrm{acc}}=1/4$, $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)\le1/4$, and $B/\sigma$ and $d$ large enough that $(1+\gamma)e^{-B^2/(16\sigma^2)}<1/2$ and $N=2R\lceil4\ln(1/\alpha)\rceil<\sqrt{\eta J_{\mathrm{cd}}/2}$, with $J_{\mathrm{cd}}$ of the Reading and $\alpha+\eta<1$. Then (b) outputs at most $1/2$ with certainty. A drawn-seed certifier with $N$ calls has $N(2N-1)/J_{\mathrm{cd}}<\eta$, so by (e) it outputs above $1/2$ with probability at least $1-\alpha-\eta>0$.

The register line of `theory/CURRENT.md` carried the same gap. It now says "Drawn seeds fail where the coupled cost is below theirs and the coupled accuracy level lies below the drawn-seed threshold, for instance at $B_A=0$ with $d$ and $B/\sigma$ large, $\epsilon_{\mathrm{acc}}<1$ and $\sqrt R\Delta/\sigma$ small."

### ch-choice-source

Accepted. Condition 1 of [def-isolated-client] reads, in both files, "$v_t$ calls $\mathsf{Train}(x(c_t,D_j,W_{t-1}),\bot)$, where $W_t$ is the value of $v_t$ and $W_0=w_0$. Here $c_t$ is the value of a parent of $v_t$ other than $v_{t-1}$ and the input node of $D_j$, or a choice of the coalition." The sentence is split to keep it under thirty words. Step 1 of the proof of [thm-dataflow-composition] (b) now cites the condition. "By condition 1, $c_t$ is neither $D_j$ nor $W_{t-1}$. Since $r_{t-1}\prec v_t\prec r_t$, $c_t$ and $O_t$ have the stated arguments." The remark of the definition in `theory/CURRENT.md` records the challenger's counterexample, in which the release means drift apart by $t$ times the per-round gap.

### ch-opening-scope

Accepted, all three clauses.

1. Item 1 now says "Coupled Train calls certify it for every learning function when the divergence of the channel at two models is computable." The theorem keeps the hypothesis, and the "Without the oracle" paragraph of [thm-coupling-certificate] states it too.
2. Item 4 now says "In the clipped aggregation instance, take a certifier sound for every learning function. Let it be accurate where the leakage is zero, below a fixed fraction of one clipped release's leakage." The fraction is the factor $1-\eta/2$ of the corollary, with $\eta$ fixed, as the asymptotics require. The item also adds "clipped" for $B<\infty$ and "At fixed error probabilities summing below one" for $\alpha+\alpha'<1$, both hypotheses of the corollary.
3. Item 4 now says "$e^{(1+o(1))\mathfrak e}\ln(1/\alpha)$ runs reach a fixed accuracy when none exceeds the threshold." The last clause is the condition of the accuracy part of (b), which the challenger's text left implicit. The exact count is $\ln(1/\alpha)\exp(\mathfrak e+2\sqrt{\mathfrak e\ln(1/\epsilon_{\mathrm{acc}})}+\ln(1/\epsilon_{\mathrm{acc}}))$, which is $\ln(1/\alpha)e^{(1+o(1))\mathfrak e}$ at fixed $\epsilon_{\mathrm{acc}}$ (proven).

### ch-tightness-inline

Accepted, with the sharpening. The proof of [thm-bounded-deviation-transfer] (c) now contains the derivation, and part (c) states the sharper constants.

Claim. In the setting of part (c), $\ln(1/\epsilon_0(\Delta))\le\ln(1/\Upsilon_{\mathfrak e}(\epsilon^{\mathrm{pr}}_0(\Delta)))+\ln(\iota+1)+1$, and every admissible transfer function $\Upsilon'$ satisfies $\Upsilon'(p)\ge e^{-1}\Upsilon_{\mathfrak e}(p)/\sqrt{8\ln(1/p)}$ for $p\in(0,\bar\Phi(\sqrt{2\mathfrak e}+1))$. Label. Proven.

Proof. Let $p=\bar\Phi(\iota)$ and $r=\iota-\sqrt{2\mathfrak e}$, so $1<r\le\iota$. By (F6)(iii), $\ln(1/p)\ge\iota^2/2>\mathfrak e$. So $\sqrt{\ln(1/p)}\ge\iota/\sqrt2$, and $\sqrt{\ln(1/p)}-\sqrt{\mathfrak e}\ge(\iota-\sqrt{2\mathfrak e})/\sqrt2=r/\sqrt2>0$. Hence $\ln(1/\Upsilon_{\mathfrak e}(p))=(\sqrt{\ln(1/p)}-\sqrt{\mathfrak e})^2\ge r^2/2$. The lower bound of (F6)(iv) gives $\bar\Phi(r)\ge\frac r{1+r^2}\varphi(r)$, so $\ln(1/\bar\Phi(r))\le r^2/2+\ln(r+1/r)+\ln\sqrt{2\pi}$. Here $r+1/r<\iota+1$ and $\ln\sqrt{2\pi}<0.92<1$. Since $\epsilon_0(\Delta)=\bar\Phi(r)$, the two bounds give the first claim. For the second, $\bar\Phi$ is continuous and strictly decreasing, so each $p$ in the range is $\bar\Phi(\iota)$ for one $\iota>\sqrt{2\mathfrak e}+1$. Then $\iota+1<2\iota\le\sqrt{8\ln(1/p)}$, and the instance of the first part with this $\iota$ gives $\ln(1/\Upsilon'(p))\le\ln(1/\epsilon_0(\Delta))\le\ln(1/\Upsilon_{\mathfrak e}(p))+\ln\sqrt{8\ln(1/p)}+1$. $\square$

The new factor $e\sqrt{8\ln(1/p)}$ is below the old $8e^2\ln(1/p)$, since their ratio is $e\sqrt{8\ln(1/p)}>e\cdot2>1$ on the range, where $\ln(1/p)>1/2$. The statement is still not vacuous, because $\ln(\Upsilon_{\mathfrak e}(p)/p)=2\sqrt{\mathfrak e\ln(1/p)}-\mathfrak e$ grows faster than $\ln(e\sqrt{8\ln(1/p)})$ as $p\to0$ (proven). The "Without the oracle" paragraph and the register line now state the factor $e\sqrt{8\ln(1/\epsilon^{\mathrm{pr}}_0(\Delta))}$ with its hypotheses.

### ch-residual-symbols

Accepted for six items, disputed for one. The table gives the new names in the final document and in `theory/CURRENT.md`.

| Symbol | Second object | Now |
| --- | --- | --- |
| $W_0$, $W_1$ | coupled pair of thm-coupling-certificate | $W^\Gamma_0$, $W^\Gamma_1$, with draws $W^{\Gamma,i}_b$, also in open problem 8 of `theory/CURRENT.md` |
| $m_0$, $m_1$ | arguments of the divergence in thm-coupling-certificate (b) | $(m,m')$, two models |
| $m_0$ | starting model of thm-replay-audit-steer | $m^{\mathrm{st}}$ |
| $o_t$ | value of the rest of the contribution in thm-bounded-deviation-transfer | $\bar o_t$, in the setting and in step 1 of the proof of (a) |
| $F$ | transfer function of thm-bounded-deviation-transfer (c) | $\Upsilon'$ |
| $K^*$ | index in the proof of thm-replay-audit-steer (a) | $k^*$ |
| $g$ | test function of (F2) and (F7) | no name |
| $\mathbf e_1$ | undefined | "the first standard basis vector" at first use, in the proof of (c) |

The dispute concerns $g$. The proposed name $h$ is the model name of def-learning-oracle, so it would trade one clash for another. The first name $(M_0,M_1)$ proposed for the coupled pair has the same problem, since $M_k$ is the $k$-th grinding run of thm-replay-audit-steer (c). (F2) now says "A measurable function with values in $[0,1]$ has integral against $P_0-\gamma P_1$ at most $\mathrm H_\gamma(P_0\|P_1)$." (F7) is stated on measurable sets, "Hölder's inequality gives $\mathbb P'(\cdot)\le\mathbb P(\cdot)^{1-1/\varpi}(\int(d\mathbb P'/d\mathbb P)^{\varpi}d\mathbb P)^{1/\varpi}$ on every measurable set", which is the only form step 4 of the proof of (a) uses. That step now reads "(F7) on $\mathbb A$ gives the first bound." The symbol table of `theory/CURRENT.md` lists $W^\Gamma_b$, $m^{\mathrm{st}}$, $k^*$, $\bar o_t$, $\Upsilon'$ and $\mathbf e_1$, and the section "Names in the round files" maps every old name.

### ch-final-wording

Accepted, items 1 to 3 as written, item 4 in another place.

1. Step 3 of the proof of [thm-coupling-certificate] (b) now reads "Under the top oracle every transcript is the image of $(\rho,Y)$ under a kernel free of the hypothesis, and an adversary that opens the seed name holds $(\rho,Y)$. So (F2) and (F1) make $\mathrm D^\top_1(K)$ the best advantage."
2. The reason in the "Degenerate oracles" paragraph of the transfer is now "since each release's noise is independent of all that the coalition holds when it sets that round's input".
3. That paragraph now says "Part (d) holds in both disciplines."
4. The fact map now lives in the section "Names in the round files" of `theory/CURRENT.md`. There it includes the challenger's sentence, "(F3) and (F5) of round 03, (F7) of round 04 and Lyapunov's theorem of round 01 have no counterpart there". It also records that McDiarmid's inequality is part of (F8), and that the DKW inequality and lazy sampling keep their names. The final document keeps one sentence, "The round files number these facts differently, and `theory/CURRENT.md` maps their numbers to these." I checked the map against the fact lists of round-01/builder.md to round-05/builder.md. The move saves four lines, which the blocking fixes and the summary search needed within 18 pages. The map serves a reader of the round files, who reads `theory/CURRENT.md` as well.

### The remark on open problem 5

Applied in `theory/CURRENT.md`. Open problem 5 there now says that feedback does not raise the capacity of a memoryless channel. It helps here because the decoder sees only the final sum $m_R$, while the coalition sees every release. The final document keeps the short form, with each heuristic sentence labelled.

## Summary sentences checked

I compared every summary sentence of the final document with the full statement it summarizes. That statement is in the final document, or in the register of `theory/CURRENT.md` and the round file that the pointer names. A sentence counts as a summary when it restates a theorem, a part of one, or a criterion of README.md in fewer words. "Complete" means that no hypothesis of the statement is missing. Otherwise the entry names the clause added. The entries marked false were false as written, with the reason in brackets.

| Where | Sentence, by its first words | Result |
| --- | --- | --- |
| Opening, paragraph 2 | "Every bound below depends ... only through" | "probabilities" became "quantities", since $\beta_\gamma(K)$ is a mean of divergences |
| Opening, paragraph 2 | "So each bound holds for every learning function" | split, and "where a result says so" added to the certification clause (false, no certificate exists against all active strategies or for an infinite admissible set) |
| Opening, paragraph 3 | "The bottom oracle gives an adversary" | complete |
| Opening, paragraph 3 | "For an experimenter the two cases" | adds "or an auditor", item 3 of def-degenerate-oracles |
| Opening, paragraph 3 | "Its bound depends ... and it fails" | adds "or becomes vacuous", criterion 4 of README.md |
| Opening, paragraph 4 | "The main results follow, one sentence each" | "one sentence each" removed (false, the items have two to six sentences) |
| Item 1 | "One training node leaks at most the coupled divergence" | complete |
| Item 1 | "Coupled Train calls certify it" | adds "when the divergence of the channel at two models is computable" |
| Item 1 | "Through a deterministic channel with atomless view laws" | adds "for the total variation", the target of (a)(iii) |
| Item 2 | "Label-only leakage at a fixed number of queries" | adds "on a finite query set with finitely many outputs" (false without it, blocking) |
| Item 2 | "With deterministic evaluation and atomless model laws" | adds "below one", the hypothesis $\mathrm{Adv}^{\mathrm{bb}}(Q)+\lambda<1$ |
| Item 3 | "Over $R$ Gaussian releases, leakage is at most" | now "If client data reach a coalition only via $R$ Gaussian releases", the isolation of def-isolated-client |
| Item 3 | "Coupled runs of a fixed strategy certify" | complete |
| Item 4 | "If a coalition's additive inputs stay within $B_A$" | now "let a coalition follow the protocol except for additive inputs" (false, a coalition that also sets choices escapes the bound by thm-dataflow-composition (d)) |
| Item 4 | "Coupled runs of the protocol certify it" | adds the count $e^{(1+o(1))\mathfrak e}\ln(1/\alpha)$ and "when none exceeds the threshold" |
| Item 4 | "In the aggregation instance, a certifier" | adds "clipped", "below a fixed fraction of one clipped release's leakage" and "at fixed error probabilities summing below one" |
| Item 5 | "With seeds from a random oracle, a prover lands training" | adds "the dataset be committed" and "passes a replay audit with a model in a target set" (false, a prover that picks its dataset after the seed steers freely) |
| Item 5 | "Under deterministic kernels grinding attains it" | adds "with at least one oracle query", since (c) needs $n_{\mathrm{nc}}=q_{\mathsf{RO}}\ge1$ |
| Item 6 | "A certifier sound for every learning function that makes $N$" | complete |
| Opening | "Each claim is labelled proven" | complete, moved before the list |
| def-learning-oracle-model, remark | "So every privacy bound below also bounds inversion" | complete |
| def-certifier, remark | "So each lower bound below binds certifiers of every larger target" | complete |
| def-degenerate-oracles, remark | "The bottom oracle is the real procedure" | adds "against an adversary that samples $\mathsf L$", part (c) of thm-perfect-substitution |
| def-degenerate-oracles, remark | "For one fixed learning function an adversary can hard-wire" | complete, reworded |
| def-degenerate-oracles, remark | "The drawn-seed discipline is what a training service" | complete, reworded |
| def-isolated-client, remark | "An experimenter that holds every input samples" | adds "and runs the strategy" |
| def-isolated-client, remark | "For a passive strategy $\epsilon_b$ is the same" | complete, reworded |
| Standing facts | the fact map | moved to `theory/CURRENT.md` and completed (ch-final-wording) |
| lem-needle-lower-bound | "Without the oracle, ... a sound certifier must output" | adds "sound at the needle functions" and "at the reference function" |
| lem-needle-lower-bound | "With $N$ runs it rules out at most $N$" | complete |
| thm-coupling-certificate | "Without the oracle, part (a)(iii) shows" | adds "drawn-seed", "the total variation", "soundly for every learning function" and "the view is a deterministic function of the model" (false, a clipped Gaussian release is atomless and drawn seeds certify it by thm-dataflow-composition (e)(iii)) |
| thm-coupling-certificate | "Analysis needs the law of the trained transformer" | complete |
| thm-coupling-certificate | "With the oracle, part (b) certifies" | adds "when the divergence of the channel at two models is computable" |
| thm-coupling-certificate | "It uses the learning function only through" | complete, reworded |
| thm-coupling-certificate | "Degenerate oracles. The certificate of (b) has no drawn-seed counterpart" | adds "Through a deterministic channel with atomless view laws" and "at $\gamma=1$" (false when read for every channel, by the same Gaussian counterexample) |
| thm-coupling-certificate | "On the adversary side, (b) brackets" | complete |
| thm-coupling-certificate | the pointers of (a)(ii), (a)(iii) and (c)(ii) | complete |
| thm-black-box-certifiability | "(b) to (d), stated. A bottom-oracle adversary" | adds "One" and "for every learning function", without which the sentence holds trivially for an adversary that knows $\mathsf L$ |
| thm-black-box-certifiability | "With deterministic $\mathsf{ev}$ and atomless model laws, a drawn-seed procedure" | complete |
| thm-black-box-certifiability | "Coupled pairs certify" | complete |
| thm-black-box-certifiability | "Without the oracle, a bound on what $q_E$ label queries reveal" | complete |
| thm-black-box-certifiability | "With the oracle, part (a) certifies" | "depends on the learning function only through" became "fixed by $C$, $|U|$, the number of queries, $\alpha$ and the accuracy" |
| thm-black-box-certifiability | "Part (c) says that drawn seeds can refute" | adds "deterministic evaluation and atomless model laws" and "when the claimed value is below one" |
| thm-black-box-certifiability | "Degenerate oracles. Part (o) holds" | complete |
| thm-dataflow-composition | "The certificate holds for every passive adversary" | complete |
| thm-dataflow-composition | "Reading of (e)(ii)", both sentences | complete |
| thm-dataflow-composition | "(a) The ciphertexts of an aggregation sub-protocol" | complete |
| thm-dataflow-composition | "For threshold CKKS that error is negligible" | adds "with smudging" and "against a deviating coalition only with six additions", open problem 6 |
| thm-dataflow-composition | "Unchecked decryption lets a public scalar" | complete |
| thm-dataflow-composition | "Noise that client $j$ adds inside its ciphertext" | complete |
| thm-dataflow-composition | "(d) No sound certifier certifies anything below $1-\eta$" | adds "In some one-round procedure", "sound for every learning function", "at some function where that leakage is zero" and the probability $1-\alpha$ |
| thm-dataflow-composition | "(e)(i) Without clipping, drawn seeds certify nothing" | adds "In the setting of (e)(ii)", "sound for every learning function" and the probability $1-\alpha-\eta$ |
| thm-dataflow-composition | "(e)(iii) with clipping ... drawn-seed runs suffice" | adds "Over $\mathfrak L_B$", "reach accuracy $\epsilon_{\mathrm{acc}}$" and "at fixed $\gamma$" |
| thm-dataflow-composition | "Without the oracle, a privacy bound for this procedure" | complete, reworded |
| thm-dataflow-composition | "Parts (e)(i) and (e)(ii) show that drawn-seed runs do not replace" | adds "at a cost free of $d$ and $B$" (false, (e)(iii) replaces the oracle at a cost exponential in $B^2/\sigma^2$) |
| thm-dataflow-composition | "With the oracle, part (b) holds for every learning function" | complete |
| thm-dataflow-composition | "It uses the learning function only through $\epsilon_b(\Delta)$, which part (c) certifies" | adds "for a fixed strategy" and "for client $j$" (false, by part (d) no certificate covers all strategies) |
| thm-dataflow-composition | "Degenerate oracles", three sentences | complete |
| thm-bounded-deviation-transfer | "Without the oracle, a bound against a coalition" and the next sentence | complete |
| thm-bounded-deviation-transfer | "With the oracle, part (a) reduces every deviation" | adds "in the additive inputs" |
| thm-bounded-deviation-transfer | "Part (b) certifies it at a cost free of $d$" | complete |
| thm-bounded-deviation-transfer | "Part (c) shows that no transfer function beats" | adds "In $G^{\mathrm{agg}}_R$ with $R\ge2$, $B_A>0$ and $B\ge2\Delta$" and "once $\epsilon^{\mathrm{pr}}_0(\Delta)<\bar\Phi(\sqrt{2\mathfrak e}+1)$" (false, at $2B<\Delta$ the zero function is a valid transfer function) |
| thm-bounded-deviation-transfer | "Part (d) and the corollary show" | adds "the clipped instance", "certifiers sound for every learning function and accurate as in the corollary" and "$\ln R\ll\mathfrak e$" (unproven as written, since with $\ln R\gg\mathfrak e$ the cost of (b) carries a factor $R$ that the lower bound lacks) |
| thm-bounded-deviation-transfer | "Degenerate oracles. Part (a) holds ... since neither reveals" | reason replaced, and "(c) and" cut (ch-final-wording) |
| thm-bounded-deviation-transfer | "At the reference function of (e), the certificate (b) is accurate" | adds "where $\theta^{\mathrm{agg}}_R=0$" and the output level (blocking) |
| thm-bounded-deviation-transfer | "A drawn-seed certifier needs about" | complete |
| thm-bounded-deviation-transfer | "So (b) fails in the drawn-seed discipline whenever" | adds $d\ge6$, $\alpha+\eta<1$ and the accuracy-level condition (false, blocking) |
| thm-bounded-deviation-transfer | "Reading. ... so that the condition of the corollary holds" | "condition" became "conditions", which include $\alpha+\alpha'<1$ |
| thm-bounded-deviation-transfer | "Then $N^\star=e^{(1+o(1))(R-1)/2}$" and "At $\varepsilon=1$" | complete |
| thm-replay-audit-steer | "Without the oracle, an auditor cannot replay" | complete |
| thm-replay-audit-steer | "and by (d) cannot separate completeness from soundness" | now the exact statement of (d), for an auditor complete for every rotation of the circle (false as a general claim, a learning function that ignores its seed is replayed exactly by drawn seeds) |
| thm-replay-audit-steer | "Parts (a) to (c) fix the steering probability" | "fix" became "bound from both sides" |
| thm-replay-audit-steer | "Nobody can write these down" | complete |
| thm-replay-audit-steer | "Degenerate oracles. The prover holds" and "So the test runs through the auditor" | complete |
| thm-replay-audit-steer | "In the coupled discipline the auditor is sound and complete" | now "has the soundness of (a) and the completeness of (b)", with their error terms |
| thm-replay-audit-steer | "Under drawn seeds the statement fails, by (d)" | adds "for the rotations of (d)" |
| thm-replay-audit-steer | "Without the random oracle (a) fails" | complete |
| thm-replay-audit-steer | the pointer of (c) to (e) | complete |
| Further results | thm-perfect-substitution | adds "Against an adversary that samples $\mathsf L$ once per Train call" |
| Further results | thm-reference-access, first sentence | adds "seen through a deterministic channel" |
| Further results | thm-reference-access, second sentence | "uniform rate on atomless views" became "rate uniform over learning functions when the views can be atomless" |
| Further results | lem-atomless-two-point | complete |
| Further results | def-model-bank and lem-bank-fidelity | complete |
| Further results | thm-bank-soundness, estimate | adds "for a finite set of tests fixed before the bank is built", round-02/builder.md (false, a test chosen on the bank voids the estimate) |
| Further results | thm-bank-soundness, label | adds "through a Gaussian release" to the first half of (d), round-04/builder.md |
| Further results | thm-active-choice-dichotomy | adds "sound for every learning function and accurate where the leakage is zero", "In some procedure", "distinct" and "up to a logarithmic factor" (false, a certifier that outputs one makes no call) |
| Further results | thm-record-level-certificate | adds "to a passive coalition" |
| Further results | thm-smoothed-choice-certificate | adds "with $B<\infty$" |
| Further results | the heuristic comparison of the two costs | complete |
| Open problem 5 | "Known (proven), $N^\star\ge(1-\alpha-\alpha')J^{\mathrm{fb}}$" | adds "under the hypotheses of the corollary" |
| Open problem 5 | the two heuristic sentences | complete, each labelled heuristic |
| Prior work | the five comparisons | complete |

The table has 92 entries. Of them, 51 add, replace or move a clause and 41 are complete (computed, by counting the rows). The fourteen entries marked false are corrected sentences that were false as written, two of them only on the reading that the bracket names. The others restore a hypothesis whose absence made the sentence wider or weaker than its theorem without making it false.

## Changes to the final document

What the theory shows.

1. Paragraph 1 is two sentences shorter with the same content. Paragraph 2 says "quantities" and limits certification to the results that state it. Paragraph 3 names the auditor and the vacuous case of criterion 4.
2. "One sentence each" is cut, and the sentence on labels moves before the list.
3. Items 1 to 5 carry the clauses of the table above.

Definitions.

1. [def-degenerate-oracles]. The remark names the adversary that samples $\mathsf L$ and is shortened.
2. [def-isolated-client]. Condition 1 excludes $v_{t-1}$ and the input node of $D_j$ as sources of $c_t$ (ch-choice-source). The coupled tail is stated inline. The remark names the experimenter that runs the strategy.

Standing facts. (F2) and (F7) no longer name a test function. The fact map moves to `theory/CURRENT.md`.

[lem-needle-lower-bound]. The "Without the oracle" paragraph names the reference function and the needle functions.

[thm-coupling-certificate]. The coupled pair is $W^\Gamma_0,W^\Gamma_1$, and the divergence of (b) takes $(m,m')$. Part (a)(iii) names its target, the total variation. The certificate of (b) is stated inline. The "Without the oracle" and "Degenerate oracles" paragraphs carry the deterministic channel and the computability. Step 3 of the proof of (b) reads as under ch-final-wording.

[thm-black-box-certifiability]. The stated part (b) is uniform over learning functions. The "Without the oracle" paragraph carries the hypotheses of (c).

[thm-dataflow-composition]. The stated parts (a), (d), (e)(i) and (e)(iii) carry their hypotheses. The "Without the oracle" paragraph limits the drawn-seed claim and the certificate. Step 1 of the proof of (b) cites condition 1.

[thm-bounded-deviation-transfer].

1. Setting. The rest of the contribution is $\bar o_t$, and $\mathfrak e$ and $\Upsilon_{\mathfrak e}$ are defined inline.
2. Part (a) and the corollary state their bounds inline. Part (c) states the sharper constants and names the function $\Upsilon'$. Part (d) states $J_3$ inline. Part (e) states $\theta^{\mathrm{agg}}_R=0$.
3. The Reading says "conditions". The "Without the oracle" and "Degenerate oracles" paragraphs read as quoted above.
4. Proof of (a). Step 1 uses $\bar o_t$, and step 4 applies (F7) on $\mathbb A$. Proof of (c). The first standard basis vector is defined, and the derivation of ch-tightness-inline replaces the pointer to round-05/builder.md. Proof of (e). It proves $\theta^{\mathrm{agg}}_R=0$.

[thm-replay-audit-steer]. The starting model is $m^{\mathrm{st}}$ and the index of the proof of (a) is $k^*$. The "Without the oracle" and "Degenerate oracles" paragraphs carry the exact content of (a), (b) and (d).

Further accepted results. The seven pointer sentences carry the clauses of the table. Two long sentences are split.

Open problems. The pointer to `theory/CURRENT.md` moves into the opening paragraph. Open problem 5 states the hypotheses of the corollary and keeps two heuristic sentences without the computed values, which `theory/CURRENT.md` keeps.

Length and style. Seven displays became inline formulas, and sentences whose last printed line held one to three words lost those words. No statement, hypothesis or label changed in these cuts. The document has 18 pages (pdfinfo). No prose sentence added this round exceeds 30 words (computed, by a script that strips mathematics). The document has no semicolon, no dash used as punctuation, no bold and no colon in prose (computed). The one sentence over 30 words is the statement of [thm-dataflow-composition] (b), which introduces a display and is unchanged since round 06.

`theory/CURRENT.md`. The title and the opening name round 07. Condition 1 of [def-isolated-client] and its remark are updated. The symbol table lists the new names. The register records the round-06 verdicts and restates the lines of [def-isolated-client], [thm-coupling-certificate], [thm-black-box-certifiability], [thm-bank-soundness], [thm-active-choice-dichotomy] and [thm-bounded-deviation-transfer] with the clauses above. Open problem 5 carries the remark on feedback, and open problem 8 uses $W^\Gamma_0$. The section "Names in the round files" holds the complete fact map and the renamings of this round.

Checks. `node scripts/build.mjs round-07/builder.md theory/CURRENT.md final/learning-oracle-theory.md` prints `BUILD OK n=3`. `node scripts/verify.mjs final` prints `FINAL OK theorems=5 nontrivial=5 items=21`.
