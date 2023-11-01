import os

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

if __name__ == "__main__":
    clear_screen()
    num = get_num()
    for i in num:
        if i != num[len(num)-1]:
            print(i,end=" ")
        else:
            print(i)