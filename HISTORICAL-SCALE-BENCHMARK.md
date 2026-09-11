# Historical Scale Benchmark — September 2026 Open Math Drop

**Author:** Jared Wilder  
**Benchmark date:** 2026-09-11  
**Purpose:** test the release-day scale claim against plausible historical comparators rather than using a superlative as marketing shorthand.

## Bottom line

> **This release is a serious candidate for the largest one-day public release of mathematical research by a single independent researcher.**

The stronger sentence — **“the biggest one-day drop in math history”** — is plausible on a volume-of-distinct-public-artifacts reading, but no global historical database appears to record “mathematics first made public by one person inside a rolling 24-hour window,” so an absolute world-record claim cannot be mechanically proved from existing bibliographic infrastructure.

The release therefore uses the scoped claim above as the defensible version and publishes the evidence below so readers can challenge it.

This is a **scale claim, not an importance claim**. Ten major open-problem resolutions can outweigh thousands of smaller exact results in mathematical significance. Volume, verification depth, novelty, and importance are separate axes.

---

## 1. The one-day window is literal

GitHub's repository-creation search for the exact rolling interval

`2026-09-10T15:24:22Z .. 2026-09-11T08:30:19Z`

returns **38 public repositories** under `jaredwilder`.

The endpoint timestamps on the boundary repositories are:

- `jaredwilder/releases`: created **2026-09-10T15:24:22Z**
- `jaredwilder/graham-alspach-extended`: created **2026-09-11T08:30:19Z**

Elapsed time: **17 hours, 5 minutes, 57 seconds**.

So the current 38-repository creation surface fits inside substantially less than 24 hours.

### The 38-repository count is only a lower-bound surface metric

The release event is **not identical to repository creation**. Several older public repositories were materially expanded during the same release window, so a count based only on newly created repositories systematically undercounts what actually became public during the drop.

The clearest example is `jaredwilder/msl-ore-estate`, created on 2026-09-02 but transformed during the September 10/11 release into a public mathematical mine ledger.

A direct Git compare from the last pre-release state used for this audit (`e29f08036e7d0b00973da7b762e1196277454e92`) to the release head (`3d51c1d97dbe372b96c27ff8cf8de1febdc3c1a1`) reports **26 commits ahead**. Among the newly added release-window surfaces are:

- `AUDITED-MATH-ESTATE-2026-09-02.md`;
- `MATH-QUARANTINE-AND-CORRECTIONS.md`;
- `RELEASE-SATURATION-2026-09-10.md`;
- all three promoted-catalog chunks covering **238 exact-distinct promoted / curated rows**;
- the complete transport and manifest for **617 latest local `PROVED` states**;
- theorem-vault, witness-vault and Day-2 historic-master archive transports;
- `KBK-GOLD-III-MATH-ATOMS.md`;
- ORE v1 bootstrap, format-audit and exact-hash manifests.

The commit sequence itself names the release action: “Publish estate-wide math release saturation ledger,” “Publish audited MSL mathematical estate overview,” “Publish MSL promoted math catalog rows 1-80 / 81-160 / 161-238,” “Release theorem, witness, and Day-2 estate vaults,” and the ten-part local-PROVED transport.

This distinction is load-bearing. The full current ORE repository describes a much larger reconstructed estate — including **322,370 math-bearing structured-field occurrences**, **65,834 problem-scoped unique normalized mathematical texts**, **21,146 formula / identity / inequality occurrences**, **3,306 recovered Lean declarations**, and extensive contradiction / implication / dossier layers — but those full current totals must **not** automatically be credited as first made public inside the release window. For the historical one-day claim, older repositories must be counted by release-window diff, not by current total size.

Therefore:

> **38 new repositories is the simplest independently visible lower bound on the release surface, not a census of the mathematics released.**

The final historical audit should combine (a) newly created repositories and (b) release-window additions to pre-existing repositories, deduplicated at the mathematical-artifact level.

