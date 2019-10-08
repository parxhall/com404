#variables
count = 0

#input statement 
live = int(input("How many live cables must I avoid?\n"))

#while input is more than one print until equation is disproved
while count < live:
    count +=1
    print("Avoiding......Done!", count, "live cable avoided!")

#finish statement once while loop is complete
print("All live cables have been avoided.")
