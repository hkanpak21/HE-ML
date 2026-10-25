# Round 00, challenger

This file reads Definitions 1 to 3, Propositions 1 to 3 and the two leave-one-out models of the learning-oracle report (source `lib/reports/src/2026-10-16-halil-learning-oracle-definition.tex`, subsections "The oracle", "Three properties", "Two leave-one-out models" and "Approximation by a model bank"). It reads them against the adversary interface (`lib/reports/src/2026-10-16-halil-adversary-interface.tex`, subsections "The adversary" and "The order, and the two kinds of result"). The sources have no page numbers, so references name subsections. Every non-trivial claim carries one of the four labels. A claim marked "proven, sketch" has the proof idea written here, and the builder must write it out in full before it enters the theory.

Notation used throughout. $\mathsf L(m,D,\mathcal H;\rho)$ is the learning function at seed $\rho\sim\mu$, and $\mathsf{ev}(m,u;\sigma)$ the evaluation map. $\mathcal O$ is the oracle, $\Pi$ a policy and $(q_T,q_E)$ the budget. For two hypotheses $H_0,H_1$, $P_b$ is the law of the view under $H_b$. $\mathrm{TV}$ is total variation distance. For $\gamma\ge 1$, $\mathrm H_\gamma(P\|Q)=\sup_S\,(P(S)-\gamma Q(S))$ is the hockey-stick divergence.

## Challenges to the starting definitions

Five challenges are blocking. Each of them makes a stated proposition false or leaves a definition without a mathematical meaning. Fourteen are not blocking.

### ch-handle-laundering

This challenge is blocking. It targets def-learning-oracle (the access property), thm-own-data-only and thm-perfect-substitution.

Definition 1 lets Train take a handle as its starting model and lets a caller evaluate every handle it holds. Nothing stops a caller from training on a handle it may evaluate and not open. Take any learning function with $\mathsf L(m,\emptyset,\mathcal H;\rho)=m$, which every gradient method satisfies. A black-box adversary holding the served model's handle $h^*$ calls $\mathsf{Train}(h^*,\emptyset,\mathcal H,\bot)$, receives a fresh handle of its own, and opens it. It now holds $m^*$. Proposition 3 restricts references and seeds and says nothing about handles, so this adversary meets its hypothesis and gains white-box access. That contradicts the proof sentence "every answer is a value of $\mathsf L$ or $\mathsf{ev}$ on inputs it holds" (proven, by this counterexample). If the fresh handle is not openable, $\mathsf{Eval}$ on $\mathsf{Train}(h^*,D_{\mathrm{adv}},\mathcal H,\bot)$ still answers queries to a fine-tuned served model. No black-box adversary in the real procedure has that, so Proposition 1 fails for the same policy (proven).

The smallest fix is one rule. Train and Open require that the caller may open every argument, Eval requires that it may evaluate the handle, and a caller may open every handle its own calls return. Under this rule an eval-only handle cannot be laundered (proven, sketch: by induction on calls, every handle a caller may open is the output of a call whose arguments it may open, or a value the procedure releases to it through the plain channel).

### ch-substitution-policy

This challenge is blocking. It targets thm-perfect-substitution.

Proposition 1 claims equality in law of the view for every procedure, inputs and adversary. Read with Definition 2, where the adversary carries an arbitrary policy, it is false in both directions (proven, two counterexamples).

1. Upward. The adversary of Proposition 2(a) obtains $\mathsf L(m,P_I,\mathcal H;\rho)$ under the honest seed, a value the real procedure never shows it. Its advantage can be one where the real advantage is zero. Proposition 2(a) is therefore a counterexample to Proposition 1.
2. Downward. In $G^{\mathcal O}$ the oracle draws and hides the seed of every learning node unless the procedure fixes it, and closure hides the state inside training. A coalition that owns a learning node sees its own seed and every iterate in the real procedure, and sees neither in $G^{\mathcal O}$.

The proof sketch assumes what it needs in the sentence "the adversary's own calls have the law of the computation it would run itself". That holds only for calls the adversary could compute from its own view.

The smallest fix is to define the realizable policy $\Pi_G(A)$ of a coalition $A$ in $G$. Under it $A$ may open its own inputs, its own seeds, public seeds and every node value it receives through the plain channel, and may evaluate the models it has query access to in $G$. Owners in $A$ pass explicit seeds they drew. Proposition 1 is then stated for $\Pi_G(A)$ alone, for the joint law of the channel outputs of honest nodes and the adversary's call answers. With this restriction the induction of the report goes through (heuristic until the builder writes it against the schedule of ch-execution-schedule). Every policy strictly above $\Pi_G(A)$ is a different threat model, and the theory should say so in one sentence.

### ch-seed-naming

This challenge is blocking. It targets def-learning-oracle and thm-reference-access.

Definition 1 passes seeds by value, and closure says the oracle reveals no seed it drew. Proposition 2(a) assumes a policy that lets the adversary pass $\rho$, where $\rho$ was drawn by the oracle. No call of Definition 1 can do that. The hypothesis of Proposition 2(a) is therefore not expressible, and the experimenter cannot form the coupled leave-one-out model of a run whose seed the oracle drew. The clause "seeds those $\Pi_c$ makes public" does not help, because a public seed is a value the caller already sees.

The smallest fix is to store every drawn seed in the oracle's table under a handle and to let Train accept a seed handle. Seeds, datasets and models then share one naming mechanism, and the policy of ch-access-policy-simplify governs all three.

### ch-budget-semantics

This challenge is blocking. It targets def-learning-oracle-model and thm-own-data-only.

Definition 2 gives the adversary a budget $(q_T,q_E)$ and does not say whether it may compute $\mathsf L$ or $\mathsf{ev}$ without the oracle. Both readings break a stated claim.

