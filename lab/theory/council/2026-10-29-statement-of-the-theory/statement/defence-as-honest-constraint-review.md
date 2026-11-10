---
model: claude-fable-5-1
discussant: defence-as-honest-constraint
date: 2026-10-30
round: 03
role: reviewer
---

# Review of the draft statement, by the discussant of defence as honest constraint

The verdict first. Twelve clauses stand as written, nine need an amendment, none is rejected. Three amendments carry mathematics. Clause 13 mixes the generative and the information exponent in its test-pair term and uses one letter for two objects. Clause 15 reads "correlational" as "degree two" again, in a softer form, and its true form is that an auditor holding the trainer's statistics at the trainer's tolerance sees every steer. Clause 20 says the white-box attacker has no bound, and every-observer statements bind it. The other six amendments fix a grain, a label, a quantifier or a unit. The three clauses the statement lacks are the negative result that no bound on the output filters, the local-randomizer defence by composition, and the open rule for when a measured price counts as met. Each amended clause is given in full, in the editor's numbering.

## Clauses

1. ACCEPT.

2. ACCEPT.

3. AMEND. The clause makes every attacker and auditor a declared learner, and the statistical bounds of the theory bind every observer, which is no declared learner. Replacement:

   Definition. A declared learner is a model family of $p$ parameters, a loss, an optimizer with batch $b$, steps $T$ and precision $\rho$ or injected noise $\varsigma$, and a readout fixed in advance. The trainer is a declared learner. The attacker and the auditor are declared learners when a statement says so, and otherwise members of the classes of clause 8, every observer among them. A learning attacker's budget is $(n,T,b,p)$, with $p$ a coordinate and not a price. Its price exists only on instances whose hidden frame is drawn per instance with positive entropy, since on a fixed instance a readout fixed in advance may be the Bayes decoder. A party that acts adds its write and deviation budgets.

4. ACCEPT.

5. AMEND. The freshness clause fixes the grain at the execution. A random first layer drawn fresh per run and reused across every record and step of that run passes it, and that layer is the kept key of items 20 to 22, which the client holds at inference. The grain is the application of the kernel. The admissibility clause against planting was dropped and belongs here. Replacement:

   Definition. A programming fixes an oracle's values at finitely many points to recorded draws and is admissible when no member of the class tells the two setups apart. A defence is a change to the procedure with three properties. Its randomness is drawn fresh at each application of the defence's kernel, independent of all other randomness, read by that application alone and by no other node, party or later application, so a per-step noise and a per-query noise pass and a random layer reused across the records of one run is a kept key. It runs at every execution. It leaves the trainer's declared components unchanged. Its utility price is the budget ratio of each honest party that pays, in that party's coordinates at a stated risk. Its security price against a class on a task is the ratio of the class's prices along one coordinate, and on a steer task the inverse ratio of the stealthy response caps with the shift chosen after the defence, in named units. A defence is admissible when the lower side of each security price holds over an instance class fixed before the defence and over every choice of a steerer within its budget.

6. AMEND. "Canaries program" is true of in-distribution canaries that replace honest records and false of the canaries deployed audits use. Replacement:

   Claim, proven. An admissible programming moves every member's success by at most $\varepsilon$ at every budget, so it measures and is never a defence, and a defence is never an admissible programming (item 10). In-distribution canaries that replace honest records, recorded seeds and recorded noise program. Out-of-distribution and random-label canaries change the law of the released model, so they program nothing and measure a record outside the honest law. Release noise, clipping, normalization and a predictive release defend.

7. AMEND. A chosen seed is not a shift $v_t(\theta)$ on the update stream. It is a choice of the noise realization with zero shift, which is how the steering file uses it for grinding. Replacement:

   Definition. A steering attacker sets records, sends an update, alters a value in transit or chooses a seed. The first three are a shift $v_t(\theta)$ on the trainer's update stream, with deviation budget $\sup_{t,\theta}\|v_t(\theta)\|$ and push-to-noise budget $\mathbb E\sum_t\|v_t(\theta_t)\|^2/(2\varsigma^2)$ along the honest trajectory. The fourth is a choice of the noise with zero shift. Stealth $\delta$ against an auditor class is advantage at most $\delta$, the auditor buying its baseline from drawn runs, and the response constant bounds the coupled displacement of the final model per unit of deviation.

