# The learning oracle as a random oracle

## The question

Read the learning oracle as a lazily sampled random function from seed names to seeds. Which statements about $\mathsf{Train}$ calls does random-oracle reasoning give that the theory lacks? Does programming, Halil's rule for the designer, admit canaries and release noise and exclude a cryptographic plug-in? What changes when the seed is a short integer stretched by a generator, and what does an experiment measure for the trainer, the attacker and the auditor?

## Meditation

### The object

Let $P^x_\rho$ be the law of $\mathsf L(x;\rho,\xi)$ over $\xi\sim\pi$, and $\bar P^x=\int P^x_\rho\,\mu(d\rho)$. In the named mode the oracle keeps a seed table $\Sigma$ from names to seeds, lazily sampled with point law $\mu$, and $\mathsf{Train}(x,n)$ returns a draw from $P^x_{\Sigma(n)}$. Two features separate this from a random oracle. The oracle allocates the names, so every new point is fresh by construction. The value at a name is a learner instance $x\mapsto P^x_{\Sigma(n)}$, which the caller evaluates at inputs of its choice. The fitting picture is a keyed family with one fresh key per name, used once in the drawn mode and many times in the named mode. The separations of thm-coupling-certificate and thm-reference-access separate one-time from many-time use of a key, and no random-oracle technique produced them.

### Five techniques

Lazy sampling proves thm-replay-audit-steer (a). lem-scrambled-seed-urn is the switching lemma between a random permutation of seed cells and a lazy oracle, and it makes chosen seeds worthless in thm-shadow-run-price-finite-views. Its one new use is the free baseline of a canary audit (prop-canary-audit-unbiased-not-sound).

Observing queries is how a random-oracle reduction extracts. A simulator of $\mathsf{Train}$ reads training inputs, and lem-needle-lower-bound and the clause of thm-exact-twin-price that calls at other inputs count for nothing are this argument.

Rewinding gives the twin, the run rewound with the data oracle reprogrammed at one record and the seed held. def-identity-coupling is that rewinding, and the rewound party is the learner, not the attacker.

Forking appears in lem-agreement-detection, used by thm-coarse-reconstruction-lattice-hard. Two runs share the secret and draw independent rotations, and the bound $p^2$ is Jensen's inequality over the shared secret, as in the reset lemma.

These three give no new statement. Programming gives the only new ones, all about the designer. The recasting thus names techniques the theory already uses (proven, by the cited proofs), and its content lies in programming and in instantiation.

### Programming as admissibility

In the random-oracle model the reduction programs, never the scheme. A designer who programs a canary acts as a reduction that measures an attacker. Programming is therefore a rule for measurement devices, and prop-programming-preserves-prices shows it can be nothing else.

A setup holds three lazily sampled oracles: the data oracle with point law $\mathcal D$, the seed table with $\mu$, and the release-noise oracle with $\mathcal N(0,\sigma^2I_d)$. A *programming* of one of them at a finite set $P$ of points with a law $\nu$ draws $V=(v_p)_{p\in P}\sim\nu$, makes the oracle answer $v_p$ at $p$, and hands $V$ to the designer. Let $Z$ be the joint value of the views of all parties other than the designer and of the oracle values at $P$. The programming is $(\mathcal C,\varepsilon)$-admissible when no test in the class $\mathcal C$ separates the law of $Z$ in the programmed setup from its law in the honest one with advantage above $\varepsilon$. It is perfect when $\nu$ is the product of the point laws and $V$ is independent of all other randomness.

All three oracles can be programmed. Canaries program the data oracle. An auditor that knows the noise programs the noise oracle. An auditor that trains a twin at a recorded seed programs the seed table at the twin's call, and since the twin reaches no other party, $Z$ keeps its law. The counterexample of thm-coupling-free-soundness (d) correlates the run with the release noise, changes the coalition's view, and is excluded by the rule. Whether every twin rule that leaves $Z$ unchanged keeps the multi-round bound is open. A defence programs nothing, because an admissible programming changes no price. Halil's rule therefore cannot admit release noise as a defence, and defences need a second rule, prop-key-free-defence-rule.

### Short seeds

