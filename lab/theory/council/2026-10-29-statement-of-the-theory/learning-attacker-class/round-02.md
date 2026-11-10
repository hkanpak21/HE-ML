---
model: claude-fable-5-1
discussant: learning-attacker-class
date: 2026-10-29
round: 02
---

# The learning attacker class, round 02

The verdict first. Six of the seven objects stand, five as written and one as a conjecture whose stated form is off by a constant that does not cancel. One proposition has a false clause. I rederived every proof in `prop-label-poison-stealth-response` by hand and checked its three formulas and its mixture bound numerically, and all hold. The three formulations agree on more than they disagree. All three say that no bound binds an attacker because it learns, that a programming measures and a defence changes the procedure, and that the published undetectable backdoors price nothing about learning. They disagree on where the trainer is declared, on whose budget a defence's utility price charges, and on which side of a backdoor the learner sits, and on each I say which side I keep. Section 1 judges the seven objects, section 2 records the conflicts and revises two of my objects, section 3 states the theory on one page, and the last section holds the verdict block.

## 1. Verdicts

### def-honest-constraint-defence

True as a definition and well posed. The three clauses, key-free, every run and same class, separate the four defences the theory holds from a kept key and from a programming, and the two prices are measurable by running both procedures. Status open is right.

Known under another name. The two-price form is the privacy against utility trade-off of differential privacy, with utility in excess risk (Bassily, Smith and Thakurta, FOCS 2014, from memory, unverified). The key-free clause is the definition of `prop-key-free-defence-rule` in the council meditation `oracle-as-random-oracle`, restated with the every-run clause added. The ratio bookkeeping is new and is bookkeeping.

ch-key-is-reuse, does not block. The clause "reaches no party as a value" is ambiguous when the honest party runs the node that draws $\omega$. A client that adds noise $\zeta$ to its update computed $\zeta$, and a client that runs a frozen random layer computed its weights, and the dataflow does not say which of the two "holds" its randomness. The property that separates honest noise from a kept key is freshness. A key is drawn once and reused across executions, so it correlates runs, and honest noise is drawn fresh at every execution and independent across executions. I propose the clause read "drawn fresh at every execution, independent across executions and of all other randomness, read by one node, and carried by no channel". Under it the frozen layer of GKVZ22 fails because the planter keeps it across runs, and per-run noise passes, which is what remark (iii) wants.

ch-utility-price-whose-budget, does not block. The utility price is defined over the trainer's budget $\beta_{\mathrm{tr}}$, and the first instance, `prop-predictive-release-priced-defence` (c), charges the consumer in answers per prediction while the trainer pays nothing. The definition should price utility over the honest parties' budgets at a stated risk for each, with the trainer's and the consumer's coordinates named, or the first instance has utility price one and its real cost is outside the definition.

ch-same-class-needs-declaration, does not block. The same-class clause reads "the trainer of $\Pi'$ lies in the trainer's declared learner class", and the theory has no object that declares the trainer. Whether per-example normalization at a median fit (item 33) is in the class of gradient methods depends on how that class is written down. My `def-learning-attacker`, revised in section 2, declares the trainer in the same form as the attacker, and the clause should read off that declaration.

ch-ratio-of-sets, does not block. A price is a set of minimal budget vectors, finite by Dickson's lemma, and the ratio "along one budget coordinate" needs the other coordinates fixed at equal values in $\Pi$ and $\Pi'$. One sentence fixes it.

Verdict ACCEPT.

### prop-programming-and-defence-are-disjoint

True as written once (a) is read in success at a fixed budget, which the parenthesis does. (b) and (c) hold by the two definitions. (d) holds with the time term of fable's `ch-prg-time-accounting`. The argument is the fundamental lemma of game playing for (a) and a comparison of definitions for the rest. Status sketch is right, since (a) rests on `prop-programming-preserves-prices` (b), which both critics marked REVISE and which stands only with $Z$ holding the parties' views.

