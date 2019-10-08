#input
light = int(input("What level of brightness is required?\n"))

#for loop
for count in range (2, light,2):
    print("\nAdjusting brightness...")
    print("Beep's brightness level:" + count*"*")
    print("Bop's brightness level:" + count*"*")

#finish
print("\nAdjustments complete!")