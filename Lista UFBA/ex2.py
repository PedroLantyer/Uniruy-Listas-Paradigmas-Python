import os,sys

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_num():
    num = []
    while (len(num)<10):
        try:
                n = int(input("Insira o numero º%d:\n" % (len(num)+1)))
                num.append(n)
                clear_screen()
        except:
            clear_screen()
            print("Erro, valor invalido\n")
    return num

def ver_num(num):
    done = False
    while done != True:
        try:
            n = int(input("Insira o numero a buscar:\n"))
            clear_screen()
            break
        except:
            clear_screen()
            print("Erro, valor invalido\n")
    pos = [i for i in range(len(num)) if num[i]==n]
    if len(pos) == 0:
        print("Valor não encontrado")
        sys.exit()
    else:
        s = "Valor encontrado na posição: "
        for i in range(len(pos)):
            s += str(pos[i])
            if i < (len(pos)-1):
                s += ","
        print(s)
        sys.exit()

if __name__ == "__main__":
    clear_screen()
    num = get_num()
    ver_num(num)