# Round 01 of learning-attacker-prices, summary

Written by the builder at the start of round 02 and saved verbatim by the integrator from the
builder's reply.

Round 01 conceded the four blocking challenges of round 00 and withdrew P1, conj-optimum-update-variance-price and conj-update-moment-degree-gap. In their place it proposed six objects:
- a setting for the update stream at the square-loss optimum, observed one FedSGD round at a time;
- a definition of a learner class by the statistic it reads;
- a theorem that a spectral estimator weighted by each update's norm recovers the secret, with plain PCA as its constant case;
- a Fano recovery bound with explicit constants;
- an exact filter for per-example normalization at a median-fitting optimum;
- a conjecture pricing the linear class by the mean spike $\beta$ and the variance-profile spike $s$.

The challenger accepted five and revised the conjecture, with BLOCKING 1 and SATISFIED no. It conceded its own round-00 error: the empirical second moment reads the variance profile of its fluctuation, and at $c_2=0$ a profile spike $s>1$ gives plain PCA an outlier as $T/d\to\infty$. It then derived an outlier equation for $\hat M$, from a Schur complement and two deterministic equivalents, in which the linear class reads the transform $\Psi(g)=\mathbb E[W^2T(W)/(1-\sigma^2g)]$. With it, the challenger refuted part (a) of the conjecture. It built a band law with $c_2=0$ and $s=0.756$ on which the bottom eigenvector of $\hat M$ has overlap 0.83 at $T=10d$, predicted 0.833 and measured 0.829 and 0.825 at $d=300$ and $d=600$. On that law the linear class's success is a window in $T$, not a threshold.

Accepted: def-optimum-update-stream, def-statistic-learner-class, thm-norm-weighted-update-pca, prop-update-direction-fano-recovery, prop-full-clipping-optimum-filter.

Revised: conj-update-linear-class-price.

Challenges open at the end of the round:
- ch-finite-ratio-profile (blocks)
- ch-precision-reads-past-the-statistic
- ch-mean-parameter
- ch-signed-weights
- ch-normalization-not-clipping
- ch-no-trainer-price
- ch-vacuous-at-measured-dimension

The challenger records fourteen challenges of round 00 as resolved and the five tied to the withdrawn degree-four aim as moot.

## For the registers

none

No paper was opened and no search was run in round 01. Cited from memory, and candidates for a search row before any enters `facts.md`:
- the generalized Marchenko and Pastur equation of Silverstein and Bai;
- an anisotropic local law for weighted sample covariance matrices;
- the Laurent and Massart tail bounds for chi-square variables, used in round 02;
- Tipping and Bishop (1999) and Lucas, Tucker, Grosse and Norouzi (NeurIPS 2019), already listed in the summary of round 00.
