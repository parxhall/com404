def sum_weights(bopWeight, beepWeight):
    total = bopWeight + beepWeight
    return total

def calc_avg_weight(bopWeight, beepWeight):
    avg = (bopWeight + beepWeight)/2
    return avg

def run():
    bopWeight = int(input("What is the weight of Bop?"))
    beepWeight = int(input("What is the weight of Beep?"))
    func = input("What would you like to calcluate (sum or average)?")
    if func == "sum":
        print("The sum of Bop and Beeps weight is", sum_weights(bopWeight, beepWeight))
    elif func == "average":
        print("The average of Bop and Beeps weight is", calc_avg_weight(bopWeight, beepWeight))
    else:
        print("What you talking bout willis?")

#call function
run()

