#input
word = input("What phrase do you see?\n")

#var
phrase = ""
print("reversing...")

#for
for count in word:
    phrase = count + phrase 

#finish
print("The phrase is:" + phrase)
print("done!")