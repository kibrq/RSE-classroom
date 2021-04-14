#!/usr/bin/env python3

def solve(n, arr):
    R = 1
    for i in range(n):
        for j in range(i):
            if arr[i] * arr[j] % 7 == 0 and arr[i] * arr[j] % 49 != 0:
                R = max(R, arr[i] * arr[j])
    return R
