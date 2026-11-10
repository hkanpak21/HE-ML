"""Numerical checks for thm-stealth-uncertainty-cap-linearized, round 01.

Every check prints PASS or FAIL with the numbers behind it. Run with
python3 cap_identities.py. No oracle, no data, no literature.
"""
import warnings
import numpy as np
from scipy.stats import norm, chi2, ncx2

# numpy 2.0 on macOS Accelerate raises spurious matmul RuntimeWarnings on finite inputs.
warnings.filterwarnings("ignore", category=RuntimeWarning)
rng = np.random.default_rng(20261030)


def chain_quantities(H, eta, sigma, T):
    """Honest covariance Sigma_T, response map R_T, and M = Sigma_T^{-1} R_T
    for T steps of theta <- theta - eta (H theta - b + sigma xi)."""
    p = H.shape[0]
    A = np.eye(p) - eta * H
    Sigma = np.zeros((p, p))
    R = np.zeros((p, p))
    Ak = np.eye(p)
    for _ in range(T):
        Sigma += eta**2 * sigma**2 * Ak @ Ak.T
        R += eta * Ak
        Ak = Ak @ A
    M = np.linalg.solve(Sigma, R)
    return Sigma, R, M


def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
    return ok


all_ok = True

# 1. Eigenvalue formulas of round 01 (a) and (b), against the matrix recursion.
p, n, T, eta, sigma = 12, 8, 60, 0.05, 0.7
Phi = rng.standard_normal((n, p))
lam_wd = 0.3
H = Phi.T @ Phi / n + lam_wd * np.eye(p)
Sigma, R, M = chain_quantities(H, eta, sigma, T)
evals, evecs = np.linalg.eigh(H)
Delta = rng.standard_normal(p)
D_T = R @ Delta
mT2_matrix = D_T @ np.linalg.solve(Sigma, D_T)
Dl = evecs.T @ Delta
r = 1 - eta * evals
mT2_formula = np.sum(Dl**2 / sigma**2 * (1 - r**T) * (2 - eta * evals) / (eta * evals * (1 + r**T)))
all_ok &= check("m_T^2 closed form", abs(mT2_matrix - mT2_formula) < 1e-9 * mT2_matrix,
                f"matrix {mT2_matrix:.6f} formula {mT2_formula:.6f}")
mtraj2 = T * Delta @ Delta / sigma**2
mu = evals.min()
all_ok &= check("m_T^2 <= (2/(eta mu T)) m_traj^2", mT2_matrix <= 2 / (eta * mu * T) * mtraj2 + 1e-12,
                f"m_T^2 {mT2_matrix:.4f}  bound {2/(eta*mu*T)*mtraj2:.4f}  eta mu T {eta*mu*T:.3f}")
all_ok &= check("m_T <= m_traj (data processing)", mT2_matrix <= mtraj2 + 1e-12,
                f"{mT2_matrix:.4f} <= {mtraj2:.4f}")
Mev = np.linalg.eigvals(Sigma @ np.linalg.inv(R)).real / (eta * sigma**2)
all_ok &= check("Sigma_T R_T^{-1} eigenvalues in [eta s^2/2, eta s^2]",
                Mev.min() >= 0.5 - 1e-12 and Mev.max() <= 1 + 1e-12,
                f"min {Mev.min():.4f} max {Mev.max():.4f} (in units of eta sigma^2)")
Mev_formula = (1 + r**T) / (1 + r)
all_ok &= check("Sigma_T R_T^{-1} eigenvalue formula (1+r^T)/(1+r)",
                np.allclose(np.sort(Mev), np.sort(Mev_formula)),
                f"max abs diff {np.abs(np.sort(Mev)-np.sort(Mev_formula)).max():.2e}")

# 1b. Supremum of (1+r)/(1+r^T) over r in [0,1) tends to 2 as T grows: non-scalar M.
for TT in (2, 10, 100, 1000):
    rr = np.linspace(0, 0.999999, 200001)
    val = ((1 + rr) / (1 + rr**TT)).max()
    print(f"      sup_r (1+r)/(1+r^T) at T={TT}: {val:.5f}")

