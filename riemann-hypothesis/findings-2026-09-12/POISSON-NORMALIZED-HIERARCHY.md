# Higher-order Poisson-normalized Toeplitz-minor hierarchy

**Author:** Jared Wilder  
**Public release:** 2026-09-12  
**Status:** exact reformulation + RH sufficiency reduction; general hierarchy remains conjectural

## 1. Consecutive Toeplitz minors

Let

\[
D_{r,k}(a)=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\qquad a_n=0\ (n<0).
\]

For the pure exponential / Poisson benchmark

\[
a^{(0)}_k=\frac1{k!},
\]

the rectangular determinant is

\[
\boxed{
D^{(0)}_{r,k}
=\prod_{j=0}^{r-1}\frac{j!}{(k+j)!}.
}
\]

A direct factorial cancellation gives

\[
\boxed{
\frac{D^{(0)}_{r,k-1}D^{(0)}_{r,k+1}}
{(D^{(0)}_{r,k})^2}
=\frac{k}{k+r}.
}
\]

## 2. Branch-C criterion = normalized log-concavity

The Branch-C inequality is

\[
\boxed{
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^{2}
}
\qquad(r,k\ge1).
\]

Define the Poisson-normalized minor

\[
R_{r,k}=\frac{D_{r,k}}{D^{(0)}_{r,k}}.
\]

Substitution of the benchmark identity gives the exact equivalence

\[
\boxed{
R_{r,k-1}R_{r,k+1}\le R_{r,k}^{2}.
}
\]

Equivalently,

\[
\boxed{
\Delta_k^2\log R_{r,k}\le0.
}
\]

Thus the two-dimensional RH route can be stated without campaign notation:

> **Higher-order Poisson-normalized log-concavity.** For every determinant order `r`, the consecutive Toeplitz minors normalized by the pure-exponential benchmark are log-concave in the shift.

## 3. Rectangular Schur formulation

By Jacobi–Trudi,

\[
D_{r,k}=s_{(k^r)}(\rho)
\]

for the specialization `rho` whose complete symmetric functions are the coefficient sequence `a_k`.

The pure exponential is the Plancherel specialization. Therefore

\[
\boxed{
R_{r,k}
=\frac{s_{(k^r)}(\rho)}
{s_{(k^r)}(\mathrm{Plancherel})}.
}
\]

The hierarchy becomes

\[
\boxed{
\left(\frac{s_{(k^r)}(\rho)}{s_{(k^r)}(\mathrm{Pl})}\right)^2
\ge
\frac{s_{((k-1)^r)}(\rho)}{s_{((k-1)^r)}(\mathrm{Pl})}
\frac{s_{((k+1)^r)}(\rho)}{s_{((k+1)^r)}(\mathrm{Pl})}.
}
\]

This is sharper than ordinary Schur log-concavity because the Plancherel normalization contributes the exact factor `k/(k+r)`.

## 4. Young-graph likelihood-ratio interpretation

There is a second exact interpretation which emerged from the representation-theory audit.

Because Schur functions are homogeneous, multiplying the specialization by a scalar contributes only a geometric factor in `|lambda|`; such a factor cancels from log-concavity along the rectangular ray. We may therefore normalize

\[
p_1(\rho)=1.
\]

A Schur-positive specialization with this normalization defines a coherent system on the Young graph by

\[
M_n^\rho(\lambda)=f^\lambda s_\lambda(\rho),
\qquad |\lambda|=n,
\]

where `f^lambda` is the number of standard Young tableaux of shape `lambda`.

The level-`n` Plancherel measure is

\[
M_n^{\rm Pl}(\lambda)=\frac{(f^\lambda)^2}{n!},
\]

while the Plancherel specialization satisfies

\[
s_\lambda(\mathrm{Pl})=\frac{f^\lambda}{n!}.
\]

Consequently

\[
\boxed{
\frac{s_\lambda(\rho)}{s_\lambda(\mathrm{Pl})}
=
\frac{M_n^\rho(\lambda)}{M_n^{\rm Pl}(\lambda)}.
}
\]

So `R_{r,k}` is exactly the **likelihood ratio of the Thoma/Schur coherent system to Plancherel measure**, evaluated at the rectangular shape

\[
\lambda_k=(k^r),\qquad |\lambda_k|=rk.
\]

The hierarchy can therefore be restated as:

