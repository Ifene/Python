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



#Light Armor
Padded = "Padded: 5gp"
Leather = "Leather: 10gp"
Studded_Leather = "Studded Leather: 45gp"

#Medium Armor
Hide = "Hide: 10gp"
Chain_Shirt = "Chain Shirt: 50gp"
Scale_Mail = "Scale Mail: 50gp"
Breastplate = "Breastplate: 400gp"
Half_Plate = "Half Plate: 750gp"

#Heavy Armor
Ring_Mail = "Ring Mail: 30gp"
Chain_Mail = "Chain Male: 75gp"
Splint = "Splint: 200gp"
Plate = "Plate: 1500gp"



#Tools
Alchemist_Supplies =""
Brewer_Supplies = ""
Calligrapher_Supplies = ""
Carpenter_Tools = ""
Cartographer_Tools = ""
Cobbler_Tools = ""
Cook_Utensils = ""
Glassblowers_Tools = ""
Jeweler_Tools = ""
Leatherworker_Tools = ""
Mason_Tools = ""
Painter_Supplies = ""
Potter_Supplies = ""
Smithing_Tools = ""
Tinkering_Tools = ""
Weavers_Tools = ""
Woodcarver_Tools = ""
Dice_Set = ""
Cards = ""
Bagpipes = ""
Drum = ""
Dulcimer = ""
Flute = ""
Lute = ""
Lyre = ""
Horn = ""
Pan_Flute = ""
Shawn = ""
Viol = ""
Navigator_Tools = ""
Thieves_Tools = ""


Martial_Ranged_Weapons = [Blowgun, Hand_Crossbow, Heavy_Crossbow, Longbow, Net]
Simple_Melee_Weapons = [Club, Dagger, Great_Club, Handaxe, Javelin, Light_Hammer, Mace, Quater_Staff, Sickle, Spear]
Simple_Ranged_Weapons = [Light_Crossbow, Dart, Shortbow, Sling]
Martial_Melee_Weapons = [Battle_Axe, Flail, Glaive, Greataxe, Great_Sword, Halberd, Lance, Long_Sword, Maul, Morning_Star, Pike, Rapier, Scimitar, Short_Sword, Trident, War_Pick, Warhammer, Whip]

Light_Armor = [Padded, Leather, Studded_Leather]
Medium_Armor = [Hide, Chain_Shirt, Scale_Mail, Breastplate, Half_Plate]
Heavy_Armor = [Ring_Mail, Chain_Mail, Splint, Plate]

tools = [Alchemist_Supplies, Brewer_Supplies, Calligrapher_Supplies, Carpenter_Tools, Cartographer_Tools, Cobbler_Tools, 
Cook_Utensils, Glassblowers_Tools, Jeweler_Tools, Leatherworker_Tools, Mason_Tools, Painter_Supplies, Potter_Supplies, Smithing_Tools, 
Tinkering_Tools, Weavers_Tools, Woodcarver_Tools, Dice_Set, Cards, Bagpipes, Drum, Dulcimer, Flute, Lute, Lyre, Horn, Pan_Flute, Shawn, 
Viol, Navigator_Tools, Thieves_Tools]


# Items in Zanathars Goods by category
Rsimple_melee = random.choice(Simple_Melee_Weapons)
Rsimple_ranged = random.choice(Simple_Ranged_Weapons)
Rmartial_melee = random.choice(Martial_Melee_Weapons)
Rmartial_ranged = random.choice(Martial_Ranged_Weapons)

Rlight_armor = random.choice(Light_Armor)
Rmedium_armor = random.choice(Medium_Armor)
Rheavy_armor = random.choice(Heavy_Armor)

Rtools = random.choice(tools)

Rdrugs = random.choice()

Weapons = [Rsimple_melee, Rsimple_ranged, Rmartial_melee, Rmartial_ranged]
Armor = [Rlight_armor, Rmedium_armor, Rheavy_armor]
Tools = [Rtools]
Drugs = []
Supplies = ("Explorer pack, Dungeon Pack, Monster Hunter pack, Chests, Barrels, Housewares, ect.")


store_items = [Weapons, Armor, Tools, Drugs, Supplies]

# Amount of Store Item in Inventory
weapons_inventory = random.randint(0, 3)

# if store_item >= 0:
#     print("That item is out of stock, sorry for the inconvience.")

starting_statement = print(f'Hello!\nWelcome to Zanathar\'s Goods, what are you looking for?')

players_choice = input(f'Weapons, Armor, Drugs, Supplies, or Tools?\n').lower()


if players_choice == "weapons":
    print(f'"Got quite a variety in stock. Take a look." {Weapons}')
elif players_choice == "armor":
    input(f'{Armor}')
elif players_choice == "drugs":
    input(f'{Drugs}')
elif players_choice == "supplies":
    input(f'{Supplies}')
elif players_choice == "tools":
    input(f'{Tools}')
else:
    print("You've disrupted my work, please leave.")