# 2. m(delta) and its first order.
for d_ in (0.01, 0.05, 0.1, 0.3):
    m = 2 * norm.ppf((1 + d_) / 2)
    print(f"      m({d_}) = {m:.5f}, sqrt(2 pi) delta = {np.sqrt(2*np.pi)*d_:.5f}, 2 Phi(m/2)-1 = {2*norm.cdf(m/2)-1:.5f}")
all_ok &= check("m(0.1) first order within 0.3 percent",
                abs(2 * norm.ppf(0.55) / (np.sqrt(2 * np.pi) * 0.1) - 1) < 3e-3)

# 3. Kantorovich bound for the feature-direction shift, spectrum ratio 2.
# Fraction reached by Delta = phi(x) is <M g, g> / (|M g| |g|), M in [k0, 2 k0].
worst = 1.0
for _ in range(20000):
    k = rng.integers(2, 6)
    t = rng.uniform(1, 2, size=k)
    t[rng.integers(k)] = 1.0 if rng.random() < 0.5 else 2.0
    g = rng.standard_normal(k)
    frac = (t * g) @ g / (np.linalg.norm(t * g) * np.linalg.norm(g))
    worst = min(worst, frac)
# two-point extreme
for w in np.linspace(0.01, 0.99, 99):
    g = np.array([np.sqrt(w), np.sqrt(1 - w)])
    t = np.array([1.0, 2.0])
    worst = min(worst, (t * g) @ g / (np.linalg.norm(t * g) * np.linalg.norm(g)))
all_ok &= check("feature-direction shift reaches >= 2 sqrt2 / 3 of the cap",
                worst >= 2 * np.sqrt(2) / 3 - 1e-9,
                f"worst found {worst:.6f}, bound {2*np.sqrt(2)/3:.6f}")
# the same for the realized chain operator M on a random instance
g = rng.standard_normal(p)
frac = g @ (M @ g) / (np.linalg.norm(M @ g) * np.linalg.norm(g))
print(f"      realized instance: fraction {frac:.5f}")

