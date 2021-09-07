def test(testVar):
    if testVar < 5:
        print((f"{testVar} is < 5: Now exiting"))
        exit()
    else:
        print((f"{testVar} is > than 5: Continuing to next evaluation"))

x = 1000
y = 2000
z = x * y
test(z)
z = x * x / y
test(z)
z = 1
test(z)