- If it may, because it is unbounded and $\mathsf L$ is a known algorithm, the budget never binds. Proposition 3 then holds, and its closing sentence, "a result in the model is therefore an advantage as a function of $(q_T,q_E)$", says nothing.
- If it may not, Proposition 3 is false. With $q_T=0$ the adversary has nothing, and with a sampler and $q_T$ shadow models it gains, which is what shadow-model attacks do.

A second problem sits under the first. A bound of the form "for every $\mathsf L$ and every adversary with budget $q_T$, the advantage is at most $f(q_T)$" is false whenever $f$ depends on $q_T$, because a fixed adversary may have a fixed $\mathsf L$ hard-wired. The generic group model meets the same problem with a random encoding (Shoup, EUROCRYPT 1997, from memory, not read).

The smallest fix has two parts. The adversary is an oracle algorithm, computationally unbounded, that reaches $\mathsf L$ only through $\mathcal O$, while $\mathsf{ev}$ is public. Every budget-dependent statement then takes one of two quantifier patterns. An attack or an estimator is one procedure that works for every $\mathsf L$. An impossibility says that for every procedure some $\mathsf L$, or a random $\mathsf L$ from a stated family, defeats it. Upper bounds that hold for every adversary are free of the budget and are statements about laws. The problems below follow this pattern.

### ch-locality-ill-posed

This challenge is blocking. It targets def-learning-oracle.

"Uses $\rho_k$ only in decisions about record $k$" is not a mathematical condition, because a decision about record $k$ is undefined for an arbitrary learning function. The natural formal reading is that $\mathsf L$ depends on $(D,\rho)$ only through $\rho_0$ and the multiset of pairs $\{(z_k,\rho_k)\}_{k\in D}$. Every realization that ignores the record seeds satisfies that reading, including stochastic gradient descent that sorts the records by value and draws one shuffle of positions from $\rho_0$ (proven). That is the example the report calls not local. The formal reading thus admits what the informal one excludes, and no reading on laws can exclude it, since locality is a property of a realization and not of a law.

No proposition uses locality. It matters only for the coupled leave-one-out model, and there only for tightness and never for soundness (thm-coupling-certificate, part c).

The smallest fix is to delete locality from Definition 1. A theorem that needs it states it as a hypothesis on a named class of realizations, for instance iterative learning functions whose batch at step $t$ is $\{k:\rho_{k,t}<q\}$.

### ch-seed-domain

This challenge is not blocking. It targets def-learning-oracle.

The seed is $(\rho_0,(\rho_k)_{k\in K})$ over the set $K$ of keys, and fresh keys are assigned when a dataset is submitted. A caller cannot pass $\rho_k$ for a key that does not exist yet, and the coupled pair needs one seed defined on the keys of both datasets. Also $P_I=\{z_i:i\in I\}$ is written as a set and loses duplicates. The smallest fix fixes one countable key space $K$ in advance, takes the seed as $\rho_0$ together with a map $K\to\mathcal R_1$ under the product law, and writes $P_I$ as the multiset of keyed records $(i,z_i)_{i\in I}$. If locality is deleted, the record index leaves the seed and $\rho$ is a plain seed in $\mathcal R$.

### ch-redundant-properties

This challenge is not blocking. It targets def-learning-oracle.

Four of the six properties do not belong in Definition 1.

- Consistency follows from fidelity. If every answer equals $\mathsf L$ at its seed, equal calls with equal explicit seeds return equal models because $\mathsf L(\cdot\,;\rho)$ is a function (proven).
- Closure says the interface has three calls, which the definition already lists. Its list of what the oracle does not reveal adds only running time, which is a cost.
- Unit cost is part of the model of Definition 2, what a call costs the caller, and not of the oracle's answers.
- Locality is deleted per ch-locality-ill-posed.

The smallest fix leaves two properties. Definition 1 becomes a table of handles, three calls, fidelity (answers are $\mathsf L$ and $\mathsf{ev}$ at the given seed, or at a fresh seed independent of everything else that the oracle stores under a handle), and an access policy. Unit cost and the budget move to Definition 2.

### ch-access-policy-simplify

This challenge is not blocking. It targets def-learning-oracle.

The policy lists references, seeds, openable handles and an optional sampler, and adds a rule on how handles travel. With ch-seed-naming and ch-handle-laundering every object lives in one table, and the policy reduces to one label per pair of caller and handle, from the list open, eval (models only) and none. Train and Open need open on every argument. Eval needs eval or open. A caller may open what its own calls return. The procedure sets the labels of honest node values through its channels, the plain channel giving open and query access giving eval. Two further gaps close with this.

- A dataset that mixes honest records and the adversary's records, the input of every poisoning step, cannot be written, since $D$ is either a reference or a dataset by value. Let $D$ be a multiset union of handles.
- The sampler is not an oracle call. It is an input node of the procedure whose output the adversary may open, so its records become ordinary handles.

### ch-handle-opacity

This challenge is not blocking. It targets def-learning-oracle and thm-perfect-substitution.

"A fresh handle" is not specified. If handles are counters, a handle the adversary receives tells it how many Train calls other callers made before, which leaks whenever the honest procedure makes a data-dependent number of calls, as early stopping does. Interleaving the adversary's calls with honest ones is harmless in the ideal oracle only when handles carry no information. The smallest fix draws handles uniformly from a set of size $2^\lambda$, or takes the view up to renaming of handles.

### ch-reference-advantage-one

This challenge is not blocking. It targets thm-reference-access, part (a).

The hypothesis $\mathsf L(m,P_I,\mathcal H;\rho)\ne\mathsf L(m,P_{I\cup\{j\}},\mathcal H;\rho)$ is an event in $\rho$. The test that outputs 0 exactly when the released model equals the recomputed one has advantage

