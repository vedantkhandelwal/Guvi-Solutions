def swap(x1,y):
    return y,x1
x1, y = map(int,input().split())
print(*swap(x1,y))
