userInput = int(input("Enter your score. "))
print(userInput)
if(userInput > 85):
    print("Distinction")
elif(userInput >= 65 and userInput < 85):
    print("Pass")
else:
    print("Fail")