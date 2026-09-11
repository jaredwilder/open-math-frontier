# open-math-frontier

**9,926 open mathematical problems in machine-readable form, with 8,501 of them carrying a
callable mechanical verifier.**

Author: Jared Wilder. First public timestamp: 2026-09-10.

## September 10, 2026 release map

For the public map of the broader mathematics drop, claim classes, strongest results, curated
repos, raw corpora, retractions, and suggested reading order, start here:

- [`MATH-DROP-2026-09-10.md`](MATH-DROP-2026-09-10.md)
- [`PUBLICATION-FIREWALL.md`](PUBLICATION-FIREWALL.md) — explicit boundary between this open
  mathematics release and unpublished applied / patent-facing IP.

The release doctrine is simple: theorem, candidate, finite computation, working record, and
retraction are different classes and remain visibly different in public.

## `frontier/open-frontier.jsonl`

One JSON object per line. Each carries a target id, family, parameters, the statement or a link to
it, the openness marking **with its source**, prize money where any exists, whether the problem is
already formalized in Lean, OEIS cross-references, a verifier field, and an explicit claim ceiling.

| | count |
|---|---|
| targets | **9,926** |
| with a callable mechanical verifier | **8,501** |
| already formalized in Lean | 307 |
| carrying prize money | 51 |

### By source

| source | targets |
|---|---|
| La Jolla Covering Repository | 7,419 |
| google-deepmind/formal-conjectures | 1,020 |
| erdosproblems.com community database (teorth/erdosproblems) | 607 |
| Wikipedia, list of unsolved problems in mathematics | 598 |
| OEIS keyword:hard | 220 |
| Radziszowski, Small Ramsey Numbers DS1.17 | 52 |
| Brouwer binary code tables | 10 |

## The rule that makes this usable

**Openness is the source's marking, never the author's.** A target is listed as open because a
maintained database says it is open, with that database named in the row. Nothing here is called
open because an attempt failed. Every row carries its own claim ceiling stating what a result
against that target would and would not establish.

The La Jolla entries are every covering number the repository does not mark as proven optimal.
The Ramsey entries are coordinate-parsed from the published survey, and only where the lower and
upper bounds differ. The binary codes are only the rows where lower is strictly less than upper.

## Other files

- `frontier/closed-frontier.jsonl` - targets that are closed, kept so the open set can be diffed
  against it rather than trusted.
- `frontier/formal-corpus.jsonl` (54 MB) - the formal statement corpus.
- `frontier/published-bounds.json` - published bounds cross-checked against targets.
- `frontier/erdos-statements.json`, `erdos-enriched.json`, `erdos-next-targets.json`,
  `erdos-uncovered-worklist.json` - the Erdos slice with tags, prizes and Lean status.
- `frontier/lean-attackability-audit.json` - which formalized targets a prover can actually attack.
- `frontier/implication-graph.json` - implications between targets.
- `ledgers/` - witnesses, transfer certificates, equivalences and leads produced against this
  frontier.

## Known limitation, stated by the tooling that built this

A target is a pinned instance plus an enumerator plus a verifier plus a claim ceiling. A row that
is only a title is not attackable, and the Wikipedia family in particular is largely titles with
no mechanical verifier. That is why the verifier count, 8,501, is reported separately from the
target count and is the number that actually matters.

## License

Apache-2.0.