A real seed is an integer $s$ in a finite set $S$, and the client's first-layer weights are $W_s=\iota(G(s))$ for a public generator $G$ and initialization routine $\iota$. Their law is atomic, and an $O(d)$-invariant law with an atom at $W\ne0$ would have uncountably many atoms of equal mass. So every real implementation lies outside $\mathcal P_{O(d)}$ (proven), and thm-short-seed-dichotomy states what survives. The replay audit has the exact structure of the uninstantiability of Canetti, Goldreich and Halevi (prop-replay-audit-uninstantiable). The seed-blind statistical results fail at every finite seed through enumeration, not diagonalization. Hardware randomness helps only as far as it makes the seed name worthless (prop-seed-grip-duality).

### Measurement

| Party | Target | Baseline | Measured side | Proven side |
| --- | --- | --- | --- | --- |
| trainer | rise $\mathrm G$ of a declared learner at $n$ records | $b$, best success when labels are drawn independently of inputs | two-sided band for the learner, a lower bound for its class | upper bound on the class's rise, such as the price $d^{k^*/2}$ of fact-generative-exponent-sq-recovery-bound |
| attacker | success of a declared family on a secret | success on a fresh lazily sampled secret, free of $\mathsf{Train}$ calls | lower band, prop-profile-run-coordinate (b) | upper bound on the class's success at the budget |
| auditor | upper bound on leakage | none | coupled certificate, an upper band for every attacker | lower bound on its own $\mathsf{Train}$ calls, thm-exact-twin-price |

The auditor's row holds the first price of the theory with both sides in hand, and def-known-price states the notion. prop-rise-decomposition-replace-one makes Halil's sentence on the learner's quality exact, with a known decomposition.

## Claims

### prop-programming-preserves-prices: programming changes no price

status: proven

uses: def-learning-oracle, thm-perfect-substitution

Statement. (a) A perfect programming leaves the law of $Z$ unchanged. (b) Let a programming be $(\mathcal C,\varepsilon)$-admissible, and let $A$ be a party and $\mathsf{win}$ a success test such that the map from $Z$ to $\mathsf{win}$, evaluated at the output of $A$ and the secret, lies in $\mathcal C$. Then the success of $A$ moves by at most $\varepsilon$ at every budget, and the price of $\mathcal C$ at level $s$ in the programmed setup lies between the honest prices at $s-\varepsilon$ and $s+\varepsilon$. (c) A modification that moves some price of $\mathcal C$ by more than $\varepsilon$ is not a $(\mathcal C,\varepsilon)$-admissible programming of any oracle. Every defence that works against $\mathcal C$ is of this kind, release noise against the unbounded class and encryption of the records against efficient classes among them. (d) Values $G(k)$ of a generator, programmed into an oracle whose honest values are uniform strings, with $k$ kept by the designer, are admissible against classes of time $T$ at $\varepsilon=\mathrm{Adv}_G(T)$, and by (b) they move no price of such a class by more than $\varepsilon$.

Proof. (a) The value at $p$ is drawn from the point law independently of all else. Drawing it before the run, as the designer does, or at first use, as the oracle does, gives one joint law of all oracle answers, and the designer's copy of $V$ is not part of $Z$. (b) Apply admissibility to the test, with the coins of $A$ absorbed, at every budget. The bracket follows from monotonicity of the price in $s$. (c) Contrapositive of (b). (d) The hybrid that runs the setup on the challenge string. $\square$

### prop-key-free-defence-rule: the rule for defences

status: proven for (a) and (b), heuristic for (c)

uses: def-learning-oracle-model, def-hard-problem-mapping

Definition. A *key-free defence* inserts a general node that applies a kernel $K(\cdot;\omega)$ to the value carried by a channel, where $\omega$ has a public law, is independent of all other randomness, is an input to no other node and reaches no party.

Statement. (a) Every party that receives the defended value, legitimate consumer and attacker alike, holds the same defended value and nothing about $\omega$. A gap between them is then a gap between their tasks or their classes, never between their information. (b) For every class closed under composition with a sampler of $K$, the best success on the defended value is at most that on the undefended value. Gaussian release noise and a random rotation of representations with the rotation erased are key-free defences. Encryption under a key that some party keeps for decryption is not, nor is any defence whose legitimate output is computed with $\omega$. (c) The rule does not exclude planting. Rounding each record's coordinate along an erased random direction $v$ to a grid of step $\gamma$ is a key-free kernel on the channel from the data owner to the trainer. It moves each record by at most $\gamma/2$ and yields records of the layered form of the pancake law, whose reconstruction the registered results price by hCLWE.

