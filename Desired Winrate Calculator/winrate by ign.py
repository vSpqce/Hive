"""
This is an alternate to winrate.py which uses your ign and gamemode instead of numbers
Sorry it's formatted terribly but I don't want to fix it right now
If you run into any issues with this, please let me know. You do need Python 3 to run this
Not made to be performant
"""

import os
from decimal import Decimal
import math
import requests

os.system("cls")  # clears your terminal (on Windows)


def calculate_winrate():
    ign = None  # username
    gamemode = None  # gamemode
    w = None    # games won
    g = None    # games played
    r = None    # current winrate
    p = None    # desired winrate
    n = None    # wins needed to get desired winrate
    gamemodes = [ 
        "wars",
        "dr",
        "hide",
        "sg",
        "murder",
        "sky",
        "ctf",
        "drop",
        "ground",
        "build",
        "party",
        "main",
        "bridge",
        "grav",
        "bed",
    ]  # every possible gamemode

    # Please try not to break my program. I was too lazy to do proper data validation.
    ign = input("What username would you like to calculate the winrate for? ")
    printinfo(ign)

    print("Available gamemodes: [wars, dr, hide, sg, murder, sky, ctf, drop, ground, build, party, all, main, bridge, grav, bed]")
    gamemode = input("Which gamemode? ")
    
    while (gamemode not in gamemodes):
        printinfo(ign)
        print("Available gamemodes: [wars, dr, hide, sg, murder, sky, ctf, drop, ground, build, party, all, main, bridge, grav, bed]")
        gamemode = input("Invalid game. Please enter a valid mode: ")
    
    printinfo(ign, gamemode)
    p = abs(Decimal(input("What is your desired winrate (please enter a percentage without the sign)? ")) / 100)
    printinfo(ign, gamemode, p)

    stats = requests.get(f"https://api.playhive.com/v0/game/all/{gamemode}/{ign}").json()

    w = stats["victories"]
    g = stats["played"]

    if p == 0 or p == 1:
        print("no")
        return

    r = Decimal(w / g)  # dividing wins by games to get current winrate
    if r >= p:
        print("You current wintrate is equal to or higher than your desired winrate")
        return

    n = (p * g - w) / (1 - p)  # if you want to know how this works, dm me
    print(f"You need to win {math.ceil(n)} games to reach a {p*100}% winrate")


def printinfo(ign, gamemode=None, p=None):
    os.system("cls")
    print(f"Username: {ign}")
    if gamemode is not None:
        print(f"Gamemode: {gamemode}")
    if p is not None:
        print(f"Desired winrate: {p*100}%")

calculate_winrate()