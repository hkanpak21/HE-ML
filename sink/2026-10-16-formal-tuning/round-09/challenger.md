# Round 09, challenger

Verdict of this turn. The three challenges of round 08 are closed, and so is the builder's consequential clause "$\Upsilon_0(p)=p$ for $p\le1$" in part (a) of [thm-bounded-deviation-transfer] (proven). I checked all 51 entries of the builder's table against the round files they name, hypothesis by hypothesis. 45 entries match. Four of these differ from their source in a quantifier or a reading and still hold, as the builder says (proven). Six entries do not match, and four of the six are blocking. Part (c)(ii) of [thm-coupling-certificate] is false as written, and open problem 8 inherits the gap (ch-seed-map-channel). The sentence on thresholds per round in [thm-dataflow-composition] (b) is false on its literal reading (ch-per-round-threshold). The summary of [thm-active-choice-dichotomy] is false without its two conditions on accuracy (ch-active-choice-conditions). The scalar sentences of [thm-dataflow-composition] (a) carry the label proven for a step that their source labels heuristic (ch-scalar-label). The builder's table did not report this last one. Two findings are not blocking. Stated part (e)(iii) holds for every $\alpha\in(0,1)$ by an argument written below, while the record proves it only for $\alpha\le1/2$ (ch-estimator-alpha-range). The closed form in (F6)(i) is undefined at $r=0$ (ch-closed-form-domain). The six definitions are accepted for the sixth consecutive round. Every fix is one clause or one sentence, so round 10 can close all six. I drop the readability item of the round-08 plan, because moving the numbers of the criterion-4 paragraphs into the statements would change frozen statements.

Every non-trivial claim carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the argument is written here in full enough to check. "Computed" marks a number from arithmetic done this round. Line numbers of the final document refer to `final/learning-oracle-theory.md` as it stands after round 09. I opened no outside source.

## Status of the round-08 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-upsilon-domain | not blocking | closed, with the consequential clause in (a) | none |
| ch-passive-stop | not blocking | closed | none |
| ch-closing-clarity | not blocking | closed, all three items | none |

### ch-upsilon-domain

The setting at line 243 now ends with "$\Upsilon_{\mathfrak e}(p)=1$ for $p>1$". The extension is nondecreasing on $[0,\infty)$ (proven). On $(0,1]$ the map $p\mapsto(\sqrt{\ln(1/p)}-\sqrt{\mathfrak e})_+$ is nonincreasing, and $\Upsilon_{\mathfrak e}(1)=\exp(-(0-\sqrt{\mathfrak e})_+^2)=1$ for every $\mathfrak e\ge0$. I checked every argument of $\Upsilon_{\mathfrak e}$ in the final document. In (a) it is $\epsilon^{\mathrm{pr}}_b(\Delta)\in[0,1]$, in (b) $\bar\epsilon_b\in[0,1]$, in (c) $p<\bar\Phi(\sqrt{2\mathfrak e}+1)<1$, and in (e) $\ln(1/\alpha)/N'$, which may exceed one. In that case the bound of (e) is $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+1\ge1\ge\hat t_b$, so (e) holds for every $N'\ge1$ (proven).

The consequential clause is needed and correct. Without it, part (a) asserted $\Upsilon_0(p)=p$ for all $p$, false at $p>1$. With "for $p\le1$" it holds, since $\Upsilon_0(p)=\exp(-\ln(1/p))=p$ on $(0,1]$ and $\Upsilon_0(0)=0$ (proven). Step 4 of the proof of (a) works with $p\in(0,1]$ and the proof of (b) uses only monotonicity, so neither proof changes. The symbol table of `theory/CURRENT.md` carries the same three cases. Closed.

### ch-passive-stop

The remark at line 85 now ends with the two sentences I proposed. The reason it gives is the right one. The builder's proof that $\epsilon_b(\Delta)$ is the same for every passive adversary under the convention (round-09/builder.md, line 33) holds (proven). The convention sits in a remark, and the final document says that a remark is not part of a definition. That placement is harmless. No theorem of the final document needs the convention, since a stop only lowers the exceedance by the proof of [thm-dataflow-composition] (c), and every certificate bounds the strategy that never stops. Only the equality in the remark itself needs it, and the remark states it. Closed.

### ch-closing-clarity

