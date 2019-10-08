#var
count= 0
fact=1

#input
num = int(input("Please enter a number:\n"))

#loop
while num > count:
    count += 1
    fact *= count

#statement
print("The factorial is " +str(fact))

