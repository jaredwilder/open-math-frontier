# Abstract Evidence-Selection and Certified-DAG Theorems

**Author:** Jared Wilder  
**Public release:** 2026-09-10

Standalone mathematics extracted from the VVC program. The VVC product architecture, implementation invariants, query compiler, storage layout, freshness machinery and system-specific epistemic claims remain outside this abstract packet.

## 1. Typed Closure Fixed-Point Theorem
For a finite graph over a declared relation language R, monotone closure that repeatedly adds obligation-relevant reachable nodes terminates in at most |V| node additions and yields the least fixed point reachable under those rules. This certifies closure relative to the declared relation system, not arbitrary semantics.

## 2. Incidence Compression Theorem
If each of N objects participates in at most r typed features, an exact shared-feature relation can have Θ(N²) logical pairwise edges while its bipartite object-feature incidence representation stores at most rN incidence edges.

## 3. Unrestricted Semantic Dependency Lower Bound
With an unrestricted relevance predicate R(q,x), exact certification that all relevant items have been discovered requires Ω(N) worst-case inspection; arbitrary undisclosed pairwise relations can expose Θ(N²) possibilities.

## 4. Dynamic Theoremization Epoch Bound
If source changes partition a lemma’s life into validity epochs and the same rent/buy policy is applied independently per epoch, summing the per-epoch bound preserves the same factor against an epoch-respecting offline optimum.

## 5. Virtual Relation Theorem
For relations generated from bounded feature incidence, pairwise neighborhoods may be materialized on demand from the incidence structure; the logical graph may be quadratic while physical relation metadata remains O(rN).

## 6. Certified Knowledge Monotonicity Theorem
If valid certified lemma set L is expanded to L'⊇L, and old proof frontiers remain admissible, then W(q;L') ≤ W(q;L). More valid certified knowledge cannot worsen the minimum achievable certified frontier cost.

## 7. Inclusion-Minimal Packet Certificate
Repeatedly deleting any evidence item whose removal preserves sufficiency terminates at an inclusion-minimal packet: no remaining individual item can be removed without violating the constraints.

## 8. Minimum Sufficient Evidence Packet (MSEP) NP-Hardness
Weighted Set Cover reduces directly to selecting the minimum-cost evidence packet whose coverage satisfies every obligation.

## 9. Irreducible Global Query Lower Bound
If an exact query can change when any arbitrary unread item changes and no sufficient statistic was maintained, any exact worst-case algorithm must inspect all N items: Ω(N) access.

## 10. Context Distance / Deletion Robustness
If δ(P) is the minimum number of evidence deletions that makes packet P insufficient, then δ(P)≥r guarantees survival of all deletions of fewer than r evidence units.

## 11. Ambiguity-Union Theorem
If the intended parse p* survives in parse set P, then Ω(p*) ⊆ ⋃_{p∈P} Ω(p).

## 12. Local-to-Global Soundness of a Certified DAG
In a finite acyclic proof DAG, if every root is valid and every local inference checker is sound and accepts its edge, every reachable terminal claim is valid.

## Scope boundary

Only the abstract graph/optimization statements are released here. VVC-specific system claims, storage/indexing mechanics, freshness implementation, parsing architecture and other potentially product-facing details remain outside the automatic math release.