# 4. Full-set label poisoner: reachable cap equals explained variance, p > n, lambda = 0 too.
for lam_wd in (0.0, 0.3):
    p, n, T, eta, sigma = 20, 7, 40, 0.04, 1.0
    Phi = rng.standard_normal((n, p))
    H = Phi.T @ Phi / n + lam_wd * np.eye(p)
    Sigma, R, M = chain_quantities(H, eta, sigma, T)
    Sig_half = np.linalg.cholesky(Sigma)  # Sigma = L L^T; use symmetric sqrt instead
    w_, V_ = np.linalg.eigh(Sigma)
    Sig_half = V_ @ np.diag(np.sqrt(w_)) @ V_.T
    Sig_mhalf = V_ @ np.diag(1 / np.sqrt(w_)) @ V_.T
    phix = rng.standard_normal(p)
    g = Sig_half @ phix
    # invariance of the training span under M and Sigma^{1/2}
    Q, _ = np.linalg.qr(Phi.T)  # orthonormal basis of S = span of features
    P_S = Q @ Q.T
    inv_M = np.linalg.norm(P_S @ M @ P_S - M @ P_S)
    inv_Sig = np.linalg.norm(P_S @ Sig_half @ P_S - Sig_half @ P_S)
    all_ok &= check(f"span invariant under M and Sigma^(1/2) (lambda={lam_wd})",
                    inv_M < 1e-9 and inv_Sig < 1e-9, f"{inv_M:.1e} {inv_Sig:.1e}")
    # best fraction over label poisons on all records: max over Delta in S of <R Delta, phi>/(m_T sd)
    # equals |P_S g| / |g| where P_S projects onto Sigma^{-1/2} R S = S.
    W = Sig_mhalf @ R @ Phi.T   # columns span W_S
    Qw, _ = np.linalg.qr(W)
    P_W = Qw @ Qw.T
    best = np.linalg.norm(P_W @ g) / np.linalg.norm(g)
    # explained variance of f(x) by f(X) across seeds
    K = Phi @ Sigma @ Phi.T
    kx = Phi @ Sigma @ phix
    var_x = phix @ Sigma @ phix
    explained = kx @ np.linalg.solve(K, kx)
    rho = np.sqrt(explained / var_x)
    all_ok &= check(f"full-set poisoner reaches sqrt(explained variance) (lambda={lam_wd})",
                    abs(best - rho) < 1e-9, f"best {best:.6f} rho {rho:.6f}")
    # the shift Delta = P_S phi(x) reaches at least 2 sqrt2/3 of that
    Delta_naive = P_S @ phix
    w_naive = Sig_mhalf @ R @ Delta_naive
    frac_naive = (w_naive @ g) / (np.linalg.norm(w_naive) * np.linalg.norm(g))
    all_ok &= check(f"Delta = P_S phi(x) reaches >= (2 sqrt2/3) rho (lambda={lam_wd})",
                    frac_naive >= 2 * np.sqrt(2) / 3 * rho - 1e-9, f"{frac_naive:.6f} vs {2*np.sqrt(2)/3*rho:.6f}")
    # the optimum Delta* = M^{-1} P_S phi(x) attains rho exactly
    Delta_star = np.linalg.solve(M, P_S @ phix)
    w_star = Sig_mhalf @ R @ Delta_star
    frac_star = (w_star @ g) / (np.linalg.norm(w_star) * np.linalg.norm(g))
    all_ok &= check(f"Delta* = M^-1 P_S phi(x) attains rho (lambda={lam_wd})",
                    abs(frac_star - rho) < 1e-9, f"{frac_star:.6f}")
    # kernel-interpolation labels realize Delta = P_S phi(x)
    c = np.linalg.solve(Phi @ Phi.T, Phi @ phix)
    all_ok &= check(f"Phi^T c = P_S phi(x) with c the kernel weights (lambda={lam_wd})",
                    np.linalg.norm(Phi.T @ c - Delta_naive) < 1e-9)
    # conditional variance reading
    cond_var = var_x - explained
    perp = phix - P_S @ phix
    sigma_perp_check = perp @ Sigma @ perp
    all_ok &= check(f"Var(f(x)|f(X)) = off-span variance (lambda={lam_wd})",
                    abs(cond_var - sigma_perp_check) < 1e-9, f"{cond_var:.6f} {sigma_perp_check:.6f}")

# 5. Sub-selection with non-scalar M: the correlation attacker can reach zero while
# the explained-variance formula says 0.316. Planar construction.
Sig2 = np.eye(2)
M2 = np.diag([1.0, 2.0])
s = np.array([1.0, 1.0]) / np.sqrt(2)      # Sigma^{1/2} s, the poisoner's one direction
g = np.array([2.0, -1.0])
a = M2 @ s
frac_actual = abs(a @ g) / (np.linalg.norm(a) * np.linalg.norm(g))
frac_expl = abs(s @ g) / (np.linalg.norm(s) * np.linalg.norm(g))
all_ok &= check("sub-selection counterexample: actual 0, explained-variance 0.316",
                frac_actual < 1e-12 and abs(frac_expl - 1 / np.sqrt(10)) < 1e-9,
                f"actual {frac_actual:.4f} explained {frac_expl:.4f}")

# 6. Secret direction: chi-square of the sphere mixture against the series bound.
def chi2_sphere_mixture(m, d, nsamp=400000):
    # E exp(m^2 Z_1) - 1 with Z_1 one coordinate of a uniform point on S^{d-1}
    z = rng.standard_normal((nsamp, d))
    z1 = z[:, 0] / np.linalg.norm(z, axis=1)
    return np.mean(np.exp(m**2 * z1)) - 1


def chi2_series(m, d, kmax=60):
    t2 = m**4
    tot, term = 0.0, 1.0
    for k in range(1, kmax):
        term *= t2 / (2 * k * (d + 2 * (k - 1)))
        tot += term
    return tot


