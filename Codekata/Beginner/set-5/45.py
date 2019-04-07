def countDigit(n1):
    if n1<=9:
        return 1
    return 1+countDigit(n1//10)

print(countDigit(int(input())))
