class Machine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.amount = 9
        self.money = 550

    def espresso(self):
        if self.water > 249 and self.beans > 15 and self.amount > 0:
            print("I have enough resources, making you a coffee!")
            self.water -= 250
            self.beans -= 16
            self.amount -= 1
            self.money += 4
            return
        if self.water < 250:
            print("Sorry, not enough water!")
        if self.beans < 16:
            print("Sorry, not enough coffee beans!")
        if self.amount < 1:
            print("Sorry, not enough disposable cups!")

    def latte(self):
        if self.water > 349 and self.beans > 20 and self.amount > 0 and self.milk > 74:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.amount -= 1
            self.money += 7
            return
        if self.water < 350:
            print("Sorry, not enough water!")
        if self.beans < 20:
            print("Sorry, not enough coffee beans!")
        if self.amount < 1:
            print("Sorry, not enough disposable cups!")
        if self.milk < 75:
            print("Sorry, not enough milk!")

    def cappuccino(self):
        if self.water > 199 and self.beans > 11 and self.amount > 0 and self.milk > 99:
            print("I have enough resources, making you a coffee!")
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            return
        if self.water < 200:
            print("Sorry, not enough water!")
        if self.beans < 12:
            print("Sorry, not enough coffee beans!")
        if self.amount < 1:
            print("Sorry, not enough disposable cups!")
        if self.milk < 100:
            print("Sorry, not enough milk!")

    def vod(self):
        print("")
        print(f"""The coffee machine has:
        {self.water} of water;
        {self.milk} of milk;
        {self.beans} of coffee beans;
        {self.amount} of disposable cups;
        {self.money} of money.""")

    def buy(self):
        while True:
            x = int(
                input("What do you want to buy?\n1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to main menu: "))
            if x == 1:
                Machine.espresso(self)
            elif x == 2:
                Machine.latte(self)
            elif x == 3:
                Machine.cappuccino(self)
            elif x == 4:
                break
            else:
                print("enter the correct number")
            break

def fill(self):
    self.water += int(input("Write how many ml of water you want to add: "))
    self.milk += int(input("Write how many ml of milk you want to add: "))
    self.beans += int(input("Write how many grams of coffee beans you want to add: "))
    self.amount += int(input("Write how many disposable coffee cups you want to add: "))

def tak(self):
    print(f"\nI gave you {self.money}")
    self.money -= self.money


cf = Machine()

while True:
    print("")
    answer = input("Write action (buy, fill, take, remaining, exit): ")
    if answer == "buy":
        cf.buy()
    elif answer == "fill":
        cf.fill()
    elif answer == "take":
        cf.take()
    elif answer == "remaining":
        cf.vod()
    elif answer == "exit":
        break
    else:
        print("Enter the action correctly")