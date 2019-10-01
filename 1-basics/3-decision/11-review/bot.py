#ask for input
direction = input("Which way should we run?\n")
#if statement
if direction == "left":
    #input
    action = input("There is a branch in the way what should we do?\n")
    #nested if statement
    if action == "jump":
        print("Yes we made it over!")
    elif action =="go round":
        print("We are being too slow he is gaining!")
    else:
        print("You didn't decide fast enough")
#else if statement
elif direction == "right":
    print("Good choice, we're getting away!")
#else statment
else:
    print("You didn't decide fast enough")
#multiple conditions with logical if or statement
if (action == "jump") or (direction == "right"):
    print("Well done! We made it out alive!")
#else if and or statemant
elif (direction == "left") and (action != "jump" or "go round"):
    print("You didn't decide fast enough and the monster got you o-o")
