# Source recovery queue — released mathematics with missing supporting bytes

**Author:** Jared Wilder  
**Started:** 2026-09-11

A mathematical result can be public while still be poorly reproducible because its original proof source, verifier, certificate, or large data object has not yet reached the public repository that describes it.

This queue exists to prevent that state from becoming permanent.

It is **not** a list of invalid mathematics. Each entry states exactly what is already public and what supporting artifact still needs recovery.

## Priority A — source recovery changes reproducibility materially

### Erdős #1005 Farey program

Current public summary:

`jaredwilder/unpublished-math-papers/erdos1005-farey/README.md`

The summary preserves several coherent reductions, period-36/scaling structure, retractions and a named remaining global theorem.

**Missing:** the full underlying source packet. One key lattice-count identity is visibly truncated in the surviving summary and should not be reconstructed from guesswork.

Recovery target: locate the original packet / transcript / source document, restore the exact missing formula from provenance, and only then promote the program beyond its current provenance-blocked status.

### Erdős #1061 primitive-seed certificate bank

Current detailed program:

`jaredwilder/unpublished-math-papers/erdos1061-aliquot-square/`

The exact verifier is public and the receipt pins the certificate bank, but the main CSV contains **152,803 primitive seeds** and is about 17 MB; it was not copied into GitHub through the connected release path.

Pinned SHA-256:

`343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68`

**Missing from the public subject tree:** `ERDOS1061_PRIMITIVE_SEEDS_200K.csv`.

Recovery target: publish the exact CSV bytes matching the pinned hash, rerun the existing verifier from the public location, and retain the receipt.

## Priority B — finite certificates / replay artifacts

### Conference-switching Ramsey-book elimination

Current canonical result note:

`jaredwilder/combinatorial-records/ramsey/conference-switching-book-elimination.md`

The estate records an exact construction-class impossibility theorem and historical producer / independent replay / one-command verification artifacts.

**Missing:** the original standalone verifier / receipt files from the source campaign.

Recovery target: locate and publish the historical replay artifacts without changing the theorem statement.

### Erdős–Selfridge odd seven-modulus obstruction

Current canonical result note:

`jaredwilder/combinatorial-records/covering-systems/erdos-selfridge-odd-seven-moduli.md`

The estate records independent CP-SAT and PySAT certification of the exact finite obstruction on the modulus set `{3,5,7,9,11,13,15}`.

**Missing:** the original solver models / certificates / run receipts.

Recovery target: publish both independent formulations and a small deterministic replay summary.

## Resolved / removed during the release

### AGI-ZETA-BOUNDED-CLOSE-2026-08-14 — REMOVED AS FALSE RH DEBT, 2026-09-14

An earlier recovery pass treated the archive name

`AGI-ZETA-BOUNDED-CLOSE-2026-08-14.zip`

as a pointer to missing Riemann-zeta mathematics.

The later raw-ore industrial ingest explicitly corrected that interpretation after Library inspection: `AGI-ζ` was an **unrelated bounded cross-domain learning packet using a Greek-letter project naming sequence**, not a missing RH packet.

Therefore this item is removed from the RH/source-recovery debt rather than kept as an unresolved mathematical artifact. The correction is semantic: no theorem or source packet is being declared recovered; the old classification itself was wrong.

### Prime-gap admissibility formalization — RESOLVED 2026-09-14

The original Lean source was recovered from `EG203-KILLSHOT-ROUND-044-SOURCE-PREDICATE-AUDIT.zip` and published in:

`jaredwilder/prime-gap-admissibility`

The recovered project contains **eleven source modules**. A pinned Lean/mathlib GitHub Actions replay completed `lake build` successfully on 2026-09-14. The repository deliberately does **not** inherit the old inconsistent “74 theorems / 8 modules” headline, and it does not claim an asymptotic prime-gap theorem. The universal permutation/bijection boundary remains open.

### Sums of three cubes, k=114 Lean module — RESOLVED 2026-09-14

The historical source `S3C_Oracle_114.lean` was recovered from the local estate and published in:

`jaredwilder/sums-three-cubes-114/lean/S3C_Oracle_114.lean`

The public repository preserves the exact mod-9/mod-7 formal core, including the exact mod-7 one-zero-coordinate result. The full mod-21 residue table remains a written/search-layer derivation unless separately kernelized, and the historical PARI scripts/raw search outputs have **not** been recovered. No fresh Lean build is claimed there unless and until one is recorded by that repository.

### Kirkman / Steiner triple-system Lean development — RESOLVED

An earlier archive note said the source was missing. The canonical public source was subsequently located at:

`jaredwilder/lean-contributions/mathlib-pr/Mathlib/Combinatorics/Design/SteinerTriple.lean`.

The archive provenance note has been corrected. The committed development is 1,473 lines, imports `Mathlib`, and contains zero `sorry`.

## Recovery doctrine

1. **Do not fabricate missing source from a summary.** Reconstructed mathematics can be useful, but it is not the historical artifact.
2. **Preserve hashes and old bytes** when they are recovered.
3. **Re-run recovered code in the current public environment** and record whether it still passes.
4. **Separate source recovery from theorem validation.** Finding a file proves provenance, not correctness.
5. **Close entries explicitly.** Once the artifact is public in its canonical home, move it to the resolved section rather than leaving a permanent “missing” warning.

A release is not finished merely because the theorem statement is visible. If the proof/code/certificate was part of the evidence, that evidence should be findable too.
