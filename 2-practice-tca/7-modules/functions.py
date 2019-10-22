def enterWord():
    #input
    word = input("Please enter a word.\n")
    display = input("How would you like me to display this?\n")
    #if statement
    if display == "1":
        func_1(word)
    elif display == "2":
        func_2(word)
    elif display == "3":
        func_3(word)
    elif display == "4":
        func_4(word)

#functions
def func_1(word):
    print(word)
    print("*" * (len(word)))

def func_2(word):
    print("*" * (len(word)))
    print(word)

def func_3(word):
    print("*" * (len(word)))
    print(word)
    print("*" * (len(word)))

def func_4(word):
    num = int(input("how many times?\n"))
    print(("*" * (len(word))+"   ")* num)
    print((word+" | ")* num)
    print(("*" * (len(word))+"   ")* num)

enterWord()