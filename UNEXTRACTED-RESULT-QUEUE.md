# Unextracted Mathematics Queue — estate saturation control surface

**Author:** Jared Wilder  
**Started:** 2026-09-11  
**Purpose:** prevent mathematically meaningful results from remaining discoverable only inside provenance dumps, route registries, contradiction histories, formalizer packets, or broad theorem banks.

This is an **audit workload**, not an unresolved-theorem count.

A raw `PROVED` label is not automatically a valid theorem, a novel theorem, or an unpublic result. The queue exists to force every mathematical identity toward an explicit terminal disposition.

## Terminal dispositions

Every reviewed mathematical object must end in exactly one of these states:

- **CANONICAL_SUBJECT** — promoted into a focused problem or subject repository;
- **COMPACT_THEOREM** — routed into `jaredwilder/erdos-proved-lemmas` or another narrow theorem bank;
- **FAMILY_HOME** — routed into an existing coherent family repository such as `combinatorial-records` or `additive-combinatorics-campaigns`;
- **PUBLIC_MINE** — retained as provenance/research ore because it is not yet a theorem-grade or reader-facing object;
- **PUBLIC_HISTORICAL** — retained specifically as historical route/correction/retraction material;
- **SUBSUMED** — an equal-or-stronger public representation already exists;
- **QUARANTINED_MIXED_IP** — mathematical material cannot yet be separated safely from biomedical, patent, product, private-data, proprietary-system, or otherwise held source material.

`PENDING_SOURCE_AUDIT` is an active-work state only. It is not a terminal disposition.

## Hard estate surfaces still requiring saturation work

### 1. Latest-local `PROVED` states

Historical Day-2 estate census:

- **617** latest-local `PROVED` states;
- spread across **171** problem families;
- **1,238** raw `PROVED` events in the underlying chronology.

These counts are workflow-state counts, not theorem counts. Many rows will collapse as duplicates, corrected variants, known results, stronger-public-result subsumptions, or invalid historical labels.

**Required action:** group by normalized problem + mathematical statement; compare against current canonical public homes; route only the strongest scope-preserving proposition.

### 2. Historically omitted PROVED-bearing families

The early curated union covered 128 rows / 87 families, but horizontal mining found:

- **97 entire PROVED-bearing families omitted** by that early union;
- containing **282 latest-PROVED states**.

This is the clearest known burial-risk class in the estate.

Pass-3 recovered many high-value examples, but the class itself is not declared exhausted.

**Required action:** maintain a per-family disposition ledger until all 97 historical omission families are represented, subsumed, corrected, or explicitly retained as mine/history.

### 3. Contradiction / status-changing histories

Estate count:

- **1,428** contradiction or status-changing histories.

These are not noise. They can contain:

- false global claims with true child theorems;
- stale `FALSE` labels on true propositions;
- stronger later scope variants;
- finite-vs-global authority mistakes;
- semantic/object mismatches;
- retractions that define the real theorem boundary.

**Required action:** inspect by mathematical proposition, not by final workflow label. Every surviving child theorem must be routed; every false claim must retain a correction record where it matters.

### 4. Formalizer obligations

Pass-4/Day-2 recovery identified:

- **3,306** recovered Lean declarations overall;
- **556** uncertified formalizer obligations containing mathematical proof/claim/witness content;
- Delta2 landscape of **546** distinct theorem-attempt IDs: 270 kernel-checked / 276 kernel-failed;
- a prioritized **35-shot** kernel firing line in the historical audit.

A kernel failure caused by parser/API/resource/type engineering is not mathematical falsification.
A green kernel receipt also does not override a semantic mismatch.

**Required action:** separate mathematical proposition, formal statement, build result, axiom footprint, and source-fidelity status. Promote only when scope is matched.

### 5. Raw theorem-bearing archives and structured fields

Recovered estate scale includes:

- **322,370** recursively recovered math-bearing structured-field occurrences;
- **65,834** problem-scoped unique normalized mathematical texts;
- **50,261** exact-text-unique math texts versus principal earlier indexes;
- **21,146** formula / identity / inequality occurrences;
- **8,276** explicit premise→conclusion passages;
- **6,339** multi-ingredient recombination passages;
- **1,488** unfinished/load-bearing ore objects.

