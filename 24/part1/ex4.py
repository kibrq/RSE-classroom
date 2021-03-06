'''
В текстовом файле k8.txt находится цепочка из не более чем 106 символов, 
в которую могут входить заглавные буквы латинского алфавита A…Z и десятичные цифры. 
Найдите длину самой длинной подцепочки, состоящей из одинаковых символов.
Выведите сначала символ, из которого строится цепочка, а затем через пробел – длину этой цепочки. 
Если таких цепочек (максимальной длины) несколько, выведите информацию о первой встретившейся цепочке.
'''



s = ''

with open('input.txt') as file:
    s = file.read().replace('\n', '')

ans = 0
ans_c = 0
cur = 0
prev = 0


for c in s:
    if c != prev:
        if cur > ans:
            ans = cur
            ans_c = prev
        cur = 1
    else:
        cur += 1
    prev = c

if cur > ans:
    ans = cur
    ans_c = prev

print(ans_c, ans)