Item 1. Open problem 2 of `theory/CURRENT.md` now names a certifier sound at level $\alpha$. With soundness the count is (e)(ii) read through the Reading (proven, round-08/challenger.md, line 40). Item 2. Stated part (e)(iii) at line 195 says "drawn-seed Train calls". Item 3. The criterion-4 paragraph at line 267 now has the drawn-seed certifier as its subject. I re-derived the builder's proof of item 3 (round-09/builder.md, line 47) and it holds (proven). Under $\alpha+\eta<1$ and $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<1-(1+\gamma)e^{-B^2/(16\sigma^2)}$, a drawn-seed certifier with $N(2N-1)<\eta J_{\mathrm{cd}}$ outputs at most that accuracy level with probability below $\alpha+\eta<1$, while (b) does so with certainty. The instance "$B_A=0$, large $d$ and $B/\sigma$, $\epsilon_{\mathrm{acc}}<1$ and small $\sqrt R\Delta/\sigma$" satisfies both conditions, and $B_A=0$ is one instance and not needed. Closed.

## The frozen statements

Method. For each entry I opened the round file at the lines that the builder names and compared hypotheses, quantifiers, constants and label with the sentence in the final document. The column "Accepted" names the challenger round whose verdict block accepted the source item, read this round from the verdict blocks of round-01/challenger.md to round-08/challenger.md. The column "Result" is one of match, match on both readings, or the slug of a challenge below.

### Parts of statements proven in round files

| No. | Item | Source read | Accepted | Result |
| --- | --- | --- | --- | --- |
| 1 | coupling (a)(ii) | round-01 lines 190 to 194, proof line 214, round-02 line 396 | 01, 02 | match. $k=\lvert\mathcal V\rvert$, $n$ per input, McDiarmid constant $2/n$ |
| 2 | coupling (a)(iii) | round-01 lines 112, 118, 164 | 01 | match |
| 3 | coupling (c)(ii) | round-01 line 208, proof line 246 | 01 | ch-seed-map-channel, false |
| 4 | black-box (b) | round-02 line 346, round-01 line 380 | 02 | match. "Within" is two-sided by (o) |
| 5 | black-box (c) | round-02 line 348, round-01 line 382 | 02 | match on both readings, see below |
| 6 | black-box (d) | round-02 lines 350 to 354, round-01 line 384 | 02 | match |
| 7 | dataflow (a), first sentence | round-03 lines 153 to 157, 181 to 185, round-04 lines 259, 265 | 03, 04 | match |
| 8 | dataflow (a), CKKS | round-03 line 179, round-04 line 265 | 04 | match, heuristic |
| 9 | dataflow (a), scalar | round-04 lines 267 to 281, round-05 lines 28, 213, round-06 line 11 | 04, 05, 06 | ch-scalar-label, label claims more than the source |
| 10 | dataflow (b), thresholds per round | round-03 lines 171, 227, round-04 line 263 | 03, 04 | ch-per-round-threshold, false on its literal reading |
| 11 | dataflow (c), DKW | round-02 lines 141 to 145, 225, round-03 line 231 | 02, 03 | match |
| 12 | dataflow (d) | round-02 lines 147 to 151, 227 to 229, round-03 lines 175, 233 | 02, 03 | match. The reference function does not depend on $\eta$ |
| 13 | dataflow (e)(i) | round-02 lines 155, 231 to 237 | 02 | match |
| 14 | dataflow (e)(iii) | round-02 lines 163 to 171, 241 to 251 | 02 | ch-estimator-alpha-range, true, record covers $\alpha\le1/2$ |
| 15 | replay (c), attack | round-02 lines 290 to 292, 306 to 310 | 02 | match |
| 16 | replay (c), match | round-03 lines 422 to 424 | 03 | match. $2/(1-e^{-1})=3.164$ |
| 17 | replay (d) | round-02 lines 294, 314 to 318 | 02 | match on both readings, see below |
| 18 | replay (e) | round-02 lines 296 to 298, 320 to 322, round-03 line 420, round-04 line 361 | 02, 03, 04 | match on both readings, see below |
| 19 | perfect substitution | round-01 lines 260 to 282, round-02 line 428 | 01, 02 | match. The second sentence is part (b) |
| 20 | reference access, first sentence | round-01 lines 294 to 298, 306 | 01 | match |
| 21 | reference access, second sentence | round-02 lines 374 to 390 | 02 | match |
| 22 | atomless two-point | round-01 lines 112 to 164, round-02 line 410 | 01, 02 | match |
| 23 | bank fidelity | round-01 lines 332 to 336, round-02 line 432 | 01, 02 | match |
| 24 | bank soundness | round-01 lines 402 to 418, round-02 line 422, round-03 lines 358, 438, round-04 line 357 | 01 to 05 | match on both readings, see below |
| 25 | active-choice dichotomy | round-03 lines 275 to 290, 304 to 322, round-04 line 319 | 03, 04 | ch-active-choice-conditions, false |
| 26 | record-level certificate | round-03 lines 350 to 354, 372 to 376 | 03 | match. Cost $N(R(1+m)+n_G)$ |
| 27 | smoothed choice, first sentence | round-04 lines 132, 150, 205, round-05 lines 203 to 205 | 04, 05 | match. $\lvert\mathrm{Net}_t\rvert\le(1+2\varrho_t/(\lambda\sigma\sqrt{2\pi}))^d$ |
| 28 | smoothed choice, second sentence | round-04/challenger.md line 95, round-05/challenger.md line 147 | 04, 05 | match, heuristic |

