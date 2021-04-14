#!/usr/bin/env python3

'''
F(n) = G(n) + F(n - 1), n > 1
F(1) = 1

G(n) = F(n - 1), n > 1
G(1) = 1
'''

def F(n):
    if n <= 1:
        return 1
    return G(n) + F(n - 1)

def G(n):
    if n <= 1:
        return 1
    return F(n - 1)

res = 0
for n in range(10):
    if (F(n) + G(n)) % 6 == 0:
        res += 1
print(res)
