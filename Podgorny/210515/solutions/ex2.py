#!/usr/bin/env python3

for x in range(10 ** 5):
    y = x
    k = x % 8
    a = 0
    b = 0
    while x > 0:
      d = x % 8
      if d == k:
        a += 1
      b += d
      x //= 8
    if a == 4 and b == 11:
        print(y)
