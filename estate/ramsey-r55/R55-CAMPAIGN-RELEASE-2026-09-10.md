# R(5,5) Campaign Release — Exact Witnesses, Extension Obstructions, and a Two-Hole Machine Interface

**Author:** Jared Wilder  
**Public release:** 2026-09-10

## Current literature boundary first

This campaign does **not** improve the current published numerical bounds on the diagonal Ramsey number R(5,5).

As of this release, the public literature gives

\[
\boxed{43\le R(5,5)\le46.}
\]

The upper bound `R(5,5) <= 46` was published by Angeltveit and McKay in 2026. The lower bound 43 comes from an explicit 42-vertex colouring in the existing literature.

Therefore this estate's independently replayed 40-vertex witness is valid but **sub-frontier**. The mathematical value of the campaign lies elsewhere: exact extension theorems, certified inextensibility of specific witnesses, repair-vs-extension geometry, reproducible finite witness objects, and an explicit machine interface for the 42/43 boundary.

## Complete estate ledger

The reconstructed campaign contains **117 objects**, now published in three deterministic ledgers:

- `OBJECT-LEDGER-PART-1.md`
- `OBJECT-LEDGER-PART-2.md`
- `OBJECT-LEDGER-PART-3.md`

The ledgers preserve the original theorem/world-result/route/retraction/defect classifications rather than silently keeping only successes.

---

# 1. Exact witness family recovered and replayed

The estate contains independently replayed red/blue K5-free colourings on:

- 30 vertices;
- 31 vertices;
- 34 vertices;
- 36 vertices from seeded repair;
- a structurally different 36-vertex Cayley construction over `Z_6 x Z_6`;
- 40 vertices.

The 40-vertex witness has red/blue K4 counts

\[
921/893.
\]

Again, it is not a record: a 42-vertex lower-bound witness is already known publicly.

## Exact untouched extension 30 -> 31

The preserved 31-vertex object restricts **exactly** to the 30-vertex object on all 435 old edges.

The new vertex has red neighbourhood

```text
[0,1,7,8,10,11,12,15,17,19,21,22,27,28].
```

Thus this is a genuine one-vertex extension, not a global repair disguised as an extension.

---

# 2. One-vertex extension theorem

Let `G` be a red/blue colouring of `K_n` with no monochromatic `K_5`. Add one new vertex `v`, and let `A` be its red neighbourhood in the old vertex set.

Then the extended colouring is monochromatic-K5-free **iff**

1. the red graph induced by `A` contains no red `K_4`; and
2. the blue graph induced by `V(G)\A` contains no blue `K_4`.

The proof is exact: any new monochromatic `K_5` must contain `v`; deleting `v` leaves the corresponding monochromatic `K_4` in its same-colour neighbourhood.

This gives an exact SAT formulation using only `n` Boolean variables and one clause per red/blue `K_4` in the base graph.

## Certified one-vertex inextensibility

Under this exact criterion, the estate records UNSAT for the following specific bases:

- the 34-vertex witness: red/blue K4 counts `414/459`;
- the seeded 36-vertex witness: `540/583`;
- the Cayley 36-vertex witness: `612/360`;
- the 40-vertex witness: `921/893`;
- the 31-vertex witness: `281/283`.

The 30-vertex witness is different: it **is** one-vertex extendable, and the resulting 31-vertex object is explicitly preserved.

This refuted an earlier campaign overgeneralization that pure one-vertex extension was globally dead.

---

# 3. Two-vertex extension theorem

Let `u,v` be two new vertices. Let `A,B` be their red neighbourhoods in the base graph.

The extension is K5-free iff the one-vertex K4 constraints hold separately for `A` and `B`, and additionally:

- if `uv` is red, the red graph on `A∩B` contains no red triangle;
- if `uv` is blue, the blue graph on `(V\A)∩(V\B)` contains no blue triangle.

This is again exact: a monochromatic K5 containing both new vertices uses a same-colour triangle in their common same-colour base neighbourhood.

For the 30-vertex base, the preserved exact two-vertex encoding has

- 61 Boolean variables;
- 1,898 clauses;
- 466 red-triangle and 458 blue-triangle source obstructions;
- result: **UNSAT**.

Thus that particular base has untouched-extension depth exactly one.

---

# 4. General k-vertex extension schema

The estate derives the natural generalization.

For a fixed K5-free base graph and `k` new vertices, the extension is K5-free iff, for every monochromatic `j`-clique among the new vertices,

\[
1\le j\le\min(k,5),
\]

the common same-colour neighbourhood in the base contains no same-colour

\[
K_{5-j}.
\]

Thus the obstruction order descends:

- one new vertex -> base `K_4` obstructions;
- two -> `K_4` plus `K_3`;
- three -> down through `K_2`;
- and so on.

For fixed `k`, this yields a compact exact SAT encoding with `kn + binom(k,2)` edge-colour variables and polynomial base-side obstruction enumeration.

---

# 5. Extension depth as a structural invariant

Define the untouched extension depth

\[
e(G)=\max\{k:\text{k new vertices can be appended without changing old edges while remaining K5-free}\}.
\]

For the tested estate objects:

