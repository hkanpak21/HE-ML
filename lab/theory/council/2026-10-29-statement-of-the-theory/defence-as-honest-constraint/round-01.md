---
model: claude-fable-5-1
discussant: defence-as-honest-constraint
date: 2026-10-29
round: 01
---

# Defence as honest constraint, round 01

The question of this aspect asks which changes to the honest procedure count as a defence, and in what unit a defence is priced. The verdict in one paragraph. Halil's rule for designer modifications, indistinguishability of a programmed value from an honest sample, is the right rule for measurement devices and cannot admit a defence, because an admissible programming moves no price (item 10 of the reading of 29 October, accepted in that clause by both council critics). His two examples, canaries and release noise, are therefore two different objects. A canary programs an oracle and measures. Release noise changes the honest procedure and defends. The criterion he offers for an acceptable change, a constraint honest parties already meet, describes practice and does no mathematical work. The criterion that does the work has three parts: the change is run by the honest parties at every execution, it introduces no value that any party keeps, and its lower bound against the attacker holds over record laws the designer did not choose. A defence then carries two prices in the trainer's units, what honest training pays for it and how far the attacker's price rises, and both have a measured side through the oracle. The theory holds four such defences and has priced none in utility. One of them, a release that answers with nature's noise (item 34), is already a defence priced in the trainer's records, and the debate did not call it one.

## 1. Halil's idea

Terms, each at first use. A *procedure* is a dataflow graph whose learning nodes call $\mathsf{Train}$ and whose values reach the parties through declared channels (definitions reading of 27 October, Definition 3). Halil's word for it is the protocol. The *designer* is the party that fixes the procedure before any run and holds no secret of it afterwards. The *honest law* of a view is the law of what a party sees when every party follows the procedure. A *programming* fixes the value of one oracle of the procedure, the data oracle, the seed table or the release-noise oracle, at finitely many points, to a value the designer draws and records (council of 27 October, meditation `oracle-as-random-oracle`, section Programming as admissibility). A *constraint* is a change to the learning function or to the dataflow that every honest party carries out at every run. The *price* of an attacker class at a success level is the set of minimal budgets at which some member of the class reaches that level on every instance of a class (definitions reading, section 4). The *trainer's units* are records, runs, steps and the compute of a stated learner class (`CONTEXT.md`, What we are building).

His idea has five clauses.

1. Measurement by programming. The designer may modify the data or the procedure when the modification programs an oracle with a value no party can tell apart from an honest sample, as a random oracle may return a fixed value in place of a fresh draw (`CONTEXT.md`, instructions of 2026-10-27, first bullet). Such modifications hand expectations for measurability, a known law to compute expectations over (`what-you-want.md`, section 1, sixth quotation, and section 2, first allowed item). Canaries and release noise are his two examples (section 2).

2. Constraints honest parties already meet are acceptable. A constraint that honest parties already meet, such as clients adding noise, is realizable and acceptable (`halil-ideas.md`, item 10). Realizability is the second constraint of the theory, every quantity realizable by experiment (`CONTEXT.md`).

3. Planting by honest parties is poison without a theorem. Asking honest clients to plant structure, so that an attacker's planted structure is lost among it, adds poison to the procedure unless a theorem backs it (item 10). A designer who hides a key-dependent direction in a released model achieves something real, and the frozen random layer that carries such a key is an ugly solution (item 4). Structure planted in one world, with training as post-processing between, adds nothing to what is known (item 9).

4. The contribution form. A result restricts a family of attacks and shows that every member succeeds at most so much on a family of models, as the comparison-sort lower bound does (item 14), on models in use today, with what the attack needed stated (item 11).

5. Same units. The attacker is priced in the units of the procedure's own training, and the headline result is a natural procedure where the attacker's price exceeds the trainer's by a margin that is named and measured (`CONTEXT.md`, What we are building, and booklet chapter 1).

