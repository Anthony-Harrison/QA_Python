class CharFind:
    '''Find specific characters and output how many occurences there are'''
    def __init__ (self):
        self.word = input("Enter a char or chars to search. ")

    def findLetter(self, check):
        lWord = check.lower()
        letterCount = {}
        for letter in self.word:
            count = lWord.count(letter)
            letterCount[letter] = count
        print(letterCount)

    def a(self):
        print("a")

    def b(self):
        return "b"
