def printDigits(n1):
    if n1<=9:
        print(n1,end=' ')
        return
    printDigits(n1//10)
    print(n1%10,end=' ')

printDigits(int(input()))
