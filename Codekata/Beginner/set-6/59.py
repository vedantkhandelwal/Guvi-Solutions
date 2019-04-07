def getDigitCount(n1):
    if n1<=9:
        return 1
    return 1 + getDigitCount(n1//10)

print(getDigitCount(int(input())))

