---
model: claude-fable-5-1
discussant: fable
date: 2026-10-29
prompt: lab/theory/spaces/learning-attacker-prices/critique/prompt-critique.md
---

# Critique of learning-attacker-prices

The ten objects that stand at the close are true as written, and every step labelled proven holds when I recompute it. No challenge of mine blocks. The space nevertheless does not answer Halil's aim, and the reason is one that the builder and the challenger could only miss together. At batch one and without noise the update stream at the optimum is the Gaussian single-index model with the label $W=|Y|$, so every price in the space is a price of recovering the hidden direction of a single-index model. The full observer's side is the degree-two case of DPLB24, which the council already named as the degree of a channel. The linear class's side is the spectral initialization theory of generalized linear models, which I know from memory only. The one theorem the challenger signed as pricing a learning attacker with both sides proven binds every attacker, and its learner enters as the witness alone, which is the form the same challenger refused in round 00. No object carries computational hardness, no object rests on one of Halil's three open rulings, and the one meeting of a measured and a proven side is a bracket of ratio 86. Section 1 lists what I recomputed, section 2 judges each object, section 3 states what both agents missed, section 4 judges the space, and section 5 tabulates the challenges.

Notation is that of the rounds. $Z=\langle u,X\rangle$, $W\ge0$ is the label magnitude, $T(w)=\mathbb E[Z^2-1\mid W=w]$, $\sigma^2=W^2+\varsigma^2$ at batch one, $c_2=\mathbb E[W^2(Z^2-1)]$, $\kappa_2=\frac12\mathbb E[W^4T(W)^2/\sigma^4]$, and $\hat M=T^{-1}\sum_tv_tv_t^\top$.

## 1. What I checked

I read the files the prompt names in its order, the four rounds in full, the registered entries fact-subgaussian-sample-covariance-concentration, thm-reconstruction-from-conditional-mean, conj-reconstruction-at-training-cost and thm-extraction-exponent-price, the library note `lib/literature/notes/colt/DPLB24.md`, and the FORMAL_SECURITY wiki pages `concepts/generative-exponent.md` and `sources/generative-exponent-single-index.md`. I rederived every proof below by hand and recomputed the constants by quadrature and by simulation in a scratch folder, with the system Python. The runs are small, and each use below states its dimension and seed count. I ran no web search. Prior work I know only from memory is labelled so, and I give no theorem number for it.

Recomputed and confirmed (empirical, numerical).

- The law $Q_0$: $p=0.68269$, $m_2=0.19875$, $m_4=0.11230$, $w_0^2=0.17863$, $T(w_0)=1.5251$, $c_2=0$ to machine precision, $\mu_2=0.2554$, and the profile spike $s=-0.105$ at $\varsigma^2=0.1$.
- The closed form of part (d) of thm-update-direction-chi-square-bound agrees with direct quadrature at $(a,\varsigma^2)\in\{(0.5,1),(1,2),(1.5,4)\}$ to twelve digits, and $\mathbb E[Z^4(Z^2-1)^2]=78$, $\mathrm{Var}(Z^4-Z^2)=74$, $1+74/4=19.5$.
- On $Q_0$ at $\varsigma^2=0.1$: $\mathrm{KL}=0.248296$ on the atom, $0.081324$ off it, $\kappa_{\mathrm{KL}}=0.160111$, which is the builder's round-03 value. Also $\kappa_2=0.1995$ and the full $\chi^2$ constant $\kappa=0.3093$. The Fano lower sides are $46.25$ at $d=200$ and $98.27$ at $d=400$, the ratios $86.5$ and $81.4$, and the one-sided Clopper and Pearson band for 40 of 40 at level $0.05$ is $0.9278$.
- The weighted spike of part (d) of thm-norm-weighted-update-pca: $0.0801$ at $\delta=0$ and $0.0756$ at $\delta=0.02$.
- The band law of round 01: $p_b=0.009819$, $T_b=0.7820$, $T_c=-0.7089$, $w_c^2=0.015867$, $c_2=0$, $s=0.7564$.
- Simulation at $d=200$, $T=20d$, 4 seeds, on $Q_0$: plain PCA overlaps at most $0.10$ for the top and the bottom eigenvector, the triangular weight reaches $0.71$ to $0.80$. On the band law at $d=300$, 3 seeds: bottom overlaps $0.83$ to $0.86$ at $T=10d$, $0.79$ to $0.83$ at $20d$, $0.57$ to $0.64$ at $100d$.
- The release theorem at $d=10$, $n=60$, $N=200$, $\tau=s=s_r=1$, 3000 draws: $R_n=0.1990$, least squares adds $0.0534$, the Bayes attacker given the design adds $0.0527$, the bound of part (c) is $0.0497$. The moment $\iota_m=d/(m-d-1)$ matches Monte Carlo at $(d,m)\in\{(10,15),(10,40),(30,80)\}$.