> Along every fixed-height rectangular ray of the Young graph, the likelihood ratio of the corresponding Schur-positive coherent system to Plancherel is log-concave in the width.

This interpretation connects the RH determinant problem directly to harmonic functions and coherent systems on the Young graph. A targeted search found the classical Thoma/coherent-system correspondence and stochastic-monotonicity theory, but did not locate this rectangular likelihood-ratio log-concavity statement.

## 5. Why it is sufficient for RH in the xi application

Desnanot–Jacobi gives

\[
D_{r+1,k}D_{r-1,k}
=D_{r,k}^{2}-D_{r,k-1}D_{r,k+1}.
\]

Under the hierarchy,

\[
D_{r+1,k}D_{r-1,k}
\ge \frac{r}{k+r}D_{r,k}^{2}.
\]

If `a_k>0` for every `k`, then `D_{0,k}=1` and `D_{1,k}=a_k>0`; induction in `r` gives

\[
D_{r,k}>0
\]

for every consecutive minor. Schoenberg's strict consecutive-minor criterion then promotes positivity to all minors of every finite order. In the transformed xi setting, the classical Pólya-frequency/Laguerre–Pólya characterization gives the RH implication.

This is a sufficiency statement, not a proof that xi satisfies the hierarchy.

## 6. Conjectural general form suggested by the audit

The finite-polynomial falsifier from epoch 23 was outside the infinite-support hypothesis. The correct adversarial class is instead the entire Laguerre–Pólya-I / denominator-free Pólya-frequency class

\[
H(z)=e^{\gamma z}\prod_i(1+\alpha_i z),
\qquad \gamma>0,\ \alpha_i\ge0.
\]

The current conjecture is:

> **Conjecture.** Every such infinite-support specialization satisfies Poisson-normalized rectangular log-concavity for all `r,k>=1`.

The statement is false if one enlarges to arbitrary Edrei/PF-infinity generating functions with denominator factors. For example,

\[
H(z)=\frac{e^{z/10}}{1-z/10}
\]

already violates the `r=k=1` sharpened inequality. Thus the conjecture is not an automatic consequence of total positivity alone; it appears to distinguish the entire denominator-free subclass.

## 7. Exact hostile tests in the correct domain

The conjecture was attacked with exact rational arithmetic on families

\[
e^{\gamma z}\prod_i(1+\alpha_i z)
\]

with positive rational parameters.

Campaign A:

- 3,000 seeded families;
- `1<=r<=5`, `1<=k<=9`;
- 135,000 exact determinant inequalities;
- zero failures.

Campaign B:

- 1,200 families including extreme ratios from `1/100` through `100`;
- up to eight linear factors;
- `1<=r<=6`, `1<=k<=12`;
- 86,400 exact determinant inequalities;
- zero failures.

The computations are evidence only.

## 8. Prior-art audit as of 2026-09-12

Nearby results checked include:

- Lam–Postnikov–Pylyavskyy, *Schur positivity and Schur log-concavity* (2005);
- David Speyer's 2026 proof of the stronger Schur-log-concavity conjectural framework;
- normalized Schur inequalities such as Sra's normalization by `s_lambda(1^n)`;
- Thoma's theorem, Schur-positive specializations and coherent systems/harmonic functions on the Young graph;
- stochastic-monotonicity results on the Young graph;
- classical Newton/Turán and higher Turán inequalities for Laguerre–Pólya coefficients;
- classical Pólya-frequency/total-positivity theory;
- 2026 rectangular-Schur and Toeplitz-minor work, including the explicit cubic xi wedge.

Those are close but the audit has not located the exact arbitrary-specialization inequality with the **Plancherel/Poisson factor `k/(k+r)`** for all rectangle orders, nor its equivalent rectangular Young-graph likelihood-ratio formulation.

This is therefore released as a **novelty candidate**. Absence from a search is not a proof of historical novelty.

## 9. Current frontier

There are now four clean proof/search directions:

1. prove the conjecture for the full Laguerre–Pólya-I / Thoma beta-parameter class;
2. find a counterexample **inside** that class;
3. attack rectangular likelihood-ratio log-concavity using harmonic/coherent-system theory on the Young graph;
4. prove the inequality only for the xi specialization by exploiting theta-kernel structure.

Any of the four is mathematically informative. The one-linear-factor subfamily is already proved in `ONE-LINEAR-FACTOR-CHARLIER-THEOREM.md`.
