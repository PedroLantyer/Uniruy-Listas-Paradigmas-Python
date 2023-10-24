import os,sys,multiprocessing
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_codigo(codigo):
    done = False
    while done != True:
        try:
            n = int(input("Insira o codigo do cliente:\n"))
            clear_screen()
            if n <= 0:
                return codigo,True
            else:
                codigo.append(n)
                return codigo,False
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def get_tipo(tipo):
    done = False
    while done != True:
        try:
            n = int(input("Insira o tipo da conta:\n1. Poupança\n2. Poupança Plus\n3. Fundos de renda fixa\n"))
            match n:
                case 1|2|3:
                    clear_screen()
                    tipo.append(n)
                    return tipo
                case _: raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido\n")    

def get_investimento(investimento):
    done = False
    while done != True:
        try:
            n = float(input("Insira o valor do investimento:\n"))
            if n <= 0:
                raise Exception()
            else:
                investimento.append(n)
                return investimento
        except:
            clear_screen()
            print("Erro, valor invalido\n")

def get_values():
    done = False
    codigo,tipo,investimento = [],[],[]
    while done != True:
        codigo,done = get_codigo(codigo)
        if done == True:
            break
        tipo = get_tipo(tipo)
        investimento = get_investimento(investimento)
        clear_screen()
    return codigo,tipo,investimento

def total_value(investimento):
    print("Valor total investido: %.2f" % sum(investimento))

def juros(tipo,investimento):
    for i in len(investimento):
        match tipo[i]:
            case 1: investimento[i] *= (1*(15/1000))
            case 2: investimento[i] *= (1*(2/100))
            case 3: investimento[i] *= (1*(4/100))
    print("Juros: %.2f" % (sum(investimento)))

if __name__ == "__main__":
    clear_screen()
    codigo,tipo,investimento = get_values()
    proc = multiprocessing.Process(target=total_value,args=(investimento, ))
    proc2 = multiprocessing.Process(target=juros,args = (tipo,investimento, ))
    proc.start()
    proc2.start()
    proc2.join()