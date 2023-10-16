import math,os
from decimal import *

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def age_check(age):
    try:
        n = int(input("Please insert your age:\n").strip())
        if n <= 0 or n >= 120:
            raise Exception()
    except:
        clear_screen()
        print("Please insert a number between 1 and 120\n")
        return age,False
    else:
        age.append(n)
        return age,True

def weight_check(weight):
    try:
        n = float(input("Please insert your weight:\n").strip())
        if math.floor(n) <= 0 or n >= 350:
            raise Exception()
    except:
        clear_screen()
        print("please insert a valid weight\nmust be between 1 and 350KG\n")
        return weight, False
    else:
        weight.append(n)
        return weight,True
    
def get_input(age,weight):
    done = False
    while done != True:
        age,done = age_check(age)
    clear_screen()
    done = False
    while done != True:
        weight,done = weight_check(weight)
    clear_screen()
    return age,weight

def over_90(weight):
    count = 0
    getcontext().prec = 2
    for i in range(len(weight)):
        weight[i] = Decimal(weight[i])
        if weight[i] > 90:
            count += 1
    return count

def avg_age(age):
    getcontext().prec = 2
    sum = 0
    for i in range(len(age)):
        sum += age[i]
    avg = Decimal(sum/len(age))
    return avg

if __name__ == "__main__":
    clear_screen()
    age,weight = [],[]
    for i in range(7):
        age,weight = get_input(age,weight)
    print(weight)
    print(age)
    input()
    ov_90 = over_90(weight)
    avg = avg_age(age)
    print("Heavier than 90KG: %d person(s)\nAverage age: %.2f years\n" % (ov_90,avg))