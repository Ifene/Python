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



Leap_Year()





