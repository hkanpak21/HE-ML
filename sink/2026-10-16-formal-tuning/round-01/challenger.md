# Round 01, challenger

Verdict of this turn. All five blocking challenges of round 00 are fixed by the new definitions, and the fourteen non-blocking ones are fixed or reduced to a residue listed below. One new challenge is blocking. ch-query-universe makes part (o) of [thm-black-box-certifiability] false as stated, and one clause fixes it. The other six proofs are correct as stated. I checked them step by step and found no gap in a statement, only errors in the paragraphs that argue non-triviality and one overclaim. No theorem earns NONTRIVIAL this round. [thm-coupling-certificate] meets parts 1 to 3 of the bar. Its part-4 argument treats the drawn-seed discipline as the bottom oracle, and [def-degenerate-oracles] contradicts that, so I re-open ch-degenerate-oracles-undefined. [thm-black-box-certifiability] should earn the tag once ch-query-universe is fixed. Steering sharpens the two open problems, gives a proof sketch for each, and answers the builder's three questions.

Every non-trivial claim below carries one of the labels proven, heuristic, empirical or open. "Proven, sketch" means that the idea of the proof is written here and the builder must write it out in full. Notation follows `theory/CURRENT.md` and round-01/builder.md.

## Status of the round-00 challenges

| Challenge | Was | Now | Residue |
| --- | --- | --- | --- |
| ch-handle-laundering | blocking | fixed | none. Access rules 1 and 2 refuse every Train or Open on a name with label eval, and step 1 of [thm-perfect-substitution] proves the induction |
| ch-substitution-policy | blocking | fixed | none. [thm-perfect-substitution] is stated for the realizable policy, and the granularity rule handles the downward counterexample |
| ch-seed-naming | blocking | fixed | none. A drawn seed is stored under a name, and Train accepts a seed name |
| ch-budget-semantics | blocking | fixed | two residues, both new challenges below, ch-upper-bound-pattern and ch-computational-adversary |
| ch-locality-ill-posed | blocking | fixed | none. Locality is deleted |
| ch-seed-domain | not blocking | fixed | none |
| ch-redundant-properties | not blocking | fixed | none |
| ch-access-policy-simplify | not blocking | fixed | label none is now redundant, see ch-definition-cuts |
| ch-handle-opacity | not blocking | fixed | none |
| ch-reference-advantage-one | not blocking | fixed | none |
| ch-plugin-test-rate | not blocking | fixed | none |
| ch-execution-schedule | not blocking | fixed | none |
| ch-learning-function-choice | not blocking | fixed | none |
| ch-eval-budget-vs-allowance | not blocking | fixed | the sentence "on a served model $q_E\le Q$" repeats the allowance, see ch-definition-cuts |
| ch-bank-fidelity-reuse | not blocking | fixed | the seed-name match of the bank cannot fire in a fixed design, see ch-definition-cuts |
| ch-bank-design-game | not blocking | fixed | none |
| ch-experimenter-equality-test | not blocking | fixed | none |
| ch-loo-models-simplify | not blocking | fixed | none |
| ch-degenerate-oracles-undefined | not blocking | re-opened | both oracles have exact forms, and the proofs use a different bottom from the one defined. See New challenges |

## Definitions

### [def-learning-oracle]

Well posed (proven by inspection). The three calls, fidelity and the access rules determine the law of every transcript given the caller's strategy. Five remarks, none blocking.

1. The label none does nothing. Names are per caller, so a caller without access to an object holds no name for it. The proofs never use the label except to say that the adversary cannot use the honest seed, which follows from its having no name for it. Cut the label (ch-definition-cuts).
2. Rule 3 says that names reach a caller "from the procedure or from a policy", but the oracle has no operation that places a name in a caller's table. The interface then has a fourth operation that the definition does not list. The smallest fix is one sentence. The oracle grants a name to a caller when the procedure or a policy directs it, with a stated label, and this is not a call of that caller. Rule 3 then moves to [def-learning-oracle-model], where the procedure lives.
3. Eval on a seed name is undefined. Restrict Eval to model names.
4. Fidelity takes the hardware randomness of distinct calls to be independent. For GPU nondeterminism that is a modelling assumption (heuristic, assuming that the scheduling of floating-point reductions in one run carries no information about another). One sentence should say so, because [thm-replay-audit-steer] depends on it.
5. The atomless law $\mu$ excludes the finite seed spaces of real training code. The theorems use it only to realize arbitrary laws from the seed. The random-table construction under [thm-reference-access] below works on a $k$-bit seed space with an error term $q2^{-k}$ (proven, sketch). The atomless hypothesis can therefore stay as an idealization whose cost is a term of that order. Whether every impossibility of round 01 survives on $k$-bit seeds with such a term is open.

