from decimal import *
if __name__ == "__main__":
    l1 = []
    for i in range(4):
        l1.append(Decimal(input()))
    l2,l3 = l1.copy(),l1.copy()
    l2.sort(),l3.sort(reverse=True)
    l4 = [l1,l2,l3]
    for i in range(len(l4)):
        s = ""
        for j in range(len(l2)):
            s += str(l4[i][j]) + " "
        else: 
            print(s)
    