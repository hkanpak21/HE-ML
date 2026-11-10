---
model: claude-fable-5-1
discussant: the-steering-attacker
date: 2026-10-30
round: 03
role: reviewer
---

# Review of the draft statement, by the steering attacker

The verdict first. The draft is right in its skeleton and in sixteen of its twenty-one clauses it says something I can check. Seven clauses stand as written. Fourteen need an amendment, and every amendment is one of three kinds: a label that overstates (clauses 8, 14, 15, 17, 21), a universal that one counterexample breaks (clauses 3, 5, 7, 12, 16, 20), or a symbol used for two things or left undefined (clauses 6, 11, 13). No clause is rejected. The statement lacks three things: the public and secret target dichotomy, which is the one place a steering attacker is priced without any model of the trainer, the objective sentence of `CONTEXT.md`, and the certifier's cost under deviation, which is the booklet's own name for the steerer's stealth budget.

On the clause the editor dropped from my round 02, that a planted law above degree two does not steer a correlational trainer, I accept the drop and the reason. A correlational trainer is linear in the label and of any Hermite degree in the input through its update features, so my clause held for the linear square-loss trainer alone. Clause 15 holds the form that survives, and my amendment there touches its labels only.

# Clauses

Clause 1. ACCEPT.

Clause 2. ACCEPT.

Clause 3. AMEND. The clause makes the auditor a declared learner. The stealth of clauses 7 and 14 is stated against the best auditor, whose advantage is the total variation, and that auditor is no learner. The budget also omits the $\mathsf{Train}$ calls and queries of Definition 3. Replacement.

> 3. Definition. A declared learner is a model family of $p$ parameters, a loss, an optimizer with batch $b$, steps $T$ and precision $\rho$ or injected noise $\varsigma$, and a readout fixed in advance. The trainer and the attacker are declared learners. The auditor is a distinguisher of a declared class, the best test, a statistic, statistical queries, or a declared learner trained on runs, and stealth is stated against that class. A learning attacker's budget is $(n,T,b,p)$ with its $\mathsf{Train}$ calls and queries beside it, $p$ a coordinate and not a price, and a party that acts adds its write and deviation budgets.

Clause 4. ACCEPT.

Clause 5. AMEND. "Leaves the trainer's declared components unchanged" excludes clipping and normalization, which change the optimizer, and clause 6 then calls them defences. The defence file's clause was the class, not the components. "Carried by no channel" is also false of release noise, which rides the release channel inside the released value. Replacement.

> 5. Definition. A programming fixes an oracle's values at finitely many points to recorded draws and is admissible when no member of the class tells the two setups apart. A defence is key-free, meaning every randomness it introduces has a public law, is drawn fresh at each execution and is read by one node, it runs at every execution, and it keeps the trainer in its declared class while it may change the trainer's update, as clipping and normalization do. Its utility price is the budget ratio of the honest party that pays, in that party's coordinates, and its security price against a class on a task is the ratio of the class's prices along one coordinate, on a steer task the inverse ratio of stealthy response caps with the shift chosen after the defence.

Clause 6. AMEND. "Canaries program" is true of an in-distribution canary that replaces an honest record and false of an added or out-of-distribution canary, by fable's `ch-canary-inclusion-not-programming` and decision 6. Replacement.

> 6. Claim, proven. An admissible programming moves every member's success by at most $\varepsilon$ at every budget, so it measures and is never a defence, and a defence is never an admissible programming (item 10). An in-distribution canary that replaces an honest record, a recorded seed and recorded noise program. An added canary and an out-of-distribution canary are not programmings and measure a record outside the honest law (decision 6). Release noise, clipping, normalization and a predictive release defend.

Clause 7. AMEND. A chosen seed is not a shift on the update stream. It changes the noise path $\xi$ and leaves the drift untouched, so its push-to-noise budget is zero and the chain bound of clause 10 says nothing about it. Listing it among the shifts makes the definition false for that choice. Replacement.

> 7. Definition. A steering attacker sets records, sends an update or alters a value in transit, each a shift $v_t(\theta)$ on the trainer's update stream, with deviation budget $\sup_{t,\theta}\lVert v_t(\theta)\rVert$ and push-to-noise budget $\mathbb E\sum_t\lVert v_t(\theta_t)\rVert^2/(2\varsigma^2)$ along the honest trajectory. A seed chosen by the attacker is a choice with zero shift, which changes the noise path and not the drift, so the chain bound of clause 10 says nothing about it and the public-target cap prices it. Stealth $\delta$ against an auditor class is advantage at most $\delta$, the auditor buying its baseline from drawn runs, and the response constant bounds the coupled displacement of the final model per unit of deviation.

