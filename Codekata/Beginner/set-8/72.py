def haveVowel():
    for i in s1:
        if i in 'aeiou':
            return "yes"
    return "no"
print(haveVowel(input()))
