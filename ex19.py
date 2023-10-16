import math,os
from decimal import *

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
    getcontext().prec = 2
    done = False
    age = []
    while done != True:
        try:
            l1 = input("Por favor insira a idade ou digite 0 para terminar:\n").split()
            n = int(l1[0])
            if n < 0:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um numero positivo ou nulo")
        else:
            if n == 0:
                done = True
            else:
                age.append(n)
            clear_screen()
    if len(age) == 0:
        print("Nenhum numero inserido portanto a media de idade é 0")
    else:
        sum = 0
        for i in range(len(age)):
            sum += age[i]
        avg = Decimal(sum/len(age))
        print("Média de idade: %.2f anos" % avg)