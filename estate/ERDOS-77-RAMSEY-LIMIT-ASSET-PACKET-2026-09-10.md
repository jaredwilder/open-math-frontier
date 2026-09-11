# Erdős #77 — Diagonal Ramsey Exponential-Limit Asset Packet

**Author:** Jared Wilder  
**Public release:** 2026-09-10

## Court result

**NOT CLOSED.** The target is the existence/value of

\[
\lim_{k\to\infty}R(k)^{1/k},
\qquad R(k)=r(k,k).
\]

This packet publishes the 23 internal theorem/diagnostic records from the terminal session while preserving the difference between proved lemmas, conditional implications, falsified operators, and open obligations.

# I. Corridor and inverse formulations

## P01 — Thin-Corridor Ramsey Inequality

For integers `n>a>=0`,

\[
\boxed{r(n-a,n)\le R(n)\le4^a r(n-a,n).}
\]

The upper bound follows by iterating the standard Ramsey recurrence

\[
r(s,t)\le r(s-1,t)+r(s,t-1)
\]

until one coordinate reaches `n-a`.

## P02 — Thin-Corridor Equivalence

If `a_n=o(n)`, then

\[
\boxed{
\frac1n\log R(n)-\frac1n\log r(n-a_n,n)\to0.
}
\]

Therefore the diagonal and any sublinear off-diagonal corridor have the same exponential limsup and liminf.

## P03 — Inverse homogeneous-set formulation

Define

\[
h(N)=\min_{|V(G)|=N}\max\{\omega(G),\alpha(G)\}.
\]

Then

\[
R(k)>N\iff h(N)<k.
\]

For `L>1`,

\[
R(k)^{1/k}\to L
\iff
\frac{h(N)}{\log N}\to\frac1{\log L}.
\]

# II. Local extremal lemmas

## P04 — Clone Saturation Lemma

In a red/blue colouring of `K_{R(k)-1}` with no monochromatic `K_k`, every vertex belongs to both a red and a blue `K_{k-1}`. Equivalently, its red neighborhood contains a red `K_{k-2}` and its blue neighborhood contains a blue `K_{k-2}`.

## P05 — Weighted Wrong-Pair Inequality

If `G` has clique number at most `a`, vertex loads satisfy `0<=s_i<=b`, and `t=Σs_i`, then for

\[
B=\sum_{ij\notin E(G),\,i<j}s_is_j
\]

one has

\[
\boxed{B\ge\frac{t(t-ab)}{2a}.}
\]

The proof is weighted Motzkin–Straus plus `Σs_i²<=bt`.

# III. The exact conditional bridge to existence of the limit

## P06 — Summable Composition Error Accumulation

Suppose a binary witness operation multiplies vertex counts and incurs parameter loss

\[
m(X\star Y)
\le
m(X)+m(Y)
+C\frac{m(X)+m(Y)}{\log^2(m(X)+m(Y))}.
\]

Then `q` identical parameter-`K` witnesses can be parenthesized so their total parameter satisfies

\[
\boxed{
M_q\le qK\exp(O(1/\log K))
=qK(1+O(1/\log K)),
}
\]

uniformly in `q`. The proof uses balanced dyadic blocks plus binary decomposition of arbitrary `q`.

## P07 — Approximate Supermultiplicativity Implies Existence

Put `A(k)=R(k)-1`. Assume there are constants `C,k_0` such that for all sufficiently large `m,n` there is

\[
0\le E(m,n)\le C\frac{m+n}{\log^2(m+n)}
\]

with

\[
\boxed{A(m+n+E(m,n))\ge A(m)A(n).}
\]

Then

\[
\boxed{\lim_{k\to\infty}R(k)^{1/k}\text{ exists}.}
\]

**This is conditional. The source campaign did not prove the approximate-supermultiplicativity hypothesis.**

## P08 — Complementary Off-Diagonal Amplification

Conditional on a composition theorem combining a witness for `r(s,Cs)` and its colour-swapped copy with multiplicative vertex count and `o(s)` parameter loss, a lower bound

\[
r(s,Cs)\ge B(C)^{s+o(s)}
\]

would imply

\[
\boxed{
\liminf_{k\to\infty}R(k)^{1/k}
\ge B(C)^{2/(1+C)}.
}
\]

Again, this is an implication, not a constructed operator.

## P09 — Optimization algebra

Using the source packet's quoted fixed-ratio off-diagonal input

\[
r(s,Cs)\ge2^{(1-1/(2C))s},
\]

