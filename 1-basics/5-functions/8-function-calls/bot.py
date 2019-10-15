

def enterWord():
    counter = 0
    word = input("Please enter a word.\n")
    display = input("How would you like me to display this?\n")
    if display == "Display in a box":
        counter = counter + 1
        print("You've selected option", counter)
        displayInBox(word)
    elif display == "Display lower case":
        counter += 2
        print("You've selected option", counter)
        displayLower(word)
    elif display == "Display upper case":
        counter += 3
        print("You've selected option", counter)
        displayUpper(word)
    elif display == "Display mirror":
        counter += 4
        print("You've selected option", counter)
        displayMirror(word)
    elif display == "Repeat":
        counter += 5
        print("You've selected option", counter)
        repeat(word)

def displayInBox(word):
    print("*" * (len(word) + 4))
    print("*", word, "*")
    print("*" * (len(word) + 4))

def displayLower(word):
    print(word.lower())

def displayUpper(word):
    print(word.upper())

def displayMirror(word):
    phrase = ""
    #for loop
    for count in range(len(word), 0, -1):
        phrase += word[count-1]
    print(phrase)

def repeat(word):
    times = int(input("How many times should I repeat"))
    for count in range (times):
        print(word)

enterWord()
