import os
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_salario(salario):
    global done
    while done != True:
        try:
            n = Decimal(input("Insira o valor do salário:\n"))
        except:
            clear_screen()
            print("valor invalido")
        else:
            break
    clear_screen()
    if n < 0:
        return salario,True
    else:
        salario.append(n)
        return salario,False


def get_filhos(filhos):
    global done
    while done != True:
        try:
            n = int(input("Insira o numero de filhos:\n"))
        except:
            clear_screen()
            print("valor invalido")
        else:
            break
    clear_screen()
    if n < 0:
        filhos.append(0)
        return filhos,True
    else:
        filhos.append(n)
        return filhos,False

def get_values(salario,filhos):
    global done
    done = False
    while done == False:
        salario,done = get_salario(salario)
        if done == True:
            break
        filhos,done = get_filhos(filhos)
    return salario,filhos

def highest_wage(salario):
    salario.sort(reverse=True)
    return("Maior salário: R$%.2f" % (salario[0]))

def avg_wage(salario):
    getcontext().prec = 2
    sum = Decimal(0)
    for i in range(len(salario)):
        sum += salario[i]
    avg = Decimal(sum/len(salario))
    return ("Média dos salários: R$%.2f" % avg)
    
def avg_filhos(filhos):
    getcontext().prec = 2
    sum = Decimal(0)
    for i in range(len(filhos)):
        sum += filhos[i]
    avg = Decimal(sum/len(filhos))
    return ("Média do numero de filhos: %.2f" % avg)

def percentage(salario):
    getcontext().prec = 2
    count = 0
    for i in salario:
        if i <= 150:
            count += 1
    percent = Decimal((count/len(salario))*100)
    return ("Porcentagem de pessoas com salário até R$150: %.2f%%" % percent)
    
if __name__ == "__main__":
    clear_screen()
    salario,filhos = [],[]
    salario,filhos = get_values(salario,filhos)
    if len(salario) == 0:
        print("Nenhum valor inserido")
        exit()
    print(avg_wage(salario))
    print(avg_filhos(filhos))
    print(highest_wage(salario))
    print(percentage(salario))
    
