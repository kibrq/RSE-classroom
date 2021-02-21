'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n*n - 5, при n > 15
F(n) = n*F(n+2) + n + F(n+3), при n ≤ 15
Определите сумму цифр значения F(1).

Ответ: 48
'''

def F(n):
    if n > 15:
        return n * n - 5
    return n * F(n + 2) + n + F(n + 3)

def digits_sum(n):
    res = 0
    while n > 0:
        res += n % 10
        n /= 10
    return res

print(digits_sum(F(1)))
