---
model: claude-fable-5-1
discussant: learning-attacker-class
date: 2026-10-29
round: 01
---

# The learning attacker class, round 01

Which class makes an attacker a learner, and what shape can a lower bound against it take? The verdict first. The attacker Halil wants is a declared learner, and the word learner alone restricts nothing, since a wide enough gradient method simulates every sample-based algorithm. A lower bound sees a learning attacker through three handles only. What it reads, the noise of its own updates, and an assumption on every efficient algorithm. The theory already holds an architecture-aware bound of the second kind and has applied it to the trainer alone. Moved to the attacker, it prices a noisy gradient attacker in steps, with the architecture entering through the norm of its updates and the hidden frame entering through the seed mode of the oracle, and it plants nothing. Halil's conjecture that the attacker pays what the trainer paid is false in both directions for a general secret and exact when the attacker's observations are the trainer's data in law. Section 1 states the idea, section 2 critiques it, section 3 gives four objects, section 4 reads them against the findings of 29 October, and section 5 gives five sentences for the statement of the theory.

## 1. Halil's idea

Terms. A learning procedure trains a model on data. The trainer is the learner that runs it, its task is the law of (input, label) it learns from, and its performance is its excess risk on that task. A view is what the attacker observes, an update, an activation, a release's answer, or a model. A secret is what the attacker wants, a record, a direction, or a client's weights. A shadow pair is one (view, secret) pair the attacker obtains by its own $\mathsf{Train}$ call at a secret it chooses. A geometric bound holds for every function of the view at a stated noise level, as differential privacy and reconstruction robustness bounds do. A learning unit is a sample, a training run, a query, a gradient step, or the compute of a stated learner.

The idea has four parts.

(a) The attacker is a learner of the trainer's kind. Attacks on learning algorithms come from other learning algorithms, so the reductions may use that subclass (`readings/2026-10-27-what-you-want.md`, section 1). The reconstructor is a learner whose inputs are the intermediate vectors and whose outputs are the raw data, with no query bound and no geometric bound, pure learning on both sides (`CONTEXT.md`, section Halil's framing of the computational view). Its learning function has the trainer's four arguments, a model family that is the special subset of parametric functions in use, a dataset, a seed and hardware randomness (`halil-ideas.md`, item 2).

(b) Its budget is in learning units. The candidate units are the number of queries, the floating-point operations, and the number of distinct seeds times the number of datasets observed (`halil-ideas.md`, item 8), and the capacity of the attacker's model relative to the model attacked, read off agreement on held-out data (item 11). How they combine into one price is open to him (item 8).

(c) The bound. A learning-constrained attacker meets a bound sharper than the geometric one, and the bound is roughly the cost of learning the main task (`halil-ideas.md`, item 1). When the reconstruction problem reduces to the learning problem under attack, the lower bound is the performance of the initial model, and a reconstructor needs a model as strong as the initial classifier (`CONTEXT.md`, same section).

(d) The form of the result. Restrict a family of attacks and show that every member succeeds at most so much on a family of models, as the comparison-sort lower bound does (`halil-ideas.md`, item 14). Realize it across architectures, sizes, data and scenarios, and state what the attack needed (item 11). Measure first, in computational terms, and hardness follows where a measured price meets a proven one (`readings/2026-10-27-what-you-want.md`, section 1).

The strongest exact form. Fix a task law $P$, a trainer of class $\mathcal C$ whose price $p_{\mathcal C}(\varepsilon)$ is the least number of samples at which some member reaches excess risk $\varepsilon$ on $P$, and a channel from a secret to the attacker's view. Let the attacker be a learner of class $\mathcal C$ trained on shadow pairs, with budget $n$ pairs, $T$ steps and $p$ parameters, and let the trainer have $p_{\mathrm{tr}}$ parameters. The idea claims three inequalities. The attacker's success on the secret is at most a function of the trainer's performance. Its price in pairs at matched accuracy is at least $p_{\mathcal C}(\varepsilon)$. Its parameter count $p$ must reach $p_{\mathrm{tr}}$ up to a stated factor.

## 2. Critique

