---
model: claude-fable-5-1
discussant: fable
date: 2026-10-27
prompt: lab/theory/council/2026-10-27-theory-directions/pseudorandomness-for-learner-classes/prompt-critique.md
---

# Critique of the meditation on pseudorandomness for learner classes

## What I read and what I checked

I read, in the order the prompt fixes, `lab/theory/CONTEXT.md`, the council `README.md`, the readings of 27 and 26 October, the meditation, and the registered objects it cites in `sink/formalizing/results.md`, `facts.md` and `problems.md`. I also read the full statement of `thm-extraction-exponent-price` in `lab/theory/spaces/hard-problem-mappings/round-02/builder.md`, the lemma `lem-level-set-moment-balance` in the round 01 builder of the same space, the note `lib/literature/notes/neurips/AKMSS21.md`, and sections 4 and 5 of `lab/theory/readings/2026-10-27-definitions.md`. I did no web search. Every attribution to a paper that is not in the registers is marked from memory, unverified.

I checked every proof of the seven claims line by line. I recomputed the Gamma-function arithmetic of claim 5, the ReLU network and the step count of claim 6, the tilt constant of claim 2, and the update covariance of the section Next. Two statements fail as written, one in each of claims 1 and 3. Every other statement is true, and two proofs need a repair.

## Claims

### def-class-pseudorandom-channel

Truth of (a). The statement holds and the proof is complete (proven). Distinct inputs almost surely, so the lazily sampled values are independent draws of $\Pi_{s,W}$ and independent of the inputs. This is the definition of lazy sampling and carries no content.

Truth of (b). A definition, so neither true nor false, and its three conditions each block a named trivialization, as the proof says. Two defects remain.

ch-chosen-input-reference. Blocks. The advantage is written as $\Pr[A^{\Pi_s^\circ}=1]$ in a named access mode, and the modes include chosen inputs. Oracle access to a law of $(U,W)$ at a chosen input $u$ is not fixed by the law. It is either a fresh draw of $W$ from the conditional law at each query, or one draw per distinct input kept for repeats. The two differ on both sides of the game. Under the fresh-draw reading, a family with deterministic labels $W=f_s(U)$ and a non-degenerate $\Pi_{s,W}$ is told from the reference by querying one point twice and checking agreement, with advantage one (proven, one line). Under the kept-draw reading the reference is a random function, which is what the meditation's prose says, and what the formula does not define. The definition is therefore under-specified in one of its four named modes, and the mode in which the random oracle was supposed to be canonical is exactly the one left open. The repair is one sentence per mode, with the reference for chosen inputs written as the lazily sampled random function with values i.i.d. $\Pi_{s,W}$, and the honest oracle for random labels fixed to one of the two readings.

ch-budget-order. Does not block. Condition (b) writes $\beta_A>\beta_T$, with the trainer in records and the attacker in Train calls or in a VSTAT parameter. The order is not defined across units, and an SQ budget is already a pair, queries and tolerance. The definitions reading of 27 October records this as the open unit problem and proposes the exponent as the unit. Under that proposal (b) becomes well-posed and item 20 reads $e_{\mathrm{att}}/e_{\mathrm{tr}}=2$. The definition should either require one unit for both parties or adopt the exponent.

Label. The label proven is right for (a) and vacuous for (b).

Novelty. None, and the meditation says so in its first pushback. With common marginals the notion is sample-access outcome indistinguishability of the constant predictor, Dwork, Kim, Reingold, Rothblum and Yona, STOC 2021 (from memory, unverified). In the polynomial-time class with random examples it is the weak pseudorandom function of Naor and Reingold (from memory, unverified). In the chosen-input mode it is the object of Naor and Rothblum, Learning to impersonate, ICML 2006, who relate learnability under adaptive queries to pseudorandomness (from memory, unverified). That last paper is the one the meditation's To-read list lacks and the one closest to its title.

Verdict REVISE.

### prop-distinguishing-versus-weak-learning

