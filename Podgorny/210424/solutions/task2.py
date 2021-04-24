#!/usr/bin/env python3

'''
Рассматривается множество чисел из промежутка '[1234; 4567]', которые делятся на 7 и не делятся на 13. Найдите количество таких чисел и максимальное число с суммой цифр больше 20. Ответ запишите без пробелов.
'''


def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def test(n):
    if n % 7 == 0 and n % 13 != 0 and sum_digits(n) > 20:
        return True


def print_ans(ans):
    print(len(ans), end='')
    print(max(ans))


ans = []

for n in range(1234, 4567 + 1):
    if test(n):
        ans.append(n)

print_ans(ans)
