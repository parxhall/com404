#ask what book they're reading
cover = input("What type of cover does the book have?\n")
#if statement
if cover == "soft":
    bound = input("Is the book perfect-bound?\n")
    #inbedded if
    if bound =="yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
        #else if statement
elif cover == "hard":
    print("Books with hard covers can be more expensive!")