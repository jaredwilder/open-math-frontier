# Corrected critical-value / adjacent-gap monotonicity under real-zero heat flow

**Author:** Jared Wilder  
**Recovered from:** RH Terminal Encirclement, Rounds 6–8  
**Public canonical release:** 2026-09-12  
**Status:** exact dynamical identity; corrected strictness condition

The source campaign stated this result as unconditionally strict while adjacent zeros remained real and distinct. A forensic pass found a small boundary case: for a two-zero symmetric configuration, equality can occur. The corrected theorem is below.

## Setup

Let `H_t(z)` be a real entire function evolving by

\[
\partial_tH_t=-\partial_z^2H_t,
\]

and suppose in the time interval under consideration that its relevant zeros are simple and real. Write them in increasing order as `x_j(t)`.

The zero dynamics are

\[
\boxed{
x_j'(t)=2\sum_{k\ne j}\frac1{x_j-x_k}}
\]

under the usual convergence/renormalization assumptions for the entire-function zero sum.

For adjacent zeros `x_j<x_{j+1}`, let

\[
g_j=x_{j+1}-x_j.
\]

Let `c_j` be the critical point between them,

\[
H_t'(c_j)=0,
\qquad
x_j<c_j<x_{j+1},
\]

and set

\[
V_j=H_t(c_j),
\qquad
\mathcal R_j=\frac{|V_j|}{g_j^2}.
\]

## 1. Critical-value energy identity

Because `H_t'(c_j)=0`, differentiation along the moving critical point gives

\[
V_j'=-H_t''(c_j).
\]

For a real-rooted canonical product, at a critical point the logarithmic derivative vanishes and

\[
-\frac{H_t''(c_j)}{H_t(c_j)}
=
\sum_k\frac1{(c_j-x_k)^2}.
\]

Hence

\[
\boxed{
\frac d{dt}\log|V_j|
=
\sum_k\frac1{(c_j-x_k)^2}.
}
\]

This identifies the logarithmic growth of the critical value with an inverse-square zero energy.

## 2. Gap identity

The adjacent-zero dynamics give

\[
\boxed{
\frac d{dt}g_j^2
=
8
-
4g_j^2
\sum_{k\ne j,j+1}
\frac1{(x_j-x_k)(x_{j+1}-x_k)}.
}
\]

## 3. Renormalized ratio derivative

Write

\[
a=c_j-x_j>0,
\qquad
b=x_{j+1}-c_j>0,
\qquad
g=a+b.
\]

Combining the two identities yields

\[
\frac{\mathcal R_j'}{\mathcal R_j}
=
\left(
\frac1{a^2}+\frac1{b^2}-\frac8{(a+b)^2}
\right)
+
\sum_{k\ne j,j+1}
\left[
\frac1{(c_j-x_k)^2}
+
\frac4{(x_j-x_k)(x_{j+1}-x_k)}
\right].
\]

The nearest-pair term factors exactly as

\[
\boxed{
\frac1{a^2}+\frac1{b^2}-\frac8{(a+b)^2}
=
\frac{(a-b)^2(a^2+4ab+b^2)}
{a^2b^2(a+b)^2}
\ge0.
}
\]

For every outer zero `x_k` outside the adjacent interval, the factors

\[
x_j-x_k,\qquad x_{j+1}-x_k
\]

have the same sign, so each outer contribution is strictly positive.

Therefore

\[
\boxed{\mathcal R_j'(t)\ge0.}
\]

Moreover, the inequality is strict if either

1. `a != b`, i.e. the critical point is not the midpoint; or
2. there exists at least one outer real zero contributing to the sum.

Thus for an all-real entire configuration with infinitely many real zeros and convergent/renormalized sums, one obtains

\[
\boxed{\mathcal R_j'(t)>0.}
\]

## 4. Correction to the source claim

The source packet said strict positivity followed whenever the adjacent zeros were distinct and real. That is too broad.

For a quadratic with exactly two symmetric zeros, there are no outer-zero terms and `a=b`, so the derivative is zero. The correct generic finite theorem is **nondecreasing**, with strictness under the explicit conditions above.

The Riemann/de Bruijn–Newman application has an infinite outer zero environment, so this correction does not remove strictness there while the all-real simple-zero product representation and sums are valid.

## 5. What it does and does not imply

This monotonicity is generic real-zero heat-flow geometry. By itself it does not prohibit a positive-time collision and therefore is not an RH close.

Its use is diagnostic: it gives an exact monotone quantity combining critical-value growth and adjacent-gap collapse, with the blow-up mechanism expressed through inverse-square zero energy.

## 6. Novelty status

Rodgers–Tao and earlier de Bruijn–Newman literature contain several gap/energy/Hamiltonian monotonicity identities. A targeted search did not locate this exact local ratio

\[
|H_t(c_j)|/(x_{j+1}-x_j)^2
\]

with the displayed factorization. Because the surrounding literature is extensive, this is published as an exact corrected theorem with **novelty unresolved**, not as a certified historical-first claim.
