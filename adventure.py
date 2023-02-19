"""
This will blah blah ai
"""

# VAR
location = "home"
player_health = 100
enemy_health = 100


def displayOptions(location):
    if location == "home":
        print("You are at home (epic)")
        print("1. Go to the arena")
        print("2. balls")
    elif location == "arena":
        print("You are in the arena.")
        print("1. Battle AI")
        print("2. Return Home")

    else:
        pass

def getChoice():
    choice = input("Enter choice (1-2):")
    return choice


def updateLocation(choice, location):
    if location = "home":
        if location not "arena":



def battle(player_health, enemy_health):
    while player_health > 0 and enemy_health > 0
        print("What move do you wish to make?")
        print("1. Attack")
        print("2. Defend")
        move = getChoice()
        enemy_move = randint(1, 2)
        if enemy_move = 1:

            
        if enemy_move = 2:


while (location !="quit"):
    displayOptions(location)
    choice = getChoice()
    location = updateLocation(choice, location)

