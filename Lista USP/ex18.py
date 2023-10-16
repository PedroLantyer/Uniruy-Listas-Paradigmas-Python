import os,math
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_num():
    getcontext().prec = 5
    done = False
    while done != True:
        try:
            l1 = input("Por favor insira o valor do carro:\n").split()
            num = Decimal(l1[0])
            if num <= 300:
                raise Exception()
        except:
            clear_screen()
            print("Valor invalido, por favor insira um numero maior que 300")
            done = False
        else:
            clear_screen()
            num = Decimal(l1[0])
            done = True
    return num

if __name__ == "__main__":
    clear_screen()
    getcontext().prec = 5
    num = get_num()
    print("Preço a vista: R$%.2f\nOpções de parcelamento:" % Decimal((num/10)*8))
    for i in range(1,11):
        juros = Decimal(1 + ((3/100) * i))
        parcela = Decimal((num*juros)/(i*6))
        print ("%dx R$%.2f" % ((i*6),parcela))

# floating point precision de 5 casas decimais utilizada para reduzir margem de erro.