import random

# Item Values

# Simple Melee Weapons
Club = "Club: 1sp"
Dagger = "Dagger: 2gp"
Great_Club = "Great Club: 2sp"
Handaxe = "Handaxe: 5gp"
Javelin = "Javelin: 5sp"
Light_Hammer = "Light Hammer: 2gp"
Mace = "Mace: 5gp"
Quater_Staff = "Quater Staff: 2sp"
Sickle = "Sickle: 1gp"
Spear = "Spear: 1gp"

# Simple Ranged Weapons
Light_Crossbow = "Light Crossbow: 25gp"
Dart = "Dart: 5cp"
Shortbow = "Shortbow: 25gp"
Sling = "Sling: 1sp"

# Martial Melee Weapons
Battle_Axe = "Battle Axe: 10gp"
Flail = "Flail: 10gp"
Glaive = "Glaive: 20gp"
Greataxe = "Greataxe: 30gp"
Great_Sword = "Great Sword: 50gp"
Halberd = "Halberd: 20gp"
Lance = "Lance: 10gp"
Long_Sword = "Long Sword: 15gp"
Maul = "Maul: 10gp"
Morning_Star = "Morning Star: 15gp"
Pike = "Pike: 5gp"
Rapier = "Rapier: 25gp"
Scimitar = "Scimitar: 25gp"
Short_Sword = "Short Sword: 10gp"
Trident = "Trident: 5gp"
War_Pick = "War Pick: 5gp"
Warhammer = "Warhammer: 15gp"
Whip = "Whip: 2gp"

# Martial Ranged Weapons
Blowgun = "Blowgun: 10gp"
Hand_Crossbow = "Hand Crossbow: 75gp"
Heavy_Crossbow = "Heavy Crossbow: 50gp"
Longbow = "Longbow: 50gp"
Net = "Net: 1gp"


# Amount of Store Item in Inventory
weapons_inventory = random.randint(0, 3)

# if store_item >= 0:
#     print("That item is out of stock, sorry for the inconvience.")

# Items in Zanathars Goods by category
simple_melee = [Dagger, Handaxe, Spear, Sickle]
simple_ranged = [Light_Crossbow, Shortbow]
martial_melee = [Glaive, Greataxe, Pike, Rapier,]
martial_ranged = [Heavy_Crossbow, Longbow, Hand_Crossbow]

Weapons = [simple_melee, simple_ranged, martial_melee, martial_ranged]
Armor = []
Drugs = ("Sunkiss, Pebbles, Moonlight")
Supplies = ("Explorer pack, Dungeon Pack, Monster Hunter pack, Chests, Barrels, Housewares, ect.")
Tools = ("Thieves, Forgery, Herbalism, Leatherworker, Smithy, Brewers, Carpenters, Disguise, ect.")

store_items = [Weapons, Armor, Drugs, Supplies, Tools]

starting_statement = print(f'Hello!\nWelcome to Zanathar\'s Goods, what are you looking for?')

players_choice = input(f'"Weapons" "Armor" "Drugs" "Supplies" "Tools"\n').lower()


if players_choice == "weapons":
    print(f'"Got quite a variety. Take a look." {random.choice(Weapons)}')
elif players_choice == "armor":
    input(f'{Armor}')
elif players_choice == "drugs":
    input(f'{Drugs}')
elif players_choice == "supplies":
    input(f'{Supplies}')
elif players_choice == "tools":
    input(f'{Tools}')
else:
    print("You're stupid, please leave.")


# Q = 50
# while Q < 100:
#     print("")
#     Q += 0
# else:
#     print("Not in my Store.")

