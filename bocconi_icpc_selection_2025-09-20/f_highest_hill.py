#!/usr/bin/env python3
"""
Contest: Bocconi ICPC Selection, September 2025 (Kattis)
Problem: F - Highest Hill

Problem in short:
    We are given n sampled heights h_1..h_n of a mountain range.
    A peak is a triple of indices 1 ≤ i < j < k ≤ n such that
        h_i ≤ ... ≤ h_j ≥ ... ≥ h_k.
    The height of the peak is min(h_j - h_i, h_j - h_k).
    Output the maximum possible peak height.

Idea:
    For each index j that can be the top of a peak we want:
      - L[j]: the smallest height on the non-decreasing run ending at j
              (the best possible h_i on the left),
      - R[j]: the smallest height on the non-increasing run starting at j
              (the best possible h_k on the right).

    We can compute these in two linear passes.

    From left to right:
        L[0] = h[0]
        if h[i-1] <= h[i], we extend the same non-decreasing slope and
            L[i] = L[i-1];
        otherwise we start a new slope and L[i] = h[i].

    From right to left:
        R[n-1] = h[n-1]
        if h[i] >= h[i+1], we extend a non-increasing slope and
            R[i] = R[i+1];
        otherwise R[i] = h[i].

    Index j can be the centre of a peak only if
        h[j-1] <= h[j] and h[j] >= h[j+1].

    For such j the best peak uses the whole slope on each side:
        height_j = min(h[j] - L[j], h[j] - R[j]).
    The answer is max height_j over all valid j.

    This runs in O(n) time and O(n) memory.
"""

import sys


def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    h = data[1:]

    L = [0] * n
    L[0] = h[0]
    for i in range(1, n):
        if h[i - 1] <= h[i]:
            L[i] = L[i - 1]
        else:
            L[i] = h[i]

    R = [0] * n
    R[-1] = h[-1]
    for i in range(n - 2, -1, -1):
        if h[i] >= h[i + 1]:
            R[i] = R[i + 1]
        else:
            R[i] = h[i]

    best = 0
    for j in range(1, n - 1):
        if h[j - 1] <= h[j] and h[j] >= h[j + 1]:
            left_min = L[j]
            right_min = R[j]

            d1 = h[j] - left_min
            d2 = h[j] - right_min
            height_j = d1 if d1 <= d2 else d2

            if height_j > best:
                best = height_j

    print(best)


if __name__ == "__main__":
    solve()