Known under another name. The distinction between programming an oracle and changing the game is the random oracle methodology (Bellare and Rogaway, ACM CCS 1993, from memory, unverified). The consequence for decisions 5 and 6 is the council's ruling 2 answered, and I agree with the answer. The narrow reading is the programming rule, the broad reading is this definition of a defence, and both are needed.

ch-success-not-budget, does not block. The clause "has security price above one against $\mathcal C$, up to $\varepsilon$ in success" mixes a budget ratio with an advantage. Fable's example in `ch-price-units` shows that an $\varepsilon$ perturbation of success can move a threshold price from 100 to 0. The sentence should say that an admissible programming moves the success of every member of $\mathcal C$ by at most $\varepsilon$ at every budget, and that the programmed price at level $s$ lies between the honest prices at $s-\varepsilon$ and $s+\varepsilon$. The parenthesis already says this and the clause should match it.

Verdict ACCEPT.

### prop-predictive-release-priced-defence

True as written. (a) holds by inspection. (b) matches `thm-release-relearning-price-bracket` parts (b) and (e) line by line, which I reread in `round-03/builder.md` of the debate. (c) I recomputed. At a fresh $x\sim\gamma_d$ independent of the records, $\mathbb E\langle\hat u-u,x\rangle^2=\mathbb E\|\hat u-u\|^2=R_n$, so the consumer's loss is $R_n+s^2$ under $\Pi$ and $R_n+2s^2$ under $\Pi'$, and averaging $k$ answers brings the excess to $s^2/k$ (proven). (d) holds by the hypotheses of the theorem. Status sketch is right, since the bracket's part (c) carries sol's repair of the slack regime.

Known under another name. Posterior predictive sampling in Bayesian linear regression, and the A-optimal design bound sol named in the debate. The reading of sampling at temperature one as the deployed form is labelled heuristic, and the transfer to a language model is not claimed, which is right.

ch-inverse-wishart-proven, does not block. The statement labels $\iota_m=d/(m-d-1)$ "from memory, unverified". The debate's challenger proved it in section 3.2 of `round-03/challenger.md` by a Schur complement, and the round-03 summary says the label can go.

ch-every-observer, does not block. The lower side binds every observer, so the defence is priced in the geometric form Halil calls too strong in item 1, and the object says so under "what remains". This is the same object as my `prop-attacker-is-trainer-under-nature` seen from the defender's side, and section 2 joins them.

Verdict ACCEPT.

### conj-honest-noise-matched-budget

Well posed as a conjecture, and its stated form is wrong by a constant that does not cancel. Parts (b) and (c) are right to first order. The stationary excess risk of constant-step descent on a quadratic with Hessian $I_d$ and update covariance $\Sigma_g$ is $\eta\,\mathrm{tr}(\Sigma_g)/4$, which I recomputed (proven), so the utility price scales as $1+b\varsigma^2/\mu_2$ (heuristic, as labelled). Part (a) has two errors in its constant.

ch-kl-constant, does not block. The Kullback divergence between $N(0,\sigma^2(1+\beta))$ and $N(0,\sigma^2)$ is $\frac12(\beta-\ln(1+\beta))=\beta^2/4+O(\beta^3)$, and the chi-square divergence is $(1+\beta)/\sqrt{1+2\beta}-1=\beta^2/2+O(\beta^3)$ (proven, two lines, and checked numerically at $\beta\in\{0.05,0.1,0.2\}$). Fable's display in the debate critique concerns the chi-square constant $\kappa$, and the conjecture reads it as $\kappa_{\mathrm{KL}}$. The factor 2 cancels in the ratio and matters for the lower side's constant.

