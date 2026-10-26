---
key: BRV26
title: Statistically Undetectable Backdoors in Deep Neural Networks
authors: Andrej Bogdanov and Alon Rosen and Neekon Vafa
venue: ICML 2026
venue_evidence: PMLR page found by the mapping agent, held copy is the anonymous ICLR 2026 submission
year: 2026
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "statistically undetectable backdoor proven, collision resistance conditional on Assumption 2"
prov: full-read
---

# BRV26, Statistically Undetectable Backdoors in Deep Neural Networks

Read on 2026-10-25 by the hard-problem-mappings space session from the held copy
(the anonymous ICLR 2026 submission, so the numbering is that copy's): Section 1
(results, interpretations, the cryptographic assumptions paragraph), Appendix A
(Definitions 4 and 5, Assumptions 1 and 2), Appendix B (Theorems 2 and 3, the
statements), Appendix C (Definition 6, Lemma 4, the construction of C.3, Theorems 5,
6 and 7, Corollary 3). The proofs of Appendix B and the experiments were read by
their headings only.

## Claim

A trainer can plant, in any network whose first layer is a frozen compressing
Gaussian matrix followed by bilipschitz layers on integer inputs, a backdoor that
is undetectable even statistically and gives it colliding inputs exponentially
closer, in the compression ratio, than any efficient adversary can find, because
finding near-kernel integer vectors of a Gaussian matrix is a lattice-hard problem.

## Method

Definition 5: the symmetric bounded perceptron (SBP) problem asks, on
$A\sim N(0,1)^{m\times n}$, for $x\in[-B:B]^n\setminus\{0\}$ with
$\lVert Ax\rVert_\infty\le\kappa\sqrt n$. Assumption 2: for p.p.t. algorithms and
$B,n\le\mathrm{poly}(m)$, finding such $x$ with $\lVert Ax\rVert_\infty\le m^{-\varepsilon}$
has negligible probability; the paper says this holds if worst-case lattice
problems are hard, citing Vafa and Vaikuntanathan 2025 and Bogdanov et al. 2025.
Theorem 2: BackdoorMatrix outputs $A$ and a uniform $z\in\{\pm1\}^n$ with
$\lVert Az\rVert_\infty\le O(\sqrt n\,2^{-n/m})$ and $A$ statistically close to
Gaussian, at distance about $\sqrt{m/n}$ up to a logarithm plus $e^{-\Omega(m)}$.
Construction (C.3): the model is $g(Ax)$, the backdoored model uses the planted $A$,
activation adds $z$. Definition 6 asks for $o(1)$ total variation between white-box
descriptions, collisions within $\delta_0$ for activated pairs, and approximate
collision resistance at $\delta_1$ against p.p.t. adversaries. Theorem 5: for
$(\alpha,\beta)$-bilipschitz $g$, $m=n^{\Omega(1)}$, $m=o(n)$, under Assumption 2,
strength $\delta_1/\delta_0=\Omega(\alpha2^{n/m}/(\beta\sqrt n\,m^{1/2+\varepsilon}))$.
Theorem 7 instantiates it for depth-$d$ LeakyReLU networks with condition numbers
at most $\gamma$; Corollary 3 ($m=n^{1/2}$, $d=n^{1/4}$) gives strength $2^{\Omega(m)}$.

## What they measured, and on what

Proofs, and preliminary experiments on Fashion-MNIST (Section 3.1, not read).

## Epistemic status

Proven conditional on Assumption 2, whose reduction to worst-case lattice problems
is cited, not proven in the paper. The statistical undetectability is unconditional.

## The limitation that matters to us

The hard problem sits in the honest Gaussian layer, which is what Halil's rule asks
for, but the attack task it prices is collision finding (invariance adversarial
examples), not a privacy task. A reconstruction mapping does not follow: for a
compressing layer on uniform integer records the record is uniform on its fiber, so
reconstruction is already statistically impossible (my finding, recorded as a dead
end in round 00 of hard-problem-mappings).

## Relationship to this project

Prior art. The one literature mapping whose carrier is the honest randomness of a
standard procedure (`fact-frozen-gaussian-layer-collision-hardness`).

## What we need to consider for our work

It shows that a natural layer yields a collision-resistant function on bounded
integers under a lattice assumption, the kind of finding `CONTEXT.md` says counts.
A privacy mapping from it would need a record law of low entropy on which the
layer is injective yet hard to invert.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/20344_Statistically_Undetectab.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Mapping note: The held PDF is the anonymous ICLR 2026 submission, authors taken from the published ICML 2026 version.
Reading record: 2026-10-25, the hard-problem-mappings space session read the sections named at the top of this note, for lab/theory/spaces/hard-problem-mappings/round-00/builder.md.
