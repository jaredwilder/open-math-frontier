# Human-first editorial standard for the public mathematics estate

**Author:** Jared Wilder

The public repositories should read like mathematics, not like the internal machinery that produced them.

The governing rule is:

> **State the mathematical object. State the main result. Explain why it matters. Then give the proof or computation and a reproducible way to check it.**

This is consistent with long-standing mathematical-writing advice from the AMS—make the opening comprehensible to a mathematician outside the specialty and state the principal results early—as well as modern research-software guidance from GitHub and JOSS: tell readers what the project does, why it is useful, how to use or verify it, and how it relates to existing work.

## 1. The first thirty seconds

A mathematician opening a repository should be able to answer, without scrolling through workflow history:

1. **What object are we studying?**
2. **What is the strongest established result here?**
3. **Why is that result interesting?**
4. **How was it proved or computed?**
5. **Where do I go to check the details?**

If the README does not answer those questions near the top, rewrite it.

A good opening usually needs only two or three paragraphs: define the object, display the theorem/value/classification, and give one sentence of context.

## 2. Main theorem before project history

The theorem statement controls the scope.

If the repository proves `P`, describe `P`. Do not replace it with the status of the larger conjecture that motivated the work.

A strong default order is:

1. main theorem / exact value / classification;
2. mathematical context and significance;
3. proof idea or computational method;
4. reproduction instructions;
5. literature and novelty status;
6. remaining mathematical question;
7. provenance and research history.

The AMS author manual gives the same basic advice in paper form: the first paragraph should locate the subject for any mathematician, the principal result should appear as soon as feasible, and a theorem should be stated before its proof.

## 3. Use ordinary mathematical nouns

Prefer:

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
- computation;
- literature search;
- open case.

Internal vocabulary can survive in historical filenames, but not as the public explanation when a standard mathematical phrase exists.

Translate, for example:

- `court` → review, theorem bank, or verification;
- `kill` → exclude, refute, eliminate;
- `gate` → check, verification condition;
- `gold` → result, theorem, finding;
- `attack` → proof attempt, research program;
- `oracle` → the actual mathematical or computational object;
- `swarm`, `expedition`, `mission` → omit or translate into the mathematical task.

## 4. Do not lead with anxiety

Avoid front-page prose such as:

- “THIS DOES NOT SOLVE THE WHOLE PROBLEM”;
- “NOT A THEOREM” when the object is an exact finite computation;
- “NOT CLOSED” as the headline of a proved child theorem;
- long disclaimers about claims nobody made.

Use positive scope instead:

- “Exact classification for arithmetic-progression denominators.”
- “Exhaustive search through `N=...`.”
- “Candidate `f(4)≥49`; remaining dependency: completeness of the cited tournament catalogue.”
- “Countable finite-sums theorem.”

A reader can see the scope from the theorem statement.

## 5. Separate correctness, verification, and novelty

These are different questions.

### Mathematical correctness

What exactly is proved or computed?

### Verification method

How was it checked?

Useful descriptions include:

- conventional proof;
- exact finite computation;
- independently reproduced computation;
- Lean theorem with disclosed axiom footprint;
- compiler-backed finite decision;
- SAT/UNSAT certificate;
- candidate result with one named unresolved dependency.

### Historical novelty

Is the result new, rediscovered, classical, folklore, or not yet adjudicated?

Do not downgrade a correct theorem because novelty is unresolved, and do not upgrade novelty because an independent computation found it.

## 6. Formalization repositories must distinguish three layers

For Lean work, keep separate:

1. **statement formalization** — the intended mathematical statement exists in Lean;
2. **formal proof** — the proposition is proved with the disclosed trust boundary;
3. **source fidelity** — the Lean proposition actually matches the source mathematics.

A clean kernel proof of the wrong proposition is still the wrong proposition. A correct statement with `sorry` is a statement formalization, not a proof.

Readers should be able to tell which layer they are looking at without interpreting project-specific status codes.

## 7. Computational mathematics should be reproducible from the README

For an exact finite result, state:

- the finite universe;
- the quantity being optimized or classified;
- the answer;
- the witness or certificate, when practical;
- the exhaustive method;
- the exact command that replays the check;
- the trust boundary if a solver or compiler is involved.

