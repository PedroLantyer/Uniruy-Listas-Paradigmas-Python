import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_channel():
    done,end = False, False
    while done != True:
        try:
            n = int(input("Insira o numero do canal:\nopcoes: 4,5,7,12\n"))
            match n:
                    case 0:
                        end = True
                    case 4:
                        n = 0
                    case 5:
                        n = 1
                    case 7:
                        n = 2
                    case 12:
                        n = 3
                    case _:
                        raise Exception()
        except:
            clear_screen()
            print("Erro, valor invalido")
        else:
            clear_screen()
            return n,end

def get_views(l1,pos):
    done,end = False,False
    while done != True:
        try:
            n = int(input("Insira o numero de espectadores:\n"))
            if n < 0:
                raise Exception()
            if n == 0:
                end = True
        except:
            clear_screen()
            print("Valor Invalido")
        else:
            clear_screen()
            l1[pos] += n
            return l1,end
        
def get_total(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def get_percentages(arr,sum):
    percent = [0,0,0,0]
    for i in range(len(arr)):
        percent[i] = ((arr[i]/sum)*100)
    return percent

def print_results(percent):
    channels = [4,5,7,12]
    for i in range(len(percent)):
        print("Porcentagem de espectadores do canal %d: %.2f%%" % (channels[i],percent[i]))

if __name__ == "__main__":
    clear_screen()
    end = False
    arr = [0,0,0,0]
    while end != True:
        pos,end = get_channel()
        if end == True:
            break
        arr,end = get_views(arr,pos)
    sum = get_total(arr)
    if sum != 0:
        percent = get_percentages(arr,sum)
        print_results(percent)
    else:
        print("Nenhum espectador")
        
