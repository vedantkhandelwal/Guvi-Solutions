import math as ma
n = input()
flag = True
for i in range(2,int(ma.sqrt(n))+1):
    if not(n%i):
        flag = False
        break
if flag:
    print("yes")
else:
    print("no")
