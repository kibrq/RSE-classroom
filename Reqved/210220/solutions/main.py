#!/usr/bin/env python3

def F(n):
    if n <= 5:
        return n + 15
    if n % 2 == 0:
        return F(n // 2) + n ** 3
    return F(n - 1) + 2 * (n ** 2)


def digits(n, r):
    if n == 0:
        return [0]
    digs = []
    while n > 0:
        digs.append(n % r)
        n //= r
    return digs


def condition(n):
    cnt = 0
    for d in digits(n, 10):
        cnt += d == 5
    if not cnt > 0:
        return False
    for d in digits(n, 8):
        cnt -= d == 5
    return cnt == 0


N = 2021
ans = 0

for delta in range(2021):
    for n in map(lambda s: N + s * delta, [-1, 1]):
        if condition(F(n)):
            ans = n
    if ans > 0:
        break

print(ans)
