# LRC(13) / Fourteen-Runner Wall — Master Mathematical Release

**Author:** Jared Wilder  
**Campaign date:** 2026-08-07  
**Public release:** 2026-09-10

## Court verdict

**The full Lonely Runner Conjecture for 13 effective speeds / 14 total runners was NOT proved in this campaign.**

The session produced a substantial reference-safe theorem estate, one large invalid branch that was explicitly retracted, multiple exact finite/computational certificates, and a terminal normal form for any hypothetical counterexample.

The strongest closed subproblem in the archived campaign is the **large-prime canonical k=13 residue class for primes p>2366**, via a repaired mod-13 reduction, exact parity certificates and 2-adic descent.

This release preserves LIVE theorems, known inputs, abstract mathematical gold, retractions, negative results, and open obligations separately.

---

# I. Normalization and covering language

A genuinely new 13-effective-speed counterexample may be normalized to distinct positive integer speeds

\[
1\le u_1<\cdots<u_{13},\qquad \gcd(u_1,\ldots,u_{13})=1.
\]

At threshold `1/14`, put

\[
B_i=\{t\in\mathbb T:\|u_it\|<1/14\}.
\]

A counterexample is exactly

\[
\boxed{\mathbb T=\bigcup_{i=1}^{13}B_i},
\]

and every `B_i` has Haar measure `1/7`.

## Deleted-Runner Trap

For

\[
W_j=\{t:\|u_it\|\ge1/13\ \forall i\ne j\},
\]

the known 12-speed theorem gives `W_j≠∅`. A 13-speed counterexample forces

\[
\boxed{W_j\subseteq\{t:\|u_jt\|<1/14\}}.
\]

Therefore finding one `t∈W_j` with `||u_jt||≥1/14` closes that tuple.

## Pair-overlap budget

If `N(t)=Σ_i 1_{B_i}(t)`, then `N≥1` and `∫N=13/7`. Hence

\[
\boxed{\sum_{i<j}\mu(B_i\cap B_j)\ge6/7.}
\]

This is true but was strategically demoted: pair overlap alone is too diffuse.

---

# II. Divisibility and probe-capacity theorems

## Mandatory divisor witness

For every integer

\[
q=2,3,\ldots,14,
\]

some normalized speed is divisible by `q`.

## Conditional maximum-anchor resonant probe theorem

If the maximum speed is `M=qa`, it is the unique multiple of `q`, and `3≤q≤14`, then the probe family

\[
t_{m,\sigma}=m/q+\sigma/(14M)
\]

makes the anchor exactly `1/14` from an integer. A nonmultiple `v<M` can kill at most two probes, and positive capacity requires

\[
\boxed{v>\frac{14-q}{q}M},\qquad \gcd(v,q)=1.
\]

Consequences include impossibility of a unique maximal 14-multiple and, for `q=3,...,7`, impossibility of a unique maximal q-multiple in this branch.

## Prime divisibility multiplicity theorem

Let

\[
h_p=\#\{i:p\mid u_i\}.
\]

For every prime `p`, the campaign derives

\[
\boxed{p\le(13-h_p)\left\lceil p/7\right\rceil.}
\]

In particular

\[
h_2\le11,
\quad h_3\le10,
\quad h_5\le8,
\quad h_7\le6,
\quad h_{11}\le7,
\quad h_{13}\le6.
\]

Together with the mandatory 13-divisor witness,

\[
\boxed{1\le h_{13}\le6.}
\]

For all primes, further consequences recorded in the late campaign include:

- `h_p≥12`: impossible;
- `h_p≥11`: only `p=2`;
- `h_p≥10` or `9`: only `p∈{2,3}`;
- `h_p≥8`: only `p∈{2,3,5}`;
- `h_p≥7`: only `p∈{2,3,5,11,17,23,29}`;
- every prime `p≥31` divides at most six speeds.

## Exact prime-probe law

For prime `7<p≤13`, a nonmultiple `v` has probe capacity

\[
\boxed{N_{p,v}(\tau)=2-\mathbf1_{\{\|v\tau\|\le(14-p)/14\}}.}
\]

