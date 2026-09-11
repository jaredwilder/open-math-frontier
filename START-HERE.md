# Start Here — September 2026 Open Math Drop

**Author:** Jared Wilder  
**Release window:** 2026-09-10 onward  
**Status:** live / append-only while the estate is still being cleared for publication

This is the shortest route into the public mathematics release under the `jaredwilder` GitHub account.
The release is still expanding. Do **not** use a fixed repository count as the definition of the drop.
The authoritative object is the public material itself, classified by evidence level and claim ceiling.

For the full map, use [`MATH-DROP-2026-09-10.md`](MATH-DROP-2026-09-10.md).  
For the historical scale benchmark, use [`HISTORICAL-SCALE-BENCHMARK.md`](HISTORICAL-SCALE-BENCHMARK.md).  
For the publication boundary protecting unpublished applied / patent-facing work, use
[`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md).

## Release-day scale

> **A serious candidate for the largest one-day public release of mathematical research by a single independent researcher.**

The phrase **“the biggest one-day drop in math history”** is being used here as a release-volume claim,
not as a claim that every file is a new theorem or that this release outranks every historical event in
mathematical importance.

The literal one-day condition has been checked. GitHub's exact creation-time query returns **38 public
repositories** created between `2026-09-10T15:24:22Z` and `2026-09-11T08:30:19Z` — a rolling window of
**17 hours, 5 minutes, 57 seconds**. Many of those repositories contain multiple independent papers,
theorems, formal declarations, exact computations, certificates, or research records.

The historical benchmark found a formidable modern comparator in OpenAI's 1 August 2026 ten-result
mathematics / theoretical-CS release, but no documented larger one-day public mathematics release by a
single independent researcher. Because no global database indexes this exact historical category, the
claim remains explicitly falsifiable rather than presented as a certified world record. If a larger
documented comparator is found, the benchmark should be corrected.

## 30-second view

This is not a collection of only successes. It intentionally contains proved mathematics, exact finite
computations, Lean formalizations, candidate results, machine-readable open-problem frontiers, failed
routes, negative results, correction records, and retractions.

A reader should keep five evidence classes separate:

- **KERNEL-VERIFIED** — Lean accepted the stated declaration under the disclosed trust boundary.
- **PROVED / EXACT** — a conventional proof or exact finite computation is supplied for the stated scope.
- **CANDIDATE** — serious and reproduced, but at least one load-bearing dependency remains outside the strongest seal.
- **WORKING RECORD / FRONTIER** — search bounds, ore, attack logs, incomplete formalizations, or research provenance.
- **RETRACTED / CORRECTED** — a claim or route later found unsound or superseded and deliberately left public.

## Strong first reads

### 1. `integral-point-sets` — a published-number move

**PROVED / EXACT:** `d(2,8) > 30000` for planar integral point sets in general position, improving the
hereditary lower bound `d(2,8) >= 22270`. The repository ships the maximality computation, a compile-ready
preprint, exact receipts, 394 impossibility certificates, and negative sweeps.

https://github.com/jaredwilder/integral-point-sets

### 2. `additive-combinatorics-campaigns` — exact finite structure + kernel/LRAT proof

Includes the exact minimum span 60 for the first 13-element C3-free set, classification through span 63,
an exact C5-free minimum-span result, a base-7 construction with exponent `log_7(3) > 1/2`, and a
Lean-kernel-checked theorem backed by a shipped 447,254-addition LRAT proof.

https://github.com/jaredwilder/additive-combinatorics-campaigns

### 3. Graham/Alspach sequenceability — several large verified finite ranges

The companion repositories cover Z_29 and Z_31, and the newest extension covers Z_37, Z_41, Z_43 and
Z_61. `graham-alspach-extended` alone verifies **22,082,109 subsets** with independent Go and Python
checkers; three of its four main moduli also ship adversarial corruption suites and deterministic
regeneration receipts.

https://github.com/jaredwilder/graham-alspach-certificates  
https://github.com/jaredwilder/graham-alspach-sequenceability  
https://github.com/jaredwilder/graham-alspach-extended

### 4. `erdos-straus-progressions` — two iff classifications inside an open conjecture

Classifies **all** Erdős–Straus solutions whose denominators form an arithmetic progression and **all**
whose denominators form a geometric progression. Both parameterizations are iff within the stated
families and ship executable verification. The full Erdős–Straus conjecture remains open.

https://github.com/jaredwilder/erdos-straus-progressions

### 5. `ck-sequences` — exact finite sequence values with optimality certificates

Publishes exact values of `C_k(N)` for k = 3, 4, 5 over 59 finite instances, each accepted only with
solver status `OPTIMAL`, direct witness re-checking, vacuity guards, and reproduction of known OEIS
sequences as negative controls. Historical novelty of the values is explicitly not assumed.

https://github.com/jaredwilder/ck-sequences

### 6. `open-math-frontier` — the machine-readable attack surface

Contains **9,926** source-attributed open mathematical targets, **8,501** with callable mechanical
verifiers, plus formalization status, claim ceilings, published-bound metadata, implication structure,
and the estate release map.

You are here.

## Formal proof / audit layer

Good entry points:

- `erdos-theorems` — curated Lean declarations with axiom-footprint receipts.
- `lean-forge-graph-theory` — a large sorry-free graph-theory corpus with machine receipts.
- `lean-contributions` — public Mathlib-facing work including Steiner/Kirkman development.
- `lean-semantic-blades` — semantic certification gates designed to catch formally valid but source-wrong proofs.
- `erdos152` and `erdos-cable-corpus` — raw formalization corpora with their defects exposed rather than hidden.

## The credibility layer is part of the release

If you want to know whether the release distinguishes mathematics from wishful thinking, read the failures:

- `eg411-superseded-closure-claims`
- `erdos411-retraction-record`
- `oracle-math-honest-inventory`
- `erdos-findings-ledger`
- `erdos-attack-logs`

The release policy is that an unfinished computation is not a null result, a bounded search is not a proof
beyond its bound, a candidate is not promoted to theorem, and a false route stays visible after correction.

## Applied-IP boundary

The math release is **not** a blanket release of the broader research estate. Pure theorem/proof/code assets
may be published after claim review; applied biomedical, control, energy, simulation, product, trade-secret,
patent-claim, or commercially load-bearing embodiments remain held unless separately and deliberately cleared.
See [`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md) before extracting material from mixed artifacts.

## Live-release rule

This file is intentionally a **front door, not a frozen inventory**. As additional estate objects clear the
correctness, authority, prior-art, and IP gates, they should be added to the full release map first and promoted
here only when they materially improve a new reader's understanding of the drop.
