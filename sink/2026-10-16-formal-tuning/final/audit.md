# Audit of the final document

Verdict. FINAL ACCEPT. No statement, proof step or definition of `final/learning-oracle-theory.md` is false or ill-posed as written, and every label matches what the document or its pointer proves. Seven findings are minor. Each has a fix of one clause, and none changes a result.

## Method

I read the document from line 1 to line 358 in order, as a reader who has not seen the rounds. I re-derived every proof that the document shows in full, step by step. These are lem-needle-lower-bound, lem-sphere-code, thm-coupling-certificate (a)(i), (a)(ii), (b) and (c)(i), thm-black-box-certifiability (o) and (a), thm-dataflow-composition (b), (c) and (e)(ii) with its Reading, all of thm-bounded-deviation-transfer with its corollary and Reading, and thm-replay-audit-steer (a), (b) and the factor $3.2$ of (c). I checked the nine standing facts and every summary against the statement it summarizes. For the active-choice paragraph I also read its source, round-03/builder.md, lines 268 to 325. I recomputed the constants $\delta_{\mathcal N}(1;1)=0.1269$, $1-\mathrm h_2(1/4)=0.1887$, $2/(1-e^{-1})=3.164$, $\ln\sqrt{2\pi}=0.919$ and $2^{0.18\cdot6-1}=1.057$ (computed). A mechanical pass, with each formula counted as one word, found no sentence above thirty words, no semicolon, no dash and no bold outside mathematics (computed).

Proofs given by pointer to a round file I did not re-derive this round. They are coupling (a)(iii) and (c)(ii), black-box (b) to (d), dataflow (a), (d), (e)(i) and (e)(iii), replay (c) to (e), and the results of the section Further accepted results. Their status rests on the verdicts of rounds 01 to 08 and on the source check of round 09. For black-box (b) I checked the constant independently. The adversary that picks the empirically best tree loses at most the mean of the largest estimation error over $\mathfrak T_{q_E}$, which is at most $\sqrt{2\ln\lvert\mathfrak T_{q_E}\rvert/n}$ and therefore below the stated $2\sqrt{\ln(2\lvert\mathfrak T_{q_E}\rvert)/n}$ (proven, sketch). I opened no outside source. The citations of Balle and Wang, Barthe et al., Gilbert and McMillan with its theorem numbers, Dong, Roth and Su, Mironov, Jia et al., Zhang et al., Jagielski et al., Steinke et al., and Kechris with its theorem number are unchecked by me.

## Findings

### ch-coupling-label-scope

Minor. Target, the Label of [thm-coupling-certificate] at line 131, "Proven, (a), (b), (c)(i), and (c)(ii) for finite views. Open, (c)(ii) for atomless views and the search for a seed map by oracle calls (open problem 8)."

The first sentence of (c)(ii), that a coupling through a seed map bounds $\mathrm H_\gamma(P_0\|P_1)$, holds for every view space by (F4), since the coupled pair has marginals $\Pi_{x_0}$ and $\Pi_{x_1}$ (proven). The Label assigns "open" to all of (c)(ii) for atomless views, so it labels a proven bound as open. The label claims less than is proven, so nothing false follows.

Smallest fix. "Proven, (a), (b), (c)(i), the bound of (c)(ii), and its exactness for finite views. Open, its exactness for atomless views and the search for a seed map by oracle calls (open problem 8)."

### ch-scalar-symbol-reuse

Minor. Target, [thm-replay-audit-steer] (d) at line 307, "the learning functions $\rho\mapsto\rho+a\bmod1$".

Line 189 introduces $a$ as the public scalar of [thm-dataflow-composition] (a). Line 307 uses $a$ again, for the offset of a rotation, without a quantifier. A reader holds two objects under one symbol.

Smallest fix. "the learning functions $\rho\mapsto\rho+a\bmod1$, one for each $a\in\mathbb R/\mathbb Z$,". The quantifier makes $a$ local to the sentence.

### ch-reading-eta-range

Minor. Target, the Reading of (e)(ii) of [thm-dataflow-composition] at line 187, "certifying below $1-(1+\gamma)e^{-B^2/(16\sigma^2)}$ at $\mathsf L^\circ$ with probability above $\alpha+\eta$ needs $N(2N-1)>\eta J_{\mathrm{cd}}$".

The symbol $\eta$ enters with no range. The claim is true for every $\eta\ge0$ (proven, from (e)(ii) and $(2J_{\mathrm{cd}}-1)\bar\Phi(B/(2\sigma))\le e^{-B^2/(16\sigma^2)}$). The approximation "about $\sqrt{\eta/2}\ldots$" that follows is meaningful only for $\eta>0$.

Smallest fix. "For $d\ge6$, $\eta\in(0,1)$ and $J_{\mathrm{cd}}=\ldots$".

### ch-intro-price-limit

