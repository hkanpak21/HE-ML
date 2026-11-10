---
model: claude-fable-5-1
discussant: defence-as-honest-constraint
date: 2026-10-29
round: 02
---

# Defence as honest constraint, round 02

The verdict first. Of the seven objects, I accept four and ask three revisions, with three blocking challenges, each with a one-line fix. The learning-attacker file's theorem is right at generative exponents one and two and wrong in its remainder and in its expectation above two, because the Haar kernel of a degree-three Hermite function has an eigenvalue of order $d^{-2}$ on a $d$-dimensional subspace, so the noisy gradient attacker's price in steps grows as $d^{\lceil(k^*+1)/2\rceil}$ and never as $d^{k^*}$ past degree two. The steering file's definition leaves the shift of a data poisoner undefined when the trainer is nonlinear, and its clause on correlational trainers mistakes label-linearity for degree two. The three formulations agree on more than they disagree. The disagreement that matters is about honest noise, which my round read as a defence and the steering file shows to be the steerer's cover, and I revise my definition and my conjecture to carry both. Section 3 gives the statement of the whole theory.

## 1. Verdicts

### 1.1 The learning attacker class

#### def-learning-attacker

Well posed as written (proven, by reading). The class $\mathcal L(\mathcal F,\ell,\mathcal O)$ with budget $(n,T,b,p)$ names what Halil's attacker is, and fact (a) says plainly that the name restricts nothing until one of three handles is applied. Fact (b) holds. The per-example square-loss update is affine in the secret, so its mean under a law is a correlational query plus a query on the view's marginal (proven, one line). Fact (c) holds. Status open is right for a definition awaiting a verdict.

Counterexample tried. Let the instance have no hidden frame, so the law of (view, secret) is fixed and known to the designer of the attacker. A readout $r$ fixed in advance may then be the Bayes decoder of the secret from the view, and the attacker reaches the optimum at $n=0$ observations and $T=0$ steps. The class therefore prices only instances whose frame is drawn per instance with positive entropy, which is the setting of every object that uses it, and the definition should say so. `ch-readout-needs-frame`, not blocking.

Known under another name. The attacker as one fixed algorithm is the attacker of 33 of the works in the sweep (`results.md`, the sweep statement of over 190 works). The function class with a divergence is capacity-bounded differential privacy (Chaudhuri, Imola and Machanavajjhala, NeurIPS 2019, Definition 3, as the file records from `fact-capacity-bounded-dp-function-class`). The definition goes past both by making the budget a vector in learning units.

Verdict ACCEPT.

#### thm-attacker-update-class-price

Parts (a), (b) and (e) are true as written and proven as stated. I rederived (a). The two step kernels are Gaussians with covariance $\eta^2\varsigma^2I_p$ and means $\eta\Delta_\theta(\phi_t)$ apart, so the chain rule gives $\mathrm{KL}=\sum_t\mathbb E_{\mathrm{null}}\|\Delta_\theta(\phi_t)\|^2/(2\varsigma^2)$, the null trajectory is independent of $\theta$, the average over $\theta$ is at most $T\bar\kappa/(2\varsigma^2)$, and Pinsker with Jensen gives $\sqrt{T\bar\kappa/(4\varsigma^2)}$ (proven). Part (b) is the two-term proof of `thm-noisy-trainer-two-term-filter` with the stated substitutions (proven).

Part (c) holds with one constant corrected. Under $\bar J$ the true covariance of the readout with $\varphi(S)$ is at most $c_0\sigma_\varphi/4$ and the test fires above $c_0\sigma_\varphi/2$, so the allowed deviation is $c_0\sigma_\varphi/4$ and Chebyshev's inequality with $\mathrm{Var}(r\varphi)\le\sigma_\varphi^2$ gives failure probability $16/(mc_0^2)$, which is $1/3$ at $m=48/c_0^2$ and $1/12$ at $m=192/c_0^2$. Under $J_\theta$ the allowed deviation is $c_0\sigma_\varphi/2$ and $m=48/c_0^2$ suffices. With $m=\lceil192/c_0^2\rceil$ the advantage is at least $31/48-4/48>1/2$ and the displayed bound $T\ge(1-2\delta_m)^2\varsigma^2/\bar\kappa$ follows as written, with $\delta_m$ at the larger $m$, still $o(1)$ (proven). `ch-chebyshev-constant`, not blocking, since the bound as written is unproven at the stated $m$ and not shown false.

