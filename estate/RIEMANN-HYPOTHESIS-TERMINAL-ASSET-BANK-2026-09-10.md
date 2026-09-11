# Riemann Hypothesis — Terminal Asset Bank

**Author:** Jared Wilder  
**Campaign date:** 2026-08-11  
**Public release:** 2026-09-10

## Court verdict

**The Riemann Hypothesis is not proved in this packet.** The source ledger itself records

```text
rh_closed: false
```

and names the surviving wall:

> **Compactified-Ratio Collective-Saddle Positivity for consecutive Toeplitz minors.**

Clay Mathematics Institute still lists the Riemann Hypothesis as an unsolved Millennium Prize Problem. This release therefore publishes identities, equivalences, sufficient criteria and killed shortcuts — not a closure claim.

# I. Coefficient / Toeplitz formulation used by the campaign

The campaign works with the standard positive coefficient representation

\[
G(z)=\sum_{k\ge0}a_kz^k
=\frac18\,\xi\!\left(\frac12+\frac{\sqrt z}{2}\right),
\]

where

\[
a_k=\frac1{(2k)!}\int_0^\infty u^{2k}\Phi(u)\,du,
\qquad \Phi(u)>0.
\]

Define consecutive Toeplitz minors

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\qquad a_\ell=0\ \text{for }\ell<0.
\]

The packet takes as external input the standard Pólya-frequency formulation: positivity of all required minors gives `PF_infinity`, which in this coefficient setting is equivalent to RH. A July 2026 external coefficient paper and its certified tail region are treated as inputs, not discoveries of this campaign.

# II. Exact Round-10 PF-atom decomposition

From the moment formula, summing before integrating gives

\[
\boxed{
G(z)=\int_0^\infty\Phi(u)\cosh(u\sqrt z)\,du.
}
\]

For fixed `u>0`,

\[
\cosh(u\sqrt z)
=
\sum_{k\ge0}\frac{u^{2k}}{(2k)!}z^k
=
\prod_{m=0}^\infty
\left(1+\frac{4u^2}{\pi^2(2m+1)^2}z\right).
\]

Therefore each atomic coefficient sequence

\[
b_k(u)=\frac{u^{2k}}{(2k)!}
\]

is `PF_infinity`.

The Riemann coefficient sequence is thus a positive continuous mixture of homothetic `PF_infinity` atoms.

## Terminal no-go: positive mixtures need not stay PF

That observation does **not** prove RH. Positive coefficientwise mixtures of PF sequences need not preserve even `PF_2`.

The packet gives a two-atom counterexample: put mass `0.9` at `u=0` and `0.1` at `u=10`. Then

\[
a_0=1,\qquad a_1=5,\qquad a_2=1000/24,
\]

so

\[
a_1^2-a_0a_2<0.
\]

This permanently kills the shortcut

> positive `Phi` + PF atoms ⇒ PF mixture.

# III. Exact determinant lift

Put

\[
b_n(u)=
\begin{cases}
 u^{2n}/(2n)!,&n\ge0,\\
 0,&n<0.
\end{cases}
\]

Then, by determinant multilinearity and absolute convergence,

\[
\boxed{
D_{r,k}
=
\int_{(0,\infty)^r}
\det[b_{k+j-i}(u_i)]_{i,j=0}^{r-1}
\prod_{i=0}^{r-1}\Phi(u_i)\,du_i.
}
\]

This is the campaign's strongest exact Round-10 identity.

The outer measure is positive. But the inner determinant does **not** have a fixed sign, so the hoped-for direct Andréief/Vandermonde positivity proof fails already at low order.

# IV. RH-equivalent criteria banked in earlier rounds

The source asset ledger records the following items with their original authority labels.

## R2-A — zero transform circle criterion

For a nontrivial zero `rho`,

\[
\Re\rho=\frac12
\iff
\left|\frac{\rho-1}{\rho}\right|=1.
\]

**Authority:** exact algebra.

## R2-C — weighted transformed-zero moment criterion

The packet defines an absolutely convergent weighted transformed-zero moment sequence and proves:

> the moments are bounded by the zeroth moment for every order iff RH.

**Authority:** proof in packet.

This public release preserves the equivalence but does not restate a transformed-moment normalization whose exact notation is not reproduced in the recovered atlas line; the source report/ledger remains the authority for the definition.

## R2-D — Toeplitz PSD hierarchy

The corresponding Toeplitz positive-semidefinite hierarchy from those weighted moments is equivalent to RH.

**Authority:** proof in packet.

## R3-A — genus-zero reduction

