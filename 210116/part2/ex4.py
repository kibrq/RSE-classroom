
'''
Определите наибольшее трехзначное значение n, при котором значение F(n), будет больше числа 7.
 Запишите в ответе сначала найденное значение n, а затем через пробел – соответствующее значение F(n).
def F(n):
  if n < 10: 
    return n
  else: 
    m = F(n//10)
    d = m%10;
    if m < d: 
      return d
    else: 
      return m
    
Ответ: 999 9
'''

def F(n):
    if n < 10:
        return n
    else:
        m = F(n // 10)
        d = m % 10
        if m < d:
            return d
        else:
            return m

# НАИБОЛЬШЕЕ ТРЕХ!!!Значное

for n in range(10**3 - 1, 10**2 - 1, -1): # 999, 998, ... 100
    if F(n) > 7:
        print(n, F(n))
        break # exit(0)