\[
e(G_{30})=1,
\]

while

\[
e(G_{31})=e(G_{34})=e(G_{36}^{seed})=e(G_{36}^{Cayley})=e(G_{40})=0.
\]

This is an object-specific invariant, not a theorem about all Ramsey witnesses of those orders.

---

# 6. Repair is not extension

The campaign's successful larger witnesses were obtained by **global repair**, not by preserving the old graph.

Byte-level restriction comparison gives:

- `30 -> 31`: `0 / 435` old edges changed = **0.00%**;
- `34 -> 36`: `299 / 561` old edges changed = **53.30%**;
- `36 -> 40`: `318 / 630` old edges changed = **50.48%**.

This kills a misleading explanation from the live campaign: the successful seeded search was not “adding vertices to a nearly finished witness.” It used an old witness as a warm start and rewrote roughly half of the inherited graph.

The resulting search lesson is structural:

> K5 defect count alone does not describe the chamber. Exact extension state/inextensibility is an additional coordinate of the search landscape.

---

# 7. Cayley witness and the abelian-order-42 wall

The campaign independently found a K5-free 36-vertex Cayley colouring over `Z_6 x Z_6` after 10,797 sampled symmetric connection sets.

For order 42, however, every finite abelian group is cyclic because

\[
42=2\cdot3\cdot7
\]

is squarefree and the Sylow factors are cyclic of pairwise coprime orders. Hence every abelian Cayley graph on 42 vertices is a circulant.

Therefore moving from cyclic to merely abelian Cayley search gives **no new order-42 family**. A genuinely new Cayley route at 42 must use a nonabelian group.

---

# 8. Exact 42/43 CNF interface

The estate preserves exact from-definition DIMACS interfaces:

## n = 42

```text
p cnf 861 1701336
```

- variables: 861
- clauses: 1,701,336
- LF-normalized logical-clause SHA-256:
  `fb5ee4fb6c3981aa87c72a5aa73a4f23cc6fbedc549a997e0cbfead50b48e14c`
- whole-file SHA-256:
  `2058a54abba4325ec0d61bb6812c3c185fff408e5edda4ceb847316e50b07e4f`

SAT is equivalent to existence of a 42-vertex K5-free red/blue colouring. Such an object is already known from the literature; the estate did not itself rediscover it in the captured campaign.

## n = 43

```text
p cnf 903 1925196
```

- variables: 903
- clauses: 1,925,196
- logical-clause SHA-256:
  `9cb36cfd39aebd5a37a1c2115efa20f76332a55ab4c224da2ac7ccee249882be`
- whole-file SHA-256:
  `25e64fe3dbe792dc3fe4ee54d2d7a08c2fbc705a119928bfbb3cd73c163965aa`

UNSAT would establish `R(5,5) <= 43`. Combined with the known lower bound, that would determine `R(5,5)=43`.

**No UNSAT certificate is present in this estate.** Current published upper bound is 46.

---

# 9. Lean two-hole close interface

The preserved `R55.lean` defines the colouring model, monochromatic K5 predicate, lower and upper certificates, and a composition theorem `close_CC55`.

The source file typechecked with exactly **two explicit `sorry` sites**:

- `gap1_at_42`: the 42-vertex lower certificate;
- `gap2_at_43`: the 43-vertex universal upper certificate.

The composition theorem itself merely says those two statements would imply the desired exact close.

A `sorry` is a hole. Therefore the Lean interface proves **nothing new about R(5,5)** by itself.

It is useful because it freezes the exact two remaining formal obligations in that attempted close architecture.

---

# 10. Retractions and repairs preserved

The campaign explicitly corrected several of its own statements:

- the live lower floors 35 and then 37 were retired when stronger in-session witnesses appeared; they remained true, not refuted;
- the claim that pure one-vertex extension was dead was refuted by the exact 30->31 extension;
- a claimed exhaustive family scope was false because not all held witness objects had actually been tested;
- the explanation that seeded extension worked by staying near the old witness was refuted by the restriction-distance measurements;
- multiple budget-exhaustion nulls were reclassified as `NO_VERDICT`, not mathematical negatives.

These repairs are part of the public release because the difference between a search failure and an UNSAT theorem is mathematically load-bearing.

---

# 11. What is genuinely reusable

The durable mathematical/research assets are:

1. exact one-, two-, and general k-new-vertex extension criteria;
2. compact SAT encodings for untouched extension;
3. object-specific extension depth;
4. exact inextensibility certificates for several witness graphs;
5. the distinction between extension and global repair, quantitatively measured;
6. two independent 36-vertex construction styles;
7. a frozen two-hole 42/43 machine interface with exact CNF hashes;
8. a complete 117-object provenance/retraction ledger.

## Nonclaims

- This campaign does not improve the current `43 <= R(5,5) <= 46` record.
- The 40-vertex witness is not novel as a Ramsey lower bound.
- The 43-vertex CNF has not been proved UNSAT here.
- The Lean two-hole interface is not a proof because both load-bearing obligations are explicitly unproved.
- Search-budget failures are not impossibility theorems.

The value of the release is the exact structural and computational attack surface, not a false numerical headline.