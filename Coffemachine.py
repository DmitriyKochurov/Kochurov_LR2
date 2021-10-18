def coffe():
    water = int(input("Write how many ml of water the coffee machine has: "))
    milk = int(input("Write how many ml of milk the coffee machine has: "))
    beans = int(input("Write how many g of coffee beans the coffee machine has: "))
    amount = int(input("Write how many cups of coffee you will need: "))
    need1 = int(200 * amount)
    need2 = int(50 * amount)
    need3 = int(15 * amount)
    cups = (min((water // 200), min((milk // 50), (beans // 15))))
    print(f"""For {amount} cups of coffee you will need: 
    {need1} ml of water
    {need2} ml of milk
    {need3} g of coffee beans""")
    if cups > amount:
        print(f"Yes, I can make that amount of coffee (and even {cups - amount} more than that).")
    if cups == amount:
        print("Yes, I can make that amount of coffee.")
    if cups < amount:
        print(f"No, I can make only {cups} cups of coffee.")


coffe()
