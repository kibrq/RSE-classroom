n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]

dp = [-1] * 10
dp[0] = 0

for l, r in pairs:
    dpc = [-1 for i in range(10)]
    for x in [l, r]:
        for d in range(10):
            if dp[d] == -1:
                continue
            p = (d + x) % 10
            if dpc[p] == -1:
                dpc[p] = dp[d] + x
            dpc[p] = min(dpc[p], dp[d] + x)
    dp = dpc[::]


print(dp[sum(map(lambda p: max(p[0], p[1]), pairs)) % 10])