### Results stated outside a statement

| No. | Item | Source read | Accepted | Result |
| --- | --- | --- | --- | --- |
| 29 | def-degenerate-oracles, remark | entry 19 | 01, 02 | match |
| 30 | def-isolated-client, remark | round-02 line 111, round-03 line 231, round-08 lines 11 to 25 | 08 | match |
| 31 | dataflow, Reading of (e)(ii) | final proof of (e)(ii), round-04 line 287, round-08/challenger.md lines 40 to 42 | 08 | match. "Certifying" carries soundness |
| 32 | dataflow, degenerate oracles | round-02 lines 135, 211, round-03 line 229 | 02, 03 | match |
| 33 | transfer, Reading | round-06 line 85 | 06 | match. $\delta_{\mathcal N}(1;1)=0.1269$ |
| 34 | transfer, degenerate oracles | parts (b), (e), round-07 lines 22 to 28, round-08 lines 41 to 43 | 07, 08 | match |
| 35 | replay, degenerate oracles | round-02 line 326 | 02 | match |
| 36 | open problem 5, known part | round-06 lines 67 to 71, round-05 lines 20, 191 | 06 | match |
| 37 | open problem 5, heuristic part | round-06 lines 45 to 71, round-07 line 82 | 06, 07 | match, heuristic |

### Standing facts

| No. | Item | Source read | Accepted | Result |
| --- | --- | --- | --- | --- |
| 38 | (F2) | round-01 line 104 | 01 | match |
| 39 | (F5) | round-01 lines 226 to 234, round-03 line 98 | 01, 03 | match |
| 40 | (F6)(i) | round-01 line 242 | 01 | ch-closed-form-domain, undefined at $r=0$ |
| 41 | (F6)(ii) | round-02 line 78 | 02 | match, rechecked by direct computation |
| 42 | (F6)(iii) | round-02 line 78 | 02 | match |
| 43 | (F6)(iv) | round-03 line 102 | 03 | match |
| 44 | (F6)(v) | round-02 line 78 | 02 | match |
| 45 | (F8), second sentence | round-01 line 240 | 01 | match. $1-e^{-x}\le x$ |

### Opening items

