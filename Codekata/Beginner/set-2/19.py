def fac(n1):
    if n1==1 or n1==0:
        return 1
    return n1*fac(n1-1)

print(fac(int(input())))
