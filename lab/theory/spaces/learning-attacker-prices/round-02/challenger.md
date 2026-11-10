# Round 02 of learning-attacker-prices, challenger

Claude Opus 5.5, challenger, 2026-10-29. Judgement of `round-02/builder.md`, after `round-01/summary.md`.

The repairs hold, and five of the six objects stand. The object I tested hardest, prop-trainer-accuracy-caps-release-attacker, is true in its three parts and wrong in two places around them. Its remark claims that release noise of nature's variance makes the attacker pay of the order of the trainer's records. That is false in its own setting, since queries of the attacker's choice can be scaled until the noise is negligible (proven, a two-line counterexample). Its reading of Halil splits his sentence into a ceiling on accuracy and a floor on cost, and it omits the reading the register already proves for his own example, a floor on the attacker's success set by the trainer's performance (thm-reconstruction-from-conditional-mean). Its own part (b) is a second instance of that floor. I add two proven pieces to the conjecture on the linear class. Its outlier equation has at most one root on each side of the bulk. Under the uniform prior, no function of $\hat M$ beats the best of its eigenvectors in mean-square overlap. One challenge blocks.

## 1. What I checked

I read the summary of round 01 and the builder's turn. I rederived the overlap function $\Omega$ of the conjecture from the Schur formula, every step of prop-signed-weight-update-pca with its constants $\frac38$ and $\frac34$, the Laurent and Massart exponent $9d/64$ of part (e) of the clipping proposition, and the three parts and the remark of the trainer proposition. I recomputed $\kappa_{\mathrm{KL}}$ on $Q_0$ by my own quadrature and the Clopper and Pearson band, and I replicated the certified witness in 40 fresh runs. Prior work known only from memory is labelled so. I did no web search.

## 2. My open challenges

ch-finite-ratio-profile is resolved. The conjecture is withdrawn, and its replacement carries the outlier equation as its content. The builder's independent implementation reproduces my numbers to 0.01. ch-precision-reads-past-the-statistic and ch-mean-parameter are resolved by the two replaced sentences of def-statistic-learner-class, which I checked word for word. ch-signed-weights is resolved by prop-signed-weight-update-pca (section 4). ch-normalization-not-clipping is resolved by the renaming and by part (e).

ch-vacuous-at-measured-dimension is resolved for the full observer on $Q_0$ by prop-measured-meets-proven-full-observer. It stays open for the linear class, as the builder says. It does not block.

ch-no-trainer-price is answered in part (section 3.4). It does not block.

The builder adds that a class bound to a fixed statistic can lose success as data grow, while the class of all estimators cannot, since it may ignore observations. The second half is proven, and the first is empirical on the band law. I agree that this belongs in the definition.

## 3. Halil's sentence and the trainer proposition

### 3.1 The mathematics

Part (a) holds (proven). The attacker's estimate is a function of the records, the queries and independent coins, so its risk is at least the Bayes risk $R_n$ from the records. In the Gaussian model $R_n=\mathbb E\,\mathrm{tr}\big((X^\top X/s^2+I_d/\tau^2)^{-1}\big)$, and convexity of $S\mapsto\mathrm{tr}(S^{-1})$ with $\mathbb EX^\top X=nI_d$ gives $R_n\ge ds^2\tau^2/(n\tau^2+s^2)$. Part (b) holds (proven). An exact linear release is solved from $d$ queries in general position, and $\epsilon^2\ge R_n$ gives $n\ge ds^2/\epsilon^2-s^2/\tau^2$, so the ratio of prices tends to $\epsilon^2/s^2$. Part (c) holds as an identity of laws (proven). The decomposition $\mathbb E\|\tilde u-u\|^2=R_n+\mathbb E\|\tilde u-\hat u\|^2$ in the remark is right (proven), since $u-\hat u$ has mean zero given the records, and the release noise and the attacker's coins are independent of $u$ given the records.

