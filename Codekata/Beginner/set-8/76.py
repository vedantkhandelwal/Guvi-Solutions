import math as ma

def isComposite(n):
    for i in range(2,int(ma.sqrt(n))+1):
        if not(n%i):
            return "yes"
    return "no"

print(isComposite(int(input())))
