
water = 400
milk = 540
beans = 120
amount = 9
money = 550


def espr():
    global water, beans, money, amount
    if water > 249 and beans > 15 and amount > 0:
        print("I have enough resources, making you a coffee!")
        water -= 250
        beans -= 16
        amount -= 1
        money += 4
        return
    if water < 250:
        print("Sorry, not enough water!")
    if beans < 16:
        print("Sorry, not enough coffee beans!")
    if amount < 1:
        print("Sorry, not enough disposable cups!")


def lat():
    global  water, milk, beans, money, amount
    if water > 249 and beans > 15 and amount > 0:
        print("I have enough resources, making you a coffee!")
        water -= 350
        milk -= 75
        beans -= 20
        amount -= 1
        money += 7
        return
    if water < 350:
        print("Sorry, not enough water!")
    if beans < 20:
        print("Sorry, not enough coffee beans!")
    if amount < 1:
        print("Sorry, not enough disposable cups!")
    if milk < 75:
        print("Sorry, not enough milk!")


def cap():
    if water > 249 and beans > 15 and amount > 0:
        print("I have enough resources, making you a coffee!")
        water -= 200
        milk -= 100
        beans -= 16
        amount -= 1
        money += 6
        return
    if water < 250:
        print("Sorry, not enough water!")
    if beans < 16:
        print("Sorry, not enough coffee beans!")
    if amount < 1:
        print("Sorry, not enough disposable cups!")
    if milk < 100:
        print("Sorry, not enough milk!")


def vod():
    global water, milk, beans, money, amount
    print ("")
    print("The coffee machine has:\n" + str(water) + " of water\n" + str(milk) + " of milk")
    print(str(beans) + " of coffee beans\n" + str(amount) + " of disposable cups")
    print(str(money) + " of money")


def buy ():
    while True:
        x = int(input("What do you want to buy?\n1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to main menu: "))
        if x == 1:
            espr()
        elif x == 2:
            lat()
        elif x == 3:
            cap()
        elif x == 4:
            break
        else:
            print("enter the correct number")
        break


def fill():
    global water, milk, beans, money, amount
    water += int(input("Write how many ml of water you want to add: "))
    milk += int(input("Write how many ml of milk you want to add: "))
    beans += int(input("Write how many grams of coffee beans you want to add: "))
    amount += int(input("Write how many disposable coffee cups you want to add: "))
    vod()


def tak():
    global money
    print("I gave you " + str(money))
    money -= money
    vod()


while True:
    print("")
    answer = input("Write action (buy, fill, take, remaining, exit): ")
    if answer == "buy":
        buy()
    elif answer == "fill":
        fill()
    elif answer == "take":
        tak()
    elif answer == "remaining":
        vod()
    elif answer == "exit":
        break
    else:
        print("Enter the action correctly")