None of the three is new. (a) is data processing. (b) is the equation-solving extraction of linear models (Tramèr, Zhang, Juels, Reiter and Ristenpart, USENIX Security 2016, from memory, unverified). (c) is the sample form of thm-bayes-release-loss-matched-price, and its release is not computable from the records, since a fresh draw of $Y$ given $X$ needs $u$. So (c) lies outside the scope of (a), and an attacker with $N>n$ such answers beats $R_n$. The proposition should say that (c) describes nature, not a release of the trainer.

### 3.2 Three readings of the sentence

Halil's sentence, in the framing of 25 October, concerns his own example. A reconstructor maps intermediate vectors to raw data, and "in case I can reduce the reconstruction work to learning problem that is being attacked I can have a clear lowerbound which is the performance of initial model". Three readings are possible, and each has a status on record.

1. A floor on the attacker's cost, so that the attacker pays at least what the trainer paid. For reconstruction it is refuted (conj-reconstruction-at-training-cost, refuted in computational-limits). For extraction from an exact release it fails by part (b). For a release that answers like nature it holds by part (c).
2. A ceiling on the attacker's accuracy for the trainer's own target. It holds by data processing, part (a).
3. A floor on the attacker's success, set by the trainer's performance. For Halil's example it is proven. thm-reconstruction-from-conditional-mean bounds the attacker's error by $2(\sqrt\epsilon+\eta_N)/|\beta_1|$ in the excess risk $\epsilon$ of the attacked model, and the register's own statement calls it "the floor on attack success in Halil's example". prop-reconstruction-label-sandwich gives the companion bound from below, in which the reconstructor succeeds at least as often as the class baseline minus the Bayes label error.

ch-third-reading (does not block). The proposition presents readings 1 and 2 as the whole of the matter, and concludes that Halil's sentence "holds as a bound on the attacker's accuracy" in the sense of reading 2. Readings 2 and 3 point in opposite directions. Reading 2 says the attacker never knows more than the trainer. Reading 3 says a better trainer makes a better attacker. Reading 3 matches the words "a lowerbound which is the performance of initial model", and the space's register already proves it for his example. The builder's own part (b) is an instance of reading 3 as well. With an exact release the attacker reaches the trainer's risk with $d$ queries, so in the release model the trainer's performance is both a ceiling, by (a), and an attained floor on success, by (b) (proven). What fails is reading 1. The honest summary for Halil is that the trainer's performance pins the attacker's accuracy from both sides and does not price the attacker. The proposition's title says the second half correctly. Its "Other regime" paragraph and the response to ch-no-trainer-price should be rewritten around the three readings before any of this reaches a reading for Halil.

### 3.3 ch-chosen-query-scaling (blocks)

The remark lets the release add noise of variance $s^2$ to its answers, and claims that the second term $\mathbb E\|\tilde u-\hat u\|^2$ is of order $ds^2/N$ for $N$ answers. Then reaching $2R_n$ would cost answers of the order of the trainer's records. In the proposition's setting the release answers queries of the attacker's choice, and their norm is not bounded. Query $te_j$ for $j\le d$. The answer is $t\hat u_j+sN_j$, so $\tilde u_j=(t\hat u_j+sN_j)/t$ has error $s^2/t^2$, and $\mathbb E\|\tilde u-\hat u\|^2=ds^2/t^2$ from $d$ queries (proven). With $t^2\ge ds^2/R_n$, which is of order $n$, the attacker reaches $2R_n$ with $d$ queries. So the remark is false as stated, and with it the sentence that the floor "needs answers as noisy as nature" in the sense used.

The repair is one hypothesis. Either the queries satisfy $\|x\|^2\le d$, the scale of the input law, or the noise scales with $\|x\|$. Under $\|x\|^2\le d$ the Fisher information of $N$ answers has trace at most $Nd/s^2$, and the van Trees inequality gives $\mathbb E\|\tilde u-\hat u\|^2$ at least of order $\min(ds^2/N,\ \mathbb E\|\hat u\|^2)$ (heuristic in the exact constant, the van Trees inequality from memory). The remark's conclusion then holds in order. The floor needs answers as noisy as nature at inputs no larger than nature's, which is exactly the condition under which the release's answers resemble records.

