import math
s1 = input()
l = len(s1)

if l%2:
    print(s1[:l//2] + '*' +s1[l//2+1:])
else:
    print(s1[:l//2-1] + '**' +s1[l//2+1:])