Part (d) is right at $k^*\in\{1,2\}$ in its leading term and wrong in its remainder, and the expectation for $k^*\ge3$ is wrong. I recomputed the Haar kernels by the moments of the uniform law on the sphere. $K_1(x,y)=\langle x,y\rangle/d$ (proven). $K_2$ has eigenvalue $1/d$ on the radial function $(|x|^2-d)/\sqrt{2d}$, which the centring removes, and $2/(d(d+2))$ on the harmonic degree-two functions (proven, two Gaussian moments, as the file says). At degree three the Hermite function $h_3(\langle u,x\rangle)$ splits into a harmonic of degree three and the function $3\langle u,x\rangle(|x|^2-(d+2))/((d+2)\sqrt6)$, which is not frame-free and is not removed by centring, since $\bar h_3=0$. I computed $K_3$ on the two pieces:
$$K_3\big(y_1(|y|^2-(d+2))\big)=\frac{3}{d(d+2)}\,x_1(|x|^2-(d+2)),\qquad K_3(y_1y_2y_3)=\frac{6}{d(d+2)(d+4)}\,x_1x_2x_3,$$
and $K_3(y_1)=0$ (proven, from $\mathbb E_u[\langle u,x\rangle^3\langle u,y\rangle^3]=(6\langle x,y\rangle^3+9\langle x,y\rangle|x|^2|y|^2)/(d(d+2)(d+4))$, $\mathbb E_u[\langle u,x\rangle^3\langle u,y\rangle]=3|x|^2\langle x,y\rangle/(d(d+2))$, and the identity $\mathbb E[P(y)|y|^2]=(d+4)\mathbb E P(y)$ for a degree-four monomial $P$ under $\gamma_d$). So the top eigenvalue of the degree-three Haar kernel is $3/(d(d+2))$, of order $d^{-2}$ and not $d^{-3}$. Two consequences. At $k^*=2$ the term $k=3$ of the sum contributes $3a_3^2G^2/(d(d+2))$, the order of the leading term, so the remainder $O(G^2/d^3)$ is false whenever $a_3\neq0$, and the correct display is $\bar\kappa\le(2a_2^2+3a_3^2)G^2/(d(d+2))+O(G^2/d^3)$. The price $T\ge c\,\varsigma^2d^2/G^2$ survives with $c$ depending on $a_2$ and $a_3$. For general $k$ the lowest non-trivial harmonic in $h_k(\langle u,\cdot\rangle)$ has degree one or two, its mass is of order $d^{-\lfloor(k-1)/2\rfloor}$, and its Haar eigenvalue is $1/d$ or $2/d^2$, so the top eigenvalue of the degree-$k$ kernel is $\Theta(d^{-\lceil(k+1)/2\rceil})$ (heuristic for $k\ge4$, by the same decomposition, not computed). The noisy gradient attacker's price in steps is therefore $d^{\lceil(k^*+1)/2\rceil}$, which equals $d^{k^*}$ at $k^*\in\{1,2\}$ and is about the statistical-query exponent $k^*/2$ plus one half above. The cross terms between degrees are handled by the Cauchy and Schwarz inequality on the pairs $(|a_k|\sqrt{\lambda_k},\|f_k\|)$, since $\tilde h_k^u$ lies in the degree-$k$ Hermite space and sees only the degree-$k$ component $f_k$ of $\partial_jg$, which gives $\bar\kappa\le G^2\sum_{k\ge k^*}a_k^2\lambda_k$ exactly (proven). `ch-lower-harmonics`, blocking, since the remainder of (d) at $k^*=2$ is false when $a_3\neq0$. The fix is the display above.

A second constant. $G$ bounds the per-example update $(g_\phi(v)-s)\nabla g_\phi(v)$ in (b) and $\sum_j\|\partial_jg_\phi\|^2_{\gamma_d}$ in (d), two different quantities, and (d) needs its own name, say $G_\nabla$. `ch-two-gradient-bounds`, not blocking.

Known under another name. The bound in (a) is the cross-predictability bound on noisy gradient descent (Abbe and Sandon, arXiv 2020, library key AS20, unread, and Shalev-Shwartz, Shamir and Shammah, ICML 2017, from memory, unverified). Their argument bounds the top eigenvalue of the frame kernel by $\sqrt{\mathrm{tr}K^2}$, the square root of the cross-predictability, which at degree $k$ is of order $d^{-k/2}$. The exact eigenvalue here, $2/(d(d+2))$ at degree two against $\sqrt3/d$, is the sharpening, and it is the one new computation of the object. Moving the bound from the trainer to the attacker is the file's idea and it is right. `ch-known-as-cross-predictability`, not blocking, a uses line.

