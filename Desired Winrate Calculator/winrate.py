"""
This is a simple program to calculate how many wins are needed for a desired winrate
If you run into any issues with this, please let me know. You do need Python 3 to run this
I made it is as simple as possible so you can use it without having any knowledge of Python
Not made to be performant
"""

import os
from decimal import Decimal
import math

os.system("cls")  # clears your terminal (on Windows)


def calculate_winrate():
    w = None  # games won
    g = None  # games played
    r = None  # current winrate
    p = None  # desired winrate
    n = None  # wins needed to get desired winrate

    # Please try not to break my program. I was too lazy to do proper data validation.
    w = abs(Decimal(input("How many games have you won? ")))
    g = abs(Decimal(input("How many total games have you played? ")))

    if (g == 0):
        print("Trying to break my program I see")

    p = abs(Decimal(input("What is your desired winrate (please enter a percentage without the sign)? "))/100)

    if (p == 0 or p == 1):
        print("no")
        return
    
    r = Decimal(w/g)  # dividing wins by games to get current winrate
    if (r >= p):
        print("You current wintrate is equal to or higher than your desired winrate")
        return
    
    n = (p*g-w)/(1-p)  # i just solved the formula here; if you want to know how it works, dm me
    print(f"You need to win {math.ceil(n)} games to reach a {p*100}% winrate")

calculate_winrate()