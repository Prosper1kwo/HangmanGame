'''
This module defines functions that will be used throughout the hangman game
'''
from hangman_pics import hang_image
from hangman_words import animal_words, fruit_words, country_words
from random import randint


def hangman_draw(error_count):
    '''
  Returns an ASCII image of a hanged-man based on the player's error_count
  '''

    if error_count == 0:
        return hang_image[0]
    if error_count == 1:
        return hang_image[1]
    if error_count == 2:
        return hang_image[2]
    if error_count == 3:
        return hang_image[3]
    if error_count == 4:
        return hang_image[4]
    if error_count == 5:
        return hang_image[5]
    if error_count == 6:
        return hang_image[6]
        # print('YOU LOSE!!')
    raise ValueError()

def encode(solution):
    '''
    Takes the inpuit of player 1 and converts it into dashes.
    '''
    solution = str(solution)
    encode_solution = ""
    for char in solution:
        if char.isalpha():
            encode_solution += '*'
        else:
            encode_solution += char
    return encode_solution

def answer_test(answer, solution):
    '''
    Checks if the letter guessed by player 2 is in the solution variable.
    '''
    if answer.upper() in solution.upper():
        return True
    else:
        return False

def decode(solution, answer, display):
    '''
    Converts  the dashes into the correctly guessed letter
    '''
    
    for i, char in enumerate(solution):
        if char == answer:
            display = display[:i] + char + display[i+1:]
            # display = display_temp
        else:
            pass

    return display

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

def guess_test(answer, past_guess):
    '''
    Checks if the letter guessed is in the list of
    guessed answers and return true or false.
    '''
    if answer in past_guess:
        print("You have already guessed this letter, here is a list of your guesses: {}\n".format(past_guess) )
        return True
    else:
        return False

def rand_word(hint):
    '''
    This function returns a random word from a list of words based on the single hint the user picked
    '''
    sol = ""
    if hint == "f":
        sol = fruit_words[randint(0, len(fruit_words) - 1)]
    elif hint == 'w':
        sol = animal_words[randint(0, len(animal_words) - 1)]
    elif hint == "c":
        sol = country_words[randint(0, len(country_words) - 1)]
        pass
    return sol

def hint_conversion(hint):
    if hint == "a":
        hint = "an animal"

    if hint == "f":
        hint == "a fruit"

    if hint == "c":
        hint = "a country"

    raise ValueError()
    
    return hint