Status sketch is right. Verdict REVISE.

#### prop-attacker-is-trainer-under-nature

True as written in each part, since each part is stated under its own hypothesis (proven, by reading, with (a) a tautology and (b) to (d) borrowed). Status sketch is right for (e).

One challenge of scope. Part (a) is stated for a release that answers with $m_P(x)$, the Bayes regression function, plus nature's noise. That is the Bayes release of item 16. A trained release answers with $\hat m(x)$, so the attacker's observations have the law of $P$ with the trained parameter in place of the true one, and the attacker's price to come within a factor $1+\kappa$ of the trainer's risk is $n/\kappa$ by item 34 part (e), which equals the trainer's price at $\kappa=1$ and exceeds it below. The title's "exactly when its observations are the trainer's data in law" holds for the Bayes release and holds for the trained release only up to the factor $1/\kappa$, which the file's own citation of item 34 carries. `ch-bayes-release-not-trained-release`, not blocking, one sentence in (a) and in the title.

Counterexample tried for (e). A secret that is the trainer's target, a channel at nature's noise, and an attacker class contained in one for which the release is indistinguishable from the data. The three conditions make the attacker a trainer on $P$ up to the parameter shift above, and I found no case where a lower bound for $\mathcal C$ on $P$ fails to transfer. The sketch is right.

Verdict ACCEPT.

#### prop-capacity-coordinate

True as written (proven, by the cited results). Part (a) uses agreement and risk as complements, which assumes a zero-one score, and the definition should say so. Part (e) is the reading my round 00 gave, that the capacity acting in every lower bound is the degree of the statistic read. One remark. $p_{\min}(s)$ at unbounded samples ignores optimization, and a family may need $p$ well above $p_{\min}$ to be trainable by $\mathcal O$ at all, which is empirical and places the measured capacity above the left edge. `ch-capacity-domain-edge`, not blocking.

Verdict ACCEPT.

### 1.2 The steering attacker

#### def-steering-attacker-price

