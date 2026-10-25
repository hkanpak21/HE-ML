---
title: "First rounds of the theory"
subtitle: "Three thinking spaces, 25 October 2026"
---

# Verdict

Three thinking spaces ran three builder and discussant rounds each and closed with no blocking challenge. The booklet, `lib/theory/booklet.pdf`, now holds 63 objects. Of these, 30 are accepted in a round, 29 are borrowed from papers, 2 are open conjectures and 2 are refuted. Five results deserve your reading, listed below with their place in the booklet. Each is proven in a round file, accepted by a discussant and re-derived by the integrator, and none is checked by you. Four decisions wait for you at the end.

Two cautions apply to all of it. The last round of each space was reviewed by gemini-4-argon-medium, whose reviews were short, so the acceptance rests partly on the earlier astra rounds and on the integrator's re-derivation. The integrator checked the arguments and the arithmetic and took the cited lattice and SQ theorems (BRST21, FGRVX17, DKRS23, DPLB24) as the spaces read them.

# 1. The seed separates split-learning attackers

Booklet Theorem 5.8, with Lemma 5.4 and Propositions 5.6 and 5.7.

A split-learning client applies a first layer $\mathrm{ReLU}(Wx)$ with i.i.d. Gaussian $W$ of expansion at least $2.1$ and is trained by an orthogonally equivariant update, plain SGD for instance. The records are drawn from the homogeneous CLWE law $H_{v,\beta,\gamma}$ with $\gamma\ge2\sqrt d$. A server that knows the seed recovers every record exactly with one linear program per record (Lei et al., NeurIPS 2019). A server without the seed faces two prices. As a statistical-query algorithm against a frozen client it needs at least $\frac{11}{288}M\tau_*^2\beta^2/\gamma^2-d$ queries, with $M=\exp(\Omega(c_0^4d))$, to reach correlation $c_0$ with the hidden coordinate. As a polynomial-time algorithm with the record-level view, frozen or trained client, it reconstructs every record within $c_1/\gamma$ only with negligible probability, unless a worst-case lattice problem has a polynomial-time quantum algorithm (BRST21 Corollary 4.2).

The mechanism is Lemma 5.4. The server's whole view of a run on records $x$ equals the view of a run on rotated records $Qx$ from a rotated initialization. So a blind server faces the records only up to a Haar-random rotation, and its task becomes non-Gaussian component analysis on the record law. The reduction costs one honest training run.

Status. Proven, part (iii) conditional on worst-case lattice hardness, part (ii) for SQ attackers only. The hardness enters through the record law. Astra calls this an artificial-distribution reduction, which is decision 4 below.

# 2. Your reconstruction example, in both regimes

Booklet Proposition 4.4, Theorem 5.9, Proposition 5.10 and Conjecture 5.11.

Statistically (Proposition 4.4), an unbounded reconstructor from a representation $Z$ succeeds at least as often as the class baseline $\bar\kappa$ minus the Bayes label error, and at most $\bar\kappa+\sqrt{I(X;Z\mid Y)/2}$. An injective representation gives success one. So for a deterministic injective representation the content of the example lies in the computational regime. Status. Proven.

Computationally (Theorem 5.9), a server that holds a top model whose predictor has excess square risk $\varepsilon$ recovers the label-relevant direction $u$ within $2(\sqrt\varepsilon+\eta_N)/|\beta_1|$ from $N$ held-out representations, and then reconstructs that coordinate of the training records too. This is the floor on attack success that your example predicts. The attacker's error is bounded above by a function of the attacked model's excess risk. Status. Proven, for a frozen linear client and Gaussian records.

The converse, that reconstruction costs what training costs, is false (Conjecture 5.11, refuted). The labels $y=\langle u,x\rangle\xi$ with an independent sign $\xi$ have Bayes predictor zero, so learning the task needs nothing, while the labels reveal $\langle u,x\rangle$ up to sign. What the reconstruction costs is the generative exponent $k^*$ of the task (Proposition 5.10). An SQ server needs $n\ge c\,d^{k^*/2}$ for $k^*\ge3$, and a sample-based server matches it. Status. Proven.

# 3. The training-run price of an unbounded attacker

Booklet Theorem 4.3 and Lemma 4.2.

One learning node trains one of two inputs, and its model reaches the attacker through $k$ views. To come within $a<\frac18$ of the best advantage on every learning function, an attacker under the bottom oracle needs at least $3k'/(1024a^2)$ Train calls, with $k'=2\lfloor k/2\rfloor$, and $2\lceil4k/a^2\rceil$ drawn-seed calls suffice. Chosen, opened and reused seeds do not help, because a random scramble of seed cells turns them into fresh draws (Lemma 4.2). Under the top oracle with deterministic kernels, one call at the honest seed reaches the optimum. In the trainer's units, the trainer spends one run and the attacker spends of order $k/a^2$. Status. Proven. The novelty of the oracle part was checked by one search only.

# 4. Exact twins have a price, and drawn seeds stay sound

Booklet Theorems 6.5 and 6.3.

A certifier that is sound over every learning function and shows near-zero leakage at a zero-leakage function makes at least $(1-\alpha')\ln((1-\alpha')/\alpha)/(-\ln(1-\epsilon_{\mathrm{acc}}))$ expected Train calls at the twin input. At $\alpha=\alpha'=10^{-3}$ and $\epsilon_{\mathrm{acc}}=10^{-2}$ that is 686.5 calls, and for 60,000 records $4.12\times10^7$. Calls at any other input, fine-tunes and warm starts included, count for nothing. This puts a number on your point that every leave-one-out twin costs a run. Status. Proven, numbers computed.

Theorem 6.3 shows that every certificate of the learning-oracle theory stays sound under independent drawn runs, for bottom-oracle targets. A shared seed buys accuracy only. Status. Proven, with two counterexamples showing that independence from the release noise and a shared seed for top-oracle targets are both needed.

# 5. The FORMAL_SECURITY proof note is false as stated

Booklet Theorem 5.1 and Lemma 5.2.

The note `FORMAL_SECURITY/.tools/proof.tex` claims that a black-box adversary against a model trained by an SQ learner on a planted-clique graph has at most the SQ advantage. With the exact oracle, a learner with $O(n^2)$ queries of tolerance $\frac13$ stores every row of the graph, and an unbounded adversary reading the model decides the clique with advantage $1-o(1)$ at $k=n^{1/2-\delta}$. What survives is Lemma 5.2. A learner that reaches its data only through $m$ one-bit samples cannot hand the planted structure to any reader unless $m=\Omega(n^2/k^2)$. Status. Refuted by counterexample, accepted line by line by astra, re-derived by the integrator. The counterexample is half a page and is the quickest result to check.

# Decisions for you

1. The two oracle definitions. The proposal is one oracle with a named and a drawn seed-access mode (booklet Section 6.1).
2. The first target. The proposal is the seed separation of Theorem 5.8, with Conjecture 5.12 as its general form.
3. The attacker class for lower bounds. The proposal is two games, never mixed. Population SQ attackers of frozen clients give unconditional bounds, and polynomial-time attackers with the record-level view give bounds conditional on lattice hardness.
4. Whether a separation whose hard instance is a record law meets your rule that a cryptographic plug-in does not count.

The objective of booklet Chapter 1 also waits for your yes or no.
