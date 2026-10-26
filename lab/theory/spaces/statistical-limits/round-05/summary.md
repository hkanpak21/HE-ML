# Summary of round 05 of statistical-limits

Builder: the space session of `statistical-limits`, 2026-10-25. Discussant: sol
(`discussant-sol.md`, 58,631 tokens), sol again, argon quota. Argon is out of quota until about
2026-10-27 13:30, after this milestone's last round. The space stops here. This is its last round
of milestone 2, and it ends with BLOCKING 0.

## What changed

The round deleted the false sentence of `thm-blind-orbit-price` (`ch-orbit-fixed-gauge`) and
applied four nonblocking corrections. Sol found no remaining false statement and accepted all seven
objects.

## Slugs accepted

With BLOCKING 0, each of these has verdict ACCEPT in this round:

- `thm-blind-orbit-price`
- `thm-train-access-price-frontier`
- `thm-same-units-gap-gaussian-mechanism`
- `thm-blind-orbit-limit`
- `prop-whitening-orbit-sample-price`
- `prop-relu-client-second-moment-identifies-weights`
- `fact-subgaussian-sample-covariance-concentration`

## Challenges open

None.

## For the registers

New results for `sink/formalizing/results.md`, all unchecked by a person. Each is stated in
`round-03/builder.md`, with the changes recorded in `round-04/builder.md` and `round-05/builder.md`.

| slug | kind | status | oracle |
| --- | --- | --- | --- |
| `thm-blind-orbit-limit` | theorem | proven | holds-without-oracle |
| `prop-whitening-orbit-sample-price` | proposition | proven | holds-without-oracle |
| `thm-blind-orbit-price` | theorem | proven | holds-without-oracle |
| `prop-relu-client-second-moment-identifies-weights` | proposition | proven | holds-without-oracle |
| `thm-train-access-price-frontier` | theorem | proven | needs-oracle (Train access) |
| `thm-same-units-gap-gaussian-mechanism` | theorem | proven | needs-oracle (Train access) |

New fact: `fact-subgaussian-sample-covariance-concentration`, see `round-03/summary.md`.

Problems.

- `prob-train-access-collapses-sample-price`: solved in the regime $\rho=n^{-a}$, $0<a<\frac12$.
  The sample price falls from $\Theta(n^{2-2a})$ to $\Theta(n^{2a})$ with $\Theta(n^{2-2a})$ Train
  calls. For constant $\rho$, sol's round-03 attack needs no reference sample.
- `prob-same-units-matched-budget-separation`: partial.
  `thm-same-units-gap-gaussian-mechanism` gives a natural procedure where the attacker's price, in
  samples plus Train calls, exceeds the trainer's by the factor $\Theta(1+n\rho^2)$, attained by an
  efficient attack. The placeholder `conj-same-units-gap` (low-rank adapter, gradient-trained
  membership adversaries) stays open.
- `prob-relu-blind-inversion-sample-price` and `prob-label-direction-same-units`, as posed in
  `round-03/summary.md`.

New search rows. None in milestone 2.

For Halil, from this milestone. Whether the Gaussian mechanism with noise calibrated to the
population covariance is the right model when the attacker has Train access. Under it, Train calls
leak the covariance, which is what collapses the sample price.
