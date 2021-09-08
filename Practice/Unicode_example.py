def split(word):
    return [char for char in word]

def uniVal(lWord):
    emp = []
    for i in lWord:
        emp.append(ord(i))

    return emp

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
aLower = split(lower)
aUpper = split(upper)
print(lower)
print(uniVal(split(aLower)))
print()
print(upper)
print(uniVal(aUpper))