| No. | Item | Source read | Accepted | Result |
| --- | --- | --- | --- | --- |
| 46 | item 1 | coupling (a)(iii), (b) | 01, 02 | match |
| 47 | item 2 | black-box (o), (a), (c) | 02 | match |
| 48 | item 3 | dataflow (b), (c) | 08 | match |
| 49 | item 4 | transfer (a), (b), corollary, round-07 line 42 | 05 to 08 | match. $\ln(1/\alpha)\exp((\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2)=e^{(1+o(1))\mathfrak e}\ln(1/\alpha)$ at fixed $\epsilon_{\mathrm{acc}}$ |
| 50 | item 5 | replay (a), entry 16 | 02, 03 | match |
| 51 | item 6 | lem-needle-lower-bound | 03 | match |

Count. 45 entries match, among them entries 5, 17, 18 and 24 on both readings. Entries 3, 9, 10, 14, 25 and 40 do not match. Every source item was accepted by the challenger of its round, and black-box certifiability, revised in round 02 after the REVISE of round 01, was accepted from round 02 on.

### The four entries that hold on both readings

Entry 5, black-box (c). The source fixes $N$ Train calls, and the final sentence fixes none. The builder's truncation argument holds (proven). Let $P_n$ run the procedure and reject at its call $n+1$. On one probability space $P_n$ accepts only where the procedure accepts, so $P_n$ also rejects every false claim except with probability $\alpha$. The source applies to $P_n$ and gives $\Pr[P_n\text{ accepts}]\le\alpha$. The acceptance event of the procedure is the increasing union over $n$ of the acceptance events of $P_n$, so its probability is at most $\alpha$. The clause "$<1$" sits inside the claim in the final sentence. If it is read as part of the claim, then at a learning function with $\mathrm{Adv}^{\mathrm{bb}}(Q)+\lambda\ge1$ the claim is false and the hypothesis bounds acceptance by $\alpha$. If it is read as a condition, the source covers that case. The sentence holds on both readings (proven).

Entry 17, replay (d). With $w(t)=\int_0^1\mathrm{acc}(t,\rho)\,d\rho$ and $\int_0^1w\ge1-\lambda'$, some $t$ has $w(t)\ge1-\lambda'$ (proven). Otherwise $\{w<1-\lambda'\}$ is the whole circle, some set $\{w\le1-\lambda'-1/k\}$ has positive measure, and the integral falls below $1-\lambda'$. So the stronger reading "some fixed point, for every $\lambda>0$" holds.

Entry 18, replay (e). $\mathbb E_U\,p_\tau(T;\mathsf L_U)=p_\tau(T;\mathsf L)$ by round-02/builder.md, line 296, so both readings of $p_\tau(T)$ give one bound (proven).

Entry 24, bank soundness. The pointer of round-03/builder.md, line 438, is [thm-record-level-certificate] (c)(ii), for records added to the fixed dataset of the bank. Part (c)(i) at line 358 gives the same linear lower bound for records removed from a fixed dataset, which is the reading of "every record of a fixed dataset" (proven, by the statement at line 358 and its proof at line 400).

### A record correction

Finding 4 of the builder says that round-02/builder.md, line 251, states the count of (e)(iii) for $\alpha\le1/2$. It does not. Line 251 writes $n=O((1+\gamma)^2e^{B^2/\sigma^2}\ln(1/\alpha)/\epsilon_{\mathrm{acc}}^2)$ with no range. Only the derivation from the margin of line 169, written by the builder this round, needs $\alpha\le1/2$. ch-estimator-alpha-range settles the range.

## Definitions

Sixth reading. No definition changed this round, in either file. Only the remark of [def-isolated-client] changed, and a remark is not part of a definition.

### [def-learning-oracle]

Unchanged. Well posed. ACCEPT.

### [def-learning-oracle-model]

Unchanged. Well posed. ACCEPT. The convention that a passive strategy takes the protocol's stop lives in the remark of def-isolated-client. Placing it in the definition of a passive strategy would be cleaner, but no theorem needs it (see ch-passive-stop above), so I do not ask for it.

### [def-degenerate-oracles]

Unchanged. Well posed. ACCEPT.

### [def-certifier]

Unchanged. Well posed. ACCEPT.

### [def-model-bank]

Unchanged. Well posed. ACCEPT.

### [def-isolated-client]

Unchanged. Well posed. ACCEPT. The exceedance probability is defined for one threshold $\Delta$. ch-per-round-threshold defines the form for thresholds per round inside the theorem that uses it, so the definition stays as it is.

Simplicity. The six definitions remain the smallest that carry the presented proofs.

## New challenges

### ch-seed-map-channel

BLOCKING. Target, part (c)(ii) of [thm-coupling-certificate] at line 131, and open problem 8 at line 362.

The sentence reads "some $\psi$ makes it exact for $\mathrm{TV}$ under deterministic kernels with a finite view". The setting allows any channel $K$. The source, round-01/builder.md, line 208, states the exact case "with a deterministic channel $\kappa$ and a finite view space". The sentence is false as written (proven, by counterexample). Let $\Xi$ be a point, identify $(\mathcal R,\mu)$ with $[0,1)$ by (F9), and let $a,b,c$ be three distinct models. Let $\mathsf L(x_0;\rho)=a$, $\mathsf L(x_1;\rho)=b$ for $\rho<1/2$ and $\mathsf L(x_1;\rho)=c$ otherwise. Let $\mathcal V=\{1,2\}$, $K(\cdot\mid a)$ uniform, $K(\cdot\mid b)=\delta_1$ and $K(\cdot\mid c)=\delta_2$. Then $P_0$ and $P_1$ are uniform and $\mathrm{TV}(P_0,P_1)=0$. For every measurable $\psi$ with $\psi_*\mu=\mu$ the coupled bound is $\mathbb E\,\mathrm{TV}(K(\cdot\mid a),K(\cdot\mid\mathsf L(x_1;\psi(\rho))))=1/2$, since a uniform law on two points is at distance $1/2$ from each point mass. No seed map makes it exact.

Open problem 8 asks, "Under deterministic kernels with atomless views, does some seed map make the coupling of thm-coupling-certificate (c)(ii) exact for $\mathrm{TV}(P_0,P_1)$ in the limit?" Without the deterministic channel the answer is no (proven, by counterexample), so the label open on it is false. Let $\mathcal M=[0,1)\cup\{a\}$, $\mathsf L(x_0;\rho)=a$, $\mathsf L(x_1;\rho)=\rho$, $K(\cdot\mid a)$ uniform on $[0,1)$ and $K(\cdot\mid m)=\delta_m$ for $m\in[0,1)$. Both view laws are uniform and atomless, so $\mathrm{TV}(P_0,P_1)=0$. Every coupled term is $\mathrm{TV}(\mathrm{Unif},\delta_m)=1$, so every seed map gives one. `theory/CURRENT.md` states open problem 8 with "a deterministic channel $\kappa$", so only the final document carries the gap.

Smallest fix. In (c)(ii), "under deterministic kernels through a deterministic channel with a finite view". In open problem 8, "Under deterministic kernels, with a deterministic channel and atomless views, does some seed map ...". The Label line of the theorem needs no change once (c)(ii) carries the channel.

### ch-per-round-threshold

BLOCKING. Target, the sentence "With a threshold $\Delta_t$ per round, $\sqrt R\Delta$ becomes $(\sum_t\Delta_t^2)^{1/2}$" in part (b) of [thm-dataflow-composition] at line 187, and the sentence on thresholds per round in step 5 of its proof at line 227.

The sources read "With a threshold $\Delta_t$ per round and the exceedance read round by round" (round-03/builder.md, line 171, and round-04/builder.md, line 263). The final sentence drops the second clause. def-isolated-client defines $\epsilon_b(\Delta)$ for one threshold only, so the literal reading keeps $\epsilon_b(\Delta)$ at the free threshold $\Delta$ of the display. On that reading the sentence is false (proven, by counterexample). Take $R=1$, deterministic kernels, $O_1=0$, a fixed choice $c$, $\mathcal M=\mathbb R^d$, $f_1(c,m)=m$, $\mathsf L(x(c,D^0_j);\rho)=0$ and $\mathsf L(x(c,D^1_j);\rho)=\mathbf e_1$. The passive adversary that reads $y_1$ has $\mathrm H_\gamma(P_0\Vert P_1)=\delta_{\mathcal N}(\varepsilon;1/\sigma)>0$. With $\Delta=2$, $D^\star_0=1$ at every seed, so $\epsilon_0(2)=0$. With $\Delta_1=s$ the literal bound is $\delta_{\mathcal N}(\varepsilon;s/\sigma)\le2\Phi(s/(2\sigma))-1$, which tends to zero as $s\to0$. On the source's reading $\epsilon_0$ is read at $\Delta_1=s<1$, equals one, and the bound holds. The proof in the final document covers only the kernel. Step 3 and the hybrid also need the threshold of round $t$.

Smallest fix. In (b), "With a threshold $\Delta_t$ per round, and $\epsilon_b$ the probability that some round $t$ has $\Vert f_t(c_t,W'_t)-f_t(c_t,W_t)\Vert>\Delta_t$, $\sqrt R\Delta$ becomes $(\sum_t\Delta_t^2)^{1/2}$." In step 5, "For thresholds per round, the hybrid clips round $t$ at $\Delta_t$, step 3 reads the exceedance of round $t$ at $\Delta_t$, and step 4 uses $\mathcal N((\Delta_t/\sigma)_t,I_R)$." With both, the statement is round-03/builder.md, line 171, and the proof is its line 227 (proven).

### ch-active-choice-conditions

BLOCKING. Target, the paragraph on [thm-active-choice-dichotomy] at line 345.

The paragraph reads "let a certifier be sound for every learning function and accurate where the leakage is zero. In some procedure it then needs Train calls linear in the number of distinct choices, or of choice sequences with state." The source lower bound is $(1-\alpha-\alpha')\lvert\mathcal C_\cup\rvert$ under the condition $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)+\epsilon_{\mathrm{acc}}<1-\eta$ (round-03/builder.md, lines 285 to 290). The paragraph drops both conditions, and without either it is false (proven, by two counterexamples, both with zero Train calls in every procedure). First, the builder's certifier outputs one with probability $1-\alpha$ and the accuracy level otherwise. It is sound at level $\alpha$ for every target and accurate with probability $\alpha$, which meets accuracy at level $\alpha'$ whenever $\alpha+\alpha'\ge1$. Second, at an accuracy level of one or more the certifier that always outputs one is sound and accurate. The same omission makes "No number suffices for an infinite set" false, since (c)(iii) gives $\Pr[\hat t\ge1-\eta]\ge1-\alpha$, which excludes accuracy only when $\alpha+\alpha'<1$. The upper half, "Coupled certificates achieve this up to a logarithmic factor", needs the accuracy level above the Gaussian term, which a certifier meets by its choice of $\Delta$, so a level in $(0,1)$ suffices for both halves (proven, by (b)(i) and (b)(ii) of round-03/builder.md with $\Delta$ chosen so that $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$ lies below the level). The register line in `theory/CURRENT.md` has the same omission.

Smallest fix. "... and let a certifier be sound for every learning function and accurate where the leakage is zero, to a fixed level below one, at error probabilities summing below one." The words follow opening item 4.

### ch-scalar-label

BLOCKING. Target, the third and fourth sentences of "The other parts, stated" at line 195, and the Label at line 197, of [thm-dataflow-composition].

The sentences read "Unchecked decryption lets a public scalar divide the protecting noise when the decryptors add it at decryption. Noise that client $j$ adds inside its ciphertext scales with the update, and the scalar then removes at most the decryption error (proven, round-04/builder.md and round-05/builder.md)." The source proves (a)(iii) for a coalition that obtains $y^{(a)}=a\tilde u+e^{(a)}+Z_1$ with $\Vert e^{(a)}\Vert\le e_{\max}$ (round-04/builder.md, lines 267 to 279). That unchecked threshold CKKS decryption gives this form, and only while $a\,\mathrm{scale}\,\Vert\tilde u\Vert_\infty$ stays below about $q_\ell/2$, is labelled heuristic there, "a statement about the scheme" (round-04/builder.md, line 281, and round-05/builder.md, line 213). The final sentences assert the property of decryption itself with the label proven, and the Label line lists as heuristic only "the realization by threshold CKKS", which is a different assumption. So the label claims more than the source proves. The mathematics of both sentences is right given the form (proven, by (ii) of round-04 and its variant with $aZ_1$ in round-05).

Smallest fix. Replace "(proven, round-04/builder.md and round-05/builder.md)." by "(proven given that decryption of $a$ times a ciphertext returns $a$ times its message plus an error of bounded norm and any noise the decryptors add, which is heuristic for CKKS, round-04/builder.md and round-05/builder.md)." In the Label, replace "Heuristic, the realization by threshold CKKS." by "Heuristic, the realization by threshold CKKS and the form of its decryption under a public scalar."

### ch-estimator-alpha-range

Not blocking. Target, stated part (e)(iii) of [thm-dataflow-composition] at line 195, "$O(e^{B^2/\sigma^2}\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha))$ drawn-seed Train calls reach accuracy $\epsilon_{\mathrm{acc}}$ in every dimension, at fixed $\gamma$".

The record proves this only for $\alpha\le1/2$. The margin of round-02/builder.md, line 169, gives accuracy with $n\ge8(1+\gamma)^2(\kappa_B+2\ln(2/\alpha))/\epsilon_{\mathrm{acc}}^2$ draws per input, where $\kappa_B=e^{B^2/\sigma^2}$, and the factor $\ln(1/\alpha)$ absorbs the constant only when $\ln(1/\alpha)\ge\ln2$. The sentence is nonetheless true for every $\alpha\in(0,1)$, with the constant $C=450(1+\gamma)^2$ (proven, sketch). Write $p=1-\alpha$ and let $\mathcal G=\{0,\epsilon_{\mathrm{acc}},2\epsilon_{\mathrm{acc}},\dots\}\cap[0,1]$ together with the point $1$. Every interval $[\theta,\theta+\epsilon_{\mathrm{acc}}]$ with $\theta\in[0,1]$ contains a point of $\mathcal G$, and an output in that interval is sound.

1. Case $\alpha\le1/2$. The record. With $\ln(2/\alpha)\le2\ln(1/\alpha)$ and $1\le\ln(1/\alpha)/\ln2$ the count is at most $90(1+\gamma)^2\kappa_B\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha)$ (computed).
2. Case $1/2<\alpha\le7/8$. Run (e)(iii) at level $1/2$ with $n=\lceil29(1+\gamma)^2\kappa_B/\epsilon_{\mathrm{acc}}^2\rceil$ per input. The margin is at most $(1+\gamma)(1+\sqrt{2\ln4})\sqrt{\kappa_B/n}\le0.495\,\epsilon_{\mathrm{acc}}$, so the output lies in $[\theta,\theta+\epsilon_{\mathrm{acc}}]$ with probability at least $1/2\ge1-\alpha$. The count $2n\le60(1+\gamma)^2\kappa_B/\epsilon_{\mathrm{acc}}^2$ is at most $C\kappa_B\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha)$, since $\ln(8/7)=0.1335$ (computed).
3. Case $\alpha>7/8$, so $p<1/8$ and $\ln(1/\alpha)\ge p$. If $C\kappa_B\epsilon_{\mathrm{acc}}^{-2}p<2$, make no call and output a uniform point of $\mathcal G$, which has at most $3/\epsilon_{\mathrm{acc}}$ points. It succeeds with probability at least $\epsilon_{\mathrm{acc}}/3>2\epsilon_{\mathrm{acc}}^2/(C\kappa_B)>p$. Otherwise take $n=\lfloor C\kappa_B\epsilon_{\mathrm{acc}}^{-2}p/2\rfloor\ge1$ per input. With probability at least $1/2$ the estimate $\hat\theta$ of (e)(iii) has $\lvert\hat\theta-\theta\rvert\le\mathfrak m$ with $\mathfrak m\le0.26\,\epsilon_{\mathrm{acc}}/\sqrt p$. Output a uniform point of $\mathcal G\cap[\hat\theta-\mathfrak m,\hat\theta+\mathfrak m+\epsilon_{\mathrm{acc}}]$, a set of at most $2\mathfrak m/\epsilon_{\mathrm{acc}}+2\le1.23/\sqrt p$ points. The output lies in $[\theta,\theta+\epsilon_{\mathrm{acc}}]$ with probability at least $0.40\sqrt p\ge p$, and the count is at most $C\kappa_B\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha)$ (computed).

