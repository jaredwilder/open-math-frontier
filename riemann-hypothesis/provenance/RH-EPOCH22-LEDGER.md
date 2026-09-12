# RH epoch 22 ledger

Rounds 1-49 of epoch 22 (absolute MSL rounds 548-596). Branch C, the determinant / total-positivity lane. Written from the round record, not from memory.

## What the epoch did

Took the criterion from a two-dimensional lattice of determinant inequalities down to a single curvature estimate on the theta kernel, with every reduction step either kernel sealed or certified in exact rational arithmetic.

The chain, top to bottom:

1. Every lattice entry is equivalent to a square-free form. KERNEL SEALED.
2. The exponential makes every entry an exact equality, so it is the criterion's whole boundary surface, not merely an extremal point.
3. The entry factors into a shift piece and an order piece, exact reciprocals at the exponential, both strictly below their benchmark values for the real object at every entry measured. Either factor alone suffices.
4. The order arm is monotone in both indices with its maximum at the corner; the shift arm's maximum drifts off the corner. The order arm is the route.
5. The corner is a three-term inequality in the first three coefficients. It is exactly the epoch-21 statement `3 I_2^2 > I_0 I_4`; the two kernels differ by a scaling of the integration variable under which the corner ratio is invariant.
6. The shift monotonicity contains no determinants: it is exactly `s_{k+1}/s_k > (k+1)/(k+2)` where `s_k = 1 - a_{k-1}a_{k+1}/a_k^2`.
7. `s_k` splits exactly into an explicit factorial factor and the even moments' log-convexity ratio; the elementary route dies because the two are the same order.
8. That ratio is the variance of `log u` under the tilted measure.
9. The variance is controlled by the Laplace curvature at the tilted mode.
10. The requirement reduces to `(log Phi)'' <= 4 (log Phi)'`, an inequality about the kernel alone with no index, no mode, no tilt.

## Certified this epoch

- `certify_curvature.py` — curvature requirement in exact rational interval arithmetic.
- `crude_le_true.py` — reduction of the crude-to-true comparison to the index-free kernel inequality.
- `link5_truncation_confound.py` — attack on the campaign's own strict repair of link 5.

## What blocked the close at the end of epoch 22

The route's top link — implication from the criterion to the target — rested on a classical criterion the estate did not hold. A source request was filed rather than fabricating the statement or attribution.

**The target remained OPEN.**

## Round 50 addendum: the tail is certified

`certify_tail.py` closes the lower half's last opening in exact rational interval arithmetic:

    tail upper bound at u=0 : 1.101398903229127086e-03
    Phi(0) lower bound      : 0.444625572414765635
    CERTIFIED relative tail : 2.477138004562849053e-03   ( < 1/300 )

At that historical point the route's lower half was considered complete and the unsourced top implication remained the only named opening.

---

# RETRACTION, epoch 23 round 7 (absolute 604)

**The criterion this ledger certifies is NOT SUFFICIENT for the target. The route above cannot reach RH, and no further work on it will change that.**

`criterion_is_not_sufficient.py`: of 3,059 constructed polynomials carrying a provably non-real conjugate pair and nonnegative coefficients, **1,686 satisfy the criterion**.

`criterion_kill_audit.py` re-ran the test with every objection removed — the criterion demanded at every order the degree allows, shifts held interior, and both the square-free and original entry forms: **1,445 of 2,284 still satisfy it, identically in both forms.**

So the criterion is a necessary condition on the tested real-rooted sequences and is not sufficient for real-rootedness.

## What survives

- The exact reductions, obstructions and identities that are independently true.
- The exact rational certifications (`certify_curvature.py`, `certify_tail.py`, `crude_le_true.py`) for the conditions they actually certify.
- The epoch-21 corner certification.

## What is withdrawn

- The route's top link in all its forms.
- The source request as a route blocker: the deeper issue was mathematical insufficiency, not missing attribution.

## Methodological correction

The campaign certified a criterion's lower half across fifty rounds before testing whether the criterion was strong enough to imply the target. The one-round falsifier family should have been run first. Future criteria should be adversarially screened for sufficiency before proof effort is invested.