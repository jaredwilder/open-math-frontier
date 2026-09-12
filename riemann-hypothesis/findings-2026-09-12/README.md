# Riemann Hypothesis findings — forensic release 2026-09-12

**Author:** Jared Wilder  
**Public release:** 2026-09-12  
**Source campaign:** 647-round RH/zeta research export plus recovered August encirclement packets

This directory is a dated public record of the strongest surviving RH-adjacent mathematics identified in a multi-pass forensic review. It is intentionally split by evidence class so that a later correction to one item does not contaminate the rest.

**No claim is made here that the Riemann Hypothesis has been proved.**

## Claim classes

- **PROVED HERE:** complete mathematical proof is given in the file, possibly using named classical theorems whose hypotheses are stated.
- **PROVED IN SOURCE CAMPAIGN:** proof/reproducible algebra survived the audit and is republished at its exact scope.
- **COMPUTATIONALLY CERTIFIED:** an explicit finite inequality/enclosure is certified by the archived or rerun verifier.
- **CONJECTURE / OPEN REDUCTION:** mathematically precise and evidence-backed, but not proved.
- **PRIOR-ART COLLISION / REDISCOVERY:** retained for completeness but not claimed novel.
- **CLASSICAL / REFORMULATIVE INFRASTRUCTURE:** included because it links the program, but not claimed as a new result.

## Headline findings

### 1. Higher-order Poisson-normalized Toeplitz-minor hierarchy

For

\[
D_{r,k}=\det[a_{k+j-i}]_{i,j=0}^{r-1},
\qquad
D^{(0)}_{r,k}=\prod_{j=0}^{r-1}\frac{j!}{(k+j)!},
\]

the Branch-C inequality

\[
(k+r)D_{r,k-1}D_{r,k+1}\le kD_{r,k}^2
\]

is exactly the log-concavity in `k` of the Poisson-normalized minors

\[
R_{r,k}=D_{r,k}/D^{(0)}_{r,k}.
\]

Equivalently, for a Schur-positive specialization `rho`, it asks for log-concavity along rectangles of

\[
\frac{s_{(k^r)}(\rho)}{s_{(k^r)}(\mathrm{Plancherel})}.
\]

After normalizing `p_1(rho)=1`, the same ratio is exactly the likelihood ratio of the corresponding Thoma/Schur coherent system to Plancherel measure at the rectangular Young diagram `(k^r)`. A multi-pass literature sweep found nearby Schur/Lorentzian/coherent-system results but no exact match for this sharper rectangular Plancherel-normalized statement. This remains a **novelty candidate, not a novelty certification**.

See `POISSON-NORMALIZED-HIERARCHY.md`.

### 2. One-linear-factor theorem via Charlier polynomials

For the entire Laguerre–Pólya-I family

\[
H(z)=e^{\gamma z}(1+\alpha z),\qquad \gamma>0,\ \alpha\ge0,
\]

the full higher-order normalized inequality is proved for **every** determinant order `r` and shift `k`.

After `x=alpha/gamma`, the normalized rectangle is

\[
\frac{D_{r,k}}{D^{(0)}_{r,k}}
=\sum_{t=0}^r {r\choose t}(k)_t x^t
={}_2F_0(-r,k;;-x)
=C_r(-k;1/x),
\]

where `C_r` is a Charlier polynomial. Orthogonality puts all Charlier zeros on the positive real axis in their polynomial variable, hence all zeros in the `k` variable are negative; therefore the normalized minor is strictly log-concave on `k>=0` for `alpha>0`.

See `ONE-LINEAR-FACTOR-CHARLIER-THEOREM.md`.

### 3. Branch-C readjudication and exact RH sufficiency chain

The epoch-23 finite-polynomial falsifier does **not** refute the global strict criterion needed by the xi coefficient sequence: all purported counterexamples terminate and therefore violate the everywhere-positive infinite-sequence hypothesis.

For an everywhere-positive coefficient sequence, the global Branch-C inequality and Desnanot–Jacobi inductively force every consecutive Toeplitz minor to be strictly positive. Schoenberg's strict consecutive-minor theorem then promotes these to total positivity at every finite order. For the transformed xi generating function, the classical Pólya-frequency/Laguerre–Pólya bridge gives the RH implication.

The criterion is therefore a valid sufficient route, but the campaign did **not** prove it globally for xi. The live gap is below this classical top link.

See `BRANCH-C-READJUDICATION.md`.

### 4. Theta/Gaussian moment frontier

The binding order-one row is reduced exactly to a comparison between the theta-kernel even-moment log-convexity rate and the Gaussian equality case. A continuous interpolation identifies the curvature of log moments with a variance of `log x` under the tilted measure.

The campaign's later substitution of curvature at the mode for a global variance bound is not justified: the tilted density is log-convex in a far-left tail, so the missing localization/tail-error theorem is load-bearing.

See `THETA-GAUSSIAN-MOMENT-FRONTIER.md`.

### 5. Discrete elliptic comparison and boundary-homotopy positivity

Positive determinant arrays normalized by a positive Desnanot–Jacobi comparison array satisfy a nonlinear discrete elliptic equation. This yields a finite-domain comparison principle and a boundary-homotopy positivity theorem.

See `DISCRETE-ELLIPTIC-COMPARISON-AND-HOMOTOPY.md`.

### 6. Top-k angular budget theorem

For a rectangular Schur representation, semistandard-tableau occupancy gives

\[
|\arg M|\le r\sum_{j=1}^{k}\vartheta_j,
\]

and hence

\[
r\sum_{j=1}^{k}\vartheta_j<\pi/2\Longrightarrow D_{r,k}>0.
\]