$$p_j=\Pr_\rho\big[\mathsf L(m,P_I,\mathcal H;\rho)\ne\mathsf L(m,P_{I\cup\{j\}},\mathcal H;\rho)\big]$$

(proven). Under the report's own example of Poisson subsampling at rate $q$ over $T$ steps, record $j$ is never sampled with probability $(1-q)^T$, the two models coincide, and the advantage is at most $1-(1-q)^T$ (proven). The smallest fix states the advantage as $p_j$, which equals one exactly when the inequality holds almost surely.

### ch-plugin-test-rate

This challenge is not blocking. It targets thm-reference-access, part (b).

The first sentence of part (b) is correct. Under drawn seeds the oracle answers have the same conditional law given the view under both hypotheses, adaptive calls included, so the total variation of the joint law equals that of the view (proven). The second sentence is correct for finite views and weaker and broader in its suggestion than it should be.

1. Rate. For a view with $k$ values, the plug-in test from $q$ samples per hypothesis has expected excess loss at most $2\sqrt{k/q}$, uniformly over all laws with $k$ values (proven, sketch: the loss is at most $\|\hat p_0-p_0\|_1+\|\hat p_1-p_1\|_1$, and $\mathbb E\|\hat p-p\|_1\le\sqrt{k/q}$). The proposition should state this rate. Almost sure convergence gives no budget.
2. Scope. A model is not a finite view. For atomless views no adversary has a uniform rate (proven, sketch in thm-black-box-certifiability, part c). The report's sentence suggests the oracle closes the gap to the optimal test, which it does only for finite views.
3. Samplability. The plug-in test needs the view to be samplable under the policy. Here the view is one node value and it is. In a dataflow graph with other honest inputs it is not.
4. Scope of the remark on differential privacy. Policy (b) is the adversary of differential privacy for one neighbouring pair, an L-aware adversary and an unbounded budget. Differential privacy quantifies over all pairs. The sentence should say "for a fixed pair".

### ch-execution-schedule

This challenge is not blocking. It targets def-learning-oracle-model.

Definition 2 does not say when the adversary acts, and every composition result needs it. The smallest fix runs the nodes in one fixed topological order. Before each node the adversary receives the channel outputs of the nodes run so far, makes oracle calls, and sets its choices for that node. The execution is interactive and the view is its transcript.

### ch-learning-function-choice

This challenge is not blocking. It targets def-learning-oracle and def-learning-oracle-model.

The interface report lists the learning function of a node among the adversary's choices, for instance training code shipped to clients or the loss of split learning. Definition 1 fixes one $\mathsf L$. The smallest fix indexes the oracle by a family $(\mathsf L_\lambda)_{\lambda\in\Lambda}$ and lets Train take $\lambda$, which is a choice when the adversary owns or ships the node. Aggregation stays a member of the family whose data space is the model space.

### ch-eval-budget-vs-allowance

This challenge is not blocking. It targets def-learning-oracle-model.

The report counts Eval calls "as the interface report counts label queries against the allowance $Q$". The allowance is a parameter of the procedure, HE-OFT's per-client limit. Eval on the adversary's own shadow models is computation. Counting both in $q_E$ mixes a protocol limit with a resource, and calls the allowance a budget, against the terminology ledger. The smallest fix, given that $\mathsf{ev}$ is public (ch-budget-semantics), makes Eval on handles the caller may open free and uncounted. Then $q_E$ counts Eval on handles it may only evaluate, and the procedure's allowance caps $q_E$ for the served model.

### ch-bank-fidelity-reuse

This challenge is not blocking. It targets def-model-bank.

"Fidelity therefore holds on $\Delta$ by construction" is true of answers one at a time. Fidelity also requires answers with drawn seeds to be independent. If one bank entry answers two drawn-seed calls, in two executions or in two calls with equal inputs, the answers are equal. An estimate from $N$ executions then has the variance of the number of distinct entries and not of $N$. The definition says nothing on drawn-seed calls, since a call in $\Delta$ has an explicit seed. The smallest fix lets a drawn-seed call consume an unused entry with equal $(a,D,\mathcal H)$ and refuses it when none remains. The empirical oracle is then a learning oracle on the calls it answers (proven, by construction).

The bank also holds samples of $\mathsf L(\cdot\,;\rho,\xi)$ with hardware randomness $\xi$ outside the seed. Fidelity holds in law when $\xi$ is part of the drawn randomness, and consistency fails. The theory should name $\xi$, and thm-replay-audit-steer uses it.

### ch-bank-design-game

This challenge is not blocking. It targets def-model-bank and the sentence "One bank thus serves all $n$ records".

The design in which each record enters each run with probability one half estimates, for record $j$, the advantage in a game where the rest of the dataset is a uniformly random half of the pool. That game differs from Proposition 2's game with a fixed $I$, which is the game differential privacy bounds. The two can differ maximally (proven, thm-bank-soundness part b). The sentence is true of the random-subset game alone. The smallest fix names that game as the estimand.

### ch-experimenter-equality-test

This challenge is not blocking. It targets the experimenter paragraph under the two leave-one-out models.

The experimenter "tests a claimed equality of laws, such as exact unlearning". From independent samples of atomless laws a test can reject equality, and its acceptance certifies nothing. No certifier sound for every learning function certifies $\mathrm{TV}<1$ on any atomless pair (proven, sketch in thm-coupling-certificate part a). The smallest fix says that the experimenter can falsify exact unlearning, and can certify it only through a coupling event.

### ch-loo-models-simplify

This challenge is not blocking. It targets the two leave-one-out models.

