#input
whole_num = int(input("How many zones must I cross?\n"))
#output
print("Crossing zones...")
#loop
while whole_num > 0:
    print("…crossed zone",whole_num)
    whole_num -= 1
#output
print("Crossed all zones. Jumanji!")