Thus at `p=13`, there is one bad slot iff `||vτ||≤1/14`, otherwise two; at `p=11`, one iff `||vτ||≤3/14`.

## Eleven-resonance saturation

If `h_11=7`, then after making the seven compressed multiples safe, at least five of the six outsiders obey

\[
\boxed{\|v\tau\|>3/14.}
\]

## GCD-sensitive composite capacity

For any modulus `q`, outsider `v`, put

\[
d=\gcd(v,q),\qquad Q=q/d.
\]

Then

\[
\boxed{N_{q,v}\le d\left\lceil Q/7\right\rceil
=\gcd(v,q)\left\lceil\frac q{7\gcd(v,q)}\right\rceil.}
\]

Hence every counterexample satisfies the all-modulus inequality

\[
\boxed{q\le\sum_{q\nmid v}\gcd(v,q)
\left\lceil\frac q{7\gcd(v,q)}\right\rceil.}
\]

---

# III. Exact 13-residue saturation geometry

For an outsider `v`, phase `τ`, write

\[
v\tau=n+\beta,\quad0\le\beta<1,
\qquad r=v\pmod{13}\ne0.
\]

At probes

\[
t_m=(m+\tau)/13,
\]

only residues satisfying

\[
rm+n\equiv0,-1\pmod{13}
\]

can be bad. Therefore

\[
\boxed{|S_v(\tau)|=2-\mathbf1_{\{\|v\tau\|\le1/14\}}.}
\]

When two slots occur,

\[
\boxed{S_v(\tau)=\{-r^{-1}n,-r^{-1}(n+1)\}\pmod{13},}
\]

with fixed chord displacement

\[
\boxed{-v^{-1}\pmod{13}.}
\]

## Private-Probe theorem

In the extremal `h_13=6` branch, every outsider has a phase/probe at which it alone covers that probe among the outsiders. This does **not** imply the runner is necessarily in one-slot mode there.

## Universal resonance normal form

For `1≤h=h_13≤6`, write the 13-divisible speeds as `13a_i` and put

\[
W_h=\{\tau:\|a_i\tau\|\ge1/14\ \forall i\}.
\]

Then

\[
\boxed{\mu(W_h)\ge(7-h)/7.}
\]

Every 13-divisible speed is safe on all lifted probes, and if

\[
Z_h(\tau)=\#\{v:\|v\tau\|\le1/14\},
\]

coverage forces

\[
\boxed{Z_h(\tau)\le13-2h.}
\]

## Extremal `h_13=6` saturation

For

\[
W=W_6,
\]

one has `μ(W)≥1/7` and `Z(τ)≤1`. Therefore every phase of `W` is one of exactly two incidence shapes:

\[
\boxed{2+2+2+2+2+2+1}
\]

with no overlap, or

\[
\boxed{2+2+2+2+2+2+2}
\]

with exactly one doubled probe.

## Strict witness-measure theorem

If `M=max_i|a_i|`, then more sharply

\[
\boxed{\mu(W_h)\ge\frac{7-h}{7}+\frac{h-1}{7M}.}
\]

In particular `μ(W_6)>1/7` for every concrete finite tuple.

## Forced local handoff

Inside the interior of `W`, at a generic event where exactly one outsider changes slot multiplicity, the disappearing/appearing slot is forced to be the unique doubled probe on the appropriate side of the transition. This is a **local/generic law only**; no global winding theorem was proved.

## Internal private witnesses

Deleting one internal speed `13a_j` and applying the 12-speed theorem yields a phase `τ_j` with

\[
\boxed{\|a_j\tau_j\|<1/14},
\]

while for every other internal speed

\[
\boxed{\|a_i\tau_j\|\ge1/13.}
\]

Thus every internal bad set is essential.

## Exact partition polynomial

In an `h_13=6` phase with one singleton outsider, exact partition of all thirteen residues implies

\[
\boxed{
\prod_{j=1}^{6}(r_jX+n_j)(r_jX+n_j+1)
(r_7X+n_7+\delta)=C(X^{13}-X)
}
\]