### 3.4 What remains of ch-no-trainer-price

My round-00 challenge asked for a comparison of attacker and trainer in an access model where the attacker sees less, with the sample-priced form of thm-bayes-release-loss-matched-price as the natural aim. The proposition gives the comparison in its simplest model and settles readings 1 and 2 there. The sample-priced statement for a learning attacker re-learning from the answers of a trained release, with norm-bounded noisy queries, is still unstated. It does not block. A round could state it as a conjecture whose lower side is the repaired remark and whose upper side is least squares on the answers.

## 4. The objects of round 02

### conj-linear-class-reads-cauchy-transform

The setting is right. $\phi$ is a function of $\sigma^2$ because $W=\sqrt{\sigma^2-\varsigma^2}$, and $\mu$ has total mass $c_2$. I rederived $\Omega$. With $F(\lambda)$ the equivalent of $h^\top(\lambda-B)^{-1}h$, $h^\top(\lambda-B)^{-2}h=-F'(\lambda)$, and the chain rule through $g$ gives exactly the stated $\Omega(g)$ (proven, given the equivalents). The exact part holds. The conjecture is now what my derivation supports, and its status, open, is honest.

Two proven additions, which the builder may take into the object.

At most one outlier on each side. On $(g_-,0)\cup(0,g_+)$,
$$\frac\gamma{g^2}+\Psi'(g)=\Big(\frac\gamma{g^2}-\mathbb E\Big[\frac{\sigma^4}{(1-\sigma^2g)^2}\Big]\Big)+\mathbb E\Big[\frac{(\sigma^2+W^2T(W))\sigma^2}{(1-\sigma^2g)^2}\Big]>0,$$
because the first bracket is positive inside the edges and $\sigma^2+W^2T(W)=\mathbb E[a^2\mid W]\ge0$. So $\gamma/g-\Psi(g)$ is strictly decreasing on each side, and $\gamma=g\Psi(g)$ has at most one root there (proven, at the level of the two equivalents). Since $\gamma/g-\Psi(g)\to+\infty$ as $g\downarrow0$ and $\to-\infty$ as $g\uparrow0$, there is an outlier above the bulk exactly when $g_+\Psi(g_+)>\gamma$, and below it exactly when $g_-\Psi(g_-)>\gamma$. This turns part (a) into a closed test at the two edges. The same positivity is $1+\Omega>0$, which matches the monotonicity of the Schur function.

Part (b) reduces to delocalization. Let $u$ be uniform, and let $F$ be any map from $\hat M$ and independent coins to the unit sphere. Put $\bar F=R^\top F(R\hat MR^\top)$ with $R$ Haar. The law of $(u,\hat M)$ is invariant under $(u,\hat M)\mapsto(Qu,Q\hat MQ^\top)$, so $\mathbb E\langle\bar F,u\rangle^2=\mathbb E\langle F,u\rangle^2$. Let $e_k$ be an eigenbasis of $\hat M$ with simple spectrum, and $J=I_d-2\sum_{k\in S}e_ke_k^\top$. Then $J\hat MJ=\hat M$, so $\bar F\overset d=J\bar F$ given $\hat M$, the coefficients $\langle\bar F,e_k\rangle$ are conditionally uncorrelated, and
$$\mathbb E\langle F,u\rangle^2=\mathbb E\Big[\sum_kp_k(\hat M)\,\mathbb E[\langle e_k,u\rangle^2\mid\hat M]\Big]\le\mathbb E\Big[\max_k\mathbb E[\langle e_k,u\rangle^2\mid\hat M]\Big],$$
with $p_k\ge0$ and $\sum_kp_k=1$ (proven). A degenerate eigenspace $E$ enters through $\|P_Eu\|^2/\dim E$ by the same argument with $O(E)$. Equality holds for the eigenvector that maximizes its conditional overlap. So in mean-square overlap no function of $\hat M$ beats the best of its eigenvectors, and Markov's inequality carries this to the success criterion $\Pr[|\langle\hat u,u\rangle|\ge\epsilon]$. Part (b) is then the statement that non-outlier eigenvectors have vanishing overlap, which is bulk delocalization (heuristic). Two outliers cannot be combined usefully. Their relative sign is invisible to the class, as the reflection $J$ shows.

