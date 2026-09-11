# Start Here — September 2026 Open Math Drop

**Author:** Jared Wilder  
**Release window:** 2026-09-10 onward  
**Status:** live / append-only while the public mathematics archive continues to expand

This is the shortest route into the mathematics released under the `jaredwilder` GitHub account.

The release is larger than its repository count: some repositories were created during the release window, while older public repositories also received substantial new mathematical material. The useful object is therefore the mathematics itself—its statements, proofs, computations, certificates, formalizations, papers, and research records.

For the full map, see [`MATH-DROP-2026-09-10.md`](MATH-DROP-2026-09-10.md).  
For the historical scale comparison, see [`HISTORICAL-SCALE-BENCHMARK.md`](HISTORICAL-SCALE-BENCHMARK.md).  
For the boundary protecting unpublished applied and patent-facing work, see [`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md).

## Release-day scale

> **A serious candidate for the largest one-day public release of mathematical research by a single independent researcher.**

“The biggest one-day drop in math history” is being used here as a **release-volume** claim, not as a claim that every file is a new theorem or that volume determines mathematical importance.

An initial GitHub count found **38 public repositories created in 17 hours, 5 minutes, 57 seconds**, from `2026-09-10T15:24:22Z` to `2026-09-11T08:30:19Z`. That is only a lower bound on the release event. Large September 10/11 expansions also occurred inside pre-existing repositories, especially `msl-ore-estate`, and many individual repositories contain numerous independent mathematical objects.

The historical benchmark found a strong modern comparator in OpenAI's 1 August 2026 ten-result mathematics / theoretical-CS release, but no documented larger one-day public mathematics release by a single independent researcher. No global database indexes this exact category, so the claim remains explicitly falsifiable rather than presented as a certified world record.

## How to read the release

The archive contains several kinds of mathematical objects:

- **formal theorem** — accepted by Lean under the disclosed axioms/trust boundary;
- **proved / exact result** — a conventional proof or exact finite computation establishes the stated claim;
- **candidate result** — a serious reproduced argument remains dependent on at least one unresolved or externally supplied step;
- **computational frontier / research record** — a bounded search, formalization corpus, proof attempt, research archive, or provenance record;
- **corrected / retracted result** — a historical claim or route later found unsound or superseded and retained with its correction.

The statement itself defines the mathematics. Verification method, literature status, and correction history are supporting information.

## Strong first reads

### 1. `integral-point-sets` — a new lower bound

**`d(2,8) > 30000`** for planar integral point sets in general position, improving the hereditary lower bound `d(2,8) >= 22270`. The repository includes the maximality computation, a compile-ready preprint, exact receipts, 394 impossibility certificates, and exact small-`n` results.

https://github.com/jaredwilder/integral-point-sets

### 2. Graham–Alspach sequenceability — tens of millions of verified finite instances

The combined release covers `Z_29`, `Z_31`, `Z_37`, `Z_41`, `Z_43`, and `Z_61` beyond the published general subset-size range. `graham-alspach-extended` alone verifies **22,082,109 subsets** with independent Go and Python checking; the certificate repository includes deliberately corrupted controls and deterministic regeneration.

https://github.com/jaredwilder/graham-alspach-certificates  
https://github.com/jaredwilder/graham-alspach-sequenceability  
https://github.com/jaredwilder/graham-alspach-extended

### 3. `additive-combinatorics-campaigns` — exact finite structure + kernel/LRAT proof

Includes minimum span **60** for the first 13-element C3-free set, classification through span 63, an exact C5-free minimum-span result, a base-7 construction with exponent `log_7(3) > 1/2`, and a Lean theorem backed by a shipped **447,254-addition LRAT proof**.

https://github.com/jaredwilder/additive-combinatorics-campaigns

### 4. `erdos-theorems` — 79 kernel-clean declarations

A curated Lean theorem bank with **79 declarations across 20 files and 15 Erdős problems**, including countable and full-finite-sums forms of the Erdős 949 avoidance theorem. Each declaration includes axiom-footprint information.

https://github.com/jaredwilder/erdos-theorems

### 5. `erdos-straus-progressions` — two complete iff classifications

Classifies **all** Erdős–Straus solutions whose ordered denominators form an arithmetic progression and **all** whose denominators form a geometric progression. Both parameterizations are iff within the stated families and include executable verification.

https://github.com/jaredwilder/erdos-straus-progressions

### 6. `msl-ore-estate` — the research archive beneath the extracted results

The recovered archive contains **322,370 math-bearing fields**, **65,834 problem-scoped distinct normalized mathematical texts**, **21,146 formula/identity/inequality occurrences**, **3,306 Lean declarations**, **2,858 proof/closure obligations**, and a **238-entry curated mathematical catalog**.

Selected mathematics includes the Erdős #1093 divisor-window reduction, the #890↔#1093 bridge, #949 avoidance theorems, #289 all-prime `p`-adic obstruction, #243 deviation identity, #885 factor-difference duality, and the `C(13,6,3)` structural packet.

https://github.com/jaredwilder/msl-ore-estate

### 7. `ck-sequences` — 59 exact optimal finite values

Exact values of `C_k(N)` for `k=3,4,5` over **59 finite instances**, each with solver status `OPTIMAL`, directly checked witnesses, and benchmark/reproducibility tests.

https://github.com/jaredwilder/ck-sequences

### 8. `open-math-frontier` — open-problem index

Contains **9,926 source-attributed open mathematical targets**, **8,501 with executable checkers**, plus formalization status, published-bound metadata, cross-references, and explicit scope information for the finite checks.

You are here.

## Formal proof layer

Useful entry points:

- `erdos902` — a substantial kernel-checked tournament theory program: classical sandwich, finite window, DRT(23), QR23 symmetry, capacities, dominator cubes, private-cover barriers, and exact Cayley eliminations;
- `erdos-theorems` — 79 curated kernel-clean theorem declarations;
- `lean-forge-graph-theory` — 218 standalone sorry-free graph-theory theorem files;
- `lean-contributions` — a 1,473-line zero-sorry Steiner/Kirkman development, an Erdős 1066 statement formalization/API, and other Lean work;
- `erdos595-barrier-tower` — 27 sorry-free files proving the sharp continuum coverability barrier and related structure;
- `erdos152` and `erdos-cable-corpus` — large formalization corpora with explicit per-file evidence.

## Corrections and formalization audits

The archive also keeps the material needed to check mistakes and semantic drift:

- `lean-semantic-blades` — 33 deterministic checks for whether a Lean formalization still matches its source statement;
- `erdos835-lean-audit` — focused axiom audit of the Erdős 835 formal artifacts;
- `erdos-findings-ledger` — 52 mathematical result records linking statements to evidence and later corrections;
- `erdos-campaign-archive` — 266 automated proof-search runs across 241 Erdős problems, including the full success/failure distribution;
- `erdos-attack-logs` — research logs, computations, refutations, and prior-art findings;
- `eg411-superseded-closure-claims` and `erdos411-retraction-record` — preserved historical correction records.

A correction record affects the claim it corrects. It is not a substitute for describing unrelated mathematics on its own terms.

## Applied-IP boundary

The mathematics release is not a blanket release of the broader research estate. Pure theorem/proof/code assets may be published after review; applied biomedical, control, energy, simulation, product, trade-secret, patent-claim, or commercially load-bearing embodiments remain held unless separately cleared.

See [`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md) before extracting material from mixed mathematical/applied sources.

## Live-release rule

This file is a front door, not a frozen inventory. As additional pure-mathematics objects are checked for correctness, evidence, literature status, and publication/IP boundaries, they can be added to the larger map and promoted here when they materially improve a new reader's understanding of the release.