in `F_13[X]`.

This is a correct finite algebraic encoding, not a contradiction by itself.

---

# IV. Exact harmonic correlation formulas

For `g=gcd(a,v)`, `A=a/g`, `V=v/g`, the mixed-threshold intersection satisfies

\[
\mu(B_a(1/13)\cap B_v(1/14))
=
\frac2{91}+\kappa(A,V),
\]

where

\[
\boxed{
\kappa(A,V)=
\frac{B_2(\{V/13-A/14\})-B_2(\{V/13+A/14\})}{AV}.}
\]

The campaign records a complete finite sign law according to `A mod 14` and `V mod 13`, verified by a companion checker. Both signs occur.

For equal `1/14` thresholds,

\[
\boxed{
\mu(B_a\cap B_v)=
\frac1{49}+
\frac{B_2(\{(V-A)/14\})-B_2(\{(V+A)/14\})}{AV}.}
\]

For the 42 internal–outsider pairs in the `6×7` branch, the independent baseline is exactly `6/7`. Writing the total correction as `K_14`,

\[
\int XZ=6/7+K_{14},
\]

and saturation gives

\[
\boxed{\mu(W)\ge1/7-K_{14}.}
\]

No universal favorable sign for `K_14` was proved.

---

# V. Late-game analytic and certified results

## Periodic bad-set discrepancy

For

\[
B_s=\{t:\|st\|<1/14\}
\]

and an interval `I` of length `L`,

\[
\boxed{|B_s\cap I|\le L/7+6/(49s).}
\]

At general threshold `λ<1/2`, the discrepancy term is

\[
\boxed{2\lambda(1-2\lambda)/s.}
\]

## Dominant Block Transfer theorem

For `k` effective speeds at threshold `1/(k+1)`, assuming LRC is known for the lower `k-r` speeds, let the lower block be bounded by `V` and the top `r` speeds be at least `U`, with `1≤r<(k+1)/2`. Then

\[
\boxed{
\frac UV>
\frac{(k-1)(k-r+1)}{k+1-2r}
\Longrightarrow LRC(k).}
\]

For `k=13`, every counterexample satisfies the recorded dominant-gap ladder

\[
\boxed{
\frac{u_{13}}{u_{12}}<13,
\quad
\frac{u_{12}}{u_{11}}\le72/5,
\quad
\frac{u_{11}}{u_{10}}\le33/2,
\quad
\frac{u_{10}}{u_9}\le20,
\quad
\frac{u_9}{u_8}\le27,
\quad
\frac{u_8}{u_7}\le48.}
\]

## Finite-volume bound and seventh gap

The campaign imports/uses the finite gcd-volume bound

\[
C=91^{12}=322475487413604782665681.
\]

This yields a quantitative slack

\[
\boxed{1/14-\lambda\ge1/(28C)}
\]

and the recorded seventh-gap bound

\[
\boxed{u_7/u_6<12C.}
\]

In the 2-dissociated lower-six branch this improves to `u_7/u_6<9C`.

## Every 12-deletion is primitive

No prime can divide any twelve speeds, hence

\[
\boxed{\gcd(u_1,\ldots,\widehat{u_j},\ldots,u_{13})=1\qquad\forall j.}
\]

## Strict Deletion Principle

Assume `LRC(k-1)`. For every k-speed tuple `V`, there exists a deletion with

\[
\boxed{\operatorname{ML}(V\setminus\{v_j\})>1/k.}
\]

For `k=13`, every hypothetical counterexample therefore contains a primitive, non-tight 12-speed deletion.

## Robust private deletion interval

For the strict deletion there is an open interval `I` on which

\[
\|u_jt\|<1/14,
\qquad
\|u_it\|>1/13\quad(i\ne j),
\]

with certified length

\[
\boxed{|I|\ge1/(13C^2).}
\]

## Arbitrary-denominator private witness

With

\[
D_0=13C^2
=1351875719774345695830656516373849784810797518893,
\]

