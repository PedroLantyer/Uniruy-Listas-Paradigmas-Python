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
    salario.append(n)
    return salario
    
def age_check(age):
    global done
    while done != True:
        try:
            n = int(input("Por favor insira sua idade:\n").strip())
            if n >= 120:
                raise Exception()
        except:
            clear_screen()
            print("Por favor insira uma idade até 120\n")
        else:
            break
    if n < 0:
        return age,True
    else:
        age.append(n)
        return age,False

def sex_check(sex):
    global done
    while done != True:  
        try:
            ch = input("Digite \'M\' para masculino ou \'F\' para feminino:\n").strip()
            ch = ch[0].upper()
            if ch != 'M' and ch != 'F':
                raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido")
        else:
            break
    sex.append(ch)
    return sex
    
def get_values():
    global done
    done = False
    age,sex,salario = [],[],[]
    while done != True:
        age,done = age_check(age)
        if done == True:
            break
        clear_screen()
        sex = sex_check(sex)
        clear_screen()
        salario = get_salario(salario)
    clear_screen()
    return age,sex,salario

def avg_wage(salario):
    getcontext().prec = 2
    sum = Decimal(0)
    for i in range(len(salario)):
        sum += salario[i]
    avg = Decimal(sum/len(salario))
    return ("Média dos salários: R$%.2f" % avg)

def extremes_age(age):
    min_val = min(age)
    max_val = max(age)
    return("Menor idade: %s\nMaior idade: %s" % (min_val,max_val))

def condition_C(salario,sex):
    count = 0
    for i in range(len(salario)):
        if salario[i] <= 200 and sex[i] == 'F':
            count += 1
    return("Numero de mulheres com o salário até R$200: %d" % count)

def condition_D(age,sex,salario):
    indexes = []
    print("\nDados referentes ao menor salário:")
    for i in range(len(salario)):
        if salario[i] == min(salario):
            indexes.append(i)
    for i in range(len(indexes)):
        if i > 0:
            print()
        print("Idade: %s" % age[indexes[i]])
        print("Sexo: %s" % sex[indexes[i]])
        print("Salario: %s" % sex[indexes[i]])
    print()

if __name__ == "__main__":
    clear_screen()
    age,sex,salario = get_values()
    print(avg_wage(salario))
    print(extremes_age(age))
    print(condition_C(salario,sex))
    condition_D(age,sex,salario)