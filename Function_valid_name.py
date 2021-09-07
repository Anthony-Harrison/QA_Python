from Test import getNum

def isValid():
    name = input("Enter a name or type 1 to quit: ")
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

state = isValid()
if state[0] == True:
    print(f"The number of vowels in this name is {state[1]}")
    print(f"The value of this name is {getNum(state[2])}. ")
else:
    print("Quitting or name is not valid. ")
    exit()




