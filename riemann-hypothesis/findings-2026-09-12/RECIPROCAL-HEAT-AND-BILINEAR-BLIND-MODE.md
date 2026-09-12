# Reciprocal heat equation and the universal bilinear blind mode

**Author:** Jared Wilder  
**Recovered from:** RH Encirclement V  
**Public canonical release:** 2026-09-12  
**Status:** exact identities / obstruction

## 1. Reciprocal nonlinear heat equation

Let

\[
G_t(z)=\sum_{n\ge0}a_n(t)z^n
\]

satisfy the coefficient heat equation

\[
\partial_tG_t=4zG_t''+2G_t'.
\]

Define

\[
H_t(z)=G_t(-z),
\qquad
E_t(z)=\frac1{H_t(z)}.
\]

Then

\[
\partial_tH_t=-4zH_t''-2H_t'.
\]

Since `E=H^{-1}`,

\[
E'=-\frac{H'}{H^2},
\qquad
E''=2\frac{(H')^2}{H^3}-\frac{H''}{H^2}.
\]

Direct substitution gives the exact reciprocal evolution

\[
\boxed{
\partial_tE_t
=-4zE_t''-2E_t'
+8z\frac{(E_t')^2}{E_t}.
}
\]

Thus Jacobi–Trudi reciprocity does **not** turn the de Bruijn–Newman coefficient flow into another copy of the same linear PDE. The dual coordinate evolves nonlinearly.

## 2. Universal bilinear harmonic blind mode

The normalized determinant dynamics use an adaptive discrete elliptic operator

\[
L_{r,k}f
=R_{r,k}\Delta_k^2f+A_{r,k}\Delta_r^2f,
\]

with `R,A>=0` and `R+A=1` in the positive phase.

For the bilinear area function

\[
f(r,k)=rk,
\]

one has identically

\[
\Delta_k^2(rk)=0,
\qquad
\Delta_r^2(rk)=0.
\]

Hence

\[
\boxed{L(rk)=0}
\]

for **every** choice of adaptive weights.

More generally every bilinear-affine function

\[
c_0+c_1r+c_2k+c_3rk
\]

lies in the kernel.

## 3. Consequence for no-escape arguments

A maximum principle plus a generic statement that a harmonic field has polynomial growth cannot by itself rule out growth on the `rk` scale: that scale is invisible to the operator.

Therefore a Phragmen–Lindelöf/no-escape theorem strong enough for the determinant lattice must use information beyond polynomial boundedness. It must rule out or control the bilinear component—for example through boundary asymptotics, normalization, sign, flux, or problem-specific regularity.

The critical invisible growth scale is the lattice area `rk`, exactly the scale on which rectangular determinant free energies naturally live.

## 4. Relation to the recovered campaign

This obstruction explains why the adaptive-harmonic heat-flow identity, although exact, was not by itself a terminal RH argument. The campaign's later Schur sensitivity and angular-phase results were attempts to inject problem-specific information invisible to the harmonic operator.

## 5. Novelty status

The calculus identity for a reciprocal of a PDE solution and the fact that bilinear functions have zero coordinate second differences are elementary. The value here is the specialized obstruction they impose on the determinant-lattice no-escape program.

This file is published as an exact research finding / route obstruction, not as a claim of a deep standalone new PDE theorem.
