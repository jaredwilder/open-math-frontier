# Generalization Benchmark Mathematics Provenance — 2026-09-10

**Author:** Jared Wilder  
**Public release:** 2026-09-10

## What this is

The estate contains repeated `generalization-proof*.json` receipts for a very large mathematical benchmark suite. One recovered run contains exactly **3,098 cases**, all marked passed by the benchmark harness.

This is **not a claim of 3,098 new research theorems**.

The recovered top-level receipt stores, per case, fields such as:

- `problem_id`;
- `kind`;
- expected result class;
- actual result class;
- `passed`;
- `report_hash`.

In the recovered artifact inspected for this release, the actual theorem/problem statements are not embedded alongside those receipt rows. Therefore a hash and a `proved` token are not enough to turn each benchmark case into an independently reviewable mathematical publication.

This file preserves the benchmark's mathematical scope and census without inflating it into research output.

## Exact recovered run statistics

```text
total_cases = 3098
passed      = 3098
failed      = 0
receipt_sha256 = 345fa1dd6009f0c63d4cd798c38c4b54c798e4b67795c960f7c14db44f9f187a
```

### Result-class census

| result class | count |
|---|---:|
| classification | 2580 |
| proved | 200 |
| witness | 155 |
| formalization | 76 |
| plan | 64 |
| barrier | 10 |
| closure | 8 |
| not_found | 5 |

Again, these are **benchmark result labels**, not novelty or publication-authority classes.

## Mathematical-domain census

| kind | cases |
|---|---:|
| analytic_number_theory | 236 |
| category_theory | 140 |
| functional_analysis | 136 |
| differential_geometry | 120 |
| additive_combinatorics | 111 |
| number_theory | 100 |
| first_order_logic | 100 |
| arithmetic_geometry | 100 |
| lemma_synthesis | 96 |
| research_program | 96 |
| theory_genesis | 88 |
| decision_procedure | 88 |
| graph | 77 |
| combinatorial | 76 |
| formalization | 76 |
| algebraic_number | 72 |
| proof_kernel | 72 |
| matrix | 68 |
| geometry | 68 |
| probability | 68 |
| proof_search | 68 |
| algebraic_geometry | 64 |
| asymptotic | 64 |
| symbolic | 64 |
| exact_analysis | 64 |
| formal_library | 64 |
| permutation_group | 64 |
| representation_theory | 60 |
| homological_algebra | 48 |
| polynomial | 44 |
| lattice | 44 |
| polynomial_diophantine | 40 |
| coding_theory | 32 |
| group_action | 32 |
| inequality | 32 |
| logic_table | 32 |
| matroid | 32 |
| semidefinite | 28 |
| finite_field | 28 |
| pde | 28 |
| linear_optimization | 24 |
| topology | 24 |
| weighted_graph | 20 |
| spectral_graph | 20 |
| boolean_cnf | 12 |
| design | 12 |
| poset | 12 |
| hadamard | 11 |
| linear_diophantine | 10 |
| sequence | 10 |
| transition_system | 10 |
| set_cover | 8 |
| finite_predicate | 5 |

## Representative case identities

The suite contains named calibration families such as:

- modular obstruction cases `mod-obstruction-0` through `mod-obstruction-11`;
- explicit modular witnesses `mod-witness-*`;
- linear Diophantine classification cases `linear-0` through `linear-9`;
- polynomial and recurrence-sequence cases `poly-seq-*`, `rec-seq-*`;
- transition-system barriers/witnesses `transition-block-*`, `transition-path-*`;
- graph clique cases `graph-cliques-*`;
- SAT/UNSAT fixture pairs `sat-*`, `unsat-*`;
- integer-root existence/nonexistence cases;
- path-independence-number cases `path-alpha-4` through `path-alpha-11`;
- odd-cycle coloring cases;
- complete-graph coloring cases;
- set-cover cases `set-cover-3` through `set-cover-8`;
- and a much broader collection across analysis, algebra, geometry, number theory, logic, optimization and formalization.

## Authority boundary

A repeated benchmark receipt is useful evidence about a mathematical reasoning system. It is not automatically a theorem archive.

For an individual benchmark item to be promoted into the public research theorem estate, the release process still requires at least:

1. the exact mathematical statement;
2. its proof/certificate or authoritative formal receipt;
3. semantic agreement between the statement and the claimed result;
4. source/novelty context if it is being presented as research rather than textbook calibration.

Until then, this suite belongs in the **calibration mathematics** layer.

## Why publish it at all

The user asked for the mathematical estate, not merely novel headline results. A 3,098-case cross-domain benchmark is part of that estate and should be visible. The correct treatment is to preserve its scale, domain composition, result classes and receipt identity without pretending that repeated successful benchmark execution equals 3,098 independent discoveries.
