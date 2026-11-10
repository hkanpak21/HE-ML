---
model: claude-fable-5-1
discussant: fable
date: 2026-10-27
prompt: lab/theory/council/2026-10-27-theory-directions/oracle-as-random-oracle/prompt-critique.md
---

# Critique of the meditation on the oracle as a random oracle

## Verdict

The meditation answers its own question honestly. Reading the seed table as a lazily sampled random oracle names four techniques the theory already uses and adds one rule, programming, which is a definition of admissible measurement devices. I accept two of the eight claims as written, ask for revision of six, and reject none. Six challenges block. Each has a fix of a few lines, and none touches the direction. The strongest idea is thm-short-seed-dichotomy, which turns the seed-blind idealization into a statement about a 64-bit key and prices it in samples and queries. The weakest part is the definition of admissibility, whose choice of $Z$ makes the meditation's own central example, the coupled twin, inadmissible under the unbounded class. The meditation drifts from Halil's aim in two places that matter. Its only price with both sides in hand has both sides proven, while Halil asked for a measured price meeting a proven one, and its attacker row holds no learning attacker.

## The question of the topic

What the random-oracle reading buys beyond language. Heuristic, since it depends on what counts as a new statement. The five techniques give nothing new, by the meditation's own audit, which I checked against the registered proofs. Lazy sampling is the proof of thm-replay-audit-steer (a). lem-scrambled-seed-urn is a switching lemma with the birthday bound $N^2/(2(M-N))$. lem-needle-lower-bound and the clause of thm-exact-twin-price on calls at other inputs are query-counting arguments, since the coupled runs agree until a call lands in the perturbed set. def-identity-coupling reruns the learner at a held seed. lem-agreement-detection takes $p^2$ from Jensen's inequality over the shared secret. The one new object is the admissibility rule, and it is a definition with two one-line corollaries. The meditation's strongest result, the short-seed cap, uses no random-oracle reasoning at all. So the frame buys a vocabulary and one definition.

Whether programming admits canaries and release noise and excludes a plug-in. Proven for each clause, under the meditation's definitions with the correction of ch-z-includes-unread-values. In-distribution canaries that replace honest records, all of them included, are a perfect programming of the data oracle and change no price. The inclusion-bit design of prop-canary-audit-unbiased-not-sound is not a programming unless the honest trainer subsamples. Random-label and out-of-distribution canaries change the law of the released model, so they are admissible only against classes that cannot separate the two model laws, and against the unbounded class the question is the total variation between those laws, which no drawn-seed experiment certifies below one by thm-coupling-certificate (a)(iii). An auditor that draws and keeps the release noise programs the noise oracle perfectly. Release noise as a defence is not a programming of any oracle, since it adds a node. A generator's output programmed into a uniform oracle is admissible against time-bounded classes by part (d) of prop-programming-preserves-prices, so programming does not exclude the plug-in. By part (b) an admissible programming moves no success by more than $\varepsilon$, so nothing a programming admits can be a source of hardness for the class it is admissible against. That sentence is the answer the meditation circles and never states.

What an experiment measures for each party. The table of the meditation is right in shape, with two corrections. The auditor's row is the only one with both sides in hand, and both sides are theorems, so it is not an instance of the measured-meets-proven price Halil described. The attacker's row has a lower band from declared attacks and an upper bound from theory only on laws the experimenter builds, as def-known-price (c) says, and the learning attacker Halil named, a shadow model or a VAE, appears in no row.

## Claims

### prop-programming-preserves-prices

Statement. Part (a) is true, and it is the lazy-sampling equivalence. Part (b) is true under its hypothesis, and the hypothesis carries the whole weight. The test that runs $A$ and checks the win must lie in $\mathcal C$, so $\mathcal C$ is a class of tests on $Z$ at least as strong as the attacker class, and the meditation names one class for both roles without saying so. The bracket on prices follows from monotonicity of the price in $s$, which I checked. Part (c) is false as written. Part (d) is false as written by a time term.

Proof check. (a) and (b) hold line by line. (b) is the standard argument that indistinguishable hybrids have close success probabilities. It is the fundamental lemma of game playing in Bellare and Rogaway, EUROCRYPT 2006, and the sequence-of-games method in Shoup's 2004 manuscript, both from memory, unverified, with no lemma number claimed.

