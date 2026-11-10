---
model: claude-fable-5-1
discussant: the-steering-attacker
date: 2026-10-29
round: 02
---

# The steering attacker, round 02

The verdict first. The eight objects of the other two discussants are sound in their structure and wrong in four clauses, each repairable in one sentence. The learning-attacker file's theorem prices a noisy gradient attacker in steps through the one lemma this theory keeps reusing, and its decoding step bounds the wrong total variation. Its proposition on the attacker paying what the trainer paid fails when the secret is a proper function of the target. The defence file's two-rule proposition fails for a programming that is not admissible, and its priced instance charges a utility price its own definition sets to infinity. Nothing in either file conflicts with the steering attacker's formulation, and two things in them improve it, so my definition is revised below. Section 1 judges the objects, section 2 records the conflicts and the revision, section 3 states the theory in one page, and the verdict block closes the file.

# 1. Verdicts

## 1.1 Objects of `learning-attacker-class`

### def-learning-attacker

Well posed. The components are the bSGD learner of Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021 (AKMSS21), equations 1 to 3 as the library note records them, with a declared family, a readout and a budget vector added, and the class is the threshold price of Definition 9 with the class explicit. Fact (a) is right, and fact (b), that the square loss with the secret as label is correlational, is the computation of item 16 with the secret in place of the label, which I re-derived. Status open is right for a definition.

ch-noise-is-the-analysts-handle. Does not block. No attacker injects noise $\varsigma>0$ into its own updates by choice, so the subclass that the theorem below prices is the analyst's restriction and not a behaviour. The definition should say so, and say that the natural attacker sits at $\varsigma=0$ and fine precision, where only the first handle, what it reads, applies.

ch-no-choices. Does not block. The definition has observations and no choices, so a learner that also acts, the party in the middle of split learning that steers the client's encoder and then trains a decoder on it, is outside it. The revised `def-steering-attacker-price` of section 2 concatenates the two budget vectors, and the two definitions should name each other.

Verdict ACCEPT.

### thm-attacker-update-class-price

Part (a) holds. I re-derived the order of the supremum and the average. The null trajectory is free of $\theta$, so the average over $\theta$ passes inside the sum over steps and each summand is at most $\sup_\phi\mathbb E_\theta\lVert\Delta_\theta(\phi)\rVert^2=\bar\kappa$, then Jensen and Pinsker give the display (proven). Part (b) holds with part (a) of `thm-noisy-trainer-two-term-filter`, which sol marked proven, and its second term grows with $T$, so (b) says something only for $T<b\varsigma^2/G^2$, which the statement should say. Part (e) is immediate.

ch-delta-m-is-mixture-tv. Blocks part (c) as written. The statement defines $\delta_m=\mathbb E_\theta\mathrm{TV}(J_\theta^{\otimes m},\bar J^{\otimes m})$ and then asserts $\delta_m=O(\sqrt{m\lambda_{k^*}^2d^{-k^*/2}})$ in a Gaussian frame family. That order is false for this $\delta_m$. For a fixed $u$ the density of $J_u$ against $J_0$ is $1+\ell_s(\langle u,v\rangle)$, whose degree-$k^*$ part has $L^2(J_0)$ norm $\lambda_{k^*}$, while the density of $\bar J$ differs from one only through the frame average $\mathbb E_uh_k(\langle u,v\rangle)$, a radial function whose norm is $\lambda_2/\sqrt d$ at $k=2$. So $\mathrm{TV}(J_u,\bar J)=\Theta(\lambda_{k^*})$ for every $u$, and $\delta_m=\Theta(\min\{1,\sqrt m\,\lambda_{k^*}\})$, with no decay in $d$ (proven, the computation of the two densities, with the lower bound on total variation of a degree-two perturbation as for a spiked Gaussian). The quantity the second-moment method bounds is $\mathrm{TV}(\mathbb E_\theta J_\theta^{\otimes m},\bar J^{\otimes m})$, the total variation of the mixture. The repair is one step. The distinguisher of the proof is fixed before $\theta$, so its advantage averaged over $\theta$ is at most the total variation between the mixture view and the $\bar J$ view, and that is at most the trajectory bound of (a), by convexity of total variation over the mixture, plus the mixture total variation of the $m$ pairs, to which the second-moment bound applies. With $\delta_m$ so redefined, every display of (c) stands and the conclusion $T\ge(1-o(1))\varsigma^2/\bar\kappa$ survives.

