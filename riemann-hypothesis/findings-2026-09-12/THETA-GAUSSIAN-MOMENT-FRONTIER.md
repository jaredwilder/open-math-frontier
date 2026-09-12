# Theta/Gaussian moment frontier for the Branch-C criterion

**Author:** Jared Wilder  
**Public canonical release:** 2026-09-12  
**Status:** exact reduction + certified finite inequalities + explicit open analytic bridge

This note isolates the surviving theta-kernel mathematics behind the order-one row of the determinant program and states the missing analytic theorem without promoting numerical agreement to proof.

## 1. Even moments and the sharp Gaussian benchmark

Let

\[
I_{2k}=\int_0^\infty x^{2k}K(x)\,dx
\]

for the positive theta-derived kernel used by the campaign.

The binding order-one inequality reduces to

\[
\boxed{
\frac{I_{2k-2}I_{2k+2}}{I_{2k}^2}
\le
\frac{2k+1}{2k-1}
}
\qquad(k\ge1).
\]

The right side is the exact Gaussian/Gamma benchmark. Define

\[
\boxed{
J_k=\frac{I_{2k}}{\Gamma(k+1/2)}.
}
\]

Using

\[
\frac{\Gamma(k-1/2)\Gamma(k+3/2)}{\Gamma(k+1/2)^2}
=\frac{2k+1}{2k-1},
\]

the weighted row is exactly equivalent to ordinary log-concavity:

\[
\boxed{
J_{k-1}J_{k+1}\le J_k^2.
}
\]

This is an exact algebraic normalization, not an asymptotic statement.

## 2. Certified finite theta inequalities

The source campaign's rational interval verifier gives

\[
\boxed{
3I_2^2-I_0I_4
\in
[3.144319836807\times10^{-4},
 5.675693447454\times10^{-4}]
}
\]

and hence rigorous positivity for the first full-kernel rung under the stated enclosure method.

A separate four-rung certificate gives positive intervals:

\[
\begin{array}{c|c}
k&\text{certified interval}\\\hline
1&[1.56335252,1.96426203]\times10^{-3}\\
2&[1.73415563,2.24619876]\times10^{-3}\\
3&[2.72502080,3.63976614]\times10^{-3}\\
4&[5.87924581,8.13406217]\times10^{-3}.
\end{array}
\]

The archived verifier includes both the theta-series remainder and the truncation tail in these enclosures.

The higher-theta-term relative tail is separately certified by

\[
\boxed{
0.002477138004562849053<\frac1{300}.
}
\]

These are finite certified inequalities. They are not a proof of the all-`k` row.

## 3. Continuous log-moment curvature

Introduce the continuous moment interpolation

\[
M(s)=\int_0^\infty x^sK(x)\,dx
\]

where differentiation under the integral is justified.

Let `mu_s` be the tilted probability measure

\[
d\mu_s(x)=\frac{x^sK(x)}{M(s)}\,dx.
\]

Then

\[
\frac{d}{ds}\log M(s)
=\mathbb E_s[\log x],
\]

and exactly

\[
\boxed{
\frac{d^2}{ds^2}\log M(s)
=\operatorname{Var}_{\mu_s}(\log x).
}
\]

Thus curvature of the continuous log-moment function is a tilted log-variance.

## 4. Discrete versus continuous: the load-bearing distinction

The desired row inequality is a **finite difference** statement at spacing two in the moment exponent. The variance identity above is a **pointwise differential** identity.

A pointwise bound on

\[
(\log M)''(s)
\]

does not automatically give the required discrete inequality unless it is integrated with the correct comparison benchmark across the full interval joining the neighboring exponents.

Likewise, agreement of a measured moment-ratio excess with a measured tilted variance is not an exact bridge unless the discretization/error terms are controlled.

This distinction is one of the places where the source campaign's later certificate status outran its dependency chain.

## 5. Why the naive global Brascamp-Lieb route fails

Write the tilted measure in log-coordinate `y=log x` as

\[
d\nu_s(y)\propto e^{-V_s(y)}\,dy.
\]

The campaign explicitly found that the relevant tilted density becomes **log-convex in a far-left region**. Equivalently, the potential is not uniformly strongly convex on the whole real line.

Therefore a global Brascamp-Lieb/Poincare bound of the form

\[
V_s''(y)\ge c>0\quad\text{for all }y
\Longrightarrow
\operatorname{Var}_{\nu_s}(y)\le c^{-1}
\]

cannot simply be invoked: its hypothesis fails in the actual tail.

## 6. Curvature at the mode is not a variance theorem

The later campaign established or numerically supported lower bounds for curvature at the moving mode. But

\[
V_s''(y_{\rm mode})\ge c
\]

at one point does **not** imply

\[
\operatorname{Var}_{\nu_s}(y)\le c^{-1}.
\]

The archived state itself observed that reciprocal mode curvature tracked the measured variance from below, not in the direction needed to upper-bound that variance.

So the substitution

> mode curvature bound => global variance bound

is not a valid completed implication.

## 7. The exact missing theorem

A viable repair must localize the measure to a region of controlled convexity and pay rigorously for the discarded tail.

A complete argument needs, uniformly in the relevant moment/tilt parameter:

1. a rigorous crossing point beyond which the potential has the required convexity;
2. a quantitative bound on the excluded far-left mass;
3. bounds on the excluded first and second log-moments;
4. an explicit inequality transferring the restricted variance estimate to the full measure;
5. integration of that continuous estimate strongly enough to recover the discrete Gaussian-normalized log-concavity inequality.

The campaign proposed this strategy but did not close all five items.

## 8. Current mathematical status

What survives is stronger than a numerical curiosity:

- an exact Gaussian/Gamma normalization;
- exact reduction to log-concavity of `J_k`;
- a continuous tilted-variance identity;
- several rigorous finite theta-kernel certificates;
- an explicit diagnosis of why global strong log-concavity fails;
- a precise localization theorem whose proof would materially advance the Branch-C route.

What does **not** survive is the claim that curvature at the mode already closes the global variance/discrete-moment step.

This file therefore records an exact analytic frontier, not an RH proof.
