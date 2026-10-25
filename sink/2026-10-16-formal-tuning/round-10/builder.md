# Round 10, builder

Verdict of this turn. The seven instructions of round-09/challenger.md are applied, four as written and three as the smallest correct variant. Item 1 keeps the challenger's words, and a full stop replaces ", and" so that no sentence exceeds thirty words. Item 3 reads "a fixed level in $(0,1)$" for "a fixed level below one", because at level zero no coupled certificate is accurate (proven, below). It also splits the sentence. Item 4 names the scalar $a$ where it is introduced and turns the long label into two sentences. Item 7 carries the variant of item 3 into the register and adds one comma. The edits pushed the final document to 19 pages. In each of the five theorem sections the line "Statement." now runs into the first part, as in the two lemma sections, and the document has 18 pages again. No other word of either file changed.

Line numbers refer to `final/learning-oracle-theory.md` and `theory/CURRENT.md` after this round. Word counts count each formula, each part marker such as (ii), and each file name as one word.

## Instructions applied

### 1. ch-seed-map-channel

Applied with one variant. In (c)(ii) of [thm-coupling-certificate] the instruction's words inside the old sentence give 31 words. The comma and "and" before "some $\psi$" became a full stop. Line 129 now reads as follows.

"(ii) A coupling through a seed map $\psi$ with $\psi_*\mu=\mu$ also bounds $\mathrm H_\gamma(P_0\|P_1)$. Some $\psi$ makes it exact for $\mathrm{TV}$ under deterministic kernels through a deterministic channel with a finite view."

Open problem 8, line 352, as written.

"8. Seed maps. Under deterministic kernels, with a deterministic channel and atomless views, does some seed map make the coupling of thm-coupling-certificate (c)(ii) exact for $\mathrm{TV}(P_0,P_1)$ in the limit?"

### 2. ch-per-round-threshold

Applied as written, in both places. The norm keeps the challenger's `\Vert`, which renders as the `\|` of the rest of the document. Part (b) of [thm-dataflow-composition], line 181.

"With a threshold $\Delta_t$ per round, and $\epsilon_b$ the probability that some round $t$ has $\Vert f_t(c_t,W'_t)-f_t(c_t,W_t)\Vert>\Delta_t$, $\sqrt R\Delta$ becomes $(\sum_t\Delta_t^2)^{1/2}$."

Step 5 of the proof of (b), line 221.

"For thresholds per round, the hybrid clips round $t$ at $\Delta_t$, step 3 reads the exceedance of round $t$ at $\Delta_t$, and step 4 uses $\mathcal N((\Delta_t/\sigma)_t,I_R)$."

### 3. ch-active-choice-conditions

Applied with a variant, for two reasons. First, the instruction makes the sentence 37 words long, so ", and let" became ". Let". Second, "a fixed level below one" admits the level zero, and at level zero the next sentence but one, "Coupled certificates achieve this up to a logarithmic factor", is false. Line 335 now reads as follows.

"Let the coalition pick choices from admissible sets. Let a certifier be sound for every learning function and accurate where the leakage is zero, to a fixed level in $(0,1)$, at error probabilities summing below one."

Claim. At level zero no coupled certificate of [thm-active-choice-dichotomy] is accurate, whatever its number of Train calls. At every level in $(0,1)$ the two halves of the paragraph hold (proven).

Proof. Every threshold $\Delta$ of def-isolated-client is positive. For $r>0$ and $\varepsilon\ge0$, the likelihood ratio of $\mathcal N(0,1)$ to $\mathcal N(r,1)$ at $y$ is $\exp(r^2/2-ry)$, which exceeds $e^\varepsilon$ on the half line $y<r/2-\varepsilon/r$. That half line has positive mass under $\mathcal N(0,1)$, so $\delta_{\mathcal N}(\varepsilon;r)>0$. The certificates (b)(i) and (b)(ii) of round-03/builder.md, lines 275 to 279, output $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$ plus a nonnegative term, capped at one. So they never output zero, and none is accurate at level zero. Now fix a level $\ell\in(0,1)$. Choose $\eta\in(0,1-\ell)$, and $\Delta>0$ with $\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)<\ell$, which exists since $\delta_{\mathcal N}(\varepsilon;r)$ tends to zero as $r$ decreases to zero (round-09/challenger.md, ch-closed-form-domain). Put $\epsilon_{\mathrm{acc}}=\ell-\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)>0$. Then the hypothesis of the corollary of round-03/builder.md, lines 285 to 290, holds, and it gives both the linear lower bound and the coupled upper bound. Part (c)(iii) at line 281 gives $\Pr[\hat t\ge1-\eta]\ge1-\alpha$ for an infinite set, which excludes accuracy at $\ell<1-\eta$ when $\alpha+\alpha'<1$. $\square$

