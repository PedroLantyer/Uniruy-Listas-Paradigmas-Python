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

def op_A(num):
    count = 0
    for i in range(len(num)):
         if (num[i] != 0) and (num[i] % 2 == 0):
            count += 1
    return count

def print_arr(num):
    for i in range(len(num)):
        if i < len(num)-1:
            print(num[i],end=" , ")
        else:
            print(num[i])

if __name__ == "__main__":
    clear_screen()
    num = get_num()
    print_arr(num)
    print(op_A(num))