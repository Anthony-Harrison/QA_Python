class Budget:
    def __init__(self, name):
        self.name = name
        self.balance = float(input("Enter your balance. "))
        self.transHis = []
    def getName(self):
        return self.name

    def balance(self):
        if self.name or self.sName:
            return self.balance

    def withdraw(self):
        amount = float(input(f"withdraw: Enter price. "))
        if amount > self.balance:
            return print("Error not enough money. ")
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
        print(f"Depositing £{amount} into {self.name}.")

    def transfer(self):
        obj = eval(input("Enter name to transfer. "))
        amount = float(input("Enter amount. "))
        if amount > self.balance:
            return print("Error not enough money. ")
        self.balance -= amount
        obj.balance += amount
        self.transHis.append(f"Transfering {amount} to {obj.name}")
        print(f"Transfering £{amount} from {self.name} to {obj.name}.")

    def spend(self):
        amount = float(input(f"Spend: Enter price. "))
        if self.balance < amount:
            return print("Not enough funds. ")
        addedItem = input("Enter name of purchase. ")        
        self.transHis.append(f"{addedItem} cost £{amount} ")
        self.balance -= amount
        return self.balance

    def transactionList(self):
        i = 0
        while i <= len(self.transHis):
            print(self.transHis[i])
            i += 1

food = Budget("Food")
clothes = Budget("Clothes")
food.transfer()
print(food.balance)
#print(food.transactionList)
#print(clothes.balance)
#print(food.balance)
#food.spend()
#print(food.balance)
#food.spend()
#food.deposit(10000000)
#print(food.balance)
#print(food.transactionList())

