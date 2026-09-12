"""K509: a control whose zero structure is VERIFIED for the object actually computed.

Take kernels that are FINITE SUMS of delta-like atoms -> the transform is a trigonometric
polynomial with exactly computable zeros:

   kern = sum_p w_p delta(u - u_p)   =>   H(z) = sum_p w_p cos(z u_p)

With commensurable u_p = p*h this is a real polynomial in cos(zh) / Chebyshev, whose zero
structure is EXACTLY computable by polynomial root finding.  No truncation ambiguity: the
transform IS the finite sum.

Build two verified controls:
  REAL:    weights making the Chebyshev polynomial have all roots in [-1,1]
  COMPLEX: weights making some roots leave [-1,1]  (then those z are complex)
Verify each by root-finding, then test whether the pair energy on the REAL zeros separates.
"""
from mpmath import mp, mpf, mpc, cos, acos, pi, polyroots, nstr
mp.dps=30
h=mpf(1)/2
def zeros_and_verify(w):
    n=len(w)-1
    C=[[mpf(0)]*(n+1) for _ in range(n+1)]
    C[0][0]=mpf(1)
    if n>=1: C[1][1]=mpf(1)
    for k in range(2,n+1):
        for i in range(k+1):
            C[k][i]=(2*C[k-1][i-1] if i>=1 else mpf(0))-C[k-2][i]
    co=[mpf(0)]*(n+1)
    for p in range(n+1):
        for i in range(n+1):
            co[i]+=w[p]*C[p][i]
    poly=[co[n-i] for i in range(n+1)]
    rts=polyroots(poly,maxsteps=300,extraprec=300)
    inb=[r for r in rts if abs(mp.im(r))<mpf(10)**-18 and -1<=mp.re(r)<=1]
    out=[r for r in rts if not(abs(mp.im(r))<mpf(10)**-18 and -1<=mp.re(r)<=1)]
    zs=sorted(acos(mp.re(r))/h for r in inb)
    return zs,len(inb),len(out)
CTRL={
 "REAL  (all roots in [-1,1])": [mpf(0),mpf(0),mpf(0),mpf(0),mpf(1)],
 "REAL2 (T_6)":                 [mpf(0)]*6+[mpf(1)],
 "COMPLEX (T_4 + 3)":           [mpf(3),mpf(0),mpf(0),mpf(0),mpf(1)],
 "MIXED (T_4 + 0.5)":           [mpf('0.5'),mpf(0),mpf(0),mpf(0),mpf(1)],
}
print("      control                        real z   out-of-band roots   VERIFIED     pair energy")
for nm,w in CTRL.items():
    zs,ni,no=zeros_and_verify(w)
    e=mpf(0)
    for i in range(len(zs)):
        for j in range(i+1,len(zs)):
            if zs[j]!=zs[i]: e+=1/(zs[j]-zs[i])**2
    ver = "all real" if no==0 else "%d COMPLEX"%no
    print("      %-30s %3d      %3d                 %-12s %s"%(nm,ni,no,ver,nstr(e,10)),flush=True)
print()
print("   These controls are EXACT: the transform is a finite sum, the polynomial is solved,")
print("   and the count of roots outside [-1,1] is the verified number of complex z.")
print()
print("DONE",flush=True)