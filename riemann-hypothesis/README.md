# Riemann Hypothesis research — current public status

**Author:** Jared Wilder  
**Current release:** 2026-09-12

This directory is the current public home for the Riemann Hypothesis work recovered from a 647-round research session.

## Current status

**The Riemann Hypothesis remains open in this work.**

The campaign produced three distinct outcomes:

1. **Branch C is refuted as an RH route.** A proposed coefficient/determinant criterion is strictly weaker than real-rootedness. Exact constructed non-real-rooted positive-coefficient polynomials satisfy the criterion, including at full tested determinant depth and for the original entry form.
2. **Branch A produced a validated numerical instrument but no surviving sufficient statistic.** Pair energy cannot certify real-rootedness; Hermite minors correctly distinguish exact finite controls but fail when applied to polynomial truncations of the target entire function because those truncations carry spurious complex roots.
3. **Branch B remains a handoff, not a result claiming RH progress.** It moves to the arithmetic Chebyshev-error representation and contains only a finite direct prime-power computation through `x=200000`.

The failed RH routes are published because their counterexamples and obstructions are mathematical results in their own right. The theta-kernel calculations are published separately because they survive the failure of Branch C.

## Exact counterexamples and obstructions

### The proposed Branch C criterion is not sufficient for real-rootedness

`branch-c/criterion_is_not_sufficient.py` constructs positive-coefficient polynomials with an irreducible quadratic factor `1 + p z + q z^2`, where `p^2 < 4q`, and tests the candidate criterion.

Archived output:

- `3059` explicitly non-real-rooted polynomials tested;
- `1686` satisfy the proposed criterion anyway.

A small exact witness has coefficient vector

`(1, 113/12, 2549/72, 1265/16, 32629/288, 1615/24)`

and contains a quadratic factor with `p=4/3`, `q=19/4`, hence `p^2-4q=-155/9<0`.

`branch-c/criterion_kill_audit.py` then repeats the test at full available determinant depth, away from boundary artifacts, and against both algebraic forms:

- `2284` non-real-rooted objects tested;
- `1445` pass the square-free criterion;
- the same `1445` pass the original entry form.

Therefore this criterion cannot imply real-rootedness and cannot close RH.

### Consecutive Toeplitz-minor positivity does not imply total positivity

`branch-c/consecutive_is_not_total.py` supplies the exact sequence

`a = (1,0,0,0,0,1)`.

Its consecutive minors in the tested hierarchy are nonnegative, but the non-consecutive minor on rows `{0,1}` and columns `{1,5}` equals

`a1*a4 - a5*a0 = -1`.

Thus a previous bridge from consecutive-minor positivity to total positivity is false. This specifically supersedes the older public description that treated a consecutive-minor criterion as a possible route to `PF_infinity`.

## Surviving theta-kernel mathematics

The failure of Branch C does **not** invalidate the exact theta-kernel inequalities that were proved along the way.

`theta-kernel/certify_full_kernel.py` gives a rational interval certificate

`3 I_2^2 - I_0 I_4 in [3.144319836807e-04, 5.675693447454e-04]`,

so the quantity is rigorously positive for the full kernel under the program's stated enclosure method.

`theta-kernel/certify_four_rungs.py` certifies four successive inequalities, with positive lower bounds for `k=1,2,3,4`:

- `[1.56335252e-03, 1.96426203e-03]`
- `[1.73415563e-03, 2.24619876e-03]`
- `[2.72502080e-03, 3.63976614e-03]`
- `[5.87924581e-03, 8.13406217e-03]`

The archived log states that both the theta-series remainder and truncation tail are included in each enclosure.

`theta-kernel/certify_tail.py` gives the certified relative higher-theta-term tail

`2.477138004562849053e-03 < 1/300`.

Finally, `theta-kernel/row_is_log_concavity.py` rewrites the weighted row exactly as ordinary log-concavity after Gaussian normalization. With

`J_k = I_{2k}/Gamma(k+1/2)`,

the row inequality becomes

`J_{k+1} J_{k-1} <= J_k^2`.

This is published as standalone theta-kernel mathematics, **not** as an RH criterion.

## Branch A: useful instrument, failed certificate

`branch-a/branchA_truncation_envelope.py` records a 64-piece truncation envelope. At the worst listed point `z=85`, the resulting zero-displacement bound is `0.0019980039`; the lower points are much tighter. This supports the reality of the numerical zero window used in that branch.

The next test destroys the hoped-for interpretation. Exact controls include an all-complex configuration with pair energy zero, so small pair energy cannot certify real-rootedness.

The Hermite-minor test behaves correctly on exact finite controls, but `branch-a/branchA_hermite_on_object.py` reports polynomial truncations with only `0/10`, `2/16`, `2/22`, `2/26`, `2/30`, and `4/34` real roots. The obstruction is the approximant: finite polynomial truncations of an entire function with infinitely many zeros can introduce many spurious complex roots.

## Branch B handoff

`branch-b/chebyshev_probe.py` directly computes the Chebyshev function from prime powers through `x=200000`. For example,

`|psi(100000)-100000|/sqrt(100000) = 0.16305977`.

These finite values are not presented as asymptotic evidence for RH. The script exists only as a clean arithmetic handoff after the two analytic/coefficient routes failed their own sufficiency tests.

## Formal source

`formal/` contains three small recovered Lean statements:

- the explicit negative non-consecutive minor;
- the generic logical fact that one `Crit(w) and not P(w)` witness refutes `forall x, Crit(x) -> P(x)`;
- the algebraic normalization of one weighted row into a log-concavity inequality.

They contain no `sorry` in the recovered source. They were not freshly compiled in the environment used for this publication pass, so source recovery and fresh compiler verification are deliberately kept distinct.

## Reproduction and provenance

See `REPRODUCIBILITY.md`, `MANIFEST.sha256`, and `provenance/`.

The two epoch ledgers are preserved as historical provenance. They include superseded intermediate beliefs; this README states the later adjudicated status.

## Scope

This release makes no claim that RH has been proved. Its strongest current content is instead:

- exact counterexamples that eliminate two tempting implication routes;
- exact computational certificates for a theta-kernel inequality family;
- a validated numerical instrument plus a precise approximant obstruction;
- a reproducible arithmetic handoff for the remaining branch.