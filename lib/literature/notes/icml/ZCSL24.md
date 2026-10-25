---
key: ZCSL24
title: Verification of Machine Unlearning is Fragile
authors: Binchi Zhang and Zihan Chen and Cong Shen and Jundong Li
venue: ICML 2024
venue_evidence: "first page footer: 'Proceedings of the 41st International Conference on Machine Learning, Vienna, Austria. PMLR 235, 2024'"
year: 2024
type: conference
placed_on: 2026-10-25
placed_by: agent
triage: cite
relation: prior-art
epistemic: "Propositions 4.2 to 4.5 proven under smoothness and Lipschitz assumptions on the loss; the attacks' success against backdoor verification and their utility empirical on MNIST, CIFAR-10 and SVHN"
prov: full-read
---

# ZCSL24, Verification of Machine Unlearning is Fragile

Read by the agent on 2026-10-25 for the theory space `oracle-and-measurement`, from the library
PDF (arXiv 2408.00929v2 of 21 April 2026, 22 pages). Read: §1 to §5, Definition 4.1, Algorithms 1
and 2, Propositions 4.2 to 4.5, Tables 1 and 2, Fig. 4. Not re-derived: the proofs of Appendix A.

## Claim

A model provider who controls the choice of minibatches can produce an unlearning proof that passes
exact replay verification, and can pass backdoor verification too, while its model still carries the
influence of the data it claims to have removed.

## Method

A proof of retraining is the trajectory $\{(w^{(t)}_r,d^{(t)}_r,g^{(t)}_r)\}$ of checkpoints, batches and
update functions. Definition 4.1 calls it valid when each step is reproducible within a threshold
$\varepsilon$ and no batch meets the unlearned set $D_u$. The adversary is the model provider, with full
access to training data, unlearned data and model (§3). Algorithm 1 retrains from scratch but replaces
each unlearned point of the original batch by its nearest same-class neighbour in the retained data, so
the replacement batch induces a gradient close to the original one. Algorithm 2 forges the retraining
proof from the logged training proof, editing only the steps whose batch met $D_u$, in parallel.

## What they measured, and on what

Proposition 4.2: Algorithm 1 returns a valid proof at threshold $\varepsilon=0$. Proposition 4.3: under
bounds $G$ on the gradient, $L_x$ on the mixed derivative and $L$ on the Hessian, the retrained model's
expected squared gradient norm on the full data $D$ is at most a term of order $1/(\gamma T)$ plus terms in
$p_u=1-(1-|D_u|/|D|)^m$ and $C_D$, the largest same-class nearest-neighbour distance. Proposition 4.4:
under step-size conditions Algorithm 2 returns a valid proof at threshold $\varepsilon>0$. Proposition
4.5: Algorithm 1 costs the time $\mathcal T(n)$ of naive retraining, and Algorithm 2 costs
$(p_u/P+(1-p_u)/(mP))\,\mathcal T(n)$ with $P$ parallel processes and batch size $m$. The text calls these
results Theorems 4.2 to 4.5. Experiments on MNIST (MLP), CIFAR-10 (CNN) and SVHN (ResNet), five seeds:
the type II error of backdoor verification is about 0.997 for Algorithm 1, as for honest retraining, and
near zero for Algorithm 2 (Table 2), and the forging method's verification errors sit below practical
thresholds (Fig. 4).

## Epistemic status

Proven, Propositions 4.2 to 4.5, under the stated assumptions on the loss. Empirical, the backdoor and
utility results. The naming of the propositions as theorems in the text is a labelling slip, not a
blurring of status.

## The limitation that matters to us

Found by us. The verifier replays the batches the prover reports and never fixes them. The prover's
freedom is the batch order, which in the HE-ML oracle model is part of the seed. Algorithm 1 costs one
run, as much as honest retraining, so a meter in runs or in work cannot separate the attack from honest
work.

## Relationship to this project

Prior art for the replay audit `thm-replay-audit-steer` of the HE-ML oracle theory, which derives the seed,
batch order included, from a random oracle on a committed dataset. That removes the batch choice this
attack needs, and the theorem's steering bound then applies.

## What we need to consider for our work

Recorded as the verified form of fact-unlearning-verification-fragile in
`lab/theory/spaces/oracle-and-measurement/round-00/builder.md`. The register's pointer, Proposition 4.5
with Algorithms 1 and 2, is right for the cost claim. Proposition 4.2 is the pointer for passing exact
replay.

## Provenance

Copied on 2026-10-25 from FORMAL_SECURITY raw/ZCSL24_UnlearningVerificationFragile.pdf for the formalizing line, see `sink/formalizing/README.md`. Title and authors were read from the first page.
Reading notes: FORMAL_SECURITY `/Users/a90/Documents/RESEARCH/FORMAL_SECURITY/wiki/sources/unlearning-verification-fragile.md`.
Mapping note: Held PDF is arXiv v2 dated 21 Apr 2026.
