"""Two checks.

A. Part (c) of thm-noise-exponent-gap. The server's second-moment recursion is
   e_{t+1} = (1 - eta)^2 e_t + eta^2 sigma^2(e_t), with
   sigma^2(e) = ((d (mu_2 + b s^2) + c_2 + (d + 1) e) / (K b)),
   e_0 = 2 r_0, target e_R <= 2 r. For each noise level the least R over a grid
   of constant steps is found, N = K R, and the slope of log N against
   log(1 + x) is fitted. The harmonic lower bound K sigma_-^2 (1/(2r) - 1/(2r_0))
   with sigma_-^2 = (d - 1)(mu_2 + b s^2)/(K b) is printed beside it.

B. The two constants of clause 17 for the clipped law W = max(0.05, min(|Z|, 4)):
   the surrogate conditional chi-square E[W^4 T(W)^2 / (W^2 + s^2)^2] / 2 and the
   spiked value c_2^2 / (2 (mu_2 + s^2)^2), and their ratio at several s^2, which
   the clause says moves with s. Also mu_2, c_2 and A for the experiment.
"""
import numpy as np
from scipy import integrate
from scipy.stats import norm

# label law W = max(0.05, min(|Z|, 4))
lo, hi = 0.05, 4.0
def w(z):
    return np.maximum(lo, np.minimum(np.abs(z), hi))

mu2, _ = integrate.quad(lambda z: w(z) ** 2 * norm.pdf(z), -12, 12, limit=400, points=[-4, -0.05, 0.05, 4])
c2, _ = integrate.quad(lambda z: w(z) ** 2 * (z * z - 1) * norm.pdf(z), -12, 12, limit=400, points=[-4, -0.05, 0.05, 4])
print(f"clipped law: mu_2 = {mu2:.6f}, c_2 = {c2:.6f}, A = {hi}, A^2/mu_2 = {hi*hi/mu2:.3f}")
print()

# Part A
d, K, r0, r = 200, 16, 1.0, 0.1
for b in [1, 8]:
    print(f"part A, trainer recursion, d={d}, K={K}, b={b}, r0={r0}, r={r}")
    print(f"{'x':>4} {'s^2':>9} {'N_tr (best const step)':>24} {'eta*':>9} {'harmonic lower bound':>22} {'ratio':>7}")
    xs = [0, 1, 4, 16, 64]
    Ns = []
    for x in xs:
        s2 = x * mu2 / b
        # the recursion is affine, e_{t+1} = alpha e_t + beta, so e_R has a closed form
        best = None
        for eta in np.geomspace(1e-5, 1.0, 20000):
            alpha = (1 - eta) ** 2 + eta ** 2 * (d + 1) / (K * b)
            beta = eta ** 2 * (d * (mu2 + b * s2) + c2) / (K * b)
            if alpha >= 1:
                continue
            fix = beta / (1 - alpha)
            if fix >= 2 * r:
                continue
            e0 = 2 * r0
            R = int(np.ceil(np.log((2 * r - fix) / (e0 - fix)) / np.log(alpha)))
            if best is None or R < best[0]:
                best = (R, eta)
        N = K * best[0]
        Ns.append(N)
        sig_minus = (d - 1) * (mu2 + b * s2) / (K * b)
        lower = K * sig_minus * (1 / (2 * r) - 1 / (2 * r0))
        print(f"{x:4d} {s2:9.4f} {N:24d} {best[1]:9.5f} {lower:22.1f} {N/lower:7.3f}")
    lx = np.log1p(np.array(xs[1:], dtype=float))
    lN = np.log(np.array(Ns[1:], dtype=float))
    slope = np.polyfit(lx, lN, 1)[0]
    print(f"slope of log N_tr against log(1+x) over x in {xs[1:]}: {slope:.4f}")
    print()

# Part B
print("part B, clause 17 constants for the clipped law, b=1")
# T(W) = E[Z^2 | W] - 1. For a in (lo, hi): Z = +-a, T = a^2 - 1.
# For the atom W=lo (|Z|<=lo): E[Z^2 | |Z|<=lo] - 1. For the atom W=hi: E[Z^2 | |Z|>=hi] - 1.
p_lo = 2 * norm.cdf(lo) - 1
p_hi = 2 * norm.sf(hi)
ez2_lo = integrate.quad(lambda z: z * z * norm.pdf(z), -lo, lo)[0] / p_lo
ez2_hi = 2 * integrate.quad(lambda z: z * z * norm.pdf(z), hi, 14)[0] / p_hi
T_lo, T_hi = ez2_lo - 1, ez2_hi - 1
def surrogate(s2):
    cont = integrate.quad(lambda a: 2 * norm.pdf(a) * a**4 * (a * a - 1) ** 2 / (a * a + s2) ** 2, lo, hi, limit=200)[0]
    atoms = p_lo * lo**4 * T_lo**2 / (lo * lo + s2) ** 2 + p_hi * hi**4 * T_hi**2 / (hi * hi + s2) ** 2
    return 0.5 * (cont + atoms)
def spiked(s2):
    return 0.5 * c2 * c2 / (mu2 + s2) ** 2
print(f"T(lo)={T_lo:.5f}, T(hi)={T_hi:.5f}, P[W=lo]={p_lo:.5f}, P[W=hi]={p_hi:.6f}")
print(f"{'s^2':>8} {'surrogate':>12} {'spiked':>12} {'ratio':>10}")
for s2 in [0.0, 0.1, 1.0, 4.0, 16.0, 64.0, 256.0, 1e4]:
    print(f"{s2:8.1f} {surrogate(s2):12.6e} {spiked(s2):12.6e} {surrogate(s2)/spiked(s2):10.4f}")
VarW2T = (integrate.quad(lambda a: 2 * norm.pdf(a) * a**4 * (a*a-1)**2, lo, hi)[0] + p_lo*lo**4*T_lo**2 + p_hi*hi**4*T_hi**2) - c2**2
print(f"limit of the ratio as s -> infinity, 1 + Var(W^2 T(W))/c_2^2 = {1 + VarW2T/c2**2:.4f}")
