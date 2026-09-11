# Complete Minimal-Failure Antichain Recovery

**Author:** Jared Wilder  
**Public release:** 2026-09-10

This file extracts one standalone finite-combinatorial theorem from the Frontier Alchemy representation archive without publishing the surrounding research-engine/product implementation.

## Theorem

Let a finite search world have a finite set of structurally legal partial assignments and an exact binary predicate saying whether a partial assignment fails the hidden constraint system.

Enumerate every structurally legal partial assignment, retain the failed assignments, and delete every failed assignment that strictly contains another failed assignment. The remaining family is exactly the inclusion-minimal failed-set antichain — equivalently, the exact hidden minimal no-good hypergraph.

### Proof

Because the legal search world is finite, every failed partial assignment contains an inclusion-minimal failed partial assignment. Exhaustive enumeration includes all of them. Removing nonminimal failed sets cannot remove a minimal failure and removes every failed set that is not minimal. The survivors are therefore exactly the minimal no-goods.

## Scope

This is a finite exhaustive-recovery theorem. It does not claim efficient complexity: the number of legal partial assignments may be exponential.

**Recovered source status:** `PROVED_IN_FROZEN_WORLD_CLASS` with proof metadata present.

## IP boundary

Only the abstract finite-set theorem is public here. No solver orchestration, product interface, action protocol, authenticated packet format, or proprietary implementation from the originating system is disclosed.
