import os,sys
from decimal import *

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_input():
    votes = [0,0,0,0,0,0]
    done = False
    while done != True:
        try:
            for i in range(4):
                print("%d - Candidato %c" % (i+1,chr(65+i)))
            print("5 - Voto nulo\n6 - Voto em branco\n0 - Sair")
            n = int(input("Insira seu voto:\n"))
            match n:
                case 1|2|3|4|5|6: votes[n-1] += 1
                case 0: break
                case _: raise Exception()
            clear_screen()
        except:
            clear_screen()
            print("Valor invalido\n")
    clear_screen()
    return votes

def results(votes):
    print("Votos:")
    for i in range(4):
        print("Candidato %c: %d" % (chr(65+i),votes[i]))
    print("Branco: %d" % votes[4])
    print("Nulo: %d\n" % votes[5])

def percents(votes):
    getcontext().prec = 2
    p1 = Decimal((votes[4]/sum(votes))*100)
    p2 = Decimal((votes[5]/sum(votes))*100)
    print("Porcentagem de votos em branco: %.2f%%\nPorcentagem de votos nulos: %.2f%%\n" % (p1,p2))

if __name__ == "__main__":
    clear_screen()
    votes = get_input()
    if sum(votes) == 0:
        print("Nenhum voto")
        sys.exit()
    else:
        results(votes)
        percents(votes)
        pass