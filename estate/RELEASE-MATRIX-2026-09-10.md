# Estate Release Matrix — 2026-09-10

**Author:** Jared Wilder  
**Purpose:** prevent omission-by-obscurity during the full mathematical estate release.

The reconstructed theorem atlas currently contains **1,571 theorem nodes** across dozens of domains, alongside 199 negative-theorem nodes and hundreds of findings/certificates. This matrix assigns each major domain a release disposition.

The disposition applies to the *domain as currently understood*, not automatically to every byte in every source archive.

## Meaning of dispositions

- **PUBLIC** — pure mathematics is already substantially represented in a public repository / release packet.
- **PUBLIC-PARTIAL** — a major clean extraction is public, but additional theorem records remain to be unpacked.
- **AUTHORITY-AUDIT** — apparently pure mathematics, but exact proof authority / hypotheses / current literature status need adjudication before promotion.
- **IP-HOLD** — mixed with product, patent, clinical, cryptographic or commercially load-bearing implementation material; only separable mathematics may be extracted.
- **APPLIED-HOLD** — science / biomedical / engineering findings are not part of the automatic pure-math release campaign.

## Domain census and current disposition

| domain | theorem nodes | disposition | public destination / action |
|---|---:|---|---|
| `erdos-271-stanley` | 278 | **PUBLIC** | `estate/ERDOS-271-STANLEY-SEQUENCES-2026-09-10.md`; full 184-entry source ledger remains provenance |
| `eg203-proof-package` | 112 | **PUBLIC** | `erdos203`, `erdos203-obstruction-calculus`, `eg203-eg411-corpus` |
| `06-all-theorem` | 77 | **PUBLIC-PARTIAL** | mixed master inventory; route pure rows into subject repos, do not dump IP-sensitive rows wholesale |
| `erdos-738-encirclement` | 62 | **PUBLIC-PARTIAL** | pure graph-theory transfer packet/index being released with #595 work |
| `erdos-595-encirclement` | 62 | **PUBLIC-PARTIAL** | `erdos595-barrier-tower` + graph-transfer release |
| `oracle-theoremos-0.9.` | 62 | **PUBLIC-PARTIAL** | formal source/statement corpus represented through `erdos152`, cable corpus and curated theorem set; per-statement semantic promotion remains gated |
| `eg411-proof-package` | 56 | **PUBLIC** | `erdos411`, `eg203-eg411-corpus`, retraction record; no false closure language |
| `eg203-killshot-round` | 55 | **PUBLIC** | EG203 repositories / corpus; exact claim ceilings retained |
| `erdos-500-encirclement` | 53 | **PUBLIC** | `combinatorial-records/erdos500/DELETION-DENSITY-INHERITANCE-TOOLKIT.md` |
| `high-gear-self` | 44 | **PUBLIC-PARTIAL** | low-rank fiber/CSP mathematics extracted into `lean-forge-graph-theory/fiber-coherence/` |
| `coherence-csp-self` | 42 | **PUBLIC-PARTIAL** | same fiber-coherence release; finite checks separated from universal claims |
| `relational-self-growth` | 42 | **PUBLIC-PARTIAL** | same pure CSP/relational theorem program |
| `erdos-738-x` | 41 | **PUBLIC-PARTIAL** | #738→#595 transfer packet; conditional theorems stay conditional |
| `fiber-coherence-self` | 40 | **PUBLIC-PARTIAL** | `lean-forge-graph-theory/fiber-coherence/README.md` |
| `permutation-gluing-self` | 38 | **PUBLIC-PARTIAL** | pure permutation/fiber obstruction material covered at theorem-program level; full record index still being unpacked |
| `theta-collision-self` | 34 | **PUBLIC-PARTIAL** | theta collision classification released in fiber-coherence packet |
| `erdos-595-self` | 32 | **PUBLIC-PARTIAL** | unconditional / conditional #595 theorem bank to be indexed explicitly |
| `unicycle-core-self` | 32 | **PUBLIC-PARTIAL** | rank-one fixed-point obstruction mathematics released; full per-record index still provenance debt |
| `encirclement-carry-free` | 32 | **IP-HOLD** | do not bulk release technical packet/encoding architecture; standalone `B_s` mathematics extracted separately |
| `the-six-vertex` | 30 | **AUTHORITY-AUDIT** | pure P6 / Erdős–Hajnal graph theory; next release after current-status and proof-authority audit |
| `vvc-terminal-encirclement` | 28 | **IP-HOLD** | mixed verified-behavior / product architecture; no automatic dump |
| `erdos-gyarfas-power` | 23 | **PUBLIC** | `lean-forge-graph-theory/erdos-gyarfas/ATTACK-AND-NEGATIVE-THEOREM-BANK.md` |
| `rank-three-kernel` | 21 | **PUBLIC-PARTIAL** | candidate tier published in fiber-coherence packet, explicitly not independently certified |
| `checkable-theorem-ledger` | 21 | **PUBLIC-PARTIAL** | mathematical/external theorem feedstock; subject-specific extraction rather than undifferentiated theorem claims |
| `science-findings-ledger` | 21 | **APPLIED-HOLD** | biomedical/science results are outside automatic math release and may overlap IP |
| `crown-action-os` | 18 | **IP-HOLD** | action-authorization / system mechanism explicitly inside patent-sensitive boundary |
| `caccetta-haggkvist-ch3` | 18 | **AUTHORITY-AUDIT** | apparently pure directed graph mathematics; release only with minimal-counterexample assumptions made explicit |
| `encirclement-rsi-frontier` | 17 | **IP-HOLD** | mixed research-system architecture |
| `humufinisher` | 17 | **IP-HOLD** | theorem / implementation family explicitly adjacent to patent docket |
| `eg203-analytic-nt` | 14 | **PUBLIC** | EG203 research corpus with source/dependency boundary |
| `rh-terminal-encirclement` | 11 | **AUTHORITY-AUDIT** | pure math but exceptionally high overclaim risk; no RH-equivalence statement promoted before exact independent audit |
| `directed-graph` | 8 | **AUTHORITY-AUDIT** | raw kernel theorem names exist; recover exact source / statements before public theorem claims |
| `eg203-20-more` | 8 | **PUBLIC** | EG203 corpus |
| `eg203-nuclear-codex` | 7 | **PUBLIC** | EG203 corpus / exact conditionality retained |
| `oracle-apex-0.8.0` | 7 | **AUTHORITY-AUDIT** | mixed autonomous-campaign result labels; subject-level proof extraction required |
| `frontier-alchemy-engine` | 6 | **IP-HOLD** | system architecture; only separable finite-CSP mathematics may be released |
| `infinite-kitchen-r2` | 6 | **IP-HOLD** | packet/capsule behavior machinery |
| `culinary-school-star` | 6 | **IP-HOLD** | behavior-summary/product mechanisms |
| `p6-lean-feed` | 6 | **AUTHORITY-AUDIT** | route with `the-six-vertex` packet |
| `eg203-lean-micro` | 6 | **PUBLIC** | EG203 formal corpus |
| `eg203-actual-close` | 6 | **PUBLIC** | public only with exact bounded/conditional scope; full #203 remains open |
| `humuhumunukunukuapuaa-finisher-2026` | 5 | **IP-HOLD** | same patent-sensitive lineage |
| `eg203-lean-unconditional` | 5 | **PUBLIC** | EG203 formal corpus |
| `eg203-hard-thing` | 5 | **PUBLIC** | EG203 corpus |
| `theorem-recipe-forge` | 4 | **PUBLIC-PARTIAL** | standalone signed sparse integer embeddings released; technical descendants held |
| `oracle-noosphere-0.6.` | 4 | **AUTHORITY-AUDIT** | autonomous result labels require claim-level extraction |
| `discrete_mathematics` | 4 | **PUBLIC-PARTIAL** | route individual pure statements to subject repositories |
| `p6-erdos-hajnal` | 3 | **AUTHORITY-AUDIT** | route with P6 packet |
| `agi-rerun-output` | 2 | **IP-HOLD** | finite-CSP theorem is separable, but surrounding system architecture is product-facing |
| `crown-acquisition-v9` | 2 | **IP-HOLD** | system |
| `three-way-recursive` | 2 | **IP-HOLD** | review for implementation disclosure before release |
| remaining EG203 microdomains | various | **PUBLIC** | consolidated in EG203 repos/corpus, keeping exact source scope |
| `erdosfire-frontier-math` | 2 | **PUBLIC-PARTIAL** | pure math statements can be extracted individually |
| `wilder-2026-paper` | 1 | **AUTHORITY-AUDIT** | inspect exact mathematical content vs applied/IP content |
| `logic`, `algebra`, `discrete_geometry`, `barrier`, `proof-obligations` | 1 each | **AUTHORITY-AUDIT** | inspect exact isolated statement before routing |
| `frontier-alchemy-representation` | 1 | **IP-HOLD / EXTRACTABLE-MATH** | minimal-no-good theorem may be public after stripping system implementation |

## Already public object-level evidence

The release also now contains an **audited 21-object witness vault** at:

`jaredwilder/combinatorial-records/witness-vault/AUDITED-WITNESS-VAULT-2026-09-10.md`

That vault includes exact independent validation metadata rather than relying on campaign status tokens.

## Saturation rule

A domain is not marked complete merely because one attractive theorem from it has been published.

`PUBLIC-PARTIAL` remains until either:

1. every surviving theorem identity has a public route, or
2. the unreleased residue is explicitly classified as duplicate, false/superseded, authority-audit debt, or IP-hold material.

That is the standard for calling this estate saturated.
