# Prime-Gap Admissibility Formalization Packet

**Author:** Jared Wilder  
**Public release:** 2026-09-10  
**Source campaign:** 2026-05-23, reconstructed and audited 2026-05-28

## What this is

This packet preserves the mathematically durable part of a long prime-gap / Cramér campaign:

- finite combinatorics of Hardy–Littlewood admissibility;
- a Lean-oriented inclusion–exclusion theorem chain;
- exact small-prime specializations;
- finite boundary witnesses;
- an empirical residue-analysis program whose substantive bias phenomena are explicitly placed against Lemke Oliver–Soundararajan (2016).

This is **not** a proof of Cramér's conjecture, a new asymptotic law for prime gaps, or a claim that observed finite-range saturation persists asymptotically.

## Core finite theorem

The campaign's central formal identity is

```text
admissibleCount p k
  = p^(k-1)
    - Σ_{t ⊆ nonzeroRes(p)} (-1)^|t| (p - |t|)^(k-1)
```

This expresses finite Hardy–Littlewood admissibility as an inclusion–exclusion count over the nonzero residue classes modulo `p`.

The formal development was organized through the chain

```text
PrimeGapInclusionExclusion
→ PrimeGapIEChain
→ PrimeGapAdmissibleClosedForm
→ PrimeGapHLBridge
→ PrimeGapMod2Exact
→ PrimeGapMod2General
→ PrimeGapMod3General
→ PrimeGapSurjectionBoundary
→ PrimeGapPermBoundary
```

The source campaign recorded all of these modules as compiling, but its final theorem/module totals were internally inconsistent. This public preservation therefore does **not** repeat the old aggregate theorem count as a certified statistic. The mathematical statements below are preserved individually.

## Exact specializations

The campaign records

\[
\boxed{\operatorname{admissibleCount}(2,k)=1}
\]

for all relevant `k`, and

\[
\boxed{\operatorname{admissibleCount}(3,k)=2^k-1}.
\]

At the first boundary `k=p`, the finite calculations give

\[
\operatorname{admissibleCount}(3,3)=7,
\]

\[
\operatorname{admissibleCount}(5,5)=601,
\]

and

\[
\operatorname{admissibleCount}(7,7)=116929.
\]

The corresponding covering counts in the campaign are

\[
2,\quad24,\quad720,
\]

matching

\[
2!,\quad4!,\quad6!.
\]

The campaign identified the general boundary statement

\[
\operatorname{coversCount}(p,p)=(p-1)!
\]

as the next theorem target via a bijection with permutations of the nonzero residues. **The audited source packet did not establish the general bijection, so this release does not mark it proved.**

## Primorial-aligned exact fractions

The finite admissibility machinery produced these exact fractions:

| constellation length | exact fraction |
|---:|---:|
| 3 | `7/36` |
| 4 | `5/72` |
| 5 | `18631/810000` |

For `k=3`, the `7/36` value was checked across several primorial moduli in the original campaign. Some of the small finite counts used `native_decide`; those should be read with their corresponding trust footprint rather than described as pure kernel reduction.

## Empirical residue program

The same campaign analyzed residue transitions across prime-gap data at multiple scales. The durable, safely stated outputs are:

- mod-30 reachable transition cells: `175 / 900`;
- exact structural impossible cells at small moduli;
- finite-scale residue dependence that survived sham controls and larger-substrate replication;
- an initially stronger one-step Markov framing was **killed** after order/BIC analysis;
- Lemke Oliver–Soundararajan (2016) was identified as the parent prior-art framework for substantive residue-bias phenomena.

The empirical program is therefore best viewed as a reproducible finite-scale measurement layer sitting on top of the formal admissibility lattice, not as a new asymptotic theorem.

## What is potentially distinctive

The defensible contribution is the combination of:

1. finite Hardy–Littlewood admissibility represented as a machine-checkable counting problem;
2. the general inclusion–exclusion closed form above;
3. exact mod-2 and mod-3 specializations;
4. explicit finite `k=p` boundary witnesses;
5. a documented empirical bridge from admissible residue cells to observed prime-gap transition support;
6. an audit trail that records where stronger statistical claims were demoted after prior-art and falsification checks.

Historical priority for any particular formula is **not adjudicated here**. A formal proof of a known finite identity is still useful; it should not be sold as mathematical novelty merely because it is formalized.

## Publication boundary

The old campaign contained finite-range fits of maximal prime gaps to `g/(log p)^2`, including saturation-style estimates below Cramér's constant. Those are interesting empirical measurements but not theorem-grade asymptotics and are deliberately not elevated in this release.

Likewise, the general permutation-boundary theorem remains open within this packet until its bijection is written and checked.

## Suggested next verification

- recover the actual `.lean` source files named above;
- compile each against a pinned Lean/Mathlib version;
- count declarations from the source rather than prose inventories;
- run `#print axioms` per exported theorem;
- separate `native_decide` finite witnesses from kernel-reduced universal theorems;
- publish the general `coversCount(p,p)=(p-1)!` statement only after the bijection is complete.

This file is a public preservation of the mathematical result graph, with the missing verification steps stated rather than silently promoted.
