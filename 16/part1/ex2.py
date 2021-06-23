#!/usr/bin/env python3

'''
Алгоритм вычисления значения функции F(n), где n - натуральное число, задан следующими соотношениями:

F(1) = 5
F(2) = 5
F(n) = 5*F(n − 1) − 4*F(n − 2) при n > 2.

Чему равно значение функции F(40)? В ответе запишите только натуральное число.

Ответ: 5
'''

# Если напсиать рекурсию, то ничего не получится
# Она будет работать очень долго, так как по многу раз считает один и те же значения

F = [0] * 50 # Можно до длины 41. Мне так удобнее, чтобы точно знать, что ничего не вылезет за границы

for n in range(1, 40 + 1):
    if n == 1:
        F[1] = 5
    elif n == 2:
        F[2] = 5
    else:
        F[n] = 5 * F[n - 1] - 4 * F[n - 2]

print(F[40])