Proof. (a) The defended value is a function of the undefended value and $\omega$, and no party holds $\omega$. (b) An attacker on the undefended value samples $\omega$ and runs the attacker on $K(\cdot;\omega)$. The examples follow by inspection, since decryption reads the key. (c) Heuristic. That the rounding kernel yields exactly $H_{v,\beta,\gamma}$ with its registered parameters is not checked. $\square$

Part (a) is the formal content of "no trapdoor". By (c), a planted law with an erased secret is a law some population could have.

### prop-canary-audit-unbiased-not-sound: one run measures and does not certify

status: proven

uses: prop-programming-preserves-prices, prop-profile-run-coordinate, fact-one-shot-estimate-consistency

Setting. The designer draws $m$ canaries $c_1,\dots,c_m\sim\mathcal D$ and independent bits $b_i$ with $\Pr[b_i=1]=1/2$. One run trains on the honest data and the canaries with $b_i=1$. A declared attack outputs a guess $g_i$ from the released model and $c_i$, and $\hat A=\frac1m\sum_i\mathbf 1[g_i=b_i]-\frac12$.

Statement. (a) The success of the attack against a fresh record, the random-oracle baseline, is computed from the one released model and fresh draws of $\mathcal D$, with no further $\mathsf{Train}$ call. (b) $\mathbb E\hat A=\mathrm{Adv}/2$, where $\mathrm{Adv}=\Pr[g=1\mid b=1]-\Pr[g=1\mid b=0]$ is the attack's random-subset membership advantage against an honest record. (c) Let $L^{**}$ memorize its training set as a lookup table, and let $L^*$ do so when a seed bit is one and output a fixed model otherwise. With the lookup test as the attack, $\mathrm{Adv}/2$ is $1/2$ at $L^{**}$ and $1/4$ at $L^*$. Every lower band computed from the released model, the canaries and the bits of one run, and sound at level $\alpha$ over $\{L^*,L^{**}\}$, is at most $1/4$ at $L^{**}$ with probability at least $1-2\alpha$, for every $m$. With $N$ independent runs, Hoeffding's inequality gives a band of width $\sqrt{\ln(1/\alpha)/(2N)}$ whatever $m$.

Proof. (a) An excluded canary is a programmed value that no node reads, so it is independent of the release. (b) $\mathbb E\,\mathbf 1[g_i=b_i]=\frac12+\frac12\mathrm{Adv}$, and the positions are exchangeable. (c) The run of $L^{**}$ has the law of the run of $L^*$ on its seed-one branch, of probability $1/2$. Soundness at $L^*$, whose target is $1/4$, forces the band to be at most $1/4$ on all but probability $2\alpha$ of that branch. $\square$

fact-one-shot-estimate-consistency records the same gap between estimate and bound for AKOOMS24.

### thm-short-seed-dichotomy: a short seed is a short key

status: proven

uses: def-seed-blind-reconstruction-game, thm-blind-orbit-limit, prop-sq-blind-reconstruction-bound, prop-fine-reconstruction-to-hclwe, thm-coarse-reconstruction-lattice-hard, fact-sq-simulates-minibatch-sgd

Setting. The client's weights are $W_s=\iota(G(s))$ with $s$ uniform on a finite set $S$, and $G$, $\iota$ and the record law are public. $P_s$ is the law of one representation under the initial weights, with its side data, under seed $s$, and $\eta=\min_{s\ne s'}\mathrm{TV}(P_s,P_{s'})>0$.

Statement. (a) In the population SQ game a seed-blind server identifies $s$ with $|S|-1$ queries of tolerance below $\eta/2$. In the sample game $N\ge2\eta^{-2}\ln(2|S|/\delta)$ representations under the initial weights identify $s$ with probability $1-\delta$. After identification the server is seed-known. (b) Let the ideal client draw $W=\iota(U)$ for $U$ uniform on $\ell$ bits. For every attacker of time $T$, its success under $W_s$ and under $W$ differ by at most $\mathrm{Adv}_G(T+T_{\mathrm{run}}+T_{\mathrm{chk}})$, the advantage against $G$ of a distinguisher that samples the records, runs the protocol at its challenge string, runs the attacker and checks success.

Proof. (a) Run a knockout tournament. A comparison of champion $c$ with challenger $s'$ queries the Scheffé set $A=\{dP_c>dP_{s'}\}$ and keeps the candidate whose $P(A)$, computed from the public laws, is nearer the answer. If the truth $t$ is in the comparison, the two candidates' values of $P(A)$ differ by their total variation, at least $\eta$, so $t$ wins when $\tau<\eta/2$. The truth wins every comparison it enters, so it is the last champion. In the sample game empirical frequencies replace the answers, and Hoeffding's inequality at deviation $\eta/2$ with a union bound over the $|S|-1$ sets that involve $t$ gives the count. (b) The distinguisher's acceptance probability is the success under $W_s$ on input $G(s)$ and under $W$ on a uniform input. $\square$

