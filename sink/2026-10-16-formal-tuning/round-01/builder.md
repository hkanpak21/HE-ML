# Round 01, builder

Verdict of this turn. All nineteen challenges of round 00 are accepted, the five blocking ones included. One of them, ch-degenerate-oracles-undefined, is accepted with a different top oracle, argued in its entry. The definitions are rewritten in `theory/CURRENT.md`. Seven items have full proofs here: lem-atomless-two-point, thm-coupling-certificate, thm-perfect-substitution, thm-reference-access, lem-bank-fidelity, thm-black-box-certifiability and thm-bank-soundness. Some parts of them remain heuristic or open, and each says so. thm-own-data-only is withdrawn. thm-dataflow-composition and thm-replay-audit-steer were not attempted.

Notation follows round 00 with the changes of `theory/CURRENT.md`. $Q_x$ is the law of the model at training input $x$, $P_b$ the law of the view under $H_b$, $\mathrm{TV}$ total variation, and $\mathrm H_\gamma(P\|Q)=\sup_B(P(B)-\gamma Q(B))$ for $\gamma\ge1$, so that $\mathrm H_1(P\|Q)=\mathrm{TV}(P,Q)$.

## Responses to challenges

### ch-handle-laundering

Accepted and fixed. Rule 1 of the access rules in def-learning-oracle requires label open on every name passed to Train or Open, and label eval or open for Eval. Rule 2 gives a caller label open on what its own calls return. The attack $\mathsf{Train}(h^*,\emptyset,\mathcal H,\bot)$ on a name $h^*$ with label eval is refused, and so is every Train call that takes $h^*$ as its starting model. The induction the challenger sketches is step 1 of the proof of thm-perfect-substitution. It shows that a model the adversary may only evaluate never enters a Train or Open call of the adversary.

### ch-substitution-policy

Accepted and fixed. thm-perfect-substitution is now stated for the realizable policy alone, which grants no label beyond the access rules. The upward counterexample is the top oracle of def-degenerate-oracles, and thm-coupling-certificate (c) shows that its gap to the real procedure can be one. On the downward counterexample, an owner in the coalition makes its node's Train call itself and holds its own seed by rule 2. The iterates inside a run are outside the model by the granularity rule of def-learning-oracle-model. A learning node is one call of $\mathsf L$, and a procedure whose owner sees the iterates has one node per step. The theorem compares the oracle adversary with a real adversary that samples $\mathsf L$ at the granularity of $G$. Policies above the realizable one are named in def-degenerate-oracles, and each theorem names the policy it assumes.

### ch-seed-naming

Accepted and fixed. A seed drawn on $\bot$ is stored under a name, and Train accepts a seed name. Seeds and models share one naming mechanism under one set of access rules. The old Proposition 2(a) is now expressible, as the top oracle in thm-reference-access (a). The experimenter forms the coupled pair with $\mathsf{Train}(x_0,\bot)$, which returns a seed name $h$, followed by $\mathsf{Train}(x_1,h)$.

### ch-budget-semantics

Accepted and fixed, both parts. The adversary is an oracle algorithm without computational bound that reaches $\mathsf L$ only through $\mathcal O$, and $\mathsf{ev}$ is public. def-learning-oracle-model fixes the three quantifier patterns. Upper bounds for every adversary are budget-free statements about laws (thm-coupling-certificate (b), thm-reference-access (b)). Attacks and estimators are one algorithm for every learning function (thm-reference-access (b), thm-black-box-certifiability (a) and (b), thm-bank-soundness (a)). Impossibilities say that for every algorithm some learning function defeats it (lem-atomless-two-point, thm-reference-access (c)).

### ch-locality-ill-posed

Accepted. Locality is deleted from the oracle, and the record-indexed seed with it. No current statement needs locality. A realization hypothesis such as Poisson subsampling enters only the open question of thm-coupling-certificate (c), where it would be stated on a named class of realizations.

### ch-seed-domain

Accepted. The seed is a plain $\rho\in\mathcal R$ with law $\mu$. Datasets are finite multisets passed by value, so $P_I$ is the multiset of $z_i$ for $i\in I$ and keeps duplicates. Record keys are gone.

### ch-redundant-properties

Accepted. The oracle keeps fidelity and access. Consistency follows from fidelity when training has deterministic kernels, since then $\mathsf L(x;\rho,\xi)$ does not depend on $\xi$. With hardware randomness it fails, as ch-bank-fidelity-reuse says, and the definition now names that randomness $\xi$. Closure is the list of three calls. Unit cost and the budget moved to def-learning-oracle-model.

### ch-access-policy-simplify

Accepted, with one further simplification. The oracle stores models and seeds and no datasets, because every dataset is passed by value. A dataset that mixes honest records and the adversary's records is formed by the procedure, at a learning node whose dataset argument is the union of an honest input node and the adversary's choice. A reference to a private pool is a choice of an index set at such a node. Labels are open, eval and none, one per caller and name. The sampler is an input node.

### ch-handle-opacity

Accepted. Names are local to the caller, and the $k$-th name a caller receives is the integer $k$. A name is then a function of the caller's own transcript and carries nothing about other callers' calls. This is the challenger's second option, the view up to renaming, built into the definition.

### ch-reference-advantage-one

Accepted. thm-reference-access (a) states the advantage as $p=\Pr_\rho[\kappa(\mathsf L(x_0;\rho))\neq\kappa(\mathsf L(x_1;\rho))]$ under deterministic kernels, and proves that no adversary under the top oracle does better.

### ch-plugin-test-rate

Accepted, all four points. The rate $2\sqrt{k/q}$ is proven in thm-reference-access (b). The atomless case is thm-reference-access (c). The scope is one learning node whose view the adversary can sample. The remark on differential privacy now says that the realizable policy is the adversary of differential privacy for one fixed neighbouring pair.

### ch-execution-schedule

Accepted. def-learning-oracle-model fixes one topological order and an interactive schedule, and the view is the transcript.

### ch-learning-function-choice

Accepted. The training input carries a learner name $\ell\in\Lambda$, so $\mathsf L(x;\rho,\xi)$ indexes the family. The learner name is a choice when the coalition owns or ships the node. Aggregation is a learner name whose datasets are multisets of models.

### ch-eval-budget-vs-allowance

Accepted. Eval on a name with label open is free, since $\mathsf{ev}$ is public. $q_E$ counts Eval calls on names with label eval, and the allowance $Q$ of the procedure caps $q_E$ on the served model. The word budget names the adversary's resource and allowance names the protocol's limit.

### ch-bank-fidelity-reuse

Accepted. def-model-bank lets each entry answer at most one call, and a drawn-seed call consumes an unused entry whose seed was drawn. lem-bank-fidelity proves that the empirical oracle agrees with a learning oracle up to its first refusal. The hardware randomness $\xi$ is part of def-learning-oracle.

### ch-bank-design-game

Accepted. thm-bank-soundness (a) names the random-subset game as the estimand of a random-half bank, and part (b) proves that it can differ maximally from the fixed game.

### ch-experimenter-equality-test

Accepted. The experimenter paragraph is not in the new definitions. Its corrected content is a consequence of lem-atomless-two-point and thm-coupling-certificate (b). From drawn seeds an experimenter can falsify a claimed equality of laws, such as exact unlearning, and cannot certify it when the laws are atomless. It certifies the equality only through a coupling event, for instance when the unlearning procedure replays training under the original seed, so that the two outputs can be compared run by run.

### ch-loo-models-simplify

Accepted. Both named leave-one-out models are removed. The coupled pair survives as the identity coupling of thm-coupling-certificate, under the realization that the oracle exposes through explicit seeds.

### ch-degenerate-oracles-undefined

Accepted in part. Both degenerate oracles now have exact forms in def-degenerate-oracles. The bottom is as proposed, the realizable policy with no bound on Train calls, which thm-perfect-substitution identifies with the real procedure.

The top differs. It is the seed-revealing policy, and it does not open honest datasets. Three arguments support the change. First, a top oracle that opens an honest dataset decides every distinguishing game with advantage one whenever $D_0\neq D_1$, so criterion 4 of the README would hold for every upper bound and would test nothing. Second, the README describes the top as naming honest data with the honest seed. In a distinguishing game the candidate datasets are known, so naming honest data is passing $D_0$ or $D_1$ by value, which needs only the honest seed. In an invert game the honest dataset is the target, and an oracle that opens it is trivial by definition. Third, the seed-revealing top has an exact characterization. Its best advantage equals the coupled divergence under deterministic kernels (thm-coupling-certificate (b), proven), so the gap between the two degenerate oracles is a measurable quantity.

## Definition changes

All definitions are in `theory/CURRENT.md`. The changes, each tied to the challenges above, are these.

1. def-learning-oracle. Locality, consistency, closure and unit cost are removed. The record-indexed seed becomes a plain seed $\rho$ with an atomless law, and hardware randomness $\xi$ is named. The oracle stores models and seeds under per-caller integer names with labels open, eval and none. Three access rules replace the policy list. Datasets are passed by value, and references are gone. Train takes a seed name, and the training input carries a learner name.
2. def-learning-oracle-model. It fixes the schedule, reduces channels to plain, query and none, states the granularity rule, defines the budget as Train calls and Eval calls on names with label eval, separates the budget from the allowance, and fixes the quantifier patterns.
3. def-degenerate-oracles is new. It names the realizable policy, the bottom, the seed-revealing top and the experimenter.
4. def-certifier is new. It defines soundness at level $\alpha$ over a class and the drawn-seed and coupled disciplines. lem-atomless-two-point and thm-coupling-certificate need it.
5. def-model-bank. Entries are single use, drawn-seed entries answer drawn-seed calls, and each entry carries its own hardware randomness.
6. The two leave-one-out models and the experimenter paragraph are removed.

## Proofs

Standing facts. Four facts recur below. Each is standard and its source is named.

The test fact. For laws $P_0,P_1$ of a view, the best advantage of any test, randomized or not, is $\mathrm{TV}(P_0,P_1)=\sup_B(P_1(B)-P_0(B))$. A set on which the density of $P_1$ exceeds that of $P_0$ attains it (Neyman and Pearson).

