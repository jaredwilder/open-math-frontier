# Human-First Editorial Standard for the September 2026 Mathematics Release

**Author:** Jared Wilder  
**Purpose:** keep public mathematical writing accurate, readable, and proportionate to the mathematics itself.

This release was produced from a large research estate containing theorem work, formal proof, computation, research logs, automated proof-search records, internal status systems, and historical corrections. Those internal systems are useful for provenance. They should **not** determine how a public mathematical result is introduced to a human reader.

The public standard is therefore:

> **State the mathematics first. State the evidence second. State the exact remaining limitation where it actually matters.**

## 1. The theorem statement controls the scope

If a theorem proves `P`, describe `P`.

Do not replace the theorem's scope with the status of a larger problem under which it was discovered.

An open parent conjecture can contain a completely proved child theorem, exact finite classification, structural reduction, or computational result. The parent problem being open does not make the child result tentative.

Likewise, a finite or conditional statement does not inherit a stronger conclusion by proximity to a solved theorem.

## 2. Lead with the strongest established mathematical content

A README or paper index should normally open in this order:

1. mathematical statement or result;
2. why it matters / what quantity or structure it changes;
3. proof, computation, certificate, or formalization method;
4. evidence boundary and remaining dependencies;
5. provenance, research history, failed routes, and internal workflow details.

Do not make a limitation the headline unless the limitation itself is the mathematical result—for example, a refutation, retraction, impossibility theorem, or formalization audit.

## 3. Do not warn against a stronger claim nobody made

Avoid reflexive prose such as:

- “THIS DOES NOT SOLVE THE WHOLE PROBLEM”;
- “NOT A THEOREM” when the actual category is “finite computation” or “candidate”;
- “NOT CLOSED” in a headline for a proved lemma;
- “this proves nothing about…” when the displayed theorem already states its domain.

Replace it with positive scope:

- “Exact classification for arithmetic-progression denominators.”
- “Finite exhaustive search through `N`.”
- “Candidate `f(4) >= 49`; remaining dependency: catalogue completeness.”
- “Countable analogue of Erdős #949.”

A mathematically competent reader can see that a theorem about a subfamily is a theorem about a subfamily.

## 4. Evidence classes describe verification, not importance

Useful evidence descriptions include:

- conventional proof;
- exact finite computation;
- independently reproduced computation;
- Lean theorem with disclosed axiom footprint;
- compiler-backed `native_decide` finite check;
- candidate result with a named unresolved dependency;
- research observation with held-out tests;
- unverified historical source claim.

Do not use the evidence label to rhetorically shrink the result. A finite theorem is still a theorem about a finite domain; a compiler-backed certificate is still a computational certificate; a candidate is best described by the precise dependency that keeps it a candidate.

## 5. Historical novelty is separate from mathematical correctness

A correct theorem can be new, rediscovered, classical, folklore, or of unresolved priority.

Say which literature search has been done and what remains uncertain. Do not downgrade mathematical correctness merely because novelty has not been adjudicated, and do not upgrade novelty merely because a result emerged from an independent computation.

## 6. Write for mathematicians, not for the internal research system

Historical filenames and directories may retain internal names for provenance. Public prose should translate them into ordinary language.

Avoid internal-system vocabulary in titles and first-contact prose when a standard mathematical phrase exists. Examples include:

- “attack surface” → “open-problem index” or “finite test interface”;
- “attack log” → “research log”;
- “kill” → “exclude,” “refute,” or “eliminate”;
- “weapon” → “argument,” “lemma,” or “method”;
- “gold inventory” → “result inventory”;
- “harvest” → “extraction” or “results”;
- “court” → “review” or “audit”;
- “blade” → “check” when discussing the public meaning rather than the historical tool name;
- “claim ceiling” → “scope”;
- “gate” → “check,” “review step,” or “verification condition”;
- “oracle” → describe the mathematical or computational object unless the historical name is itself relevant;
- “swarm,” “expedition,” “high-seam,” “mission,” “campaign” → use ordinary mathematical descriptions in the public summary.

