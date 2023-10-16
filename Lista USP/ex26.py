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

def age_check(age):
    done = False
    i = 1
    while done == False:
        try:
            n = int(input("#%d Please insert your age:\nalternatively insert 0 to end\n" % i).strip())
            if n < 0 or n >= 120:
                raise Exception()
        except:
            clear_screen()
            print("Please insert a number between 1 and 120 or type 0 to end\n")
        else:
            clear_screen()
            i += 1
            if n == 0:
                return age
            else:
                age.append(n)

def average_calc(age):
    if len(age) == 0:
        return "No value"
    else:
        getcontext().prec = 2
        sum = 0
        for i in range(len(age)):
            sum += age[i]
        avg = "Media: " + str(Decimal(sum/len(age)))
        return avg

if __name__ == "__main__":
    clear_screen()
    age = []
    age = age_check(age)
    avg = average_calc(age)
    print(avg)