### 2.1 Where the idea is false

The inequalities of part (c) fail in both directions when the secret is not the trainer's target.

Attacker above trainer. Take Gaussian inputs and labels $Y=\langle u,X\rangle\xi$ with $\xi$ an independent sign. The Bayes square-loss predictor is zero, so the trainer's performance is nil and the trainer learns nothing about $u$. The channel from $u$ to the label law has generative exponent 2, and an attacker recovers $u$ from $\Theta(d)$ pairs (booklet 5.11, `what-we-have` items 29 to 31). The trainer's performance caps nothing here, and the attacker's price bears no relation to the trainer's, which is zero (proven).

Attacker below trainer. A single-index law with generative exponent at least 3 has a vanishing first Hermite coefficient, so a trainer of excess risk $\varepsilon$ exists whose release does not yield the direction (proven, the refutation of `prop-label-relevant-attacker-at-most-trainer` by sol in round 03 of statistical-limits). In the Gaussian linear model, a release that answers exactly is relearned from $d$ queries whatever the trainer's $n$ records (proven, item 34 part (b)), and the label direction is read off a release of excess risk $\varepsilon$ within $O(\sqrt\varepsilon)$ with no learning on the attacker's side (proven, item 24).

Where the inequality holds, it holds because of the channel. A release that answers with nature's noise at nature's power costs the attacker about $(n-d-1)/\kappa$ answers to come within a factor $1+\kappa$ of the trainer's risk (proven, item 34 parts (c) to (e)). A Bayes release costs a correlational learner exactly what the data cost (proven, item 16). Membership against the Gaussian mechanism costs $\Theta(1+n\rho^2)$ times the trainer's price (proven, item 15). In each case the attacker's observations are the trainer's data in law, or carry at least their noise. The attacker's class enters none of these lower sides.

### 2.2 Where the idea is ill-posed

