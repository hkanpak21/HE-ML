"""Check of lem-genie-chi-square-finite for the clipped law W = min(|Z|, A), b = 1.

kappa_chi2(varsigma_0) = E_a chi^2(nu_a || gamma_1). For a < A the conditional
law of Z given W = a is the pair {-a, +a}, and the two-atom closed form of
thm-update-direction-chi-square-bound (d) applies. For the atom a = A, of mass
2 Phibar(A), Z given W = A is gamma_1 restricted to |z| >= A, and nu_A is
computed by quadrature. The lemma's bound is
    sqrt(1 + A^2/(b s0^2)) * (1 - 2 A^2/(b s0^2))^(-1/2) - 1   for s0^2 > 2 A^2 / b.
The table also reports the value below the lemma's threshold, where the bound
does not apply and the quantity is still finite for this law.
"""
import numpy as np
from scipy import integrate
from scipy.stats import norm

A = 2.0

def chi2_two_atom(a, s2):
    s = np.sqrt(s2)
    sig2 = a * a + s2
    pref = sig2 / (s * np.sqrt(2 * a * a + s2))
    return pref * 0.5 * (np.exp(a**4 / (2 * a * a + s2)) + np.exp(-a**4 / s2)) - 1.0

def chi2_atom_A(s2, A=A):
    """Z given W=A is gamma_1 on |z|>=A. m = xi A Z + varsigma N. Reference N(0, A^2 + s2)."""
    sig2 = A * A + s2
    s = np.sqrt(s2)
    zs = np.linspace(A, A + 12.0, 6001)
    wz = norm.pdf(zs) / norm.sf(A)    # density of |Z| given |Z|>=A, on z>=A, mass one
    def dens(y):
        # m = xi A |Z| + varsigma N, a symmetric mixture of N(+-A z, s2) over z
        vals = 0.5 * (norm.pdf(y, loc=A * zs, scale=s) + norm.pdf(y, loc=-A * zs, scale=s))
        return np.trapezoid(vals * wz, zs)
    ys = np.linspace(-14 * np.sqrt(sig2), 14 * np.sqrt(sig2), 20001)
    p = np.array([dens(y) for y in ys])
    q = norm.pdf(ys, scale=np.sqrt(sig2))
    mass = np.trapezoid(p, ys)
    chi2 = np.trapezoid(p * p / q, ys) - 1.0
    return chi2, mass

def kappa_chi2(s2, A=A):
    cont, _ = integrate.quad(lambda a: 2 * norm.pdf(a) * chi2_two_atom(a, s2), 0.0, A, limit=200)
    atom, mass = chi2_atom_A(s2, A)
    return cont + 2 * norm.sf(A) * atom, cont, atom, mass

def bound(s2, A=A, b=1):
    t = A * A / (b * s2)
    if 2 * t >= 1:
        return np.inf
    return np.sqrt(1 + t) / np.sqrt(1 - 2 * t) - 1.0

print(f"clipped law W=min(|Z|,A), A={A}, b=1, mass of atom = {2*norm.sf(A):.5f}")
print(f"{'s0^2/A^2':>9} {'kappa_chi2':>12} {'continuous':>12} {'atom chi2':>12} {'atom mass':>10} {'lemma bound':>12}")
for frac in [0.5, 1.0, 2.0, 2.5, 3.0, 4.0, 8.0]:
    s2 = frac * A * A
    k, cont, atom, mass = kappa_chi2(s2)
    print(f"{frac:9.2f} {k:12.6f} {cont:12.6f} {atom:12.6f} {mass:10.6f} {bound(s2):12.4f}")

print()
print("exponent check: kappa_chi2(s) * (A^2 + s^2)^2 should approach a constant as s grows")
for frac in [4.0, 8.0, 16.0, 32.0, 64.0]:
    s2 = frac * A * A
    k, *_ = kappa_chi2(s2)
    print(f"{'s^2/A^2':>9}={frac:6.1f}  kappa={k:.6e}  kappa*(A^2+s^2)^2={k*(A*A+s2)**2:.6f}")
