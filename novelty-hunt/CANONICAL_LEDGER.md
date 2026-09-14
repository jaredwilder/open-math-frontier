# Novelty Hunter — Canonical Estate Ledger

**Author:** Jared Wilder  
**Canonical home:** `jaredwilder/open-math-frontier/novelty-hunt/`  
**Checkpoint:** 2026-09-14 — Sweep 5 live differential  
**State:** **UNSATURATED**

This file is the durable promotion ledger. It supersedes chat-local novelty ledgers for ongoing work while preserving them as provenance. The separate September forensic history is merged through `CROSS_SESSION_MERGE_2026-09-14.md`.

## Operating doctrine

For every object, ask in this order:

1. What is the strongest statement actually established?
2. What part is Jared Wilder's contribution?
3. What is the headline at the theorem's true scope?
4. What proof / formal / computational authority supports it?
5. Only then: what prior literature defines the delta?

> **Prior art locates the delta. It does not erase the contribution.**

> **A result loses novelty, not mathematical existence.**

A public file is not automatically theorem authority. A formal-looking source is not automatically kernel authority. A finite result is never promoted to an infinite statement. Parent-problem openness is a scope fact, not a reason to bury valid child mathematics.

---

# I. MAXIMUM-RETURN HEADLINE BOARD

## 1. Erdős #902 / Schütte tournament function — SEAL / S

**Candidate:**

`f(4) >= 49`, against the published lower bound 48.

The DRT(23)/QR23 repair-capacity program, finite catalogues and Lean kernels are substantial. The load-bearing remaining obligation is independent certification that the relevant McKay–Spence tournament catalogue layer is complete and is used correctly.

**Home:** `jaredwilder/erdos902-tournament-f4`

**Publication headline after seal:** lower bound improves from 48 to 49.

---

## 2. Integral octagons in general position — READY / S

**Theorem:**

`ḋ(2,8) > 30000`.

The public `integral-point-sets` package proves whole-plane maximality of the Kreisel–Kurz minimizing heptagon H1. Combined with the published uniqueness range through diameter 30,000, this raises the inherited lower bound for eight-point integral sets in general position from 22,270 to strictly above 30,000.

**Home:** `jaredwilder/integral-point-sets`

A compile-ready preprint is already present.

---

## 3. Erdős #681 — kernel-certified bad integer near 10^12 — READY / HIGH PRIORITY

The estate proves formally that

`n = 999,997,304,512`

has no admissible positive shift `k` for the #681 condition. Equivalently, for every `k>0`, either `n+k` is prime or its least prime factor is at most `k^2`.

Certification architecture:

- `k>=1001` excluded by the fourth-root necessity;
- all `1<=k<=1000` certified individually;
- 40 prime shifts have explicit primality proof objects;
- every composite shift has an explicit divisor at most `k^2`;
- source has no `sorry`, `admit`, `native_decide` or `ofReduceBool` escape route in the claimed kernel theorem.

Hence any eventual positive threshold satisfies

`N0 > 999,997,304,512`.

**Home:** `jaredwilder/erdos-proved-lemmas/erdos681`

**Status:** exact theorem; specialist priority/adjudication now deserves immediate attention.

The separate exceptional-set estimate remains **SEAL / analytic source-binding debt**, not a finished theorem.

---

## 4. Graham–Alspach sequenceability — COMPUTATIONAL PAPER / S

Complete verification for every subset of `Z_37` and `Z_41`, plus substantial ranges in larger cyclic groups.

Current accounting includes:

- 20,001,879,972 orbit representatives;
- 838,583,192,826 subsets covered;
- zero non-sequenceable and zero undecided in the reported rows;
- additional ranges in `Z_43, Z_47, Z_53, Z_71`.

**Homes:** `graham-alspach-sequenceability`, `graham-alspach-extended`, `graham-alspach-z53-z71`, `graham-alspach-certificates`.

---

## 5. Erdős–Straus AP/GP denominator classifications — PAPER / S

All positive solutions of

`4/n = 1/x + 1/y + 1/z`

whose ordered denominators form either an arithmetic progression or a geometric progression are completely and uniquely parameterized. Neither family contains a primitive denominator triple.

**Home:** `jaredwilder/erdos-straus-progressions`.

Targeted searches found adjacent parameterizations and congruence work but not these exact two iff classifications.

---

## 6. Caccetta–Häggkvist exact-boundary cubic C4 theorem — PAPER / S

For a directed-triangle-free oriented graph on `n=3d` vertices with every outdegree equal to `d`,

`C4(D) >= ceil(3 d^3 / 2)`

