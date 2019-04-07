def isnum(i):
    if i.isnumeric():
        return True
    return False

s11 = input()
print("".join(filter(isnum, s11)))
