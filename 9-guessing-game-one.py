# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

# Exercise 9 

# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, 
# or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

def getUserInput():
    userInput = input("Guess a number between 1 and 9: ")
    return userInput

playing = True
numberOfGuesses = 0
numberOfCorrectGuesses = 0

print("Welcome to the guessing game!")
print("Type 'exit' at any time to close the game and see your score!")

while playing:     
    randomNumber = random.randint(1, 9) 
    while playing:
        guessString = getUserInput()
        if guessString == "exit":
            playing = False
            break
        guess = int(guessString)
        numberOfGuesses = numberOfGuesses + 1
        if (guess == randomNumber):
            numberOfCorrectGuesses = numberOfCorrectGuesses + 1
            print("You got it spot on!")
            break       
        elif (guess < randomNumber):
            print("You guessed too low, oh no..")
        else:
            print("You guessed too high, oh no..")
    if guessString == "exit":
        playing = False
        print("You've had {} guesses and {} correct guesses".format(numberOfGuesses, numberOfCorrectGuesses))
        break
    else:
        playing = True
