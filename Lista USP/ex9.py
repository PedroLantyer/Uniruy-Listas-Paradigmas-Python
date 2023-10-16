import os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def verify_input(n):
    try:
        Decimal(n)
    except:
        clear_screen()
        print("ERRO: Por favor insira um numero:")
        return False
    else:
        return True

def set_type(n):
    count = 0
    for i in range(len(n)):
        if n[i] == ".":
            count = 1
            break
    if count == 1:
        n = Decimal(n)
        return n,"DECIMAL"
    else:
        n = int(n)
        return n,"INT"

def get_input():
    done = False
    while done != True:
        n = input().strip()
        done = verify_input(n)
    else:
        clear_screen()
        n,data_type = set_type(n)
        return n,data_type

def tabuada(n,data_type):
    val = 0
    for i in range(1,11):
        if data_type == "INT":
            val = int(n*i)
            print("%d x %d = %d" % (n,i,val))
        elif data_type == "DECIMAL":
            val = Decimal(n*i)
            print("%.2f x %d = %.2f" % (n,i,val))

if __name__ == "__main__":
    getcontext().prec = 2
    clear_screen()
    n,data_type = get_input()
    tabuada(n,data_type)
    