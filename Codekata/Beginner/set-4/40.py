n1 = int(input())
if n1==1:
    print(1)
elif n1==2:
    print(1,1)
else:
    a = 1
    b = 1
    print(1,1,end=' ')
    for i in range(2,n1):
        c = a+b
        a = b
        b = c
        print(c,end=' ')