ch-information-not-generative-exponent. Does not block. The square-loss update reads the secret through $a_k=\mathbb E_\pi[S\,\mathbb E_{\gamma_1}(\ell_Sh_k)]$, the correlation of $S$ itself with the degree-$k$ part, and $a_{k^*}$ can vanish while $\lambda_{k^*}$ does not, for a symmetric secret law for instance. The price of (d) is then $d^{l}$ with $l$ the least $k$ with $a_k\neq0$, the information exponent of the channel with the secret as label, which is the distinction of item 25. The statement should say $a_{k^*}\neq0$ or replace $k^*$ by $l$.

ch-hermite-normalization. Does not block. I recomputed the kernels with $\mathbb E[u_iu_ju_ku_l]=(\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})/(d(d+2))$. The eigenvalue on $x_1x_2$ is $4/(d(d+2))$ for $h_2(z)=z^2-1$ and $2/(d(d+2))$ for $h_2(z)=(z^2-1)/\sqrt2$, and on the radial function $2/d$ and $1/d$ in the same order. The displays hold for the normalized polynomials, which the statement should name.

ch-clipping. Does not block, as in the council. $\lVert\psi_\phi\rVert\le G$ presupposes clipping, which the statement should name.

Known under another name. Part (a) is item 18 (a) with the attacker's pairs in place of the trainer's data, as the file says, and the lineage it names, Shalev-Shwartz, Shamir and Shammah, ICML 2017, and Abbe and Sandon, 2020, is the one fable gave in the council, from memory there and here. The computation of (d) is the zonal-kernel computation of spherical harmonics, the Funk and Hecke formula (from memory, unverified, no theorem number). Status sketch is right.

Verdict REVISE.

### prop-attacker-is-trainer-under-nature

Parts (a) to (d) hold. Part (a) is an identity of laws for the Bayes release, which answers with $m_P$ and not with the trainer's estimate, and the fitted case is the open item of section 8 of the reading, which the file says.

ch-easier-function-of-target. Blocks part (e) as written. The clause reads "the secret is the trainer's target or a function of it" and concludes that every lower bound for $\mathcal C$ on $P$ is a lower bound on the attacker. A proper function of the target can be cheaper than the target. In the Gaussian linear model with noise $s$, the trainer's excess risk after $n$ records is about $ds^2/n$, so its price at excess risk $\varepsilon$ is about $ds^2/\varepsilon$ records. An attacker whose secret is the first coordinate $u_1$ observes the data in law under (a), runs least squares, and has $\mathrm{Var}(\tilde u_1)\approx s^2/n$, so it reaches squared error $\varepsilon$ from about $s^2/\varepsilon$ records, $d$ times fewer than the trainer's price (proven, the variance of one coordinate of least squares under Gaussian design). The repair is to read the clause as "the secret is the trainer's target, or the lower bound is for the secret as a learning problem on $P$".

Known under another name. Part (b) is item 16, part (c) is item 34 (b), and the whole is the data-processing reading of extraction as learning from the release, which the debate stated. Status sketch is right.

Verdict REVISE.

### prop-capacity-coordinate

True as read. Part (a) is a definition, (b) cites items 32 and 14, (c) cites the theorem above, (d) cites item 34, and (e) is a reading of the register that I checked against items 11 to 34.

ch-weight-parameters. Does not block. The norm-weighted estimator carries a weight function beside its $d$ coordinates, so "share $p=d$" holds for the constant weight and the one-parameter weight families only, which (b) should say.

Verdict ACCEPT.

## 1.2 Objects of `defence-as-honest-constraint`

### def-honest-constraint-defence

Well posed, and the three clauses do the work the file says. The key-free clause is part (a) of `prop-key-free-defence-rule` as a condition, the every-run clause is the lesson of item 18, and the admissibility-against-planting clause is the carrier clause of `def-hard-problem-mapping` placed on the defence. Status open is right.

ch-utility-payer. Does not block the definition, and it blocks the third object below. The utility price is a ratio of trainer budgets in records, runs or steps at a risk $r$. The defence the file then prices, the predictive release, leaves the trainer untouched and charges the consumer, whose one-shot loss rises from $R_n+s^2$ to $R_n+2s^2$ with no trainer budget that brings it back, so by the definition $\upsilon_\Delta(r)=\infty$ for $r$ between the two. The repair is to let the payer be the honest party that pays, trainer or consumer, in its declared budget coordinates, queries included.