The independent leave-one-out model is a sample from the law under $H_0$ and nothing more, since the advantage of any test is a difference of two marginal probabilities (proven). Naming it adds an object. The coupled one depends on the realization of $\mathsf L$ and not on its law (ch-locality-ill-posed), so "what record $j$ did in this run" is a property of the realization. The smallest fix keeps one object, the coupled pair under a named realization, where it earns its place, which is in certificates (thm-coupling-certificate).

### ch-degenerate-oracles-undefined

This challenge is not blocking. It targets def-learning-oracle-model and the non-triviality bar of the README.

The bar refers to two degenerate oracles that the report describes in words. With ch-substitution-policy and ch-access-policy-simplify they get exact forms. The top policy $\Pi_\top$ opens every handle, honest datasets and honest seeds included. The bottom is $\Pi_G(A)$ held by an L-aware adversary (ch-budget-semantics), which is the real procedure. Every policy lies between them, and every theorem should name the policy it assumes.

## Problems

One principle links the five problems. I state it as heuristic, since the problems test it. An upper bound on leakage or on steering is certifiable from oracle calls, for every learning function, when it reduces to the probability of an event the oracle can sample. A lower bound is always certifiable, because the advantage of any one test is such a probability. thm-coupling-certificate proves the two ends of the principle for distinguishing. The other four apply it to black-box access, to the model bank, to composition through a dataflow graph and to steering.

All five assume the corrected definitions of the challenges above: one table of handles under the label policy, an adversary that reaches $\mathsf L$ only through $\mathcal O$ with $\mathsf{ev}$ public, the quantifier patterns of ch-budget-semantics, and the interactive schedule of ch-execution-schedule. One lemma serves three problems and is worth stating once, as lem-atomless-two-point. It is part (a) of thm-coupling-certificate. A suggested order of work is lem-atomless-two-point, thm-coupling-certificate, thm-black-box-certifiability, thm-bank-soundness, thm-dataflow-composition, thm-replay-audit-steer.

| Requirement | Problems |
| --- | --- |
| privacy, distinguish | thm-coupling-certificate, thm-black-box-certifiability, thm-bank-soundness, thm-dataflow-composition |
| security, steer | thm-replay-audit-steer |
| composition with adaptivity and channels | thm-dataflow-composition |
| what oracle calls certify | thm-coupling-certificate, and parts of the other four |
| Eval budget against Open | thm-black-box-certifiability |
| model bank | thm-bank-soundness |

### thm-coupling-certificate

Question. What can oracle calls certify about the distinguishing advantage of every adversary, uniformly over learning functions?

Procedure. One learning node and two hypotheses that fix its dataset, $D_0$ under $H_0$ and $D_1$ under $H_1$, neighbouring for instance. The view is $V_b=\kappa(\mathsf L(m,D_b,\mathcal H;\rho))$ for a channel $\kappa$, with law $P_b$. The best advantage of any adversary under the bottom policy is $\mathrm{TV}(P_0,P_1)$ whatever its budget (proven, data processing and Neyman and Pearson).

Certifier. The experimenter, with $N$ Train calls. It outputs $\hat t\in[0,1]$ and is sound at level $\alpha$ over a class $\mathfrak L$ of learning functions when $\Pr[\mathrm{TV}(P_0,P_1)\le\hat t]\ge 1-\alpha$ for every $\mathsf L\in\mathfrak L$.

Expected statement, in three parts.

(a) Drawn seeds certify nothing. Let $\mathfrak L$ contain every learning function and let the certifier make drawn-seed calls only. Then for every $\mathsf L$ with $P_0=P_1=P$ atomless, $\Pr_{\mathsf L}[\hat t\ge 1]\ge 1-\alpha$. Proven, sketch. Split the view space into $M$ cells $C_1,\dots,C_M$ of mass $1/M$ under $P$, with $M$ even. For $S\subseteq[M]$ with $|S|=M/2$, let $\mathsf L_S$ give $P_0=P(\cdot\mid\cup_{i\in S}C_i)$ and $P_1=P(\cdot\mid\cup_{i\notin S}C_i)$, so $\mathrm{TV}=1$. Draw $S$ uniformly. Given that the $2N$ samples fall in distinct cells, their joint law under the mixture over $S$ equals their joint law under $\mathsf L$. A collision has probability at most $2N^2/M$ under each, so the two sample laws are within $4N^2/M$ in total variation. Soundness on every $\mathsf L_S$ gives $\Pr[\hat t\ge 1]\ge 1-\alpha$ under the mixture, hence

$$\Pr_{\mathsf L}[\hat t\ge 1]\ge 1-\alpha-\frac{4N^2}{M},$$

and $M$ is arbitrary. Finite-precision models are not atomless. With atoms of mass at most $1/M$ the cells have unequal mass, and the bound should hold up to a constant (heuristic, the builder must redo the count). Whether the conclusion survives when $\mathfrak L$ is a structured class, transformers trained by stochastic gradient descent for instance, is open, because $\mathsf L_S$ need not lie in it.

(b) Shared seeds certify a coupling. For any realization,

$$\mathrm{TV}(P_0,P_1)\le\beta:=\Pr_\rho\big[V_0(\rho)\ne V_1(\rho)\big],$$

the coupling inequality (proven). From $N$ explicit-seed pairs with $K$ divergences, the Clopper and Pearson upper bound $\bar\beta_\alpha(K,N)$ is a sound certificate for every learning function, and $\bar\beta_\alpha(0,N)=1-\alpha^{1/N}\le\ln(1/\alpha)/N$ (proven). For a noise channel $V_b=f(\mathsf L(m,D_b,\mathcal H;\rho))+Z$ with $Z\sim\mathcal N(0,\sigma^2 I)$, and every $\varepsilon\ge 0$ and $\Delta>0$,

