---
model: claude-fable-5-1
discussant: learning-attacker-class
date: 2026-10-29
round: 03
role: editor
---

# The statement of the theory, draft

Merged from the three round-02 proposals. Each clause is a definition, an assumption, a claim with its status in the four words, or a line of scope. Items refer to `readings/2026-10-29-what-we-have.md`.

## Statement

1. Definition. A learning function $\mathsf L(x;\rho,\xi)$ maps a training input, a seed and hardware randomness to a model, served by the learning oracle through $\mathsf{Train}$, $\mathsf{Eval}$ and $\mathsf{Open}$ in a named mode that reuses seeds and a drawn mode that cannot. A procedure is a dataflow graph with declared channels, a party is a view, choices and a goal, and a certifier bounds leakage from $\mathsf{Train}$ calls.

2. Claim, proven. The oracle is realizable, an unbounded attacker gains nothing from it, and a certifier sees it through the seed name alone, coupled runs certifying leakage for every learning function (items 1 to 8).

3. Definition. A declared learner is a model family of $p$ parameters, a loss, an optimizer with batch $b$, steps $T$ and precision $\rho$ or injected noise $\varsigma$, and a readout fixed in advance. Trainer, attacker and auditor are declared learners. A learning attacker's budget is $(n,T,b,p)$, with $p$ a coordinate and not a price, and a party that acts adds its write and deviation budgets.

4. Definition. A price is the set of minimal budgets at which some member of a class reaches a success level, and a stealth level when it acts, on every instance of a class of record laws. Comparisons run along one coordinate or in exponent, and the exponent alone is no unit (proven, item 28). A price is known within a factor when a declared attack's measured budget lies within that factor of a proven lower side for a class containing it.

5. Definition. A programming fixes an oracle's values at finitely many points to recorded draws and is admissible when no member of the class tells the two setups apart. A defence is key-free, its randomness fresh at each execution and carried by no channel, runs at every execution, and leaves the trainer's declared components unchanged. Its utility price is the budget ratio of the honest party that pays, in that party's coordinates, and its security price against a class on a task is the ratio of the class's prices along one coordinate, on a steer task the inverse ratio of stealthy response caps with the shift chosen after the defence.

6. Claim, proven. An admissible programming moves every member's success by at most $\varepsilon$ at every budget, so it measures and is never a defence, and a defence is never an admissible programming (item 10). Canaries, recorded seeds and recorded noise program. Release noise, clipping, normalization and a predictive release defend.

7. Definition. A steering attacker sets records, sends an update, alters a value in transit or chooses a seed, each a shift $v_t(\theta)$ on the trainer's update stream, with deviation budget $\sup_{t,\theta}\|v_t(\theta)\|$ and push-to-noise budget $\mathbb E\sum_t\|v_t(\theta_t)\|^2/(2\varsigma^2)$ along the honest trajectory. Stealth $\delta$ against an auditor class is advantage at most $\delta$, the auditor buying its baseline from drawn runs, and the response constant bounds the coupled displacement of the final model per unit of deviation.

8. Claim, proven. No lower bound binds an attacker because it learns, since fine-precision SGD on an engineered network simulates any PAC learner (Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, Theorem 1a). A bound sees a learning attacker through three handles only: what it reads, a statistic, statistical queries in the worst-rounding model (Theorem 1c) or correlational queries under the square loss, the noise of a Gaussian update chain, which is the analyst's handle, and an assumption on every efficient algorithm.

9. Assumption. Two games, never mixed. Statistical-query and noisy-chain bounds are unconditional, polynomial-time bounds with the record-level view are conditional on named lattice hardness (Halil, 2026-10-25).

10. Claim, proven. One lemma, three uses. Under two laws the trajectory laws of a Gaussian update chain differ in total variation by at most $\sqrt{T\bar\kappa/(4\varsigma^2)}$, $\bar\kappa$ the mean squared shift of the per-example update mean along the null trajectory (item 18 (a)). It bounds the trainer as a filter, the noisy gradient attacker in steps, and the steerer's stealth.

