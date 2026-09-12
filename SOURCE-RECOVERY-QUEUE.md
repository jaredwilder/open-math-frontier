# Source recovery queue — released mathematics with missing supporting bytes

**Author:** Jared Wilder  
**Started:** 2026-09-11

A mathematical result can be public while still be poorly reproducible because its original proof source, verifier, certificate, or large data object has not yet reached the public repository that describes it.

This queue exists to prevent that state from becoming permanent.

It is **not** a list of invalid mathematics. Each entry states exactly what is already public and what supporting artifact still needs recovery.

## Priority A — source recovery changes reproducibility materially

### AGI-ZETA-BOUNDED-CLOSE-2026-08-14 packet

The 2026-09-11 RH corpus inventory explicitly identifies a separate archive:

`AGI-ZETA-BOUNDED-CLOSE-2026-08-14.zip`

and describes it as a **32-file zeta packet** with its own pre-registration, failed-routes folder, fresh-court A/B replication, and `verify_zeta_packet.py`.

The current session export contains the inventory pointer but **not the archive bytes**. A filesystem/artifact-closure search of the exported session found no copy of the ZIP or its constituent packet files.

**Missing:** the complete `AGI-ZETA-BOUNDED-CLOSE-2026-08-14.zip` packet from the original Downloads/archive location.

Recovery target:

1. recover the exact ZIP bytes from the original archive of record;
2. preserve the original archive SHA-256;
3. inventory all 32 files before interpreting claims;
4. rerun `verify_zeta_packet.py` from the recovered bytes;
5. compare A/B replication receipts and failed-route records;
6. extract any surviving mathematics into the canonical RH subject home;
7. retain the raw packet under provenance rather than making the ZIP itself the reader-facing canonical home.

This packet has **not** been mathematically audited by the current release pass and should not be inferred from its filename or inventory description.

### Prime-gap admissibility formalization

Current public summary:

`jaredwilder/unpublished-math-papers/prime-gap-admissibility/README.md`

The summary records a multi-module Lean/mathlib chain containing finite Hardy–Littlewood admissibility counting, inclusion–exclusion, exact mod-2/mod-3 formulas, first-cover boundary results, and a finite admissibility bridge.

**Missing:** the original `.lean` source files / project tree.

The historical dossier is internally inconsistent about corpus size: it says “74 Lean theorems across 8 modules,” while its listed inventory appears to contain 9 modules and a different theorem total. Do not repeat either total as audited fact until the source tree is recovered and recounted.

Recovery target:

1. locate the original Lean modules;
2. preserve exact historical bytes/hashes when available;
3. run a current clean build;
4. count declarations directly from source;
5. record `#print axioms` / `sorry` status;
6. only then decide whether this formal program graduates to a dedicated repository.

### Sums of three cubes, k=114 Lean module

Current public summary:

`jaredwilder/unpublished-math-papers/sums-three-cubes-114/README.md`

The released mathematics includes the exact mod-7 theorem that every solution has exactly one variable divisible by 7, the mod-9 residue structure, the mod-21 search reduction, and a recorded inventory of **15 proved Lean theorems with 0 sorry**.

**Missing:** the referenced original Lean source

`UNIVERSAL_LAW/oracle/math/EG411Formal/EG411Formal/S3C_Oracle_114.lean`.

Recovery target: publish the historical source, build it, recount declarations and record its current axiom footprint.

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

## Resolved during the release

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
