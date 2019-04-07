import re
s1 = input()
count=0
for i in s1:
    if not(i.isalnum()):
        count+=1
print(count)
