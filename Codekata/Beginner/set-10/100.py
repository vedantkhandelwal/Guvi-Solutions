import functools
l1 = list(map(int,input()))
print(functools.reduce(lambda a,b:a*b ,l1))
