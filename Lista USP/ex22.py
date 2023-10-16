import math,os

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
    clear_screen()
    done = False
    while done != True:
        age,done = age_check(age)
    clear_screen()
    done = False
    while done != True:
        weight,done = weight_check(weight)
    clear_screen()
    return age,weight

def groups(age,weight):
    results = [[0 for i in range(0)]for j in range(4)]
    for i in range(len(age)):
        if age[i] <= 10:
            results[0].append(weight[i])
        elif age[i] > 10 and age[i] <= 20:
            results[1].append(weight[i])
        elif age[i] > 20 and age[i] <= 30:
            results[2].append(weight[i])
        elif age[i] > 30:
            results[3].append(weight[i])
    return results

if __name__ == "__main__":
    clear_screen()
    age, weight = [],[]
    for i in range(5):
        age, weight = get_input(age,weight)
    results = groups(age,weight)
    strings = ["1 to 10 year(s) old","11 to 20 years old", "21 to 30 years old", "31 and older"]
    for i in range(len(results)):
        sum = 0
        for j in range(len(results[i])):
            sum += results[i][j]
        else:
            if len(results[i]) != 0:
                avg = (sum/len(results[i]))
            else:
                avg = 0
            print("Average weight in age group - %s: %.2f" % (strings[i],avg))
    