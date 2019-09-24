# questions for people to input
print("What is your name human?")
name = str(input())
print("How old are you (in years)?")
years = int(input())
print("How tall are you (in meters)?")
height = int(input())
print("How much do you weigh (in kilograms)?")
weight = int(input())
# this is the equation to work out the bmi using the data we've collected
bmi = weight/(height**2)
# this is where data is displayed
print(name, "you are", years, "years old and your bmi is ", bmi,".")