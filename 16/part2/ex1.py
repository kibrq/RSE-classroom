'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n, при n ≤ 3
при n > 3:
  F(n) = n + 3 + F(n–1), при чётном n;
  F(n) = n*n + F(n-2), при нечётном n;
Определите количество натуральных значений n на отрезке [1; 1000], при которых F(n) кратно 7.

Ответ: 285
'''

def F(n):
    if n <= 3:
        return n
    if n % 2 == 0:
        return n + 3 + F(n - 1)
    return n * n + F(n - 2)

cnt = 0
for n in range(1, 1000 + 1):
    if F(n) % 7 == 0:
        cnt += 1
print(cnt)