Clause 8. AMEND. "Three handles only" is a universal about every possible bound, and nothing proves it. What is proven by reading is that every bound of the theory uses one of the three. An attacker that acts is also bound through a fourth thing, the auditor's view of the target event, which is no property of the attacker at all. Replacement.

> 8. Claim, proven, the second sentence by reading of the register. No lower bound binds an attacker because it learns, since fine-precision SGD on an engineered network simulates any PAC learner (Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, Theorem 1a). Every bound of the theory sees a learning attacker through one of three handles: what it reads, a statistic, statistical queries in the worst-rounding model (Theorem 1c) or correlational queries under the square loss, the noise of a Gaussian update chain, the trainer's or the attacker's own, the latter the analyst's handle, and an assumption on every efficient algorithm. An attacker that acts is bound beside these through the auditor's view of the target event.

Clause 9. ACCEPT.

Clause 10. ACCEPT. I re-derived the constant. Each step contributes $\lVert\Delta\rVert^2/(2\varsigma^2)$ to the Kullback divergence whatever the step size, since the step multiplies the shift and the noise alike, and Pinsker gives the display.

Clause 11. AMEND. Item 22 carries its hardness in a hidden discrete label set and item 28 in a hidden subset, so "along a hidden direction" is too narrow. The degree of a channel is the generative exponent in a Gaussian frame family, by `thm-shadow-price-is-generative-exponent`, and sol's `ch-degree-domain` shows the general definition ill-posed, so the frame must be named. Replacement.

> 11. Claim, proven and empirical. Shadow runs cost $\Theta(k/a^2)$, membership against the Gaussian mechanism $\Theta(1+n\rho^2)$ times the trainer's price, and the full observer's update price is bracketed within a factor 86, the one price with a measured and a proven side in one unit (items 11, 15, 29 to 31). Every computational price rests on structure in the record law along a hidden direction or a hidden subset, and in a Gaussian frame family the degree of a channel is the generative exponent with the secret as label (proven, items 20 to 28).

Clause 12. AMEND. "Exactly when" asserts an equivalence, and the three counterexamples show only that each condition is needed, not that nothing else suffices. Replacement.

> 12. Claim, proven in the Gaussian linear model and for correlational classes, open beyond. The attacker pays what the trainer paid when its observations are the trainer's data in law and its secret is the trainer's target as a learning problem, for every class at the Bayes release with nature's noise and inputs, for correlational classes under any centred noise, and for the trained release within the factor $1/\kappa$ (items 16, 34). Each condition is needed. A proper function of the target can cost $d$ times less, an exact release is relearned from $d$ queries, and for another secret neither inequality holds (booklet 5.11).

Clause 13. AMEND. Two faults. The order of $\delta_m$ is governed by the generative exponent $k^*$, since the test pairs see the channel through any transform of the label and the chi-square of `thm-shadow-price-is-generative-exponent` (2) starts at $k^*$. With $l>k^*$ the written order $d^{-l/2}$ understates $\delta_m$ and the sentence is false. The letter $\lambda$ also names two things, the DPLB24 coefficient in $\delta_m$ and the Haar eigenvalue in $\bar\kappa$. I checked the eigenvalues. For normalized Hermite polynomials the degree-3 kernel has eigenvalue $3/(d(d+2))$ on $(\lvert x\rvert^2-(d+2))x_i$, by the sixth moments of the sphere, and $6/(d(d+2)(d+4))$ on harmonic cubics, so the top value is the one written. The bound $\bar\kappa\le G_\nabla^2\sum_ka_k^2\lambda_k$ holds by Cauchy and Schwarz over degrees once each zonal term is placed in its own Wiener chaos. Replacement.

> 13. Claim, proven for the chain bound and the kernel eigenvalues, heuristic above degree three. A noisy gradient attacker regressing the secret on shadow pairs needs $T\ge(1-2\delta_m)^2\varsigma^2/\bar\kappa$ steps to decode weakly at every frame, with $\delta_m$ the total variation between $m$ test pairs from the frame mixture and from the frame-averaged law, of order $\sqrt{m\lambda_{k^*}^2d^{-k^*/2}}$ with $k^*$ the generative exponent and $\lambda_{k^*}$ its coefficient, and $\bar\kappa\le G_\nabla^2\sum_{k\ge l}a_k^2\nu_k$, $l\ge k^*$ the information exponent of the channel with the secret as label, $a_k$ its Hermite coefficients, $G_\nabla^2$ the family's squared gradient norm in $L^2(\gamma_d)$, and $\nu_k$ the top eigenvalue of the centred degree-$k$ Haar kernel for normalized Hermite polynomials, $\nu_1=1/d$, $\nu_2=2/(d(d+2))$, $\nu_3=3/(d(d+2))$ (proven), $\nu_k=\Theta(d^{-\lceil(k+1)/2\rceil})$ for $k\ge4$ (heuristic). The price in steps is of order $\varsigma^2d^{\lceil(l+1)/2\rceil}/(a_l^2G_\nabla^2)$, and capacity lowers it by at most the factor $p$.

