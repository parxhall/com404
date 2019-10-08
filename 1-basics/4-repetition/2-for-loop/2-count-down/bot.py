#input
step = int(input("How far are we from the cave?\n"))

#for loop
for count in range (0, step,1):
    print(str(step - count) +" steps remaining")

#finish
print("\nWe have reached the cave!")