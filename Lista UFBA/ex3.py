import os,sys
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_num():
    num = []
    while (len(num)<10):
        try:
                n = float(input("Insira o numero º%d:\n" % (len(num)+1)))
                num.append(n)
                clear_screen()
        except:
            clear_screen()
            print("Erro, valor invalido\n")
    return num

def op_a(num):
    getcontext().prec = 2
    avg = Decimal(sum(num)/len(num))
    print("Media dos valores %.2f" % avg)

def op_b(num):
    max_val,min_val = max(num), min(num)
    print("Maior valor: %.2f\nMenor valor: %.2f" % (max_val,min_val))

def op_c(num):
    count = [0,0,0]
    for i in range(len(num)):
        if num[i] > 0:
            count[0] += 1
        elif num[i] < 0:
            count[1] += 1
        else:
            count[2] += 1
    print("Numeros positivos: %d\nNumeros Negativos: %d\nNumeros nulos: %d" % (count[0],count[1],count[2]))

if __name__ == "__main__":
    clear_screen()
    num = get_num()
    op_a(num)
    op_b(num)
    op_c(num)