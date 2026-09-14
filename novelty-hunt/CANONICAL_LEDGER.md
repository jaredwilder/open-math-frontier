# Novelty Hunter — Canonical Estate Ledger

**Author:** Jared Wilder  
**Canonical home:** `jaredwilder/open-math-frontier/novelty-hunt/`  
**Checkpoint:** 2026-09-14  
**State:** UNSATURATED  
**Supersedes for ongoing work:** the chat-local `NOVELTY_HUNTER_CANONICAL_ESTATE_HEADLINE_LEDGER_v2_2026-09-14.md` as the durable working ledger. That artifact remains provenance.

This is a **promotion ledger**, not a rejection ledger.

For each object:

1. reconstruct the strongest statement actually established;
2. identify Jared Wilder's exact contribution delta;
3. grade the mathematical headline at its true scope;
4. identify proof / formal / computational authority;
5. only then use prior art to position the contribution.

> **Prior art locates the delta. It does not erase the contribution.**

> **A result loses novelty, not mathematical existence.**

Status vocabulary:

- **READY** — theorem/result can be written and submitted at current scope;
- **SEAL** — major candidate with a named remaining authority dependency;
- **PAPER** — coherent standalone theorem package;
- **COMPUTATIONAL PAPER** — exact finite/classification result with reproducible evidence;
- **MINE** — strong buried candidate needing a dedicated proof/novelty pass;
- **KNOWN/REDISCOVERY** — mathematically real, novelty collided/subsumed;
- **QUARANTINE** — broken edge / statement mismatch preserved as regression data.

---

# 1. Front-rank board

## 1.1 Integral octagons in general position — READY / S

**Claim:** `ḋ(2,8) > 30000`.

The `integral-point-sets` program proves whole-plane maximality of the Kreisel–Kurz minimizing heptagon H1. Combined with published uniqueness through diameter 30,000, every 8-point integral configuration in general position has diameter strictly above 30,000.

**Home:** `jaredwilder/integral-point-sets`.

**Headline:** new lower bound for integral octagons in general position.

---

## 1.2 Erdős #902 / Schütte tournament function — SEAL / S

**Candidate:** `f(4) >= 49`, against the published lower bound 48.

The repair-capacity computation reproduces exactly and the surrounding DRT(23)/QR23/Lean program is substantial. The remaining named dependency is independent certification that the relevant McKay–Spence tournament catalogue layer is complete and used correctly.

**Home:** `jaredwilder/erdos902-tournament-f4`.

**Action:** treat the catalogue bridge as a finite certification job, not a reason to demote the theorem.

---

## 1.3 Graham–Alspach sequenceability — COMPUTATIONAL PAPER / S

Complete verification for every subset of `Z_37` and `Z_41`, plus larger cyclic ranges.

Current public accounting:

- 20,001,879,972 orbit representatives;
- 838,583,192,826 subsets covered;
- zero non-sequenceable and zero undecided in the reported rows;
- additional verified ranges in `Z_43, Z_47, Z_53, Z_71`.

**Homes:** `graham-alspach-sequenceability`, `graham-alspach-extended`, `graham-alspach-z53-z71`, `graham-alspach-certificates`.

---

## 1.4 Erdős–Straus AP/GP denominator classifications — PAPER / S

Every positive solution of

`4/n = 1/x + 1/y + 1/z`

whose ordered denominators are in arithmetic progression or geometric progression is completely and uniquely parameterized. Neither family contains primitive denominator triples.

**Home:** `jaredwilder/erdos-straus-progressions`.

Targeted searches found adjacent parameterizations/congruence work but not these exact two iff classifications.

---

## 1.5 Caccetta–Häggkvist extremal boundary — PAPER + FORMALIZE / S

If an oriented graph has `3d` vertices, every outdegree equals `d`, and it contains no directed triangle, then

`C4(D) >= ceil(3 d^3 / 2)`

and equivalently

`tr(A^4) >= 6 d^3`.

**Home:** `jaredwilder/caccetta-haggkvist-triangles`.

