# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

# Exercise 12

# Write a program that takes a list of numbers
# (for example, a = [5, 10, 15, 20, 25]) and makes a 
# new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.


def getFirstAndLastNumber(items):
    return [items[0], items[len(items) -1]]

print(getFirstAndLastNumber([1, 2, 3, 4, 5]))
print(getFirstAndLastNumber([1, 2, 3, 4]))
print(getFirstAndLastNumber([1, 2, 3, 4, 5, 6]))
