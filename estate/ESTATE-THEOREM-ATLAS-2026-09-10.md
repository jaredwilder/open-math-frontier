# Estate Theorem Atlas — 2026-09-10

Author: Jared Wilder

Public preservation of the audited mathematical estate. Each entry keeps its authority and scope. Nothing here becomes a parent-problem solution by adjacency, and inclusion is not a novelty claim.

## Current post-audit promotions

- **#486:** summable forbidden mass implies ordinary natural density under the correct activation threshold. **Independent rediscovery:** current research found Araújo (2026) already covers the summable delayed multi-residue regime.
- **#949:** sharp q≤5 finite theorem + kernel-checked countable analogue + finite-sums strengthening; continuum case remains open.
- **#1061:** aliquot-square primitive-seed generator and exact certificate bank; construction, not the current parent frontier.
- **#247:** all-base irrationality under the Erdős limsup hypothesis; not transcendence.
- **#406:** 3-adic admissible-exponent sieve with O(N^(log_3 2)) counting growth; not finiteness.
- **#413:** parameterized logarithmic predecessor window.
- **#727:** infinite k=2 prime-parametrized obstruction family.
- **#1212:** infinitely many isolated admissible vertices.
- **#359:** reciprocal-prefix invariant for the corrected greedy sequence.
- **#973:** exact n=2 golden-ratio extremum; parent later solved externally.

## Frozen audited vault