Minor. Target, item 4 of the opening at line 16, "it needs $e^{(1-o(1))\mathfrak e}$ Train calls when $\mathfrak e/d\to0$".

The term $o(1)$ is with respect to $\mathfrak e\to\infty$, as in the corollary of [thm-bounded-deviation-transfer]. The item names only $\mathfrak e/d\to0$, which also holds along sequences with $\mathfrak e$ bounded, where the expression says nothing. The lower half of the corollary needs no condition on $R$, so the item is otherwise faithful (proven, from (d) and the expansion in its proof).

Smallest fix. "it needs $e^{(1-o(1))\mathfrak e}$ Train calls as $\mathfrak e\to\infty$ with $\mathfrak e/d\to0$".

### ch-closed-form-memory

Minor. Target, (F6)(i) at line 96, "(Balle and Wang, ICML 2018, from memory)".

The closed form is the one numerical tool of the Reading of [thm-bounded-deviation-transfer], and its only support in the document is a citation marked "from memory". It has a one-line proof (proven). The likelihood ratio of $\mathcal N(0,1)$ to $\mathcal N(r,1)$ at $y$ is $\exp(r^2/2-ry)$. It exceeds $e^\varepsilon$ exactly when $y<r/2-\varepsilon/r$, and that set attains the supremum in $\mathrm H_{e^\varepsilon}$.

Smallest fix. Replace the parenthesis by "(the likelihood ratio of $\mathcal N(0,1)$ to $\mathcal N(r,1)$ exceeds $e^\varepsilon$ exactly where $y<r/2-\varepsilon/r$)". The citation may follow it once someone checks it.

### ch-replay-completeness-term

Minor. Target, [thm-replay-audit-steer] (d) at line 307 and the paragraph "Without the oracle" at line 313, "A drawn-seed auditor complete up to $\lambda'$".

The phrase "complete up to $\lambda'$" is not defined in the document. Part (b) defines completeness only through the acceptance probability of the honest prover.

Smallest fix, in both places. "A drawn-seed auditor that accepts the honest prover with probability at least $1-\lambda'$ against each of them".

### ch-dataset-node-before-use

Minor. Target, [def-isolated-client] at line 72, "Let $G$ be a procedure in which client $j$ owns the input node of $D_j$."

The symbol $D_j$ appears before any sentence introduces it. Only line 79, "Under $H_b$, $D_j=D^b_j$", fixes its value. The definition is well posed, since the node is identified by its owner and the hypotheses fix its value.

Smallest fix. "Let $G$ be a procedure in which client $j$ owns the input node that holds its dataset $D_j$."

## Assessment

The document defines a learning oracle that runs an arbitrary learning function and names the seed, so that a caller can rerun training on a neighbouring dataset with the same seed. On that model it proves bounds that depend on the learning function only through quantities that such coupled reruns estimate. The proven core is this. One training node leaks at most the coupled divergence (thm-coupling-certificate (b)). Gaussian releases of a client with state compose, against every strategy, to a Gaussian term plus the probability that coupled updates differ by more than a threshold (thm-dataflow-composition (b)). A coalition that deviates by at most $B_A$ in its additive inputs inflates that probability by at most a function set by $\mathfrak e=(R-1)B_A^2/(2\sigma^2)$, tight up to a factor $e\sqrt{8\ln(1/p)}$. In the clipped aggregation instance every certifier sound for all learning functions and accurate where the leakage is zero pays $e^{(1-o(1))\mathfrak e}$ Train calls (thm-bounded-deviation-transfer). Replay audits with seeds from a random oracle bound steering by the reach of the target (thm-replay-audit-steer). The needle lemma bounds the Train calls of every certifier (lem-needle-lower-bound). Drawn-seed certifiers cannot certify below one through a deterministic channel with atomless views, and with clipping they pay Train calls exponential in the smaller of $d$ and $B^2/\sigma^2$ (coupling (a)(iii), dataflow (e)). These are worst-case statements over all learning functions, proven.

The limits are as follows. A certificate is useful only when coupled reruns of the actual training pipeline rarely differ by more than the threshold. The document measures nothing, so whether this holds for a transformer trained with a shared seed is empirical and open. Fidelity of hardware randomness is a modelling assumption, heuristic on GPUs, and the atomless seed is an idealization proven harmless only for thm-reference-access (c) (open problem 9). The ciphertext reduction for threshold CKKS is heuristic (open problem 6). The guarantees concern a fixed pair of datasets, with record-level forms only by pointer. Several proofs exist only in round files, which the document names. Novelty against the auditing literature is open, as the section Prior work states. To check the core, read the proof of thm-dataflow-composition (b), steps 3 to 5 at lines 213 to 221, then step 3 of the proof of thm-bounded-deviation-transfer (a) at line 269. The first replaces the clipped update by a hybrid that differs from the real run only on the exceedance event. The second bounds the Rényi moment of the deviation one release at a time.

## Verdicts

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
FINAL ACCEPT
```