## 2. The objects

### thm-update-direction-chi-square-bound

True as written (proven, every step rederived). Step 2 needs the symmetry of $\nu_a$ to kill the $k=1$ term, and the statement has it. Step 4 compares $\rho^2\sim\mathrm{Beta}(\frac12,\frac{d-1}2)$ with $G_1^2/d$ term by term, which holds because $(d/2)_k\ge(d/2)^k$. Step 5 uses $(1-x)^{-1/2}-1\le x$ on $[0,\frac12]$, which holds by convexity since the value at $\frac12$ is $0.414$. Part (c)'s constant 2304 is $12\cdot192$ with the loose fourth moment $6b^2A^4$, and the tighter $3b^2A^4$ would give 1152. Part (d) holds with the numbers above.

Hypotheses and status are right. The content is standard. Part (a) is the second-moment method with the Gaussian comparison on the sphere. DPLB24 Lemma 3.1 represents the $\chi^2$ divergence between two planted single-index laws through $\lambda_k$ and the overlap, which is Step 2 with $\hat c_k=\lambda_k\zeta_k$ (record, the DPLB24 note, section 3). Part (b) is the one piece new to the record, and it is exactly the observation that the normalized update is a single-index sample whose along-$u$ law is $\nu_a$. Part (d) is a clean computation.

ch-chi-square-is-planted-second-moment (does not block). The uses line should name DPLB24 Lemma 3.1 as the form of Step 2, so that the booklet does not present the method as new.

Verdict ACCEPT.

### def-optimum-update-stream

Well posed (proven). Properties (i) to (iii) hold as stated. I rederived (iii) with every cross term vanishing by the signs of $\xi$, $X_w$ and $\zeta$, and the bound $s\ge-1$ follows from $Z^2-1\ge-1$.

ch-stream-is-single-index-sample (does not block). The definition omits its own identification. At $b=1$ and $\varsigma=0$ the observer sees $v_t=\xi_tW_tX_t$, hence the direction $\pm X_t/\|X_t\|$ and the norm $W_t\|X_t\|$, and $\|X_t\|^2/d=1+O(d^{-1/2})$. So the stream is $T$ samples of the single-index model with input $\xi X\sim\gamma_d$ and label $W$ known to relative precision $O(d^{-1/2})$, under the conditional law of $W$ given $Z$ symmetrized in $Z$ (proven, by the definition). Noise $\varsigma>0$ adds an isotropic Gaussian and leaves the structure. The definition should say so in one sentence, because every later price is then a single-index price and the literature on it applies at once (section 3.1). The builder said as much once in round 00 and neither agent returned to it.

Verdict ACCEPT.

### thm-norm-weighted-update-pca

True as written (proven, every step rederived). Part (a) is the $O(d-1)$ symmetry. In Step 3 the condition on $T$ gives $\eta\le\frac38\lambda_-|\gamma_g|/(c_0^2(A+\varsigma)^2\lambda_+)$ and $K^2\eta\le\frac38|\gamma_g|/\lambda_+\le\frac38$, so the quadratic branch of the registered fact never binds. Step 4 is a two-sided Rayleigh argument and needs no Davis and Kahan theorem. In part (c) the stated $6(A^2+\varsigma^2)^2/d$ is valid and the exact value is $2(A^2+\varsigma^2)^2/d$, as the challenger said. The quadrature values of part (d) are right.

ch-fact-form (does not block, from memory, unverified). The registered fact places $K^2$ outside $\max(\delta,\delta^2)$. Vershynin's Theorem 4.6.1, which it quotes through BRST21, places $K^2$ inside $\delta$, so the quadratic branch there carries $K^4$. The proof is unaffected because $K^2\eta\le\frac38$, so only the linear branch is used, and the absolute constant $C_1$ absorbs the difference. The integrator should check the fact's wording against the book when it is in the library.