The word learner restricts nothing. Mini-batch SGD with batch $b$ and gradient precision $\rho<1/(8b)$ on an engineered network of $r+O(T'(n+\log b))$ parameters simulates any PAC method on $m$ samples up to error $\delta$ in $T'=O(mn/\delta)$ steps (Abbe, Kamath, Malach, Sandon and Srebro, NeurIPS 2021, Theorem 1a, in the library, read in full). A maximum-likelihood mixture with one component per observation reads the empirical measure, so the statistic class of item 32 is every estimator once the statistic is the empirical measure (proven, the debate's challenge `ch-learner-clause-empty`). A class of learners carries a lower bound only after a restriction on its access, its noise or its computation, and part (a) names none.

Capacity read off held-out agreement is a success level. Agreement is the functional the attacker is scored on, so the capacity at which agreement $s$ is reached is a point of the price's domain and not a value of the price. Part (b) puts it among the units.

The units do not combine. Part (c) says roughly the cost, in one unit. The theory has four, samples, $\mathsf{Train}$ calls, queries with a tolerance, and time, and the exponent of a price is not a unit, since one degree costs $d^{k/2}$ in a Gaussian frame and $d^k$ in a subset frame (proven, item 28). The comparison-sort analogy of part (d) counts one unit, comparisons. A learning attacker has four, and part (b) leaves their combination open.

### 2.3 Where the idea is already known

A learning-constrained attacker that meets a sharper bound than the geometric one is capacity-bounded differential privacy. Chaudhuri, Imola and Machanavajjhala (NeurIPS 2019, Definition 3) restrict the adversary to a function class, linear, reproducing kernel or two-layer ReLU, through restricted $f$-divergences, and post-processing holds only under a closure condition (verified in `sink/formalizing/facts.md`, `fact-capacity-bounded-dp-function-class`). The class there is a set of functions and the price is a divergence. Halil's idea goes beyond it in two places, the class is an algorithm with a budget, and the price is in learning units. The theory has not cited this notion.

Pseudorandomness against a class of distinguishers is outcome indistinguishability (Dwork, Kim, Reingold, Rothblum and Yona, STOC 2021, from memory, unverified). The council found that item 19 is its constant-predictor case.

The embedding of gradient attackers in query classes is known in three forms. SGD embeds in statistical queries when $b\rho^2>C\log(Tp/\delta)$, for the worst valid rounding (Abbe et al., NeurIPS 2021, Theorem 1c). Full-batch gradient descent on the square loss is a correlational learner, and correlational lower bounds give $d^{\mathrm{Leap}/2}$ for Gaussian data (Abbe, Boix-Adserà and Misiakiewicz, COLT 2023, Proposition 2, as the register records it, the note is a sweep and I did not open the paper) and $d^{l^*/2}$ with $l^*$ the information exponent (Damian, Lee and Soltanolkotabi, COLT 2022, from memory, unverified). Online SGD on one neuron pays $d^{l^*-1}$ for $l^*\ge3$ (Ben Arous, Gheissari and Jagannath, JMLR 2021, from memory, unverified). Noisy gradient descent on any architecture is bounded by the cross-predictability of the family (Abbe and Sandon, arXiv 2020, in the library as AS20, unread, and Shalev-Shwartz, Shamir and Shammah, ICML 2017, from memory, unverified). Item 18 of the theory is of this last kind.

Hardness against every efficient learner is a one-way function. Blum, Furst, Kearns and Lipton (CRYPTO 1993, from memory, unverified) build one from any learning problem hard on average, and if no infinitely-often one-way function exists, every unknown adaptively changing distribution is learnable in polynomial time (Hirahara and Nanashima, ECCC TR23-100, 2023, Theorem 2.4, verified in `fact-pessiland-learning`). So part (d) stated against every efficient attacker on a samplable law is a one-way function, which `CONTEXT.md` counts as a result.

The comparison-sort form is the unconditional bound against a restricted class. The theory adopted it on 2026-10-25 as the first of its two games. Item 22 is its escape, lattice reduction reading labels that every statistical-query tester misses.

### 2.4 Where the idea is right and the theory has not used it

The restriction to learners is what gives the price its existence. A learning attacker must decode across secrets, so it is a universal reader, and a targeted attack on one candidate record has no learning price (proven, item 17). The theory proved item 17 and never stated it as the reason the learning attacker is the right class.

The theory holds an architecture-aware bound on a gradient learner and has applied it to the trainer only. Item 18 bounds the trajectory of noisy population gradient descent on a fixed model through its update class, with the sparse parity as the instance. Nothing in its proof uses that the learner is the trainer. Section 3 moves it to the attacker.

Pure learning on both sides is exact in two places. Item 16 says a Bayes release is a correlational twin of the data, and item 34 part (c) says a release at nature's noise and nature's power is the data in law. In both the attacker is a trainer, and section 3 states the condition.

A gradient learner from an isotropic initialization is equivariant under the orthogonal group (`fact-orthogonal-equivariance-of-training`), so at every secret it pays the Bayes price of a secret drawn from the orbit (proven, `prop-equivariant-learner-orbit-prior`). This is the exact sense in which the random oracle enters a gradient learner, it holds in exact arithmetic for SGD and fails for Adam (item 13), and the theory has used it for the trainer alone.

Capacity enters a proven bound through one quantity. In the object of section 3 the attacker's parameter count bounds the norm of its update, and the norm of its update divides the price in steps. This is modest and exact, and it is the only link between item 11 and a theorem.

## 3. A better formulation

A lower bound sees a learning attacker through what it reads, through the noise of its own updates, or through an assumption on every efficient algorithm. The first handle is the statistic class of item 32 and the statistical-query class of items 26 and 27. The third is the polynomial-time game of items 20 to 23. The second is the one the theory has and has not used on the attacker, and it is the only one in which the attacker's architecture enters. Four objects follow. The first defines the class and its budget. The second is the bound of the second kind. The third states Halil's conjecture in the form the theory supports. The fourth places capacity.

### def-learning-attacker: the learning attacker and its budget
status: open
uses: def-uniform-security-profile, def-shadow-learning-game, def-statistic-learner-class

Statement. An access model names one type of observation, an update of the target's training, a release's answer at an input, a released model, or a shadow pair. A learning attacker $A=(\mathcal F_p,\ell,\mathcal O,r)$ is a model family $\mathcal F_p=\{g_\phi\mid\phi\in\mathbb R^p\}$, a loss $\ell(\phi,o)$ on one observation, an optimizer $\mathcal O$ with its batch $b$, step count $T$, step sizes, initialization law, and either a gradient precision $\rho$ or an injected noise $\varsigma$, and a readout $r$ fixed in advance that maps $\phi_T$ and the target's view to an estimate of the secret. Observations reach $A$ only through $\ell$ and $\mathcal O$. The budget of $A$ is $(n,T,b,p)$, where $n$ counts observations and a shadow pair costs one $\mathsf{Train}$ call, and the trainer's parameter count $p_{\mathrm{tr}}$ is the reference of $p$. Success is a declared functional on held-out views, the overlap with a direction or the agreement with a label, at a level $s$. The class $\mathcal L(\mathcal F,\ell,\mathcal O)$ holds every learning attacker with those components and any budget, and $\mathrm{price}_{\mathcal L}(s)$ is the threshold price of `def-uniform-security-profile` with the class explicit.

Three facts fix how the definition is used.

(a) Without a restriction, $\mathcal L$ is every estimator. With $\rho<1/(8b)$ and an engineered family, mini-batch SGD simulates any PAC method (proven, Abbe et al. 2021, Theorem 1a, borrowed). So a lower bound for $\mathcal L$ names one of three restrictions. On access, $A$ reads a statistic $S$ of the observations, which is `def-statistic-learner-class`, or embeds in statistical queries under $b\rho^2>C\log(Tp/\delta)$ in the worst-rounding model (proven, Theorem 1c, borrowed), or is correlational. On noise, $\varsigma>0$, which is `thm-attacker-update-class-price`. On computation, polynomial time under a named assumption, which is the second game of 2026-10-25 and is never mixed with the first two.

(b) The square loss with the secret as label is correlational. For $\ell(\phi,(v,s))=\frac12(g_\phi(v)-s)^2$ the per-example update is $(g_\phi(v)-s)\nabla g_\phi(v)$, affine in $s$, so its mean under a law depends on the law through $\mathbb E[\nabla g_\phi(V)\,g_\phi(V)]$ and $\mathbb E[S\nabla g_\phi(V)]$ alone, and the population gradient method is a correlational algorithm (proven, the computation of item 16 part (b) with the secret in place of the label). A decoder trained by square-loss gradient descent on shadow pairs is therefore priced by every correlational lower bound on the channel.

(c) Every coordinate is measurable. $T$, $b$, $p$, $\rho$ and $\varsigma$ are declared, $n$ is counted by the oracle, and success is read on held-out views. The oracle's count of seeds times datasets, Halil's item 8, is the count of distinct $(\rho,x)$ pairs behind the $n$ observations.

Regime. Without the oracle, shadow pairs are real training runs and $n$ is their count. In the statistical regime the class is dropped and the price is the one of items 11 and 29.

### thm-attacker-update-class-price: a noisy gradient attacker pays in steps the inverse of its update-shift energy
status: sketch
uses: def-learning-attacker, def-shadow-learning-game, thm-noisy-gradient-query-filter, thm-noisy-trainer-two-term-filter, thm-shadow-price-is-generative-exponent, def-class-pseudorandom-channel

Setting. A shadow game with hidden frame $\theta$, prior $\pi$ on secrets, pair law $J_\theta$, and the frame-averaged law $\bar J=\mathbb E_\theta J_\theta$. A learning attacker of `def-learning-attacker` with per-example update $\psi_\phi(o)\in\mathbb R^p$, $\|\psi_\phi\|\le G$, and injected noise $\zeta_t\sim\mathcal N(0,\varsigma^2I_p)$ at each step. The update shift at $\phi$ is $\Delta_\theta(\phi)=\mathbb E_{J_\theta}\psi_\phi-\mathbb E_{\bar J}\psi_\phi$, and the update-shift energy is $\bar\kappa=\sup_\phi\mathbb E_\theta\|\Delta_\theta(\phi)\|^2$, the variance over frames of the mean update. The decoding hypothesis is that every bounded frame-free readout is weak at the average frame, $\sup_{\|g\|_\infty\le1}\mathrm{Cov}_{\bar J}(g(V),\varphi(S))\le c_0\sigma_\varphi/4$.

Statement.

(a) For population gradient descent with injected noise, $\mathbb E_\theta\,\mathrm{TV}\big(\mathcal L(\phi_{0:T}\mid J_\theta),\mathcal L(\phi_{0:T}\mid\bar J)\big)\le\sqrt{T\bar\kappa/(4\varsigma^2)}$.

(b) For mini-batch gradient descent on $n$ pairs with batch $b$, any reuse and injected noise, the bound is $\sqrt{T\bar\kappa/\varsigma^2+TG^2/(b\varsigma^2)}$, with the constants of `thm-noisy-trainer-two-term-filter`.

(c) Under the decoding hypothesis, an attacker that reaches weak decoding $c_0$ at every frame with probability $2/3$ needs $T\ge(1-2\delta_m)^2\varsigma^2/\bar\kappa$ steps in case (a), where $\delta_m=\mathbb E_\theta\mathrm{TV}(J_\theta^{\otimes m},\bar J^{\otimes m})$ for $m=\lceil48/c_0^2\rceil$ test pairs. In a Gaussian frame family of generative exponent $k^*$, $\delta_m=O(\sqrt{m\lambda_{k^*}^2d^{-k^*/2}})$, so the price is $T\ge(1-o(1))\varsigma^2/\bar\kappa$ as $d$ grows.

(d) In the Gaussian frame family with square loss and the secret as label, $\Delta_u(\phi)_j=-\sum_{k\ge k^*}a_k\langle h_k(\langle u,\cdot\rangle)-\bar h_k,\partial_jg_\phi\rangle_{\gamma_d}$ with $a_k=\mathbb E_\pi[S\,\mathbb E_{\gamma_1}(\ell_Sh_k)]$ and $\bar h_k$ the Haar average of $h_k(\langle u,\cdot\rangle)$. The Haar kernel of degree 1 has norm $1/d$, and the centred Haar kernel of degree 2 has norm $2/(d(d+2))$ on the degree-2 Hermite space. Hence $\bar\kappa\le a_1^2G^2/d+O(G^2/d^2)$ at $k^*=1$, and $\bar\kappa\le2a_2^2G^2/(d(d+2))+O(G^2/d^3)$ at $k^*=2$, so the price is $T\ge c\,\varsigma^2d^{k^*}/(a_{k^*}^2G^2)$ for $k^*\in\{1,2\}$. For $k^*\ge3$ the same order $d^{k^*}$ is expected and not computed.

(e) Capacity enters through $G$. If each parameter's gradient is bounded by $g_{\max}$ then $G^2\le p\,g_{\max}^2$, so a family with $p$ parameters lowers the price in steps by at most the factor $p$.

Proof. (a) The initial laws agree. The null trajectory is driven by $\mathbb E_{\bar J}\psi_\phi$ and the noise, and its law is free of $\theta$. The chain rule for Gaussian kernels gives $\mathrm{KL}(\mathcal L(\cdot\mid\bar J)\,\|\,\mathcal L(\cdot\mid J_\theta))=\sum_{t<T}\mathbb E_{\mathrm{null}}\|\Delta_\theta(\phi_t)\|^2/(2\varsigma^2)$. The null trajectory is independent of $\theta$, so averaging over $\theta$ inside the sum gives at most $T\bar\kappa/(2\varsigma^2)$, and Pinsker's inequality with Jensen's inequality finishes (proven, the proof of `thm-noisy-gradient-query-filter` (a) with the attacker's pairs in place of the trainer's data). (b) The two-term argument of `thm-noisy-trainer-two-term-filter` (a), with $\bar\kappa$ in place of $C^2\bar\gamma$ and the batch term $TG^2/(b\varsigma^2)$ from the variance of a batch mean around the population mean (proven, same proof). (c) Build a distinguisher between $J_\theta$ and $\bar J$. Run the attacker, then draw $m$ fresh pairs and output 1 when the empirical covariance of $r(\phi_T,V)$ with $\varphi(S)$ exceeds $c_0\sigma_\varphi/2$. Under $J_\theta$ the attacker succeeds with probability $2/3$ and Chebyshev's inequality with $m\ge48/c_0^2$ keeps the estimate within $c_0\sigma_\varphi/4$ except with probability $1/12$, so the output is 1 with probability at least $7/12$. Under $\bar J$ the readout is a frame-free bounded function, its covariance is at most $c_0\sigma_\varphi/4$ by the decoding hypothesis, and the output is 1 with probability at most $1/12$. The advantage $1/2$ is at most the total variation between the two views, which is at most the trajectory bound of (a) plus $\delta_m$ (proven, data processing and the triangle inequality). Solve for $T$. The order of $\delta_m$ is the second-moment bound of `def-class-pseudorandom-channel` (a) with $\chi_{\bar J}(J_u,J_{u'})\le\sum_k\lambda_k^2\langle u,u'\rangle^k$ and $\mathbb E|\langle u,u'\rangle|^{k^*}=O(d^{-k^*/2})$ (proven for the bound, with $\bar J$ in place of the product law, which the identity of `thm-shadow-price-is-generative-exponent` (2) allows after centring). The decoding hypothesis itself holds in the Gaussian frame family with margin $O(d^{-1/2})$ at $k^*=2$, since the frame-free part of $\mathbb E[S\mid V]$ is a function of $|V|^2$ whose covariance with a bounded readout is $O(\sigma_S^2/\sqrt d)$ (proven for $k^*=2$ by one expectation, heuristic for other degrees). (d) The update is affine in $s$ by `def-learning-attacker` (b), so $\Delta_u(\phi)=-\mathrm{Cov}_{J_u}(S,\nabla g_\phi(V))+\mathrm{Cov}_{\bar J}(S,\nabla g_\phi(V))$, and $\mathbb E[S\mid V=v]=\sum_{k\ge k^*}a_kh_k(\langle u,v\rangle)$ by `thm-shadow-price-is-generative-exponent` (1) (proven). The Haar kernel $K_k(x,y)=\mathbb E_u[h_k(\langle u,x\rangle)h_k(\langle u,y\rangle)]$ has $K_1(x,y)=\langle x,y\rangle/d$ (proven). At degree 2, $K_2$ has eigenvalue $1/d$ on the radial function $(|x|^2-d)/\sqrt{2d}$ and $2/(d(d+2))$ on harmonic degree-2 functions such as $x_1x_2$ (proven, two Gaussian moments). Centring by $\bar h_k$ removes the radial component, which is frame-free, so only the harmonic eigenvalue remains (proven). The Cauchy and Schwarz inequality over $k$ gives the displays, with the higher-degree terms of order $G^2d^{-k}$ (heuristic, the cross terms between degrees are not computed). The order for $k^*\ge3$ is open. (e) Immediate from $\|\psi_\phi\|^2=\sum_j\psi_{\phi,j}^2$ (proven).

