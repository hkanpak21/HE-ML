# Round 04, challenger

Verdict of this turn. The blocking challenge ch-dataset-node-channel is closed. The new clause of [def-isolated-client] hides the input node of $D_j$, step 1 of [thm-dataflow-composition] (b) now names that node and the two facts its induction uses, and every theorem that uses the definition still holds (proven, by the re-check below). Every other round-03 challenge is fixed, except ch-symbol-clash, whose old instances are renamed but whose new round-04 text adds nine fresh clashes. I checked every new or revised proof step by step. I found no false statement. [lem-sphere-code] is correct, with constant $1-\mathrm h_2(1/4)=0.1887$ (computed). [thm-smoothed-choice-certificate] is correct in all five parts and the corollary. The product bound survives adaptivity because the coalition's input of round $t-1$ is measurable before the noise $Z_{t-1}$ is drawn. The change of measure of (c) is exactly the probability-preservation inequality of Rényi differential privacy, applied along the path, and its exponent $(\varpi-1)(R-1)B_A^2/(2\sigma^2)$ is right, with $R-1$ because the input of the last round reaches no node that the exceedance reads. Part (c) is the best result of the round and earns NONTRIVIAL. One constant can be settled cheaply. The factor four lost in the lower bound of (d) comes from nearest-point decoding of a code with minimum distance one. Threshold decoding of a nearly orthogonal code recovers it, and the price then has constant $1/2$ whenever $\mathfrak e/d\to0$ (proven, sketch, under Steering). That is the one problem I set, as a strengthening of part (d), with no new slug. Seven challenges are new or reopened, none blocking. The most useful is ch-reference-strategy. Measuring the coalition's deviation from the protocol's input, instead of from zero, makes (c) at $B_A=0$ coincide with the passive certificate of [thm-dataflow-composition] (c), so the final document can state one theorem for both. All six definitions are now accepted, eleven results are accepted, seven of them NONTRIVIAL, and the blocking count is zero.

Every non-trivial claim carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the idea is written here and the builder must write it out. Notation follows `theory/CURRENT.md`. I opened no outside source this round. Two facts are cited from memory and used only in heuristic claims, Shannon's coding theorem for the additive white Gaussian noise channel and the fact that orthogonal signalling attains its capacity at low signal-to-noise ratio. Hoeffding's inequality for a sum of independent signs, $\Pr[|\sum_{i\le d}\omega_i\omega'_i|>\kappa d]\le2e^{-\kappa^2d/2}$, is standard and used in a proven sketch.

## Status of the round-03 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-dataset-node-channel | blocking | fixed | none. Checked below for every procedure that uses the definition |
| ch-adaptivity-scope | not blocking | fixed | none. The Gaussian form of the instance is correct, $0.6-8\bar\Phi(3)=0.5892$ (computed) |
| ch-tree-symmetry | not blocking | fixed | none |
| ch-finite-scalar-attack | not blocking | fixed | the Reading needs one clause on where the protecting noise is added (ch-scalar-noise-placement) |
| ch-scalar-sharpness | not blocking | fixed | none |
| ch-invert-remark | not blocking | fixed | the remark uses $\mathrm H^{\to}_i$, $\delta_R$ and $F^{\to}$ before any definition introduces them (folded into ch-symbol-clash) |
| ch-bank-call-count | not blocking | fixed | none |
| ch-symbol-clash | reopened | reopened again | the round-03 clashes are renamed, the round-04 text adds nine new ones |
| ch-open-problems-exact | not blocking | fixed | item 5 needs a rewrite in the light of the problem under Steering (ch-open-problem-five) |

Detail on ch-dataset-node-channel. The fix has three parts, and each is needed. Ownership by client $j$ makes the dataset a value that the coalition cannot set, because the values of nodes that the coalition owns are its choices under [def-learning-oracle-model]. Channel none for the input node closes the counterexample of round 03. Condition 2 already restricts the children of that node to the $v_t$. With the three, the induction of step 1 holds (proven). A node other than the input node of $D_j$, the $v_t$ and the $r_t$ reads neither $D_j$ nor any $W_t$. The coalition receives the input node and the $v_t$ only through the releases and, under the seed-revealing policy, the revealed seeds. Every other input node has a value with one law under both hypotheses, which $\omega$ carries. I re-ran the check on each procedure the builder lists, $G_1$, the procedure of (e), $G^{\mathcal C}$, $G^{\mathrm{agg}}$, $G^{\mathrm{rec}}$, $G^{\mathrm{two}}$, $G^{\mathrm{two}}_R$, $G^{\mathrm{ad}}$, $G^{\mathrm{agg}}_R$ and $G_{\mathrm{enc}}$. In each, client $j$ owns its dataset node and no channel releases it (proven, by inspection). The lower bounds argue from step 1 at a reference function and are unaffected. One wording point, not a challenge. Step 1 says that every other input node has "a value that the hypotheses fix". A sampler of fresh records is an input node whose output is random. "A value whose law the hypotheses fix, carried by $\omega$" is the exact form.

## Definitions

### [def-learning-oracle]

Unchanged and well posed. Accepted in rounds 02, 03 and now 04. ACCEPT.

### [def-learning-oracle-model]

The definition is unchanged. Two remarks are added.

The inversion remark is correct (proven, by the definition of $\mathrm H_\gamma$). It uses three objects of [thm-record-level-certificate] before any definition introduces them. The final document should either move the average form under that theorem or define the three objects in the remark.

The transfer remark has a correct first sentence with the wrong reason, and a second sentence that is not exact. First sentence. A certifier sound for $\theta'\ge\theta$ is sound for $\theta$, since $\theta(\mathsf L)\le\theta'(\mathsf L)\le\hat t$ on the soundness event (proven, one line). So every lower bound of the form "every certifier sound for $\theta$ satisfies $\Pr_{\mathsf L^\circ}[\hat t\ge\vartheta]\ge p$" holds for every certifier sound for $\theta'$. That covers the needle bounds and also the pair-code bounds of [thm-dataflow-composition] (e) and [thm-smoothed-choice-certificate] (e), which do not go through [lem-needle-lower-bound]. The condition $\theta'(\mathsf L^\circ)=0$ is needed only to read the bound as a failure. Second sentence. "A sub-procedure whose other nodes the coalition can simulate" is labelled proven, but simulation is not defined. The condition that makes $\theta'\ge\theta$ true is data processing. For every adversary of the stated procedure, some adversary of the larger one has a view from which a measurable map, the same under both hypotheses, recovers the stated view. Honest clients whose updates enter the sum fail this condition, and open problem 1 asks whether they lower the divergence, so the informal wording hides a real case (ch-lower-bound-transfer). ACCEPT, since the remark is not part of the definition.

### [def-degenerate-oracles]

Unchanged and well posed. ACCEPT.

### [def-certifier]

Unchanged and well posed. ACCEPT.

### [def-model-bank]

Unchanged and well posed. Only [thm-bank-soundness] and part (d) of [thm-record-level-certificate] use it. If neither is presented in full in the final document, the definition can move to the section that states them. Not a challenge. ACCEPT.

### [def-isolated-client]

Well posed (proven, by inspection). The opening sentence gives client $j$ the input node of $D_j$, and condition 4 sends it through channel none. The coupled execution, the exceedance and the coupled tail are unchanged. The coupled tail with two states, $\beta_t(c,w^0,w^1,\Delta)$, is used by the sum bound of step 3 of [thm-dataflow-composition] (b), so it stays. The remark on thresholds per round moved into that theorem, as round 03 asked. The last sentence of the remarks cites a round and a challenge, which the final document must drop, since a definition does not carry its history. Simplicity. The definition is as small as the theorems that use it allow, since state, stop and twin are each used. ACCEPT. This is the first acceptance in its current form, and the stopping rule needs a second in round 05.

## Proofs

### Sphere code [lem-sphere-code]

Claim. At least $2^{0.18d}$ points of the unit sphere of $\mathbb R^d$ have pairwise distances at least one, and the Voronoi cells of any set of points with pairwise distances at least $s$ keep a Gaussian of scale $\sigma'$ centred at a point with probability at least $1-(J-1)\bar\Phi(s/(2\sigma'))$.

