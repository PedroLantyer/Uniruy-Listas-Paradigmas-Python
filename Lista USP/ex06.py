from decimal import *
import os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

if __name__ == "__main__":
    clear_screen()
    delta = 26 #sales increase for each 50 cent reduction
    getcontext().prec = 2
    price = Decimal(5.00)
    count = 0
    while price >= 1:
        sales = 120+(delta*count)
        profit = Decimal(price*(sales)-200)
        print("Preço: %.2f\nIngressos: %d\nLucro máximo: %.2f" % (price,sales,profit))
        if price > 1:
            print()
        count += 1
        price -= Decimal(0.5)