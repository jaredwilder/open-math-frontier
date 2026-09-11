# open-math-frontier

**9,926 open mathematical problems in machine-readable form, with 8,501 of them carrying a callable mechanical verifier.**

Author: Jared Wilder. First public timestamp: 2026-09-10.

## September 2026 mathematics release

For the broader public mathematics release, **start with the results-first front door**:

- [`START-HERE.md`](START-HERE.md) — strongest mathematics, evidence classes, ORE scale, formal layer, and audit layer;
- [`MATH-DROP-2026-09-10.md`](MATH-DROP-2026-09-10.md) — the larger append-only estate map;
- [`HISTORICAL-SCALE-BENCHMARK.md`](HISTORICAL-SCALE-BENCHMARK.md) — the falsifiable historical-scale comparison;
- [`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md) — the boundary between the open mathematics release and unpublished applied / patent-facing IP.

The release doctrine is simple: **the theorem statement says what was established, the evidence class says how strongly, and the audit record says what failed.** The classes remain separate rather than one being used to rhetorically substitute for another.

## `frontier/open-frontier.jsonl`

One JSON object per line. Each carries a target id, family, parameters, the statement or a link to it, the openness marking **with its source**, prize money where any exists, whether the problem is already formalized in Lean, OEIS cross-references, a verifier field, and an explicit claim ceiling.

| | count |
|---|---:|
| targets | **9,926** |
| with a callable mechanical verifier | **8,501** |
| already formalized in Lean | 307 |
| carrying prize money | 51 |

### By source

| source | targets |
|---|---:|
| La Jolla Covering Repository | 7,419 |
| google-deepmind/formal-conjectures | 1,020 |
| erdosproblems.com community database (teorth/erdosproblems) | 607 |
| Wikipedia, list of unsolved problems in mathematics | 598 |
| OEIS keyword:hard | 220 |
| Radziszowski, Small Ramsey Numbers DS1.17 | 52 |
| Brouwer binary code tables | 10 |

## The rule that makes this usable

**Openness is the source's marking, never the author's.** A target is listed as open because a maintained database says it is open, with that database named in the row. Nothing here is called open because an attempt failed. Every row carries its own claim ceiling stating what a result against that target establishes.

The La Jolla entries are covering numbers the repository does not mark as proven optimal. The Ramsey entries are coordinate-parsed from the published survey only where lower and upper bounds differ. The binary-code entries are rows where the lower bound is strictly below the upper bound.

## Other files

- `frontier/closed-frontier.jsonl` — closed targets, retained so the open set can be diffed against a frozen complement;
- `frontier/formal-corpus.jsonl` (54 MB) — the formal statement corpus;
- `frontier/published-bounds.json` — published bounds cross-checked against targets;
- `frontier/erdos-statements.json`, `erdos-enriched.json`, `erdos-next-targets.json`, `erdos-uncovered-worklist.json` — the Erdős slice with tags, prizes and Lean status;
- `frontier/lean-attackability-audit.json` — which formalized targets expose a callable prover-facing surface;
- `frontier/implication-graph.json` — implications between targets;
- `ledgers/` — witnesses, transfer certificates, equivalences and leads produced against the frontier.

## Attackability boundary

A target is most useful to a machine when it has a pinned instance, an enumerator, a verifier and a claim ceiling. A title-only row is still useful as indexed problem data but is not mechanically attackable in the same sense. That is why the release reports **8,501 callable verifiers separately from 9,926 total targets** rather than collapsing those quantities.

## License

Apache-2.0.