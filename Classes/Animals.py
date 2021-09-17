from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

    def describe(self):
        print(f"This is {self.getName()} they are {self.getAge()} years old.")
    '''Abstract methods define methods which must
     be implemented by sub classes.'''
    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def eat():
        print("eatign")

    def speak(self):
        print("Meow!!")


class Dog(Animal):
    def speak(self):
        print("Woof")




