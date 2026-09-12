"""Non-vacuous hunt: small INTEGER sequences, exhaustive over a bounded box."""
from fractions import Fraction as F
from itertools import combinations, product

NC = 7


def det(M):
    n = len(M)
    M = [r[:] for r in M]
    d = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]; d = -d
        d *= M[c][c]
        inv = F(1) / M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] * inv
            if f:
                for cc in range(c, n):
                    M[r][cc] -= f * M[c][cc]
    return d


def T(a, rows, cols):
    return det([[a[c - r] if 0 <= c - r < len(a) else F(0) for c in cols] for r in rows])


def consec_ok(a, rmax=3):
    for r in range(1, rmax + 1):
        for r0 in range(0, 3):
            for c0 in range(0, len(a) - r):
                if T(a, list(range(r0, r0 + r)), list(range(c0, c0 + r))) < 0:
                    return False
    return True


def gen_neg(a):
    for size in (2, 3):
        for rows in combinations(range(0, 4), size):
            for cols in combinations(range(0, 6), size):
                if list(rows) == list(range(rows[0], rows[0] + size)) and \
                   list(cols) == list(range(cols[0], cols[0] + size)):
                    continue
                v = T(a, list(rows), list(cols))
                if v < 0:
                    return (rows, cols, v)
    return None


VALS = [0, 1, 2, 3, 4, 6]
qual = 0
found = []
tested = 0
for tup in product(VALS, repeat=5):
    a = [F(1)] + [F(v) for v in tup] + [F(0)]
    tested += 1
    if not consec_ok(a):
        continue
    qual += 1
    b = gen_neg(a)
    if b:
        found.append((a[:6], b))
        if len(found) >= 6:
            break

print("   exhaustive over %d integer sequences in the box" % tested, flush=True)
print("   qualifying (all consecutive minors nonneg): %d" % qual, flush=True)
print("   of those with a NON-consecutive minor negative: %d" % len(found), flush=True)
print()
if qual == 0:
    print("   PROBE VACUOUS.", flush=True)
elif found:
    print("   *** COUNTEREXAMPLES: consecutive positivity does NOT imply total positivity.", flush=True)
    for a6, (rows, cols, v) in found[:6]:
        print("      a = %s   rows=%s cols=%s  minor = %s"
              % ([str(x) for x in a6], rows, cols, str(v)), flush=True)
else:
    print("   none in %d qualifying integer sequences." % qual, flush=True)
print()
print("DONE", flush=True)