8. AMEND. The simulation is a theorem and the count of handles is a reading of the register, and the clause labels both proven. Replacement:

   Claim, proven for the simulation, a reading of the register for the count. No lower bound binds an attacker because it learns, since fine-precision SGD on an engineered network simulates any PAC learner (Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, Theorem 1a). Every bound the theory holds sees a learning attacker through one of three handles: what it reads, a statistic, statistical queries in the worst-rounding model (Theorem 1c) or correlational queries under the square loss, the noise of a Gaussian update chain, which the analyst injects and the attacker in practice does not, and an assumption on every efficient algorithm.

9. ACCEPT.

10. ACCEPT.

11. ACCEPT.

12. ACCEPT. The $d$-fold gap for a proper function of the target is the steering file's `ch-easier-function-of-target`, one coordinate of $u$ at $s^2/\varepsilon$ records against the trainer's $ds^2/\varepsilon$, and it is right.

13. AMEND. Three faults. The test-pair term $\delta_m$ is governed by the generative exponent $k^*$ of the channel and its first Hermite coefficient, since any test on pairs may read the frame, while the update-shift energy is governed by the information exponent $l$, and the clause writes $l$ in both places, so $\delta_m$ is understated whenever $k^*<l$. The letter $\lambda$ names both the Haar eigenvalue and a Hermite coefficient. The decoding hypothesis, which the lower bound needs, and the test-pair count are absent. Replacement:

   Claim, proven for the chain bound and the kernel eigenvalues up to degree three, heuristic above. Under the decoding hypothesis, that no bounded frame-free readout decodes weakly at the frame-averaged law, which holds at generative exponent two with margin $O(d^{-1/2})$, a noisy gradient attacker regressing the secret on shadow pairs needs $T\ge(1-2\delta_m)^2\varsigma^2/\bar\kappa$ steps to decode weakly at every frame. Here $\delta_m$ is the mean total variation between $m$ test pairs at one frame and $m$ pairs from the frame-averaged law, with $m\ge192/c_0^2$ at weak-decoding level $c_0$, of order $\sqrt{m\,\zeta_{k^*}^2d^{-k^*/2}}$ with $k^*$ the generative exponent of the channel with the secret as label and $\zeta_{k^*}$ its first Hermite coefficient. And $\bar\kappa\le G_\nabla^2\sum_{k\ge l}a_k^2\lambda_k$, with $l$ the information exponent, $a_k$ the Hermite coefficients of the conditional mean of the secret given the view, $G_\nabla^2$ the family's squared gradient norm, and $\lambda_k$ the top eigenvalue of the centred degree-$k$ Haar kernel, $\lambda_1=1/d$, $\lambda_2=2/(d(d+2))$, $\lambda_3=3/(d(d+2))$ (proven), $\lambda_k=\Theta(d^{-\lceil(k+1)/2\rceil})$ for $k\ge4$ (heuristic). The price in steps is of order $\varsigma^2d^{\lceil(l+1)/2\rceil}/G_\nabla^2$, with a constant set by $a_l$ and, when $l$ is even, by $a_{l+1}$ as well, since $\lambda_l$ and $\lambda_{l+1}$ then share an order, and capacity lowers it by at most the factor $p$.

14. ACCEPT.

15. AMEND. The clause says stealth is possible only above the trainer's update degree, where nothing is steered. A network's update has every degree, and a planted law at degree $k$ with $d^{k/2}$ above an auditor's budget steers it while staying stealthy against that auditor. What holds is the equivalence through the trainer's own statistics. Replacement:

   Claim, proven in exponent for the prices, by the definition of the shift for the equivalence. Every steer is a shift of the statistics the trainer reads, its per-example update means, beyond the trainer's own sampling noise at its budget, so an auditor whose class holds those statistics at the trainer's tolerance detects every steer, and stealth against that auditor is impossible wherever steering happens. Against a weaker statistical-query auditor, a planted law at Hermite degree $k$ along a hidden direction costs $d^{k/2}$ to detect (DPLB24 Theorem 3.2), so a steer at degree $k$ is stealthy against an auditor of budget below $d^{k/2}$ exactly when the trainer's update has a degree-$k$ component that resolves the shift at the trainer's budget, which a linear model never has above degree two and a network has at every degree. Attacker-planted structure yields attack results and never a defence theorem, and the published undetectable backdoors plant in training coins or a frozen layer (GKVZ22 Theorem 6.4, BRV26 Theorems 2 and 5).

16. ACCEPT.