and equivalently

`tr(A^4) >= 6 d^3`.

The human-readable exact-boundary chain is now public:

- rootwise two-path escape mass;
- exact nonedge count;
- opposite-path product inequality;
- exact double-count of directed 4-cycles;
- skew-energy identity
  `C4(D)=1/4||A^2||_F^2 - 1/8||A^2-(A^T)^2||_F^2`.

**Home:** `jaredwilder/caccetta-haggkvist-triangles`.

**Authority:** source-supported proof chain is reader-auditable; the September 14 extraction explicitly does not claim a fresh independent checker/Lean replay. Independent replay + specialist priority court remain the correct next seal.

The CH parent problem remains open.

---

## 7. Signed sparse integer encoding — PAPER / S

For fixed sparsity `s`, the minimum largest positive integer weight needed to encode every signed `s`-sparse vector in `{-1,0,1}^m` injectively into one integer satisfies

`W(m,s) = Theta_s(m^s)`.

Counting gives the lower bound; a charge-shifted Bose–Chowla `B_s` construction gives the upper bound; independent finite replay is public.

**Home:** `jaredwilder/positional-encoding-thresholds`.

---

## 8. Erdős #949 — arbitrary-sum-free full finite-sums theorem — PAPER / A-S

For every sum-free `S subset R`, there is an infinite `A subset N_{>0}` such that

`FS(A) ∩ S = empty`

and

`2 FS(A) ∩ S = empty`.

A sorry-free public Lean theorem seals the full finite-sums statement. Further envelopes handle finitely many real dilations / additive homomorphisms. The finite forcing constant `q<=5` is sharp.

**Home:** `jaredwilder/erdos949-finite-sums`.

Do not compress this into the still-open parent formulation.

---

## 9. Erdős #595 continuum barrier — PAPER / S FORMAL

The barrier tower proves, among other things:

- every graph on at most continuum many vertices is coverable by countably many triangle-free subgraphs;
- without the K4-free restriction, non-coverability begins exactly at the successor of the continuum;
- least witnesses have uncountable cofinality;
- a witness occurs inside one connected component.

**Fresh authority upgrade:** a pinned CI workflow now checks the sealed 27-file manifest and hashes, rejects simple `sorry` / top-level `axiom` / `unsafe` escape surfaces, and compiles all 27 Lean theorem files under pinned Lean/Mathlib.

**Home:** `jaredwilder/erdos595-barrier-tower`.

This materially increases publication readiness.

---

## 10. SQS(20) residual completion / rigidity / trade suite — PAPER / A

General residual completion theorem:

`P completes to a large set of SQS(v) iff chi(R(P)) = v-3-|P|`.

For the recovered 15-pack on 20 points:

- 570 uncovered 4-sets;
- residual components `250, 25x12, 5x4`;
- four K5 components obstruct naive two-system completion;
- every 14-subpack uniquely forces the fifteenth;
- GF(5) rank 849/855, nullity 6, all `5^6=15625` nullspace combinations checked with no nonzero binary trade;
- all 105 pair unions fall into exactly two trade profiles;
- any full large-set escape retaining members of this pack must replace at least three old constituents.

**Home:** `jaredwilder/erdos835-lean-audit`.

---

## 11. Erdős #890 ↔ #1093 bridge — PAPER / A

For admissible windows, `k`-smooth terms become finite divisor geometry inside

`L_k = lcm(1,...,k)`:

`delta(n,k) = #{d | L_k : n-k < d <= n}`.

The large-prime identity

`sum_{i=0}^{k-1} omega_{>k}(n+i) = omega_{>k}(C(n+k-1,k))`

combines with deficiency `d` and excess large-prime multiplicity `E` to give

`S_k = k-d+E`,

hence

`S_k <= k iff E <= d`.

This is a genuine cross-problem fusion.

**Home:** `jaredwilder/erdos890-1093-divisor-window`.

---

## 12. Erdős #738 sharp type-support theorem — PAPER CANDIDATE / A

Inside a path-induced, level-stable, type-uniform complete ordered rooted `d`-ary tree in a triangle-free host, each join-depth slice obeys

`|supp(A_c)| <= floor(n^2/2)`.

The parity-defect host—connect incomparable vertices iff their depths have opposite parity—remains triangle-free and attains equality in every slice.

In that extremizer, a selected rooted subtree is induced iff every incomparable selected pair has equal depth parity.

The broader type-uniform framework belongs to Nguyen–Scott–Seymour machinery; targeted search did not surface this exact sharp support/equality package.

