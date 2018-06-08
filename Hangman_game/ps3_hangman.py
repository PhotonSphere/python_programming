# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random, string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.\n\n")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    right_count = 0
    for i in secretWord:
        if i in lettersGuessed:
            right_count += 1
    if len(secretWord) == right_count:
        return True
    return False     


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = ''
    for i in secretWord:
        if i in lettersGuessed:
            guessedWord += i
        else:
            guessedWord += '_ '
    return guessedWord
            

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    for i in lettersGuessed:
        if i not in removedLetters:
            avaiLetters.remove(i)
            removedLetters.append(i)
    return ''.join(avaiLetters)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # My code written in IDE...
    '''
    life = 8
    print('Hello, let\'s start the hangman game. \nThe secret word contains missing letters: \n')
    print(getGuessedWord(secretWord, lettersGuessed))
    print('\n\n')
    while life:
        guess = input('Make a guess for the letter in the secret word: ')
        
        if guess not in avaiLetters:
            guess = input('You have already guessed the letter. Guess again!')
            
        lettersGuessed.append(guess)
        
        if guess in secretWord:
            print('You guessed the letter correctly.\n\n')
        else:
            print('Your guess in wrong')
            life -= 1

        if isWordGuessed(secretWord, lettersGuessed):
            print('Congrats you have successful guessed the word.')
            break
        elif life==0:
            print('\nThe secret word was {}'.format(secretWord))
            print('\nYou have exhausted your chances. Better luck next time.')
            break
        
        print(getGuessedWord(secretWord, lettersGuessed))
        print('\n')
        print('You have following letters to guess from: {}'.format(getAvailableLetters(lettersGuessed)))
     '''
    # Code correct to clear the test in Edx
    life = 8
    print('Welcome to the game Hangman! \nI am thinking of a word that is {} letters long \n'.format(len(secretWord)))
    #print(getGuessedWord(secretWord, lettersGuessed))
    print('-----------')
    while life:
        
        print('You have {} guesses left'.format(life))
        print('Available Letters: {}'.format(getAvailableLetters(lettersGuessed)))
        guess = input('Please guess a letter: ')
    
        lettersGuessed.append(guess)  
       
        if lettersGuessed.count(guess) > 1:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        elif guess in secretWord:
            print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
        else:
            print('Oops! That letter is not in my word: {}'.format('_'))
            life -= 1
        print('-----------')
        
        
        
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        elif life==0:
            print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
            break


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

if __name__ == '__main__':
    wordlist = loadWords()
    secretWord = chooseWord(wordlist).lower()
    avaiLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
        'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 'z']
    lettersGuessed = []
    removedLetters = []
    hangman(secretWord)
