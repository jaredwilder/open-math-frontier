# Transformed-zero moment, Toeplitz-PSD, and Stieltjes criteria for RH

**Author:** Jared Wilder  
**Recovered from:** RH Terminal Encirclement, Rounds 2–3  
**Public canonical release:** 2026-09-12  
**Status:** exact/standard-equivalence layer; not claimed novel

This note preserves a clean chain of RH-equivalent moment formulations from the source campaign. The ingredients are classical enough that this release does **not** claim novelty; they are useful because they connect the zero, Toeplitz, and Stieltjes coordinates used elsewhere in the program.

## 1. Reciprocal-spectrum transform

For a nontrivial zero `rho` define

\[
z_\rho=\frac{\rho-1}{\rho}=1-\frac1\rho.
\]

Then

\[
\boxed{
\Re\rho=\frac12
\iff
|z_\rho|=1.
}
\]

The functional-equation symmetries become

\[
\boxed{
z_{1-\rho}=z_\rho^{-1},
\qquad
z_{\bar\rho}=\overline{z_\rho}.}
\]

## 2. Absolutely convergent weighted moments

Set

\[
w_\rho=\frac1{|\rho(1-\rho)|^2}
\]

and

\[
M_n=\sum_\rho w_\rho z_\rho^n.
\]

The weight gives absolute convergence for every fixed `n`.

If RH holds, every transformed zero lies on the unit circle, so by the triangle inequality

\[
|M_n|\le M_0.
\]

Conversely, if RH fails, some transformed zero has modulus `R>1`. Since `|z_rho|->1` with height, a maximal modulus `R>1` is attained among finitely many zeros. The contribution from the finite set on `|z|=R` is a nonzero finite exponential sum; along a subsequence its normalized magnitude has positive limsup. Lower-modulus terms are exponentially smaller. Therefore `|M_n|>M_0` for some sufficiently large `n`.

Hence

\[
\boxed{
RH
\iff
|M_n|\le M_0\quad\text{for every }n\ge1.
}
\]

## 3. Toeplitz PSD criterion

Form

\[
T_N=(M_{j-k})_{j,k=0}^{N}.
\]

Under RH, `M_n` are Fourier moments of a positive discrete measure on the unit circle, so every `T_N` is positive semidefinite.

Conversely, positive semidefiniteness of all such matrices implies in particular the `2 x 2` inequalities

\[
|M_n|\le M_0,
\]

and the preceding criterion gives RH.

Thus

\[
\boxed{
RH
\iff
T_N\succeq0\quad\text{for every }N.
}
\]

This is a different Toeplitz hierarchy from the coefficient-minor Branch-C hierarchy; the two should not be conflated.

## 4. Functional-equation quotient

Set

\[
t=s(1-s).
\]

Since `xi(s)=xi(1-s)`, there is an entire function `F` such that

\[
\boxed{\xi(s)=F(s(1-s)).}
\]

Its order is `1/2`, hence genus zero.

For a nontrivial zero `rho`, put

\[
\tau_\rho=\rho(1-\rho).
\]

Using the absence of nontrivial real zeta zeros in `(0,1)`,

\[
\boxed{
RH
\iff
\text{every zero of }F\text{ is positive real}.
}
\]

## 5. Genus-zero power sums and Stieltjes moments

The genus-zero product gives

\[
-\frac{F'(t)}{F(t)}
=
\sum_j\frac1{\tau_j-t}.
\]

Near the origin,

\[
-\frac{F'(t)}{F(t)}
=
\sum_{n\ge0}m_nt^n,
\qquad
m_n=\sum_j\tau_j^{-(n+1)}.
\]

Under RH, `x_j=1/tau_j` are positive and

\[
m_n=\sum_j x_j^{n+1},
\]

so `(m_n)` is a Stieltjes moment sequence.

Conversely, with the standard determinacy and analytic-continuation argument supplied by the growth of the genus-zero function, the Stieltjes property forces the singular support of the logarithmic derivative to lie on the positive real axis and hence forces all zeros `tau_j` to be positive real.

Therefore

\[
\boxed{
RH
\iff
(m_n)_{n\ge0}\text{ is a Stieltjes moment sequence}.
}
\]

By the classical Stieltjes criterion this is equivalent to

\[
\boxed{
(m_{i+j})_{i,j=0}^{N}\succeq0,
\qquad
(m_{i+j+1})_{i,j=0}^{N}\succeq0
\quad\text{for all }N.
}
\]

## 6. Arithmetic half-plane coordinate

For `x>0`, set

\[
\sigma(x)=\frac{1+\sqrt{1+4x}}2>1.
\]

Then `sigma(1-sigma)=-x`, and differentiation of `xi(s)=F(s(1-s))` gives

\[
\boxed{
-\frac{F'(-x)}{F(-x)}
=
\frac1{2\sigma-1}\frac{\xi'(\sigma)}{\xi(\sigma)}.
}
\]

The right side lies in the absolutely convergent half-plane `sigma>1`, providing a direct arithmetic coordinate for the Stieltjes transform.

## 7. Novelty status

Unit-circle transforms of RH, positive-definite Toeplitz moment criteria, Stieltjes moment characterizations, and quotienting xi by the functional equation all have substantial classical relatives (Li/Chebyshev/Weil/moment literature).

The source campaign itself made **no novelty claim** for these criteria. This release preserves them as exact infrastructure and as bridges among the program's coordinate systems, not as priority claims.