Clause 14. AMEND. The secret-direction order $d^{1/4}\sqrt\delta$ was heuristic in my round 01, by a second-moment computation and the Gaussian mean-testing boundary from memory, and the clause labels the whole "proven in the linear model". The function $m(\delta)$ is also used before it is defined. Replacement.

> 14. Claim, proven in the linear model for a known direction, heuristic for a secret one. Write $m(\delta)=2\Phi^{-1}((1+\delta)/2)$, which is $\sqrt{2\pi}\,\delta$ to first order. A stealthy label poisoner of noisy gradient descent moves the trigger response by at most $m(\delta)$ honest standard deviations with a known direction (proven) and by order $d^{1/4}\sqrt\delta$ with a secret one (heuristic, the Gaussian mean-testing boundary from one observation), a trajectory auditor regains $\sqrt{\eta\mu T/2}$ once $\eta\mu T\ge2$ (proven), and the response constant is $1/\mu$ under strong convexity, $((1+\eta L)^T-1)/L$ under smoothness (proven), open for real training.

Clause 15. AMEND. The detection price $d^{k/2}$ is DPLB24 Theorem 4.1 against the product null with Gaussian records, and an honest law that is itself structured along its task direction is a different null, so the label must say so. The correlational trainer's price at degree $k$ is the from-memory result of section 6 of the reading, and the clause states it as proven. Replacement.

> 15. Claim, proven in exponent for Gaussian records against the product null, heuristic for a structured honest law. A planted law that steers a correlational trainer through a label moment of Hermite degree $k$ along a hidden direction is detected by a statistical-query auditor at price of order $d^{k/2}$ (DPLB24 Theorem 4.1), which is the correlational trainer's own price at that degree (from memory, unverified), so stealth against an auditor of the trainer's degree is possible only above the trainer's update degree, where nothing is steered. Attacker-planted structure yields attack results and never a defence theorem, and the published undetectable backdoors plant in training coins or a frozen layer (GKVZ22 Theorem 6.4, BRV26 Theorems 2 and 5).

Clause 16. AMEND. "Four defences bind every observer" contradicts the same sentence, which says the fourth binds nothing against the unconstrained class. The last sentence takes a ratio of lower bounds for a lower bound on a ratio, which holds only when the undefended attacker attains its bound. Replacement.

