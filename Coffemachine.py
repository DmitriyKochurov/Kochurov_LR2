
water = 400
milk = 540
beans = 120
amount = 9
money = 550


def espr():
    global water, beans, money, amount
    water -= 250
    beans -= 16
    amount -= 1
    money += 4
    return


def lat():
    global  water, milk, beans, money, amount
    water -= 350
    milk -= 75
    beans -= 20
    amount -= 1
    money += 7
    return


def cap():
    global water, milk, beans, money, amount
    water -= 200
    milk -= 100
    beans -= 12
    money += 6
    return


def vod():
    global water, milk, beans, money, amount
    print("The coffee machine has:\n" + str(water) + " of water\n" + str(milk) + " of milk")
    print(str(beans) + " of coffee beans\n" + str(amount) + " of disposable cups")
    print(str(money) + " of money")


def buy ():
    x = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappucino: "))
    if x == 1:
        espr()
    elif x == 2:
        lat()
    elif x == 3:
        cap()
    else:
        print("Enter the correct number")
    vod()


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
    vod()
    print("")
    answer = input("Write action (buy, fill, take): ")
    if answer == "buy":
        buy()
        break
    elif answer == "fill":
        fill()
        break
    elif answer == "take":
        tak()
        break
    else:
        print("Enter the action correctly")
