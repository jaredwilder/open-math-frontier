# False-Close Blacklist — Second-Pass Supplement

**Author:** Jared Wilder  
**Public release:** 2026-09-10

A second recovered blacklist contained additional poisoned routes and sharper falsifiers not present in the first public blacklist. This supplement preserves them without silently reconciling source-numbering conflicts.

## Erdős #260

**Poisoned claim:** a sparse-binary irrationality proof transfers directly to the source series.

**Killer:** the source contains terms of the form

\[
\frac{a_n}{2^{a_n}},
\]

so the numerator `a_n` creates binary carries. A proof for a pure indicator series `sum 2^{-a_n}` does not automatically transfer.

---

## Erdős #454

**Poisoned claim:** finite divisor-prefix results close or materially settle the target.

**Killer:** cross-problem contamination. The actual source target is a prime-index sum problem; the imported divisor-prefix statement is about the wrong mathematical object.

---

## Erdős #400

**Poisoned finite data:** `g_2(24)=2` and `g_2(11)=3`.

**Killer:** the exact values in the recovered audit are respectively

\[
g_2(24)=3,
\qquad
g_2(11)=2.
\]

Any argument depending on the stale values must be recomputed.

---

## Erdős #168

**Poisoned finite datum:** `F(42)=30`.

**Killer:** the recovered exact value is

\[
\boxed{F(42)=34.}
\]

---

## Erdős #1038

**Poisoned witness:**

\[
\frac{x^2-1}{2}
\]

was treated as an admissible monic polynomial witness.

**Killer:** its leading coefficient is `1/2`, so it is not monic and does not satisfy the source problem's normalization.

The valid endpoint quadratic witness is instead

\[
x^2-1,
\]

whose sublevel measure is `2sqrt2`.

---

## Erdős #1054 — sharper recovered counterinstance

The first blacklist already marks a universal finite-data formula as poisoned. The second blacklist gives a concrete source counterinstance:

for `p=11`,

\[
12=1+2+3+6,
\]

so under the campaign's exact `f` convention,

\[
\boxed{f(12)\le6,}
\]

contradicting the promoted formula `f(p+1)=p`.

---

## Erdős #1073 — sharper recovered modular falsifier

The first blacklist already rejects the claimed Wilson-style prime-power extension. The recovered compact falsifier is

\[
8!+1\equiv1\pmod9,
\]

so the asserted odd-prime-power congruence fails already modulo `3^2`.

---

## Sigma(6) numbering conflict

A second source blacklist indexes the poisoned statement

> `sigma(6)=6` is a fixed point

under **#412**, whereas the earlier recovered blacklist indexed the same mistake under **#410**.

The mathematical falsifier is unambiguous:

\[
\sigma(6)=12.
\]

The problem-number discrepancy is preserved rather than silently normalized; source-contract review is required before assigning the correction to one canonical problem ID.

---

## Policy

Blacklist the false **claim**, not every theorem on the same route. A corrected sublemma may remain useful even when the closure inference built on it is poisoned.