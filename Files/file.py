def createF():
    with open("Files\\teamName.txt", "w") as file:
        l = ["a", "b", "c", "d", "e"]
        for n in range(0,5):
            newline = f"This is team {l[n]} \n"
            file.write(newline)
def appFile():
    with open("Files\\teamName.txt","r") as file:
        toSend = ""
        count = 0
        for lines in file:
            if count == 0:
                toSend += "This is a new line\n"
            else:
                toSend += lines
            count += 1
        file = open("Files\\teamName.txt","w")
        file.write(toSend)
   
createF()
appFile()