# Riemann Hypothesis research — current public status

**Author:** Jared Wilder  
**Current release:** 2026-09-12

This directory is the public home for RH/zeta mathematics recovered from the 647-round research export and the earlier August encirclement packets.

> **Forensic correction, 2026-09-12:** the earlier same-day statement that Branch C was refuted is superseded. The finite-polynomial falsifier removed the terminating boundary and therefore did not satisfy the infinite everywhere-positive hypothesis needed by the global strict-minor implication. Branch C is a **valid sufficient-criterion route**, but the criterion has **not** been proved globally for the xi coefficients.

**The Riemann Hypothesis remains open in this work.**

## Start here

The multi-pass audit and current novelty ledger are now published under:

`findings-2026-09-12/`

The packet includes separate files for:

- the higher-order Poisson/Plancherel-normalized Toeplitz-minor hierarchy;
- a new all-order/all-shift theorem for `exp(gamma z)(1+alpha z)` via Charlier polynomials;
- the Branch-C readjudication and exact RH sufficiency reduction;
- the theta/Gaussian moment frontier and the precise missing localization/variance theorem;
- discrete elliptic comparison and boundary-homotopy positivity;
- the top-`k` angular budget theorem;
- exact reciprocal/transposed curvature duality;
- the rational determinant orbit, fixed-slope linearization and dynamic ellipticity;
- an explicit novelty/prior-art audit;
- exact hostile-test source and receipts on genuine infinite-support Laguerre–Pólya-I families.

## Current campaign state

### Branch C — reopened: valid sufficient criterion, analytic proof incomplete

Let

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1}.
\]

The global criterion is

\[
\boxed{
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
}
\qquad(r,k\ge1).
\]

For an everywhere-positive coefficient sequence, Desnanot–Jacobi gives

\[
D_{r+1,k}D_{r-1,k}
\ge\frac r{k+r}D_{r,k}^2>0,
\]

so the criterion inductively forces every consecutive minor to be strictly positive. The classical Schoenberg/Katkova strict-consecutive-minor theorem then promotes this to total positivity at every finite order; the standard Pólya-frequency/Laguerre–Pólya bridge gives the RH implication for the transformed xi sequence.

Thus:

\[
\boxed{
\text{global Branch-C criterion for xi}\Longrightarrow RH.
}
\]

What is **not** proved is that xi satisfies the global criterion.

The live gaps preserved in the source campaign include the higher-order/order-ascent step and the theta-measure localization/variance estimate. In particular, curvature at one moving mode does not by itself control global variance, and the relevant tilted density is log-convex in a far-left tail, so a naive global Brascamp–Lieb argument does not apply.

See `findings-2026-09-12/BRANCH-C-READJUDICATION.md` and `findings-2026-09-12/THETA-GAUSSIAN-MOMENT-FRONTIER.md`.

### Why the epoch-23 falsifier is not a counterexample

The historical scripts constructed finite polynomials and explicitly excluded the terminating boundary. A fresh seeded rerun reproduced

```text
2284 non-real-rooted polynomials tested
1445 interior hits for the original criterion
1445/1445 hits violate the everywhere-positive infinite-sequence premise
```

Those computations remain published as historical negative controls. They do not refute the global strict criterion.

Likewise `a=(1,0,0,0,0,1)` correctly shows that **nonnegative** consecutive minors do not imply total positivity; it does not refute the classical **strict** consecutive-minor theorem.

## Strongest new mathematical target from the audit

For the pure exponential/Poisson benchmark

\[
D^{(0)}_{r,k}=\prod_{j=0}^{r-1}\frac{j!}{(k+j)!},
\]

one has

\[
\frac{D^{(0)}_{r,k-1}D^{(0)}_{r,k+1}}
{(D^{(0)}_{r,k})^2}
=\frac{k}{k+r}.
\]

Hence Branch C is exactly log-concavity in `k` of

\[
\boxed{
R_{r,k}=D_{r,k}/D^{(0)}_{r,k}.
}
\]

Via Jacobi–Trudi this is the rectangular Schur ratio

\[
\boxed{
\frac{s_{(k^r)}(\rho)}{s_{(k^r)}(\mathrm{Plancherel})}.
}
\]

The three-pass literature sweep found strong nearby Schur-log-concavity results but no exact match for this sharper Poisson/Plancherel-normalized hierarchy. It is published as a **novelty candidate, not a certified historical-first theorem**.

The hierarchy has now been proved for the complete one-linear-factor family

\[
H(z)=e^{\gamma z}(1+\alpha z),
\qquad\gamma>0,\alpha\ge0,
\]

because the normalized rectangular minor is a Charlier polynomial in `-k` and therefore has only negative zeros as a polynomial in the shift.

## Exact hostile tests in the correct domain

The conjectural hierarchy was tested using exact rational arithmetic on genuine infinite-support Laguerre–Pólya-I families

\[
e^{\gamma z}\prod_i(1+\alpha_i z).
\]

Two published campaigns currently record:

- 3,000 families, `1<=r<=5`, `1<=k<=9`: **135,000 exact inequalities**, zero failures;
- 1,200 more hostile/extreme families, `1<=r<=6`, `1<=k<=12`: **86,400 exact inequalities**, zero failures.

These computations are evidence, not proof.

## Other surviving mathematics

The current findings packet also publishes at exact scope:

- the nonlinear discrete elliptic equation for normalized determinant arrays and its finite-domain comparison/homotopy theorem;
- the exact rational determinant-odds orbit `(r+mu)/(k+nu)` and fixed-slope linearization;
- dynamic discrete harmonicity of `partial_t log(D/B)` along the coefficient heat flow and superharmonicity of the second derivative;
- the top-`k` angular phase budget for rectangular Schur minors;
- exact reciprocal/transposed-rectangle curvature duality;
- rigorous theta-kernel interval certificates and the Gaussian-normalized moment reduction;
- Branch-A heat-flow instrumentation and its negative controls;
- Branch-B arithmetic handoff.

## Prior-art boundary

The novelty ledger deliberately marks classical or collided mechanisms rather than claiming them:

- Desnanot–Jacobi, Jacobi–Trudi, Schoenberg total positivity and order-one Turán/Newton machinery are classical infrastructure;
- Michalowski's July 2026 work gives the explicit xi cubic wedge `D_{r,k}>0` for `r>=2`, `k>=10^18 r^3`;
- a July 22, 2026 public fixed-shift construction already uses the reciprocal/Jacobi–Trudi pole mechanism, so the recovered August fixed-shift theorem is not claimed as novel;
- the recovered `67.301545...%` simple-zero computation is preserved but is not presented as a public numerical record.

See `findings-2026-09-12/NOVELTY-AUDIT.md`.

## Reproduction and provenance

The original export hash and core recovered scripts remain under `MANIFEST.sha256`, `REPRODUCIBILITY.md`, `provenance/`, `branch-a/`, `branch-b/`, `branch-c/`, `theta-kernel/`, and `formal/`.

Historical files are preserved even when their interpretation has been superseded. The current adjudication is the one stated on this page and in `findings-2026-09-12/`.
