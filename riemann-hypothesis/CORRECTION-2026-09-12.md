# Correction to the September 10 RH terminal asset bank

**Author:** Jared Wilder  
**Correction date:** 2026-09-12  
**Updated forensic adjudication:** 2026-09-12

The historical file `estate/RIEMANN-HYPOTHESIS-TERMINAL-ASSET-BANK-2026-09-10.md` mixed two different statements about consecutive Toeplitz minors:

1. **nonnegative** consecutive minors imply total positivity;
2. **strictly positive** consecutive minors of every order imply total positivity through the classical Schoenberg criterion.

The first statement is false. The second is a classical theorem and is the relevant one for the global Branch-C implication.

## Nonnegative shortcut: refuted

The exact sequence

`a=(1,0,0,0,0,1)`

has nonnegative consecutive minors in the tested hierarchy while the non-consecutive `2 x 2` minor on rows `{0,1}` and columns `{1,5}` is

`a1*a4-a5*a0=-1`.

Therefore

> nonnegative consecutive minors => total positivity

is false.

This example does **not** refute the strict theorem because its coefficient sequence contains zeros.

## The later Branch-C retraction was also overbroad

A subsequent epoch-23 audit constructed finite non-real-rooted positive-coefficient polynomials and reported:

- `2284` non-real-rooted finite objects tested;
- `1445` satisfy the criterion on the tested interior region.

That computation is reproducible, but its interpretation as a refutation of the global xi criterion was wrong.

The test deliberately excluded the terminating boundary. Every test object is a finite polynomial, so after its last coefficient one has `a_N=0`. Hence every such object violates the everywhere-positive infinite-sequence hypothesis used in the strict consecutive-minor induction.

A fresh seeded re-audit reproduces the old count and gives:

```text
interior hits for original criterion: 1445
hits violating everywhere-positive coefficient premise: 1445
```

Thus **1445/1445 purported counterexamples lie outside the load-bearing global hypothesis**.

## Current adjudication

For an infinite coefficient sequence with `a_k>0` for every `k`, the global Branch-C inequality

\[
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
\]

and Desnanot–Jacobi imply

\[
D_{r+1,k}D_{r-1,k}
\ge\frac r{k+r}D_{r,k}^2>0.
\]

Starting from `D_{0,k}=1` and `D_{1,k}=a_k>0`, induction gives strict positivity of every consecutive minor. Schoenberg's classical strict-consecutive-minor theorem then promotes this to total positivity at every finite order.

Therefore Branch C is **not refuted by the finite-polynomial audit**. It remains a valid sufficient-criterion route to RH.

It is still incomplete: the research campaign did not prove the determinant inequality globally for the xi coefficients. The surviving gap is analytic, including the higher-order/order-ascent step and the theta-measure localization/variance bridge.

## Current public record

The current forensic findings and novelty audit are under

`riemann-hypothesis/findings-2026-09-12/`.

Historical falsifier scripts and outputs remain published as negative controls. Their computations are preserved; only the invalid global interpretation is superseded.
