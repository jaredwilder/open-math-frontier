# RH findings novelty audit — 2026-09-12

**Author:** Jared Wilder  
**Audit date:** 2026-09-12  
**Status:** literature-search record, not a guarantee of historical novelty

This file records what the multi-pass literature sweep did and did not find. The rule is conservative: a nearby theorem does not automatically kill novelty, but an actual mechanism-level collision does.

## Verdict table

| Finding | Mathematical status | Novelty status after current sweep |
|---|---|---|
| Higher-order Poisson/Plancherel-normalized rectangular log-concavity | conjecture / exact RH reduction | **high-priority novelty candidate; no exact match found** |
| One-linear-factor Charlier theorem | proved | **new formulation/application candidate; classical Charlier ingredients** |
| Branch-C strict-minor sufficiency chain | proved reduction using classical theorems | **not claimed novel as topological/TP machinery; campaign-specific criterion/reduction timestamped** |
| Discrete elliptic comparison + boundary-homotopy positivity | proved | **novelty unresolved; no exact formulation found** |
| Top-k angular budget | proved | **possible modest novelty; close sector/phase prior art exists** |
| Rational determinant orbit + fixed-slope linearization | exact algebra/continuum derivation | **novelty unresolved** |
| Dynamic determinant ellipticity along heat flow | exact differential identity | **novelty unresolved; Toda/heat-flow literature is large** |
| Exact reciprocal curvature duality | exact algebraic identity | **not presently claimed novel** |
| Theta/Gaussian normalized moment reduction | exact reduction + finite certificates | **novelty of specific reduction unresolved; underlying variance identity classical** |
| Fixed-shift reciprocal-pole eventual positivity | theorem | **mechanism-level prior-art collision found; do not claim novelty** |
| Order-one sharp Turan row | theorem | **classical / prior art** |
| Uniform cubic xi wedge | theorem | **prior art: Michalowski 2026** |
| 67.3015452606% simple-zero candidate | computational candidate | **do not claim numerical record or public priority** |
| PTS interval-certifier self-test | computational machinery | **not a theorem/novelty headline** |

## 1. Main novelty target: Poisson-normalized rectangular log-concavity

The strongest current candidate is

\[
R_{r,k}=\frac{s_{(k^r)}(\rho)}{s_{(k^r)}(\mathrm{Pl})}
\]

and the conjecture

\[
R_{r,k}^2\ge R_{r,k-1}R_{r,k+1}.
\]

Equivalently,

\[
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2.
\]

### Nearby literature checked

**Lam–Postnikov–Pylyavskyy (2005), Schur positivity and Schur log-concavity.** Their Schur-positive inequalities are highly relevant but do not by themselves supply the sharper Plancherel ratio `k/(k+r)` appearing here.

**David Speyer (2026), L-log-concavity and a proof of the conjecture of Lam, Postnikov and Pylyavskyy, arXiv:2601.05007.** This resolves a strong Schur-log-concavity framework. The statement compares products of Schur functions under partition-balancing hypotheses. The current audit did not derive from it the arbitrary-specialization inequality after division by the Plancherel rectangle value.

**Normalized Schur-function literature.** Results using normalizations such as `s_lambda(x)/s_lambda(1^n)` were checked. That normalization is not the Plancherel/Poisson benchmark used here.

**Newton/Turan/higher Turan and Pólya-frequency theory.** These explain substantial `r=1` structure and total positivity, but no exact all-rectangle sharpened factor was located.

**Verdict:** no exact prior-art match located. Release as a conjectural novelty candidate, not as a theorem or certified historical first.

## 2. One-linear-factor Charlier theorem

For

\[
H(z)=e^{\gamma z}(1+\alpha z),
\]

the normalized rectangle is

\[
R_{r,k}={}_2F_0(-r,k;;-\alpha/\gamma)
=C_r(-k;\gamma/\alpha),
\]

up to the standard Charlier parameter notation.

Charlier polynomials, their hypergeometric representation, orthogonality and positive real zeros are classical. The potentially new step is identifying the **rectangular Toeplitz/Schur normalized determinant as a Charlier polynomial in the shift `k`** and using that to prove the full hierarchy for every `(r,k)` in this LP-I subfamily.

Targeted searches combining Charlier, Toeplitz determinant, rectangular Schur, `exp(z)(1+xz)` and normalized minors did not locate this exact formulation.

**Verdict:** theorem proved; formulation/application is a novelty candidate, but classical ingredients must be credited.

## 3. Discrete elliptic comparison and homotopy positivity