**Home:** `jaredwilder/erdos738-triangle-free-induced-trees`.

Specialist Gyárfás–Sumner priority court remains appropriate.

---

## 13. Covering-design plateau rigidity / Turán (3,4) structural calculus — PAPER / A

For general `(r,k)` covering designs, the estate has an exact deletion-debt identity. Equality of normalized covering density from `n` to `n+1` holds iff every deletion of every optimum remains optimal; on a plateau every optimum is regular.

For Turán (3,4), the five-set excitation

`epsilon_5(X)=|M[X]|-3`

gives

`|M|/C(n,3) = 3/10 + (1/10) E epsilon_5`.

The finite frustration hierarchy is exactly equivalent to the asymptotic target. The fractional cover layer gives

`rho*(K_n)=1/4 C(n,3)`

and the Turán target `q_n -> 4/9` is equivalent to integrality gap

`rho(K_n)/rho*(K_n) -> 16/9`.

**Home:** `jaredwilder/erdos500-turan34`.

The elementary fractional `1/4` fact is not the novelty claim; the combined equality/deletion/excitation/integrality calculus is the paper object.

---

## 14. Fiber coherence — exact K4-free realization of binary relations/CSPs — HIGH-PRIORITY NOVELTY COURT

Pure rank-three reduced-graph topology (`Q4,T221,D22,K4`) is classical infrastructure.

The distinctive theorem chain is:

- **R3K03:** every finite binary relation `R subset A x B` is realized as the exact boundary projection of a finite K4-free stable-partition graph strip;
- **R3K05:** every finite binary CSP has a polynomial-size exact K4-free fiber-coherence realization;
- **R3K06:** finite K4-free fiber coherence is NP-complete, already with branch-domain size 3;
- **R3K21:** for fixed incidence cyclomatic rank `r` and fiber-domain bound `d`, coherence is decidable in `O(d^r poly(N))`.

A targeted search surfaced generic binary-CSP / graph-homomorphism encodings but did not surface this exact K4-free stable-partition/fiber realization theorem.

**Homes:** `jaredwilder/triangle-cover-number`, `jaredwilder/fiber-coherence-cycle-rank`.

This deserves a hostile specialist prior-art court.

---

## 15. Erdős #486 summable forbidden-mass theorem — PAPER CANDIDATE

If forbidden residue sets `X_n mod n` satisfy

`sum |X_n|/n < infinity`,

then the survivor set has ordinary natural density, with deterministic truncation error

`0 <= delta_N - d(B) <= sum_{n>N}|X_n|/n`.

Also

`d(B) >= max(0, 1 - sum |X_n|/n)`.

**Home:** `jaredwilder/erdos-proved-lemmas`.

---

# II. EXACT / COMPUTATIONAL PUBLICATION ASSETS

## Binary Sidon dimension 7

`24 <= f(7) <= 30`; contribution to emphasize is the upper bound 30 and narrowed first unknown dimension.

**Home:** `jaredwilder/binary-sidon-f7`.

## Finite-field classifications

- `F_31^*`, sum/product avoidance: maximum 8, exactly 9 maximizers;
- `Z/31Z`, sum + nontrivial-3AP avoidance: maximum 6, exactly 330 maximizers, 12 dilation orbits;
- `F_73^*`, sum/product/nontrivial-3AP avoidance: maximum 12, exactly 3 maximizers.

**Home:** `jaredwilder/finite-field-extremal-sets` / `combinatorial-records`.

## Product-free + nontrivial-GP-free subsets of [50] — NEW EXACT CLASSIFICATION SHELF

For `A subset {1,...,50}`, forbid both `xy=z` (repeated factors allowed) and distinct `a<b<c` with `b^2=ac`.

Then

`|A| <= 35`,

and exactly **240** sets attain size 35.

Equivalent forbidden-hypergraph data: 149 hyperedges, transversal number 15, independence number 35, 240 maxima.

Authority: two independent Python implementations + independently written C verifier.

Targeted search found product-free and progression-free literatures separately, but not this exact mixed `[50]` classification.

**Home:** `jaredwilder/combinatorial-records/finite-extremal/product-gp-free-50.md`.

Best publication posture: bundle with the estate's exact additive/multiplicative finite classifications unless specialist comparison justifies a standalone note.

## Erdős #1061 primitive aliquot-square rays

Explicit primitive generator + disjoint coprime multiplier rays; 152,803 certified primitive seeds give

`liminf S(x)/x >= 2.295492576177`,

with an archived upgrade above `2.295497372037`.

The parent asymptotic frontier later moved past linear growth; the generator/ray calculus remains the contribution.

