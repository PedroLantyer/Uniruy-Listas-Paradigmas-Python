import os,random,sys
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu_interaction():
    done = False
    while done != True:
        try:
            n = int(input("Menu de opções:\n1. Média aritmética\n2. Média ponderada\n3. Sair\nDigite a opção desejada\n"))
            match n:
                case 1|2|3:
                    clear_screen()
                    return n
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Erro, opção invalida\n")

def op_1():
    nums = []
    getcontext().prec = 2
    while len(nums) != 2:
        try:
            print("Média aritmética")
            n = int(input("Insira o %dº valor:\n" % (len(nums)+1)))
        except:
            clear_screen()
            print("Erro valor invalido\n")
        else:
            clear_screen()
            nums.append(n)
    avg = Decimal(sum(nums)/len(nums))
    print("Media aritmética dos numeros %d e %d: %.2f" % (nums[0],nums[1],avg))

def op_2():
    nums,weigth = [],[]
    getcontext().prec = 2
    while len(weigth) != 3:
        try:
            print("Média ponderada")
            if len(nums) == len(weigth):
                n = int(input("Insira o %dº valor:\n" % (len(nums)+1)))
                clear_screen()
                nums.append(n)
            else:
                x = float(input("Insira o %dº peso:\n" % (len(weigth)+1)))
                if x <= 0:
                    raise Exception()
                clear_screen()
                weigth.append(x)
        except:
            clear_screen()
            print("Erro valor invalido\n")
    for i in range(len(nums)):
        nums[i] *= weigth[i]
    avg = Decimal(sum(nums)/sum(weigth))
    print("Média ponderada dos numeros %d,%d e %d: %.2f" % (nums[0],nums[1],nums[2],avg))

if __name__ == "__main__":
    clear_screen()
    n = menu_interaction()
    match n:
        case 1:
            op_1()
        case 2:
            op_2()
        case 3:
            sys.exit()