Assembled in its strongest form. A defence is a constraint that honest parties carry out at every run, with no key kept by any party, whose effect on a named family of attacks against a named family of models is a theorem, and whose two prices are stated in the trainer's units, what honest training pays for it and how far the attacker's price rises. The hardness a defence creates comes from the honest data law or from training itself and never from a planted key. The designer measures both prices with programmed oracles, which leave the honest law unchanged. Where his words leave a choice is clause 1, which names canaries and release noise together as modifications of one kind, and decision 5 of the reading of 29 October asks which reading of that clause he meant.

## 2. Critique

### 2.1 The programming rule admits no defence

Under the rule of clause 1, a programming is admissible when no party tells the programmed setup from the honest one. `prop-programming-preserves-prices` (b), with the correction that the compared object $Z$ holds the views of the parties other than the designer and nothing else (fable, `ch-z-includes-unread-values`), says that an admissible programming moves the success of every attacker of the class by at most $\varepsilon$, and a perfect programming by nothing (proven, the fundamental lemma of game playing, Bellare and Rogaway, EUROCRYPT 2006, from memory, unverified, no lemma number claimed). Both critics accept this clause. So a canary that replaces an honest record measures the honest price and moves it by nothing, and an auditor who records the release noise measures the noisy procedure and moves its price by nothing. Release noise as a defence is not a programming of any oracle of the undefended procedure, because it adds a node (fable). sol states the same from the other side. Fix a procedure whose honest release already includes Gaussian noise. Programming its noise oracle preserves that procedure's law, and the noisy procedure can still have a different security profile from the procedure without noise. These are different comparisons. Clause 1 therefore names two objects as one. A canary is a programming of the data oracle and measures. Release noise is a change of the procedure and defends. Decision 5 asks for a narrow or a broad reading of one rule. The answer is that the narrow reading is the programming rule and the broad reading is the definition of a defence, and the theory needs both as separate rules.

The rule also excludes no cryptographic plug-in. A generator's output programmed into an oracle whose honest values are uniform strings is admissible against time-bounded classes, at $\varepsilon$ equal to the generator's advantage with the setup's running time charged (`prop-programming-preserves-prices` (d), with the time term both critics demanded). So the exclusion of the plug-in is a separate rule on the carrier of hardness, which `def-hard-problem-mapping` already states. A mapping whose only hard instance is a key-dependent change made for security does not count.

### 2.2 "Already meet" gives no criterion

Whether honest clients add noise is a fact about practice. The same operation, clipping each gradient and adding Gaussian noise, is the recipe of DP-SGD (Abadi, Chu, Goodfellow, McMahan, Mironov, Talwar and Zhang, ACM CCS 2016, library key ACGMMTZ16, note unfilled, details from memory, unverified), a deployed honest behaviour and a defence in one. The theory's only quantified notion of honesty is the deviation budget $B_A$ of `thm-bounded-deviation-transfer` (item 6). A coalition whose inputs to the releases stay within $B_A$ of the prescribed ones raises the coupled tail to a fixed function of the honest one, with $\mathfrak e=(R-1)B_A^2/(2\sigma^2)$, and certifying it costs about $e^{\mathfrak e}$ runs (proven). Honesty is a parameter, and "already meet" is the point $B_A=0$ of it.

The criterion that does the mathematical work in his sentence lies elsewhere, in three conditions. The constraint is run at every execution by the honest party, it introduces no value that any party keeps, and its cost to the honest party is stated. Per-example normalization (item 33) meets all three and is not something clients already do. A frozen random first layer meets the first, is realizable, and keeps a key, the layer's seed, in the hands of the client. So "already meet" excludes the defence that works and admits the construction Halil calls ugly.

### 2.3 Noise against planting is not a distinction between operations

Clause 3 puts noise on the acceptable side and planted structure on the poison side. Both are kernels the honest party applies to a value in transit, and no rule on the kernel separates them. `prop-key-free-defence-rule` (c) (fable REVISE, sol REJECT) rounds each record's coordinate along an erased random direction to a grid and claims a law of the pancake form. fable's blocking challenge shows the rounded law without smoothing is the easy case, since `prop-blind-lll-label-recovery` reads exactly discrete hidden labels from $d+1$ representations by lattice reduction in exact arithmetic (item 22), and sol shows that the rounded and the smoothed laws are mutually singular, so no transfer to the registered hCLWE parameters is established (open). The general point survives both challenges and both critics state it. A key-free kernel can plant. So the ban on planting cannot live in a rule on modifications. It lives in the instance class, the record laws the designer does not choose, which is the carrier clause of `def-hard-problem-mapping`.