P08 would produce exponent

\[
f(C)=\frac{2-1/C}{1+C}.
\]

The exact maximizer is

\[
\boxed{C_*=(1+\sqrt3)/2},
\]

with

\[
\boxed{f(C_*)=4-2\sqrt3.}
\]

Thus **conditional on P08**, the corresponding diagonal base would be

\[
2^{4-2\sqrt3}=1.4498447105\ldots.
\]

The calculus is proved; the Ramsey conclusion remains conditional on the missing composition theorem.

# IV. Binary polarity constructions

## P10 — Explicit binary nonedge-polarity digraph

For `p>=1`, let

\[
V(D_p)=\{(a,b)\in(\mathbb F_2^p\setminus\{0\})^2:a\cdot b=1\}
\]

and

\[
(a,b)\to(a',b')\iff a\cdot b'=0.
\]

Then:

1. `D_p` is loopless;
2. `D_p` is `T_{p+1}`-free;
3. exactly
   \[
   \boxed{|D_p|=(2^p-1)2^{p-1};}
   \]
4. consequently
   \[
   \boxed{\frac{|D_{p_1+p_2+1}|}{|D_{p_1}||D_{p_2}|}\to8.}
   \]

## P11 — Tagged direct-sum XOR identity

Embedding two factor vertices with an additional tag coordinate gives product arc bit

\[
\boxed{e(x,y)=e_1(x,y)\oplus e_2(x,y).}
\]

## P12 — Exact pattern-collision identity

If `c_D(F)` counts ordered tuples with upper-triangular arc pattern `F`, then the XOR product satisfies

\[
\boxed{
I_t(D_1\otimes D_2)
=
\sum_F c_{D_1}(F)c_{D_2}(F),
}
\]

where `I_t` counts ordered forward-independent `t`-tuples.

## P13 — Pattern collision implies triangular orthogonality

Equal factor arc patterns imply, after doubling the vector coordinates,

\[
\boxed{A_i\cdot B_j=0\qquad(i<j).}
\]

This converts product-pattern collision into a triangular bilinear-system count.

# V. Exact tensor/rank algebra

## P14 — Exact Tensor-Flag Rank Formula

Let

\[
L_1\subseteq\cdots\subseteq L_t\subseteq U
\]

be a nested flag and `b_1,...,b_t in W`. Choose a basis `e_1,...,e_d` adapted to the flag and let

\[
\tau_r=\min\{j:e_r\in L_j\}.
\]

Then

\[
\boxed{
\dim\left(\sum_{j=1}^t L_j\otimes\langle b_j\rangle\right)
=
\sum_{r=1}^d
\dim\operatorname{span}\{b_j:j\ge\tau_r\}.
}
\]

This is a standalone algebra theorem over any field.

## P15 — Mixed Bilinear Product Theorem

For factor dimensions `p_1,p_2`, block matrix

\[
Q=\begin{pmatrix}I&M\\N&I\end{pmatrix}
\]

and the source tagged bilinear lift, the full Cartesian factor map is injective, each image vertex has diagonal value one, and the resulting digraph is

\[
\boxed{T_{p_1+p_2+2}\text{-free}.}
\]

The theorem is algebraically valid; P21 below proves that the unrestricted full product is still unusable as the desired Ramsey composition.

## P16 — One-sided mixer affine equations

For the one-sided mixer, forward-independence imposes equations

\[
\boxed{
(a_{1i}+a_{1j})^T M b_{2j}
=
a_{1i}\cdot b_{1j}+a_{2i}\cdot b_{2j}
\qquad(i<j).
}
\]

The coefficient tensor is

\[
(a_{1i}+a_{1j})\otimes b_{2j}.
\]

## P17 — Exact mixer rank via affine prefix flags

Let

\[
L_j=\operatorname{span}\{a_{1i}+a_{1j}:i<j\}.
\]

Then P14 gives exact mixer coefficient rank

\[
\boxed{
R_M(X)
=
\sum_{r=1}^{d_A}
\operatorname{rank}\{b_{2j}:j\ge\tau_r\}.
}
\]

In particular, if `d_j=dim L_j` and `rho_j=rank{b_{2l}:l>=j}`, then

\[
\boxed{R_M(X)\ge d_j\rho_j.}
\]

## P18 — Rank-weighted first moment

For uniform random mixer bits, a consistent affine system of rank `R(X)` survives with probability

\[
\boxed{2^{-R(X)}}.
\]