Check of (a) (proven). The entropy bound on the binomial sum is right for $p\le1/2$ and every integer $r\le pd$, including non-integer $pd$, since the step uses only $(p/(1-p))^i\ge(p/(1-p))^{pd}$ for $i\le pd$. A maximal code of minimum Hamming distance $\lceil d/4\rceil$ covers the cube at radius $\lceil d/4\rceil-1\le d/4$. So $|\mathcal W|\ge2^{d(1-\mathrm h_2(1/4))}$, where $\mathrm h_2$ is the binary entropy. I computed $1-\mathrm h_2(1/4)=0.18872$, so the constant $0.18$ holds with room. The squared distance $4\,\mathrm{Ham}(\omega,\omega')/d\ge4\lceil d/4\rceil/d\ge1$ is right. Small dimensions also check. At $d\le4$ the code is the whole cube, and $2^d\ge\lceil2^{0.18d}\rceil=2$.

Check of (b) (proven). The cells are open and disjoint. The event $\mathbf p_k+G\notin V_k$ needs $\|\mathbf p_k+G-\mathbf p_l\|\le\|G\|$ for some $l\neq k$, and expanding the square gives $\langle G,\mathbf e\rangle\ge\|\mathbf p_l-\mathbf p_k\|/2$. Ties have probability zero. The union bound and (G3) finish.

Weakest step. None of substance. The constant could be raised to $\log_2(2/\sqrt3)\approx0.2075$ up to a polynomial factor by the spherical-cap volume bound for angle $\pi/3$ (heuristic, from memory). Nothing below needs it.

Non-triviality. Not claimed. The lemma is coding theory. ACCEPT.

### Smoothed-choice certificate [thm-smoothed-choice-certificate]

Claim. In $G^{\mathrm{agg}}_R$, a coalition client whose inputs to the release have norm at most $B_A$ is bounded through a product of smoothed tails on escape balls, certified by a covering. In every isolated procedure in which the coalition acts only through additive inputs of norm at most $B_A$, its exceedance is at most that of the null strategy, transformed by $\Upsilon_{\mathfrak e}$ with $\mathfrak e=(R-1)B_A^2/(2\sigma^2)$, and this is certified at a cost free of $d$. Any certifier sound over every learning function pays a number of Train calls at least $\min\{2^{0.18d},\eta e^{\mathfrak e/4}\}$ up to constants, and drawn seeds fail.

Assumptions. The client of (a) and (b) is stateless. (c) allows state. The coalition acts only through input nodes whose only child is $r_t$, its contribution enters $O_t$ additively, and every other choice it makes is the protocol's. The release noise is Gaussian and independent of everything else. The policy is realizable or seed-revealing.

Threat model. An adaptive, unbounded coalition that sees every release, may stop after a release and, under the seed-revealing policy, sees client $j$'s seeds before it sets the input of the same round.

#### Part (a), the product bound

Step 1 (proven). The continued strategy is admissible and agrees with the stopping one until the stop, so the stopping strategy's exceedance is a maximum over a subset of the rounds of the continued one.

Step 2 (proven). I checked the three facts. $m_{t-1}$ is a function of $\omega$, $\zeta_{\le t-2}$ and $Z_{\le t-2}$. The input $u_{t-1}$ is set before $r_{t-1}$ runs and after $v_{t-1}$ runs, so under the seed-revealing policy it may read $\bar\rho_{t-1}=\rho_{t-1}$, which is a coordinate of $\zeta_{t-1}$ and so lies in $\mathcal G_t$. $W_{t-1}$ is a function of $m_{t-1}$ and $\zeta_{t-1}$, because the client is stateless. So $z_t$ is $\mathcal G_t$-measurable. $Z_{t-1}$ and $\zeta_t$ are independent of $\mathcal G_t$ and of each other. $E_s$ for $s<t$ is a function of $z_s+Z_{s-1}$ and $\zeta_s$ with $s-1\le t-2$. Fubini's theorem then gives $\Pr[E_t\mid\mathcal G_t]=\tilde\beta_t(z_t)$.

Step 3 (proven). $A_{t-1}\in\mathcal G_t$, so the conditioning step is valid, and the induction gives the product on the event of no escape. The decomposition $z_t-m_1=\sum_{s\le t-1}(u_s+\mathrm{clip}_B(W_s-m_s))+\sum_{s\le t-2}Z_s$ is right, since $z_t=m_t-Z_{t-1}$. The sum of the noises has law $\mathcal N(0,(t-2)\sigma^2I_d)$ whatever the strategy, because the joint law of the $Z_s$ does not depend on it. (F7) is correct. $\mathbb E e^{G_i^2/4}=\sqrt2$, Markov's inequality gives $2^{d/2}e^{-r^2/4}$, and that equals $\alpha'$ at $r_d(\alpha')$. $\mathrm{Esc}_2$ is empty and the union over $3\le t\le R$ costs at most $\alpha_{\mathrm{esc}}$.

The case $b=1$ (proven). The norm of the coupled difference has the same law when the two draws of hardware randomness are exchanged, so $\tilde\beta_t$ is the same function.

Weakest step. The $\mathcal G_t$-measurability of $u_{t-1}$. It rests on step 1 of [thm-dataflow-composition] (b), which now holds, and on the order $v_{t-1}\prec r_{t-1}$. If the seed of round $t-1$ were revealed only after the input of round $t-1$ is set, the claim would still hold. If the input of round $t-1$ could read $Z_{t-1}$, it would fail. No procedure of the theory allows the latter.

#### Part (b), the covering certificate

Lipschitz step (proven). $\mathrm{TV}(\mathcal N(z,\sigma^2I_d),\mathcal N(z',\sigma^2I_d))=2\Phi(\|z-z'\|/(2\sigma))-1\le\|z-z'\|/(\sigma\sqrt{2\pi})$. The integrand $\beta_t((t,\cdot),\Delta)$ is measurable by Fubini's theorem, since $\mathsf L$ is jointly measurable.

Coverage and nets (proven). Each draw is a Bernoulli variable with mean $\tilde\beta_t(z)$, since it uses a fresh $Z$, a fresh seed and fresh hardware randomness. The union bound runs over $n_{\mathrm{pt}}$ Clopper and Pearson bounds. Maximality gives a net point within $\lambda\sigma\sqrt{2\pi}$, and the volume count gives $|\mathrm{Net}_t|\le(1+2\varrho_t/(\lambda\sigma\sqrt{2\pi}))^d$. The zero-exceedance bound $R(\ln(n_{\mathrm{pt}}/\alpha)/n+\lambda)$ is right, since round 1 carries no $\lambda$ and is counted once.

The correction to my round-03 base (proven). The escape radius contains the random walk of the release noise, of order $\sigma\sqrt{td}$, so the covering base grows like $R^{3/2}\sqrt d/\epsilon_{\mathrm{acc}}$ even at small $B_A$ and $B$. My base $R(B_A+B)/(\lambda\sigma)$ omitted it. The builder is right.

Weakest step. None in the logic. The cost is the issue. At $B_A=0$ the covering pays $\exp(\Theta(d\ln(R^{3/2}\sqrt d/\epsilon_{\mathrm{acc}})))$ calls where the passive certificate of [thm-dataflow-composition] (c) pays $O(R\ln(1/\alpha)/\epsilon_{\mathrm{acc}})$. Part (b) beats part (c) only when $\mathfrak e$ exceeds about $d\ln(R^{3/2}\sqrt d/\epsilon_{\mathrm{acc}})$ (heuristic comparison of the two costs). The final document can state (a) and (b) with a pointer.

#### Part (c), the transfer from the null strategy

This is the part the task singled out. I checked each step and tried three ways to break it.

Step 1 (proven). The exceedance event is the same measurable set $\mathbb A$ of $(V,y_{<R})$ under the strategy and under the null strategy. Three hypotheses carry it. The coalition's input nodes have the single child $r_t$, so their values reach later nodes only through $y_t$. Every other choice that enters a node is the protocol's, a function of procedure values and not of the adversary's state. $o_t$ reads neither $v_t$ nor the coalition's inputs, and its own randomness lies in $\omega$, which round 02 defines to hold the randomness of each $r_t$ other than $Z_t$. With these, $c_t$, $W_t$, $W'_t$ and $o_t$ are the same maps of $(V,y_{<t})$ under both strategies. The adversary's state, and so $U_t$, is a function of $\omega$, $y_{<t}$ and $\bar\rho_{\le t}$, and $\bar\rho_{\le t}$ lies in $V$. The event reads $y_{<R}$ only, because $c_R$ is the value of a parent of $v_R$, and $v_R$ runs before $r_R$.

Step 2 (proven). Given $(V,y_{<t})$ the release $y_t$ is $\mathcal N(U_t+M_t,\sigma^2I_d)$ under $P$ and $\mathcal N(M_t,\sigma^2I_d)$ under $Q$, because $Z_t$ is independent of $(V,Z_{<t})$ and $(V,y_{<t})$ is a function of $(V,Z_{<t})$. The density is the product of $R-1$ Gaussian likelihood ratios.

Step 3, the moment (proven). (F6) gives, for one Gaussian shift $u$,

$$\int\Big(\frac{\varphi_\sigma(y-u)}{\varphi_\sigma(y)}\Big)^{\varpi}\varphi_\sigma(y)\,dy=\exp\Big(\frac{\varpi(\varpi-1)\|u\|^2}{2\sigma^2}\Big).$$

I recomputed it. The ratio is $\exp(\langle y,u\rangle/\sigma^2-\|u\|^2/(2\sigma^2))$, its power $\varpi$ has mean $\exp(\varpi^2\|u\|^2/(2\sigma^2)-\varpi\|u\|^2/(2\sigma^2))$ by (G4). The conditional moment given $\mathcal F_t$ is bounded by its value at $\|U_t\|=B_A$, uniformly over paths, and the tower property over $t<R$ gives $\exp((R-1)\varpi(\varpi-1)B_A^2/(2\sigma^2))$. This is the adaptive composition of the Rényi divergence of order $\varpi$ of the Gaussian mechanism, $D_\varpi=(R-1)\varpi B_A^2/(2\sigma^2)$, since $\mathbb E_Q(dP/dQ)^\varpi=e^{(\varpi-1)D_\varpi}$.

Step 4, the power and the exponent (proven). Hölder's inequality with exponents $\varpi/(\varpi-1)$ and $\varpi$ and $\mathbf 1_{\mathbb A}^{\varpi/(\varpi-1)}=\mathbf 1_{\mathbb A}$ give

$$P(\mathbb A)\le Q(\mathbb A)^{1-1/\varpi}\Big(\mathbb E_Q\Big(\frac{dP}{dQ}\Big)^{\varpi}\Big)^{1/\varpi}\le Q(\mathbb A)^{1-1/\varpi}\exp\Big(\frac{(\varpi-1)(R-1)B_A^2}{2\sigma^2}\Big).$$

The power $1/\varpi$ removes one factor $\varpi$ from the moment, which is why the exponent carries $\varpi-1$ and not $\varpi(\varpi-1)$. This is the probability-preservation inequality $P(\mathbb A)\le(e^{D_\varpi}Q(\mathbb A))^{(\varpi-1)/\varpi}$. The optimization over $q=\varpi-1$ is right. With $\mathfrak L=\ln(1/Q(\mathbb A))$, the logarithm is $\psi(q)=-\mathfrak Lq/(1+q)+q\mathfrak e$, the minimum is at $1+q=\sqrt{\mathfrak L/\mathfrak e}$ when $\mathfrak L>\mathfrak e$, and the value there is $-(\sqrt{\mathfrak L}-\sqrt{\mathfrak e})^2$. I checked the algebra term by term.

Tightness of the exponent (proven, sketch). The transfer is tight to first order in the exponent. Take $d=1$, one round of shift, $Q=\mathcal N(0,\sigma^2)$, $P=\mathcal N(B_A,\sigma^2)$ and $\mathbb A=\{y>x\sigma\}$. Then $\ln(1/Q(\mathbb A))=x^2/2+O(\ln x)$, $\Upsilon_{\mathfrak e}(Q(\mathbb A))=\exp(-(x-B_A/\sigma)^2/2+O(\ln x))$, and $P(\mathbb A)=\bar\Phi(x-B_A/\sigma)$ has the same exponent. So no better function of $Q(\mathbb A)$ alone exists to first order in the exponent.

Step 5, the certificate (proven). $\Upsilon_{\mathfrak e}$ is nondecreasing on $[0,1]$, so the Clopper and Pearson upper bound transfers. The zero-exceedance arithmetic is right. $\ln(1/\bar\epsilon_b)\ge(\sqrt{\mathfrak e}+\sqrt{\ln(1/\epsilon_{\mathrm{acc}})})^2$ gives $\Upsilon_{\mathfrak e}(\bar\epsilon_b)\le\epsilon_{\mathrm{acc}}$. The two orders use the two forms of [thm-dataflow-composition] (b) without the factor $\gamma$, $\delta_{\mathcal N}+\epsilon_0$ for $\mathrm H_\gamma(P_0\|P_1)$ and $\delta_{\mathcal N}+\epsilon_1$ for $\mathrm H_\gamma(P_1\|P_0)$, and the experimenter samples $\mathsf{Ex}_1$ under the null strategy for the second.

Three attempts to break (c), all failed. First, a coalition that reads client $j$'s seed of round $t$ before it sets $u_t$. $U_t$ is still a function of $(V,y_{<t})$, and the step-2 conditional law is unchanged, so the bound holds under the top oracle. Second, a client with state. The maps of step 1 carry the state chains through $V$ and $y_{<t}$, and no step uses statelessness. Third, the input of the last round. $u_R$ moves $y_R$ only, which no node of the exceedance reads, so the exponent counts $R-1$ rounds and not $R$. The input of round $R$ is still covered, because [thm-dataflow-composition] (b) holds for every strategy and the input of round $R$ does not enter the exceedance.

What (c) does not cover. A coalition whose input enters the release nonlinearly, for instance through a robust aggregation rule such as a coordinate-wise median, or through a clip applied to the aggregate. A coalition that sets choices other than its additive inputs, which is the domain of [thm-active-choice-dichotomy]. Norm bounds in a norm other than the Euclidean one (ch-euclidean-norm-proof).

Weakest step. Step 1, the claim that the maps are the same under both strategies. It is where the three structural hypotheses enter, and a coalition input node with a second child, for instance a coalition-owned general node that forwards it to a later honest node, would break it. The setting excludes that, and the final statement should name the three hypotheses explicitly as the conditions of the theorem.

#### Part (d), the needle lower bounds

Sphere-code needles (proven). Distinct learner names per round make the needle sets lie in round $R$ only, which [def-isolated-client] allows, because a choice holds the learner name. Under $\mathsf L_k$, rounds $t<R$ return the starting model, so $y_t=B_A\mathbf q_k+Z_t$ under both hypotheses, and $m_R=\mathbf p_k+\sum_{t<R}Z_t$. The averaging identity (F2) with $y_{<R}$ as the common coordinate gives $\mathrm H_\gamma(P_0\|P_1)=\Pr[m_R\in V_k]\,\delta_{\mathcal N}(\varepsilon;B/\sigma)$. Lemma (b) with $s=(R-1)B_A$ and $\sigma'=\sigma\sqrt{R-1}$ gives the escape probability $\frac J2e^{-(R-1)B_A^2/(8\sigma^2)}$. I checked the arithmetic. $J_1\le\lceil2^{0.18d}\rceil$ points exist because the code size is an integer at least $2^{0.18d}$.

Ball needles (proven). $r=\sigma\sqrt{2(R-1)d/\eta}$ gives escape probability at most $\eta/2$ by Markov's inequality. A maximal $2r$-separated set in the ball of radius $(R-1)B_A$ has at least $((R-1)B_A/(2r))^d$ points, which equals the stated base. The strategy $u_t=(\mathbf p_k-m_1)/(R-1)$ has norm at most $B_A$.

The corollary (proven). The arithmetic of both items is right, and the regime condition $\mathfrak e\le2d/5$ gives $\mathfrak e/4\le d/10\le0.18d\ln2=0.1248d$ (computed), so $J_1=\lfloor\eta e^{\mathfrak e/4}\rfloor$.

Weakest step. Not a gap. The bound is loose by a factor four in the exponent, and the cause is identifiable. Nearest-point decoding of a code with minimum distance $s$ errs with probability about $e^{-s^2/(8\sigma'^2)}$, and minimum distance one on the unit sphere gives $e^{-\mathfrak e/4}$. Even an exactly orthogonal code has distance $\sqrt2$ and gives only $e^{-\mathfrak e/2}$ under this decoding. Threshold decoding against a nearly orthogonal code gives $e^{-\mathfrak e(1-o(1))}$. The problem under Steering writes this out.

#### Part (e), drawn seeds

Check (proven). The strengthened (e)(ii) of [thm-dataflow-composition] is checked below. Its pair code with $2J_{\mathrm{cd}}$ points of the sphere of radius $B$ lies in $\mathfrak L_B$, the test errs only when nearest-point decoding errs, and the collision bound $N(2N-1)/J_{\mathrm{cd}}$ of round 02 applies, because the family agrees outside $x_0$ and $x_1$. At $\mathsf L^\circ$ the seed-revealing adversary learns nothing, since $\mathsf L^\circ(x_0;\rho)=\mathsf L^\circ(x_1;\rho)$ for every seed. The outputs of (b) and (c) at $\mathsf L^\circ$ are their zero-exceedance values.

Weakest step. Inherited. The criterion-4 content is the pair code of [thm-dataflow-composition] (e), as in [thm-active-choice-dichotomy].

#### Readings of the builder

The DP-FedAvg numbers are right. With $B_A=B$ and noise multiplier $z=\sigma/B$, $\mathfrak e=(R-1)/(2z^2)$. At $z=1$ and $\epsilon_{\mathrm{acc}}=0.01$ the factor is $1.99\times10^4$ at $R=3$ and $2.18\times10^8$ at $R=11$ (computed). One consequence deserves a sentence in the final document, because it is the result Halil's setting needs. $\mathfrak e$ grows linearly in $R$, and (d) shows that the growth is not an artefact of (c). For model dimension $d$ far above $\mathfrak e$, every certifier sound over every learning function that certifies a value below $(1-\eta/2)\,\delta_{\mathcal N}(\varepsilon;B/\sigma)$ at the reference function pays at least about $\eta e^{(R-1)/(8z^2)}$ Train calls against a norm-bounded adaptive coalition client in DP-FedAvg (proven, from the corollary at $B_A=B$). At $z=1$ and $R=1001$ that is about $\eta e^{125}$. So against an adaptive coalition with norm-bounded inputs, certification by training runs is feasible for few rounds or for $B_A\ll\sigma/\sqrt R$, and infeasible in general beyond that. The worst-case bound $\delta_{\mathcal N}(\varepsilon;2\sqrt RB/\sigma)$, which needs no call, is then the only bound available, and it tends to one.

The application to the aggregation sub-protocol is correct as an implication (proven, given the realization error). RoFL's range proofs are cited from a search summary, so their norm is not checked here, and ch-euclidean-norm-proof asks for one clause.

#### Non-triviality

Criterion 1. $\epsilon^{\mathrm{nl}}_b$ and $\tilde\beta_t$ are defined by coupled Train calls that reuse a seed name. Criterion 2. Without the oracle, a bound against an adaptive coalition that moves the next starting model needs the law of the trained model on a continuum of starting models, and with state on every reachable history. Criterion 3. Every bound depends on $\mathsf L$ only through $\epsilon^{\mathrm{nl}}_b$ or $\tilde\beta_t$, and (c) is free of $d$, $B$, the state and the architecture. Criterion 4. The certificates of (b) and (c) fail in the drawn-seed discipline by (e), under item 3 of [def-degenerate-oracles], at every $B_A\ge0$. The criterion-4 content is inherited from the pair code. The new content, the transfer of (c) and the needle bounds of (d), is genuinely new and holds in both disciplines where it concerns lower bounds. The final document should say so, as for the other inherited cases. ACCEPT NONTRIVIAL.

### Dataflow composition, corrections [thm-dataflow-composition]

Step 1 of (b) (proven). Checked under Status above.

Part (a)(iii), finite form (proven). For (i), $F^r$ is closed, on $G_a$ the point $y^{(a)}/a$ lies within $r$ of $\tilde u$, and the triangle inequality gives $\tilde u\in F^{2r}$ under $H_1$. $\Pr[G_a^c]\le\Pr[\|Z_1\|>ar-e_{\max}]$ holds under both hypotheses, whatever the law of $e^{(a)}$ given $\tilde u$. The condition $ar>e_{\max}$ is not needed for the inequality and only keeps it non-vacuous. For (ii), the projection on $\mathbf n$ gives $\bar\Phi((a\mathfrak d/2-e_{\max})/\sigma)$ under each hypothesis. I checked both signs. The Reading needs one clause (ch-scalar-noise-placement). The hypothesis $y^{(a)}=a\tilde u+e^{(a)}+Z_1$ puts the protecting noise outside the scalar. That holds when the decryptors add the noise at decryption, as smudging or central noise. When each client adds its share of the noise inside its ciphertext, as in distributed differential privacy over secure aggregation, the scalar multiplies the noise too, and (ii) then gives nothing beyond the case $a=1$ (proven, by the same computation with $Z_1$ replaced by $aZ_1$).

Part (e)(ii), strengthened (proven). The $2J_{\mathrm{cd}}$ code points have norm $B$ and pairwise distances at least $B$. The test fails under $P^\varsigma_0$ only if nearest-point decoding errs, which lemma (b) bounds by $(2J_{\mathrm{cd}}-1)\bar\Phi(B/(2\sigma))$, and the same bound holds under $P^\varsigma_1$. The threshold arithmetic is right. $(2J_{\mathrm{cd}}-1)\bar\Phi(B/(2\sigma))\le J_{\mathrm{cd}}e^{-B^2/(8\sigma^2)}\le e^{-B^2/(16\sigma^2)}$ for $J_{\mathrm{cd}}\le e^{B^2/(16\sigma^2)}$, and $\lfloor2^{0.18d-1}\rfloor\ge1$ needs $d\ge6$. The Reading's $\sqrt{\eta/2}\min\{2^{0.09d},e^{B^2/(32\sigma^2)}\}$ is right up to a factor $\sqrt2$ in the first argument, and the word "about" covers it. This proves my round-02 sketch $e^{\Omega(\min(d,B^2/\sigma^2))}$, which I accept as now proven.

Thresholds per round (proven). With threshold $\Delta_t$ in round $t$ the kernel of step 4 uses shifts $\Delta_t/\sigma$, and the Gaussian term is $\delta_{\mathcal N}(\varepsilon;(\sum_t\Delta_t^2)^{1/2}/\sigma)$.

Non-triviality, re-confirmed. The changed steps do not touch the facts behind criteria 1 to 4, and the strengthened (e)(ii) strengthens criterion 4. ACCEPT NONTRIVIAL.

### Active-choice dichotomy, corrections [thm-active-choice-dichotomy]

The adaptivity remark (proven). I recomputed the four noiseless laws and the totals $0.5$, $0.5$ and $0.6$. The noisy bound loses $2\Pr[G^c]\le8\bar\Phi(\mathfrak s/(2\sigma))$, which is right, since each release errs with probability $2\bar\Phi(\mathfrak s/(2\sigma))$. The instance also shows that (a)(i) is tight here, since its bound $\delta_{\mathcal N}(0;\sqrt2\Delta/\sigma)+0.6$ tends to $0.6$ as $\Delta\to0$, and the adaptive strategy attains $0.6$ in the noiseless limit (computed).

The reverse order of (a)(ii) (proven). The embedding of $\mathsf{Ex}_1$ uses the tree triple with the hardware draws exchanged, and $D^\star_1\le D^{\mathbb T}$ holds because the norm is symmetric. The sentence that the prefix of length $t$ is first used in round $t$ now cites the stop and the single run of each $v_t$.

The aggregation sentence. The three facts replace "exactly", and each is proven.

Non-triviality, re-confirmed. ACCEPT NONTRIVIAL.

### Record-level certificate, corrections [thm-record-level-certificate]

Part (b)(ii) for $R$ rounds (proven). Under $H_0$ the coupled difference of a round $t<R$ equals $\Delta$, which does not exceed $\Delta$, and round $R$ exceeds exactly when $S>\iota$. So $\epsilon_0(\Delta)=\bar\Phi(\iota)$. Under $H_1$, $S\sim\mathcal N(\sqrt{R-1}\,\Delta,1)$. The two Mills-ratio limits are right. The first ratio tends to $e^{\varepsilon'}$ since $\iota\Delta'=\varepsilon'$. In the second, $u^2-\iota^2\ge(\varepsilon^2(R-1)/R-\varepsilon'^2)/\Delta'^2-\varepsilon$ has a positive leading coefficient, so the ratio tends to zero. This closes ch-scalar-sharpness.

Part (d), clauses (proven). The Bernoulli-inclusion clause and the level $1-3\alpha$ are as round 03 asked.

Non-triviality, re-confirmed. ACCEPT NONTRIVIAL.

### Bank soundness, label [thm-bank-soundness]

The label is right. The withdrawal of the second half of (d) is accepted. The reason given for dropping the Poisson item is not right (ch-poisson-reason). The reason given is that a class of learning functions defined by subsampling would be transparent to the certifier. Poisson subsampling is public in DP-SGD and is naturally a general node of the procedure, a node that draws the subset from its own randomness, and not a property of $\mathsf L$. In that form nothing is made transparent, and the question becomes one about procedures. The item is out of scope because no theorem of the theory uses it, and that is the reason to state. ACCEPT.

### Replay-audit steering, notation [thm-replay-audit-steer]

The statement of (e) now uses $n_{\mathrm{rep}}$. Nothing else changed. ACCEPT NONTRIVIAL.

## New challenges

### ch-reference-strategy

Not blocking. Simplification, due before the final document. Targets [thm-smoothed-choice-certificate] (c) and the opening of round-04/builder.md, which says that (c) compares every bounded strategy "with the protocol's own strategy". In the general setting of (c) the comparison strategy is the null strategy $u_t=0$. That is the protocol's strategy in $G^{\mathrm{agg}}_R$ but not in a procedure where coalition clients send honest updates. The proof gives more than the statement. Let $u^{\mathrm{pr}}_t$ be the input the protocol prescribes, a measurable function of procedure values, and call a strategy $B_A$-deviating when $\|u_t-u^{\mathrm{pr}}_t\|\le B_A$. Steps 1 to 5 hold with $Q$ the law under the protocol's strategy, since the step-3 moment depends only on $\|U_t-U^{\mathrm{pr}}_t\|$ (proven, sketch). Then (c) reads $\epsilon_b\le\Upsilon_{\mathfrak e}(\epsilon^{\mathrm{pr}}_b)$ with $\epsilon^{\mathrm{pr}}_b$ the protocol's exceedance probability. At $B_A=0$ it is the passive certificate of [thm-dataflow-composition] (c), since $\Upsilon_0(p)=p$. Smallest fix. State (c) with the protocol's strategy as reference and deviation bounded by $B_A$. Present it in the final document as one theorem, passive and bounded-active together, with $G^{\mathrm{agg}}_R$ as the instance of the other parts.

### ch-open-problem-five

Not blocking, due before the final document. Targets open problem 5 in `theory/CURRENT.md`. Two points. First, item (i) asks whether $\ln N^\star=(1/2+o(1))(R-1)B_A^2/\sigma^2$ while $\mathfrak e\le2d/5$. The answer depends on $\mathfrak e/d$. When $\mathfrak e/d\to0$ the answer is yes, by the sketch under Steering together with (c) (proven, sketch). When $\mathfrak e/d$ stays bounded away from zero, the natural candidate is the capacity of the Gaussian channel from the coalition's choice to $m_R$, $(d/2)\ln(1+2\mathfrak e/d)$, which lies strictly below $\mathfrak e$ (heuristic, from Shannon's coding theorem, cited from memory). Item (ii) already asks for the capacity form $d\ln(\sqrt{R-1}\,B_A/(\sigma\sqrt d))+O(d)$ at large $\mathfrak e/d$, so one question covers both regimes. Second, $N^\star$ counts Train calls, and each run of (c) costs $2R$ of them. A sharp constant in units of $\mathfrak e$ needs $\ln R=o(\mathfrak e)$. Smallest fix. Replace (i) by "Is $\ln N^\star=(1+o(1))\,\frac d2\ln(1+2\mathfrak e/d)$ as $\mathfrak e\to\infty$ with $\ln R=o(\mathfrak e)$, for every fixed ratio $\mathfrak e/d$?", record the regime $\mathfrak e/d\to0$ as known once the problem under Steering is proven, and merge (ii) into the same question.

### ch-lower-bound-transfer

Not blocking, due before the final document. Targets the transfer remark of [def-learning-oracle-model]. Smallest fix. Replace the reason by "since a certifier sound for $\theta'\ge\theta$ is sound for $\theta$". Replace the second sentence by "If, for every adversary of the stated procedure, some adversary of the larger procedure has a view from which one measurable map recovers the stated view under both hypotheses, then $\theta'\ge\theta$ by data processing." Add that honest clients whose updates enter a sum do not meet this condition.

### ch-scalar-noise-placement

Not blocking, due before the final document. Targets the Reading of [thm-dataflow-composition] (a)(iii). Smallest fix. One sentence. The bound applies when the decryptors add the protecting noise at decryption. If the clients add it inside their ciphertexts, the scalar multiplies it, and the attack gains nothing.

### ch-euclidean-norm-proof

Not blocking. Targets the application paragraph of [thm-smoothed-choice-certificate]. $B_A$ is a Euclidean bound. A range proof that bounds each coordinate by $b_\infty$ gives only $B_A=k_A\sqrt d\,b_\infty$, and then $\mathfrak e$ grows linearly in $d$, so the certificate is no longer free of $d$ in effect (proven, by $\|v\|_2\le\sqrt d\|v\|_\infty$). Smallest fix. Write "proves in zero knowledge that the Euclidean norm of its input is at most $B_A/k_A$", and leave the claim about which norms RoFL supports to a source that is opened.

### ch-poisson-reason

Not blocking. Targets the dropped item in `theory/CURRENT.md` and the label of [thm-bank-soundness]. Smallest fix. Replace the transparency reason by "Subsampling is a node of the procedure, and no theorem of this theory uses it, so the question is out of scope."

### ch-symbol-clash

Reopened, not blocking, due before the final document. The round-04 text adds nine clashes against the table of `theory/CURRENT.md`. $\ell_t$ is a learner name in the setting of $G^{\mathrm{agg}}_R$ and a likelihood ratio in step 2 of (c). $\mathfrak L$ is a class of learning functions in [def-certifier] and $\ln(1/p)$ in step 4 of (c). $E$ is a measurable set of views and $E_t$ the exceedance event of round $t$ in (a). $\mathrm H_2$ in lem-sphere-code (a) reads as a hockey-stick divergence of order two. $s$ is a seed name and the separation in lem-sphere-code (b). $\mathcal F_t$ is a filtration in (c) and $\mathcal F$ the ideal functionality. $u$ is a coalition input $u_t$, the round-1 shift in (e), and the code points $u^\pm_i$. $P,Q$ in step 2 of (c) clash with the view laws $P_b$ and the allowance $Q$. $A_t$ in (a) clashes with the coalition $A$, and $V$ in (c) with the cells $V_k$ and the view space $\mathcal V$. Also, the inversion remark uses $\mathrm H^{\to}_i$, $\delta_R$ and $F^{\to}$, none of which is in the table. Smallest fix. Rename locally in the final document, for instance $\mathrm h_2$, $\Lambda_t$ for the ratio, $\mathfrak l$ for $\ln(1/p)$, $\mathcal E_t$ for the exceedance event, $\mathcal F^{\mathrm{rel}}_t$, $v^\pm_i$ and $\mathbb P,\mathbb Q$.

## Steering

### Problem, the sharp constant (a strengthening of part (d) of [thm-smoothed-choice-certificate])

Claim (proven, sketch). Let $B<\infty$, $B_A>0$, $\eta\in(0,1)$, $\kappa\in(0,1)$, and let $a_\eta$ satisfy $\bar\Phi(a_\eta)=\eta/4$, so $a_\eta\le\sqrt{2\ln(2/\eta)}$ by (G3). Let

$$J_3=\min\Big\{\big\lceil e^{\kappa^2d/4}\big\rceil-1,\ \Big\lfloor\frac\eta2\exp\Big(\tfrac12\big((1-\kappa)\sqrt{2\mathfrak e}-a_\eta\big)_+^2\Big)\Big\rfloor\Big\}.$$

Every certifier of $\theta^{\mathrm{agg}}_R$ sound at level $\alpha$ over every learning function satisfies $\Pr_{\mathsf L^\circ}[\hat t\ge(1-\eta/2)\,\delta_{\mathcal N}(\varepsilon;B/\sigma)]\ge1-\alpha-N/J_3$. With $\kappa=2\sqrt{\mathfrak e/d}$, $\mathfrak e<d/4$ and $\mathfrak e\ge1$, whenever $(1-\kappa)\sqrt{2\mathfrak e}\ge a_\eta$ and the second argument of the minimum is at least one,

$$\ln J_3\ge\mathfrak e\Big(1-4\sqrt{\mathfrak e/d}\Big)-a_\eta\sqrt{2\mathfrak e}+\ln(\eta/2)-1 .$$

With the upper bound of the corollary, $\ln N^\star=(1+o(1))\,\mathfrak e$ as $\mathfrak e\to\infty$ with $\mathfrak e/d\to0$ and $\ln R=o(\mathfrak e)$, and $\epsilon_{\mathrm{acc}},\alpha,\alpha',\eta$ fixed. The constant of open problem 5 is then $1/2$ in units of $(R-1)B_A^2/\sigma^2$, and the transfer of part (c) is optimal in that regime.

Sketch. Write $\rho_c=(R-1)B_A$ and $s_c=\sigma\sqrt{R-1}$, so $\rho_c/s_c=\sqrt{2\mathfrak e}$. Code. Draw $J$ independent uniform sign vectors $\omega_k\in\{\pm1\}^d$. Hoeffding's inequality gives $\Pr[|\langle\omega_k,\omega_l\rangle|>\kappa d]\le2e^{-\kappa^2d/2}$, and a union bound over fewer than $J^2/2$ pairs leaves a code with $|\langle\mathbf q_k,\mathbf q_l\rangle|\le\kappa$ for $\mathbf q_k=\omega_k/\sqrt d$ whenever $J<e^{\kappa^2d/4}$. Strategy. $u_t=B_A\mathbf q_k$ for $t<R$ and $u_R=0$, so that $m_R=m_1+\rho_c\mathbf q_k+G$ with $G\sim\mathcal N(0,s_c^2I_d)$, as in the proof of (d). Decoding regions. With $\tau=\rho_c-a_\eta s_c$, let

$$V_k=\big\{m:\langle m-m_1,\mathbf q_k\rangle>\tau,\ \langle m-m_1,\mathbf q_l\rangle\le\tau\ \text{for every }l\neq k\big\},$$

which are measurable and pairwise disjoint. Each $\langle G,\mathbf q_l\rangle$ has law $\mathcal N(0,s_c^2)$, so

$$\Pr[m_R\notin V_k]\le\Phi\Big(\frac{\tau-\rho_c}{s_c}\Big)+(J-1)\,\bar\Phi\Big(\frac{\tau-\kappa\rho_c}{s_c}\Big)\le\frac\eta4+\frac J2\exp\Big(-\tfrac12\big((1-\kappa)\sqrt{2\mathfrak e}-a_\eta\big)^2\Big)\le\frac\eta2$$

for $J\le J_3$. The needles $\mathsf L_k$ of part (d) with these cells, and [lem-needle-lower-bound], give the bound. The expansion of $\ln J_3$ uses $(1-\kappa)^2\ge1-2\kappa$, $\lfloor y\rfloor\ge y/2$ for $y\ge1$, and $\lceil e^{\mathfrak e}\rceil-1\ge e^{\mathfrak e-1}$, which makes the second argument the smaller one.

Why it matters. It replaces the interval $[1/8,1/2]$ by the exact constant $1/2$ in the regime that matters for large models, $\mathfrak e\ll d$. It turns part (c) from a sufficient certificate into an optimal one there. The proof is one page and uses only (G3), Hoeffding's inequality and [lem-needle-lower-bound]. It is the only new problem, and round 05 should take it together with consolidation. The regime $\mathfrak e=\Theta(d)$ stays open, in the form of ch-open-problem-five.

### Consolidation

Round 05. The builder answers the seven challenges, proves the sharp constant, splits part (c) of [thm-smoothed-choice-certificate] into its own theorem in the reference-strategy form, with a new slug, and drafts `final/learning-oracle-theory.md` with the symbol table applied. Round 06. The challenger reviews the draft as if it were the final document, re-checks the split theorem and confirms all six definitions a second time.

### Prominent proofs for the final document

Present in full, in this order.

1. [lem-needle-lower-bound]. Short, and every lower bound of the theory uses it or the pair code.
2. [thm-coupling-certificate] (a) and (b). The chain from real leakage to the top oracle to the coupled divergence, and its certificate. This is the base of everything else.
3. [thm-dataflow-composition] (b) and (c). The hybrid and coupling argument through Gaussian releases for stateful clients and stopping strategies, and the passive certificate. Part (e)(ii) with [lem-sphere-code] (a) as the criterion-4 witness, about one page together.
4. The bounded-deviation transfer, part (c) of [thm-smoothed-choice-certificate] in the reference-strategy form, with part (d) and the sharp constant. This is the Rényi change of measure and its matching lower bound.
5. [thm-replay-audit-steer] (a) and (b). The one steering result, so that the document covers security as well as privacy.

State with a pointer to their rounds. [thm-perfect-substitution] and [thm-reference-access] (round 01 with round 02), [lem-atomless-two-point] (round 01 with corrections in rounds 02 and 03), [thm-black-box-certifiability] (rounds 01 and 02), [thm-active-choice-dichotomy] (rounds 03 and 04, with the adaptivity remark stated as an example), [thm-record-level-certificate] (rounds 03 and 04), [thm-bank-soundness] (rounds 01 to 04), parts (a), (b) and (e) of [thm-smoothed-choice-certificate] (round 04), [thm-dataflow-composition] (a) and (d) (rounds 02 to 04), and [lem-bank-fidelity] (round 01).

### Answers to the builder's questions

1. Yes, with ch-reference-strategy. State part (c) as a theorem of its own, for every isolated procedure, with the protocol's strategy as reference. $G^{\mathrm{agg}}_R$ stays the instance for (a), (b), (d) and (e).
2. No. Round 05 should settle the constant in the regime $\mathfrak e/d\to0$ by the sketch above. Leaving the regime $\mathfrak e=\Theta(d)$ open is acceptable, in the form of ch-open-problem-five.
3. The drop is accepted. The reason is not, by ch-poisson-reason.

### Convergence

This is review round four of at least six. No challenge is blocking. Definitions. All six are accepted in this file, five of them for the third time. [def-isolated-client] needs one more acceptance in round 05. Theorems. Eleven results stand accepted, seven of them NONTRIVIAL, well above the bar of six and three. The stopping rule can be met at round 06 if round 05 introduces no blocking challenge. The theory lacks no result for a finished document. What it lacks is the split of part (c), the sharp constant, the symbol pass and the final text.

## Verdicts

Six definitions and eleven results are judged. Seven results are NONTRIVIAL. No challenge is blocking.

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
VERDICT thm-coupling-certificate ACCEPT NONTRIVIAL
VERDICT thm-bank-soundness ACCEPT
VERDICT thm-dataflow-composition ACCEPT NONTRIVIAL
VERDICT thm-replay-audit-steer ACCEPT NONTRIVIAL
VERDICT thm-active-choice-dichotomy ACCEPT NONTRIVIAL
VERDICT thm-record-level-certificate ACCEPT NONTRIVIAL
VERDICT thm-black-box-certifiability ACCEPT NONTRIVIAL
VERDICT thm-smoothed-choice-certificate ACCEPT NONTRIVIAL
BLOCKING 0
```
