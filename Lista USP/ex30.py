import random,os,sys
from decimal import *

#NOTA PARA O PROFESSOR: SE O SENHOR QUISER FAZER OS TESTES MAIS RÁPIDO, BASTA APERTAR ENTER QUE ELE VAI ATRIBUIR UM VALOR ALEATORIO AO INPUT


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_price(og_price):
    try:
        n = float(input("Insira o preço do produto:\n"))
        if n < 0:
            raise Exception()
    except:
        clear_screen()
        n = float(random.randint(10,500)+(random.randint(0,99)/100))
        print("Erro, valor invalido, inserido valor aleatorio\nvalor inserido: R$%d\n" % n)
        og_price.append(n)
    else:
        clear_screen()
        og_price.append(n)
    return og_price

def get_code(code):
    try:
        n = int(input("Insira o codigo do produto:\n"))
    except:
        clear_screen()
        n = int(random.randint(1,9999))
        print("Erro, valor invalido, inserindo valor aleatorio\nvalor inserido: %d\n" % n)
        code.append(n)
        return code, False
    else:
        clear_screen()
        if n < 0:
            return code,True
        else:
            code.append(n)
            return code,False

def get_values():
    code,og_price = [],[]
    done = False
    while done != True:
        code,done = get_code(code)
        if done == True:
            break
        og_price = get_price(og_price)
    return code,og_price

def alter_prices(adjusted_price):
    for i in range(len(adjusted_price)):
        adjusted_price[i] *= 1.2
    return adjusted_price

def price_avgs(og_price,adjusted_price):
    getcontext().prec = 2
    sum = [0,0]
    for i in range(len(og_price)):
        sum[0] += og_price[i]
        sum[1] += adjusted_price[i]
    avg_og,avg_adj = Decimal(sum[0]/len(og_price)), Decimal(sum[1]/len(adjusted_price))
    print("Media dos preços originais: R$%.2f\nMedia dos preços ajustados (aumento de 20%%): R$%.2f" % (avg_og,avg_adj))

def print_values(code,og_price,adjusted_price):
    lengths = [0 for i in range(len(code))]
    for i in range(len(code)):
        print("Codigo do produto: %d\nPreço original: R$%.2f\nPreço ajustado: R$%.2f\n" % (code[i],og_price[i],adjusted_price[i]))

if __name__ == "__main__":
    clear_screen()
    code,og_price = get_values()
    if len(code) == 0:
        print("Nenhum valor inserido")
        sys.exit()
    else:
        adjusted_price = [x for x in og_price]
        adjusted_price = alter_prices(adjusted_price)
        print_values(code,og_price,adjusted_price)
        price_avgs(og_price,adjusted_price)
