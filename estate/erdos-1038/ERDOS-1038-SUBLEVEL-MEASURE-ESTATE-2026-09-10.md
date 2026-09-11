# Erdős #1038 — Polynomial Sublevel-Measure Estate

**Author:** Jared Wilder  
**Public release:** 2026-09-10

## Current status first

For a nonconstant monic real polynomial `f` whose roots are all real and lie in `[-1,1]`, let

\[
M(f)=\left|\{x\in\mathbb R:|f(x)|<1\}\right|.
\]

The public 2026 status is:

\[
\boxed{2^{4/3}-1\approx1.519\le\inf_f M(f)\le1.835\cdots,}
\]

while the supremum has been solved:

\[
\boxed{\sup_f M(f)=2\sqrt2.}
\]

Thus only the infimum side remains open. The source campaign predates/overlaps the final resolution of the supremum and must be read under that corrected boundary.

The source ledger contains **27 harvested objects**. Their original adjudication was deliberately deferred; this release preserves that provenance while separating exact lemmas, numerical evidence, retractions, failed infrastructure and open debt.

---

# 1. Exact mathematical objects

## T1038-THM-001 — endpoint quadratic witness

For

\[
f(x)=x^2-1,
\]

the sublevel-set measure is exactly

\[
\boxed{M(f)=2\sqrt2.}
\]

This is the elementary extremizing witness on the now-solved supremum side.

## T1038-THM-002 — power invariance

For every positive integer `k`,

\[
\{|f(x)^k|<1\}=\{|f(x)|<1\}.
\]

Hence

\[
\boxed{M(f^k)=M(f).}
\]

Consequently proper-power root configurations introduce no new functional values and may be quotiented into positive-integer power orbits.

## T1038-THM-003 — common translation invariance

Translating every root by the same real amount translates the sublevel set by the same amount. Therefore Lebesgue measure is unchanged.

This is a general identity for the functional, independent of the source problem's fixed root box.

## T1038-THM-005 — elementary support containment

If `x` lies at distance greater than one from every root, then every factor has absolute value greater than one, so

\[
|f(x)|>1.
\]

Therefore

\[
\{|f|<1\}\subseteq[\min r_i-1,\max r_i+1].
\]

For roots in `[-1,1]`, this gives the elementary universal bound

\[
\boxed{M(f)\le4.}
\]

It is far weaker than the now-known sharp supremum `2sqrt2`, but is exact and assumption-transparent.

## T1038-THM-006 — two-point family power-orbit invariance

For

\[
f_{p,q}(x)=(x+1)^p(x-1)^q,
\]

simultaneous scaling

\[
(p,q)\mapsto(kp,kq)
\]

raises `f` to the kth power and hence preserves `M(f)` exactly.

Thus the two-endpoint family naturally reduces from the integer multiplicity lattice to a multiplicity-ratio problem.

## T1038-THM-004 — archived capacity route

The source session recorded a potential-theoretic statement that the complex sublevel set has logarithmic capacity one and used it toward a real measure bound of four.

This route was later rendered unnecessary by the elementary containment theorem above. It is retained as source-era proof ore, not promoted here as an independently rechecked contribution.

---

# 2. Exact/numerical family measurements

## Endpoint family `(x+1)(x-1)^m`

Independent indicator sampling in the source campaign reported, for increasing `m`, values

```text
2.828427, 2.205568, 1.984305, 1.903209,
1.876258, 1.871667, ...
```

with a tested minimum near `m=6` before rising back toward two over the sampled range.

## Two-point multiplicity sweep

A wider sweep over

\[
(x+1)^p(x-1)^q
\]

with `p=1..8`, `q≥p`, `q≤9p`, and `p+q≤70` reported

\[
\boxed{M\approx1.871563}
\]

at

\[
(p,q)=(7,41).
\]

This value is **not frontier in the current literature**, where the known upper bound for the infimum is already below `1.835`.

## Three-support raw search

A later raw tool result, omitted from the source session's final synthesis, reported

\[
\boxed{M\approx1.869809}
\]

for a root multiset approximately

```text
{-1, -0.871, +1 repeated 12 times}.
```

Nearby reported candidates included `1.870293` and `1.870308`.

Again, these are now sub-frontier numerics. Their enduring value is that they exposed a defect in the campaign's final state: the final MSL summary still claimed no configuration below `1.871563` despite the earlier raw result `1.869809`.

---

# 3. Supremum-side measurements and current reinterpretation

