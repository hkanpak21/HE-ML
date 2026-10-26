---
key: ZSWB22
title: Lattice-Based Methods Surpass Sum-of-Squares in Clustering
authors: Ilias Zadik and Min Jae Song and Alexander S. Wein and Joan Bruna
venue: COLT 2022
venue_evidence: wiki /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/zadik-lattice-surpass-sos.md (venue field COLT 2022, no source URL given); first page carries only arXiv:2112.03898v2 (7 Jan 2022)
year: 2022
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: tool
epistemic: "proven, for exactly discrete hidden labels in a Gaussian background"
prov: full-read
---

# ZSWB22, Lattice-Based Methods Surpass Sum-of-Squares in Clustering

Read on 2026-10-25 by the computational-limits space session from the held copy
(arXiv 2112.03898v2): Section 1 to Theorem 1.3, Section 2 (Definitions 2.1 to
2.6, Theorem 2.3, Claim 2.7), Section 3 (Assumption 3.1, Model 3.2, Algorithm 1,
Theorem 3.3 and its intuition) and Section 4 to Corollary 4.4 with Claim 4.5. The
proofs of the appendices and Sections 5 to 7 were read by their headings only.

## Claim

For clustering-type problems with a hidden discrete direction in a Gaussian
background, LLL recovers the hidden integer labels and the direction exactly from
$d+1$ samples in polynomial time, where SoS and low-degree lower bounds suggest
that $\tilde\Theta(d^2)$ samples are needed.

## Method

Assumption 3.1: $\Sigma\succeq0$ is $u$-weakly separable if $\Sigma u=0$ and its other
eigenvalues lie in $[d^{-C},d^C]$. Model 3.2: known spacing $a\in[d^{-c},d^c]$,
arbitrary integer labels $x_i\in[-2^d,2^d]$, a unit $u$, a $u$-weakly separable
$\Sigma$, and samples $z_i\sim N(ax_iu,\Sigma)$. Algorithm 1: with $Z=[z_2\cdots z_{d+1}]$,
compute the dependency $\lambda=(1,-Z^{-1}z_1)$, truncate it to $N=\lceil d^4(\log d)^2\rceil$
bits, run LLL on a $(d+2)$-dimensional integer lattice built from the truncated
$\lambda$ and $M=2^{2d}$, read an integer vector $t_1$, solve $Z^\top u'=at_1$, and
normalize. The labels are recovered from the dependency alone, before $u$.

## What they measured, and on what

Theorem 3.3: with probability $1-e^{-\Omega(d)}$ there is $\epsilon\in\{\pm1\}$ with
$\hat x_i=\epsilon x_i$ for all $i$ and $\hat u=\epsilon u$, in $\mathrm{poly}(d)$ steps.
Claim 2.7: the discrete Gaussian $\nu$ of width 1 on $(1/\gamma)\mathbb Z$ has normalizer
$Z\ge\gamma\sqrt{2\pi}(1-2(1+1/(4\pi\gamma)^2)e^{-2\pi^2\gamma^2})>1$ and tails
$\Pr[|x|\ge t]\le4e^{-t^2/2}$ for $t\ge\gamma$. Model 4.3 (homogeneous CLWE without
noise) reduces to Model 3.2 (Claim 4.5), and Corollary 4.4 solves it with $d+1$
samples for $\gamma=\mathrm{poly}(d)$. Applications to planted sparse vectors and Gaussian
clustering follow in Section 4.

## Epistemic status

Proven. The paper notes that inverse-polynomial noise defeats the method, and that
SQ and low-degree lower bounds remain formally true.

## The limitation that matters to us

The method needs the hidden coordinate to be exactly a multiple of an integer, or
exponentially close to one. The paper states it.

## Relationship to this project

Tool. Algorithm 1 depends on the samples only through a linear dependency, which
an injective linear client preserves, so a seed-blind split-learning server can
run it on representations. This is my reading, used in the computational-limits
aim `conj-sq-sample-games-separate`: the SQ game and the sample game separate on
noiseless pancakes.

## What we need to consider for our work

The seed's price on discrete hidden structure is polynomial against record-level
attackers, whatever the SQ bounds say. Lattice attacks belong in every experiment
on discrete records.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/ZSWB22_LatticeSurpassSOS.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/zadik-lattice-surpass-sos.md`.
Mapping note: The wiki gives the venue without a source.
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-03/builder.md.
