# RH Odds-Lattice Rational-Orbit Asset

**Author:** Jared Wilder  
**Public release:** 2026-09-10

## Status first

This is an exact recurrence asset from the RH terminal campaign. **It does not prove RH.** The final analytic tube lemma remains unproved.

## Exact recurrence

The odds lattice is

\[
1+Y_{r+1,k}
=
\frac{Y_{r,k}^2}{1+Y_{r-1,k}}
\frac{(1+Y_{r,k-1})(1+Y_{r,k+1})}
{Y_{r,k-1}Y_{r,k+1}}.
\]

## Exact two-parameter rational orbit

The recurrence has the exact family

\[
\boxed{Y^{\mu,\nu}_{r,k}=\frac{r+\mu}{k+\nu}.}
\]

The canonical benchmark

\[
\boxed{Y^*_{r,k}=r/k}
\]

arises from the `PF_infinity` coefficient sequence

\[
a_k=1/k!.
\]

## Normalization

Set

\[
Z_{r,k}=\frac{k}{r}Y_{r,k}.
\]

Then the benchmark is simply

\[
Z\equiv1.
\]

At fixed slope `k/r -> alpha`, the archived frozen linearization around the benchmark has dispersion

\[
\boxed{\lambda+\lambda^{-1}
=2+4\alpha\sin^2(\theta/2).}
\]

For the longest spatial waves

\[
\theta\asymp1/r,
\]

the corresponding amplification across `O(r)` determinant generations is only

\[
e^{O(1)},
\]

rather than an `e^{c\sqrt r}` instability.

## Unproved terminal close lemma

The source campaign froze the following remaining target.

For each compact `alpha` interval, construct an analytic/Gevrey norm and an exact shifted orbit `B^{mu,nu}` such that the normalized nonlinear recurrence preserves a tube

\[
\boxed{\|Y/B^{\mu,\nu}-1\|_{\mathcal A}<\delta<1.}
\]

Then show that the Riemann odds field enters this tube from an overlap region using the certified analytic-continuation / saddle estimates for the coefficient potential.

Combined with the archived cubic tail and the other residual strictness gates, such a theorem could extend the positivity region relevant to the RH coefficient program.

**Court status:** `UNPROVED`.

This file exists so the exact solvable recurrence family and the actual remaining lemma are public separately from any RH closure rhetoric.