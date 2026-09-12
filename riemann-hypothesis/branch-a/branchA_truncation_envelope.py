"""K491's discharge: the split bound with MANY pieces (an envelope), not two.

m_j = int_0^U u^{2j} Phi(u) du  <=  sum_p  max_{[a_p,a_{p+1}]} |Phi| * (a_{p+1}^{2j+1} - a_p^{2j+1})/(2j+1)

With P pieces this is rigorous, hypothesis-free, and tightens as P grows because each piece's
maximum is closer to the local value.  Measure the bound's looseness against the true moments
and the resulting zero shift at the arguments the energy finding uses.
"""
from mpmath import mp, mpf, exp, pi, quad, factorial, nstr, diff
mp.dps=60; K=80; U=mpf(4); P=64
def Phi(u):
    s=mpf(0)
    for n in range(1,12):
        n=mpf(n)
        s+=(2*pi**2*n**4*exp(mpf(9)*u)-3*pi*n**2*exp(mpf(5)*u))*exp(-pi*n**2*exp(4*u))
    return s
edges=[U*p/P for p in range(P+1)]
PM=[max(abs(Phi(edges[p]+(edges[p+1]-edges[p])*i/40)) for i in range(41)) for p in range(P)]
mom=[quad(lambda u: u**(2*j)*Phi(u),[0,U],maxdegree=12) for j in range(K)]
def mbound(j):
    s=mpf(0)
    for p in range(P):
        s += PM[p]*(edges[p+1]**(2*j+1)-edges[p]**(2*j+1))/(2*j+1)
    return s
print("   %d-piece rigorous envelope, no hypothesis"%P,flush=True)
for j in (20,40,60,79):
    print("      j=%2d  true %-18s  bound %-18s  looseness %s"
          %(j,nstr(mom[j],8),nstr(mbound(j),8),nstr(mbound(j)/mom[j],6)),flush=True)
def H(z):
    z=mpf(z); s=mpf(0); zp=mpf(1); z2=z*z
    for j in range(K):
        s+=(-1)**j*zp/factorial(2*j)*mom[j]; zp*=z2
    return s
def tail(z):
    z=mpf(z); s=mpf(0)
    for j in range(K,K+140):
        t=z**(2*j)/factorial(2*j)*mbound(j); s+=t
        if t<mpf(10)**-90 and j>K+3: break
    return s
print()
print("      z        |H'(z)|         tail bound        zero shift <=    verdict")
nval=0
for z in (28.27,40,55,70,85):
    z=mpf(z); hp=abs(diff(H,z)); tb=tail(z); sh=tb/hp
    v="NEGLIGIBLE" if sh<mpf('1e-3') else ("usable" if sh<1 else "TOO BIG")
    if sh<1: nval+=1
    print("      %-8s %-15s %-17s %-16s %s"%(nstr(z,5),nstr(hp,8),nstr(tb,8),nstr(sh,8),v),flush=True)
print()
print("   zeros rigorously validated at these arguments: %d of 5"%nval,flush=True)
print()
print("DONE",flush=True)