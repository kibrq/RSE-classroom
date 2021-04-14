#!/usr/bin/env python3


def solve(n, a):
    R, biggestNotDiv7, biggestDiv7 = 1, 0, 0
    for element in a:
        if element % 7 == 0:
            R = max(R, element * biggestNotDiv7)
            biggestDiv7 = max(element, biggestDiv7)
            continue
        R = max(R, element * biggestDiv7)
        biggestNotDiv7 = max(element, biggestNotDiv7)

    return R
