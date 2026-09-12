# Exact reciprocal / transposed-rectangle curvature duality

**Author:** Jared Wilder  
**Public canonical release:** 2026-09-12  
**Status:** exact algebraic identity; novelty unresolved

Let

\[
D_{r,k}(a)=\det[a_{k+j-i}]_{i,j=0}^{r-1}
\]

for a coefficient sequence `a` with nonzero leading term.

Normalize

\[
h_n=a_n/a_0,
\qquad
H(z)=\sum_{n\ge0}h_nz^n,
\]

and define the Jacobi–Trudi reciprocal sequence `b` by

\[
\sum_{n\ge0}b_nz^n=\frac1{H(-z)}.
\]

Dual Jacobi–Trudi for rectangular partitions exchanges order and shift:

\[
\boxed{
D_{r,k}(a)=a_0^r D_{k,r}(b)
}
\]

under this normalization convention.

Define the shift curvature

\[
Q_a(r,k)
=\frac{D_{r,k-1}(a)D_{r,k+1}(a)}{D_{r,k}(a)^2}
\]

and the odds variable

\[
Z_a(r,k)
=\frac rk\frac{Q_a(r,k)}{1-Q_a(r,k)}
=\frac rk
\frac{D_{r,k-1}(a)D_{r,k+1}(a)}
{D_{r+1,k}(a)D_{r-1,k}(a)}.
\]

Applying the transposed-rectangle identity to the four neighboring minors gives

\[
\boxed{
Z_a(r,k)Z_b(k,r)=1.
}
\]

Equivalently, using Desnanot–Jacobi on both lattices, the corresponding shift curvatures satisfy the complementary relation

\[
\boxed{
Q_a(r,k)+Q_b(k,r)=1
}
\]

whenever the displayed normalized quantities are defined.

## Compactified-ratio corollary

Set

\[
\theta=\frac{k}{k+r}.
\]

Transposition sends `(r,k)` to `(k,r)`, hence

\[
\theta\longmapsto1-\theta.
\]

Therefore, at ratios where fixed-slope limits exist,

\[
\boxed{
A_a(\theta)A_b(1-\theta)=1.
}
\]

Vanishing of the normalized odds on one side is dual to blow-up on the other.

## Why it matters

The two ends of the determinant lattice are not independent. Any uniform fixed-slope or endpoint theorem can be transported through the reciprocal sequence, converting large-order/small-shift information into small-order/large-shift information and vice versa.

This identity is exact; the existence or positivity of any proposed asymptotic limit is a separate analytic problem.

## Novelty note

Dual Jacobi–Trudi and reciprocal symmetric-function identities are classical. The release claims only the exact specialized curvature identities above as part of this research program; no historical-first claim is made without further literature review.
