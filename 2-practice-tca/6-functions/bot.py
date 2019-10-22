#functions
def is_league_united(hero_1,hero_2):
    if hero_1 == "superman" and hero_2 == "wonder woman" or hero_1 == "wonder woman" and hero_2 == "superman":
        print("True")
    else:
        print("false")

def decide_plan(hero_1,hero_2):
    is_league_united(hero_1,hero_2)
    if is_league_united == "True":
        print("Time to save the world!")
    else:
        print("We must unite the league!")

def run():
    hero_1 = input("What is our first heros name?\n")
    hero_2 = input("What is our second heros name?\n")
    option = input("What should we do? (plan or league)\n")
    if option == "league":
        is_league_united(hero_1,hero_2)
    elif option == "plan":
        decide_plan(hero_1,hero_2)
    else:
        print("Invalid command. Please try again")

#run functions
run()
run()

