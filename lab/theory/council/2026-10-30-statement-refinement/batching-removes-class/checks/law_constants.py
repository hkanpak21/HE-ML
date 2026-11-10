"""Constants of the round-04 experiment law W = min(|Z|, 4) with sigma_0^2 = mu_2, and of the
alternative sigma_0^2 = 3 mu_2. Reports mu_2, c_2, beta = c_2 / (mu_2 + sigma_0^2), the
Gaussian-limit prices gamma_beta = (4 + beta) / (3 beta^2) against 1 / beta^2, and the two
Gaussian-limit divergences, chi-square (1 - beta^2)^(-1/2) - 1 and Kullback
(beta - log(1 + beta)) / 2.

Run: python3 law_constants.py
"""
import numpy as np
from scipy import integrate, stats

phi = stats.norm.pdf


def moments(A):
    mu2 = integrate.quad(lambda z: min(z * z, A * A) * phi(z), -np.inf, np.inf)[0]
    c2 = integrate.quad(lambda z: min(z * z, A * A) * (z * z - 1) * phi(z), -np.inf, np.inf)[0]
    return mu2, c2


def main():
    for A in (4.0,):
        mu2, c2 = moments(A)
        for mult in (1.0, 3.0):
            s0 = mult * mu2
            beta = c2 / (mu2 + s0)
            chi = (1 - beta ** 2) ** -0.5 - 1 if beta < 1 else float('inf')
            kl = 0.5 * (beta - np.log(1 + beta))
            print(f"W=min(|Z|,{A}), sigma0^2={mult} mu2: mu2={mu2:.6f} c2={c2:.6f} beta={beta:.6f} "
                  f"gamma_beta={(4+beta)/(3*beta**2):.4f} 1/beta^2={1/beta**2:.4f} "
                  f"chi2_inf={chi:.4f} kl_inf={kl:.4f}")


if __name__ == '__main__':
    main()
