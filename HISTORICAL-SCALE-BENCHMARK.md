# Historical Scale Benchmark — September 2026 Open Math Drop

**Author:** Jared Wilder  
**Benchmark date:** 2026-09-11  
**Purpose:** compare the scale of this release with plausible historical precedents.

## Bottom line

> **This release is a serious candidate for the largest one-day public release of mathematical research by a single independent researcher.**

The stronger phrase — **“the biggest one-day drop in math history”** — is plausible if “biggest” means the volume of distinct mathematical research made public in one concentrated event. It cannot currently be certified as an absolute world record because there is no historical database indexing exactly this category: mathematics first made public by one independent researcher inside a rolling 24-hour window.

The claim is therefore stated as a serious, falsifiable candidate rather than a certified record.

This is a **scale claim, not an importance claim**. Mathematical significance, novelty, depth, verification strength, and release volume are different questions.

---

## 1. The one-day condition is literal

A GitHub creation-time search over

```text
2026-09-10T15:24:22Z .. 2026-09-11T08:30:19Z
```

finds **38 public repositories** under `jaredwilder`.

Boundary timestamps:

- `jaredwilder/releases`: created **2026-09-10T15:24:22Z**
- `jaredwilder/graham-alspach-extended`: created **2026-09-11T08:30:19Z**

Elapsed time: **17 hours, 5 minutes, 57 seconds**.

That proves that the initial new-repository wave fits comfortably inside a rolling 24-hour window.

### Why 38 repositories is only a lower bound on the release

The release was not limited to newly created repositories. Several older public repositories received substantial new mathematical material during the same period.

The clearest example is `jaredwilder/msl-ore-estate`, created on 2026-09-02 but expanded heavily during September 10/11. A direct comparison from the last pre-release state used in this audit (`e29f08036e7d0b00973da7b762e1196277454e92`) to the release head (`3d51c1d97dbe372b96c27ff8cf8de1febdc3c1a1`) shows **26 new commits**.

Those commits added, among other things:

- `AUDITED-MATH-ESTATE-2026-09-02.md`;
- `MATH-QUARANTINE-AND-CORRECTIONS.md`;
- `RELEASE-SATURATION-2026-09-10.md`;
- the **238-entry curated mathematical catalog**;
- the historical transport of **617 latest workflow records labelled `PROVED`**;
- theorem and witness archives;
- additional mathematical extraction and provenance files.

The current ORE repository is much larger still, with **322,370 math-bearing recovered fields**, **65,834 problem-scoped distinct normalized mathematical texts**, **21,146 formula/identity/inequality occurrences**, and **3,306 recovered Lean declarations**. Those present-day totals should not all be credited automatically to the one-day release; for older repositories, only the material actually added during the release window belongs in a strict historical census.

So:

> **38 newly created repositories is a simple, independently visible lower bound on the release event, not a count of the mathematics released.**

A rigorous final census should combine newly created repositories with the actual September 10/11 additions to older repositories, while deduplicating the same mathematical result when it appears in multiple forms.

---

## 2. What kind of material was released

The release contains many different mathematical object types:

- conventional proofs;
- exact finite classifications and computations;
- Lean formalizations;
- independently checkable computational certificates;
- candidate results with named unresolved dependencies;
- papers and preprints;
- open-problem datasets;
- theorem banks and extracted lemma collections;
- bounded computational frontiers;
- counterexamples, failed approaches, corrections, and retractions.

Representative public scale markers include:

- `integral-point-sets`: **`d(2,8) > 30000`**, a compile-ready preprint, exact receipts, 394 impossibility certificates, and related exact finite results;
- `additive-combinatorics-campaigns`: exact extremal results plus a Lean theorem backed by a **447,254-addition LRAT proof**;
- the Graham–Alspach release family, including `graham-alspach-extended`, which verifies **22,082,109 subsets** across `Z_37`, `Z_41`, `Z_43`, and `Z_61` with independent Go and Python implementations;
- `zero-sum-theorem-closures`: a finite derivation system reaching a fixed point at **889 typed theorems** from 27 seeds, with **10,528,320 direct assignments** independently replayed;
- `open-math-frontier`: **9,926** source-attributed open mathematical targets, **8,501** with executable checkers;
- `erdos-theorems`: **79 Lean declarations across 20 files and 15 Erdős problems**, with clean axiom-footprint accounting;
- `lean-forge-graph-theory`: **218 sorry-free Lean theorem files** with 217 verification receipts;
- `erdos-cable-corpus`: **914 Lean files across 152 Erdős problems**, with compile and axiom status audited file by file;
- `erdos-campaign-archive`: **266 automated proof-search runs across 241 Erdős problems**, 2,979 files and 215 Lean files, preserving successes, refutations, dead ends, and null results;
- `erdos152`: **160 Lean formalizations of open Erdős problem statements** with a semantic audit;
- `oracle-math-honest-inventory`: **725 public mathematical records** with evidence level attached to each;
- `graham-alspach-certificates`: **60,134 certificate rows for `Z_29` alone**, independently checked in Go and Python.

