---
model: gemini-4-argon-medium
discussant: argon
date: 2026-10-25
prompt: lab/theory/spaces/statistical-limits/round-02/prompt-argon.md
---

Proven. All three blocking challenges from round 01—`ch-urn-common-nuisance`, `ch-profile-comparator`, and `ch-label-policy-optimum`—as well as the nonblocking challenges and domain remarks are closed by the revisions in `round-02/builder.md`. No blocking challenges remain (`BLOCKING 0`), and `lem-scrambled-seed-urn`, `thm-shadow-run-price-finite-views`, and `prop-reconstruction-label-sandwich` now have complete proofs.

### Revised objects

1. `fact-reconstruction-query-lower-bounds`

Proven. The statement is true as written, its hypotheses match Mukherjee and Lokam (arXiv:2303.16372v6), and `ch-reconstruction-majority-omission` is closed by separating the unnumbered target-independent majority-adversary bound for $\varepsilon \ge 0.042$ in Appendix B.5 from the unestablished unrestricted Theorem 10 and Corollary 12. Heuristic. It remains non-trivial borrowed background pricing reconstruction in observed trainer outputs under differential privacy.

2. `def-uniform-security-profile`

Proven. `ch-profile-comparator` is closed. Splitting Property 1 into (i) general interfaces where $g_{\{\iota\},\mathsf P}(\beta)=0$ holds as an infimum by fidelity-preserving internal simulation of reference draws and auxiliary Train calls, (ii) complete plain-channel observations where $\mathrm{TV}(P_0,P_1)$ and $\mathrm D^\top_1(K)$ are attained at zero budget, and (iii) finite query channels under the bottom oracle where $\mathrm{Adv}^{\mathrm{bb}}(q_E)$ is attained by hard-wiring an optimal depth-$q_E$ strategy tree makes every clause true as written. Heuristic. As a definition it is supporting notation, made non-trivial under `CONTEXT.md` by the theorems that compute it.

3. `lem-scrambled-seed-urn`

