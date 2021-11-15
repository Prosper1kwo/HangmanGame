'''
These functions store data to be used in the game.
'''
from random import randint
from hangman_words import animal_words, fruit_words, country_words

def guess_store(answer, past_guess):
    '''
    Stores the letters you have guessed into a list
    to be displayed
    '''
    if answer in past_guess:
        pass
    elif answer != "" or answer != " ":
        past_guess.append(answer)
    else:
        print("Invalid Input")
    
    return past_guess

def rand_word(hint):
    '''
    This function returns a random word from a list of words based on the single hint the user picked
    '''
    sol = ""
    if hint == "f":
        sol = fruit_words[randint(0, len(fruit_words) - 1)]
    elif hint == 'a':
        sol = animal_words[randint(0, len(animal_words) - 1)]
    elif hint == "c":
        sol = country_words[randint(0, len(country_words) - 1)]
        pass
    return sol