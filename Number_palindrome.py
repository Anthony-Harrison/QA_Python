def rev(word):
    revWord = str(word) [::-1]
    return revWord

def ckPal(word):
    if word != rev(word):
        return True
    else:
      return False
    
state = False
num = int(input("Enter a number. "))
loops = 0
while state == False:
    while str(num) != rev(num):
        num = num + int(rev(num))
        state = ckPal(num)
        loops += 1
    else:
        break
if loops > 0:
    print((f"Palindrome ended at {num} with {loops} loops."))
else:
    print((f"The number {num} is already a palindrome."))