Novelty. The estimator is the spectral method with a preprocessing function for single-index models. DPLB24 Theorem 4.1 at $k=2$ is the partial trace of the empirical degree-two Hermite tensor of $(x,\mathcal T(y))$ with a denoiser $\mathcal T=\zeta_2$, and $\zeta_2(w)=T(w)/\sqrt2$ here, so the signed weight $\psi\propto W^2T(W)/\sigma^4$ of prop-signed-weight-update-pca at $\varsigma=0$ is that denoiser up to the normalization by $\sigma^2$ (record, the DPLB24 note). The exact symmetry of (a) and the Lipschitz perturbation of (c), which handle the fact that the observer reads $W\|X\|$ and not $W$, are the part specific to this stream.

Verdict ACCEPT.

### prop-update-direction-fano-recovery

True as written (proven, every step rederived). Step 1 is Markov's inequality on $e^{d\rho^2/4}$ with $\mathbb Ee^{d\rho^2/4}\le\sqrt2$ from Step 4 of the theorem. Step 2 is data processing for the indicator of the event $F$ followed by $\mathrm{kl}(p'\|q')\ge p'\log(1/q')-\log2$. Step 3 is the golden formula with $Q=P_\circ$. Step 4's cap $K(a)$ is the Gaussian KL under convexity, and $\mathbb E[m^2\mid a]=\sigma^2-\varsigma^2+b^{-2}\sum_ia_i^2T(a_i)$ is right. The constant is $\frac43\log2=0.9242$. The limit 39 and the tail split at $3\sqrt{\log\varsigma}$ hold.

Hypotheses and status are right. The argument is the Fano bound with a spherical cap, standard, and its value is the explicit constant. It binds the genie observer that sees the label magnitudes, so its $\kappa_{\mathrm{KL}}$ overstates what the real observer learns, as the builder says.

Verdict ACCEPT.

### prop-full-clipping-optimum-filter

True as written (proven). Parts (a) to (d) are one line each. Part (e) uses the lower tail $\Pr[\chi^2_d\le d-2\sqrt{dx}]\le e^{-x}$ at $x=9d/64$, where $d-2\sqrt{dx}=d/4$, and the triangle inequality through the two normalized streams, which have one law by (b).

Hypotheses and status are right after the renaming of round 02. The content is elementary. At a conditional median with no atom the residual's sign is a fair coin independent of the input, so the normalized per-example gradient is a function of the input and the model alone. This is a correct observation about sign descent at a median fit and it has no depth. Its title claims a mechanism that removes every degree of the channel, and that is true because normalization at the optimum removes the label from the update altogether, including the learning signal. The proposition is an exact filter and a trivial one.

Verdict ACCEPT.

### prop-signed-weight-update-pca

True as written (proven, rederived). The two parts $g_\pm$ each satisfy the theorem, the errors add, $\eta\le\frac34$ follows from $|\gamma_g|\le2(A+\varsigma)^2$ and $\rho_++\rho_-\ge1$, and Step 4 of the theorem uses only the form $\alpha I_d+\gamma uu^\top$ with real $\alpha$. The remark that $\gamma_g\approx2\kappa_2/\|\psi\|_\infty$ for the linearized weight is right in order (heuristic).

Verdict ACCEPT.

### def-statistic-learner-class

Well posed (proven). The class $\mathcal A_S$ of functions of a statistic and independent coins, its price, the subsampling closure and the two replaced sentences are right. Remark (i)'s bound $k-N$ holds, since the minimum-norm solution of $\phi S=S$ is the projection $SS^+$.

ch-learner-clause-empty (does not block). The challenger noted in round 01 that a learning attacker in the definition's sense is as large as the class of all estimators, because a maximum-likelihood mixture with $n$ components reads the empirical measure. The definition keeps the learning clause as decoration and prices classes by their statistic. Halil's sentence that attacks come from learning algorithms is then met in name. The object that is priced is a sufficiency class, and no lower bound in the space binds a learner because it learns.

ch-known-within-unbounded (does not block). The definition calls a price known within $c$ for any finite $c$. With no cap on $c$ every bracketed price is known. The word should be reserved, or the definition should name the $c$ at which a price counts as met, since Halil's sentence is that hardness arrives when the two sides meet.

Verdict ACCEPT.

### conj-linear-class-reads-cauchy-transform

Well posed, and its exact parts hold. The Schur identities are right (proven). Given the two deterministic equivalents, the terms in $\sigma^2$ cancel and the outlier equation is $\gamma=g\Psi(g)$ (proven, algebra rederived). The derivative identity that gives at most one root on each side holds, because $\sigma^2+W^2T(W)=\mathbb E[a^2\mid W]\ge0$ (proven). Part (b1) holds (proven, rederived). The Haar average keeps the mean-square overlap, the reflections in the eigenbasis make the coefficients conditionally uncorrelated, and $\bar F$ is conditionally independent of $u$ given $\hat M$, so the overlap is a convex combination of the eigenvectors' conditional overlaps. The first Taylor coefficients of $\Psi$ are $c_2$ and $s\,\mathbb E[\sigma^4]$ (proven). My simulations reproduce the band law's window to within $0.03$.

Status. The object is accepted as well posed with content open. I think the status is wrong, and that most of the content is a theorem in print.

ch-cauchy-transform-is-spectral-initialization (does not block, from memory, unverified). At $\varsigma=0$ the matrix $\hat M=T^{-1}\sum_tW_t^2(\xi_tX_t)(\xi_tX_t)^\top$ is the spectral initialization matrix $T^{-1}\sum_t\mathcal T(y_t)x_tx_t^\top$ of a generalized linear model with Gaussian inputs, label $y=W$ and preprocessing $\mathcal T(y)=y^2$. Lu and Li (Information and Inference, 2020) prove the phase transition and the limiting overlap of its top eigenvector in the proportional regime $d/T\to\gamma$, in closed form through two Cauchy-type transforms of the law of $(\mathcal T(y),Z)$, by the same Schur complement and the same deterministic equivalents. Their formulas are, as far as I recall them, the builder's equation and $\Omega$. Mondelli and Montanari (Found. Comput. Math., 2019) and Luo, Alghamdi and Lu (IEEE Trans. Signal Process., 2019) give the optimal preprocessing, which is the signed weight of the builder's remark, and show that it reaches the weak recovery threshold. Noise $\varsigma>0$ changes the along-$u$ law to $\nu_a$ and is a mild extension. Part (a) is therefore a theorem to borrow at $\varsigma=0$, and a short extension at $\varsigma>0$, and its status should become borrowed or sketch after the search. No search row exists for any of these papers, and the search gate requires one before the claim of novelty stands.

ch-full-observer-is-dplb24-at-degree-two (does not block, with record). Part (c) says both ends of the full observer's bracket scale with $1/\kappa_2$ at large noise. At $\varsigma=0$, $\kappa_2=\frac12\mathbb E[T(W)^2]=\lambda_2^2$ in the notation of DPLB24 Definition 2.4 with label $W$. DPLB24 Theorem 4.1 at $k=2$ recovers the direction from $\tilde O(d/\lambda_2^2)$ samples, Theorem 6.1 gives the information-theoretic rate $\tilde\Theta(d/(\lambda_2^2\epsilon^2))$, and Eq. (3), which the paper inherits from Mondelli and Montanari and from Barbier et al., states that the degree is two exactly when $\mathbb E[\mathbb E[Z^2-1\mid Y]^2]\ne0$ (record, the DPLB24 note and the wiki page `concepts/generative-exponent.md`). The full observer's price of order $d/\kappa_2$ is this. The gap between plain PCA and the full observer is DPLB24 Proposition 2.6 at the level of constants. PCA reads the label transform $y\mapsto y^2$, whose degree-two Hermite coefficient is $c_2/\sqrt2$, and the full observer reads the best transform, whose coefficient is $\lambda_2$. On $Q_0$ the first vanishes and the second does not. In the council's words, the linear class reads an information exponent and the full observer reads the generative exponent, both equal to two, at the level of $\lambda_2$ against $c_2$. The council had already accepted that the degree of a channel is the generative exponent with the secret as the label. The space re-derived its degree-two case.

What remains after the two challenges is the finite-ratio window on the band law, which is a corollary of the outlier equation, and the batch dependence, which the conjecture does not state.

Verdict REVISE, for status and attribution. No statement is false.

### prop-measured-meets-proven-full-observer

True as written (proven given the numerical constant, which I recomputed to six digits). The rotation argument that makes runs at $u=e_1$ Bayes runs holds because the weights are functions of norms and the eigenvector is equivariant. The band is sound. The ratios are $86.5$ and $81.4$.

ch-bracket-is-not-a-meeting (does not block). The object says that this is the first instance of Halil's sentence that a price is known when a measured price meets a proven one. A ratio of 86 is a bracket. It is not a meeting. The gap is the genie's label magnitudes in $\kappa_{\mathrm{KL}}$, Fano's $1/24$, and a triangular weight chosen by hand at $T=20d$ with $T=10d$ left uncertified at 22 of 40. The honest sentence is that the full observer's price on $Q_0$ at $d=200$ lies in $[47,4000]$. The lower side binds every estimator, so the object prices no learner.

Verdict ACCEPT.

### thm-release-relearning-price-bracket

True as written (proven, every step rederived and checked numerically). Part (a) is data processing with Jensen's inequality on the convex map $S\mapsto\mathrm{tr}(S^{-1})$. Part (b) is the scaling attack. The decomposition of Step 3 holds because $u-\hat u$ has conditional mean zero given the records and the release noise and coins are independent of $u$ given them. In Step 4, $S_X=\tau^2I_d-\Sigma_{\mathrm{post}}$ by the law of total covariance, $S_X^{-1}=I_d/\tau^2+s^2(X^\top X)^{-1}/\tau^4$, the posterior of $\hat u$ given an adaptive design is Gaussian with precision $S_X^{-1}+\sum_jx_jx_j^\top/s_r^2$, and the AM and HM inequality with Jensen's inequality for $y\mapsto d^2/y$ gives the display. The direction of the final solve is right, since $R_n\le s^2\iota_n$ weakens the requirement on $N$. Part (d) is least squares. Part (e) follows with the inverse Wishart moment, which the challenger proved. My simulation puts the bound five percent below the Bayes attacker given the design, as the challenger found.

Two slips of wording. The upper end of (e) is the least integer $N\ge d+2$ with $N-d-1\ge(n+s^2/\tau^2)/\kappa$, which can exceed $d+1+(n+s^2/\tau^2)/\kappa$ by one. The title's "exactly when" is an overstatement, since the price is of the order of $n s_r^2/(\kappa s^2)$ under the power cap for every $s_r>0$, and the words should be "when and only to the extent that".

Novelty. None. Part (a) is data processing. Part (b) is the equation-solving extraction of a linear model. Parts (c) to (e) are Bayesian linear regression with the A-optimal design bound on the trace of the posterior covariance (from memory, unverified). The challenger named the source and accepted it.

ch-learner-absent-from-floor (does not block, section 3.2). The challenger wrote that this is the first statement in the space in which a learning attacker is priced in learning units with both sides proven. The lower side of parts (c) and (e) binds every attacker, unbounded ones included. Least squares enters as the witness that attains it. This is the form the challenger refused in round 00, in ch-learner-class-gap, as a statistical price with the attacker class playing no part in the lower bound. The theorem is correct and it is not what the challenger said it is.

ch-floor-is-a-change-of-units (does not block). In absolute terms the attacker's extra error from $N$ answers at power $d$ is of order $ds_r^2/N$, which does not involve $n$. The trainer's records enter only because the target error is set at $\kappa R_n$ with $R_n\approx ds^2/n$. The sentence that the attacker pays the trainer's records is then the identity $ds_r^2/N=\kappa ds^2/n$ read as $N=ns_r^2/(\kappa s^2)$. It is true, and it is a choice of units. The phenomenon behind it is that an answer at nature's noise and nature's power is a record, which is part (c) of the superseded proposition under the name nature.

Verdict ACCEPT.

## 3. What both agents missed together

### 3.1 The update stream is the single-index model

At $b=1$ the stream of def-optimum-update-stream is, up to the $O(d^{-1/2})$ fluctuation of $\|X\|$ and the Gaussian noise $\zeta$, the dataset $(\xi X,W)$ of a single-index model whose hidden direction is the secret (proven, section 2). Every price in the update-stream half of the space is therefore a sample complexity for recovering a single-index direction, with three estimator classes: plain PCA, the spectral method with a preprocessing function, and every estimator. For this triple the literature holds the following, part on record and part from memory.

- The information-theoretic side at degree two: DPLB24 Theorem 6.1 and Eq. (3), with $\lambda_2^2=\kappa_2$ (record).
- The efficient upper side at degree two with the optimal denoiser: DPLB24 Theorem 4.1 (record).
- The SQ lower side at degree two: DPLB24 Theorem 3.2 (record).
- The finite-ratio phase transition and overlap of plain and preprocessed PCA: Lu and Li 2020, with the optimal preprocessing of Mondelli and Montanari 2019 and Luo, Alghamdi and Lu 2019 (from memory, unverified).
- The exact asymptotic limits of the full observer in the proportional regime: Barbier, Krzakala, Macris, Miolane and Zdeborová, PNAS 2019 (from memory, unverified).

The council had already ruled that the degree of a channel is DPLB24's generative exponent with the secret as the label, and thm-shadow-price-is-generative-exponent stands in the register. The space did not apply its own council's ruling to its own setting. The reason, I think, is that both agents read the stream as a security object, a FedSGD round, and never wrote down that the client's update is a labelled sample. A critic who had watched one agent would have been as likely to miss it, since the identification is one line and the stream's description hides it behind $v_t$.

The consequence for the verdicts is a status change on the conjecture and an attribution on three proven objects. The consequence for the space is larger. Its claim to have given Halil's subclass an exact meaning is the claim that the information exponent of the label transform $y^2$ differs from the generative exponent at the level of constants, and that is DPLB24 Proposition 2.6.

### 3.2 The learner is absent from every proven lower side

The proven lower bounds of the space are thm-update-direction-chi-square-bound, prop-update-direction-fano-recovery and parts (a), (c) and (e) of thm-release-relearning-price-bracket. Each binds every estimator. The only lower side in which a class enters is part (b1) of the conjecture, and that class is the set of functions of $\hat M$, a sufficiency class. No bound in the space holds because the attacker learns by gradient steps, by a declared loss, or on a declared architecture. Halil's two sentences, that attacks come from learning algorithms and that the attacker's model must be as strong as the attacked one, are therefore met by a class named for a statistic and by a witness that is a learner, which is the shape the challenger called insufficient for G1 in round 00 and sufficient in round 03. The standard moved between the rounds and no round says so.

### 3.3 The showcase laws are knife edges

The laws on which the linear class fails, $Q_0$ and the band law, satisfy one equation, $c_2=0$, by construction. The challenger said in round 00 that this is a knife edge sharper than the builder's, and the council had rejected the degree-four aim for planting a moment balance. On a generic law the price of linearity is the Jensen ratio $1+\mathrm{Var}(W^2T(W))/c_2^2$, a constant, equal to $19.5$ for $Y=\langle u,X\rangle\xi$ at large noise (proven in the limit), and the challenger measured no gain for the weighted estimator over PCA at the experiment law at measurable dimension (empirical, round 00). The gap the space exhibits is infinite exactly where a designer has balanced one moment of the label law. That is a weaker version of the plant Halil ruled out, and it is the same weakness the council found in item 20. The space's honest result on generic laws is that the linear attacker is within a constant of optimal.

### 3.4 Hardness

No object in the space is computationally hard, and no object separates a polynomial-time class from the statistical price. The setting cannot give one. A linear model at its square-loss optimum on Gaussian inputs is a channel of generative exponent two for every label law with $\lambda_2\ne0$, and DPLB24 place the statistical and the efficient price at $\Theta(d)$ there. Hardness in this setting is reachable only by a label law with $\lambda_2=0$, which is the planted construction the council rejected. This is a limit of the setting. The method has its own limit. Information bounds and sufficiency arguments bind classes of estimators, and the space has no tool that binds a gradient learner of a fixed architecture, which the builder conceded in P2 of round 00 and nobody has lifted.

## 4. The space against Halil's aim

Does it answer the aim. In part. Halil asked for a bound on the success of a VAE, or anything, given the setting, in computational terms, with a measured side meeting a proven side and hardness arriving from that meeting. The space gives a bound on the success of a linear VAE given the setting, through the outlier equation, with the mechanism of its failure named, and a bracket for every attacker at a measured dimension. It gives nothing in computational terms beyond the count of observations, nothing that binds a learner as a learner, and no hardness. The release theorem gives the floor on cost Halil described, in the Gaussian linear model, and that floor is Bayesian linear regression.

Where it falls short, and why. Section 3 gives the two limits. The setting, a Gaussian linear model at its optimum, is a degree-two single-index channel in which the statistical and efficient prices coincide. The method, information and sufficiency bounds, cannot see a learner's algorithm. The council's object was chosen to be the simplest channel training produces, and the space found that in that channel there is nothing to price except the gap between PCA and the optimal spectral method.

Beautiful or ugly. The pair of the Cauchy-type transform for the linear class and the $L^2$ norm for the full observer, read off one signed measure, is beautiful. It is also, if my memory of Lu and Li and of Mondelli and Montanari is right, theirs. The release theorem and the clipping proposition are plain. The constants 2304, 86 and $2.2\times10^8$ are honest and ugly, and the builder said so.

Known under another name. Yes, and section 3.1 names them. The parts I can source from the library are DPLB24 Lemma 3.1, Proposition 2.6, Theorems 3.2, 4.1 and 6.1 and Eq. (3). The parts I know from memory are the spectral initialization theory and the exact GLM limits, and a search must run before any object of this space enters the booklet as new.

The three rulings. No object rests on an answer to any of them. The release theorem prices a given $s_r$ and recommends nothing, as the challenger required. Clipping is part of the procedure as given. No canary and no seed appears. I agree with the challenger here (proven, by reading).

The next space. Two statements, in order. First, the search gate. The next space runs the rows for Lu and Li 2020, Mondelli and Montanari 2019, Luo, Alghamdi and Lu 2019 and Barbier et al. 2019, and reclassifies the conjecture. Second, the one statement to prove, which is the only claim of the space about a mechanism of training rather than about the label law, and which round 01 proposed and round 02 dropped.

In def-optimum-update-stream with bounded labels, $\varsigma>0$ and $c_2\ne0$, let $p_{\hat M}(b)$ be the price of the class of functions of $\hat M$ and $p_*(b)$ the price of every estimator, both at overlap $\frac12$ and success $\frac23$, at batch $b$. Then
$$\lim_{b\to\infty}\frac{p_{\hat M}(b)}{p_*(b)}=1,\qquad\text{with}\qquad \frac{\kappa(b)}{\beta_b^2/2}=1+\frac{\mathrm{Var}(W^2T(W))}{b\,c_2^2}+O(b^{-2}),$$
where $\kappa(b)$ is the per-update $\chi^2$ of the theorem and $\beta_b=c_2/(\mu_2+b\varsigma^2)$.

The second display is the first-order content and I expect it to be a short computation (heuristic, from the central limit theorem for the along-$u$ component, whose variance excess is $\beta_b$ and whose higher Hermite coefficients fall as $b^{-3}$). The first display needs the full observer's threshold in the Gaussianizing limit, where the model tends to the spiked covariance model and PCA is optimal under the spherical prior (heuristic, Perry, Wein, Bandeira and Moitra, Ann. Statist. 2018, from memory, unverified). The statement plants nothing, uses no oracle, is measurable by varying $b$ at fixed $b\varsigma^2$, and says what batching does to a learning attacker. It is also where the single-index literature stops, since a batched update is a sum of labelled samples and not one of them.

## 5. Challenges

| Challenge | Object | Blocks |
| --- | --- | --- |
| ch-chi-square-is-planted-second-moment | thm-update-direction-chi-square-bound | no |
| ch-stream-is-single-index-sample | def-optimum-update-stream | no |
| ch-fact-form | thm-norm-weighted-update-pca | no |
| ch-learner-clause-empty | def-statistic-learner-class | no |
| ch-known-within-unbounded | def-statistic-learner-class | no |
| ch-cauchy-transform-is-spectral-initialization | conj-linear-class-reads-cauchy-transform | no |
| ch-full-observer-is-dplb24-at-degree-two | conj-linear-class-reads-cauchy-transform | no |
| ch-bracket-is-not-a-meeting | prop-measured-meets-proven-full-observer | no |
| ch-learner-absent-from-floor | thm-release-relearning-price-bracket | no |
| ch-floor-is-a-change-of-units | thm-release-relearning-price-bracket | no |

None blocks. No statement is false and no definition is ill posed. The REVISE on the conjecture is for its status and its attribution.

## Verdicts

```text
VERDICT thm-update-direction-chi-square-bound ACCEPT
VERDICT def-optimum-update-stream ACCEPT
VERDICT thm-norm-weighted-update-pca ACCEPT
VERDICT prop-update-direction-fano-recovery ACCEPT
VERDICT prop-full-clipping-optimum-filter ACCEPT
VERDICT prop-signed-weight-update-pca ACCEPT
VERDICT def-statistic-learner-class ACCEPT
VERDICT conj-linear-class-reads-cauchy-transform REVISE
VERDICT prop-measured-meets-proven-full-observer ACCEPT
VERDICT thm-release-relearning-price-bracket ACCEPT
BLOCKING 0
```
