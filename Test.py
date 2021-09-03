def split(word):
    return [char for char in word]


def getNum(nameList):
    i = 0
    nameNum = 0
    while i < len(nameList):
        k = str(i)
        nameNum = nameNum + ord(k)
        i = i + 1
    return nameNum

nameOne = split("Anthony")
nameTwo = split("Harrison")

conOne = getNum(nameOne)
conTwo = getNum(nameTwo)

compatability = (conOne / conTwo) * 100
print(compatability)
print(nameOne)

