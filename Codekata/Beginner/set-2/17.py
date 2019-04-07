import math as m
n = input()
p1 = len(n)

sum=0
for i in n:
    sum+=m.pow(int(i),p1)

if sum==int(n):
    print("yes")
else:
    print("no")
