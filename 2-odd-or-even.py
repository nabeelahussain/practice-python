# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# Exercise 2

# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?


def isItOddOrEven():
    stringNumber = input("Give me a number: ")
    number = int(stringNumber)
    if number % 2 == 0:
        print("You're even!")
    else:
        print("You're odd!")

isItOddOrEven()