one fixed index `j` has the property that for **every integer `d>D_0`** there exists `a∈Z` with

\[
\boxed{
\left\|\frac{au_j}{d}\right\|<1/14,
\qquad
\left\|\frac{au_i}{d}\right\|>1/13\ (i\ne j).}
\]

Thus the private witness appears on every sufficiently fine denominator grid.

## Quantitative singleton/private-witness mass

Let

\[
N(t)=\#\{i:\|u_it\|\le1/13\}.
\]

For a counterexample, `N≥1`, `∫N=2`, and near zero `N=13`. Balancing positive and negative parts gives

\[
\boxed{\mu\{t:N(t)=1\}\ge\frac{22}{13u_{13}}.}
\]

At a singleton time the unique `1/13`-bad runner must be `1/14`-bad. Therefore some fixed runner has private witness mass at least

\[
\boxed{22/(169u_{13}).}
\]

## Strict Loneliness Flag

Every 13-speed tuple admits a nested chain

\[
V_{13}\supset V_{12}\supset\cdots\supset V_2
\]

with

\[
\boxed{|V_m|=m,
\qquad\operatorname{ML}(V_m)>1/(m+1)\quad(2\le m\le12).}
\]

Inside a bounded counterexample the archived campaign records a quantitative margin

\[
\operatorname{ML}(V_m)
\ge
1/(m+1)+1/(2C(m+1)).
\]

---

# VI. Exact subset-GCD budget and majority collapse

The campaign uses the exact divisor-support identity

\[
\boxed{
G(\mathbf u)=
\sum_{S\subseteq[13]}\gcd(u_i:i\in S)
=
\sum_{d\ge1}\varphi(d)(2^{h_d}-1).}
\]

With external finite bound

\[
G(\mathbf u)\le91^{12},
\]

if `q` divides at least `h` speeds then

\[
\boxed{(2^h-1)q\le91^{12}.}
\]

## GCD support amplification

If an `h`-subset, `h≥7`, has gcd `q`, and the outsiders have

\[
d_j=\gcd(q,v_j),
\]

then the all-modulus capacity theorem implies

\[
\boxed{\sum_jd_j\ge\frac{h-6}{6}q,}
\]

so some outsider satisfies

\[
\boxed{d_j\ge\frac{h-6}{6(13-h)}q.}
\]

## Certified recursive majority-GCD collapse

The companion verifier exhausts the finite divisor-multiset relaxation and certifies that every hypothetical counterexample obeys

\[
\boxed{
\begin{array}{c|cccccc}
|S|&12&11&10&9&8&7\\\hline
\gcd(S)\le&1&2&4&9&36&288
\end{array}}
\]

with relaxation-extremal divisor multisets

\[
11:2;(1,1),
\quad
10:4;(1,1,2),
\quad
9:9;(1,1,1,3),
\]

\[
8:36;(1,1,4,4,9),
\quad
7:288;(1,1,1,1,8,36).
\]

These certify sharpness of the **necessary-condition relaxation**, not existence of counterexamples.

The complete archived subset-GCD ladder is

\[
\begin{array}{c|c}
13&1\\
12&1\\
11&2\\
10&4\\
9&9\\
8&36\\
7&288\\
6&5118658530374679089931\\
5&10402435077858218795667\\
4&21498365827573652177712\\
3&46067926773372111809383\\
2&107491829137868260888560\\
1&322475487413604782665681
\end{array}
\]

The majority collapse `1,2,4,9,36,288` is the substantive new finite reduction in the source campaign.

## Maximal `h_7=6` transition-cover theorem

If exactly six speeds are divisible by 7, write them `7a_i`. For every outsider `v`,

\[
\boxed{
v\le
\sum_{i=1}^6
\gcd(a_i,v)
\left\lceil\frac{v/\gcd(a_i,v)}7\right\rceil.}
\]

Hence

\[
\sum_i\gcd(a_i,v)\ge v/7,
\qquad
\max_i\gcd(a_i,v)\ge v/42,
\]

and globally

\[
\boxed{\max(\text{outsiders})\le6\max(\text{7-divisible speeds}).}
\]