11. Claim, proven and empirical. Shadow runs cost $\Theta(k/a^2)$, membership against the Gaussian mechanism $\Theta(1+n\rho^2)$ times the trainer's price, and the full observer's update price is bracketed within a factor 86, the one price with a measured and a proven side in one unit (items 11, 15, 29 to 31). Every computational price needs structure in the record law along a hidden direction, and the degree of a channel is the generative exponent with the secret as label (proven, items 20 to 28).

12. Claim, proven in the Gaussian linear model and for correlational classes, open beyond. The attacker pays what the trainer paid exactly when its observations are the trainer's data in law and its secret is the trainer's target as a learning problem, for every class at the Bayes release with nature's noise and inputs, for correlational classes under any centred noise, and for the trained release within the factor $1/\kappa$ (items 16, 34). A proper function of the target can cost $d$ times less, an exact release is relearned from $d$ queries, and for another secret neither inequality holds (booklet 5.11).

13. Claim, proven for the chain bound and the kernel eigenvalues, heuristic above degree three. A noisy gradient attacker regressing the secret on shadow pairs needs $T\ge(1-2\delta_m)^2\varsigma^2/\bar\kappa$ steps to decode weakly at every frame, with $\delta_m$ the mixture total variation of $m$ test pairs from the frame-averaged law, of order $\sqrt{m\lambda_l^2d^{-l/2}}$, and $\bar\kappa\le G_\nabla^2\sum_{k\ge l}a_k^2\lambda_k$, $l$ the information exponent of the channel with the secret as label, $a_k$ its Hermite coefficients, $G_\nabla^2$ the family's squared gradient norm, and $\lambda_k$ the top eigenvalue of the centred degree-$k$ Haar kernel, $\lambda_1=1/d$, $\lambda_2=2/(d(d+2))$, $\lambda_3=3/(d(d+2))$ (proven), $\lambda_k=\Theta(d^{-\lceil(k+1)/2\rceil})$ for $k\ge4$ (heuristic). The price in steps is of order $\varsigma^2d^{\lceil(l+1)/2\rceil}/(a_l^2G_\nabla^2)$, and capacity lowers it by at most the factor $p$.

14. Claim, proven in the linear model. A stealthy label poisoner of noisy gradient descent moves the trigger response by at most $m(\delta)$ honest standard deviations with a known direction and order $d^{1/4}\sqrt\delta$ with a secret one, a trajectory auditor regains $\sqrt{\eta\mu T/2}$ once $\eta\mu T\ge2$, and the response constant is $1/\mu$ under strong convexity, $((1+\eta L)^T-1)/L$ under smoothness, open for real training.

15. Claim, proven in exponent. A planted law that steers a correlational trainer at Hermite degree $k$ is detected by a statistical-query auditor at price at most $d^{k/2}$, the trainer's own price at that degree, so stealth is possible only above the trainer's update degree, where nothing is steered. Attacker-planted structure yields attack results and never a defence theorem, and the published undetectable backdoors plant in training coins or a frozen layer (GKVZ22 Theorem 6.4, BRV26 Theorems 2 and 5).