ch-choices-in-the-class. Does not block. The attacker class $\mathcal A$ is a class with a budget and a task, which admits passive classes as written. A defence against a steering attacker needs the class to carry choices, with the lower side of the security price a supremum over the attacker's admissible shifts, since the attacker chooses its shift after seeing the defence. The revised `def-steering-attacker-price` of section 2 supplies the coordinates.

Known under another name. The two prices are the privacy and utility sides of the differential-privacy tradeoff with the class made explicit (Dwork, McSherry, Nissim and Smith, TCC 2006, from memory, unverified, as the file says).

Verdict REVISE.

### prop-programming-and-defence-are-disjoint

Part (a) holds under item 10 with fable's correction of $Z$. Parts (c) and (d) hold.

ch-nonadmissible-programming. Blocks part (b) as written. Part (b) reads "no defence is a programming of an oracle of $\Pi$" and its proof separates the two by the node set. Take the seed table and program it, at the point of every run, to one value the designer draws once and records. By the file's own Terms this is a programming, one oracle, finitely many points, a drawn and recorded value. By `def-honest-constraint-defence` it is also a $\Delta$, since it introduces no randomness, runs at every execution and keeps the trainer's class. It moves prices. Every run returns the same model, so the shadow-run price of item 11 falls to one call, and the drawn-seed certificates of item 5 are void. So a programming is a defence, or an anti-defence, and the dichotomy fails. The repair is one word. For an admissible programming, which leaves the law of every party's view unchanged, part (b) holds, since a defence changes that law or the price and an admissible programming changes neither (proven, item 10 clause (b)).

Known under another name. The admissible programming is the programmability of the random oracle read as a game-playing hop, as the file says. Status sketch is right.

Verdict REVISE.

### prop-predictive-release-priced-defence

