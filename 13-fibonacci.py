# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

# Exercise 13

# Write a program that asks the user how many
# Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of
# numbers in the sequence to generate.

# (Hint: The Fibonnaci seqence is a sequence of numbers
# where the next number in the sequence is the sum of
# the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...)

def getNextElementInSequence(sequence):
    lastElement = sequence[len(sequence) - 1]
    secondLastElement = sequence[len(sequence) - 2]
    nextElement = lastElement + secondLastElement
    sequence.append(nextElement)
    return sequence

def getStartOfSequence():
    sequence = []
    sequence.append(1)
    sequence.append(1)
    return sequence

def getUserInput():
    number = input("Pick a number of Fibonnaci numbers to generate: ")
    return number

def generateFibonacciSequence():
    sequence = getStartOfSequence()
    numbersToGenerate = getUserInput()
    for number in range(numbersToGenerate - 2):
        sequence = getNextElementInSequence(sequence)
    if numbersToGenerate < 2:
        sequence.pop()
    if numbersToGenerate < 1:
        sequence.pop()
    print(sequence)

generateFibonacciSequence()