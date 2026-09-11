# Publication Firewall — Open Mathematics vs. Applied IP

**Author:** Jared Wilder  
**Public release date:** 2026-09-10

This repository and the companion mathematics repositories are an **open mathematical release**.
They do not constitute a blanket release of every mathematical idea, algorithm, implementation,
product mechanism, biomedical method, control system, patent claim, trade secret, or commercial
application in the author's broader research estate.

## Public by default in this math drop

The following classes are intended to be public when they appear in the named repositories:

- theorem statements and proofs explicitly committed to public math repositories;
- Lean source and disclosed axiom/verification receipts;
- finite exact computations and reproducibility scripts committed with a stated claim ceiling;
- counterexamples, failed routes, retractions, and correction records;
- problem statements, literature references, open-target metadata, and machine-readable frontiers;
- general-purpose proof-audit and semantic-certification methodology released here;
- pure combinatorial, number-theoretic, graph-theoretic, geometric, and formal methods whose public
  repository expressly contains the method itself.

## Not released merely because related mathematics is public

Public disclosure of an abstract mathematical object does **not** by itself disclose or authorize
publication of any unpublished implementation or application that uses it. In particular, this
math drop does not intentionally publish unpublished details of:

- patient-specific diagnosis, monitoring, prognosis, treatment, triage, or physiological-control
  systems;
- organ-network, instability, perturbation, coupling, route/shape/memory, or longitudinal clinical
  embodiments beyond material already deliberately made public in their own dedicated record;
- pharmacology / digital-twin product machinery, calibration pipelines, regulator-facing methods,
  clinical datasets, or patient-level inference systems;
- energy, grid, battery, industrial, optimization, game-engine, simulation, or other applied
  product embodiments where the implementation is commercially load-bearing;
- private source corpora, credentials, infrastructure, deployment details, unpublished source code,
  or business logic;
- pending patent claim language, continuation strategy, unpublished embodiments, or material being
  held for patent-family expansion.

If a mathematical theorem here has an applied embodiment elsewhere, only the files actually
committed to the public repository are part of this release.

## Repository boundary rule

A public repository is authoritative for what was intentionally released. A mention in a README,
research log, memory file, issue, or cross-reference is **not** an instruction to dump the contents
of a private repository or unpublished archive.

The release process should therefore obey:

1. **Pure theorem/proof/code asset?** Presumptively publishable after correctness/claim review.
2. **General proof infrastructure?** Publishable when it does not expose private data, credentials,
   or a commercially load-bearing applied pipeline.
3. **Applied mechanism with plausible patent/product value?** HOLD unless it already has an
   intentional public disclosure record or is separately cleared.
4. **Mixed artifact?** Extract and publish the standalone mathematical theorem or method; retain the
   application-specific embodiment privately.
5. **Uncertain boundary?** HOLD. A missed math upload can be published later; an accidental enabling
   disclosure cannot be made private again in the meaningful publication sense.

## No implied claims

Nothing in this firewall asserts that any retained idea is patentable, secret, commercially
valuable, or legally protectable. It is a publication-scope rule only.

Nothing in this document changes the licenses attached to files already released. Nothing here
creates a restriction on mathematical material that was intentionally published under an open
license. The purpose is simply to prevent the phrase "release the math estate" from being mistaken
for "publish every application in the broader research estate."

## Corrections

If an applied-IP detail is accidentally committed, preserve the correction record and seek
appropriate legal advice about consequences; deleting a Git commit should not be represented as
undoing a public disclosure.

For the mathematical claim taxonomy and the public release map, see `MATH-DROP-2026-09-10.md`.
