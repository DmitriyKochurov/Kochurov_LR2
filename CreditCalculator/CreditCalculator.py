import math

crdt = int(input("Enter the loan principal:\n"))
print("""What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:""")
ch = input()
if ch == "m":
    ms = int(input("Enter the monthly payment: \n"))
    repayment = crdt // ms
    print(f"It will take {repayment} month to repay the loan.")
if ch == "p":
    nmr = int(input("Enter the number of months: \n"))
    payment = math.ceil(crdt / nmr)
    last_payment = math.ceil(crdt - (nmr - 1) * payment)
    if last_payment != payment:
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
    else:
        print(f"Your monthly payment = {payment}.")