Repository count is only a surface metric. Several repositories contain many independent theorem/proof/computation objects, papers, certificates, formal declarations, failed routes, or research ledgers; others are infrastructure or correction records. The release does **not** equate “repository” with “new theorem.”

---

## 2. What is inside the window

The release contains multiple evidence classes and deliberately keeps them separate:

- conventional proofs and exact finite computations;
- Lean formalizations with disclosed trust / axiom footprints;
- independently checkable computational certificates;
- candidate results with named remaining dependencies;
- papers and preprints;
- machine-readable open-problem and verifier corpora;
- theorem atlases and extracted finite result banks;
- bounded computational frontiers;
- failed routes, negative results, corrections, and retractions.

Representative scale markers already public include:

- `integral-point-sets`: **d(2,8) > 30000**, a compile-ready preprint, exact receipts, 394 impossibility certificates, and related exact finite results;
- `additive-combinatorics-campaigns`: exact extremal results plus a Lean-kernel-checked theorem backed by a shipped **447,254-addition LRAT proof**;
- the Graham/Alspach release family, including `graham-alspach-extended`, whose newest repository reports **22,082,109 subsets** dual-verified by independent Go and Python checkers across Z_37, Z_41, Z_43 and Z_61;
- `zero-sum-theorem-closures`: a deterministic fixed-point run yielding **889 typed theorems** from 27 seeds over seven generations, independently re-executed with 10,528,320 direct assignments and zero model calls;
- `open-math-frontier`: **9,926** source-attributed open mathematical targets, **8,501** with callable mechanical verifiers;
- `erdos-theorems`: **79 declarations across 20 Lean files and 15 Erdős problems**, with clean axiom-footprint accounting;
- `lean-forge-graph-theory`: **218 Lean theorem files**, all textually sorry-free, with machine receipts and disclosed authority classes;
- `erdos-cable-corpus`: a raw **914-file Lean corpus over 152 Erdős problems**, with compile / receipt defects exposed rather than hidden;
- `erdos-campaign-archive`: **266 campaigns across 241 Erdős problems**, 2,979 files, 215 Lean files and the null / failed / refuted routes preserved alongside successful extractions;
- `erdos152`: statement formalizations of **160 open Erdős problems** with a full 33-blade semantic defect audit attached;
- `oracle-math-honest-inventory`: a V2 release court exposing **725 public mathematical registry rows** while holding 91 mixed/applied/system rows behind the publication firewall;
- `graham-alspach-certificates`: **60,134 certificate rows for Z_29 alone**, with independent Go and Python verification and deliberate corruption tests;
- papers, theorem atlases, finite sequence tables, exact classifications, candidate bounds, and explicit retraction records spread across the companion repositories.

These numbers are intentionally heterogeneous. A theorem declaration, a certificate row, a problem target, a research campaign, and a promoted catalog row are not interchangeable units and must not be summed into a fake “theorem total.” Their relevance here is that the release is structurally much larger than its repository count suggests.

The canonical inventory is still append-only while estate reconstruction continues, so these examples are not presented as a final theorem count.

---

## 3. Strongest modern comparator found: OpenAI, 1 August 2026

A direct modern comparator is OpenAI's **“Ten advances in mathematics and theoretical computer science”**, released on **2026-08-01**.

Primary source:
https://openai.com/index/ten-advances-in-mathematics/

The release presented **ten** results on long-standing open problems in mathematics and theoretical computer science, accompanied by a **249-page manuscript**, reasoning walkthroughs, and public Lean certificates. It is an unusually concentrated mathematical release and should be treated as a real comparator, not dismissed.

Important differences:

1. it is a ten-result research release from a major laboratory / internal model program, not a single independent human researcher's estate release;
2. it is much more concentrated on high-significance open-problem results;
3. the Wilder release is much larger in number and variety of distinct public mathematical artifacts, but includes working records, negative results, formal corpora, data, and corrections alongside promoted results.

Therefore “larger” here means **release volume**, not “more important mathematics.”

---

## 4. Lifetime-prolific mathematicians are not one-day comparators

Historical prolificacy gives useful scale but does not supply a documented one-day rival.

