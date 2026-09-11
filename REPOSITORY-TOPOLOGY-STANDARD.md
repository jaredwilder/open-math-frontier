# Repository Topology Standard for the September 2026 Mathematics Release

**Author:** Jared Wilder  
**Purpose:** keep the public mathematics estate navigable as the release grows.

A public mathematics release should not force a reader to excavate one giant repository to find unrelated theorems, formalizations, papers, certificates, and active frontiers.

The organizing rule is:

> **An actively investigated mathematical problem should default toward its own public home once it has a coherent research surface.**

That threshold is deliberately generous. The failure we are guarding against is not “too many repositories”; it is **real mathematics becoming effectively invisible because it is buried inside a general dump**.

At the same time, one isolated lemma does not need a toy repository. The useful hierarchy is:

> **focused problem/subject repository > compact theorem bank > provenance/intake archive**

## 1. Focused problem or subject repository

Use a focused repository when a problem or body of mathematics has an identity a mathematician could reasonably follow as a program.

A dedicated repository is normally justified as soon as **any one** of these is present:

- multiple nontrivial results or lemmas forming a chain;
- a substantial formalization corpus;
- computation, certificates, witnesses, or exact search code specific to the problem;
- a live research frontier with explicit unresolved obligations;
- a meaningful correction/refutation history that belongs with the problem;
- a paper or multi-paper program;
- enough material that a citation should land somewhere built specifically for that mathematics.

The repository does **not** have to wait until the parent problem is solved. An honest open-problem research program is itself a coherent public object.

Examples in the current estate include:

- `erdos152` — 160 formalized Erdős problem statements;
- `erdos902` — tournament theory around Erdős #902;
- `integral-point-sets` — integral-point-set results and certificates;
- `erdos595-barrier-tower` — now the problem-level home for the formal continuum barrier **and** the recovered 65-card triangle-cover theorem bank;
- `erdos835-lean-audit` — despite the historical name, now the problem-level home for both the Johnson-graph Lean audit and the SQS(20) completion/rigidity program;
- the Graham–Alspach sequenceability repositories;
- the EG203/Kummer paper, finite-obstruction, and obstruction-calculus repositories.

## 2. Compact theorem bank

Use a theorem bank for finished child theorems that are substantial enough to publish but still genuinely small and self-contained.

`erdos-proved-lemmas` serves this role for compact Erdős results.

A theorem should graduate from the bank when it accumulates a program around it: more results, formal code, certificates, a substantial computation, a paper, or a live frontier. At that point the focused repository becomes the preferred home and the theorem bank becomes an index/summary layer.

## 3. Provenance / intake archive

Use a large archive to preserve extraction chronology, source packets, historical research notes, mixed theorem material, and objects awaiting classification.

Examples:

- `msl-ore-estate` — estate-wide research provenance;
- `unpublished-math-papers` — public pure-math intake/provenance archive after extraction.

An archive may keep a mirror after promotion, but it should not remain the only place to discover a mature problem program.

## 4. The anti-burial rule

When deciding between “leave it in the dump” and “give it a problem home,” bias toward the problem home when there is real substance.

A particularly strong trigger is **research density**: if a folder already contains dozens of theorem cards, multiple proof routes, a verifier, a certificate family, or several internally named subtheories, the organizational question is already settled. It is a research program.

Current examples discovered during the release sweep:

- Erdős #738: 62 proved-in-packet statements/schemas, 12 explicit targets, a 45,301-byte theorem bank, verifier and manifests;
- Erdős–Gyárfás power-of-two cycles: 202 theorem cards across ten coherent families, including proved results, computational certificates, negative theorems, refuted routes and explicit targets;
- Caccetta–Häggkvist directed triangles: a 23KB theorem ledger plus a terminal-defect package and a long exact-boundary structural program;
- Erdős #595: a 65-card triangle-cover theorem bank in addition to the formal barrier package;
- Erdős #835: a Lean proof-status program plus independent SQS(20) residual-coloring, rigidity and trade mathematics.

Those are not archive folders in any meaningful scholarly sense. They are programs that require problem-level homes.

## 5. Avoid duplicate canonical homes

The generous promotion threshold does **not** imply one new repository for every newly discovered folder.

If the same mathematical problem already has a substantial dedicated repository, enrich that repository instead of creating a rival canonical home.

This is why:

- the buried #595 theorem bank was promoted into `erdos595-barrier-tower` rather than starting a competing triangle-cover repository;
- the SQS(20) packet was promoted into the existing #835 repository rather than splitting #835 by evidence modality;
- recovered EG203 analytic papers are indexed from `eg203-kummer-papers` instead of creating another #203 silo.

Organize primarily by **mathematical problem/program**, secondarily by proof technology or historical session.

## 6. Formalization corpora deserve their own homes

A formalization corpus is itself a coherent research object even when many statements remain unproved.

For example, **160 formalized Erdős statements are a repository-scale object**. Their value is not determined by whether they are 160 finished proofs; the corpus has its own purpose, audit history, and source-fidelity questions.

Keep statement corpora, theorem banks, and semantic-audit tools conceptually separate.

## 7. Historical names can remain inside archives

Internal filenames such as `gold`, `court`, `attack`, `blade`, `shot`, `campaign`, `forge`, or `mine` may remain when changing them would damage provenance or links.

They should not determine the public repository identity. Human-facing README files translate historical process vocabulary into ordinary mathematical language.

## 8. Corrections stay local

A correction belongs beside the theorem, computation, or formalization it corrects.

Do not use one failed route as a reason to make an entire repository lead with failure. Conversely, do not hide a correction when it changes the statement readers would otherwise cite.

## 9. Archives should route, not hoard

When new mathematics first lands in an intake archive:

1. establish that the object is pure mathematics and safe to release;
2. identify its mathematical problem or subject;
3. check whether a focused public repository already exists;
4. if yes, route the result there and retain the archival copy as provenance;
5. if no and the object is genuinely small, route it to the appropriate theorem bank;
6. if no and the object already has a coherent research surface, put it on the dedicated-repository promotion queue immediately;
7. once the dedicated repository exists and is initialized, make it the preferred reading/citation surface and leave the archive as provenance.

## 10. Reader test

Before publishing or routing a substantial result, ask:

> **If a mathematician arrived from a citation to this result, would the repository they land in look like it was built for that mathematics?**

If the answer is no because they first encounter dozens of unrelated subjects, the result needs a better home.

A second test is equally useful:

> **Could a researcher follow the history, surviving results, evidence, corrections and next open step of this problem without understanding the rest of Jared Wilder's estate?**

If not, the problem is still too buried.
