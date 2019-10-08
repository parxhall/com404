#var
count = 0
total = 0

#input statement
num = int(input("How many numbers should i sum up?\n"))

while num > count:
    count += 1
    total += int(input("Please enter number "+ str(count) +" of "+ str(num) +":\n"))

#finish statement
print("The answer is "+ str(total))