Halil's item 10 is right in its conclusion and wrong in its criterion. The theorem it asks for is the uniformity of the attacker's lower bound over record laws the defence did not manufacture. The knife edges of the debate illustrate the failure mode. A label transformation that makes $c_2=0$ closes the channel to the linear class (item 32), and it is a defence against that class exactly on the laws for which the designer knew enough to balance the moment, which is a law the designer chose.

### 2.4 The defences the theory holds are statistical, known in shape, and unpriced in utility

Every defence the theory holds binds every observer: Gaussian releases (item 6), noisy gradients (item 18), normalization (item 33), and the release with nature's noise (item 34). This is the shape of differential privacy, honest noise priced against every post-processing (Dwork, McSherry, Nissim and Smith, TCC 2006, from memory, unverified), and the utility price of such noise in excess risk is the private empirical risk minimization literature (Bassily, Smith and Thakurta, FOCS 2014, from memory, unverified, no theorem number). fable reads the bound of item 18 as differential-privacy accounting with Fano's inequality, vacuous for every deployed run, and the honest filter needs $\sigma^2\gtrsim TC^2/b$, a regime real training avoids (council meditation `trainer-as-filter`, pushback 5). Normalization is exact and trivial. At the optimum it removes the label from the update, learning signal included (fable, critique of `prop-full-clipping-optimum-filter`). A defence against every observer is the geometric guarantee Halil calls too strong in item 1.

Two registered facts say when restricting the attacker class can help a noise defence. In the client-server setting with outputs of constant dimension, every computationally private mechanism converts into a statistically private one of about the same utility (`fact-gky11-low-dimension-cdp-collapse`, Groce, Katz and Yerukhimovich, TCC 2011, library key GKY11, verified). In the two-party setting, computational privacy reaches constant error on the Hamming distance where statistical privacy pays an error of order $\sqrt n$ (`fact-two-party-dp-sqrt-n-error`, McGregor, Mironov, Pitassi, Reingold, Talwar and Vadhan, FOCS 2010, verified). So a class-specific noise defence has room only where the view is high-dimensional or the computation is distributed. That is the split and federated setting Halil names in item 1, and nothing in the theory fills the cell.

### 2.5 Where the idea is right and unused

Three places.

First, item 34 is already a defence priced in the trainer's units, and the debate did not call it one. The constraint is that the release answers each query with a draw carrying nature's noise at nature's power, in place of the posterior mean. Under it the attacker's price to come within a factor $1+\kappa$ of the trainer's risk rises from $d$ queries to about $n/\kappa$, the trainer's own record count, and least squares, a learner of the trainer's own class, attains it. Sampling at temperature one is what deployed generative models do, so this is a constraint honest parties already meet in his sense, with a theorem.

Second, `fact-ldp-equals-sq` (Kasiviswanathan, Lee, Nissim, Raskhodnikova and Smith, FOCS 2008, recorded, not re-read) says a concept class is learnable under local differential privacy exactly when it is learnable by statistical queries. A trainer that reads records through local randomizers is therefore an SQ trainer, and item 26 makes it a filter against every attacker of its output. Honest clients adding noise to their own records is a defence by composition, and no object says so.

Third, realizability. The oracle runs the defended and the undefended procedure, so both prices of a defence have a measured side, and no defence in the theory has been measured. The cell that prices attacker and defender in one unit at a matched budget, with the attacker in the trainer's class, is unclaimed in the literature (`fact-same-units-cell-unclaimed`, `prob-same-units-matched-budget-separation`).

## 3. A better formulation

Four objects. The first defines the defence and its two prices, the second separates it from programming and settles decision 5, the third is an instance the theory already proves, and the fourth is the conjecture that would make the idea a result about the matched budget.

