
def solve(n, arr):
    dp = [0, 10**9]
    for i in range(1, n):
        ndp = [0, 0]
        ndp[0] = dp[1]
        ndp[1] = min(dp[0], dp[1]) + arr[i] - arr[i - 1]
        dp = ndp[::]
    return dp[1]

