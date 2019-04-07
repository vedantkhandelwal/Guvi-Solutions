def checkProduct(n1,m):
    if (n1*m)%2:
        return "odd"
    else:
        return "even"

n1,m = map(int, input().split())
print(checkProduct(n1,m))
