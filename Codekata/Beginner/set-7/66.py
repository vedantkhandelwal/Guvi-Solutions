import math as ma
def isPrime(n):
    for i in range(2,int(ma.sqrt(n))+1):
        if not(n%i):
            return 'no'
    return 'yes'
print(isPrime(int(input())))

