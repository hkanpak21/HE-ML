---
model: gemini-4-argon-medium
discussant: argon
date: 2026-10-25
prompt: lab/theory/spaces/computational-limits/round-02/prompt-argon.md
---

This review judges the seven resubmitted objects of Round 02 in `computational-limits` against the ten blocking challenges and the non-blocking remarks of Round 01, checking whether each statement holds as written, whether the proofs and literature citations hold line by line, and whether the objects satisfy the constraints of `CONTEXT.md`.

### Summary of Round 02 Repairs

The repairs close **all ten blocking challenges** of Round 01 (proven). Specifically:
1. **Pancake covariance sign (`ch-pancake-covariance-sign`)**: Fixed in `fact-clwe-hardness` and carried cleanly through `prop-sq-blind-reconstruction-bound` and `prop-fine-reconstruction-to-hclwe` (proven).
2. **Keyed encoding confidence (`ch-keyed-encoding-confidence`)**: Restored in `fact-ideal-keyed-encoding-weak-learner` (proven).
3. **SQ price range and witness uniformity (`ch-sq-price-range`, `ch-witness-uniformity`)**: Fixed with explicit margins, packing bounds, query subtraction, and dimension-independent witness parameters in `prop-sq-blind-reconstruction-bound` (proven).
4. **Initial observation schedule (`ch-initial-observation-schedule`)**: Restricted to representations computed under $W_0$ in `thm-blind-split-seed-separation` (proven).
5. **Conjecture scope (`ch-conjecture-erasing-client`, `ch-conjecture-whitening-scope`)**: Fixed via exact polynomial-time seed-known recoverability and isotropic $A$ in `conj-seed-price-is-ngca-price` (proven).
6. **Randomized single-index SQ bound (`ch-label-sq-self-correlation`, `ch-label-sq-code-overlap`, `ch-label-sq-auxiliary-budget`)**: Fixed in `prop-sq-label-relevant-reconstruction-bound` by assuming $I_{\chi^2}[P]<\infty$ for the diagonal bound, restoring the square root in DPLB24 Lemma E.3, and fixing $r, P, c_0$ independently of $d$ (proven).

The two wording corrections noted by the builder for `def-seed-blind-reconstruction-game` and `thm-reconstruction-from-conditional-mean` also close the non-blocking remarks from Round 01 (proven).

---

### Judgement of Objects by Slug

#### 1. `fact-clwe-hardness`: homogeneous CLWE is a hard hidden-direction law