So the sentence is not false. It states more than the record proves, and the argument above is the only proof of the range $\alpha>1/2$. Open problem 2 of `theory/CURRENT.md` repeats the count without a range.

Smallest fix. "(e)(iii) Over $\mathfrak L_B$ and for $\alpha\le1/2$, $O(e^{B^2/\sigma^2}\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha))$ drawn-seed Train calls ...". The alternative, keeping the sentence and pointing to this file for $\alpha>1/2$, adds a proof by reference and is not the smaller change.

### ch-closed-form-domain

Not blocking. Target, (F6)(i) at line 96. The sentence attaches the closed form $\Phi(r/2-\varepsilon/r)-e^\varepsilon\Phi(-r/2-\varepsilon/r)$ to the shift $r\ge0$, and the form is undefined at $r=0$, where $\delta_{\mathcal N}(\varepsilon;0)=0$. It tends to zero as $r$ decreases to zero (proven, as the builder says). No proof in the final document uses the closed form at $r=0$. The closed form itself is proven in one line and needs no memory (proven). The likelihood ratio of $\mathcal N(0,1)$ to $\mathcal N(r,1)$ at $y$ is $\exp(r^2/2-ry)$, which exceeds $e^\varepsilon$ exactly when $y<r/2-\varepsilon/r$, and that set gives the supremum in $\mathrm H_{e^\varepsilon}$. The Reading of the transfer uses $\delta_{\mathcal N}(1;1)=\Phi(-1/2)-e\,\Phi(-3/2)=0.1269$ (computed).

