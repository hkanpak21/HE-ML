# Round 10, challenger

Verdict of this turn. The text now in `final/learning-oracle-theory.md` closes all six challenges of round 09, and the three variants of the builder are correct (proven, arguments below). The level "in $(0,1)$" is needed. At level zero the upper half of the active-choice paragraph is false, and the wording "below one" of round-09/challenger.md admitted that level. The six definitions are accepted for the seventh consecutive round. This review raises no new challenge. All 21 items stand at ACCEPT, eight of them NONTRIVIAL, and BLOCKING is 0. The audit of the final document is `final/audit.md`.

Every non-trivial claim carries one of the labels proven, heuristic, empirical or open. "Computed" marks arithmetic or a mechanical check done this round. Line numbers refer to `final/learning-oracle-theory.md` and `theory/CURRENT.md` after round 10. I opened no outside source. The working folder is not under version control, so I could not diff the final document against its round-09 state. I compared each edited sentence with its instruction, and for the audit I read the whole document again.

## Status of the round-09 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-seed-map-channel | blocking | closed, with the split sentence | none |
| ch-per-round-threshold | blocking | closed | none |
| ch-active-choice-conditions | blocking | closed, with the level in $(0,1)$ | none |
| ch-scalar-label | blocking | closed, with the scalar $a$ named | none |
| ch-estimator-alpha-range | not blocking | closed | none |
| ch-closed-form-domain | not blocking | closed | none |

### ch-seed-map-channel

Line 129 now reads "(ii) A coupling through a seed map $\psi$ with $\psi_*\mu=\mu$ also bounds $\mathrm H_\gamma(P_0\|P_1)$. Some $\psi$ makes it exact for $\mathrm{TV}$ under deterministic kernels through a deterministic channel with a finite view." The variant turns ", and" into a full stop. The pronoun "it" names the coupling through a seed map, the only coupling in the first sentence, so the meaning is unchanged.

Both sentences are true as written (proven). First sentence. For measurable $\psi$ with $\psi_*\mu=\mu$, the pair $(\mathsf L(x_0;\rho,\xi_0),\mathsf L(x_1;\psi(\rho),\xi_1))$ has marginals $\Pi_{x_0}$ and $\Pi_{x_1}$, so (F4) bounds $\mathrm H_\gamma(P_0\|P_1)$ by its mean divergence, for every channel. Second sentence. With $\Xi$ a point, a deterministic channel $\kappa$ and finite $\mathcal V$, let $A^b_v=\{\rho:\kappa(\mathsf L(x_b;\rho))=v\}$, of mass $P_b(v)$. By (F9), subsets of equal mass of an atomless standard space are isomorphic modulo null sets. So some $\psi$ with $\psi_*\mu=\mu$ maps a subset of $A^0_v$ of mass $\min\{P_0(v),P_1(v)\}$ into $A^1_v$ for every $v$, and the rest onto the rest. Then $\Pr[\kappa(W^\Gamma_0)\neq\kappa(\mathsf L(x_1;\psi(\rho)))]\le1-\sum_v\min\{P_0(v),P_1(v)\}=\mathrm{TV}(P_0,P_1)$, and the first sentence gives the reverse inequality. Both counterexamples of round 09 use a channel that is not deterministic, so they lie outside the new hypothesis. Open problem 8 at line 352 now carries "with a deterministic channel and atomless views", so the label open applies to a question that the counterexample does not settle. The Label line, "(c)(ii) for finite views", needs no change for this challenge. Closed.

### ch-per-round-threshold

