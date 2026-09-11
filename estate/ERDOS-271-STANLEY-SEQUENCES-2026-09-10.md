# Erdős #271 — Stanley Sequences: Public Asset Extraction

**Author:** Jared Wilder  
**Campaign:** 2026-08-06  
**Public release:** 2026-09-10

## Status

The flagship Erdős #271 problem is **not closed** by this work. The campaign produced an audited 184-entry theorem/claim ledger and a coherent chain of exact reductions from the greedy rule to one support-size problem.

The internal ledger ended with:

- 111 `RETAINED_PROVED` entries;
- 27 `RETAINED_PROVED_WITH_CORRECTION` entries;
- 1 `RETAINED_PROVED_SUBSUMED` entry;
- 13 conditional theorems;
- 18 explicit conjectures / targets;
- 7 refuted or retired statements;
- 4 exact finite computations;
- 2 exploratory unverified objects;
- 1 external dependency.

Those are **ledger statuses**, not independent historical-novelty judgments.

## Canonical notation

For the greedy Stanley sequence seeded by `a_0=0, a_1=n`, write

\[
A_k=\{a_0,\dots,a_k\},\qquad g_k=a_{k+1}-a_k,
\]

\[
\Delta_k=\{a_k-a_i:0\le i\le k\},
\]

\[
U_k=\{2a_j-a_i:0\le i<j<k\},
\]

\[
m_k(x)=\#\{(i,j):0\le i<j<k,\ 2a_j-a_i=x\},
\]

and

\[
\mu_k=\frac{\binom{k}{2}}{|U_k|}.
\]

For `A(4)`, the forced seed omissions `1,2,3` are not in any reflection set, giving

\[
|U_k\cap[0,a_k)|=a_k-k-3.
\]

For a general fixed seed `n`, replace `3` by `n-1`.

# 1. Exact greedy dynamics

## Single-state obstruction theorem

The next greedy gap is determined by the difference state alone:

\[
g_k=\min\{d\ge1:d\notin(\Delta_k-2\Delta_k)\},
\]

with update

\[
\Delta_{k+1}=\{0\}\cup(g_k+\Delta_k).
\]

This removes absolute positions from the one-step decision.

## Decimated-correlation characterization

Define

\[
C_k(d)=\#\{\varepsilon\in\Delta_k:2\varepsilon+d\in\Delta_k\}.
\]

Then

\[
g_k=\min\{d\ge1:C_k(d)=0\},
\]

and the exact transport law is

\[
C_{k+1}(d)=C_k(d+g_k)+\mathbf 1_{\Delta_k}(d-g_k).
\]

So the next gap is the first zero of a decimated autocorrelation profile that shifts and receives one sparse translated patch.

## Consecutive-gap inequality

\[
g_{k+1}\ne g_k.
\]

The selected hole is repaired immediately at the next state.

# 2. Hole survival and multiplicative deserts

Let `H_k` be the positive holes of the obstruction set. Then

\[
H_{k+1}=\{r\ge1:r+g_k\in H_k,\ r\notin g_k+\Delta_k\}.
\]

A gap falls precisely when there is an older surviving hole in its multiplicative annulus:

\[
g_{k+1}<g_k
\iff
H_k\cap(g_k,2g_k)\ne\varnothing.
\]

When nonempty,

\[
g_{k+1}=\min(H_k\cap(g_k,2g_k))-g_k.
\]

If the interval contains no hole, then the gap rises.

Every later hole has an ancestral hole obtained by reversing these translations and avoiding every intervening mirror patch; holes are transported rather than spontaneously created.

# 3. Reflection-union normal form

The greedy sequence can be written as

\[
a_k=\min\{m>a_{k-1}:m\notin U_k\},
\]

with

\[
U_{k+1}=U_k\cup(2a_k-A_{k-1}).
\]

Thus accepted terms are exactly first holes in an oriented reflection support.

For

\[
R_j=2a_j-A_{j-1}
\]

and

\[
K_j=R_j\setminus\bigcup_{r<j}R_r,
\]

`K_j` is the set of nonmembers whose first killer is `a_j`. Apart from the forced seed omissions,

\[
\mathbb N_0\setminus A(n)
=
\{1,\dots,n-1\}\ \dot\cup\ \dot\bigcup_{j\ge1}K_j.
\]

