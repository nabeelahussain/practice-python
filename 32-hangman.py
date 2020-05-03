# https://www.practicepython.org/exercise/2017/01/10/32-hangman.html

# Exercise 32

# In this exercise, we will finish building Hangman.
# In the game of Hangman, the player only has 6 incorrect
# guesses (head, body, 2 legs, and 2 arms) before they lose the game.

# In Part 1, we loaded a random word list and picked a word from it.
# In Part 2, we wrote the logic for guessing the letter and displaying
# that information to the user. In this exercise, we have to put it all
# together and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting
# point. Now add the following features:

# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a
# letter they already guessed, don’t penalize them - let them guess again.


# Optional additions:

# When the player wins or loses, let them start a new game.

# Rather than telling the user "You have 4 incorrect guesses left",
# display some picture art for the Hangman. This is
# challenging - do the other parts of the exercise first!

# Your solution will be a lot cleaner if you make use of functions to help you!
import random

def displayHangman(numberOfIncorrectGuesses):
    print("You have {} incorrect guesses left".format(6 - numberOfIncorrectGuesses))
    if numberOfIncorrectGuesses == 1:
        print('''
        +---+
        |   |
        O   |
            |
            |
            |
        ''')
    if numberOfIncorrectGuesses == 2:
        print('''
        +---+
        |   |
        O   |
        |   |
            |
            |
        ''')
    if numberOfIncorrectGuesses == 3:
        print('''
         +---+
         |   |
         O   |
        /|   |
             |
             |
        ''')
    if numberOfIncorrectGuesses == 4:
        print('''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        ''')
    if numberOfIncorrectGuesses == 5:
        print('''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        ''')
    if numberOfIncorrectGuesses == 6:
        print('''
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        ''')


def getWords():
    words = []
    file = open("sowpods.txt", "r")
    for line in file:
        words.append(line)
    return words

def getRandomWord():
    mylist = getWords()
    return random.choice(mylist).strip()

def getLetter():
    letter = input("Guess a letter: ")
    return letter.upper()

def play(word):
    fullyGuessed = False
    numberOfIncorrectGuesses = 0
    maxNumberOfIncorrectGuesses = 6
    guessedLetters = []
    correctlyGuessedLetters = []
    while fullyGuessed != True and numberOfIncorrectGuesses < maxNumberOfIncorrectGuesses:
        guessedLetter = getLetter()
        if guessedLetter in guessedLetters:
            print("You've already guessed that letter!")
            continue
        guessedLetters.append(guessedLetter)
        if guessedLetter in word:
            correctlyGuessedLetters.append(guessedLetter)
            print(getWordProgress(correctlyGuessedLetters, word))
            fullyGuessed = getFullyGuessed(correctlyGuessedLetters, word)
        else:
            numberOfIncorrectGuesses = numberOfIncorrectGuesses + 1
            print("Wrong!!")
            displayHangman(numberOfIncorrectGuesses)
            if numberOfIncorrectGuesses >= maxNumberOfIncorrectGuesses:
                print("Game Over! x _ x")
    print("Thanks for playing!")

def getWordProgress(guessedLetters, word):
    result = ""
    for letter in word:
        if letter in guessedLetters:
            result = result + letter + " "
        else:
            result = result + "_ "
    return result.strip()

def getFullyGuessed(guessedLetters, word):
    wordProgress = getWordProgress(guessedLetters, word)
    if "_" in wordProgress:
        return False
    else:
        return True

stillPlaying = ""

while stillPlaying.upper() != "N":
    play(getRandomWord())
    stillPlaying = input("Do you want to play again? Y/n: ")

print("Have a great day!")
