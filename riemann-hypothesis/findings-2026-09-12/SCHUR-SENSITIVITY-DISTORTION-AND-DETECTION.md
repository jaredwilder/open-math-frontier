# Rectangular Schur sensitivity, distortion, and zero-detection bounds

**Author:** Jared Wilder  
**Recovered from:** RH Encirclement V  
**Public canonical release:** 2026-09-12  
**Status:** exact theorems; novelty unresolved

This note separates three exact rectangular-Schur results that were previously buried inside the larger Encirclement-V report.

## 1. Occupancy-cap / sensitivity theorem

Assume the generating function is in a real-zero Pólya-frequency phase so that

\[
G(z)=a_0\prod_{j\ge1}(1+\alpha_j z),\qquad \alpha_j>0,
\]

and the consecutive Toeplitz minor is represented by

\[
D_{r,k}=a_0^r s_{(r^k)}(\alpha).
\]

Define the logarithmic sensitivity to the zero parameter `alpha_j` by

\[
q_j
:=
\alpha_j\frac{\partial}{\partial\alpha_j}
\log s_{(r^k)}(\alpha).
\]

Because the Schur polynomial has a positive semistandard-tableau expansion, `q_j` is the expected number of appearances of symbol `j` under the tableau Gibbs measure weighted by its monomial.

A rectangle `(r^k)` has `r` columns, and semistandard tableaux are strictly increasing down columns. A fixed symbol can therefore appear at most once in each column. Hence

\[
\boxed{0\le q_j\le r.}
\]

Homogeneity of degree `rk` gives Euler's identity

\[
\boxed{\sum_j q_j=rk.}
\]

For the normalized sensitivities

\[
p_j=\frac{q_j}{rk},
\]

one obtains

\[
\boxed{
0\le p_j\le\frac1k,
\qquad
\sum_jp_j=1.
}
\]

So no individual zero parameter can carry more than `1/k` of the normalized logarithmic sensitivity of a rectangular minor.

## 2. Exact multiplicative distortion bound

Let `alpha_j,beta_j>0` and define

\[
\delta_j=\log(\alpha_j/\beta_j).
\]

Suppose for some `J`

\[
|\delta_j|\le M_J\quad(j\le J),
\]

and

\[
|\delta_j|\le\varepsilon_J\quad(j>J).
\]

Every tableau monomial has exponents `m_j` satisfying

\[
0\le m_j\le r,
\qquad
\sum_jm_j=rk.
\]

Therefore the log ratio of any corresponding pair of monomials lies in

\[
[-rJM_J-\varepsilon_Jrk,
  rJM_J+\varepsilon_Jrk].
\]

All Schur coefficients are nonnegative, so the same extremal bounds hold for the full positive sums:

\[
\boxed{
\left|
\log\frac{s_{(r^k)}(\alpha)}{s_{(r^k)}(\beta)}
\right|
\le
rJM_J+\varepsilon_Jrk.
}
\]

Dividing by area gives

\[
\boxed{
\frac1{rk}
\left|
\log\frac{s_{(r^k)}(\alpha)}{s_{(r^k)}(\beta)}
\right|
\le
\frac{JM_J}{k}+\varepsilon_J.
}
\]

This makes precise the statement that agreement of zero parameters in the tail controls rectangular-minor free-energy density, while finitely many exceptional low parameters cost only `O(1/k)` after area normalization.

## 3. Single-pair detection delay

Suppose all zero parameters are positive real except one conjugate pair

\[
\rho e^{\pm i\theta}.
\]

Every variable exponent in a rectangular tableau is at most `r`. Therefore the absolute phase of every tableau monomial contributed by this pair is at most

\[
r|\theta|.
\]

If

\[
\boxed{r|\theta|<\frac\pi2,}
\]

then every monomial has positive real part. Conjugation symmetry makes the Schur value real, so

\[
\boxed{D_{r,k}>0\quad\text{for every }k.}
\]

Consequently, a Toeplitz minor capable of detecting that conjugate pair through a sign loss must satisfy

\[
\boxed{
r\ge\frac{\pi}{2|\theta|}.}
\]

As the pair approaches the negative real axis (`theta -> 0` in the relevant angular-defect coordinate), the required detecting determinant order diverges.

This gives a quantitative mechanism for escape-to-infinity in determinant order.

## 4. Relation to the top-k theorem

The single-pair bound is the one-defect case of the stronger sorted angular budget

\[
r\sum_{j=1}^k\vartheta_j<\pi/2
\Longrightarrow D_{r,k}>0,
\]

published separately in `TOP-K-ANGULAR-BUDGET.md`.

## 5. Novelty status

The ingredients—semistandard tableaux, positivity of Schur coefficients, homogeneity, and sector arguments—are classical. The targeted literature sweep did not locate these exact sensitivity/distortion/detection statements packaged for rectangular Toeplitz minors.

A relevant nearby 2026 result is Philip B. Zhang's *Normalized skew Schur polynomials are Lorentzian* (arXiv:2608.12266), but its normalization is coefficientwise factorial normalization of a fixed polynomial, not the Plancherel/Poisson rectangle ratio used by the RH hierarchy here.

These results are therefore published as exact surviving mathematics with **historical novelty unresolved**, not as certified first discoveries.