16. Claim, proven. Four defences bind every observer, Gaussian releases, noisy gradients, normalization, and a release with nature's noise, the last costing the attacker $\Theta(n/(\kappa d))$ against the power-constrained class and nothing against the unconstrained one, and the consumer $k$ answers per prediction for excess $s^2/k$ (items 6, 18, 33, 34). Against the noisy gradient class a defence's security price has lower side $\bar\kappa^{\Pi}/\bar\kappa^{\Pi'}$ (proven given clause 13).

17. Claim, heuristic. Honest Gaussian noise on client updates multiplies the trainer's rounds by $1+b\varsigma^2/\mu_2$ and every passive observer's update price by $(1+b\varsigma^2/\mu_2)^2$ in exponent, with constants that depend on the label law at fixed batch, since the full observer's per-update chi-square $\frac12\mathbb E[W^4T(W)^2/(W^2+\varsigma^2)^2]$ and the spiked surrogate $\frac12c_2^2/(\mu_2+\varsigma^2)^2$ have a ratio that changes with $\varsigma$ (proven). On the steer task its security price is one in units of the honest spread (proven in the linear instance).

18. Open. A bound for a batch-one gradient attacker at fine precision without injected noise outside the single-index family, the core. A natural learning problem yielding a one-way function. A defence priced against a learner class at a matched budget. The response constant of real training.

19. Scope. Planted hardness for a defence theorem does not count, the ban lives in the instance class, and the attacker may plant. A cheap cryptographic plug-in does not count, a natural one-way function would, and the seed generator is Halil's decision 4.

20. Scope. A real seed is a short key and caps every seed-blind bound at the number of seeds, seed-blind results hold for SGD and fail for Adam, items 21 to 23 hold in exact arithmetic, and the arbitrary white-box attacker has no bound (proven, items 2, 13, 20). A backdoor and a watermark are channels whose learner is the auditor or the user, a watermark's price being its key length (CHLX25 Corollary 5.2, CGZ24 Lemma 4). The natural-data oracle is parked and homomorphic encryption set aside.

21. Claim, proven by the definitions. The oracle supplies the runs: drawn runs give baselines, coupled runs the response and the leakage certificate, the two seed modes $\bar\kappa$ along the attacker's trajectory, and both procedures a defence's two prices. A measured failure of a declared attack is never a lower bound (item 2), and on real data only the measured side exists.

## Where each clause came from

| Clause | Source, and the side taken where the files disagreed |
| --- | --- |
| 1, 2, 4, 9, 11, 18 to 21 | the common sections of all three files, Definitions 1 to 9, items 1 to 31, `CONTEXT.md` |
| 3, 8 | `def-learning-attacker` (mine), the budget concatenation and the analyst's handle (steering), `prop-capacity-coordinate` folded in |
| 5 | `def-honest-constraint-defence` (defence), my freshness clause, the paying party (steering and mine) against the trainer-only ratio |
| 6 | `prop-programming-and-defence-are-disjoint` (defence), the admissibility fix (steering) |
| 7 | `def-steering-attacker-price` (steering), the shift as a function of the state and the seed as a choice (defence and mine) against its revision |
| 10 | item 18 (a) stated once (steering) |
| 12 | `prop-attacker-is-trainer-under-nature` (mine), the proper-function repair (steering) and the trained-release factor (defence) taken |
| 13 | `thm-attacker-update-class-price` (mine), the lower harmonics and $G_\nabla$ (defence), the mixture total variation, the information exponent and the normalization (steering) taken, the degree-three eigenvalue rederived by me |
| 14 | `prop-label-poison-stealth-response` (steering), the condition $\eta\mu T\ge2$ (defence) |
| 15 | `prop-secret-target-planted-detection` (steering), its (d) replaced by the repair the defence file and I gave |
| 16 | `prop-predictive-release-priced-defence` (defence), the second class value (steering), remark (iv) of the defence file |
| 17 | `conj-honest-noise-matched-budget` (defence) with its steer line, in exponent only, my constant objection against both accepts |

## What was dropped, and why

- The steering file's clause that a planted law above degree two does not steer a correlational trainer, false once the update features reach degree three. Clause 15 holds the true form.
- The $(1+o(1))$ form of the honest-noise conjecture at fixed batch, and my per-frame $\delta_m$ and $d^{k^*}$ order. The constants do not cancel, the total variation was the wrong one, and the order is false from degree three on.
- The key-free clause "reaches no party as a value" and the trainer-only utility price, ambiguous and contradicted by the first priced defence.
- The three-party frame, the oracle read as a random oracle, the replay audit as a plug-in and the learning one-way function of item 20, withdrawn or narrowed before this round, and Halil's conjecture of item 1 in its own words, refuted in both directions, its exact condition kept in clause 12.
