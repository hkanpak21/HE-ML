---
model: gemini-4-argon-medium
discussant: argon
date: 2026-10-25
prompt: lab/theory/spaces/oracle-and-measurement/round-02/prompt-argon.md
---

Proven. Round 02 closes all seven blocking challenges of [discussant-astra.md](file:///Users/a90/Documents/RESEARCH/HE-ML/lab/theory/spaces/oracle-and-measurement/round-01/discussant-astra.md) and presents eight objects in [builder.md](file:///Users/a90/Documents/RESEARCH/HE-ML/lab/theory/spaces/oracle-and-measurement/round-02/builder.md) that hold as written with zero blocking challenges.

### Closure of Round 01 Blocking Challenges

- **`ch-seed-enumeration-conditions`**: Closed (proven). The revised `fact-small-seed-space-breaks-dp` explicitly requires exact integration of all remaining randomness for exact marginal laws, a single joint seed decoder $\hat s(Y)=s$ across both hypotheses for exact top access, and proves the $\mathrm D^\top_1-2e$ advantage bound when $\Pr[\hat s(Y)\neq s]\le e$.
- **`ch-known-covariance-noise-range`**: Closed (proven). `fact-hsu-membership-sample-gap` now states the complete dimension threshold $d\gtrsim n+n^2\rho^2+n^2/m$, attributes the matching known-covariance attack to Dwork, Smith, Steinke, Ullman and Vadhan (FOCS 2015), and separates bounded $\rho$ (order $n^2$ at $m=2$) from growing $\rho$ (order $n^2\rho^2$).
- **`ch-forging-strict-cost`**: Closed (proven). `fact-unlearning-verification-fragile` distinguishes parallel time under $P$ processes from single-process work $p_u+(1-p_u)/m$, notes equality to $1$ at $P=m=1$, and restricts strict savings to $P\ge 2$ or ($m\ge 2$ and $p_u<1$).
- **`ch-meter-domain-and-equivalence`**: Closed (proven). `def-seed-access-modes` replaces division by the multiplicative inequality $N_X\inf_{x\in X}\mathsf{work}(x)\le C$ and adds the corpus-size coordinate $\mathsf{size}(x)$ so `prop-drawn-mode-is-fs-oracle` matches `def:cost`.
- **`ch-profile-adaptive-shadow-cost`**: Closed (proven). `prop-profile-run-coordinate` (b) separates two-phase families ($k_i$ shadow runs per trial) from general adaptive families ($2k_i$ shadow runs across two independent executions).
- **`ch-paired-discordance-baseline`**: Closed (proven). The paired-trial remark in `prop-profile-run-coordinate` gives the exact variance $p_0(1-p_0)+p_1(1-p_1)-2\,\mathrm{Cov}(T_0,T_1)$ and requires $\mathrm{Cov}(T_0,T_1)>0$ for variance reduction.
- **`ch-one-sided-twin-asymmetry`**: Closed (proven). `thm-exact-twin-price` restricts the base-input lower bound in (a) and (b) to $\theta_{\mathrm{ex}}$ and $\theta_{\mathrm{tv}}$, states the one-sided bound at the numerator input $x_1$, and records the four-base-call counterexample as part (c).

### Line-by-Line Verifications

1. **`thm-exact-twin-price` part (c), base-input counterexample, and part (a) shift construction** (proven). In part (c), at $\varepsilon=1$, $\alpha=0.05$, $\epsilon_{\mathrm{acc}}=0.01$, $\alpha'=0$, let $a=\Pr[W_0=0]$ and $b=\Pr[W_1=0]$. If $a\ge 1/e$ and $b\ge 0.99$, then for every measurable $E$, $P_0(E)\ge a\,\mathcal N(0,\sigma^2I_d)(E)$ and $P_1(E)\le b\,\mathcal N(0,\sigma^2I_d)(E)+(1-b)$, so $P_1(E)-eP_0(E)\le (b-ea)\mathcal N(0,\sigma^2I_d)(E)+1-b\le 0.01$ since $b-ea\le 1-1=0$; thus $\theta_{\mathrm{hs}}\le 0.01$. Whenever $\theta_{\mathrm{hs}}>0.01$, either $a<1/e$, making $\Pr[\hat t=0.01]\le a^4<e^{-4}\approx 0.0183<\alpha$, or $b<0.99$, making $\Pr[\hat t=0.01]\le b^{368}<0.99^{368}\approx 0.0248<\alpha$. At $\mathsf L^\circ$, $a=b=1$, so $\hat t=0.01$ with $N_0=4<298.1$. In part (a), perturbing $x_1$ on $S_B$ by $s\mathbf e$ leaves $P_0$ and $P_1$ identical on $\mathcal R\setminus S_B$. Conditional on $\rho\in S_B$ (mass $m/M$), the release law is $Q_B$ under $H_0$ and $Q_B(\cdot-s\mathbf e)$ under $H_1$. Because any law on $\mathbb R^d$ is tight, $\mathrm{TV}(Q_B,Q_B(\cdot-s\mathbf e))\to 1$ as $s\to\infty$, and for $E_s=\{y:\langle y,\mathbf e\rangle>s/2\}$, $Q_B(E_s-s\mathbf e)=Q_B(\langle y,\mathbf e\rangle>-s/2)\to 1$ while $e^\varepsilon Q_B(E_s)\to 0$. Since $\binom{M}{m}$ is finite at fixed $M$, a single $s_M$ drives both divergences above $\frac12(p+\epsilon_{\mathrm{acc}})>\epsilon_{\mathrm{acc}}$ uniformly over all $B$.
2. **`prop-profile-run-coordinate` (b), the two kinds of trial** (proven). For a two-phase family, the shadow call sequence and seeds are fixed before the challenge, so $S$ is independent of the two procedure executions $(V_0,V_1)$; conditioning on $S$ and taking expectation yields $\mathbb E[D]=\mathbb E_S[\Pr[\mathcal A_{k_i}(S,V_1)=1\mid S]-\Pr[\mathcal A_{k_i}(S,V_0)=1\mid S]]=\mathrm{Adv}(\mathcal A_{k_i})$ at cost $k_i$ shadow runs. For a general family, running two complete, independent executions under $H_1$ and $H_0$ gives $\mathbb E[D]=\mathrm{Adv}(\mathcal A_{k_i})$ by linearity of expectation at cost $2k_i$ shadow runs. In both cases $D\in\{-1,0,1\}$ has range length $2$, so Hoeffding's inequality gives $\Pr[\bar D_i-\mathbb E[D]<-\lambda]\le \exp(-2n_i\lambda^2/4)=\exp(-n_i\lambda^2/2)$, matching $\underline\ell_i=\bar D_i-\sqrt{2\ln(r/\alpha)/n_i}$.
3. **`thm-coupling-free-soundness` (b), exchanged coordinates of $\mathsf{Ex}^\Theta_1$** (proven). When proving the reverse bounds with $\epsilon^\Theta_1(\Delta)$, the roles of $H_0$ and $H_1$ are swapped while keeping $\zeta_t=((\rho^0_t,\xi^0_t),(\rho^1_t,\xi^1_t))\sim\Theta_t$. The hybrid releases $O_t+F^0_t+\mathrm{clip}_\Delta(F^1_t-F^0_t)+Z_t$, where $F^b_t$ is driven by $(\rho^b_t,\xi^b_t)$. Before the first exceedance $\|F^1_t-F^0_t\|>\Delta$, the unclipped release is $O_t+F^1_t+Z_t$, so the hybrid follows the $H_1$ trajectory driven by $(\rho^1_t,\xi^1_t)$ with twin $F^0_t$ driven by $(\rho^0_t,\xi^0_t)$. That is exactly $\mathsf{Ex}^\Theta_1$ with the coordinates of $\Theta_t$ exchanged, required because $\Theta_t$ need not be exchangeable.

### Object Judgments

- **`fact-small-seed-space-breaks-dp`**: True as written, proof and TV triangle-inequality step hold line by line, hypotheses are exact, and it provides measurable empirical context under [CONTEXT.md](file:///Users/a90/Documents/RESEARCH/HE-ML/lab/theory/CONTEXT.md) (proven for the decoding bound; empirical for Nasr et al., USENIX Security 2023, §6.3, Violation 2, Fig. 8). Nothing missed from [NHSBTJCT23.md](file:///Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/usenix-security/NHSBTJCT23.md).
- **`fact-hsu-membership-sample-gap`**: True as written and faithful to Haghifam, Smith and Ullman, FOCS 2026 (to appear), arXiv:2508.19458v1, Definitions 2.1, 2.4, 3.2, Theorems 3.1, 3.3, 4.1, and §1.2.1, with the known-covariance upper bound credited to Dwork et al., FOCS 2015 (proven). One minor detail from [HSU25.md](file:///Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/focs/HSU25.md) not repeated in the summary text is that Definition 3.2 requires the symmetric estimator to lie within Mahalanobis distance $\sqrt{2\rho^2 d}$ of the empirical mean with probability at least $0.99$, which does not affect the statement.
- **`fact-unlearning-verification-fragile`**: True as written and faithful to Zhang, Chen, Shen and Li, ICML 2024, Definition 4.1 and Propositions 4.2–4.5 (proven). A background detail in [ZCSL24.md](file:///Users/a90/Documents/RESEARCH/HE-ML/lib/literature/notes/icml/ZCSL24.md) left implicit in the shorthand "assumptions of Proposition 4.3" is that the loss has $G$-bounded gradients, $L_x$-bounded mixed derivatives, and $L$-Lipschitz Hessian, and the bound depends on the maximum same-class nearest-neighbour distance $C_D$.
- **`def-seed-access-modes`**: Well-posed definition, remark proof holds line by line, hypotheses are exact, and the two-coordinate meter $(\mathsf{work},\mathsf{size})$ prices oracle calls in experimentally measurable training units without cryptographic plug-ins (proven).
- **`prop-drawn-mode-is-fs-oracle`**: True as written, transcript and cost identifications hold line by line under the stated recipe, initialization, and utility restrictions, and it cleanly unifies the two repositories' oracle interfaces (proven).
- **`thm-coupling-free-soundness`**: True as written, all four parts and the five-step composition proof hold line by line with the right marginal, independence, and shared-seed hypotheses, and the exceedance term $\epsilon^\Theta_b(\Delta)$ is directly measurable by experiment (proven).
- **`prop-profile-run-coordinate`**: True as written, the virtual-table simulation in (a), two-phase vs. general trial concentration in (b), and coupled upper band in (c) hold line by line under the right hypotheses, turning the security profile into a concrete experimental protocol (proven).
- **`thm-exact-twin-price`**: True as written, the finite-partition avoidance, dominated convergence, Jensen step, shift extension, record-level convexity, and part (c) counterexample hold line by line, establishing a non-trivial, experimentally realizable oracle certification lower bound and matching upper bound (proven).

## Verdicts

```text
VERDICT fact-small-seed-space-breaks-dp ACCEPT
VERDICT fact-hsu-membership-sample-gap ACCEPT
VERDICT fact-unlearning-verification-fragile ACCEPT
VERDICT def-seed-access-modes ACCEPT
VERDICT prop-drawn-mode-is-fs-oracle ACCEPT
VERDICT thm-coupling-free-soundness ACCEPT
VERDICT prop-profile-run-coordinate ACCEPT
VERDICT thm-exact-twin-price ACCEPT
BLOCKING 0
```