$$\mathrm H_{e^\varepsilon}(P_0\|P_1)\le\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)+\Pr_\rho\Big[\big\|f(\mathsf L(m,D_0,\mathcal H;\rho))-f(\mathsf L(m,D_1,\mathcal H;\rho))\big\|>\Delta\Big],$$

where $\delta_{\mathcal N}(\varepsilon;s)=\mathrm H_{e^\varepsilon}(\mathcal N(0,1)\|\mathcal N(s,1))$ (proven, sketch: joint convexity of $\mathrm H_\gamma$ over the mixture in $\rho$, and monotonicity of $\delta_{\mathcal N}$ in $s$). The tail is again a Bernoulli parameter and is certifiable the same way. Hardware randomness $\xi$ drawn independently in the two runs still yields a coupling, so soundness survives GPU nondeterminism and only tightness suffers (proven).

(c) Tightness depends on the realization. Some learning function has $\mathrm{TV}(P_0,P_1)=0$ and $\beta=1$, for instance $\mathsf L(m,D,\mathcal H;\rho)=\rho\oplus h(D)$ with $\rho$ uniform on $\{0,1\}^d$ and $h(D_0)\ne h(D_1)$ (proven). Open: a condition on the realization, with Poisson-subsampled iterative learning functions as the candidate, under which $\beta$ is at most a constant times $\mathrm{TV}$, or $\mathrm{TV}$ plus an oracle-measurable term, for channels that collapse the model (labels, quantized outputs).

Why it meets the bar. (1) $\beta$ and the tail are defined by Train calls with shared explicit seeds. (2) Without the oracle, a certificate on the total variation between laws of trained transformers needs those laws. (3) Part (b) holds for every learning function and uses it only through $\beta$ and the tail. (4) Part (a) is the bottom oracle for the experimenter, drawn seeds only, which is what the real procedure supplies, and it makes every certificate vacuous. Part (b) needs the reuse of an explicit seed that only the oracle supplies. The theorem separates the two seed disciplines.

Why it is not a textbook fact. The coupling inequality and two-point lower bounds are textbook. Three things are not. The explicit seed of the learning oracle makes a coupling samplable for every learning function. This is the only route to an upper certificate, by part (a). The tightness of that route is a property of the realization, by part (c). The closest prior work I recall is property testing for differential privacy (Gilbert and McMillan, 2018, from memory, not read). The builder must place and read it before claiming part (a) as new.

### thm-black-box-certifiability

Question. The interface report records Küpçü's question, when $Q$ label queries reach what the shared head reveals. In the oracle model, what can be certified about the black-box advantage at Eval budget $q_E$ compared with white-box access, and how many Train calls does an adversary need to use $q_E$ queries well?

Procedure and adversary. One learning node under $H_0$ or $H_1$ as in thm-coupling-certificate. The evaluation map has outputs in a finite set $\mathcal Y$ with $|\mathcal Y|=C$, labels for instance. The query universe $U$ is finite and may have size $2^d$. A black-box adversary makes $q_E$ adaptive Eval calls on the target handle, which it may evaluate and not open. Its strategy is a $C$-ary tree of depth $q_E$ whose internal nodes carry queries and whose leaves carry bits. Write $\mathcal T_q$ for the set of such trees, so that

$$|\mathcal T_q|\le |U|^{(C^q-1)/(C-1)}\,2^{C^q}.$$

The black-box optimum is $\mathrm{Adv}^{\mathrm{bb}}(q_E)=\max_{\tau\in\mathcal T_{q_E}}\big(\Pr_{H_1}[\tau=1]-\Pr_{H_0}[\tau=1]\big)$, and the white-box optimum is $\mathrm{Adv}^{\mathrm{wb}}=\mathrm{TV}(P_0,P_1)$ on the model. The adversary or the experimenter holds policy (b) of thm-reference-access, references to both datasets and drawn seeds.

Expected statement, in four parts.

(a) Black-box leakage is certifiable from both sides. From $N$ drawn-seed samples per hypothesis, with probability at least $1-\alpha$ and for every learning function,

$$\Big|\max_{\tau\in\mathcal T_{q_E}}\widehat{\mathrm{Adv}}(\tau)-\mathrm{Adv}^{\mathrm{bb}}(q_E)\Big|\le\epsilon_N:=\sqrt{\frac{2\ln(4|\mathcal T_{q_E}|/\alpha)}{N}},$$

