# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

# Exercise 30

# In this exercise, the task is to write a function
# that picks a random word from a list of words
# from the SOWPODS dictionary. Download this file
# and save it in the same directory as your Python code.
# This file is Peter Norvig’s compilation of the dictionary
# of words used in professional Scrabble tournaments.
# Each line in the file contains a single word.

# Hint: use the Python random library for picking a random word.
import random

def getWords():
    words = []
    file = open("sowpods.txt", "r")
    for line in file:
        words.append(line)
    return words

def getRandomWord():
    mylist = getWords()
    return random.choice(mylist)

print(getRandomWord())
