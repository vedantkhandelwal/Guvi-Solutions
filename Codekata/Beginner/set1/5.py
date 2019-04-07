a1,b1,c1 = map(int,input().split())
max = a1 if a1>b1 else b1
max = c1 if max<c1 else max
print(max)