ch-b-in-order-versus-exact (does not block). As written, (b) says "beats in order" and then states an exact limit for $p_{\hat M}(\epsilon)/d$. The second does not follow from the first. The reduction above gives the exact form in mean-square overlap, so (b) should be stated in that form.

A small scope note. With $\varsigma=0$ and an atom of $W$ at zero, the lower edge exists only for $\gamma<\Pr[W>0]$, not for every $\gamma\in(0,1)$. The band law has $\Pr[W>0]=0.69$.

Verdict ACCEPT.

### prop-signed-weight-update-pca

(a) holds, since $M_g=M_{g_+}-M_{g_-}$ and each part has the form of the theorem (proven). (b) holds line by line (proven). Each part, at failure probability $\vartheta/2$, gives $\|\hat M_{g_\pm}-M_{g_\pm}\|\le\rho_\pm c_0^2(A+\varsigma)^2\eta$, because $\lambda_{\max}K_\pm^2\le\rho_\pm c_0^2(A+\varsigma)^2$. The condition gives $\eta\le3|\gamma_g|/(8c_0^2(A+\varsigma)^2(\rho_++\rho_-))$, with the same $\sqrt{18/128}=\frac38$ as before. The bound $\eta\le\frac34$ follows from $|\gamma_g|\le\lambda_{\max}(M_{g_+})+\lambda_{\max}(M_{g_-})\le2(A^2+\varsigma^2)\le2(A+\varsigma)^2$ and $\rho_++\rho_-\ge1$. Step 4 indeed uses only the form $\alpha I_d+\gamma uu^\top$ with real $\alpha$. For $g\ge0$, $\rho_+=\lambda_+/\lambda_-$ recovers the theorem with $\log(4/\vartheta)$.

The remark is right in order (heuristic). $\gamma_g\approx2\kappa_2/\|\psi\|_\infty$, and the bracket ratio is of order $\sup\psi^2\sigma^4$ over its mean.

Verdict ACCEPT.

### prop-measured-meets-proven-full-observer

(a). My own quadrature on a grid of the same size gives $\mathrm{KL}=0.2477$ on the atom, 0.0813 from the continuous part and $\kappa_{\mathrm{KL}}=0.1599$, against the builder's 0.2468 and 0.1596 (empirical, numerical). With 0.1599 the lower sides are $T\ge46.33$ at $d=200$ and $T\ge98.44$ at $d=400$, so the stated 46.4 and 98.6 overstate them slightly. The ratios become 86.3 and 81.3. (b). The success probability of the declared estimator is the same at every $u$, because its weights are functions of norms and its eigenvector is equivariant, so runs at $u=e_1$ give the Bayes success (proven). The one-sided Clopper and Pearson band for 40 of 40 at level 0.05 is $0.05^{1/40}=0.928$ (proven). I replicated the witness in 40 fresh runs at $d=200$ and $T=20d$ with another seed. All 40 succeeded, with mean overlap 0.73 and minimum 0.66, and 17 of 40 succeeded at $T=10d$ against the builder's 22 (empirical). (c) follows.

ch-quadrature-is-not-a-proof (does not block). The lower side is called proven, and it rests on a numerical value of $\kappa_{\mathrm{KL}}$ that two quadratures put 0.2 percent apart. For a proven witness with explicit constants, state a certified upper value, for instance $\kappa_{\mathrm{KL}}\le0.161$ with a stated quadrature error bound, and recompute the ratio, which stays below 87.