### def-honest-constraint-defence: a defence and its two prices

status: open

uses: def-learning-oracle, def-uniform-security-profile, def-hard-problem-mapping, prop-profile-run-coordinate

Definition. Let $\Pi$ be a procedure with learning function $\mathsf L$. Fix a trainer target, a population risk $R$, and let $\beta_{\mathrm{tr}}^{\Pi}(r)$ be the least trainer budget, in records, runs or steps, at which the honest output of $\Pi$ reaches risk $r$. Fix an attacker class $\mathcal A$ with a budget, a task with success $\mathrm{succ}$, an instance class $\mathfrak J$ of record laws, and write $\mathrm{price}^{\Pi}_{\mathcal A}(s)$ for the price of $\mathcal A$ at success $s$ on $\mathfrak J$ under $\Pi$. A *defence* $\Delta$ maps $\Pi$ to a procedure $\Pi'=\Delta(\Pi)$ with three properties.

- Key-free. Every randomness $\omega$ that $\Delta$ introduces has a public law, is independent of all other randomness, is read by one node of $\Pi'$, and reaches no party as a value.
- Every run. The honest parties run $\Pi'$ at every execution, so the honest law of the attacker's view under $\Pi'$ may differ from its law under $\Pi$.
- Same class. The trainer of $\Pi'$ lies in the trainer's declared learner class.

