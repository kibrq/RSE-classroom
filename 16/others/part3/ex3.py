
'''
Определите наименьшее значение n, при котором сумма чисел, которые будут выведены при вызове F(n), будет больше 3200000.
 Запишите в ответе сначала найденное значение n, а затем через пробел – соответствующую сумму выведенных чисел.

def F( n ):
  print(n*n)
  if n > 1:
    print(2*n+1)
    F(n-2)
    F(n//3)

Ответ: 199 3238315
'''

vals = []

def F(n) :
    vals.append(n * n)
    if n > 1:
        vals.append(2 * n + 1)
        F(n - 2)
        F(n // 3)

for n in range(1, 10**5 - 1):
    F(n)
    if sum(vals) > 3200000:
        print(n, sum(vals))
        break
    vals.clear() # !!! ВАЖНО