Consequences. The conclusion of thm-blind-orbit-limit fails once $N\ge2\eta^{-2}\ln(2|S|/\delta)$, about 400 representations for 64-bit seeds at $\eta=1/2$ and $\delta=10^{-2}$ (computed). Every seed-blind SQ lower bound, prop-sq-blind-reconstruction-bound included, is capped at $|S|-1$ queries. By (b), prop-fine-reconstruction-to-hclwe and thm-coarse-reconstruction-lattice-hard transfer from $\ell$-bit ideal seeds with an additive $\mathrm{Adv}_G$. So does a gradient attacker's ideal-seed bound from fact-sq-simulates-minibatch-sgd, since the attacker runs inside the distinguisher, while the SQ bound it came from does not. The step from atomless to $\ell$-bit seeds is the open finite-precision problem.

### prop-replay-audit-uninstantiable: the replay audit is a Fiat-Shamir audit

status: proven

uses: thm-replay-audit-steer, def-reach-spread-joint-reach

Statement. (a) For every function $h$ from strings to seeds used in place of the random oracle, and every atomless $\mu$, some learning function $L_h$ with deterministic kernels and some target $T$ have reach $p_\tau(T)=0$, while a prover that evaluates $h$ once wins the audit with probability one. Part (a) of thm-replay-audit-steer therefore fails under every instantiation, over the class of all learning functions. (b) In the interactive audit, where the auditor draws $\rho\sim\mu$ after the commitment and sends it, every prover wins with probability at most $n_{\mathrm{rep}}\,p_\tau(T)$, for every learning function.

Proof. (a) Let $L_h(x;\rho)=t_0\in T$ if $\rho=h(\mathrm{cm},0)$ and $m_1$, at distance above $\tau$ from $T$, otherwise. The reach is $\mu(\{h(\mathrm{cm},0)\})=0$. The prover outputs $(t_0,0)$, and the replay at $h(\mathrm{cm},0)$ returns $t_0$. (b) A win needs a replay within $\tau$ of $T$. Given $\rho\sim\mu$ the replays use fresh hardware randomness, independent of the prover's output, and a union bound over $n_{\mathrm{rep}}$ replays finishes. $\square$

The random oracle buys non-interactivity, at the price of the factor $q+1$ and of the heuristic that the learning function does not compute $h$. Part (b) removes the plug-in that prob-reduce-security-to-known-learning-problems flags in this theorem.

### prop-seed-grip-duality: one quantity prices the seed name and the short seed

status: proven

uses: def-learning-oracle, def-identity-coupling, thm-coupling-free-soundness, fact-rerun-reproduction-error

Definition. The *grip* of the seed at input $x$ is $g_x=\sup_{\rho}\mathrm{TV}(P^x_\rho,\bar P^x)$.

Statement. (a) Under any seed law $\mu'$ in place of $\mu$, finite or pseudorandom ones included, the model law at $x$ moves by at most $g_x$ in total variation, and a view of $k$ learning nodes by at most $k\sup_xg_x$, against every class. (b) The identity coupling at $(x,x')$ lies within $g_x+g_{x'}$ in total variation of the independent coupling, which drawn-seed calls sample. So the coupled tail and the tail of the independent twin rule differ by at most $g_x+g_{x'}$. If $\bar P^x$ is atomless, a run and its rerun at one seed coincide with probability at most $2g_x$. (c) An initialization that is a deterministic function of the seed, with atomless law, has grip one.

