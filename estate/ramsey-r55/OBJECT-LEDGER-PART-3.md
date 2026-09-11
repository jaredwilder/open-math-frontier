# R(5,5) Estate Object Index — Part 3

Objects 79–117 of 117. Recovered source statuses are provenance, not fresh adjudication.

## P1-D2 — D2

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** Campaign defect retained by the session; exact original wording is not restated in the final packet and remains source-linked rather than guessed.
- **Provenance:** transcript defect ledger

## P1-D3 — D3

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** The launched R(5,5) lane had not terminated; later CLEARED when W4 returned an honest NO_VERDICT.
- **Provenance:** transcript defect ledger

## P1-D4 — D4

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** Three launches were refused for an undeclared proxy; the question guard was right.
- **Provenance:** transcript defect ledger

## P1-D5 — D5

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** Estate instrument conflict: overnight_question_guard required a flag that oracle/run.py refused to parse; worked around by wrapper, not repaired.
- **Provenance:** transcript defect ledger

## P1-D6 — D6

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** A launch was refused for buffered output; without the guard the session could have narrated from a stale file.
- **Provenance:** transcript defect ledger

## P1-D7 — D7

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** The extension instrument wrote nothing until return, so it was blind by construction; relaunch inherited the defect.
- **Provenance:** transcript defect ledger

## P1-D8 — D8

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** The session oversubscribed the machine with seven processes and attempted to kill operator compute; the guard correctly refused.
- **Provenance:** transcript defect ledger

## P1-D9 — D9

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** R9 had a field-name collision: key t named both the Ramsey parameter and elapsed seconds, silently overwriting the parameter.
- **Provenance:** transcript defect ledger

## P1-D10 — D10

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** R6 DIFFICULTY_DELTA asserted an unchecked explanation; W28 later refuted the explanation while the measured result survived.
- **Provenance:** transcript defect ledger

## P1-D11 — D11

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** FAMILY_SCOPE EXHAUSTIVE named a prose domain without enumerating the actual set; W28 omitted held objects and enabled a false generalization.
- **Provenance:** transcript; final defect ledger at record 515

## P1-D12 — D12

- **Category:** `MSL_OR_HARNESS_DEFECT`
- **Source status:** `SOURCE_DEFECT`
- **Claim:** Original /jexport omitted scratchpad artifacts while claiming nothing was left behind. The new scratchpad-enabled export fixes this corpus-level preservation hole.
- **Provenance:** transcript; final defect ledger at record 515

## P2-WIT-30-seed30 — seed30.json

- **Category:** `EXACT_WITNESS_ARTIFACT`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** Preserved K5-free witness object on n=30; independent estate-side from-definition replay returns no red K5 and no blue K5. Red/blue K4 counts 248/239.
- **Provenance:** scratchpads/scratchpad/r55/seed30.json

## P2-WIT-31-seed31 — seed31.json

- **Category:** `EXACT_WITNESS_ARTIFACT`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** Preserved K5-free witness object on n=31; independent estate-side from-definition replay returns no red K5 and no blue K5. Red/blue K4 counts 281/283.
- **Provenance:** scratchpads/scratchpad/r55/seed31.json

## P2-WIT-34-seed34 — seed34.json

- **Category:** `EXACT_WITNESS_ARTIFACT`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** Preserved K5-free witness object on n=34; independent estate-side from-definition replay returns no red K5 and no blue K5. Red/blue K4 counts 414/459.
- **Provenance:** scratchpads/scratchpad/r55/seed34.json

## P2-WIT-36-seed36 — seed36.json

- **Category:** `EXACT_WITNESS_ARTIFACT`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** Preserved K5-free witness object on n=36; independent estate-side from-definition replay returns no red K5 and no blue K5. Red/blue K4 counts 540/583.
- **Provenance:** scratchpads/scratchpad/r55/seed36.json

## P2-WIT-36-cayley36 — cayley36.json

