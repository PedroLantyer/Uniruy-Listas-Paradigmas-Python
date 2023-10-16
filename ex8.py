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
        n = int(n)
        if n > 120 or n <= 0:
            raise Exception()
    except:
        clear_screen()
        print("ERRO: Por favor insira uma idade maior que 0 e menor que 120:")
        return False
    else:
        return True

def sort_inputs(n,arr):
    n = int(n)
    if n <= 15:
        arr[0] += 1
    elif n > 15 and n <= 30:
        arr[1] += 1
    elif n > 30 and n <= 45:
        arr[2] += 1
    elif n > 45 and n <= 60:
        arr[3] += 1
    else:
        arr[4] += 1 

if __name__ == "__main__":
    clear_screen()
    getcontext().prec = 2
    strings = ["Até 15 anos:","De 16 a 30 anos:","De 31 a 45 anos:","De 46 a 60 anos:","Maiores de 61 anos:"]
    age_group = [0,0,0,0,0]
    for i in range(15):
        done = False
        while done != True:
            n = input("Por favor insira a idade:\n")
            done = verify_input(n)
        else:
            clear_screen()
            sort_inputs(n,age_group)
    clear_screen()
    for i in range(len(strings)):
        print("%s %d" % (strings[i],age_group[i]))
    print()
    for i in range(0,5,4):
        avg = Decimal((age_group[i]*100)/15)
        print("%s %.2f%%" % (strings[i],avg))