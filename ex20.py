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
    age = []
    done = False
    while done != True:
        try:
            l1 = input("Por favor insira um numero inteiro e positivo ou digite 0 para terminar:\n").split()
            n = int(l1[0])
            if n < 0:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um numero inteiro e positivo")
        else:
            if n == 0:
                done = True
            else:
                age.append(n)
            clear_screen()
    age.sort()
    if len(age) != 0:
        low,high = age[0],age[-1]
    print("Valor mais baixo: %d\nValor mais alto: %d" % (low,high))