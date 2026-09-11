# MathFire 8.0.0 — Pure-Mathematics Release

**Author:** Jared Wilder  
**Public release:** 2026-09-10

This file extracts the pure mathematical results from MathFire Round Eight without releasing or marketing the broader research-engine/product architecture.

The source release added 91 executable operations, 364 generated campaigns, one corruption attack per new operation, and independent-result gates. Those engineering counts are context; the two mathematical results below are the publication units.

## Result A — Erdős–Straus solutions with denominators in arithmetic progression

Internal theorem id:

```text
round8.erdos_straus_ap_parameterization_theorem
```

**Authority in the archived release:** all-parameter algebraic proof, plus an independent implementation sanity layer.

The theorem concerns the restricted Erdős–Straus equation

\[
\frac4n=\frac1x+\frac1y+\frac1z
\]

under the additional condition that the three denominators form an arithmetic progression.

The archived release reports:

- an all-parameter algebraic derivation for the AP-denominator family;
- a separate independent verifier importing no MathFire code;
- **76,115** coprime parameter pairs checked by that verifier;
- **456,690** constructed solutions independently checked.

### Scope ceiling

This is **not a solution of the Erdős–Straus conjecture**. It is a theorem about the AP-denominator subfamily.

The estate's original novelty clearance labeled it `apparently_new_after_systematic_search`, but this public release deliberately does **not** elevate that to a priority claim. Parametric and arithmetic-progression methods for Erdős–Straus sit in a substantial existing literature. The exact formula should be compared line-by-line with that literature before any historical novelty statement is made.

The independent finite verifier is a sanity check on the all-parameter algebra, not the logical proof of the universal theorem.

## Result B — finite multiplicative classification on `[50]`

Internal theorem id:

```text
round8.multiplicative_n50_theorem
```

Three independent implementations agree on the exact finite classification:

- maximum: **35**;
- minimum transversal: **15**;
- number of extremizers: **240**;
- canonical extremal digest: recorded in the source release;
- first witness: recorded;
- extremizer core: recorded.

The implementations were intentionally different:

1. primary bit-mask transversal solver;
2. independent Python `set` / `frozenset` solver;
3. independent C branch-and-bound implementation.

### Scope ceiling

This theorem is **strictly scoped to `[50]`**. It is not an asymptotic classification and is not evidence for an unproved infinite extrapolation unless a transfer theorem is supplied.

## Evidence discipline

The release architecture required each mathematical operation to have:

1. a structural recognizer;
2. an executable transformation;
3. operation-specific result semantics;
4. independent certificate replay;
5. hostile-corruption rejection;
6. held-out campaigns;
7. explicit finite or symbolic scope.

Those are engineering controls around the results. They do not alter the mathematical claim ceiling.

## Nonclaims

- MathFire does not solve arbitrary number theory problems.
- The AP theorem does not settle Erdős–Straus.
- The `[50]` theorem does not become an infinite theorem by pattern recognition.
- `apparently_new_after_systematic_search` is not a universal novelty certificate.

## What is deliberately not released here

This document extracts theorem statements and verification facts only. It does **not** disclose product-facing orchestration, commercially load-bearing research-engine internals, authenticated reasoning-capsule designs, or other implementation material identified elsewhere in the estate as potential IP.

Pure mathematics: public. Product mechanism: separate decision.
