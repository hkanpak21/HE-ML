"""Check of step 2 of thm-noise-exponent-gap, the Mehler contraction.

Label law W = |Z|, batch b = 1, so nu_a is the law of (xi a^2 + varsigma N)/sigma
with sigma^2 = a^2 + varsigma^2. The closed form of the chi-square is part (d)
of thm-update-direction-chi-square-bound. The check has two parts.

1. The Hermite coefficients c_k of d nu_a / d gamma_1 at the reference noise
   varsigma_0, by quadrature, then the sum over k of rho^(2k) c_k^2 with
   rho^2 = (a^2 + varsigma_0^2)/(a^2 + varsigma^2), against the closed form at
   noise varsigma. Equality is the semigroup identity. The odd coefficients
   must vanish.
2. The ratio chi^2(varsigma)/chi^2(varsigma_0) against rho^4. The ratio must be
   at most rho^4, and it tends to rho^4 when the k = 2 term dominates.
"""
import numpy as np
from numpy.polynomial.hermite_e import hermeval
from scipy.special import factorial

def chi2_closed(a, s2):
    s = np.sqrt(s2)
    sig2 = a * a + s2
    pref = sig2 / (s * np.sqrt(2 * a * a + s2))
    return pref * 0.5 * (np.exp(a**4 / (2 * a * a + s2)) + np.exp(-a**4 / s2)) - 1.0

def ratio_density(x, a, s2):
    """d nu_a / d gamma_1 at x, nu_a the law of (xi a^2 + varsigma N)/sigma."""
    sig = np.sqrt(a * a + s2)
    s = np.sqrt(s2)
    y = sig * x
    dens = 0.5 * (np.exp(-(y - a * a) ** 2 / (2 * s2)) + np.exp(-(y + a * a) ** 2 / (2 * s2))) / (s * np.sqrt(2 * np.pi))
    dens_scaled = dens * sig
    gamma = np.exp(-x * x / 2) / np.sqrt(2 * np.pi)
    return dens_scaled / gamma

def hermite_coeffs(a, s2, K=40):
    """Coefficients of d nu_a / d gamma_1 in the normalized probabilists' Hermite
    basis, by trapezoid quadrature against gamma_1 on [-14, 14], with the
    three-term recurrence He_{k+1} = x He_k - k He_{k-1}."""
    x = np.linspace(-14.0, 14.0, 280001)
    g = np.exp(-x * x / 2) / np.sqrt(2 * np.pi)
    f = ratio_density(x, a, s2)
    c = np.zeros(K + 1)
    h_prev = np.zeros_like(x)
    h = np.ones_like(x)
    for k in range(K + 1):
        hk = h / np.sqrt(float(factorial(k)))
        c[k] = np.trapezoid(g * f * hk, x)
        h_prev, h = h, x * h - k * h_prev
    return c

print("part 1, semigroup identity, W=|Z|, b=1")
print(f"{'a':>5} {'s0^2':>6} {'s^2':>6} {'closed chi2(s)':>16} {'sum rho^2k c_k^2':>18} {'max |odd c_k|':>14} {'c_1':>10}")
for a in [0.5, 1.0, 1.5]:
    for s0 in [1.0, 2.0]:
        c = hermite_coeffs(a, s0)
        for s2 in [2.0, 4.0, 16.0]:
            if s2 <= s0:
                continue
            rho2 = (a * a + s0) / (a * a + s2)
            ks = np.arange(len(c))
            recon = np.sum((rho2 ** ks[1:]) * c[1:] ** 2)
            closed = chi2_closed(a, s2)
            odd = np.max(np.abs(c[1::2]))
            print(f"{a:5.2f} {s0:6.2f} {s2:6.2f} {closed:16.9f} {recon:18.9f} {odd:14.2e} {c[1]:10.2e}")

print()
print("part 2, contraction ratio against rho^4")
print(f"{'a':>5} {'s0^2':>6} {'s^2':>6} {'chi2(s)/chi2(s0)':>18} {'rho^4':>12} {'ratio/rho^4':>12}")
for a in [0.5, 1.0, 1.5, 2.0]:
    s0 = 2.0 * a * a + 0.5
    for s2 in [s0 * 2, s0 * 4, s0 * 16, s0 * 64]:
        rho2 = (a * a + s0) / (a * a + s2)
        r = chi2_closed(a, s2) / chi2_closed(a, s0)
        print(f"{a:5.2f} {s0:6.2f} {s2:6.2f} {r:18.6e} {rho2**2:12.6e} {r/rho2**2:12.6f}")