* **Statement & Proof**: **True as written; proof holds line by line (proven).**
  In Bruna, Regev, Song, and Tang (STOC 2021, `BRST21`), Lemma 7.2 analyzes the noiseless distribution $D_{(1/\gamma')\mathbb Z}$ along $w$. Because the Fourier transform of $x^2 \rho(x)$ is $\big(\frac{1}{2\pi} - y^2\big)\rho(y)$, Poisson summation gives
  $$\mathbb E_{x \sim D_{(1/\gamma')\mathbb Z}}[x^2] = \frac{1}{2\pi}\frac{\sum_{k \in \mathbb Z} (1 - 2\pi (\gamma' k)^2)\rho(\gamma' k)}{\sum_{k \in \mathbb Z} \rho(\gamma' k)} = \frac{1}{2\pi} - \Delta',$$
  where $\Delta' = \frac{\sum_{k \in \mathbb Z} (\gamma' k)^2 \rho(\gamma' k)}{\rho(\gamma' \mathbb Z)} \ge 0$. Since $\rho(\gamma' \mathbb Z) = 1 + 2\sum_{k \ge 1} e^{-\pi \gamma'^2 k^2} \ge 1$ and for $\gamma' \ge 1$ the $k=1,-1$ terms contribute $2\gamma'^2 e^{-\pi \gamma'^2}$ while $\sum_{|k|\ge 2} (\gamma' k)^2 e^{-\pi \gamma'^2 k^2} < 0.01 \gamma'^2 e^{-\pi \gamma'^2}$, we have $\Delta' \in [0, 2.01 \gamma'^2 e^{-\pi \gamma'^2}]$.
  In Corollary 7.3, $H_{w,\beta,\gamma}$ is obtained by adding independent Gaussian noise of parameter $\beta/\gamma$ to $H_{w,\gamma'}$ with $\gamma' = \sqrt{\beta^2+\gamma^2}$ and rescaling by $1/\sqrt{1+(\beta/\gamma)^2}$. Along $w$, the variance becomes
  $$\frac{\frac{1}{2\pi} - \Delta' + \frac{(\beta/\gamma)^2}{2\pi}}{1+(\beta/\gamma)^2} = \frac{1}{2\pi} - \Delta, \quad \Delta = \frac{\Delta'}{1+(\beta/\gamma)^2} \le \Delta'.$$
  Since $\beta \in (0,1)$ and $\gamma \ge 1$, $\gamma^2 \le \gamma'^2 \le \gamma^2+1$, so $\Delta \le 2.01(\gamma^2+1)e^{-\pi \gamma^2} \le 3(\gamma^2+1)e^{-\pi \gamma^2}$. On $w^\perp$, the variance rescales identically to $1/(2\pi)$. This closes `ch-pancake-covariance-sign` (proven).
* **Hypotheses & Literature**: Exact match to BRST21 Definitions 2.19, 2.21, Claim 2.22, Corollary 4.2, Lemma 7.2, Corollary 7.3, Theorem 7.5, and Corollary 9.4 (proven).
* **Constraints of `CONTEXT.md`**: Borrowed literature fact used as a hardness tool; compliant (proven).

---

#### 2. `fact-ideal-keyed-encoding-weak-learner`: an ideal keyed encoding hands over the concept

* **Statement**: **True as written (proven).**
  Restoring the $(1/2-\varepsilon, \delta)$ balanced-error guarantee with constants $0 < \varepsilon, \delta < 1/2$ matches Definition 2 and Theorem 1 of Chen, Goldwasser, Jovanović, Machado, Miyazaki, andTessaro (ICML 2021 / arXiv, `CGJMMT21`), where the learner achieves balanced error at most $1/2 - \varepsilon$ with probability at least $1 - \delta$ over the training sample and encoding key, and the oracle-aided predictor runs in time $\mathrm{poly}(m, 1/\varepsilon, 1/\delta, 1/\tau)$. This closes `ch-keyed-encoding-confidence` (proven).
* **Constraints of `CONTEXT.md`**: Compliant literature fact (proven).

---

#### 3. `prop-sq-blind-reconstruction-bound`: SQ price of blind reconstruction from a frozen client

* **Statement & Proof**: **True as written; proof holds line by line (proven).**
  * *Common reduction and covariance check*: Under the corrected covariance from `fact-clwe-hardness`, $\sigma_{\max} = (2\pi)^{-1/2}$ and $\sigma_a = (2\pi)^{-1/2}(1 - 2\pi\Delta)^{1/2}$. For $\gamma \ge 2$, $2\pi\Delta \le 6\pi(5)e^{-4\pi} \approx 3.29 \times 10^{-4} < 4 \times 10^{-4}$, so $\sigma_a \ge \sqrt{0.9996}(2\pi)^{-1/2} \ge 0.9998(2\pi)^{-1/2}$ (proven).
  * *Truncation and tolerance*: With $L = \sqrt{\log(48\gamma d/(\beta c_0))}$ and $\tau_1 = c_0/(9\sqrt{2\pi}L\sqrt d)$, the oracle error per coordinate is $L\tau_1 = \frac{c_0}{9\sqrt{2\pi}\sqrt d} \le \frac{c_0\sigma_a}{8\sqrt d}$ (since $1/9 < 0.9998/8$). For the tail error, the density ratio bound $H_w(u)/D_0(u) \le 3\gamma/\beta$ holds because $\sum_{k\in\mathbb Z} e^{-\pi(k-\gamma t)^2/\beta^2} \le 1 + 2\sum_{k\ge 1} e^{-\pi k^2} < 2.1$ for $\beta \in (0,1)$ and the normalization constant of $H_w$ is $\frac{\beta}{\sqrt{\beta^2+\gamma^2}}\sum_{k\in\mathbb Z} e^{-\pi k^2/(\beta^2+\gamma^2)} \ge \frac{\beta}{\sqrt{2}\gamma}$, giving ratio $\le 2.1\sqrt{2}\gamma/\beta < 3\gamma/\beta$. Since $\mathbb E_{g \sim D_0}[|g|\mathbf 1\{|g|>L\}] = 2\int_L^\infty t e^{-\pi t^2}\,dt = \frac{1}{\pi}e^{-\pi L^2}$ and $e^{-\pi L^2} \le e^{-L^2} = \frac{\beta c_0}{48\gamma d}$, the tail error is at most $\frac{3\gamma}{\beta}\frac{1}{\pi}\frac{\beta c_0}{48\gamma d} = \frac{c_0}{16\pi d} \le \frac{c_0\sigma_a}{8\sqrt d}$. Combining both errors over $d$ coordinates yields $\|\hat w - \bar w\|_2 \le c_0\sigma_a/4$, $|\langle \hat w, w\rangle| \ge 3c_0\sigma_a/4$, $\|\hat w\|_2 \le \sigma_{\max} + c_0\sigma_a/4 \le 2\sigma_{\max}$, and $|\langle \hat s, w\rangle| \ge \frac{3c_0\sigma_a}{8\sigma_{\max}} \ge 0.3749 c_0 > c_0/3 = \rho_0$ (proven).
  * *Part (a) FGRVX17 search bound*: With $M = \lfloor e^{d\alpha_0^2/4}/2\rfloor$, a standard union bound over $\binom{M}{2}$ pairs of uniform unit vectors gives pairwise overlap at most $\alpha_0 = \rho_0^2/2$. By the Gram matrix bound, any unit vector $\hat s$ has $\langle \hat s, w\rangle \ge \rho_0$ for at most $\frac{1}{\rho_0^2 - \alpha_0} = \frac{2}{\rho_0^2}$ directions in $U$, and hence $|\langle \hat s, w\rangle| \ge \rho_0$ for at most $4/\rho_0^2$ directions. Under the explicit hypothesis $M \ge 48/\rho_0^2$, the fraction solved by one output is $\eta \le \frac{4}{\rho_0^2 M} \le \frac{1}{12}$, so with $\alpha = 2/3$, $\frac{\alpha-\eta}{1-\eta} \ge \frac{2/3 - 1/12}{1} = \frac{7}{12} \ge \frac{1}{2}$ and $|D_{\hat s}| \ge (1-\eta)M \ge \frac{11}{12}M$.
    By BRST21 Proposition 8.3 (applicable since $\gamma \ge 2$ and $\alpha_0 \le 1/18$ imply $\gamma^2(1-\alpha_0^2) \ge 4(1 - 1/324) > 1$), $D_{\hat s}$ is $(\gamma_c, \beta_c)$-correlated relative to $D_0$ with $\gamma_c = 8e^{-\pi\gamma^2(1-\alpha_0^2)}$ and $\beta_c = 2(\gamma/\beta)^2$.
    Mapping $[-1,1]$-valued queries to $[0,1]$ via $(h+1)/2$ scales expectations and tolerances by $1/2$, so $\mathrm{VSTAT}(t)$ with $t = 1/\tau_*^2$ has error at most $\max\{1/t, \frac{1}{2\sqrt t}\} = \frac{\tau_*}{2}$ on $[0,1]$, hence $\tau_*$ on $[-1,1]$. Setting $1/(3\bar\gamma) = 1/\tau_*^2$ gives $\bar\gamma = \tau_*^2/3$. Under the explicit hypothesis $\tau_*^2 \ge 6\gamma_c$, $\gamma' = \bar\gamma - \gamma_c \ge \tau_*^2/6 > 0$. By Feldman, Grigorescu, Reyzin, Vempala, and Xiao (J. ACM 2017, `FGRVX17`), Lemma 3.10 and Theorem 3.2:
    $$q + d \ge \frac{\alpha - \eta}{1 - \eta}|D_{\hat s}|\frac{\gamma'}{\beta_c - \gamma_c} \ge \frac{1}{2} \cdot \frac{11}{12}M \cdot \frac{\tau_*^2/6}{2(\gamma/\beta)^2} = \frac{11}{288}M\frac{\tau_*^2\beta^2}{\gamma^2}.$$
    Subtracting $d$ yields the exact stated bound, closing `ch-sq-price-range` (proven).
  * *Part (b) DKRS23 testing bound*: Fixing $j^* \ge 1, \kappa > 0, c_0, \sigma$ independently of $d$ guarantees that the sub-Gaussian tail of $A$ controls the $j^*$-th Hermite polynomial $h_{j^*}$ uniformly in $d$, making $M_h$ and $\tau_2 = \rho_1^{j^*}\kappa/(4M_h)$ positive constants independent of $d$. Under the null $\gamma_d$, $\langle \hat s, u\rangle \sim \gamma_1$ conditionally on $\hat s$, so $\mathbb E[h_{j^*}(\langle \hat s, u\rangle)] = 0$ because $j^* \ge 1$. Under $P^A_w$, Ornstein–Uhlenbeck gives $|\mathbb E[h_{j^*}(\langle \hat s, u\rangle)]| \ge \rho_1^{j^*}\kappa$. Since $\tau_1 = \tilde\Theta(d^{-1/2})$ and $\tau_2 = \Theta(1)$ both strictly exceed the DKRS23 Theorem 1.5 tolerance threshold $O_k(d^{-((1-\lambda)/4-c)k}) + (1+o(1))\nu$ when $((1-\lambda)/4-c)k > 1/2$ and $\nu \le d^{-((1-\lambda)/4-c)k}$ for large $d$, the minimum tolerance $\min(\tau, \tau_1, \tau_2)$ can only fall below the threshold if $\tau$ does. This closes `ch-witness-uniformity` (proven).
* **Constraints of `CONTEXT.md`**: Standard rotation-invariant initialization, no cryptographic plug-in, explicit SQ prices. Part (b) applies to general moment-matched distributions $P^A_v$, avoiding the pancake distribution entirely (proven).

---

#### 4. `prop-fine-reconstruction-to-hclwe`: polynomial-time price of fine blind reconstruction

* **Statement & Proof**: **True as written; proof holds line by line (proven).**
  * *Step 2 covariance and least-squares conditioning*: With $\Sigma \succeq \frac{1-2\pi\Delta}{2\pi}I_d \succeq \frac{0.99}{2\pi}I_d$ for $\gamma \ge 2$, the whitened rows $\Sigma^{-1/2}u_j$ are isotropic and sub-Gaussian with norm $O(\sqrt{\log(\gamma/\beta)})$. By BRST21 Lemma 7.4 (Vershynin Theorem 4.6.1), for $N = Cd\log^2(\gamma/\beta)$ with $C$ sufficiently large, $\|\frac{1}{N}\Sigma^{-1/2}U^\top U\Sigma^{-1/2} - I_d\|_{\rm op} \le 1/2$ with probability $1 - e^{-\Omega(d)}$. Hence $U^\top U \succeq \frac{N}{2}\Sigma \succeq \frac{0.99 N}{4\pi}I_d$, which gives $\sigma_{\min}(U) \ge \sqrt{\frac{0.99 N}{4\pi}} = \frac{\sqrt{0.99}}{\sqrt{2}}\frac{\sqrt N}{\sqrt{2\pi}} \ge \frac{\sqrt N}{2\sqrt{2\pi}}$ (since $\sqrt{0.99/2} \approx 0.7035 > 0.5$).
  * *Step 3 angle and phase test*: From $\|e\|_\infty \le c_1/\gamma$, $\|e\|_2 \le \sqrt N c_1/\gamma$, so $\|\hat w - \kappa w\|_2 \le \frac{\|e\|_2}{\sigma_{\min}(U)} \le 2\sqrt{2\pi}c_1/\gamma = \frac{1}{8\pi\gamma}$. Since $\|w\|_2 = 1$, the angle $\theta$ between $\hat w$ and $\kappa w$ satisfies $\sin\theta \le \|\hat w - \kappa w\|_2 \le \frac{1}{8\pi\gamma}$, and for $\theta \in [0, \pi/2]$, $\theta \le \frac{\pi}{2}\sin\theta \le \frac{1}{16\gamma} \le \frac{1}{8\gamma}$. In Step 3, $\mathbb E|a| \le \sqrt{\mathbb E[a^2]} = \sigma_a \le (2\pi)^{-1/2}$ under the deficit bound. With $\mathrm{poly}(d)$-bit arithmetic and polynomial protocol cost $T_{\rm run}$, numerical rounding perturbs $S$ by $2^{-\mathrm{poly}(d)} \ll \kappa_\beta/6$. This closes `ch-pancake-covariance-sign` and the non-blocking precision remark (proven).
* **Constraints of `CONTEXT.md`**: Reduces fine reconstruction of a standard learning protocol (frozen or trained) to hCLWE without modifying the training procedure (proven).

---

#### 5. `thm-blind-split-seed-separation`: the seed separates attackers for pancake records

* **Statement & Proof**: **True as written; proof holds line by line (proven).**
  * *Part (i)*: By Lei, Jalal, Dhillon, and Dimakis (NeurIPS 2019, `LJDD19`), Theorem 3, an expansive ReLU layer with i.i.d. Gaussian weights $m \ge 2.1 d$ is injective on a fixed input $x_i$ independent of $W_0$ with probability $1 - e^{-\Omega(d)}$ and invertible via a linear program. Restricting the trained-client claim to representations computed under the initial weights $W_0$ (the first batch, or all records if an initial forward pass occurs before the first gradient step) ensures $W_0$ is known to the seed-known attacker and independent of $x_i$. This closes `ch-initial-observation-schedule` (proven). The heuristic remark on tracking subsequent weights is properly labeled heuristic (heuristic).
  * *Parts (ii) and (iii)*: Follow immediately from `prop-sq-blind-reconstruction-bound` part (a) and `prop-fine-reconstruction-to-hclwe`, keeping $\tau_* = \min(\tau, \tau_1)$ and polynomial protocol cost (proven).
* **Constraints of `CONTEXT.md`**: As noted in Round 01, the client architecture and training rule are completely standard (Gaussian initialization, ReLU, SGD), so there is no cryptographic plug-in in the learner (proven). However, the hardness is imported via the pancake record distribution $H_{v,\beta,\gamma}$ rather than arising from an intrinsic learning task on natural data (heuristic). The builder properly flags this as Decision 3 for Halil while pairing it with the moment-matched SQ bound of `prop-sq-blind-reconstruction-bound` part (b).

---

#### 6. `conj-seed-price-is-ngca-price`: the seed is worth the NGCA price of the record law

* **Statement & Settled Parts**: **Well posed; settled parts are true as written (proven).**
  * *Recoverability (`ch-conjecture-erasing-client`)*: Restricting to frozen clients of $\mathcal P_{O(d)}$ for which a polynomial-time seed-known attacker recovers every record exactly from $(\omega, z_i)$ with probability $1-o(1)$ excludes erasing clients (e.g., $W_0 = 0$ or constant $\psi_\theta$) while keeping full-column-rank linear layers and expansive Gaussian ReLU layers (by LJDD19 Theorem 3). This closes `ch-conjecture-erasing-client` (proven).
  * *Isotropy and upper inclusion (`ch-conjecture-whitening-scope`)*: Requiring $A$ to have mean $0$ and covariance $I_r$ makes $P^A_V$ isotropic ($\mathbb E[x]=0$, $\mathbb E[xx^\top]=I_d$). By `lem-whitening-gives-rotated-records`, for a frozen full-column-rank linear client, population whitening yields $u_i = T(z_i - \mathbb E[z]) = R x_i$ with $R \sim \mathrm{Haar}(O(d))$ independent of the records. Thus $u_i \sim P^A_{RV}$ where $RV$ is a uniformly random orthonormal frame, and $(RV)^\top u_i = V^\top R^\top R x_i = V^\top x_i$ recovers the target coordinates directly without any unknown scaling factor. This closes `ch-conjecture-whitening-scope` (proven).
* **Open status**: The open parts (blind inversion of expansive ReLU layers without the seed, finite-sample whitening perturbation in NGCA, coarse polynomial-time lattice hardness) are cleanly delineated and testable by experiment (open).

---

#### 7. `prop-sq-label-relevant-reconstruction-bound`: what the labels cost the server

* **Statement & Proof**: **True as written; proof holds line by line (proven).**
  * *Reduction to single-index search*: As established in Round 01, simulating the frozen linear client $W'$ on single-index samples $(x', y)$ and asking $d$ coordinate queries clipped at $L = \sqrt{2\ln(16\sqrt d/c_0)}$ at $\mathrm{VSTAT}(n_1)$ with $n_1 = \lceil 64 L^2 d/c_0^2\rceil$ produces a unit vector $\hat s$ with $|\hat s \cdot w^*| \ge \rho = 3c_0/5$ with probability at least $2/3$, using $Q = q + d \le d^r$ calls to $\mathrm{VSTAT}(n')$, $n' = \max(n, n_1)$ (proven).
  * *Diagonal correlation (`ch-label-sq-self-correlation`)*: In Damian, Pillaud-Vivien, Lee, and Bruna (COLT 2024, `DPLB24`), Lemma 2.3 and the proof of Lemma E.2 expand the $\chi^2$-inner product relative to the null $\gamma_d \otimes P_y$ as $\chi_0(P_w, P_{w'}) = \sum_{k \ge k^*} \lambda_k^2 (w \cdot w')^k$. On the diagonal ($w = w'$), $\chi_0(P_w, P_w) = \sum_{k \ge k^*} \lambda_k^2 = I_{\chi^2}[P]$. By explicitly assuming $I_{\chi^2}[P] < \infty$ and setting $\beta_c = I_{\chi^2}[P]$, the diagonal correlation hypothesis of FGRVX17 Lemma 3.10 holds rigorously without relying on DPLB24's unstated $\beta_c = 1$ step. This closes `ch-label-sq-self-correlation` (proven).
  * *Code overlap and Gram bound (`ch-label-sq-code-overlap`)*: DPLB24 Lemma E.3 constructs a packing of $m \le d^{d^{1/4}}$ unit vectors with pairwise overlap $|w_i \cdot w_j| \le \epsilon = \sqrt{C\log_d(m)^2/d} = \sqrt{C}\log_d(m)/\sqrt d$. Off the diagonal, since $\lambda_k^2 \le 1$ (or bounded by $\beta_c$; in fact $\lambda_k = \|\mathbb E[h_k(Z)\mid Y]\|_{L^2(P_y)} \le \|h_k(Z)\|_{L^2(\gamma_1)} = 1$ by Jensen's inequality), $|\chi_0(P_{w_i}, P_{w_j})| \le \lambda_{k^*}^2 \epsilon^{k^*} + \frac{\epsilon^{k^*+1}}{1-\epsilon} \le 2\lambda_{k^*}^2 \epsilon^{k^*} =: \gamma_c$ whenever $\epsilon \le 1/2$ and $\lambda_{k^*}^2 \ge 2\epsilon$.
    With $P, c_0, r$ fixed independently of $d$, assume for contradiction (or case split) that $n' < d^{k^*/2}$. Choosing $m = \lceil 12 Q n' \beta_c/\alpha'\rceil + \lceil 4/\rho^2\rceil$ with $Q \le d^r$ makes $m = O(d^{r + k^*/2})$, so $\log_d(m) \le \ell(P, c_0, r)$ is bounded by a constant for large $d$, and $m \le d^{d^{1/4}}$ holds for large $d$. Consequently, $\epsilon = \sqrt{C}\ell/\sqrt d = O(d^{-1/2})$. For large $d$, this satisfies $\epsilon \le \rho^2/2$ (enabling the Gram bound that any $\hat s$ solves at most $4/\rho^2$ code directions), $\epsilon \le 1/2$, $\lambda_{k^*}^2 \ge 2\epsilon$, and $\eta = 4/(\rho^2 m) \to 0$ so $\alpha' = (\alpha-\eta)/(1-\eta) \ge 1/2$.
    Plugging $m - 4/\rho^2 \ge 12 Q n' \beta_c/\alpha'$ into FGRVX17 Theorem 3.2:
    $$Q \ge \alpha'(m - 4/\rho^2)\frac{1/(3n') - \gamma_c}{\beta_c - \gamma_c} \ge 12 Q n' \beta_c \frac{1/(3n') - \gamma_c}{\beta_c} = 12 Q n'(1/(3n') - \gamma_c),$$
    which simplifies to $1/(3n') - \gamma_c \le 1/(12n')$, i.e., $n' \ge \frac{1}{4\gamma_c} = \frac{d^{k^*/2}}{8\lambda_{k^*}^2 C^{k^*/2}\ell^{k^*}}$. This closes `ch-label-sq-code-overlap` (proven).
  * *Auxiliary budget (`ch-label-sq-auxiliary-budget`)*: Because $P, c_0, r$ are fixed independently of $d$, the lower bound is $n' \ge c(P, c_0, r)d^{k^*/2}$ with no growing $r$ degradation. Since $k^* \ge 3$ and $n_1 = \Theta(d\log d) = o(d^{3/2})$, for large $d$ we have $n_1 < c(P, c_0, r)d^{k^*/2}$, which forces $n = n' \ge c(P, c_0, r)d^{k^*/2}$. This closes `ch-label-sq-auxiliary-budget` (proven).
  * *Part (b) denoiser*: Applying DPLB24's Algorithm 1 to $(Tz_i, T_P(y_i)) = (Rx_i, T_P(y_i))$ with the denoiser $T_P$ of DPLB24 Theorem 4.1 matches the literature theorem's exact specification (proven).
* **Constraints of `CONTEXT.md`**: Directly prices reconstruction of the label-relevant feature in learning units (the generative exponent $k^*$), without any cryptographic or artificial distribution (inputs are standard Gaussian $x \sim \gamma_d$) (proven).

## Verdicts

```text
VERDICT fact-clwe-hardness ACCEPT
VERDICT fact-ideal-keyed-encoding-weak-learner ACCEPT
VERDICT prop-sq-blind-reconstruction-bound ACCEPT
VERDICT prop-fine-reconstruction-to-hclwe ACCEPT
VERDICT thm-blind-split-seed-separation ACCEPT
VERDICT conj-seed-price-is-ngca-price ACCEPT
VERDICT prop-sq-label-relevant-reconstruction-bound ACCEPT
BLOCKING 0
```
