test = int(input("Enter a number "))


if test > 1:
    for i in range(2, test//2):
        if (test % i) == 0:
            print(test, "is not a prime number")
            break
    else:
        print(test, "is a prime number")
else:
    print(test, "is not a prime number")