Part (a) holds. Part (b) matches the register. I checked the bracket against `thm-release-relearning-price-bracket` (e) in round 03 of the space, which reads $(n-d-1)/\kappa-s^2/\tau^2-s^4/(\tau^4(n-d-1))\le N\le d+1+(n+s^2/\tau^2)/\kappa$ at $s_r=s$, so $\pi_\Delta=\Theta(n/(\kappa d))$ for $n\gg d$ (proven there, with sol's six repairs pending). Part (d) holds.

ch-utility-payer, continued. Blocks part (c) as written. The arithmetic of (c) is right, $R_n+s^2$ against $R_n+2s^2$ and $s^2/k$ after $k$ answers averaged, but the conclusion $\upsilon_\Delta=k$ in queries per prediction and $\upsilon_\Delta=1$ in records does not follow from the definition, which sets $\upsilon_\Delta(r)=\infty$ for the consumer's one-shot risk below $2s^2$ and has no query coordinate. The repair lives in the definition, as above.

ch-class-named-in-statement. Does not block. The security price is $\Theta(n/(\kappa d))$ against the power-constrained class and one against the unconstrained class, by item 34 (b). The statement names the class in its setting and should name the second value beside the first, since the defence defends against a class and not against every observer.

Verdict REVISE.

### conj-honest-noise-matched-budget

Well posed as a conjecture, and its heuristics check. The covariance $b^{-1}((\mu_2+b\varsigma^2)I_d+c_2uu^\top)$ is property (i) of `def-optimum-update-stream` (proven there). The spike-to-bulk ratio $c_2/(\mu_2+b\varsigma^2)$ and the threshold $d(\mu_2+b\varsigma^2)^2/c_2^2$ follow (heuristic, as the file labels them). I recomputed the stationary excess risk of constant-step descent on a quadratic with Hessian $I_d$ and update covariance $\Sigma_g$ as $\eta\,\mathrm{tr}\Sigma_g/4$ to first order, which gives $\upsilon=1+b\varsigma^2/\mu_2$ (heuristic, right). Status open is right.

ch-trivial-trainer-task. Does not block. At $\theta^*=0$ the trainer learns nothing, and $\upsilon$ measures how fast a noisy walk contracts to zero, so the matched budget of (c) compares the attacker's learning to the trainer's non-learning. The conjecture should be posed on a law with a public target beside the secret, $Y=\langle w,X\rangle+\xi W(\langle u,X\rangle)$ with $w$ the trainer's target and $u$ the secret in the noise structure. The trainer then learns $w$ at a price that carries the noise, the update covariance keeps the spike $c_2uu^\top$ along $u$, and the released model carries $w$ and nothing of $u$. The same computation applies and $\upsilon$ becomes a learning price.

Verdict ACCEPT.

# 2. Conflicts

## 2.1 Where the three formulations disagree

On the attacker. The learning-attacker file defines a passive learner with a budget in observations, steps, batch and parameters. Mine defines an active party with a shift, a write budget and a deviation budget. Neither contains the other, and the party in the middle of split learning is both, so the disagreement is one of scope. I keep both and concatenate them in the revised definition below. The interface of 2026-10-16 already states that every adversary is a triple of a view, choices and a goal (`def-interface-view`, `def-interface-choices`, the goals), so the concatenation restores the registered frame.

On the handle that binds a learner. The learning-attacker file says a bound sees a learner through what it reads, through the noise of its own updates, or through an efficiency assumption. I add that a steerer is bound through the trainer's noise, not its own. The two noise handles are one lemma, item 18 (a), the Kullback chain rule for a Gaussian Markov chain, applied to three chains: the trainer's, as a filter against a passive attacker, the attacker's own, as a price in steps, and the trainer's again, as the steerer's stealth. I keep the lemma as one object with three uses and ask the editor to state it once.

On whose noise defends. The defence file conjectures that honest noise on updates is paid once by the trainer and twice by the passive attacker. In my linear instance the same noise $\varsigma$ enters the steerer's stealthy response as $\varsigma$ and the honest spread as $\varsigma$, so in relative units honest noise neither helps nor hurts a steerer, while it prices the passive attacker. I keep both statements. They are about two attackers and one defence, and the defence file's two-price form should carry a third line for the steering class, in which the security price of honest noise is one.

On planting. The defence file places the ban on planting in the instance class, the record laws the designer did not choose. Mine says the attacker's planting is a move of the game and escapes the ban. These agree. The carrier clause binds the designer and the theorist, and the attacker is bound by nothing but its budget. What I add is the consequence, that attacker planting yields attack results only.

On Halil's item 1. All three refute the conjecture that the attacker pays what the trainer paid. The learning-attacker file gives the exact condition under which it holds, the observations are the trainer's data in law, with the repair of ch-easier-function-of-target. Mine gives the case where it is ill-posed, the backdoor and the watermark, whose learner is the auditor. The statement should carry both.

## 2.2 Where the others persuaded me, with the revised object

Two points changed my definition. The learning-attacker file's ch-learner-clause-empty applies to my auditor as much as to its attacker, so the auditor's baseline must be stated as a price, the shadow-run price, and not assumed. The defence file's two-price form needs a security-price coordinate for the steering class, which my definition did not supply. The revised object follows in full under its old slug.

### def-steering-attacker-price: the steering attacker, its shift and its price

status: open
uses: def-learning-oracle-model, def-interface-choices, def-steer-goal, def-distinguish-goal, def-certifier, thm-bounded-deviation-transfer, thm-shadow-run-price-finite-views, def-learning-attacker, def-honest-constraint-defence

Fix a procedure in which a trainer runs $T$ steps $\theta_{t+1}=\theta_t-\eta_t(g_t+\varsigma\xi_t)$, with $g_t$ the honest update at step $t$, $\xi_t\sim\mathcal N(0,I_p)$ independent, and $\varsigma>0$ the trainer's noise. A steering attacker is an adversary of Definition 3 whose choices are nonempty. Its three kinds of choice act on the update stream as one object. Setting $k$ of the $n$ records changes $g_t$ by $v_t=\nabla L_{D'}(\theta_t)-\nabla L_D(\theta_t)$. Sending an update changes $g_t$ by the difference from the prescribed one. Altering a value in transit changes $g_t$ by the Jacobian of the receiving node applied to the alteration. The shift of the attacker is the sequence $(v_t)_{t<T}$. Its write budget is $k$, its deviation budget is $B_A=\max_t\lVert v_t\rVert$, and its push-to-noise budget is $\mathfrak e=\sum_{t<T}\lVert v_t\rVert^2/(2\varsigma^2)\le TB_A^2/(2\varsigma^2)$, the quantity of `thm-bounded-deviation-transfer` with the update stream as the release.

