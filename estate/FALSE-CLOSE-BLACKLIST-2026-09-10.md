# False-Close Blacklist — 2026-09-10

**Author:** Jared Wilder  
**Purpose:** preserve poisoned mathematical claims and their falsifiers so they cannot silently re-enter the research estate.

These are not merely “failed ideas.” Each item below records a claim that was strong enough to look like a closure route and was later found false, semantically mismatched, or unsupported in a load-bearing way.

A blacklisted claim may only be revived by a fresh proof that explicitly defeats the listed falsifier.

---

## Erdős #396

**Poisoned claim:** `k=2` never works.

**Falsifier:** explicit `n=2480` and `n=3478` satisfy the relevant congruence/witness condition in independent prior checks.

---

## Erdős #1199

**Poisoned claim:** Hindman’s theorem closes the coloring problem.

**Falsifier:** Hindman finite-sums does not supply the required diagonal sums `2a`; the proposed `v_2 mod 2` countercoloring also fails on `A={4m+1}`.

---

## Erdős #885

**Poisoned claim:** an LCM construction closes all intersections.

**Falsifier:** already false at `k=2`:

\[
D(12)=\{1,4,11\},
\qquad
D(24)=\{2,5,10,23\},
\]

so

\[
D(12)\cap D(24)=\varnothing.
\]

---

## Erdős #1203

**Poisoned claim:** a uniform boundedness / negative close.

**Falsifier:** for fixed `k=3`, the campaign quantity has an `omega(n+3)`-driven unbounded lower mechanism along highly composite squarefree-rich values of `n+3`. The claimed uniform bound cannot hold.

---

## Erdős #829

**Poisoned claim:** Mahler gives super-polylogarithmic growth strong enough to close branch B.

**Falsifier:** the classical theorem does not supply the claimed strength. The campaign inflated a known logarithmic-power lower bound.

---

## Erdős #101

**Poisoned claim:** Melchior / Green–Tao / Füredi–Palásti close the four-rich-line extremal problem.

**Falsifier:** the argument conflated ordinary-line / three-rich-line results with the four-rich extremal target. No closure follows.

---

## Erdős #155

**Poisoned claim:** if `A` is Sidon then `A ∪ 3A` is Sidon, giving `F(3N) >= 2F(N)`.

**Falsifier:** take

\[
A=\{1,2\}.
\]

Then

\[
A\cup3A=\{1,2,3,6\},
\]

but

\[
1+3=2+2.
\]

---

## Erdős #200

**Poisoned claim:** Rankin prime gaps negate the arithmetic-progression target.

**Falsifier:** large prime gaps do not create the required long arithmetic progressions. The route is a non sequitur.

---

## Erdős #279

**Poisoned claim:** a simple sieve gives a complete negative close.

**Falsifier:** the campaign jump is unsupported. Treat the statement as poisoned until a complete exact proof is recovered and independently audited.

---

## Erdős #653

**Poisoned claim:** a grid construction proves `g(n)/n -> 0`.

**Falsifier:** extremal direction was reversed. Constructing one low-spectrum configuration cannot upper-bound a quantity defined as a maximum over configurations.

---

## Erdős #1073

**Poisoned claim:** Wilson’s theorem for odd prime powers closes the problem, and an `O(sqrt x)` count follows.

**Falsifier:** the asserted Wilson congruence is not valid modulo arbitrary `p^a` in that form, and the divisor-shape lemma does not imply the claimed counting bound.

---

## Erdős #251

**Poisoned claim:** a broad irrationality theorem covering every increasing sequence `a_n`.

**Falsifier:** take

\[
a_n=n.
\]

Then

\[
\sum_{n\ge1}\frac{n}{2^n}=2,
\]

which is rational.

---

## Erdős #389

**Poisoned claim:** universal impossibility in the campaign’s consecutive-product condition.

**Falsifier:** `n=2, k=5` is an explicit working case.

The independently preserved witness satisfies

\[
2\cdot3\cdot4\cdot5\cdot6=720
\]

and

\[
7\cdot8\cdot9\cdot10\cdot11=55440=77\cdot720.
\]

---

## Erdős #410

**Poisoned claim:** `6` is a fixed point of `sigma`.

**Falsifier:** perfectness means

\[
\sigma(6)=12=2\cdot6,
\]

not `sigma(6)=6`.

---

## Erdős #383

**Poisoned claim:** every `n^2+1` has a prime factor greater than `n` in the claimed form.

**Falsifier:** for `n=7`,

\[
n^2+1=50=2\cdot5^2,
\]

and neither prime factor exceeds seven.

---

## Erdős #1054

**Poisoned claim:** a universal formula promoted from finite data.

**Falsifier:** the campaign already has a counterinstance at `n=12`, together with domain-convention drift. The formula must be re-derived from the exact source definition before reuse.

---

## Erdős #943

**Poisoned claim:** a kernel-green result closes the additive-convolution target.

**Falsifier:** wrong operation. The formal result concerns a factorization/product surrogate rather than the required additive convolution.

---

## Erdős #513

**Poisoned claim:**

\[
\sum_{k\ge0} z^{2^k}
\]

is an admissible transcendental **entire** function supplying the desired lacunary witness.

**Falsifier:** the series has radius of convergence one. For `|z|>1`, its terms do not even tend to zero.

---

## Erdős #891

**Poisoned claim:** an `Omega`-window theorem closes or directly proves the canonical `omega`-window target.

**Falsifier:** `Omega` counts prime factors with multiplicity while `omega` counts distinct prime factors. The substitution is exactly the semantic drift forbidden by the problem contract.

---

## Erdős #170

**Poisoned claim:** the stated `R(k)` duality is proved for arbitrary `A subset Z`.

**Falsifier:** the proof silently converts an unrestricted-mark difference basis into one with

\[
A\subseteq\{0,\ldots,N\}.
\]

The required normalization lemma is absent.

---

# Release doctrine

This blacklist is append-only in spirit.

A counterexample, semantic mismatch, wrong-operation proof, or missing normalization step is mathematical information. It should remain visible beside the positive theorem bank rather than being erased when a campaign moves on.

The presence of a problem number here does **not** say the underlying Erdős problem is false or solved. It says only that the named closure route is poisoned until its explicit defect is repaired.