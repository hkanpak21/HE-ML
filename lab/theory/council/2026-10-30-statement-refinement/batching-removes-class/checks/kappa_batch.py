"""The per-update chi-square kappa(b) of the update stream at batch b, against its Gaussian
limit, on the law W = |Z| 1{|Z| <= A}, with per-example noise sigma_0^2 = mu_2.

Given the batch's magnitudes a = (W_i), the along-u component of the update is
m = b^{-1} sum_i xi_i W_i Z_i plus N(0, sigma_0^2 / b). On this law Z = +-W whenever W > 0,
so m ranges over the 2^b values b^{-1} sum_i eps_i a_i^2 with equal weights, and the
chi-square of the normalized along-u law nu_a against gamma_1 is the exact pair sum
chi^2(nu_a || gamma_1) + 1 = 2^{-2b} sum_{m, m'} K(m, m'),
K(m, m') = sigma^2 / (tau sqrt(2 sigma^2 - tau^2)) exp[(tau^2 (m^2 + m'^2) - sigma^2 (m - m')^2)
          / (2 tau^2 (2 sigma^2 - tau^2))],
sigma^2 = b^{-2} sum a_i^2 + tau^2, tau^2 = sigma_0^2 / b (step 7 of
thm-update-direction-chi-square-bound). kappa(b) = E_a chi^2 is then a Monte Carlo over a.

Predictions checked:
  kappa_inf = (1 - beta^2)^{-1/2} - 1, the Gaussian spiked limit, beta = c_2 / (mu_2 + sigma_0^2).
  kappa_G(b) = E_a chi2_G(eps_a), the Gaussian surrogate at the batch's own spike eps_a.
  The first-order coefficients C_1 of kappa(b) = kappa_inf + C_1 / b + O(b^-2):
    author (round 04): kappa_inf * Var(W^2 T(W)) / c_2^2
    this round: three terms, scale and spike fluctuation, bias, and fourth cumulant.

Run: python3 kappa_batch.py
"""
import numpy as np
from scipy import integrate, stats

A = 2.0
phi = stats.norm.pdf
Phi = stats.norm.cdf


def trunc_moment(p):
    """E[Z^p ; |Z| <= A]."""
    return integrate.quad(lambda z: z ** p * phi(z), -A, A)[0]


def kernel_check():
    """Check K(m, m') against direct quadrature once."""
    sigma2, tau2, m, mp = 1.3, 0.4, 0.5, -0.2
    tau, sigma = np.sqrt(tau2), np.sqrt(sigma2)
    direct = integrate.quad(lambda x: phi((x - m) / tau) * phi((x - mp) / tau) / tau ** 2
                            / (phi(x / sigma) / sigma), -30, 30)[0]
    closed = sigma2 / (tau * np.sqrt(2 * sigma2 - tau2)) * np.exp(
        (tau2 * (m ** 2 + mp ** 2) - sigma2 * (m - mp) ** 2) / (2 * tau2 * (2 * sigma2 - tau2)))
    return direct, closed


def chi2_given_a(a, sigma0_2):
    b = len(a)
    tau2 = sigma0_2 / b
    sigma2 = np.sum(a ** 2) / b ** 2 + tau2
    nz = a[a > 0]
    # all sign patterns on the nonzero entries
    k = len(nz)
    if k == 0:
        ms = np.array([0.0])
    else:
        signs = ((np.arange(2 ** k)[:, None] >> np.arange(k)[None, :]) & 1) * 2 - 1
        ms = signs @ (nz ** 2) / b
    pref = sigma2 / (np.sqrt(tau2) * np.sqrt(2 * sigma2 - tau2))
    M, Mp = np.meshgrid(ms, ms, indexing='ij')
    expo = (tau2 * (M ** 2 + Mp ** 2) - sigma2 * (M - Mp) ** 2) / (2 * tau2 * (2 * sigma2 - tau2))
    val = pref * np.mean(np.exp(expo)) - 1.0
    # Gaussian surrogate at the same spike
    eps = (np.sum(a ** 2 * (a ** 2 - 1)) / b ** 2) / sigma2
    chi_g = (1 - eps ** 2) ** -0.5 - 1 if eps < 1 else np.inf
    return val, chi_g, eps