Label. Proven is right for (a) and (b). The object is a definition with two corollaries, and the context says definitions alone are not results, so the right prefix is def- with a remark.

ch-z-includes-unread-values. Blocking. $Z$ includes the oracle values at $P$. The body claims that the auditor's twin, which programs the seed table at the twin's call with the recorded seed, leaves the law of $Z$ unchanged because the twin reaches no party. Under the definition this is false. Write $M$ for the released model, $\rho$ for the real run's seed and $\rho'$ for a fresh seed. In the programmed setup the pair $(M,\rho)$ enters $Z$, and in the honest setup the pair $(M,\rho')$ does. Their total variation is $\int\mathrm{TV}(P^x_\rho,\bar P^x)\,\mu(d\rho)$, the mean grip of prop-seed-grip-duality (proven, by writing the total variation of the mixture $\mu(d\rho)P^x_\rho(dm)$ against the product $\mu(d\rho)\bar P^x(dm)$). For deterministic kernels with atomless $\bar P^x$ it equals one, and the test $\mathbf 1[M=\mathsf L(x;\rho)]$ attains it, since two independent draws from an atomless law coincide with probability zero. So the identity coupling is inadmissible against the unbounded class under the meditation's own definition, and the twin programming is not perfect either, since the programmed value is a copy of other randomness. The fix is to let $Z$ hold the views of the parties other than the designer and nothing else. Then the twin is admissible at $\varepsilon=0$, in-distribution canaries that replace records stay perfect, and the admissibility of random-label canaries becomes a question about the class, as it should be.

ch-price-units. Blocking. Part (c) compares a price, which is a budget, with $\varepsilon$, which is an advantage. Read literally it is false. Let the honest setup give every attacker of budget below $100$ success $\tfrac12$ and every attacker of budget at least $100$ success $\tfrac12+2\varepsilon$. Let the programmed setup raise the first group to $\tfrac12+\varepsilon$ and leave the second. Every success moves by at most $\varepsilon$, so the programming is $(\mathcal C,\varepsilon)$-admissible, and the price at level $\tfrac12+\varepsilon$ moves from $100$ to $0$ (proven, by the definition of the price). The bracket of (b) allows this, since it places the programmed price between the honest prices at $\tfrac12$ and $\tfrac12+2\varepsilon$. The fix is to state (c) in success units. A modification that moves the success of some $A\in\mathcal C$ by more than $\varepsilon$ is not an admissible programming. The sentence on defences then stands, with a working defence read as one that lowers some success by more than $\varepsilon$.

ch-prg-time-accounting. Blocking. Part (d) claims admissibility against classes of time $T$ at $\varepsilon=\mathrm{Adv}_G(T)$. The distinguisher of the hybrid runs the whole setup on the challenge string before it runs the test, so its time is $T$ plus the setup's time, and the right bound is $\mathrm{Adv}_G(T+T_{\mathrm{setup}})$. The meditation does this accounting correctly in thm-short-seed-dichotomy (b). The fix is one term.

Non-triviality. None as mathematics. As a rule it is useful once $Z$ is fixed.

### prop-key-free-defence-rule

Statement. Part (a) is a tautology on the defended channel and an overstatement beyond it. Part (b) is the simulation argument and is correct. Part (c) is labelled heuristic and its conclusion is contradicted by a registered result.

Proof check. (b) holds for every class closed under composition with a sampler of $K$. For the unbounded class and for polynomial time with an efficiently samplable kernel this is immediate. For the SQ class, a query $\varphi$ on the defended law is the query $v\mapsto\mathbb E_\omega\,\varphi(K(v;\omega))$ on the undefended law, so closure holds when the query class is all bounded measurable functions.

ch-key-free-a-overstated. Not blocking. The sentence that a gap between the parties is never a gap between their information is false when a party holds other channels. The split-learning server holds the labels, and a model consumer may hold a validation set. The fix is to add "through that channel".

ch-rotation-is-a-kept-key. Not blocking, since the example is stated under the hypothesis that the rotation is erased. The hypothesis fails for every split protocol the registered results cover. The client applies $W$ to every record, trains it, and needs it at inference, so $\omega=W$ is an input to other nodes and reaches a party, and the legitimate output is computed with $\omega$. By the meditation's own criterion in (b), the seed-blind rotation of $\mathcal P_H$ is a kept key, which is what the section on short seeds says in other words. The two passages should agree.

ch-rounding-is-noiseless-clwe. Blocking. Rounding each record's coordinate along $v$ to the grid $\gamma\mathbb Z$ gives layers of width zero. These are records with exactly discrete hidden labels, and prop-blind-lll-label-recovery, registered and accepted, recovers the labels and the direction from $d+1$ representations in polynomial time in the exact-arithmetic model. So the rounded law is the easy case, and the clause that the registered results price its reconstruction by hCLWE is false in the model where those results are proven (proven, by the registered statement). The fix is to add Gaussian noise of width $\beta$ along $v$ after rounding, which is again a key-free kernel, and to check that the result lies in the parameter range of fact-clwe-hardness. The general point of (c) survives the fix. A key-free kernel can plant, so the ban on planting must live in the instance class, as the meditation says.

Label. Proven for (a) and (b) is right once (a) is narrowed. Heuristic for (c) is right, and the heuristic is false as stated.

Non-triviality. (b) is the data-processing inequality. The useful content is the classification, and one of its three examples is wrong.

### prop-canary-audit-unbiased-not-sound

Statement. (a), (b) and (c) are true as written. I recomputed each.

Proof check. (b). $\mathbb E\,\mathbf 1[g_i=b_i]=\tfrac12\Pr[g=1\mid b=1]+\tfrac12(1-\Pr[g=1\mid b=0])=\tfrac12+\tfrac12\mathrm{Adv}$, so $\mathbb E\hat A=\mathrm{Adv}/2$. This is the identity between membership advantage and the probability of a correct guess in Yeom, Giacomelli, Fredrikson and Jha, IEEE CSF 2018, from memory, unverified. (c). At $L^{**}$ the lookup test gives $g_i=b_i$ exactly, so $\mathrm{Adv}=1$. At $L^*$ it gives $g_i=b_i$ on the seed-one branch and $g_i=0$ otherwise, so $\mathrm{Adv}=\tfrac12$. The two-point argument is correct. Let $B$ be the event that the band exceeds $\tfrac14$. Soundness at $L^*$ gives $\Pr_{L^*}[B]\le\alpha$, the seed-one branch has probability $\tfrac12$, and the law of the triple of model, canaries and bits at $L^{**}$ is the conditional law at $L^*$ on that branch, so $\Pr_{L^{**}}[B]\le2\alpha$. The Hoeffding width $\sqrt{\ln(1/\alpha)/(2N)}$ is right for $N$ independent run-level averages in $[-\tfrac12,\tfrac12]$.

ch-canary-inclusion-not-programming. Blocking for the body's sentence that canaries program the data oracle, as applied to this setting. The run trains on the honest data and the included canaries, so the dataset has $n+\mathrm{Bin}(m,\tfrac12)$ records and the law of the released model is not the honest law. A programming fixes oracle values at points of the honest dataflow. It does not add records or exclude them. The setting is a programming only when the honest trainer already subsamples each record with probability $\tfrac12$ and the designer learns the subsampling bits by programming the seed table. Otherwise the inference from prop-programming-preserves-prices, that the measurement reports the honest price, is unavailable. The fix costs nothing. Let the canaries replace $m$ honest positions and let all of them be included. Let the baseline of (a) be the attack's success on fresh draws from $\mathcal D$ evaluated on the one released model. Then the programming is perfect, $\hat A$ is the difference of two empirical means and is unbiased for $\mathrm{Adv}$, and (c) holds verbatim with the same $L^*$ and $L^{**}$.

Label. Proven is right.

Non-triviality. (b) is known. (c) is a two-point lower bound of Le Cam's kind, elementary and useful. Its content is that one run estimates a seed-level average and cannot certify it, and that the certificate costs $N$ runs whatever $m$. The parallel to fact-one-shot-estimate-consistency is fair. The one-run audit of Steinke, Nasr and Jagielski, NeurIPS 2023, from memory, unverified, is sound over the class of differentially private mechanisms with the privacy parameter as its target, so it has a different class and a different target, and (c) neither contradicts nor reproduces it.

### thm-short-seed-dichotomy

Statement. True as written. The preliminary claim that every real implementation lies outside $\mathcal P_{O(d)}$ is true for $d\ge2$. The orbit of a nonzero matrix under right multiplication by $O(d)$ is a manifold of positive dimension, so an invariant law with an atom there would carry uncountably many atoms of equal mass (proven, elementary). At $d=1$ the orbit has two points and the argument fails, which is harmless.

Proof check. (a). If the truth $t$ is in a comparison, the oracle's answer lies within $\tau<\eta/2$ of $P_t(A)$ and at distance at least $\eta-\tau>\eta/2$ from the other candidate's value, so $t$ wins. The truth wins every comparison it enters and is the last champion after $|S|-1$ comparisons. In the sample game Hoeffding's inequality at deviation $\eta/2$ gives $2\exp(-N\eta^2/2)$ per set, and the union over the $|S|-1$ sets that involve $t$ gives $N\ge2\eta^{-2}\ln(2(|S|-1)/\delta)$, which the stated bound rounds up. I recomputed the number. At $\eta=\tfrac12$, $|S|=2^{64}$ and $\delta=10^{-2}$ the bound is $8(65\ln2+\ln100)=397.3$, so "about 400" is right. (b) is the generator hybrid with the correct time term.

Known result. (a) is the Scheffé tournament for a finite class of laws, in Devroye and Lugosi, Combinatorial Methods in Density Estimation, Springer 2001, from memory, unverified, with Yatracos's 1985 construction behind it. The content here is the observation that the seed-blind idealization caps every statistical and SQ lower bound at the seed's size, and the tournament is only the tool.

ch-sq-cap-is-inapplicability. Not blocking. The consequences say that prop-sq-blind-reconstruction-bound is capped at $|S|-1$ queries. The registered bound assumes an $O(d)$-invariant initialization law, which a finite seed violates, so the bound does not apply to the implementation rather than being capped. The right sentence is that no SQ lower bound above $|S|-1$ queries can hold for any implementation with $|S|$ seeds.

ch-sq-cap-unmeasurable. Not blocking. A price of $|S|-1$ queries at $|S|=2^{64}$ is one no experiment realizes, and so is $\exp(\Omega(c_0^4d))$. Under Halil's constraint both the ideal and the finite seed-blind SQ games are unmeasurable, and the measurable game is the sample game with a declared polynomial-time attacker, where (b) says the measurement reports the pseudorandomness of the implementation's generator composed with one run. The consequences should say this.

Label. Proven is right.

Non-triviality. The mathematics is standard. The statement is the most consequential in the meditation for Halil's constraints, since it says which registered results are statements about a 64-bit key.

### prop-replay-audit-uninstantiable

Statement. (a) and (b) are true. The body's claim that the audit has the exact structure of the uninstantiability of Canetti, Goldreich and Halevi is false in the order of its quantifiers.

Proof check. (a). The learning function $L_h$ returns $t_0$ at the single seed $h(\mathrm{cm},0)$ and $m_1$ elsewhere, its reach is $\mu(\{h(\mathrm{cm},0)\})=0$ under atomless $\mu$, and the prover that outputs $(t_0,0)$ is accepted by the replay at that seed. Correct. (b). Each replay is a draw at $\rho\sim\mu$ with fresh hardware randomness, the event that it lies within $\tau$ of $T$ has probability $p_\tau(T)$ whatever the prover does, and a win requires one such event, so the union bound gives $n_{\mathrm{rep}}\,p_\tau(T)$. Correct, and independence from the prover's output is not even needed.

ch-cgh-quantifier-order. Not blocking. Canetti, Goldreich and Halevi, STOC 1998 and J. ACM 2004, from memory, unverified, build one scheme that is secure in the random-oracle model and insecure under every instantiation, the order being one scheme for all $h$. Part (a) builds, for each $h$, a learning function $L_h$ that depends on $h$, the order being one $L_h$ per $h$. The weaker order is the folklore observation that a public function is not a random oracle to a party that reads its description, and it is what the phrase "over the class of all learning functions" quietly grants. The comparison to Canetti, Goldreich and Halevi should go. Goldwasser and Kalai, FOCS 2003, from memory, unverified, is the reference for Fiat-Shamir in particular, with the same caveat on order.

ch-commitment-in-learning-function. Not blocking. The final document fixes $x$ with the dataset inside it and a commitment $\mathrm{cm}$ that the auditor can open. $L_h$ evaluates $h(\mathrm{cm},0)$, so it needs $\mathrm{cm}$ as a function of $x$. With a deterministic commitment this holds. With commitment randomness from a finite set, $L_h$ returns $t_0$ on the finite set of seeds $h(\mathrm{cm},0)$ over all openings, which is still $\mu$-null. The proof should say which.

Label. Proven is right.

Non-triviality. (a) is near-trivial once the order is seen. (b) is a remark on thm-replay-audit-steer and belongs there. The replay audit is already flagged as a plug-in result in the register, and the meditation's own frame says the random oracle buys non-interactivity at the price of the factor $q+1$. I would drop the object and keep (b) as a remark.

### prop-seed-grip-duality

Statement. (a), (b) and (c) are true.

Proof check. (a). Joint convexity of total variation gives $\mathrm{TV}(\int P^x_\rho\,\mu'(d\rho),\bar P^x)\le\int\mathrm{TV}(P^x_\rho,\bar P^x)\,\mu'(d\rho)\le g_x$, and the hybrid over $k$ nodes uses the supremum over inputs because downstream inputs depend on upstream outputs. (b). The total variation of a product against a product is at most the sum of the marginal total variations, then convexity in $\rho$. The diagonal is null under $\bar P^x\otimes\bar P^x$ when $\bar P^x$ is atomless, so the probability of a coincidence under the identity coupling is at most the total variation to the independent coupling, at most $2g_x$. (c). A point mass against an atomless law has total variation one.

ch-grip-exactly. Not blocking. The sentence that hardware randomness makes a short seed safe exactly as far as it makes the seed name worthless states an equality. The proposition proves one upper bound $g_x$ for both quantities. At $g_x=1$ the two coincide for deterministic kernels, and for intermediate grips the sentence is one-directional. Write "at least as far as".

ch-grip-upper-bound-unmeasurable. Not blocking, and it matters for Halil's constraint. (a) needs $g_x$ from above. A two-sample classifier between reruns at a named seed and fresh-seed runs gives a lower bound on $\mathrm{TV}(P^x_\rho,\bar P^x)$ by data processing, and it is itself a learning problem priced in learning units, which fits Halil's aim. No registered certifier gives an upper bound on the total variation of two atomless laws of trained models, and thm-coupling-certificate (a)(iii) is the registered form of that obstacle for a related pair of laws. So the direction of the duality that would make a finite seed safe without a generator assumption is, today, unmeasurable, and the meditation should say so.

Known result. The grip is a cousin of reproducibility in Impagliazzo, Lei, Pitassi and Sorrell, STOC 2022, from memory, unverified, which shares the seed and varies the data, while the grip shares the data and varies the hardware randomness against the seed.

Label. Proven is right.

Non-triviality. Convexity of total variation. The definition is the useful part, since it is the only object in the meditation that could price a finite seed against every class without a generator assumption, and the meditation undersells it.

### prop-rise-decomposition-replace-one

Statement. (a) and (b) are true and known. The counterexample of (c) is correct. The bound of (c) is true up to a constant in the binary case with a uniform label marginal and needs its own statement otherwise.

Proof check. (a). $(D^{(i)},z_i)$ has the law of $(D,z')$, since $z_i$ is independent of $D^{(i)}$ and $D^{(i)}\sim\mathcal D^n$, and each seed enters its own expectation through its marginal, so the coupling of the two seeds is irrelevant. Summing gives training accuracy minus $b$ equal to $\mathrm G+\mathrm M$, and $\mathrm M$ equals training accuracy minus test accuracy, the generalization gap. (c). On $\mathcal D$ the threshold at $\tfrac12$ fits about $0.8$ of the sample, so the learner memorizes with high probability, its training accuracy is one, its test accuracy tends to $0.8$, and $\mathrm M\to0.2$. On $\mathcal D^\circ$ every threshold has true accuracy $\tfrac12$, the class of threshold classifiers has finite VC dimension, so the best empirical fit is $\tfrac12+O_P(n^{-1/2})$ and falls below $0.7$, the learner outputs the majority constant, and $\mathrm C\to0$. Correct. For the bound of (c), in binary classification with uniform labels the random-label fit minus $\tfrac12$ is half the empirical Rademacher complexity, and symmetrization bounds the expected generalization gap of empirical risk minimization by twice the Rademacher complexity, so $\mathrm M\le4\mathrm C$ in that case (heuristic, from memory, unverified, the constants being those of Bartlett and Mendelson, JMLR 2002). For a non-uniform label marginal the random labels are not symmetric signs and the relation to a complexity needs its own statement.

ch-rise-is-borrowed. Not blocking. (a) is the replace-one identity between the expected generalization gap and expected stability, in Bousquet and Elisseeff, JMLR 2002, and in Shalev-Shwartz, Shamir, Srebro and Sridharan, JMLR 2010, from memory, unverified, with no theorem number claimed. $\mathrm M$ is the average of the replace-one form of Feldman's memorization score, STOC 2020, from memory, unverified. The object should be a fact- entry once the papers are in the library, with the counterexample of (c) as the only new piece.

Label. The mixed label is right and honest.

Non-triviality. (b) is the useful sentence for Halil's measurement question. The mean memorization costs one run and held-out data, and only the per-record score costs the twin price of thm-exact-twin-price. That link should be stated as such.

### def-known-price

Definition. Well posed. It is the standard notion of a tight bound with the upper side measured.

ch-certified-is-not-proven. Blocking for (b). The definition says a proven witness is a statement valid at $J$. (b) offers the coupled certificate of thm-coupling-certificate and the drawn-seed certificate of thm-black-box-certifiability as proven witnesses. Both are random outputs sound at level $\alpha$ over a class of learning functions. Neither is a statement valid at $J$. Under the definition as written (b) is false, and the bracket of the definition then holds with probability at least $1-2\alpha$ in place of $1-\alpha$. The fix is a third kind of witness, the certified witness, sound at level $\alpha$ over a named class of learning functions, with the probability adjusted. This third kind is the one Halil's oracle produces, so it deserves the name.

ch-known-price-both-sides-proven. Not blocking. (a) presents the auditor's price as the first price of the theory with both sides in hand. Both sides are theorems in thm-exact-twin-price, the lower bound and the matching coupled certificate, and the certificate's accuracy at the zero-leakage function is proven, not measured. So (a) is a tight theorem, which is good, and it is not an instance of the price Halil described, where the oracle measures one side and the theory proves the other. The sentence should say which it is.

Label. Proven for (a) and (b), open for (c), is right once (b) is fixed. (c) is the honest sentence of the meditation. No certificate sound over every learning function exists for the SQ or gradient classes, so their prices are known only on laws the experimenter builds.

## The meditation as a whole

Direction against Halil's aim. Heuristic. Halil's aim is a bound on the success of a learning attacker in learning units, measured and proven, with hardness from the flow of information and modifications allowed when they give a law to compute expectations over. The meditation serves the auditor's side of that aim well. It does not serve the attacker's side. No claim prices a learning attacker, the gradient attacker of the definitions reading is absent, and the only computational statements are a generator hybrid and a key-free simulation. The meditation is honest about this in its last pushback and in def-known-price (c).

Where it drifts. Three places. First, the admissibility rule reads Halil's sentence in CONTEXT.md faithfully, as indistinguishability of a programmed value from an honest sample, while the integrator's reading in the aim document is broader, a modification allowed when it gives a known law to compute expectations over. The meditation's conclusion that the rule cannot admit release noise as a defence follows from the narrow reading. It should be put to Halil as a choice between two readings of his own words, with the two-rule proposal as the consequence of the narrow one. Second, the meditation introduces the designer as a fourth party. Halil's frame has three, and the designer is the auditor in every example given, so the fourth party is a name for the auditor's extra knowledge. Third, the price with both sides in hand is a theorem on both sides, as said above.

Strongest idea. thm-short-seed-dichotomy with the atoms argument. It converts an idealization the theory has leaned on into two numbers an experiment can check, about 400 representations for an unbounded server to identify a 64-bit seed and $|S|-1$ queries for an SQ one. It says plainly that the polynomial-time seed-blind results of the theory rest on the pseudorandomness of the implementation's generator composed with training. That is a measurable statement about a component of the procedure. It is close to the excluded plug-in, and Halil's rule should decide whether an assumption on an existing component counts as one. The grip is the second idea, and the only one that could make finite seeds safe without that assumption.

What should be dropped. The five techniques, kept as one paragraph of language. prop-replay-audit-uninstantiable, with its (b) moved to a remark on thm-replay-audit-steer. prop-rise-decomposition-replace-one (a) and (b) as new objects. def-known-price (a) as the headline price. The sentence that programming is what coupled runs do, which the meditation itself drops and which ch-z-includes-unread-values shows to be false under its own definition.

What it missed. Five things. First, the sentence that answers the topic's second question, that an admissible programming is price-neutral and so can never be a source of hardness for the class it is admissible against, so the programming rule need not exclude a plug-in. Second, the relation between the lazily sampled seed table and the random-oracle reference of the aim document. These are two different uses of the random oracle. The seed table is a keyed family with one fresh key per name, as the meditation says. The reference is the law $\mathcal D^\circ$ in the trainer's row of the table. The meditation uses both and never relates them, and the other topics of the council build on the second. Third, the learning attacker. Fourth, the measurability of the grip from above. Fifth, that under finite seeds the seed-blind SQ game is unmeasurable in both its ideal and its finite form, so the only measurable seed-blind attacker is a declared polynomial-time one.

Beauty. Heuristic. The atoms argument and the Scheffé tournament are clean. The grip is a clean definition. The admissibility bookkeeping with $P$, $\nu$, $V$ and $Z$ is the ugly part, and def-known-price is bookkeeping. The conjecture at the end, that the seed is worth the lesser of its code size and the NGCA price, is the kind of statement Halil asked for, the geometry of a code against a planted direction. It is well posed as written, and its lower side asks the SQ dimension argument of the registered proof to pack directions from the code rather than from the sphere, which that argument should allow (heuristic).

## Challenges

| Challenge | Attached to | Blocks |
| --- | --- | --- |
| ch-z-includes-unread-values | prop-programming-preserves-prices, definition of $Z$ | yes |
| ch-price-units | prop-programming-preserves-prices (c) | yes |
| ch-prg-time-accounting | prop-programming-preserves-prices (d) | yes |
| ch-rounding-is-noiseless-clwe | prop-key-free-defence-rule (c) | yes |
| ch-canary-inclusion-not-programming | prop-canary-audit-unbiased-not-sound, setting | yes |
| ch-certified-is-not-proven | def-known-price (b) | yes |
| ch-key-free-a-overstated | prop-key-free-defence-rule (a) | no |
| ch-rotation-is-a-kept-key | prop-key-free-defence-rule (b) | no |
| ch-sq-cap-is-inapplicability | thm-short-seed-dichotomy, consequences | no |
| ch-sq-cap-unmeasurable | thm-short-seed-dichotomy, consequences | no |
| ch-cgh-quantifier-order | prop-replay-audit-uninstantiable | no |
| ch-commitment-in-learning-function | prop-replay-audit-uninstantiable (a) | no |
| ch-grip-exactly | prop-seed-grip-duality | no |
| ch-grip-upper-bound-unmeasurable | prop-seed-grip-duality (a) | no |
| ch-rise-is-borrowed | prop-rise-decomposition-replace-one | no |
| ch-known-price-both-sides-proven | def-known-price (a) | no |

## Verdicts

```text
VERDICT prop-programming-preserves-prices REVISE
VERDICT prop-key-free-defence-rule REVISE
VERDICT prop-canary-audit-unbiased-not-sound REVISE
VERDICT thm-short-seed-dichotomy ACCEPT
VERDICT prop-replay-audit-uninstantiable REVISE
VERDICT prop-seed-grip-duality ACCEPT
VERDICT prop-rise-decomposition-replace-one REVISE
VERDICT def-known-price REVISE
BLOCKING 6
```
