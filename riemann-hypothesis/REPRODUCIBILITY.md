# Reproducibility notes

## Source archive

This publication pass was made from the 1,284-file session export supplied on 2026-09-12. Its SHA-256 is recorded in `MANIFEST.sha256`.

## Fresh reruns performed during the publication pass

The following recovered programs were rerun directly from the exported source on 2026-09-12:

- `branch-c/criterion_is_not_sufficient.py` — reproduced `3059` non-real-rooted objects and `1686` false admissions.
- `branch-c/criterion_kill_audit.py` — reproduced `2284` full-depth/interior non-real-rooted objects and `1445` false admissions in both criterion forms.
- `branch-c/consecutive_is_not_total.py` — reproduced the exact negative non-consecutive minor, beginning with `a=(1,0,0,0,0,1)` and value `-1`.
- `theta-kernel/row_is_log_concavity.py` — reproduced the exact algebraic equivalence check and the reported normalized-moment ratios through `k=9`.
- `branch-b/chebyshev_probe.py` — freshly recomputed the finite prime-power table through `x=200000`.

The heavier rational enclosure scripts in `theta-kernel/` are published together with their archived output logs from the source session. They were not all freshly rerun during this publication pass; the distinction is intentional.

## Suggested commands

```bash
python branch-c/criterion_is_not_sufficient.py
python branch-c/criterion_kill_audit.py
python branch-c/consecutive_is_not_total.py
python theta-kernel/row_is_log_concavity.py
python branch-b/chebyshev_probe.py
```

## Formal files

The recovered Lean files are tiny and contain no `sorry`. A Lean executable was not available in the publication runtime, so this release does not claim a fresh compile on 2026-09-12. Source recovery and fresh compiler verification are kept distinct.