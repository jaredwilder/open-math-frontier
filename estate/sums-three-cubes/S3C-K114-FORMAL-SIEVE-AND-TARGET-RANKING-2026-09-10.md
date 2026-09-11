# Sums of Three Cubes — k=114 Formal/Sieve Scaffold and Comparative Target Ranking

**Author:** Jared Wilder  
**Source campaign:** 2026-05-27  
**Public release:** 2026-09-10

## Status first

This campaign **did not find a new representation of an open sums-of-three-cubes case**. No triple was found for k=114 or for the other tracked cases.

The durable assets are:

1. a formal/modular scaffold for `a^3+b^3+c^3=114`;
2. exact mod-3 / mod-7 / CRT restrictions and a practical sieve;
3. bounded search receipts, explicitly not promoted to global mathematics;
4. partial singular-series measurements;
5. a comparative target-ranking result showing that the smallest tracked case was not the best compute target under that proxy;
6. a negative-results ledger preventing bounded null searches or one-prime heuristics from being oversold.

The labels “open” below reproduce the **May 2026 source campaign’s literature baseline**. They are historical provenance, not a claim that no case changed status after that date.

---

# I. Equation and classical obstruction

The equation is

\[
a^3+b^3+c^3=k,
\qquad a,b,c\in\mathbb Z.
\]

Cubes modulo 9 lie in `{0,±1}`. Therefore integers

\[
k\equiv4,5\pmod9
\]

are obstructed.

The campaign focused first on

\[
\boxed{k=114}
\]

under its then-current literature baseline.

Since

\[
114\equiv6\equiv-3\pmod9,
\]

any representation forces each cube to contribute `-1 mod 9`, hence each base lies in the `-1 mod 3` class:

\[
\boxed{a\equiv b\equiv c\equiv2\pmod3.}
\]

---

# II. Exact mod-7 structure for k=114

Cube residues modulo 7 are

\[
\{0,1,6\}.
\]

Since

\[
114\equiv2\pmod7,
\]

the only compatible residue pattern is one zero cube residue plus two `1` cube residues. Therefore every solution satisfies:

\[
\boxed{\text{exactly one of }a,b,c\text{ is divisible by }7.}
\]

Equivalently, the campaign isolates `p=7` as the first strong local-density penalty for `k=114`.

Archived formal theorem identities include:

- `cube_residues_mod7`;
- `two_not_cube_mod7`;
- `s3c_114_mod7_zero_count`;
- `s3c_114_mod7_one_div_by7`;
- `s3c_114_combined_sieve_necessary`.

---

# III. CRT sieve modulo 21

Combining the mod-3 and mod-7 constraints gives:

| role | mod 3 | mod 7 | allowed mod 21 |
|---|---:|---:|---:|
| unique 7-divisible variable | `2` | `0` | `14` |
| each nonzero-mod-7 variable | `2` | `{1,2,4}` | `{8,2,11}` |

After using permutation symmetry to choose which variable is 7-divisible, the source campaign estimates an approximately

\[
\boxed{343\times}
\]

reduction against the naive residue search.

Empirical engineering receipts from the local run:

- unsieved height `H=5,000`: about 176 s;
- sieved height `H=20,000`: about 44 s.

Thus the sieve covered roughly 16 times more height in about one quarter the time in that local implementation.

These are performance receipts, not asymptotic complexity theorems.

---

# IV. Formal Lean scaffold recovered from the campaign

The source campaign records a built file

`S3C_Oracle_114.lean`

with `0 sorry` and 15 theorem identities:

1. `cube_residues_mod9`
2. `s3c_mod9_not_four`
3. `s3c_mod9_not_five`
4. `k114_mod9`
5. `k114_obstruction_clear`
6. `s3c_114_each_cube_minus1`
7. `s3c_114_base_mod3`
8. `s3c_114_no_soln_height3`
9. `s3c_114_from_triple`
10. `cube_residues_mod7`
11. `k114_mod7`
12. `s3c_114_mod7_zero_count`
13. `s3c_114_mod7_one_div_by7`
14. `two_not_cube_mod7`
15. `s3c_114_combined_sieve_necessary`

The future-solution verification pattern was deliberately separated from search:

```lean
theorem s3c_114_verified : IsS3C 114 :=
  s3c_114_from_triple A B C (by norm_num)
```

with `A,B,C` replaced only by an actual found triple.

**Authority caveat:** this public packet preserves the source campaign's claimed build record; this release-day pass did not independently recover and rebuild that exact Lean file.

---

# V. Bounded local searches

The campaign reports:

- `NO_SOL_H5000` for k=114;
- `NO_SOL_H20000_SIEVED` for k=114.

These are deliberately **not** marketed as mathematical progress relative to state-of-the-art S3C searches. Their value is toolchain reproducibility and sieve validation.