- **Category:** `EXACT_WITNESS_ARTIFACT`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** Preserved K5-free witness object on n=36; independent estate-side from-definition replay returns no red K5 and no blue K5. Red/blue K4 counts 612/360.
- **Provenance:** scratchpads/scratchpad/r55/cayley36.json

## P2-WIT-40-seed_best — seed_best.json

- **Category:** `EXACT_WITNESS_ARTIFACT`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** Preserved K5-free witness object on n=40; independent estate-side from-definition replay returns no red K5 and no blue K5. Red/blue K4 counts 921/893.
- **Provenance:** scratchpads/scratchpad/r55/seed_best.json

## P2-EXT-30-31 — Exact 30→31 untouched extension

- **Category:** `EXACT_EXTENSION_ARTIFACT`
- **Source status:** `ESTATE_BYTE_DERIVED`
- **Claim:** The preserved 31-vertex object restricts EXACTLY to seed30 on all old edges. Its new vertex has red neighbourhood A=[0, 1, 7, 8, 10, 11, 12, 15, 17, 19, 21, 22, 27, 28].
- **Provenance:** seed30.json + seed31.json

## P2-EDGE-seed30-seed31 — 30→31 exact extension

- **Category:** `SEARCH_MECHANISM_MEASUREMENT`
- **Source status:** `ESTATE_BYTE_DERIVED`
- **Claim:** Restriction comparison changes 0 of 435 old edges (0.00%).
- **Provenance:** seed30.json vs seed31.json

## P2-EDGE-seed34-seed36 — 34→36 seeded repair

- **Category:** `SEARCH_MECHANISM_MEASUREMENT`
- **Source status:** `ESTATE_BYTE_DERIVED`
- **Claim:** Restriction comparison changes 299 of 561 old edges (53.30%).
- **Provenance:** seed34.json vs seed36.json

## P2-EDGE-seed36-seed_best — 36→40 seeded repair

- **Category:** `SEARCH_MECHANISM_MEASUREMENT`
- **Source status:** `ESTATE_BYTE_DERIVED`
- **Claim:** Restriction comparison changes 318 of 630 old edges (50.48%).
- **Provenance:** seed36.json vs seed_best.json

## P2-CNF-42 — Exact R(5,5) CNF at n=42

- **Category:** `FINITE_CERTIFICATE_INTERFACE`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** p cnf 861 1701336; 1701336 clause lines present. LF-normalized logical-clause SHA-256 = fb5ee4fb6c3981aa87c72a5aa73a4f23cc6fbedc549a997e0cbfead50b48e14c, matching the transcript-generated digest. Whole-file SHA-256 = 2058a54abba4325ec0d61bb6812c3c185fff408e5edda4ceb847316e50b07e4f.
- **Provenance:** scratchpad/r55/r55_n42.cnf

## P2-CNF-43 — Exact R(5,5) CNF at n=43

- **Category:** `FINITE_CERTIFICATE_INTERFACE`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** p cnf 903 1925196; 1925196 clause lines present. LF-normalized logical-clause SHA-256 = 9cb36cfd39aebd5a37a1c2115efa20f76332a55ab4c224da2ac7ccee249882be, matching the transcript-generated digest. Whole-file SHA-256 = 25e64fe3dbe792dc3fe4ee54d2d7a08c2fbc705a119928bfbb3cd73c163965aa.
- **Provenance:** scratchpad/r55/r55_n43.cnf

## P2-LEAN-INTERFACE — R55.lean two-hole close interface

- **Category:** `FORMALIZATION_INTERFACE`
- **Source status:** `SOURCE_ARTIFACT`
- **Claim:** Self-contained Lean file defines Colouring, MonoK5, LowerCertificate, UpperCertificate, RamseyFiveFiveIs; close_CC55 composes exactly gap1_at_42 and gap2_at_43, and the two gaps are the only explicit sorry sites in the preserved file.
- **Provenance:** scratchpads/scratchpad/r55/R55.lean

