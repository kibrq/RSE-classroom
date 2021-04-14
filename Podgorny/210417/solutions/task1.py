#!/usr/bin/env python3

'''
F(n) = F(n - 1), n = 1, 3, 5, ...
F(n) = F(n - 1) + 1, n = 2, 4, 6, 8, ...
F(n) = 100, n <= 0
'''

def F(n):
    if n <= 0:
        return 100
    if n % 2 == 0:
        return F(n - 1) + 1
    else:
        return F(n - 1)


def digits_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

print(F(10), F(100))
print(digits_sum(F(10)) + digits_sum(F(100)))