**Action:** independent Lean formalization and specialist literature seal.

---

## 1.6 Signed sparse integer encoding — PAPER / S

For fixed sparsity `s`, the least possible largest positive integer weight needed to injectively encode every signed `s`-sparse vector in `{-1,0,1}^m` into one integer satisfies

`W(m,s) = Theta_s(m^s)`.

Counting gives the lower bound; a charge-shifted Bose–Chowla `B_s` construction gives the upper bound.

**Home:** `jaredwilder/positional-encoding-thresholds`.

---

## 1.7 Erdős #949 — PAPER / A-S

For arbitrary sum-free `S subset R`, the estate has a public sorry-free Lean theorem producing infinite `A subset N` such that

`FS(A) ∩ S = empty`

and

`2 FS(A) ∩ S = empty`.

Further envelopes cover finitely many dilations / additive homomorphisms. The finite forcing constant `q<=5` is sharp.

**Home:** `jaredwilder/erdos949-finite-sums` plus formal theorem bank.

**Boundary:** do not misstate the remaining continuum parent formulation.

---

## 1.8 Erdős #595 continuum barrier / triangle-cover theory — PAPER / S formal

A 27-file sorry-free Lean package proves, among other things:

- every graph on at most continuum many vertices is a countable union of triangle-free subgraphs;
- without the `K4`-free restriction, non-coverability starts exactly at the successor of the continuum;
- least witnesses have uncountable cofinality;
- a witness occurs inside one connected component.

The larger `triangle-cover-number` program contains coherence/CSP/cycle-rank theory.

**Homes:** `erdos595-barrier-tower`, `triangle-cover-number`.

---

## 1.9 SQS(20) residual completion / rigidity / trade suite — PAPER / A

For a partial large set `P` of pairwise block-disjoint SQS(v), with `q=v-3-|P|`, completion is equivalent to `chi(R(P))=q` for the residual graph on uncovered 4-sets.

For the recovered 15-pack on 20 points:

- 570 uncovered 4-sets;
- residual component sizes `250, 25x12, 5x4`;
- four `K5` components obstruct naive completion by two more systems;
- every 14-subpack uniquely forces the fifteenth;
- GF(5) rank `849/855`, nullity 6, all `5^6=15625` combinations checked with no nonzero binary trade;
- all 105 pair unions fall into exactly two trade profiles: 30 same-row and 75 cross-row;
- any full large-set escape retaining systems from this pack must replace at least three old constituents.

**Home:** `jaredwilder/erdos835-lean-audit`.

---

## 1.10 General covering-design plateau rigidity — PAPER / A-S candidate

Let `c_n^{r,k}` be the minimum number of `r`-sets meeting every `k`-set. For an optimal `(r,k)` cover on `n+1` vertices,

`sum_v (|M-v|-c_n^{r,k}) = (n+1-r)c_{n+1}^{r,k} - (n+1)c_n^{r,k}`.

Consequences:

- normalized density is nondecreasing;
- a density plateau occurs **iff every vertex deletion of every optimum is itself optimal**;
- on a plateau, **every optimum is regular** with point degree `c_{n+1}^{r,k}-c_n^{r,k}`.

This is wider than the Turán (3,4) problem in which it was discovered.

**Home:** `jaredwilder/erdos500-turan34`.

Targeted search found standard Schönheim/deletion theory but not this exact equality/full-heredity/regularity characterization.

---

## 1.11 Turán (3,4) five-set excitation / frustration coordinates — PAPER / A

For a four-set cover `M`, every five-set `X` contains at least three selected triples. Define

`epsilon_5(X)=|M[X]|-3`.

Then

`C(n-3,2)|M| = 3 C(n,5) + sum_X epsilon_5(X)`

and

`|M|/C(n,3) = 3/10 + (1/10) E epsilon_5`.

Define `Lambda_s` as the minimum total five-set excitation on `s` vertices. Then

`Lambda_s = C(s-3,2)c_s - 3C(s,5)`

and

