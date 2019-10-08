#variables
count = 0

#input statement 
bars = int(input("How many bars should be charged?\n"))

#while input is more than one print until equation is disproved
while count < bars:
    count +=1
    print("Charging:", count * "█ ")

#finish statement once while loop is complete
print("The battery is fully charged.")