Proof. (a) $\mathrm{TV}(\int P^x_\rho\,\mu'(d\rho),\bar P^x)\le\int\mathrm{TV}(P^x_\rho,\bar P^x)\,\mu'(d\rho)\le g_x$ by convexity, and a hybrid over the nodes. (b) $\mathrm{TV}(P^x_\rho\otimes P^{x'}_\rho,\bar P^x\otimes\bar P^{x'})\le\mathrm{TV}(P^x_\rho,\bar P^x)+\mathrm{TV}(P^{x'}_\rho,\bar P^{x'})$, then convexity in $\rho$. The diagonal is null under $\bar P^x\otimes\bar P^x$. (c) $P^x_\rho$ is a point mass and $\bar P^x$ has no atom. $\square$

Hardware randomness makes a short seed safe exactly as far as it makes the seed name worthless. By (c) the initial view of split learning gets no protection from it. fact-rerun-reproduction-error reports distances and not total variation, so it does not bound $g$ for whole runs.

### prop-rise-decomposition-replace-one: the learner's rise splits exactly

status: proven for (a), (b) and the counterexample of (c), from memory for the bound of (c)

uses: def-identity-coupling

Setting. $\mathcal D$ is a law on $X\times Y$ with $Y$ finite, $A$ a learner with seed law $\mu$, $D=(z_1,\dots,z_n)\sim\mathcal D^n$, $h=A(D;\rho)$ and $\mathrm{acc}(h,z)=\mathbf 1[h(x)=y]$. The reference law $\mathcal D^\circ=\mathcal D_X\otimes\mathcal D_Y$ draws each label from a lazily sampled random function with the label marginal. Its baseline $b=\max_y\mathcal D_Y(y)$ is the best success of any predictor at a fresh point of $\mathcal D^\circ$. The generalization rise is $\mathrm G=\mathbb E\,\mathrm{acc}(h,z')-b$ for a fresh $z'\sim\mathcal D$. The memorization is $\mathrm M=\frac1n\sum_i\mathbb E[\mathrm{acc}(h,z_i)-\mathrm{acc}(h^{(i)},z_i)]$, where $h^{(i)}$ is trained, at any seed of law $\mu$, on $D$ with $z_i$ reprogrammed to a fresh draw, a dataset written $D^{(i)}$.

Statement. (a) $\mathbb E\,\frac1n\sum_i\mathrm{acc}(h,z_i)-b=\mathrm G+\mathrm M$, for every learner and every coupling of the two seeds. (b) $\mathrm M$ is the generalization gap, so its mean costs one run and held-out data, and only per-record memorization needs twins. (c) The capacity $\mathrm C$, the expected training accuracy on a sample of $\mathcal D^\circ$ minus $b$, bounds $\mathrm M$ for empirical risk minimizers over a class, by symmetrization. It does not bound $\mathrm M$ for learners in general.

Proof. (a) $(D^{(i)},z_i)$ has the law of $(D,z')$, so $\mathbb E\,\mathrm{acc}(h^{(i)},z_i)=\mathbb E\,\mathrm{acc}(h,z')$, and each seed enters through its marginal alone. (b) Read off (a). (c) Take $x$ uniform on $[0,1]$ and $y=\mathbf 1[x>1/2]$ flipped with probability $0.2$. The learner returns its sample as a lookup table, with the best threshold elsewhere, when some threshold fits the sample to $0.7$, and the majority constant otherwise. On $\mathcal D$ it memorizes with high probability, so $\mathrm M\to0.2$. On $\mathcal D^\circ$ the best threshold fits $1/2+O_P(n^{-1/2})$ by the Dvoretzky-Kiefer-Wolfowitz inequality, so the learner outputs the constant and $\mathrm C\to0$. $\square$

### def-known-price: when a price is known

status: proven for (a) and (b), open for (c)

uses: prop-profile-run-coordinate, thm-exact-twin-price, thm-coupling-certificate, thm-black-box-certifiability

Definition. Fix a class $\mathcal C$, an instance $J$, a success level $s$ and a scalar budget. The price is $\pi=\inf\{\beta:\text{some }A\in\mathcal C\text{ of budget }\beta\text{ has }\mathrm{succ}_J(A)\ge s\}$. A measured witness is a declared $A\in\mathcal C$ of budget $\beta_m$ with a lower confidence band at least $s$, sound at level $\alpha$ (prop-profile-run-coordinate (b)). A proven witness is a statement valid at $J$ that every $A'\in\mathcal C$ of budget below $\beta_p$ has success below $s$. The price is known within $c$ when $\beta_m\le c\beta_p$, and then $\pi\in[\beta_p,\beta_m]$ with probability at least $1-\alpha$. Along a family $J_d$ it is known in exponent when $\ln\beta_m/\ln\beta_p\to1$.

Statement. (a) The auditor's price in $\mathsf{Train}$ calls for certifying near-zero leakage is known within a ceiling (thm-exact-twin-price). (b) On a learning function reached only through the oracle, a proven witness exists in two registered cases: for every class through a coupled certificate of the unbounded advantage (thm-coupling-certificate), and for label queries with finite views through drawn-seed runs (thm-black-box-certifiability). (c) For the SQ and gradient classes no certificate sound over every learning function is registered, so their prices are known only on laws the experimenter builds, where a theorem's hypotheses hold by construction.

Proof. The bracket holds on the event that the band is valid. (a) and (b) are the cited theorems. Whether (c) can be overcome is open. $\square$

## Pushbacks on the frame

The recasting is mostly language, since four of the five techniques have registered instances. Drop the loose sentence that programming is what coupled runs do. The power of the named mode comes from many-time use of a key, which random-oracle reasoning does not touch.

Halil's rule cannot admit release noise as a defence, because an admissible programming changes no price. Keep the rule for measurement devices and adopt prop-key-free-defence-rule for defences. That rule excludes encryption under a kept key, and no rule on modifications excludes planting. The ban on planting belongs to the instance class, through record laws the designer does not choose.

The rule excludes the useful canaries. Random-label and out-of-distribution canaries are not honest samples, so they measure worst-case leakage, the target of differential-privacy auditing, and say nothing about an honest record. In-distribution canaries measure the average leakage of an honest record. Halil should decide which target canaries serve.

The idealized seed hides that a real seed is a short key. In an implementation the seed-blind separation is the security of a 64-bit key stretched into the first layer by a generator not built as a cryptographic primitive. Every statistical and SQ seed-blind result is an artifact of the idealization. The polynomial-time results survive only if the generator is pseudorandom for the attacker composed with one run, a cryptographic assumption on a component of the procedure and close to the excluded plug-in. Halil should rule on it, and conj-seed-price-is-ngca-price needs restating with the seed's size in it.

"A price is known when the two sides meet" is the standard notion of a tight bound, and for learner classes the sides meet on synthetic laws only. The learner's rise decomposition is known. Unless a statement beyond the replace-one identity and symmetrization appears, "learning theory itself" is not a contribution of this frame.

## To read

All entries are from memory and unverified.

- Bellare and Rogaway, ACM CCS 1993. Programming and lazy sampling.
- Canetti, Goldreich and Halevi, STOC 1998. Whether their counterexample reads the instantiation's description as $L_h$ does.
- Goldwasser and Kalai, FOCS 2003. Fiat-Shamir uninstantiability, against the interactive audit.
- Bellare and Palacio, CRYPTO 2002. Whether the $p^2$ of lem-agreement-detection is the reset lemma's bound.
- Steinke, Nasr and Jagielski, NeurIPS 2023. The class over which their one-run audit is sound.
- Yeom, Giacomelli, Fredrikson and Jha, IEEE CSF 2018. The theorem tying a bounded-loss membership advantage to the generalization gap.
- Bousquet and Elisseeff, JMLR 2002. The replace-one identity.
- Feldman, STOC 2020. The memorization score.
- Zhang, Bengio, Hardt, Recht and Vinyals, ICLR 2017. Random-label fits as the capacity $\mathrm C$.
- The PyTorch generator documentation, and Matsumoto and Nishimura, ACM TOMACS 1998. The seed width, and whether MT19937 state is recoverable from Gaussian draws.

## Next

conj-seed-worth-code-or-ngca. In the setting of prop-sq-blind-reconstruction-bound (a), let the seed derivation map $S$ onto client rotations whose images of the pancake direction form a set $U$ of unit vectors with pairwise overlap at most $\alpha_0$, and let the initial representation laws be pairwise at total variation at least $\eta$. Then the seed-blind SQ price of weak reconstruction lies between $\frac{11}{288}\min\{|U|,M\}\,\tau_*^2\beta^2/\gamma^2-d$ queries and $|U|-1$ queries of tolerance below $\eta/2$. The seed is worth the lesser of its code size and the NGCA price, and the SQ class sees the geometry of the code and not its pseudorandomness.
