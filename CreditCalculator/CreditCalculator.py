import math
import argparse

par = argparse.ArgumentParser()
par.add_argument("--principal", type=int)
par.add_argument("--payment", type=int)
par.add_argument("--interest", type=float)
par.add_argument("--periods", type=int)
par.add_argument("--annuity", type=float)
par.add_argument("--type", type=str)
args = par.parse_args()


def q(princ, pay, inter):
    i = (inter * 0.01 / 12)
    fraction = (pay / (pay - i * princ))
    result0 = math.ceil(math.log(fraction, i + 1))
    y = result0 / 12
    m = (y - math.floor(y)) * 12
    if math.floor(m) != 0:
        print(f"It will take {math.floor(y)} years and {math.ceil(m)} months to repay this loan!\n")
    else:
        print(f"It will take {math.ceil(y)} years to repay this loan!\n")
    print(f"Overpayment {int(princ * (1 + inter * 0.01 / 0.75) - princ)}")


def n(prin, per, inter):
        i = (inter * 0.01 / 12)
        num = pow(1 + i, per)
        result1 = prin * ((i * num) / (num - 1))
        print(f"Your monthly payment = {math.ceil(result1)}!\n")
        print(f"Overpayment {math.ceil(result1) * per - prin}")

def w(pay, per, inter):
        i = (inter * 0.01 / 12)
        num = pow(1 + i, per)
        result2 = math.floor(float(pay / ((i * num) / (num - 1))))
        print(f"Your loan principal = {result2}!\n")
        print(f"Overpayment {pay * per - result2}")


def diff(principal, periods, interest):
    i = interest * 0.01 / 12
    month = 0
    result = 0
    steps = list(reversed(range(2, periods + 2)))
    for monthly in steps:
        monthly -= 1
        d = math.ceil(principal / periods) + i * ((principal * monthly) / periods)
        result += d
        month += 1
        print(f"Month {month}: payment is {math.ceil(d)}")
    print(f"Overpayment {math.ceil(result - principal)}")


try:
    if args.type == "annuity":
        if args.payment is not None and args.principal is not None:
            if args.principal > 0 and args.payment > 0 and args.interest > 0:
                q(args.principal, args.payment, args.interest)
            else:
                print("Incorrect parameters")
        elif args.principal is not None and args.periods is not None:
            if args.principal > 0 and args.periods > 0 and args.interest > 0:
                n(args.principal, args.periods, args.interest)
            else:
                print("Incorrect parameters")
        elif args.payment is not None:
            if args.payment > 0 and args.periods > 0 and args.interest > 0:
                w(args.payment, args.periods, float(args.interest))
            else:
                print("Incorrect parameters")
    elif args.type == "diff":
        if args.principal > 0 and args.periods > 0 and args.interest > 0:
            diff(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")
except TypeError:
    print("Incorrect parameters")