The original filename can be shown in parentheses or a directory map when provenance matters.

## 7. Avoid model-centric self-description unless it is scientifically relevant

Do not headline a mathematical result with facts such as:

- number of language-model calls;
- which agent generated it;
- token counts;
- model names;
- “AI verified” / “AI discovered.”

If independence from a model is genuinely relevant to a verification claim, state it in the reproducibility section after describing the mathematical check itself.

The human reader cares first about the statement and whether the evidence can be reproduced.

## 8. Corpus scale is not theorem count

Large archives may contain hundreds of thousands of mathematical records, formulas, workflow events, Lean declarations, or structured fields.

When reporting corpus scale:

- name the unit in ordinary language;
- separate archive counts from curated result counts;
- distinguish source labels from adjudicated mathematics;
- avoid summing heterogeneous units into a synthetic “theorem count.”

Large-scale provenance is valuable on its own. It does not need to impersonate a theorem tally.

## 9. Corrections stay public, but corrections do not become the frame for unrelated work

Retractions, counterexamples, failed routes, and verification failures remain part of the public record.

They should be prominent when they affect the result being discussed. They should not be promoted into the title of an unrelated theorem bank merely to signal caution.

A correction record supports trust by showing what changed. It is not a universal disclaimer attached to everything else the author has done.

## 10. Prefer human mathematical nouns

Good public nouns:

- theorem;
- lemma;
- proposition;
- classification;
- reduction;
- construction;
- counterexample;
- certificate;
- finite search;
- formalization;
- proof attempt;
- research note;
- paper;
- archive;
- corpus;
- computation;
- literature search;
- open case.

These words already carry precise mathematical meaning. Prefer them over project-management or agent-system vocabulary.

## 11. Candidate results should name the dependency

A good candidate description says:

> **Candidate `f(4) >= 49`.** The finite capacity computation reproduces exactly; the remaining dependency is completeness of the cited external tournament catalogue.

A poor candidate description says:

> **NOT A THEOREM. DO NOT OVERCLAIM.**

The first tells the reader what exists and what remains. The second communicates anxiety rather than mathematics.

## 12. Formalization repos should distinguish three different questions

For Lean work, keep separate:

1. **statement formalization** — is the problem represented in Lean?
2. **formal proof** — is the proposition proved without `sorry` or unsupported axioms?
3. **source fidelity** — does the formal proposition actually match the intended mathematical statement?

A repository can make substantial progress on one layer without completing the others.

## 13. Reproducibility prose should say what a reader can actually do

Prefer:

> “Run `verify.py`; it recomputes all 59 finite optima and checks every witness.”

or

> “Two independently written implementations agree on all 22,082,109 covered subsets.”

over:

> “The system passed the hostile gate.”

Verification should be described as an executable mathematical action.

## 14. Suggested README shape

For a result repository:

```text
# Mathematical title

One- or two-sentence result statement.

## Result
Exact theorem / value / classification.

## Proof or computation
What establishes it.

## Verification / reproduction
How another person can check it.

## Literature / novelty status
Only if relevant.

## Remaining question
Only the actual remaining mathematical dependency.
```

For an archive or corpus:

```text
# Human description of the archive

What kinds of mathematical objects it contains and its scale.

## Selected mathematics
The strongest extracted objects first.

## Archive structure
Where to find the raw records.

## Evidence labels
How to interpret heterogeneous source statuses.

## Corrections
Only claims that actually require correction.
```

## 15. Final test

Before publishing front-facing prose, ask:

> **If the reader had never seen our agents, internal workflow, status labels, or research jargon, would this page still immediately tell them what the mathematics is?**

If not, rewrite it.

The target is neither hype nor self-deprecation. It is **accurate mathematical salience**: the strongest established statement receives the strongest visual and editorial emphasis it actually deserves.