so $N=O\big((C^{q_E}\ln|U|+\ln(1/\alpha))/\epsilon^2\big)$ samples suffice for accuracy $\epsilon$ (proven, sketch: Hoeffding's inequality and a union bound over $\mathcal T_{q_E}$).

(b) Exchange rate between Train and Eval calls. An L-oblivious adversary under policy (b) spends $q_T$ Train calls on its own shadow models, which it may open, so their Eval calls are free. If it plays the empirically best tree against the target, its advantage is at least $\mathrm{Adv}^{\mathrm{bb}}(q_E)-2\epsilon_{q_T/2}-\alpha$ for every learning function (proven, sketch). Open: a matching lower bound, a family of learning functions on which every adversary with $q_T\le c\,C^{q_E}/\epsilon^2$ falls short of the optimum by $\epsilon$. If it holds, each additional label query costs a factor $C$ in shadow models.

(c) White-box leakage is certifiable from below only. For every L-oblivious white-box adversary with $q_T$ Train calls and every $M$, some learning function has $\mathrm{Adv}^{\mathrm{wb}}=1$ and gives that adversary advantage $O((q_T+1)^2/M)$ (proven, sketch: lem-atomless-two-point with the challenge sample added to the shadow samples, and averaging over $S$ to fix one $\mathsf L_S$). By thm-coupling-certificate part (a) no drawn-seed certifier bounds $\mathrm{Adv}^{\mathrm{wb}}$ from above. Hence "$Q$ label queries reach the head" can be falsified and never certified from drawn seeds, while "the head reveals at least $x$ more than $Q$ labels" can be certified, through one white-box test and part (a) (proven, from the two parts). This fixes the form any answer to Küpçü's question can take.

(d) Shared seeds. With explicit-seed pairs and deterministic $\mathsf{ev}$, the probability $\Pr_\rho[\exists u\in U:\ \mathsf{ev}(\mathsf L(m,D_0,\mathcal H;\rho),u)\ne\mathsf{ev}(\mathsf L(m,D_1,\mathcal H;\rho),u)]$ bounds $\mathrm{Adv}^{\mathrm{bb}}(q)$ for every $q$, and $O(\ln(1/\alpha)/\epsilon)$ pairs certify it, whatever $q_E$ and $C$ (proven, from thm-coupling-certificate part b). Open: how loose this certificate is against the one of part (a).

Why it meets the bar. (1) Every quantity is defined by Train and Eval calls. (2) Without the oracle, the law of a trained transformer's labels on $U$ is needed. (3) The rates depend on the learning function only through $C$, $|U|$ and $q_E$. (4) Under $\Pi_\top$, one Train call with the honest seed gives advantage equal to the coupled divergence on the queried inputs. Composing the example of thm-coupling-certificate part (c) with a label map makes that one while $\mathrm{Adv}^{\mathrm{bb}}(q_E)=0$, so the ceiling of part (a) fails for the top oracle.

Why it is not a textbook fact. Uniform convergence over adaptive query trees is textbook learning theory. The exchange rate between Train and Eval calls uniform over learning functions, and the asymmetry between black-box access (certifiable from both sides) and white-box access (from below only), are not to my knowledge. I ran no search, so novelty is open.

### thm-bank-soundness

Question. What does a model bank of the kind membership attacks use actually estimate, how well, and for which game?

Procedure. A pool $P=(z_1,\dots,z_n)$ and a bank of $k$ runs. Run $i$ trains on $S_i$, which contains each record independently with probability $1/2$, under an independent seed. For record $j$ and a test $\tau$, a function of the view and of $z_j$, the estimate $\widehat{\mathrm{Adv}}_j(\tau)$ is the frequency of $\tau=1$ over runs with $j\in S_i$ minus that over runs with $j\notin S_i$. The random-subset game $G^{\mathrm{rs}}_j$ draws $S\subseteq[n]\setminus\{j\}$ with independent inclusion at rate $1/2$ and trains on $P_S$ under $H_0$ and on $P_{S\cup\{j\}}$ under $H_1$. The fixed game $G^{\mathrm{fix}}_{S,j}$ is the same with $S$ fixed, which is Proposition 2's game.

Expected statement, in four parts.

(a) Estimand and simultaneous error. For fixed $j$ and given the pattern of membership of $j$ across runs, the in-runs are independent draws of the $H_1$ view of $G^{\mathrm{rs}}_j$ and the out-runs of its $H_0$ view (proven, sketch: runs are independent, and in each run the inclusion of $j$ is independent of $S_i\setminus\{j\}$). For a finite test class $\mathcal T$, with probability at least $1-2\alpha$, simultaneously for all $j\in[n]$ and $\tau\in\mathcal T$,

$$\big|\widehat{\mathrm{Adv}}_j(\tau)-\mathrm{Adv}_{G^{\mathrm{rs}}_j}(\tau)\big|\le\sqrt{\frac{2\ln(4n|\mathcal T|/\alpha)}{k_{\min}}},\qquad k_{\min}\ge\frac{k}{2}-\sqrt{\frac{k\ln(2n/\alpha)}{2}}$$

(proven, sketch: Hoeffding's inequality per record and test, a union bound, and Hoeffding's inequality on the binomial counts). Reusing one bank across $n$ records costs a factor $\ln n$ and nothing more.

(b) Gap to the fixed game. $\mathrm{Adv}^*(G^{\mathrm{rs}}_j)\le\mathbb E_S\,\mathrm{Adv}^*(G^{\mathrm{fix}}_{S,j})$ (proven, joint convexity of total variation). The gap can be maximal. The learning function that outputs the parity of $|D|$ has $\mathrm{Adv}^*(G^{\mathrm{rs}}_j)=0$ and $\mathrm{Adv}^*(G^{\mathrm{fix}}_{S,j})=1$ for every $S$ once $n\ge 2$ (proven, sketch: the parity of a binomial with at least one trial at rate $1/2$ is uniform). A shared bank thus bounds the average fixed-game leakage from below and certifies nothing about the fixed-game leakage that differential privacy bounds.

(c) Shadow adversary. In the average-case game, where the honest dataset is drawn from a data distribution and the adversary holds a sampler, an L-oblivious adversary that builds one offline bank of $q_T$ shadow models and attacks a black-box label view at Eval budget $q_E$ reaches the average-case black-box optimum within $O\big(\sqrt{(C^{q_E}\ln|U|+\ln(n/\alpha))/q_T}\big)$ for all $n$ targets at once (heuristic, expected from part (a) and thm-black-box-certifiability; the builder must check the class count when the test depends on the target record).

(d) Open. The least number of Train calls of a design that yields coupled certificates (thm-coupling-certificate part b) for $G^{\mathrm{fix}}_{S,j}$ for all $n$ records at once. Exact leave-one-out costs $n+1$ calls per seed. Conjecture: $\Omega(n)$ per seed for designs sound for every learning function, and $o(n)$ under a Poisson-subsampled realization. Both open.

Why it meets the bar. (1) The bank is the empirical oracle, and every quantity is a frequency over its entries. (2) Without it, the estimand needs the law of a model trained on random halves. (3) The rates depend on the learning function only through $C$, $|U|$ and $q_E$. (4) Under $\Pi_\top$, one Train call on the honest dataset with the honest seed gives the coupled advantage of the fixed game (ch-reference-advantage-one), which part (b) shows can be one where the bank's estimand is zero, so the bank's ceiling fails. For an L-aware adversary under the bottom policy the rate term of part (c) vanishes, and part (c) is vacuous.

Why it is not a textbook fact. The design is the one of Carlini et al. (IEEE S&P 2022, cited in the report from memory). I know of no statement that separates what it estimates from the fixed-dataset leakage it is used to report. I ran no search, so this is open.

### thm-dataflow-composition

Question. How do per-node, oracle-measured quantities compose through a dataflow graph of several learning nodes with ciphertext, sum and noise channels, against an adversary that adapts across rounds?

Procedure. A dataflow graph of $R$ rounds. In round $t$ each client $i\in[N]$ computes $m_{t,i}=\mathsf L(m_t,D_i,\mathcal H;\rho_{t,i})$. A general node computes $s_t=\sum_i w_i(m_{t,i}-m_t)$ under threshold encryption. A decryption node releases $y_t=s_t+Z_t$ with smudging noise $Z_t\sim\mathcal N(0,\sigma^2 I)$, and $m_{t+1}=g(m_t,y_t)$ for a public map $g$. Ciphertexts reach the coalition through the Enc channel and $y_t$ through the plain channel. The builder should extend to any graph with channels among plain, sum, Enc, noise and none where the proof allows.

Adversary. A coalition $A$ that contains the server and some clients, with $j\notin A$, interactive per ch-execution-schedule, under $\Pi_G(A)$. It is passive at model arguments when each honest learning node's starting model is the protocol's function of the released values. It is active when the server sets each client's starting model in each round, adaptively, which is the choice ARES, LOKI and Pasquini et al. make in the interface report.

Goal. Distinguish $H_0$ and $H_1$, which differ in one record of $D_j$, written $D_j^0$ and $D_j^1$.

Oracle-defined quantity. The coupled sensitivity tail of client $j$ at starting model $m$,

$$\beta(m,\Delta)=\Pr_\rho\Big[w_j\,\big\|\mathsf L(m,D_j^0,\mathcal H;\rho)-\mathsf L(m,D_j^1,\mathcal H;\rho)\big\|>\Delta\Big].$$

Expected statement, in four parts.

(a) Channel reduction. $\mathrm{Adv}_G(A)\le\sum_{t=1}^R\mathrm{Adv}^{\mathrm{cpa\text{-}d}}(B_t)+\mathrm{Adv}_{G_{\mathrm{rel}}}(A)$, where $G_{\mathrm{rel}}$ replaces every Enc channel by none and keeps the released values. For CKKS the notion is IND-CPA-D, since IND-CPA does not survive released decryptions (Li and Micciancio, EUROCRYPT 2021, from memory, not read). The reductions $B_t$ run honest nodes through the oracle, so the assumption must hold relative to $\mathcal O$. That holds when $\mathsf L$ is efficiently computable and $\mathcal O$ does not depend on the key, since $B_t$ can then simulate $\mathcal O$ (heuristic, to be proven). This is the one place where unit cost must not enter a running-time argument.

(b) Passive composition. For every $\varepsilon\ge 0$ and $\Delta>0$,

$$\mathrm H_{e^\varepsilon}(P_0\|P_1)\le\delta_{\mathcal N,R}(\varepsilon;\Delta/\sigma)+\sum_{t=1}^R\mathbb E\big[\beta(m_t,\Delta)\big],$$

where $\delta_{\mathcal N,R}$ is the $R$-fold adaptive composition of the Gaussian mechanism and the expectation is over the honest law of $m_t$ (heuristic). The step per round is thm-coupling-certificate part (b) conditioned on the history, which fixes $m_t$ under passivity, while the other clients' contributions have the same law under both hypotheses. The builder must prove that tails that depend on the history enter through their expectation, and must settle under which hypothesis that expectation is taken, or bound it by the larger of the two. Each term on the right is then certifiable by coupled whole-run executions (expected, from thm-coupling-certificate part b).

(c) Active separation. For every $\eta>0$ some learning function has $\mathbb E[\beta(m_t,\Delta)]=0$ for all $t$ under the honest law, while an active server wins with advantage at least $1-\eta$ in one round (proven, sketch: $\mathsf L$ writes $D$ into the model at a scale far above $\sigma$ when $m$ lies in a set the honest dynamics never reach, and ignores $D$ elsewhere). No certifier with finitely many Train calls bounds $\sup_m\beta(m,\Delta)$ from above uniformly over learning functions (proven, sketch: the same construction placed at a starting model the certifier never queries). Clipping bounds the supremum by construction and recovers the accounting of DP-SGD, where the oracle has no role. The oracle therefore certifies passive adversaries, and active ones only under structure in $m$, which is open.

(d) Open. The sum channel. In the coupled execution the other clients share their seeds across the two hypotheses, so their randomness cancels, and the bound of part (b) is the same for one client or a thousand. Whether a certifiable quantity can credit the other clients' contributions as noise is open.

Why it meets the bar. (1) $\beta$ is defined by coupled Train calls. (2) Without the oracle, unclipped training has no known sensitivity and the bound needs the law of the trained model at every round. (3) The bound holds for every learning function and uses it only through $\beta$. (4) Under $\Pi_\top$ the coalition opens the seed of the smudging node, removes $Z_t$, and the bound of part (b) fails.

Why it is not a textbook fact. Adaptive composition of Gaussian mechanisms is textbook. Replacing a worst-case sensitivity by a coupled, oracle-measured tail, averaged over the honest trajectory, is not, and part (c) marks where that replacement stops. The CKKS layer needs IND-CPA-D and an assumption relative to the oracle, which no composition theorem of the differential privacy literature carries. Individual privacy accounting (Feldman and Zrnic, NeurIPS 2021, from memory, not read) uses realized per-record norms under clipping, and the builder must check it.

### thm-replay-audit-steer

Question. A deviating party trains a model and must convince an auditor that it ran the learning function on a committed dataset. How far can it steer the model and still pass, when hardware nondeterminism forces the auditor to accept any model within a tolerance? The statement covers HE-OFT's remedy of a checker that recomputes for a deviating server (interface report, deviating server) and proof-of-learning (Jia et al., IEEE S&P 2021, from memory, not read).

Procedure. Public $m_0$ and $\mathcal H$, and a binding commitment $c$ to $D$. The prover picks a nonce $\eta$, and the seed is $\rho=R(c,\eta)$ for a random oracle $R$ with output law $\mu$. A Train call with explicit seed $\rho$ returns $\mathsf L(m_0,D,\mathcal H;\rho,\xi)$, with hardware randomness $\xi$ fresh per call (ch-bank-fidelity-reuse). The prover outputs $(m,\eta)$. The auditor may open $D$, makes $r$ Train calls at $\rho$ with outputs $m_1,\dots,m_r$, and accepts when $\min_{i\le r}d(m,m_i)\le\tau$ for a metric $d$ on the model space.

Goal. Steer. The prover wins when $m\in T$ for a target set $T$ and the auditor accepts. The auditor plays the defender's discriminator of the interface report.

Oracle-defined quantities. The reach $p_\tau(T)=\Pr_{\rho,\xi}[d(\mathsf L(m_0,D,\mathcal H;\rho,\xi),T)\le\tau]$ and the spread $s_\tau=\Pr_{\rho,\xi,\xi'}[d(\mathsf L(m_0,D,\mathcal H;\rho,\xi),\mathsf L(m_0,D,\mathcal H;\rho,\xi'))>\tau]$. Both are Bernoulli parameters, certifiable as in thm-coupling-certificate part (b).

