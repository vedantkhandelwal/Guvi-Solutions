a1,b = map(int,input().split())
for i in range(min(a1,b),0,-1):
    if not(a1%i) and not(b%i):
        print(i)
        break
