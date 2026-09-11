# Buried Mathematics — program promotion index

**Author:** Jared Wilder  
**Started:** 2026-09-11

This index exists for one reason: **substantial mathematical programs must not become invisible merely because they were first released inside a provenance archive.**

It is a temporary navigation and promotion surface. Once a program has a dedicated problem repository, that repository becomes the preferred reading/citation home and this page points there.

## Priority A — already unquestionably repository-scale

### Erdős #738 / triangle-free Gyárfás–Sumner

Current source: `jaredwilder/unpublished-math-papers/erdos738-theorem-bank/`  
Planned home: `jaredwilder/erdos738-triangle-free-induced-trees`

Recovered program:

- **62** statements/schemas marked proved in the packet;
- **12** explicit unproved search targets;
- **45,301-byte** human-readable theorem bank;
- independent finite verifier and verification receipt;
- paper-shaped subtheories in extremal type tensors, mixing/spider structure, chromatic escape, induced-path contact codes and contamination-fan calculus.

The dedicated repository shell already exists, but it currently has no initial commit; the connected GitHub contents API cannot initialize a zero-commit repository. Until that shell is initialized, the archive remains the byte-complete public source.

### Erdős–Gyárfás power-of-two cycles

Current source: `jaredwilder/unpublished-math-papers/erdos-gyarfas-power-cycle/`

The V2 research bank contains **202 exact theorem cards** across ten coherent families:

- 120 proved in the packet;
- 16 computationally certified;
- 9 proved negative theorems;
- 9 refuted routes;
- 34 explicit checkable targets;
- remaining cards are conditional, source-derived or withdrawn with status preserved.

Major layers include minimum-counterexample sparsity, C4-free expansion, cubic/high-degree defect kernels, perfect-matching transition quotients, ear theory, cubic suppression, lens decomposition, dyadic subset-sum criteria, packet hypergraphs, monotone-CNF reduction and exact finite obstruction certificates.

This should receive a dedicated problem repository rather than remain a four-JSONL-card archive folder.

### Caccetta–Häggkvist directed triangles

Current source: `jaredwilder/unpublished-math-papers/caccetta-haggkvist/`

The program includes:

- a **23KB theorem ledger** from the first fifteen rounds;
- an **8.5KB** Rounds 18–19 terminal-defect package;
- exact-boundary regular-kernel structure;
- escape, bridge, fan and chamber identities;
- two-path matrix/fourth-moment structure;
- directed-C4 auxiliary-graph structure;
- a corrected opposite-fan theorem;
- critical-cycle edge potentials and an exact defect telescope;
- supported statements, conditional reductions, proposals, structural diagnoses and explicit retractions.

A human README now exists in the archive, but the program warrants its own repository.

### Erdős #890 ↔ #1093

Current compact home: `jaredwilder/erdos-proved-lemmas/erdos890-1093-bridge.md`  
Additional provenance: `jaredwilder/unpublished-math-papers/`

This has grown past theorem-bank scale: large-prime binomial identity, deficiency/excess accounting, admissible LCM divisor-window reduction, finite deficiency engine through the released range, and a substantial forensic problem history. It should graduate to a dedicated problem/program repository.

## Priority B — large audited theorem programs

### Erdős #271 — Stanley sequences

Current source: `jaredwilder/unpublished-math-papers/erdos271-stanley/`

Audited master ledger: **184 entries**:

- 111 retained proved;
- 27 retained proved with correction;
- 1 retained proved/subsumed;
- 13 conditional theorems;
- 18 conjectures/targets;
- 7 refuted/retired;
- 4 finite computational verifications;
- 2 exploratory/unverified;
- 1 external dependency.

The terminal retained reduction introduces reflection support `U_k` and mean multiplicity `mu_k`, obtaining

`a_k = Theta(k + k^2/mu_k)`,

and, using superlinearity,

`a_k = Theta(k^2/mu_k)`.

