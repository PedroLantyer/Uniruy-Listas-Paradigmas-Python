import os,random
from decimal import *

#NOTA PARA O PROFESSOR: SE O SENHOR QUISER FAZER OS TESTES MAIS RÁPIDO, BASTA APERTAR ENTER QUE ELE VAI ATRIBUIR UM VALOR ALEATORIO AO INPUT

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def get_input():
    nums,done = [],False
    while done != True:
        try:
            if len(nums) == 0:
                n = int(input("Insira um numero ou insira \'0\' para terminar\n"))
            else:
                n = int(input("Insira outro numero ou insira \'0\' para terminar\n"))
        except:
            clear_screen()
            n = random.randint(1,1000)
            nums.append(n)
            print("Erro, valor inserido invalido, inserindo valor aleatorio. Numero inserido: %d\n" % n)
        else:
            clear_screen()
            if n == 0:
                break
            else:
                nums.append(n)
    return nums

def op_A(nums):
    count = 0
    for i in nums:
        if i < 35:
            count += 1
    print("Quantidade de numeros menores que 35: %d" % count)

def op_B(nums):
    getcontext().prec = 2
    sum,count = 0,0
    for i in nums:
        if i > 0:
            sum += i
            count += 1
    if count == 0:
        print("Media dos numeros inteiros: 0")
    else:
        avg = Decimal(sum/count)
        print("Media dos numeros inteiros: %.2f" % avg)

def op_C(nums):
    count = 0
    getcontext().prec = 2
    for i in nums:
        if i >= 50 and i <= 100:
            count += 1
    res = Decimal((count/len(nums))*100)
    print("Porcentagem de numeros entre 50 e 100: %.2f%%" % (res))

def op_D(nums):
    count = [0,0]
    getcontext().prec = 2
    for i in nums:
        if i < 50:
            count[0] += 1
            if i >= 10 and i <= 20:
                count[1] += 1
    if count[0] == 0:
        print("Porcentagem de numeros menores que 50 que estão no intervalo [10,20]: 0%")
    else:
        res = Decimal((count[1]/count[0])*100)
        print("Porcentagem de numeros menores que 50 que estão no intervalo [10,20]: %.2f%%" % res)

if __name__ == "__main__":
    clear_screen()
    nums = get_input()
    if len(nums) == 0:
        print("Nenhum valor inserido")
    else:
        op_A(nums)
        op_B(nums)
        op_C(nums)
        op_D(nums)