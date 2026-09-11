# Repository Topology Standard for the September 2026 Mathematics Release

**Author:** Jared Wilder  
**Purpose:** keep the public mathematics estate navigable as the release grows.

A public mathematics release should not force a reader to excavate one giant repository to find unrelated theorems, formalizations, papers, and certificates.

The organizing rule is:

> **One coherent mathematical subject gets one coherent public home once it is large enough to stand on its own.**

Large archives remain valuable for provenance, but they are not substitutes for subject organization.

## 1. Three repository roles

### Focused subject repository

Use a focused repository when a body of mathematics has its own identity: a theorem family, substantial formalization corpus, paper program, certificate program, sustained open-problem investigation, or exact classification project.

This is the preferred reading and citation surface.

Examples in the current release include:

- `erdos152` — 160 formalized Erdős problem statements;
- `erdos902` — tournament theory around Erdős #902;
- `integral-point-sets` — integral-point-set results and certificates;
- `erdos595-barrier-tower` — the formal continuum coverability theorem;
- the Graham–Alspach sequenceability repositories;
- the EG203/Kummer paper and obstruction-calculus repositories.

### Compact theorem bank

Use a theorem bank for finished child theorems that are substantial enough to publish but too small to justify a repository by themselves.

`erdos-proved-lemmas` serves this role for compact Erdős results.

If a theorem later grows into a larger subject program, the focused subject repository becomes the preferred home. The theorem bank may keep a concise statement and link.

### Provenance / intake archive

Use a large archive to preserve extraction chronology, source packets, historical research notes, mixed theorem material, and objects awaiting classification.

Examples:

- `msl-ore-estate` — estate-wide research provenance;
- `unpublished-math-papers` — public pure-math intake/provenance archive after extraction.

An archive can keep a mirror after promotion, but it should not remain the only place to discover mature subject mathematics.

## 2. Promotion triggers

A subject should normally receive a focused repository when one or more of these conditions holds:

- it contains a substantial formalization corpus;
- it contains multiple nontrivial theorems forming a coherent program;
- it has papers, certificates, proofs, and/or independent verification layers of its own;
- it is independently citable or likely to be read without the rest of the estate;
- it has a substantial directory tree whose contents are mostly about one mathematical object;
- it has roughly dozens of formal/theorem records rather than one isolated note;
- a reader must currently navigate unrelated subject matter to understand it.

These are information-architecture triggers, not novelty claims.

## 3. Avoid duplicate canonical homes

Do not let two repositories both present themselves as the definitive version of the same result.

When a richer subject repository exists:

- the focused repository is the preferred home;
- theorem banks contain a compact statement and link;
- archives retain provenance and extraction chronology;
- release indices point to the focused repository.

This keeps corrections and future extensions from fragmenting across several competing copies.

## 4. Formalization corpora deserve their own homes

A formalization corpus is itself a coherent research object even when many statements remain unproved.

For example, **160 formalized Erdős statements are a repository-scale object**. Their value is not determined by whether they are 160 finished proofs; the corpus has its own purpose, audit history, and source-fidelity questions.

Keep statement corpora, theorem banks, and semantic-audit tools conceptually separate.

## 5. Historical names can remain inside archives

Internal filenames such as `gold`, `court`, `attack`, `blade`, `shot`, `campaign`, or `mine` may remain when changing them would damage provenance or links.

They should not determine the public repository identity. Human-facing README files translate historical process vocabulary into ordinary mathematical language.

## 6. Corrections stay local

A correction belongs beside the theorem, computation, or formalization it corrects.

Do not use one failed route as a reason to make an entire repository lead with failure. Conversely, do not hide a correction when it changes the statement readers would otherwise cite.

## 7. Archives should route, not hoard

When new mathematics first lands in an intake archive:

1. establish that the object is pure mathematics and safe to release;
2. identify its mathematical subject;
3. check whether a focused public repository already exists;
4. if yes, route the result there and leave an archival provenance copy;
5. if no and the object is small, route it to the appropriate theorem bank;
6. if no and the object is already a coherent program, mark it for a new dedicated repository rather than allowing the intake archive to become its permanent home.

## 8. Current standalone-repository queue

The live routing ledger in `jaredwilder/unpublished-math-papers/SUBJECT-ROUTING.md` currently identifies several strong candidates, including:

- Erdős #890 ↔ #1093 large-prime/deficiency program;
- the 184-entry Erdős #271 Stanley-sequence ledger;
- the 76-entry Erdős #500 / Turán (3,4) extraction;
- the 62-result Erdős #738 theorem bank;
- the 13-speed Lonely Runner program;
- the fiber-coherence / rank-three-kernel program;
- the 41-vertex circulant `R(5,5)` structural program;
- several sharp finite-field and product/GP-free classification projects.

The queue should evolve as the archive is mined.

## 9. Reader test

Before publishing a new repository or major subject folder, ask:

> **If a mathematician arrived from a citation to this result, would the repository they land in look like it was built for that mathematics?**

If the answer is no because they first encounter dozens of unrelated subjects, the result needs a better home.
