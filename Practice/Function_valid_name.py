from Test import getNum

def isValid(name):
    for char in name:
        if char.isdigit():
            return False, 0
    else:
        vowels = nameVowels(name)
        return True, vowels[0], name[1]

def nameVowels(name):
    numVowels = 0
    for char in name:
        c = char
        if c in "aeiouAEIOU":
            numVowels += 1
    return numVowels, name

def compatible(n1, n2):
    state1 = isValid(n1)
    state2 = isValid(n2)
    if state1[0] == True:
        num1 = getNum(n1)
    if state2[0] == True:
        num2 = getNum(n2)
    else:
        print("Not valid ")
        exit()
    compt = (num1 / num2) * 100
    return round(compt,2)


#state = isValid()
#if state[0] == True:
#    print(f"The number of vowels in this name is {state[1]}")
#    print(f"The value of this name is {getNum(state[2])}. ")
#else:
#    print("Quitting or name is not valid. ")
#    exit()
test = compatible("Baba", "Boo")
print(test)