Therefore

\[
\mathbb E I_t(M)\le\sum_X2^{-R(X)}.
\]

With random ordering and independent sampling probability `theta`, the corresponding bound becomes

\[
\boxed{
\frac{\theta^t}{t!}
\sum_X2^{-R(X)}.
}
\]

# VI. Exact diagnostics and falsification

## P19 — Uniform-rank first-moment barrier

If the argument only uses `N^t` ordered tuples with

\[
N=2^{\beta t+o(t)}
\]

and at most one binary equation per unordered pair, then even maximal uniform rank gives exponent

\[
(\beta-1/2)t^2+o(t^2).
\]

So this **specific raw-count + uniform-rank architecture** cannot close for `beta>1/2`. This is not a universal impossibility theorem.

## P20 — Two-cross-matrix bit ceiling

At the source optimum `C_*`, two cross matrices supply only coefficient

\[
0.4880338717\ldots
\]

at quadratic scale, below target exponent

\[
0.5358983848\ldots.
\]

The deficit is

\[
0.0478645131\ldots.
\]

Again: information-budget diagnosis, not impossibility of every correlated construction.

## P21 — Full Mixed-Product Fiber Obstruction

Fix a second coordinate pair `v=(b_1,b_2)` in the full Cartesian product. Its fiber has

\[
2^{p_1+p_2-2}
\]

vertices. Partition by the single bit `c(u)=u^TQv`. One class has size at least

\[
\boxed{2^{p_1+p_2-3}}
\]

and is completely edgeless.

Thus any induced subset with independence number below `t` satisfies

\[
\boxed{
|S|
\le
2(t-1)(2^{p_1}-1)(2^{p_2}-1).
}
\]

This is the terminal countercertificate killing the unrestricted full mixed-bilinear Cartesian product as an exponent-preserving composition witness.

# VII. Fiber-free polarity search space

## P22 — Perfect matching in the valid-pair incidence graph

Let `H_p` be the bipartite graph on two copies of `F_2^p\{0}` with

\[
a\sim b\iff a\cdot b=1.
\]

It is `2^{p-1}`-regular on both sides, so it has a perfect matching. Equivalently, there is a bijection

\[
\boxed{\pi:\mathbb F_2^p\setminus\{0\}\to\mathbb F_2^p\setminus\{0\}}
\]

such that

\[
\boxed{a\cdot\pi(a)=1}
\]

for every nonzero `a`.

## P23 — Matching-restricted polarity digraph

For any such bijection, define

\[
a\to a'\iff a\cdot\pi(a')=0.
\]

Then the digraph is loopless, has exactly `2^p-1` vertices, and is

\[
\boxed{T_{p+1}\text{-free}.}
\]

Unlike the full-pair construction it has no repeated `a`- or `b`-coordinate fibers.

An ordered tuple is forward-independent exactly when

\[
\boxed{a_i\cdot\pi(a_j)=1\quad\text{for all }i\le j.}
\]

No theorem in the source packet proves that some choice of `pi` has the independent-set bound needed for Erdős #77.

# VIII. Killed routes

The terminal session permanently banked these failures:

1. ordinary lexicographic product;
2. plain XOR as a standalone composition;
3. universal strong induced-pattern entropy rigidity from Ramsey-freeness alone;
4. independent noisy blow-up;
5. generic high-value rank lemma from factor Ramsey parameters alone;
6. raw `N^t` + uniform binary-rank first moment above `beta=1/2`;
7. unrestricted full mixed-bilinear Cartesian product as an exponent-preserving composition witness.

# IX. Exact remaining obligations

The source packet ended with three genuine research obligations:

- **U01:** a coordinate-controlled rank/container theorem for sparse factor families;
- **U02:** a fiber-free correlated additive-dimension composition operator — the terminal missing edge;
- **U03:** a Ramsey bound for the matching-polarity digraph `D_pi` for a suitably chosen matching `pi`.

# X. Claim boundary

The durable contribution is a serious reduction and a set of exact algebraic tools/countercertificates around the limit problem.

The packet **does not prove**:

\[
\lim_{k\to\infty}R(k)^{1/k}
\]

exists, nor does it determine its value. The only theorem that gives existence here is P07, and it is explicitly conditional on an approximate-supermultiplicative composition hypothesis that remains unproved.

Current 2026 Ramsey literature continues to improve exponential upper and off-diagonal bounds; those advances do not by themselves settle this limit question, and this release makes no contrary claim.
