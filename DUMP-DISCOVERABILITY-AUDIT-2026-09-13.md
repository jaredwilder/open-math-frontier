# Mathematics recovered from broad repositories

Ten coherent research programs now have populated, problem-specific public
homes. Their sources previously lived inside mixed public archives
and mathematical release ZIPs. Across the ten promotions, **1,017 research
files** were preserved and their public Git blob IDs checked against the
original source commits or exact ZIP members.

This is a discoverability and routing audit. It does not rank novelty or
upgrade the mathematical status of a source claim.

## Round 13 routing reconciliation — current status

The supplied canonical ledger/report through Round 13 classify **zero active P0 publication gaps** in their reviewed queue. This is a scoped publication classification, not a percentage of all archived mathematics or a proof/novelty claim.

The [main release index](https://github.com/jaredwilder/erdos-release-index#focused-subject-homes) now links all **18 reported missing focused homes**, including #77's existing `diagonal-ramsey-corridor`. The same live check found and linked **10 additional existing homes**. All 28 destinations were public and populated; these were navigation repairs, not 28 newly discovered publication packages.

The named reader/correction queue was handled as follows:

- **#251 / #1212:** direct routes to the already public [dyadic-prefix denominator statement](https://github.com/jaredwilder/erdos-findings-ledger/blob/main/theorems/ERDOS-251-DYADIC-PREFIX-DENOMINATOR.md) and [fixed-row run identity](https://github.com/jaredwilder/erdos-findings-ledger/blob/main/theorems/ERDOS-1212-ROW-RUN-COORDINATE.md); companion theorem-bank pages now distinguish the indexing conventions and separate local statements.
- **#477:** a [complete all-quadratic written proof](https://github.com/jaredwilder/erdos-proved-lemmas/blob/master/erdos477-all-quadratics.md), prepared for this release using the reflection identity. This resolves the reader's missing proof exposition. It is not a recovered historical source artifact or a kernel check beyond the existing square case.
- **#289 / #486:** direct links to the [all-prime written obstruction](https://github.com/jaredwilder/erdos-proved-lemmas/blob/master/erdos289-padic-reciprocal-obstructions.md) and [quantitative density theorem](https://github.com/jaredwilder/erdos-proved-lemmas/blob/master/erdos486-summable-forbidden-mass.md). The #289 parity statement now explicitly requires positive global 2-adic level; the proof-authority map separates its written and narrower formal components.
- **#949:** the [complement-cardinality child](https://github.com/jaredwilder/erdos949-finite-sums/blob/main/human/complement-cardinality.md) now has a complete written proof. Its exact historical Lean declaration/receipt remains unlocated, so no kernel-check claim is made for this child. The original finite-sums writeup and Lean bytes are preserved.
- **Archived corrections:** [Q-031 through Q-035](https://github.com/jaredwilder/msl-ore-estate/blob/main/MATH-QUARANTINE-AND-CORRECTIONS.md#round-7-corrections-surfaced-on-2026-09-13) surface #260/#562/#383/#1054/#889 using exact campaign/route identifiers; Q-036 records the #289 hypothesis repair. Missing original scratchpad receipts are not represented as transported.

**Remaining exact transport:** `ERDOS1061_PRIMITIVE_SEEDS_200K.csv`, reported size 17,026,297 bytes and 152,803 data rows, expected SHA-256 `343b12fceb642d15b898f1a4bbbd9018b4a4301c0e72ac46ba30f559358e1a68`. The [existing #1061 home](https://github.com/jaredwilder/erdos1061-aliquot-square) awaits the actual recovered file; its report hash alone is not the payload. The source was described as recovered in Library but has not been located in the accessible files checked here.

Beyond those explicit provenance items, work proceeds by named frontier problem and frozen statement. The historical candidate sections below are leads from earlier passes, not a new undifferentiated publication denominator. See the [routing receipt](ROUND13-ROUTING-RECEIPT-2026-09-13.json) for the exact publication commits and checks.

## New focused homes

| Problem | Previously buried in | Research files | Preferred home |
|---|---|---:|---|
| #850: radical coincidences | `erdos-computational-searches/erdos850` | 23 | [erdos850-radical-coincidences](https://github.com/jaredwilder/erdos850-radical-coincidences) |
| #273: prime-minus-one covering systems | `erdos-computational-searches/erdos273` | 916 | [erdos273-covering-systems](https://github.com/jaredwilder/erdos273-covering-systems) |
| #20: sunflower lemmas and constructions | `erdos-campaign-archive/campaigns/erdos20-close-2026-09-05` | 15 | [erdos20-sunflower](https://github.com/jaredwilder/erdos20-sunflower) |
| #592: ordinal Ramsey framework | `erdos-campaign-archive/campaigns/erdos592-close-2026-09-05` | 8 | [erdos592-ordinal-ramsey](https://github.com/jaredwilder/erdos592-ordinal-ramsey) |
| #593: obligatory hypergraphs | `erdos-campaign-archive/campaigns/erdos593-close-2026-09-05` | 11 | [erdos593-obligatory-hypergraphs](https://github.com/jaredwilder/erdos593-obligatory-hypergraphs) |
| #146: degenerate Turán reductions | `erdos-campaign-archive/campaigns/erdos146-attack-2026-09-05` | 10 | [erdos146-degenerate-turan](https://github.com/jaredwilder/erdos146-degenerate-turan) |
| #1192: additive-basis representation energy | Campaign archive plus corrected findings-ledger note | 7 | [erdos1192-representation-energy](https://github.com/jaredwilder/erdos1192-representation-energy) |
| #39: Sidon density | `erdos-campaign-archive/campaigns/erdos39-close-2026-09-05` | 4 | [erdos39-sidon-density](https://github.com/jaredwilder/erdos39-sidon-density) |
| #74: bounded bipartite defect | `erdos-campaign-archive/campaigns/erdos74-close-2026-09-05` | 4 | [erdos74-bipartite-defect](https://github.com/jaredwilder/erdos74-bipartite-defect) |
| Finite-field extremal sets: F31, Z31, F73 | `combinatorial-records/finite-fields` and three MathFire ZIPs | 19 | [finite-field-extremal-sets](https://github.com/jaredwilder/finite-field-extremal-sets) |

Each home has a mathematical introduction, a file-by-file reading map,
explicit evidence boundaries, source license, an immutable source manifest,
and a runnable source-integrity check. GitHub descriptions and mathematical
topics were set. The original archives now link directly to the new homes.

The promoted objects are research programs: #850 has search implementations,
independent controls, a structural lemma, Lean examples and a finite frontier;
#273 has a reduction, multiple search methods, receipts and corrections;
the first batch's three formal packages have linked theorem files, audit logs and explicit
unresolved obligations. The file counts describe their provenance footprint,
not the number or importance of their mathematical results.

## What was checked for this promotion

- All 1,017 research-file Git blobs in the new public repositories match the
  pinned source snapshots. Each repository also supplies SHA-256 checks.
- The #850 small control was rerun through 30,000: seven two-term pairs,
  independently rechecked by trial division, and no three-term pair. Its
  historical 464,637,500,000 frontier was not rerun.
- The #273 parity identity and Selfridge one-half construction were rerun,
  including independent covering checks and the parity lift. This is not a
  two-half solution or a rerun of its large SAT searches.
- The six #20 Lean source hashes match the historical build receipt exactly.
  The three formal packages retain historical build evidence; no fresh Lean
  compilation was performed in this pass.
- The #592 literature verdicts and #593 literature hypotheses remain explicit.
  A formal conditional implication does not certify its mathematical inputs.

Source commits, destination commits and verified routing edits are recorded
in [the machine-readable publication receipt](DUMP-DISCOVERABILITY-RECEIPT-2026-09-13.json).

## Second pass: leads from the canonical estate ledger

The supplied canonical forensic report and workbook were used as leads,
then checked against current public source trees and repository contents.
The workbook's **Buried Headlines, row 14 (#146) and row 19 (#1192)** identified
two of the new homes. The attached files were read without modification.

This pass added **25 exact research files (1,050,156 bytes)** across four
populated repositories. Their READMEs lead with mathematics, distinguish
proved supporting results from unresolved targets, and map the source files.

- **#146:** 51 named historical axiom checks across three Lean files
  (26 + 11 + 14). The smaller 37 count omitted the third file. Minimum-degree
  extraction is present; greedy embedding and the final `r=1` assembly are
  not. The deliberately incomplete probe is visibly excluded from authority.
- **#1192:** six campaign artifacts are joined to the exact corrected proof
  note. The reader sees the `r·2^k` cutoff repair before the route history.
  These are elementary supporting inequalities, with no novelty claim and
  no general higher-order basis construction.
- **#39:** both Sidon criteria agree on 4,511 tested sets; a fresh bounded
  replay checks 40 standard-greedy terms, 30 formal-predicate terms and nine
  small prime constructions. The infinite density theorem is represented by
  historical Lean evidence, not established by this finite replay.
- **#74:** the finite-vertex guard, bounded-defect coloring theorem and
  `Set.ncard` counterexample are explained together. This formalizes a
  classical obstruction, without solving the prescribed growth-rate problem.

All destination research Git blobs match their original public trees.
The #39 and #74 source hashes also match the historical receipts. There was
no fresh Lean compilation. File integrity, historical proof checks and
mathematical novelty are separate claims.

The live reconciliation found the #738 bank, #595/fiber maps, RH Epoch 32
method-obstruction package and #902 reading surface already present. The
readable 617-row catalogue had also been repaired earlier. Those stale debts
did not generate duplicate repositories. The #1061 subject home exists, but
its named 152,803-row primitive-seed CSV remains an exact-source recovery gap;
its absence is not repaired by another README.

## Third pass: original certificates recovered from engine and design ZIPs

This pass recovered complete mathematical authority behind summaries that
were already public. It added **one focused home and one substantial source
recovery inside an existing home**, preserving 44 original research files.

### Three finite-field classifications in one home

[finite-field-extremal-sets](https://github.com/jaredwilder/finite-field-extremal-sets)
organizes three separate finite problems:

| Domain and constraints | Exact maximum | Number of maximizing sets |
|---|---:|---:|
| F31 nonzero residues, sum/product-free | 8 | 9 |
| Z31, sum-free and nontrivial-3-AP-free | 6 | 330, in 12 dilation orbits |
| F73 nonzero residues, sum/product/nontrivial-3-AP-free | 12 | 3 |

The 19 preserved research files combine eight original public records with
eleven exact mathematical members from three MathFire ZIPs. They include all
three original C/C++ verifiers and their historical outputs. The F31 final
packet and F73 development packet have different ZIP hashes and remain
separate theorem identities.

A fresh Python computation reproduces the complete maximizing layers and
checks historical witness/orbit lists. Six twelve-vertex control domains are
also exhaustively checked by direct equation evaluation (24,576 subsets).
[Successful CI](https://github.com/jaredwilder/finite-field-extremal-sets/actions/runs/34780653757)
compiled and ran all three original C/C++ verifiers. Recovered engine-release
provenance does not create a new historical novelty claim.

### SQS(20): the actual P15 and its checks are now public

The existing [#835 home](https://github.com/jaredwilder/erdos835-lean-audit#exact-source-package-and-fresh-replay)
now contains the 25-file `JSPACE-v0.7-ERDOS835-40R` source package, including
the exact fifteen systems and original verifier programs.

Fresh replay confirms all 15 GF(5) rank-849/nullity-6 rigidity systems, all
105 pair-trade profiles and the representative spectral-incidence identity.
An independent graph reconstruction exhibits all four residual K5s and
checks component sizes `250, 12×25, 4×5`, establishing that at least three
old constituents must change in any full large-set extension. Original
result JSON objects match the replay. This is a finite theorem about this
particular pack; the global problem and separate Lean dependencies remain.

### Leads that did not justify new repositories

- #564's seven JSON proof-chain records still need usable mathematical
  semantics and authority beyond route-status logs.
- The twin-prime package remains conditional on unproved Type I and Type II
  inputs; its existing archival subject directory already states that boundary.
- The broader #477 all-quadratic assertion was found in summaries and
  incomplete dossiers; the inspected complete Lean proof is square-only.
  The later Round 13 section above supplies a complete new written presentation;
  recovery of the exact historical broader formal artifact remains separate.
- A bounded next-source scan identified small formal number-theory leads
  for #479, #456 and #936. These need subject-bank comparison and proof review;
  their labels or source counts do not justify three more repositories.

## A large package connected to its existing subject home

`additive-combinatorics-campaigns/apex-c3-campaign` contains **821 files**
(222,931,844 bytes at the inspected source commit), including the APX-031
formal closure and chunked LRAT material, minimum-span searches and research
targets. The nine-file `ck-sequences` tree did not include or point to this
package before the audit.

The [C_k subject home](https://github.com/jaredwilder/ck-sequences#related-c3-proof-and-minimum-span-package)
now links directly to the overview, closure report and proof chunks at a
pinned source commit. The mixed additive archive links back. The large
source package remains in the archive; this change supplies subject-level
discovery without another competing C_k repository or a duplicate payload.

## Historical routing candidates from earlier passes

These earlier source leads are retained for reference. They are not active P0
publication debts in the Round 13 canonical queue above.

| Program | Current source | Size of the identified package | Routing candidate |
|---|---|---:|---|
| #564: hypergraph Ramsey reduction work | [proof-chain package](https://github.com/jaredwilder/additive-combinatorics-campaigns/tree/b8d712e9bdc05388ac841fd52791ea61f4ed0289/erdos564-expedition) | 7 files, 87,236 bytes | Focused #564 home after reading the accepted reductions and retractions together |
| Twin-prime analytic reductions | [source corpus](https://github.com/jaredwilder/combinatorial-records/tree/2dbb2f38399e2c0ae6979cde28e03503f4a6c04c/twin-primes) | 7 files, 1,015,916 bytes | Focused conditional-reduction program after checking its claim and correction records |

Earlier report-led source locations are retained here; use the current reader routes above:

- [#486 summable forbidden mass](https://github.com/jaredwilder/unpublished-math-papers/tree/main/erdos486-summable-forbidden-mass): a compact density theorem with the load-bearing activation rule `n<m`; an explicit corollary/dependency map is a better next step than a new dump.
- [#477 square-tiling kernel](https://github.com/jaredwilder/erdos-campaign-archive/tree/dad8bf3925ec7584a2e782b06e102e54587c2094/campaigns/erdos477-campaign-001): the report's broader all-quadratics claim still needs its own original proof surfaced; the inspected public Lean file proves the square slice.
- [#289 reciprocal obstruction campaign](https://github.com/jaredwilder/erdos-campaign-archive/tree/dad8bf3925ec7584a2e782b06e102e54587c2094/campaigns/erdos289-campaign-001): connect the all-prime written argument to the narrower formal and finite-search components without conflating their scopes.

## Apparent gaps that should not create duplicate repositories

The earlier large promotions already have populated homes: power-of-two
cycles, CH3, fiber coherence, the #890/#1093 bridge, P6 Erdős–Hajnal, #142,
#1061, #271, #500, Lonely Runner, #949, #1066 and the 41-vertex Ramsey
circulant. The DNA code and strongly regular graph packages also have homes.

Several recovery repositories contain only short report passages about small
lemmas or finite examples. Those belong in a compact subject bank until
substantial source material is recovered. Abstract encoding results already
have `positional-encoding-thresholds`; intentionally withheld applied machine
catalogues are not missing mathematical promotions.

The audit used current public repository names, directory trees, routing
documents and selected source files. It covered the principal campaign,
paper, computation and recovery collections at navigation level; it was not
a line-by-line mathematical review of every archived campaign.