The doctrine rule is explicit:

> “No solution up to H” is not “no solution exists.”

---

# VI. Partial singular-series measurements

For primes `p≤80`, the source PARI computation reported

\[
S_{\le80}(114)=0.448679,
\]

versus the solved baseline

\[
S_{\le80}(42)=0.673514.
\]

The ratio is approximately

\[
\boxed{0.6662.}
\]

At `p=7` specifically, the local factor/count proxy was recorded as

- `k=114`: count 27, ratio `0.551020`;
- `k=42`: count 55, ratio `1.122449`.

The relative `p=7` penalty is therefore about

\[
0.491.
\]

This is consistent with the exactly-one-zero-mod-7 theorem above.

Partial singular products are **measurement proxies**, not proofs of search difficulty or existence.

---

# VII. Comparative target-ranking experiment

The campaign computed the same `p≤80` partial-product proxy for

\[
\{42,114,390,627,633,732,921,975\}.
\]

The May-2026 table was:

| k | source-session status | partial product `p≤80` | ratio vs 42 |
|---:|---|---:|---:|
| 42 | solved baseline | 0.673514 | 1.000000 |
| 627 | tracked open | 0.499977 | 0.742342 |
| 732 | tracked open | 0.498879 | 0.740711 |
| 114 | tracked open | 0.448679 | 0.666177 |
| 633 | tracked open | 0.345331 | 0.512731 |
| 921 | tracked open | 0.264835 | 0.393214 |
| 975 | tracked open | 0.247020 | 0.366763 |
| 390 | tracked open | 0.220931 | 0.328027 |

Under **this specific partial singular-series proxy**, the source campaign ranks the tracked unsolved targets:

\[
\boxed{627\approx732 >114>633>921>975>390}
\]

from most locally favorable to least favorable.

The strategic finding is therefore:

> the smallest tracked open case was **not** the best compute target under this measured local-density proxy.

The source recommendation was to prioritize `k=627` or `k=732` before `k=114`, while avoiding `k=390` for near-term brute-force work.

This is a **target-selection heuristic/result**, not a theorem that one case has a smaller actual first solution than another.

---

# VIII. Conditional first-solution-height heuristic

The source campaign used the heuristic model

\[
N(k,H)\sim c\,S(k)\log H
\]

and anchored it to the known `k=42` solution scale. This gave source-session estimates such as

- `k=627`: about `10^22.8`;
- `k=732`: about `10^22.8`;
- `k=114`: about `10^25.4` from the `p≤80` product;
- `k=633`: about `10^33.0`;
- `k=921`: about `10^43.0`;
- `k=975`: about `10^46.1`;
- `k=390`: about `10^51.6`.

A separate `p≤200` partial-product estimate for `k=114` gave about `10^31.7`.

These are explicitly **heuristic HOLD values**, not predictions with proof authority.

---

# IX. A useful mod-7 contrast

The campaign records:

\[
633\equiv3\pmod7.
\]

Although `3` is not itself a cubic residue modulo 7, it decomposes as

\[
3=1+1+1\pmod7.
\]

Thus unlike `k=114`, the mod-7 analysis does **not** force one variable to be divisible by 7 for `k=633`.

This kills the oversimplification that all difficult tracked cases are difficult for the same mod-7 reason.

---

# X. Negative-results ledger

The campaign permanently banks these nonclaims:

1. **No S3C case was solved.** No new triple was found.
2. **The smallest tracked case was not the hardest under the measured proxy.**
3. **Mod 7 alone does not rank difficulty.** For example, `921` shares a mod-7 class with `627/732` but had a substantially lower full `p≤80` product.
4. **Local null searches to 5,000 or 20,000 are not literature-level search bounds.**
5. **A bounded null search is never promoted to universal nonexistence.**
6. **Lean verifies exact identities/residue facts or an explicit candidate triple; it is not being used as a bulk search oracle.**

---

# XI. Reproducibility/provenance from the source session

The source record names PARI scripts for the modular/singular-series work, including:

- `oracle_s3c_r2_sieve.gp`
- `oracle_s3c_r4.gp`
- `oracle_s3c_singular.gp`
- `oracle_s3c_r6.gp`
- `oracle_s3c_r7_sieved.gp`
- `oracle_s3c_r8_sing200.gp`
- `oracle_s3c_r8b_delta.gp`
- `oracle_s3c_all7_sing80.gp`

and records original project commits for the execution-card run, k=114 findings record, and comparative ranking run.

## Final release interpretation

This is not a solved-Diophantine-equation announcement. It is a public release of a useful computational-number-theory scaffold:

- exact modular restrictions;
- a formally oriented proof interface;
- a high-yield CRT sieve;
- local-density measurements;
- comparative compute-target selection;
- and explicit negative knowledge about what those computations do not establish.
