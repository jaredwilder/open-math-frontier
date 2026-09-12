from fractions import Fraction
from math import factorial
import random
import sys

SEED = 20260912
TRIALS = 3000
RMAX = 5
KMAX = 9

# H(z)=exp(gamma*z)*prod_i(1+alpha_i*z), gamma>0, alpha_i>=0.
# Exact rational arithmetic. Tests
# (k+r) D_{r,k-1}D_{r,k+1} <= k D_{r,k}^2.


def coeffs(gamma, alphas, N):
    p = [Fraction(1)]
    for a in alphas:
        q = [Fraction(0)] * (len(p) + 1)
        for i, c in enumerate(p):
            q[i] += c
            q[i + 1] += c * a
        p = q
    out = []
    for n in range(N + 1):
        s = Fraction(0)
        for j, c in enumerate(p):
            if j <= n:
                s += c * gamma ** (n - j) / factorial(n - j)
        out.append(s)
    return out


def bareiss(M):
    A = [row[:] for row in M]
    n = len(A)
    if n == 0:
        return Fraction(1)
    if n == 1:
        return A[0][0]
    sign = 1
    prev = Fraction(1)
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((i for i in range(k + 1, n) if A[i][k]), None)
            if piv is None:
                return Fraction(0)
            A[k], A[piv] = A[piv], A[k]
            sign = -sign
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) / prev
        prev = pivot
        for i in range(k + 1, n):
            A[i][k] = 0
    return sign * A[-1][-1]


def D(a, r, k):
    return bareiss([
        [a[k + j - i] if k + j - i >= 0 else Fraction(0) for j in range(r)]
        for i in range(r)
    ])


def check(a, r, k):
    d = D(a, r, k)
    dm = D(a, r, k - 1)
    dp = D(a, r, k + 1)
    gap = k * d * d - (k + r) * dm * dp
    return gap >= 0, gap


rng = random.Random(SEED)
vals = [Fraction(i, j) for j in range(1, 8) for i in range(1, 9)]
checked = 0
worst = None

for t in range(TRIALS):
    gamma = rng.choice(vals)
    m = rng.randint(0, 6)
    alphas = [rng.choice(vals) for _ in range(m)]
    a = coeffs(gamma, alphas, KMAX + RMAX + 2)
    for r in range(1, RMAX + 1):
        for k in range(1, KMAX + 1):
            ok, gap = check(a, r, k)
            checked += 1
            if not ok:
                print("FAIL", t, "gamma", gamma, "alphas", alphas,
                      "r,k", r, k, "gap", gap)
                sys.exit(1)
            if worst is None or gap < worst[0]:
                worst = (gap, gamma, alphas, r, k)

print("PASS exact rational families", TRIALS, "inequalities", checked)
print("min absolute gap", worst)
