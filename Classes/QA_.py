class Dog:
    def __init__(self, name, breed, energy):
        self.name = name
        self.breed = breed
        self.energy = energy

bilbo_waggins = Dog()
chewbarka = Dog()
chewbarka.energy = "low"

print(bilbo_waggins.energy)
bilbo_waggins.speak()

print(f"chewbarkas' energy is {chewbarka.energy}.")
chewbarka.speak()
