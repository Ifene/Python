import random

Monsters = []

Random_Monsters = ['Pixies', 'Dryad', 'Killmoulis', 'Korred', 'Boggle']

# Encounter_Number = []
# Encounter_Number.append(input("How many encounters? \n" ))


Choice = input("Do you wish for a 'random' generated monster or wish to 'choose' them? \n").lower()

if Choice == 'random':
    print("I've found these creature's stirring about: ", [Random_Monsters])
elif Choice == 'choose':
    input("Your choosing destiny then? Well here ya go.", [Monsters])
    print("Click the text of the monster to bring up the stat sheet.")
else:
    print("You've got allot of balls for messing with me, try again.")
