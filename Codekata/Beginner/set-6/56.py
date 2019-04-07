def CheckDigitAndAlphabet(s1):
    digitFlag = False
    alphaFlag = False
    for i in s1:
        if i.isdigit():
            digitFlag = True
        elif i.isalpha():
            alphaFlag = True
        if digitFlag and alphaFlag:
            return 'Yes'
    return 'No'

s1 = input()
print(CheckDigitAndAlphabet(s1))
