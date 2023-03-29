import random
import sys
import time
import os


Game = True
Dmg = True

os.system('cls')
while Game == True:
    #D20 Dice
    D20 = random.randint(1, 20)
    #D100
    D100 = random.randint(1, 100)

    Roll1 = input("Do you want to roll a 'd20', 'd100', or 'Damage'? (To end type 'end') \n").lower()
    os.system('cls')

    if Roll1 == 'd20':
        #The user gets 2 d20 rolls if they have advantage/disadvantage
        Advantage = input("Do you have Advantage/Disadvantage? 'yes' or 'no'? \n").lower()
        if Advantage == 'yes':
            #Added time for suspense
            os.system('cls')
            time.sleep(2.5)
            print(f'First Roll: {D20}')
            D20 = random.randint(1, 20)
            print(f'Second Roll: {D20}')
            time.sleep(1.5)
            Another1 = input("Would you like to roll again? 'yes' or 'no' \n").lower()
            if Another1 == 'yes':
                os.system('cls')
                ""
            else:
                Game = False
        #No advantage means single d20 roll
        elif Advantage == 'no':
            os.system('cls')
            time.sleep(2.5)
            print(f'Roll: {D20}')
            time.sleep(1.5)
            Another1 = input("Would you like to roll again? 'yes' or 'no' \n").lower()
            if Another1 == 'yes':
                os.system('cls')
                ""
            else:
                Game = False
        else:
            print("Please answer yes or no")
            time.sleep(1.5)

    elif Roll1 == 'd100':
        os.system('cls')
        time.sleep(2.5)
        print(f'Roll: {D100}')
        time.sleep(1.5)
        Another2 = input("Would you like to roll again? 'yes' or 'no' \n").lower()
        if Another2 == 'yes':
            os.system('cls')
            ""
        else:
            Game = False

    elif Roll1 == 'damage':
        Dmg = True
        while Dmg == True:
            def Dmg_Dice(Dice):
                Individual_Rolls = []
                if Dice == "d4":
                    D4_Amount = int(input("How many D4's? \n"))
                    if 1 <= D4_Amount <= 100:
                        # x serves for how many times the statement is executed
                        for x in range(D4_Amount):
                            Roll = random.randint(1,4)
                            Individual_Rolls.append(Roll)
                        print("Individual rolls:", Individual_Rolls)
                        total_damage = sum(Individual_Rolls)
                        print("Total damage:", total_damage)
                        time.sleep(2)
                    else:
                        os.system('cls')
                        print("That's way to many, try a smaller number.")
                        time.sleep(2.5)

                elif Dice == 'd6':
                    D6_Amount = int(input("How many D6's? \n"))
                    if 1 <= D6_Amount <= 100:
                        # x serves for how many times the statement is executed
                        for x in range(D6_Amount):
                            Roll = random.randint(1,6)
                            Individual_Rolls.append(Roll)
                        print("Individual rolls:", Individual_Rolls)
                        total_damage = sum(Individual_Rolls)
                        print("Total damage:", total_damage)
                        time.sleep(2)

                elif Dice == 'd8':
                    D8_Amount = int(input("How many D8's? \n"))
                    if 1 <= D8_Amount <= 100:
                        # x serves for how many times the statement is executed
                        for x in range(D8_Amount):
                            Roll = random.randint(1,8)
                            Individual_Rolls.append(Roll)
                        print("Individual rolls:", Individual_Rolls)
                        total_damage = sum(Individual_Rolls)
                        print("Total damage:", total_damage)
                        time.sleep(2)

                elif Dice == 'd10':
                    D10_Amount = int(input("How many D10's? \n"))
                    if 1 <= D10_Amount <= 100:
                        # x serves for how many times the statement is executed
                        for x in range(D10_Amount):
                            Roll = random.randint(1,10)
                            Individual_Rolls.append(Roll)
                        print("Individual rolls:", Individual_Rolls)
                        total_damage = sum(Individual_Rolls)
                        print("Total damage:", total_damage)
                        time.sleep(2)

                elif Dice == 'd12':
                    D12_Amount = int(input("How many D12's? \n"))
                    if 1 <= D12_Amount <= 100:
                        # x serves for how many times the statement is executed
                        for x in range(D12_Amount):
                            Roll = random.randint(1,12)
                            Individual_Rolls.append(Roll)
                        print("Individual rolls:", Individual_Rolls)
                        total_damage = sum(Individual_Rolls)
                        print("Total damage:", total_damage)
                        time.sleep(2)

                else:
                    os.system('cls')
                    print("Please enter a valid dice number 'd4' 'd6' 'd8' 'd10' 'd12'")
                    time.sleep(3)
                    
            Dice_Amount = input("What sided dice are you using? 'd4' 'd6' 'd8' 'd10' 'd12' \n")
            os.system('cls')      
            Dmg_Dice(Dice=Dice_Amount)
            Another3 = input("Would you like to roll again? 'yes' or 'no' \n").lower()
            os.system('cls')
            if Another3 == 'yes':
                os.system('cls')
                Dmg = True
            else:
                Dmg = False
    
    elif Roll1 == 'end': 
        Game = False
    else: 
        os.system('cls')
        print("That's not a valid answer. Please enter one of the options.")
else:
    print("End of Dice Roller")
    
