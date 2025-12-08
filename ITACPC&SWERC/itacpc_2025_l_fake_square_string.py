#!/usr/bin/env python3
"""
Contest: ITACPC 2025
Problem: L - Fake Square String

Problem in short:
    Carlos builds a string by:
      1) choosing a string x,
      2) forming x + x,
      3) inserting one extra character at any position.
    Given the final string s, output the character inserted in step 3.

Idea:
    In x + x every character appears an even number of times.
    After inserting one extra character c, c is the only character whose
    total count in s is odd. We count frequencies of all letters and
    return the one with odd parity. This is O(n) with constant memory.
"""

import sys


def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]

    cnt = [0] * 26
    for ch in s:
        idx = ord(ch) - 97
        cnt[idx] ^= 1

    for i in range(26):
        if cnt[i]:
            print(chr(97 + i))
            break


if __name__ == "__main__":
    solve()
