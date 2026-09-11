# Publication Boundary — Open Mathematics vs. Unpublished Applied Work

**Author:** Jared Wilder  
**Public release date:** 2026-09-10

This repository and its companion mathematics repositories are an **open release of mathematical research**. They are not a blanket publication of every algorithm, implementation, product mechanism, biomedical method, control system, patent claim, trade secret, or commercial application in the broader research estate.

## Material intended to be public

When committed to the named public mathematics repositories, the following kinds of material are intended for public release:

- theorem statements and proofs;
- Lean source together with disclosed axiom and verification information;
- exact finite computations and reproducibility scripts whose mathematical scope is stated explicitly;
- counterexamples, failed approaches, retractions, and correction records;
- problem statements, literature references, open-problem metadata, and structured problem datasets;
- general methods for checking proofs, computations, and formalizations;
- pure combinatorial, number-theoretic, graph-theoretic, geometric, and formal mathematics expressly included in a public repository.

## Related applications are not automatically public

Publishing an abstract theorem or algorithm does **not** automatically publish every application or implementation that uses it.

In particular, this mathematics release does not intentionally disclose unpublished details of:

- patient-specific diagnosis, monitoring, prognosis, treatment, triage, or physiological-control systems;
- clinical or physiological applications of network, instability, perturbation, coupling, longitudinal, or related mathematical ideas beyond material already deliberately made public in its own record;
- pharmacology or digital-twin product implementations, calibration systems, regulator-facing methods, clinical datasets, or patient-level inference machinery;
- energy, grid, battery, industrial, optimization, game-engine, simulation, or other applied implementations whose technical details may have commercial or intellectual-property significance;
- private source corpora, credentials, infrastructure, deployment details, unpublished source code, or business logic;
- pending patent language, continuation strategy, unpublished embodiments, or material reserved for possible future filings.

Only material actually committed to a public repository is part of this release.

## Practical publication rule

A mention in a README, research log, issue, memory file, or cross-reference is **not** permission to publish the contents of a private repository or unpublished archive.

Use the following rule when deciding whether to extract material:

1. **Pure theorem, proof, or mathematical code?** Publish after checking correctness and the stated scope.
2. **General proof or verification infrastructure?** Publish when it does not expose private data, credentials, or application-specific implementation details.
3. **Applied mechanism with possible product or patent significance?** Do not publish without explicit clearance.
4. **Mixed mathematical/applied source?** Extract the standalone mathematics and keep the application-specific implementation private.
5. **Uncertain boundary?** Do not publish yet. Mathematical material can be released later; an accidental public disclosure cannot meaningfully be made private again simply by deleting a commit.

## What this policy does and does not say

This document does not assert that any unpublished idea is patentable, secret, commercially valuable, or legally protectable. It is only a publication-scope policy.

It also does not change the license or public status of material already intentionally released under an open license.

Its purpose is simply to prevent “release the mathematics” from being interpreted as “publish every application and implementation in the broader research archive.”

## Accidental disclosure

If application-specific or patent-sensitive material is accidentally committed, preserve an accurate correction record and obtain appropriate legal advice. Removing a Git commit should not be represented as undoing a public disclosure.

For the public mathematics map, see [`MATH-DROP-2026-09-10.md`](MATH-DROP-2026-09-10.md). For the public writing standard, see [`HUMAN-FIRST-EDITORIAL-STANDARD.md`](HUMAN-FIRST-EDITORIAL-STANDARD.md).