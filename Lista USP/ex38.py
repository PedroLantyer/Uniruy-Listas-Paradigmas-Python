import os,sys
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
            n = int(input("Menu de opções:\n1. Novo Salário\n2. Férias\n3. Décimo terceiro\n4. Sair\nDigite a opção desejada\n"))
            match n:
                case 1|2|3|4:
                    return n
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def get_salario():
    done = False
    while done != True:
        try:
            n = float(input("Insira o valor do salario:\n"))
            if n < 1:
                raise Exception()
            else:
                return n
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def get_meses():
    done = False
    while done != True:
        try:
            n = int(input("Insira o numero de meses trabalhados:\n"))
            if n in range(1,13):
                return n
            else:
                raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def op_1():
    getcontext().prec = 2
    salario = (get_salario())
    og_sal = salario
    if salario in range(1,350):
        salario = Decimal(salario*1.15)
    elif salario in range(350,601):
        salario = Decimal(salario*1.1)
    elif salario > 600:
        salario = Decimal(salario*1.05)
    print("Salario original: R$%.2f\nSalario novo: R$%.2f\n" % (og_sal,salario))

def op_2():
    getcontext().prec = 2
    salario = get_salario()
    ferias = Decimal(salario/3)
    print("Salario: R$%.2f\nFerias: R$%.2f\n" % (salario,ferias))

def op_3():
    salario = get_salario()
    meses = get_meses()
    decimo_terceiro = Decimal((salario*meses)/12)
    print("Salario: R$%.2f\nMeses trabalhados: R$%d\n13º: R$%.2f\n" % (salario,meses,decimo_terceiro))

def exit_prompt():
    done = False
    while done != True:
        try:
            s = input("Digite \"SIM\" para continuar ou \"NÃO\" para sair\n").strip().upper()
            match s[:3]:
                case "SIM": return False
                case "NAO"|"NÃO": return True
        except:
            clear_screen()
            print("Erro, valor invalido\n")

if __name__ == "__main__":
    done = False
    while done != True:
        clear_screen()
        op = menu_interaction()
        clear_screen()
        match op:
            case 1: op_1()
            case 2: op_2()
            case 3: op_3()
            case 4: sys.exit()
        done = exit_prompt()