Data processing. For a Markov kernel $K$ and every $\gamma\ge1$, $\mathrm H_\gamma(KP_0\|KP_1)\le\mathrm H_\gamma(P_0\|P_1)$. Indeed $(KP_0)(B)-\gamma(KP_1)(B)=\int K(B\mid v)\,(P_0-\gamma P_1)(dv)$, and a function with values in $[0,1]$ integrates against the signed measure $P_0-\gamma P_1$ to at most its mass on the positive set of a Hahn decomposition, which is at most $\mathrm H_\gamma(P_0\|P_1)$. In particular, a transcript generated from a view by a kernel that does not depend on the hypothesis has total variation at most that of the view.

The realization fact. Every Borel probability law $Q$ on a standard Borel space is the law of $g(\rho)$ for $\rho\sim\mu$ and some measurable $g$. The space $(\mathcal R,\mu)$ is standard and atomless, so it is isomorphic modulo null sets to $[0,1]$ with Lebesgue measure (Kechris, Classical Descriptive Set Theory, Theorem 17.41, from memory). A standard Borel space is Borel isomorphic to a Borel subset of $\mathbb R$ (Kuratowski), and the quantile function of the image law maps the uniform law onto it.

Lyapunov's theorem. If $\nu_0,\nu_1$ are atomless finite measures on one space, the set of pairs $(\nu_0(B),\nu_1(B))$ over measurable $B$ is convex (Lyapunov, 1940). With $\nu_0=\nu_1$ this is Sierpiński's theorem that an atomless measure takes every value between zero and its total mass.

### Atomless two-point lemma [lem-atomless-two-point]

Statement. Fix training inputs $x_0\neq x_1$ and a measurable deterministic channel $\kappa:\mathcal M\to\mathcal V$ into a standard Borel view space. For a learning function $\mathsf L$ write $Q_b=Q_{x_b}$ and $P_b=\kappa_*Q_b$. Let $\mathcal C$ be a certifier of $\theta=\mathrm{TV}(P_0,P_1)$ in the drawn-seed discipline with at most $N$ Train calls, sound at level $\alpha$ over a class $\mathfrak L$ (def-certifier). Let $\mathsf L\in\mathfrak L$, and suppose that $\mathfrak L$ contains every learning function that agrees with $\mathsf L$ at all training inputs other than $x_0$ and $x_1$. The class of all learning functions satisfies this.

(a) If $P_0=P_1=P$ and $\mathcal V$ has a partition into an even number of measurable cells, each of $P$-mass in $(0,\eta]$, then $\Pr_{\mathsf L}[\hat t\ge1]\ge1-\alpha-N(2N-1)\eta$.

(b) If $P_0=P_1=P$ and every atom of $P$ has mass at most $\eta\le1/4$, then $\Pr_{\mathsf L}[\hat t\ge1]\ge1-\alpha-4N(2N-1)\eta$.

(c) If $P_0$ and $P_1$ are atomless, then $\Pr_{\mathsf L}[\hat t\ge1]\ge1-\alpha$.

(d) Let $\kappa$ be the identity and let $F:\mathcal M\to\mathcal F$ be measurable with $\mathcal F$ finite. If $Q_0$ and $Q_1$ are atomless, the conclusion of (c) holds for a certifier sound over the smaller class of learning functions that agree with $\mathsf L$ outside $\{x_0,x_1\}$ and give $F$ the same law as $\mathsf L$ at $x_0$ and at $x_1$.

Label. Proven, all four parts.

Proof. Step 1, the modification. Let $C_1,\dots,C_M$ be a partition of $\mathcal V$ into measurable cells with $p^b_i=P_b(C_i)$, $M$ even, and $p^b_i>0$ for every $i$ and $b$. For a set $S\subseteq\{1,\dots,M\}$ of size $M/2$ let $A_S=\bigcup_{i\in S}C_i$. Let $\mathsf L_S$ agree with $\mathsf L$ at every training input other than $x_0,x_1$, and give the model laws

$$Q^S_0=Q_0\big(\cdot\mid\kappa^{-1}A_S\big),\qquad Q^S_1=Q_1\big(\cdot\mid\kappa^{-1}A_S^c\big)$$

at $x_0$ and $x_1$. Both conditioning events have positive mass. By the realization fact there are measurable $g^S_b$ with $g^S_b(\rho)\sim Q^S_b$ for $\rho\sim\mu$, and we set $\mathsf L_S(x_b;\rho,\xi)=g^S_b(\rho)$. Then $\mathsf L_S\in\mathfrak L$. Its view laws $P_0(\cdot\mid A_S)$ and $P_1(\cdot\mid A_S^c)$ give mass one to the disjoint sets $A_S$ and $A_S^c$, so $\mathrm{TV}=1$ and soundness gives $\Pr_{\mathsf L_S}[\hat t\ge1]\ge1-\alpha$. Write $\overline{\Pr}$ for the experiment that draws $S$ uniformly among the sets of size $M/2$ and runs the certifier against $\mathsf L_S$. Then $\overline{\Pr}[\hat t\ge1]\ge1-\alpha$.

Step 2, the transcript as a function of two sample sequences. In the drawn-seed discipline every Train call has $s=\bot$, and by fidelity each answer is a fresh draw given its input. Let $Y_b=(Y_b^1,\dots,Y_b^N)$ be independent draws from $Q_b$ under $\mathsf L$, and from $Q^S_b$ under $\mathsf L_S$. Let $W$ collect the certifier's coins and, for every call index $k\le N$, an independent pair $(\rho'_k,\xi'_k)\sim\mu\otimes\pi$. Answer each call at $x_b$ by the next unused entry of $Y_b$, and the $k$-th call, when its input $x$ is neither $x_0$ nor $x_1$, by $\mathsf L(x;\rho'_k,\xi'_k)$. The seed names the certifier receives are integers fixed by its own transcript. This produces the transcript through one measurable map $\Phi(Y_0,Y_1,W)$, with the law of the real interaction under $\mathsf L$ and under each $\mathsf L_S$. In both experiments $W$ has the same law and is independent of $(Y_0,Y_1)$. By data processing,

$$\big|\Pr_{\mathsf L}[\hat t\ge1]-\overline{\Pr}[\hat t\ge1]\big|\le\mathrm{TV}\big(\mathcal L(Y_0,Y_1),\overline{\mathcal L}(Y_0,Y_1)\big),$$

where $\mathcal L$ and $\overline{\mathcal L}$ denote laws in the two experiments.

Step 3, reduction to cells. Let $c^k_b$ be the index of the cell that contains $\kappa(Y^k_b)$, and $c=(c_0,c_1)\in\{1,\dots,M\}^{2N}$. Under $\mathsf L$, given $c$, the entries are independent with $Y^k_b\sim Q_b(\cdot\mid\kappa^{-1}C_{c^k_b})$. Under every $\mathsf L_S$ the same holds, since $Q^S_b(\cdot\mid\kappa^{-1}C_i)=Q_b(\cdot\mid\kappa^{-1}C_i)$ for every cell $i$ of positive $Q^S_b$-mass. So both laws of $(Y_0,Y_1)$, and the mixture over $S$, are images of the respective laws of $c$ under one Markov kernel. Data processing gives $\mathrm{TV}(\mathcal L(Y_0,Y_1),\overline{\mathcal L}(Y_0,Y_1))\le\mathrm{TV}(u,\bar u)$, where $u$ and $\bar u$ are the laws of $c$ in the two experiments.

Step 4, the cell laws. Under $\mathsf L$,

$$u(c)=\prod_{k=1}^N p^0_{c^k_0}\prod_{k=1}^N p^1_{c^k_1}.$$

Under $\mathsf L_S$ the cell of $Y^k_0$ has law $p^0_i\mathbf 1[i\in S]/P_0(A_S)$ and that of $Y^k_1$ has law $p^1_i\mathbf 1[i\notin S]/P_1(A_S^c)$. Averaging over $S$,

$$\bar u(c)=u(c)\;\mathbb E_S\!\left[\frac{\mathbf 1\big[c^k_0\in S\text{ and }c^k_1\notin S\text{ for all }k\big]}{\big(P_0(A_S)\,P_1(A_S^c)\big)^N}\right].$$

In the setting of (a), $P_0(A_S)P_1(A_S^c)=P(A_S)(1-P(A_S))\le1/4$. In the setting of (c), step 5 gives $p^0_i=p^1_i=1/M$, so $P_0(A_S)=P_1(A^c_S)=1/2$ and the product equals $1/4$. In both settings the denominator is at most $4^{-N}$.

Let $E$ be the set of cell vectors whose $2N$ entries are distinct. For $c\in E$, which requires $2N\le M$, exactly $\binom{M-2N}{M/2-N}$ of the $\binom{M}{M/2}$ sets $S$ contain the $N$ entries of $c_0$ and avoid the $N$ entries of $c_1$. Hence

$$\bar u(c)\ \ge\ u(c)\,4^N\frac{\binom{M-2N}{M/2-N}}{\binom{M}{M/2}}\ =\ u(c)\prod_{i=0}^{N-1}\frac{M-2i}{M-2i-1}\ \ge\ u(c).$$

The identity follows from

$$\frac{\binom{M-2N}{M/2-N}}{\binom{M}{M/2}}=\frac{\prod_{i=0}^{N-1}(M/2-i)^2}{\prod_{j=0}^{2N-1}(M-j)}=\prod_{i=0}^{N-1}\frac{(M-2i)^2/4}{(M-2i)(M-2i-1)}.$$

Since $\bar u\ge u$ on $E$,

$$\mathrm{TV}(u,\bar u)=\sum_c\big(u(c)-\bar u(c)\big)_+\le u(E^c)\le\binom{2N}{2}\max_{b,i}p^b_i.$$

The last step is a union bound over the $\binom{2N}{2}$ pairs of positions. Under $u$ two positions carry independent cells with laws $p$ and $p'$, which coincide with probability $\sum_ip_ip'_i\le\max_ip'_i$. With steps 1 and 2, $\Pr_{\mathsf L}[\hat t\ge1]\ge1-\alpha-N(2N-1)\max_{b,i}p^b_i$. In (a) the maximum is at most $\eta$, which proves (a).

