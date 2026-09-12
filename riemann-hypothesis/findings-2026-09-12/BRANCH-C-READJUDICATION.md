# Branch C readjudication — valid sufficient criterion, incomplete analytic proof

**Author:** Jared Wilder  
**Public canonical release:** 2026-09-12  
**Status:** forensic correction; RH remains open

## Executive result

The epoch-23 statement that Branch C had been refuted was based on a domain mismatch.

The falsifier used **finite polynomials**, tested only an **interior subset** of their finite Toeplitz lattices, and then treated surviving examples as counterexamples to an implication whose load-bearing setting is an **infinite coefficient sequence with `a_k>0` at every index**.

A fresh seeded rerun reproduced the old count and simultaneously exposed the mismatch:

```text
seeded non-real-rooted polynomials tested: 2284
interior hits for original criterion: 1445
hits violating everywhere-positive coefficient premise: 1445
```

Thus **1445/1445** purported counterexamples lie outside the global hypothesis relevant to xi.

This restores Branch C as a valid sufficient-criterion route. It does **not** complete RH, because the criterion itself was not proved globally for the xi coefficients.

## 1. Global criterion

Let

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\qquad a_n=0\ (n<0),
\]

with `D_{0,k}=1`.

The criterion is

\[
\boxed{
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
}
\qquad(r,k\ge1).
\]

Desnanot–Jacobi gives

\[
D_{r+1,k}D_{r-1,k}
=D_{r,k}^2-D_{r,k-1}D_{r,k+1},
\]

so the criterion is equivalently

\[
\boxed{
rD_{r,k-1}D_{r,k+1}
\le kD_{r+1,k}D_{r-1,k}.}
\]

## 2. Strict consecutive-minor induction

Assume

\[
a_k>0\qquad(k\ge0)
\]

and the criterion for all `r,k>=1`.

Then

\[
D_{r,k-1}D_{r,k+1}
\le\frac{k}{k+r}D_{r,k}^2,
\]

hence

\[
\boxed{
D_{r+1,k}D_{r-1,k}
\ge\frac{r}{k+r}D_{r,k}^2.
}
\]

The base rows are

\[
D_{0,k}=1,
\qquad
D_{1,k}=a_k>0.
\]

Therefore induction in `r` yields

\[
\boxed{D_{r,k}>0\quad(r\ge0,k\ge1).}
\]

At `k=0`, the Toeplitz block is triangular with diagonal `a_0`, so `D_{r,0}=a_0^r>0`.

Thus the global criterion forces the full strict consecutive-minor lattice.

## 3. Classical promotion to total positivity

Schoenberg's strict consecutive-minor criterion, quoted explicitly in Katkova's 2005 paper *Multiple positivity and the Riemann zeta-function*, says that positivity of the required consecutive minors through order `m` promotes to positivity of all minors through order `m` for the Toeplitz setting.

Applying this at every finite order gives `PF_infinity`.

For the transformed xi generating function, the classical Aissen–Schoenberg–Whitney–Edrei / Laguerre–Pólya characterization supplies the real-zero bridge.

Therefore the top implication is genuine:

\[
\boxed{
\text{global Branch-C criterion for xi}
\Longrightarrow PF_\infty
\Longrightarrow RH.
}
\]

The classical theorem is infrastructure, not claimed novel here.

## 4. Why the epoch-23 falsifier misses the theorem

The audit source explicitly contains a boundary exclusion of the form

```python
if k+r+1 >= N:
    continue
```

for a coefficient vector of finite length `N`.

But every such polynomial satisfies

\[
a_N=0,
\qquad
D_{1,N}=0,
\]

and therefore cannot satisfy the everywhere-positive premise used in the induction above.

The `1686/3059` and `1445/2284` computations remain valid statements about their finite/interior test domain. They simply are not counterexamples to the infinite strict criterion.

Likewise `1+z^5` correctly refutes

> nonnegative consecutive minors imply total positivity,

but says nothing against the **strict** consecutive-minor theorem.

## 5. Why this still does not prove RH

The epoch-22 label that the lower half was complete also fails forensic review. The source state itself preserved open or computation-supported links:

1. **Order/local ascent:** ascent was measured at sampled entries; a general proof was left open.
2. **Order arm to variance:** the moment excess was matched to tilted-log variance only approximately, with exact error terms left open.
3. **Theta-vs-Gaussian variance comparison:** desired globally, observed numerically, not proved.
4. **Far-left tail:** the tilted density becomes log-convex there, invalidating the naive global Brascamp–Lieb hypothesis.
5. **Localization repair:** the campaign proposed restricting to the convex region but did not rigorously pay all crossing, discarded-mass and variance-error terms.
6. **Mode-curvature substitution:** curvature at one moving mode was later promoted as though it controlled global variance; that implication is not valid without a localization theorem.

So the correct state is

\[
\boxed{
\text{the determinant criterion is sufficient for RH, but is not proved globally for xi.}
}
\]

## 6. Current proof obligations

The live route is now precise:

- prove or refute the Poisson-normalized higher-order log-concavity hierarchy on the actual xi determinant lattice;
- close the theta-measure localization/variance estimate with explicit tail error;
- prove the higher-order/order-ascent bridge exactly rather than by measured agreement;
- then invoke the strict total-positivity theorem.

The correct adversarial counterexample class is the actual infinite-support hypothesis class, not terminating polynomials with their boundary removed.