The variant follows the challenger's own argument, which ends "a level in (0,1) suffices for both halves".

### 4. ch-scalar-label

Applied with a variant, for two reasons. First, the sentence before writes "a public scalar" and names no symbol, so $a$ would be used before its definition. The words "$a$" now follow "a public scalar". Second, the instruction's label makes the sentence 56 words long. The citation stays on the claim, and the label becomes two sentences that keep every word of the challenger's label. Line 189 now reads as follows in this part.

"Unchecked decryption lets a public scalar $a$ divide the protecting noise when the decryptors add it at decryption. Noise that client $j$ adds inside its ciphertext scales with the update, and the scalar then removes at most the decryption error (round-04/builder.md and round-05/builder.md). These claims are proven given that decryption of $a$ times a ciphertext returns $a$ times its message plus an error of bounded norm and any noise the decryptors add. That form is heuristic for CKKS."

"These claims" covers the third and the fourth sentence, as the challenger's verdict on the mathematics of both does. The form is the hypothesis $y^{(a)}=a\tilde u+e^{(a)}+Z_1$ with $\Vert e^{(a)}\Vert\le e_{\max}$ of round-04/builder.md, line 267. Its heuristic status is round-04/builder.md, line 281, and round-05/builder.md, line 213. The Label, line 191, as written.

"Heuristic, the realization by threshold CKKS and the form of its decryption under a public scalar."

### 5. ch-estimator-alpha-range

Applied as written. Line 189.

"(e)(iii) Over $\mathfrak L_B$ and for $\alpha\le1/2$, $O(e^{B^2/\sigma^2}\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha))$ drawn-seed Train calls reach accuracy $\epsilon_{\mathrm{acc}}$ in every dimension, at fixed $\gamma$ (proven, round-02/builder.md)."

### 6. ch-closed-form-domain

Applied as written. Line 96, in (F6)(i).

"... where $\delta_{\mathcal N}(\varepsilon;r)=\mathrm H_{e^\varepsilon}(\mathcal N(0,1)\|\mathcal N(r,1))$ is nondecreasing in the shift $r\ge0$ and, for $r>0$, equals $\Phi(r/2-\varepsilon/r)-e^\varepsilon\Phi(-r/2-\varepsilon/r)$ (Balle and Wang, ICML 2018, from memory)."

### 7. Mirrors in `theory/CURRENT.md`

Register line of thm-active-choice-dichotomy, line 170. The clause carries the variant of item 3, so that the register reads like the final document. The register sentence had 51 words before this round. It now splits where the clause ends, and the sentence that carries the clause has 27 words. The rest of the cell is unchanged.

"Let a certifier be sound for all learning functions and accurate at the reference function, to a fixed level in $(0,1)$, at error probabilities summing below one. Its certification then costs Train calls linear in the distinct admissible choices, ..."

Register line of thm-dataflow-composition, line 168, as written.

"heuristic (realization by threshold CKKS, six additions, the form of CKKS decryption under a public scalar)"

Open problem 2, line 182, with one comma added. Without it the two formulas would read as one.

"In every dimension and for $\alpha\le1/2$, $O(e^{B^2/\sigma^2}\epsilon_{\mathrm{acc}}^{-2}\ln(1/\alpha))$ drawn-seed Train calls give a uniformly accurate certifier."

Verdicts and changes. The title names round 10. The six definitions read "ACCEPT in rounds 02 to 09", or "04 to 09" for def-isolated-client. The other accepted items carry "latest in round 09". The register's rule gives the status "proposed" to an item that no challenger has judged in its current form. So the three items that round 09 sent to REVISE read "proposed in round 10", followed by what round 10 changed. The round-09 REVISE with its challenges and the round-08 ACCEPT NONTRIVIAL follow. Their Round column reads 10, and their Proof column adds this file.

### Length of the final document

After the seven items the PDF had 19 pages, with the section Prior work on page 19. The line "Statement." of each theorem section now runs into its first part, as "Statement. (a) Soundness." in [thm-replay-audit-steer]. The sections of [lem-needle-lower-bound] and [lem-sphere-code] already had this form. This removes five paragraph breaks and changes no word. The PDF has 18 pages.

## Checks after editing

Symbols. Every symbol that an edit introduces is defined before its use in the final document.

