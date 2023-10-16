import os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_weigth(weigth):
    getcontext().prec = 2
    continue_op = True
    while continue_op != False:
        try:
            weigth_i = Decimal(input("Por favor insira seu peso em KG:\n"))
            if weigth_i < 20 or weigth_i > 300:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um peso entre 20KG e 300KG")
        else:
            clear_screen()
            weigth.append(weigth_i)
            break
    return weigth

def get_height(weigth):
    continue_op = True
    while continue_op != False:
        try:
            heigth_i = int(input("Por favor insira sua altura em cm:\n"))
            if heigth_i < 50 or heigth_i > 250:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira uma altura entre 50 e 250cm")
        else:
            clear_screen()
            heigth.append(heigth_i)
            break
    return heigth

def get_age(age):
    continue_op = True
    while continue_op != False:
        try:
            age_i = int(input("Por favor insira sua idade:\n"))
            if age_i < 1 or age_i > 120:
                raise Exception()
        except:
            clear_screen()
            print("Erro, por favor insira um numero entre 1 e 120")
        else:
            clear_screen()
            age.append(age_i)
            break
    return age

def eye_color(eye):
    continue_op = True
    while continue_op != False:
        try:
            eye_c = input("Por favor escolha a cor do seu olho:\nA - Azul\nP - Preto\nV - Verde\nC -Castanho\n")[0].strip().upper()
            match eye_c:
                case 'A':
                    eye_c = "Azul"
                case 'P':
                    eye_c = "Preto"
                case 'V':
                    eye_c = "Verde"
                case 'C':
                    eye_c = "Castanho"
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Error, por favor escolha uma das opções disponiveis")
        else:
            clear_screen()
            eye.append(eye_c)
            break
    return eye

def hair_color(hair):
    continue_op = True
    while continue_op != False:
        try:
            hair_c = input("Por favor insira a cor do seu cabelo:\nP - Preto\nC- Castanho\nR - Ruivo\nL - Louro\n")[0].strip().upper()
            match hair_c:
                case 'L':
                    hair_c = "Louro"
                case 'P':
                    hair_c = "Preto"
                case 'R':
                    hair_c = "Ruivo"
                case 'C':
                    hair_c = "Castanho"
                case _:
                    raise Exception()
        except:
            clear_screen()
            print("Error, por favor escolha uma das opções disponiveis")
        else:
            clear_screen()
            hair.append(hair_c)
            break
    return hair

def condition_1(age,weigth):
    count = 0
    for i in range(len(age)):
        if age[i] > 50 and weigth[i] < 60:
            count += 1
    return count

def condition_2(age,heigth):
    getcontext().prec = 2
    sum,count = 0,0
    for i in range(len(age)):
        if heigth[i] < 150:
            sum += age[i]
            count += 1
    media = Decimal(sum/count)
    return media

def conditions_3_and_4(eye,hair,n):
    getcontext().prec = 2
    x,D = 0,0
    for i in range(len(eye)):
        if eye[i] == "Azul":
            x += 1
        elif eye[i] != "Azul" and hair[i] == "Ruivo":
            D += 1
    C = Decimal((x/n)*100)
    return C,D

def print_results(A,B,C,D):
    print("Maiores de 50 anos e com peso inferior a 50KG: %d pessoa(s)" % A)
    print("Media de idade das pessoas com altura inferior a 1.5m: %.2f ano(s)" % B)
    print("Porcentagem de pessoas que tem olho azul: %.2f%%" % C)
    print("Tem cabelo ruivo e não tem olho azul: %d pessoa(s)" % D)

if __name__ == "__main__":
    clear_screen()
    n = 20
    weigth,age,eye,hair,heigth = [],[],[],[],[]
    for i in range(n):
        age = get_age(age)
        heigth = get_height(heigth)
        weigth = get_weigth(weigth)
        eye = eye_color(eye)
        hair = hair_color(hair)
    A = condition_1(age,weigth)
    B = condition_2(age,heigth)
    C,D = conditions_3_and_4(eye,hair,n)
    print_results(A,B,C,D)
    