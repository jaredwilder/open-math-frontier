# RH epoch 23 ledger

Rounds 1-28 (absolute MSL rounds 598-625). Written from the round record.

## Headline: the epoch KILLED its own predecessor's route

Epoch 22 spent fifty rounds certifying a criterion on the determinant lane. Epoch 23 tested,
in one round, whether that criterion is strong enough to imply RH. **It is not.**

`rh-first-rung/criterion_is_not_sufficient.py`: 1,686 of 3,059 constructed polynomials with
a provably non-real conjugate pair satisfy the criterion.
`rh-first-rung/criterion_kill_audit.py`: the kill survives at every order the degree allows,
with interior shifts, in both entry forms - 1,445 of 2,284, identically in both.

Branch C is **closed as dead**. Five further candidate criteria were then screened *before*
any proof was invested (the law this taught): plain Newton admits 99.9% of the non-real-rooted
family, sharp Newton 18.8%, Hankel-depth-3 94.0%, and the three strongest admit the identical
169 objects - stacking adds nothing. The lane's whole coefficient-inequality strategy is
structurally incapable of sufficiency.

## Branch A: from nothing to one established quantity

Branch A (de Bruijn-Newman heat flow) is the only lane whose criterion is equivalent to RH by
construction, so no sufficiency screen can kill it. It had no instrument at all.

What the epoch built, each step forced by the failure of the last:

1. The certified epoch-22 machinery **relaxes** into the easy regime of the flow - it carries
   no information at the hard limit.
2. Spacing statistics are dead: the gaps do not move together (3 shrink, 4 grow monotonically),
   so no scalar spacing quantity has a direction.
3. The **pair energy** `E(t) = sum 1/(z_i - z_j)^2` does have one. It rises monotonically as
   the deformation decreases, at two independent truncations, across the full parameter range,
   with its dominant term strictly interior.
4. Getting that answer took an instrument: adaptive quadrature (too slow), a fixed-node rule
   (fast, but with an oscillation ceiling that produced ~600 spurious zeros when pushed), and
   finally the **flat-cost moment series** whose cost is independent of the argument.
5. The two instruments disagreed. The moments were adjudicated against a third method and
   **exonerated** (agreement to 50 digits). The real cause was the alternating series'
   cancellation, and a **precision rule** was derived: digits lost 1.5 / 6.7 / 13.2 / 21.5 at
   arguments 20 / 40 / 60 / 85, term counts 26 / 45 / 66 / 70.
6. A run **sized in advance by that rule** (70 digits, 80 terms) completed all three parameters
   and settled it: 7 zeros each, dominant pair (4,5) - interior - and both truncations rising
   monotonically through 0.09964 -> 0.10242 and 0.13037 -> 0.13302.

Artifacts: `branchA_energy_sized.py` / `.out.txt`, `branchA_precision_rule.py`,
`branchA_moment_adjudication.py`.

## Kernel record

Receipts 081-086. Including:
- `rh-necessary-not-sufficient-081` - **empty axiom footprint**, the first in this campaign.
  One object satisfying a criterion while failing the property refutes the implication. This is
  the logic that killed branch C, as a proof term.
- `rh-gap-rate-bound-083`, `rh-energy-no-collision-084`, `rh-monotone-range-ceiling-086` - the
  three bound *shapes* branch A would consume.
- `rh-sum-dominates-term-085` - a finite sum of nonnegatives dominates each term, over an
  arbitrary Finset. This repaired a seal declared thin at the moment it passed.

## Self-convictions and retractions

- **SC15**: certified a criterion for fifty rounds before testing its sufficiency. The test took
  one round. *Test sufficiency against a constructed family the target is false for, first.*
- **SC16**: nested a root finder inside an expensive quadrature inside a parameter scan without
  measuring one evaluation. Remedy applied the next round; it produced the quantity the branch
  had been missing.
- **RR47**: a "tightening gap" was a minimum over two components moving in opposite directions.
- **RR48 / RR50**: the edge-domination discharge was retracted on a cheaper instrument's output,
  then reinstated once that instrument was shown to be past the precision wall. Both moves were
  correct on the information available.
- **C8, C9, C10**: a vacuous hunt, a definitional equivalence reported as a discovery, and a
  verdict line written before its own numbers.

## Round 34 addendum: the energy finding is rigorously validated

The energy finding rested on zeros of a *truncated* series, and the precision rule bounds
cancellation only, not truncation. Two attempts at a truncation bound failed and were filed as
failures: a crude uniform bound (overestimates the moments by ~108 orders) and a geometric
bound (rests on decreasing moment ratios - the ratios *rise*, 0.0116 -> 0.533, and the probe's
own test said so; SC17).

`branchA_truncation_envelope.py` closes it. A 64-piece rigorous envelope on the moments -
hypothesis-free, each piece bounded by the kernel's maximum there - cuts the looseness from
~1e48 to 4.3e4 and validates the whole window:

    z        zero shift <=        verdict
    28.27    1.34e-88             negligible
    40       4.21e-63             negligible
    55       1.26e-38             negligible
    70       2.12e-19             negligible
    85       0.0020               usable (spacing ~6)

Every zero the energy finding uses is therefore located to well inside the spectrum's spacing,
against the *untruncated* object. The displacement inference itself is kernel-sealed
(`rh-zero-displacement-088`).

## Rounds 35-49: the energy killed, the Hermite route found and killed

**The energy is insufficient, and worse - anti-correlated.** A perturbation test (with the
merge *verified* by zero count before any number was read) showed the energy rising as a pair
approaches the line's edge - 0.132 -> 0.142 -> 0.247 -> 0.435 - and then *falling* to 0.051 once
the pair has left, below the unperturbed 0.132. On exact controls (`branchA_verified_controls.py`,
finite atomic kernels whose roots are solved exactly) the quantity reads **0.0** when all roots
are verified complex, against 1.46 and 5.93 when all are real. No ceiling on it can exclude
complex zeros. Kernel-sealed as the general fact: removing a positive term from a finite sum of
nonnegatives strictly lowers it (`rh-removal-lowers-sum-089`).

**The bench.** Finite atomic kernels give exact ground truth with no truncation and no
perturbation contamination - the instrument the campaign needed after four contaminated or
vacuous testing rounds. It screened four candidate functionals in one round: three killed by
overlap, and the one that separated perfectly was declared a **tautology** (it was the real-root
count itself). Kernel-sealed: a separator equivalent to a property adds nothing
(`rh-tautological-separator-090`, empty axiom footprint).

**The Hermite sequence** (`branchA_hermite_screen.py`) passes the bench: all minors positive
exactly on the all-real controls, on none of the complex ones, and its positive count is *not*
the real-root count - so it is sufficient, non-tautological, and computable from coefficients
alone, which is what branch A holds.

**And it is dead on the object** (`branchA_hermite_on_object.py`). Normalizing by the largest
root magnitude removes the numerical blow-up completely (minors from ~1e275 down to <63), and
reveals the real obstruction: every truncation of an entire function with infinitely many zeros
carries spurious complex roots - 2 to 4 real out of 34 at every degree - so its minors fail
regardless of what the object does. Kernel-sealed: a test constant across approximants
discriminates nothing (`rh-uninformative-test-091`, empty axiom footprint).

## Where this leaves the target

**OPEN.** Branch A holds one established quantity and three sealed bound shapes, and none of the
three numbers those shapes consume - a tail bound, a rate, a ceiling. Branch C is dead. Nothing
in this epoch proves RH or comes close to it.
