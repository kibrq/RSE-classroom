'''
В текстовом файле k7a-6.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите длину самой длинной подцепочки, не содержащей гласных букв.
'''

'''
В текстовом файле k7a-5.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F.
Найдите длину самой длинной подцепочки, не содержащей символов C и F.
'''

'''
В текстовом файле k7a-3.txt находится цепочка из символов латинского алфавита A, B, C, D, E, F. 
Найдите длину самой длинной подцепочки, состоящей из символов A, B, E, F (в произвольном порядке).
'''

s = ''

with open('input.txt') as file:
    s = file.read().replace('\n', '')

avoid = ['C', 'F']

ans = 0
cur = 0

'''
CEAFCBAEFADFEDBBBBBBBBBB
'''

for c in s:
    if c in avoid:
        ans = max(ans, cur)
        cur = 0
    else:
        cur += 1

ans = max(ans, cur)

print(ans)