ch-full-observer-constant, blocks. The conjecture says $\pi_{\Delta_\varsigma}=(1+b\varsigma^2/\mu_2)^2(1+o(1))$ along $d\to\infty$ at fixed $b$ and $\varsigma$, for every observer. The full observer reads the label magnitude from the update's norm at relative precision $O(d^{-1/2})$ at every noise level (proven, the identification of `ch-stream-is-single-index-sample`), so its per-update chi-square along $u$ at $b=1$ is, to second order in $T(W)$, $\kappa_2(\varsigma)=\frac12\mathbb E\big[W^4T(W)^2/(W^2+\varsigma^2)^2\big]$, while the Gaussian surrogate that gives the spiked threshold has $\frac12c_2^2/(\mu_2+\varsigma^2)^2$. Their ratio $C(\varsigma)$ equals $\mathbb E[T(W)^2]\mu_2^2/c_2^2$ at $\varsigma=0$ and $\mathbb E[W^4T(W)^2]/c_2^2$ as $\varsigma\to\infty$ (proven, by substitution), and these differ unless $W$ is constant. So the full observer's price ratio is $(1+b\varsigma^2/\mu_2)^2\,C(\varsigma)/C(0)$ up to the Fano and spectral constants, and the $(1+o(1))$ form is false for the full observer by a factor bounded away from one. For the constant-weight statistic class the threshold is the outlier equation of `conj-linear-class-reads-cauchy-transform`, which reduces to the spiked-covariance threshold $d/\beta_b^2$ only in the Gaussianizing limit, so even there the $(1+o(1))$ form is unsupported at fixed $b$. The repair is one of two. State (a) in exponent, both prices being $\Theta(d)$ with the ratio of their constants $(1+b\varsigma^2/\mu_2)^2$ up to a factor between one and $1+\mathrm{Var}(W^2T(W))/(b\,c_2^2)$. Or state it along $b\to\infty$ at fixed $b\varsigma^2$, where the batched update Gaussianizes, both constants tend to one, and the form holds, which is the batching claim of my debate critique.

ch-trainer-task-trivial, does not block. At $\theta^*=0$ the utility price is the price of staying at zero against noise, as the object says. The general case needs the per-example gradient variance at a nonzero optimum, and the conjecture should name that as its real target.

Verdict REVISE.

### def-steering-attacker-price

Well posed, and the right object. Reading every choice as an additive shift on the update stream is what lets the stealth currency of item 6 and the trajectory bound of item 18 apply to poisoning, model poisoning and alteration in transit at once. The response constant is a stability constant and its two bounds hold by the stated inductions, which I checked. Status open is right.

Known under another name. The push-to-noise budget $\sum_t\|v_t\|^2/(2\varsigma^2)$ is the Rényi privacy budget of the Gaussian mechanism applied to the deviation (Mironov, CSF 2017, registered as `fact-mironov-renyi-gaussian-mechanism`). The response constant is uniform algorithmic stability (Bousquet and Elisseeff, JMLR 2002, from memory, unverified), and its growth as $((1+\eta L)^T-1)/L$ under smoothness alone is the shape of the stability bound for SGD (Hardt, Recht and Singer, ICML 2016, from memory, unverified).

