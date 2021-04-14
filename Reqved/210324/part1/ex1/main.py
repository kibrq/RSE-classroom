import solution as s
import naive_solution as ns

import random as r

for i in range(100):
    print(i)
    n = r.randint(1, 15)

    arr = sorted([r.randint(-100, 100) for _ in range(n)])

    ans = s.solve(n, arr)
    correct = ns.solve(n, arr)

    if ans != correct:
        print(correct, ans)
        print(n, arr)
        break


