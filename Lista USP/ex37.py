import os,sys
from decimal import *

class divide_by_zero_exception(Exception):
    pass

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def menu_interaction():
    done = False
    while done != True:
        try:
            n = int(input("Menu de opções:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n0. Sair\nDigita a opção de sua escolha\n"))
            match n:
                case 1|2|3|4|0:
                    clear_screen()
                    return n
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Erro, opção invalida\n")

def get_nums(nums,op):
    while len(nums) != 2:
        try:
            n = int(input("Insira o %dº numero:\n" % (len(nums)+1)))
            if len(nums) == 1 and op == 4 and n == 0:
                raise divide_by_zero_exception()
            clear_screen()
            nums.append(n)
        except divide_by_zero_exception:
            clear_screen()
            print("Erro, impossivel dividir por zero, digite outro numero")
        except:
            clear_screen()
            print("Erro, valor invalido")
    return nums

def op_1():
    nums = []
    nums = get_nums(nums,1)
    print("Soma dos numeros %d e %d: %d" % (nums[0],nums[1],sum(nums)))

def op_2():
    nums = []
    nums = get_nums(nums,2)
    print("%d - %d: %d" % (nums[0],nums[1],(nums[0]-nums[1])))

def op_3():
    nums = []
    nums = get_nums(nums,3)
    print("%d multiplicado por %d: %d" % (nums[0],nums[1],(nums[0]*nums[1])))

def op_4():
    nums = []
    nums = get_nums(nums,4)
    getcontext().prec = 2
    div = Decimal(nums[0]/nums[1])
    if div == int(div):
        print("%d dividido por %d: %d" % (nums[0],nums[1],(div)))
    else:
        print("%d dividido por %d: %.2f" % (nums[0],nums[1],(div)))

def exit_prompt():
    done = False
    while done != True:
        try:
            ch = input("Digite \'SIM\' para continuar ou \'NÃO\' para terminar\n").strip().upper()
            match ch[:3]:
                case "SIM":
                    return False
                case "NÃO"|"NAO":
                    return True
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Erro, opção invalida\n")


if __name__ == "__main__":
    clear_screen()
    done = False
    while done != True:
        op = menu_interaction()
        clear_screen()
        match op:
            case 1: op_1()
            case 2: op_2()
            case 3: op_3()
            case 4: op_4()
            case 0: sys.exit()
        done = exit_prompt()
        clear_screen()