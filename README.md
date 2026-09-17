# Open Math Frontier

**9,926 open mathematical problems in structured form, with executable checkers for 8,501 targets.**

The collection combines published open-problem lists, formal conjecture corpora, exact finite tables, and machine-checkable target definitions into one searchable dataset.

## Collection

| | count |
|---|---:|
| indexed open targets | **9,926** |
| targets with an executable checker | **8,501** |
| targets already formalized in Lean | **307** |
| targets carrying prize money | **51** |

### Main sources

| source | targets |
|---|---:|
| La Jolla Covering Repository | 7,419 |
| `google-deepmind/formal-conjectures` | 1,020 |
| Erdős Problems community database | 607 |
| Wikipedia unsolved-problems list | 598 |
| OEIS keyword `hard` | 220 |
| Radziszowski, *Small Ramsey Numbers* DS1.17 | 52 |
| Brouwer binary-code tables | 10 |

## Data format

[`frontier/open-frontier.jsonl`](frontier/open-frontier.jsonl) contains one JSON object per target. Depending on the source, a row can include:

- problem identifier and mathematical family;
- exact statement or source link;
- source recording the problem as open;
- parameters and published bounds;
- prize information;
- Lean formalization status;
- OEIS cross-references;
- an executable checker;
- a scope field stating exactly what a successful computation establishes.

Related files include:

- [`frontier/closed-frontier.jsonl`](frontier/closed-frontier.jsonl) — closed targets for comparison;
- `frontier/formal-corpus.jsonl` — formal problem statements;
- `frontier/published-bounds.json` — published bound data;
- `frontier/erdos-statements.json` and related files — the Erdős subset;
- `frontier/implication-graph.json` — recorded implications between targets;
- `ledgers/` — witnesses, equivalences, transfer certificates, and research leads.

## Interpretation

A target is listed as open because its cited source marks it open. Local experiments do not determine that status.

Likewise, a checker proves only the finite or formal statement it encodes. A bounded search is not treated as a universal theorem; the `scope` field records that distinction explicitly.

For covering numbers, entries are included where the source does not mark the value proven optimal. Ramsey entries are included when published lower and upper bounds differ. Binary-code entries are included when the published lower bound is strictly below the upper bound.

## Start here

- [`START-HERE.md`](START-HERE.md) — selected mathematics and a short reading path.
- [`erdos-release-index`](https://github.com/jaredwilder/erdos-release-index) — problem-by-problem map of the public Erdős work.
- [`HUMAN-FIRST-EDITORIAL-STANDARD.md`](HUMAN-FIRST-EDITORIAL-STANDARD.md) — editorial conventions used for public mathematical writeups.

## License

Apache-2.0.

Author: Jared Wilder.
