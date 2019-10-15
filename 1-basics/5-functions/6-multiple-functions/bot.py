def display_ladder(steps):
    print("""
    | |
    ***""" * (steps))

def create_ladder():
    steps = int(input("How many steps are remaining?\n"))
    display_ladder(steps)

create_ladder()