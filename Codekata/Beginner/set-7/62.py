s1 = input()
for i in range(len(s1)):
    if s1[i]!=0 and s1[i]!=1:
        break
if i==len(s1)-1:
    print("yes")
else:
    print("no")