for d in (10, 100, 1000):
    for m in (1.0, d**0.25, 1.5 * d**0.25):
        exact = chi2_series(m, d)
        mc = chi2_sphere_mixture(m, d, 200000)
        bound = np.exp(m**4 / (2 * d)) - 1
        ok = exact <= bound + 1e-12 and abs(mc - exact) < 0.05 * max(exact, 1e-3) + 2e-3
        all_ok &= check(f"chi2 mixture <= exp(m^4/2d)-1 at d={d}, m={m:.3f}",
                        ok, f"series {exact:.5f} mc {mc:.5f} bound {bound:.5f}")

# stealth radius and detection radius
for d in (100, 1000, 10000):
    delta = 0.05
    m_stealth = (2 * d * np.log(1 + 4 * delta**2))**0.25
    tv_bound = 0.5 * np.sqrt(np.exp(m_stealth**4 / (2 * d)) - 1)
    # chi-square test: W = |Sigma^{-1/2}(theta - mu)|^2, threshold p + m^2/2
    m_det = (64 * d)**0.25
    thr = d + m_det**2 / 2
    type1 = chi2.sf(thr, d)
    type2 = ncx2.cdf(thr, d, m_det**2)
    print(f"      d={d}: stealth radius at delta=0.05 is m <= {m_stealth:.3f} = {m_stealth/d**0.25:.3f} d^(1/4), "
          f"TV bound {tv_bound:.4f}; chi-square test at m = {m_det:.3f} = 2.83 d^(1/4): "
          f"advantage {1-type1-type2:.3f}")
    all_ok &= check(f"TV bound equals delta at the stealth radius (d={d})", abs(tv_bound - delta) < 1e-9)
    all_ok &= check(f"chi-square auditor has advantage >= 1/2 at m=(64d)^(1/4) (d={d})", 1 - type1 - type2 >= 0.5)

# 7. Stationary covariance equals (eta s^2/2) (H (I - eta H/2))^{-1}, and the posterior identity.
p, n, eta, sigma = 6, 30, 0.05, 0.8
Phi = rng.standard_normal((n, p))
s_noise, tau = 0.5, 2.0
lam_wd = s_noise**2 / (n * tau**2)
H = Phi.T @ Phi / n + lam_wd * np.eye(p)
Sigma_inf, R_inf, _ = chain_quantities(H, eta, sigma, 4000)
closed = (eta * sigma**2 / 2) * np.linalg.inv(H @ (np.eye(p) - eta * H / 2))
all_ok &= check("stationary covariance closed form", np.allclose(Sigma_inf, closed, rtol=1e-6, atol=1e-10),
                f"max abs diff {np.abs(Sigma_inf-closed).max():.2e}")
post = (s_noise**2 / n) * np.linalg.inv(H)
ratio_ev = np.linalg.eigvalsh(np.linalg.inv(post) @ closed * (2 * s_noise**2 / (n * eta * sigma**2)))
all_ok &= check("stationary / posterior = (I - eta H/2)^-1 up to the temperature match",
                np.allclose(np.sort(ratio_ev), np.sort(1 / (1 - eta * np.linalg.eigvalsh(H) / 2)), rtol=1e-6),
                f"ratio eigenvalues in [{ratio_ev.min():.4f}, {ratio_ev.max():.4f}]")

# 8. Hoeffding count of clause 22.
a, alpha = 0.05, 0.05
N = int(np.ceil(np.log(2 / alpha) / (2 * a**2)))
all_ok &= check("Hoeffding count ceil(ln(2/alpha)/(2a^2)) at a=alpha=0.05", N == 738, f"N={N}, 2exp(-2Na^2)={2*np.exp(-2*N*a**2):.4f}")

# 9. Response constant bounds by simulation of the coupling on a quadratic.
p, T, eta = 5, 50, 0.1
evH = rng.uniform(0.5, 3.0, size=p)
H = np.diag(evH)
L_, mu_ = evH.max(), evH.min()
eta = 1 / L_
Delta = rng.standard_normal(p)
D = np.zeros(p)
for _ in range(T):
    D = D - eta * (H @ D - Delta)