Smallest fix. "... is nondecreasing in the shift $r\ge0$ and, for $r>0$, equals $\Phi(r/2-\varepsilon/r)-e^\varepsilon\Phi(-r/2-\varepsilon/r)$ ...". The citation may stay.

## Instructions for round 10

Each item names its challenge and gives the smallest correct text. Line numbers refer to `final/learning-oracle-theory.md` after round 09. Nothing outside these items changes in the final document.

1. ch-seed-map-channel, two places. Line 131, in (c)(ii), replace "under deterministic kernels with a finite view" by "under deterministic kernels through a deterministic channel with a finite view". Line 362, open problem 8, replace "Under deterministic kernels with atomless views, does some seed map" by "Under deterministic kernels, with a deterministic channel and atomless views, does some seed map".
2. ch-per-round-threshold, two places. Line 187, replace "With a threshold $\Delta_t$ per round, $\sqrt R\Delta$ becomes $(\sum_t\Delta_t^2)^{1/2}$." by "With a threshold $\Delta_t$ per round, and $\epsilon_b$ the probability that some round $t$ has $\Vert f_t(c_t,W'_t)-f_t(c_t,W_t)\Vert>\Delta_t$, $\sqrt R\Delta$ becomes $(\sum_t\Delta_t^2)^{1/2}$." Line 227, replace "For thresholds per round, step 4 uses $\mathcal N((\Delta_t/\sigma)_t,I_R)$." by "For thresholds per round, the hybrid clips round $t$ at $\Delta_t$, step 3 reads the exceedance of round $t$ at $\Delta_t$, and step 4 uses $\mathcal N((\Delta_t/\sigma)_t,I_R)$."
3. ch-active-choice-conditions. Line 345, replace "and let a certifier be sound for every learning function and accurate where the leakage is zero." by "and let a certifier be sound for every learning function and accurate where the leakage is zero, to a fixed level below one, at error probabilities summing below one."
4. ch-scalar-label, two places. Line 195, replace "(proven, round-04/builder.md and round-05/builder.md)." by "(proven given that decryption of $a$ times a ciphertext returns $a$ times its message plus an error of bounded norm and any noise the decryptors add, which is heuristic for CKKS, round-04/builder.md and round-05/builder.md)." The symbol $a$ is then defined by "a public scalar" in the sentence before. Line 197, replace "Heuristic, the realization by threshold CKKS." by "Heuristic, the realization by threshold CKKS and the form of its decryption under a public scalar."
5. ch-estimator-alpha-range. Line 195, replace "(e)(iii) Over $\mathfrak L_B$, $O(" by "(e)(iii) Over $\mathfrak L_B$ and for $\alpha\le1/2$, $O(".
6. ch-closed-form-domain. Line 96, replace "is nondecreasing in the shift $r\ge0$ and equals" by "is nondecreasing in the shift $r\ge0$ and, for $r>0$, equals".
7. `theory/CURRENT.md`, mirrors of items 3 to 5, so that the audit can read the final document against the register. In the register line of thm-active-choice-dichotomy, after "accurate at the reference function", add ", to a fixed level below one, at error probabilities summing below one". In the register line of thm-dataflow-composition, add "the form of CKKS decryption under a public scalar" to its heuristic list. In open problem 2, after "In every dimension", add "and for $\alpha\le1/2$". Record in the register the round-09 verdicts below and the round-10 changes.

