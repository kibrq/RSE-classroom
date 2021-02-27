#!/usr/bin/env python3

def F(n):
    if n <= 5:
        return n + 15
    if n % 2 == 0:
        return F(n // 2) + n ** 3 - 1
    return F(n - 1) + 2 * (n ** 2) + 1


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
    print(digits(n, 10), digits(n, 8))
    for d in digits(n, 10):
        cnt += d == 5
    if cnt == 0:
        return False
    for d in digits(n, 8):
        cnt -= d == 5
    return cnt == 0


N = 2021
ans = 0

for delta in range(N):
    for n in map(lambda s: N + s * delta, [-1, 1]):
        if condition(F(n)):
            ans = n
    if ans > 0:
        break

print(ans)
