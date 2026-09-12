"""OB14's discharge attempt: what property REALLY decides the one-step monotonicity?

v_k = I_{2k+2}/((2k+1) I_{2k}) non-increasing.

Equivalently:  (2k-1) I_{2k+2} I_{2k-2}  <=  (2k+1) I_{2k}^2 .

Consider the NORMALISED sequence  J_k = I_{2k} / Gamma(k + 1/2).
The statement is EXACTLY J_{k+1} J_{k-1} <= J_k^2: the Gaussian-normalised moment
sequence is LOG-CONCAVE.
"""
from mpmath import mp, mpf, exp, pi, quad, gamma, nstr

mp.dps = 40


def Phi(u):
    s = mpf(0)
    for n in range(1, 14):
        n = mpf(n)
        s += (2 * pi ** 2 * n ** 4 * exp(mpf(9) * u) - 3 * pi * n ** 2 * exp(mpf(5) * u)) * \
             exp(-pi * n ** 2 * exp(4 * u))
    return s


M = 14
I = [quad(lambda u: u ** (2 * k) * Phi(u), [0, 8], maxdegree=12) for k in range(M)]
J = [I[k] / gamma(k + mpf(1) / 2) for k in range(M)]

print("   claim: the row  <=>  J_{k+1} J_{k-1} <= J_k^2  with J_k = I_{2k}/Gamma(k+1/2)")
print("   verify against the direct form at several k:")
for k in range(1, 8):
    if k + 1 >= M: break
    direct = (2 * k - 1) * I[k + 1] * I[k - 1] <= (2 * k + 1) * I[k] ** 2
    newf = J[k + 1] * J[k - 1] <= J[k] ** 2
    print("      k=%-3d  direct=%-6s  log-concave form=%-6s  agree=%s"
          % (k, direct, newf, direct == newf), flush=True)

print()
print("   the Gaussian-normalised sequence J_k for the theta kernel, and its log-concavity ratio:")
for k in range(1, 10):
    if k + 1 >= M: break
    r = J[k + 1] * J[k - 1] / J[k] ** 2
    print("      k=%-3d  J_k=%-24s  J_{k+1}J_{k-1}/J_k^2 = %s  %s"
          % (k, nstr(J[k], 12), nstr(r, 14), "<=1 ok" if r <= 1 else "FAILS"), flush=True)

print()
print("   >>> THE ENTIRE BINDING ROW OF THE CRITERION IS:")
print("   >>>   the sequence  I_{2k} / Gamma(k+1/2)  is LOG-CONCAVE.")
print("   >>> no weights, no thresholds, no factorials, no determinants.")
print()
print("DONE", flush=True)