17. AMEND. The constant objection is right, and I withdraw the $(1+o(1))$ form at fixed batch. The steer line fixes its units without saying so. In honest-spread units the cap is $m(\delta)$ whatever the noise, and in absolute units the honest spread grows with $\varsigma$, so a stealthy steerer displaces the model further. The absolute unit is the one the consumer meets at the trigger, and the statement must name its units. Replacement:

   Claim, heuristic. Honest Gaussian noise $\varsigma$ on client updates multiplies the trainer's rounds by $1+b\varsigma^2/\mu_2$ and every passive observer's update price by $(1+b\varsigma^2/\mu_2)^2$, both in exponent of $\varsigma$ and with constants that depend on the label law at fixed batch, since the full observer's per-update chi-square $\frac12\mathbb E[W^4T(W)^2/(W^2+\varsigma^2)^2]$ and the spiked surrogate $\frac12c_2^2/(\mu_2+\varsigma^2)^2$ have a ratio that moves with $\varsigma$ (proven). On the steer task the same noise leaves the stealthy trigger response at $m(\delta)$ honest standard deviations, so its security price is one in units of the honest spread, and the honest spread grows linearly in $\varsigma$, so in absolute units a stealthy steerer's displacement grows linearly in $\varsigma$ and the security price on the steer task is $\varsigma_0/\varsigma$ against a reference noise $\varsigma_0$ (proven in the linear instance). A defence's steer-task price names its units, and the absolute unit is the one the consumer meets at the trigger.

18. ACCEPT.

19. ACCEPT.

20. AMEND. "The arbitrary white-box attacker has no bound" is false as written, and the label proven is wrong for it. Gaussian releases, noisy gradients and normalization bind every observer, white box included (items 6, 18, 33). What fails for the white-box attacker is every bound that sees a class through what it reads, and what is missing is a computational bound that sees its class. Replacement:

   Scope. A real seed is a short key and caps every seed-blind bound at the number of seeds, seed-blind results hold for SGD and fail for Adam, and items 21 to 23 hold in exact arithmetic (proven, items 13 and 20 to 23). The white-box attacker is bound by every-observer statements alone, Gaussian releases, noisy gradients and normalization among them, since every bound that sees a class through what it reads fails once the attacker holds the representation, and no computational bound sees its class (proven for the first part, items 6, 18 and 33, a reading of the register for the second). A backdoor and a watermark are channels whose learner is the auditor or the user, a watermark's price being its key length (CHLX25 Corollary 5.2, CGZ24 Lemma 4). The natural-data oracle is parked and homomorphic encryption set aside.

21. ACCEPT.

## Clauses the statement lacks

22. Claim, proven. No bound on the trainer's output alone filters. A trainer that outputs one bit, or an $\varepsilon$-differentially private bit, hands a planted parity to the identity attacker, so no bound on the entropy, the mutual information or the central privacy loss of the output composes with a statistical-query lower bound. A filter restricts the trainer while it trains, its access, its state or its trajectory. Under Gaussian noise the attacker's advantage is at most $\sqrt{TC^2\bar\gamma/\sigma^2+\mathcal I/2}$ with $\mathcal I=2TC^2/(b\sigma^2)$ the trajectory's information about the sample, and the second term cannot be dropped, since one noisy step into a hashed table memorizes every record at $\mathcal I=\Theta(d^2\log d)$ (item 18). Hence a defence acts on the learning function or the dataflow during training and never on the released output alone, and the honest filter is a theorem only at $\sigma^2\gtrsim TC^2/b$, a regime deployed training avoids, so at deployed noise the noise defence has a measured side and no proven side.

23. Claim, proven given `fact-ldp-equals-sq` (recorded, not re-read). A trainer that reads each record through a local randomizer is a statistical-query learner, by Kasiviswanathan, Lee, Nissim, Raskhodnikova and Smith, FOCS 2008, so by item 26 every statistical-query-hard secret stays hidden from every attacker of its output, white box included. Client-side noise on records is therefore a defence by composition, with security price the statistical-query price of the secret and utility price the statistical-query price of the task at the randomizer's tolerance, both open in their constants. It is the one defence in the theory whose proven side binds every attacker without the regime condition of clause 22, and no object states it as a defence.

24. Open. The factor within which a price counts as known. Along a family indexed by $d$ a price is known in exponent when the logarithms of the measured and the proven budgets have a ratio tending to one, and at a fixed dimension the factor is stated with the result, 86 being the only instance. No rule says when a measured side on real data, where no law is stated, meets a proven side on a law the experimenter built. Until one exists a result on real data is the measured price of a declared attack and nothing more.

## Counts

ACCEPT 12. AMEND 9. REJECT 0.
