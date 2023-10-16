import os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def verify_input(n):
    try:
        n = int(n)
        if n > 120 or n <= 0:
            raise Exception()
    except:
        clear_screen()
        print("ERRO: Por favor insira uma idade maior que 0 e menor que 120:")
        return False
    else:
        return True

        

if __name__ == "__main__":
    arr = []
    count = 0
    clear_screen()
    for i in range(10):
        done = False
        while done != True:
            n = input("Por favor insira a idade em anos:\n")
            done = verify_input(n)
        else:
            arr.append(int(n))
            clear_screen()
    else:
        for i in range(len(arr)):
            if arr[i] >= 18:
                count += 1
        print("Numero de pessoas maiores de idade: %d" % count)