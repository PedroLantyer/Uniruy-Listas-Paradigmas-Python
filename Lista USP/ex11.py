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

def check_value(n):
    try:
        n = Decimal(n)
        if n <= 0:
            raise Exception()
    except:
        clear_screen()
        print("Valor invalido, por favor insira um numero maior que 0")
        return False
    else:
        return True
    
def check_char(ch):
    try:
        if len(ch) == 0 or (ch[0].upper() != "P" and ch[0].upper() != "V"):
            raise Exception()
    except:
        clear_screen()
        print("ERRO: por favor insira \'P\' ou \'V\'\n")
        return False
    else:
        return True
    

def get_input():
    getcontext().prec = 2
    parcela = []
    total_P = 0
    total_V = 0
    for i in range(15):
        done = False
        while done != True:
            ch = input("Insira \'P\' para compra parcelada ou insira 'V' para compra a vista:\nNOTA: Apenas o primeiro valor inserido sera válido\n").strip()
            done = check_char(ch)
        done = False
        clear_screen()
        while done != True:
            n = input()
            done = check_value(n)
        n = n
        clear_screen()
        if ch[0].upper() == "P":
            parcela.append(float(n))
            total_P += Decimal(n)
        elif ch[0].upper() == "V":
            total_V += Decimal(n)
    return total_P,total_V,parcela

if __name__ == "__main__":
    clear_screen()
    total_p,total_v,parcela = get_input()
    print("Total das compras a vista: R$%.2f\nTotal das compras parceladas: R$%.2f\nTotal das compras: R$%.2f\n" % (total_v,total_p,(total_p+total_v)))
    for i in range(len(parcela)):
        print("Valor da primeira parcela da compra parcela #%d = R$%.2f" % ((i+1),Decimal(parcela[i]/3)))