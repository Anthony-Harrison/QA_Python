
listVar = ["bananas", "Screwdriver", 243, "Keys", 100, 10000001]
for i in listVar:
    print(i)
    if type(i) == str:
        print([char for char in i])
print("-------------------------------------------------------------")

dictList = {"1" : "2", "3" : "4"}

for i in dictList :
    print(dictList.items())
    print(dictList[i])


print(list(range(111,11,-10)))
print("-------------------------------------------------------------")
i = 0
lenVar = len(listVar)
while i < lenVar:
    print("Hello")
    i += 1
    