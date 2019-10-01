#diclare variables
even = 0
odd = 0
#first input
f = int(input("Please enter the first whole number.\n"))
#second input
s = int(input("Please enter the second whole number.\n"))
#third input
t = int(input("Please enter the third whole number.\n"))

#if statement, % remainder
if (f % 2) == 0:
    even += 1
else:
    odd += 1
if (s % 2) == 0:
    even += 1
else:
    odd += 1
if (t % 2) == 0:
    even += 1
else:
    odd += 1

print("There were ", even ," even and ", odd ," odd numbers.")