### [def-learning-oracle-model]

Well posed for the theorems of round 01, which are about one learning node. Four points need a change before the next problems.

1. ch-computational-adversary. The adversary has no computational bound, and the definition releases a ciphertext "through the plain channel". An unbounded adversary decrypts it, so in this model every procedure with ciphertexts released to the coalition is a plaintext procedure. That is harmless now and fatal for [thm-dataflow-composition] part (a).
2. ch-upper-bound-pattern. Quantifier pattern 1 says an upper bound for every adversary is free of the budget. [thm-black-box-certifiability] (o) is an upper bound for every adversary that depends on $q_E$. The two are consistent once pattern 1 reads "free of $q_T$". The Eval budget on a served model is capped by the procedure's allowance, so it may enter an upper bound.
3. Charging. The definition does not say whether the Train call that a semi-honest owner in $A$ makes for its own node counts against $q_T$. If it counts, a coalition with $q_T=0$ cannot run its own nodes. Say that calls the procedure requires are not charged.
4. Goals. Invert and steer are defined by reference to the interface report. The final document must stand alone, and [thm-replay-audit-steer] needs steer. Define each goal in one sentence, or keep only distinguish until a theorem uses another goal.

### [def-degenerate-oracles]

The two oracles now have exact forms. The proofs use them inconsistently, and that is the re-opened ch-degenerate-oracles-undefined below. Item 3, the experimenter, is not a degenerate oracle. It is a caller outside any procedure, and rule 2 already gives it label open on every name it receives. Move it to [def-certifier] (ch-definition-cuts).

### [def-certifier]

Well posed. Two clarifications. First, $N$ counts all Train calls, while [thm-coupling-certificate] (a) uses $N$ calls at each input. Use one convention. Second, say that the certifier is an oracle algorithm that reaches $\mathsf L$ only through $\mathcal O$. Soundness over a class is otherwise met by a certifier that hard-wires $\mathsf L$ whenever the class is a singleton.

### [def-model-bank]

Well posed, and two parts can go (ch-definition-cuts). The asynchronous design that queues unmatched calls as training jobs is the learning oracle itself and adds nothing. The match "$\rho_i=s$ with $s$ the name of a seed" never fires in a fixed design when $s$ names a drawn seed, since a fixed entry equals a draw from the atomless $\mu$ with probability zero. A coupled design then needs entries whose seed is tied to another entry's drawn seed, and the definition has no such entries. The smallest fix deletes the seed-name match. A coupled design draws its seeds before the bank is built and lists them as fixed values, which [lem-bank-fidelity] already covers.

## Proofs

### Atomless two-point lemma [lem-atomless-two-point]

Checked. Steps 1 to 5 and part (d) are correct (proven). I verified the identity for the ratio of binomial coefficients, the inequality $\bar u\ge u$ on the event of distinct cells, and the union bound $u(E^c)\le\binom{2N}{2}\max p$. The probability space is the certifier's coins and the oracle's draws under one fixed $\mathsf L$. The quantifiers read: for every certifier and every $\mathsf L$ in a class closed under changes at $x_0$ and $x_1$. Part (c) is stronger than the round-00 sketch, because it needs only atomless $P_0$ and $P_1$, which may differ.

Counterexamples tried, none succeeds.

- A certifier that trains at a third input with a model obtained at $x_0$ as its starting model. The map $\Phi$ covers it, because $\mathsf L_S$ equals $\mathsf L$ at every other input.
- A certifier that opens the models and sees more than the view. Step 3 conditions on the model inside each cell, so seeing the model does not help.
- The case $2N>M$. Then $N(2N-1)\eta\ge 1$ and the bound is vacuous, which is consistent.

Weakest step. Step 2. The variable $W$ must also hold the evaluation randomness $\sigma$ of the certifier's Eval calls, or $\Phi$ is not a map of $(Y_0,Y_1,W)$. One clause fixes it.

Paragraphs. Two sentences are false.

- "Without the oracle" says that "a training service that draws its own randomness, or the bottom oracle, supplies independent draws and nothing else". The bottom oracle is the realizable policy, and under it a caller passes its own seed names to Train (rule 2 and the Train call). It samples the identity coupling of [thm-coupling-certificate] (proven, from the definitions). Only the training service supplies independent draws alone.
- "Degenerate oracles" says that a learning function that ignores its dataset has $\beta=0$. That holds only if it also ignores $\xi$. With atomless hardware randomness that affects the output, $\beta=1$.