The *utility price* of $\Delta$ at risk $r$ is $\upsilon_\Delta(r)=\beta^{\Pi'}_{\mathrm{tr}}(r)/\beta^{\Pi}_{\mathrm{tr}}(r)$, infinite when $\Pi'$ never reaches $r$. The *security price* of $\Delta$ against $\mathcal A$ at success $s$ is $\pi_\Delta(s)=\mathrm{price}^{\Pi'}_{\mathcal A}(s)/\mathrm{price}^{\Pi}_{\mathcal A}(s)$ along one budget coordinate, and along a family of instances indexed by $d$ the two prices are compared in exponent. A defence is *priced* when $\upsilon_\Delta$ and $\pi_\Delta$ are both stated with their status. It is *admissible against planting* when the lower side of $\pi_\Delta$ holds for every law in $\mathfrak J$ and $\mathfrak J$ is fixed before $\Delta$ is chosen.

Measurement (proven, from the definitions). The oracle runs $\Pi$ and $\Pi'$. Each $\beta_{\mathrm{tr}}(r)$ is read off the declared trainer's risk curve with a confidence band from held-out records. The upper side of each attacker price is a declared attack of $\mathcal A$ with a lower confidence band on its success (`prop-profile-run-coordinate` (b)), and its lower side is a theorem, as `def-known-price` requires. So both prices are measurable for every defence, and a priced defence is known within a factor when the measured and the proven sides meet.

Remarks. (i) Programming is not a defence. A programming of the oracles of $\Pi'$ measures $\Pi'$ and leaves both of its prices within $\varepsilon$ in success (proven, `prop-programming-preserves-prices` (b) with $Z$ the parties' views). (ii) The key-free clause concerns what $\Delta$ introduces. The honest procedure's own randomness, a client's seed among it, is not a defence and is judged by decision 4. (iii) A kept key fails the first clause, so encryption under a key, and a direction hidden in a model by a designer who keeps it, are not defences. This is the formal content of the plug-in exclusion for defences, and the carrier clause covers the rest.

Other regime and the oracle. The definition is regime-free, since $\mathcal A$ is a parameter. Without the oracle the measured side of the attacker's price survives when the attack needs no training run, and the trainer's side needs real training in both cases.

### prop-programming-and-defence-are-disjoint: the two rules of the designer

status: sketch

uses: def-honest-constraint-defence, prop-programming-preserves-prices

Statement. Let $\Pi$ be a procedure and $\mathcal C$ an attacker class.

- (a) No admissible programming of $\Pi$ against $\mathcal C$ has security price above one against $\mathcal C$, up to $\varepsilon$ in success (proven, `prop-programming-preserves-prices` (b), both critics accepting the clause once $Z$ holds the parties' views, with fable's `ch-price-units` observed, so the statement is in success and never in budget).
- (b) No defence is a programming of an oracle of $\Pi$. A programming fixes values at points of the honest dataflow of $\Pi$ and keeps its node set, and a defence changes a node or adds one (proven, by the two definitions).
- (c) Classification (proven, by (a) and (b)). A canary that replaces an honest record is a programming of the data oracle and never a defence. Release noise, clipping, normalization and a predictive release are defences and never programmings of $\Pi$. An auditor that records the release noise of $\Pi'$ programs the noise oracle of $\Pi'$ perfectly and measures $\Pi'$.
- (d) The programming rule excludes no cryptographic plug-in. A generator's output programmed into a uniform oracle is admissible against classes of time $T$ at $\varepsilon=\mathrm{Adv}_G(T+T_{\mathrm{setup}})$ (proven, `prop-programming-preserves-prices` (d) with the time term of `ch-prg-time-accounting`). The exclusion of the plug-in for defences is the key-free clause of `def-honest-constraint-defence` together with the carrier clause of `def-hard-problem-mapping`.

Sketch. (a) is the bracket of `prop-programming-preserves-prices` (b), read at a fixed budget. (b) compares the two definitions. (c) applies them to each example. In the canary case the fix of fable's `ch-canary-inclusion-not-programming` is needed, the canaries replace honest positions and all are included. (d) is the hybrid with the setup charged.

Consequence for decisions 5 and 6. The narrow reading is the right reading of the programming rule, and under it canaries, recorded seeds and known noise are measurement devices (decision 5, first half). The broad reading, a modification that gives a known law, is not a reading of the programming rule. It is `def-honest-constraint-defence`, and release noise counts as a defence under it, with two prices to state (decision 5, second half). An in-distribution canary measures the leakage of a typical record and an out-of-distribution canary is not a programming, so it measures a record outside the honest law (decision 6, as the council found).

Other regime and the oracle. The classification is regime-free. The oracle enters through (c). Programming is how the oracle measures a fixed procedure, and the defence is what the two procedures it runs differ by.

### prop-predictive-release-priced-defence: answering with nature's noise is a priced defence

status: sketch

uses: def-honest-constraint-defence, thm-release-relearning-price-bracket, thm-bayes-release-loss-matched-price

Setting. The Gaussian linear model of `thm-release-relearning-price-bracket`. Records $Y_i=\langle u,X_i\rangle+sN_i$ for $i\le n$, with $X_i\sim\gamma_d$, $N_i\sim N(0,1)$, prior $u\sim N(0,\tau^2I_d)$, $n\ge d+2$. The trainer outputs the posterior mean $\hat u$ with Bayes risk $R_n=\mathbb E\,\mathrm{tr}\,\Sigma_{\mathrm{post}}$. The procedure $\Pi$ answers a query $x$ with $\langle\hat u,x\rangle$. The defence $\Delta$ gives $\Pi'$, which answers with $\langle\hat u,x\rangle+sN'$ for a fresh $N'\sim N(0,1)$. This is the posterior predictive draw up to its posterior variance term $x^\top\Sigma_{\mathrm{post}}x$. The attacker class is every query algorithm with average power $\mathbb E\sum_{j\le N}\|x_j\|^2\le Nd$, the power of honest queries $x\sim\gamma_d$, adaptive queries allowed. Its task is to output $\tilde u$ with $\mathbb E\|\tilde u-u\|^2\le(1+\kappa)R_n$. The honest consumer's task is to predict $Y$ at a fresh $x\sim\gamma_d$ in square loss.

Statement.

- (a) $\Delta$ is a defence. $N'$ has a public law, is independent of everything, is read by the release node only and reaches no party as a value. $\Pi'$ runs at every query. The trainer is unchanged (proven, by inspection).
- (b) Security price. Under $\Pi$ the price is $d$ queries, since $d$ answers in general position determine $\hat u$ (`thm-release-relearning-price-bracket` (b)). Under $\Pi'$ it lies between $(n-d-1)/\kappa-s^2/\tau^2-s^4/(\tau^4(n-d-1))$ and $d+1+(n+s^2/\tau^2)/\kappa$ queries (part (e)). So $\pi_\Delta=\Theta(n/(\kappa d))$ for $n\gg d$ (proven, given parts (c) to (e) of that theorem, which sol asked to repair in the regime of their slack, and given $\iota_m=d/(m-d-1)$, the mean of the inverse Wishart law, from memory, unverified).
- (c) Utility price. The consumer's one-shot square loss at a fresh $x$ is $R_n+s^2$ under $\Pi$ and $R_n+2s^2$ under $\Pi'$, since $N'$ is independent of $(\hat u-u,N)$ given $x$, and $\mathbb E\langle\hat u-u,x\rangle^2=\mathbb E\|\hat u-u\|^2=R_n$ for $x\sim\gamma_d$ independent of the records (proven). To bring the excess over $\Pi$ down to $s^2/k$ the consumer averages $k$ answers at $x$, so in queries per prediction $\upsilon_\Delta=k$ at excess $s^2/k$, and in records $\upsilon_\Delta=1$ (proven).
- (d) Admissible against planting. The lower side of (b) holds for every $u$ under the prior and every $s>0$, $\tau>0$. The carrier is nature's noise $s$ and the honest query power, properties of the data and of the consumer, chosen by neither $\Delta$ nor the designer (proven, by the hypotheses of the theorem).

Sketch of what remains. The bound of (b) binds every observer, and against the statistic class or a gradient attacker no sharper lower side is known (open). The exact predictive draw, with variance $s^2+x^\top\Sigma_{\mathrm{post}}x$, has the same bracket up to a factor $1+O(d/n)$, since $\mathrm{tr}\,\Sigma_{\mathrm{post}}=R_n\le s^2\iota_n$ (heuristic). The measured side is least squares on $N$ answers, run against $\Pi$ and $\Pi'$ at $d\in\{50,100,200\}$, $n=10d$, $\kappa\in\{0.1,0.5,1\}$, with the least $N$ reaching $(1+\kappa)R_n$ in 40 runs recorded on each side (empirical, to be run).

Other regime and the oracle. The bracket is statistical and needs no oracle, and the computational side is empty here since least squares attains the lower side. Sampling at temperature one from a generative model answers with a draw from its predictive law, so a release that samples is the deployed form of $\Pi'$ and a release that returns its logits or greedy outputs is the deployed form of $\Pi$. The extraction of a production language model's last layer from its logit interface (Carlini and coauthors, 2024, from memory, unverified, not in the library) is an attack on $\Pi$, and (b) says what sampling would cost such an attack in this model, by a factor of the trainer's record count over the dimension (heuristic, the transfer from the linear model to a language model is not claimed).

### conj-honest-noise-matched-budget: honest noise on updates is paid once by the trainer and twice by the attacker

status: open

uses: def-honest-constraint-defence, def-optimum-update-stream, prop-update-direction-fano-recovery, thm-norm-weighted-update-pca, thm-same-units-gap-gaussian-mechanism

Setting. `def-optimum-update-stream` with its $\mu_2=\mathbb EY^2$ and $c_2=\mathbb E[Y^2(Z^2-1)]\neq0$, batch $b$, and client noise $\varsigma$. $\Pi_0$ is the stream at $\varsigma=0$ and $\Pi_\varsigma=\Delta_\varsigma(\Pi_0)$ adds $\zeta_t\sim N(0,\varsigma^2I_d)$ to each client's update. The trainer is the server, which runs FedSGD on the mean of $K$ client updates per round, from a start $\theta_0\neq\theta^*$ with step $\eta$, on the population square loss, whose Hessian is $I_d$ and whose per-example gradient covariance at $\theta^*$ is $\mu_2I_d+c_2uu^\top$ (proven, property (i) of the definition). The attacker is every observer of $T$ client updates, with the task of overlap $\frac12$ with $u$ at probability $\frac23$. Along $d\to\infty$ at fixed $b$, $\varsigma$, $K$ and label law:

- (a) Security price. $\pi_{\Delta_\varsigma}=(1+b\varsigma^2/\mu_2)^2\,(1+o(1))$. The full observer's price in updates is $\Theta\big(d(\mu_2+b\varsigma^2)^2/c_2^2\big)$ (heuristic). Its lower side is $T\ge(d/24-0.93)/\kappa_{\mathrm{KL}}$ with $\kappa_{\mathrm{KL}}$ the Kullback divergence of one batch-$b$ update along $u$, equal to $\beta_b^2/2$ to first order with $\beta_b=c_2/(\mu_2+b\varsigma^2)$ (heuristic, fable's display in the debate critique, section 4). Its upper side is the spectral estimator of `thm-norm-weighted-update-pca` at the constant weight, whose spike is $c_2/b$ against a bulk of $(\mu_2+b\varsigma^2)/b$ (proven, property (i)), with the spiked-covariance threshold $T\asymp d(\mu_2+b\varsigma^2)^2/c_2^2$ (heuristic, from memory).
- (b) Utility price. $\upsilon_{\Delta_\varsigma}(r)=(1+b\varsigma^2/\mu_2)(1+o(1))$ for every excess risk $r$ below the initial one and above zero. The stationary excess risk of the server at step $\eta$ is $\eta\,\mathrm{tr}(\Sigma_g)/4$ to first order, with $\Sigma_g=(Kb)^{-1}\big((\mu_2+b\varsigma^2)I_d+c_2uu^\top\big)$ the covariance of the averaged update, so reaching $r$ needs $\eta\le4rKb/(d(\mu_2+b\varsigma^2))(1+o(1))$ and the rounds to contract the initial excess risk $r_0$ to $r$ number $\ln(r_0/r)/\eta$ (heuristic, the standard constant-step computation on a quadratic, from memory, and a decreasing step changes the constant and not the scaling).
- (c) Matched budget. The attacker pays $\pi_{\Delta_\varsigma}/\upsilon_{\Delta_\varsigma}=1+b\varsigma^2/\mu_2$ times what the trainer pays, the shape of `thm-same-units-gap-gaussian-mechanism`, $\Theta(1+n\rho^2)$, with $b\varsigma^2/\mu_2$ in place of $n\rho^2$ (heuristic, from (a) and (b)).
- (d) For the statistic class $\mathcal A_{\hat M}$ the same holds up to the factor $1+\mathrm{Var}(W^2T(W))/(b\,c_2^2)$, if fable's batching claim holds (open).

Admissibility. The law is generic, $c_2\neq0$ holds off a knife edge, Gaussian inputs, nothing hidden beyond nature's $u$, and the honest noise is Halil's own example of an acceptable constraint. The lower side of (a) holds for every $u$ on the sphere and every label law with the stated moments, so the carrier is nature's $\mu_2$ against $c_2$ and the honest noise.

What settles it. (a) needs $\kappa_{\mathrm{KL}}$ at batch $b$ in closed form, a computation inside the proof of `prop-update-direction-fano-recovery`, and the spiked-covariance threshold at batch $b$. (b) needs the stationary-risk computation with its constant. The experiment runs at $d=200$, $b\in\{1,8\}$, $K=16$, $\varsigma^2\in\{0,\mu_2/b,4\mu_2/b\}$, and records the rounds for the server to reach $r=r_0/10$ and the updates for the weighted estimator to reach overlap $\frac12$, 40 runs each. The prediction is that the first grows by $1+b\varsigma^2/\mu_2$ and the second by its square. A drift of either exponent refutes (a) or (b). The trainer's task is trivial in this setting, since $\theta^*=0$, and the content is the exponent of the noise, two for the attacker against one for the trainer. The general case replaces $\mu_2$ by the per-example gradient variance at the optimum.

Other regime and the oracle. The statistical side is this conjecture. The computational side is empty at degree two, where the statistical and efficient prices coincide (fable, from DPLB24). No oracle is needed, since the attacker is passive. The oracle's role is the measured side, which runs $\Pi_0$ and $\Pi_\varsigma$.

## 4. What the current theory supports or blocks

By item of `readings/2026-10-29-what-we-have.md`.

Supports.

- Item 10. `prop-programming-preserves-prices` (b), accepted in that clause by both critics, is the proof that no programming is a defence, and so the separation of the two rules. Its parts (c) and (d) need the fixes of section 2.1 and are not used beyond them.
- Item 6. Gaussian releases are a defence by the definition, with a proven security price against every observer and a certifier price in runs. The deviation budget $B_A$ is the theory's one quantified notion of honesty.
- Item 15. The one same-units price in the theory is under a noise defence, the Gaussian mechanism on the mean, with the factor $\Theta(1+n\rho^2)$. Its hypothesis, noise following the population covariance, is an honest constraint. `conj-honest-noise-matched-budget` is its shape in a learning procedure.
- Item 18. The noisy-gradient filter binds every white-box attacker in $T$, $C$, $b$ and $\sigma$, and its lesson that a filter must restrict the trainer while it trains, never its output alone, is the every-run clause of the definition.
- Item 26 with `fact-ldp-equals-sq`. Local randomizers make a trainer an SQ learner, so client-side noise on records is a defence by composition against every attacker of the output.
- Item 33. Normalization at a median fit is a defence that closes the channel exactly, and clipping below $w_{\min}\sqrt d/2$ equals it except with probability $Te^{-9d/64}$.
- Item 34. The predictive release is a defence priced in the trainer's records, `prop-predictive-release-priced-defence`.
- Item 2 and item 17. An unbounded attacker gains nothing from $\mathsf{Train}$ calls, and a targeted reader has only statistical bounds, so a defence's security price against either is a statistical quantity, and the oracle enters a defence's measurement only through the trainer's side and through bounded attacker classes.
- Decisions 5 and 6. Both are answered by `prop-programming-and-defence-are-disjoint` if Halil accepts the two-rule reading.

Blocks.

- Item 10 blocks the reading of clause 1 under which release noise is admissible as a programming. It is a defence or it is nothing.
- Item 27. Every degree above two comes from the moments of the record law along a hidden direction. A defence that raises the degree of the channel against statistical-query or low-degree attackers must put structure into the record law, which the carrier clause excludes unless training itself produces it. So every defence the theory can prove today has a security price against every observer and none against a learner class, and the class-specific defence of `conj-honest-noise-matched-budget` (d) rests on an open claim.
- Item 25 and the knife edges of item 32. Moment balancing is a defence only on laws the designer knew, and the council reads it as planting.
- Item 18, fable's reading. The composed bound is vacuous for deployed runs, so the honest-noise defence has a proven security price only at $\sigma^2\gtrsim TC^2/b$. Its measured side exists at every noise level and its proven side does not.
- Item 20. A defence that relies on the attacker's seed-blindness is capped at the number of seeds, and whether the generator's pseudorandomness is the excluded plug-in is decision 4, which the key-free clause does not decide, since the seed is the honest procedure's randomness and not the defence's.
- The utility price has no instance. No object of the theory states what a defence costs the trainer. `prop-predictive-release-priced-defence` (c) is the first, and it is elementary.

## 5. The statement from this aspect

A defence is a change to the honest learning function or its dataflow, run at every execution, whose randomness has a public law and reaches no party, and it is a different object from a programming, which fixes an oracle's values to measure a fixed procedure and moves no price. Every defence carries two prices in the trainer's units, the budget the defended trainer pays beyond the undefended one to reach the same risk, and the factor by which the price of a named attacker class rises. A defence is a result when both prices are stated, its attacker bound holds over record laws the designer did not choose, and the oracle measures both by running the defended and the undefended procedure. The theory holds four defences, Gaussian releases, noisy gradients, per-example normalization and a release answering with nature's noise, all priced against every observer and one priced in the trainer's records. Pricing a defence against a learner class at a matched budget is the open cell, and honest noise on client updates is its first candidate.
