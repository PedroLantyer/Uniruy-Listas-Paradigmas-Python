import os

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

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

def answer_check(answer):
    try:
        ch = input("Did you like our new product?\nType \"Y\" for Yes or \"N\" for No\n").strip().upper()[0]
        if ch != "Y" and ch != "N":
            raise Exception()
    except:
        clear_screen()
        print("Error, please input one of the available options")
        return answer,False
    else:
        clear_screen()
        answer.append(ch)
        return answer,True
    
def get_inputs(sex,answer):
    done = False
    while done != True:
        sex,done = sex_check(sex)
    clear_screen()
    done = False
    while done != True:
        answer,done = answer_check(answer)
    clear_screen()
    return sex,answer

def op_A(answer):
    count = 0
    for i in range(len(answer)):
        if answer[i] == 'Y':
            count += 1
    return count

def op_B(answer):
    count = 0
    for i in range(len(answer)):
        if answer[i] == 'N':
            count += 1
    return count

def op_C(sex,answer):
    count = 0
    for i in range(len(answer)):
        if answer[i] == 'Y' and sex[i] == 'F':
            count += 1
    return count

def op_D(sex,answer):
    count = [0,0]
    for i in range(len(answer)):
        if sex[i] == 'M':
            if answer[i] == 'N':
                count[0] += 1
            count[1] += 1
    percentage = ((count[0]/count[1])*100)
    return percentage

def print_result(A,B,C,D):
    print("Answered \"Yes\": %d person(s)" % A)
    print("Answered \"No\": %d person(s)" % B)
    print("Amount of women who answered \"Yes\": %d" % C)
    print("Percentage of men who answered \"No\": %.2f%%" % D)

if __name__ == "__main__":
    sex,answer,n = [],[],5
    clear_screen()
    for i in range(n):
        sex,answer = get_inputs(sex,answer)
    A,B,C,D = op_A(answer),op_B(answer),op_C(sex,answer),op_D(sex,answer)
    print_result(A,B,C,D)