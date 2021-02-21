'''
Из числа n можно получить n + 3, n + 7, n * 2, n * 3
Сколько способов из 1 получить N.
'''
N = 1000

dp = [0] * N # dp = [0] * 1000, [0,..., 0]

dp[1] = 0

for n in range(2, N):
    ''' Все переходы рассматриваем '''
    dp[n] = min(dp[n - 3] + 1, dp[n - 7] + 1)
    if n % 2 == 0:
        dp[n] = min(dp[n], dp[n // 2] + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], dp[n // 3] + 1)

INFTY = 10**9 # 10^9
dp = [INFTY] * N

dp[1] = 0

for n in range(1, N):
    dp[n + 3] = min(dp[n + 3], dp[n] + 1)
    dp[n + 7] = min(dp[n + 7], dp[n] + 1)
    if 2 * n < N:
        dp[2 * n] = min(dp[2 * n], dp[n] + 1)
    if 3 * n < N:
        dp[3 * n] = min(dp[3 * n], dp[n] + 1)    
    
print(dp[15])