Prior work. I read only the abstract of arXiv 1806.06427 (Gilbert and McMillan). It describes lower bounds on the query complexity of verifying pure differential privacy, which it calls infeasible at common parameters. The builder's sentence that pure differential privacy "cannot be verified with finitely many samples (their Theorem 10)" needs the theorem quoted before it enters the final document.

Non-triviality. A two-point lemma of property testing, which the builder does not propose as non-trivial. ACCEPT.

### Coupling certificate [thm-coupling-certificate]

Checked. Parts (a)(i), (a)(ii), (a)(iii), (b) steps 1 to 6, the Gaussian case, (c)(i) and (c)(ii) are correct as stated (proven). Specific checks follow.

- (a)(ii). The bounded difference of $\|\hat p-p\|_1$ is $2/N$, so McDiarmid's inequality gives $e^{-Nt^2/2}$, as written.
- (b) step 3. The disintegration of the densities is correct. The almost-sure sets depend on the set $B$ of the $\pi$-system, and countably many null sets have a null union.
- (b) step 4. The equality under deterministic kernels holds, because the inner mixture over $\xi$ is then trivial.
- Gaussian case. The kernel $y\mapsto(s/s')y+\sqrt{1-s^2/s'^2}\,Z$ maps $\mathcal N(s',1)$ to $\mathcal N(s,1)$ and fixes $\mathcal N(0,1)$, so $\delta_{\mathcal N}$ is nondecreasing. The closed form agrees with the analytic Gaussian mechanism of Balle and Wang (ICML 2018) as I recall it. I did not reopen that paper.
- (c)(ii). The glued map preserves $\mu$, and it agrees with the coupling inequality.

The probability space of $\Gamma$ is one drawn seed and two independent hardware draws. The calls $\mathsf{Train}(x_0,\bot)$ and then $\mathsf{Train}(x_1,h)$ produce exactly this law.

Weakest step. Step 5 says that $\mathrm{TV}(P_0,P_1)$ is "the best advantage of the bottom oracle, at every budget". This is true as a supremum over adversaries for one fixed $\mathsf L$, attained with no Train call by an adversary that hard-wires the Neyman and Pearson set of that $\mathsf L$. An adversary uniform over learning functions does not attain it, by [thm-reference-access] (c). One clause should say which reading is meant.

Paragraphs. Two corrections.

- "Without the oracle" says that "no certificate on the leakage of an atomless release exists, whatever the number of training runs". Part (a)(iii) covers deterministic channels only, and the lemma's remark leaves randomized channels open. The sentence is false for the Gaussian channel with bounded $f$. If $\|f\|\le B$, then $\mathrm H_{e^\varepsilon}(P_0\|P_1)\le\delta_{\mathcal N}(\varepsilon;2B/\sigma)$ with no call at all (proven, by joint convexity and the monotonicity above). Restrict the sentence to deterministic channels.
- "Degenerate oracles" calls drawn seeds "what the bottom oracle supplies". That is false by the first correction under [lem-atomless-two-point].

Non-triviality. Criterion 1 holds, since $\beta_\gamma(K)$ is defined by coupled Train calls. Criterion 2 holds, since a certificate otherwise needs the law of the trained model. Criterion 3 holds, since (b) is uniform over learning functions and uses them only through $\beta_\gamma(K)$. Criterion 4, as argued, does not hold. The bound of (b) holds under the seed-revealing top with equality under deterministic kernels, so it neither fails nor becomes vacuous there. Under the realizable bottom the caller samples $\Gamma$ itself. The only degenerate case in which the theorem fails is an experimenter restricted to drawn seeds, (a)(iii), and [def-degenerate-oracles] does not name that case. My ruling: the tag is granted in round 02 once [def-degenerate-oracles] names the drawn-seed discipline as the degenerate case for experimenters, and the two paragraphs are corrected. The orchestrator may overrule this reading of criterion 4. ACCEPT.

### Perfect substitution [thm-perfect-substitution]

Checked. Correct (proven). The simulator depends on $\mathcal A$ alone. It samples $\mathsf L$, so it is an $\mathsf L$-sampling adversary, which is all the statement claims.

Weakest step. Step 3 ends with "the adversary stops with probability one". That is a hypothesis on adversaries and belongs in [def-learning-oracle-model]. With it, the finite-dimensional laws determine the law of the transcript.

Scope. The theorem identifies the bottom oracle with the real procedure against an adversary that samples $\mathsf L$. It does not identify it with an adversary that knows $\mathsf L$. For upper bounds this changes nothing, because they are statements about laws and hold for an adversary that knows $\mathsf L$ by data processing (proven). [def-degenerate-oracles] should state this in one sentence, because the proofs use both readings (ch-degenerate-oracles-undefined).

The "Without the oracle" and "Degenerate oracles" paragraphs are correct. ACCEPT, not proposed as non-trivial, and I agree.

### Reference access [thm-reference-access]

Checked. (a) is correct (proven), and its optimality is step 5 of [thm-coupling-certificate]. (b) is correct (proven). The step $\sup_B|d(B)-\hat d(B)|\le\frac12\|p_1-\hat p_1\|_1+\frac12\|p_0-\hat p_0\|_1$ uses that a signed measure of total mass zero has $\sup_B|\nu(B)|=\frac12\|\nu\|_1$. (c) is correct under (i) and under (ii) (proven). Under (i) the adversary may pass a seed name from a call at $x_0$ to a call at a third input. That is harmless, because the chosen $\mathsf L$ is constant at every other input.

Weakest step. The heuristic part of (c), adversaries that pass their own explicit seeds at $x_0$ or $x_1$ under deterministic kernels.

Answer to the builder's question 2. Write it. The realizable policy permits explicit seeds, and an adversary that forms coupled shadow pairs is its most natural member, so (c) without it misses the case that matters. A permutation of an atomless seed space is awkward. A random table is simpler (proven, sketch).

Identify $(\mathcal R,\mu)$ with $[0,1)$ under Lebesgue measure, and let $\pi_k(\rho)=\lfloor 2^k\rho\rfloor$. Draw independent uniform variables $U_{b,i}$ on $[0,1)$ for $b\in\{0,1\}$ and $0\le i<2^k$, and set

$$\mathsf L_U(x_b;\rho)=g_b\big(U_{b,\pi_k(\rho)}\big),$$

constant at every other input, where $g_b$ realizes a law $Q'_b$ from one uniform variable. Take $g_0=g_1$ realizing $Q$ for the reference function, and $g_b=g^S_b$ as in step 1 of [lem-atomless-two-point] for the separated one. Every member of the family has deterministic kernels. The separated members have $\mathrm{TV}(P_0,P_1)=1$, because their views at $x_0$ lie in $A_S$ and at $x_1$ in $A_S^c$. Under a random member, the honest model at $x_b$ is $g_b(U_{b,J})$ with $J=\pi_k(\rho^*)$ uniform. The index $J$ is independent of everything the adversary sees, since the table entries are independent of their indices. An answer at $x_c$ under a seed with a new prefix is a fresh draw from $Q'_c$, and a repeated prefix returns a value the adversary already holds. So until the adversary passes a seed whose prefix equals $J$ at the honest input, an event of probability at most $q2^{-k}$, the transcript is a fixed map of $q+1$ independent draws per input and of independent randomness. Steps 3 and 4 of the lemma then give

$$\mathbb E_{S,U}\,\mathrm{Adv}(\mathcal A,\mathsf L_{S,U})\le\frac{2(q+1)(2q+1)}{M}+\frac{2q}{2^k},$$

and some member attains at most this value. This covers every adversary under the realizable policy, explicit seeds included, and it works on a $k$-bit seed space.

Non-triviality. (a) is a coupling identity, (b) is data processing with the plug-in rate, and (c) is the two-point lemma. ACCEPT, without the tag.

### Own data only [thm-own-data-only]

The withdrawal is accepted. Its correct content is in [thm-perfect-substitution] and [thm-reference-access] (b) and (c). The verdict REJECT stands, so that the slug cannot enter the final document.

### Bank fidelity [lem-bank-fidelity]

Checked. Correct (proven). The entry chosen for a call is a function of the transcript, and an unused entry is independent of it, because the entries are independent. The chain rule then couples the two executions until the first refusal.

Weakest step. The independence of the stored hardware randomness $\xi_i$ across runs. It is the same assumption as remark 4 under [def-learning-oracle] (heuristic for real hardware).

A call with a seed name of a drawn seed is refused almost surely by a fixed design (see [def-model-bank]). The bound in the lemma counts that refusal, so the lemma stays true, and such a design is useless for coupled pairs. ACCEPT, not proposed as non-trivial.

### Black-box certifiability [thm-black-box-certifiability]

Part (o) is false as stated (proven, counterexample). The trees in $\mathcal T_q$ query $U$, and nothing restricts the adversary's Eval calls to $U$. Let $\mathcal U=U\cup\{u^*\}$, let $\mathsf{ev}(m,u)=0$ for every $u\in U$, and let $\mathsf{ev}(m,u^*)$ be a bit that differs between $\mathsf L(x_0;\rho)$ and $\mathsf L(x_1;\rho)$ for every $\rho$. Then $\mathrm{Adv}^{\mathrm{bb}}(q)=0$, and one query at $u^*$ wins with advantage one. This is ch-query-universe, and it is blocking. The smallest fix is to add to the setting the clause "every Eval call on the served name queries a point of $U$", or to set $U=\mathcal U$ finite.

The rest is correct (proven).

- (a). Hoeffding's inequality per tree and input, a union bound over $\mathcal T_q$, and the count $\ln|\mathcal T_q|\le C^q(\ln|U|+\ln 2)$, all checked.
- (b). The variance proxy $1/(2N)$ of a difference of two independent means, and the maximal inequality $\sqrt{2v\ln(2K)}$, checked. The advantage is $\mathbb E[A(\hat\tau)]$, because the shadow models are independent of the served one.
- (c). [lem-atomless-two-point] (d) with $F(m)=(\mathsf{ev}(m,u))_{u\in U}$ applies. The modified functions keep the law of $F$ at both inputs, so $\mathrm{Adv}^{\mathrm{bb}}(Q)$ does not change and the collapse claim is false for them.
- (d). [thm-coupling-certificate] (b) with the channels $F$ and the identity.

Weakest step. Part (o), above. With the fix, the proof of (o) holds for adversaries that know $\mathsf L$ as well, since $\omega$ may contain anything independent of the hypothesis and of the served model.

Scope. Two limits should be stated in one sentence each. First, the certificate of (a) costs $C^{q_E}$ runs, so it serves small $q_E$ only, and whether that cost is necessary is the builder's open lower bound. Second, the collapse certificate of (d) needs a small $\beta$. For learning functions of the stochastic gradient type, $\beta$ is at least the probability that record $j$ enters some batch, since an update that uses the record changes the parameters almost surely (heuristic). The certificate of (d) is then vacuous. With (c), this means that in this model a claim that $Q$ labels reach what the head reveals can be refuted and, for realistic learners, never certified (heuristic, through the second limit).

Paragraphs. The top counterexample is correct. I checked that the first binary digit of $\rho+1/2\bmod 1$ is the flipped digit of $\rho$. "Under the bottom oracle held by an adversary that knows $\mathsf L$" mixes two objects, see ch-degenerate-oracles-undefined.

Non-triviality. Criteria 1 to 3 hold. Criterion 4 holds, because (o) fails under the seed-revealing top by the paragraph's counterexample. Parts (o) and (a) together certify the label-only leakage of an arbitrary trained model at budget $q_E$ from above, uniformly over learning functions and against adversaries that know $\mathsf L$. Part (c) separates black-box from white-box certification. I expect ACCEPT NONTRIVIAL once the clause is added. REVISE this round.

### Bank soundness [thm-bank-soundness]

Checked. (a) and (b) are correct (proven). In (a), Hoeffding's inequality is applied given the membership pattern of $j$, with a random $k_{\min}$. That is correct, because the union bound over $j$ and $\tau$ holds for every pattern. In (b), the parity of a binomial count with at least one trial at rate one half is uniform.

Weakest step. (a) needs $\mathcal T$ fixed before the bank is built. The setting says so, and a report that selects tests on the bank and then reads their estimates off the same bank voids (a). A one-sentence warning belongs in the final document.

Paragraphs. "Degenerate oracles" uses the parity example to show that the bank misses a seed-revealing adversary. In that example the learning function is deterministic and $\mathrm{TV}=1$ in the fixed game, so the bottom oracle already wins with advantage one. The example shows the gap between games and says nothing about the top.

Non-triviality. (a) is Hoeffding's inequality on a design, and (b) is an averaging identity with a counterexample. ACCEPT, without the tag. Part (b) is the useful content for the literature study, since the random-half design is the one membership-attack evaluations use.

## New challenges

### ch-query-universe

BLOCKING. Targets [thm-black-box-certifiability] (o), and (b) through it. The counterexample is under Proofs. Smallest fix: restrict the Eval calls on the served name to $U$, or set $U=\mathcal U$ finite.

### ch-degenerate-oracles-undefined (re-opened)

Not blocking. Targets [def-degenerate-oracles], and the "Without the oracle" and "Degenerate oracles" paragraphs of [lem-atomless-two-point], [thm-coupling-certificate], [thm-black-box-certifiability] and [thm-bank-soundness].

The proofs use three different objects as "the bottom".

1. The defined one is the realizable policy with no bound on $q_T$, held by an adversary that reaches $\mathsf L$ only through the oracle.
2. Some paragraphs use an adversary that knows $\mathsf L$. For one fixed $\mathsf L$ its best success equals that of the first object, since an oracle algorithm may hard-wire $\mathsf L$ (proven). For statements uniform over learning functions the two differ, by [thm-reference-access] (c).
3. Other paragraphs use the drawn-seed discipline. It is strictly weaker than the first object for certification, by [lem-atomless-two-point] (c) against [thm-coupling-certificate] (b) (proven).

Smallest fix, three sentences in [def-degenerate-oracles]. (i) For a fixed learning function, the best success under the bottom oracle equals the best success of an adversary that knows $\mathsf L$. (ii) For an experimenter, the degenerate case is the drawn-seed discipline of [def-certifier], which is what a party receives from a training service that draws and hides its own randomness. (iii) The seed-revealing policy coincides with the README's top, which names honest data with the honest seed, whenever the hypotheses fix every honest dataset. Otherwise it is weaker, and a theorem whose honest data are drawn names the policy it uses. Then correct the paragraphs listed above.

Answer to the builder's question 1. Yes, the seed-revealing policy is acceptable as the top, under sentence (iii). The three arguments of the builder are sound for games in which the hypotheses fix all honest data, which is the setting of differential privacy. In an average-case game, such as the game of [thm-bank-soundness] (c), naming other honest datasets is more than knowing their seeds, and the difference matters for the sum channel of [thm-dataflow-composition].

### ch-computational-adversary

Not blocking now, blocking for [thm-dataflow-composition] (a). Targets [def-learning-oracle-model]. An unbounded adversary decrypts every ciphertext it receives, so a procedure that releases threshold-CKKS ciphertexts to the coalition is modelled as a plaintext release (proven, for parameters at which a ciphertext and the public key determine the plaintext). Smallest fix, one sentence. The adversary is unbounded, except in a statement that uses a computational assumption, where it runs in polynomial time with unit cost per oracle call. A reduction in such a statement must implement $\mathcal O$ itself, so it needs $\mathsf L$ computable in polynomial time.

### ch-upper-bound-pattern

Not blocking. Targets [def-learning-oracle-model], quantifier pattern 1. Replace "free of the budget" by "free of $q_T$". The same edit should say that Train calls required by the procedure are not charged.

### ch-identity-coupling-scope

Not blocking. Targets the scope sentence of [thm-coupling-certificate]. Under deterministic kernels the certificate of (b) equals the seed-revealing adversary's best advantage (proven, (b)). It therefore never credits randomness that the training seed controls. Two consequences decide which of Halil's procedures it can serve, and the theory should state both.

- Noise drawn outside the learning function is credited. Smudging noise added at threshold decryption is a general node, and the Gaussian case of (b) counts it.
- Noise drawn inside the learning function from its seed is not credited. Noisy gradient descent that draws its noise from $\rho$ has $\beta_{e^\varepsilon}$ near one on the plain channel, because the shared seed cancels the noise and the gradients differ (heuristic, for any run in which record $j$ is sampled). Crediting it needs a seed map $\phi$ of (c)(ii), and finding $\phi$ from oracle calls is the builder's open question.

### ch-paragraph-corrections

Not blocking. The smallest fixes, each quoted under Proofs.

1. [lem-atomless-two-point] step 2. Add the evaluation randomness to $W$.
2. [lem-atomless-two-point] "Degenerate oracles". Write "ignores its dataset and $\xi$".
3. [thm-coupling-certificate] "Without the oracle". Write "of a release through a deterministic channel".
4. [thm-coupling-certificate] step 5. Say "a supremum over adversaries for a fixed learning function".
5. [thm-bank-soundness] "Degenerate oracles". Replace the parity example, or drop the claim about the top.

### ch-definition-cuts

Not blocking. Cuts that lose no theorem.

1. Delete the label none (see [def-learning-oracle], remark 1).
2. Move access rule 3 to [def-learning-oracle-model], and name the grant operation in one sentence.
3. Move the experimenter from [def-degenerate-oracles] to [def-certifier].
4. Delete the asynchronous design and the seed-name match from [def-model-bank].
5. Delete "On a served model $q_E\le Q$", which the query channel already says.

## Steering

The single-node distinguishing theory is in good shape after this round. Its definitions are well posed, five of its seven proofs are correct as stated, and the remaining fixes are local. The next work should leave the single node. Both open problems do, and I sharpen both. Each comes with a proof sketch, so that round 02 can reach full proofs.

### Sharpened [thm-dataflow-composition]

Answer to the builder's question 3. Neither the expectation under $H_0$ with symmetry, nor the maximum over the two hypotheses. Take the tail along the trajectory of the first argument of the hockey-stick divergence, through a hybrid on the left. This costs no factor $e^\varepsilon$. Differential privacy for the pair needs both orders, and each order uses its own trajectory.

Setting. Rounds $t=1,\dots,R$. The honest client $j$ has dataset $D^b_j$ under $H_b$. Its starting model $m_{t,j}$ in round $t$ is any function of the coalition's view before round $t$. A passive coalition sets it by the protocol, and an active one chooses it. The release is $y_t=a_t+w_j\big(\mathsf L(x^b_t;\rho_t,\xi_t)-m_{t,j}\big)+Z_t$ with $x^b_t=(\ell,m_{t,j},D^b_j,\mathcal H)$. Here $a_t$ collects the other clients' terms, a function of the history, their own seeds and hardware randomness, and the coalition's choices. The noise $Z_t\sim\mathcal N(0,\sigma^2I)$ comes from a general node whose randomness the coalition does not hold. The coupled tail is

$$\beta(m,\Delta)=\Pr_\Gamma\Big[w_j\big\|\mathsf L(x^1(m);\rho,\xi_1)-\mathsf L(x^0(m);\rho,\xi_0)\big\|>\Delta\Big].$$

Target statement, after ch-computational-adversary has removed the ciphertexts through part (a). For every coalition strategy, every $\varepsilon\ge0$ and every $\Delta>0$,

$$\mathrm H_{e^\varepsilon}(P_0\|P_1)\le\delta_{\mathcal N}\big(\varepsilon;\sqrt R\,\Delta/\sigma\big)+\sum_{t=1}^R\mathbb E_{H_0}\big[\beta(m_{t,j},\Delta)\big],$$

where the expectation runs along the execution under $H_0$ with that strategy.

Proof sketch (proven, sketch, resting on two results of Dong, Roth and Su, JRSS-B 2022, from memory and not read). Put both executions on one probability space that shares everything, and give client $j$ in round $t$ the triple $(\rho_t,\xi^0_t,\xi^1_t)$. Let $d_t=w_j\big(\mathsf L(x^1_t;\rho_t,\xi^1_t)-\mathsf L(x^0_t;\rho_t,\xi^0_t)\big)$ and $\mathrm{clip}_\Delta(v)=v\min(1,\Delta/\|v\|)$. The hybrid $M$ releases the $H_1$ value minus $\mathrm{clip}_\Delta(d_t)$, evaluated along its own trajectory.

1. $M$ and the $H_0$ execution release the same value in every round until the first $t$ with $\|d_t\|>\Delta$. The seed and hardware randomness of round $t$ are fresh and independent of $m_{t,j}$, so $\mathrm{TV}(P_0,M)\le\sum_t\mathbb E_{H_0}[\beta(m_{t,j},\Delta)]$.
2. Given the history, the round-$t$ laws under $M$ and $H_1$ are mixtures, with one mixing law, of $\mathcal N(v-c,\sigma^2I)$ and $\mathcal N(v,\sigma^2I)$ with $\|c\|\le\Delta$. Joint convexity, step 2 of [thm-coupling-certificate] (b) for every $\gamma>0$ and in both orders, bounds each hockey-stick divergence of the pair by that of $\mathcal N(0,1)$ against $\mathcal N(\Delta/\sigma,1)$. By the duality between trade-off functions and families of hockey-stick bounds, the pair is $\Delta/\sigma$-GDP. Adaptive composition of GDP makes the whole view $\sqrt R\,\Delta/\sigma$-GDP, so $\mathrm H_{e^\varepsilon}(M\|P_1)\le\delta_{\mathcal N}(\varepsilon;\sqrt R\Delta/\sigma)$.
3. $\mathrm H_\gamma(P_0\|P_1)\le\mathrm{TV}(P_0,M)+\mathrm H_\gamma(M\|P_1)$, by splitting $P_0(B)-\gamma P_1(B)$.

What to prove in round 02.

- (a) The channel reduction to IND-CPA-D under ch-computational-adversary. Li and Micciancio is the source the builder named.
- (b) The bound above in full, and its certificate for a passive coalition. The experimenter simulates the $H_0$ execution, since it holds all honest data, and draws one coupled pair per round. The sum of $R$ indicators is certified by Hoeffding's inequality with range $R$.
- (c) For an active coalition, the same bound holds and is certifiable against one named strategy by simulating it. No certifier bounds the supremum over strategies uniformly over learning functions. That is round 00's part (c), still to be proven.

Criterion 4 is the hard part, and the builder must face it now. The bound holds under the seed-revealing top, because revealing $\rho_t$ removes nothing the coupling uses. Criterion 4 must therefore come from the experimenter's side, and there it is open. With clipped updates, $\|$update$\|\le B$, drawn seeds certify the trivial bound $\delta_{\mathcal N}(\varepsilon;2B\sqrt R/\sigma)$ with no call (proven, by the argument under [thm-coupling-certificate]). A separation therefore has to be quantitative. Open question, and the one that would make this theorem NONTRIVIAL: for updates of norm at most $B$ in dimension $d$, does some family of learning functions force every drawn-seed certifier with fewer than $e^{cd}$ runs to output no less than the trivial bound, minus $o(1)$, while the coupled tail is zero? If yes, the coupled certificate separates from drawn seeds exponentially in the dimension, which is the transformer case.

### Sharpened [thm-replay-audit-steer]

The round-00 statement simplifies, and its heuristic part (c) can now be proven. The setting is as in round 00. The prover may know $\mathsf L$ and makes $q_R$ queries to the random oracle $R$. The auditor makes $r$ replays and accepts when $\min_i d(m,m_i)\le\tau$. Here $p_\tau(T)$ is the reach and $s_\tau$ the spread. The set $T$ must be closed, so that $d(\cdot,T)$ is measurable and a nearest point exists.

(a) Soundness, $\Pr[\text{win}]\le(q_R+1)\,r\,p_\tau(T)$ (proven, sketch). The output seed is one of at most $q_R+1$ values of $R$, each with law $\mu$ and independent of the others. The term $+1$ covers a nonce the prover never queried, so no separate guessing term is needed. Let replays be defined for every candidate seed. They are independent of the prover's model, because the prover's own calls use fresh hardware randomness. A win forces $d(m_i,T)\le d(m_i,m)\le\tau$ for some replay $m_i$. A union bound over candidates and replays finishes.

(b) Completeness, at least $1-s_\tau$ (proven). The first replay alone suffices.

(c) Attack (proven, sketch). The prover runs one Train call per fresh seed, stops at the first run within $\tau/2$ of $T$, and outputs a nearest point of $T$. Write $p=p_{\tau/2}(T)$ and $s=s_{\tau/2}$. In each trial, the probability that the run lands within $\tau/2$ and the auditor's replay lands within $\tau/2$ of the run is at least $p-s$, by $\Pr[A\cap B]\ge\Pr[A]-\Pr[B^c]$. The triangle inequality makes this a win. Since the trials are independent,

$$\Pr[\text{win}]\ge\Big(1-\frac sp\Big)\big(1-(1-p)^{q_T}\big),\qquad q_T\le q_R.$$

This removes the dependence between reach and spread that round 00 left heuristic.

(d) Criterion 4. A prover that chooses its seed freely wins with probability $\sup_\rho\Pr_\xi[\cdot]$. For $\mathsf L(x;\rho)=\rho$ on $[0,1)$, $T=[0,\eta]$ and $\tau=0$, that probability is one while $p_0(T)=\eta$, so (a) fails (proven). Criteria 2 and 3 hold, because the bound uses $\mathsf L$ only through reach and spread. With (a) and (c) matched up to $\tau$ against $\tau/2$, $r$ and $q_R$ against $q_T$, I would tag this theorem NONTRIVIAL. The bound for a prover that does not know $\mathsf L$, in $q_T$ in place of $q_R$, stays open.

## Verdicts

Five definitions and eight results are judged. thm-own-data-only is withdrawn, and its REJECT stands. One challenge is blocking, ch-query-universe.

```text
VERDICT def-learning-oracle ACCEPT
VERDICT def-learning-oracle-model REVISE
VERDICT def-degenerate-oracles REVISE
VERDICT def-certifier ACCEPT
VERDICT def-model-bank ACCEPT
VERDICT lem-atomless-two-point ACCEPT
VERDICT thm-coupling-certificate ACCEPT
VERDICT thm-perfect-substitution ACCEPT
VERDICT thm-reference-access ACCEPT
VERDICT thm-own-data-only REJECT
VERDICT lem-bank-fidelity ACCEPT
VERDICT thm-black-box-certifiability REVISE
VERDICT thm-bank-soundness ACCEPT
BLOCKING 1
```
