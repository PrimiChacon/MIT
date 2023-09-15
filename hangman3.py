# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

#is_word_guessed('applr', ['a', 'p', 'l', 'r'])

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = []
    for letters in secret_word:
        if letters in letters_guessed:
            guessed_word.append(letters)
        else:
            guessed_word.append("_")
    return guessed_word

#get_guessed_word('secret_word', ['s'])

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = []
    for letters in string.ascii_lowercase:
        if letters not in letters_guessed:
            available_letters.append(letters)
    return available_letters
    
#get_available_letters([])



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a world that is " + str(len(secret_word)) + " letters long.")
    print ("-----------")
    print ("You have 3 warnings left.")
    print ("You have 6 guesses left.")
    available_letters = get_available_letters([])
    print('Available letters: ' + ''.join(available_letters))
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaning = 3

    while is_word_guessed(secret_word,letters_guessed) == False:
        letter_guessed = (input("Please guess a letter : "))

        if guesses_remaining <= 0:
            print ("Sorry, you ran out of guesses. The word was " + secret_word)
            break
        if letter_guessed not in string.ascii_lowercase:
            if warnings_remaning == 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: " + str(guesses_remaining) + " guesses")
            if warnings_remaning > 0:
                warnings_remaning -= 1
                print("Oops! That is not a valid letter. You have " + str(warnings_remaning) + " warnings:")

        if letter_guessed in string.ascii_lowercase:
            available_letters = get_available_letters(letters_guessed)

            if letter_guessed not in available_letters:
                if warnings_remaning == 0:
                    guesses_remaining -= 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + str(guesses_remaining) + " guesses")
                if warnings_remaning > 0:
                    warnings_remaning -= 1
                    print("Oops! You've already guessed that letter. You now have " + str(warnings_remaning) + " warnings:")

            if letter_guessed in available_letters:
                get_guessed_word(secret_word, letters_guessed)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if letter_guessed not in letters_guessed:
                    print("Good guess:")
                    letters_guessed.append(letter_guessed)
#                    print(letters_guessed)


                vowels_list = ["a", "e", "i", "o", "u"]



                guessed_word = get_guessed_word(secret_word, letters_guessed)
#                print(guessed_word)

                if letter_guessed not in guessed_word:
                    print("Oops! That letter is not in my word:")
                    if letter_guessed in vowels_list:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1








        available_letters = get_available_letters(letters_guessed)

        guessed_word = get_guessed_word(secret_word, letters_guessed)

        print(''.join(guessed_word))

#        if  letter_guessed in guessed_word:
#            break



        if guesses_remaining <= 0:
            print ("Sorry, you ran out of guesses. The word was " + secret_word)
            break
        print ("You have " + str(guesses_remaining) + " guesses left.")







        get_available_letters(letters_guessed)
        print('Available letters: ' + ''.join(available_letters))
    else:
        print ("Congratulations, you won!")
        secret_word_unique = []
        for character in secret_word:
            if character not in secret_word_unique:
                secret_word_unique.append(character)
                number_unique = len (secret_word_unique)
        print ("Your total score for this game is: " + str(guesses_remaining * number_unique))






# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    for x in range (len(my_word)):
        letter_my_word = my_word[x:x+1]
        letter_other_word = other_word[x:x+1]
        if letter_my_word == "_":
            continue
        if letter_my_word != letter_other_word:
            return False
        if letter_my_word == letter_other_word:
            continue
    return True

print(match_with_gaps("m__o","mayo"))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched_words=[]
    for word in wordlist:
        if len(word) != len(my_word):
            continue
        if len(word) == len(my_word):
            if match_with_gaps(my_word,word) == True:
                matched_words.append(word)
    if len(matched_words) == 0:
        return (print ("No matches found"))

    return print(matched_words)

show_possible_matches("app__")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a world that is " + str(len(secret_word)) + " letters long.")
    print("-----------")
    print("You have 3 warnings left.")
    print("You have 6 guesses left.")
    available_letters = get_available_letters([])
    print('Available letters: ' + ''.join(available_letters))
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaning = 3

    while is_word_guessed(secret_word, letters_guessed) == False:
        letter_guessed = (input("Please guess a letter : "))

        if guesses_remaining <= 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word)
            break
        if letter_guessed == "*":
            print ("Possible word matches are: ")
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            print(''.join(guessed_word))
            show_possible_matches(''.join(guessed_word))
        if letter_guessed not in string.ascii_lowercase and letter_guessed !="*":
            if warnings_remaning == 0:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess: " + str(guesses_remaining) + " guesses")
            if warnings_remaning > 0:
                warnings_remaning -= 1
                print("Oops! That is not a valid letter. You have " + str(warnings_remaning) + " warnings:")

        if letter_guessed in string.ascii_lowercase:
            available_letters = get_available_letters(letters_guessed)

            if letter_guessed not in available_letters and letter_guessed !="*":
                if warnings_remaning == 0:
                    guesses_remaining -= 1
                    print(
                        "Oops! You've already guessed that letter. You have no warnings left so you lose one guess: " + str(
                            guesses_remaining) + " guesses")
                if warnings_remaning > 0:
                    warnings_remaning -= 1
                    print("Oops! You've already guessed that letter. You now have " + str(
                        warnings_remaning) + " warnings:")

            if letter_guessed in available_letters:
                get_guessed_word(secret_word, letters_guessed)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                if letter_guessed not in letters_guessed:
                    print("Good guess:")
                    letters_guessed.append(letter_guessed)
                #                    print(letters_guessed)

                vowels_list = ["a", "e", "i", "o", "u"]

                guessed_word = get_guessed_word(secret_word, letters_guessed)
                #                print(guessed_word)

                if letter_guessed not in guessed_word:
                    print("Oops! That letter is not in my word:")
                    if letter_guessed in vowels_list:
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1

        available_letters = get_available_letters(letters_guessed)

        guessed_word = get_guessed_word(secret_word, letters_guessed)

        print(''.join(guessed_word))

        #        if  letter_guessed in guessed_word:
        #            break

        if guesses_remaining <= 0:
            print("Sorry, you ran out of guesses. The word was " + secret_word)
            break
        print("You have " + str(guesses_remaining) + " guesses left.")

        get_available_letters(letters_guessed)
        print('Available letters: ' + ''.join(available_letters))
    else:
        print("Congratulations, you won!")
        secret_word_unique = []
        for character in secret_word:
            if character not in secret_word_unique:
                secret_word_unique.append(character)
                number_unique = len(secret_word_unique)
        print("Your total score for this game is: " + str(guesses_remaining * number_unique))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.



if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