## P2-ONESHOT-CODE — oneshot.py exact one-vertex oracle

- **Category:** `EXECUTABLE_ATTACK`
- **Source status:** `SOURCE_ARTIFACT`
- **Claim:** Preserved executable encodes K19 as n SAT variables with one clause per red K4 and one per blue K4; UNSAT is decisive for the fixed base.
- **Provenance:** scratchpads/scratchpad/r55/oneshot.py

## P2-EXT2-CODE — ext2exact.py exact two-vertex oracle

- **Category:** `EXECUTABLE_ATTACK`
- **Source status:** `SOURCE_ARTIFACT`
- **Claim:** Preserved executable uses 2n+1 variables; one-vertex K4 constraints plus K3 intersection constraints conditioned on the colour of uv. For seed30 the source-recorded run is 61 vars / 1898 clauses / UNSAT.
- **Provenance:** scratchpads/scratchpad/r55/ext2exact.py

## P2-CAYLEY-REPLAY — Deterministic Cayley36 replay

- **Category:** `STRUCTURED_WITNESS`
- **Source status:** `ESTATE_REPLAYED`
- **Claim:** Re-running the preserved deterministic seed reproduces the Z6×Z6 witness after 10,797 sampled connection sets and yields the exact 18-element symmetric connection set recorded in PASS2-SCRATCHPAD-GOLD.md.
- **Provenance:** scratchpads/scratchpad/r55/cayley.py; cayley36.json

## P2-EXPORT-D12-FIX — D12 is materially fixed in this new export

- **Category:** `EXPORT_INFRASTRUCTURE`
- **Source status:** `ESTATE_VERIFIED`
- **Claim:** metadata/MANIFEST report 39 scratchpad files, 169,697,131 scratchpad bytes; the witness JSONs, scripts, logs, Lean interface and both huge CNFs are physically present.
- **Provenance:** EXPORT-MANIFEST.json; source MANIFEST.json

## P2-ORE-NOISE — Inherited hook context dominates naive ore ranking

- **Category:** `EXPORTER_FINDING`
- **Source status:** `ESTATE_OBSERVATION`
- **Claim:** The heuristic ore index ranks many detached hook/VVC standing facts above session-local R(5,5) results. Session-local semantic mining works, but ore acceleration should split INHERITED_CONTEXT from SESSION_LOCAL evidence.
- **Provenance:** ore/ore_candidates.jsonl

## P2-BASH-MUTATION-GAP — Write/Edit ledger sees zero mutations despite many scratchpad artifacts

- **Category:** `EXPORTER_FINDING`
- **Source status:** `ESTATE_OBSERVATION`
- **Claim:** This session creates files through Bash/heredocs and Python, so tool-level Write/Edit replay reports 0/0 while scratchpad capture contains the final bytes. The estate is complete enough for final-state mining, but shell-side mutation lineage needs its own index.
- **Provenance:** EXPORT-MANIFEST.json; raw/transcript.jsonl

## P2-ARCHIVE-SCALE — Large scratchpads stress archive creation

- **Category:** `EXPORTER_FINDING`
- **Source status:** `ESTATE_OBSERVATION`
- **Claim:** The deterministic estate directory completes, but v0.1 compression at level 9 exceeded the execution window on the ~170 MB CNF-heavy scratchpad. Fast/hybrid compression is required for production exports.
- **Provenance:** runtime test of msl_estate_export.py v0.1

## P3-EXTENSION-DEPTH — Untouched extension depth e(G)

- **Category:** `DERIVED_THEOREM_OR_INVARIANT`
- **Source status:** `DERIVED_FROM_SOURCE`
- **Claim:** Define e(G)=max k such that k new vertices can be appended without changing the base while preserving K5-freeness. Source results give e(seed30)=1; e(seed31)=e(seed34)=e(seed36)=e(cayley36)=e(seed40)=0 for the tested objects.
- **Provenance:** K19,K21,W29,W30,W31,W28/RR8

