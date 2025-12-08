#!/usr/bin/env python3
"""
Contest: Bocconi ICPC Selection, September 2025 (Kattis)
Problem: D - Opening Ceremony

Problem in short:
    We have n tower blocks with heights h_i.
    In one move we can either:
      - remove all floors of a single tower, or
      - choose a floor x and remove that floor from every tower
        with height at least x.
    Find the minimum number of moves needed to remove all floors.

Idea:
    Let k be the number of horizontal shots.
    After k such shots, every tower with h_i > k must still be removed individually.
    The optimal k is 0 or equal to some tower height.

    We sort h, and for m = 0..n we let
        k = 0          if m = 0,
        k = h[m-1]     otherwise.
    Then at most (n - m) towers have height > k, so
        cost = k + (n - m).
    Taking the minimum over all m gives the answer in O(n log n).
"""

import sys

def solve():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    h = data[1:]
    h.sort()
    res = n 
  
    for m in range(n + 1):
        k = h[m - 1] if m > 0 else 0
        cost = k + (n - m)
        if cost < res:
            res = cost
    print(res)

if __name__ == "__main__":
    solve()