`sup_s Lambda_s/C(s,5) = lim_n (10 q_n - 3)`.

Thus Turán (3,4) is equivalent to the exact frustration-supremum value `13/9`.

The minimum five-vertex local state is unique up to isomorphism (`P3 disjoint K2` after complementing triples to pairs).

The same program has an exact one-point extension operator via pair-cover number `tau_2(H)` and extension defect/slack calculus.

**Home:** `jaredwilder/erdos500-turan34`.

---

## 1.12 Erdős #890 ↔ #1093 bridge — PAPER / A

For the #1093 window, smooth terms become divisors of `L_k=lcm(1,...,k)`:

`delta(n,k)=#{d|L_k : n-k<d<=n}`.

The large-prime identity

`sum_{i=0}^{k-1} omega_{>k}(n+i) = omega_{>k}(C(n+k-1,k))`

combines with deficiency `d` and excess large-prime multiplicity `E` to give

`S_k = k-d+E`,

hence

`S_k <= k  iff  E <= d`.

This is a genuine cross-problem fusion.

**Home:** `jaredwilder/erdos890-1093-divisor-window`.

---

## 1.13 Diagonal Ramsey sublinear-corridor invariance — SHORT PAPER / A

For `n>a>=0`,

`r(n-a,n) <= R(n) <= 4^a r(n-a,n)`.

Therefore if `a_n=o(n)`,

`(log R(n)-log r(n-a_n,n))/n -> 0`.

So diagonal Ramsey numbers and **every** sublinear off-diagonal corridor have identical exponential limsup and liminf. Convergence on any one such corridor is equivalent to convergence on the diagonal.

The program also proves that approximate supermultiplicativity

`A(m+n+E(m,n)) >= A(m)A(n)`, `A(k)=R(k)-1`,

with `E(m,n)=O((m+n)/log^2(m+n))`, is enough to force existence of `lim R(k)^(1/k)`.

**Home:** `jaredwilder/diagonal-ramsey-corridor`.

---

## 1.14 Erdős #486 summable forbidden-mass theorem — PAPER candidate

If forbidden residue sets `X_n mod n` satisfy

`sum |X_n|/n < infinity`,

then the survivor set has ordinary natural density. If `delta_N` is the finite periodic truncation density and `T_N=sum_{n>N}|X_n|/n`, then

`0 <= delta_N - d(B) <= T_N`.

Also

`d(B) >= max(0, 1-sum |X_n|/n)`.

**Home:** `erdos-proved-lemmas/erdos486-summable-forbidden-mass.md`.

---

## 1.15 Erdős #738 sharp type-uniform tensor obstruction — MINE -> serious novelty target

The focused public bank contains 62 `PROVED_IN_PACKET` and 12 `UNPROVED_CHECKABLE_TARGET` entries, inside a 174-claim research surface.

The strongest distinctive family is T06–T09.

For a complete ordered `d`-ary rooted tree embedded path-induced, level-stable and type-uniform in a triangle-free host, each join-depth support slice obeys

`|supp(A_c)| <= floor(n^2/2)`, `n=k-c`.

A parity-defect host (connect incomparable vertices iff their depths have opposite parity) remains triangle-free and attains equality in every slice.

In that extremizer, a selected rooted subtree is induced iff every incomparable selected pair has equal depth parity.

**Home:** `jaredwilder/erdos738-triangle-free-induced-trees`.

**Novelty state:** general type-uniform framework found in modern Gyárfás–Sumner machinery; targeted search did not find this exact sharp `floor(n^2/2)` + parity-extremizer/equality package. Specialist court required.

---

## 1.16 Fiber coherence / exact K4-free CSP realization — MINE / high priority

Pure rank-three reduced-graph topology (`Q4,T221,D22,K4`) is classical infrastructure, not novelty credit.

The source-specific mathematics begins at relation semantics. The strongest surviving target is the theorem chain

`arbitrary binary relation -> K4-free exact strip -> arbitrary binary CSP exact K4-free realization`.