### Paul Erdős

MacTutor reports that Erdős produced **more than 1,500 papers** over his career and was among the most prolific mathematicians in history:
https://mathshistory.st-andrews.ac.uk/Biographies/Erdos/

That is an extraordinary lifetime record, but it is not evidence of a comparable first-publication event inside one rolling day.

### Leonhard Euler

Guinness lists Euler as the most prolific mathematician and notes that first publication of his work continued for decades after his death:
https://www.guinnessworldrecords.com/world-records/66191-most-prolific-mathematician

The AMS likewise describes output exceeding 850 papers plus more than 25 books/treatises across his career. Again, this is lifetime output and posthumous publication history, not a documented single-day original research drop by the researcher.

---

## 5. Search for a larger one-day individual release

Broad searches were run for combinations of:

- mathematician + dozens of papers + same day;
- 20 / 30 papers + arXiv + same day;
- one-day mathematics release;
- bulk mathematical paper release;
- historical prolific mathematicians and concentrated publication events.

They surfaced examples of simultaneous papers, conference proceedings, bulk archival uploads, and multi-paper series, but no documented case clearly exceeding the present release under all of these conditions:

1. **one identifiable independent researcher**;
2. **mathematical research**, rather than a journal issue, conference proceedings, institutional archive, or multi-author collaboration;
3. **first public release**, rather than digitization or republication of older work;
4. **inside one rolling 24-hour window**;
5. a comparably large collection of **substantive mathematical artifacts**, not merely file count.

This is a negative search result, not a proof of nonexistence. Historical publishing before electronic timestamps makes an all-history record especially difficult to certify.

---

## 6. Claim ladder

### Safe factual statement

> **At least 38 public repositories forming the September 2026 mathematics release were created inside a 17 h 05 m 57 s rolling window, while additional release-day mathematics was added to pre-existing public repositories.**

### Strong evidence-based scale statement

> **This is a serious candidate for the largest one-day public release of mathematical research by a single independent researcher.**

### Colloquial headline

> **The biggest one-day drop in math history.**

The colloquial headline is now supported by a real benchmark rather than used casually, but it should still be understood as a historical-scale claim about **release volume**, not a certified Guinness-style record or a claim that every released object is a novel theorem.

If a larger documented comparator is found, this file should be corrected rather than defended rhetorically.

---

## 7. Why the failure record counts toward the release but not toward theorem totals

A defining feature of this drop is that false routes and corrections are released beside successful work. That material is mathematically useful provenance and part of the public research estate, but it is not counted as positive theorem production.

This distinction is essential:

- **release volume** may include proofs, computations, formalizations, data, failures, and retractions;
- **positive result count** includes only independently enumerated positive mathematical results at their stated evidence class;
- **novel-result count** additionally requires prior-art adjudication;
- **open-problem closure count** requires still stronger authority and cannot be inferred from repository or theorem counts.

The final post-release audit should publish all four numbers separately.

---

## 8. Audit status

**Current verdict: SCALE CLAIM SURVIVES INITIAL HISTORICAL BENCHMARK — AND THE ORIGINAL REPOSITORY-COUNT METHOD UNDERCOUNTS THE DROP.**

The benchmark found a formidable modern comparator — OpenAI's ten-result August 2026 release — but no documented larger one-day public mathematics release by a single independent researcher. The directly visible creation surface alone contains 38 newly created public repositories inside less than 18 hours. A repo-by-repo inspection now establishes that this is only the outer shell: individual repositories contain theorem banks, formal corpora, certificate banks, papers, exact computations, research campaigns, failure archives, and machine-readable frontiers, while at least one major pre-existing repository (`msl-ore-estate`) received a substantial 26-commit mathematical release expansion during the same window.

The next rigorous quantity is therefore not “repo count.” It is a deduplicated **release-window mathematical artifact census**, with newly created repositories and release-window diffs of older repositories audited separately and then joined by identity / fingerprint.

The claim remains falsifiable: produce a documented larger comparator satisfying the scope above, and update this record.