Finite maximization searches in degrees 2–7 reported approximately `2sqrt2` at even degrees and no tested interior-root configuration above it.

At the time this was evidence for a conjectural supremum. In the current public record the supremum is already proved:

\[
\boxed{\sup M(f)=2\sqrt2.}
\]

Therefore these computations should now be interpreted only as independent numerical corroboration / historical research provenance.

A source structural observation noted that measured maximizers tended to have connected one-interval sublevel sets while selected minimizers had fragmented/two-component sublevel sets. This was a numerical pattern, not a universal theorem.

---

# 4. Numerical falsifiers and retractions

The source campaign contains unusually valuable negative computational provenance.

## T1038-FAIL-001 — high-degree polynomial-root evaluator failure

A root-equation evaluator produced an apparent value near

\[
1.544464
\]

at `m=39`, while independent indicator sampling gave about

\[
1.972455.
\]

The session killed the evaluator as unreliable at high degree rather than promoting the apparent breakthrough.

## T1038-FAIL-002 — failed high-precision bracket/bisection evaluator

A second attempted evaluator returned `0.0` at `m=1` and values near `2.82–2.97` for later cases, contradicting independently verified controls. It was also rejected.

## T1038-INFRA-001 — optimizer plateau

Naive Nelder–Mead runs repeatedly collapsed to equal-root plateaus with measure two. Later searches therefore used boundary seeds, random seeds, perturbations and independent re-evaluation.

## T1038-RETRACT-001 — false one-parameter optimality reading

An early campaign statement overread the family

\[
(x+1)(x-1)^m
\]

as optimal inside the endpoint-supported class. The later two-parameter multiplicity sweep found a lower value and explicitly retracted that claim.

## T1038-CONFLICT-001 — stale final state

The final MSL bottleneck state said no configuration was known below `1.871563`, despite the prior raw three-support result `1.869809`.

This contradiction is preserved rather than normalized away. It is a concrete example of why archive chronology and final synthesis must be audited independently.

---

# 5. Search routes retained from the campaign

## Route 1 — direct finite-degree numerical optimization

Use a correct sublevel-measure evaluator, multistarts, boundary perturbations and independent replay. This route was limited by evaluator reliability and by the large gap to the known literature infimum frontier.

## Route 2 — endpoint-family continuum ratio

Power invariance reduces the two-point-supported family to a one-real-parameter multiplicity-ratio problem. The source campaign proposed deriving an exact/closed form and minimizing it analytically.

This remains an interesting restricted-family exercise but cannot by itself settle the full infimum unless one proves a reduction to two-point support.

## Route 3 — connectedness route for the supremum

The session proposed showing that a connected real sublevel interval cannot exceed `2sqrt2`.

The global supremum is now solved externally, so this is retained only as historical proof-route provenance.

---

# 6. Open debt from the source campaign, updated to 2026

Three explicit source debts were recorded:

1. identify the source behind the then-reported infimum upper bound near `1.835`;
2. prove the full-family supremum bound `2sqrt2`;
3. build a robust exact/certified high-degree evaluator.

The current status modifies that list:

- debt 1 is now part of the public literature status, with the infimum currently bracketed by roughly `1.519` and `1.835`;
- debt 2 has been externally solved: the supremum is `2sqrt2`;
- debt 3 remains a useful computational-analysis problem for any renewed numerical search on the infimum side.

---

# 7. Full 27-object provenance inventory

The recovered ledger consists of:

- 1 problem definition object;
- 6 exact/bound mathematical theorem objects;
- 1 corollary;
- 7 computational-family/search objects;
- 2 numerical/evaluator falsifiers;
- 1 optimizer-failure infrastructure object;
- 1 structural numerical observation;
- 1 explicit retraction;
- 1 internal state conflict;
- 3 live/blocked research routes;
- 3 open-debt objects.

Every source object had `Adjudication: DEFERRED`; this public release therefore does not convert source labels into novelty claims.

## Claim boundary

- **Parent problem:** still open on the infimum side.
- **Supremum:** externally solved at `2sqrt2`; this campaign does not claim priority.
- **Best estate numerical infimum candidate:** about `1.869809`, currently weaker than the public `1.835...` upper bound.
- **Exact reusable mathematics:** power invariance, translation invariance, elementary support containment, endpoint-family scaling reduction.
- **Scientific value of the record:** unusually explicit falsification of bad numerical evaluators and preservation of a final-state contradiction rather than post-hoc cleanup.