The finite-fiber program also identifies cycle rank four as the first fixed-rank minimal incoherence core not exhaustively classified.

**Home:** `jaredwilder/fiber-coherence-cycle-rank`.

---

# 2. Strong exact / computational assets

## 2.1 Binary Sidon dimension 7 — READY

Coordinate splitting gives `f(d)<=2f(d-1)`, hence

`24 <= f(7) <= 30`.

The lower witness 24 is known; the contribution to emphasize is the upper bound 30 and narrowed first unknown dimension.

**Home:** `jaredwilder/binary-sidon-f7`.

## 2.2 Finite-field exact classifications — COMPUTATIONAL PAPER

- `F_31^*`, simultaneous sum/product avoidance: maximum 8, exactly 9 maximizers;
- `Z/31Z`, sum-free + nontrivial-3AP-free: maximum 6, exactly 330 maximizers, 12 unit-dilation orbits;
- `F_73^*`, simultaneous sum/product/nontrivial-3AP avoidance: maximum 12, exactly 3 maximizers.

**Home:** `jaredwilder/finite-field-extremal-sets`.

## 2.3 Erdős #1061 primitive aliquot-square rays — PAPER

With `q=sigma(a)-a`, `b=q^2-a`, the stated primality/copimality conditions give primitive solutions of

`sigma(a)+sigma(b)=sigma(a+b)`.

Primitive seeds generate disjoint coprime multiplier rays. A 152,803-seed certificate yields

`liminf S(x)/x >= 2.295492576177`,

with archived extension above `2.295497372037`.

The later parent asymptotic frontier moved beyond linear growth; the generator/ray calculus remains the contribution.

**Home:** `jaredwilder/erdos1061-aliquot-square`.

## 2.4 Pascal / finite-difference extremal atlas — COMPUTATIONAL PAPER

For sorted `a<b<c<d` with gaps `p,q,r`, a `C3` violation is equivalent to one of five exact linear gap relations:

`p+r=2q`, `p=3r`, `r=3p`, `p=2q+3r`, `r=2q+3p`.

Exact C3 tables include `C3(51)=12`, with a kernel-checked span-50 statement backed by a 447,254-addition LRAT proof. The finite table gives an infinite-density consequence.

**Homes:** `pascal-relation-extremal-atlas`, `ck-sequences`, `additive-combinatorics-campaigns`.

## 2.5 Rado-equation avoidance atlas — COMPUTATIONAL PAPER

Eleven complete solver-optimal sequences, 839 exact values for equations `ax+by=cz`, with reported OEIS absences for ten sequences.

**Home:** `jaredwilder/rado-equation-avoidance-atlas`.

## 2.6 Conference-switching impossibility theorem — READY note

For symmetric conference-matrix switching, the book-avoidance inequalities force

`C_ij(s_i+s_j)<=0`

for all distinct pairs, while `C^2=(N-1)I` implies a strictly positive row sum expression, contradiction.

This eliminates the entire switched symmetric-conference construction class for the stated Ramsey-book target.

**Homes:** `ramsey-construction-class-eliminations`, `combinatorial-records`.

## 2.7 Erdős #598 exact finite polychromatic values — MINE

Recovered exact values:

- `L(4,3,2)=2`, maximum colors 3;
- `L(5,3,2)=4`, maximum colors 2;
- `L(6,4,2)=3`, maximum colors 5.

Extremizers are tied to `K4` matchings, `C5`/complement, and a `K6` one-factorization.

Specialist novelty status unresolved.

## 2.8 Ramsey R(5,5) cyclic witness structure — EXACT STRUCTURAL NOTE

For the 41-vertex circulant witness with connection set `±{1,2,3,5,7,10,13,15,16,17}`:

- multiplication by 9 maps the graph to its complement;
- `9^2=-1 mod 41`;
- `alpha=omega=4`;
- 410 edges, 1230 triangles, 1025 `K4`s and 1025 independent 4-sets;
- `chi=11`, and `chi(G-v)=10` for every vertex;
- automorphism group `D_41` of order 82;
- clique polynomial `1+41x+410x^2+1230x^3+1025x^4`.