This is retained as a proved two-parameter phase criterion. Nearby classical sector criteria exist; exact novelty is not claimed without further specialist comparison.

See `TOP-K-ANGULAR-BUDGET.md`.

### 7. Rectangular Schur sensitivity, distortion, and single-pair detection delay

The semistandard-tableau representation gives the exact normalized sensitivity cap

\[
0\le p_j\le1/k,\qquad\sum_jp_j=1,
\]

an explicit tail/free-energy distortion bound for perturbations of zero parameters, and the quantitative single-pair detection law

\[
r|\theta|<\pi/2\Longrightarrow D_{r,k}>0\quad\text{for every }k.
\]

Thus a conjugate pair with angular defect `theta` cannot be detected by sign loss below order `pi/(2|theta|)`.

See `SCHUR-SENSITIVITY-DISTORTION-AND-DETECTION.md`.

### 8. Exact reciprocal/transposed curvature duality

Dual Jacobi–Trudi exchanges order and shift. For the normalized curvature/odds variable `Z`,

\[
Z_a(r,k)Z_b(k,r)=1
\]

for the reciprocal dual sequence `b`. The compactified ratio `theta=k/(k+r)` is sent to `1-theta`.

See `RECIPROCAL-CURVATURE-DUALITY.md`.

### 9. Rational orbit, fixed-slope continuum and dynamic ellipticity

The determinant-odds recurrence admits the exact two-parameter rational family

\[
Y_{r,k}^{\mu,\nu}=\frac{r+\mu}{k+\nu},
\]

with the factorial Toeplitz orbit `Y=r/k`. The recovered campaign derives the tangent fixed-slope continuum, its exact local Jacobian and dispersion law, and the dynamic heat-flow identities

\[
R^D\Delta_k^2V+A^D\Delta_r^2V=0
\]

for `V=partial_t log(D/B)`, with the second time derivative superharmonic. Combined with boundary-homotopy positivity, this gives a no-bounded-first-nucleation principle under the stated positivity hypotheses.

See `RATIONAL-ORBIT-AND-DYNAMIC-ELLIPTICITY.md`.

### 10. Reciprocal nonlinear heat equation and universal `rk` blind mode

The reciprocal Jacobi–Trudi generating coordinate evolves by

\[
\partial_tE=-4zE''-2E'+8z(E')^2/E,
\]

not by a second copy of the linear heat equation. Independently, `rk` and every bilinear-affine function lie in the kernel of every adaptive operator `R Delta_k^2 + A Delta_r^2`. This identifies a universal `rk`-scale obstruction to naive polynomial-growth no-escape arguments.

See `RECIPROCAL-HEAT-AND-BILINEAR-BLIND-MODE.md`.

### 11. Xi as a positive PF-infinity mixture and exact determinant lift

The xi coefficient generating function has the exact mixture representation

\[
G(z)=\int_0^\infty\Phi(u)\cosh(u\sqrt z)\,du,
\]

where each fixed-`u` atomic coefficient sequence is `PF_infinity`. Multilinearity gives an exact positive-measure determinant lift. The natural symmetrized integrand is nevertheless sign-indefinite already at order two, killing the direct pointwise-positive Andréief-style route. The same packet gives an exact tilted-MGF representation of every normalized Toeplitz block.

See `XI-MIXTURE-AND-DETERMINANT-LIFT.md`.

### 12. Corrected critical-value / gap monotonicity theorem

For adjacent real zeros of the heat-flow entire function, with critical value `V_j` and gap `g_j`, the local ratio

\[
\mathcal R_j=|V_j|/g_j^2
\]

satisfies an exact nonnegative derivative decomposition. It is nondecreasing in general and strictly increasing whenever the critical point is asymmetric or an outer real zero is present. The source campaign's blanket strictness statement is corrected accordingly.

See `CRITICAL-VALUE-GAP-MONOTONICITY.md`.

### 13. Transformed-zero moment / Toeplitz-PSD / Stieltjes coordinates

The recovered terminal packet also gives clean RH-equivalent formulations through a unit-circle zero transform, positive-semidefinite Toeplitz moment matrices, and a genus-zero Stieltjes moment sequence after quotienting by the functional equation. These are retained as **classical/reformulative infrastructure, not novelty claims**.

See `TRANSFORMED-ZERO-MOMENT-CRITERIA.md`.

## Exact hostile computation on the conjectural hierarchy

Two exact-rational campaigns on genuine infinite-support Laguerre–Pólya-I sequences of the form

\[
e^{\gamma z}\prod_i(1+\alpha_i z),\qquad \gamma>0,\ \alpha_i\ge0,
\]

have produced no counterexample:

- 3,000 seeded families, `1<=r<=5`, `1<=k<=9`: **135,000 exact inequalities**, zero failures;
- a second campaign including extreme parameter ratios, 1,200 families, `1<=r<=6`, `1<=k<=12`: **86,400 exact inequalities**, zero failures.

Exact source and receipts are under `computation/`. This is evidence only. It is not substituted for proof.

## Prior-art boundary

The release deliberately does **not** claim novelty for classical Desnanot–Jacobi, Jacobi–Trudi, Schoenberg total-positivity criteria, ordinary order-one Turán/Newton inequalities, the transformed-zero moment criteria, or the fixed-shift reciprocal-pole mechanism where close July-2026 prior art was located.

The strongest unresolved novelty target remains the **higher-order Poisson/Plancherel-normalized rectangular log-concavity hierarchy**, together with partial theorems and structural consequences specific to it.

See `NOVELTY-AUDIT.md`.
