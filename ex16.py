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

def get_weigth(weigth):
    getcontext().prec = 2
    continue_op = True
    while continue_op != False:
        try:
            weigth_i = Decimal(input("Por favor insira seu peso em KG:\n"))
            if weigth_i < 20 or weigth_i > 300:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um peso entre 20KG e 300KG")
        else:
            clear_screen()
            weigth.append(weigth_i)
            break
    return weigth

def get_height(weigth):
    continue_op = True
    while continue_op != False:
        try:
            heigth_i = int(input("Por favor insira sua altura em cm:\n"))
            if heigth_i < 50 or heigth_i > 250:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira uma altura entre 50 e 250cm")
        else:
            clear_screen()
            heigth.append(heigth_i)
            break
    return heigth

def get_age(age):
    continue_op = True
    while continue_op != False:
        try:
            age_i = int(input("Por favor insira sua idade:\n"))
            if age_i < 1 or age_i > 120:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um numero entre 1 e 120")
        else:
            clear_screen()
            age.append(age_i)
            break
    return age

def condition_1(age,n):
    getcontext().prec = 2
    sum = 0
    for i in range(len(age)):
        sum += age[i]
    media = Decimal(sum/n)
    return media

def condition_2(weigth,heigth):
    count = 0
    for i in range(len(weigth)):
        if weigth[i] > 90 and heigth[i] < 150:
            count += 1
    return count

def condition_3(age,heigth,n):
    getcontext().prec = 2
    count = 0
    for i in range(len(age)):
        if (age[i] >= 10 and age[i] <= 30) and heigth[i] > 190:
            count += 1
    percent = Decimal((count/n)*100)
    return percent

def print_results(A,B,C):
    print("Média de idade: %.2f ano(s)" % A)
    print("Peso superior a 90KG e altura inferior a 1.5m: %d pessoa" % B)
    print("Porcentagem de pessoas que tem mais de 1.9m de altura e tem entre 10 e 30 anos de idade: %.2f%%" %C)

if __name__ == "__main__":
    clear_screen()
    n = 10
    weigth,age,heigth = [],[],[]
    for i in range(n):
        age = get_age(age)
        heigth = get_height(heigth)
        weigth = get_weigth(weigth)
    A,B,C = condition_1(age,n),condition_2(weigth,heigth),condition_3(age,heigth,n)
    print_results(A,B,C)