# practice with Python

# practice with numbers

from re import X
from typing import ValuesView


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







