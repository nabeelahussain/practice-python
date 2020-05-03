# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

# Exercise 8

# Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

# Remember the rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import getpass
enter = getpass.getpass

playing = True

def getWeapon(player):
    weapon = enter( player + "Choose rock, paper or scissors: ")
    while weapon not in ["rock", "paper", "scissors"]:
        weapon = enter( player + "Choose rock, paper or scissors: ")
    return weapon

while playing:

    weapon = getWeapon("player 1 ")
    weapon2 = getWeapon("player 2 ")


    if (weapon == "rock" and weapon2 == "paper") or (weapon == "paper" and weapon2 == "rock"):
        print("The winner is paper!")
        if weapon == "paper":
            print("Well done Player 1!")
        else:
            print("Well done Player 2!")
    elif (weapon == "scissors" and weapon2 == "rock") or (weapon == "rock" and weapon2 == "scissors"):
        print("The winner is rock!")
        if weapon == "rock":
            print("Well done Player 1!")
        else:
            print("Well done Player 2!")
    elif (weapon == "paper" and weapon2 == "scissors") or (weapon == "scissors" and weapon2 == "paper"):
        print("The winner is scissors!")
        if weapon == "scissors":
            print("Well done Player 1!")
        else:
            print("Well done Player 2!")
    else:
        print("It's a draw!")

    Continue = input("Do you want to continue playing? Type Y/n: ")
    if Continue == "n":
        playing = False 