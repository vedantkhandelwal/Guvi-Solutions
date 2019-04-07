a1,b = map(int,input().split())
for i in range(max(a1,b),(a1*b)+1):
    if not(i%a1) and not(i%b):
        print(i)
        break
