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
    
def height_check(height):
    try:
        n = float(input("Please insert your height:\n").strip())
        if math.floor(n) <= 25 or n >= 250:
            raise Exception()
    except:
        clear_screen()
        print("please insert a valid height\nmust be between 25 and 250cm\n")
        return height, False
    else:
        height.append(n)
        return height,True

def get_input(age,height,weight):
    done = False
    while done != True:
        age,done = age_check(age)
    clear_screen()
    done = False
    while done != True:
        height,done = height_check(height)
    clear_screen()
    done = False
    while done != True:
        weight,done = weight_check(weight)
    clear_screen()
    return age,height,weight

def age_group(age):
    elder = 0
    for i in range(len(age)):
        if age[i] > 50:
            elder += 1
    return elder

def avg_height(age,height):
    getcontext().prec = 2
    sum,count = 0,0 
    for i in range(len(age)):
        if age[i] >= 10 and age[i] <= 20:
            sum += height[i]
            count += 1
    if count != 0:
        avg = Decimal(sum/count)
    else:
        avg = 0
    return avg

def under_40(weight):
    getcontext().prec = 2
    count = 0
    for i in range(len(weight)):
        if weight[i] < 40:
            count += 1
    if count != 0:
        percent = Decimal((count/len(weight))*100)
    else:
        percent = 0
    return percent

if __name__ == "__main__":
    clear_screen()
    age,height,weight = [],[],[]
    for i in range(25):
        age,height,weight = get_input(age,height,weight)
    elder = age_group(age)
    avg = avg_height(age,height)
    percent = under_40(weight)
    print("Older than 50yo: %d person(s)\nAverage height of people who are between 10 and 20yo: %.2fcm\nPercentage of people under 40KG: %.2f%%\n" % (elder,avg,percent))