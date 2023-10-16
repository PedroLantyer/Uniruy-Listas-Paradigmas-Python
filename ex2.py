import os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

if __name__ == "__main__":
    done = False
    while done != True:
        try:
            n = int(input("insira um numéro inteiro e positivo: \n"))
            if n <= 0:
                raise Exception()
        except:
            clear_screen()
            print("input invalido, tente novamente")
            done = False
        else:
            sum = 0
            for i in range(1,n+1):
                sum += 1/i
            print("%.4f" %sum)
            done = True