Truth of (a). Holds (proven, rechecked). Under $P^\circ$ every $h$ has risk at least $\ell^\circ$. The query $\ell(h(X),Y)$ at tolerance $\epsilon/3$ answers below $\ell^\circ-2\epsilon/3$ under $P_s$ on the learner's success and above $\ell^\circ-\epsilon/3$ under $P^\circ$ for every output. Threshold $\ell^\circ-\epsilon/2$ separates, with advantage at least $1-\delta$.

Truth of (b). The statement holds, the proof as written does not (proven, with the repair below). The path argument is right. The exact $P^\circ$ answers fix the path, and if every path query had gap at most $\tau$ under $P_s$ those answers would be valid for $P_s$ and the output would be 0. The kept query has gap $g\ge\tau/2$. Hoeffding's lemma gives the tilt a gain of at least $\lambda g-\lambda^2/8$. The proof then sets $\lambda=4g$ and reads off $2g^2\ge\tau^2/2$. The learner does not know $g$. It knows an estimate $\hat g$ with $\lvert\hat g-g\rvert\le\tau/4$. With $\lambda=4\hat g$ the gain is $2g^2-2(\hat g-g)^2$, which is above $3\tau^2/8$ and need not reach $\tau^2/2$. With the fixed choice $\lambda=2\tau$ the gain is $2\tau g-\tau^2/2\ge\tau^2/2$, since $g\ge\tau/2$ (proven). The statement survives with $\lambda=2\tau$ and no knowledge of $g$.

ch-tilt-parameter. Does not block. Replace $\lambda=4g$ by $\lambda=2\tau$ in the proof of (b).

ch-perfect-distinguisher. Does not block. Part (b) assumes a deterministic algorithm that outputs 1 on $P_s$ against every valid oracle and 0 on $P^\circ$. That is a distinguisher of advantage one at a fixed $s$. The definition of claim 1 averages over the prior and allows advantage $\epsilon<1$. For that case (b) says nothing, and the title's "equals" is qualitative. The standard repair is the boosting argument that runs the distinguisher as a weak learner against the current predictor, which is the content of the multicalibration and outcome-indistinguishability papers the meditation lists (from memory, unverified).

Truth of (c). Holds (proven, rechecked). The gain of $h$ over the constant $EY$ is $2\,\mathrm{Cov}(Y,h)-E(h-EY)^2$, so gain $\epsilon$ forces covariance at least $\epsilon/2$. For $h=EY+\tau(g-Eg)$ with $\lvert g\rvert\le1$ the gain is $2\tau\,\mathrm{Cov}(Y,g)-\tau^2\mathrm{Var}(g)\ge2\tau^2-\tau^2=\tau^2$. With common marginals $\mathrm{Cov}_{P_s}(Y,g(X))$ equals the gap of the statistic $yg(x)$ between $P_s$ and $P^\circ$, so square-loss weak learning is exactly a correlational statistic with a gap.

Truth of (d). Holds (proven). $E[Y\mid X]=0$, so the best square-loss predictor is the constant 0. Given $Y=y$ the variable $Z$ is $\pm y$ with equal probability, so $E[Z\mid Y]=0$ and $E[h_2(Z)\mid Y]=(Y^2-1)/\sqrt2\ne0$, hence $k^*=2$. The label marginal is $N(0,1)$ by symmetry, so the family has common marginals and the reference is $N(0,I_d)\otimes N(0,1)$. For binary labels every statistic is $a(x)+yb(x)$ and its gap under common $X$ marginal is a covariance, so the three readings meet.

Truth of (e). Holds given `fact-xu-usable-information-definition` and the hypothesis that the family contains $\nu$ as a side-information-free predictor, which makes $H_V(Y)=H(Y)$ (proven given the fact).

Label. Proven, right.

Novelty. Each part is known. The equivalence of statistical queries and correlational queries for Boolean labels is Bshouty and Feldman, JMLR 2002 (from memory, unverified). The distinguisher-to-predictor step by an exponential tilt is the boosting step of Hébert-Johnson, Kim, Reingold and Rothblum, ICML 2018, and of the outcome-indistinguishability paper (from memory, unverified). Its computational analogue, KL-hardness of prediction against indistinguishability, is Vadhan and Zheng, STOC 2012 (from memory, unverified). The proposition's service to the project is to pin the loss, and the square-loss counterexample (d) does that.