The exact equation

\[
R^Be^{\Delta_k^2U}+A^Be^{\Delta_r^2U}=1
\]

and its factorial specialization

\[
k e^{\Delta_k^2U}+r e^{\Delta_r^2U}=k+r
\]

yield a finite-domain comparison principle and boundary-homotopy positivity theorem.

Desnanot–Jacobi, Toda/octrahedron recurrences and discrete maximum principles are classical. Searches for the exact logarithmic normalization plus first-zero/homotopy theorem did not find a direct statement.

**Verdict:** valid theorem, novelty unresolved. Publish rather than suppress; do not advertise a historical-first result yet.

## 4. Top-k angular budget

The tableau occupancy cap

\[
|\arg M|\le r\sum_{j=1}^k\vartheta_j
\]

and resulting sufficient condition

\[
r\sum_{j=1}^k\vartheta_j<\pi/2
\Longrightarrow D_{r,k}>0
\]

are elementary once the rectangular Schur representation is in place.

Classical Schoenberg/sector methods and phase criteria are nearby. The top-`k` semistandard occupancy sharpening was not found verbatim in the targeted sweep.

**Verdict:** proved and useful; likely not the flagship novelty claim until a specialist search is complete.

## 5. Fixed-shift reciprocal-pole mechanism: collision found

A public construction dated **July 22, 2026**, *The first fifteen Xi-coefficient shifts are nonnegative at every Toeplitz rank*, uses the same central mechanism:

- rectangular Jacobi–Trudi duality;
- fixed original shift becomes fixed-size reciprocal determinant;
- reciprocal-xi pole expansion;
- Vandermonde structure and eventual positivity.

That is close enough to the recovered August Encirclement-IV theorem that this release does **not** claim novelty for the mechanism.

The result remains useful as independent derivation/infrastructure.

## 6. Cubic wedge: explicit prior art

Wojciech Michalowski, *An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients*, arXiv:2607.16795 (July 18, 2026), proves

\[
D_{r,k}>0\qquad(r\ge2,\ k\ge10^{18}r^3).
\]

This is an important external boundary for the current work: the remaining determinant problem includes the complementary two-scale region rather than the already-certified cubic tail.

No novelty is claimed for that wedge.

## 7. Order-one row

Sharp Turan/Newton-type inequalities for the xi coefficient sequence have prior literature, including the Csordas–Norfolk–Varga line cited in Katkova's work.

The order-one row is therefore infrastructure/calibration, not a new theorem claim.

## 8. 67.3015452606% simple-zero candidate

The recovered packet contains exact transfer algebra and two exhaustive finite interval-subdivision runs for the constant

\[
0.673015452606376894\ldots.
\]

However, stronger 67.31–67.32% candidate computations were publicly circulating in August 2026, and this packet's public GitHub commit is dated September 11, 2026.

**Verdict:** preserve the computation and its internal campaign provenance; do not claim a public numerical record or priority from the current evidence.

## 9. Reciprocal curvature duality

Dual Jacobi–Trudi immediately makes order/shift transposition natural. The specialized identities

\[
Z_a(r,k)Z_b(k,r)=1
\]

and

\[
Q_a(r,k)+Q_b(k,r)=1
\]

are exact, but the underlying duality is classical enough that this audit does not currently claim novelty.

## 10. Rational orbit and dynamic ellipticity

The recovered program contains:

- exact rational odds family `(r+mu)/(k+nu)`;
- factorial orbit `r/k`;
- tangent fixed-slope correction family;
- exact Jacobian and dispersion law;
- discrete harmonicity of `partial_t log(D/B)` along the coefficient heat flow;
- superharmonicity of the second time derivative.

The search found extensive integrable-systems/Toda/octrahedron literature but no immediate exact match for the whole specialized package.

**Verdict:** exact mathematics with novelty unresolved. It belongs in the public record, but not yet under a strong historical-first headline.

## 11. Audit rule going forward

Publication here means **dated disclosure**, not “the literature has been exhaustively proven not to contain an equivalent theorem.”

Future updates should move items only in one of four directions:

1. `NOVELTY CANDIDATE -> NOVEL` after a stronger specialist prior-art audit;
2. `NOVELTY CANDIDATE -> REDISCOVERY` when a genuine equivalent prior theorem is found;
3. `CONJECTURE -> THEOREM` after proof;
4. `THEOREM -> CORRECTED/RETRACTED` if a mathematical defect is found.

The public history should preserve those transitions rather than silently rewriting them.