Known Ramsey bound, potential novelty only in the complete structural analysis.

---

# 3. Clean structural assets below the front board

## Erdős #973

Exact `n=2` minimax value `(sqrt(5)-1)/2`. Parent later solved negatively elsewhere; finite golden-ratio extremum remains clean.

## Erdős #289

All-prime p-adic reciprocal-sum obstruction generalizing the familiar `p=2` parity slice. Needs formalization and priority court.

## Erdős #885

Factor-difference / square duality:

`d in D(N) iff exists s : s^2=d^2+4N`.

Sorry-free Lean theorem exists. Structural coordinate change, not parent close.

## Erdős #477

Scope correction: no unique direct-sum complement exists for **every quadratic integer polynomial** `ak^2+bk+c`, `a!=0`. Do not shrink this to the square case.

## Erdős #400

Recovered universal package includes logarithmic upper control and factorial-subsequence lower witness `g_k(m!) >= m+k-3`. Child-theorem program, not front board yet.

## Erdős #479

For every `j>=0` and odd prime `p`, with `e=2^j`, `n=ep`, one has `n | (2^n-2^e)`. Clean infinite family.

## Erdős #700

For primes `p<q`, the estate proves `f(pq)=p` for the binomial-gcd extremal function. Clean child theorem; stronger 2026 parent progress exists.

## C(13,6,3) point-degree theorem

Any family of 6-subsets of a 13-point set covering every triple has every point in at least 8 blocks. The nominal 20-block hypothesis in the Lean theorem is unused.

## Greedy singleton-seed sum avoidance

Recovered candidate formula:

`A_k={n>=k : n mod (3k-1) in [k,2k-1]}`.

Checked for `k=1..10`, 300 terms each. Needs clean proof + literature/name search.

---

# 4. Proof-reconstruction queue

## Shifted Schur-type equation

Archive seam reports exact parity law for maximum subsets of `[1,n]` avoiding `x+y=z+c` with repeats allowed: `ceil(n/2)` for even `c`, `floor(n/2)` for odd `c`, beyond the small-`c` boundary.

**Status:** finite-pattern report only. Reconstruct universal proof or find first counterexample before promotion.

## Rado-family collapse

Archive seam reports that avoiding

`x1+k x2=x3`

and avoiding

`x1+...+x_{k+1}=x_{k+2}`

appear to have identical extremal function

`n-floor(n/(k+1))`

for tested `k=1..4`, `n=6..30`.

**Status:** finite-pattern discovery. Prove or kill universally before literature court.

## Erdős #238

Statement reconciliation required. A restricted small-`c1` theorem is classical; one finite window-cover lemma survives with a `k-1` sharpening. Do not promote the disputed stronger slice without re-freezing definitions.

---

# 5. RH / Weil auxiliary novelty court — separate from RH claims

**Hard boundary:** RH remains open. No off-critical zeta zero was found.

Surviving auxiliary objects include:

- exact isolated-quartet eigenpair for `K_a(u,v)=2(cosh(a(u-v))-1)` on `[-L,L]`;
- repaired compact-jet invisibility theorem using an entire even polynomial deformation inserting a symmetric quartet while converging to 1 on every fixed compact finite jet;
- no-uniform-cluster-floor theorem: in the unrestricted finite partner-quartet family, the ratio of the most negative cluster eigenvalue to the isolated eigenvalue has infimum zero, even with distinct unit-multiplicity parameters if arbitrarily close parameters are allowed;
- live Epoch 40 adaptive theorem and generic score-shell masking no-go;
- live Epoch 41 center-independent Blaschke separation product.

These are method-obstruction/local-spectral candidates only. They must never be advertised as an RH proof or disproof.

See `CROSS_SESSION_MERGE_2026-09-14.md` for exact cross-session state and commit identifiers.

---

# 6. Known / independent rediscovery controls

Correct mathematics with collided/subsumed novelty remains in the estate. Important controls include:

