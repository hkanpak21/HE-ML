---
key: FGRVX17
title: Statistical Algorithms and a Lower Bound for Detecting Planted Cliques
authors: Vitaly Feldman and Elena Grigorescu and Lev Reyzin and Santosh S. Vempala and Ying Xiao
venue: J. ACM 64(2)
venue_evidence: /Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/feldman-statistical-algorithms-planted-clique.md
year: 2017
type: journal
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: tool
epistemic: "proven, unconditional for statistical algorithms against an adversarial oracle, and against the honest 1-STAT in Theorem 2.10"
prov: full-read
---

# FGRVX17, Statistical Algorithms and a Lower Bound for Detecting Planted Cliques

Read on 2026-10-25 by the computational-limits space session from the held copy
(arXiv 1201.1214v6): the introduction, Section 2 in full, Section 3.1 (Theorem
3.2 and its proof opening), Section 3.1.1 (Theorem 3.7), Section 3.2 (Definitions
3.8 and 3.9, Lemma 3.10, Corollaries 3.11 and 3.12), the statements of Section
3.3 (Theorems 3.13 and 3.17), and Section 5.1 (Lemma 5.2, Theorems 5.3 and 5.4).
Sections 4, 5.2 and 6 and the appendix were read by their headings only.

## Claim

Statistical algorithms, those that see a distribution only through expectations
of chosen functions, need $n^{\Omega(\log n)}$ queries of tolerance near the
sampling scale to detect a planted $k$-biclique of size $k\le n^{1/2-\delta}$ in
its distributional form, and 1-bit sampling algorithms need $\Omega(n^2/k^2)$
fresh samples, both unconditionally.

## Method

The paper defines the distributional planted $k$-biclique problem (Problem 1.1):
$D_S$ on $\{0,1\}^n$ is uniform with probability $1-k/n$ and has the coordinates
of $S$ set to $1$ with probability $k/n$, so one sample is the adjacency row of a
left vertex of a bipartite graph. It defines three oracles: STAT($\tau$)
(Definition 2.2, any answer within $\tau$), VSTAT($t$) (Definition 2.3, any answer
within $\max\{1/t,\sqrt{p(1-p)/t}\}$ of the mean $p$, which tracks the binomial
spread of $t$ samples), and 1-STAT (Definition 2.4, a Boolean function evaluated
on one fresh sample, the honest oracle). The lower-bound tool is the statistical
dimension with average correlation (Definitions 2.5, 2.6 and 3.1), built from the
pairwise correlations $\chi_D(D_1,D_2)=\langle D_1/D-1,D_2/D-1\rangle_D$. Theorem
3.2: if $\mathrm{SDA}(Z,\bar\gamma,\eta)=d$, a randomized SQ algorithm that solves
$Z$ with probability $\alpha>\eta$ needs $(\alpha-\eta)d/(1-\eta)$ calls to
VSTAT($1/(3\bar\gamma)$). Theorem 3.7 is the decision version, $(2\alpha-1)d$
queries. Lemma 3.10 and Corollary 3.12 pass from pairwise correlations bounded by
$\gamma$ off the diagonal and $\beta$ on it to the dimension. Theorem 3.13
simulates $m$ calls to 1-STAT by $m$ calls to VSTAT($m/\delta^2$) at a loss
$\delta$ in success, and Theorem 3.17 turns SDA bounds into 1-STAT bounds. The
adversary is the oracle, which answers with the null expectation whenever that is
a valid answer.

## What they measured, and on what

A proof. Lemma 5.2 bounds the average correlation of large sets of planted
distributions, Theorem 5.3 gives $\mathrm{SDA}(Z,2^{\ell+1}k^2/n^2,1/\binom nk)\ge
n^{2\ell\delta}/3$ for $\ell\le k$ and $\delta\ge1/\log n$, and with
$\ell=\log r-1$ this yields Theorem 2.9: for any constant $\delta>0$,
$k\le n^{1/2-\delta}$ and $r>0$, solving the problem with probability $2/3$ needs
$n^{\Omega(\log r)}$ queries to VSTAT($n^2/(rk^2)$), no polynomial-time
statistical algorithm succeeds with VSTAT($o(n^2/k^2)$), and $n^{\Omega(\log n)}$
queries to VSTAT($n^{2-\delta}/k^2$) are needed, for search and for testing
against $U$. Theorem 5.4 is the randomized decision form with success
$1/2+1/t$. Theorem 2.10: any 1-bit sampling algorithm that tells $U$ from every
$D_S$ with probability $2/3$ needs $\Omega(n^2/k^2)$ calls. Upper bounds in
Section 2.4: $n$ queries $h_i(x)=x_i$ to VSTAT($16n^2/k^2$), tolerance $k/(4n)$,
recover $S$, and $n^{O(\log n)}$ queries to VSTAT($25n/k$) recover it for
$k\ge\log n$. Appendix A shows the average-case bipartite problem equals the
distributional one with $n$ samples.

## Epistemic status

Proven, unconditionally, for statistical algorithms. The claim that most natural
algorithms are statistical is heuristic, argued in the introduction with the
exception of Gaussian elimination. The lower bounds against STAT and VSTAT
quantify over an adversarial oracle. Only Theorem 2.10 is against an honest
oracle, and it needs fresh samples for every call.

## The limitation that matters to us

The bound is about the worst valid oracle, so it says nothing about a learner
that meets a particular oracle such as exact or sample-averaged answers, and it
is about a law of independent rows, not about statistical access to the rows of
one fixed graph. This is my finding, applied in the round-00 judgement of the
FORMAL_SECURITY proof note. The paper states the oracle quantifier in its
definitions and the sample connection in Appendix A.

## Relationship to this project

Prior art and tool. It supplies the statistical-dimension machinery that every
SQ bound in the computational-limits space uses (Theorem 3.2, Corollary 3.12),
and the planted-structure bound that the proof note tried to lift.

## What we need to consider for our work

An SQ bound on a learner passes to anything computed from the learner's output
(post-processing), which is the residue of the proof note. An SQ bound on an
attacker binds only attackers that are statistical, and real attackers meet one
oracle. Search lower bounds for weak recovery come from Corollary 3.12 with
pairwise correlation bounds such as BRST21 Proposition 8.3. The held copy has no
Theorem 1.1 of the form $q\tau^2\ge\Omega(n^{2\delta})$ quoted by the proof note.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/FGRVX17_SQLowerBoundPC.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/feldman-statistical-algorithms-planted-clique.md`.
Mapping note: Held PDF is arXiv v6 (15 Aug 2016). Wiki gives the conference version STOC 2013, which would give FGRVX13.
Reading record: 2026-10-25, the computational-limits space session read the sections named at the top of this note, for lab/theory/spaces/computational-limits/round-00/builder.md.
Reading record: 2026-10-25, the hard-problem-mappings space session read Section 3.1 (Definition 3.1, Theorem 3.2), Theorem 3.7 with its proof (the decision version), Section 3.2 (Definitions 3.8 and 3.9, Lemma 3.10, Corollaries 3.11 and 3.12), and the statements of Theorems 3.13, 3.16, 3.17 and 3.18, for lab/theory/spaces/hard-problem-mappings/round-01/builder.md.