def sample_a(rng, b):
    z = rng.standard_normal(b)
    w = np.abs(z)
    w[w > A] = 0.0
    return w


def main():
    direct, closed = kernel_check()
    print(f"kernel check: quadrature {direct:.10f}, closed form {closed:.10f}")
    mu2 = trunc_moment(2)
    m4 = trunc_moment(4)
    m6 = trunc_moment(6)
    m8 = trunc_moment(8)
    c2 = m4 - mu2
    sigma0_2 = mu2
    D = mu2 + sigma0_2
    beta = c2 / D
    kappa_inf = (1 - beta ** 2) ** -0.5 - 1
    # law moments. W^2 T(W) = Z^2 (Z^2 - 1) on |Z| <= A, zero outside.
    E_w2t = c2
    E_w2t_sq = m8 - 2 * m6 + m4
    var_w2t = E_w2t_sq - c2 ** 2
    var_w2 = m4 - mu2 ** 2
    cov_w2t_w2 = (m6 - m4) - c2 * mu2
    kappa4_bar = -2 * m8  # E[W^4 (E[Z^4|W] - 3 E[Z^2|W]^2)] with Z = +-W on the support
    print(f"law: A={A}, mu2={mu2:.6f}, c2={c2:.6f}, sigma0^2={sigma0_2:.6f}, D={D:.6f}, beta={beta:.6f}")
    print(f"     Var(W^2 T) = {var_w2t:.6f}, Var(W^2) = {var_w2:.6f}, Cov(W^2 T, W^2) = {cov_w2t_w2:.6f}, "
          f"kappa4_bar = {kappa4_bar:.6f}")
    print(f"kappa_inf = (1 - beta^2)^(-1/2) - 1 = {kappa_inf:.6f}  (beta^2/2 = {beta**2/2:.6f})")
    # first-order coefficients
    chi_p = beta * (1 - beta ** 2) ** -1.5
    chi_pp = (1 + 2 * beta ** 2) * (1 - beta ** 2) ** -2.5
    var_eps = (var_w2t - 2 * beta * cov_w2t_w2 + beta ** 2 * var_w2) / D ** 2
    bias_eps = (beta * var_w2 - cov_w2t_w2) / D ** 2
    c_scale = 0.5 * chi_pp * var_eps
    c_bias = chi_p * bias_eps
    c_cum = beta ** 2 / (4 * (1 - beta ** 2) ** 2.5) * kappa4_bar / D ** 2
    c_author = kappa_inf * var_w2t / c2 ** 2
    print(f"first-order C_1 (so kappa(b) ~ kappa_inf + C_1 / b):")
    print(f"   author's coefficient            {c_author:+.6f}")
    print(f"   scale and spike fluctuation     {c_scale:+.6f}")
    print(f"   bias of the spike               {c_bias:+.6f}")
    print(f"   fourth cumulant                 {c_cum:+.6f}")
    print(f"   Gaussian-surrogate total        {c_scale + c_bias:+.6f}")
    print(f"   full total                      {c_scale + c_bias + c_cum:+.6f}")
    rng = np.random.default_rng(20261030)
    print()
    print(" b   N_a    kappa(b)      se       kappa_G(b)    se      (kappa-kappa_inf)*b  (kappa_G-kappa_inf)*b")
    for b, Na in ((1, 20000), (2, 20000), (3, 20000), (4, 20000), (6, 10000), (8, 6000), (10, 3000), (12, 1200)):
        vals = np.empty(Na)
        gvals = np.empty(Na)
        for i in range(Na):
            a = sample_a(rng, b)
            vals[i], gvals[i], _ = chi2_given_a(a, sigma0_2)
        k, se = vals.mean(), vals.std(ddof=1) / np.sqrt(Na)
        kg, seg = gvals.mean(), gvals.std(ddof=1) / np.sqrt(Na)
        print(f"{b:2d} {Na:6d}  {k:.6f}  {se:.6f}   {kg:.6f}  {seg:.6f}   {(k-kappa_inf)*b:+.4f}             {(kg-kappa_inf)*b:+.4f}")


if __name__ == '__main__':
    main()
