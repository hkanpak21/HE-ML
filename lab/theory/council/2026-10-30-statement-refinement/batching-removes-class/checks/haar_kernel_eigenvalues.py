"""Eigenvalues of the degree-k Haar kernel for normalized Hermite polynomials.

K_k(x, y) = E_u[h_k(<u, x>) h_k(<u, y>)], u uniform on S^{d-1}, h_k the normalized
Hermite polynomial, acting on L^2(gamma_d). Two independent computations.

1. Brute force. In the orthonormal Hermite basis H_alpha, |alpha| = k, the identity
   h_k(<u, x>) = sum_alpha sqrt(k!/alpha!) u^alpha H_alpha(x) for unit u gives the matrix
   M_{alpha beta} = sqrt(k!/alpha!) sqrt(k!/beta!) E_u[u^{alpha+beta}], and the sphere
   moment E_u[u^gamma] = prod (gamma_i - 1)!! / (d (d+2) ... (d+2k-2)) for even gamma.
   Its eigenvalues are the eigenvalues of K_k.

2. Closed form. K_k commutes with O(d), the k-th Wiener chaos splits into the
   inequivalent components V_{k,j}, j = k, k-2, ..., and by Schur's lemma K_k is the
   scalar lambda_{k,j} on V_{k,j}. The Funk and Hecke argument gives
   lambda_{k,j} = E[rho^k G_j(rho)], rho = <u, u'> for independent uniform u, u', and
   G_j the Gegenbauer polynomial C_j^{(d/2-1)} normalized by G_j(1) = 1. The component
   j = 0 is the frame-free part that centring removes. The top centred eigenvalue
   nu_k is max_{j >= 1} lambda_{k,j}.

Run: python3 haar_kernel_eigenvalues.py
"""
from fractions import Fraction
from itertools import combinations_with_replacement
from math import factorial

import numpy as np
import sympy as sp


def dfact(n):
    """Double factorial with (-1)!! = 1."""
    out = 1
    while n > 1:
        out *= n
        n -= 2
    return out


def sphere_moment(gamma, d):
    """E_u[prod u_i^{gamma_i}] for u uniform on S^{d-1}, exact rational."""
    if any(g % 2 for g in gamma):
        return Fraction(0)
    k = sum(gamma) // 2
    num = 1
    for g in gamma:
        num *= dfact(g - 1)
    den = 1
    for i in range(k):
        den *= d + 2 * i
    return Fraction(num, den)


def multi_indices(d, k):
    out = []
    for comb in combinations_with_replacement(range(d), k):
        alpha = [0] * d
        for i in comb:
            alpha[i] += 1
        out.append(tuple(alpha))
    return out


def brute_force_eigs(d, k):
    idx = multi_indices(d, k)
    n = len(idx)
    w = np.array([np.sqrt(factorial(k) / np.prod([factorial(a) for a in al])) for al in idx])
    M = np.zeros((n, n))
    for i, a in enumerate(idx):
        for j, b in enumerate(idx):
            if j < i:
                continue
            g = tuple(x + y for x, y in zip(a, b))
            M[i, j] = M[j, i] = w[i] * w[j] * float(sphere_moment(g, d))
    return np.sort(np.linalg.eigvalsh(M))[::-1]


def rho_even_moment(m, d):
    """E rho^{2m} for rho = <u, u'>, as a sympy expression in d."""
    out = sp.Integer(1)
    for i in range(m):
        out *= sp.Rational(2 * i + 1) / (d + 2 * i)
    return out


def lambda_kj(k, j, d):
    """E[rho^k G_j(rho)] with G_j the Gegenbauer polynomial normalized at 1."""
    x = sp.symbols('x')
    lam = d / sp.Integer(2) - 1
    G = sp.gegenbauer(j, lam, x)
    G = sp.expand(G / G.subs(x, 1))
    poly = sp.Poly(G, x)
    total = sp.Integer(0)
    for (power,), coeff in poly.terms():
        p = k + power
        if p % 2 == 0:
            total += coeff * rho_even_moment(p // 2, d)
    return sp.simplify(total)


def closed_form_nu(k, d):
    """The claimed closed form of the top centred eigenvalue."""
    if k % 2 == 1:
        num = dfact(k)
        den = sp.Integer(1)
        for i in range((k + 1) // 2):
            den *= d + 2 * i
    else:
        num = k * dfact(k - 1)
        den = sp.Integer(1)
        for i in range(k // 2 + 1):
            den *= d + 2 * i
    return sp.Rational(num) / den


def main():
    d = sp.symbols('d', positive=True)
    print("Closed forms lambda_{k,j}(d) = E[rho^k G_j(rho)], j >= 1, and the claimed nu_k")
    print("A row gives k, then j: lambda_{k,j}, then the claimed nu_k and whether it equals max_j.")
    ok_all = True
    for k in range(1, 11):
        row = []
        vals = {}
        for j in range(k, -1, -2):
            v = sp.factor(lambda_kj(k, j, d))
            vals[j] = v
            row.append(f"j={j}: {v}")
        claimed = sp.factor(closed_form_nu(k, d))
        lowest = 1 if k % 2 else 2
        match = sp.simplify(vals[lowest] - claimed) == 0
        # ordering: lambda_{k,j} decreasing in j >= 1 for all d >= 3, checked at d = 3..60
        order_ok = True
        pos_ok = True
        for dd in range(3, 61):
            seq = [float(vals[j].subs(d, dd)) for j in range(lowest, k + 1, 2)]
            if any(seq[i] < seq[i + 1] - 1e-15 for i in range(len(seq) - 1)):
                order_ok = False
            if any(s < -1e-15 for s in seq):
                pos_ok = False
        ok_all &= match and order_ok and pos_ok
        print(f"k={k}: " + "; ".join(row))
        print(f"      claimed nu_k = {claimed}, equals lambda_{{k,{lowest}}}: {match}, "
              f"decreasing in j (d=3..60): {order_ok}, nonnegative: {pos_ok}")
        # leading order in d
        lead = sp.limit(vals[lowest] * d ** ((k + 1) // 2 + (1 if k % 2 == 0 else 0)), d, sp.oo)
        print(f"      nu_k * d^ceil((k+1)/2) -> {lead} as d -> oo")
    print("Closed forms match the lowest nonradial component and dominate:", ok_all)

    print()
    print("Brute force in the Hermite basis against the closed forms, d = 3..6, k = 1..5")
    for k in range(1, 6):
        for dd in range(3, 7):
            if k >= 5 and dd > 5:
                continue
            eigs = brute_force_eigs(dd, k)
            pred = {}
            for j in range(k, -1, -2):
                pred[j] = float(lambda_kj(k, j, dd))
            # multiplicities N_j = dim of harmonics of degree j in R^d
            def N(j, dd):
                from math import comb
                if j == 0:
                    return 1
                if j == 1:
                    return dd
                return comb(dd + j - 1, j) - comb(dd + j - 3, j - 2)
            pred_list = []
            for j, v in pred.items():
                pred_list += [v] * N(j, dd)
            pred_list = np.sort(np.array(pred_list))[::-1]
            err = np.max(np.abs(eigs - pred_list)) if len(eigs) == len(pred_list) else float('nan')
            print(f"k={k} d={dd}: dim={len(eigs)}, max |brute - closed| = {err:.2e}, "
                  f"top centred = {max(v for j, v in pred.items() if j >= 1):.6f}, "
                  f"claimed nu_k = {float(closed_form_nu(k, dd)):.6f}")


if __name__ == '__main__':
    main()
