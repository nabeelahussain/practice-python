# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Exercise 1

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them
# the year that they will turn 100 years old.

def printYearITurn100():
    name = input("Give me your name: ")
    ageString = input("Give me your age: ")
    print("Your name is " + name)
    print("Your age is " + ageString)
    age = int(ageString)
    currentyear = 2019
    numberofyears = 100 - age
    year = currentyear + numberofyears
    yearString = str(year)
    print("You will be 100 years old " + name + ", in " + yearString + ".") 

printYearITurn100()