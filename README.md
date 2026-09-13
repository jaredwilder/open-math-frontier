# Open Math Frontier

**9,926 open mathematical problems collected in structured form, with executable checkers for 8,501 of them.**

Author: Jared Wilder. First public timestamp: 2026-09-10.

## September 2026 mathematics release

For the broader public mathematics release, start with:

- [`START-HERE.md`](START-HERE.md) — strongest mathematics and a short reading path;
- [`MATH-DROP-2026-09-10.md`](MATH-DROP-2026-09-10.md) — the larger append-only release map;
- [`HISTORICAL-SCALE-BENCHMARK.md`](HISTORICAL-SCALE-BENCHMARK.md) — the historical release-scale comparison;
- [`HUMAN-FIRST-EDITORIAL-STANDARD.md`](HUMAN-FIRST-EDITORIAL-STANDARD.md) — public writing standard: mathematics first, evidence second, internal workflow jargon kept out of the front door;
- [`REPOSITORY-TOPOLOGY-STANDARD.md`](REPOSITORY-TOPOLOGY-STANDARD.md) — subject organization standard: focused repository > compact theorem bank > provenance archive;
- [`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md) — the boundary between public mathematics and unpublished applied / patent-facing work.

Throughout the release, the mathematical statement comes first. Verification method, scope, prior-art status, and correction history are recorded separately. Coherent mathematical subjects should also have coherent public homes rather than accumulating indefinitely in a general archive.

## The open-problem index

`frontier/open-frontier.jsonl` contains one JSON object per target. A row may include:

- problem identifier and mathematical family;
- parameters and statement, or a source link;
- the public source marking the problem open;
- prize information where applicable;
- Lean formalization status;
- OEIS cross-references;
- an executable checker where one exists;
- a scope field describing exactly what a successful computation would establish.

| | count |
|---|---:|
| indexed targets | **9,926** |
| targets with an executable checker | **8,501** |
| already formalized in Lean | 307 |
| carrying prize money | 51 |

### Sources

| source | targets |
|---|---:|
| La Jolla Covering Repository | 7,419 |
| google-deepmind/formal-conjectures | 1,020 |
| erdosproblems.com community database (`teorth/erdosproblems`) | 607 |
| Wikipedia list of unsolved problems in mathematics | 598 |
| OEIS keyword `hard` | 220 |
| Radziszowski, *Small Ramsey Numbers* DS1.17 | 52 |
| Brouwer binary-code tables | 10 |

## How open status is assigned

A target is listed as open because its cited source marks it open. The repository does not infer openness from whether a local attempt succeeded or failed.

Likewise, an executable checker establishes only the finite or formal statement encoded by that checker. Each row records its scope so a bounded computation cannot silently become a universal theorem.

The La Jolla entries are covering numbers not marked proven optimal by that repository. Ramsey entries are included where the published lower and upper bounds differ. Binary-code entries are included where the lower bound is strictly below the upper bound.

## Other files

- `frontier/closed-frontier.jsonl` — closed targets, retained so the open set can be compared against them;
- `frontier/formal-corpus.jsonl` (54 MB) — formal problem statements;
- `frontier/published-bounds.json` — published bounds cross-checked against targets;
- `frontier/erdos-statements.json`, `erdos-enriched.json`, `erdos-next-targets.json`, `erdos-uncovered-worklist.json` — the Erdős subset with tags, prizes and Lean status;
- `frontier/lean-attackability-audit.json` — historical filename for the audit of which formalized targets have an executable proof/test interface;
- `frontier/implication-graph.json` — recorded implications between targets;
- `ledgers/` — witnesses, transfer certificates, equivalences, and research leads.

## Executable-check boundary

Not every indexed problem is mechanically testable. A title-only record is still useful as problem data, but it cannot be run through a finite checker. The **8,501** figure counts targets with an executable checking procedure; **9,926** is the total indexed open-problem collection.

Keeping those figures separate makes the dataset easier to interpret.

## License

Apache-2.0.

## Exact source publication — 2026-09-13

The [published batch receipt](PUBLICATION-BATCH-01-2026-09-13.md) links five updated mathematical repositories, recovered tables and source packets, finite replay results, and hash-verified public commits. The [live release-debt ledger](LIVE-ESTATE-RELEASE-DEBT-2026-09-13.md) marks the corresponding table and transport debts resolved.
