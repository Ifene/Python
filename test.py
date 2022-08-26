# practice with Python

# practice with numbers


def numtest1():
    print(1+1)
    print(2*2)
    print(7/4)
    print(50%5)
    print(23%2)
    print(2**3)
    print(2+10*10+3)
    print((2+10)*(10+3))


# Practicing store ideas

def store():
    long_sword = 50

    hand_axe = 10

    total_purchase = long_sword + hand_axe

    value_long_sword = f'{long_sword} Gold'

    #value_long_sword = str(long_sword)+' Gold'

    print(total_purchase)

    print(value_long_sword)


# Intro to Input

def Input():
    input("What's your name?")

    print("Hello " + input("What is your name?"))


# Learning the len command and variables

def Len():
    print(len(input("What is your name? ")))
    # Other way to do this
    nam = input("What's your name? ")
    print(len(nam))


def vart():
    a = input("a: ")
    b = input("b: ")

    z = a
    v = b
    a = v
    b = z

    a = print("a: " + a)
    b = print("b: " + b)


# Tip Calculator

def Calculator() :
    print("Welcome to the tip calculator!")
    bill = input("What was the total bill? ")
    tip = input("How much tip would you like to give? 10, 12, or 15? ")
    people = input("How many people to split the bill?")

    tbill = float(bill) / float(people)
    ttip = float(tip) / 100 + 1

    tot = print(f'{round(tbill * ttip, 2): .2f}')

# Modular learning. % sign is used here instead of division
def Modular():
    number = int(input("Which number do you want to check? "))
    if number % 2 == 0:
     Even_Total = print("This is an even number.")
    else:
     Odd_Total = print("This is an odd number.")


# BMI Calculator
def BCalc():
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))

    BMI = int(weight / (height**2))

    if BMI <= 18.5:
        print(f"Your BMI is {BMI}, You are slightly underweight.")
    elif BMI <= 25:
        print(f"Your BMI is {BMI}, You have a normal weight.")
    elif BMI <= 30:
        print(f"Your BMI is {BMI}, You are slightly overweight.")
    elif BMI <= 35:
        print(f"Your BMI is {BMI}, You are obese.")
    else: print(f"Your BMI is {BMI}, You are clinically obese")


