class Character:
    def __init__(self, name, health = 10, armour = 3, attack = 5):
        self.name = name
        self.health = health
        self.armour = armour
        self.attack = attack

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        return f"name changed to {self.getName()}"

    def getHealth(self):
        return self.health
    
    def setHealth(self, health):
        self.health = health
    
    def getArmour(self):
        return self.armour
    
    def setArmour(self, armour):
        self.armour = armour

    def getAttack(self):
        return self.attack
    
    def setAttack(self, attack):
        self.attack = attack

    def attackObj(self, obj):
        atkVal = self.getAttack() - obj.getArmour()
        tmp = obj.getHealth() - atkVal
        obj.setHealth(tmp)
        print(f"{atkVal} points of damage done to {obj.name}")


class Player(Character):
    heal = 5
    def doHeal(self):
        self.setHealth = self.getHealth + self.heal

class Enemy(Character):
    regen = 2

    def doRegen(self):
        self.setHealth = self.getHealth + self.regen



#print(a.getHealth())
#print(a.setName("Asda"))
#print(a.getName())
#print(type(a))
#print(type(b))
#a.attackObj(b)
#print(b.getHealth())

def main():
    a = Character("Anth")
    b = Character("Bill",1)
    player = input("Would you like to play? Yes/No? ")
    if player.lower().strip() == "yes":
        print("Playing against an enemy")
        player = input("What would you like to do?\n1: Attack \n2: Heal \nChoose:")
        if player.lower().strip() == "1" or player.lower().strip() == "attack":
            a.attackObj(b)
            if b.getHealth() < 1:
                print("you win!")
    
    
    
    else:
        print("Quitting")
        exit()

if __name__ == "__main__":
    main()