---
title: "The debate on learning-attacker prices"
subtitle: "A Claude Opus builder against a Claude Opus challenger, four rounds, then criticized by Claude Fable and sol, 28 and 29 October 2026"
---

The challenger declared itself satisfied at round 03, with ten objects standing and no blocking challenge. Fable re-derived every proof and constant, accepted nine and asked one revision, with no blocking challenge. sol accepted four and asked for six local repairs. The mathematics is correct. The space does not close the gap you named. Every proven lower bound binds all estimators, never a learner as a learner. Its main setting is also the Gaussian single-index model in another form, where the statistical and efficient prices coincide and much of the structure is known. What it does give is an exact answer to your sentence on "the performance of initial model", and the first price known from a measured side and a proven side. Files are in `lab/theory/spaces/learning-attacker-prices/`, the rounds in `round-00/` to `round-03/` and the critiques in `critique/`.

# 1. What was built

The setting. One federated round at the trainer's square-loss optimum, with Gaussian inputs and labels $Y=\xi W$, where $\xi$ is an independent sign and $W$ depends on $\langle u,X\rangle$. The labels have conditional mean zero, so the trained linear model is the same for every secret direction $u$ and learns nothing about it. The server sees one update per client. The question is what an observer of $T$ updates learns about $u$.

Every observer. A Fano bound says every estimator needs about $d/(24\kappa)$ updates, with $\kappa$ the Kullback divergence of one update along $u$ (proven). A spectral estimator that weights each update by a function of its norm reaches overlap $\frac12$ in 40 of 40 declared runs at $T=20d$ (empirical). On the challenger's law $Q_0$ the price of the full observer is therefore known within a factor $86.5$ at $d=200$ and $81.4$ at $d=400$. This is the first price in the theory with a measured side and a proven side, both counted in updates. The factor is wide, and the lower side rests on a quadrature value with an error estimate, not a certified integral.

The linear attacker. PCA and a linear VAE read only the empirical covariance of the updates. The debate showed that this class reads a Cauchy-type transform of one signed measure of the label law, while the full observer reads a weighted $L^2$ norm of the same measure. The finite identities are proven, two deterministic equivalents are heuristic, and the outlier equation matches simulation within 0.02 (conjecture, accepted as well posed). The learner class enters the price. On a law with $c_2=0$, the second moment carries no signal along $u$. There PCA stays at or below overlap 0.09, while the weighted estimator reaches 0.86 at $T=40d$ for $d=200$ and 0.88 for $d=400$ (empirical, the builder's runs, with the challenger's close behind).

A defence. Per-example normalization of the gradients at a median-fitting optimum makes each update carry only the sign of its residual. At the optimum of this setting it closes the channel exactly, for every observer (proven).

Re-learning from a release. In the Gaussian linear model, an attacker queries a trained release instead of watching updates. Your sentence then has three readings, and all three are now settled.

- The trainer's performance caps the attacker's accuracy (proven, data processing).
- It floors the attacker's success. For your reconstruction example this is the registered `thm-reconstruction-from-conditional-mean`.
- It floors the attacker's cost only when the release answers with nature's noise at inputs no larger than nature's. Then an attacker needs about $n/\kappa$ answers to come within a factor $1+\kappa$ of the trainer's risk, and least squares, a learner of the trainer's own class, attains it (proven). Without the noise or without the bound on query size, $d$ queries suffice.

# 2. What the critics found

The update stream is the single-index model (Fable, proven). At batch one a client's update is, up to small fluctuations, a labelled sample $(\xi X,|Y|)$ of a single-index model whose hidden direction is the secret. So the full observer's price is the degree-two price of Damian, Pillaud-Vivien, Lee and Bruna (DPLB24, Theorems 3.2, 4.1 and 6.1, all in our library). The gap between PCA and the weighted estimator is their Proposition 2.6. The outlier equation and the optimal weight belong to the theory of spectral initialization: Lu and Li 2020, Mondelli and Montanari 2019, Luo, Alghamdi and Lu 2019. None of these three is in the library, and Fable cites them from memory. The council had ruled that the degree of a channel is the DPLB24 generative exponent, and the space did not apply that ruling to its own setting.

No learner in any lower bound (Fable, proven by reading). Every proven lower side binds every estimator. The only class with a lower side is a sufficiency class, the functions of the empirical covariance. Nothing binds an attacker because it trains by gradient steps on a declared architecture. The challenger refused this shape in round 00 and accepted it in round 03, and no round says the standard moved.

The showcase laws are knife edges (Fable). The laws on which PCA fails satisfy $c_2=0$ by construction. That is a balanced moment, a weaker form of the planting the council rejected for item 20. On a generic law the linear attacker is within a constant factor of optimal, $1+\mathrm{Var}(W^2T(W))/c_2^2$, which is $19.5$ for $Y=\langle u,X\rangle\xi$ at large noise (proven in the limit).

No hardness (Fable, proven from DPLB24). The setting has degree two, so the statistical and efficient prices are both of order $d$. Hardness here needs a label law with no degree-two signal, which is planting.

The release theorem is classical in its parts (sol). It is Gaussian conjugate regression with an A-optimal-design trace bound. Its assembly for model extraction may be new, and no search has checked.

sol's six blocking challenges are local, each with a short repair:
- a degenerate stream with zero labels;
- an atom missing from one formula of the clipping result;
- an overstated claim about clipping;
- how the class definition selects a minimizer;
- the existence of the bulk edges in the outlier equation;
- the regime of the slack in the release bracket.

# 3. What this means

Statistical prices of learning attacks are now measurable in this theory, with a measured side and a proven side. Your sentence on the initial model has an exact answer. Both live in Gaussian linear settings, and both are known results in other words, pending the search.

The council and the debate reached the same wall from two directions. Whenever we take the simplest channel that training produces, it reduces to a known single-index or regression problem. The only lower bounds that see the attacker's class restrict what it reads: statistical queries, or a statistic. No tool in the theory binds a gradient learner of a fixed architecture, and that remains the open core (open).

# 4. The next step, and your decisions

The critics propose two different next statements.

- Fable. First run the search on spectral initialization and the exact limits of generalized linear models. Then prove that batching makes the linear attacker optimal: the ratio of the linear class's price to the full observer's tends to one as the batch grows, with first correction $\mathrm{Var}(W^2T(W))/(b\,c_2^2)$. Fable calls it the only claim of the space about a mechanism of training, and it plants nothing.
- sol. Price actual one-pass linear SGD, with labels $\xi\min(|\langle u,X\rangle|,1)$, by a finite-dimensional bracket attained by a declared gradient attacker. The bracket charges both the updates observed and the attacker's own optimizer work, with every parameter bounded from independent runs.

Three decisions are yours.

1. Should the search gate run on spectral initialization before any object of this space enters the booklet?
2. Which next statement, Fable's on batching or sol's on charging the attacker's optimizer work, or should the line stop here?
3. Should the ten objects enter the booklet with attributions to the known results, or stay in the space?