# Leap Year Calculator
def Leap_Year():
    year = int(input("Which year do you want to check? "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('leap')
            else:
                print('not leap')
        else:
            print('leap year')
    else:
        print('not leap')


def Pizza_Quiz():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size pizza do you want? S, M, or L ")
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    extra_cheese = input("Do you want extra cheese? Y or N ")


    bill = 0

    if size == "S":
        bill = 15
        if add_pepperoni == "Y":
         bill += 2
    if size == "M":
        bill = 20
        if add_pepperoni == "Y":
         bill += 3
    if size == "L":
        bill = 25
        if add_pepperoni == "Y":
         bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}.")

    #Another way to do this problem

    # if size == "S":
    #     bill += 15
    # elif size == "M":
    #     bill += 20
    # elif size == "L":
    #     bill += 25

    # if add_pepperoni == "Y":
    #     if size == "S":
    #      bill += 2
    #     else:
    #      bill += 3
    
    # if extra_cheese == "Y":
    #     bill += 1


def love_calculator():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")

    combined_string = name1 + name2
    lower_combined_string = combined_string.lower()
    t = lower_combined_string.count("t")
    r = lower_combined_string.count("r")
    u = lower_combined_string.count("u")
    e = lower_combined_string.count("e")

    true = t + r + u + e

    l = lower_combined_string.count("l")
    o = lower_combined_string.count("o")
    v = lower_combined_string.count("v")
    e = lower_combined_string.count("e")

    love = l + o + v + e

    Total = int(str(true) + str(love))

    if Total < 10 or Total > 90:
        print(f"Your score is {Total}, you go together like coke and mentos")
    elif Total >= 40 and Total <=50:
        print(f"Your score is {Total}, you are alright together.")
    else:
        print(f"Your score is {Total}")


def forest_game():
    print('''
    *******************************************************************************
    |   [  | v':    :              |        |_,;c    
    | ]    |/; |,   |              |   [  ( __,/     
    |    ,-'/  ;\ ,<  _',\.-._,;   |      ] |    n   
    |   -' /   _;';    '=_'-' ,)  ,\        |   ,;   
    |  ]  / \,'__/--,_,-- 'mm'J -"_  ]       '-,+_   
    |    /    / "''-.,;"---''--'"" \      ]   __  "-'
    ;' [      / :    : _c           /         /  ",_,'
    |      [ | v|  , '/             c c    \ |        
    \    ]   |  \ /| :             |;|]   . \|        
    [      /"--'/  |            c@  )    )/|        
    \     ]    ,-"'<':               (    /^ |        
    | ]       / :   '|             |  )      |        
    | |   /  |  |    ;,-;,         |,)(     ]|        
    |  \^ |  |  :  |\ ,'           \ /   [   |        
    |  ?  /  \_ |  /|:              | , \    |        
    |  | ('.   "--' |:,    ;        :\ /    [|        
    |  ;\~)   _     \_) ',_|   ,    | ),  \_ :        
    |   |/ [ /""-,_   '-'(    /.'   | \   |  '-_      
    | [      |  |  "---,__"'=';=,_  |  \ /|\    '"-,__
    |     ]  |  :    |    ""'^.\    |   | |    \      
    |  [    ]|  |    :              | ]  \ \   /  _AsH
    *******************************************************************************
    ''')
    print("Welcome to Angellusare, the Great Jungle of Paston.\nYou awake in a jungle on a cobble path heading north.")
    print("Your mission is to survive and escape the jungle.") 

    Begin = input('Do you "follow" the cobble path or "walk" into the jungle?\n').lower()
    if Begin == "follow":
        dir = input('As you travel the path ahead of you it splits into two ways. Do you go "left" or "right" \n') .lower()
        if dir == "left":
            chest = input('Continuing down the path on your right side you come across 3 stone podiums with a chest on each one.\nEach chest is colored; which do you choose "red", "yellow", "blue", or "none" and keep walking.\n').lower()
            if chest == "red":
                print("You have chosen a fate worse than death. You are eaten alive by fire ants.\n")
            elif chest == "yellow":
                print("A beautiful flower that smells good enough to eat. You die to poison.\n")
            elif chest == "blue":
                print("You find many rations and a map out of the jungle. You continue down the path taking every twist and turn correctly until you reach the edge of the jungle. Out in front of you is nothing but a mass desert. You survived Angellusare and now freedom is just beyond the horizon. You win!\n")
            else:
                print("Deciding not to gamble fate is wise but when it determines your survival you wish you would've chosen a chest. You go a ways down the path to a river. The path ends at it with no other path on the opposite side. You cross the river but on the other side of it as you get out are moss covered skeletons that stab you through the chest and leave your body to run down the river.\n")
        else:
            print("A directional path leads you into a cave. In that cave as you walk through it you feel a piercing pain in your chest. Then you feel your body fluids being drained.\nIn a small light you see a giant spider has grabbed you and sank its fangs into your heart. You die.\n")
    else:
        print("You wandered off the path into the unknown jungle of Paston. You will never find your way out nor be found. You died of starvation.\n")


def ran_function():
    import random

    Toss = random.randint(0,1)

    if Toss == 0:
        print("Heads")
    else:
        print("Tails")



def list_random():
    # Split string method
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇

    import random

    total_number = len(names)
    random_choice = random.ranint(0, total_number - 1)
    person_pays = names[random_choice]
    print(person_pays +"is going to buy the meal today.")


    # person_pay = random.choice(names)


def Nested_List_practice():
    # 🚨 Don't change the code below 👇
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    #Write your code below this row 

    horizontal = int(position[0])
    vertical = int(position[1])

    map[vertical - 1][horizontal - 1] = "X"

    #Write your code above this row 👆

    # 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")


def Rock_Paper_Scissors():
    rock = '''
        _______
    ---'   ____)
           (_____)
           (_____)
           (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
               ______)
              _______)
              _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    '''

    #Write your code below this line 👇

    import random

    game_images = [rock, paper, scissors]

    players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

    if players_choice >= 3 or players_choice < 0:
        print("You typed an invalid number, you lose!")
    else:
        print(game_images[players_choice])
    
        npc_random_choice = random.randint(0, 2)
        
        print(f"Computer chose:")
        print(game_images[npc_random_choice])
        
        if players_choice == 0 and npc_random_choice == 2:
            print("You win!")
        elif npc_random_choice == 0 and players_choice == 2:
            print("You lose!")
        elif npc_random_choice > players_choice:
            print("You lose!")
        elif players_choice > npc_random_choice:
            print("You win!")
        elif npc_random_choice == players_choice:
            print("It's a draw!")


def A_Loop():
    student_heights = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    # 🚨 Don't change the code above 👆


    #Write your code below this row 👇

    total_height = 0
    for height in student_heights:
        total_height += height

    A_height = round(int(total_height) / 7)

    print(A_height)