These are deliberately heterogeneous units. A theorem, certificate row, problem target, Lean file, research run, and archival record are not interchangeable and should not be added together into a synthetic theorem total.

Their relevance here is different: they show that the release is substantially larger than a count of repositories suggests.

---

## 3. Strongest modern comparator found: OpenAI, 1 August 2026

A direct modern comparator is OpenAI's **“Ten advances in mathematics and theoretical computer science”**, released on **2026-08-01**.

Primary source:  
https://openai.com/index/ten-advances-in-mathematics/

That release presented **ten results** on long-standing open problems in mathematics and theoretical computer science, together with a **249-page manuscript**, reasoning walkthroughs, and public Lean certificates. It is a serious comparator and should not be minimized.

The two releases differ substantially:

1. OpenAI's release came from a major research laboratory/model program rather than one independent researcher;
2. its ten results are far more concentrated around major open-problem advances;
3. the Wilder release is much broader in number and type of public mathematical objects, including theorem banks, finite classifications, formal corpora, papers, research archives, failed approaches, and corrections.

So “larger” in this benchmark means **release volume**, not “more important mathematics.”

---

## 4. Lifetime prolificacy is a different comparison

### Paul Erdős

MacTutor reports that Erdős produced **more than 1,500 papers** over his career:
https://mathshistory.st-andrews.ac.uk/Biographies/Erdos/

That is an extraordinary lifetime record, but it is not evidence of a comparable first-publication event inside one rolling day.

### Leonhard Euler

Guinness lists Euler as the most prolific mathematician and notes that first publication of his work continued for decades after his death:
https://www.guinnessworldrecords.com/world-records/66191-most-prolific-mathematician

The AMS likewise describes an output exceeding 850 papers plus more than 25 books and treatises. Again, that is lifetime output and posthumous publication history, not a documented single-day original research release by the researcher.

---

## 5. Search for a larger one-day individual release

Broad searches were run for combinations of:

- mathematician + dozens of papers + same day;
- 20 / 30 papers + arXiv + same day;
- one-day mathematics release;
- bulk mathematical paper release;
- historically prolific mathematicians and concentrated publication events.

The searches surfaced simultaneous papers, conference proceedings, bulk archival uploads, and multi-paper series, but no documented example clearly exceeding this release under all of the following conditions:

1. **one identifiable independent researcher**;
2. **mathematical research**, rather than a journal issue, conference proceedings, institutional archive, or multi-author collaboration;
3. **first public release**, rather than later digitization or republication;
4. **inside one rolling 24-hour window**;
5. a comparably large set of **substantive mathematical research objects**, not merely a large file count.

This is a negative search result, not a proof that no such precedent exists. Historical publishing before electronic timestamps makes an all-history comparison especially difficult.

---

## 6. Claim ladder

### Directly checkable statement

> **At least 38 public repositories belonging to the September 2026 mathematics release were created inside a 17 h 05 m 57 s rolling window, while additional release-day mathematics was added to older public repositories.**

### Historical-scale statement

> **This is a serious candidate for the largest one-day public release of mathematical research by a single independent researcher.**

### Colloquial headline

> **The biggest one-day drop in math history.**

The headline should be understood as a statement about **release volume**, not a Guinness-certified record and not a claim that every released object is historically novel or mathematically more important than every comparator.

If a larger documented precedent is found, this benchmark should be updated.

---

## 7. Positive results and research history should be counted separately

A defining feature of this release is that counterexamples, failed approaches, and corrections are public alongside successful mathematics.

Those materials are part of the **release volume** because they are substantive research records. They are not part of a positive theorem count.

A rigorous final accounting should therefore report separate totals for:

- overall public research material released;
- positive mathematical results;
- results whose historical novelty has been checked;
- open-problem closures, where any are claimed;
- formal proofs / certificates / exact computations as distinct verification categories.

That separation is more informative than one inflated aggregate number.

---

## 8. Current assessment

**The historical scale claim survives the initial comparison, and the original repository-count method clearly undercounts the release.**

The benchmark found a formidable modern comparator in OpenAI's August 2026 ten-result release, but no documented larger one-day public mathematics release by a single independent researcher.

The 38 newly created public repositories are only the outer shell. Direct inspection shows theorem banks, formal corpora, certificate banks, papers, exact computations, research archives, and substantial September 10/11 additions to older repositories such as `msl-ore-estate`.

The next rigorous quantity is therefore a **deduplicated census of mathematical material actually made public during the release window**, distinguishing new repositories from new material added to older repositories and identifying the same result when it appears as prose, code, Lean, certificate, and subject-repository extraction.

The claim remains falsifiable: produce a documented larger comparator satisfying the criteria above, and this record should be revised.