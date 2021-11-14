import math


def m():
    crdt = int(input("Enter the loan principal:\n"))
    monthly_payment = int(input("Enter the monthly payment:\n"))
    loan_interest = float(input("Enter the loan interest:\n"))
    i = (loan_interest * 0.01 / 12)
    fraction = (monthly_payment / (monthly_payment - i * crdt))
    result_n = math.ceil(math.log(fraction, i+1))
    y = result_n / 12
    m = (y - math.floor(y)) * 12
    if math.floor(y) != 0:
        print(f"It will take {math.floor(y)} years and {math.ceil(m)} months to repay this loan!\n")
    else:
        print(f"It will take {math.ceil(y)} years to repay this loan!\n")

    def q():
        crdt = int(input("Enter the loan principal:\n"))
        period = int(input("Enter the number of periods:\n"))
        loan_int = float(input("Enter the loan interest:\n"))
        i = (loan_int * 0.01 / 12)
        num = pow(1 + i, period)
        result1 = crdt * ((i * num) / (num - 1))
        print(f"Your monthly payment = {math.ceil(result1)}!\n")

    def r():
        ann = float(input("Enter the annuity payment:\n"))
        per = int(input("Enter the number of periods:\n"))
        loan_int = float(input("Enter the loan interest:\n"))
        i = (loan_int * 0.01 / 12)
        num = pow(1 + i, per)
        result2 = ann / ((i * num) / (num - 1))
        print(f"Your loan principal = {math.floor(result2)}!\n")

    while True:
        ch = input(f"""What do you want to calculate?
            type "n" for number of monthly payments,
            type "a" for annuity monthly payment amount,
            type "p" for loan principal:\n""")
        if ch == "n":
            m()
        if ch == "a":
            q()
        if ch == "p":
            r()