The target set $\Gamma$ is a set of models. It is public when the auditor's class contains a member that evaluates the indicator of $\Gamma$ on its view, and secret otherwise. A backdoor's target set $\Gamma_\tau$, fixed by a trigger $\tau$ the auditor does not hold, is secret. The auditor is a distinguisher of class $\mathcal A$ with budget $\beta_{\mathrm{aud}}$ of reference samples, $\mathsf{Train}$ calls and queries, between the honest execution and the steered one, on a stated view: the trajectory $(\theta_1,\dots,\theta_T)$, the final model $\theta_T$, or outputs on honest queries. The auditor's baseline, the honest rate $s^\circ=\Pr[\theta_T\in\Gamma]$ and the honest spread of its view, is not given to it. It buys the baseline with drawn runs at the honest input, at the price of `thm-shadow-run-price-finite-views`, and the $\mathsf{Train}$ calls so spent are part of $\beta_{\mathrm{aud}}$. Success is $s=\Pr[\theta'_T\in\Gamma]$ under the steered execution. Stealth $\delta$ means every auditor of $(\mathcal A,\beta_{\mathrm{aud}})$ has advantage at most $\delta$.

A steering attacker may also be a learning attacker of `def-learning-attacker`, trained on observations of its own before or while it acts, and its budget is then the concatenation $(k,B_A,q_T,q_E,n,T_{\mathrm{att}},b,p)$. The steering price at $(s,\delta,\mathcal A,\beta_{\mathrm{aud}})$ over an instance class is the set of minimal budgets at which some steering attacker reaches success at least $s$ on every instance with stealth $\delta$. The response of the trainer is $D_T=\theta'_T-\theta_T$ under coupled runs, meaning the same seed and the same $\xi$, and the response constant $S$ is the least number with $\lVert D_T\rVert\le S\,B_A$ over the admissible shifts. The response constant is a stability constant of the trainer. Under $\mu$-strong convexity and $\eta\le1/L$ it is at most $1/\mu$, and under $L$-smoothness alone it is at most $((1+\eta L)^T-1)/L$ (proven, by the coupling induction of `prop-label-poison-stealth-response`). For real training it is open.

The security price of a defence $\Delta$ against the steering class, in the sense of `def-honest-constraint-defence`, is the ratio of the least deviation budgets that reach $(s,\delta)$ under $\Delta(\Pi)$ and under $\Pi$, with the attacker's shift chosen after the defence, so the lower side is a supremum over admissible shifts. Equivalently it is the inverse ratio of the stealthy response caps. For honest Gaussian noise on the updates it is one in units of the honest spread (proven in the linear instance, open beyond it).

Measurement. The write budget, the deviation budget, $T$, $\eta$ and $\varsigma$ are read off the procedure, and $\mathfrak e$ is computed from the shift. Success and the honest rate are frequencies over drawn runs. The response and the response constant are read off coupled runs, which need seed names (item 3). The auditor's advantage is bounded below by a classifier two-sample test on drawn runs of its view and above by the coupled certificate of item 3 when the view is a deterministic function of the model.

The other regime. The price is stated for every auditor of a class. Against the class of all auditors, stealth is total variation and the bounds are statistical. Against a restricted class, statistical queries, a statistic, or a classifier of bounded capacity, stealth is weaker and permits a larger shift, and the difference is the auditor's class price, which has no bound for the reason the learning-attacker file gives, that the word learner restricts nothing. Without the oracle the auditor cannot buy its baseline, and stealth has no reference. With it, drawn runs supply the baseline and coupled runs the response.

One further change to my round 01. In `prop-secret-target-planted-detection` (d) the clause "detects it at the trainer's own query price plus the noise cost" now reads "detects it at the trainer's own query price, plus the noise cost, plus the shadow-run price of the honest values of those statistics", for the same reason.

# 3. A statement of the whole theory