Step 5, the partitions. For (b), write $P=\sum_jw_j\delta_{a_j}+P^c$ with atoms $a_j$ of mass $w_j\le\eta$ and an atomless part $P^c$ that gives the atoms mass zero. Group the atoms greedily. Add atoms to the current block until its mass reaches $\eta$, then open a new block. Each closed block has mass in $[\eta,2\eta)$, since the last atom added has mass at most $\eta$, and at most one block stays open, with mass below $\eta$. The set of atoms is countable, hence Borel, and its complement carries $P^c$ alone. By Sierpiński's theorem cut that complement into pieces of mass exactly $\eta$ and one remainder of mass below $\eta$. Merge the open block and the remainder into one cell when their total mass is positive. Every cell now has mass in $(0,2\eta]$, and there are at least $1/(2\eta)\ge2$ cells. If their number is odd it is at least three, and merging two cells leaves an even number of cells of mass at most $4\eta$. Part (a) with $4\eta$ in place of $\eta$ gives (b).

For (c), fix an even $M$. The restrictions of $P_0$ and $P_1$ to any set of positive mass are atomless. Suppose a set $V'$ has $P_0(V')=P_1(V')=r/M$ with $r\ge2$. By Lyapunov's theorem the pairs $(P_0(B),P_1(B))$ for $B\subseteq V'$ form a convex set that contains $(0,0)$ and $(r/M,r/M)$, hence $(1/M,1/M)$. Take such a $B$ as a cell and continue in $V'\setminus B$. Starting from $V'=\mathcal V$ this gives $M$ cells with $p^0_i=p^1_i=1/M$. Step 4 gives $\Pr_{\mathsf L}[\hat t\ge1]\ge1-\alpha-N(2N-1)/M$ for every even $M$, which proves (c).

For (d), $\kappa$ is the identity and cells live in $\mathcal M$. For each $f\in\mathcal F$, apply Lyapunov's theorem inside the fiber $F^{-1}(f)$ to obtain $M$ cells $C_{f,i}$ with $Q_b(C_{f,i})=Q_b(F^{-1}(f))/M$ for $b\in\{0,1\}$ and $i\le M$. Set $A_S=\bigcup_f\bigcup_{i\in S}C_{f,i}$. Then $Q_0(A_S)=Q_1(A_S^c)=1/2$, and $Q_0(\cdot\mid A_S)$ gives $F^{-1}(f)$ the mass $Q_0(F^{-1}(f))$, so $\mathsf L_S$ leaves the law of $F$ unchanged and lies in the smaller class. Run steps 2 to 4 with the cell $(f,i)$ in place of $i$. Under $\mathsf L$ the index $i$ of each entry is uniform on $\{1,\dots,M\}$ and independent of $f$. Under $\mathsf L_S$ the law of $f$ is unchanged and $i$ is uniform on $S$ at $x_0$ and on $S^c$ at $x_1$, independently of $f$. The ratio $\bar u/u$ therefore depends on the indices $i$ alone and is the expression of step 4. The bound $N(2N-1)/M$ follows with $E$ the event that the $2N$ indices $i$ are distinct. $\square$

Remarks. The lemma covers adaptive calls at arbitrary training inputs and any atomless view law. It does not cover randomized channels, such as the Gaussian channel, where the modification changes the view law without separating it. That case is open. The class hypothesis matters. Whether the conclusion survives for a structured class, transformers trained by stochastic gradient descent for instance, is open, because $\mathsf L_S$ need not lie in it.

Without the oracle. The lemma describes the experimenter who lacks the oracle's explicit seeds. A training service that draws its own randomness, or the bottom oracle, supplies independent draws and nothing else. For a model trained in floating point the view law is atomic, but its atoms are far smaller than any feasible $1/N^2$, so part (b) applies with a negligible term (heuristic, assuming no bit-exact model has probability near $1/N^2$). An analytic certificate would need the law of the trained model, which nobody can write down for a transformer.

Degenerate oracles. The lemma is a statement about the bottom discipline. It fails in the coupled discipline that the top oracle and the experimenter share. For a learning function that ignores its dataset, $\beta=0$ and thm-coupling-certificate (b) gives $\hat t=1-\alpha^{1/N}<1$ with certainty.

Prior work. Gilbert and McMillan, "Property testing for differential privacy", Allerton 2018, arXiv 1806.06427 (https://arxiv.org/abs/1806.06427), read in its introduction and Section 5. They restrict to discrete output laws on $n$ points. They prove that pure differential privacy cannot be verified with finitely many samples from black-box access (their Theorem 10), and that testing $(\varepsilon,\delta)$-approximate differential privacy needs $\Omega(\max\{n^{1-o(1)},1/\alpha^2\})$ samples per database (their Theorem 12, through a technique of Valiant 2011). At $\varepsilon=0$ the quantity is total variation. Our lemma is the atomless form of the same phenomenon for one-sided certification, with a weaker birthday-type rate, and it adds adaptive calls at other inputs and the fiber version (d). We do not claim it as new. Its role is the contrast with shared seeds in thm-coupling-certificate.

### Coupling certificate [thm-coupling-certificate]

Setting. One learning node trains $x_b$ under $H_b$, with $x_0\neq x_1$, and its model reaches the view through a channel $K$, a Markov kernel from $\mathcal M$ to a standard Borel space $\mathcal V$. The view laws are $P_b$ as in def-certifier. The identity coupling $\Gamma$ is the law of

$$(W_0,W_1)=\big(\mathsf L(x_0;\rho,\xi_0),\ \mathsf L(x_1;\rho,\xi_1)\big),\qquad\rho\sim\mu,\ \xi_0\sim\pi,\ \xi_1\sim\pi,$$

all independent. The experimenter samples it with $\mathsf{Train}(x_0,\bot)$, which returns a seed name $h$, and $\mathsf{Train}(x_1,h)$. For $\gamma\ge1$ the coupled divergence and the divergence probability are

$$\beta_\gamma(K)=\mathbb E_\Gamma\Big[\mathrm H_\gamma\big(K(\cdot\mid W_0)\,\big\|\,K(\cdot\mid W_1)\big)\Big],\qquad\beta=\Pr_\Gamma[W_0\neq W_1].$$

Let $J_b$ be the law of $(\rho,Y)$ with $\rho\sim\mu$, $\xi\sim\pi$ and $Y\sim K(\cdot\mid\mathsf L(x_b;\rho,\xi))$. It is what the top oracle shows an adversary that sees the node through $K$. The top divergence is $\mathrm D^\top_\gamma(K)=\mathrm H_\gamma(J_0\|J_1)$.

Statement.

(a) Drawn seeds. (i) For an event $E\subseteq\mathcal V$ fixed before sampling, $N$ drawn-seed calls at each input and one-sided Clopper and Pearson bounds at level $\alpha/2$, on $P_1(E)$ from below and on $P_0(E)$ from above, give a lower certifier of $\mathrm{TV}(P_0,P_1)$ at level $\alpha$, sound over every learning function. (ii) If $\mathcal V$ has $k$ elements and $\hat p_b$ is the empirical law of $N$ drawn-seed views at $x_b$, then

$$\hat t=\min\Big\{1,\ \mathrm{TV}(\hat p_0,\hat p_1)+\sqrt{k/N}+\sqrt{2\ln(2/\alpha)/N}\Big\}$$

is sound at level $\alpha$ over every learning function. (iii) For a deterministic channel, no drawn-seed certifier sound over every learning function outputs $\hat t<1$ with probability above $\alpha$ when $P_0$ and $P_1$ are atomless (lem-atomless-two-point (c)).

(b) Shared seeds. For every learning function, every channel $K$ and every $\gamma\ge1$,

$$\mathrm H_\gamma(P_0\|P_1)\ \le\ \mathrm D^\top_\gamma(K)\ \le\ \beta_\gamma(K)\ \le\ \beta,$$

with $\mathrm D^\top_\gamma(K)=\beta_\gamma(K)$ when training has deterministic kernels. At $\gamma=1$ the left end is the best advantage of the bottom oracle and $\mathrm D^\top_1(K)$ the best advantage of the top oracle, at every budget. If $g(w_0,w_1)=\mathrm H_\gamma(K(\cdot\mid w_0)\|K(\cdot\mid w_1))$ is computable, then from $N$ independent draws of $\Gamma$, at a cost of $2N$ Train calls,

$$\hat t=\min\Big\{1,\ \frac1N\sum_{i=1}^Ng(W_0^i,W_1^i)+\sqrt{\frac{\ln(1/\alpha)}{2N}}\Big\}$$

is sound at level $\alpha$ for $\mathrm H_\gamma(P_0\|P_1)$, and for $\mathrm D^\top_\gamma(K)$, over every learning function. When $g$ takes values in $\{0,1\}$, the one-sided Clopper and Pearson bound is also sound, and it equals $1-\alpha^{1/N}\le\ln(1/\alpha)/N$ when no pair diverges. For the Gaussian channel $K(\cdot\mid m)=\mathcal N(f(m),\sigma^2I_d)$ and $\gamma=e^\varepsilon$, $g(w_0,w_1)=\delta_{\mathcal N}(\varepsilon;\|f(w_0)-f(w_1)\|/\sigma)$ with $\delta_{\mathcal N}(\varepsilon;s)=\mathrm H_{e^\varepsilon}(\mathcal N(0,1)\|\mathcal N(s,1))$, and for every $\Delta>0$

$$\beta_{e^\varepsilon}(K)\le\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)+\Pr_\Gamma\big[\|f(W_0)-f(W_1)\|>\Delta\big].$$

(c) Tightness. (i) Some learning function with deterministic kernels has $\mathrm{TV}(P_0,P_1)=0$ and $\mathrm D^\top_1=\beta_1=\beta=1$ for the plain channel. (ii) For every measurable $\phi:\mathcal R\to\mathcal R$ with $\phi_*\mu=\mu$, the $\phi$-coupling $(W_0,W^\phi_1)=(\mathsf L(x_0;\rho,\xi_0),\mathsf L(x_1;\phi(\rho),\xi_1))$ satisfies $\mathrm H_\gamma(P_0\|P_1)\le\mathbb E[\mathrm H_\gamma(K(\cdot\mid W_0)\|K(\cdot\mid W^\phi_1))]$, and the experimenter samples it with explicit seeds. Under deterministic kernels, with a deterministic channel $\kappa$ and a finite view space, some $\phi$ gives $\Pr[\kappa(W_0)\neq\kappa(W^\phi_1)]=\mathrm{TV}(P_0,P_1)$.

Label. Proven, (a), (b), (c)(i) and (c)(ii) as stated. Open, three questions. Does (c)(ii) extend to atomless views? Can a near-optimal $\phi$ be found from oracle calls, uniformly over learning functions? Is there a condition on the realization, Poisson-subsampled iterative learning functions being the candidate, under which $\beta_1(\kappa)\le c\cdot\mathrm{TV}(P_0,P_1)$ for channels that collapse the model?

Proof of (a)(i). By fidelity, the number of drawn-seed views at $x_b$ in $E$ is binomial with parameters $N$ and $P_b(E)$. The one-sided Clopper and Pearson bounds satisfy $\Pr[\underline p_1\le P_1(E)]\ge1-\alpha/2$ and $\Pr[P_0(E)\le\bar p_0]\ge1-\alpha/2$ at every value of the parameter (Clopper and Pearson, Biometrika 1934). On the intersection of the two events, $\underline t=\underline p_1-\bar p_0\le P_1(E)-P_0(E)\le\mathrm{TV}(P_0,P_1)$.

Proof of (a)(ii). $\mathrm{TV}(p_0,p_1)=\frac12\|p_0-p_1\|_1\le\mathrm{TV}(\hat p_0,\hat p_1)+\frac12\big(\|\hat p_0-p_0\|_1+\|\hat p_1-p_1\|_1\big)$ by the triangle inequality. For one input, $\mathbb E\|\hat p-p\|_1=\sum_v\mathbb E|\hat p(v)-p(v)|\le\sum_v\sqrt{p(v)/N}\le\sqrt{k/N}$, by Jensen's inequality and the Cauchy and Schwarz inequality. Changing one of the $N$ draws changes $\|\hat p-p\|_1$ by at most $2/N$, so McDiarmid's inequality gives $\Pr\big[\|\hat p-p\|_1\ge\sqrt{k/N}+t\big]\le e^{-Nt^2/2}$. With $t=\sqrt{2\ln(2/\alpha)/N}$ and a union bound over the two inputs, $\frac12(\|\hat p_0-p_0\|_1+\|\hat p_1-p_1\|_1)\le\sqrt{k/N}+\sqrt{2\ln(2/\alpha)/N}$ with probability at least $1-\alpha$.

Proof of (a)(iii). This is lem-atomless-two-point (c).

Proof of (b). Step 1, measurability. Let $K_0,K_1$ be kernels from a standard Borel space $\mathcal W$ to $\mathcal V$. The Borel sets of $\mathcal V$ are generated by a countable algebra $\mathcal A_0$. For probability laws $P,Q$, a Borel set $B$ and $\epsilon>0$ there is $A\in\mathcal A_0$ with $(P+Q)(A\triangle B)<\epsilon$ (the approximation theorem for measures, Halmos, Measure Theory, Section 13, from memory). Then $P(A)-\gamma Q(A)$ is within $(1+\gamma)\epsilon$ of $P(B)-\gamma Q(B)$, so $\mathrm H_\gamma(P\|Q)=\sup_{A\in\mathcal A_0}(P(A)-\gamma Q(A))$. A countable supremum of the measurable maps $w\mapsto K_0(A\mid w)-\gamma K_1(A\mid w)$ is measurable, so $w\mapsto\mathrm H_\gamma(K_0(\cdot\mid w)\|K_1(\cdot\mid w))$ is measurable.

Step 2, the mixture inequality. Let $\Theta$ be a probability law on $\mathcal W_0\times\mathcal W_1$ and $K_0,K_1$ kernels from $\mathcal W_0$ and $\mathcal W_1$ to $\mathcal V$. For every Borel $B$,

$$\int K_0(B\mid w_0)\,\Theta(dw)-\gamma\int K_1(B\mid w_1)\,\Theta(dw)=\int\big(K_0(B\mid w_0)-\gamma K_1(B\mid w_1)\big)\,\Theta(dw)\le\int\mathrm H_\gamma\big(K_0(\cdot\mid w_0)\|K_1(\cdot\mid w_1)\big)\,\Theta(dw).$$

Taking the supremum over $B$ gives $\mathrm H_\gamma(\Theta K_0\|\Theta K_1)\le\int\mathrm H_\gamma(K_0(\cdot\mid w_0)\|K_1(\cdot\mid w_1))\,\Theta(dw)$, which is joint convexity of $\mathrm H_\gamma$.

Step 3, the top divergence as an average. Let $Q^\rho_b=\int K(\cdot\mid\mathsf L(x_b;\rho,\xi))\,\pi(d\xi)$, a kernel in $\rho$ by Fubini's theorem. Then $J_b(d\rho,dy)=\mu(d\rho)\,Q^\rho_b(dy)$. We show

$$\mathrm D^\top_\gamma(K)=\int\mathrm H_\gamma\big(Q^\rho_0\|Q^\rho_1\big)\,\mu(d\rho).$$

For the upper bound, a set $B\subseteq\mathcal R\times\mathcal V$ with sections $B_\rho$ has $J_0(B)-\gamma J_1(B)=\int(Q^\rho_0(B_\rho)-\gamma Q^\rho_1(B_\rho))\,\mu(d\rho)$, which is at most the right side. For the lower bound, let $\lambda=J_0+J_1$ and let $f_b$ be a density of $J_b$ with respect to $\lambda$. The set $B^*=\{f_0>\gamma f_1\}$ gives $J_0(B^*)-\gamma J_1(B^*)=\int(f_0-\gamma f_1)_+\,d\lambda$. Now $\lambda(d\rho,dy)=\mu(d\rho)\lambda_\rho(dy)$ with $\lambda_\rho=Q^\rho_0+Q^\rho_1$. For a countable generating $\pi$-system $\mathcal P$ of $\mathcal V$ that contains $\mathcal V$, every measurable $A\subseteq\mathcal R$ and every $B\in\mathcal P$ satisfy $\int_A\big(\int_Bf_b(\rho,y)\lambda_\rho(dy)-Q^\rho_b(B)\big)\mu(d\rho)=0$, since both terms equal $J_b(A\times B)$. So for $\mu$-almost every $\rho$ the two finite measures $B\mapsto\int_Bf_b(\rho,\cdot)\,d\lambda_\rho$ and $Q^\rho_b$ agree on $\mathcal P$, and by the $\pi$-$\lambda$ theorem they agree everywhere. Hence $f_b(\rho,\cdot)$ is a density of $Q^\rho_b$ with respect to $\lambda_\rho$ for almost every $\rho$, and

$$\int(f_0-\gamma f_1)_+\,d\lambda=\int\mu(d\rho)\int\big(f_0(\rho,y)-\gamma f_1(\rho,y)\big)_+\lambda_\rho(dy)=\int\mathrm H_\gamma\big(Q^\rho_0\|Q^\rho_1\big)\,\mu(d\rho),$$

because $\mathrm H_\gamma(P\|Q)=\int(p-\gamma q)_+\,d\lambda'$ for densities $p,q$ with respect to any dominating $\lambda'$.

Step 4, the chain. The first inequality is step 2 with $\Theta$ the law of $(\rho,\rho)$ and the kernels $\rho\mapsto Q^\rho_b$, since $P_b=\int Q^\rho_b\,\mu(d\rho)$, combined with step 3. For the second, fix $\rho$ and apply step 2 with $\Theta=\pi\otimes\pi$ on $(\xi_0,\xi_1)$ and the kernels $\xi_b\mapsto K(\cdot\mid\mathsf L(x_b;\rho,\xi_b))$. This gives $\mathrm H_\gamma(Q^\rho_0\|Q^\rho_1)\le\iint\mathrm H_\gamma\big(K(\cdot\mid\mathsf L(x_0;\rho,\xi_0))\|K(\cdot\mid\mathsf L(x_1;\rho,\xi_1))\big)\,\pi(d\xi_0)\pi(d\xi_1)$. Integrating over $\mu$ and using step 3 gives $\mathrm D^\top_\gamma(K)\le\beta_\gamma(K)$. When $\Xi$ is a point, $Q^\rho_b=K(\cdot\mid\mathsf L(x_b;\rho))$ and the inequality is an equality. For the third, $\mathrm H_\gamma(P\|P)=\sup_B(1-\gamma)P(B)=0$ for $\gamma\ge1$ and $\mathrm H_\gamma\le1$, so the integrand of $\beta_\gamma$ is at most $\mathbf 1[W_0\neq W_1]$. The event $\{W_0\neq W_1\}$ is measurable because the diagonal of a standard Borel space is Borel.

Step 5, the two advantages. Under the realizable policy the adversary's best advantage is $\mathrm{TV}(P_0,P_1)$, by the proof of thm-reference-access (b). That proof does not use this theorem, and it holds for every channel, since it uses only that the adversary's own calls do not depend on the hypothesis. Under the top oracle the adversary sees $(\rho,Y)$ and the answers to its own calls. Given the past, each answer has a law fixed by $\rho$, the adversary's inputs and fresh randomness, which does not depend on the hypothesis. By data processing in both directions the transcript has total variation $\mathrm{TV}(J_0,J_1)=\mathrm D^\top_1(K)$, and the test fact makes this the best advantage.

Step 6, statistics. The pairs $(W^i_0,W^i_1)$ are independent draws of $\Gamma$, because each uses a fresh drawn seed and fresh hardware randomness. The values $g(W^i_0,W^i_1)\in[0,1]$ are independent with mean $\beta_\gamma(K)$. Hoeffding's inequality gives $\Pr[\bar g\le\beta_\gamma(K)-t]\le e^{-2Nt^2}$, and $t=\sqrt{\ln(1/\alpha)/(2N)}$ gives $\Pr[\beta_\gamma(K)\le\hat t]\ge1-\alpha$. Since $\mathrm H_\gamma(P_0\|P_1)\le\mathrm D^\top_\gamma(K)\le\beta_\gamma(K)$, the certifier is sound for both. For values in $\{0,1\}$ the count is binomial with parameter $\beta_\gamma(K)$, and the one-sided Clopper and Pearson bound is exact. With no divergence the bound is the $p$ that solves $(1-p)^N=\alpha$, which is $1-\alpha^{1/N}=1-e^{-\ln(1/\alpha)/N}\le\ln(1/\alpha)/N$.

For the Gaussian channel, translation, rotation and scaling are bijections, so data processing in both directions gives $\mathrm H_{e^\varepsilon}(\mathcal N(a,\sigma^2I)\|\mathcal N(b,\sigma^2I))=\delta_{\mathcal N}(\varepsilon;\|a-b\|/\sigma)$. Balle and Wang give the closed form $\delta_{\mathcal N}(\varepsilon;s)=\Phi(s/2-\varepsilon/s)-e^\varepsilon\Phi(-s/2-\varepsilon/s)$ (ICML 2018, arXiv 1805.06530, from memory, and it matches the calibration condition quoted by later work), so $g$ is computable. The map $s\mapsto\delta_{\mathcal N}(\varepsilon;s)$ is nondecreasing. For $0<s\le s'$ the kernel $y\mapsto(s/s')y+\sqrt{1-s^2/s'^2}\,Z$ with $Z\sim\mathcal N(0,1)$ maps $\mathcal N(0,1)$ to itself and $\mathcal N(s',1)$ to $\mathcal N(s,1)$, and data processing applies. Since also $\delta_{\mathcal N}\le1$, $g(W_0,W_1)\le\delta_{\mathcal N}(\varepsilon;\Delta/\sigma)+\mathbf 1[\|f(W_0)-f(W_1)\|>\Delta]$, and taking expectations gives the tail form. $\square$

