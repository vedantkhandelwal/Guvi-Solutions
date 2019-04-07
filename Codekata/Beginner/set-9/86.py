from collections import Counter
s1 = input()
print("Yes" if sorted(Counter(s1).values())[-1]==1 else "No")