Measurement. $\bar\kappa$ is measured by the oracle without a new tool. When the hidden frame is carried by the seed, as in the orbit and split-learning instances, $J_\theta$ is the named mode with one seed and $\bar J$ is the drawn mode, and the update shift at $\phi$ is the difference of the mean per-example updates under the two modes along the attacker's own trajectory. When the frame is the data's, $\bar J$ is realized by pooling pairs across independent instances. The quantities $T$, $\varsigma$, $G$, $p$ and the success are declared or read. The experiment fixes an architecture, varies $\varsigma$ and $d$, and records the least $T$ at which overlap $\frac12$ is reached against $\varsigma^2/\bar\kappa$.

Limits. The bound is vacuous as $\varsigma\to0$, and at $\varsigma=0$ fine-precision SGD simulates PAC learning (`fact-fine-precision-sgd-simulates-pac`) and mini-batch noise carries a second-degree channel that the update class misses (council, trainer-as-filter, heuristic). The batch-one attacker without injected noise is therefore outside this theorem, and it is the open core. The bound plants nothing. At $k^*\in\{1,2\}$ the channel is what real training produces (items 13 and 29) and the content is the measured dependence on $G$, $\varsigma$, $T$, $p$ and $d$, which is Halil's measurement before hardness. A degree above 2 needs vanishing low moments of the record law along the hidden direction, which is the council's objection of item 27, and this theorem inherits it.

