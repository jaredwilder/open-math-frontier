# Mathematics recovered from broad repositories

Five coherent research programs now have populated, problem-specific public
homes. They previously lived inside the campaign archive or the combined
computational-search repository. Across the five promotions, **973 research
files** were preserved and their public Git blob IDs checked against the
original source commits.

This is a discoverability and routing audit. It does not rank novelty or
upgrade the mathematical status of a source claim.

## New focused homes

| Problem | Previously buried in | Research files | Preferred home |
|---|---|---:|---|
| #850: radical coincidences | `erdos-computational-searches/erdos850` | 23 | [erdos850-radical-coincidences](https://github.com/jaredwilder/erdos850-radical-coincidences) |
| #273: prime-minus-one covering systems | `erdos-computational-searches/erdos273` | 916 | [erdos273-covering-systems](https://github.com/jaredwilder/erdos273-covering-systems) |
| #20: sunflower lemmas and constructions | `erdos-campaign-archive/campaigns/erdos20-close-2026-09-05` | 15 | [erdos20-sunflower](https://github.com/jaredwilder/erdos20-sunflower) |
| #592: ordinal Ramsey framework | `erdos-campaign-archive/campaigns/erdos592-close-2026-09-05` | 8 | [erdos592-ordinal-ramsey](https://github.com/jaredwilder/erdos592-ordinal-ramsey) |
| #593: obligatory hypergraphs | `erdos-campaign-archive/campaigns/erdos593-close-2026-09-05` | 11 | [erdos593-obligatory-hypergraphs](https://github.com/jaredwilder/erdos593-obligatory-hypergraphs) |

Each home has a mathematical introduction, a file-by-file reading map,
explicit evidence boundaries, source license, an immutable source manifest,
and a runnable source-integrity check. GitHub descriptions and mathematical
topics were set. The original archives now link directly to the new homes.

The promoted objects are research programs: #850 has search implementations,
independent controls, a structural lemma, Lean examples and a finite frontier;
#273 has a reduction, multiple search methods, receipts and corrections;
the three formal packages have linked theorem files, audit logs and explicit
unresolved obligations. The file counts describe their provenance footprint,
not the number or importance of their mathematical results.

## What was checked for this promotion

- All 973 research-file Git blobs in the new public repositories match the
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

## Remaining coherent candidates identified

These source packages still warrant a focused routing pass. They are linked
here immediately so a reader need not rediscover them in a dump.

| Program | Current source | Size of the identified package | Routing candidate |
|---|---|---:|---|
| #39: Sidon density formalization and computation | [campaign](https://github.com/jaredwilder/erdos-campaign-archive/tree/2f4c8e421137c53fd5d8414cabb3f543a3a12f55/campaigns/erdos39-close-2026-09-05) | 4 files, 46,947 bytes | Focused #39 home, incorporating the related additive-combinatorics note |
| #74: bounded-defect coloring formalization | [campaign](https://github.com/jaredwilder/erdos-campaign-archive/tree/2f4c8e421137c53fd5d8414cabb3f543a3a12f55/campaigns/erdos74-close-2026-09-05) | 4 files, 29,822 bytes | Focused #74 home or a compact theorem-bank entry with a direct reading map |
| #564: hypergraph Ramsey reduction work | [proof-chain package](https://github.com/jaredwilder/additive-combinatorics-campaigns/tree/b8d712e9bdc05388ac841fd52791ea61f4ed0289/erdos564-expedition) | 7 files, 87,236 bytes | Focused #564 home after reading the accepted reductions and retractions together |
| Twin-prime analytic reductions | [source corpus](https://github.com/jaredwilder/combinatorial-records/tree/2dbb2f38399e2c0ae6979cde28e03503f4a6c04c/twin-primes) | 7 files, 1,015,916 bytes | Focused conditional-reduction program after checking its claim and correction records |

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