The readability item of round-08/challenger.md, plan item 3, is not an instruction. The criterion-4 paragraph of [thm-bounded-deviation-transfer] at line 267 states results, entry 34 of the builder's table, and its numbers come from (b), (e) and the Reading of thm-dataflow-composition (e)(ii). Moving them into those statements changes frozen statements. The dataflow paragraph at line 201 has three sentences and states its claims already. Neither paragraph can be trimmed without changing a statement, so both stay.

After the changes, run `node scripts/build.mjs round-10/builder.md theory/CURRENT.md final/learning-oracle-theory.md` and `node scripts/verify.mjs final`. The second will report the three items at REVISE until the round-10 challenger judges them.

## Verdicts

Six definitions and fifteen results with slug tags in the final document, judged as they stand there now. [thm-coupling-certificate], [thm-dataflow-composition] and [thm-active-choice-dichotomy] stand at REVISE, because each has a sentence that is false as written or labelled beyond its source. Each needs one clause from the list above, and each meets the four-part bar once the clause is in. The other non-trivial results keep ACCEPT NONTRIVIAL. Four challenges are blocking.

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
VERDICT thm-coupling-certificate REVISE
VERDICT thm-black-box-certifiability ACCEPT NONTRIVIAL
VERDICT thm-dataflow-composition REVISE
VERDICT thm-bounded-deviation-transfer ACCEPT NONTRIVIAL
VERDICT thm-replay-audit-steer ACCEPT NONTRIVIAL
VERDICT thm-perfect-substitution ACCEPT
VERDICT thm-reference-access ACCEPT
VERDICT thm-bank-soundness ACCEPT
VERDICT thm-active-choice-dichotomy REVISE
VERDICT thm-record-level-certificate ACCEPT NONTRIVIAL
VERDICT thm-smoothed-choice-certificate ACCEPT NONTRIVIAL
BLOCKING 4
```
