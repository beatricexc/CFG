#Battle droids top trumps

#Game compares a random stat
#loser gets removed from the list
#winer is the last one who is left in the list

#We will use 2D lists ( or arrays to make this game)

import random as r

def results(element,stat):
    if droids[position][element] > droids[randnum][element]:
        print(stat, droids[position][element], "vs", droids[randnum][element])
        print(droid_choice, " You win!")
        print(droids[randnum][0], " has been removed from the list")
        droids.remove(droids[randnum])
        print(droids)

    elif droids[position][element]< droids[randnum][element]:
        print(stat, droids[position][element], "vs", droids[randnum][element])
        print(droid_choice, "You lose!")
        print(droids[position][0], " has been removed from the list")
        droids.remove(droids[position])
        print(droids)
    else:
        print(stat, droids[position][element], "vs", droids[randnum][element])
        print("It's a draw!")

droids = [
    ["RD2D2", 3, 9,5],
    ["C3P0", 2, 8, 4],
    ["Robocop", 9,7,6],
    ["Terminator", 9, 4, 6]
]

while len(droids) > 1:
    print("Choose from the following droids: ")

    for x in range(len(droids)):
        print(droids[x][0])

    droid_choice = input("Please enter te droid name you want: ")

    for x in range(len(droids)):
        if droid_choice == droids[x][0]:
            print("Good choice!")
            position = x
            print(x)

            randnum = r.randint(0, len(droids)-1)# letting the computer choose a droid randomly

            print(randnum)

            while position == randnum:
                randnum = r.randint(0, len(droids)-1)
                print(randnum)

            print("The two droids to do the battle are: ")
            print(droids[position])
            print("AND")
            print(droids[randnum])

            attribute = input("""What attribute would you like to choose
            out of STRENGTH (s), INTELLIGENCE (i) or SPEED (s)""")

            if attribute == "s":
                stat = "Strength"
                results(1, stat)
            elif attribute == "i":
                stat = "Intelligence"
                results(2, stat)
            elif attribute == "sp":
                stat = "Speed"
                results(3, stat)
            else:
                print("Invalid input")
            break #breaking out of the loop

print(droids[0][0],"is the winner!")