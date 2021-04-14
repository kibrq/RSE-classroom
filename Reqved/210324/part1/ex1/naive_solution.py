import itertools

def solve(n, arr):
    mn = 10**9
    for i in range(n):
        for c in itertools.combinations(range(n - 1), i):
            flag = True
            satisfy = [0] * n
            for el in c:
                satisfy[el] = satisfy[el + 1] = 1
            for s in satisfy:
                flag &= s
            if not flag:
                continue
            d = 0
            for el in c:
                d += arr[el + 1] - arr[el]
            mn = min(d, mn)
    return mn