---

# VII. Additive / Riesz obstruction

For a 2-dissociated n-set, the archived campaign proves

\[
\boxed{
\operatorname{ML}(V)
\ge
\frac1{2\pi}
\arccos\left(1-\sqrt{\frac3{2n}}\right).}
\]

At `n=13`, this equals approximately `0.135210985878358 > 1/14`. Therefore every hypothetical counterexample has a nonzero short additive relation

\[
\boxed{\sum_{i=1}^{13}\varepsilon_i u_i=0,
\qquad
\varepsilon_i\in\{-2,-1,0,1,2\}.}
\]

The late campaign combines this with gap/divisibility structure in an `Additive-or-Cluster` transfer program with separately certified constants.

---

# VIII. Large-prime canonical subproblem — CLOSED IN THE ARCHIVED CAMPAIGN

The late campaign repairs the mod-13 polynomial reduction and obtains a scalar-canonical normal form for a large-prime canonical residue class.

## Repaired mod-13 reduction

For a canonical branch with

\[
u_i\equiv i\pmod p,
\]

the argument reduces to

\[
u_i\equiv\alpha i\pmod{13},
\]

then by CRT to a scalar-canonical congruence

\[
u_i\equiv b i\pmod M,
\qquad M=13p.
\]

## Exact parity certificate lemma

For

\[
F_e(x)=\min_{1\le i\le13}\|ix+e_i/2\|,
\]

exact rational certificates prove the required `1/13` bound for **8190 of the 8192 parity patterns**. The only unresolved masks at that stage are the all-zero mask and the parity mask `e_i≡i (mod 2)`.

## Scalar-canonical 2-adic descent

If

\[
M\ge1183,
\qquad\gcd(b,M)=1,
\qquad u_i\equiv bi\pmod M,
\]

then the archived descent rules out a counterexample.

## Closed large-prime canonical class

Consequently the source campaign records:

> For every prime `p>2366`, a primitive canonical tuple satisfying `u_i≡i (mod p)` cannot be an LRC(13) counterexample.

This is a **subproblem closure**, not a solution of LRC(13).

---

# IX. Retraction record

The campaign explicitly found and removed a false inference:

> If one chosen runner is a counterexample, then changing the stationary runner to any other runner also gives a counterexample.

This is false. Failure of loneliness for one chosen runner does not imply failure for another.

Accordingly the following target-level structures were **retracted**:

- universal residue multiplicity for every original runner and every `q≤14`;
- the global original-14-speed 3-AP-free claim;
- unique-13-farthest elimination obtained by changing reference;
- a global 14-point simultaneous congruence-partner skeleton;
- the mod-13 `(7,7)` two-fiber reduction on the original 14 runners;
- bilateral internal witnesses based on independently choosing bases in both fibers;
- bilateral Hall matching as a target reduction;
- seven near-opposite pairs as a target reduction;
- the 57-state / 2793-state bilateral packet program as a target close;
- the 49-base invariant lattice / centroid conservation as target constraints;
- the robust-or-critical bilateral witness-set theorem;
- simultaneous compression of every mod-13 fiber using independently changed bases.

These remain public as negative provenance rather than being silently erased.

---

# X. Abstract gold salvaged from the retracted branch

## Saturated-cover combinatorics

If seven subsets of a 13-set each have size at most two and cover all thirteen elements:

- total incidence 13 forces exactly six pairs and one singleton with no overlap;
- total incidence 14 forces seven pairs and exactly one doubled element.

## Hall lemma for near-partitions

For two seven-block covers of a 13-set, every block of size at most two, if every k-block subfamily has union size at least `2k-1`, then the block-intersection bipartite graph satisfies Hall and has a perfect matching.

## Equal-chord cycle tilings

If all capacity-two blocks are edges of one `C_13`, saturated covers reduce to alternating matching / near-perfect edge patterns.

## Packet diameter observation

If fixed nonzero integer frequencies `d_i` satisfy

\[
\|d_i\tau\|<1/7
\]

