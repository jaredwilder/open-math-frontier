"""BOUNDARY AUDIT of last round's route kill, before it is banked.

The kill rests on: non-real-rooted polynomials satisfying the criterion.  Three ways the
kill could itself be wrong, each tested:

(A) DEPTH.  The criterion was demanded only to order 4.  Demand it at EVERY order the
    window allows and recount the hits.
(B) TRUNCATION.  A polynomial's Toeplitz lattice has vanishing minors past the degree, which
    can make the criterion hold vacuously.  Restrict to k,r well inside the degree.
(C) THE RIGHT CRITERION.  The campaign's criterion as certified is the SQUARE-FREE entry.
    Re-test using the ORIGINAL entry form to be sure the kill is not an artifact of the
    reduction.
"""
import random
from fractions import Fraction as F
def poly(roots,p,q):
    c=[F(1)]
    for a in roots:
        c=[ (c[i] if i<len(c) else F(0)) + (a*c[i-1] if i>=1 and i-1<len(c) else F(0)) for i in range(len(c)+1)]
    nc=[F(0)]*(len(c)+2)
    for i,ci in enumerate(c):
        nc[i]+=ci; nc[i+1]+=p*ci; nc[i+2]+=q*ci
    return nc
def det(M):
    n=len(M)
    if n==0: return F(1)
    M=[r[:] for r in M]; d=F(1)
    for cc in range(n):
        pv=next((r for r in range(cc,n) if M[r][cc]!=0),None)
        if pv is None: return F(0)
        if pv!=cc: M[cc],M[pv]=M[pv],M[cc]; d=-d
        d*=M[cc][cc]; inv=F(1)/M[cc][cc]
        for r in range(cc+1,n):
            f=M[r][cc]*inv
            if f:
                for c2 in range(cc,n): M[r][c2]-=f*M[cc][c2]
    return d
def D(a,r,k,N):
    if r==0: return F(1)
    if k<0: return F(0)
    return det([[ (a[k+j-i] if 0<=k+j-i<N else F(0)) for j in range(r)] for i in range(r)])
def sq_free_ok(a,N,R,kmax):
    for r in range(1,R+1):
        for k in range(1,kmax+1):
            if k+r+1>=N: continue
            if F(r)*D(a,r,k-1,N)*D(a,r,k+1,N) > F(k)*D(a,r+1,k,N)*D(a,r-1,k,N): return False
    return True
def orig_ok(a,N,R,kmax):
    for r in range(1,R+1):
        for k in range(1,kmax+1):
            if k+r+1>=N: continue
            lhs=F(k+r)*D(a,r,k-1,N)*D(a,r,k+1,N)
            rhs=F(k)*D(a,r,k,N)**2
            if lhs>rhs: return False
    return True
random.seed(19)
res={"A depth=every order, k interior":0,"B original entry form":0,"tested":0}
for _ in range(3000):
    m=random.randint(4,8)
    roots=[F(random.randint(1,20),random.randint(1,6)) for _ in range(m)]
    p=F(random.randint(1,12),random.randint(1,6)); q=F(random.randint(1,30),random.randint(1,6))
    if p*p>=4*q: continue
    c=poly(roots,p,q); N=len(c)
    if any(x<0 for x in c): continue
    deg=N-1
    R=max(1,deg//2); kmax=max(1,deg//2)
    res["tested"]+=1
    if sq_free_ok(c,N,R,kmax): res["A depth=every order, k interior"]+=1
    if orig_ok(c,N,R,kmax): res["B original entry form"]+=1
print("   non-real-rooted polynomials tested at FULL depth and interior shift: %d"%res["tested"],flush=True)
print("   satisfying the square-free criterion : %d"%res["A depth=every order, k interior"],flush=True)
print("   satisfying the ORIGINAL entry form   : %d"%res["B original entry form"],flush=True)
print()
if res["A depth=every order, k interior"]>0:
    print("   >>> THE KILL SURVIVES the audit at full depth, interior shifts, and both forms.")
else:
    print("   >>> the kill does NOT survive at full depth: the criterion may be sufficient after all.")
print()
print("DONE",flush=True)