Expected statement, in four parts.

(a) Soundness. Every prover, unbounded and L-aware, that makes $q_R$ queries to $R$ wins with probability at most $(q_R+1)\,r\,p_\tau(T)$ plus the probability of guessing an unqueried output of $R$ (proven, sketch: the final seed is one of at most $q_R$ queried seeds or a fresh one, each distributed per $\mu$, the auditor's $\xi$ is independent of $m$, and acceptance with $m\in T$ forces some replay within $\tau$ of $T$, so a union bound over replays and candidates applies).

(b) Completeness. An honest prover passes with probability at least $1-s_\tau$ (proven).

(c) Attack. A grinding prover with $q_T$ Train calls keeps the first seed whose run lands within $\tau/2$ of $T$ and moves to a point of $T$. It wins with probability about $(1-(1-p_{\tau/2}(T))^{q_T})(1-s_{\tau/2})$ (heuristic, the builder must handle the dependence between reach and spread at the same seed). Parts (a) and (c) together give the order of the steering probability up to the change from $\tau$ to $\tau/2$ and from $q_R$ to $q_T$.

(d) Open. A bound in $q_T$ in place of $q_R$ for L-oblivious provers, which needs a random family of learning functions per ch-budget-semantics. With exact consistency the tolerance can be zero and the reach becomes $\Pr[\mathsf L\in T]$, so deterministic kernels are a security parameter. Steering through the data, choosing $D$ before the commitment, lies outside this theorem, and that is where poisoning lives.

Why it meets the bar. (1) Reach and spread are defined by Train calls with explicit seeds. (2) Without the oracle the reach is a property of the law of trained models near $T$, unknown for transformers. (3) The bound holds for every learning function and uses it only through reach and spread. (4) If the policy lets the prover pass any explicit seed, the top oracle for the prover, it wins with probability $\sup_\rho\Pr_\xi[\cdot]$, which can be one while $p_\tau(T)$ is tiny, so part (a) fails.

Why it is not a textbook fact. Part (a) is the grinding argument of the Fiat and Shamir transform. The content lies elsewhere. The security of a training audit reduces to two oracle-measurable probabilities and two counts. The tolerance that hardware forces ties completeness to soundness through $\tau$. The resulting bound is certifiable. Of the five problems this one is the weakest against the bar, and part (d) is what would make it strong.

## Verdicts

Each starting item is judged on one line. def-learning-oracle needs ch-handle-laundering, ch-seed-naming and ch-locality-ill-posed fixed. def-learning-oracle-model needs ch-budget-semantics fixed. def-model-bank is well posed, and two claims around it are false or too broad (ch-bank-fidelity-reuse, ch-bank-design-game). thm-perfect-substitution is false as stated (ch-substitution-policy, ch-handle-laundering) and true for the realizable policy. thm-reference-access is ill-posed in part (a) (ch-seed-naming) and needs its advantage and rate corrected. thm-own-data-only is rejected because, once ch-budget-semantics and ch-handle-laundering are fixed, it is either false (L-oblivious adversary) or the definition of the bottom oracle, which thm-perfect-substitution already states. The new problems receive no verdict, since nothing about them is proven yet.

```text
VERDICT def-learning-oracle REVISE
VERDICT def-learning-oracle-model REVISE
VERDICT def-model-bank REVISE
VERDICT thm-perfect-substitution REVISE
VERDICT thm-reference-access REVISE
VERDICT thm-own-data-only REJECT
BLOCKING 5
```