Line 181 now defines $\epsilon_b$ for thresholds per round as the probability that some round $t$ has $\Vert f_t(c_t,W'_t)-f_t(c_t,W_t)\Vert>\Delta_t$. Step 5 at line 221 now clips round $t$ at $\Delta_t$ in the hybrid, reads the exceedance of round $t$ at $\Delta_t$ in step 3, and uses $\mathcal N((\Delta_t/\sigma)_t,I_R)$ in step 4. The round-09 counterexample no longer applies (proven). There $R=1$, the coupled difference is $\mathbf e_1$ at every seed, and at $\Delta_1=s<1$ the new $\epsilon_0$ equals one, so the bound holds.

The proof holds with the three changes (proven). Step 3 is unchanged once $t^\star$ is the first round with $\Vert F^1_t-F^0_t\Vert>\Delta_t$. In step 4 coordinate $t$ of the kernel uses (F6)(ii) with $r=\Delta_t/\sigma$, so the kernel maps $\mathcal N(0,I_R)$ to $\mathcal L_{\mathrm{hyb}}$ and $\mathcal N((\Delta_t/\sigma)_t,I_R)$ to $\mathcal L_1$. Then (F6)(i) gives $\delta_{\mathcal N}(\varepsilon;(\sum_t\Delta_t^2)^{1/2}/\sigma)$. The sum bound in the same paragraph of (b) keeps one threshold, and it says so by its argument $\Delta$. Closed.

### ch-active-choice-conditions

Line 335 now reads "Let the coalition pick choices from admissible sets. Let a certifier be sound for every learning function and accurate where the leakage is zero, to a fixed level in $(0,1)$, at error probabilities summing below one." I judged the variant against round-03/builder.md, lines 268 to 325, which I read this round.

The builder's level-zero argument holds (proven). For $r>0$ and $\varepsilon\ge0$ the half line $y<r/2-\varepsilon/r$ has positive mass under $\mathcal N(0,1)$, and on it the density of $\mathcal N(0,1)$ exceeds $e^\varepsilon$ times that of $\mathcal N(r,1)$. So $\delta_{\mathcal N}(\varepsilon;r)>0$. The certificates (b)(i) and (b)(ii) of round 03 output at least $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$ with $\Delta>0$, so none is accurate at level zero, and the sentence "Coupled certificates achieve this up to a logarithmic factor" fails there. The wording "below one" of my predecessor therefore needed the lower end.

At every level $\ell\in(0,1)$ both halves hold (proven). Lower half. Take $\eta\in(0,1-\ell)$. An output at most $\ell<1-\eta$ with probability at least $1-\alpha'$ meets (c)(i) and (c)(ii) of round 03 only with $N\ge(1-\alpha-\alpha')\lvert\mathcal C_\cup\rvert$ and $N\ge(1-\alpha-\alpha')\prod_t\lvert\mathcal C_t\rvert$. With an infinite set, (c)(iii) gives $\Pr[\hat t\le\ell]\le\alpha<1-\alpha'$. Upper half. $\delta_{\mathcal N}(\varepsilon;r)$ tends to zero as $r$ decreases to zero. For $\varepsilon>0$ both terms of the closed form vanish, since $r/2-\varepsilon/r\to-\infty$. For $\varepsilon=0$ the value is $2\Phi(r/2)-1$. So some $\Delta>0$ has $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)<\ell$. With $\epsilon_{\mathrm{acc}}=\ell-\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$, certificate (b)(i) outputs at most $\ell$ at the reference function with certainty from $2\lvert\mathcal C_\cup\rvert\lceil R\ln(K/\alpha)/\epsilon_{\mathrm{acc}}\rceil$ Train calls, where $K=\sum_t\lvert\mathcal C_t\rvert\le R\lvert\mathcal C_\cup\rvert$. Certificate (b)(ii) does so from $2\lvert\mathbb T\rvert\lceil\ln(1/\alpha)/\epsilon_{\mathrm{acc}}\rceil$, with $\lvert\mathbb T\rvert\le2\prod_t\lvert\mathcal C_t\rvert$ when every set has two or more elements. At fixed $R$, $\alpha$, $\alpha'$ and $\ell$, the stateless ratio to the lower bound is of order $\ln(K/\alpha)$, and the stateful ratio is a constant (computed from the two bounds). So "up to a logarithmic factor" holds.

The lower half alone also holds at level zero, since accuracy at level zero implies accuracy at every positive level. The variant restricts the paragraph only where its second half fails, which is the smallest correct restriction. Splitting the sentence changes no claim. The register line at `theory/CURRENT.md` line 170 carries the same clause. Closed.

### ch-scalar-label

Line 189 now names "a public scalar $a$" before its first use, cites round-04/builder.md and round-05/builder.md after the fourth sentence, and adds "These claims are proven given that decryption of $a$ times a ciphertext returns $a$ times its message plus an error of bounded norm and any noise the decryptors add. That form is heuristic for CKKS." The Label at line 191 reads "Heuristic, the realization by threshold CKKS and the form of its decryption under a public scalar."