Objects. A learning function $\mathsf L(x;\rho,\xi)$ maps a training input, a seed and hardware randomness to a model, and the learning oracle serves it through $\mathsf{Train}$, $\mathsf{Eval}$ and $\mathsf{Open}$ in the named and the drawn mode (Definitions 1, 2 and 4, accepted). A procedure is a dataflow graph, and a party in it is a view, a set of choices and a goal, distinguish, invert or steer (Definition 3 and the interface triple, accepted). Coupled runs share a seed and differ in the input, and a certifier bounds a leakage target from $\mathsf{Train}$ calls (Definitions 5 to 7, accepted). The oracle is realizable, an unbounded attacker gains nothing from it, and a certifier sees it through the seed name (proven, items 1 to 3). An attacker is a declared learner, a model family, a loss, an optimizer and a readout, with choices, records set, updates sent or values altered, and a budget vector in learning units: observations or $\mathsf{Train}$ calls, queries with a tolerance, steps at a noise level, parameters, write budget and deviation budget. A price at a success level, and at a stealth level when the attacker acts, is the set of minimal budgets at which some member of a class reaches it on every instance of a class (Definition 9 with the class explicit, accepted). A defence is a key-free change to the honest procedure run at every execution, with a utility price paid by the honest party that pays and a security price per attacker class, and a programming of an oracle is a measurement device that changes no price (proven, item 10).

Classes and handles. No lower bound binds an attacker because it learns (proven, AKMSS21 Theorem 1a). A bound binds it through what it reads, a statistic or statistical queries, through the Kullback chain rule on a noisy update stream, the trainer's as a filter against a passive attacker, the attacker's own as a price in steps, the trainer's again as the steerer's stealth (proven, one lemma, item 18 (a)), or through an assumption on every efficient algorithm under lattice hardness (proven, items 20 to 23), and the unconditional game and the efficient game are never mixed. The auditor who judges stealth is a party of the same kind, with a baseline it buys from drawn runs (proven, item 11).

Claims. Statistical prices are exact and measured, shadow runs at $\Theta(k/a^2)$, membership at $\Theta(1+n\rho^2)$ times the trainer's, update observation known within a factor 86 by experiment (proven and empirical, items 11, 15, 29 to 31). The attacker pays what the trainer paid exactly when its observations are the trainer's data in law and its secret is the trainer's target, and otherwise in neither direction (proven, items 16, 34, booklet 5.11). A trainer filters while it trains and never by its output alone (proven, item 18). A steering attacker is an additive shift on the update stream, its stealth against an auditor of the stream is its push-to-noise budget, and its effect is the trainer's response constant. In the linear model with noisy gradient descent stealth caps the trigger response at $m(\delta)$ honest standard deviations for a known direction, the trajectory auditor is worth $\sqrt{\eta\mu T/2}$ over the final-model auditor (sketch), and a secret direction buys $d^{1/4}$ (heuristic). Against a correlational trainer a planted law above degree two does not steer and at degree two is detected at price $d$ (proven). Every computational price rests on a hidden direction or subset in the record law (proven, items 25 to 28).

Aim. A declared learning attacker's measured budget meeting a proven bound of a class that contains it, in one unit, within a factor the theory has still to fix, on a law outside the single-index family (open). A defence priced against a learner class at matched budget (open, with honest noise on updates as the first candidate). The response constant of real training (open).

Scope. A cheap cryptographic plug-in does not count, and a natural learning problem that yields a one-way function would (`CONTEXT.md`). The designer and the theorist may not plant, by the carrier clause. The attacker may, and what it buys is an attack result, never a defence theorem. A backdoor and a watermark are channels whose learner is the auditor, and their published undetectability rests on planted training coins or a frozen layer and prices nothing about learning (proven, GKVZ22 Theorem 6.4, BRV26 Theorems 2 and 5, read as constructions). The natural-data oracle is parked and homomorphic encryption is set aside.

Measurement. The oracle supplies the honest law by drawn runs, the honest rate, the honest spread and the shadow runs, the response by coupled runs under seed names, and the measured upper side of every price. The proven lower side comes from the class. A price is known when the two meet within a stated factor (empirical for the upper side, proven for the lower). A measured failure of a declared attack is never a lower bound (proven, item 2).

## Verdicts

```text
VERDICT def-learning-attacker ACCEPT
VERDICT thm-attacker-update-class-price REVISE
VERDICT prop-attacker-is-trainer-under-nature REVISE
VERDICT prop-capacity-coordinate ACCEPT
VERDICT def-honest-constraint-defence REVISE
VERDICT prop-programming-and-defence-are-disjoint REVISE
VERDICT prop-predictive-release-priced-defence REVISE
VERDICT conj-honest-noise-matched-budget ACCEPT
BLOCKING 4
```
