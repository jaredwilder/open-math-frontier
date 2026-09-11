# Live Addenda — September 11, 2026

**Author:** Jared Wilder  
**Purpose:** append-only supplement to `MATH-DROP-2026-09-10.md` while release-day publication is still active.

The September 10 release map was necessarily a snapshot. This file records material that went public after that map was written and should be folded into the canonical map during the final release-surface pass.

## New repositories now public

### `graham-alspach-extended`

**EXACT FINITE COMPUTATION / DUAL VERIFIED.**

Extends the Graham/Alspach sequenceability release to four further cyclic groups:

| modulus | covered subset sizes | subsets covered | orbit representatives |
|---|---:|---:|---:|
| Z_37 | 29–36 | 10,739,176 | 298,344 |
| Z_41 | 34–40 | 4,598,479 | 114,998 |
| Z_43 | 36–42 | 6,220,768 | 148,157 |
| Z_61 | 56–60 | 523,686 | 8,738 |
| **total** | | **22,082,109** | **570,237** |

Each accepted witness family is checked by independent Go and Python implementations. Z_37, Z_41 and Z_43 also carry adversarial corruption suites and deterministic regeneration receipts. The repository explicitly separates three generated-but-unverified moduli and does not ship those witnesses as verified evidence.

This is a finite verification in the stated groups and size ranges, not a proof of the full Graham/Alspach conjecture.

Repository: https://github.com/jaredwilder/graham-alspach-extended

### `erdos-straus-progressions`

**PROVED RESTRICTED-FAMILY CLASSIFICATIONS + EXECUTABLE CHECKS.**

Two complete if-and-only-if classifications inside the Erdős–Straus equation `4/n = 1/x + 1/y + 1/z`:

1. all positive solutions whose ordered denominators form an arithmetic progression;
2. all integer solutions whose denominators form a geometric progression.

Both parameterizations are unique within their stated family. Both imply that no primitive denominator triple exists in that family. The repository ships separate AP and GP verifiers, brute-force agreement checks, negative controls, and wider committed sweeps.

The full Erdős–Straus conjecture remains open and is explicitly stated to be untouched.

Repository: https://github.com/jaredwilder/erdos-straus-progressions

### `ck-sequences`

**EXACT FINITE OPTIMA; NOVELTY NOT YET ADJUDICATED.**

Publishes exact values of `C_k(N)` for the largest subset of `{1,...,N}` containing no tuple with vanishing k-th finite difference:

- C3: 16 values for N = 30..45;
- C4: 26 values for N = 1..26;
- C5: 17 values for N = 1..17.

All 59 values were accepted only with CP-SAT status `OPTIMAL`, direct witness verification, a vacuity guard, and successful reproduction of published OEIS benchmark sequences. C3 was independently recomputed in a separate process.

The repository explicitly does **not** claim historical novelty for the values until literature adjudication is complete.

Repository: https://github.com/jaredwilder/ck-sequences

## Release-surface corrections still required

1. `erdos-release-index` still opens with a frozen count of **thirty-six** public repositories. That count is already obsolete and should be replaced by a live-release description or a generated count after the drop stops moving.
2. `open-math-frontier` is the declared canonical hub, while `erdos-release-index` also presents itself as an index. The final surface should make one canonical and the other a curated Erdős-facing index rather than leave two competing front doors.
3. Fixed repository counts should be avoided during the active release window. The release is append-only and still growing.
4. New repositories should not be promoted merely because they exist. Promotion requires a clear claim class, scope ceiling, reproducibility story, and—where novelty matters—prior-art adjudication.
5. Empty-looking GitHub size metadata is not sufficient to classify a repository as empty during active publication; README/content inspection is required. Several September 11 repositories populated immediately after creation.

## Current suggested reading order

1. `START-HERE.md`
2. `MATH-DROP-2026-09-10.md`
3. `PUBLICATION-FIREWALL.md`
4. `integral-point-sets`
5. `additive-combinatorics-campaigns`
6. Graham/Alspach trilogy (`graham-alspach-certificates`, `graham-alspach-sequenceability`, `graham-alspach-extended`)
7. `erdos-straus-progressions`
8. `ck-sequences`
9. formal proof/audit corpora
10. failure, retraction and working-record repositories

This addendum should remain append-only until the release stabilizes, after which its promoted entries can be folded into the canonical map and the file retained as release-day provenance.
