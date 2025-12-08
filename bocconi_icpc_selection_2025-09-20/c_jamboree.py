#!/usr/bin/env python3
"""
Contest: Bocconi ICPC Selection, September 2025 (Kattis)
Problem: C - Jamboree

Problem in short:
    There are N items with sizes a_i and M scouts.
    Each scout can carry at most two items; the load of a scout is the
    sum of sizes of the items they carry.
    Distribute the items to minimize the maximum load of any scout.

Idea:
    Sort the sizes. If N <= M, every item can be carried alone and the
    answer is max(a_i).

    Otherwise, some scouts must carry two items. Let p = N - M >= 1.
    Exactly p scouts carry two items (2p items total) and the remaining
    N - 2p items are carried alone. To minimize the maximum load, the
    single items should be the largest ones, so the 2p smallest items
    are used for pairs. Among these, we pair smallest with largest:
        (a_0, a_{2p-1}), (a_1, a_{2p-2}), ...
    The maximum pair sum over these pairs is one candidate; the other
    candidate is the largest single item (if any).
    The answer is the maximum of these values. Complexity O(N log N).
"""

import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    n, m = data[0], data[1]
    a = data[2:]
    a.sort()

    p = max(0, n - m)
    res = 0

    for i in range(p):
        s = a[i] + a[2 * p - 1 - i]
        if s > res:
            res = s

    if 2 * p < n and a[-1] > res:
        res = a[-1]

    print(res)


if __name__ == "__main__":
    solve()