ch-declaration-order (does not block). The band is sound only if the weight and $T=20d$ were fixed before any run was seen, including the descriptive runs at $10d$ and $15d$. The file should state the order. My replication was run after the builder had declared the estimator, so it certifies the band at $d=200$ whatever the order was.

This is the first price in the space known within a stated factor at a measured dimension. The factor is large, and the file says why.

Verdict ACCEPT.

### prop-trainer-accuracy-caps-release-attacker

See section 3. Parts (a), (b) and (c) are true and elementary. The remark is false in the proposition's own setting (ch-chosen-query-scaling, blocks). The reading of Halil omits the floor on success that the register proves for his example, and the proposition's own part (b) instantiates it (ch-third-reading, does not block). Part (c) describes nature, not a release, which the statement should say.

Verdict REVISE.

### def-statistic-learner-class

The two replaced sentences are right. The added remark is right, and its "heuristic" label covers the band-law evidence. With the closure under subsampling, which a learner that may discard observations would have, $p_S$ would again be the left end of an interval. The definition should say which class it means.

Verdict ACCEPT.

### prop-full-clipping-optimum-filter

The renaming is right. Part (e) holds (proven, given the tail bound). $d-2\sqrt{dx}=d/4$ at $x=9d/64$, so $\Pr[\|X\|^2\le d/4]\le e^{-9d/64}$. Off that event $\|\psi\|=W\|X\|>w_{\min}\sqrt d/2>C$. A union bound over $T$ records and the triangle inequality through the normalized streams, which have one law by (b), give $2Te^{-9d/64}$. The bound is far below one at any measured dimension, $e^{-28}$ at $d=200$.

Verdict ACCEPT.

## 5. The space after round 02

The space now holds one price known within a stated factor at a measured dimension, an exact filter from training, and a conjecture on the linear class that has a closed outlier test and whose optimality part reduces to bulk delocalization. That is a theory of a statistic class against the full observer in Halil's sense of a subclass. Its beautiful object is the pair of the Cauchy transform and the $L^2$ norm of one signed measure of the label law.

What keeps me from signing it is one false remark and one misreading, both in the proposition that answers Halil's sentence on the trainer. The false remark blocks, and a hypothesis on the query norm repairs it. The misreading does not block, but it is the sentence most likely to reach Halil, and it reverses the direction the register already proves for his example. The sample-priced comparison with a trained release remains unstated, and it can stand with an honest status.

## 6. Challenges

| Challenge | Object | Blocks | Status |
| --- | --- | --- | --- |
| ch-chosen-query-scaling | prop-trainer-accuracy-caps-release-attacker, remark | yes | new |
| ch-third-reading | prop-trainer-accuracy-caps-release-attacker | no | new |
| ch-b-in-order-versus-exact | conj-linear-class-reads-cauchy-transform (b) | no | new |
| ch-quadrature-is-not-a-proof | prop-measured-meets-proven-full-observer (a) | no | new |
| ch-declaration-order | prop-measured-meets-proven-full-observer (b) | no | new |
| ch-no-trainer-price | the aims | no | answered in part |
| ch-vacuous-at-measured-dimension | the linear class | no | open for that class only |
| ch-finite-ratio-profile, ch-precision-reads-past-the-statistic, ch-mean-parameter, ch-signed-weights, ch-normalization-not-clipping | | | resolved |

## Satisfied

SATISFIED no

One blocking challenge remains, ch-chosen-query-scaling, in the remark that carries the space's answer on the trainer. The reading of Halil's sentence that goes with it omits the floor on success already proven for his example, and a further round that repairs both would change that verdict.

## Verdicts

```text
VERDICT conj-linear-class-reads-cauchy-transform ACCEPT
VERDICT prop-signed-weight-update-pca ACCEPT
VERDICT prop-measured-meets-proven-full-observer ACCEPT
VERDICT prop-trainer-accuracy-caps-release-attacker REVISE
VERDICT def-statistic-learner-class ACCEPT
VERDICT prop-full-clipping-optimum-filter ACCEPT
BLOCKING 1
```
