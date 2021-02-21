'''
Текстовый файл 24.txt состоит не более чем из 106 символов X, Y и Z. 
Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''

'''
XYZYXYXYXYZ.... ZZX
'''

s = ''

with open('input.txt') as file:
    s = file.read().replace('\n', '')


prev = 0
ans = 0
cur = 0

for c in s:
    if c == prev:
        ans = max(ans, cur)
        cur = 1
    else:
        cur += 1
    prev = c

ans = max(ans, cur)


'''
В текстовом файле k7.txt находится цепочка из символов латинского алфавита A, B, C длиной не более 106 символов.
Найдите длину самой длинной подцепочки, состоящей из символов C.
'''

s = input()

ans = 0
cur = 0

for c in s:
    if c != 'C':
        ans = max(ans, cur)
        cur = 0
    else:
        cur += 1
