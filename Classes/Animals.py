class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        '''This is what triple quote comments are for'''
        return self.name

    def setName(self, name):
        '''This is what triple quote comments are for'''
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        '''This is what triple quote comments are for'''
        self.age = age

    def describe(self):
        print(f"This is {self.getName()} they are {self.getAge()} years old.")

    def speak(self):
        print("What animal am I???")

class Cat(Animal):
    def speak(self):
        print("Meow!!")


class Dog(Animal):
    def speak(self):
        print("Woof")