Proof of (c)(i). Let $\mathcal R=[0,1)$ with Lebesgue measure, $\Xi$ a point, $\mathcal M=[0,1)$, and $\mathsf L(x;\rho)=\rho+h(D)\bmod1$ with $h(D_0)=0$ and $h(D_1)=1/2$. Both model laws are uniform, so $\mathrm{TV}(P_0,P_1)=0$ for the plain channel. Every seed gives $W_0\neq W_1$, so $\beta=1$, and $\beta_1(\mathrm{id})=\Pr[W_0\neq W_1]=1$. Deterministic kernels give $\mathrm D^\top_1=\beta_1=1$.

Proof of (c)(ii). Since $\phi(\rho)\sim\mu$, the pair $(W_0,W^\phi_1)$ has marginals $Q_{x_0}$ and $Q_{x_1}$, and step 2 of (b) applies with $\Theta$ its law. The experimenter draws $\rho$ itself and calls $\mathsf{Train}(x_0,\rho)$ and $\mathsf{Train}(x_1,\phi(\rho))$. For the second claim, let $V_b(\rho)=\kappa(\mathsf L(x_b;\rho))$, $A_v=\{V_0=v\}$ and $B_v=\{V_1=v\}$, with $\mu(A_v)=p_0(v)$ and $\mu(B_v)=p_1(v)$. By Sierpiński's theorem choose $A'_v\subseteq A_v$ and $B'_v\subseteq B_v$ of measure $\min(p_0(v),p_1(v))$. The complements $A''$ of $\bigcup_vA'_v$ and $B''$ of $\bigcup_vB'_v$ both have measure $1-\sum_v\min(p_0(v),p_1(v))=\mathrm{TV}(P_0,P_1)$. A Borel set of positive measure in a standard atomless probability space, with its normalized measure, is again standard and atomless, so any two such sets of equal measure are isomorphic modulo null sets (Kechris, Theorem 17.41). Gluing isomorphisms $A'_v\to B'_v$ and $A''\to B''$, and defining $\phi$ arbitrarily on a null set, gives a measurable $\phi$ with $\phi_*\mu=\mu$ and $V_1(\phi(\rho))=V_0(\rho)$ on $\bigcup_vA'_v$. Hence $\Pr[V_0(\rho)\neq V_1(\phi(\rho))]\le\mathrm{TV}(P_0,P_1)$, and the reverse inequality is the coupling inequality. In the example of (c)(i), $\phi(\rho)=\rho+1/2\bmod1$ gives zero. $\square$

