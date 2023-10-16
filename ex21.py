import math,os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_num():
    done = False
    while done != True:
        try:
            l1 = input("Por favor insira um numero inteiro e positivo ou nulo:\n").split()
            num = int(l1[0])
            if num < 0:
                raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido:\n")
        else:
            done = True
    clear_screen()
    return num

def fatorial(num):
    result = 1
    if num != 0:
        for i in range(1,num+1):
            result *= i
    else:
        pass
    return result

def exit_prompt():
    done = False
    while done != True:
        try:
            l1 = input("Digite \"SIM\" para continuar ou digite \"NAO\" para terminar o programa\n").split()
            s = (l1[0].upper())[0:3]
            print(len(s))
            if (s != "SIM" and s != "NAO" and s != "NÃO"):
                raise Exception()
        except:
            clear_screen()
            print("Não consegui entender")
        else:
            if s == "SIM":
                return not(True)
            else:
                return not(False)

if __name__ == "__main__":
    clear_screen()
    done = False
    while done != True:
        clear_screen()
        num = get_num()
        result =  fatorial(num)
        print("%d! = %d" % (num,result))
        done = exit_prompt()
    clear_screen()