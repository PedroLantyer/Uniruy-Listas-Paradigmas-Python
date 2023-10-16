import os

class duplicate_registration(Exception):
    #exception triggered if registration value is a duplicate
    pass

#Global variable for names
sim_names = ["James","Kirk","Lars","Robert","Jason","Cliff","Dave","Gary","Tom","Scott","Becker","Steve","Yngwie","Zakk","Joe"]

def clear_screen():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except:
        pass

def get_score(score,i):
    n = 1
    while len(score[i]) != 3:
        try:
            x = int(input("please insert score #%d:\n" % n).strip())
            if x < 0 or x > 10:
                raise Exception()
        except:
            clear_screen()
            print("Error, please insert a number between 0 and 10")
        else:
            clear_screen()
            n += 1
            score[i].append(x)
            if score[i][0] == -1:
                del score[i][0]
    return score,True

def get_attendance(attendance):
    try:
        x = int(input("please insert the amount of lessons attended:\nNOTES: Max value is 120\n").strip())
        if x < 0 or x > 120:
            raise Exception()
    except:
        clear_screen()
        print("Error, please insert a number between 0 and 120")
        return attendance,False
    else:
        clear_screen()
        attendance.append(x)
        return attendance,True
    
def get_registration(registration):
    try:
        s = input("Please insert your registration number:\nNote:must contain 8 numbers\n").strip()
        if len(s) != 8:
            raise Exception()
        n = int(s)
        if len(registration) != 0:
            for i in range(len(registration)):
                if n == registration[i]:
                    raise duplicate_registration()
    except duplicate_registration:
        clear_screen()
        print("Error, this registration has already been inserted, please type a different registration")
        return registration,False
    except:
        clear_screen()
        print("Error, please insert a valid registration number")
        return registration,False
    else:
        clear_screen()
        registration.append(n)
        return registration,True

def get_input(n):
    attendance,registration = [],[]
    score = [[-1 for i in range(1)] for j in range(n)]
    for i in range(n):
        clear_screen()
        done = False
        while done != True:
            registration,done = get_registration(registration)
        clear_screen()
        done = False
        while done != True:
            score,done = get_score(score,i)
        clear_screen()
        done = False
        while done != True:
            attendance,done = get_attendance(attendance)
        clear_screen()
    return registration,score,attendance

def student_result(result,score,i):
    sum = 0
    for j in range(3):
        sum += score[i][j]
    avg = sum/3
    result.append(avg)
    return result

def extremes(result,registration):
    low = min(result)
    high = max(result)
    lowest = [i for i in range(len(result)) if result[i] == low]
    highest = [i for i in range(len(result)) if result[i] == high]
    return lowest,highest,low,high

def automated_inputs():
    #function used only during testing
    clear_screen()
    n = 15
    print("Automated inputs\nValues:")
    registration = [i for i in range(12345671,(12345671+n+1))]
    score = [[(j+5) for i in range(3)] for j in range(n) if j + 5 <= 10]
    while len(score) != n:
        for i in range(len(score),n):
            score.append([4,4,4])
    attendance = [i for i in range(40,(40+(n*10)),10) if i < 120]
    while len(attendance) != n:
        k = 50
        for i in range(len(attendance),n):
            attendance.append(k)
            k -= 3
    print(registration)
    print(attendance)
    print(score)
    print("Press enter")
    input()
    clear_screen()
    return registration,score,attendance,n
    #function used only during testing

def print_min_max(lowest,highest,low,high,registration):
    print("Lowest score: %d" % low)
    print("Student(s) with the lowest score:")
    for i in range(len(lowest)):
       print("Name: %s - Registration: %d" % (sim_names[lowest[i]],registration[lowest[i]]))
       if i == (len(lowest)-1):
        print()
    print("Highest score: %d" % high)
    print("Student(s) with the highest score:")
    for i in range(len(highest)):
        print("Name: %s - Registration: %d" % (sim_names[highest[i]],registration[highest[i]]))
        if i == (len(highest)-1):
            print()

def failed(result,attendance):
    count = [0,0,0,0]
    for i in range(len(result)):
        if attendance[i] < 40 and result[i] < 6:
            count[3] += 1
            count[2] += 1
        elif attendance[i] < 40:
            count[3] += 1
            count[1] += 1
        elif result[i] < 6:
            count[3] += 1
            count[0] += 1
    return count

def print_fails(count):
    print("Students who weren't approved: %d" % (count[3]))
    print("Students who weren't approved due to having both low scores and low attendance: %d" % (count[2]))
    print("Students who weren't approved due to low scores (and only low scores): %d" % (count[0]))
    print("Students who weren't approved due to low attendance (and only low attendance): %d" % (count[1]))

def print_student(registration,result,attendance):
    print("Students: \n")
    for i in range(len(result)):
        print("Registration: %d" % registration[i])
        print("Name: %s" % sim_names[i])
        if result[i] < 6 or attendance[i] < 40:
            print("Not approved")
        else:
            print("approved")
        if i != len(result)-1:
            print()

def print_everything(registration,result,attendance,lowest,highest,low,high,count):
    print_student(registration,result,attendance)
    print_min_max(lowest,highest,low,high,registration)
    print_fails(count)

if __name__ == "__main__":
    n = 3
    result = []
    op = 0
    #op = 1 #used only during testing
    if op == 0:
        registration,score,attendance = get_input(n)
    else:
        #sets automated values for the inputs, used to streamline testing
        registration,score,attendance,n = automated_inputs()
    for i in range(n):
        result = student_result(result,score,i)
    lowest,highest,low,high = extremes(result,registration)
    count = failed(result,attendance)
    print_everything(registration,result,attendance,lowest,highest,low,high,count)


    