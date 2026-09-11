# Start Here — September 2026 Open Math Drop

**Author:** Jared Wilder  
**Release window:** 2026-09-10 onward  
**Status:** live / append-only while the estate is still being cleared for publication

This is the shortest route into the public mathematics release under the `jaredwilder` GitHub account.
The release is still expanding. **Do not use a fixed repository count as the definition of the drop.**
The authoritative object is the public mathematical material itself, classified by evidence level and claim ceiling.

For the full map, use [`MATH-DROP-2026-09-10.md`](MATH-DROP-2026-09-10.md).  
For the historical scale benchmark, use [`HISTORICAL-SCALE-BENCHMARK.md`](HISTORICAL-SCALE-BENCHMARK.md).  
For the publication boundary protecting unpublished applied / patent-facing work, use
[`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md).

## Release-day scale

> **A serious candidate for the largest one-day public release of mathematical research by a single independent researcher.**

The phrase **“the biggest one-day drop in math history”** is used here as a release-volume claim, not as a claim that every file is a new theorem or that release size determines mathematical importance.

The first mechanically easy container count found **38 public repositories created in 17 hours, 5 minutes, 57 seconds**, from `2026-09-10T15:24:22Z` to `2026-09-11T08:30:19Z`. That number is an **initial new-repository lower bound, not the size of the mathematical drop**. The release also contains major September 10/11 publication expansions inside pre-existing repositories, most visibly `msl-ore-estate`, together with subject extractions whose mathematical object counts are much larger than their repository counts.

The historical benchmark found a formidable modern comparator in OpenAI's 1 August 2026 ten-result mathematics / theoretical-CS release, but no documented larger one-day public mathematics release by a single independent researcher. Because no global database indexes this exact historical category, the claim remains falsifiable rather than presented as a certified world record.

## 30-second view

The drop spans several mathematical object classes:

- **KERNEL-VERIFIED** — Lean accepted the stated declaration under the disclosed trust boundary.
- **PROVED / EXACT** — a conventional proof or exact finite computation is supplied for the stated scope.
- **CANDIDATE** — a serious reproduced argument with at least one load-bearing dependency outside the strongest available seal.
- **COMPUTATIONAL FRONTIER / WORKING RECORD** — bounded searches, ore, attack logs, formalization corpora, and research provenance.
- **RETRACTED / CORRECTED** — claims or routes later found unsound or superseded and preserved as part of the audit trail.

These classes coexist in the release; they are not interchangeable.

## Strong first reads

### 1. `integral-point-sets` — new published-number lower bound

**PROVED / EXACT:** `d(2,8) > 30000` for planar integral point sets in general position, improving the hereditary lower bound `d(2,8) >= 22270`. The repository ships the maximality computation, a compile-ready preprint, exact receipts, 394 impossibility certificates, and exact small-`n` results.

https://github.com/jaredwilder/integral-point-sets

### 2. `graham-alspach-extended` + certificate repos — tens of millions of verified finite instances

The Graham/Alspach sequenceability release covers `Z_29`, `Z_31`, `Z_37`, `Z_41`, `Z_43`, and `Z_61` beyond the published general subset-size range. `graham-alspach-extended` alone verifies **22,082,109 subsets** with independent Go and Python checking; the companion certificate bank carries adversarial corruptions and deterministic regeneration receipts.

https://github.com/jaredwilder/graham-alspach-certificates  
https://github.com/jaredwilder/graham-alspach-sequenceability  
https://github.com/jaredwilder/graham-alspach-extended

### 3. `additive-combinatorics-campaigns` — exact finite structure + kernel/LRAT proof

Includes minimum span **60** for the first 13-element C3-free set, classification through span 63, an exact C5-free minimum-span result, a base-7 construction with exponent `log_7(3) > 1/2`, and a Lean-kernel-checked theorem backed by a shipped **447,254-addition LRAT proof**.

https://github.com/jaredwilder/additive-combinatorics-campaigns

### 4. `erdos-theorems` — 79 kernel-clean declarations

A curated Lean theorem bank with **79 declarations across 20 files and 15 Erdős problems**, including the countable and full-finite-sums forms of the Erdős 949 avoidance theorem. Each declaration carries axiom-footprint accounting.

https://github.com/jaredwilder/erdos-theorems

### 5. `erdos-straus-progressions` — two complete iff classifications

Classifies **all** Erdős–Straus solutions whose ordered denominators form an arithmetic progression and **all** whose denominators form a geometric progression. Both parameterizations are iff within the stated families and ship executable verification.

https://github.com/jaredwilder/erdos-straus-progressions

### 6. `msl-ore-estate` — the mine under the release

The audited provenance layer exposes **322,370 math-bearing structured-field occurrences**, **65,834 problem-scoped unique normalized mathematical texts**, **21,146 formula / identity / inequality occurrences**, **3,306 recovered Lean declarations**, **2,858 explicit closure obligations**, and a **238-row exact-distinct promoted catalog**. Its crown surfaces include the #1093 divisor-window reduction, #890↔#1093 bridge, #949 avoidance theorems, #289 all-prime p-adic obstruction, #243 deviation identity, #885 factor-difference duality, and the `C(13,6,3)` structural packet.

https://github.com/jaredwilder/msl-ore-estate

### 7. `ck-sequences` — 59 exact optimal finite values

Publishes exact values of `C_k(N)` for `k = 3,4,5` over **59 finite instances**, each accepted only with solver status `OPTIMAL`, direct witness re-checking, and reproducibility controls.

https://github.com/jaredwilder/ck-sequences

### 8. `open-math-frontier` — the machine-readable attack surface

Contains **9,926** source-attributed open mathematical targets, **8,501** with callable mechanical verifiers, plus formalization status, claim ceilings, published-bound metadata, implication structure, and the estate release map.

You are here.

## Formal proof layer

Good entry points:

- `erdos902` — a substantial kernel-checked tournament theory program: classical sandwich, finite window, DRT(23), QR23 symmetry, capacities, dominator cubes, private-cover barriers, and exact Cayley eliminations.
- `erdos-theorems` — curated kernel-clean theorem declarations.
- `lean-forge-graph-theory` — 218 standalone sorry-free graph-theory theorem files.
- `lean-contributions` — a 1,473-line zero-sorry Steiner/Kirkman development, Erdős 1066 formalization/API, and other Lean work.
- `erdos595-barrier-tower` — 27 sorry-free files proving the sharp continuum coverability barrier and related structure.
- `erdos152` and `erdos-cable-corpus` — large formalization corpora with explicit per-file evidence states.

## Audit and integrity layer

The release keeps falsification and correction material public **as support for the mathematical record, not as the headline for unrelated results**:

- `lean-semantic-blades` — deterministic semantic checks for source/formalization drift;
- `erdos835-lean-audit` — an axiom audit whose negative findings are themselves the result;
- `erdos-findings-ledger` — scope-pinned verdicts and evidence paths;
- `erdos-campaign-archive` and `erdos-attack-logs` — full-denominator research provenance;
- `eg411-superseded-closure-claims` and `erdos411-retraction-record` — preserved historical correction records.

The operating rule is simple: **the theorem statement says what was established; the evidence class says how strongly; the audit trail says what failed. None substitutes for the others.**

## Applied-IP boundary

The math release is **not** a blanket release of the broader research estate. Pure theorem/proof/code assets may be published after claim review; applied biomedical, control, energy, simulation, product, trade-secret, patent-claim, or commercially load-bearing embodiments remain held unless separately and deliberately cleared.
See [`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md) before extracting material from mixed artifacts.

## Live-release rule

This file is a front door, not a frozen inventory. As additional estate objects clear the correctness, authority, prior-art, and IP gates, they should be added to the full release map and promoted here when they materially improve a new reader's understanding of the drop.
