# Novelty Hunter

**Author:** Jared Wilder  
**Canonical state date:** 2026-09-14 — Sweep 5  
**Mission:** continuously mine the public mathematical estate at `github.com/jaredwilder` for the strongest defensible novelty, publishable theorem packages, exact classifications, and buried headline results.

## Why this exists

The estate is too large and too live for any single chat context, repository README, or one-pass audit. Results have repeatedly been found *after* earlier sweeps appeared complete, and new releases have landed while the novelty hunt itself was running.

The governing rules are:

> **Prior art locates the delta. It does not erase the contribution.**

> **A result loses novelty, not mathematical existence.**

A sweep asks what is actually proved, what part is Jared Wilder's contribution, what the true mathematical scope is, what evidence makes it publishable, and only then how literature positions the result.

## Canonical files

- [`CANONICAL_LEDGER.md`](CANONICAL_LEDGER.md) — cumulative GitHub-native novelty/headline ledger. **Update this file rather than spawning pass ledgers.**
- [`BOARD.md`](BOARD.md) — current publication / closure / novelty-court queue.
- [`STATE.json`](STATE.json) — machine-readable checkpoint.
- [`CONTINUATION_PROTOCOL.md`](CONTINUATION_PROTOCOL.md) — zero-context recovery instructions.
- [`CROSS_SESSION_MERGE_2026-09-14.md`](CROSS_SESSION_MERGE_2026-09-14.md) — imported authority state from the separate Round-40 forensic session.

## Mandatory live-delta rule

Every future sweep must inspect **commits newer than the last Novelty Hunter checkpoint** before declaring the board stable. Sweep 5 proved why: the #681 theorem, new #251/#727/#1212/#289 child results, the CH exact-boundary proof chain, and the full #595 CI replay all appeared in the live estate after earlier summaries existed.

Source authority also outranks ledger metadata. If a findings row says “theorem” but its cited paper says “schema,” the paper controls.

## Current top line

The estate currently contains multiple serious publication objects, led by:

1. **Erdős #902:** candidate `f(4) >= 49`, pending catalogue-completeness certification.
2. **Integral point sets:** `ḋ(2,8) > 30000`.
3. **Erdős #681:** kernel-certified bad integer `999,997,304,512`, forcing any eventual threshold above it.
4. **Graham–Alspach:** complete `Z_37` and `Z_41`, with 838+ billion subsets covered across the expanded frontier.
5. **Erdős–Straus:** complete AP/GP denominator classifications.
6. **Caccetta–Häggkvist:** cubic directed-`C4` exact-boundary theorem; full human proof chain public, independent replay still desired.
7. **Signed sparse encoding:** `W(m,s)=Theta_s(m^s)`.
8. **Erdős #949:** arbitrary-sum-free full finite-sums theorem package.
9. **Erdős #595:** continuum barrier, now with fresh CI replay of all 27 sealed Lean theorem files.
10. **SQS(20):** residual completion / rigidity / trade suite.
11. **#890↔#1093:** deficiency/excess cross-problem bridge.
12. **Erdős #738:** sharp `floor(n^2/2)` type-support obstruction + parity extremizer.
13. **Turán / covering design #500:** plateau rigidity + excitation/frustration + integrality-gap calculus.
14. **Fiber coherence:** exact K4-free realization of arbitrary binary relations/CSPs, pending specialist prior-art court.
15. **#486:** summable forbidden-mass density theorem.

The exact-classification shelf also includes finite-field suites and the newly promoted `[50]` product-free / nontrivial-GP-free theorem (`max=35`, exactly 240 maximizers).

That list is **not assumed exhaustive**. Explicit state: `SATURATION = false`.

## Current authority / integrity

Current GitHub blob SHA for the canonical ledger:

```text
a0aae59856bcd77e2014b7f158d48a63045272f7
```

Current board blob SHA:

```text
c6ad35d1544f7e6adabc428490c41ff698999662
```

The older chat-local ledgers remain provenance only; GitHub-native state controls ongoing work.