Without the oracle. Without explicit seeds, part (a)(iii) shows that no certificate on the leakage of an atomless release exists, whatever the number of training runs. A certificate by analysis needs the law of the trained transformer, or a mechanism built to have a known law, such as clipping and Gaussian noise in DP-SGD, whose accounting uses a worst-case sensitivity and ignores the data. With the oracle, part (b) certifies $\mathrm H_\gamma(P_0\|P_1)$ for every learning function, and it uses the learning function only through $\beta_\gamma(K)$, a mean of a computable function of coupled pairs.

Degenerate oracles. The theorem separates the two degenerate oracles exactly. An experimenter restricted to what the bottom oracle supplies, drawn seeds, certifies nothing above on atomless views, by (a)(iii). The certificate of (b) is the top oracle's best advantage under deterministic kernels, so against the top oracle it is an equality and guarantees nothing that the adversary does not attain. By (c)(i) the gap between the two oracles can be one. The certificate therefore measures what the seed is worth. A release whose seed stays hidden leaks at most $\beta_\gamma(K)$, and a release whose seed leaks leaks exactly $\beta_\gamma(K)$ under deterministic kernels.

Prior work. Couplings that share or align randomness are the standard way to prove differential privacy of a program whose code is known. Barthe, Gaboardi, Grégoire, Hsu and Strub, LICS 2016 (https://arxiv.org/abs/1601.05047), build approximate couplings in the logic apRHL+. LightDP (Zhang and Kifer, POPL 2017, https://arxiv.org/abs/1607.08228) and ShadowDP (Wang, Ding, Wang, Kifer and Zhang, PLDI 2019, https://arxiv.org/abs/1903.12254) use randomness alignments, maps between the random variables of two executions, which are the seed maps $\phi$ of (c)(ii). Those works analyze code symbolically. Part (b) samples the coupling for a learning function whose code is opaque and proves that the sampled certificate is sound and equals the top oracle's advantage. Hyland and Tople (arXiv 1912.02919, https://arxiv.org/abs/1912.02919, abstract read) report that hiding the seed lowers membership-attack success on non-convex models, an empirical instance of the gap between the two degenerate oracles, on their four datasets. Their abstract states no confidence guarantee for their estimates. One targeted search found no statement of (b) as a sound certificate for opaque learning functions. Novelty of (b) is open until the auditing literature is read (Jagielski, Ullman and Oprea, NeurIPS 2020, and Steinke, Nasr and Jagielski, NeurIPS 2023, both from memory, both lower bounds by attacks).

### Perfect substitution [thm-perfect-substitution]

Setting. Fix a procedure $G$, a coalition $A$, the inputs and $(\mathsf L,\mu,\pi,\mathsf{ev},\nu)$. An $\mathsf L$-sampling adversary in $G$ has the schedule, channels and allowance of def-learning-oracle-model. At any time it may obtain $\mathsf L(x;\rho,\xi)$ with a fresh $\xi\sim\pi$, for a training input $x$ it holds and a seed $\rho$ it holds or draws from $\mu$. Its transcript records the channel outputs, the query answers, the results of these computations with the seeds it drew, and its coins, with names given by its own count. The honest values are the values and the seeds of all honest nodes.

Statement.

(a) For every adversary $\mathcal A$ in $G^{\mathcal O}$ under the realizable policy, there is an $\mathsf L$-sampling adversary $\mathcal S$ in $G$ that makes one computation of $\mathsf L$ per Train call of $\mathcal A$ and one real query per Eval call of $\mathcal A$ on a name with label eval, such that the joint law of the honest values and the transcript of $\mathcal A$ in $G^{\mathcal O}$ equals the joint law of the honest values and the transcript of $\mathcal S$ in $G$.

(b) Every $\mathsf L$-sampling adversary in $G$ is an adversary in $G^{\mathcal O}$ under the realizable policy, with the same joint law.

(c) At every goal, the best success under the bottom oracle equals the best success of an $\mathsf L$-sampling adversary in $G$.

Label. Proven.

Proof. Step 1, what the adversary may open. Under the realizable policy the coalition obtains names only by rule 2, from its own Train calls with label open, and from the query channel with label eval. No rule changes a label. By rule 1 every Train call of $\mathcal A$ takes values it holds and names with label open. By induction over the calls of $\mathcal A$, each name with label open holds either a seed drawn by a call of $\mathcal A$ or $\mathsf L(x;\rho,\xi)$ for an $x$ and a $\rho$ that $\mathcal A$ held or could open, with fresh $\xi$. A model behind a name with label eval never enters a Train or Open call of $\mathcal A$. This proves the induction of ch-handle-laundering.

Step 2, the simulator. $\mathcal S$ runs $\mathcal A$ and keeps a table of the names of $\mathcal A$. On $\mathsf{Train}(x,s)$ it replaces each name in $x$ and $s$ by the value in its table, which exists by step 1. It draws $\rho\sim\mu$ when $s=\bot$, computes $\mathsf L(x;\rho,\xi)$ with fresh $\xi$, and stores the model and the drawn seed under the next names. On $\mathsf{Open}(h)$ it returns the stored value. On $\mathsf{Eval}(h,u)$ it computes $\mathsf{ev}$ with fresh $\sigma$ when $h$ has label open, and otherwise forwards $u$ to the real query interface of the model behind $h$, which exists by step 1. It relays channel outputs, and it sets the choices that $\mathcal A$ sets.

Step 3, equality of laws. List the events of an execution in schedule order. They are node runs, channel deliveries and calls of the adversary. We compare the two executions event by event. Given the whole past, made of the honest values so far, the transcript so far and the adversary's state, the next event has the same conditional law in both executions.

- An honest learning node computes $\mathsf L(x_v;\rho_v,\xi_v)$ with $x_v$ a function of the past. In $G^{\mathcal O}$ the oracle draws $\rho_v$ unless the procedure feeds a seed node, and draws $\xi_v$, independently of everything else by fidelity. In $G$ the node draws them fresh. The seed name has label none for $A$ in $G^{\mathcal O}$, and the seed is private in $G$.
- Honest evaluation and general nodes apply the same formulas with fresh randomness.
- A channel delivery is a fixed function of the node value. Names are fixed by the count of the receiver's own transcript and are equal in both executions.
- A call of the adversary is a function of its state. Its answer has the same conditional law by step 2, since fresh draws in the oracle and in $\mathcal S$ have the same law and are independent of the past. A query on a served model returns $\mathsf{ev}(m_v,u;\sigma)$ with the node value $m_v$ and fresh $\sigma$ in both executions, within the same allowance.
- Choices for the next node are functions of the adversary's state.

For every $n$ the joint laws of the first $n$ events therefore agree, by the chain rule for kernels. The adversary stops with probability one, and the law of a finite transcript is determined by these finite-dimensional laws.

For (b), the $\mathsf L$-sampling adversary replaces each computation of $\mathsf L$ by $\mathsf{Train}(x,\rho)$, passing values it holds, or by $\mathsf{Train}(x,\bot)$ when it draws the seed. Values need no label, and queries become Eval calls on the name the query channel delivers. The kernels of step 3 are again equal. Part (c) follows because success at every goal is a function of the honest values and the transcript. $\square$

Without the oracle. Removing the oracle leaves the same problem, by this theorem. It does not meet criterion 2 of the non-triviality bar and is not proposed as non-trivial. Its role is to identify the bottom oracle with the real procedure, so that every upper bound proven for the bottom oracle is a bound on the real procedure at the granularity of $G$.

Degenerate oracles. The theorem fails for the top oracle. In thm-coupling-certificate (c)(i) the real procedure gives every adversary advantage zero and the top oracle gives advantage one. It also fails without rule 1 of the access rules, by the laundering attack of ch-handle-laundering.

### Reference access [thm-reference-access]

Setting. One honest learning node trains $x_b$ under $H_b$, with a seed drawn by the oracle. For membership, $x_b$ has dataset $P_I$ under $H_0$ and $P_{I\cup\{j\}}$ under $H_1$, but any $x_0\neq x_1$ is allowed. The adversary knows $x_0$ and $x_1$, and receives $\kappa$ of the model through the plain channel, for a deterministic channel $\kappa$. Let $P_b=\kappa_*Q_{x_b}$.

Statement.

(a) Top. Let training have deterministic kernels. Under the top oracle, the adversary that calls $\mathsf{Train}(x_0,h)$ with the honest seed name $h$ and outputs one exactly when $\kappa$ of the answer differs from its view has advantage

$$p=\Pr_\rho\big[\kappa(\mathsf L(x_0;\rho))\neq\kappa(\mathsf L(x_1;\rho))\big],$$

and no adversary under the top oracle has larger advantage, at any budget. If $\mathsf L(x_0;\rho)=\mathsf L(x_1;\rho)$ on an event of probability $e$, for instance the event that a Poisson-subsampled realization never samples record $j$, then $p\le1-e$.

(b) Bottom. Under the realizable policy every adversary has advantage at most $\mathrm{TV}(P_0,P_1)$, at any budget. If $\mathcal V$ has $k$ elements, the plug-in adversary with $2q$ drawn-seed Train calls has advantage at least $\mathrm{TV}(P_0,P_1)-2\sqrt{k/q}$, for every learning function. For a neighbouring pair this is the adversary of differential privacy for that one pair.

(c) No uniform rate on atomless views. Suppose some law on $\mathcal M$ has an atomless image under $\kappa$, as when $\kappa$ is the identity and $\mathcal M$ is uncountable. Let $q$ bound the adversary's Train calls at $x_0$ and $x_1$. For every adversary under the realizable policy and every $\epsilon>0$ there is a learning function with $\mathrm{TV}(P_0,P_1)=1$ under which the adversary has advantage at most $\epsilon$, provided either (i) its Train calls at $x_0$ and $x_1$ all draw their seeds and it never opens the seed names they return, or (ii) the hardware randomness $\xi$ has an atomless law. For every even $M$ one such function gives advantage at most $2(q+1)(2q+1)/M$.

Label. Proven, (a), (b), and (c) under (i) or (ii). Heuristic, (c) for adversaries that pass their own explicit seeds at $x_0$ or $x_1$ under deterministic kernels. The expected argument scrambles a finite seed space by a uniformly random permutation, which turns distinct explicit seeds into draws without replacement, and it is not written yet.

Proof of (a). Under $H_0$ the view is $\kappa(\mathsf L(x_0;\rho))$, which equals $\kappa$ of the answer, so the adversary outputs zero. Under $H_1$ it outputs one exactly when $\kappa(\mathsf L(x_1;\rho))\neq\kappa(\mathsf L(x_0;\rho))$, with probability $p$. Optimality is thm-coupling-certificate (b), step 5, with $K=\kappa$. The best advantage under the top oracle is $\mathrm D^\top_1(\kappa)=\beta_1(\kappa)$, and $\beta_1(\kappa)=\Pr_\rho[\kappa(\mathsf L(x_0;\rho))\neq\kappa(\mathsf L(x_1;\rho))]=p$ because the total variation between two point masses is the indicator that they differ. The last claim holds because the event of probability $e$ lies in the complement of the event that defines $p$.

Proof of (b). The transcript is the view together with answers to the adversary's own calls and its coins. Given the past, each answer has a law fixed by the adversary's inputs, its own seeds and fresh randomness, which does not depend on the hypothesis or on the honest seed, whose name has label none. So the transcript is the image of the view under a kernel that does not depend on the hypothesis, and data processing with the test fact gives the bound. For the plug-in adversary, let $\hat p_b$ be the empirical law of $q$ drawn-seed views at $x_b$, let $\hat A=\{v:\hat p_1(v)>\hat p_0(v)\}$ and $A^*=\{v:p_1(v)>p_0(v)\}$, and let the test output one on $\hat A$. With $d=p_1-p_0$ and $\hat d=\hat p_1-\hat p_0$,

$$\mathrm{TV}(P_0,P_1)-d(\hat A)=\big(d(A^*)-\hat d(A^*)\big)+\big(\hat d(A^*)-\hat d(\hat A)\big)+\big(\hat d(\hat A)-d(\hat A)\big)\le2\sup_B|d(B)-\hat d(B)|,$$

since $\hat A$ maximizes $\hat d$. Also $\sup_B|d(B)-\hat d(B)|\le\frac12\|p_1-\hat p_1\|_1+\frac12\|p_0-\hat p_0\|_1$, and $\mathbb E\|\hat p_b-p_b\|_1\le\sqrt{k/q}$ as in thm-coupling-certificate (a)(ii). The test is independent of the challenge, so the advantage is $\mathbb E[d(\hat A)]\ge\mathrm{TV}(P_0,P_1)-2\sqrt{k/q}$.

Proof of (c). We choose the reference learning function. Fix a law $Q$ on $\mathcal M$ with $P=\kappa_*Q$ atomless, which exists by hypothesis. Let $\mathsf L(x_0;\cdot)$ and $\mathsf L(x_1;\cdot)$ both realize $Q$, from the seed under (i) and from $\xi$ under (ii), by the realization fact applied to $(\mathcal R,\mu)$ or to $(\Xi,\pi)$. Let $\mathsf L$ be constant at every other training input. Under $\mathsf L$ the view has law $P$ under both hypotheses and the adversary's own calls do not depend on the hypothesis, so its advantage is zero. By Sierpiński's theorem cut $\mathcal V$ into $M$ cells of $P$-mass $1/M$. Define $\mathsf L_S$ as in step 1 of lem-atomless-two-point, realized from the seed under (i) and from $\xi$ under (ii). Each $\mathsf L_S$ has $\mathrm{TV}=1$.

Every model the adversary receives from $x_0$ or $x_1$, the honest one included, is a fresh draw. Under (i) the seeds at those inputs are drawn and never opened, and the honest seed has label none. Under (ii) the output depends only on fresh $\xi$, whatever seed is passed. At other inputs the answers do not depend on $S$. As in step 2 of the lemma, write the transcript under hypothesis $b$ as a fixed map of $Y_0,Y_1$, each with $q+1$ entries, and independent randomness $W$. The honest model is $Y^1_b$, and the adversary's calls at $x_c$ use $Y^2_c,Y^3_c,\dots$. Steps 3 and 4 of the lemma with $q+1$ entries per input give, for each $b$,

$$\big|\overline{\Pr}[\mathcal A=1\mid H_b]-\Pr_{\mathsf L}[\mathcal A=1\mid H_b]\big|\le\binom{2q+2}{2}\frac1M=\frac{(q+1)(2q+1)}{M}.$$

Hence $\mathbb E_S\,\mathrm{Adv}(\mathcal A,\mathsf L_S)\le2(q+1)(2q+1)/M$, and some $S$ attains at most this value. Taking $M\ge2(q+1)(2q+1)/\epsilon$ proves (c). $\square$

Without the oracle. Without the oracle the adversary's best attack depends on the law of the trained model, and no uniform statement about it is possible. With the oracle, part (b) gives one attack that works for every learning function on finite views at rate $2\sqrt{k/q}$ in Train calls, and part (c) proves that no such rate exists on atomless views. The learning function enters only through $k$ and $q$.

Degenerate oracles. Parts (a) and (b) are the two degenerate oracles for one node. Their gap is $p-\mathrm{TV}(P_0,P_1)$, which thm-coupling-certificate (c)(i) shows can be one. Part (b) is vacuous for an adversary that knows $\mathsf L$, which attains $\mathrm{TV}(P_0,P_1)$ with no Train call. Part (c) concerns adversaries that reach $\mathsf L$ only through the oracle.

### Own data only [thm-own-data-only]

Withdrawn. Once ch-budget-semantics and ch-handle-laundering are fixed, the old statement is either the identification of the bottom oracle with the real procedure, which thm-perfect-substitution proves, or false for adversaries that reach $\mathsf L$ only through the oracle. Its correct budget-dependent content is thm-reference-access (b) and (c). The rate of (b) is the gain of shadow models on finite views, and (c) proves that no uniform gain exists on atomless views.

### Bank fidelity [lem-bank-fidelity]

Statement. For every design $\Delta$ and every caller strategy, there is a coupling of the execution against the empirical oracle $\widehat{\mathcal O}_\Delta$ and the execution against a learning oracle under which the two transcripts agree up to the first refusal. Hence for every event $B$ of transcripts, $|\Pr_{\widehat{\mathcal O}_\Delta}[B]-\Pr_{\mathcal O}[B]|\le\Pr_{\widehat{\mathcal O}_\Delta}[\text{some call is refused}]$. A fixed design that matches every call of a non-adaptive caller has probability zero of refusal.

Label. Proven.

Proof. The entries of the bank are independent across $i$. For a drawn entry the pair $(\rho_i,\xi_i)$ has law $\mu\otimes\pi$, and for a fixed entry $\xi_i$ has law $\pi$. Up to the first refusal, the transcript is a function of the caller's coins and of the entries used so far. The entry chosen for the next call is the least unused index that matches, a function of the transcript. It is unused, so its randomness is independent of the transcript. Its answer therefore has the conditional law that def-learning-oracle prescribes, $\mathsf L(x;\rho,\xi)$ with fresh $\xi$, and with fresh $\rho$ when $s=\bot$. Eval and Open act identically. The chain rule over events, as in step 3 of thm-perfect-substitution, couples the two executions until the first refusal, and the bound on $B$ follows. $\square$

Without the oracle. The lemma makes the ideal oracle realizable. Every statement proven in the oracle model holds for an experiment run against a bank, up to the probability of refusal. Without it, an estimate from a bank would need its own argument for each design.

Degenerate oracles. The lemma is about implementing the oracle, and it holds under every policy. It makes no claim that a degenerate oracle could void. This is why it is a lemma and is not proposed as non-trivial.

### Black-box certifiability [thm-black-box-certifiability]

Setting. One learning node trains $x_b$ under $H_b$, and the model reaches the adversary through the query channel, as a name with label eval and allowance $Q\ge q_E$. The output set $\mathcal Y$ is finite with $C\ge2$ elements, and the query universe $U\subseteq\mathcal U$ is finite. The evaluation map may be randomized, with fresh $\sigma$ per query. Let $\mathcal T_q$ be the set of deterministic strategies with $q$ queries, complete $C$-ary trees of depth $q$ whose internal nodes carry queries in $U$ and whose leaves carry bits, so

$$|\mathcal T_q|\le|U|^{(C^q-1)/(C-1)}\,2^{C^q}.$$

For a tree $\tau$ let $A(\tau)=\Pr_{H_1}[\tau=1]-\Pr_{H_0}[\tau=1]$, where the model is drawn from $Q_{x_b}$ and each query has fresh evaluation randomness. Let $\mathrm{Adv}^{\mathrm{bb}}(q)=\max_{\tau\in\mathcal T_q}A(\tau)$ and $\mathrm{Adv}^{\mathrm{wb}}=\mathrm{TV}(Q_{x_0},Q_{x_1})$.

Statement.

(o) Reduction. Under the realizable policy every adversary with $q_E$ Eval calls on the served name has advantage at most $\mathrm{Adv}^{\mathrm{bb}}(q_E)$, whatever its Train calls.

(a) Certificate from both sides. With $N$ drawn-seed models at each input, opened by the experimenter, let $\hat A(\tau)$ be the frequency of $\tau=1$ over the models at $x_1$ minus that over the models at $x_0$, each tree run once per model with fresh evaluation randomness. With probability at least $1-\alpha$, for every learning function,

$$\max_{\tau\in\mathcal T_q}|\hat A(\tau)-A(\tau)|\le\epsilon_N:=\sqrt{\frac{2\ln(4|\mathcal T_q|/\alpha)}{N}},\qquad\text{hence}\qquad\Big|\max_\tau\hat A(\tau)-\mathrm{Adv}^{\mathrm{bb}}(q)\Big|\le\epsilon_N.$$

Accuracy $\epsilon$ needs $N=O\big((C^q\ln|U|+\ln(1/\alpha))/\epsilon^2\big)$.

(b) Exchange rate. The adversary under the realizable policy that spends $q_T=2N$ Train calls on shadow models, $N$ at each input, and plays $\hat\tau=\arg\max_\tau\hat A(\tau)$ with $q_E$ Eval calls on the served name has advantage at least

$$\mathrm{Adv}^{\mathrm{bb}}(q_E)-2\sqrt{\ln(2|\mathcal T_{q_E}|)/N}$$

for every learning function.

(c) White box. Let $\mathsf{ev}$ be deterministic and $Q_{x_0},Q_{x_1}$ atomless, and let $\varepsilon\ge0$ with $\mathrm{Adv}^{\mathrm{bb}}(Q)+\varepsilon<1$. A drawn-seed procedure with $N$ Train calls that accepts the collapse claim $\mathrm{Adv}^{\mathrm{wb}}\le\mathrm{Adv}^{\mathrm{bb}}(Q)+\varepsilon$ with probability at most $\alpha$ whenever the claim is false, over every learning function, accepts with probability at most $\alpha$ under $\mathsf L$. A white-box test with a certified advantage above a certified upper bound on $\mathrm{Adv}^{\mathrm{bb}}(Q)+\varepsilon$ refutes the claim.

(d) Shared seeds. With deterministic $\mathsf{ev}$ and $F(m)=(\mathsf{ev}(m,u))_{u\in U}$, for every $q$,

$$\mathrm{Adv}^{\mathrm{bb}}(q)\le\mathrm{TV}(F_*Q_{x_0},F_*Q_{x_1})\le\Pr_\Gamma[F(W_0)\neq F(W_1)]\quad\text{and}\quad\mathrm{Adv}^{\mathrm{wb}}\le\beta,$$

both certifiable from coupled pairs as in thm-coupling-certificate (b), with $O(\ln(1/\alpha)/\epsilon)$ pairs at accuracy $\epsilon$ when no pair diverges. A collapse is certified when the certified upper bound on $\beta$ is at most the certified lower bound on $\mathrm{Adv}^{\mathrm{bb}}(Q)$ from (a), plus $\varepsilon$.

Label. Proven, (o), (a), (b), (c), (d). Open, a matching lower bound for (b), a family of learning functions on which every adversary with $q_T\le c\,C^{q_E}/\epsilon^2$ Train calls falls short of $\mathrm{Adv}^{\mathrm{bb}}(q_E)$ by $\epsilon$. Open, how loose the certificate of (d) is against that of (a).

Proof of (o). Represent the randomness of the adversary's own calls in advance. The $k$-th own Train call uses an independent pair $(\rho'_k,\xi'_k)$ when it draws, and an independent $\xi'_k$ when it passes a seed. Its own Eval calls use independent $\sigma'_k$. Call the coins and these variables $\omega$. They are independent of the hypothesis and of the served model. Given $\omega$ the adversary is deterministic, and its next query to the served name is a function of the earlier served answers. Padded to $q_E$ queries, its interaction with the served model is a tree $\tau_\omega\in\mathcal T_{q_E}$, and its output is the leaf bit. Its advantage is $\mathbb E_\omega A(\tau_\omega)\le\mathrm{Adv}^{\mathrm{bb}}(q_E)$.

Proof of (a). A complete $C$-ary tree of depth $q$ has $(C^q-1)/(C-1)$ internal nodes and $C^q$ leaves, which gives the count. For a fixed tree $\tau$ the $N$ outcomes at $x_b$ are independent Bernoulli draws with mean $\Pr_{H_b}[\tau=1]$, because the models are independent draws from $Q_{x_b}$ and the evaluation randomness is fresh. Hoeffding's inequality gives $\Pr[|\hat p_b(\tau)-p_b(\tau)|\ge\epsilon/2]\le2e^{-N\epsilon^2/2}$, so $\Pr[|\hat A(\tau)-A(\tau)|\ge\epsilon]\le4e^{-N\epsilon^2/2}$. A union bound over $\mathcal T_q$ with $4|\mathcal T_q|e^{-N\epsilon^2/2}=\alpha$ gives $\epsilon_N$. Finally, $|\max\hat A-\max A|\le\max|\hat A-A|$. The count gives $\ln|\mathcal T_q|\le C^q(\ln|U|+\ln2)$ for $C\ge2$, hence the order of $N$.

Proof of (b). Let $Y_\tau=\hat A(\tau)-A(\tau)$. It is a difference of two independent means of $N$ centered variables with values in an interval of length one, so it is sub-Gaussian with variance proxy $1/(2N)$ by Hoeffding's lemma. For $K$ such variables, $\mathbb E\max_k|Y_k|\le\sqrt{2v\ln(2K)}$ with $v$ the proxy, since $e^{\lambda\mathbb E\max|Y|}\le\sum_k(\mathbb Ee^{\lambda Y_k}+\mathbb Ee^{-\lambda Y_k})\le2Ke^{\lambda^2v/2}$ and $\lambda$ can be optimized. So $\mathbb E\max_\tau|Y_\tau|\le\sqrt{\ln(2|\mathcal T_{q_E}|)/N}$. Let $\tau^*$ attain $\mathrm{Adv}^{\mathrm{bb}}(q_E)$. Then $A(\hat\tau)\ge\hat A(\hat\tau)-|Y_{\hat\tau}|\ge\hat A(\tau^*)-|Y_{\hat\tau}|\ge A(\tau^*)-2\max_\tau|Y_\tau|$. The shadow models are independent of the served model, so the advantage is $\mathbb E[A(\hat\tau)]$, which proves the bound. Eval calls on the shadow models are free because the adversary opens them.

Proof of (c). Black-box outcomes are functions of $F(m)$ and the evaluation randomness, so the law of $F(m)$ at both inputs fixes $\mathrm{Adv}^{\mathrm{bb}}(Q)$. By lem-atomless-two-point (d) with this $F$, there are learning functions $\mathsf L_S$ that agree with $\mathsf L$ outside $\{x_0,x_1\}$, have the same law of $F$ at both inputs, and have $\mathrm{Adv}^{\mathrm{wb}}=1$. For them $\mathrm{Adv}^{\mathrm{bb}}(Q)$ is unchanged, so the claim is false and each $\mathsf L_S$ accepts with probability at most $\alpha$. Steps 2 to 4 of the lemma, with the acceptance event in place of $\{\hat t\ge1\}$, give $\Pr_{\mathsf L}[\text{accept}]\le\alpha+N(2N-1)/M$ for every even $M$. The refutation claim holds because both certificates hold together with probability at least $1-2\alpha$ by a union bound.

Proof of (d). Every tree's outcome is a randomized function of $F(m)$, with a kernel that does not depend on the hypothesis, so data processing gives the first inequality. The second and the third are thm-coupling-certificate (b) with the deterministic channels $F$ and the identity. $\square$

Without the oracle. A bound on what $q_E$ label queries reveal needs the law of the trained transformer's labels on $U$. With the oracle, (a) certifies $\mathrm{Adv}^{\mathrm{bb}}$ from both sides and (b) gives an attack, uniformly over learning functions, at a cost that depends on the learning function only through $C$, $|U|$ and $q_E$. Part (c) fixes the form any answer to Küpçü's question can take with drawn seeds. The statement that $Q$ label queries reach what the head reveals can be refuted and never certified on atomless model laws. Part (d) shows what shared seeds add, a certifiable collapse when the coupled divergence is small.

Degenerate oracles. Under the top oracle the reduction (o) fails. In the example of thm-coupling-certificate (c)(i), let $\mathsf{ev}(m,u)$ be the $u$-th binary digit of $m$. Both model laws are uniform, so $\mathrm{Adv}^{\mathrm{bb}}(q)=0$ for every $q$, while a top adversary that knows $\rho$ computes the first digit under $H_0$, queries it once and wins with advantage one. Under the bottom oracle held by an adversary that knows $\mathsf L$, part (b) is vacuous, since that adversary plays $\tau^*$ with no Train call. The exchange rate of (b) is the content of the theorem for adversaries that reach $\mathsf L$ only through the oracle.

Prior work. Sablayrolles et al. (ICML 2019, from memory, cited in the interface report) prove a collapse of white-box to black-box membership inference under a Gibbs posterior assumption on the parameters. Part (c) says that without such an assumption, and without shared seeds, the collapse can only be refuted from training runs. Uniform convergence over a finite class of adaptive trees is textbook. No search was run for the exchange rate (b) or the asymmetry (c), so their novelty is open.

### Bank soundness [thm-bank-soundness]

Setting. A pool $P=(z_1,\dots,z_n)$ and a template $x(D)=(\ell,m_0,D,\mathcal H)$. A bank of $k$ runs draws, independently for each run $i$, a set $S_i\subseteq\{1,\dots,n\}$ that contains each record independently with probability $1/2$, and trains $x(P_{S_i})$ with a drawn seed. The view of run $i$ is $V_i$, a function of its model through a fixed channel. A test is a map $\tau(V,j)\in\{0,1\}$, and $\mathcal T$ is a finite set of tests fixed before the bank is built. The estimate for record $j$ is

$$\hat A_j(\tau)=\frac{1}{k^{\mathrm{in}}_j}\sum_{i:\,j\in S_i}\tau(V_i,j)-\frac{1}{k^{\mathrm{out}}_j}\sum_{i:\,j\notin S_i}\tau(V_i,j),$$

with $k^{\mathrm{in}}_j$ and $k^{\mathrm{out}}_j$ the numbers of runs with and without $j$. The random-subset game $G^{\mathrm{rs}}_j$ draws $S\subseteq\{1,\dots,n\}\setminus\{j\}$ with independent inclusion at rate $1/2$, trains $x(P_S)$ under $H_0$ and $x(P_{S\cup\{j\}})$ under $H_1$, and $A^{\mathrm{rs}}_j(\tau)$ is the advantage of $\tau$ in it. The fixed game $G^{\mathrm{fix}}_{S,j}$ is the same with $S$ fixed, with advantage $A^{\mathrm{fix}}_{S,j}(\tau)$.

Statement.

(a) Estimand and simultaneous error. With probability at least $1-2\alpha$, simultaneously for all $j$ and all $\tau\in\mathcal T$,

$$\big|\hat A_j(\tau)-A^{\mathrm{rs}}_j(\tau)\big|\le\sqrt{\frac{2\ln(4n|\mathcal T|/\alpha)}{k_{\min}}},\qquad k_{\min}=\min_j\min(k^{\mathrm{in}}_j,k^{\mathrm{out}}_j)\ge\frac k2-\sqrt{\frac{k\ln(2n/\alpha)}{2}},$$

for every learning function.

(b) Gap to the fixed game. For every test, $A^{\mathrm{rs}}_j(\tau)=\mathbb E_SA^{\mathrm{fix}}_{S,j}(\tau)$, so the best advantage satisfies $\mathrm{Adv}^*(G^{\mathrm{rs}}_j)\le\mathbb E_S\mathrm{Adv}^*(G^{\mathrm{fix}}_{S,j})$. The gap can be one. If $\mathsf L$ outputs the parity of $|D|$ and $n\ge2$, then $\mathrm{Adv}^*(G^{\mathrm{rs}}_j)=0$ and $\mathrm{Adv}^*(G^{\mathrm{fix}}_{S,j})=1$ for every $S$.

(c) Shadow adversary, average-case game. An adversary with a sampler, one offline bank of $q_T$ shadow models and Eval budget $q_E$ on a label view reaches the average-case black-box optimum within $O\big(\sqrt{(C^{q_E}\ln|U|+\ln(n/\alpha))/q_T}\big)$ for all $n$ targets at once.

(d) The least number of Train calls of a design that yields coupled certificates for $G^{\mathrm{fix}}_{S,j}$ for all $n$ records at once.

Label. Proven, (a) and (b). Heuristic, (c), expected from (a) and thm-black-box-certifiability (a) with the class of trees indexed by the target record, and the count of that class is not checked. Open, (d), with the challenger's conjecture of $\Omega(n)$ calls per seed for designs sound for every learning function and $o(n)$ under a Poisson-subsampled realization.

Proof of (a). Fix $j$ and condition on the membership pattern of $j$ across the runs. Runs are independent. In each run the inclusion of $j$ is independent of $S_i\setminus\{j\}$, which is a rate-one-half subset of the other records, and of the seed. So given the pattern, the views of runs with $j$ are independent draws of the $H_1$ view of $G^{\mathrm{rs}}_j$, and those without $j$ of its $H_0$ view, by fidelity of the bank (lem-bank-fidelity, with no refusal since the design is fixed). For a fixed $\tau$, Hoeffding's inequality given the pattern gives $|\hat A_j(\tau)-A^{\mathrm{rs}}_j(\tau)|\le\sqrt{2\ln(4n|\mathcal T|/\alpha)/\min(k^{\mathrm{in}}_j,k^{\mathrm{out}}_j)}$ except with probability $\alpha/(n|\mathcal T|)$, by the computation in thm-black-box-certifiability (a). A union bound over $j$ and $\tau$ gives probability at least $1-\alpha$ for all of them, and $\min(k^{\mathrm{in}}_j,k^{\mathrm{out}}_j)\ge k_{\min}$. The counts $k^{\mathrm{in}}_j$ and $k^{\mathrm{out}}_j$ are binomial with parameters $k$ and $1/2$. Hoeffding's inequality gives $\Pr[k^{\mathrm{in}}_j<k/2-t]\le e^{-2t^2/k}$, and a union bound over the $2n$ counts with $t=\sqrt{k\ln(2n/\alpha)/2}$ gives the bound on $k_{\min}$ with probability at least $1-\alpha$.

Proof of (b). Under $H_1$ of $G^{\mathrm{rs}}_j$, $\Pr[\tau=1]=\mathbb E_S\Pr_{G^{\mathrm{fix}}_{S,j},H_1}[\tau=1]$, and the same holds under $H_0$. Subtracting gives the identity, and $\max_\tau\mathbb E_S\le\mathbb E_S\max_\tau$ gives the inequality. For the example, in $G^{\mathrm{fix}}_{S,j}$ the parities of $|S|$ and $|S|+1$ differ, so the test that reads the parity has advantage one. In $G^{\mathrm{rs}}_j$, $|S|$ is binomial with $n-1\ge1$ trials at rate one half, whose parity is uniform, so the parities of $|S|$ and $|S|+1$ are both uniform and the view laws are equal. $\square$

Without the oracle. The estimand of a bank is a property of the law of models trained on random halves of the pool, which nobody can write down for a transformer. With the bank, which lem-bank-fidelity makes an oracle, part (a) estimates it for every learning function and every record at a cost of a logarithmic factor in $n$. Part (b) proves that this estimand bounds the average fixed-game leakage from below and certifies nothing about the fixed-game leakage that differential privacy bounds.

Degenerate oracles. Under the top oracle the adversary of the fixed game gets the coupled advantage $p$ of thm-reference-access (a), which is one in the parity example while the bank's estimand is zero. A bank-based leakage report therefore misses a seed-revealing adversary by up to one. For an adversary that knows $\mathsf L$, the rate term of part (c) vanishes and (c) is vacuous.

Prior work. The design is the one Carlini et al. use (IEEE S&P 2022, from memory, not placed). No search was run for a statement that separates its estimand from the fixed-dataset leakage, so the novelty of (b) is open.

### Not attempted this round [thm-dataflow-composition] and [thm-replay-audit-steer]

Neither problem was attempted in round 01. For thm-dataflow-composition the per-round step is thm-coupling-certificate (b) with the Gaussian channel, and the history dependence of the coupled tail is the open step. Two readings bear on it. Li and Micciancio, EUROCRYPT 2021, ePrint 2020/1533 (https://eprint.iacr.org/2020/1533), define the notion that later revisions call IND-CPA-D and give passive key-recovery attacks on CKKS implementations that release decryptions, so IND-CPA does not suffice once decryptions are released (search summary, paper not read). Feldman and Zrnic, NeurIPS 2021 (https://papers.neurips.cc/paper_files/paper/2021/file/ec7f346604f518906d35ef0492709f78-Paper.pdf), account privacy per individual through a Rényi filter and apply it to noisy gradient descent (abstract read). Its per-record realized losses are the analytic counterpart of the coupled tail, and the comparison is for round 02.

## Questions for the challenger

1. Is the seed-revealing policy acceptable as the top degenerate oracle of the README, in place of opening every handle, given the three arguments under ch-degenerate-oracles-undefined?
2. thm-reference-access (c) is proven for adversaries whose calls at the challenge inputs draw their seeds without opening them, and for every adversary when hardware randomness is atomless. Is that scope enough, or should round 02 write the random-permutation argument for explicit seeds under deterministic kernels?
3. For thm-dataflow-composition (b), should the expectation of the coupled tail be taken along the honest trajectory under $H_0$, with the $H_1$ trajectory handled by symmetry, or bounded by the maximum over the two hypotheses?
