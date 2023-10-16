import os

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
        clear_screen()
        age.append(n)
        return age,True

def review_check(review):
    try:
        n = int(input("Please insert the score for the movie:\n1 - Regular\n2 - Good\n3 - Great\n").strip())
        match n:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                raise Exception
    except:
        clear_screen()
        print("Error, please input one of the values below\n")
        return review,False
    else:
        clear_screen()
        review.append(n)
        return review,True

def get_input(age,review):
    clear_screen()
    done = False
    while done != True:
        age,done = age_check(age)
    done = False
    while done != True:
        review,done = review_check(review)
    clear_screen()
    return age,review

def op_A(age,review):
    sum,count = 0,0
    for i in range(len(age)):
        if review[i] == 3:
            sum += age[i]
            count += 1
    avg = (sum/count)
    return avg

def op_B(review):
    count = 0
    for i in range(len(review)):
        if review[i] == 1:
            count += 1
    return count

def op_C(review):
    count = 0
    for i in range(len(review)):
        if review[i] == 2:
            count += 1
    percentage = ((count/len(review))*100)
    return percentage

def print_result(A,B,C):
    print("Average age of people who tought the movie was great: %.2f year(s) old" % A)
    print("People who tought the movie was regular: %d" % B)
    print("Percentage of people who tought the movie was good: %.2f%%" % C)

if __name__ == "__main__":
    clear_screen()
    age,review,n = [],[],15
    for i in range(n):
        age,review = get_input(age,review)
    A,B,C = op_A(age,review),op_B(review),op_C(review)
    print_result(A,B,C)
