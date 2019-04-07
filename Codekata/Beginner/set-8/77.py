def printFactors(n1):
    for i in range(1,n1+1):
        if not(n1%i):
            print(i,end=" ")

print(printFactors(int(input())))