\[
\xi(s)=F(s(1-s))
\]

with `F` entire of order `1/2` and genus zero.

**Authority:** standard complex analysis.

## R3-B — Stieltjes moment criterion

The transformed power-sum sequence is a Stieltjes moment sequence iff RH.

**Authority:** Stieltjes moment theorem + analytic continuation argument.

## R3-D — exact logarithmic-derivative calculus identity

For the campaign's transformed coordinate `x` and corresponding `sigma>1`,

\[
h(x)=\frac{\xi'(\sigma)}{(2\sigma-1)\xi(\sigma)}.
\]

**Authority:** exact calculus.

# V. Heat-flow / zero-dynamics assets

## R5-A — real-rooted approximation sufficient criterion

If entire approximants `Xi_N` have only real zeros and converge locally uniformly to `Xi`, then Hurwitz/Rouché/Laguerre–Pólya closure implies RH.

This is an exact **sufficient lemma**. The missing object is a construction having both required properties.

## R6-G — adjacent heat-flow gap identity

The packet derives an exact evolution identity for the gap between adjacent real zeros under the relevant heat flow.

## R7-V — critical-value inverse-square energy identity

At critical points between zeros, the logarithmic derivative of the critical value is expressed as an inverse-square zero-energy sum.

## R8-A — monotone normalized critical ratio

While adjacent zeros remain real and distinct, the packet proves strict increase of

\[
R_j=\frac{|H_t(c_j)|}{g_j^2},
\]

where `c_j` is the intervening critical point and `g_j` the adjacent-zero gap.

### Killed overreach

`R8-A` alone does **not** prohibit a Newman collision. The ledger explicitly marks that attempted RH close as killed by a genericity audit.

# VI. Determinant algebra bank

## R9-A — Desnanot–Jacobi identity

The consecutive minors satisfy

\[
\boxed{
D_{r+1,k}D_{r-1,k}
=
D_{r,k}^2-D_{r,k-1}D_{r,k+1}.
}
\]

The attempted inference that this condensation identity alone propagates known tail positivity inward is marked **killed**.

## T10-6 — rectangular Schur form

The same determinant is the rectangular Schur specialization

\[
D_{r,k}=s_{(k^r)}
\]

under `h_n=a_n`.

**Authority:** Jacobi–Trudi.

## T10-8 — tilted-measure block normalization

Normalized block entries can be written as gamma ratios multiplied by the full moment-generating function of

\[
X_k=2\log U
\]

under the `k`-tilted `Phi` measure.

This recasts the determinant problem as a collective tilted-measure asymptotic problem.

# VII. Negative theorem bank

The campaign publicly preserves the following killed routes:

1. unjustified positive rank-one decomposition of the prime side;
2. crude archimedean domination of the prime kernel;
3. atomwise complete monotonicity / literal prime sum-of-squares strategy;
4. generic derivative-to-function hyperbolicity propagation — killed by explicit counterexample;
5. using monotonicity of `R_j` alone to prohibit Newman collision;
6. using Desnanot–Jacobi condensation alone to propagate tail positivity inward;
7. direct PF-atom mixture closure;
8. fixed-sign determinant-integrand / naïve Andréief–Vandermonde positivity.

Negative results are part of the release because they define the actual frontier.

# VIII. External certified tail and exact surviving wall

The campaign imported a 2026 external result proving

\[
D_{r,k}>0
\qquad
(k\ge10^{18}r^3)
\]

uniformly in `r`.

The complementary regime remained open in the source packet.

The terminal target was therefore frozen as:

> Construct a positive normalization `N_{r,k}` and a positive continuum leading model, uniform in
> \[
> \theta=\frac{k}{k+r}\in[0,1],
> \]
> such that
> \[
> N_{r,k}D_{r,k}
> =F(\theta)(1+\varepsilon_{r,k}),
> \qquad F(\theta)>0,
> \qquad
> \sup_{k\ge0}|\varepsilon_{r,k}|\to0
> \]
> as `r→∞`.

Such a theorem, combined with finite residual verification and the consecutive-minor criterion, would close the coefficient approach.

**It is unproved.** That is the wall, not a disguised proof.

# IX. Current-status boundary

Clay Mathematics Institute still lists the Riemann Hypothesis under its unsolved Millennium Prize Problems. Anthropic's August 2026 announcement likewise described substantial progress on the fraction of critical-line zeros while explicitly stating that its system did not solve RH.

Accordingly, every equivalence and identity in this packet must be read as an **attack surface / criterion / exact transformation**, never as a proof that the required positivity condition has been established.