all_ok &= check("response <= |Delta|/mu under strong convexity", np.linalg.norm(D) <= np.linalg.norm(Delta) / mu_ + 1e-12,
                f"{np.linalg.norm(D):.4f} <= {np.linalg.norm(Delta)/mu_:.4f}")
all_ok &= check("response <= |Delta| ((1+eta L)^T - 1)/L under smoothness",
                np.linalg.norm(D) <= np.linalg.norm(Delta) * ((1 + eta * L_)**T - 1) / L_)

# 10. Learning attacker from N drawn runs: uniform deviation of the correlation objective.
# |J_hat(c) - J(c)| <= 2 eps/(1-eps) when the whitened sample covariance is within eps of I.
k = 6
Kfull = np.eye(k + 1) + 0.6 * np.ones((k + 1, k + 1))
Kh = np.linalg.cholesky(Kfull)
worst_dev, worst_eps = 0.0, 0.0
for N in (50, 200, 1000):
    Z = rng.standard_normal((N, k + 1)) @ Kh.T
    Khat = Z.T @ Z / N
    Kmh = np.linalg.inv(Kh)
    E = Kmh @ Khat @ Kmh.T - np.eye(k + 1)
    eps = np.linalg.norm(E, 2)
    for _ in range(300):
        c = rng.standard_normal(k)
        cz = np.concatenate([c, [0.0]])
        ex = np.zeros(k + 1); ex[-1] = 1.0
        J = (cz @ Kfull @ ex) / np.sqrt((cz @ Kfull @ cz) * (ex @ Kfull @ ex))
        Jh = (cz @ Khat @ ex) / np.sqrt((cz @ Khat @ cz) * (ex @ Khat @ ex))
        worst_dev = max(worst_dev, abs(J - Jh) - 2 * eps / (1 - eps))
    print(f"      N={N}: whitened covariance error eps={eps:.4f}, bound 2eps/(1-eps)={2*eps/(1-eps):.4f}")
all_ok &= check("uniform deviation |J_hat - J| <= 2 eps/(1-eps)", worst_dev <= 1e-12, f"max excess {worst_dev:.2e}")

# 11. Fraction reached by the regression attacker against N, population check (empirical rate).
p, n, T, eta, sigma = 30, 10, 40, 0.03, 1.0
Phi = rng.standard_normal((n, p))
H = Phi.T @ Phi / n + 0.05 * np.eye(p)
Sigma, R, M = chain_quantities(H, eta, sigma, T)
w_, V_ = np.linalg.eigh(Sigma)
Sig_half = V_ @ np.diag(np.sqrt(w_)) @ V_.T
Sig_mhalf = V_ @ np.diag(1 / np.sqrt(w_)) @ V_.T
phix = Phi[0] * 0.6 + 0.8 * rng.standard_normal(p)   # partly in span
g = Sig_half @ phix
K = Phi @ Sigma @ Phi.T
kx = Phi @ Sigma @ phix
rho = np.sqrt(kx @ np.linalg.solve(K, kx) / (phix @ Sigma @ phix))
print(f"      population multiple correlation rho(x) = {rho:.4f}")
for N in (20, 50, 200, 1000, 5000):
    fr = []
    for _ in range(200):
        out = (rng.standard_normal((N, p)) @ Sig_half) @ np.vstack([Phi, phix]).T
        Kh = np.cov(out.T, bias=True)
        c = np.linalg.solve(Kh[:n, :n], Kh[:n, n])
        w = Sig_mhalf @ R @ Phi.T @ c
        fr.append((w @ g) / (np.linalg.norm(w) * np.linalg.norm(g)))
    fr = np.array(fr)
    print(f"      N={N}: mean fraction {fr.mean():.4f}, 5th pct {np.percentile(fr,5):.4f}, "
          f"rho - fraction {rho-fr.mean():.4f}, k/N {n/N:.4f}, sqrt(k/N) {np.sqrt(n/N):.4f}")

print("\nALL PASS" if all_ok else "\nSOME CHECK FAILED")