For `A(4)`, the target `a_k=Theta(k^2/log k)` is thereby equivalent within the campaign reduction to `mu_k=Theta(log k)` and `|U_k|=Theta(k^2/log k)`.

### Erdős #500 / Turán (3,4)

Current source: `jaredwilder/unpublished-math-papers/erdos500-turan34/`

Canonical reconstructed surface: **76 distinct records**, including 43 proved-in-packet results, 7 finite exhaustive results, 18 explicit targets, exact finite witnesses/classifications, a sharp bound, an equivalence, an analytic result and a negative theorem.

Mathematical layers include complement-covering duality, finite-to-global density transfer, deletion-excess identities, plateau rigidity, pair-codegrees, four/five-set waste/excitation, exact small covering values, cyclic pair rotors, one-point extension, graph-generated cover classification, independent-triple repair, integral-gap reformulation and rooted collision identities.

### Lonely Runner — 13 effective speeds

Current source: `jaredwilder/unpublished-math-papers/lonely-runner-13/`

The archive contains a 14KB late-round theorem bank, terminal normal form, structured theorem bank/supplement, and deeper master provenance. A new human README now surfaces the program.

Among the late deductions are:

- an explicit finite speed envelope and uniform slack below `1/14`;
- seven adjacent-gap restrictions;
- an all-prime multiplicity theorem and majority-gcd hierarchy;
- a strict deletion theorem producing a non-tight 12-speed deletion;
- a robust private deletion interval.

This is a coherent research program and should receive a dedicated repository.

## Priority C — focused finite / structural programs

The following archive subjects are already strong standalone candidates and should be checked for existing homes before any new repo is created:

- `fiber-coherence-theorem-bank/` + `rank-three-kernel/` — related graph/CSP structural work;
- `ramsey-r55-circulant-structure/` — 41-vertex circulant `(5,5)` Ramsey structure/certificates;
- `polynomial-dynamics-coordinates/` — recurrence/coordinate mathematics;
- `product-gp-free-50/` — exact finite extremal classification with 240 extremizers;
- `f31-sum-product-avoidance/`;
- `f73-mixed-avoidance/`;
- `erdos1142-order-sieve/` if its program-scale computation/formal artifacts exceed the compact theorem-bank summary;
- `erdos949-sumfree-ip/`;
- `erdos1066-lattice-barriers/`;
- `erdos156-maximal-sidon-barrier/`;
- `erdos247-sparse-binary-irrationality/`;
- `erdos243-divisibility-irrationality/`.

## Consolidated instead of split

These were found buried but **did not need another competing repository**:

- Erdős #595 triangle-cover theorem bank → promoted into `jaredwilder/erdos595-barrier-tower`;
- Erdős #835 SQS(20) completion/rigidity/trades → promoted into `jaredwilder/erdos835-lean-audit`, now treated as the #835 problem program despite its historical repo name;
- EG203 recovered analytic-route papers → indexed from `jaredwilder/eg203-kummer-papers`;
- Erdős #376 Kummer criterion → integrated into `jaredwilder/erdos376-successor-frontier`;
- Erdős #503 geometry → integrated into `jaredwilder/erdos-lean-remainder`;
- additive/Sidon results #52, #153 and #241 → `jaredwilder/additive-combinatorics-campaigns`.

## Audit-first promotion

**Repository scale is not theorem authority.** Large folders with unusually high-stakes claims should be audited before their headline is amplified. `riemann-hypothesis/` is currently the clearest example.

The correct response to a large unaudited folder is therefore **audit immediately**, not either “bury it forever” or “promote the headline blindly.”

## Promotion rule

A program should leave this page and become a dedicated canonical repository when:

1. a writable repository exists;
2. the human README states the mathematics directly;
3. theorem / target / computation / correction statuses remain distinct;
4. provenance back to the intake archive is retained;
5. the release index is updated to point to the new home.

The archive is allowed to remember everything. It is not allowed to hide the mathematics.
