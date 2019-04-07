import re
s1 = input()
count=0
for i in s1:
    if i.isdigit():
        count+=1
print(count)
