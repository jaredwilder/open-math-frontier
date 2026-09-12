"""K521's remedy: NORMALIZED minors, and degree above 26.

Normalize the roots: replace w by w/S with S the scale of the roots, so the power sums stay
O(n).  Hermite minor positivity is INVARIANT under w -> w/S for S > 0 (it only rescales each
minor by a positive power of S), so the normalization is free.

Calibrate first (K517) on a known case, then run the object at growing degree.
"""
from mpmath import mp, mpf, exp, pi, quad, factorial, matrix, polyroots, nstr
mp.dps=120
def Phi(u):
    s=mpf(0)
    for n in range(1,12):
        n=mpf(n)
        s+=(2*pi**2*n**4*exp(mpf(9)*u)-3*pi*n**2*exp(mpf(5)*u))*exp(-pi*n**2*exp(4*u))
    return s
NMAX=34
mom=[quad(lambda u: u**(2*j)*Phi(u),[0,4],maxdegree=12) for j in range(NMAX+1)]
def norm_minors(rts):
    n=len(rts)
    S=max(abs(r) for r in rts)
    rr=[r/S for r in rts]
    p=[sum(r**k for r in rr) for k in range(2*n)]
    ms=[]
    for k in range(1,n+1):
        M=matrix(k,k)
        for i in range(k):
            for j in range(k): M[i,j]=p[i+j]
        d=mp.det(M)
        ms.append(mp.re(d))
    return ms,S
print("   CALIBRATION (K517): known all-real and known complex")
for nm,rts in (("all real 1,2,3,4",[mpf(k) for k in (1,2,3,4)]),
               ("complex 1,2,i,-i",[mpf(1),mpf(2),mp.mpc(0,1),mp.mpc(0,-1)])):
    ms,S=norm_minors(rts)
    print("      %-18s all positive: %-5s   minors %s"%(nm,all(m>0 for m in ms),
          ", ".join(nstr(m,6) for m in ms)),flush=True)
print()
print("      N    real roots   all normalized minors > 0?   min minor        max |minor|")
for N in (10,16,22,26,30,34):
    co=[(-1)**j*mom[j]/factorial(2*j) for j in range(N+1)]
    poly=[co[N-i] for i in range(N+1)]
    rts=polyroots(poly,maxsteps=600,extraprec=600)
    nreal=sum(1 for r in rts if abs(mp.im(r))<mpf(10)**-40)
    ms,S=norm_minors(rts)
    print("      %2d   %2d/%2d        %-27s %-16s %s"
          %(N,nreal,N,"YES" if all(m>0 for m in ms) else "no",nstr(min(ms),7),nstr(max(abs(m) for m in ms),7)),flush=True)
print()
print("   READING: the normalization keeps the minors in range; the real-root column says")
print("   whether the truncation has begun to resolve the object's real zeros at all.")
print()
print("DONE",flush=True)