Verdict REVISE.

### prop-class-pseudorandomness-collapse

Truth of (a). Holds (proven, rechecked). Unbounded algorithms attain the total variation. The chi-square of the mixture against the product is $E_{s,s'}(E_{P^\circ}[L_sL_{s'}])^n-1$ with $L_s=dP_s/dP^\circ$, and $E_{P^\circ}[L_sL_{s'}]=1+\chi_{P^\circ}(P_s,P_{s'})$ since $EL_s=1$. Then $\mathrm{TV}\le\frac12\sqrt{\chi^2}$. This is the second-moment method, and $\chi_{P^\circ}(P_s,P_{s'})$ is the pairwise correlation of FGRVX17.

Truth of (b). Holds up to one conflation (proven given the registered facts).

ch-sq-average-case. Does not block. The decision problem $B(\{P_s\},P^\circ)$ of FGRVX17 is worst-case over the planted law, while the advantage of claim 1 is averaged over the prior with a tolerance $\epsilon<1$. The registered Theorems 3.7 and 3.13 bound the worst case. The average case is the randomized statistical dimension of Feldman, COLT 2017, which the meditation lists as unread (from memory, unverified). The sentence should name which of the two it means.

Truth of (c). The statement is true for a fixed direction $u$ and false under the definition it invokes (proven, with the counterexample below). The proof writes $X=Zu+X_\perp$ for one $u$, computes the gap as $\sum_{1\le j<k}c_jE[T(Y)h_j(Z)]$, and that computation is right. For $k\le k^*$ every term vanishes by the definition of $k^*$, and for $k>k^*$ the test $q=h_{k^*}(\langle u,\cdot\rangle)$ with $T(y)=E[h_{k^*}(Z)\mid Y=y]$ has gap $E[(E[h_{k^*}(Z)\mid Y])^2]>0$. That test depends on $u$. The claim opens with "take the notation of `def-class-pseudorandom-channel`", whose advantage puts the supremum over tests outside the expectation over the prior, and it speaks of a family.

ch-collapse-prior-average. Blocks. Under the prior-averaged advantage with a test fixed before $u$ is drawn, the "only if" fails for every odd $k^*$. Counterexample. Let $Y=Z+\varepsilon$ with $\varepsilon\sim N(0,\sigma^2)$ independent of $X$. Then $E[h_1(Z)\mid Y]=Y/(1+\sigma^2)\ne0$, so $k^*=1$. Take $k=2$, so $q$ is affine, $q(x)=\langle v,x\rangle+c$. The gap at $u$ is $\langle u,v\rangle E[T(Y)Z]$ for every $T$, and its average over $u$ uniform on the sphere is zero. So every test of the stated class has prior-averaged advantage zero while $k>k^*$, and the family is exactly pseudorandom in the sense of claim 1 at degree 2. In general, for $q$ of degree at most $k^*$ the prior-averaged gap is $E_u[c_{k^*}(u)]\,E[T(Y)h_{k^*}(Z)]$, where $c_{k^*}(u)=E[q(X)h_{k^*}(\langle u,X\rangle)]$ is a homogeneous polynomial of degree $k^*$ in $u$, and its spherical average vanishes for odd $k^*$ by the symmetry $u\mapsto-u$ (proven). For even $k^*$ the test $q=\sum_ih_{k^*}(x_i)$ has $c_{k^*}(u)=\sum_iu_i^{k^*}>0$ and the "only if" survives (proven). Two-sample tests of the form $T(y)T(y')\langle x,x'\rangle^{k^*}$ have a gap free of the sign of $u$ and restore the equivalence for every $k^*$ (heuristic, the constant not computed here). The repair is to state (c) for a fixed $u$, with the supremum inside the prior, or to enlarge the class to tests of two samples. The second repair is the better one, since it is the class in which low-degree detection is actually priced.

Label. Proven, right for (a) and (b), wrong for (c) as written.

Novelty. None, and the meditation claims none. Part (c) is the definition of the generative exponent of DPLB24, registered as `fact-generative-exponent-sq-recovery-bound`, read against the product reference.

Verdict REVISE.

### thm-bayes-release-loss-matched-price

Truth. Every part holds (proven, rechecked). (a) is the tower property with $E\xi=0$ and $\xi$ independent of $X$. (b) is linearity of $E[(f_\theta(X)-Y)\nabla_\theta f_\theta(X)]$ in $Y$ given $X$, under the stated integrability and the interchange of gradient and expectation. (c) follows because the excess square risk under $P$ is $E(h-m_P)^2$ and the two oracles, or the two gradient fields with the same injected noise, give the output the same law. (d) is immediate, since a sign of mean $m_P(x)$ has the conditional law of $Y$ given $X=x$.

Label. Proven, right.

Novelty. The mathematics is a tower property. Its use is the strongest observation of the meditation. It shows that `thm-extraction-exponent-price` separates trainer from extractor only because the trainer's algorithm reads $y^2$, a statistic outside the correlational class, and that a gradient trainer on $P_\natural$ would pay the extractor's price $d^2$ itself. The record of 26 October did not say this, and `lib/theory/2026-10-26-what-we-have.md` item 20 should carry it. The consequence drawn in the prose, that no learning one-way setup of extraction type exists for square-loss population gradient trainers, is proven in the population and correlational-oracle units.

ch-population-units. Does not block. The budget in (c) is steps of a population method or the tolerance of a correlational oracle. In samples, the identity breaks through $E[Y^2\mid X]$ against $m_P^2+\sigma^2$, as the proof's last sentence says. The sample-priced version of the theorem is open, and it is the same object as the channel of the section Next. The statement should say that its unit excludes samples.

ch-bayes-release-only. Does not block. The release is the exact Bayes predictor. A fitted release $f_{\hat\theta}$ has $m_{R}\ne m_P$ and (a) fails. The registered open problem on extraction of a fitted release stands, and the theorem should name it.

Verdict ACCEPT.

### prop-extraction-gap-information-exponent

Truth of (a). Holds (proven, rechecked). If $E[h_k(Z)\mid Y]=0$ almost surely then $E[Yh_k(Z)]=0$, so $k_{\mathrm{IE}}\ge k^*$. For $Y'=m_P(Z)+\sigma\xi$ the Hermite coefficients $E[Y'h_k(Z)]$ equal those of $Y$, so $k_{\mathrm{IE}}(Q_{m_P,\sigma})=k_{\mathrm{IE}}(P)$ and the same inequality applies. The first half is DPLB24 Proposition 2.6, registered as `fact-generative-below-information`, which the claim should cite in place of a fresh proof.

Truth of (b). Holds given (a) and the exponents of `thm-extraction-exponent-price` (proven). One cosmetic point. The theorem's trainer price is $O(d^{\max(1,k^*(P)/2)})$, so the trainer's exponent is $\max(1,k^*/2)$ and the ratio is at most $(k_{\mathrm{IE}}/2)/\max(1,k^*/2)\le k_{\mathrm{IE}}/k^*$. The stated bound holds and is loose when $k^*(P)=1$.

Truth of (c). Holds (proven, recomputed). With $t=z^2$ the integral gives $E[\lvert Z\rvert^pe^{-Z^2/2}]=\Gamma(\tfrac{p+1}{2})/\sqrt{2\pi}$. Then $E[m_\natural(Z)h_2(Z)]=(\Gamma(2)-\Gamma(1))/\sqrt{4\pi}=0$, because $\Gamma(2)=\Gamma(1)=1$, and $E[m_\natural(Z)h_4(Z)]=(\Gamma(3)-6\Gamma(2)+3\Gamma(1))/\sqrt{48\pi}=(2-6+3)/\sqrt{48\pi}=-1/\sqrt{48\pi}$. Odd coefficients vanish by evenness. So $k_{\mathrm{IE}}(P_\natural)=4$, and with $k^*(m_\natural)=4$ from `lem-level-set-moment-balance` and $k^*(P_\natural)=2$ from part (d) of the extraction theorem, equality holds in (a). The cancellation $\Gamma(2)=\Gamma(1)$ is the same fact as the Jacobian balance of the registered lemma, seen from the other side. That is a pleasing identity and the kind of mathematics `CONTEXT.md` asks for.

Truth of (d). Holds by inspection of `thm-blind-split-seed-separation`, whose labels are unconstrained and whose attacker target is the record or the pancake direction (proven).

Label. Proven, right.

Novelty. (a) is registered. (c) is a computation. The reading, that the gap of item 20 is the distance between the information exponent and the generative exponent of one label law, is correct and is the second-strongest observation of the meditation. The prose adds that a correlational trainer of $P_\natural$ pays $d^{k_{\mathrm{IE}}/2}=d^2$. That lower bound is Damian, Lee and Soltanolkotabi, COLT 2022, for correlational queries, and the online SGD rate $d^{k_{\mathrm{IE}}-1}$ is Ben Arous, Gheissari and Jagannath, JMLR 2021 (both from memory, unverified, and the meditation labels the first the same way).

ch-cite-registered-fact. Does not block. Part (a) should use `fact-generative-below-information` and the proof should shrink to the second sentence.

Verdict ACCEPT.

### thm-noisy-gradient-query-filter

Truth of (a). Holds (proven, rechecked). The kernels are Gaussian with common covariance $\eta_t^2\varsigma^2I$ and means apart by $\eta_t\Delta_s(\theta_t)$, so each step contributes $\lVert\Delta_s(\theta_t)\rVert^2/(2\varsigma^2)$ to the KL divergence along the null trajectory. The null trajectory is free of $s$, so the average over $s$ passes inside and is at most $T\bar\kappa_f/(2\varsigma^2)$. Pinsker and Jensen give $E_s\mathrm{TV}\le\sqrt{T\bar\kappa_f/(4\varsigma^2)}$. The hypothesis $\eta_t>0$ keeps the kernels non-degenerate.

Truth of (b). Holds by data processing and convexity (proven).

Truth of (c). Holds (proven, recomputed). For binary labels $\psi_\theta=a_\theta+yb_\theta$ with $\lVert b_\theta\rVert\le G$, and $\Delta_S(\theta)=E[\chi_S(X)b_\theta(X)]=\hat b_\theta(S)$. Parseval bounds $\sum_{\lvert S\rvert=k}\lVert\hat b_\theta(S)\rVert^2$ by $G^2$, so the average over uniform $S$ is at most $G^2/\binom nk$. Advantage $1/3$ needs $TG^2/(4\varsigma^2\binom nk)\ge1/9$, which is $T\ge4\varsigma^2\binom nk/(9G^2)$. The network is right. With $r$ the number of $-1$ coordinates in $S$, the function $1+\sum_{j=0}^{k-1}c_j\mathrm{ReLU}(r-j)$ has increments $f(r)-f(r-1)=\sum_{j<r}c_j$, which alternate $-2,2,-2,\dots$, so $f(r)=(-1)^r$ for $r=0,\dots,k$, and the last unit $j=k-1$ is used at $r=k$.

Truth of (d). Holds (proven). $L_{P_s}(\theta^\circ)=\ell^\circ$ because $Y$ has law $\nu$ under every $P_s$, the gradient at $\theta^\circ$ is $\Delta_s(\theta^\circ)$ under the hypothesis $\nabla L_{P^\circ}(\theta^\circ)=0$, and the descent lemma gives the drop $\lVert\Delta_s\rVert^2/(2\beta)$. The hypothesis on $\nabla L_{P^\circ}$ is automatic when the constant minimizer is interior and $\ell$ is differentiable, since then $E_\nu\ell'(c^*,Y)=0$ factors out of $E_\mu\nabla_\theta f_{\theta^\circ}(X)$.

Label. Proven, right.

Novelty. Parts (a) and (c) restate the variance bound of Shalev-Shwartz, Shamir and Shammah, ICML 2017, whose Section 3 bounds the gradient variance over an orthogonal target family by $G^2$ over the family size, and the noisy-gradient failure of Abbe and Sandon, NeurIPS 2020 (both from memory, unverified). The meditation says as much. The KL chain-rule form is clean and I would keep it in the booklet as a borrowed result with its own proof once the two papers are read.

ch-filter-is-sq. Does not block. The meditation presents the theorem as a handle on gradient learners beyond the SQ embedding. The vector $\psi_\theta$ is a vector of $p$ statistical queries, and $\Delta_s(\theta)$ is their gap. The theorem is an SQ bound for the specific query set an architecture asks, finer than the generic embedding of `fact-sq-simulates-minibatch-sgd` and still inside SQ. The third question of the topic is therefore not answered by it. The only candidate in the meditation that leaves SQ in the correlational sense is the batch covariance of the section Next, and it is unproven.

ch-clipped-gradient. Does not block. Part (c) assumes $\lVert\psi_\theta\rVert_2\le G$ for every $\theta$. For the ReLU architecture that computes $\chi_S$ the raw gradient is unbounded in $\theta$, so $G$ presupposes clipping, which the statement should name. The bound then applies to the clipped method and the architecture that computes the target.

Verdict ACCEPT.

### prop-equivariant-learner-orbit-prior

Truth. Holds (proven, rechecked). $D_{hs}$ has the law of $hD_s$, equivariance in law gives $A(D_{hs})\overset d=h\cdot A(D_s)$, and $r(h\cdot g,hs)=r(g,s)$ by the change of variable $x\mapsto h^{-1}x$ inside $P_{hs}$. The risk of $A$ is constant on the orbit, so it equals its Haar average, which is the Bayes risk of $A$ under the orbit prior, which is at least the Bayes-optimal risk under that prior. The composition of two equalities in law is legitimate because the law of $A$'s output depends on its input only through the input's law and independent internal randomness.

Label. Proven, right.

Novelty. None. The $O(d)$ case with sparse targets is Ng, ICML 2004, where rotationally invariant learners need $\Omega(d)$ samples for a one-sparse target (from memory, unverified). The equality of the best equivariant risk with the Haar-Bayes and minimax risks is the Hunt-Stein theorem for compact groups, in Lehmann and Romano, Testing Statistical Hypotheses, chapter 8 (from memory, unverified), and the meditation labels it the same way. `thm-blind-orbit-limit` is the same averaging with the seed-blind server in place of the learner, as the meditation says. The reading, that equivariance is the exact sense in which a random oracle enters a gradient learner, is right and is a good sentence for the booklet.

ch-orbit-closure. Does not block. The family must be closed under $H$ for $P_{hs}$ to be a member, and the statement should say so.

Verdict ACCEPT.

## The computation of the section Next

I recomputed the per-example update covariance (proven). With $g=(\langle\theta,X\rangle-Y)X$ and $Y=\langle u,X\rangle\xi$, the mean is $\theta$ under $P_u$ and under the reference, since $E\xi=0$. The second moment is $E[\langle\theta,X\rangle^2XX^\top]-2E[\langle\theta,X\rangle YXX^\top]+E[Y^2XX^\top]$. The Gaussian fourth moment gives $\lVert\theta\rVert^2I+2\theta\theta^\top$ for the first term, the cross term vanishes with $E\xi$, and $E[\langle u,X\rangle^2XX^\top]=I+2uu^\top$. Subtracting $\theta\theta^\top$ gives $(1+\lVert\theta\rVert^2)I+\theta\theta^\top+2uu^\top$ under $P_u$ and $(1+\lVert\theta\rVert^2)I+\theta\theta^\top$ under the reference, as stated. Part (a) of Next is then immediate from claim 6 with $\bar\kappa_f=0$ (proven). Note that the drift $-\eta\theta$ contracts $\theta_t$ toward zero from $\theta_0=0$, so $\lVert\theta_t\rVert$ stays at the noise scale and the spike $2uu^\top$ is not diluted by the model (proven, one line).

Part (b) is a spiked-covariance problem under the Gaussian surrogate the meditation flags. The observed update of a batch of size $b$ with injected noise has covariance $\Sigma_u/b+\varsigma^2I$, so the spike has strength $2/(1+\lVert\theta\rVert^2+b\varsigma^2)$ relative to the bulk, and the sample count at which a rank-one spike of strength $\lambda$ in dimension $d$ becomes recoverable scales as $d/\lambda^2$, which gives $T\asymp d\,(1+b\varsigma^2)^2$ (heuristic, the BBP scaling for spiked Wishart matrices, from memory, unverified). The updates are products of Gaussians rather than Gaussian vectors, so the surrogate is where a proof would spend its effort. The reading of the AKMSS21 threshold $b\rho^2$ as the closing of this channel is a heuristic with the right form, since the rounding scale $\rho$ hides batch fluctuations of scale $1/\sqrt b$ exactly when injected noise $\varsigma$ hides a covariance of scale $1/b$ (heuristic).

This is the one statement in the meditation that is new to the record, measurable with the oracle, and priced in learning units, namely steps $T$ against $d(1+b\varsigma^2)^2$. It is also the sample-priced remainder of claim 4. The two should be one object.

## The meditation as a whole

### Against Halil's aim

Halil's first sentence asks for a measurable bound on the success of a VAE or a shadow model given the setting, in place of cryptographic bounds that practice beats. The meditation spends claims 1 to 3 on definitional equivalences and reaches its own conclusion that the single-party notion is notation. That conclusion is right and useful, because it stops the project from publishing outcome indistinguishability under a new name, which Halil ruled out as "just handing a framework". It is also where the meditation drifts. No claim prices a shadow learner. No claim measures anything. No claim uses the designer's programming rule of 27 October. The three-party frame of the reading is answered in the negative, auditor excluded, trainer and attacker as one type, and that answer is correct, but the meditation does not then return to Halil's own words and ask what the notion buys the attacker's price.

Where it does serve the aim is claims 4 and 5. They answer his second sentence, that attacks come from learning algorithms, with a sharp statement. A loss-matched learning attacker that re-learns a Bayes release pays the trainer's price in population or correlational units (proven), and the one gap in the record exists because the trainer used a non-correlational query (proven). That is a measurable prediction with a stated target. The learning curve of a square-loss shadow learner on released answers coincides with the trainer's learning curve on data, up to the batch-noise term. Halil's rule that experiments follow the claim is met, and the oracle supplies both curves.

On his constraints. No cryptographic plug-in appears. Claims 6 and 7 are realizable by experiment in steps and in samples. The mathematics of claims 4, 5(c) and 6(a) is short and clean. The definition (b) of claim 1 is three ad hoc conditions and is the ugliest object here, and it is also the one the meditation itself asks to drop.

### The strongest idea

Claims 4 and 5 read together with the section Next. Extraction is re-learning for loss-matched classes, the only gap in the record is $k_{\mathrm{IE}}/k^*$ of one label law, and the remaining channel from a trainer that learns nothing is the second moment of its batch updates. That triple is a theory of one small object, the linear model on $Y=\langle u,X\rangle\xi$, with a proven part, an open part and an experiment. It is what `CONTEXT.md` asks for.

### What to drop

The name learning one-way function and condition (b) of claim 1. The meditation's own pushback 4 is right, and claim 4 proves that the object is empty for the trainer class the aim cares about. The single-party definition as a contribution. The auditor as a party of the same type, as pushback 6 says. Claims 2 and 3 as results. They should stay as notes that pin the loss and name the known invariants, each with its reference once read.

### What it missed

1. How the reference is realized. The product of marginals is the permutation null. For the attacker, pair each secret with the view of an independent run, which costs one extra Train call per sample and produces exactly $\Pi_s^\circ$ (proven, independence of runs). For the trainer, shuffle the labels. Under Halil's rule of 27 October this is an admissible programming of the oracle, since every view handed out is an honest view of some run (heuristic, a reading of the rule). This makes the notion measurable and the meditation never says it.
2. How the advantage is measured. A supremum over a class is not an experiment. Item 9 of the reading of 26 October already says that a profile is measurable only for a named family of attacks, from below, with theory supplying the upper band. The pseudorandomness advantage inherits that, and the meditation should have said where its numbers come from.
3. The trainer's own case against the reference is the random-label experiment of Zhang, Bengio, Hardt, Recht and Vinyals, ICLR 2017, in which networks fit shuffled labels (from memory, unverified). The reading's sentence "memorization is the rise on the random part" has that experiment as its measurement, and the meditation does not connect them.
4. Naor and Rothblum, ICML 2006, on learnability against pseudorandomness under adaptive queries, which is the chosen-input mode of claim 1 (from memory, unverified).
5. The sample-priced version of claim 4 and the fitted release. Both are where the real trainer lives, and the meditation puts the first in Next and the second nowhere.
6. The third question of the topic. The update class is an SQ query set, so nothing in the meditation leaves SQ except the unproven batch covariance. The honest answer is that the question is open, and the meditation should say it in one sentence rather than present claim 6 as the handle.
7. The claim in the prose that a learner of time $t$ outputs a predictor of time at most $t$ holds for circuits, where the output has size at most $t$, and fails for uniform descriptions, where a short program may run long (proven, trivially). The reading of 27 October carries the same sentence and should carry the same caveat.

### The three questions of the topic

Can learnability and security be one notion. As notation, yes, and it is outcome indistinguishability of the constant predictor against a learner class (from memory, unverified, pending the search). As a result, no, by claim 3, and the meditation agrees.

Does the learning one-way function fit the extraction and seed-separation results. Item 20 fits only with an SQ trainer that reads $y^2$ against an SQ extractor, and not for a gradient trainer (proven in population units by claim 4, heuristic in samples). Item 15 does not fit, because its attacker target is not a function of the trainer's target and its hardness is a trapdoor on the seed with borrowed or statistical hardness behind it (proven by inspection). The name should go.

What can be said for gradient learners of a fixed architecture beyond the SQ embedding. Two true things and one open thing. The architecture's update class gives an SQ bound with the architecture's own query set (claim 6, proven, still SQ). Equivariance makes every secret a Haar-random one on its orbit (claim 7, proven). The batch covariance is a correlational-blind channel that may leak what the drift does not (Next, open). The dynamics of information exponents along the trajectory remain the open core, as the meditation says.

## Challenges in one list

| Challenge | Claim | Blocks |
| --- | --- | --- |
| ch-chosen-input-reference | def-class-pseudorandom-channel | yes |
| ch-budget-order | def-class-pseudorandom-channel | no |
| ch-tilt-parameter | prop-distinguishing-versus-weak-learning | no |
| ch-perfect-distinguisher | prop-distinguishing-versus-weak-learning | no |
| ch-collapse-prior-average | prop-class-pseudorandomness-collapse | yes |
| ch-sq-average-case | prop-class-pseudorandomness-collapse | no |
| ch-population-units | thm-bayes-release-loss-matched-price | no |
| ch-bayes-release-only | thm-bayes-release-loss-matched-price | no |
| ch-cite-registered-fact | prop-extraction-gap-information-exponent | no |
| ch-filter-is-sq | thm-noisy-gradient-query-filter | no |
| ch-clipped-gradient | thm-noisy-gradient-query-filter | no |
| ch-orbit-closure | prop-equivariant-learner-orbit-prior | no |

## Verdicts

```text
VERDICT def-class-pseudorandom-channel REVISE
VERDICT prop-distinguishing-versus-weak-learning REVISE
VERDICT prop-class-pseudorandomness-collapse REVISE
VERDICT thm-bayes-release-loss-matched-price ACCEPT
VERDICT prop-extraction-gap-information-exponent ACCEPT
VERDICT thm-noisy-gradient-query-filter ACCEPT
VERDICT prop-equivariant-learner-orbit-prior ACCEPT
BLOCKING 2
```
