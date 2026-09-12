from fractions import Fraction
from math import factorial
import random

SEED = 20260912
TRIALS = 1200
RMAX = 6
KMAX = 12

# H(z)=exp(gamma*z)*prod_i (1+alpha_i*z), gamma>0, alpha_i>=0.
# Exact rational arithmetic. Tests the normalized higher-order inequality
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
    return bareiss([[a[k + j - i] if k + j - i >= 0 else Fraction(0)
                     for j in range(r)] for i in range(r)])


def audit_family(gamma, alphas):
    a = coeffs(gamma, alphas, KMAX + RMAX + 2)
    cache = {}

    def dc(r, k):
        key = (r, k)
        if key not in cache:
            cache[key] = D(a, r, k)
        return cache[key]

    count = 0
    for r in range(1, RMAX + 1):
        for k in range(1, KMAX + 1):
            dm, d0, dp = dc(r, k - 1), dc(r, k), dc(r, k + 1)
            gap = k * d0 * d0 - (k + r) * dm * dp
            if gap < 0:
                return False, (r, k, gap, dm, d0, dp)
            count += 1
    return True, count


vals = [Fraction(1, 100), Fraction(1, 30), Fraction(1, 10), Fraction(1, 3),
        Fraction(1), Fraction(3), Fraction(10), Fraction(30), Fraction(100),
        Fraction(2, 7), Fraction(7, 2), Fraction(11, 13), Fraction(13, 11)]

families = []
for g in vals:
    families += [
        (g, []),
        (g, [Fraction(1, 100)]),
        (g, [Fraction(100)]),
        (g, [Fraction(1, 100), Fraction(100)]),
        (g, [Fraction(1, 10), Fraction(1), Fraction(10)]),
    ]

rng = random.Random(SEED)
while len(families) < TRIALS:
    g = rng.choice(vals)
    m = rng.randint(0, 8)
    alphas = [rng.choice(vals) for _ in range(m)]
    families.append((g, alphas))

checks = 0
for i, (g, aa) in enumerate(families[:TRIALS]):
    ok, info = audit_family(g, aa)
    if not ok:
        print("FAIL family", i, "gamma", g, "alphas", aa, "detail", info)
        raise SystemExit(1)
    checks += info

print("PASS")
print("seed", SEED)
print("families", TRIALS)
print("r_range", 1, RMAX)
print("k_range", 1, KMAX)
print("exact_inequalities", checks)
print("family_class H(z)=exp(gamma*z)*prod(1+alpha_i*z), gamma>0, alpha_i>=0")
