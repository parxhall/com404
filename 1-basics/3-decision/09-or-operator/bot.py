#ask for input
adventure = input("What type of adventure should I have?\n")
#if statement
if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest!")
#else if
elif adventure == "safe" or "long":
    print("Taking the safe route!")
#else
else:
    print("Not sure which route to take.")