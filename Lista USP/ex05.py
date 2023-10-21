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

def exit_prompt(str1):
    done = False
    while done != True:
        ans = input(str1)
        try:
            ans.strip()
            ans = ans.upper()
            if (ans != "SIM" and ans != "NÃO" and ans != "NAO"):
                raise Exception()
        except:
            clear_screen()
            print("Não consegui entender, tente novamente")
            done = False
        else:
            if (ans == "SIM"):
                clear_screen()
                return True
            else:
                clear_screen()
                return False

def calc_bonus(total):
    getcontext().prec = 2
    if total < 1000:
        if total == 0:
            return 0
        else:
            return (Decimal(total/10))
    else:
        return (Decimal(total*Decimal(0.15)))
    
def get_name():
    done = False
    while done != True:
        name = input("Por favor insira seu nome:\n")
        try:
            if (name.strip().isalpha() == False) or (len(name.strip()) < 2):
                raise Exception()
            name.capitalize()
        except:
            clear_screen()
            print("Não consegui entender, tente novamente")
            done = False
        else:
            done = True
    return name

def get_purchases():
    done = False
    total = 0
    clear_screen()
    while done != True:
        try:
            val = Decimal(input("Insira o valor da compra: \n"))
            if val < 0:
                raise Exception()
        except:
            clear_screen()
            print("Numero invalido, tente novamente:")
            done = False
        else:
            clear_screen()
            total += val
            done = not(exit_prompt("Deseja inserir mais um valor?\nSe sim digite \"SIM\"\nSe não digite \"NÃO\"\n"))
    return total

if __name__ == "__main__":
    done = False
    while done != True:
        clear_screen()
        getcontext().prec = 2
        name = get_name()
        total = get_purchases()
        bonus = calc_bonus(total)
        print("Nome: %s\nValor total das compras: R$%.2f\nSeu bonûs é: R$%.2f" % (name,total,bonus))
        done = not(exit_prompt("\nDeseja continuar?\nSe sim digite \"SIM\"\nSe não digite \"NÃO\"\n"))