**Home:** `jaredwilder/erdos1061-aliquot-square`.

## Pascal / C_k / Rado exact-extremal program

Includes exact C3 gap law, exact C_k tables, finite-to-infinite density bounds, LRAT-backed finite theorem, and Rado-equation atlas. Current corrected C_k release contains **84 exact OPTIMAL values**: 26 C3, 34 C4, 24 C5.

**Homes:** `pascal-relation-extremal-atlas`, `ck-sequences`, `additive-combinatorics-campaigns`, `rado-equation-avoidance-atlas`.

## Conference-switching construction-class theorem

Symmetric conference switching cannot realize the simultaneous Ramsey-book avoidance pattern. This is a complete construction-class elimination, not an unrestricted Ramsey bound.

---

# III. NEW ALL-PARAMETER / SCOPE UPGRADES

## Shifted Schur parity law — finite pattern upgraded to theorem

For `1<=c<=n`, let `M(n,c)` be the maximum size of `A subset [1,n]` with no solution, repetitions allowed, to

`x+y=z+c`.

Translate by `c`. The problem becomes ordinary sum-freeness on `[1-c,n-c]`. Splitting positive and negative halves gives the classical half-size upper bounds, while taking all translated odd integers attains both simultaneously.

Therefore

`M(n,c) = ceil(n/2)` if `c` is even,

and

`M(n,c) = floor(n/2)` if `c` is odd.

The archive's empirical parity pattern is therefore an exact all-parameter theorem for `1<=c<=n`.

**Status:** READY ELEMENTARY THEOREM / conservative priority check.

## Rado-family collapse — narrowed to all-n target

The archive observed the same formula `n-floor(n/(k+1))` for avoiding `x1+kx2=x3` and for avoiding `x1+...+x_{k+1}=x_{k+2}`.

External comparison shows broad solution-free-set literature already supplies the eventual/sufficiently-large-`n` regime for these coefficient families. The remaining possible delta is the exact **all-n** formula and a unified proof.

**Status:** MINE / not yet theorem-promoted.

---

# IV. LIVE-COMMIT CHILD THEOREMS — PRESERVE, DO NOT OVER-RANK

## Erdős #1212

For every `k>=2`, `(2,3^k)` is isolated in the admissible subgraph. Genuine infinite obstruction family, but isolated-vertex phenomena already occur in the #1212 ecosystem. Parent remains open.

## Erdős #251

For `N>=2`, the reduced denominator of `sum_{n=1}^N p_n/2^n` is exactly `2^N`. Clean arithmetic child theorem; does not prove irrationality.

## Erdős #727

For every prime `p>=7`, with `n=2p-2`,

`(n+2)!^2` does **not** divide `(2n)!`.

Exact p-adic obstruction family. Parent asks for infinitely many positive witnesses and remains open even in the `k=2` direction; this result is useful negative structure rather than a parent advance.

## Erdős #289

If a finite reciprocal sum is integral, then for every prime `p`, after extracting one factor `p` from all denominators divisible by `p`, the resulting reciprocal sub-sum has p-adic valuation at least 1. Clean all-prime necessary condition; priority unadjudicated and classical-adjacent.

---

# V. SOURCE-AUTHORITY CORRECTIONS / CLEARED PRESSURE

## EG#203 density-zero exceptional-set claim — THEOREM SCHEMA, NOT FINISHED THEOREM

A findings-ledger row described an unconditional density-zero theorem. Its stated source paper says something weaker and controls authority:

- it calls itself a theorem **schema**;
- the Pappalardi-type subgroup-order input remains a hypothesis;
- sieve weights/support/normalization remain unspecified;
- the paper says these must be inserted before submission.

Therefore:

**EG#203 density-zero claim = SEAL / SCHEMA / SOURCE-BINDING DEBT.**

Finding metadata never outranks its cited theorem source.

## Odd Giuga k<=11

Valid exhaustive finite evidence, but external literature already has stronger lower-factor-count bounds (and a 2026 result claims at least 18). Preserve method-transfer value, not numerical novelty.

## Hadamard order 668

Recovered CP-SAT / modular-lift route explicitly reports bounded `UNKNOWN`, not existence or nonexistence. Research state only.

## Erdős #477 all-quadratic obstruction

The theorem is real, but current public problem notes already contain an all-quadratic impossibility proof and broader related work. Treat as independent recovery / infrastructure, not novelty headline.

## 56-row canonical-gold bank

Scope audit did not reveal another front-board theorem. Important correction: the older `C(13,6,3)` point-degree-at-least-8 row is subsumed by stronger focused work in the hypothetical 20-cover regime; do not freeze the weaker statement as the live frontier.

