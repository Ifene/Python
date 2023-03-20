import random
import os
import time

Monsters = []

Dryad = "<a href='https://www.dndbeyond.com/monsters/16849-dryad'>Dryad</a>"

print(Dryad)

Random_Monsters = ['Pixies', Dryad, 'Killmoulis', 'Korred', 'Boggle']


# Encounter_Number = []
# Encounter_Number.append(input("How many encounters? \n" ))

Choice = input("Do you wish for a 'random' generated monster or wish to 'choose' them? \n").lower()

X = False
while X == False:
    if Choice == 'random':
        print("I've found these creature's stirring about: ", [Random_Monsters])
        X = True
    elif Choice == 'choose':
        print("Your choosing destiny then? Well here ya go. \n", 'Click the text of the monster to bring up the stat sheet. \n', [Monsters])
        X = True
    else:
        print("That's not an option I gave ye, try again.")
        X = True