- Erdős #655 literal negative close via regular polygons — exact prior match to Zach Hunter;
- #25 summable congruence sieve;
- #376 Kummer carry criterion;
- #456 endpoint family;
- #700 semiprime/valuation slices;
- #849 exact endpoints through `t=4` (`120`, `3003`);
- #887 short-interval divisor construction;
- #1049 Lambert identity;
- #197 finite 3-AP-free permutation ordering;
- maximal Sidon `Omega(N^{1/3})` blocker bound;
- pure four-topology cyclomatic-rank-three classification.

These are **positive controls for theorem recovery**, not failures.

---

# 7. Permanent quarantine / regression set

Do not resurrect as closes without repairing the broken edge:

- #539 false identity;
- #101 witness violates no-five-collinear hypothesis;
- #193 target-version/infinite-range mismatch;
- #410 divisor-sum semantic mismatch;
- #510 zero entered weakened domain;
- #829 invalid Mahler-style branch;
- #1203 universal claim refuted by later explicit value;
- #1210 false shifted-coprimality step;
- #683 finite contract versus global extrapolation;
- #891 `Omega` multiplicity variant confused with live `omega` problem;
- #943 multiplicative factorization substituted for additive convolution;
- #701 finite certificates survive, universal one-star claim false.

Quarantine is preserved as regression data, never silently deleted.

---

# 8. Search surfaces already drained

Do not spend a new pass merely repeating these without an orthogonal lens:

- 617/617 latest-local `PROVED` states headline/scope-reviewed;
- 282/282 omitted-family states across 97 families;
- 335/335 represented-family upgrade states;
- Pass-4 556-object formalizer residue classified;
- A-proved atlas broad headline/scope surface drained;
- nested/archive seam partially mined;
- #738 exact theorem bank publicly reconstructed through Round 40.

The estate is still unsaturated because deeper passes continue to change the board, but future work must be **set-difference / scope / equality-case / bridge / proof-upgrade mining**, not raw repetition.

---

# 9. Publication queue

1. Seal Erdős #902 `f(4)>=49`.
2. Submit integral-octagon `ḋ(2,8)>30000` paper.
3. Graham `Z_37/Z_41` complete sequenceability paper.
4. Erdős–Straus AP/GP classification paper.
5. CH cubic-`C4` theorem + formal seal.
6. Signed-sparse encoding `Theta_s(m^s)` paper.
7. Erdős #949 full finite-sums package.
8. Erdős #595 continuum-barrier formal paper.
9. SQS(20) completion/rigidity/trade paper.
10. General covering-design plateau-rigidity paper.
11. Turán (3,4) excitation/frustration + extension/deletion calculus paper.
12. #890 ↔ #1093 bridge.
13. Diagonal Ramsey corridor + approximate-supermultiplicativity note.
14. #738 sharp type-uniform tensor obstruction specialist court / paper if priority survives.
15. Fiber-coherence exact K4-free relation/CSP realization hostile prior-art court.
16. #486 summable forbidden-mass theorem.
17. Finite-field exact classifications.
18. Pascal/Rado exact-extremal package.
19. #1061 primitive-ray construction.
20. Conference-switching impossibility note.

Proof-reconstruction queue:

- shifted `x+y=z+c` parity law;
- Rado-family extremal collapse;
- greedy singleton-seed periodicity formula;
- `R(5,5)` cyclic witness structural note if literature comparison leaves a delta.

---

# 10. Next-pass contract

A new novelty pass should search specifically for:

- theorem scope wider than the repo/problem title;
- equality cases of standard inequalities;
- exact equivalences hiding under “reduction”;
- conditional implications that are clean standalone theorems;
- finite empirical laws one proof away from all-parameter form;
- formal theorems with unused hypotheses or stronger scope than their names;
- cross-repository fusions;
- archive results not routed to subject homes;
- independent rediscoveries where proof/formalization/range/structure is still new.

A pass ends by updating this ledger, `BOARD.md`, `STATE.json`, and the continuation protocol when necessary.

**Saturation verdict: NO.**
