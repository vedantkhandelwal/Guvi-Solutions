

x = int(input())
print(numberOfDigit(x))
def numberOfDigit(x):
    if x==1:
        return 1
    return x%10+numberOfDigit(x//10)