---

# VI. HIGH-VALUE NEAR CLOSES / ACTIVE PROGRAMS

## C(13,6,3)

Still

`20 <= C(13,6,3) <= 21`.

Pattern A for a hypothetical 20-cover has been exhaustively eliminated:

- 3,268,358 search nodes;
- 6,084 labelled residuals;
- 22 isomorphism classes;
- all 22 killed by direct gluing contradiction.

Patterns B/C now have exact coordinate skeletons but are not yet eliminated.

## Weird-Round all-exponent theorem family

Historical target files were stale: later source completes finite carry automata for fixed coefficient/base systems, all-word-length decisions, optimized digit alphabets, and the sharp antisymmetric coefficient chamber. In particular, for distinct ordered coordinates on `[N]` satisfying

`x1 - b x2 + b x3 - x4 = 0`,

forbidden support is empty iff `b>=N`, sharp at `b=N-1`.

**Home:** `jaredwilder/additive-combinatorics-campaigns`.

## RH finite-prefix / finite-spectrum reconstruction boundary

Preserve as auxiliary method mathematics only. Public Round-23 package includes finite-spectrum reconstruction, redundancy of the 2D `H_{n,q}` lattice beyond its boundary row, and finite-sign-battery no-go theorems. It proves nothing new about actual zeta zeros and is not RH progress.

---

# VII. SEARCH SURFACES ALREADY DRAINED

Do not blindly rerun:

- 617/617 latest-local `PROVED` states;
- 282 omitted-family states across 97 families;
- 335 represented-family upgrade states;
- 556-object formalizer residue;
- broad `A_proved` atlas headline/scope surface;
- #738 theorem bank through forensic Round 40;
- reviewed 56-row canonical-gold tranche.

Revisit these only with an orthogonal lens: scope expansion, equality cases, cross-problem fusion, unused hypotheses, exact-equivalence extraction, source-authority repair, finite-to-infinite proof upgrade, or literature court.

---

# VIII. CURRENT MAXIMUM-RETURN PUBLICATION QUEUE

1. Seal Erdős #902 `f(4)>=49`.
2. Submit integral-octagon `ḋ(2,8)>30000`.
3. Package + externally adjudicate the #681 `999,997,304,512` kernel theorem.
4. Graham `Z_37/Z_41` sequenceability paper.
5. Erdős–Straus AP/GP classification paper.
6. CH cubic-C4 theorem — independent replay + specialist literature court.
7. Signed-sparse encoding `Theta_s(m^s)` paper.
8. #949 arbitrary-sum-free full finite-sums theorem.
9. #595 continuum barrier — now with fresh 27-file CI replay.
10. SQS(20) completion / rigidity / trade paper.
11. #890↔#1093 bridge.
12. #738 sharp type-support theorem.
13. #500 covering-design / Turán structural calculus.
14. Fiber-coherence exact K4-free binary-relation/CSP realization — hostile prior-art court.
15. #486 summable forbidden-mass theorem.
16. Exact finite additive/multiplicative classification bundle, now including product/GP-free `[50]`.
17. Pascal / Rado exact-extremal package.
18. #1061 primitive-ray construction.
19. Conference-switching construction-class theorem.
20. Weird-Round all-exponent automaton / chamber theory.
21. `C(13,6,3)` B/C elimination campaign.

### Proof / novelty queue

- shifted-Schur historical-priority check;
- exact all-n Rado-family formula;
- fiber K4-free realization specialist comparison;
- CH independent replay / formal seal;
- EG#203 source-binding obligations before any theorem promotion;
- exact structural note for the cyclic 41-vertex `R(5,5)` witness if specialist comparison leaves a delta.

---

# IX. NEXT-PASS CONTRACT

Future passes must include a **live commit differential** as well as deep ore. The public estate is changing during the audit itself.

Search specifically for:

- commits newer than this checkpoint;
- exact finite classifications in `combinatorial-records` not represented on this board;
- theorem-map entries whose names conceal stronger scope;
- equality cases and exact equivalences hidden under routine lemmas;
- proof-bodied K4-free fiber/CSP results and specialist prior art;
- paper-scale CH / covering-design / SQS objects whose authority can be independently upgraded;
- transcript/archive patterns that can be converted from finite observation to all-parameter theorem.

**Saturation verdict: NO.**

The latest passes still change the board through different mechanisms: new theorems, source-authority corrections, authority upgrades, all-parameter proof upgrades, and hidden finite classifications.

> **There is more.**