Proven. `ch-urn-common-nuisance` and `ch-urn-filtration` are closed; the statement is true as written and the proof is now complete rather than a sketch.
- **Common nuisance hypothesis:** Fixing the learning setting $\Lambda$ (common seed law $\mu$ on $[0,1)^2$ with uniform second coordinate, evaluation map, model injection $s$, and deterministic response map at all $x \neq x_0$) across $p$ and $p'$ ensures that all steps outside new-cell Train calls at $x_0$ share identical conditional kernels.
- **Augmented history and Bayes' rule:** Recording the numerical seed $\rho=(\rho_a,\rho_b)$ of every Train call in $h_j$ at call time—even when the adversary holds the seed only by name—makes subsequent `Open` calls measurable functions of $h_j$ and makes the sequence of queried cells $c_1,\dots,c_{t-1}$ and current cell $c$ at $x_0$ determined by $h$. Because all other answers in $h$ have conditional laws independent of $\pi$, Bayes' rule over the finite group of $M!$ bijections yields the uniform posterior over bijections satisfying $\lambda(\pi(c_r))=u_r$ for $r<t$, giving the exact without-replacement law $q_h(v)=(Mp(v)-r_v)/(M-t+1)$ and $\mathrm{TV}(q_h,p)\le (t-1)/(M-t+1)$ at a new cell.
- **Hybrid bound along paths:** Applying the one-step triangle and data-processing inequality $\mathrm{TV}(P_{1:j},Q_{1:j})\le \mathrm{TV}(P_{1:j-1},Q_{1:j-1}) + \mathbb E_{P_{1:j-1}}[\mathrm{TV}(K_j(\cdot\mid h),K'_j(\cdot\mid h))]$ and summing over $j\le L$ integrates the kernel discrepancy along paths of the scrambled run $P$. Along every path, at most $N$ steps are new-cell Train calls at $x_0$, and the $t$-th such call contributes at most $(t-1)/(M-N)$, bounding every finite prefix by $N^2/(2(M-N))$ without measurable coupling selection.
- **Passage to infinite sequences:** Padding after termination embeds the run into a countable product of standard Borel spaces. Because cylinder sets form a generating algebra, total variation on the product $\sigma$-algebra equals $\sup_L \mathrm{TV}(P_{1:L},Q_{1:L})$, and the martingale/filtration supremum for KL divergence on increasing prefix $\sigma$-algebras (plus data processing to the transcript) gives $\mathrm{KL}(\tilde T_v\|\tilde T'_v)\le N\,\mathrm{KL}(p\|p')$.
- **Non-triviality:** Proven. Uses a genuinely uniform finite permutation rather than a cryptographic plug-in, meeting `CONTEXT.md`.

4. `thm-shadow-run-price-finite-views`

Proven. `ch-shadow-small-budgets`, `ch-shadow-policy-quantifiers`, and `ch-label-policy-optimum` are closed; all six parts (a)–(f) are true as written with complete proofs.
- **Part (a):** Requiring $N\ge 2$ guarantees $n=\lfloor N/2\rfloor \ge 1$ so the empirical laws $\hat p_0,\hat p_1$ are well-defined, while the trivial constant-$0$ rule covers $N\le 1$ with gap $\mathrm{TV}(P_0,P_1)\le 1$.
- **Part (b):** Stating the lower bound separately per policy resolves the quantifier ambiguity: for each policy, the primitive-tape decision-rule reduction and sign-flipping hypercube family produce a hard instance $\mathsf L^\sigma$ for any given $N$-call adversary of that policy, and because $\mathsf L^\sigma$ ignores the seed, the top optimum equals $\mathrm{TV}(P_0,P_1)$ on this family.
- **Part (c):** Now rests on the complete proof of `lem-scrambled-seed-urn`, whose shared-setting hypothesis $\Lambda$ holds across $\sigma$ because $\mathsf L(x_1;\rho)=s(Q_1(\rho_a))$ and all responses outside $\{x_0,x_1\}$ are independent of $\sigma$.
- **Part (f):** Distinguishing the query set size $|U|$ from the query allowance $q_E\le |U|$ and restricting variation to a fixed subset $U_0\subseteq U$ of size $q_E$ makes $\mathrm{Adv}^{\mathrm{bb}}(q_E)$ equal to the marginal table total variation on $U_0$ under the bottom oracle (giving the $k=C^{q_E}$ bounds), while under the top oracle the optimum is properly identified as the top divergence of the restricted table channel on $U_0$, attained in one call by part (d). Open. Whether the factor of order $\ln|U|/(C-1)+1$ between the general upper bound and the $U_0$-supported lower bound is necessary remains open, as stated.
- **Non-triviality:** Heuristic. Prices distinguishing in training runs without cryptographic assumptions and separates bottom from top oracle access under deterministic kernels, with finite-view divergences realizable in experiment.

### Carried objects

5. `fact-hsu-membership-sample-gap`: Proven. Stating $\rho>0$ as in HSU25 Definition 2.4 keeps the borrowed statement and its non-trivial sample-complexity baseline acceptable.
6. `fact-hsu-gap-prices-covariance`: Proven. Adding the domain conditions $\rho>0$, $n\ge 4$, and $m\ge 2$ of HSU25 Theorem 4.1 keeps the borrowed statement acceptable.
7. `fact-yeom-dp-bounds-membership-advantage`: Proven. Unchanged and acceptable as borrowed differential-privacy baseline.
8. `fact-yeom-generalization-error-gives-advantage`: Proven. Unchanged and acceptable as borrowed one-evaluation membership advantage identity.
9. `fact-lira-priced-in-training-runs`: Empirical. Unchanged and acceptable as borrowed empirical training-run benchmark.
10. `fact-lira-low-fpr-yeom-game`: Proven. Adding the positive-probability condition for the conditional OUT draw and the probability-one exclusion condition for equivalence with Yeom's game keeps the borrowed statement acceptable.
11. `fact-balle-reconstruction-robustness-definition`: Proven. Unchanged and acceptable as borrowed statistical reconstruction definition.
12. `fact-balle-dp-bounds-reconstruction`: Proven. Unchanged and acceptable as borrowed Rényi and pure DP reconstruction bounds.
13. `fact-dinur-nissim-reconstruction-thresholds`: Proven. Explicitly stating $\delta>0$ in DN03 Theorem 5 keeps the borrowed statement acceptable.
14. `fact-pac-privacy-mutual-information-bound`: Proven. Unchanged and acceptable with the prior-guess monotonicity condition.
15. `fact-pac-privacy-gaussian-release-bound`: Proven. Noting that this is the deterministic specialization alongside XD23 §4.2/Corollary 2 and retaining $\|M(X)\|_2\le r$ for Theorem 4 keeps the borrowed statement acceptable.
16. `fact-zhao-accuracy-forces-attribute-leakage`: Proven. Unchanged and acceptable with positive-probability attribute groups.
17. `fact-balle-reconnn-priced-in-shadow-runs`: Empirical. Scoping "needs the initialization" to the tested ReconNN attack and noting that initialization is part of the seed when training shuffles closes `ch-reconnn-seed-interpretation` and keeps the fact acceptable.
18. `prop-reconstruction-label-sandwich`: Proven. Separating $S^\star=\bar\kappa$ from the tail argument for $S^\star>\bar\kappa$ and distinguishing head-error removal above $\bar\kappa-\varepsilon^\star$ from residual information $I(X;Z\mid Y)$ above $\bar\kappa$ closes `ch-sandwich-endpoint-details` and keeps the proposition acceptable as a complete proof.

## Verdicts

```text
VERDICT fact-reconstruction-query-lower-bounds ACCEPT
VERDICT def-uniform-security-profile ACCEPT
VERDICT lem-scrambled-seed-urn ACCEPT
VERDICT thm-shadow-run-price-finite-views ACCEPT
VERDICT fact-hsu-membership-sample-gap ACCEPT
VERDICT fact-hsu-gap-prices-covariance ACCEPT
VERDICT fact-yeom-dp-bounds-membership-advantage ACCEPT
VERDICT fact-yeom-generalization-error-gives-advantage ACCEPT
VERDICT fact-lira-priced-in-training-runs ACCEPT
VERDICT fact-lira-low-fpr-yeom-game ACCEPT
VERDICT fact-balle-reconstruction-robustness-definition ACCEPT
VERDICT fact-balle-dp-bounds-reconstruction ACCEPT
VERDICT fact-dinur-nissim-reconstruction-thresholds ACCEPT
VERDICT fact-pac-privacy-mutual-information-bound ACCEPT
VERDICT fact-pac-privacy-gaussian-release-bound ACCEPT
VERDICT fact-zhao-accuracy-forces-attribute-leakage ACCEPT
VERDICT fact-balle-reconnn-priced-in-shadow-runs ACCEPT
VERDICT prop-reconstruction-label-sandwich ACCEPT
BLOCKING 0
```
