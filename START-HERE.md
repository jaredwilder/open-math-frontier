# Start here — Jared Wilder's public mathematics

This page is the shortest route into the mathematical work published across the `jaredwilder` GitHub account.

You do not need to understand the research workflow, archive history, or internal project names to read the results. Start with a theorem, computation, construction, or formal proof that interests you; the provenance material is there when you need it.

## Five good first reads

### Integral point sets: `d(2,8) > 30000`

[`integral-point-sets`](https://github.com/jaredwilder/integral-point-sets) proves

\[
\boxed{d(2,8)>30000}
\]

for planar integral point sets in general position. The argument combines the uniqueness of the small-diameter Kreisel–Kurz heptagon with an exact maximality computation showing that it cannot be extended by another integral-distance point. The repository includes a paper draft, exact arithmetic, and reproducibility material.

### Erdős #902: tournament domination

[`erdos902`](https://github.com/jaredwilder/erdos902) is the most substantial Lean-centered problem repository in the release. It contains a formal proof of the classical sandwich

\[
(n+2)2^{n-1}-1\le f(n)\le n+3n^2 2^n,
\]

exact small values, the finite window `48≤f(4)≤67`, order-49 Cayley eliminations, and detailed structure for the order-23 doubly regular tournaments appearing at the `f(4)` boundary.

### Erdős–Straus progression denominators

[`erdos-straus-progressions`](https://github.com/jaredwilder/erdos-straus-progressions) gives complete if-and-only-if parametrizations for Erdős–Straus solutions whose denominators form either an arithmetic progression or a geometric progression. This is a compact repository with explicit formulas and direct finite verification.

### Additive combinatorics and exact finite structure

[`additive-combinatorics-campaigns`](https://github.com/jaredwilder/additive-combinatorics-campaigns) contains several independent results, including the minimum span of a 13-element `C3`-free set, classification through span 63, a minimum-span result for eight-element `C5`-free sets, positional/carry constructions, and a Lean theorem backed by a shipped LRAT proof.

### Triangle-cover number and fiber coherence

For graph structure and CSP connections, start with [`triangle-cover-number`](https://github.com/jaredwilder/triangle-cover-number), [`erdos595-barrier-tower`](https://github.com/jaredwilder/erdos595-barrier-tower), and [`fiber-coherence-cycle-rank`](https://github.com/jaredwilder/fiber-coherence-cycle-rank). Together they contain the continuum threshold for countable triangle-free covers, K4-free structural results, exact relation gadgets, and an NP-completeness theorem for finite fiber coherence.

## If you want formal mathematics

- [`erdos902`](https://github.com/jaredwilder/erdos902) — tournament theory and exact finite structure in Lean.
- [`erdos-theorems`](https://github.com/jaredwilder/erdos-theorems) — a compact bank of 79 kernel-clean declarations across 15 Erdős problems.
- [`lean-contributions`](https://github.com/jaredwilder/lean-contributions) — a 1,473-line Steiner triple-system/Kirkman development, the #1066 formalization, and standalone formal results.
- [`erdos595-barrier-tower`](https://github.com/jaredwilder/erdos595-barrier-tower) — 27 sorry-free Lean files around triangle-cover number and cardinal thresholds.
- [`erdos152`](https://github.com/jaredwilder/erdos152) — 160 formalized Erdős problem statements, useful as a source-to-Lean corpus rather than a proof collection.

For formalization quality and source fidelity, see [`lean-semantic-blades`](https://github.com/jaredwilder/lean-semantic-blades) and [`formalizer-kernel-audit`](https://github.com/jaredwilder/formalizer-kernel-audit).

## If you want exact computation

- [`graham-alspach-sequenceability`](https://github.com/jaredwilder/graham-alspach-sequenceability), [`graham-alspach-certificates`](https://github.com/jaredwilder/graham-alspach-certificates), and [`graham-alspach-extended`](https://github.com/jaredwilder/graham-alspach-extended) — explicit sequenceability certificates with independent checking.
- [`finite-field-extremal-sets`](https://github.com/jaredwilder/finite-field-extremal-sets) — complete small-prime finite-field classifications.
- [`covering-13-6-3`](https://github.com/jaredwilder/covering-13-6-3) — exact structural reduction of the unresolved `C(13,6,3)` case.
- [`binary-sidon-f7`](https://github.com/jaredwilder/binary-sidon-f7) — the interval `24≤f(7)≤30`, explicit witnesses, and a calibrated exact-search frontier.
- [`erdos930-consecutive-block-square`](https://github.com/jaredwilder/erdos930-consecutive-block-square) — explicit square/cube block products, Pell families, and the lower-threshold obstruction `k≥5` for `r=2`.

A good computational repository here states the finite universe, gives the witness or certificate, explains the exhaustive method, and provides a command that another reader can run.

## If you want open-problem structure

These repositories do not need the parent conjecture to be solved in order to contain useful mathematics:

- [`erdos-gyarfas-power-of-two-cycles`](https://github.com/jaredwilder/erdos-gyarfas-power-of-two-cycles) — cubic-surplus identities, bounded defect kernels, quotient cycle doubling, and two eliminated ratio branches.
- [`caccetta-haggkvist-triangles`](https://github.com/jaredwilder/caccetta-haggkvist-triangles) — exact-boundary identities and a directed-4-cycle lower-bound route.
- [`p6-erdos-hajnal`](https://github.com/jaredwilder/p6-erdos-hajnal) — a complete-bipartite-minus-disjoint-rectangles normal form, trace bound, pure-pair theorem, and crown quotient.
- [`lonely-runner-13`](https://github.com/jaredwilder/lonely-runner-13) — a large-prime residue-class theorem with an exact 8192-mask parity classification.
- [`diagonal-ramsey-corridor`](https://github.com/jaredwilder/diagonal-ramsey-corridor) — thin-corridor equivalence, a conditional supermultiplicativity route, and explicit construction barriers.

## If you want compact proved lemmas

[`erdos-proved-lemmas`](https://github.com/jaredwilder/erdos-proved-lemmas) collects finished child theorems that do not yet need a full subject repository. It is usually the best place to look for a single theorem associated with an otherwise much larger Erdős problem.

[`erdos-release-index`](https://github.com/jaredwilder/erdos-release-index) is the broader problem-by-problem navigation map.

## The open-problem dataset

This repository, [`open-math-frontier`](https://github.com/jaredwilder/open-math-frontier), contains **9,926 source-attributed open mathematical targets**, with **8,501 executable finite or mechanical checkers**. The dataset combines covering-design tables, formal-conjecture corpora, Erdős problems, Ramsey data, coding tables, OEIS references, and other sources.

The checker attached to a row should be read at its declared scope: a finite checker establishes a finite statement, not an unbounded theorem.

## Archives and provenance

The public estate also contains research archives, source-recovery repositories, failed routes, and correction records. They are useful for reproducibility and historical reconstruction, but they are not the recommended first contact with the mathematics.

Examples include:

- [`erdos-campaign-archive`](https://github.com/jaredwilder/erdos-campaign-archive) — full proof-search runs, including failures and null results;
- [`nested-archive-mathematics`](https://github.com/jaredwilder/nested-archive-mathematics) — mathematics recovered from archives inside archives;
- [`divergent-mirror-mathematics`](https://github.com/jaredwilder/divergent-mirror-mathematics) — mathematics recovered from a divergent source mirror;
- [`erdos-counterexample-queue`](https://github.com/jaredwilder/erdos-counterexample-queue) — counterexamples and corrections recovered from research transcripts;
- historical retraction repositories where a specific earlier claim requires a correction record.

When a subject has a focused repository, cite and read the focused repository rather than the archive copy.

## How the public writeups are meant to read

The editorial rule is simple:

> **State the mathematical object. State the main result. Explain why it matters. Then give the proof or computation and a reproducible way to check it.**

Proof status, literature priority, corrections, and provenance are important, but they should clarify a theorem rather than bury it.

The detailed standard is [`HUMAN-FIRST-EDITORIAL-STANDARD.md`](HUMAN-FIRST-EDITORIAL-STANDARD.md). The full machine-readable map is [`MATH-DROP-2026-09-10.md`](MATH-DROP-2026-09-10.md).

## Applied-work boundary

This public mathematics release is intentionally separate from biomedical, industrial, product, proprietary, and patent-facing work. See [`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md) before extracting material from mixed research sources.

Author: Jared Wilder.