The words "These claims" refer to the third and fourth sentences. The first two sentences of (a) carry their own labels in parentheses, and the new sentence follows the pointer of the fourth. The mathematics holds given the form (proven). When the decryptors add $Z$ at decryption, decryption of $a$ times the aggregate ciphertext returns $a\tilde u+e^{(a)}+Z$ with $\Vert e^{(a)}\Vert\le e_{\max}$, and division by $a$ leaves noise $(e^{(a)}+Z)/a$. When client $j$ adds $Z$ inside its ciphertext, decryption returns $a(\tilde u+Z)+e^{(a)}$, and division leaves $\tilde u+Z+e^{(a)}/a$, so the scalar removes at most the decryption error. The heuristic list now names the assumption that round-04/builder.md, line 281, and round-05/builder.md, line 213, label heuristic. The label no longer claims more than the source. The symbol $a$ reappears in [thm-replay-audit-steer] (d) as the offset of a rotation. The audit records this as minor (ch-scalar-symbol-reuse). Closed.

### ch-estimator-alpha-range

Line 189 now reads "(e)(iii) Over $\mathfrak L_B$ and for $\alpha\le1/2$, ...", the range the record proves. Open problem 2 of `theory/CURRENT.md`, line 182, states the same range. Open problem 4 cites (e)(iii) for $R=1$ and fixes no level, so it needs no change. The argument for $\alpha>1/2$ in round-09/challenger.md stays in the record and is not used. Closed.

### ch-closed-form-domain

Line 96 now attaches the closed form to $r>0$. Closed. The citation is still marked "from memory", although the closed form has a one-line proof. The audit proposes the proof as a minor fix (ch-closed-form-memory).

### Instruction 7 and the page count

The three mirrors are at `theory/CURRENT.md` lines 168, 170 and 182. The register gives the three revised items the status "proposed in round 10", as its own rule requires. Merging each "Statement." line into its first part changes no word. A mechanical pass over the final document, with each formula counted as one word, finds no sentence above thirty words, no semicolon, no dash and no bold outside mathematics (computed).

## Definitions

Seventh reading. In `theory/CURRENT.md` only the title and the register changed this round. The builder reports no change to the definition section of the final document. I could not diff, so I read each definition there again against `theory/CURRENT.md`.

### [def-learning-oracle]

Well posed. Names are per-caller counters, Train resolves a model name or a seed name before running $\mathsf L$, and fidelity fixes the joint law of every execution. ACCEPT.

### [def-learning-oracle-model]

Well posed. The final document states the computational case only as "bounds its running time". No theorem of the final document uses a computational assumption, so nothing depends on the omitted detail. ACCEPT.

### [def-degenerate-oracles]

Well posed. ACCEPT.

### [def-certifier]

Well posed. The remark on larger targets is proven in one line by $\theta\le\theta'\le\hat t$ on the soundness event. ACCEPT.

### [def-model-bank]

The final document gives a summary, and `theory/CURRENT.md` holds the full definition. Well posed there. ACCEPT.

### [def-isolated-client]

Well posed. The symbol $D_j$ appears in "owns the input node of $D_j$" one sentence before $H_b$ fixes its value. The audit records this as minor (ch-dataset-node-before-use). It does not make the definition ill-posed, since the node is named by its owner and $H_b$ fixes its value. ACCEPT.

Simplicity. The six definitions remain the smallest that carry the presented proofs. Each clause of def-isolated-client is used by step 1 of the proof of [thm-dataflow-composition] (b), and the remark of def-certifier carries [thm-bounded-deviation-transfer] (e) to $\theta^{\mathrm{agg}}_R$.

## New challenges

None. The audit in `final/audit.md` records seven minor findings on wording, labels and symbols. None makes a statement, a proof step or a definition false or ill-posed.

## Verdicts

Six definitions and fifteen results with slug tags in the final document. The three items that round 09 sent to REVISE now meet the four-part bar again, since their clauses restore true statements without changing the role of the oracle. [thm-coupling-certificate] has the oracle in (b), needs the law of the trained model without it by (a)(iii), depends on $\mathsf L$ only through $\beta_\gamma(K)$, and fails under drawn seeds by (a)(iii). [thm-dataflow-composition] does the same through $\epsilon_b(\Delta)$, with (e) for the drawn-seed failure. [thm-active-choice-dichotomy] keeps the oracle and the certificates that rounds 03 to 08 accepted as non-trivial, and the restored conditions change only the range of accuracy levels.

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
