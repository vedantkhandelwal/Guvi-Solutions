def getSum(n1):
    if n1<=9:
        return n
    return n1%10 + getSum(n1//10)

print(getSum(int(input())))
