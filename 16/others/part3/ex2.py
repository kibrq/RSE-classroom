'''
Определите наименьшее число n такое, что при вызове F(n) второе выведенное число будет больше числа 51. 
Запишите в ответе сначала найденное значение n, а затем через пробел – соответствующее значение F(n).

def F(n):
  print( n ) 
  if n > 0: 
    d = (n%10 + F(n//10))
    print(d)
    return d
  else: 
    return 0

Ответ: 520 7
'''

vals = []

def F(n):
  vals.append(n)
  if n > 0: 
    d = (n%10 + F(n//10))
    vals.append(d)
    return d
  else: 
    return 0

for n in range(1, 10**5 + 1):
    res = F(n)
    if len(vals) > 1 and vals[1] > 51:
        print(n, res)
    vals.clear()
