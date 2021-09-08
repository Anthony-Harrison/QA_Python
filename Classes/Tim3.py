class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        '''Returns the name of the animal'''
        return self.name

    def setName(self, name):
        '''Set name of animal'''
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
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


d1 = Dog("Fido", 12)
c1 = Cat("Cinder", 8)

d1.describe()
d1.speak()