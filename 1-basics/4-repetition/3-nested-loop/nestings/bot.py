#var
pos1 = 0
pos2 = 0
poscount = 0

#input
seq = input("please enter a sequence (using - and a marker of your choice.\n")
char = input("please enter the character for the marker.\n")

#for
for count in seq:
    poscount += 1
    if count == char:
        if pos1 > 0:
            pos2 = poscount
        else:
            pos1 = poscount

#calculate distance
fincount = abs(pos2 -pos1) - 1


print("The distance between the markers is " + str(fincount))