ch-shift-depends-on-state, does not block. For data poisoning $v_t=\nabla L_{D'}(\theta)-\nabla L_D(\theta)$ depends on the state, and the definition writes it at $\theta_t$ without saying whether the honest or the steered state is meant. The stealth bound of item 18 evaluates the shift along the honest trajectory and the response uses the steered one. Define $v_t(\theta)$ as a function of the state and take $B_A$ as its supremum over the states the honest trajectory visits.

ch-noise-is-injected, does not block. The definition fixes a trainer with injected noise $\varsigma>0$. For a trainer with batch noise alone the push-to-noise budget is undefined, and stealth is the total variation between trajectory laws under data sampling, for which the theory has no formula. The definition should say that it covers noisy-gradient trainers and that the batch-noise case is open, or let $\varsigma^2$ stand for the batch-noise scale as a heuristic.

ch-jacobian-is-first-order, does not block. The shift of a value in transit is the difference of the receiving node's outputs, and the Jacobian applied to the alteration is its first-order form.

Verdict ACCEPT.

### prop-label-poison-stealth-response

True as written, every step rederived. The two chains share the matrix $I-\eta A$ and the noise, so both views are Gaussian with one covariance and means apart by $D_t$, with $D_{t+1}=(I-\eta A)D_t+\eta\Delta$ (proven). The trajectory Mahalanobis distance is $T\|\Delta\|^2/\varsigma^2$ by the chain rule (proven). The final-model formula follows from $D_{T,\lambda}=(1-r_\lambda^T)\Delta_\lambda/\lambda$ and $\mathrm{Var}_\lambda=\eta^2\varsigma^2(1-r_\lambda^{2T})/(\eta\lambda(2-\eta\lambda))$ (proven). I checked the formula against a direct computation at $d=6$, $T=40$ and a random $A$, and the two agree to six digits, the bound of (b) holds with room, $\|D_T\|\le\|\Delta\|/\mu$ holds, and the Cauchy and Schwarz bound of (c) is attained at $x=\Sigma_T^{-1}D_T$ (empirical, a scratch computation). The bound (b) needs $r_\lambda\ge0$, which $\eta\le1/\lambda_{\max}(A)$ gives. The displacement bound of (d), $m(\delta)\varsigma\sqrt{\eta/\mu}$, follows from $\mathrm{Var}_\lambda\le\eta\varsigma^2/\mu$ (proven). The status can rise from sketch, since a second reader has now redone the arithmetic.

Known under another name. Gaussian location testing on a linear filter, and the gradient-descent bias $A^{-1}(I-(I-\eta A)^T)\Delta$, both classical and neither in the library. The content specific to the theory is exact and measurable, and the trajectory against final-model factor $\sqrt{\eta\mu T/2}$ is the one statement a reviewer would keep.

ch-direction-needs-write-budget, does not block. Part (d) says the write budget does not enter. It does not enter the norm bound. With $k=1$ the direction of $\Delta$ is the direction of the one record's input, so a trigger response at a chosen $\tau$ needs $k\ge d$ or chosen records. The sentence should say that stealth binds the norm of the shift for every write budget and that the direction needs the write budget stated.

Verdict ACCEPT.

### prop-secret-target-planted-detection

Parts (a), (b), (c) and (e) are true as written. (a) is the indicator auditor and Hoeffding's inequality (proven). (b) matches the library notes. GKVZ22 Theorem 6.4 gives a white-box undetectable backdoor under Hypothesis 3.7 and Assumption 6.3, with the secret in the random Fourier features' coins, and BRV26 Theorem 2 gives a planted matrix within total variation about $\sqrt{m/n}$ of Gaussian, with Theorem 5 conditional on Assumption 2 (proven there, as the notes record). (c) is data processing with DPLB24 Theorem 3.2 and FGRVX17 Theorem 2.9, and the $\varepsilon$ scaling of $\lambda_{k^*}$ is labelled heuristic, which is right. (e) is the second-moment method on a location mixture. I checked $\mathbb E\exp(m^2\langle u,u'\rangle)-1$ against $m^4/(2d)$ by Monte Carlo at $d\in\{200,400,1000\}$ and the two agree within the sampling error (empirical, a scratch computation). The classical boundary it names is Gaussian mean testing from one observation (Baraud, Bernoulli 2002, from memory, unverified, as flagged).

ch-correlational-degree-unbounded, blocks. Part (d) concludes that "against a correlational trainer, stealth at degree above two and steering are incompatible". A square-loss gradient trainer on a nonlinear model reads correlational queries of every Hermite degree its gradient features span, which is how it learns a single-index function of information exponent 3 (the correlational price $d^{l^*/2}$ for Gaussian data, Abbe, Boix-Adserà and Misiakiewicz, COLT 2023, Proposition 2, as registered, and Damian, Lee and Soltanolkotabi, COLT 2022, from memory, unverified). A planted law whose generative and information exponents both equal 3 therefore steers such a trainer, while every statistical-query auditor pays $d^{3/2}$ to detect it (DPLB24 Theorem 3.2). So stealth at degree three against statistical-query auditors and steering of a correlational trainer are compatible, and the conclusion is false for every trainer whose gradient features have Hermite degree above two. It holds for linear and quadratic models only. The clause "detects it at the trainer's own query price plus the noise cost (proven, definition of the shift)" is also heuristic and not proven, since detecting a shift of size $\|v\|$ in one statistic against noise $\varsigma$ costs about $\varsigma^2/\|v\|^2$ observations, which is not the trainer's query price. The repair is a true and stronger statement. A planted law that steers a correlational trainer differs from the honest law at some Hermite degree $k$ that the trainer's features reach, its generative exponent is at most $k$ (DPLB24 Proposition 2.6, `fact-generative-below-information`), so a statistical-query auditor detects it at price at most $d^{k/2}$, which is the trainer's own correlational price at that degree. The auditor never pays more than the steered trainer pays to be steered, in exponent (proven from the two cited results, constants heuristic). Stealth is then possible only above the trainer's degree, where nothing is steered.

Verdict REVISE.

## 2. Conflicts

Where the three formulations agree. No lower bound binds an attacker because it learns, and a bound enters through what it reads, through noise, or through an assumption, which the defence file states for defences and the steering file states for auditors. A programming measures a fixed procedure and moves no price, and a defence changes the procedure. The published undetectable backdoors place the planted law in coins or a frozen layer and price nothing about learning. Every defence the theory holds binds every observer, which is the geometric form Halil calls too strong. The oracle's seed modes are the measurement device, for the response by coupled runs, for honest rates by drawn runs, and for my update-shift energy by the two modes.

Where they disagree, and which side I keep.

1. Where the trainer is declared. The defence file's same-class clause needs a declared trainer and the theory has none. My `def-learning-attacker` declares the attacker as a model family, a loss, an optimizer and a readout. The two files persuaded me that the trainer must be declared in the same form, so that the same-class clause, the utility price and the comparison of the two parties' budgets all read one declaration. The revised definition is below.

2. Whose budget a defence's utility price charges. The defence file charges the trainer, and its first instance charges the consumer. I keep the two-price form and ask that the utility price range over the honest parties, each at a stated risk. In the predictive release the trainer pays nothing and the consumer pays $k$ answers per prediction for excess $s^2/k$.

3. The predictive release, defence or condition. The defence file calls the release at nature's noise a defence with security price $\Theta(n/(\kappa d))$. I call it the condition under which the attacker's observations are the trainer's data in law, so that the attacker is a trainer and every lower bound for the trainer's class transfers. Both are true and they are one object seen from two sides. The defence turns the attacker into a trainer, and its security price is my equality divided by the $d$ queries of the exact release. I keep mine as the statement about the attacker and add the defence reading as part (f), below.

4. Which side of a backdoor holds the learner. The steering file says the learner in a backdoor or a watermark is the auditor or the user, and that item 1's conjecture attaches to the wrong side. I agree and keep its side. The auditor is a learning attacker in my definition, with the bit honest or steered as its secret and its view as its observation, so the three handles apply to the auditor as they apply to the passive attacker. A watermark's price is the key length, a plug-in, and holds no learning unit, as the steering file says.

5. Whether a learning-constrained steerer has a bound. The steering file says it has none beyond the shift it causes. I agree for the act of steering. Where a steerer also learns, as the party in the middle of split learning learns a decoder after steering the encoder, the decoder is a learning attacker and `thm-attacker-update-class-price` prices it when it trains with injected noise. The two budgets, the steering file's $(k,B_A,q_T,q_E)$ and my $(n,T,b,p)$, are the active and the passive parts of one budget vector.

6. The class-specific defence. The defence file names the open cell, a defence priced against a learner class at a matched budget, and offers honest noise on updates as the first candidate, against the statistic class. I offer a second route. The security price of a defence against the noisy-gradient class is the ratio $\bar\kappa^{\Pi}/\bar\kappa^{\Pi'}$ of the update-shift energies of the undefended and the defended channel for the declared attacker architecture, by `thm-attacker-update-class-price` (c). It is measurable by the two seed modes under both procedures, and it is the one price in the theory that depends on the attacker's architecture.

7. Halil's item 9. The steering file reads "training is post-processing" as right for an auditor who holds the data and wrong otherwise. I add that for a learning attacker on a channel the training is the channel, and item 24, where the release gives up the label direction, shows training lowering a price to nothing. We agree that the sentence is false as a general claim.

### def-learning-attacker: the learning attacker and its budget, revised
status: open
uses: def-uniform-security-profile, def-shadow-learning-game, def-statistic-learner-class, def-honest-constraint-defence, def-steering-attacker-price

Statement. An access model names one type of observation, an update of the target's training, a release's answer at an input, a released model, a shadow pair, or an auditor's view of a run. A declared learner $A=(\mathcal F_p,\ell,\mathcal O,r)$ is a model family $\mathcal F_p=\{g_\phi\mid\phi\in\mathbb R^p\}$, a loss $\ell(\phi,o)$ on one observation, an optimizer $\mathcal O$ with its batch $b$, step count $T$, step sizes, initialization law, and either a gradient precision $\rho$ or an injected noise $\varsigma$, and a readout $r$ fixed in advance that maps $\phi_T$ and the target's view to an estimate. Observations reach $A$ only through $\ell$ and $\mathcal O$. The trainer is a declared learner $(\mathcal F_{p_{\mathrm{tr}}},\ell_{\mathrm{tr}},\mathcal O_{\mathrm{tr}},r_{\mathrm{tr}})$ whose observations are the records and whose readout is the release. A learning attacker is a declared learner whose observations come from the access model and whose estimate is of the secret. An auditor is a learning attacker whose secret is the bit honest or steered. The budget of a learning attacker is $(n,T,b,p)$, where $n$ counts observations and a shadow pair costs one $\mathsf{Train}$ call, and $p_{\mathrm{tr}}$ is the reference of $p$. Success is a declared functional on held-out views, the overlap with a direction or the agreement with a label, at a level $s$. The class $\mathcal L(\mathcal F,\ell,\mathcal O)$ holds every learning attacker with those components and any budget, and $\mathrm{price}_{\mathcal L}(s)$ is the threshold price of `def-uniform-security-profile` with the class explicit. The same-class clause of `def-honest-constraint-defence` holds when the defended trainer's declaration has the same $\mathcal F$, $\ell$ and $\mathcal O$ up to the defence's own change, and the utility price of that definition ranges over the declared honest parties, each at a stated risk.

(a) Without a restriction, $\mathcal L$ is every estimator. With $\rho<1/(8b)$ and an engineered family, mini-batch SGD simulates any PAC method (proven, Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, Theorem 1a, borrowed). So a lower bound for $\mathcal L$ names one of three restrictions. On access, $A$ reads a statistic of the observations, which is `def-statistic-learner-class`, or embeds in statistical queries under $b\rho^2>C\log(Tp/\delta)$ in the worst-rounding model (proven, Theorem 1c, borrowed), or is correlational. On noise, $\varsigma>0$, which is `thm-attacker-update-class-price`. On computation, polynomial time under a named assumption, the second game of 2026-10-25, never mixed with the first two.

(b) The square loss with the secret as label is correlational. For $\ell(\phi,(v,s))=\frac12(g_\phi(v)-s)^2$ the per-example update $(g_\phi(v)-s)\nabla g_\phi(v)$ is affine in $s$, so its mean under a law depends on the law through $\mathbb E[\nabla g_\phi(V)\,g_\phi(V)]$ and $\mathbb E[S\nabla g_\phi(V)]$ alone, and the population gradient method is a correlational algorithm (proven, the computation of item 16 part (b)). A decoder trained by square-loss gradient descent on shadow pairs is priced by every correlational lower bound on the channel, and a correlational trainer is steered only at the Hermite degrees its features reach, which is the repair of `prop-secret-target-planted-detection` (d).

(c) Every coordinate is measurable. $T$, $b$, $p$, $\rho$ and $\varsigma$ are declared, $n$ is counted by the oracle, success is read on held-out views, and the count of seeds times datasets of Halil's item 8 is the count of distinct $(\rho,x)$ pairs behind the $n$ observations.

Regime. Without the oracle, shadow pairs are real training runs and $n$ is their count. In the statistical regime the class is dropped and the price is that of items 11 and 29.

### prop-attacker-is-trainer-under-nature: the attacker pays what the trainer paid exactly when its observations are the trainer's data in law, revised
status: sketch
uses: def-learning-attacker, thm-bayes-release-loss-matched-price, thm-release-relearning-price-bracket, thm-reconstruction-from-conditional-mean, conj-reconstruction-at-training-cost, prop-predictive-release-priced-defence

Statement. Let $P$ be the task law with regression function $m_P$, let $\mathcal C$ be a learner class with price $p_{\mathcal C}(\varepsilon)$ in samples, and let the release answer an input $x$ with $m_P(x)$ plus a noise.

(a) If the attacker's inputs are drawn from the input law of $P$ and the noise at $x$ has the law of the label noise of $P$ at $x$, the attacker's observations are independent draws from $P$, so $\mathrm{price}^{\mathrm{att}}_{\mathcal C}(\varepsilon)=p_{\mathcal C}(\varepsilon)$ for every class $\mathcal C$ (proven, the two laws coincide).

(b) If the noise is any centred noise of finite variance independent of $x$ and $\mathcal C$ is correlational, square-loss population gradient methods included, the equality holds (proven, item 16 parts (a) to (c)).

(c) If the attacker chooses its inputs without a power constraint, or the release answers exactly, the equality fails, and $d$ queries suffice in the Gaussian linear model for every $n$ (proven, item 34 part (b)).

(d) If the secret is not a function of $m_P$, neither inequality between the prices holds in general (proven, the two counterexamples of round 01, section 2.1).

(e) Halil's conjecture in the form the theory supports. The attacker pays at least the trainer when the secret is the trainer's target or a function of it, the channel carries at least nature's noise at nature's inputs, and the attacker's class is contained in one for which the release is indistinguishable from the data. Under these every lower bound for $\mathcal C$ on $P$ is a lower bound on the attacker (proven from (a) and (b)). Without the second condition the attacker interpolates, and without the first the two problems are unrelated.

(f) The defence reading. The release of (a) is the defence $\Delta$ of `prop-predictive-release-priced-defence`. Its security price against every observer is the ratio of the price of (a) to the $d$ queries of (c), $\Theta(n/(\kappa d))$ in the Gaussian linear model (proven, item 34 part (e)), and its utility price falls on the consumer, $k$ answers per prediction for excess $s^2/k$, and not on the trainer (proven, part (c) of that object). The defence works by making the attacker a trainer.

Sketch. (a) is the identity of laws. (b) is `thm-bayes-release-loss-matched-price` (c). (c), (d) and (f) cite the results named. (e) composes (a) and (b) with the data-processing ceiling of item 34 part (a). The nonlinear case of (e) beyond the Gaussian linear model and correlational classes is open.

Regime. No oracle is needed, since the release is the object. In the computational regime the equality transfers every computational lower bound on the task to the attacker, the one place where the trainer's hardness becomes the attacker's.

## 3. A statement of the whole theory

The theory prices an adversary against a learning procedure in the units of the procedure's own training, proves the prices by reduction to learning problems with known thresholds, and measures them by experiment with the oracle supplying the runs.

Objects. A learning function $\mathsf L(x;\rho,\xi)$ maps a training input, a seed and hardware randomness to a model. The learning oracle serves $\mathsf{Train}$, $\mathsf{Eval}$ and $\mathsf{Open}$ in the named and the drawn mode and is realizable, so every bound proven under it holds for the real system (proven, `thm-perfect-substitution`). A certifier bounds leakage from $\mathsf{Train}$ calls, soundly through the seed name alone (proven, items 3 to 8). A procedure is a dataflow graph with declared channels. Every party, trainer, attacker and auditor, is a declared learner, a model family, a loss, an optimizer with batch, steps and noise, and a readout (`def-learning-attacker`, open). A price is the set of minimal budgets at which some member of a class reaches a success level on every instance (`def-uniform-security-profile`, proven finite). A budget is a vector, observations, $\mathsf{Train}$ calls, steps, batch and parameters for a party that observes, and records set, deviation and push-to-noise for a party that acts (`def-steering-attacker-price`, open).

Classes and the form of a price. The unbounded class gains nothing from $\mathsf{Train}$ calls (proven, item 2). The statistic class reads a declared statistic, and the statistical-query class reads queries with a tolerance. A learning attacker is bound through what it reads, the noise of its own updates, or an assumption on every efficient algorithm, and through nothing else in the theory (proven by reading). The polynomial-time class under named lattice hardness is a second game, never mixed with the first (Halil, 2026-10-25). A price is stated in one unit at a declared success and never as an exponent alone (proven, item 28).

Claims. The statistical prices of shadow runs, reconstruction, membership and update observation are exact (proven, items 11 to 15 and 29). Every computational price maps onto statistical queries, low-degree methods or a lattice problem and needs structure in the record law along a hidden direction (proven in each instance, items 20 to 28). The degree of a channel is the generative exponent with the secret as label (proven, item 27). The attacker pays what the trainer paid exactly when its observations are the trainer's data in law (proven in the Gaussian linear model and for correlational classes, items 16 and 34, open beyond). A noisy gradient attacker pays in steps at least the inverse of its update-shift energy, its architecture entering through its update norm (sketch, `thm-attacker-update-class-price`). A defence is a key-free change to the honest procedure run at every execution, distinct from a programming, which measures and moves no price (proven, item 10), and it carries a utility price and a security price. Four defences exist, all priced against every observer, one in the trainer's records (proven, items 6, 18, 33 and 34). A steering attacker is an additive shift on the update stream. In the linear model stealth caps its response at $m(\delta)$ honest standard deviations with a known direction and at order $d^{1/4}\sqrt\delta$ with a secret one, and a trajectory auditor regains $\sqrt{\eta\mu T/2}$ (proven, `prop-label-poison-stealth-response`). An auditor pays at most the steered trainer's own degree price to detect a steer that works (proven in exponent).

Aims. A price for a declared learning attacker on a channel real training produces, with a measured and a proven side in one unit and a fixed factor between them (open). A defence priced against a learner class at a matched budget (open). The response constant of real training (open).

Scope and exclusions. Hardness planted in the record law for a defence theorem does not count, a cryptographic plug-in does not count, and attacker-planted structure is a move of the game that yields attack results only (proven by the definitions). The natural-data oracle is parked. The arbitrary white-box attacker has no bound (proven, item 2). Seed-blind results hold for SGD and fail for Adam, and every seed-blind bound is capped at the number of seeds (proven, items 13 and 20). No bound binds a batch-one gradient attacker without injected noise on a law outside the single-index family (open).

Measurement. The oracle supplies the runs. The named and the drawn mode realize the frame-indexed and the frame-averaged laws, so the update-shift energy is read off the two modes. Coupled runs read a trainer's response to a shift, drawn runs read honest rates and spreads, and a defence's two prices are read by running both procedures. A price is known when a declared attacker's measured budget meets a proven bound of a class that contains it, in one unit, within a factor the theory has still to fix, and the first instance is a bracket of 86 (empirical, item 31).

## Verdicts

```text
VERDICT def-honest-constraint-defence ACCEPT
VERDICT prop-programming-and-defence-are-disjoint ACCEPT
VERDICT prop-predictive-release-priced-defence ACCEPT
VERDICT conj-honest-noise-matched-budget REVISE
VERDICT def-steering-attacker-price ACCEPT
VERDICT prop-label-poison-stealth-response ACCEPT
VERDICT prop-secret-target-planted-detection REVISE
BLOCKING 2
```
