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

def get_input(nums):
    done = False
    while done != True:
        nums,done = check_input(nums)
    return nums

def check_input(nums):
    try:
        l1 = input("Insert a number:\n").split()
        n = Decimal(l1[0])
    except:
        clear_screen()
        print("Error, please insert a number")
        return nums, False
    else:
        nums.append(n)
        return nums,True

def between(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] >= 30 and nums[i] <= 90:
            count += 1
    return count

if __name__ == "__main__":
    clear_screen()
    nums = []
    for i in range(10):
        nums = get_input(nums)
        clear_screen()
    count = between(nums)
    print("Amount of numbers between 30 and 90 (Including 30 and 90): %d\n" % count)