These are not claims of 322,370 or 65,834 theorems. They are mining surfaces.

**Required action:** rank by problem density, dependency centrality, proof/evidence strength, correction history, and whether the same object already has a canonical public home.

### 6. Cross-problem implication / revival graph

Recovered graph surfaces:

- **15,027** implication-stitch edges;
- **1,043** multi-hop candidate chains;
- **461** explicit route-revival requirements;
- **415** killed-route → later-positive candidates;
- **1,469** revival-requirement → existing-gold links;
- **606** branch-level composite dossiers;
- **303** per-problem synthesis dossiers.

**Required action:** mine for cases where several compact child theorems together constitute a research program deserving a dedicated repository, even though no single row looked repo-scale.

### 7. Missing source/certificate bytes

Known examples include recovered mathematical statements for which original solver receipts, historical Lean bytes, or large source data are missing from the current GitHub surface.

**Required action:** never fabricate missing artifacts. Publish the exact statement/evidence currently available and record the missing artifact as a provenance obligation.

## Already closed accounting surfaces

### Canonical Gold 56

`jaredwilder/erdos-proved-lemmas/CANONICAL-GOLD-56-DISPOSITION.md` gives a terminal public disposition for all **56** reviewed rows:

- **47 ROUTED / ROUTED_CORRECTED**;
- **9 SUBSUMED**;
- **0 HELD / PENDING**.

Do **not** spend extraction effort treating those 56 rows as unresolved merely because copies remain in ORE or broad repositories.

### Pass-3 gold

`jaredwilder/erdos-ore-findings/pass3-2026-09-02/` contains 29 curated result rows plus 28 fusion deductions, proof repairs and close audits.

Many are already routed or subsumed. New routing work must compare against the live public estate before creating another representation.

## Promotion threshold

A problem/program defaults toward a dedicated canonical repository when any of the following is true:

1. multiple nontrivial results form a dependency chain;
2. substantial formal code exists;
3. dedicated computation/certificates/witnesses exist;
4. there is a live frontier with explicit obligations;
5. correction/refutation history is mathematically load-bearing;
6. a paper or paper series exists;
7. a mathematician could reasonably follow the problem as a continuing research program.

A single compact child theorem does not need a toy repository.

## Non-double-counting rule

The same mathematical statement appearing in ORE, a theorem bank, a README, a paper and a Lean file is **one underlying mathematical result with multiple evidence/publication modalities**.

When counting the release, report separately:

- underlying deduplicated mathematical objects;
- formal/kernel artifacts;
- exact computations/certificates;
- candidates/open targets;
- refutations/corrections;
- provenance/mine objects;
- infrastructure/verifiers/corpora.

Do not sum those categories into a fake theorem count.

## Current highest-priority program promotions

See `BURIED-PROGRAMS-INDEX.md`. The current high-priority set includes at least:

- Erdős #738 / triangle-free Gyárfás–Sumner;
- Erdős–Gyárfás power-of-two cycles;
- Caccetta–Häggkvist directed triangles;
- fiber-coherence / cycle-rank / rank-three-kernel program;
- Erdős #890↔#1093;
- Erdős #77 diagonal Ramsey exponential-limit program;
- P6 Erdős–Hajnal;
- Erdős #271 Stanley sequences;
- Erdős #500 / Turán (3,4);
- Lonely Runner 13;
- Erdős #949;
- Erdős #1066;
- R(5,5) 41-vertex circulant structural program.

Additional programs promoted by the current topology pass are tracked in `PROGRAM-PROMOTIONS-ROUND2.md`.

## Saturation criterion

Release saturation is reached only when:

1. every known mathematical source family has an explicit disposition;
2. no high-density problem program is reachable only through a dump/mine path;
3. compact finished results have a reader-facing theorem/family home;
4. contradictions and corrections are linked to the claims they govern;
5. broad repositories clearly distinguish formal authority from research mirrors;
6. remaining quarantine is caused by a real IP/privacy/source boundary, not organizational neglect.

Until then, the governing rule is:

> **The archive may remember everything. It may not hide the mathematics.**
