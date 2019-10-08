#input
word = input("What phrase do you see?\n")

#var
phrase = ""
print("reversing...")

#for loop
for count in range(len(word), 0, -1):
    phrase += word[count-1]


#finish
print("The phrase is:" + phrase)
print("done!")