## P3-GENERAL-EXT-K — Exact k-vertex extension criterion

- **Category:** `DERIVED_THEOREM_SCHEMA`
- **Source status:** `DERIVED_FROM_SOURCE`
- **Claim:** For a fixed K5-free base G and k new vertices, an extension is K5-free iff for every monochromatic j-clique among the new vertices (1≤j≤min(k,5)), the common same-colour neighbourhood in G contains no same-colour K_{5-j}; j=5 is the no-base-vertex case. K19 and K21 are j≤1 and j≤2 special cases, while K22 records the descending obstruction orders.
- **Provenance:** K19; K21; K22

## P3-FIXED-K-SAT — Fixed-k extension has a compact exact SAT encoding

- **Category:** `DERIVED_EXECUTABLE_ARCHITECTURE`
- **Source status:** `DERIVED_FROM_SOURCE`
- **Claim:** Use kn + C(k,2) Boolean edge-colour variables. For each j≤min(k,5), each j-subset of new vertices and each base K_{5-j}, emit clauses forbidding the corresponding monochromatic K5. For fixed k the base-side enumeration is O(n^4), a dramatic reduction from recolouring all C(n+k,2) edges.
- **Provenance:** oneshot.py; ext2exact.py; K22

## P3-REPAIR-DISTANCE — Global repair crosses chambers by massive base rewrites

- **Category:** `DERIVED_SEARCH_INSIGHT`
- **Source status:** `ESTATE_BYTE_DERIVED`
- **Claim:** The successful 34→36 and 36→40 runs alter about half of the inherited old edges (53.3% and 50.5%), whereas the exact 30→31 extension alters none. The right model is not “add a vertex and locally patch”; it is “use a prior witness as a warm start for a new graph search.”
- **Provenance:** seed34 vs seed36; seed36 vs seed40; seed30 vs seed31

## P3-SEARCH-OBJECTIVE — Two-coordinate search state

- **Category:** `DERIVED_SEARCH_ARCHITECTURE`
- **Source status:** `DERIVED_FROM_SOURCE`
- **Claim:** Search should track both monochromatic-K5 defect E(G) and exact extension state/depth e(G), rather than E(G) alone. Exact UNSAT information can identify dead extension chambers and guide base rewrites.
- **Provenance:** R14; W28; W29; W31; P3-EXTENSION-DEPTH

## P3-SCOPE-LEDGER-LAW — EXHAUSTIVE must bind an enumerated domain object

- **Category:** `MSL_LANGUAGE_DERIVATION`
- **Source status:** `DERIVED_FROM_SOURCE`
- **Claim:** D11 is mechanically preventable: FAMILY_SCOPE EXHAUSTIVE should reference a machine-generated domain ledger/hash, not a prose phrase such as “all campaign-held objects.” The exporter can generate that ledger from certified-object inventory.
- **Provenance:** D11; RR8; W28; EA1

## P3-SOURCE-FIRST-CLOSE — Known explicit witness ingestion should precede rediscovery

- **Category:** `CLOSE_GRAMMAR_DERIVATION`
- **Source status:** `DERIVED_FROM_SOURCE`
- **Claim:** When the close contract requires independent verification rather than independent discovery, SOURCE→OBJECT→independent verifier is a legal direct route and should be attempted before many rounds of rediscovery. This is the R15 lesson from the audit.
- **Provenance:** R15; EA1

## P3-COURT-OF-RECORD — Deterministic archaeology and semantic mining should remain separate

- **Category:** `ESTATE_ARCHITECTURE`
- **Source status:** `WORKFLOW_DERIVATION`
- **Claim:** The estate layer should certify bytes, chronology, scopes, receipts and artifact presence; the semantic passes should harvest generously; adjudication/novelty stay later. This corpus demonstrates that separation prevents both lost artifacts and premature downgrading.
- **Provenance:** estate test