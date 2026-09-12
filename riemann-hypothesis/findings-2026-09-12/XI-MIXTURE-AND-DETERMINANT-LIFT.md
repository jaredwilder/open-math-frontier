# Xi as a positive mixture of PF-infinity atoms and an exact determinant lift

**Author:** Jared Wilder  
**Recovered from:** RH Terminal Encirclement, Round 10  
**Public canonical release:** 2026-09-12  
**Status:** exact representation + exact no-go for the natural positive-integrand route

Let the transformed xi coefficient sequence be

\[
a_k=\frac1{(2k)!}\int_0^\infty u^{2k}\Phi(u)\,du,
\]

with the standard positive Riemann kernel `Phi`.

## 1. Positive mixture of homothetic PF-infinity atoms

Summing before integrating gives

\[
\boxed{
G(z)=\int_0^\infty \Phi(u)\cosh(u\sqrt z)\,du.
}
\]

For fixed `u>0`, Euler's product gives

\[
\boxed{
\cosh(u\sqrt z)
=
\prod_{m=0}^{\infty}
\left(1+\frac{4u^2}{\pi^2(2m+1)^2}z\right).
}
\]

Thus the atomic coefficient sequence

\[
b_k(u)=\frac{u^{2k}}{(2k)!}
\]

is `PF_infinity` for every fixed `u`.

Therefore the Riemann coefficient sequence is an exact **positive continuous mixture of homothetic PF-infinity atoms**.

This does not imply the mixture is `PF_infinity`: coefficientwise positive mixtures do not preserve total positivity in general. A simple two-atom measure can already fail `PF_2`.

## 2. Exact determinant-level lift

Write

\[
b_n(u)=
\begin{cases}
u^{2n}/(2n)!,&n\ge0,\\
0,&n<0.
\end{cases}
\]

Then

\[
a_n=\int_0^\infty b_n(u)\Phi(u)\,du.
\]

By row multilinearity of the determinant and absolute convergence,

\[
\boxed{
D_{r,k}
=
\int_{(0,\infty)^r}
\det[b_{k+j-i}(u_i)]_{i,j=0}^{r-1}
\prod_{i=0}^{r-1}\Phi(u_i)\,du_i.
}
\]

The outer measure is positive. A fixed-sign theorem for the inner determinant would therefore be extremely strong.

## 3. The natural pointwise-positivity route fails already at order two

For `r=2`, symmetrize under `u<->v`:

\[
\mathcal S_{2,k}(u,v)
=b_k(u)b_k(v)
-\frac12\left[b_{k+1}(u)b_{k-1}(v)+b_{k+1}(v)b_{k-1}(u)\right].
\]

For `k>=1`, exact factorial simplification gives

\[
\boxed{
\mathcal S_{2,k}(u,v)
=
\frac{u^{2k-2}v^{2k-2}}{((2k)!)^2}
\left[u^2v^2-\frac{c_k}{2}(u^4+v^4)\right],
}
\]

where

\[
\boxed{
c_k=\frac{(2k)(2k-1)}{(2k+1)(2k+2)}\in(0,1).}
\]

For fixed `v>0` and `u/v -> infinity`, the bracket is negative. For `u=v`, it is positive because `c_k<1`.

Therefore the natural symmetrized row-multilinearity integrand has **both signs**.

Hence:

\[
\boxed{
\text{A direct proof based on pointwise positivity of this natural determinant lift cannot work, already at }r=2.
}
\]

This no-go is narrow: it does not exclude a different integral representation or a cancellation theorem using the special shape of `Phi`.

## 4. Exact tilted-measure coordinate

Let

\[
m_{2k}=\int_0^\infty u^{2k}\Phi(u)\,du,
\qquad
d\nu_k(u)=\frac{u^{2k}\Phi(u)}{m_{2k}}\,du,
\]

and set

\[
X_k=2\log U,\qquad U\sim\nu_k.
\]

Then for every integer `s>=-k`,

\[
\boxed{
\frac{a_{k+s}}{a_k}
=
\frac{\Gamma(2k+1)}{\Gamma(2k+2s+1)}
\mathbb E_{\nu_k}[e^{sX_k}].
}
\]

Consequently, for `k>=r-1`,

\[
\boxed{
\frac{D_{r,k}}{a_k^r}
=
\det_{0\le i,j<r}
\left[
\frac{\Gamma(2k+1)}{\Gamma(2k+2(j-i)+1)}
\mathbb E_{\nu_k}(e^{(j-i)X_k})
\right].
}
\]

If

\[
K_k(s)=\log\mathbb E_{\nu_k}[e^{sX_k}],
\]

each normalized block entry is exactly

\[
\exp\left(K_k(s)+\log\Gamma(2k+1)-\log\Gamma(2k+2s+1)\right),
\qquad s=j-i.
\]

This coordinate explains the regime change: when `k>>r^3`, only a local small-`s/k` cumulant model is needed; at fixed slope `k~alpha r`, the matrix samples the full large-deviation profile at `s/k=O(1)`.

## 5. Novelty status

The integral formula for xi, Euler product for `cosh`, determinant multilinearity, and exponential tilting are classical ingredients. The exact determinant lift, explicit order-two sign-indefinite kernel, and tilted block coordinate are published here as the campaign's specialized synthesis.

The source campaign itself marked the determinant lift as likely a standard technique with application novelty unchecked. This release therefore timestamps the exact formulation and no-go without claiming historical priority.
