# Round 05 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25. The last round of milestone 2.
It removes the sentence that round 04 blocked, applies the four nonblocking corrections, and
carries the six objects accepted in round 04. Statements and proofs not restated here are those of
the files named, unchanged.

## Responses to challenges

ch-orbit-fixed-gauge. Accepted. The sentence "nothing buys the rotation itself" is deleted from
`thm-blind-orbit-price`. In its client class the positive-definite $R$ is identifiable from the
covariance of the representations, so the records are identifiable in their own coordinates. The
rotation stays hidden only under the orthogonally invariant initialization of
`thm-blind-orbit-limit`. The numbered statements are unchanged.

ch-whitening-refinement-regime. Accepted. The heuristic refinement $d^2/(4N)$ of
`prop-whitening-orbit-sample-price` is deleted. The exact bound carries the result.

ch-absolute-value-singular-path. Accepted. Step 2 of `thm-blind-orbit-price` now perturbs one
endpoint to be invertible, so the determinant along the segment is a nonzero polynomial with
finitely many roots, integrates between them, and uses continuity of $|\cdot|$ at the roots.

ch-orbit-prior-conditioning. Accepted. In Step 4 the independence, the Gaussian marginals and
$\mathbb E\|\tau\mathrm{Sym}(A)\|_F^2=\tau^2D$ hold before conditioning, and Steps 5 and 6 account
for the conditioning through $\Pr[\mathcal C]$.

ch-train-threshold-inversion. Accepted. Part (d) of `thm-train-access-price-frontier` now solves
the inequality of (b) for $m$. An attack with $m\ge2$ fails when
$m<m^\ast=n^2/((\kappa/c-1)d^\star)$, and $m^\ast=(c/(\kappa-c)+o(1))\,n^{2a}\to\infty$, so padding
an attack with $m<2$ to two samples is allowed for $n$ large.

## Objects

### thm-blind-orbit-price: the statistical price of blind reconstruction up to rotation is order d squared over N

status: sketch

uses: prop-whitening-orbit-sample-price, prop-reconstruction-label-sandwich, fact-subgaussian-sample-covariance-concentration

Setting, Statement (parts 1 and 2), Regime and Experiment as in `round-04/builder.md`. Proof as
there, with Steps 2 and 4 worded as in the responses above.

The other regime, revised. The lower bound holds for unbounded servers and the upper bound is
attained by empirical whitening, so the price is the same for efficient servers. The theorem prices
the records modulo rotation. In this class of positive-definite clients the orientation is
identifiable too. For clients with orthogonally invariant initialization the orientation is hidden
whatever the budget, by `thm-blind-orbit-limit`.

## Objects carried from round 04 with ACCEPT

### prop-whitening-orbit-sample-price: empirical whitening of a frozen affine client returns the affine shape of the records

status: sketch

uses: thm-blind-orbit-limit, lem-whitening-gives-rotated-records

As in `round-04/builder.md`, without the heuristic refinement.

### thm-train-access-price-frontier: Train calls replace population samples in the membership price of noisy mean estimation

status: sketch

uses: fact-hsu-membership-sample-gap, fact-hsu-gap-prices-covariance, fact-subgaussian-sample-covariance-concentration, def-uniform-security-profile

As in `round-04/builder.md`, with the inversion of part (d) stated as in the response above.

### fact-subgaussian-sample-covariance-concentration: the sample covariance of sub-gaussian rows concentrates in operator norm

status: borrowed

uses: none

Unchanged.

### thm-blind-orbit-limit: an unbounded seed-blind server learns the records only up to the symmetry of the record law

status: sketch

uses: def-seed-blind-reconstruction-game, lem-equivariant-view-coupling

Unchanged.

### prop-relu-client-second-moment-identifies-weights: a frozen Gaussian ReLU client is identified up to rotation by its second moment

status: sketch

uses: thm-blind-orbit-limit, fact-lei-random-expansive-layers-invertible

Unchanged from round 04.

### thm-same-units-gap-gaussian-mechanism: in noisy mean estimation the attacker pays a factor one plus n rho squared over the trainer

status: sketch

uses: thm-train-access-price-frontier, fact-hsu-membership-sample-gap

Unchanged from round 04.
