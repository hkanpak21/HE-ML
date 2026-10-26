# Summary of round 04 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25. Discussant: sol
(`discussant-sol.md`, 94,424 tokens), sol again, argon quota, since argon is out of quota until
about 2026-10-27 13:30.

## What changed

Following Halil's "simplify whenever possible", the builder file was cut to 12k characters. The
round proved `thm-blind-orbit-price`. Against frozen linear clients near an isometry, with no side
data, every seed-blind server has orbit error above $c\,d^2/N$ with probability above one half at
some client, and empirical whitening reaches $(d^2+2d)/N$. So the minimax price of reconstructing
Gaussian records up to rotation is $\Theta(d^2/N)$, and relative accuracy $\epsilon$ costs
$\Theta(d/\epsilon^2)$ representations. The proof turns any reconstruction into an estimate of the
inverse square root $R$ of the representations' covariance, using a $\sqrt2$-Lipschitz bound for the
matrix absolute value. A conditioned Gaussian prior on $R$ then makes the ceiling of
`prop-reconstruction-label-sandwich` a Fano bound. Sol checked all seven steps and the constants. It
found one false sentence in the theorem's other-regime paragraph: "nothing buys the rotation
itself". In this positive-definite client class the population covariance fixes the orientation, so
the records are identifiable in their own coordinates. The rotation stays hidden only under the
orthogonally invariant initialization of `thm-blind-orbit-limit`. The round also restated part (d)
of `thm-train-access-price-frontier` for $\rho=n^{-a}$, and sol accepted it.

## Slugs accepted

Verdict ACCEPT, in a round with BLOCKING 1, so not yet eligible:
`prop-whitening-orbit-sample-price`, `thm-train-access-price-frontier`,
`fact-subgaussian-sample-covariance-concentration`, `thm-blind-orbit-limit`,
`prop-relu-client-second-moment-identifies-weights`, `thm-same-units-gap-gaussian-mechanism`. Verdict
REVISE: `thm-blind-orbit-price`. All seven go to round 05.

## Challenges open

Blocking, answered in `round-05/builder.md`: `ch-orbit-fixed-gauge`. Not blocking:
`ch-whitening-refinement-regime`, `ch-absolute-value-singular-path`, `ch-orbit-prior-conditioning`,
`ch-train-threshold-inversion`.

## For the registers

New results, pending the verdict of round 05: `thm-blind-orbit-price` (theorem, proven,
holds-without-oracle), `thm-train-access-price-frontier` (theorem, proven, needs-oracle, Train
access), `prop-whitening-orbit-sample-price`, `prop-relu-client-second-moment-identifies-weights`,
`thm-blind-orbit-limit` and `thm-same-units-gap-gaussian-mechanism`.

Problems. `prob-train-access-collapses-sample-price`: answered yes in the regime $\rho=n^{-a}$,
$0<a<\frac12$, by `thm-train-access-price-frontier` (d). Outside it, for constant $\rho$, sol's
round-03 attack needs no reference sample. Status partial to solved in that regime.

New search rows. None.
