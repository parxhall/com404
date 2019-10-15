#define function
def cross_bridge(step):
    #variables
    count = 0
    #while loop
    while step > count:
        count += 1
        #if statement
        if count < 5:
            print("Crossed step")
        elif count > 5:
            print("The bridge is collapsing!")
        else:
            print("we must keep going!")

#call function
cross_bridge(3)
cross_bridge(6)