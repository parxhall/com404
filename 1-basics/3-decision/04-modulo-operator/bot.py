#ask for input and give it a datatype
num = int(input("Please enter a whole number.\n"))
#if statement, % remainder
if (num % 2) == 0:
    print("The number {0} is an even number." .format(num))
else:
    print("The number {0} is an odd number.". format(num))