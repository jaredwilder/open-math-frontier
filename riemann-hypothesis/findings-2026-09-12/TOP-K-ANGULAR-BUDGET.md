# Top-k angular budget theorem for rectangular Toeplitz minors

**Author:** Jared Wilder  
**Recovered from:** RH Encirclement V, Round 9  
**Public canonical release:** 2026-09-12  
**Status:** PROVED IN SOURCE CAMPAIGN; novelty unresolved

Assume a consecutive Toeplitz minor is represented in the zero-parameter coordinate by a rectangular Schur polynomial of shape `(r^k)`.

Let the absolute angular defects of the relevant complex zero parameters be sorted

\[
\vartheta_1\ge\vartheta_2\ge\cdots\ge0.
\]

A semistandard tableau monomial of shape `(r^k)` has total degree `rk`, while the exponent of any individual variable is at most `r` because columns are strictly increasing.

Therefore the largest possible total absolute phase is obtained by spending the available exponent budget `r` on the `k` largest angular defects. Hence every tableau monomial satisfies

\[
\boxed{
|\arg M|\le r\sum_{j=1}^{k}\vartheta_j.
}
\]

Consequently, if

\[
\boxed{
r\sum_{j=1}^{k}\vartheta_j<\frac{\pi}{2},
}
\]

then every tableau monomial lies in the open right half-plane. Their positive-coefficient sum therefore has positive real part, and in particular the rectangular Schur polynomial—and hence the corresponding consecutive Toeplitz minor—is strictly positive:

\[
\boxed{
r\sum_{j=1}^{k}\vartheta_j<\frac{\pi}{2}
\quad\Longrightarrow\quad
D_{r,k}>0.
}
\]

## Detection interpretation

A determinant at scale `(r,k)` cannot change sign through phase accumulation while the top-`k` angular budget remains below `pi/2`.

Thus any phase-driven first-loss mechanism at that scale must satisfy

\[
\boxed{
\sum_{j=1}^{k}\vartheta_j\ge \frac{\pi}{2r}.
}
\]

This is sharper than charging every angular defect: only the `k` largest defects can saturate the rectangle's universal monomial occupancy budget.

## Frontier

If a hypothetical loss sequence escapes with both `r,k -> infinity`, finite information about any fixed number of low zeros is not by itself enough: the relevant positivity test samples an increasing top-`k` angular budget.

The resulting analytic target is control of

\[
r\sum_{j=1}^{k}\vartheta_j(t)
\]

in the two-scale regime.

## Novelty note

Classical sector/phase criteria for Pólya-frequency and real-rootedness problems are nearby prior art. The precise semistandard-tableau top-`k` occupancy sharpening above was not located in the targeted sweep, but this release does not claim historical priority without a specialist symmetric-function/total-positivity review.