Regime. This is the unconditional game. In the polynomial-time game a lattice attacker with no noise is not bound, by item 22. Without the oracle, $\bar\kappa$ is measured from independent real runs, at the price of one run per frame.

### prop-attacker-is-trainer-under-nature: the attacker pays what the trainer paid exactly when its observations are the trainer's data in law
status: sketch
uses: def-learning-attacker, thm-bayes-release-loss-matched-price, thm-release-relearning-price-bracket, thm-reconstruction-from-conditional-mean, conj-reconstruction-at-training-cost

Statement. Let $P$ be the task law with regression function $m_P$, let $\mathcal C$ be a learner class with price $p_{\mathcal C}(\varepsilon)$ in samples, and let the release answer an input $x$ with $m_P(x)$ plus a noise.

(a) If the attacker's inputs are drawn from the input law of $P$ and the noise at $x$ has the law of the label noise of $P$ at $x$, the attacker's observations are independent draws from $P$, so $\mathrm{price}^{\mathrm{att}}_{\mathcal C}(\varepsilon)=p_{\mathcal C}(\varepsilon)$ for every class $\mathcal C$ (proven, the two laws coincide).

(b) If the noise is any centred noise of finite variance independent of $x$ and $\mathcal C$ is correlational, square-loss population gradient methods included, the equality holds (proven, item 16 parts (a) to (c)).

