#variables
health = 100
#output
print("Your health is 100%. Escape is in progress...")
#loop
for count in range(5):
    who = input("…Oh dear, who is that?\n")
    if who == "Smiler's Bot":
        health -= 20
        print("Time to jam out of here!")
    elif who == "Hacker":
        health += 20
        print("Yay! Better follow this one!")
    else:
        print("Phew, just another emoji!")
#output
print( "Escaped! Health is",health,"%")