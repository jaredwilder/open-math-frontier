# One-linear-factor theorem for the Poisson-normalized hierarchy

**Author:** Jared Wilder  
**Public release:** 2026-09-12  
**Status:** PROVED HERE

## Theorem

Let

\[
H(z)=e^{\gamma z}(1+\alpha z),
\qquad \gamma>0,\ \alpha\ge0,
\]

and write

\[
H(z)=\sum_{n\ge0}a_nz^n.
\]

For

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\]

one has for every `r>=1`, `k>=1`

\[
\boxed{
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^{2}.
}
\]

If `alpha>0`, the normalized inequality is strict.

Equivalently, the Poisson-normalized minors

\[
R_{r,k}=\frac{D_{r,k}}{D^{(0)}_{r,k}},
\qquad
D^{(0)}_{r,k}=\gamma^{rk}\prod_{j=0}^{r-1}\frac{j!}{(k+j)!},
\]

are log-concave in `k` for every determinant order `r`.

## Proof

Set

\[
x=\frac{\alpha}{\gamma}.
\]

Since

\[
a_n=\frac{\gamma^n}{n!}(1+nx),
\]

the geometric factor `gamma^n` contributes the common determinant factor `gamma^(rk)`. It therefore cancels from `R_{r,k}`, so it is enough to take `gamma=1`.

By Jacobi–Trudi,

\[
D_{r,k}=s_{(k^r)}(\rho),
\]

where the complete-symmetric generating function of `rho` is

\[
H_\rho(z)=e^z(1+xz).
\]

Regard `rho` as the sum of the Plancherel specialization `Pl` with `H_Pl(z)=e^z` and the one-dual-variable specialization `eta` with `H_eta(z)=1+xz`.

The skew-Cauchy/Jacobi–Trudi addition formula gives

\[
s_{(k^r)}(\mathrm{Pl}+\eta)
=\sum_{\mu\subseteq(k^r)}
 s_\mu(\mathrm{Pl})s_{(k^r)/\mu}(\eta).
\]

For a single dual variable, the skew term is nonzero exactly when `(k^r)/mu` is a vertical strip. For a rectangle there is exactly one such partition of each strip size `t=0,...,r`:

\[
\mu_t=(k^{r-t},(k-1)^t),
\]

and

\[
s_{(k^r)/\mu_t}(\eta)=x^t.
\]

At Plancherel specialization,

\[
s_\lambda(\mathrm{Pl})=\frac{f^\lambda}{|\lambda|!}=\frac1{H_\lambda},
\]

where `H_lambda` is the hook-length product. A direct hook-length ratio for the rectangle and `mu_t` gives

\[
\frac{s_{\mu_t}(\mathrm{Pl})}{s_{(k^r)}(\mathrm{Pl})}
=\binom rt (k)_t,
\]

with `(k)_t=k(k+1)...(k+t-1)` the rising factorial.

Therefore

\[
\boxed{
R_{r,k}(x)
=\sum_{t=0}^r\binom rt(k)_t x^t.
}
\]

Using `(-r)_t=(-1)^t r!/(r-t)!`, this is

\[
R_{r,k}(x)
={}_2F_0(-r,k;;-x).
\]

For `x>0`, the standard Charlier polynomial normalization

\[
C_r(y;a)={}_2F_0(-r,-y;;-1/a)
\]

therefore gives

\[
\boxed{
R_{r,k}(x)=C_r(-k;1/x).
}
\]

For `a>0`, Charlier polynomials are orthogonal with respect to the positive Poisson measure on the nonnegative integers. Hence all `r` zeros of `C_r(y;a)` are real, simple, and positive.

Writing those zeros as `xi_1,...,xi_r>0`, the polynomial in the shift `k` has the form

\[
R_{r,k}(x)=c\prod_{j=1}^r(k+\xi_j),
\qquad c>0.
\]

Thus for every real `k>=0`,

\[
\frac{d^2}{dk^2}\log R_{r,k}(x)
=-\sum_{j=1}^r\frac1{(k+\xi_j)^2}<0.
\]

So `R_{r,k}` is strictly log-concave on the nonnegative real axis and in particular

\[
R_{r,k}^2>R_{r,k-1}R_{r,k+1}
\qquad(k\ge1).
\]

Multiplying back by the Poisson benchmark, whose neighboring ratio is `k/(k+r)`, yields

\[
(k+r)D_{r,k-1}D_{r,k+1}<kD_{r,k}^2.
\]

When `alpha=0`, `R_{r,k}=1` and equality holds. QED.

## Checks

The closed form reproduces, for example,

\[
R_{2,k}=1+2kx+k(k+1)x^2,
\]

\[
R_{3,k}=1+3kx+3k(k+1)x^2+k(k+1)(k+2)x^3.
\]

The formula was independently checked symbolically on small rectangles before publication.

## Novelty status

The Charlier hypergeometric identity and the location of Charlier zeros are classical. The potential new content is the identification of the one-linear-factor Laguerre–Pólya Toeplitz rectangles with this Charlier polynomial in the **shift parameter**, and its use to prove the higher-order Poisson-normalized hierarchy for all `(r,k)` in this subfamily.

A targeted search before release did not locate this exact Toeplitz/rectangular formulation. This is not a claim that no equivalent statement exists elsewhere.

## Why it matters for the RH program

The theorem proves the conjectural hierarchy on the first nontrivial entire Laguerre–Pólya-I deformation of the pure exponential, at every determinant order and shift. It upgrades earlier finite symbolic checks of one-factor examples to a uniform theorem.

The next structural question is whether adding a second dual/linear factor preserves the normalized hierarchy. The simple one-variable Charlier real-rootedness proof does not automatically extend: for multiple factors the normalized rectangle is a higher-degree multivariate specialization rather than the same one-parameter orthogonal polynomial.
