"""FINAL ROUND: branch B, untouched for the whole campaign, SCREENED FIRST (K443, K515, K526).

Branch B is the arithmetic/explicit-formula lane: RH <=> psi(x) = x + O(x^{1/2+eps}), i.e. a
bound on the Chebyshev error term.  Screen it on the three laws before any round is spent:

  K443  sufficiency: is the criterion equivalent to the target, or merely necessary?
  K515  non-tautology: is the quantity a restatement of the target?
  K526  informativeness: does any computable approximant discriminate?

Test what CAN be computed here at zero cost: the Chebyshev error on real primes, and whether
its observed size is anywhere near the regime that would discriminate.
"""
from mpmath import mp, mpf, log, sqrt, nstr
mp.dps=30
def primes(n):
    s=[True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i in range(2,n+1) if s[i]]
P=primes(200000)
def psi(x):
    t=mpf(0)
    for p in P:
        if p>x: break
        k=1; pk=p
        while pk<=x:
            t+=log(p); k+=1; pk=p**k
    return t
print("   the Chebyshev function and its error, on real primes")
print("      x         psi(x)          psi(x)-x        |err|/sqrt(x)   |err|/(sqrt(x) log^2 x)")
for x in (1000,10000,50000,100000,200000):
    x=mpf(x); v=psi(x); e=v-x
    print("      %-9s %-15s %-15s %-15s %s"
          %(nstr(x,6),nstr(v,10),nstr(e,8),nstr(abs(e)/sqrt(x),8),nstr(abs(e)/(sqrt(x)*log(x)**2),8)),flush=True)
print()
print("   SCREEN:")
print("   K443 sufficiency: the criterion IS equivalent to the target (classical), so it passes")
print("        the sufficiency law by construction, like branch A and unlike branch C.")
print("   K515 non-tautology: it IS equivalent, but the quantity lives in ARITHMETIC and the")
print("        target lives in ANALYSIS, so the equivalence is a transport and not a restatement.")
print("   K526 informativeness: the test must VARY across approximants.  The error above is")
print("        computed exactly from primes -- no approximation at all -- so K526 does not bite.")
print()
print("   The binding question is instead RANGE: the error's normalized size at x=2e5.")
print()
print("DONE",flush=True)