> 16. Claim, proven. Three defences bind every observer, Gaussian releases, noisy gradients and normalization, and a release with nature's noise binds every power-constrained observer, costing the attacker $\Theta(n/(\kappa d))$ against that class and nothing against the unconstrained one, and the consumer $k$ answers per prediction for excess $s^2/k$ (items 6, 18, 33, 34). Against the noisy gradient class a defence's price under $\Pi'$ is at least $(1-2\delta_m)^2\varsigma^2/\bar\kappa^{\Pi'}$, so its security price has lower side $\bar\kappa^{\Pi}/\bar\kappa^{\Pi'}$ when the undefended attacker attains its bound (proven given clause 13).

Clause 17. AMEND. The per-update chi-square written is the second-order value under a Gaussian surrogate for the update given $W$, and the update given $W$ is not Gaussian, so "proven" overstates it. The conclusion that the constants do not cancel stands as heuristic. Replacement.

> 17. Claim, heuristic. Honest Gaussian noise on client updates multiplies the trainer's rounds by $1+b\varsigma^2/\mu_2$ and every passive observer's update price by $(1+b\varsigma^2/\mu_2)^2$ in exponent, with constants that depend on the label law at fixed batch, since the full observer's per-update chi-square under the Gaussian surrogate given $W$, $\frac12\mathbb E[W^4T(W)^2/(W^2+\varsigma^2)^2]$ to second order in the spike, and the spiked value $\frac12c_2^2/(\mu_2+\varsigma^2)^2$ have a ratio that changes with $\varsigma$ (heuristic, the surrogate is not the update law). On the steer task its security price is one in units of the honest spread (proven in the linear instance).

Clause 18. ACCEPT.

Clause 19. ACCEPT.

Clause 20. AMEND. "The arbitrary white-box attacker has no bound (proven)" is false. Item 18 binds every white-box attacker of a noisy trainer and item 26 every attacker of a statistical-query trainer's output. What is true is that no bound reaches it through its own class. Item 2 is also cited for a claim it does not make. Replacement.

> 20. Scope. A real seed is a short key and caps every seed-blind bound at the number of seeds, seed-blind results hold for SGD and fail for Adam, items 21 to 23 hold in exact arithmetic (proven, items 13, 20), and the arbitrary white-box attacker is bound only through the trainer, by its filter and by composition (items 18, 26), never through its own class. A backdoor and a watermark are channels whose learner is the auditor or the user, a watermark's price being its key length (CHLX25 Definition 3.1 and Theorem 4.1, CGZ24 Lemma 4). The natural-data oracle is parked and homomorphic encryption set aside.

Clause 21. AMEND. "On real data only the measured side exists" is false of the bounds that quantify over every learning function or every law. The needle bound and the shadow-run price hold for every learning function, the public-target cap for every law, and the chain bound with $\bar\kappa$ measured on the actual dataset. Replacement.

> 21. Claim, proven by the definitions. The oracle supplies the runs: drawn runs give baselines, coupled runs the response and the leakage certificate, the two seed modes $\bar\kappa$ along the attacker's trajectory, and both procedures a defence's two prices. A measured failure of a declared attack is never a lower bound (item 2). On real data the proven side survives in the bounds that quantify over every learning function or every law, the needle and shadow-run bounds, the public-target cap and the chain bound with $\bar\kappa$ measured, and elsewhere only the measured side exists.

# Clauses the statement lacks

First, the public and secret target sets. The draft defines the auditor in clause 7 and never says what stealth buys, which is the one bound on a steering attacker that needs no model of the trainer.

> Claim, proven. When the auditor's class evaluates the indicator of the target set, every steering attacker with stealth $\delta$ has success at most the honest rate plus $\delta$, and the auditor buys the honest rate within $a$ at confidence $1-\alpha$ from $\lceil\ln(2/\alpha)/(2a^2)\rceil$ drawn runs at the honest input, sound for every learning function (items 7, 11). A chosen seed is a steering attacker with zero shift and advantage $1-s^\circ$ against that auditor, so a public target needs no seed control, and the replay audit is the secret-target case with seed control (item 9). When the target set is secret, the cap fails (GKVZ22 Theorem 6.4, BRV26 Theorems 2 and 5), the auditor's task is to detect the planted law, and its price is the detection price of that law against its class, the generative exponent for a planted direction (item 27) and FGRVX17 Theorem 2.9 for a planted clique, an attack result and never a defence theorem.

Second, the objective. The draft lists what is open in clause 18 and never says what the theory is for.

> Objective. The theory prices an adversary against a learning procedure in the units of the procedure's own training, proves the prices by reduction to learning problems with known thresholds, with or without the oracle, and measures the same prices by experiment, the oracle supplying the runs (`CONTEXT.md`). Its headline target is a natural procedure in which a declared attacker's price exceeds the trainer's by a margin that is named and measured, with item 15 the one instance, at $\Theta(1+n\rho^2)$ under the Gaussian mechanism (proven), and the matched-budget form of clause 17 the next candidate (open).

Third, the certifier under deviation. The draft's push-to-noise budget of clause 7 is a quantity the booklet already prices on the certifier's side, and the statement should say the two are one.

> Claim, proven. A coalition that deviates its additive inputs to Gaussian releases by at most $B_A$ raises the coupled tail to a fixed function of the honest one, coupled runs certify it with about $e^{\mathfrak e}$ runs, $\mathfrak e=(R-1)B_A^2/(2\sigma^2)$, and every certifier sound for every learning function needs $e^{(1-o(1))\mathfrak e}$ $\mathsf{Train}$ calls (item 6). Certifying against a coalition with admissible choices costs runs linear in the number of choices and is impossible for infinitely many (`thm-active-choice-dichotomy`). The push-to-noise budget of clause 7 is this $\mathfrak e$ with the update stream as the release, so the steerer's stealth and the certifier's cost are one quantity.

# Counts

ACCEPT 7. Clauses 1, 2, 4, 9, 10, 18, 19.

AMEND 14. Clauses 3, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 20, 21.

REJECT 0.
