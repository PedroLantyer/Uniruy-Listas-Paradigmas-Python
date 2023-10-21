import random,os,string,sys
from decimal import *

#NOTA PARA O PROFESSOR: SE O SENHOR QUISER FAZER OS TESTES MAIS RÁPIDO, BASTA APERTAR ENTER QUE ELE VAI ATRIBUIR UM VALOR ALEATORIO AO INPUT


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_stock(stock):
    chars = list(string.ascii_uppercase)
    chars.remove("F")
    try:
        ch = (input("Insira a letra correspondente a ação, ou insira \'F\' para terminar\n").strip().upper())[0]
        if (ch.isalpha()) != True:
            raise Exception()
    except:
        clear_screen()
        ch = random.choice(chars)
        print("Erro, valor invalido! Valor aleatorio inserido: %c" % ch)
        stock.append(ch)
        return stock,False
    else:
        clear_screen()
        if ch == "F":
            return stock,True
        else:
            stock.append(ch)
            return stock,False

def get_prices(price_list,operation):
    try:
        n = float(input("Por favor insira o valor de %s da ação\n" % operation))
        if n <= 0:
            raise Exception()
    except:
        clear_screen()
        n = float(random.randint(1,1000)+(random.randint(0,99) % 100))
        print("Erro, valor invalido! Valor aleatorio inserido: %.2f" % n)
    else:
        clear_screen()
    price_list.append(n)
    return price_list

def get_values():
    stock,buy,sell = [],[],[]
    done = False
    while done != True:
        stock,done = get_stock(stock)
        if done == True:
            break
        buy = get_prices(buy,"compra")
        sell = get_prices(sell,"venda")
    return stock,buy,sell

def get_profit(stock,buy,sell):
    profit,count,total = [],[0,0], 0
    for i in range(len(stock)):
        val = sell[i]-buy[i]
        profit.append(val)
        if val < 200:
            count[0] += 1
        elif val > 1000:
            count[1] += 1
    for i in range(len(profit)):
        total += profit[i]
    return profit,count,total

def print_results(profit,count,total):
    for i in range(len(profit)):
        print("Lucro da ação numero %d: R$%.2f" % ((i+1),profit[i]))
    print("Total de ações com lucro abaixo de R$200: %d" % count[0])
    print("Total de ações com lucro acima de R$1000: %d" % count[1])
    print("Lucro total: %.2f" % total)

if __name__ == "__main__":
    clear_screen()
    stock,buy,sell = get_values()
    if len(stock) == 0:
        print("Nenhum valor inserido")
        sys.exit()
    else:
        profit,count,total = get_profit(stock,buy,sell)
        print_results(profit,count,total)
