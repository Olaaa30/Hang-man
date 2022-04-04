from words import words
import random
import string
def getvalidword(words):
    # pick a random word in the list of words
    word = random.choice(words)
    #pick another word if '-' or ' ' is in the word
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word
def hangman():
    # generate a word using the getvalidword function
    word = getvalidword(words)
    # create a set of the unique letters in the word
    word_letters = set(word)
    # create a set of the letters in the english alphabet
    alphabets = set(string.ascii_uppercase)
    # create an empty set that will hold the letters that the player has used
    used_letters = set()
    # this loop keeps running till all the letters in the word have been guessed
    while len(word_letters) > 0:
        # print the letters of the alphabets that the user has used. 
        print('You have used ', ' '.join(used_letters))
        # create a list that keeps track of the letters of the word that the user has guessed 
        # correctly and pass a '-' for the letters remaining
        word_list = [letter if letter in used_letters else '-' for letter in word ]
        # print the word list
        print('Current word: ', ' '.join(word_list))
        # get the user to guess a letter
        userletter = input('Guess a letter: ').upper()
        # check if the letter hasn't been used before
        if userletter in alphabets - used_letters:
            used_letters.add(userletter)
            # if the letter hasn't been used before, and it's in the word list, remove it
            # from the list of words
            if userletter in word_letters:
                word_letters.remove(userletter)
        # print a message if the letter has already been used
        elif userletter in used_letters:
            print('You have already used this character. Try again')
        # print a message if the user entered an invalid character
        else:
            print('Invalid character. Please try again.')
hangman()