(c) If the attacker chooses its inputs without a power constraint, or the release answers exactly, the equality fails, and $d$ queries suffice in the Gaussian linear model for every $n$ (proven, item 34 part (b)).

(d) If the secret is not a function of $m_P$, neither inequality between the prices holds in general (proven, the two counterexamples of section 2.1).

(e) Halil's conjecture in the form the theory supports. The attacker pays at least the trainer when three conditions hold. The secret is the trainer's target or a function of it. The channel carries at least nature's noise at nature's inputs. The attacker's class is contained in one for which the release is indistinguishable from the data. Under them every lower bound for $\mathcal C$ on $P$ is a lower bound on the attacker (proven from (a) and (b)). Without the second condition the attacker interpolates, and without the first the two problems are unrelated.

Sketch. (a) is the identity of laws. (b) is `thm-bayes-release-loss-matched-price`, whose part (c) states the equality of budgets for correlational algorithms and square-loss gradient methods, with finite batches breaking it only through $\mathbb E[Y^2\mid X]$ (proven there). (c) and (d) cite the results named. (e) composes (a) and (b) with the data-processing ceiling of item 34 part (a). The nonlinear case of (e) beyond the Gaussian linear model and correlational classes is where this proposition is a sketch (open).

Regime. The statement needs no oracle, since the release is the object. In the computational regime the equality transfers every computational lower bound on the task to the attacker, which is the one place where the trainer's hardness becomes the attacker's.

