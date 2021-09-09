class Character:
    def __init__(self, hp=100 , armour=3, attack=10):
        self.hp = hp
        self.armour = armour
        self.attack = attack

    def getHp(self):
        return self.hp
    
    def setHp(self, attack):
        self.hp = attack - self.armour
    



a = Character()
print(a.getHp())