The definition is right in its frame and ill-posed in one clause. For record setting it defines the shift as $v_t=\nabla L_{D'}(\theta_t)-\nabla L_D(\theta_t)$ and then calls the shift "the sequence $(v_t)_{t<T}$", with its deviation budget $\max_t\|v_t\|$ and its push-to-noise budget $\sum_t\|v_t\|^2/(2\varsigma^2)$. For a trainer whose gradient is nonlinear in $\theta$ the shift is a function $\theta\mapsto v_t(\theta)$, the honest and the steered trajectories visit different points, and the definition does not say along which trajectory the sequence is read. The stealth bound of `thm-noisy-gradient-query-filter` (a) reads it along the honest trajectory in expectation, and the response reads it along the steered one. For label poisoning of a linear model the shift is the constant $-\Delta$ and nothing is lost, which is why the instance below stands. `ch-shift-along-which-trajectory`, blocking for the record-setting and in-transit clauses, since the deviation budget and $\mathfrak e$ are undefined there. The fix is one sentence: the shift is the map $v_t(\theta)$, the deviation budget is $\sup_{t,\theta}\|v_t(\theta)\|$, and the push-to-noise budget is $\mathbb E\sum_t\|v_t(\theta_t)\|^2/(2\varsigma^2)$ along the honest trajectory.

The response constant is right. I rederived the contraction. With $\eta\le1/L$ and $\mu$-strong convexity, $\|D_t-\eta(\nabla L(\theta'_t)-\nabla L(\theta_t))\|\le(1-\eta\mu)\|D_t\|$, so $\|D_{t+1}\|\le(1-\eta\mu)\|D_t\|+\eta B_A$ and $\|D_T\|\le B_A/\mu$, and under smoothness alone the factor is $1+\eta L$ (proven).

Seed grinding, used in the next object, chooses a seed and is none of the three kinds of choice, so it is outside this definition as written. `ch-seed-is-a-fourth-choice`, not blocking, add the seed as a choice with zero shift.

Known under another name. The response constant is the uniform stability of the trainer (Bousquet and Elisseeff, JMLR 2002, from memory, unverified). The push-to-noise budget of a trajectory is the Gaussian differential privacy parameter of $T$ compositions, $\mu_{\mathrm{GDP}}^2/2$ with $\mu_{\mathrm{GDP}}=\sqrt T B_A/\varsigma$ (Dong, Roth and Su, JRSS-B 2022, from memory, unverified). The influence of a record on the trainer through its gradient is the influence function (Koh and Liang, ICML 2017, from memory, unverified). The definition's content is to put these three in one object with the auditor's class as a parameter, which none of them does.

Status open is right. Verdict REVISE.

#### prop-label-poison-stealth-response

True as written. I redid the arithmetic the author asked a second reader to redo. Along an eigendirection $D_{T,\lambda}=\Delta_\lambda(1-r_\lambda^T)/\lambda$ and $\mathrm{Var}=\eta^2\varsigma^2(1-r_\lambda^{2T})/(1-r_\lambda^2)$, and with $1-r_\lambda^2=\eta\lambda(2-\eta\lambda)$ and $1-r^{2T}=(1-r^T)(1+r^T)$ the quotient is the formula of (a) (proven). Each term is at most $2\Delta_\lambda^2/(\eta\mu\varsigma^2)$, which sums to $(2/(\eta\mu T))m_{\mathrm{traj}}^2$ (proven). The Cauchy and Schwarz step in the $\Sigma_T$ inner product, the inversion $m\le m(\delta)$, the bound $\|D_T\|\le\|\Delta\|/\mu$, and $\|\Sigma_T\|\le\eta\varsigma^2/\mu$ for the displacement of (d) all hold (proven). The factor of (b) is a gain only when $\eta\mu T\ge2$, which the statement should say.

One wording. In (d), $k$ records produce $\|\Delta\|$ with label changes of total weighted size at least $n\|\Delta\|$, with equality when aligned, and the file writes "at most". `ch-write-budget-direction`, not blocking.

Known under another name. The trajectory separation $m_{\mathrm{traj}}=\sqrt T\|\Delta\|/\varsigma$ is the Gaussian differential privacy parameter of $T$ Gaussian mechanisms with sensitivity $\|\Delta\|$ (Dong, Roth and Su, from memory, unverified). The gain of the final-model auditor under strong convexity is the last-iterate privacy of noisy gradient descent, where the privacy loss of $\theta_T$ stays bounded while the trajectory's grows as $\sqrt T$ (Chourasia, Ye and Shokri, NeurIPS 2021, from memory, unverified, and privacy amplification by iteration, Feldman, Mironov, Talwar and Thakurta, FOCS 2018, from memory, unverified). The exact formula of (a) and its reading as a cap on the trigger response are the object's own. `ch-known-as-last-iterate-privacy`, not blocking, a uses line.

Status sketch is right. Verdict ACCEPT.

#### prop-secret-target-planted-detection

Parts (a), (b), (c) and (e) hold. In (a) the indicator auditor has advantage $s-s^\circ$ and the Hoeffding count is right (proven). In (e) the chi-square of the mixture against the honest Gaussian is $\mathbb E\exp(m_T^2\langle u,u'\rangle)-1$, and with $\mathbb E\langle u,u'\rangle^2=1/d$ and $\mathbb E\langle u,u'\rangle^4=3/(d(d+2))$ the expansion $m_T^4/(2d)+O(m_T^8/d^2)$ follows (proven, the second-moment method). The detection boundary $m_T\gg d^{1/4}$ is the mean of the chi-square statistic against its standard deviation $\sqrt{2d}$ (proven).

Part (d) is false in its last sentence. A correlational trainer reads the label linearly and reads the view through arbitrary functions, the coordinates of its update. For the linear model those functions have degree at most two in the record, and a planted law that differs from the honest one only at Hermite degrees three and above leaves the population gradient unchanged, so the clause holds there. For a trainer whose update has every degree, a two-layer network, a planted law at degree three moves the population gradient and steers, while a statistical-query auditor on the data pays $d^{3/2}$ to detect it. So "against a correlational trainer, stealth at degree above two and steering are incompatible" holds for trainers whose per-example update is a polynomial of degree at most two, the linear model, and fails in general. `ch-correlational-is-not-degree-two`, blocking for that sentence. The fix names the trainer's update degree in place of its label-linearity.

Two notes. In (c), the scaling of $\lambda_{k^*}$ by the mixture weight $\varepsilon$ is exact, since the coefficients of $dP_\varepsilon/dP_0-1$ are linear in $\varepsilon$, so the label heuristic can be proven. `ch-mixture-weight-is-exact`, not blocking. In (a), seed grinding sits outside `def-steering-attacker-price` as written, see above. `ch-grinding-outside-definition`, not blocking.

Known under another name. The detection boundary of (e) is the Gaussian mean testing boundary (Baraud, Bernoulli 2002, from memory, unverified, as the file says). Parts (b) and (c) are borrowed and say so.

Status sketch is right. Verdict REVISE.

### 1.3 Challenges

| Challenge | Object | Blocks |
| --- | --- | --- |
| `ch-readout-needs-frame` | `def-learning-attacker` | no |
| `ch-chebyshev-constant` | `thm-attacker-update-class-price` (c) | no |
| `ch-lower-harmonics` | `thm-attacker-update-class-price` (d) | yes |
| `ch-two-gradient-bounds` | `thm-attacker-update-class-price` (b), (d) | no |
| `ch-known-as-cross-predictability` | `thm-attacker-update-class-price` | no |
| `ch-bayes-release-not-trained-release` | `prop-attacker-is-trainer-under-nature` (a) | no |
| `ch-capacity-domain-edge` | `prop-capacity-coordinate` (a) | no |
| `ch-shift-along-which-trajectory` | `def-steering-attacker-price` | yes |
| `ch-seed-is-a-fourth-choice` | `def-steering-attacker-price` | no |
| `ch-write-budget-direction` | `prop-label-poison-stealth-response` (d) | no |
| `ch-known-as-last-iterate-privacy` | `prop-label-poison-stealth-response` | no |
| `ch-correlational-is-not-degree-two` | `prop-secret-target-planted-detection` (d) | yes |
| `ch-mixture-weight-is-exact` | `prop-secret-target-planted-detection` (c) | no |
| `ch-grinding-outside-definition` | `prop-secret-target-planted-detection` (a) | no |

## 2. Conflicts

Six places where the three formulations differ, with the side I keep.

1. Honest noise, defence or cover. My round 01 priced the trainer's noise $\varsigma$ as a defence against every observer, with security price $(1+b\varsigma^2/\mu_2)^2$. The steering file shows that the same noise is what gives a steerer stealth. Under stealth $\delta$ against a trajectory auditor the stealthy displacement is $\varsigma\,m(\delta)/(\mu\sqrt T)$, linear in $\varsigma$, and at $\varsigma=0$ no nonzero shift is stealthy. Both are true, so a security price must be indexed by the task. I concede and revise `def-honest-constraint-defence` below. The learning-attacker file is silent on this.

2. Whether a defence can have a security price against a learner class. My round 01 said every defence the theory can prove binds every observer and none a learner class. The learning-attacker file's theorem, once revised, gives a lower side in steps for the noisy gradient attacker through the update-shift energy $\bar\kappa$, and a defence changes $\bar\kappa$. I concede that a class-specific security price now has a proven lower side, $\bar\kappa^{\Pi}/\bar\kappa^{\Pi'}$, and add it to the definition. I keep the critique that the class is not the attacker in practice. The handle is noise the attacker injects into its own updates, which a shadow model or a VAE trained at fine precision does not do, and the file says as much in its limits.

3. The reading of item 34. The learning-attacker file reads it as the condition under which the attacker pays what the trainer paid. My round 01 reads it as a defence priced in the trainer's records. The two compose. The defence is the move that brings the release to nature's law, and the equality is why the price then meets the trainer's. We differ on one point. The file's (a) is stated for the Bayes release, and the trained release gives the price $n/\kappa$, not $n$, so the attacker pays the trainer's price only at $\kappa=1$. I keep my reading and have raised the challenge.

4. The unit. The learning-attacker file prices in steps at a noise level with a budget vector $(n,T,b,p)$. The steering file prices in a deviation budget and a push-to-noise budget. My round prices a defence as a ratio along one budget coordinate. All three agree that a price is a set of budgets and that the exponent alone is no unit (item 28). I keep the ratio along one coordinate as the form of a defence's price and take the two files' coordinates as the coordinates it may run along.

5. Attacker-planted structure. The steering file says the attacker's planting escapes the planting objection and yields attack results only. My round put the ban on planting in the instance class, the record laws the designer did not choose. These agree. A defence against a steerer must hold for every shift the steerer may choose within its deviation budget, which is the uniformity my definition asks for with the attacker's choices in place of the record law. No change.

6. The trainer's cost. Neither file prices what the trainer or the honest consumer pays for a defence, and the steering file's response constant is the trainer's loss under a steer, not under a defence. My definition is the only one with a utility price, and I keep it. The response constant and the utility price are both stability quantities of the trainer, and the oracle reads both from coupled runs and training curves.

### def-honest-constraint-defence: a defence and its two prices

status: open

uses: def-learning-oracle, def-uniform-security-profile, def-hard-problem-mapping, prop-profile-run-coordinate, def-learning-attacker, def-steering-attacker-price, thm-attacker-update-class-price

Revised from round 01 in three places. The security price is indexed by the task and the class and admits a steer task. The same-class clause names the trainer's components of `def-learning-attacker`. A remark gives the class-specific lower side.

Definition. Let $\Pi$ be a procedure whose trainer has components $(\mathcal F,\ell,\mathcal O)$ in the sense of `def-learning-attacker`. Fix a trainer target, a population risk $R$, and let $\beta^{\Pi}_{\mathrm{tr}}(r)$ be the least trainer budget, in records, runs or steps, at which the honest output of $\Pi$ reaches risk $r$. Fix a task $\tau$, an attacker class $\mathcal A$ with a budget, a success functional, and an instance class $\mathfrak J$ of record laws, and write $\mathrm{price}^{\Pi}_{\mathcal A}(\tau,s)$ for the price of $\mathcal A$ at success $s$ on $\tau$ over $\mathfrak J$ under $\Pi$. A *defence* $\Delta$ maps $\Pi$ to a procedure $\Pi'=\Delta(\Pi)$ with three properties.

- Key-free. Every randomness $\omega$ that $\Delta$ introduces has a public law, is independent of all other randomness, is read by one node of $\Pi'$, and reaches no party as a value.
- Every run. The honest parties run $\Pi'$ at every execution, so the honest law of the attacker's view under $\Pi'$ may differ from its law under $\Pi$.
- Same components. The trainer of $\Pi'$ has the components $(\mathcal F,\ell,\mathcal O)$ of the trainer of $\Pi$, with the defence's kernel applied to the values the dataflow carries and not to the learner.

The *utility price* of $\Delta$ at risk $r$ is $\upsilon_\Delta(r)=\beta^{\Pi'}_{\mathrm{tr}}(r)/\beta^{\Pi}_{\mathrm{tr}}(r)$, infinite when $\Pi'$ never reaches $r$. The *security price* of $\Delta$ against $\mathcal A$ on $\tau$ at success $s$ is $\pi_\Delta(\mathcal A,\tau,s)=\mathrm{price}^{\Pi'}_{\mathcal A}(\tau,s)/\mathrm{price}^{\Pi}_{\mathcal A}(\tau,s)$ along one budget coordinate, and along a family indexed by $d$ the two prices are compared in exponent. For a steer task the class is the steering attackers of `def-steering-attacker-price` at stealth $\delta$ against a named auditor class, the budget coordinate is the deviation budget, and the success is the displacement or the trigger response, so that $\pi_\Delta<1$ says the defence widens what a stealthy steerer reaches. A defence is *priced* when $\upsilon_\Delta$ and $\pi_\Delta$ are stated, with their status, for every task the statement names. It is *admissible against planting* when the lower side of each $\pi_\Delta$ holds for every law in $\mathfrak J$ and every choice of the steerer within its budget, with $\mathfrak J$ fixed before $\Delta$ is chosen.

Measurement (proven, from the definitions). The oracle runs $\Pi$ and $\Pi'$. Each $\beta_{\mathrm{tr}}(r)$ is read off the declared trainer's risk curve with a confidence band from held-out records. The upper side of each attacker price is a declared attack of $\mathcal A$ with a lower confidence band on its success (`prop-profile-run-coordinate` (b)), and its lower side is a theorem, as `def-known-price` requires. For a steer task the response is read off coupled runs and the auditor's advantage is bounded below by a two-sample test on drawn runs (`def-steering-attacker-price`, Measurement).

Remarks. (i) Programming is not a defence. A programming of the oracles of $\Pi'$ measures $\Pi'$ and leaves its prices within $\varepsilon$ in success (proven, `prop-programming-preserves-prices` (b) with $Z$ the parties' views). (ii) The key-free clause concerns what $\Delta$ introduces. The honest procedure's own randomness, a client's seed among it, is judged by decision 4. (iii) A kept key fails the first clause, so encryption under a key and a direction a designer hides and keeps are not defences, which is the plug-in exclusion for defences, and the carrier clause of `def-hard-problem-mapping` covers the rest. (iv) Against the noisy gradient attacker class of `def-learning-attacker` with injected noise $\varsigma_A$, the lower side of the price in steps is $\varsigma_A^2/\bar\kappa$ up to the factor $(1-2\delta_m)^2$ (`thm-attacker-update-class-price` (c), sketch), so the security price against that class has lower side $\bar\kappa^{\Pi}/\bar\kappa^{\Pi'}$, the ratio of the update-shift energies of the two shadow games, which the oracle measures along the attacker's own trajectory (proven given that theorem). A defence that makes the view's law free of the secret has $\bar\kappa^{\Pi'}=0$ and infinite security price against every class, as normalization at a median fit does (item 33).

Other regime and the oracle. As in round 01. The definition is regime-free, since $\mathcal A$ and $\tau$ are parameters.

### conj-honest-noise-matched-budget: honest noise is paid once by the trainer, twice by the passive observer, and widens the stealthy steerer once

status: open

uses: def-honest-constraint-defence, def-optimum-update-stream, prop-update-direction-fano-recovery, thm-norm-weighted-update-pca, thm-same-units-gap-gaussian-mechanism, prop-label-poison-stealth-response, def-steering-attacker-price

Setting and parts (a) to (d) as in round 01, with $\Pi_\varsigma=\Delta_\varsigma(\Pi_0)$ the stream in which each client adds $\zeta_t\sim N(0,\varsigma^2I_d)$ to its update, the server averaging $K$ updates per round with step $\eta$ on a population square loss of Hessian $I_d$ and per-example gradient covariance $\mu_2I_d+c_2uu^\top$ at the optimum. Along $d\to\infty$ at fixed $b$, $\varsigma$, $K$ and label law:

- (a) Against every passive observer of $T$ client updates, $\pi_{\Delta_\varsigma}=(1+b\varsigma^2/\mu_2)^2(1+o(1))$ (heuristic, as in round 01).
- (b) For the server, $\upsilon_{\Delta_\varsigma}(r)=(1+b\varsigma^2/\mu_2)(1+o(1))$ (heuristic, as in round 01).
- (c) The passive observer pays $1+b\varsigma^2/\mu_2$ times what the trainer pays, the shape of `thm-same-units-gap-gaussian-mechanism` (heuristic, from (a) and (b)).
- (d) For the statistic class the same holds up to $1+\mathrm{Var}(W^2T(W))/(b\,c_2^2)$, if fable's batching claim holds (open).
- (e) Steering. Let one client be a steering attacker whose shift on its own update at round $t$ is $v_t$, and let the auditor be the server watching that client's $T$ updates. The client's push-to-noise budget is $\sum_t\|v_t\|^2/(2\varsigma^2)$, and under stealth $\delta$ against the server the displacement of the server's model at the end is at most of order $\varsigma\,m(\delta)/(K\sqrt T)$ times the response constant, linear in $\varsigma$ (heuristic, `prop-label-poison-stealth-response` (c) and (d) with the client's update stream as the audited view, the factor $1/K$ from averaging, and the response constant of `def-steering-attacker-price`, which is one for a Hessian $I_d$ at $\eta\le1$). So $\pi_{\Delta_\varsigma}$ on the steer task, with the deviation budget as coordinate and the displacement as success, is of order $1/\varsigma$ relative to any fixed $\varsigma_0>0$, and at $\varsigma=0$ no nonzero shift is stealthy against the server (proven, the two trajectories then differ with probability one).

What settles it. (a) and (b) as in round 01. (e) needs the response of the averaged noisy chain to a one-client shift, a two-line extension of the linear instance (open, expected proven). The experiment adds to the round-01 runs one steering client with a constant label shift at three deviation budgets, and records the server's displacement and a classifier two-sample test on the client's updates at $\varsigma^2\in\{0,\mu_2/b,4\mu_2/b\}$. The prediction is that the largest stealthy displacement grows linearly in $\varsigma$ while the passive observer's price grows as its square and the server's rounds as its first power.

Admissibility and the other regime. As in round 01. The steer part is statistical and binds every auditor.

## 3. A statement of the whole theory

The theory prices the parties of a learning procedure in the units of learning and proves and measures the same prices.

Objects. A learning function $\mathsf L(x;\rho,\xi)$ maps a training input, a seed and hardware randomness to a model. The learning oracle serves it through $\mathsf{Train}$, $\mathsf{Eval}$ and $\mathsf{Open}$, in a named mode that reuses seeds and a drawn mode that cannot, and it is realizable by the real procedure, invisible to an unbounded attacker, and visible to a certifier through the seed name alone (proven, items 1 to 3). A procedure is a dataflow of learning nodes and channels, and its parties, the trainer, the attacker, the auditor and the designer, each hold a view and choices. The twin of a run is the same seed on a neighbouring dataset, and the coupled divergence over twins certifies leakage for every learning function (proven, items 3 to 8). A defence is a key-free change to the procedure run at every execution, and a programming fixes an oracle's values to measure a fixed procedure and moves no price (proven, item 10).

Attacker classes. Every observer, bound by the information in its view. The statistical-query class and the statistic class, bound by what they read. The learning attacker, a declared family, loss, optimizer and readout with budget $(n,T,b,p)$, bound through what it reads, through noise it injects into its own updates, or through an assumption on every efficient algorithm, and never by the word learner alone (proven, AKMSS21 Theorem 1a). The polynomial-time class under a named assumption, in a game never mixed with the first (Halil, 2026-10-25). The steering attacker, an additive shift on the trainer's update stream with a deviation budget and a push-to-noise budget, faced by an auditor of a named class. The trainer and the auditor are learners of the same kind.

Prices. A price is the set of minimal budgets at which some member of a class reaches a success level on every instance of a class of record laws (finite, Dickson's lemma). It is a vector, and comparisons with the trainer run along one coordinate or in exponent, since the exponent alone is no unit (proven, item 28). A price is known within a factor when a declared attack's measured budget, with a lower confidence band on its success, lies within that factor of a proven lower side, and one price is known, within 86 (empirical and proven, item 31). A defence carries two prices, what honest training pays and how the price of a named class on a named task moves, both measured by running the defended and the undefended procedure (proven, by definition).

What the theory claims. The statistical prices of shadow runs, reconstruction, membership and update observation are exact (proven, items 11 to 19). Every computational price maps the attack onto statistical queries, a low-degree method or a lattice problem, and each needs structure in the record law along a hidden direction (proven under named assumptions, items 20 to 28). The attacker pays what the trainer paid exactly when its observations are the trainer's data in law, and in general neither inequality holds (proven, with the trained release at the factor $1/\kappa$). A noisy gradient attacker pays in steps $\varsigma^2/\bar\kappa$, with $\bar\kappa$ the variance over frames of its mean update, of order $d^{\lceil(k^*+1)/2\rceil}$ in a Gaussian frame family (sketch). Honest noise on updates is paid once by the trainer, twice by the passive observer, and widens the stealthy steerer once (heuristic). A stealthy label poisoner of noisy gradient descent on a linear model moves the trigger response by a few honest standard deviations when its direction is known and by order $d^{1/4}$ when secret, and a trajectory auditor cuts both by $\sqrt{\eta\mu T/2}$ (proven). Attacker-planted structure yields attack results and never a defence theorem (proven, by the roles).

What it aims to prove. A lower bound for a gradient learner of a fixed architecture at fine precision, without injected noise, on a law outside the single-index family (open, the core). A natural learning problem that yields a one-way function (open). A defence priced against a learner class at a matched budget, with the attacker in the trainer's class (open, the cell is unclaimed in the literature).

Scope and exclusions. No planted hard problem carries a lower bound unless training itself produces the structure, and the ban lives in the instance class (Halil, 2026-10-25 and 2026-10-27). No kept key, so no cryptographic plug-in, and whether a seed generator's pseudorandomness is one is Halil's decision 4. A real seed is a short key and caps every seed-blind bound at the number of seeds (proven, item 20). Results in exact arithmetic say so (items 21 to 23). The natural-data oracle is parked. The two games are never mixed.

Measurement. The oracle supplies the runs. The measured side of an attack is a declared attack's lower band on success at a budget, the measured side of a trainer is its risk curve, coupled runs certify leakage and read the response to a steer, and drawn runs supply every baseline. On real data only the measured side exists, since no law is stated (proven, section 6 of the reading of 29 October), and the proven side enters through laws the experimenter builds or through bounds uniform over every learning function.

## Verdicts

```text
VERDICT def-learning-attacker ACCEPT
VERDICT thm-attacker-update-class-price REVISE
VERDICT prop-attacker-is-trainer-under-nature ACCEPT
VERDICT prop-capacity-coordinate ACCEPT
VERDICT def-steering-attacker-price REVISE
VERDICT prop-label-poison-stealth-response ACCEPT
VERDICT prop-secret-target-planted-detection REVISE
BLOCKING 3
```