### prop-capacity-coordinate: capacity is a coordinate of the budget and not a price
status: sketch
uses: def-learning-attacker, thm-attacker-update-class-price, thm-release-relearning-price-bracket, def-statistic-learner-class

Statement. (a) Held-out agreement $s$ is the success coordinate. The capacity needed for agreement $s$ is $p_{\min}(s)=\min\{p\mid\inf_\phi\mathrm{risk}(g_\phi)\le1-s\}$ at unbounded samples, an approximation quantity of $\mathcal F$ alone, and it is the left edge of the domain of $\mathrm{price}_{\mathcal L}$ in $p$ (proven, by the definitions). It is measured by fitting $\mathcal F_p$ for rising $p$ with the oracle supplying pairs (empirical). (b) $p$ bounds no success. Plain PCA and the norm-weighted spectral estimator share $p=d$ and differ without bound on laws with $c_2=0$ (proven and empirical, item 32), and one linear program with no learned parameter inverts a ReLU client (proven, item 14). (c) $p$ enters a proven lower bound only through $G$ in `thm-attacker-update-class-price` (e), where it lowers the price in steps by at most the factor $p$. (d) In the Gaussian linear model, matching capacity means $p=p_{\mathrm{tr}}=d$, and the sample price at that capacity is item 34. (e) The capacity that acts in every lower bound of the theory is the degree of the statistic or query the attacker reads (items 27 and 32), which $p$ does not bound. The budget keeps $p$ for the measured side, and the proven side uses $G$ and the degree.

