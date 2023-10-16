import os,math
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
        print("Please insert a number between 1 and 120")
        return age,False
    else:
        age.append(n)
        return age,True
    
def sex_check(sex):
    try:
        ch = input("Type \'M\' for male or \'F\' for female:\n").strip()
        ch = ch[0].upper()
        if ch != 'M' and ch != 'F':
            raise Exception()
    except:
        clear_screen()
        print("Error, invalid input")
        return sex,False
    else:
        sex.append(ch)
        return sex,True

def averages(age,sex):
    getcontext().prec = 2
    sum,sum_m,sum_f,male,female = 0,0,0,0,0
    for i in range(len(age)):
        if sex[i] == "M":
            sum_m += age[i]
            sum += age[i]
            male += 1
        elif sex[i] == "F":
            sum_f += age[i]
            sum += age[i]
            female += 1
    avg = Decimal(sum/len(age))
    if male != 0:
        avg_m = Decimal(sum_m/male)
    else:
        avg_m = 0
    if female != 0:
        avg_f = Decimal(sum_f/female)
    else:
        avg_f = 0
    return avg,avg_m,avg_f

def get_inputs(age,sex):
    done = False
    while done != True:
        age,done = age_check(age)
    clear_screen()
    done = False
    while done != True:
        sex,done = sex_check(sex)
    clear_screen()
    return sex,age

if __name__ == "__main__":
    clear_screen()
    age,sex = [],[]
    for i in range(7):
        sex,age = get_inputs(age,sex)
    avg,m,f = averages(age,sex)
    print("Average age = %.2f Years\nAverage age (Men) = %.2f Years\nAverage age (Women) = %.2f Years\n" % (avg,m,f))
