class Dog:
    '''This is a dog class WOOF!!!'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print ("bark")

    def getName(self):
        '''Returns the name of the Dog'''
        return self.name

    def setName(self, name):
        '''Set name of Dog'''
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age
    
d = Dog("Fido", 12)

print(f"{d.getName()} is {d.getAge()} years old.")
    