#define function
def climb_ladder(stepCross, stepRemain):
    if stepCross < stepRemain:
        print("Still some way to go!")
    else:
        print("We made it!")
#call function
climb_ladder(2, 5)
climb_ladder(5, 5)