| Edit | Symbol | Defined at |
| --- | --- | --- |
| 1, 6 | $\psi$, $\mathrm{TV}$, deterministic channel, $r$ | setting of (c) at line 129 for $\psi$, line 48 for $\mathrm{TV}$, remark of def-certifier at line 56, (F6)(i) itself for the shift $r$ |
| 2 | $\Delta_t$ | the same sentence, "a threshold $\Delta_t$ per round" |
| 2 | $\epsilon_b$, $W'_t$ | def-isolated-client, line 81 |
| 2 | $f_t$ | def-isolated-client, line 72 |
| 2 | $W_t$, $c_t$ | def-isolated-client, item 1, line 74 |
| 2 | the hybrid, step 3 | step 2 at line 205, step 3 at line 213 |
| 3 | level, error probabilities | def-certifier, line 54, and the corollary of [thm-bounded-deviation-transfer], line 251 |
| 4 | $a$ | "a public scalar $a$", line 189, in the sentence before its first use |
| 5 | $\alpha$, $\mathfrak L_B$ | def-certifier, line 54, and (e)(ii), line 185 |

Sentence length, with the counting rule above. Every sentence that an edit created or changed has at most thirty words.

| Line | Sentence | Words |
| --- | --- | --- |
| 96 | (F6)(i) | 22 |
| 129 | "(ii) A coupling ... also bounds ..." | 13 |
| 129 | "Some $\psi$ makes it exact ..." | 18 |
| 181 | "With a threshold $\Delta_t$ per round ..." | 19 |
| 189 | "Unchecked decryption lets a public scalar $a$ ..." | 18 |
| 189 | "Noise that client $j$ adds ..." | 25 |
| 189 | "These claims are proven given ..." | 29 |
| 189 | "That form is heuristic for CKKS." | 6 |
| 189 | "(e)(iii) Over $\mathfrak L_B$ and for $\alpha\le1/2$ ..." | 22 |
| 191 | "Heuristic, the realization ..." | 16 |
| 221 | "For thresholds per round, the hybrid clips ..." | 26 |
| 335 | "Let the coalition pick choices from admissible sets." | 8 |
| 335 | "Let a certifier be sound ..." | 28 |
| 352 | open problem 8, the question | 26 |
| CURRENT 170 | "Let a certifier be sound for all learning functions ..." | 27 |
| CURRENT 182 | "In every dimension and for $\alpha\le1/2$ ..." | 15 |

Reading in context. Each edited sentence was read with the sentences around it.

1. In (c)(ii), "it" in the new second sentence names the coupling through a seed map of the first. The Label, "(c)(ii) for finite views", needs no change, as the challenger said.
2. In (b), the new $\epsilon_b$ replaces $\epsilon_b(\Delta)$ in both bounds of the display, and $\Delta_t$ replaces $\Delta$ in round $t$. The sum over $\beta_t$ in the sentence before keeps one threshold. A round that does not run has no $c_t$ or $W_t$, so "some round $t$" ranges over the rounds that run, as the maximum in def-isolated-client does.
3. In the active-choice paragraph, "it" in "In some procedure it then needs" names the certifier of the new second sentence. "No number suffices for an infinite set" now inherits both conditions, which ch-active-choice-conditions requires.
4. In (a), the citation of round-04 and round-05 stays with the two claims. The new label sentence states the form of decryption once. The Label line keeps "Proven, (a) given the realization error", and its heuristic list now names the form, so the two together carry both assumptions.
5. Part (e)(iii) and open problem 2 now state the same range. Open problem 4 cites (e)(iii) for $R=1$ and states no level, so it needed no change.
6. In (F6)(i) the closed form now carries its domain. No proof of the final document uses it at $r=0$.

Writing rules. No edited sentence has a semicolon, a dash used as punctuation, a colon in prose, or bold. The variants add no term outside `CONTEXT.md` and the theory.

Scope of the change. A diff of `final/learning-oracle-theory.md` against its round-09 state shows the eleven edited places of items 1 to 6 and the five merged "Statement." lines, and nothing else. A diff of `theory/CURRENT.md` shows the title, the three edits of item 7 and the Status, Round and Proof columns of the register.

Pages. `pdfinfo final/learning-oracle-theory.pdf` reports 18 pages.

Commands. `node scripts/build.mjs round-10/builder.md theory/CURRENT.md final/learning-oracle-theory.md` prints `BUILD OK n=3`. `node scripts/verify.mjs final` reports exactly the three items that round 09 left at REVISE, thm-coupling-certificate, thm-dataflow-composition and thm-active-choice-dichotomy, and no other failure. The round-10 challenger judges them.
