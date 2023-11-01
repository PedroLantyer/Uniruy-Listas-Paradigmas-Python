import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_arr(arr,s):
    print("Numeros %s: " % s, end= "")
    if len(arr) == 0:
        print("Nenhum valor")
    for i in range(len(arr)):
        if i < (len(arr)-1):
            print(arr[i], end= " , ")
        else:
            print(arr[i])

def build_arr(pos,neg,n):
    if n > 0:
        pos.append(n)
        if len(pos) == 5:
            print_arr(pos,"positivos")
            print()
            pos.clear()
    if n < 0:
        neg.append(n)
        if len(neg) == 5:
            print_arr(neg,"negativos")
            print()
            neg.clear()

def get_nums():
    done = False
    pos,neg = [],[]
    count = 1
    while done != True:
        try:
            n = int(input("Insira o %dº numero ou insira 0 para terminar:\n" % count))
            count += 1
            if n == 0:
                clear_screen()
                break
            else:
                clear_screen()
                build_arr(pos,neg,n)
        except:
            clear_screen()
            print("Valor invalido")
    return pos,neg

if __name__ == "__main__":
    clear_screen()
    pos,neg = get_nums()
    print_arr(pos,"positivos")
    print_arr(neg,"negativos")