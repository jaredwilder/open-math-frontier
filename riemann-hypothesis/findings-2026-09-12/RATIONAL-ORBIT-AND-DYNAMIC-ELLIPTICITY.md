# Rational determinant orbit, fixed-slope linearization, and dynamic ellipticity

**Author:** Jared Wilder  
**Recovered from:** RH Encirclements II–IV  
**Public canonical release:** 2026-09-12  
**Status:** exact identities and derived theorems; novelty unresolved

## 1. Exact determinant-odds recurrence

For positive consecutive Toeplitz minors define

\[
R_{r,k}=\frac{D_{r,k-1}D_{r,k+1}}{D_{r,k}^2},
\qquad
A_{r,k}=\frac{D_{r-1,k}D_{r+1,k}}{D_{r,k}^2},
\]

and

\[
Y_{r,k}=\frac{A_{r,k}}{R_{r,k}}.
\]

Desnanot–Jacobi gives

\[
R_{r,k}+A_{r,k}=1,
\]

and the induced odds recurrence is

\[
1+Y_{r+1,k}
=
\frac{Y_{r,k}^2}{1+Y_{r-1,k}}
\frac{(1+Y_{r,k-1})(1+Y_{r,k+1})}
{Y_{r,k-1}Y_{r,k+1}}.
\]

## 2. Exact rational orbit

For constants `mu,nu`, wherever defined,

\[
\boxed{
Y^{\mu,\nu}_{r,k}=\frac{r+\mu}{k+\nu}
}
\]

satisfies the nonlinear recurrence exactly.

The one-sided Toeplitz/factorial boundary selects

\[
\boxed{Y^*_{r,k}=\frac rk.}
\]

The corresponding factorial benchmark is

\[
\boxed{
D^{(0)}_{r,k}=\prod_{j=0}^{r-1}\frac{j!}{(k+j)!}.
}
\]

The same exact orbit simultaneously identifies the natural scales

\[
k\asymp r^3\Rightarrow Y^*\asymp r^{-2},
\qquad
k\asymp r^2\Rightarrow Y^*\asymp r^{-1},
\qquad
k\asymp r\Rightarrow Y^*=O(1).
\]

## 3. Correct fixed-slope continuum

Set

\[
\alpha=k/r
\]

and use

\[
Y_{r,k}=y(\alpha)+r^{-1}z(\alpha)+O(r^{-2}).
\]

Expanding the exact recurrence gives, at first nontrivial order,

\[
\boxed{
(\alpha^2y+1)p''
+2\alpha y p'
+\frac{y(\alpha^2-1)}{y+1}(p')^2=0,
\qquad p=\log y.
}
\]

The factorial orbit selects

\[
\boxed{y(\alpha)=\alpha^{-1}.}
\]

At next order,

\[
\boxed{
\alpha^2z''+4\alpha z'+2z=0,
}
\]

so

\[
\boxed{
z(\alpha)=A/\alpha+B/\alpha^2.}
\]

Those two correction directions are exactly tangent to the shifted rational family

\[
\frac{r+\mu}{k+\nu}
=
\frac1\alpha
+\frac1r
\left(\frac\mu\alpha-\frac\nu{\alpha^2}\right)
+O(r^{-2}).
\]

## 4. Exact normalized map and linearization

Normalize by the factorial orbit:

\[
Z^{\rm II}_{r,k}=\frac{k}{r}Y_{r,k}.
\]

Then the benchmark is the exact fixed field

\[
\boxed{Z^{\rm II}_{r,k}=1.}
\]

Linearizing around it with `Z=1+epsilon` yields the exact one-step Jacobian

\[
\frac{\partial Z_{r+1,k}}{\partial Z_{r-1,k}}
=-\frac{(r-1)(k+r+1)}{(r+1)(k+r-1)},
\]

\[
\frac{\partial Z_{r+1,k}}{\partial Z_{r,k-1}}
=-\frac{(k-1)(k+r+1)}{(r+1)(k+r-1)},
\]

\[
\frac{\partial Z_{r+1,k}}{\partial Z_{r,k}}
=\frac{2(k+r+1)}{r+1},
\qquad
\frac{\partial Z_{r+1,k}}{\partial Z_{r,k+1}}
=-\frac{k+1}{r+1}.
\]

At fixed slope `k=alpha r`, the frozen linearized recurrence becomes

\[
\boxed{
\varepsilon_{r+1,k}
=-\varepsilon_{r-1,k}
-\alpha\varepsilon_{r,k-1}
+2(\alpha+1)\varepsilon_{r,k}
-\alpha\varepsilon_{r,k+1}+o(1).
}
\]

For a local Fourier mode

\[
\varepsilon\sim\lambda^r e^{i\theta k},
\]

one obtains

\[
\boxed{
\lambda+\lambda^{-1}=2+4\alpha\sin^2(\theta/2),
}
\]

or

\[
\boxed{
\omega(\theta;\alpha)
=2\operatorname{arsinh}(\sqrt\alpha\,|\sin(\theta/2)|),
\qquad
\lambda_\pm=e^{\pm\omega}.
}
\]

For longest wavelengths `theta=O(r^{-1})`, one has `r omega=O(1)`. Thus normalization by the exact orbit removes the spurious long-wave `exp(c sqrt(r))` instability produced by an earlier mis-scaled background analysis. High-frequency modes remain unstable and require additional regularity control.

## 5. Dynamic ellipticity along the de Bruijn–Newman coefficient flow

Under the coefficient deformation

\[
\partial_t a_k=(2k+2)(2k+1)a_{k+1},
\]

write

\[
U_{r,k}(t)=\log\frac{D_{r,k}(t)}{B_{r,k}},
\qquad
V_{r,k}=\partial_tU_{r,k}.
\]

Differentiating the normalized Desnanot–Jacobi equation gives exactly

\[
\boxed{
R^D_{r,k}\Delta_k^2V_{r,k}
+A^D_{r,k}\Delta_r^2V_{r,k}=0.
}
\]

Thus the homotopy velocity is discrete harmonic in the adaptive determinant metric whenever the surrounding minors are positive.

Differentiating once more, with `W=partial_t^2 U`, gives

\[
\boxed{
R^D\Delta_k^2W+A^D\Delta_r^2W
=-R^D(\Delta_k^2V)^2-A^D(\Delta_r^2V)^2\le0.
}
\]

So the second time derivative is superharmonic with an explicit nonpositive quadratic source.

## 6. No bounded first nucleation

Combine dynamic ellipticity with the finite-domain boundary-homotopy theorem. If a finite boundary remains positive throughout the homotopy, a first interior zero cannot occur inside that bounded domain.

Therefore any hypothetical first-loss sequence that survives all finite positive boundaries must escape determinant-index space:

\[
\boxed{(r_n,k_n)\to\infty.}
\]

With independent large-shift and fixed-shift positivity frontiers, this sharpens to a genuinely two-scale obstruction in which both coordinates must grow.

## 7. Novelty status

Desnanot–Jacobi, Toda/octrahedron recurrences and discrete harmonic principles have extensive classical literature. The exact rational two-parameter orbit, its tangent fixed-slope continuum, the displayed normalized dispersion relation, and the adaptive heat-flow ellipticity are released here as exact mathematics from the campaign.

A targeted audit has not established historical priority for these specialized formulations. They are therefore timestamped and published with **novelty unresolved**, rather than either suppressed or overclaimed.