## Doubling-sentinel theorem

For every accepted `a_j`, the value

\[
2a_j
\]

is a genuinely new first kill. Hence every stage has positive fresh yield:

\[
\nu_j:=|K_j|\ge1.
\]

## Guaranteed-yield theorem

The later audited ledger strengthens this to

\[
\nu_j\ge\#\{i<j:a_i<2g_{j-1}\},
\]

with equality for the fresh layer above the historical ceiling under the ledger's stated decomposition.

## Large-gap maximal yield

If

\[
g_{j-1}>\frac{a_{j-1}}2,
\]

then the entire raw reflection layer is fresh:

\[
K_j=R_j,
\qquad
\nu_j=j.
\]

The converse was explicitly rejected.

# 4. Multiplicity growth reduction

The exact reflection multiplicities satisfy

\[
\sum_xm_k(x)=\binom{k}{2},
\]

\[
|U_k|=|\operatorname{supp}m_k|,
\]

and

\[
\mu_k=\frac{\binom{k}{2}}{|U_k|}.
\]

After the campaign's support-utilization correction, the retained growth relation is

\[
\boxed{a_k=\Theta\!\left(k+\frac{k^2}{\mu_k}\right)}.
\]

Every infinite Stanley sequence is superlinear by the external zero-density theorem for 3-AP-free sets, so for a fixed seed this becomes

\[
\boxed{a_k=\Theta\!\left(\frac{k^2}{\mu_k}\right)}.
\]

For `A(4)`, the historical growth target

\[
a_k=\Theta(k^2/\log k)
\]

is therefore equivalent within this reduction to

\[
\boxed{\mu_k=\Theta(\log k)}
\]

and equivalently

\[
\boxed{|U_k|=\Theta(k^2/\log k)}.
\]

This pair of support inequalities is the campaign's final proof cut. It remains open in the packet.

# 5. Collision restrictions retained by the audit

Several exact collision restrictions survived, including:

- equal-step chain exclusion: three middle terms in a single multiplicity fiber cannot form a 3-term arithmetic progression;
- second mixed-shadow exclusion: distinct relevant `p,q,r` cannot satisfy `4p=q+r` in the stated mixed-shadow configuration;
- third mixed-shadow exclusion: distinct relevant `p,q,r` cannot satisfy `2r=q+2p` in the stated configuration;
- reverse mixed-shadow restrictions prohibit additional affine coincidences such as `4q=2p+r`, `4p=2q+r`, and `r=p+q` under the corresponding hypotheses;
- along the representation-chain construction, paired differences obey a doubling relation `ΔI=2ΔJ`.

These are local structure theorems, not the missing logarithmic multiplicity bound.

# 6. Corrections that stay public

The campaign did not silently erase its own failed ideas.

- A single primitive finite transition matrix was rejected as an explanation of permanently different power-law exponents.
- A bounded physical window in `Δ_k` was shown insufficient because large pairs can produce small values of `δ-2ε`.
- The claimed Ternary Scale Mixing Lemma failed audit; exact finite data showed maximum per-scale multiplicities increasing through the tested range rather than supporting the intended bounded statement.
- The A(4) support-utilization identity required the seed correction
  \[
  \eta_k=\frac{a_k-k-3}{|U_k|},
  \]
  rather than the earlier `a_k-k` numerator.
- The false converse to the large-gap maximal-yield theorem was retired.

# 7. Exact endpoint of the campaign

The strongest retained compression is

\[
\boxed{\text{Stanley growth is the inverse of mean oriented-reflection multiplicity:}\quad
 a_k=\Theta(k^2/\mu_k).}
\]

For `A(4)`, the unresolved support problem is

\[
\boxed{|\{2a_j-a_i:0\le i<j<k\}|=\Theta(k^2/\log k).}
\]

That is where the campaign ends. It is a reduction of the historical growth problem, not a proof of it.

## Authority and novelty boundary

No historical novelty review was completed for the reflection-union, first-kill, multiplicity, or mixed-shadow reductions. Several may be equivalent to known Stanley-sequence covering formulations. Computational claims remain finite. External superlinearity depends on the standard zero-density theorem for 3-AP-free sets.

The public value of this release is therefore the complete structural reduction and explicit negative knowledge, not a claim to have solved Erdős #271.