throughout an open interval `J`, then

\[
\boxed{|J|\le2/(7\max_i|d_i|).}
\]

These are retained as standalone mathematics, not as proofs of the retracted target reductions.

---

# XI. Negative theorem / dead-route bank

The following failures remain part of the mathematical record:

1. Generic pair-overlap alone is too diffuse to force the required rigidity.
2. Bare CRT/divisor coverage does not kill the mod-13 saturation branch.
3. Static congruence-partner structure is insufficient; an explicit primitive arithmetic witness killed the implication.
4. `1/13` separation from a base does not prevent pair distance `<1/7`.
5. Signed Hall cancellation is false combinatorially.
6. “57 packets = complete arithmetic state” was too aggressive; marked-base data had been quotiented away.
7. 49-base coherence with unrelated witnesses is too weak because witness phases vary independently.
8. A single Beatty/floor packet is not plausibly impossible; quotient freedom leaves substantial flexibility.
9. First moments do not kill the `h_13=6` branch.
10. Neither mixed-threshold nor equal-threshold harmonic correction has a universal favorable sign.
11. Local forced handoffs do not by themselves produce a proved global winding invariant.
12. Essentiality of the six internal bad sets does not imply disjointness or union-bound equality.

Audit correction: the Round-7 claim that Pair Mode produced the only compressed pair below `1/7` was too strong; only the designated doubled probe/pair was unique. Likewise, deleted-runner private witnesses do not imply every outsider appears globally as a two-slot transition direction.

---

# XII. Terminal conditional close

For `1≤h≤6`, define `TS(h)` as the statement that there do **not** exist integers

\[
a_1,\ldots,a_h,
\qquad
v_1,\ldots,v_{13-h},
\qquad13\nmid v_j,
\]

satisfying the inherited distinctness/primitivity constraints such that, for **every**

\[
\tau\in W_h=\{\|a_i\tau\|\ge1/14\ \forall i\},
\]

the exact outsider slot sets cover all thirteen residue probes.

Then

\[
\boxed{TS(1)\land\cdots\land TS(6)\Longrightarrow LRC(13).}
\]

The campaign did **not** prove all six `TS(h)`.

The sharpest branch is `TS(6)`, where the archive already has:

- `μ(W_6)>1/7`;
- saturated 13-cover structure at every phase of `W_6`;
- exact generic handoff rules;
- six essential internal frequencies;
- outsider private probes from deleted-runner witnesses;
- exact harmonic and gcd-sensitive probe formulas.

A certified impossibility proof for `TS(6)` would prove `h_13≤5`, but would not by itself close LRC(13).

---

# XIII. Final counterexample normal form

Any genuine 13-effective-speed counterexample surviving this campaign must satisfy all of:

- every 12-deletion is primitive;
- at least one deletion is strictly non-tight;
- one fixed runner has private witnesses on every sufficiently fine denominator grid;
- singleton/private-witness mass at least `22/(13u_13)`;
- every modulus obeys the gcd-sensitive probe-capacity law;
- every 7-subset gcd is at most `288`;
- every 8-subset gcd at most `36`;
- every 9-subset gcd at most `9`;
- every 10-subset gcd at most `4`;
- every 11-subset gcd at most `2`;
- the dominant-gap restrictions above;
- a nonzero additive relation with coefficients in `{-2,-1,0,1,2}`;
- `1≤h_13≤6` with the universal lifted-probe saturation constraints.

The exact missing implication is:

> A primitive non-tight 12-speed tuple satisfying the majority-GCD collapse cannot be extended by one integer speed into a 13-speed `1/14` counterexample.

That extension theorem was **not** proved.

## Final campaign verdict

- **Full LRC(13) closure:** NO.
- **Terminal structural reduction:** YES.
- **Large-prime canonical residue subproblem:** closed in the archived campaign for `p>2366`.
- **Largest invalid branch:** identified and retracted.
- **Strongest equality wall:** `h_13=6`, with universal saturated-cover structure on a set of measure strictly greater than `1/7`.

No unproved extension lemma is being relabeled as a solution.