Sketch. Each part cites the result named. Part (e) is a reading of the register, and the claim that no bound of the theory depends on $p$ otherwise is checked against items 11 to 34 (proven, by reading).

Regime. Capacity is a property of the attacker's family and needs no oracle. In the computational regime the relevant capacity is the degree, by item 27.

## 4. What the current theory supports or blocks

Supports.

- Item 2. The oracle has value only to a bounded attacker, and `def-learning-attacker` is the bounded attacker the oracle is for.
- Item 11. The shadow-run price $\Theta(k/a^2)$ binds every attacker, so it is a floor for the learning attacker's $n$ in pairs.
- Items 15, 16 and 34. The three places where the attacker pays what the trainer paid, which `prop-attacker-is-trainer-under-nature` collects.
- Item 17. The targeted reader has no learning price, which is why the universal learner is the class with one.
- Item 18. The proof of `thm-attacker-update-class-price` (a) and (b) is the proof there, moved from the trainer to the attacker.
- Item 24. The ceiling of the trainer's performance on the attacker's accuracy, part (a) of item 34.
- Item 26. The SQ embedding of SGD holds in the worst-rounding model only, which fixes handle one of `def-learning-attacker` (a).
- Item 27. The degree of a channel with the secret as label, which gives $a_k$ and $\lambda_k$ in part (d).
- Item 32. The statistic class is handle one, and its $c_2=0$ separation is the one place where the class enters a lower side.

Blocks or limits.

- Item 13 and item 20. Equivariance holds for SGD and fails for Adam, so the orbit prior of section 2.4 covers SGD attackers only, and about 400 representations identify a 64-bit seed, so a named-mode learning attacker with that many shadow pairs is seed-known and every seed-blind price is capped.
- Item 22. Lattice reduction beats every statistical-query tester, so a bound for $\mathcal L$ with handle one or two says nothing against an attacker that runs LLL.
- Item 25. The extraction gap vanishes against square-loss gradient trainers, so a statement about $\mathcal L$ must declare the loss, which `def-learning-attacker` does.
- Item 28. The exponent is not a unit, so the price of `thm-attacker-update-class-price` is stated in steps at a noise level, never as an exponent alone.
- Item 31. A ratio of 86 between a measured and a proven side is a bracket. The theory needs the factor at which a price counts as met, and this round does not fix it.
- Item 33. Per-example normalization closes the update channel for every observer, the learning attacker included. Its pricing as a defence belongs to `defence-as-honest-constraint`.
- Decision 3 of section 10. The gradient attacker embedded in SQ is handle one. This round adds handle two and keeps the two games unmixed.
- Section 8, the core. The batch-one attacker without injected noise on a law outside the single-index family is outside every object here.

## 5. The statement from this aspect

A learning attacker is a declared learner, a model family, a loss, an optimizer with its batch, steps and noise, and a readout, trained on observations the oracle supplies, and its budget is the vector of observations, steps, batch and parameters. No lower bound binds an attacker because it learns. A bound binds it through what it reads, through the noise of its own updates, or through an assumption on every efficient algorithm, and each statement of the theory names which. The attacker pays what the trainer paid exactly when its observations are the trainer's data in law, which holds for a release that answers with nature's noise at nature's inputs, and for correlational learners under any centred noise. A price is known when a declared learning attacker's measured budget meets a proven bound of a class that contains it, in the same unit, within a factor the theory has still to fix.