Prefer:

> `python verify.py` recomputes all 59 finite optima and checks every witness.

over:

> the campaign passed its hostile verification gate.

JOSS review criteria use essentially the same standard for research software: a reviewer should be able to understand the purpose, install or run the software, exercise its core functionality, and verify that it works.

## 8. Explain why the result matters, but do not advertise

One or two sentences of significance are valuable. Marketing language is not.

Good:

> “The identity converts a potentially large minimum counterexample into a matching-dominated cubic skeleton with a bounded exceptional core.”

Bad:

> “A revolutionary frontier theorem that changes everything.”

Let the theorem carry the weight.

## 9. Counts are supporting information, not the headline

Large archives may contain thousands of files, theorem records, formal declarations, or proof-search events. Those counts can be useful, but they are not substitutes for mathematical content.

On a subject repository, prefer:

> “Every continuum-sized graph is countably coverable by triangle-free subgraphs.”

before:

> “27 Lean files and 65 theorem cards.”

For an archive repository, corpus scale may properly be the subject—but name the unit precisely and distinguish raw records from reviewed mathematics.

## 10. Corrections remain public without swallowing the page

Retractions, counterexamples, and failed routes belong in the public record when they affect a claim.

They should not become universal disclaimers for unrelated mathematics. A correction belongs next to the theorem or route it corrects.

When an entire repository is itself a correction record, say so plainly and preserve the historical source. Otherwise, lead with the surviving mathematics.

## 11. A README is a front door, not an archive dump

GitHub's own README guidance emphasizes five questions: what the project does, why it is useful, how to get started, where to get help, and who maintains it.

For a mathematical result repository, adapt that to:

```text
# Mathematical title

One- or two-sentence statement of the object and main result.

## Main result
The theorem, value, classification, or construction.

## Why it matters
A short mathematical interpretation.

## Proof / computation
The essential method.

## Reproduce
Commands, dependencies, certificates, or Lean build instructions.

## Literature
Only what a reader needs to place the result.

## Remaining question
Only the real unresolved mathematical dependency.
```

For an archive:

```text
# Human description of the archive

What mathematical material it contains and why the archive exists.

## Selected mathematics
The strongest extracted objects first.

## Archive map
Where the source records live.

## Evidence labels
How historical statuses should be interpreted.

## Corrections
Only the corrections that actually matter here.
```

## 12. Citeable repositories should be easy to cite

Serious research repositories should make authorship, title, license, and preferred citation unambiguous. Where useful, add a `CITATION.cff`; GitHub recognizes it natively and the Citation File Format is designed to make software and datasets straightforward to cite.

A repository that corresponds to a paper should link the paper prominently. A repository that is itself the primary research object should make that clear rather than forcing readers to infer which archive copy is canonical.

## 13. Human-readable mathematics outranks historical filenames

Historical filenames may remain strange for provenance. Do not rename source artifacts if doing so would break hashes or chronology merely to make them pretty.

Instead, create a clear reading surface above them:

> “The proof is in `CH3-BIG-GUNS-MASTER-DOSSIER.md` (historical filename). The main theorem is …”

The repository should translate the archive for the reader rather than requiring the reader to learn the archive's dialect.

## 14. The final test

Before publishing or revising a README, ask:

> **If a mathematician arrived here from a paper citation or search result and knew nothing about the internal research system, would the first screen immediately tell them what the mathematics is?**

If not, rewrite it.

The target is not hype and not defensive understatement. It is **accurate mathematical salience**: the strongest established statement receives the strongest editorial emphasis it actually deserves.

## Research basis

This standard draws on:

- American Mathematical Society author guidance: make the opening comprehensible beyond the specialty, state principal results early, and state the theorem before its proof;
- GitHub's README guidance: explain what the project does, why it is useful, and how a reader gets started;
- Journal of Open Source Software review criteria: clear statement of need, relation to prior work, documentation, examples, tests, reproducibility, and references;
- Citation File Format guidance for machine- and human-readable citation metadata.

The sources inform the presentation standard; mathematical claims remain governed by their own proofs, computations, and cited literature.