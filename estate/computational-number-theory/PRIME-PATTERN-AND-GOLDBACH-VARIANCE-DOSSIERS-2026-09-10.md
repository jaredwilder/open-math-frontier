# Prime-Pattern and Goldbach Variance — Bounded Computational Dossier Release

**Author:** Jared Wilder  
**Source reports:** 2026-05-18  
**Public release:** 2026-09-10

## Authority first

These are **empirical computational-number-theory dossiers, not theorems**. The source reports contain internal inconsistencies between their headline narratives, adversarial/killed-claim sections, and stated availability of raw data. This release therefore preserves only:

1. report-stated finite-range measurements;
2. the explicit comparator designs;
3. negative/falsified claims;
4. the source reports' own warnings about missing raw data and unsupported asymptotic narratives.

No asymptotic statement about primes, Goldbach representations, twin primes, cousin primes, or Sophie-Germain primes is promoted from these dossiers.

---

# I. Prime-pattern variance comparison

The source experiment compares three prime-pattern classes:

- twins `(p,p+2)`;
- cousins `(p,p+4)`;
- Sophie-Germain pairs `(p,2p+1)`.

The intended assay uses a segmented sieve over a finite interval, fixed-width counting windows, Fano factor `variance/mean`, and two main comparators:

- homogeneous Bernoulli at the empirical class rate;
- inhomogeneous Bernoulli informed by class-appropriate Hardy–Littlewood intensity.

The report explicitly warns that density-only models and primorial-resonance narratives are not sufficient without matched inhomogeneous comparators.

## Report-stated finite-range Fano curves

For the window widths

```text
W = [100, 420, 840, 1000, 1260, 10000, 100000]
```

the dossier records:

### Twin primes

```text
Fano_obs = [0.9008, 0.8410, 0.8330, 0.8243, 0.8058, 1.0572, 4.6672]
```

### Cousin primes

```text
Fano_obs = [0.8883, 0.8455, 0.8322, 0.8402, 0.8471, 1.1203, 4.5724]
```

### Sophie-Germain pairs

```text
Fano_obs = [1.2226, 2.2133, 3.5316, 4.0503, 4.8456, 32.6756, 324.0841]
```

At `W=1260`, the same report states an inhomogeneous Hardy–Littlewood comparator around

```text
SG Fano_obs = 4.8456
SG Fano_HL  = 4.9433
```

while the twins/cousins are still around `0.81–0.85` in the stated run.

These are **report-stated finite measurements**. This release-day pass has not independently regenerated their prime list, window counts, or comparator simulations.

## What the source itself killed

The dossier explicitly rejects or blocks stronger readings including:

- a universal “Modular Symmetry Lock” law;
- a universal phase-transition threshold at a primorial;
- using unproduced correlation/suppression metrics as evidence;
- claiming all linear prime patterns stay sub-Poissonian until a universal resonance breaks;
- treating density-only comparators as enough;
- claiming shuffled/sham controls establish structure without matched baselines;
- claiming all pattern Fano curves converge to one;
- claiming Sophie-Germain pairs follow the same variance curve as additive-gap pairs.

The source adversarial review specifically calls several precision claims **hallucinated relative to the evidence then available**. Those claims are not promoted here.

## Safe interpretation

Within the finite reported run, the three pattern classes behaved differently under the stated windowing scheme. That is a reproducible-computation target, not a theorem about asymptotic prime statistics.

---

# II. Goldbach representation-count variance

Let `r(2N)` denote the number of Goldbach representations under the source counting convention.

Two related dossiers explored finite-range variance, Hardy–Littlewood normalization, Fano factors, shuffled controls and spectral summaries.

## Critical source contradiction

One dossier begins by stating that the claimed crossover **cannot be confirmed because the required contiguous raw counts are missing**. Later pages in the same report present simulation/assay numbers and stronger prose. Another dossier likewise contains promoted claims that are later killed or adversarially rejected.

Therefore none of the headline “modular fractal,” “spectral masking,” “hyperuniform,” or asymptotic crossover narratives are release-grade findings.

## Report-stated raw-scale Fano measurements

One source table records, for example:

```text
scale ~10^4:
W=10   Fano_obs=23.2928
W=50   Fano_obs=23.7304
W=100  Fano_obs=23.7484

scale ~10^5:
W=10   Fano_obs=134.7219
W=50   Fano_obs=137.2011
W=100  Fano_obs=137.2584
```

The same table reports shuffled controls of broadly comparable order, which is itself a warning against attributing the raw overdispersion to a specific arithmetic mechanism without normalization.

A separate report later gives a very different normalized-table regime, including values such as

```text
W=10    Fano_obs=0.0002  Fano_shuff=0.1827
W=100   Fano_obs=0.0001  Fano_shuff=0.0180
W=1000  Fano_obs=0.0001  Fano_shuff=0.0223
W=5000  Fano_obs=0.0004  Fano_shuff=0.0215
```

and `Final_Scale_Delta_Obs_vs_Inhomo = 0.000388`.

Because the dossiers do not provide a single clean, independently replayed raw-data lineage tying all of these numbers to one frozen pipeline, this release preserves them as **historical report outputs only**.

## Correct experimental design retained from the dossiers

The strongest reusable asset is the assay design:

1. generate exact prime data with a validated segmented sieve;
2. compute exact `r(2N)` on contiguous even integers;
3. construct a local expected intensity using the Hardy–Littlewood singular series plus a fitted smooth scale term;
4. de-singularize the counts;
5. measure Fano curves over multiple fixed window widths;
6. compare against identical-grid homogeneous, inhomogeneous and block-shuffle controls;
7. use moving-block bootstrap intervals based on measured residual autocorrelation;
8. require an independent implementation cross-check before promotion.

The source explicitly says asymptotic inference is forbidden from the bounded experiment alone.

## Negative-result bank

Across the two Goldbach dossiers, the source itself kills or blocks claims including:

- simple Poisson representation counts;
- variance independent of the prime factors of `2N`;
- unnormalized Fano as evidence for a structural transition;
- singular-series slope alone as proof of long-range order;
- hyperuniformity claims without de-singularized residual tests;
- white-noise residual claims;
- phase-transition / “gas-to-crystal” narratives without contiguous validated raw counts;
- using a single spectral statistic as a stand-in for the required variance assay;
- large-scale extrapolation beyond the tested interval.

Several high-precision metrics were explicitly flagged by the adversarial review as unsupported or hallucinated relative to the source evidence available at that stage.

---

# III. Why this is public

The point of this release is not to preserve every seductive interpretation. It is to preserve the **measured-or-claimed finite outputs, the comparator machinery, the contradictions, and the killed narratives** so future work does not start from a cleaned-up mythology of the experiment.

## Claim ceiling

- no Goldbach conjecture progress is claimed;
- no twin-prime theorem is claimed;
- no Hardy–Littlewood error-term theorem is claimed;
- no asymptotic variance law is claimed;
- no “modular symmetry lock,” “spectral masking,” or “fractal” law is promoted;
- all listed numerical outputs remain finite-range source-report measurements until independently replayed from raw counts.

This is a **computational-math provenance release** below theorem authority.