"""The Gaussian spiked covariance model: PCA overlap, the overlap-1/2 price, and bulk
delocalization. A numerical check of two facts cited from memory in the round file.

Model: v_t ~ N(0, I_d + beta u u^T), t = 1..T, T = gamma d. Paul's formula (from memory):
the squared overlap of the top sample eigenvector with u tends to
(1 - c/beta^2) / (1 + c/beta), c = d/T = 1/gamma, when c < beta^2.
Setting it to 1/4 gives gamma_beta = (4 + beta) / (3 beta^2), against the detection
threshold 1/beta^2.

Run: python3 spiked_overlap.py
"""
import numpy as np


def paul(beta, c):
    return max(0.0, (1 - c / beta ** 2) / (1 + c / beta))


def main():
    rng = np.random.default_rng(20261030)
    d = 400
    for beta in (0.4, 0.7, 1.0):
        gamma_beta = (4 + beta) / (3 * beta ** 2)
        print(f"beta={beta}: detection threshold 1/beta^2 = {1/beta**2:.4f}, "
              f"overlap-1/2 threshold gamma_beta = {gamma_beta:.4f}, ratio = {(4+beta)/3:.4f}")
        u = np.zeros(d)
        u[0] = 1.0
        for gamma in (0.8 * gamma_beta, gamma_beta, 1.25 * gamma_beta, 2 * gamma_beta):
            T = int(round(gamma * d))
            ov = []
            bulk = []
            succ = 0
            reps = 20
            for _ in range(reps):
                X = rng.standard_normal((T, d))
                X[:, 0] *= np.sqrt(1 + beta)
                M = X.T @ X / T
                w, V = np.linalg.eigh(M)
                top = V[:, -1]
                ov.append(top[0] ** 2)
                bulk.append(np.max(V[0, :-1] ** 2))
                succ += abs(top[0]) >= 0.5
            print(f"   gamma={gamma:.3f} T={T}: mean sq overlap {np.mean(ov):.4f} "
                  f"(Paul {paul(beta, 1/gamma):.4f}), success at 1/2: {succ}/{reps}, "
                  f"max bulk sq overlap {np.mean(bulk):.4f} (log d / d = {np.log(d)/d:.4f})")


if __name__ == '__main__':
    main()