| Erdős | authority | asset | exact statement | scope ceiling |
|---:|---|---|---|---|
| 1 | `FINITE_EXACT` | Sharper constant ceiling from a five-element sum-distinct witness | The admissible set A={6,9,11,12,13} subset [1,13] has all 32 subset sums distinct. Therefore any universal strict constant C in the frozen Lean formulation must satisfy C<13/32. | A necessary ceiling on C, not a proof that any positive universal C exists. |
| 17 | `MANUAL_EXACT` | Prime-difference hardness reduction | If Erdős #17 has infinitely many good primes p, then every positive even integer n is a difference q1-q2 of two primes. | Necessary consequence only; it does not prove #17. The campaign's stronger twin-prime inference is false because n=2 can always reuse 5-3. |
| 33 | `MANUAL_EXACT` | Square-root counting baseline | If every sufficiently large integer is representable as m^2+a with a in A, then liminf A(N)/sqrt(N) >= 1. | This reaches the baseline 1 only; the canonical second question asks whether the liminf must be strictly greater than 1. |
| 51 | `HIGH_VALUE_PARTIAL` | Totient preimage structure | n=a*prod_{p|n} p/(p-1); factorial constraints on omega(n) give size control on minimal preimages; finite block n_{2^t}=2^(t+1) for t=32..63 was certified. | General asymptotic bridge requires audit. |
| 68 | `MANUAL_EXACT` | Factorial reciprocal expansion | 1/(n!-1)=sum_{j>=1}(n!)^{-j} for n>=2. | Identity only; irrationality remains. |
| 82 | `MANUAL_EXACT` | Ramsey regular-induced-subgraph baseline | Every n-vertex graph has a regular induced subgraph on at least floor(log_4 n)+1 vertices; hence F(n)>=floor(log_4 n)+1. | Only a logarithmic baseline. It does not imply the canonical F(n)/log n -> infinity. |
| 120 | `MANUAL_EXACT` | Unbounded-A stratum | For every infinite unbounded A subset R, there exists a positive-measure set E containing no affine copy aA+b with a!=0; E=[0,1] works. | Solves only the unbounded-A stratum. The bounded infinite-A case remains the substantive part. |
| 145 | `KNOWN_PUBLIC_WEAKER` | Squarefree-gap moments for 0<=alpha<=1 | Using fixed-gap densities plus telescoping tail control, the squarefree gap moment limit exists for every 0<=alpha<=1; at alpha=1 the limit is 1. | Known and much weaker than the current literature: record as proof-architecture recovery only, not novelty. |
| 153 | `HIGH_VALUE_LEMMA` | Sidon energy package | Sidon sum-injectivity plus Cauchy-Schwarz controls gap/additive energy. | Exact constants/source hypotheses should be formalized. |
| 155 | `LEAN_REPAIR` | Sidon extremal monotonicity | F(N+1) <= F(N)+1. | Pipeline theorem, not canonical close. |
| 170 | `KERNEL_FINITE_CERT` | Perfect 5-ruler parity obstruction | No 5-point perfect difference ruler exists in [0,10]. | Finite endpoint/certificate, not asymptotic close. |
| 200 | `MANUAL_EXACT` | Prime-AP common-difference divisibility | A sufficiently long prime arithmetic progression forces every small prime q, apart from an endpoint exception when a term itself equals q, to divide the common difference d. | Classical necessary condition only. |
| 236 | `MANUAL_EXACT` | Trivial logarithmic representation cap | For f(n)=#{n=p+2^k}, f(n)<=floor(log2 n)+1. | Only O(log n), not the desired o(log n). |
| 238 | `MANUAL_EXACT` | Small-c2 stratum | For every fixed c2<2 and c1>0, the #238 conclusion holds for all sufficiently large x. | Only the c2<2 subcase; general c2 remains the problem. |
| 241 | `MANUAL_EXACT` | Sharp elementary B3 multiset count | For a B3 set A subset [1,N], binom(|A|+2,3) <= 3N-2; hence |A|^3 < 18N. | One-sided upper bound only; canonical asymptotic constant remains untouched. |
| 243 | `MANUAL_EXACT` | Divisibility-chain irrationality obstruction | If a_m|a_{m+1} and a_{m+1}/a_m -> infinity, then sum 1/a_m is irrational. | Restricted structural theorem, not canonical converse. |
| 247 | `MANUAL_EXACT` | Sparse-binary irrationality theorem | If a_1<a_2<... and limsup a_n/n = infinity, then sum 2^(-a_n) is irrational. | Canonical problem asks transcendence, not merely irrationality. |
| 254 | `MANUAL_EXACT` | Rational-theta hypothesis equivalence | For reduced theta=a/q in (0,1), sum_{n in A} ||theta n|| diverges iff A contains infinitely many n not divisible by q. | Only the rational-theta portion of the canonical hypothesis. |
| 274 | `MANUAL_EXACT` | Infinite-group cardinality collapse | A finite exact coset partition of an infinite group cannot have all part cardinalities distinct. | Cardinality version only; does not solve finite-index Herzog-Schönheim formulation. |
| 276 | `KERNEL_CERTIFIED` | Fibonacci-type common divisors | For any recurrence a[n+2]=a[n+1]+a[n], d divides every term iff d divides gcd(a0,a1). | Does NOT bridge to canonical fixed-N gcd condition; varying prime factors can alternate. |
| 289 | `MANUAL_EXACT` | Kürschák 2-adic interval obstruction | A nontrivial consecutive reciprocal interval has nonintegral sum; maximal-v2 signature yields parity constraints. | Known classical mechanism; global combination still open. |
| 291 | `RECONSTRUCT_REQUIRED` | Harmonic/Sondow p-adic criterion | Raw campaign claims a criterion linking p | gcd(a_n,L_n) to a harmonic sum modulo p at floor(n/p). | Do not promote until every p/n hypothesis and numerator normalization is reconstructed. |
| 376 | `HIGH_VALUE_REDUCTION` | Kummer carry characterization | gcd(C(2n,n),105)=1 iff doubling n has no carries in bases 3,5,7. | Requires exact formalization/hypothesis audit; likely known reduction. |
| 385 | `MANUAL_EXACT` | Universal baseline for F(n) | For all n>=5, F(n)>=n; for odd n>=5, F(n)>=n+1. | Does not prove divergence F(n)-n -> infinity. |
| 390 | `MANUAL_EXACT` | Largest-prime carrier bound | If p_*(n)>n/2 is the largest prime <=n, any admissible factorial factorization must contain a factor >=2p_*(n), yielding lower bound f(n)>=2p_*(n) under route definition. | Check exact definition of f before reuse. |
| 394 | `MANUAL_EXACT` | Prime t2 formula | For odd prime p, t_2(p)=p-1 under the route definition. | Endpoint p=2 and exact indexing convention must be handled. |
| 400 | `MANUAL_EXACT` | Factorial construction lower bound | For fixed k>=2, g_k(m!) >= m+k-3 via (m!-1,m,1,...,1). | Unboundedness only; canonical average/asymptotic remains open. |
| 400 | `MANUAL_EXACT` | k=2 logarithmic upper bound | If a!b! divides n!, then a+b-n <= s2(a)+s2(b)-s2(n)=O(log n). | Known easy direction; does not determine asymptotic. |
| 412 | `MANUAL_EXACT` | Sigma strict-growth lemma | For n>=2, sigma(n)>=n+1, with equality iff n is prime. Hence every sigma-orbit starting at n>=2 is strictly increasing and repetition-free. | Does not imply orbit intersection in the canonical problem. |
| 413 | `MANUAL_EXACT` | Logarithmic predecessor window | Condition m+omega(m)<=n for all m<n is equivalent to omega(n-k)<=k; k>=log2 n is automatic; k=1 forces n-1 prime power. | First clause only; second epsilon clause separate. |
| 445 | `KNOWN_PUBLIC_ROUTE` | Classical c>3/4 route | The standard incomplete Kloosterman-sum count yields the desired inverse pair in every interval of length H=p^c once c>3/4. | Known theorem architecture only; canonical target asks every c>1/2. |
| 456 | `MANUAL_EXACT` | Totient-preimage prime anchor | For every prime p, m_{p-1}=p, where m_n is the least m with n|phi(m). | Only anchors one n for each prime p. |
| 477 | `MANUAL_REDUCTION` | Density necessity for unique polynomial tiling | If Z=A+f(Z) uniquely with deg f=d>=2, counting polynomial values in a long interval forces A to have density 1 in the appropriate sense. | Needs one-/two-tail bookkeeping before formal promotion. |
| 479 | `MANUAL_EXACT` | Infinite congruence subfamily | For j>=0, e=2^j and odd prime p, n=e*p satisfies n | 2^n-2^e. | Known favorable subfamily; not a close. |
| 489 | `MANUAL_EXACT` | Finite-A periodic squared-gap formula | For finite A with gcd(A)=1, the avoiding set B is periodic mod M=lcm(A); its squared-gap mean is an exact cyclic-period average. | Finite-A stratum only. |
| 495 | `MANUAL_EXACT` | Littlewood rational-coordinate stratum | If alpha or beta is rational, then liminf n||n alpha||||n beta||=0. | Irrational-irrational case remains Littlewood. |
| 535 | `MANUAL_EXACT` | Powers-of-two equal-gcd obstruction | For every r>=3 and N>=1, the powers of two <=N give f_r(N) >= floor(log2 N)+1. | Elementary lower bound only. |
| 579 | `MANUAL_EXACT` | Common-neighborhood lemma | In a K_{2,2,2}-free graph, the common neighborhood of any nonadjacent pair is K_{2,2}-free. | Local lemma only. |
| 595 | `MANUAL_EXACT` | Countable-graph stratum trivial | Every countable graph is a countable union of triangle-free graphs. | Any difficult witness must be genuinely uncountable. |
| 602 | `MANUAL_EXACT` | Countable-family colouring stratum | Every countable family of countably infinite sets with pairwise finite intersections admits a 2-colouring making each member bichromatic. | Canonical family may be uncountable. |
| 653 | `MANUAL_EXACT` | Distance-count sandwich | For n>=7, ceil(n/2) <= g(n) <= n-2 under the frozen distinct-distance definition. | Partial bounds only; does not settle g(n)~n. |
| 681 | `MANUAL_EXACT` | Fourth-root search window | If n+k is composite with least prime factor >k^2 then k^4<n+k. | Finite-window reduction only. |
| 683 | `MANUAL_EXACT` | Exponent ceiling obstruction | At (n,k)=(10,3), P(C(10,3))=5, so any universal c must satisfy 3^(1+c)<=5; in particular c=1/2 is impossible. | Partial obstruction only. |
| 689 | `MANUAL_EXACT` | Double-count necessary condition | If residue classes a_p modulo every prime p<=n cover each m in [1,n] at least twice, then sum_{p<=n} ceil(n/p) >= 2n. | Necessary condition only; asymptotically weak. |
| 726 | `HIGH_VALUE_REFORMULATION` | Mertens/fractional-part reformulation | Indicator n in (p/2,p) mod p can be rewritten exactly in residue/fractional-part terms, isolating a weighted equidistribution problem. | Asymptotic equidistribution unresolved. |
| 727 | `MANUAL_EXACT` | Infinite obstruction family at k=2 | For prime p>=7 and n=2p-2, ((n+2)!)^2 does not divide (2n)!. | Obstruction family; does not address infinitely many successes. |
| 730 | `MANUAL_EXACT` | Central binomial parity | C(2n,n) is even for n>=1. | Tiny reusable lemma only. |
| 774 | `MANUAL_EXACT` | Finite-union implies proportionately dissociated | If A is the union of k dissociated sets, then every finite B subset A contains a dissociated subset of size at least |B|/k. | Easy converse direction only. |
| 821 | `MANUAL_EXACT` | Totient parity | phi(m) is even for all m>=3. | Tiny reusable lemma only. |
| 826 | `MANUAL_EXACT` | Short k-window | If k>=sqrt(n), then tau(n+k)<=4(k+1); only k<sqrt(n) can be hard. | Finite-window reduction only. |
| 881 | `MANUAL_EXACT` | Order-1 endpoint construction | For k=1, take A=N and B={n:n≡2 mod4}; then A is minimal of order 1 and A\B is an asymptotic basis of order 2. | Only the k=1 endpoint. |
| 886 | `MANUAL_EXACT` | Easy epsilon>=1/2 endpoint | For epsilon>=1/2, the divisor interval has length <=1, so K=1 works. | Hard range 0<epsilon<1/2 remains. |
| 887 | `MANUAL_EXACT` | Infinite two-divisor cluster at n^(1/4) scale | For n=m(m-1)(m+1)(m+2), two explicit divisors lie in the target n^(1/4)-scale interval for all large m. | Shows K must be at least 2 for a fixed C infinitely often; not a refutation. |
| 912 | `MANUAL_EXACT` | Exponent-one primes in n! | v_p(n!)=1 iff n/2<p<=n, so their count is pi(n)-pi(floor(n/2)). | Structural component only. |
| 913 | `KNOWN_PUBLIC_PARTIAL` | Powerful-neighbour sparsity reduction | Distinct prime-factor exponents in n(n+1) force n or n+1 powerful; candidate count <=X is O(sqrt X). | Known public partial; no novelty claim. |
| 930 | `MANUAL_EXACT` | Infinite Pell family for k=2,r=2 | Pell solutions x^2-24y^2=1 generate infinitely many exact length-2 square-product examples. | Fixed stratum only; does not settle forall-r exists-k. |
| 936 | `MANUAL_EXACT` | Modulo-9 periodicity | 9 divides 2^n+1 iff n≡3 mod6. | Local obstruction only. |
| 949 | `CERTIFICATE_PLUS_TRANSFER` | Finite sum-free forcing with universal lift | For every sum-free S subset R, some q in {1,...,12} has q,2q notin S. | Superseded by the sharper q<=5 release; continuum target remains open. |
| 968 | `MANUAL_EXACT` | Prime-ratio monotonicity equivalence | For u_n=p_n/n and d_n=p_{n+1}-p_n, u_n<u_{n+1} iff n*d_n>p_n iff d_n>p_n/n. | Reformulation only. |
| 979 | `MANUAL_EXACT` | Prime-square parity obstruction and exact collision | For k=2, f_2(n)=0 at n≡3 mod4; f_2(410)=2 with {7,19} and {11,17}. | Finite/example-level structure only. |
| 985 | `MANUAL_EXACT` | Fermat-prime primitive-root subfamily | For every Fermat prime p>=5, 3 is a primitive root mod p. | Favorable subfamily only. |
| 1052 | `MANUAL_EXACT` | No odd unitary-perfect integer | There is no odd unitary-perfect integer n>1. | Does not settle finiteness of all unitary-perfect numbers. |
| 1052 | `MANUAL_EXACT` | Two-prime-factor unitary-perfect classification | The only unitary-perfect integer with exactly two distinct prime factors is 6. | Exactly-two-factor stratum only. |
| 1055 | `MANUAL_EXACT` | Class-1 smooth-shift barrier | A class-1 prime is exactly a prime p with p+1=2^a3^b, so its infinitude clause contains the open 3-smooth-shift prime problem. | Hardness reduction, not progress on infinitude. |
| 1060 | `MANUAL_EXACT` | Parity characterization for k*sigma(k) | k*sigma(k) is odd iff k is an odd square; also 12*sigma(12)=14*sigma(14)=336. | Structural characterization + collision only. |
| 1061 | `MANUAL_EXACT` | No diagonal sigma solutions | sigma(2a)>2 sigma(a) for every a>=1; hence sigma(a)+sigma(a)=sigma(2a) never. | Reduction only. |
| 1073 | `MANUAL_EXACT` | Large-prime-factor barrier for factorial-plus-one divisors | If u>1 divides n!+1, every prime factor p of u satisfies p>n; if u is composite then u>n^2. | Shape restriction only. |
| 1085 | `MANUAL_EXACT` | Exact one-dimensional unit-distance extremum | For n>=1, f_1(n)=n-1. | Dimension d=1 only. |
| 1085 | `KNOWN_PUBLIC_ROUTE` | Quadratic scale in dimensions d>=4 | For fixed d>=4, floor(n/2)ceil(n/2)<=f_d(n)<=binom(n,2), so f_d(n)=Theta(n^2). | Known construction/scale recovery. |
| 1094 | `KNOWN_BASELINE` | Sylvester prime-factor theorem | For n>=2k, C(n,k) has a prime factor >k. | Background theorem. |
| 1104 | `MANUAL_EXACT` | Monotonicity of triangle-free chromatic extremum | If f(n) is the maximum chromatic number of a triangle-free n-vertex graph, then f(n+1)>=f(n). | Structural lemma only. |
| 1192 | `MANUAL_REDUCTION` | No Sidon basis of order 2 | An order-2 basis needs A(x)>=(sqrt(2)-o(1))sqrt(x), while Sidon sets have <=(1+o(1))sqrt(x). | Square-sum condition is weaker than Sidon; not canonical refutation. |
