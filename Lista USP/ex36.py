import os,sys
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_age(age):
    try:
        n = int(input("Por favor digite sua idade, ou digite 0 para terminar\n"))
        clear_screen()
        if n <= 0:
            return age,True
        else:
            age.append(n)
            return age,False
    except:
        clear_screen()
        print("Erro, idade invalida\n")
        return age,False
    
def get_heigth(heigth):
    try:
        n = int(input("Por favor digite sua altura em cm\n"))
        clear_screen()
        if n <= 0 or n > 250:
            raise Exception()
        else:
            heigth.append(n)
            return heigth
    except:
        clear_screen()
        print("Erro, altura invalida\n")
        return heigth
    
def avg(age,heigth):
    x,count = 0,0
    for i in range(len(heigth)):
        if age[i] > 50:
            x += heigth[i]
            count += 1
    if count == 0:
        print("Nenhuma pessoa acima de 50 anos")
        sys.exit()
    else:
        getcontext().prec = 2
        avg = Decimal(x/count)
        print("Media de altura das pessoas com mais de 50 anos: %.2fcm" % avg)

def get_input():
    age,heigth = [],[]
    done = False
    while done != True:
        if len(age) == len(heigth):
            age,done = get_age(age)
            if done == True:
                break
        elif len(heigth) < len(age):
            heigth = get_heigth(heigth)
    return age,heigth

if __name__ == "__main__":
    clear_screen()
    age,heigth = get_input()
    avg(age,heigth)

