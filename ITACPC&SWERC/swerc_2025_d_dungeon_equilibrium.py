#!/usr/bin/env python3
"""
Contest: SWERC 2025
Problem: D - Dungeon Equilibrium

Problem in short:
    We have n monsters with types a_i.
    A level is balanced if for every type x that appears, there are
    exactly x monsters of that type (and the empty level is also
    balanced). We may delete monsters and want the minimum deletions.

Idea:
    Let f[x] be the frequency of type x.
    For each x, in the final balanced array x must appear either 0 or x times.
    Minimum deletions for this x are:
        - f[x]        if f[x] < x  (delete all)
        - f[x] - x    if f[x] ≥ x  (keep exactly x)
    Summing over all x is the answer. We can compute f with a
    Counter and loop x = 0..n. Complexity O(n).
"""

import sys
from collections import Counter


def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:]

    cnt = Counter(a)
    ans = 0
    for x in range(n + 1):
        c = cnt[x]
        if c < x:
            ans += c
        else:
            ans += c - x

    print(ans)


if __name__ == "__main__":
    solve()
ve()
