import os

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def answers():
    chars = []
    count = 1
    while len(chars) < 20:
        try:
            ch = input("Insira o gabarito da questão numero %d:\n" % count)
            if (ord(ch) in range(65,69)) == False:
                raise Exception()
            else:
                count += 1
                chars.append(ch)
        except:
            print("Valor invalido, insira \'A\',\'B\',\'C\',\'D\' ou \'E\'\n")
    return chars

def input(type):
    try:
        print("")

def students():
    arr = [0 for i in range(20) for j in range(50)]
    for i in range(len(arr)):
        for j in range(len(arr)[j]):

