import os,sys

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_nums():
    done = False
    nums = []
    while done != True:
        try:
            n = int(input("Insira numeros positivos ou negativos.\nTotal de numeros inseridos: %d\n" % len(nums)))
            clear_screen()
            if n == 0:
                break
            else:
                nums.append(n)
        except:
            clear_screen()
            print("Erro, valor invalido\n")
    return nums

def results(nums):
    if len(nums) == 0:
        print("Nenhum numero inserido")
        sys.exit()
    pos = [x for x in nums if x > 0]
    neg = [x for x in nums if x < 0]
    s1,s2 = sum(pos),sum(neg)
    print("Soma dos numeros positivos: %d\nSoma dos numeros negativos: %d\nSoma dos numeros positivos e negativos: %d" % (s1,s2,(s1+s2)))

if __name__ == "__main__":
    clear_screen()
    nums = get_nums()
    results(nums)
