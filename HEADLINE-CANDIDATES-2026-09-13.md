# Headline mathematics: external-review shortlist

**Author:** Jared Wilder. Selection dated 2026-09-13.

These are prominent mathematical results from the portion of the estate reviewed so far. This is a working shortlist, not a claim that the entire estate has been ranked. Selection emphasizes an exact mathematical statement, substantial scope, and accessible evidence. Historical novelty is left for external review; existing corrections and proof boundaries remain attached.

## 1. A cubic four-cycle barrier for hypothetical CH3 counterexamples

Let D be a finite oriented graph on n=3d vertices, with every vertex of outdegree d and no directed triangle. Then the number of directed four-cycles, counted up to cyclic rotation, satisfies

`C4(D) >= ceil(3d^3/2)`.

**Why it stands out:** a strong quantitative constraint on the exact boundary of the Caccetta–Häggkvist triangle problem, with a short elementary counting proof.

The proof counts two-step paths across nonadjacent pairs. Their total mass is at least `3d^2(d+1)/2`; there are `3d(d-1)/2` nonadjacent pairs. Applying `ab >= d(a+b-d)` for `0<=a,b<=d` forces the opposite-path product sum to be at least `3d^3`. Every directed four-cycle contributes exactly twice. Opposite vertices cannot be adjacent without creating a directed triangle.

**Evidence:** the explicit [source proof](https://github.com/jaredwilder/caccetta-haggkvist-triangles/blob/main/source/big-guns-2026-08-06/CH3-TERMINAL-AUDIT-CUBIC-C4-THEOREM.md), inspected through its counting argument in this review. No new Lean/kernel check is claimed. This is a structural consequence of the stated hypothetical configuration, not a solution of CH3.

## 2. A complete sum/product avoidance classification modulo 31

For `A subset F31*`, forbid both `x+y=z` and `xy=z` modulo 31, with repeated variables allowed. Then `|A|<=8`, and **exactly nine sets** attain size eight.

**Why it stands out:** a sharp extremal bound together with every equality case for two interacting operations.

**Evidence:** a fresh independent exhaustive Python search reproduced the maximum and all nine extremizers. It builds the forbidden sets directly from modular arithmetic, branches on inclusion/exclusion, and prunes only impossible or insufficient-cardinality completions. [The theorem, checker, search explanation and dated receipt](https://github.com/jaredwilder/combinatorial-records/tree/main/finite-fields/F31-sum-product-free) are public. This is a finite classification for this field.

## 3. Elimination of both order-49 Cayley tournament families

No Cayley tournament on either `Z/49Z` or `F7^2` has property S4: every four vertices are beaten by a vertex outside that four-set.

**Why it stands out:** complete exclusion of two structured families at a specific frontier order, with proof-checker evidence rather than search failure.

**Evidence:** the [published monolithic encoding and certificate report](https://github.com/jaredwilder/erdos902/blob/main/ORDER49_MONOLITHIC_ASSAULT.md) records two independent UNSAT solvers and DRAT verification. Those large traces were not rerun in this shortlist review. Arbitrary order-49 tournaments remain outside this elimination.

## 4. Four kernels govern all 2-connected graphs of cycle rank three

Suppress maximal degree-two paths in a finite simple 2-connected graph with cyclomatic number three. The resulting loopless multigraph kernel has exactly one of four branch types: `Q4`, `T221`, `D22`, or `K4`.

**Why it stands out:** an exhaustive structural classification that supplies a compact starting point for the associated coherence/CSP analysis.

**Evidence:** the [focused fiber-coherence source program](https://github.com/jaredwilder/fiber-coherence-cycle-rank) contains the rank-three packet and its hypotheses. This classification's prose/source authority is separate from the newly replayed round-four finite checks; that replay does not certify every rank-three statement. Rank-four targets remain open.

## 5. Exact finite-difference avoidance thresholds

Let C_k(N) be the largest subset of `{1,...,N}` with no k+1 distinct elements admitting any ordering with vanishing kth finite difference. Published exact thresholds include

`C3(51)=12`, and `C4(30)=10`, `C4(31)=11`, `C4(32)=12`.

**Why it stands out:** exact optima and explicit witnesses identify precise transitions, rather than only lower-bound constructions.

**Evidence:** the [extension tables and receipts](https://github.com/jaredwilder/ck-sequences/blob/master/evidence/extension-2026-09-11.md) report OPTIMAL solver status and successful prior-table replay. This review directly checked all 11,880 ordered distinct quadruples of the printed 12-element C3(51) witness; the matching upper bound remains supported by the published optimization receipt, not a new optimization run here. The ordering convention is essential.

## Review handoff

For external assessment, begin with the precise statement and hypotheses above, then inspect the linked proof, witness or verifier. Novelty conclusions should be recorded separately from mathematical validity, finite completeness and formal verification. Archive size and generated-card counts are not used as headline evidence.
