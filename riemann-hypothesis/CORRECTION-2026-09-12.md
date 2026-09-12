# Correction to the September 10 RH terminal asset bank

**Author:** Jared Wilder  
**Correction date:** 2026-09-12

The historical file `estate/RIEMANN-HYPOTHESIS-TERMINAL-ASSET-BANK-2026-09-10.md` described a coefficient route in which positivity of a hierarchy of **consecutive** Toeplitz minors was treated as a possible bridge to total positivity / `PF_infinity` and hence to an RH criterion.

That bridge is false in the required generality.

An exact counterexample is

`a=(1,0,0,0,0,1)`.

The tested consecutive minors are nonnegative, while the non-consecutive `2 x 2` minor on rows `{0,1}` and columns `{1,5}` is

`a1*a4-a5*a0=-1`.

Accordingly, the older document is retained only as a historical record of the state of the investigation on September 10. It must not be read as the current route status.

A later adversarial audit also refuted the separate Branch C candidate criterion directly: among `2284` explicitly non-real-rooted positive-coefficient objects tested at full available depth and interior shift, `1445` satisfy the square-free criterion and the same `1445` satisfy the original entry form.

**Current adjudication:** Branch C is dead as an RH route; RH remains open in this work. The theta-kernel interval certificates remain valid standalone mathematics and are separated from the failed implication.

See this directory's `README.md` for the current public status and the exact reproduction scripts.