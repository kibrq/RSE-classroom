#!/usr/bin/env python3

'''
  Исполнитель Простачок преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
  1. Прибавить 2
  2. Прибавить 3
  3. Умножить на 2

  Первая команда увеличивает число на 2, вторая – на 3, третья – увеличивает число вдвое. Сколько различных чисел может быть получено из числа `10` всеми возможными алгоритмами длиной `5` команд?

  Ответ: `83`
'''

DEPTH = 5
START = 10
s = set()

def f(n, depth):
    if depth >= DEPTH:
        s.add(n)
        return # Не забываем!
    f(n + 2, depth + 1)
    f(n + 3, depth + 1)
    f(n * 2, depth + 1)

f(START, 0)

print(len(s))
