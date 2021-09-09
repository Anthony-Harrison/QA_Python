import pytest



user_funds = 10.31
item_price = 5

if item_price < user_funds:
    print("You have enough money!")
elif item_price >= user_funds:
    print("You have the precise amount of money")
elif item_price < user_funds:
    print("Sorry you don\'t have enough money")

def product(n,a,d):
    total = n * a * d
    i = 0
    if total == 1:
        for n in n:
            total = i
    return total

print(product(4,4,5))

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True
print(is_prime(13))

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0
while n < 5:
    for i in item_list:
        print(i)
        n += 1
